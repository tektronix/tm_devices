"""A class containing properties and attributes shared between devices and control mixins."""

from abc import ABC, abstractmethod

from tm_devices.helpers import DeviceConfigEntry
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


# TODO: nfelt14: Look into making this private or filtering it out of the docs
# TODO: nfelt14: Look into moving the _get_errors() abstract method to this class for
#  type hinting and usage in the control classes
class AbstractDeviceControl(ABC):  # pylint: disable=too-few-public-methods
    """Abstract class with properties and attributes shared between devices and control mixins."""

    def __init__(self, config_entry: DeviceConfigEntry, verbose: bool) -> None:
        """Create a device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
        """
        self._is_open = False
        self._verbose = verbose
        self._config_entry = config_entry
        self._enable_verification = True

    @property
    @abstractmethod
    def _name_and_alias(self) -> str:
        """A string containing the device name and alias."""

    @cached_property
    @abstractmethod
    def ip_address(self) -> str:
        """The IP address of the device."""
