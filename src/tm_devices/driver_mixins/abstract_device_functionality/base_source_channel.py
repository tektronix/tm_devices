"""Base source channel module."""

from abc import ABC, abstractmethod
from typing import Optional

from tm_devices.driver_mixins.device_control import PIControl
from tm_devices.driver_mixins.shared_implementations._extension_mixin import (
    _ExtendableMixin,  # pyright: ignore[reportPrivateUsage]
)


class BaseSourceChannel(_ExtendableMixin, ABC):
    """Base source channel."""

    def __init__(self, pi_control: PIControl, channel_name: str) -> None:
        """Create a source channel.

        Args:
            pi_control: A PI device.
            channel_name: The channel name for the source channel.
        """
        self._name = channel_name
        self._num = None
        if channel_num := "".join(filter(str.isdigit, channel_name)):
            self._num = int(channel_num)
        self._pi_control = pi_control

    @property
    def name(self) -> str:
        """Return the channel name."""
        return self._name

    @property
    def num(self) -> Optional[int]:
        """Return the channel number."""
        return self._num

    @abstractmethod
    def set_amplitude(self, value: float, absolute_tolerance: float = 0) -> None:
        """Set the amplitude on the source channel.

        Args:
            value: The amplitude value to set.
            absolute_tolerance: The acceptable difference between two floating point values.
        """
        raise NotImplementedError

    @abstractmethod
    def set_offset(self, value: float, absolute_tolerance: float = 0) -> None:
        """Set the offset on the source channel.

        Args:
            value: The offset value to set.
            absolute_tolerance: The acceptable difference between two floating point values.
        """
        raise NotImplementedError

    @abstractmethod
    def set_state(self, value: int) -> None:
        """Set the output state to ON/OFF (1/0) on the source channel.

        Args:
            value: The output state.
        """
        raise NotImplementedError
