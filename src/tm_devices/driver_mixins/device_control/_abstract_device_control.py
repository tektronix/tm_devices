"""A class containing properties and attributes shared between devices and control mixins."""

from abc import ABC, abstractmethod
from typing import Tuple

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
