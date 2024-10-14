"""Base Data Acquisition (DAQ) device driver module."""

from abc import ABC

from tm_devices.drivers.device import Device
from tm_devices.helpers import DeviceTypes


class DataAcquisitionSystem(Device, ABC):
    """Base Data Acquisition (DAQ) device driver."""

    _DEVICE_TYPE = DeviceTypes.DAQ.value

    ################################################################################################
    # Private Methods
    ################################################################################################
