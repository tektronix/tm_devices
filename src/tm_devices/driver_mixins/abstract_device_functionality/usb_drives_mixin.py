"""A mixin class providing common methods and attributes for devices with usb ports."""

from abc import ABC, abstractmethod
from typing import Tuple

from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


# pylint: disable=too-few-public-methods
class USBDrivesMixin(ABC):
    """A mixin class which adds the usb_drives property."""

    @cached_property
    @abstractmethod
    def usb_drives(self) -> Tuple[str, ...]:
        """Return a list of all connected USB drives."""
