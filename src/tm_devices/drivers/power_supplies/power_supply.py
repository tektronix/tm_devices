"""Base Power Supply Unit (PSU) device driver module.

PSUs include PI devices.
"""

from abc import ABC

from tm_devices.drivers.device import Device
from tm_devices.helpers import DeviceTypes
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


class PowerSupplyUnit(Device, ABC):
    """Base Power Supply Unit (PSU) device driver."""

    ################################################################################################
    # Properties
    ################################################################################################
    @cached_property
    def device_type(self) -> str:
        """Return a string representing the device type."""
        return DeviceTypes.PSU.value

    ################################################################################################
    # Public Methods
    ################################################################################################
