"""Base device driver module."""

import concurrent.futures
import logging
import socket
import time

from abc import ABC, abstractmethod
from contextlib import contextmanager, suppress
from functools import cached_property as functools_cached_property
from typing import (
    Any,
    final,
    Generator,
    Optional,
    Tuple,
    TypeVar,
)

from packaging.version import Version

from tm_devices.driver_mixins.device_control._abstract_device_control import (
    _AbstractDeviceControl,  # pyright: ignore[reportPrivateUsage]
)
from tm_devices.driver_mixins.shared_implementations._extension_mixin import (
    _ExtendableMixin,  # pyright: ignore[reportPrivateUsage]
)
from tm_devices.helpers import (
    check_network_connection,
    check_port_connection,
    ConnectionTypes,
    DeviceConfigEntry,
)
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

_T = TypeVar("_T")
_FAMILY_BASE_CLASS_PROPERTY_NAME = "_product_family_base_class"

_logger: logging.Logger = logging.getLogger(__name__)


def family_base_class(cls: _T) -> _T:
    """A decorator indicating a class is the top level of a unique product family tree.

    Notes:
        All subclassed children will point to the decorated class.
    """
    setattr(cls, _FAMILY_BASE_CLASS_PROPERTY_NAME, cls)
    return cls


# pylint: disable=too-many-instance-attributes,too-many-public-methods
class Device(_AbstractDeviceControl, _ExtendableMixin, ABC):
    """Base device driver that all devices inherit from."""

    ################################################################################################
    # Categories:
    # - Magic Methods
    # - Abstract Properties
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
            verbose: A boolean indicating if verbose output should be printed. If True,
                communication printouts will be logged with a level of INFO. If False,
                communication printouts will be logged with a level of DEBUG.
        """
        super().__init__(config_entry, verbose)
        self._is_open = True
        self._device_number: int = -1  # set after creation by DeviceManager
        self._reboot_quiet_period = 0
        self._series = self.__class__.__name__

        # These private attributes are used by the auto-generated commands subpackage
        self._command_verification_enabled = False
        self._command_syntax_enabled = False

    def __str__(self) -> str:
        """Return a string representation of the class."""
        line_break_length = 90
        retval = f"{'=' * (line_break_length // 2)} {self.name} {'=' * (line_break_length // 2)}\n"
        retval += f"  {self.__class__} object at {id(self)}"

        for prop in self._get_self_properties():
            if not prop.startswith("_"):
                retval += f"\n    {prop}={self.__getattribute__(prop)!r}"

        retval += f"\n{'=' * (line_break_length + 2 + len(self.name))}"
        return retval

    ################################################################################################
    # Abstract Properties
    ################################################################################################
    @cached_property
    @abstractmethod
    def device_type(self) -> str:
        """Return a string representing the device type."""

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
    def _open(self) -> bool:
        """Perform the actual opening code.

        Returns:
           A boolean indicating if device connected successfully.
        """

    def _reboot(self) -> None:
        """Perform the actual rebooting code."""
        raise NotImplementedError(
            f"``._reboot()`` is not yet implemented for the {self.__class__.__name__} driver",  # noqa: EM102
        )

    ################################################################################################
    # Properties - Private and Public
    ################################################################################################
    @cached_property
    def name_and_alias(self) -> str:
        """Return string for easy ID of device in console output prints."""
        retval = self.name
        if self.alias:  # pylint: disable=using-constant-test
            retval += f' "{self.alias}"'
        return retval.replace(" NotImplemented", "")

    @property
    def address(self) -> str:
        """Return the device address as defined in the config_entry.

        This could be an IP address, hostname, or USB device address.
        """
        return self._config_entry.address

    @cached_property
    def alias(self) -> str:
        """Return the alias if it exists, otherwise an empty string."""
        return self._config_entry.alias if self._config_entry.alias is not None else ""

    @cached_property
    def command_argument_constants(self) -> Any:
        """Return the device command argument constants."""
        raise NotImplementedError(
            f"The {self.__class__.__name__} driver does not have a Python API for its commands yet."  # noqa: EM102
        )

    @property
    def command_syntax_enabled(self) -> bool:
        """Return a string containing the syntax of the command being accessed.

        This property indicates when the syntax should be returned instead of writing/querying the
        device and returning the result.
        """
        return self._command_syntax_enabled

    @property
    def command_verification_enabled(self) -> bool:
        """Indicate if command verification is enabled.

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

    @cached_property
    def commands(self) -> Any:
        """Return the device commands."""
        raise NotImplementedError(
            f"The {self.__class__.__name__} driver does not have a Python API for its commands yet."  # noqa: EM102
        )

    @cached_property
    def config_entry(self) -> DeviceConfigEntry:
        """Return the device config."""
        return self._config_entry

    @property
    def connection_type(self) -> str:
        """Return a string indicating the connection type."""
        return self._config_entry.connection_type.value

    @property
    def device_number(self) -> int:
        """Return the device number, if it was not created by the DeviceManager it will be -1."""
        return self._device_number

    @property
    def enable_verification(self) -> bool:
        """Return the boolean which indicates if verification checks should happen.

        This can be disabled after developing a script in order to increase the speed of the script.

        Notes:
            - If ``.enable_verification`` is set to ``False``, then no verification of any
              commands sent using the ``.set_and_check()`` method will occur
              (the "check" portion of "set" and "check" will be skipped).
            - If ``.enable_verification`` is set to ``True``, then
              verification will happen for commands sent using the ``.set_and_check()`` method
              (both the "set" and "check" portions will be executed).
        """
        return self._enable_verification

    @enable_verification.setter
    def enable_verification(self, value: bool) -> None:
        """Set the ``self.enable_verification`` attribute."""
        self._enable_verification = value

    @property
    def is_open(self) -> bool:
        """Indicate if the connection to the device is currently open."""
        return self._is_open

    @cached_property
    def name(self) -> str:
        """Return the device name.

        Usually something like "SCOPE 1"
        """
        return f"{self.device_type} {max(0, self.device_number) or ''}".strip()

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
        if self._config_entry.connection_type not in {
            ConnectionTypes.USB,
            ConnectionTypes.SERIAL,
            ConnectionTypes.GPIB,
            ConnectionTypes.MOCK,
        }:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(socket.gethostbyaddr, self.address)
                try:
                    return future.result(timeout=2)[0]  # Use a two-second timeout for the lookup
                except (socket.gaierror, socket.herror, concurrent.futures.TimeoutError):
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

    @contextmanager
    def temporary_enable_verification(
        self, temporary_enable_verification: bool
    ) -> Generator[None, None, None]:
        """Enable (or disable) all verification of communication for the duration of the context.

        This will temporarily set the
        [`Device.enable_verification`][tm_devices.drivers.device.Device.enable_verification]
        property to the specified value, and then reset it to the previous value
        when the context exits.

        Args:
            temporary_enable_verification: The temporary verification value (True or False).
        """
        old_enable_verification = self.enable_verification
        self.enable_verification = temporary_enable_verification
        try:
            yield
        finally:
            self.enable_verification = old_enable_verification

    ################################################################################################
    # Public Methods
    ################################################################################################
    @final
    def check_network_connection(self) -> Tuple[bool, str]:
        """Check the network connection to the device using an external ping command.

        Wrapper function for
        [`check_network_connection`][tm_devices.helpers.check_network_connection].

        Returns:
            A tuple containing a boolean indicating if there is a network connection and
                a string with the result of the ping command.
        """
        return check_network_connection(self.name_and_alias, self.ip_address)

    @final
    def check_port_connection(self, port: int, timeout_seconds: int = 5) -> bool:
        """Check if the given port is open on the device.

        Wrapper function for [`check_port_connection`][tm_devices.helpers.check_port_connection].

        Args:
            port: The port to check.
            timeout_seconds: The number of seconds to use as the socket timeout.

        Returns:
            A boolean indicating if the port is open.
        """
        return check_port_connection(
            self.name_and_alias,
            self.ip_address,
            port,
            timeout_seconds=timeout_seconds,
        )

    @final
    def cleanup(self, verbose: bool = True) -> None:
        """Perform the cleanup defined for the device.

        Args:
            verbose: Set this to False in order to disable printouts.
        """
        with self.temporary_verbose(verbose):
            _logger.info("Beginning Device Cleanup on %s", self.name_and_alias)
            self._cleanup()
            _logger.info("Finished Device Cleanup on %s", self.name_and_alias)

    @final
    def close(self) -> None:
        """Close this device and all its used resources and components."""
        _logger.info("Closing Connection to %s", self.name_and_alias)
        self._close()

    @final
    def get_errors(self) -> Tuple[int, Tuple[str, ...]]:
        """Get the current errors from the device.

        !!! note
            This method will clear out the error queue after reading the current errors.

        Returns:
            A tuple containing the current error code alongside a tuple of the current error
                messages.
        """
        return self._get_errors()

    @final
    def has_errors(self) -> bool:
        """Check if the device has any errors.

        !!! note
            This method will clear out the error queue after reading the current errors.

        Returns:
            A boolean indicating if any errors were found in the device. True means there were
                errors, False means no errors were found.
        """
        return bool(self.get_errors()[0])

    @final
    def reboot(self, quiet_period: int = 0) -> bool:
        """Reboot the device and reconnect all its used resources and components.

        Args:
            quiet_period: Optional sleep after the reboot in seconds.

        Returns:
            A boolean representing the status of the reboot.
        """
        # Reset the cached properties
        for prop in self._get_self_properties():
            if isinstance(getattr(self.__class__, prop), functools_cached_property):
                # Try to delete the cached_property, if it raises an AttributeError,
                # that means that it has not previously been accessed and
                # there is no need to delete the cached_property.
                with suppress(AttributeError):
                    self.__delattr__(prop)  # pylint: disable=unnecessary-dunder-call

        # Reboot the device
        _logger.info("Rebooting %s", self.name_and_alias)
        self._reboot()
        self.close()
        # Depending on the instrument model, shutdown time or reboot time can take longer
        if quiet_period or self._reboot_quiet_period:
            sleep_time = max(self._reboot_quiet_period, quiet_period)
            _logger.info("Waiting for %d seconds", sleep_time)
            time.sleep(sleep_time)
        _logger.info("Reopening Connection to %s", self.name_and_alias)
        if rebooted := self._open():
            _logger.info("Connection Reestablished with %s", self.name_and_alias)
        else:
            _logger.error("Failed to reestablish the connection with %s", self.name_and_alias)
        return rebooted

    @final
    def wait_for_network_connection(
        self,
        wait_time: float,
        sleep_seconds: int = 2,
        accept_immediate_connection: bool = False,
    ) -> bool:
        """Wait for a network connection to the device.

        Args:
            wait_time: The number of seconds to wait for the network connection.
            sleep_seconds: The number of seconds to sleep in between connection attempts.
            accept_immediate_connection: A boolean indicating if a connection on the
                                         first attempt is a valid connection.

        Returns:
            A boolean indicating if a network connection was made within the given time limit.

        Raises:
            AssertionError: Indicating that the device erroneously connected on the first try.
        """
        attempt_num = 0
        network_connection = False
        _logger.log(
            logging.INFO if self._verbose else logging.DEBUG,
            "Attempting to establish a network connection with %s",
            self.ip_address,
        )
        start_time = time.perf_counter()
        while (time.perf_counter() - start_time) <= wait_time:
            if network_connection := self.check_network_connection()[0]:
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

        if network_connection:
            _logger.log(
                logging.INFO if self._verbose else logging.DEBUG,
                "Successfully established a network connection with %s after %.2f seconds",
                self.ip_address,
                total_time,
            )
        else:
            _logger.warning(
                "Unable to establish a network connection with %s after %.2f seconds",
                self.ip_address,
                total_time,
            )
        return network_connection

    def wait_for_port_connection(
        self,
        port: int,
        wait_time: float,
        sleep_seconds: int = 5,
        accept_immediate_connection: bool = False,
    ) -> bool:
        """Wait for a connection to be made to the given port on the device.

        Args:
            port: The port to check.
            wait_time: The maximum time to wait in seconds.
            sleep_seconds: The number of seconds to sleep in between connection attempts.
            accept_immediate_connection: A boolean indicating if a connection on the
                                         first attempt is a valid connection.

        Returns:
            A boolean indicating if a connection was made to the port within the given time limit.

        Raises:
            AssertionError: Indicating that the device erroneously connected on the first try.
        """
        attempt_num = 0
        port_connection = False
        _logger.log(
            logging.INFO if self._verbose else logging.DEBUG,
            "Attempting to establish a connection to port %d on %s",
            port,
            self.ip_address,
        )
        start_time = time.perf_counter()
        while (time.perf_counter() - start_time) <= wait_time:
            if port_connection := self.check_port_connection(port, timeout_seconds=sleep_seconds):
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

        if port_connection:
            _logger.log(
                logging.INFO if self._verbose else logging.DEBUG,
                "Successfully established a connection to port %d on %s after %.2f seconds",
                port,
                self.ip_address,
                total_time,
            )
        else:
            _logger.warning(
                "Unable to establish a connection to port %d on %s after %.2f seconds",
                port,
                self.ip_address,
                total_time,
            )
        return port_connection

    ################################################################################################
    # Private Methods
    ################################################################################################
    def _get_self_properties(self) -> Tuple[str, ...]:
        """Get a complete list of all the properties of the device."""
        return tuple(
            p
            for p in dir(self.__class__)
            if isinstance(getattr(self.__class__, p), (functools_cached_property, property))
        )
