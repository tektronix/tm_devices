import abc

from abc import ABC

from tm_devices.helpers import DeviceConfigEntry

class Device(ABC, metaclass=abc.ABCMeta):
    class NestedClass:
        """This is a nested class."""

    def __init__(self, config_entry: DeviceConfigEntry, verbose: bool) -> None: ...
    def already_exists(self) -> None:
        """Return nothing."""
    @property
    def existing_property(self) -> int:
        """Return an int."""
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
    def custom_list(self) -> list[str]:
        """Return the model and serial in a list."""
    def custom_return_none(self) -> None:
        """Return nothing.

        This has a multi-line description.
        """

def function_1(arg1: str, arg2: int = 1) -> bool: ...

class OtherDevice(ABC, metaclass=abc.ABCMeta):
    def __init__(self, config_entry: DeviceConfigEntry, verbose: bool) -> None: ...

def function_2(arg1: str, arg2: int = 2) -> bool: ...
