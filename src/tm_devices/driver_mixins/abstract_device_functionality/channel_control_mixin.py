"""A mixin class that provides access to methods for controlling channels on a device."""

from abc import ABC, abstractmethod
from typing import final, Tuple

from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


class ChannelControlMixin(ABC):
    """A mixin class which adds methods and properties for controlling channels on a device."""

    ################################################################################################
    # Abstract Properties
    ################################################################################################
    @property
    @abstractmethod
    def all_channel_names_list(self) -> Tuple[str, ...]:
        """Return a tuple containing all the channel names."""

    @cached_property
    @abstractmethod
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""

    ################################################################################################
    # Abstract Methods
    ################################################################################################
    @abstractmethod
    def turn_channel_off(self, channel_str: str) -> None:
        """Turn off the specified channel.

        Args:
            channel_str: The name of the channel to turn off.
        """

    @abstractmethod
    def turn_channel_on(self, channel_str: str) -> None:
        """Turn on the specified channel.

        Args:
            channel_str: The name of the channel to turn on.
        """

    ################################################################################################
    # Public Methods
    ################################################################################################
    @final
    def turn_all_channels_off(self) -> None:
        """Turn all channels off."""
        for ch_str in self.all_channel_names_list:
            self.turn_channel_off(ch_str)

    @final
    def turn_all_channels_on(self) -> None:
        """Turn all channels on."""
        for ch_str in self.all_channel_names_list:
            self.turn_channel_on(ch_str)
