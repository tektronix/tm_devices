"""Base Data Acquisition (DAQ) device driver module."""

from abc import ABC

from tm_devices.helpers import DeviceTypes


# pylint: disable=too-few-public-methods
class DataAcquisitionSystem(ABC):  # noqa: B024
    """Base Data Acquisition (DAQ) device driver."""

    _DEVICE_TYPE = DeviceTypes.DAQ.value

    ################################################################################################
    # Private Methods
    ################################################################################################
