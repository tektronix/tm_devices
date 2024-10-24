"""AWG7K device driver module."""

from types import MappingProxyType
from typing import Dict, Optional, Tuple

from tm_devices.commands import AWG7KMixin
from tm_devices.drivers.awgs.awg import (
    AWG,
    AWGSourceChannel,
    AWGSourceDeviceConstants,
    ParameterBounds,
)
from tm_devices.drivers.awgs.awg5k import (
    AWG5KSourceChannel,
)
from tm_devices.drivers.device import family_base_class
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813
from tm_devices.helpers.enums import SignalGeneratorOutputPathsBase


@family_base_class
class AWG7K(AWG7KMixin, AWG):
    """AWG7K device driver."""

    _DEVICE_CONSTANTS = AWGSourceDeviceConstants(
        memory_page_size=1,
        memory_max_record_length=32400000,
        memory_min_record_length=2,
    )

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################
    @cached_property
    def source_channel(self) -> "MappingProxyType[str, AWGSourceChannel]":
        """Mapping of channel names to AWG7KSourceChannel objects."""
        channel_map: Dict[str, AWG7KSourceChannel] = {}
        for channel_name in self.all_channel_names_list:
            channel_map[channel_name] = AWG7KSourceChannel(self, channel_name)
        return MappingProxyType(channel_map)

    ################################################################################################
    # Private Methods
    ################################################################################################
    def _get_series_specific_constraints(
        self,
        output_signal_path: Optional[SignalGeneratorOutputPathsBase],
    ) -> Tuple[ParameterBounds, ParameterBounds, ParameterBounds]:
        """Get constraints which are dependent on the model series and parameters.

        Args:
            output_signal_path: The signal path that the output is taking.

        Returns:
            Ranges for amplitude, offset, and sample rate.
        """
        if not output_signal_path:
            output_signal_path = self.OutputSignalPath.DCA

        # if we are using the high bandwidth options
        if "02" in self.opt_string or "06" in self.opt_string:
            amplitude_range = ParameterBounds(lower=500.0e-3, upper=1.0)
            offset_range = ParameterBounds(lower=-0.0, upper=0.0)
        elif output_signal_path == self.OutputSignalPath.DCA:
            amplitude_range = ParameterBounds(lower=50e-3, upper=2.0)
            offset_range = ParameterBounds(lower=-0.5, upper=0.5)
        # if the DIR path is connected
        else:
            amplitude_range = ParameterBounds(lower=50e-3, upper=1.0)
            offset_range = ParameterBounds(lower=-0.0, upper=0.0)
        # AWG(Arbitrary Waveform Generator)7(Series)xx(GS/s)x(Channels)z(Model)
        # AWG7122C means the sample rate max is 12 GHz, a AWG7062C would have a 6 GHz max
        sample_rate_range = ParameterBounds(lower=10.0e6, upper=int(self.model[4:6]) * 1.0e9)

        return amplitude_range, offset_range, sample_rate_range


class AWG7KSourceChannel(AWG5KSourceChannel):
    """AWG7K signal source channel composite."""

    _awg: AWG7K  # pyright: ignore[reportIncompatibleVariableOverride]

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Public Methods
    ################################################################################################
    def set_offset(self, value: float, absolute_tolerance: float = 0) -> None:
        """Set the offset on the source channel.

        Args:
            value: The offset value to set.
            absolute_tolerance: The acceptable difference between two floating point values.
        """
        output_path = float(self._awg.query(f"AWGCONTROL:DOUTPUT{self.num}:STATE?"))
        if not ("02" in self._awg.opt_string or "06" in self._awg.opt_string) and not output_path:
            # Can only set offset on AWG7k's without 02 and 06 options and when then
            # output state is 0.
            self._awg.set_if_needed(
                f"{self.name}:VOLTAGE:OFFSET",
                value,
                tolerance=absolute_tolerance,
            )
        elif value:
            # No error is raised when 0 is the offset value and the output signal path
            # is in a state where offset cannot be set.
            offset_error = (
                f"The offset can only be set on {self._awg.model} without an 02 or 06 "
                "option and with an output signal path of "
                f"{self._awg.OutputSignalPath.DCA.value} "
                f"(AWGCONTROL:DOUTPUT{self.num}:STATE set to 0)."
            )
            raise ValueError(offset_error)

    def set_output_signal_path(
        self, value: Optional[SignalGeneratorOutputPathsBase] = None
    ) -> None:
        """Set the output signal path on the source channel.

        Args:
            value: The output signal path.
        """
        if not ("02" in self._awg.opt_string or "06" in self._awg.opt_string):
            # Can only set the output signal path on AWG7k's without 02 and 06 options.
            super().set_output_signal_path(value)
