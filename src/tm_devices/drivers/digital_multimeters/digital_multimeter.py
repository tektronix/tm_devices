"""Base Digital Multimeter (DMM) device driver module."""

from abc import ABC

from tm_devices.drivers.device import Device
from tm_devices.helpers import DeviceTypes
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


class DigitalMultimeter(Device, ABC):
    """Base Digital Multimeter (DMM) device driver."""

    ################################################################################################
    # Properties
    ################################################################################################
    @cached_property
    def device_type(self) -> str:
        """Return a string representing the device type."""
        return DeviceTypes.DMM.value

    ################################################################################################
    # Public Methods
    ################################################################################################

    ################################################################################################
    # Private Methods
    ################################################################################################
