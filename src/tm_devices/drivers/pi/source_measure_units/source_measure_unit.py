"""Base Source Measure Unit (SMU) device driver module.

SMUs include TSP devices and PI devices.
"""
from abc import ABC

from tm_devices.drivers.pi.tsp_device import TSPDevice
from tm_devices.helpers import DeviceTypes


class SourceMeasureUnit(TSPDevice, ABC):
    """Base Source Measure Unit (SMU) device driver."""

    _DEVICE_TYPE = DeviceTypes.SMU.value

    ################################################################################################
    # Public Methods
    ################################################################################################
