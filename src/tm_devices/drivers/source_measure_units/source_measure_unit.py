"""Base Source Measure Unit (SMU) device driver module.

SMUs include TSP devices and PI devices.
"""

from abc import ABC

from tm_devices.drivers.device import Device
from tm_devices.helpers import DeviceTypes


class SourceMeasureUnit(Device, ABC):
    """Base Source Measure Unit (SMU) device driver."""

    _DEVICE_TYPE = DeviceTypes.SMU.value

    ################################################################################################
    # Public Methods
    ################################################################################################
