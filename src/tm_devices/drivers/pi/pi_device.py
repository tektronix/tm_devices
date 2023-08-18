# pyright: reportUnnecessaryTypeIgnoreComment=none
"""Base Programmable Interface (PI) device driver module."""
import inspect
import os
import socket
import time

from abc import ABC, abstractmethod
from contextlib import contextmanager
from functools import cached_property
from typing import final, Generator, Optional, Sequence, Tuple, Union

import pyvisa as visa

from packaging.version import Version
from pyvisa import constants as visa_constants

from tm_devices.drivers.device import Device
from tm_devices.drivers.pi._ieee488_2_commands import IEEE4882Commands
from tm_devices.helpers import (
    check_visa_connection,
    create_visa_connection,
    DeviceConfigEntry,
    get_model_series,
    get_version,
    get_visa_backend,
    print_with_timestamp,
    PYVISA_PY_BACKEND,
)
from tm_devices.helpers.constants_and_dataclasses import UNIT_TEST_TIMEOUT


# pylint: disable=too-many-instance-attributes,too-many-public-methods
class PIDevice(Device, ABC):
    """Base Programmable Interface (PI) device driver."""

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
    ) -> None:
        """Create a PI device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
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
        self._visa_backend = self._get_visa_backend()
        # Use a default timeout of 30 seconds, if running unit tests use a smaller amount.
        self._default_visa_timeout = (
            30000
            if not bool(os.environ.get("TM_DEVICES_UNIT_TESTS_RUNNING"))
            else UNIT_TEST_TIMEOUT
        )
        self._ieee_cmds = self._IEEE_COMMANDS_CLASS(self)  # type: ignore
        self.reset_visa_timeout()

    ################################################################################################
    # Abstract Properties
    ################################################################################################
    @property
    @abstractmethod
    def all_channel_names_list(self) -> Tuple[str, ...]:
        """Return a tuple containing all the channel names."""

    @cached_property
    @abstractmethod
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""

    ################################################################################################
    # Abstract Methods
    ################################################################################################
    @abstractmethod
    def expect_esr(self, esr: Union[int, str], error_string: str = "") -> Tuple[bool, str]:
        r"""Check for the expected number of errors and output string.

        Args:
            esr: Expected ``*ESR?`` value
            error_string: Expected error buffer string.
                Multiple errors should be separated by a \n character

        Returns:
            Boolean indicating if the check passed or failed and a string with the results.
        """

    @abstractmethod
    def get_eventlog_status(self) -> Tuple[bool, str]:
        """Help function for getting the eventlog status.

        Returns:
            Boolean indicating no error, String containing concatenated contents of event log.
        """

    def turn_channel_off(self, channel_str: str) -> None:
        """Turn off the specified channel.

        Args:
            channel_str: The name of the channel to turn off.

        Raises:
            NotImplementedError: Indicates the current driver has not implemented this method.
        """
        # TODO: implement for all driver subclasses then remove this blanket NotImplementedError
        raise NotImplementedError(
            f"``.{inspect.currentframe().f_code.co_name}()``"  # pyright: ignore
            f" is not yet implemented for the {self.__class__.__name__} driver"
        )

    def turn_channel_on(self, channel_str: str) -> None:
        """Turn on the specified channel.

        Args:
            channel_str: The name of the channel to turn on.

        Raises:
            NotImplementedError: Indicates the current driver has not implemented this method.
        """
        # TODO: implement for all driver subclasses then remove this blanket NotImplementedError
        raise NotImplementedError(
            f"``.{inspect.currentframe().f_code.co_name}()``"  # pyright: ignore
            f" is not yet implemented for the {self.__class__.__name__} driver"
        )

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
    def visa_backend(self) -> str:
        """Return the VISA backend in use."""
        return self._visa_backend

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
        if self._verbose:
            print(f"{self._name_and_alias} VISA timeout set to: {timeout_ms}ms")

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
        if "-" in sw_version:
            split_sw = sw_version.split("-")
            retval = get_version(split_sw[0])
        elif " " in sw_version.lstrip():
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

    ################################################################################################
    # Context Manager Methods
    ################################################################################################
    @contextmanager
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
    def check_visa_connection(self, verbose: bool = True) -> bool:
        """Check if a VISA connection can be made to the device.

        Wrapper function for :py:func:`~tm_devices.helpers.check_visa_connection`.

        Args:
            verbose: Set this to False in order to disable printouts.
        """
        return check_visa_connection(
            self._config_entry,
            self._visa_library_path,
            self._name_and_alias,
            verbose=verbose and self._verbose,
        )

    def device_clear(self) -> None:  # pragma: no cover
        """Clear the input and output buffers of the VISA device."""
        self._visa_resource.clear()

    def disable_srq_events(self) -> None:  # pragma: no cover
        """Disable the service request event for the device."""
        self._visa_resource.disable_event(
            visa_constants.VI_EVENT_SERVICE_REQ, visa_constants.VI_QUEUE  # type: ignore
        )

    def enable_srq_events(self) -> None:  # pragma: no cover
        """Enable the service request event for the device."""
        self._visa_resource.enable_event(
            visa_constants.VI_EVENT_SERVICE_REQ, visa_constants.VI_QUEUE  # type: ignore
        )

    def get_visa_stb(self) -> int:  # pragma: no cover
        """Return the VISA status byte."""
        return self._visa_resource.read_stb()

    def query(
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
        if self._verbose and verbose:
            print_with_timestamp(f"({self._name_and_alias}) Query >>  {query!r}")

        try:
            response = self._visa_resource.query(query).strip()
            if remove_quotes:
                response = response.replace('"', "")
        except (visa.VisaIOError, socket.error) as error:
            pi_cmd_repr = f" for {query!r} " if self._verbose and verbose else " "
            msg = f"The query{pi_cmd_repr}failed with the following message: {error!r}"
            raise visa.Error(msg) from error

        if self._verbose and verbose:
            print_with_timestamp(f"Response from {query!r} >>  {response!r}")

        if not allow_empty and not response:
            pi_cmd_repr = (
                f" for the following query: {query!r} " if self._verbose and verbose else ""
            )
            msg = f"An empty string was returned{pi_cmd_repr}"
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
        if self._verbose and verbose:
            print_with_timestamp(f"({self._name_and_alias}) Query Binary Values >>  {query!r}")

        try:
            response = self._visa_resource.query_binary_values(query)  # pyright: ignore
        except (visa.VisaIOError, socket.error) as error:
            pi_cmd_repr = f" for {query!r} " if self._verbose and verbose else " "
            msg = f"The query{pi_cmd_repr}failed with the following message: {error!r}"
            raise visa.Error(msg) from error

        if self._verbose and verbose:
            print_with_timestamp(
                f"Response from {query!r} >>  {', '.join([str(x) for x in response])!r}"
            )

        if not response:
            pi_cmd_repr = (
                f" for the following query: {query!r} " if self._verbose and verbose else ""
            )
            msg = f"An empty string was returned{pi_cmd_repr}"
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
                (not abs(actual_value) <= (abs(value) + tolerance))
                and (str(value) != str(actual_value))
            )
        ) or (not allow_equal and not abs(actual_value) < (abs(value) + tolerance)):
            max_value = value + tolerance
            self.raise_failure(
                f"query_less_than failed for query: {query}\n  "
                f"max ({'inclusive' if allow_equal else 'exclusive'}): "
                f"{max_value}\n  act: {actual_value}"
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
        if self._verbose and verbose:
            print_with_timestamp(f"({self._name_and_alias}) Query Raw Binary >>  {query!r}")

        try:
            self._visa_resource.write(query)
            response = self.read_raw()
        except (visa.VisaIOError, socket.error) as error:
            pi_cmd_repr = f" for {query!r} " if self._verbose and verbose else " "
            msg = f"The query{pi_cmd_repr}failed with the following message: {error!r}"
            raise visa.Error(msg) from error

        if self._verbose and verbose:
            print_with_timestamp(f"Response from {query!r} >>  {response!r}")

        if not response.strip():
            pi_cmd_repr = (
                f" for the following query: {query!r} " if self._verbose and verbose else ""
            )
            msg = f"An empty string was returned{pi_cmd_repr}"
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
    ) -> Tuple[bool, str]:
        """Query the and verify the result.

        Args:
            query: The query that is being checked.
            value: The expected value of the query.
            tolerance: The acceptable difference between two floating point values.
            percentage: A boolean indicating what kind of tolerance check to perform.
                 False means absolute tolerance: +/- tolerance.
                 True means percent tolerance: +/- (tolerance / 100) * value.
            remove_quotes: Set this to True to remove all double quotes from the returned value.
            custom_message_prefix: A custom message to be prepended to the failure message.

        Returns:
            Tuple containing the boolean verification result and the value returned from the query.
        """
        actual_value = self.query(query, remove_quotes=remove_quotes)
        message_prefix = f"query_response failed for query: {query}"
        if custom_message_prefix:
            message_prefix = f"{custom_message_prefix}\n{message_prefix}"
        query_passed = self.verify_values(
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
        """Query the and verify the result is not the given value.

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
        query_passed = self.verify_values(
            value,
            actual_value,
            custom_message_prefix=message_prefix,
            expect_fail=True,
        )
        return query_passed, actual_value

    def read(self) -> str:
        """Return the read results from the VISA resource."""
        return self._visa_resource.read()

    def read_raw(self) -> bytes:
        """Return the read_raw results from the VISA resource."""
        return self._visa_resource.read_raw()

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

        Returns:
            The output of the query portion of the method.
        """
        self.write(f"{command} {value}")
        if self._enable_verification:
            check = self.query(command + "?", remove_quotes=remove_quotes)
            message_prefix = f"Failed to set {command} to {value}"
            if custom_message_prefix:
                message_prefix = f"{custom_message_prefix}\n{message_prefix}"
            self.verify_values(
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

    @final
    def turn_all_channels_off(self) -> None:
        """Turn all channels off."""
        for ch_str in self.all_channel_names_list:
            self.turn_channel_off(ch_str)

    @final
    def turn_all_channels_on(self) -> None:
        """Turn all channels on."""
        for ch_str in self.all_channel_names_list:
            self.turn_channel_on(ch_str)

    def wait_for_srq_event(self, timeout: int) -> visa.resources.resource.WaitResponse:
        """Wait for the service request event to happen, up to the given timeout.

        Args:
            timeout: Time to wait (in seconds).

        Returns:
            The WaitResponse for the SRQ event.
        """
        # The timeout value is multiplied by 1000 because the function expects milliseconds.
        return self._visa_resource.wait_on_event(
            visa_constants.VI_EVENT_SERVICE_REQ,  # type: ignore
            timeout * 1000,
        )

    def wait_for_visa_connection(
        self,
        wait_time: float,
        sleep_seconds: int = 5,
        accept_immediate_connection: bool = False,
        verbose: bool = True,
    ) -> bool:
        """Wait for a VISA connection to be made to the device.

        Args:
            wait_time: The maximum time to wait in seconds.
            sleep_seconds: The number of seconds to sleep in between connection attempts.
            accept_immediate_connection: A boolean indicating if a connection on the
                                         first attempt is a valid connection.
            verbose: Set this to False in order to disable printouts.

        Returns:
            A boolean indicating if a VISA connection was made within the given time limit.

        Raises:
            AssertionError: Indicating that the device erroneously connected on the first try.
        """
        attempt_num = 0
        visa_connection = False
        if verbose:
            print_with_timestamp(
                f"Attempting to establish a VISA connection with {self._resource_expression}"
            )
        start_time = time.perf_counter()
        while (time.perf_counter() - start_time) <= wait_time:
            if visa_connection := self.check_visa_connection(verbose=False):
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

        if verbose:
            if visa_connection:
                print_with_timestamp(
                    f"Successfully established a VISA connection with {self._resource_expression} "
                    f"after {total_time:.2f} seconds"
                )
            else:
                print_with_timestamp(
                    f"Unable to establish a VISA connection with {self._resource_expression} "
                    f"after {total_time:.2f} seconds"
                )

        return visa_connection

    def write(self, command: str, opc: bool = False, verbose: bool = True) -> None:
        r"""Write a command to the device.

        Args:
            command: The command to write to the device
            opc: Boolean indicating if ``*OPC?`` should be queried after sending the command.
            verbose: Set this to False in order to disable printouts.

        Raises:
            Error: An error occurred while sending the command.
            SystemError: ``*OPC?`` did not return "1" after sending the command.
        """
        if self._verbose and verbose:
            print_with_timestamp(f"({self._name_and_alias}) Write >>  {command!r}")

        try:
            self._visa_resource.write(command)
        except (visa.VisaIOError, socket.error) as error:
            pi_cmd_repr = f" for {command!r} " if self._verbose and verbose else " "
            msg = f"The write{pi_cmd_repr}failed with the following message: {error!r}"
            raise visa.Error(msg) from error

        if opc and (result := self.ieee_cmds.opc()) != "1":
            pi_cmd_repr = f" {command!r}" if self._verbose and verbose else " the command"
            msg = f"After issuing{pi_cmd_repr}, OPC returned incorrect data: {result!r}"
            raise SystemError(msg)

    def write_raw(self, command: bytes, verbose: bool = True) -> None:
        r"""Write a raw command to the device.

        Args:
            command: The command to write to the device
            verbose: Set this to False in order to disable printouts.

        Raises:
            Error: An error occurred while sending the command.
        """
        if self._verbose and verbose:
            print_with_timestamp(f"({self._name_and_alias}) Write Raw >>  {command!r}")

        try:
            self._visa_resource.write_raw(command)
        except (visa.VisaIOError, socket.error) as error:
            pi_cmd_repr = f" for {command!r} " if self._verbose and verbose else " "
            msg = f"The raw write{pi_cmd_repr}failed with the following message: {error!r}"
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
            else UNIT_TEST_TIMEOUT
        )
        self.ieee_cmds.cls()
        self.reset()
        self.reset_visa_timeout()
        self.expect_esr(0)

    def _close(self) -> None:
        """Close this device and all its used resources and components."""
        self._visa_resource.close()
        self._visa_resource = None  # type: ignore
        self._is_open = False

    def _get_visa_backend(self) -> str:
        """Determine what the VISA backend is for this device.

        Returns:
            A string containing the VISA backend.
        """
        return get_visa_backend(self._visa_resource.visalib.library_path.path)

    def _has_errors(self) -> bool:
        """Check if the device has any errors.

        Returns:
            A boolean indicating if any errors were found in the device.
        """
        return not self.expect_esr(0)[0]

    def _open(self) -> bool:
        """Open necessary resources and components and return a boolean indicating success."""
        opened = True
        if self._visa_resource is None:  # type: ignore
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

        self._is_open = opened
        return opened
