"""Base Systems Switch (SS) device driver module."""

from abc import ABC

from tm_devices.helpers import DeviceTypes


# pylint: disable=too-few-public-methods
class SystemsSwitch(ABC):  # noqa: B024
    """Base Systems Switch (SS) device driver."""

    _DEVICE_TYPE = DeviceTypes.SS.value

    ################################################################################################
    # Public Methods
    ################################################################################################
