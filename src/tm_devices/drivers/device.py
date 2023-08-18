"""Base device driver module."""
import socket
import time

from abc import ABC, abstractmethod
from contextlib import contextmanager
from functools import cached_property
from typing import (
    Any,
    final,
    Generator,
    Optional,
    Tuple,
    TypeVar,
    Union,
)

from packaging.version import Version

from tm_devices.driver_mixins.class_extension_mixin import ExtendableMixin
from tm_devices.helpers import (
    check_network_connection,
    check_port_connection,
    ConnectionTypes,
    DeviceConfigEntry,
    get_timestamp_string,
    print_with_timestamp,
)

_T = TypeVar("_T")
_FAMILY_BASE_CLASS_PROPERTY_NAME = "_product_family_base_class"


def family_base_class(cls: _T) -> _T:
    """A decorator indicating a class is the top level of a unique product family tree.

    Notes:
        All subclassed children will point to the decorated class.
    """
    setattr(cls, _FAMILY_BASE_CLASS_PROPERTY_NAME, cls)
    return cls


# pylint: disable=too-many-instance-attributes,too-many-public-methods
class Device(ExtendableMixin, ABC):
    """Base device driver that all devices inherit from."""

    _DEVICE_TYPE: str  # should be implemented by device type base classes

    ################################################################################################
    # Categories:
    # - Magic Methods
    # - Abstract Cached Properties
    # - Abstract Methods - Private and Public
    # - Properties - Private and Public
    # - Cached Properties
    # - Context Manager Methods
    # - Public Methods
    # - Private Methods
    ################################################################################################

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(self, config_entry: DeviceConfigEntry, verbose: bool) -> None:
        """Create a device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
        """
        self._is_open = True
        self._verbose = verbose
        self._config_entry = config_entry
        self._device_number: int = -1  # set after creation by DeviceManager
        self._enable_verification = True
        self._reboot_quiet_period = 0
        self._series = self.__class__.__name__

        # These are private attributes to be overwritten by generated drivers
        self._commands: Any = NotImplemented
        self._command_argument_constants: Any = NotImplemented
        self._command_verification_enabled = False
        self._command_syntax_enabled = False

    def __str__(self) -> str:
        """Return a string representation of the class."""
        line_break_length = 90
        retval = f"{'=' * (line_break_length // 2)} {self.name} {'=' * (line_break_length // 2)}\n"
        retval += f"  {self.__class__} object at {id(self)}"

        for prop in [
            p
            for p in dir(self.__class__)
            if isinstance(getattr(self.__class__, p), (cached_property, property))
            and not p.startswith("_")
        ]:
            retval += f"\n    {prop}={self.__getattribute__(prop)!r}"

        retval += f"\n{'=' * (line_break_length + 2 + len(self.name))}"
        return retval

    ################################################################################################
    # Abstract Cached Properties
    ################################################################################################
    @cached_property
    @abstractmethod
    def manufacturer(self) -> str:
        """Return the manufacturer of the device."""

    @cached_property
    @abstractmethod
    def model(self) -> str:
        """Return the full model of the device."""

    @cached_property
    @abstractmethod
    def serial(self) -> str:
        """Return the serial number of the device."""

    @cached_property
    @abstractmethod
    def sw_version(self) -> Version:
        """Return the software version of the device."""

    ################################################################################################
    # Abstract Methods - Private and Public
    ################################################################################################
    @abstractmethod
    def _cleanup(self) -> None:
        """Perform the actual cleanup code."""

    @abstractmethod
    def _close(self) -> None:
        """Perform the actual closing code."""

    @abstractmethod
    def _has_errors(self) -> bool:
        """Check if the device has any errors.

        Returns:
            A boolean indicating if any errors were found in the device.
        """

    @abstractmethod
    def _open(self) -> bool:
        """Perform the actual opening code.

        Returns:
           A boolean indicating if device connected successfully.
        """

    @abstractmethod
    def _reboot(self) -> None:
        """Perform the actual rebooting code."""
        raise NotImplementedError(
            f"``._reboot()`` is not yet implemented for the {self.__class__.__name__} driver"
        )

    ################################################################################################
    # Properties - Private and Public
    ################################################################################################
    @property
    def _name_and_alias(self) -> str:
        """Return string for easy ID of device in console output prints."""
        retval = self.name
        if self.alias:
            retval += f' "{self.alias}"'
        return retval.replace(" NotImplemented", "")

    @property
    def address(self) -> str:
        """Return the device address as defined in the config_entry.

        This could be an IP address, hostname, or USB device address.
        """
        return self._config_entry.address

    @property
    def alias(self) -> str:
        """Return the alias if it exists, otherwise an empty string."""
        return self._config_entry.alias if self._config_entry.alias is not None else ""

    @property
    def command_argument_constants(self) -> Any:
        """Return the device command argument constants."""
        return self._command_argument_constants

    @property
    def command_syntax_enabled(self) -> bool:
        """Return a string containing the syntax of the command being accessed.

        This property indicates when the syntax should be returned instead of writing/querying the
        device and returning the result.
        """
        return self._command_syntax_enabled

    @property
    def command_verification_enabled(self) -> bool:
        """Return a boolean indicating if command verification is enabled.

        This property only applies to commands sent using the ``.commands`` property of the
        device.

        Notes:
            - If ``.enable_verification`` is set to ``False``, then no verification will happen at
              all.
            - If ``.enable_verification`` is set to ``True`` and this property is ``True``, then
              verification **will** happen for commands sent using the ``.commands`` property of the
              device.
            - If ``.enable_verification`` is set to ``True`` and this property is ``False``, then
              verification **will not** happen for commands sent using the ``.commands`` property of
              the device.
        """
        return self._command_verification_enabled

    @property
    def commands(self) -> Any:
        """Return the device commands."""
        return self._commands

    @property
    def config_entry(self) -> DeviceConfigEntry:
        """Return the device config."""
        return self._config_entry

    @property
    def connection_type(self) -> str:
        """Return a string indicating the connection type."""
        return self._config_entry.connection_type.value

    @property
    def device_number(self) -> int:
        """Return the device number, if Device not created through DeviceManager will be -1."""
        return self._device_number

    @property
    def device_type(self) -> str:
        """Return a string representing the device type."""
        return self._DEVICE_TYPE

    @property
    def enable_verification(self) -> bool:
        """Return the boolean which indicates if verification checks should happen.

        This can be disabled after developing a script in order to increase the speed of the script.
        """
        return self._enable_verification

    @enable_verification.setter
    def enable_verification(self, value: bool) -> None:
        """Set the ``self.enable_verification`` attribute."""
        self._enable_verification = value

    @property
    def is_open(self) -> bool:
        """Return a boolean indicating if the connection to the device is currently open."""
        return self._is_open

    @property
    def name(self) -> str:
        """Return the device name.

        Usually something like "SCOPE 1"
        """
        return f"{self.device_type} {self.device_number}"

    @property
    def port(self) -> Optional[int]:
        """Return the device port, or None if the device doesn't have a port."""
        return self._config_entry.lan_port

    @cached_property
    def series(self) -> str:
        """Return the series of the device.

        Returns:
            The series of the device, e.g. MSO5, TSOVu, TEKSCOPE, AFG3K, AWG5200
        """
        return self.__class__.__name__

    @property
    def verbose(self) -> bool:
        """Return the verbose attribute of the device."""
        return self._verbose

    ################################################################################################
    # Cached Properties
    ################################################################################################
    @cached_property
    def hostname(self) -> str:
        """Return the hostname of the device or an empty string if unable to fetch that."""
        if self._config_entry.connection_type not in {ConnectionTypes.USB}:
            try:
                # TODO: figure out a better way to lower the timeout for the gethostbyaddr() call
                return socket.gethostbyaddr(self.address)[0]
            except (socket.gaierror, socket.herror):
                pass
        return ""

    @cached_property
    def ip_address(self) -> str:
        """Return the IPv4 address of the device or an empty string if unable to fetch that."""
        if self._config_entry.connection_type not in {ConnectionTypes.USB}:
            try:
                return socket.gethostbyname(self.address)
            except (socket.gaierror, socket.herror):
                pass
        return ""

    ################################################################################################
    # Context Manager Methods
    ################################################################################################
    @contextmanager
    def command_syntax(self) -> Generator[None, None, None]:
        """Enable command syntax for the duration of this context manager.

        This method is designed to be used as a context manager (``with device.command_syntax():``)
        around any blocks of code where the literal syntax of commands accessed using the
        ``.commands`` property is desired.

        This is accomplished by setting the ``.command_syntax_enabled`` property to ``True`` for the
        duration of the context manager.
        """
        self._command_syntax_enabled = True
        try:
            yield
        finally:
            self._command_syntax_enabled = False

    @contextmanager
    def command_verification(self) -> Generator[None, None, None]:
        """Enable command verification for the duration of this context manager.

        This method is designed to be used as a context manager (``with
        device.command_verification():``) around any blocks of code where verification of commands
        sent using the ``.commands`` property is desired.

        This is accomplished by setting the ``.command_verification_enabled`` property to ``True``
        for the duration of the context manager.
        """
        self._command_verification_enabled = True
        try:
            yield
        finally:
            self._command_verification_enabled = False

    @contextmanager
    def temporary_verbose(self, temporary_verbose: bool) -> Generator[None, None, None]:
        """Set a temporary console output verbosity for the duration of the context.

        This will reset the verbosity to the previous value when the context exits.

        Args:
            temporary_verbose: The temporary verbosity value.
        """
        old_verbose = self._verbose
        self._verbose = temporary_verbose
        try:
            yield
        finally:
            self._verbose = old_verbose

    ################################################################################################
    # Public Methods
    ################################################################################################
    @final
    def check_network_connection(self, verbose: bool = True) -> Tuple[bool, str]:
        """Check the network connection to the device using an external ping command.

        Wrapper function for :py:func:`~tm_devices.helpers.check_network_connection`.

        Args:
            verbose: Set this to False in order to disable printouts.

        Returns:
            A tuple containing a boolean indicating if there is a network connection and
            a string with the result of the ping command.
        """
        return check_network_connection(
            self._name_and_alias, self.ip_address, verbose=verbose and self._verbose
        )

    @final
    def check_port_connection(
        self, port: int, timeout_seconds: int = 5, verbose: bool = True
    ) -> bool:
        """Check if the given port is open on the device.

        Wrapper function for :py:func:`~tm_devices.helpers.check_port_connection`.

        Args:
            port: The port to check.
            timeout_seconds: The number of seconds to use as the socket timeout.
            verbose: Set this to False in order to disable printouts.

        Returns:
            A boolean indicating if the port is open.
        """
        return check_port_connection(
            self._name_and_alias,
            self.ip_address,
            port,
            timeout_seconds=timeout_seconds,
            verbose=verbose and self._verbose,
        )

    @final
    def cleanup(self, verbose: bool = True) -> None:
        """Perform the cleanup defined for the device.

        Args:
            verbose: Set this to False in order to disable printouts.
        """
        with self.temporary_verbose(verbose):
            print(f"Beginning Device Cleanup on {self._name_and_alias}")
            self._cleanup()
            print(f"Finished Device Cleanup on {self._name_and_alias}")

    @final
    def close(self) -> None:
        """Close this device and all its used resources and components."""
        print_with_timestamp(f"Closing Connection to {self._name_and_alias}")
        self._close()

    @final
    def has_errors(self) -> bool:
        """Check if the device has any errors.

        Returns:
            A boolean indicating if any errors were found in the device.
        """
        return self._has_errors()

    @final
    def raise_error(self, message: str) -> None:
        """Raise an AssertionError with the provided message indicating there was an error.

        Args:
            message: The message to add to the AssertionError.

        Raises:
            AssertionError: Prints out the error message with a traceback.
        """
        # Make the message smaller
        message = ", ".join([x.strip() for x in message.split("\n")])
        message = f"{get_timestamp_string()} - ERROR: ({self._name_and_alias}) : {message}"
        raise AssertionError(message)

    @final
    def raise_failure(self, message: str) -> None:
        """Raise an AssertionError with the provided message indicating there was a failure.

        Args:
            message: The message to add to the AssertionError.

        Raises:
            AssertionError: Prints out the failure message with a traceback.
        """
        # Make the message smaller
        message = ", ".join([x.strip() for x in message.split("\n")])
        message = f"{get_timestamp_string()} - FAILURE: ({self._name_and_alias}) : {message}"
        raise AssertionError(message)

    @final
    def reboot(self, quiet_period: int = 0) -> bool:
        """Reboot the device and reconnect all its used resources and components.

        Args:
            quiet_period: Optional sleep after the reboot in seconds.

        Returns:
            A boolean representing the status of the reboot.
        """
        print_with_timestamp(f"Rebooting {self._name_and_alias}")
        self._reboot()
        self.close()
        # Depending on the instrument model, shutdown time or reboot time can take longer
        if quiet_period or self._reboot_quiet_period:
            sleep_time = max(self._reboot_quiet_period, quiet_period)
            print_with_timestamp(f"Waiting for {sleep_time} seconds")
            time.sleep(sleep_time)
        print_with_timestamp(f"Reopening Connection to {self._name_and_alias}")
        if rebooted := self._open():
            print_with_timestamp(f"Connection Reestablished with {self._name_and_alias}")
        else:
            print_with_timestamp(
                f"Failed to reestablish the connection with {self._name_and_alias}"
            )
        return rebooted

    @final
    def verify_values(  # noqa: PLR0913
        self,
        expected_value: Union[str, float],
        actual_value: Union[str, float],
        tolerance: float = 0,
        percentage: bool = False,
        custom_message_prefix: str = "",
        log_error: bool = False,
        expect_fail: bool = False,
    ) -> bool:
        """Compare and verify actual value with expected value.

        Args:
             expected_value: The expected value.
             actual_value: The actual value.
             tolerance: The acceptable difference between two floating point values, e.g. 0.0005
             percentage: A boolean indicating what kind of tolerance check to perform.
                 False means absolute tolerance: +/- tolerance.
                 True means percent tolerance: +/- (tolerance / 100) * value.
             custom_message_prefix: A custom message to be prepended to the failure message.
             log_error: Indicate if an error should be logged instead of a failure
             expect_fail: Indicate if a failure is expected and should be treated as a pass

        Returns:
            Boolean indicating whether the check passed or failed.
        """
        message = custom_message_prefix + "\n" if custom_message_prefix else ""

        try:
            _ = float(tolerance)
            _ = float(expected_value)
            _ = float(actual_value)
            number_comparison = True
        except ValueError:
            number_comparison = False

        if number_comparison:
            expected_value = float(expected_value)
            actual_value = float(actual_value)
            if percentage:
                tolerance = abs((tolerance / 100.0) * expected_value)
            message, verify_passed = self._verify_numerical_value(
                expected_value, actual_value, tolerance, message, expect_fail
            )
        else:
            expected_value = str(expected_value)
            actual_value = str(actual_value)
            message, verify_passed = self._verify_string_value(
                expected_value, actual_value, message, expect_fail
            )
        # Mark as pass/fail
        if not verify_passed:
            if log_error:
                self.raise_error(message)
            else:
                self.raise_failure(message)

        return verify_passed

    @final
    def wait_for_network_connection(
        self,
        wait_time: float,
        sleep_seconds: int = 2,
        accept_immediate_connection: bool = False,
        verbose: bool = True,
    ) -> bool:
        """Wait for a network connection to the device.

        Args:
            wait_time: The number of seconds to wait for the network connection.
            sleep_seconds: The number of seconds to sleep in between connection attempts.
            accept_immediate_connection: A boolean indicating if a connection on the
                                         first attempt is a valid connection.
            verbose: Set this to False in order to disable printouts.

        Returns:
            A boolean indicating if a network connection was made within the given time limit.

        Raises:
            AssertionError: Indicating that the device erroneously connected on the first try.
        """
        attempt_num = 0
        network_connection = False
        if verbose:
            print_with_timestamp(
                f"Attempting to establish a network connection with {self.ip_address}"
            )
        start_time = time.perf_counter()
        while (time.perf_counter() - start_time) <= wait_time:
            if network_connection := self.check_network_connection(verbose=False)[0]:
                # pylint: disable=compare-to-zero
                if not (attempt_num == 0 and not accept_immediate_connection):
                    break
                msg = (
                    f"A network connection was established with "
                    f"{self.ip_address} on the first attempt "
                    f"when it should not have been."
                )
                raise AssertionError(msg)
            time.sleep(sleep_seconds)
            attempt_num += 1

        end_time = time.perf_counter()
        total_time = end_time - start_time

        if verbose:
            if network_connection:
                print_with_timestamp(
                    f"Successfully established a network connection with {self.ip_address} "
                    f"after {total_time:.2f} seconds"
                )
            else:
                print_with_timestamp(
                    f"Unable to establish a network connection with {self.ip_address} "
                    f"after {total_time:.2f} seconds"
                )
        return network_connection

    def wait_for_port_connection(
        self,
        port: int,
        wait_time: float,
        sleep_seconds: int = 5,
        accept_immediate_connection: bool = False,
        verbose: bool = True,
    ) -> bool:
        """Wait for a connection to be made to the given port on the device.

        Args:
            port: The port to check.
            wait_time: The maximum time to wait in seconds.
            sleep_seconds: The number of seconds to sleep in between connection attempts.
            accept_immediate_connection: A boolean indicating if a connection on the
                                         first attempt is a valid connection.
            verbose: Set this to False in order to disable printouts.

        Returns:
            A boolean indicating if a connection was made to the port within the given time limit.

        Raises:
            AssertionError: Indicating that the device erroneously connected on the first try.
        """
        attempt_num = 0
        port_connection = False
        if verbose:
            print_with_timestamp(
                f"Attempting to establish a connection to port {port} on {self.ip_address}"
            )
        start_time = time.perf_counter()
        while (time.perf_counter() - start_time) <= wait_time:
            port_connection = self.check_port_connection(
                port, timeout_seconds=sleep_seconds, verbose=False
            )
            if port_connection:
                # pylint: disable=compare-to-zero
                if not (attempt_num == 0 and not accept_immediate_connection):
                    break
                msg = (
                    f"A connection was established with port {port} on "
                    f"{self.ip_address} on the first attempt "
                    f"when it should not have been."
                )
                raise AssertionError(msg)
            time.sleep(sleep_seconds)
            attempt_num += 1

        end_time = time.perf_counter()
        total_time = end_time - start_time

        if verbose:
            if port_connection:
                print_with_timestamp(
                    f"Successfully established a connection to port {port} on {self.ip_address} "
                    f"after {total_time:.2f} seconds"
                )
            else:
                print_with_timestamp(
                    f"Unable to establish a connection to port {port} on {self.ip_address} "
                    f"after {total_time:.2f} seconds"
                )
        return port_connection

    ################################################################################################
    # Private Methods
    ################################################################################################

    @staticmethod
    @final
    def _verify_numerical_value(
        expected_value: float,
        actual_value: float,
        tolerance: float,
        message: str,
        expect_fail: bool,
    ) -> Tuple[str, bool]:
        """Compare and verify a numerical value with expected value.

        Args:
             expected_value: The expected value.
             actual_value: The actual value.
             tolerance: The acceptable difference between two floating point values, e.g. 0.0005
             message: The failure message to edit and return.
             expect_fail: Indicate if a failure is expected and should be treated as a pass

        Returns:
            Tuple containing the failure message and a boolean indicating if the check passed.
        """
        max_value = expected_value + tolerance
        min_value = expected_value - tolerance
        # Verify that the number is within the tolerance.
        # Also check to make sure that the string of each number is
        # identical, this prevents issues from returned values that have
        # a trailing zero or some other non-contributing character that
        # will cause comparison issues.
        if (
            not expect_fail
            and (
                abs(expected_value - actual_value) <= tolerance
                or str(expected_value) == str(actual_value)
            )
        ) or (
            expect_fail
            and not (
                abs(expected_value - actual_value) <= tolerance
                or str(expected_value) == str(actual_value)
            )
        ):
            verify_passed = True
        else:
            message += (
                f"Actual result {'does not match' if not expect_fail else 'matches'} "
                f"the expected result within a tolerance of {tolerance}"
                f"\n  max: {max_value}"
                f"\n  act: {actual_value}"
                f"\n  min: {min_value}"
            )
            verify_passed = False

        return message, verify_passed

    @staticmethod
    @final
    def _verify_string_value(
        expected_value: str,
        actual_value: str,
        message: str,
        expect_fail: bool,
    ) -> Tuple[str, bool]:
        """Compare and verify a string value with expected value.

        Args:
             expected_value: The expected value.
             actual_value: The actual value.
             message: The failure message to edit and return.
             expect_fail: Indicate if a failure is expected and should be treated as a pass

        Returns:
            Tuple containing the failure message and a boolean indicating if the check passed.
        """
        if (not expect_fail and expected_value == actual_value) or (
            expect_fail and expected_value != actual_value
        ):
            verify_passed = True
        else:
            message += (
                f"Actual result {'does not match' if not expect_fail else 'matches'} "
                f"the expected result"
                f"\n  exp{' != ' if expect_fail else ': '}{expected_value}"
                f"\n  act{' == ' if expect_fail else ': '}{actual_value}"
            )
            verify_passed = False

        return message, verify_passed
