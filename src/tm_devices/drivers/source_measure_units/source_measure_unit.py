"""Base Source Measure Unit (SMU) device driver module.

SMUs include TSP devices and PI devices.
"""

from abc import ABC

from tm_devices.drivers.device import Device
from tm_devices.helpers import DeviceTypes
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


class SourceMeasureUnit(Device, ABC):
    """Base Source Measure Unit (SMU) device driver."""

    ################################################################################################
    # Properties
    ################################################################################################
    @cached_property
    def device_type(self) -> str:
        """Return a string representing the device type."""
        return DeviceTypes.SMU.value

    ################################################################################################
    # Public Methods
    ################################################################################################
