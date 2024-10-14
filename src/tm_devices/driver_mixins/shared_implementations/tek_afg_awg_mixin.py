"""A private mixin for common methods and attributes for Tektronix AFG and AWG devices."""

from abc import ABC, abstractmethod
from typing import Tuple

from tm_devices.driver_mixins.abstract_device_functionality.signal_generator_mixin import (
    SignalGeneratorMixin,
)
from tm_devices.driver_mixins.shared_implementations.class_extension_mixin import ExtendableMixin
from tm_devices.driver_mixins.shared_implementations.common_pi_system_error_check_mixin import (
    CommonPISystemErrorCheckMixin,
)
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


class TektronixAFGAWGMixin(
    CommonPISystemErrorCheckMixin, SignalGeneratorMixin, ExtendableMixin, ABC
):
    """A private mixin for common methods and attributes for Tektronix AFG and AWG devices."""

    ################################################################################################
    # Properties
    ################################################################################################
    @property
    def all_channel_names_list(self) -> Tuple[str, ...]:
        """Return a tuple containing all the channel names."""
        return tuple(f"SOURCE{x+1}" for x in range(self.total_channels))

    @cached_property
    def opt_string(self) -> str:
        r"""Return the string returned from the ``*OPT?`` query when the device was created."""
        return self.query("*OPT?")

    @cached_property
    @abstractmethod
    def total_channels(self) -> int:
        """Return the total number of channels."""

    ################################################################################################
    # Public Methods
    ################################################################################################

    ################################################################################################
    # Private Methods
    ################################################################################################
    def _validate_channels(self, channel: str) -> Tuple[str, ...]:
        """Create a list of channels to use on the source based on the desired channel number.

        Args:
            channel: The channel name to output the signal from, or 'all'.

        Returns:
            A tuple containing the list of channels to use.
        """
        # Verify the channel given is valid
        if channel not in (valid_channels := ["all", *self.all_channel_names_list]):
            msg = f"Invalid channel name {channel!r}, valid items: {valid_channels}"
            raise AssertionError(msg)

        return self.all_channel_names_list if channel == "all" else (channel,)
