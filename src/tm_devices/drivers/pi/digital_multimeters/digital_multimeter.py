"""Base Digital Multimeter (DMM) device driver module."""

from abc import ABC

from tm_devices.drivers.pi.tsp_device import TSPDevice
from tm_devices.helpers import DeviceTypes


class DigitalMultimeter(TSPDevice, ABC):
    """Base Digital Multimeter (DMM) device driver."""

    _DEVICE_TYPE = DeviceTypes.DMM.value

    ################################################################################################
    # Properties
    ################################################################################################

    ################################################################################################
    # Public Methods
    ################################################################################################

    ################################################################################################
    # Private Methods
    ################################################################################################
