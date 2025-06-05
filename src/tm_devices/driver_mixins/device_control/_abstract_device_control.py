"""A class containing properties and attributes shared between devices and control mixins."""

from abc import ABC, abstractmethod
from typing import Tuple

from packaging.version import Version

from tm_devices.helpers import DeviceConfigEntry
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


class _AbstractDeviceControl(ABC):  # pyright: ignore[reportUnusedClass]
    """Abstract class with properties and attributes shared between devices and control mixins."""

    def __init__(self, config_entry: DeviceConfigEntry, verbose: bool) -> None:
        """Create a device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed. If True,
                communication printouts will be logged with a level of INFO. If False,
                communication printouts will be logged with a level of DEBUG.
        """
        self._is_open = False
        self._verbose = verbose
        self._config_entry = config_entry
        self._enable_verification = True

    @cached_property
    @abstractmethod
    def name_and_alias(self) -> str:
        """A string containing the device name and alias."""

    @cached_property
    @abstractmethod
    def ip_address(self) -> str:
        """The IP address of the device."""

    @abstractmethod
    def _get_errors(self) -> Tuple[int, Tuple[str, ...]]:
        """Get the current errors from the device.

        !!! note
            This method will clear out the error queue after reading the current errors.

        Returns:
            A tuple containing the current error code alongside a tuple of the current error
                messages.
        """

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
