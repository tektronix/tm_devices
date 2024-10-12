"""Base Systems Switch (SS) device driver module."""

from abc import ABC

from tm_devices.drivers.device import Device
from tm_devices.helpers import DeviceTypes


# pylint: disable=too-few-public-methods
class SystemsSwitch(Device, ABC):
    """Base Systems Switch (SS) device driver."""

    _DEVICE_TYPE = DeviceTypes.SS.value

    ################################################################################################
    # Public Methods
    ################################################################################################
