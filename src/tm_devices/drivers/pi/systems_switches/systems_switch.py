"""Base Systems Switch (SS) device driver module."""
from abc import ABC

from tm_devices.drivers.pi.tsp_device import TSPDevice
from tm_devices.helpers import DeviceTypes


class SystemsSwitch(TSPDevice, ABC):
    """Base Systems Switch (SS) device driver."""

    _DEVICE_TYPE = DeviceTypes.SS.value

    ################################################################################################
    # Public Methods
    ################################################################################################
