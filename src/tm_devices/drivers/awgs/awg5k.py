"""AWG5K device driver module."""

from types import MappingProxyType
from typing import Dict, Optional, Tuple

from tm_devices.commands import AWG5KMixin
from tm_devices.drivers.awgs.awg import (
    AWG,
    AWGSourceChannel,
    AWGSourceDeviceConstants,
    ParameterBounds,
)
from tm_devices.drivers.device import family_base_class
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813
from tm_devices.helpers.enums import SignalGeneratorOutputPathsBase


@family_base_class
class AWG5K(AWG5KMixin, AWG):
    """AWG5K device driver."""

    _DEVICE_CONSTANTS = AWGSourceDeviceConstants(
        memory_page_size=1,
        memory_max_record_length=16200000,
        memory_min_record_length=1,
    )

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################
    @cached_property
    def source_channel(self) -> "MappingProxyType[str, AWGSourceChannel]":
        """Mapping of channel names to AWG5KSourceChannel objects."""
        channel_map: Dict[str, AWG5KSourceChannel] = {}
        for channel_name in self.all_channel_names_list:
            channel_map[channel_name] = AWG5KSourceChannel(self, channel_name)
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

        # if DIR output path is disconnected
        if output_signal_path == self.OutputSignalPath.DCA:
            amplitude_range = ParameterBounds(lower=20.0e-3, upper=4.5)
            offset_range = ParameterBounds(lower=-2.25, upper=2.25)
        # otherwise the DIR output path is connected
        else:
            amplitude_range = ParameterBounds(lower=20.0e-3, upper=0.6)
            offset_range = ParameterBounds(lower=-0.0, upper=0.0)

        # AWG(Arbitrary Waveform Generator)5(Series)0x(.6 + .6x GS/s)x(x Channels)z(Model)
        # AWG5012B means the sample rate max is 1.2 GHz, a AWG5002B would have a 600 MHz max
        sample_rate_range = ParameterBounds(
            lower=10.0e6, upper=600.0e6 + (600.0e6 * int(self.model[5]))
        )
        return amplitude_range, offset_range, sample_rate_range


class AWG5KSourceChannel(AWGSourceChannel):
    """AWG5K signal source channel composite."""

    _awg: AWG5K

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
        if not float(self._awg.query(f"AWGCONTROL:DOUTPUT{self.num}:STATE?")):
            # Can only set offset when then output state is 0.
            self._awg.set_if_needed(
                f"{self.name}:VOLTAGE:OFFSET",
                value,
                tolerance=absolute_tolerance,
            )
        elif value:
            # No error is raised when 0 is the offset value and the output signal path
            # is in a state where offset cannot be set.
            offset_error = (
                f"The offset can only be set on {self._awg.model} with an output signal path of "
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
        if not value or value == self._awg.OutputSignalPath.DCA:
            # Translate DCA to output state of 0.
            output_state = 0
        elif value == self._awg.OutputSignalPath.DIR:
            # Translate DIR to output state of 1.
            output_state = 1
        else:
            output_signal_path_error = (
                f"{value.value} is an invalid output signal path for {self._awg.model}."
            )
            raise ValueError(output_signal_path_error)
        self._awg.set_if_needed(f"AWGCONTROL:DOUTPUT{self.num}:STATE", output_state)
