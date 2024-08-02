"""Base Data Acquisition (DAQ) device driver module."""

from abc import ABC

from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.pi.tsp_device import TSPDevice
from tm_devices.helpers import DeviceTypes


@family_base_class
class DataAcquisitionSystem(TSPDevice, ABC):
    """Base Data Acquisition (DAQ) device driver."""

    _DEVICE_TYPE = DeviceTypes.DAQ.value

    ################################################################################################
    # Private Methods
    ################################################################################################
