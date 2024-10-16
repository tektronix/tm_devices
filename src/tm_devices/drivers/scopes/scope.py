"""Base Scope device driver module."""

from abc import ABC, abstractmethod
from typing import Tuple

from tm_devices.drivers.device import Device
from tm_devices.helpers import DeviceTypes
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


class Scope(Device, ABC):
    """Base Scope device driver."""

    _DEVICE_TYPE = DeviceTypes.SCOPE.value

    ################################################################################################
    # Abstract Properties
    ################################################################################################
    @cached_property
    @abstractmethod
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""

    ################################################################################################
    # Abstract Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################
    @property
    def all_channel_names_list(self) -> Tuple[str, ...]:
        """Return a tuple containing all the channel names."""
        return tuple(f"CH{x+1}" for x in range(self.total_channels))
