import abc

from abc import ABC
from typing import List

from tm_devices.helpers import DeviceConfigEntry

class Device(ABC, metaclass=abc.ABCMeta):
    def __init__(self, config_entry: DeviceConfigEntry, verbose: bool) -> None: ...
    def already_exists(self) -> None:
        """Return nothing."""
    @property
    def inc_cached_count(self) -> int:
        """Increment a local counter."""
    @property
    def inc_count(self) -> int:
        """Increment a local counter."""
    @property
    def class_name(self) -> str:
        """Return the class name."""
    def custom_model_getter(
        self, value1: str, value2: str = "add", value3: str = "", value4: float = 0.1
    ) -> str:
        """Return the model."""
    def custom_list(self) -> List[str]:
        """Return the model and serial in a list."""
    def custom_return_none(self) -> None:
        """Return nothing.

        This has a multi-line description.
        """
