import abc

from abc import ABC
from dataclasses import dataclass

from tm_devices.helpers import DeviceConfigEntry

class TSPControl(ABC, metaclass=abc.ABCMeta):
    def __init__(self, config_entry: DeviceConfigEntry, verbose: bool) -> None: ...
    def already_exists(self) -> None:
        """Return nothing."""
    def added_tsp_method(self) -> None:
        """Return nothing."""

@dataclass(frozen=True)
class CustomDataclass:
    value1: str
    value2: int = 1
