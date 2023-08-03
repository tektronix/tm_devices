"""Base Application Programming Interface (API) device driver module."""
from abc import ABC

from tm_devices.drivers.device import Device


class APIDevice(Device, ABC):
    """Base Application Programming Interface (API) device driver."""
