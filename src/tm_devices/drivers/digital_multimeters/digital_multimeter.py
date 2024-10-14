"""Base Digital Multimeter (DMM) device driver module."""

from abc import ABC

from tm_devices.drivers.device import Device
from tm_devices.helpers import DeviceTypes


class DigitalMultimeter(Device, ABC):
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
