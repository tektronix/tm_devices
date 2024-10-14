"""Base Power Supply Unit (PSU) device driver module.

PSUs include PI devices.
"""

from abc import ABC

from tm_devices.drivers.device import Device
from tm_devices.helpers import DeviceTypes


class PowerSupplyUnit(Device, ABC):
    """Base Power Supply Unit (PSU) device driver."""

    _DEVICE_TYPE = DeviceTypes.PSU.value

    ################################################################################################
    # Public Methods
    ################################################################################################
