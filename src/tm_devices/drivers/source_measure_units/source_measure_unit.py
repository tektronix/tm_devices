"""Base Source Measure Unit (SMU) device driver module.

SMUs include TSP devices and PI devices.
"""

from abc import ABC

from tm_devices.helpers import DeviceTypes


# pylint: disable=too-few-public-methods
class SourceMeasureUnit(ABC):  # noqa: B024
    """Base Source Measure Unit (SMU) device driver."""

    _DEVICE_TYPE = DeviceTypes.SMU.value

    ################################################################################################
    # Public Methods
    ################################################################################################
