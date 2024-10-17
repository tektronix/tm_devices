"""Base Data Acquisition (DAQ) device driver module."""

from abc import ABC

from tm_devices.drivers.device import Device
from tm_devices.helpers import DeviceTypes
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


class DataAcquisitionSystem(Device, ABC):
    """Base Data Acquisition (DAQ) device driver."""

    ################################################################################################
    # Properties
    ################################################################################################
    @cached_property
    def device_type(self) -> str:
        """Return a string representing the device type."""
        return DeviceTypes.DAQ.value

    ################################################################################################
    # Private Methods
    ################################################################################################
