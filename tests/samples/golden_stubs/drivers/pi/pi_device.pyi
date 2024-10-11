import abc

from abc import ABC

from tm_devices.helpers import DeviceConfigEntry

class PIDevice(ABC, metaclass=abc.ABCMeta):
    def __init__(self, config_entry: DeviceConfigEntry, verbose: bool) -> None: ...
    def already_exists(self) -> None:
        """Return nothing."""
    def added_method(self) -> None:
        """Return nothing."""

class OtherDevice(ABC, metaclass=abc.ABCMeta):
    def __init__(self, config_entry: DeviceConfigEntry, verbose: bool) -> None: ...
