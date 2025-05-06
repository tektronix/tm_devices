"""Base Programmable Interface (PI) control class module."""

import contextlib
import logging
import os
import socket
import time
import warnings

from abc import ABC
from pathlib import Path
from typing import final, Generator, List, Optional, Sequence, Tuple, Union

import pyvisa as visa

from packaging.version import Version
from pyvisa import constants as visa_constants
from pyvisa import VisaIOError

from tm_devices.driver_mixins.device_control._abstract_device_visa_write_query_control import (
    _AbstractDeviceVISAWriteQueryControl,  # pyright: ignore[reportPrivateUsage]
)
from tm_devices.driver_mixins.shared_implementations._extension_mixin import (
    _ExtendableMixin,  # pyright: ignore[reportPrivateUsage]
)
from tm_devices.driver_mixins.shared_implementations.ieee488_2_commands import IEEE4882Commands
from tm_devices.helpers import (
    check_visa_connection,
    create_visa_connection,
    DeviceConfigEntry,
    get_model_series,
    get_version,
    get_visa_backend,
    PYVISA_PY_BACKEND,
    raise_failure,
    verify_values,
)
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813
from tm_devices.helpers.constants_and_dataclasses import PACKAGE_NAME

_logger: logging.Logger = logging.getLogger(__name__)


class PIControl(_AbstractDeviceVISAWriteQueryControl, _ExtendableMixin, ABC):  # pylint: disable=too-many-public-methods
    """Base Programmable Interface (PI) control class.

    !!! important
        Any class that inherits this control mixin must also inherit a descendant of the
        [`Device`][tm_devices.drivers.device.Device] class in order to have access to the
        attributes required by this class.
    """

    # This is a class constant that can be overwritten by children which defines
    # the class to use for the IEEE 488.2 commands.
    _IEEE_COMMANDS_CLASS = IEEE4882Commands

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
        default_visa_timeout: int,
    ) -> None:
        """Create a PI device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed. If True,
                communication printouts will be logged with a level of INFO. If False,
                communication printouts will be logged with a level of DEBUG.
            visa_resource: The VISA resource object.
            default_visa_timeout: The default VISA timeout value in milliseconds.
        """
        super().__init__(config_entry, verbose)
        self._visa_resource: visa.resources.MessageBasedResource = visa_resource
        self._resource_expression = str(self._visa_resource.resource_info.resource_name)
        self._visa_library_path = self._visa_resource.visalib.library_path.path
        if self._visa_library_path == "py":  # pragma: no cover
            # For reboots to work, visa.ResourceManager needs "@py" passed in, not "py"
            self._visa_library_path = PYVISA_PY_BACKEND
        elif self._visa_library_path.endswith(".yaml"):  # pragma: no cover
            # Mark this as a simulated VISA backend
            self._visa_library_path += "@sim"
        # Use a default timeout of 30 seconds, if running unit tests use a smaller amount.
        self._default_visa_timeout = default_visa_timeout
        self._ieee_cmds = self._IEEE_COMMANDS_CLASS(self)
        self.reset_visa_timeout()

    ################################################################################################
    # Abstract Properties
    ################################################################################################

    ################################################################################################
    # Abstract Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################
    @property
    def default_visa_timeout(self) -> int:
        """Return the default VISA timeout value in milliseconds."""
        return self._default_visa_timeout

    @property
    def ieee_cmds(self) -> IEEE4882Commands:
        """Return an internal class containing methods for the standard IEEE 488.2 command set."""
        return self._ieee_cmds

    @property
    def resource_expression(self) -> str:
        """Return the VISA resource expression."""
        return self._resource_expression

    @property
    def visa_timeout(self) -> float:
        """Return the current VISA timeout of the device in milliseconds."""
        return self._visa_resource.timeout

    @visa_timeout.setter
    def visa_timeout(self, timeout_ms: float) -> None:
        """Set the VISA timeout of the device in milliseconds.

        Args:
            timeout_ms: The new VISA timeout, in milliseconds.
        """
        self._visa_resource.timeout = timeout_ms
        _logger.debug("%s VISA timeout set to: %.3fms", self.name_and_alias, timeout_ms)

    @property
    def visa_resource(self) -> visa.resources.MessageBasedResource:
        """Return the VISA resource object.

        This gives access to all the attributes and methods that PyVISA provides.
        """
        return self._visa_resource

    ################################################################################################
    # Cached Properties
    ################################################################################################
    @cached_property
    def sw_version(self) -> Version:
        """Return the software version of the device."""
        id_string_parts = self.idn_string.split(",")
        sw_version = id_string_parts[-1]
        if ":" in id_string_parts[-1]:
            sw_version = id_string_parts[-1].rsplit(":", 1)[-1]
        if " " in sw_version.lstrip():
            split_sw = sw_version.split(" ")
            retval = get_version(split_sw[0])
        else:
            retval = get_version(sw_version)
        return retval

    @cached_property
    def idn_string(self) -> str:
        r"""Return the string returned from the ``*IDN?`` query when the device was created."""
        return self.ieee_cmds.idn()

    @cached_property
    def manufacturer(self) -> str:
        """Return the manufacturer of the device."""
        return self.idn_string.split(",")[0].strip()

    @cached_property
    def model(self) -> str:
        """Return the full model of the device."""
        return self.idn_string.split(",")[1].strip()

    @cached_property
    def serial(self) -> str:
        """Return the serial number of the device."""
        return self.idn_string.split(",")[2].strip()

    @cached_property
    def series(self) -> str:
        """Return the series of the device.

        Returns:
            The series of the device, e.g. MSO5, TSOVu, TEKSCOPE, AFG3K, AWG5200
        """
        return get_model_series(self.model)

    @cached_property
    def visa_backend(self) -> str:
        """Return the VISA backend in use."""
        return get_visa_backend(self._visa_resource.visalib.library_path.path)

    ################################################################################################
    # Context Manager Methods
    ################################################################################################
    @contextlib.contextmanager
    def temporary_visa_timeout(self, temporary_timeout_ms: float) -> Generator[None, None, None]:
        """Set a temporary VISA timeout value for the duration of the context.

        This will reset the VISA timeout to the previous value when the context exits.

        Args:
            temporary_timeout_ms: The temporary VISA timeout value, in milliseconds.
        """
        old_timeout = self.visa_timeout
        self.visa_timeout = temporary_timeout_ms
        try:
            yield
        finally:
            self.visa_timeout = old_timeout

    ################################################################################################
    # Public Methods
    ################################################################################################
    @final
    def check_visa_connection(self) -> bool:
        """Check if a VISA connection can be made to the device.

        Wrapper function for [`check_visa_connection`][tm_devices.helpers.check_visa_connection].
        """
        return check_visa_connection(
            self._config_entry,
            self._visa_library_path,
            self.name_and_alias,
        )

    def device_clear(self) -> None:  # pragma: no cover
        """Clear the input and output buffers of the VISA device."""
        self._visa_resource.clear()

    def disable_srq_events(self) -> None:  # pragma: no cover
        """Disable the service request event for the device."""
        self._visa_resource.disable_event(
            visa_constants.VI_EVENT_SERVICE_REQ,  # pyright: ignore[reportArgumentType]
            visa_constants.VI_QUEUE,  # pyright: ignore[reportArgumentType]
        )

    def enable_srq_events(self) -> None:  # pragma: no cover
        """Enable the service request event for the device."""
        self._visa_resource.enable_event(
            visa_constants.VI_EVENT_SERVICE_REQ,  # pyright: ignore[reportArgumentType]
            visa_constants.VI_QUEUE,  # pyright: ignore[reportArgumentType]
        )

    def get_visa_stb(self) -> int:  # pragma: no cover
        """Return the VISA status byte."""
        return self._visa_resource.read_stb()

    def poll_query(  # noqa: PLR0913  # pylint: disable=too-many-locals
        self,
        number_of_polls: int,
        query: str,
        wanted_val: Union[float, str],
        sleep_time: float = 0.4,
        tolerance: float = 0,
        percentage: bool = False,
        invert_range: bool = False,
        invalid_values: Union[List[Union[float, str]], None] = None,
    ) -> None:
        """Poll the query until the wanted value appears.

        Args:
            number_of_polls: The number of times to poll the query.
            query: The query to poll.
            wanted_val: The desired value to poll for.
            sleep_time: The time to wait between polls (in seconds).
            tolerance: The acceptable difference between two floating point values.
            percentage: A boolean indicating what kind of tolerance check to perform.
                 False means absolute tolerance: +/- tolerance.
                 True means percent tolerance: +/- (tolerance / 100) * value.
            invert_range: A boolean indicating when to stop polling.
                 False means polling until the wanted value appears.
                 True means polling until a different value from the wanted value appears.
            invalid_values: A list of values that should never be received when polling.

        Raises:
            AssertionError: Indicating that the device never reached the wanted value.
        """
        if invalid_values is None:
            invalid_values = []
        poll_number: int = 0
        query_list = ""
        if isinstance(wanted_val, float):
            tolerance = abs(tolerance * 0.01 * wanted_val if percentage else tolerance)
        while poll_number < number_of_polls:
            queried_value = self.query(query)
            query_list += f"\t{poll_number} - {queried_value}\n"
            if invalid_values:
                self.ieee_cmds.cls()
                error_check = (
                    float(queried_value) not in invalid_values
                    if isinstance(wanted_val, (float, int))
                    else queried_value not in invalid_values
                )
            else:
                error_check = True
            if error_check:
                float_comparison = (
                    isinstance(wanted_val, (float, int))
                    and wanted_val - tolerance
                    <= float(queried_value)
                    <= float(wanted_val) + tolerance
                )
                str_comparison = isinstance(wanted_val, str) and queried_value == wanted_val
                if (not invert_range and (float_comparison or str_comparison)) or (
                    invert_range and not (float_comparison or str_comparison)
                ):
                    return
            time.sleep(sleep_time)
            poll_number += 1
        msg = (
            f"{query} {'never' if not invert_range else 'always'} "
            f"returned {wanted_val}, received:\n{query_list}"
        )
        raise AssertionError(msg)

    def query(  # pylint: disable=arguments-differ
        self,
        query: str,
        *,
        verbose: bool = True,
        remove_quotes: bool = False,
        allow_empty: bool = False,
    ) -> str:
        """Send a query to the device and return the result.

        Args:
            query: The query to send to the device.
            verbose: Set this to False in order to disable printouts.
            remove_quotes: Set this to True to remove all double quotes from the returned value.
            allow_empty: Set this to True if an empty return string is permitted.

        Returns:
            The results of the query.

        Raises:
            Error: An error occurred while sending the command.
            SystemError: An empty string was returned from the device.
        """
        _logger.log(
            logging.INFO if self._verbose and verbose else logging.DEBUG,
            "(%s) Query >>  %r",
            self.name_and_alias,
            query,
        )
        self._command_logger.debug(query)
        try:
            response = self._visa_resource.query(query).strip()
            if remove_quotes:
                response = response.replace('"', "")
        except (visa.VisaIOError, socket.error) as error:
            pi_cmd_repr = f" for {query!r} " if verbose else " "
            msg = (
                f"The query of {self.name_and_alias}{pi_cmd_repr}"
                f"failed with the following message: {error!r}"
            )
            _logger.error(msg)  # noqa: TRY400
            raise visa.Error(msg) from error

        _logger.log(
            logging.INFO if self._verbose and verbose else logging.DEBUG,
            "Response from %r >>  %r",
            query,
            response,
        )

        if not allow_empty and not response:
            pi_cmd_repr = f" for the following query: {query!r}" if verbose else ""
            msg = f"An empty string was returned from {self.name_and_alias}{pi_cmd_repr}"
            _logger.error(msg)
            raise SystemError(msg)

        return response

    def query_binary(self, query: str, verbose: bool = True) -> Sequence[float]:
        """Send a query to the device and return the binary values.

        Args:
            query: The query to send to the device.
            verbose: Set this to False in order to disable printouts.

        Returns:
            The results of the query.

        Raises:
            Error: An error occurred while sending the command.
            SystemError: An empty string was returned from the device.
        """
        _logger.log(
            logging.INFO if self._verbose and verbose else logging.DEBUG,
            "(%s) Query Binary Values >>  %r",
            self.name_and_alias,
            query,
        )
        self._command_logger.debug(query)
        try:
            response = self._visa_resource.query_binary_values(query)  # pyright: ignore[reportUnknownMemberType]
        except (visa.VisaIOError, socket.error) as error:
            pi_cmd_repr = f" for {query!r} " if verbose else " "
            msg = (
                f"The binary query of {self.name_and_alias}{pi_cmd_repr}"
                f"failed with the following message: {error!r}"
            )
            _logger.error(msg)  # noqa: TRY400
            raise visa.Error(msg) from error

        _logger.log(
            logging.INFO if self._verbose and verbose else logging.DEBUG,
            "Response from %r >>  %r",
            query,
            response,
        )

        if not response:
            pi_cmd_repr = f" for the following binary query: {query!r}" if verbose else ""
            msg = f"An empty string was returned from {self.name_and_alias}{pi_cmd_repr}"
            _logger.error(msg)
            raise SystemError(msg)

        return response

    def query_expect_timeout(
        self, invalid_command: str, timeout_ms: int = 200, verbose: bool = True
    ) -> str:
        """Send a query expecting it to time out and fail.

        Args:
            invalid_command:
                The bad command to query.
            timeout_ms:
                The VISA timeout duration for this function (in milliseconds).
            verbose:
                A flag to decide if we should print out a message indicating what query was sent.

        Returns:
            The timeout error or the response to the query.

        Raises:
            visa.errors.Error: Any non-timeout error will be re-raised.
        """
        retval = ""
        with self.temporary_visa_timeout(timeout_ms):
            try:
                retval = self.query(invalid_command, verbose=verbose)
            except visa.errors.Error as error:
                error_args = error.args[0]
                # Only want to gracefully handle a timeout
                if (
                    "VisaIOError('VI_ERROR_TMO" in error_args
                    and "Timeout expired before operation completed.')" in error_args
                ):
                    # VISA function ends the current query interaction (probably buffer related)
                    self.device_clear()
                else:
                    raise
        return retval

    def query_less_than(
        self,
        query: str,
        value: Union[float, str],
        tolerance: float = 0,
        percentage: bool = False,
        allow_equal: bool = False,
    ) -> bool:
        """Send the given query and verify the result is less than the expected response.

        Args:
            query: The command that is being checked.
            value: The expected value of the query.
            tolerance: The acceptable difference between two floating point values.
            percentage: A boolean indicating what kind of tolerance check to perform.
                 False means absolute tolerance: +/- tolerance.
                 True means percent tolerance: +/- (tolerance / 100) * value.
            allow_equal: A boolean indicating if equal results should be allowed.

        Returns:
            Boolean indicating whether the check passed or failed.
        """
        query_passed = True
        actual_value = float(self.query(query).strip())
        tolerance = float(tolerance)
        value = float(value)
        if percentage:
            tolerance = abs((tolerance / 100.0) * value)
        # Verify that the number is within the tolerance.
        # Also check to make sure that the string of each number isn't
        # identical, this prevents issues from returned values that have
        # a trailing zero or some other non-contributing character that
        # will cause comparison issues.
        if (
            allow_equal
            and (
                (abs(actual_value) < (abs(value) + tolerance)) and (str(value) != str(actual_value))
            )
        ) or (not allow_equal and abs(actual_value) >= (abs(value) + tolerance)):
            max_value = value + tolerance
            raise_failure(
                self.name_and_alias,
                f"query_less_than failed for query: {query}\n  "
                f"max ({'inclusive' if allow_equal else 'exclusive'}): "
                f"{max_value}\n  act: {actual_value}",
            )

        return query_passed

    def query_raw_binary(self, query: str, verbose: bool = True) -> bytes:
        """Send a command to the device and then read and return the raw binary values.

        Args:
            query: The query to send to the device.
            verbose: Set this to False in order to disable printouts.

        Returns:
            The raw results of the query.

        Raises:
            Error: An error occurred while sending the command.
            SystemError: An empty string was returned from the device.
        """
        _logger.log(
            logging.INFO if self._verbose and verbose else logging.DEBUG,
            "(%s) Query Raw Binary >>  %r",
            self.name_and_alias,
            query,
        )
        self._command_logger.debug(query)
        try:
            self._visa_resource.write(query)
            response = self.read_raw()
        except (visa.VisaIOError, socket.error) as error:
            pi_cmd_repr = f" for {query!r} " if verbose else " "
            msg = (
                f"The raw binary query of {self.name_and_alias}{pi_cmd_repr}"
                f"failed with the following message: {error!r}"
            )
            _logger.error(msg)  # noqa: TRY400
            raise visa.Error(msg) from error

        _logger.log(
            logging.INFO if self._verbose and verbose else logging.DEBUG,
            "Response from %r >>  %r",
            query,
            response,
        )

        if not response.strip():
            pi_cmd_repr = f" for the following raw binary query: {query!r}" if verbose else ""
            msg = f"An empty string was returned from {self.name_and_alias}{pi_cmd_repr}"
            _logger.error(msg)
            raise SystemError(msg)

        return response

    def query_response(
        self,
        query: str,
        value: Union[str, float],
        tolerance: float = 0,
        percentage: bool = False,
        remove_quotes: bool = False,
        custom_message_prefix: str = "",
        allow_empty: bool = False,
    ) -> Tuple[bool, str]:
        """Query the device and verify the result.

        Args:
            query: The query that is being checked.
            value: The expected value of the query.
            tolerance: The acceptable difference between two floating point values.
            percentage: A boolean indicating what kind of tolerance check to perform.
                 False means absolute tolerance: +/- tolerance.
                 True means percent tolerance: +/- (tolerance / 100) * value.
            remove_quotes: Set this to True to remove all double quotes from the returned value.
            custom_message_prefix: A custom message to be prepended to the failure message.
            allow_empty: Set this to True if an empty return string is permitted.

        Returns:
            Tuple containing the boolean verification result and the value returned from the query.
        """
        actual_value = self.query(query, remove_quotes=remove_quotes, allow_empty=allow_empty)
        message_prefix = f"query_response failed for query: {query}"
        if custom_message_prefix:
            message_prefix = f"{custom_message_prefix}\n{message_prefix}"
        query_passed = verify_values(
            self.name_and_alias,
            value,
            actual_value,
            tolerance=tolerance,
            percentage=percentage,
            custom_message_prefix=message_prefix,
        )
        return query_passed, actual_value

    def query_response_not(
        self,
        query: str,
        value: str,
        remove_quotes: bool = False,
        custom_message_prefix: str = "",
    ) -> Tuple[bool, str]:
        """Query the device and verify the result is not the given value.

        Args:
            query: The query that is being checked.
            value: The value that the query should not return.
            remove_quotes: Set this to True to remove all double quotes from the returned value.
            custom_message_prefix: A custom message to be prepended to the failure message.

        Returns:
            Tuple containing the boolean verification result and the value returned from the query.
        """
        actual_value = self.query(query, remove_quotes=remove_quotes)
        message_prefix = f"query_response_not failed for query: {query}"
        if custom_message_prefix:
            message_prefix = f"{custom_message_prefix}\n{message_prefix}"
        query_passed = verify_values(
            self.name_and_alias,
            value,
            actual_value,
            custom_message_prefix=message_prefix,
            expect_fail=True,
        )
        return query_passed, actual_value

    def read(self) -> str:
        """Return the read results from the VISA resource."""
        return self._visa_resource.read()

    def read_raw(self, size: Optional[int] = None) -> bytes:
        """Return the read_raw results from the VISA resource.

        Args:
            size: The chunk size to use to perform the reading. Defaults to None,
                meaning the resource wide set value is set.

        Returns:
            The bytes read from the device.
        """
        return self._visa_resource.read_raw(size)

    def reset_visa_timeout(self) -> None:
        """Reset the VISA timeout to the default value."""
        self.visa_timeout = self._default_visa_timeout

    def set_and_check(  # noqa: PLR0913
        self,
        command: str,
        value: Union[str, float],
        tolerance: float = 0,
        percentage: bool = False,
        remove_quotes: bool = False,
        custom_message_prefix: str = "",
        *,
        expected_value: Optional[Union[str, float]] = None,
        opc: bool = False,
    ) -> str:
        """Send the given command with the given value and then verify the results.

        Args:
            command: The command to send.
                For example: ``:AFG:FUNCTION``
            value: The value being set by the command.
                For example: ``SINE``
            tolerance: The acceptable difference between two floating point values.
            percentage: A boolean indicating what kind of tolerance check to perform.
                 False means absolute tolerance: +/- tolerance.
                 True means percent tolerance: +/- (tolerance / 100) * value.
            remove_quotes: Set this to True to remove all double quotes from the returned value.
            custom_message_prefix: A custom message to be prepended to the failure message.
            expected_value: An optional, alternative value expected to be returned.
            opc: Boolean indicating if ``*OPC?`` should be queried after sending the command.

        Returns:
            The output of the query portion of the method.
        """
        self.write(f"{command} {value}", opc=opc)
        if self._enable_verification:
            check = self.query(command + "?", remove_quotes=remove_quotes)
            message_prefix = f"Failed to set {command} to {value}"
            if custom_message_prefix:
                message_prefix = f"{custom_message_prefix}\n{message_prefix}"
            verify_values(
                self.name_and_alias,
                value if expected_value is None else expected_value,
                check,
                tolerance=tolerance,
                percentage=percentage,
                custom_message_prefix=message_prefix,
                log_error=True,
            )
        else:
            check = ""
        return check

    def set_if_needed(  # noqa: PLR0913
        self,
        command: str,
        value: Union[str, float],
        tolerance: float = 0,
        percentage: bool = False,
        remove_quotes: bool = False,
        custom_message_prefix: str = "",
        *,
        expected_value: Optional[Union[str, float]] = None,
        opc: bool = False,
        allow_empty: bool = False,
        verify_value: bool = False,
    ) -> Tuple[bool, str]:
        """Query the command's field and update it if the value does not match the input.

        Args:
            command: The command to send.
                For example: ``:AFG:FUNCTION``
            value: The value being set by the command.
                For example: ``SINE``
            tolerance: The acceptable difference between two floating point values.
            percentage: A boolean indicating what kind of tolerance check to perform.
                 False means absolute tolerance: +/- tolerance.
                 True means percent tolerance: +/- (tolerance / 100) * value.
            remove_quotes: Set this to True to remove all double quotes from the returned value.
            custom_message_prefix: A custom message to be prepended to the failure message.
            expected_value: An optional, alternative value expected to be returned.
            opc: Boolean indicating if ``*OPC?`` should be queried after sending the command.
            allow_empty: Set this to True if an empty return string is permitted.
            verify_value: Boolean indicating to verify value after write.

        Returns:
            Tuple containing the boolean value indicating if the command needed to be set and
                the value returned from the query.
        """
        try:
            query_passed, actual_value = self.query_response(
                query=command + "?",
                value=value,
                tolerance=tolerance,
                percentage=percentage,
                remove_quotes=remove_quotes,
                custom_message_prefix=custom_message_prefix,
                allow_empty=allow_empty,
            )
        except AssertionError:
            query_passed = False
            if verify_value:
                actual_value = self.set_and_check(
                    command,
                    value,
                    tolerance,
                    percentage,
                    remove_quotes,
                    custom_message_prefix,
                    expected_value=expected_value,
                    opc=opc,
                )
            else:
                self.write(f"{command} {value}", opc=bool(opc))
                actual_value = ""
        return not query_passed, actual_value

    def wait_for_srq_event(self, timeout: int) -> visa.resources.resource.WaitResponse:
        """Wait for the service request event to happen, up to the given timeout.

        Args:
            timeout: Time to wait (in seconds).

        Returns:
            The WaitResponse for the SRQ event.
        """
        # The timeout value is multiplied by 1000 because the function expects milliseconds.
        return self._visa_resource.wait_on_event(
            visa_constants.VI_EVENT_SERVICE_REQ,  # pyright: ignore[reportArgumentType]
            timeout * 1000,
        )

    def wait_for_visa_connection(
        self,
        wait_time: float,
        sleep_seconds: int = 5,
        accept_immediate_connection: bool = False,
    ) -> bool:
        """Wait for a VISA connection to be made to the device.

        Args:
            wait_time: The maximum time to wait in seconds.
            sleep_seconds: The number of seconds to sleep in between connection attempts.
            accept_immediate_connection: A boolean indicating if a connection on the
                                         first attempt is a valid connection.

        Returns:
            A boolean indicating if a VISA connection was made within the given time limit.

        Raises:
            AssertionError: Indicating that the device erroneously connected on the first try.
        """
        attempt_num = 0
        visa_connection = False
        _logger.log(
            logging.INFO if self._verbose else logging.DEBUG,
            "Attempting to establish a VISA connection with %s",
            self._resource_expression,
        )
        start_time = time.perf_counter()
        while (time.perf_counter() - start_time) <= wait_time:
            if visa_connection := self.check_visa_connection():
                # pylint: disable=compare-to-zero
                if not (attempt_num == 0 and not accept_immediate_connection):
                    break
                msg = (
                    f"A VISA connection was established with "
                    f"{self._resource_expression} on the first attempt "
                    f"when it should not have been."
                )
                raise AssertionError(msg)
            time.sleep(sleep_seconds)
            attempt_num += 1

        end_time = time.perf_counter()
        total_time = end_time - start_time

        if visa_connection:
            _logger.log(
                logging.INFO if self._verbose else logging.DEBUG,
                "Successfully established a VISA connection with %s after %.2f seconds",
                self._resource_expression,
                total_time,
            )
        else:
            _logger.warning(
                "Unable to establish a VISA connection with %s after %.2f seconds",
                self._resource_expression,
                total_time,
            )

        return visa_connection

    def write(self, command: str, opc: bool = False, verbose: bool = True) -> None:  # pylint: disable=arguments-differ
        r"""Write a command to the device.

        Args:
            command: The command to write to the device
            opc: Boolean indicating if ``*OPC?`` should be queried after sending the command.
            verbose: Set this to False in order to disable printouts.

        Raises:
            Error: An error occurred while sending the command.
            SystemError: ``*OPC?`` did not return "1" after sending the command.
        """
        if "\n" in command:
            _logger.log(
                logging.INFO if self._verbose and verbose else logging.DEBUG,
                "(%s) Write >>\n%s",
                self.name_and_alias,
                "\n".join(["    " + x for x in command.split("\n")]),
            )
        else:
            _logger.log(
                logging.INFO if self._verbose and verbose else logging.DEBUG,
                "(%s) Write >>  %r",
                self.name_and_alias,
                command,
            )
        self._command_logger.debug(command)
        try:
            self._visa_resource.write(command)
        except (visa.VisaIOError, socket.error) as error:
            pi_cmd_repr = f" for {command!r} " if verbose else " "
            msg = (
                f"The write to {self.name_and_alias}{pi_cmd_repr}"
                f"failed with the following message: {error!r}"
            )
            _logger.error(msg)  # noqa: TRY400
            raise visa.Error(msg) from error

        if opc and (result := self.ieee_cmds.opc()) != "1":
            pi_cmd_repr = f" {command!r}" if verbose else " the command"
            msg = (
                f"After issuing{pi_cmd_repr} to {self.name_and_alias}, "
                f"OPC returned incorrect data: {result!r}"
            )
            _logger.error(msg)
            raise SystemError(msg)

    def write_raw(self, command: bytes, verbose: bool = True) -> None:
        r"""Write a raw command to the device.

        Args:
            command: The command to write to the device
            verbose: Set this to False in order to disable printouts.

        Raises:
            Error: An error occurred while sending the command.
        """
        _logger.log(
            logging.INFO if self._verbose and verbose else logging.DEBUG,
            "(%s) Write Raw >>  %r",
            self.name_and_alias,
            command,
        )
        self._command_logger.debug(command)
        try:
            self._visa_resource.write_raw(command)
        except (visa.VisaIOError, socket.error) as error:
            pi_cmd_repr = f" for {command!r} " if verbose else " "
            msg = (
                f"The raw write to {self.name_and_alias}"
                f"{pi_cmd_repr}failed with the following message: {error!r}"
            )
            _logger.error(msg)  # noqa: TRY400
            raise visa.Error(msg) from error

    ################################################################################################
    # Public Methods (PI Library)
    ################################################################################################
    def factory_reset(self) -> None:
        r"""Send the ``FACTORY`` command followed by an ``*OPC?`` query.

        This command is equivalent to pressing the DEFAULT SETUP button located on
        the instrument front panel or selected Default Setup from the File menu.

        It recalls the instrument to factory default settings.

        In addition to what ``*RST`` does, this command also performs the following operations:

        - Clears any pending OPC operations
        - Resets the following IEEE488.2 registers:
        - ``*ESR`` 0 (Event Status Enable Register)
        - ``*SRE`` 0 (Service Request Enable Register)
        - DESE 255 (Device Event Status Enable Register)
        - ``*PSC`` 1 (Power-on Status Clear Flag)
        - Deletes all defined aliases.
        - Enables command headers (:HEADer 1).

        ``FACTORY`` only resets the programmable interface settings, it does not change the
        user interface settings.
        """
        self.write("FACTORY", opc=True)

    def reset(self) -> None:
        r"""Send the ``*RST`` command followed by an ``*OPC?`` query.

        ``*RST`` only resets the programmable interface settings, it does not change the user
        interface settings.
        """
        self.ieee_cmds.rst()
        self.ieee_cmds.opc()

    ################################################################################################
    # Private Methods
    ################################################################################################
    def _cleanup(self) -> None:
        """Perform the cleanup defined for the device."""
        self.visa_timeout = (
            120000
            if not bool(os.environ.get("TM_DEVICES_UNIT_TESTS_RUNNING"))
            else self.default_visa_timeout
        )
        self.ieee_cmds.cls()
        self.reset()
        self.reset_visa_timeout()
        self.expect_esr(0)

    def _close(self) -> None:
        """Close this device and all its used resources and components."""
        try:
            self._visa_resource.close()
        except VisaIOError as error:
            error_msg = f"Error encountered while closing the visa resource:\n{error}"
            warnings.warn(error_msg, stacklevel=2)
            _logger.exception(error_msg)
        self._visa_resource = None  # pyright: ignore[reportAttributeAccessIssue]
        self._is_open = False

    @cached_property
    def _command_logger(self) -> logging.Logger:
        """Create a logger that will be used to log commands sent via write/query-like methods."""
        # Create the logger
        command_logger = logging.getLogger(f"{self._config_entry.address}-visa_logger")
        command_logger.setLevel(logging.DEBUG)
        command_logger.propagate = False
        command_logger.addHandler(logging.NullHandler())
        with contextlib.suppress(IndexError, StopIteration):
            # Get the top-level log filepath
            main_log_file = Path(
                next(
                    x
                    for x in logging.getLogger(PACKAGE_NAME).handlers
                    if isinstance(x, logging.FileHandler)
                ).baseFilename
            )
            # Create the handler with the filename based on the main log file
            command_log_handler = logging.FileHandler(
                main_log_file.as_posix().replace(
                    main_log_file.suffix, f"_visa_commands_{self._config_entry.address}.log"
                ),
                mode="w",
                encoding="utf-8",
            )
            # Create the formatter
            command_log_formatter = logging.Formatter("%(message)s")
            command_log_handler.setFormatter(command_log_formatter)
            command_log_handler.setLevel(logging.DEBUG)
            command_logger.addHandler(command_log_handler)
        return command_logger

    def _open(self) -> bool:
        """Open necessary resources and components and return a boolean indicating success."""
        opened = True
        if self._visa_resource is None:  # pyright: ignore[reportUnnecessaryComparison]
            opened = False
            # 5 seconds when running unit tests, else 600 seconds (10 minutes)
            num_seconds_to_attempt_reconnection = (
                5 if bool(os.environ.get("TM_DEVICES_UNIT_TESTS_RUNNING")) else 600
            )
            sleep_time_seconds = 5
            # Attempt to reconnect with the device many times.
            for iteration in range(num_seconds_to_attempt_reconnection // sleep_time_seconds):
                try:
                    time.sleep(sleep_time_seconds)
                    # Create new VISA connection
                    self._visa_resource = create_visa_connection(
                        self._config_entry,
                        visa_library=self._visa_library_path,
                        verbose_connection_failure_logging=False,
                    )
                    opened = True
                    if iteration < 1 and not bool(
                        os.environ.get("TM_DEVICES_UNIT_TESTS_REBOOT_ALLOW")
                    ):
                        # It shouldn't be able to reconnect on the first try.
                        # If it does, it most certainly did not reboot.
                        opened = False
                    break
                except ConnectionError:
                    # raised by the create_visa_connection() function
                    pass

        if self._visa_resource is not None:  # pyright: ignore[reportUnnecessaryComparison]
            self.reset_visa_timeout()
        self._is_open = opened
        return opened
