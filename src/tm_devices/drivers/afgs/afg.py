"""Base AFG device driver module."""

import re

from abc import ABC, abstractmethod
from dataclasses import dataclass
from types import MappingProxyType
from typing import Dict, Literal, Optional, Tuple, Type, Union

from tm_devices.driver_mixins.abstract_device_functionality.base_afg_source_channel import (
    BaseAFGSourceChannel,
)
from tm_devices.driver_mixins.abstract_device_functionality.signal_generator_mixin import (
    ExtendedSourceDeviceConstants,
    ParameterBounds,
    SourceDeviceConstants,
)
from tm_devices.driver_mixins.device_control import PIControl
from tm_devices.driver_mixins.shared_implementations._tektronix_pi_afg_awg_mixin import (
    _TektronixPIAFGAWGMixin,  # pyright: ignore[reportPrivateUsage]
)
from tm_devices.drivers.device import Device, family_base_class
from tm_devices.helpers import DeviceTypes, LoadImpedanceAFG
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813
from tm_devices.helpers.enums import (
    SignalGeneratorFunctionsAFG,
    SignalGeneratorOutputPathsBase,
)


@dataclass(frozen=True)
class AFGSourceDeviceConstants(SourceDeviceConstants):
    """Class to hold source device constants."""

    functions: Type[SignalGeneratorFunctionsAFG] = SignalGeneratorFunctionsAFG


# NOTE: Currently all AFGs are controlled via PI, hence the usage of the PIControl mixin here. If
# this changes in the future, the class inheritance structure may need to be modified and the
# control class inheritance responsibility moved to the newly created Family Base Classes. The other
# option would be to create two abstract AFG parent classes and two distinct AFGSourceChannel
# classes, with one set using the PIControl mixin and one set using another control mixin.
@family_base_class
class AFG(_TektronixPIAFGAWGMixin, PIControl, Device, ABC):
    """Base AFG device driver."""

    ################################################################################################
    # Properties
    ################################################################################################
    @cached_property
    def device_type(self) -> str:
        """Return a string representing the device type."""
        return DeviceTypes.AFG.value

    @cached_property
    def source_channel(self) -> "MappingProxyType[str, AFGSourceChannel]":
        """Mapping of channel names to AFGSourceChannel objects."""
        channel_map: Dict[str, AFGSourceChannel] = {}
        for channel_name in self.all_channel_names_list:
            channel_map[channel_name] = AFGSourceChannel(self, channel_name)
        return MappingProxyType(channel_map)

    @property
    def source_device_constants(self) -> AFGSourceDeviceConstants:
        """The constants defining what functions and memory sizes are allowed for the device."""
        return self._DEVICE_CONSTANTS  # type: ignore[attr-defined]

    @cached_property
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""
        if match := re.match(r"AFG\d+(\d)", self.model):
            return int(match.group(1))
        return 0  # pragma: no cover

    ################################################################################################
    # Public Methods
    ################################################################################################
    def generate_function(  # noqa: PLR0913
        self,
        frequency: float,
        function: SignalGeneratorFunctionsAFG,
        amplitude: float,
        offset: float,
        channel: str = "all",
        output_signal_path: Optional[SignalGeneratorOutputPathsBase] = None,
        termination: Literal["FIFTY", "HIGHZ"] = "FIFTY",
        duty_cycle: float = 50.0,
        polarity: Literal["NORMAL", "INVERTED"] = "NORMAL",
        symmetry: float = 100.0,
    ) -> None:
        """Generate a predefined waveform given the following parameters.

        Args:
            frequency: The frequency of the waveform to generate.
            function: The waveform shape to generate.
            amplitude: The amplitude of the signal to generate.
            offset: The offset of the signal to generate.
            channel: The channel name to output the signal from, or 'all'.
            output_signal_path: Unused in this class.
            termination: The impedance this device's ``channel`` expects to see at the received end.
            duty_cycle: The duty cycle percentage within [0.4, 99.6].
            polarity: The polarity to set the signal to.
            symmetry: The symmetry to set the signal to, only applicable to certain functions.
        """
        del output_signal_path  # Not used in AFGs.
        self._validate_generated_function(function)

        # Generate the waveform on the given channel
        for channel_name in self._validate_channels(channel):
            source_channel = self.source_channel[channel_name]
            # Temporarily turn off this channel
            source_channel.set_state(0)
            source_channel.set_function_properties(
                frequency=frequency,
                function=function,
                amplitude=amplitude,
                offset=offset,
                burst_count=0,
                termination=termination,
                duty_cycle=duty_cycle,
                polarity=polarity,
                symmetry=symmetry,
            )
            # Turn on the channel
            source_channel.set_state(1)

            # Check if burst is enabled on any channel of the AFG
            burst_state = False
            for burst_channel in range(1, self.total_channels + 1):
                if self.query(f"SOURCE{burst_channel}:BURST:STATE?") == "1":
                    burst_state = True
            if (
                self.total_channels > 1  # pylint: disable=comparison-with-callable
                and function.value != SignalGeneratorFunctionsAFG.DC.value
                and not burst_state
            ):
                # Initiate a phase sync (between CH 1 and CH 2 output waveforms on two channel AFGs)
                self.source_channel["SOURCE1"].initiate_phase_sync()
            # Check for system errors
            self.expect_esr(0)

    def setup_burst(  # noqa: PLR0913
        self,
        frequency: float,
        function: SignalGeneratorFunctionsAFG,
        amplitude: float,
        offset: float,
        burst_count: int,
        channel: str = "all",
        output_signal_path: Optional[SignalGeneratorOutputPathsBase] = None,
        termination: Literal["FIFTY", "HIGHZ"] = "FIFTY",
        duty_cycle: float = 50.0,
        polarity: Literal["NORMAL", "INVERTED"] = "NORMAL",
        symmetry: float = 100.0,
    ) -> None:
        """Set up the AFG for sending a burst of waveforms given the following parameters.

        Args:
            frequency: The frequency of the waveform to generate.
            function: The waveform shape to generate.
            amplitude: The amplitude of the signal to generate.
            offset: The offset of the signal to generate.
            burst_count: The number of wavelengths to be generated.
            channel: The channel name to output the signal from, or 'all'.
            output_signal_path: Unused in this class.
            termination: The impedance this device's ``channel`` expects to see at the received end.
            duty_cycle: The duty cycle percentage within [0.4, 99.6].
            polarity: The polarity to set the signal to.
            symmetry: The symmetry to set the signal to, only applicable to certain functions.
        """
        del output_signal_path  # Not used in AFGs.
        self._validate_generated_function(function)
        # Generate the waveform on the given channel
        for channel_name in self._validate_channels(channel):
            source_channel = self.source_channel[channel_name]
            source_channel.set_function_properties(
                frequency=frequency,
                function=function,
                amplitude=amplitude,
                offset=offset,
                burst_count=burst_count,
                termination=termination,
                duty_cycle=duty_cycle,
                polarity=polarity,
                symmetry=symmetry,
            )
            source_channel.set_state(1)

    def generate_burst(self) -> None:
        """Generate a burst of waveforms by forcing trigger."""
        self.write("*TRG")
        self.expect_esr(0)

    def get_waveform_constraints(  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        function: Optional[SignalGeneratorFunctionsAFG] = None,
        waveform_length: Optional[int] = None,
        frequency: Optional[float] = None,
        output_signal_path: Optional[SignalGeneratorOutputPathsBase] = None,
        load_impedance: LoadImpedanceAFG = LoadImpedanceAFG.HIGHZ,
    ) -> ExtendedSourceDeviceConstants:
        """Get the constraints that restrict the waveform to certain parameter ranges.

        Args:
            function: The function that needs to be generated.
            waveform_length: The length of the waveform if no function or arbitrary is provided.
            frequency: The frequency of the waveform that needs to be generated.
            output_signal_path: Unused in this class.
            load_impedance: The suggested impedance on the source.

        Returns:
            A Named Tuple containing a set of parameters and their restricted bounds.
        """
        del output_signal_path

        if not function:
            msg = "AFGs must have a function defined."
            raise ValueError(msg)
        (
            amplitude_range,
            frequency_range,
            offset_range,
            sample_rate_range,
        ) = self._get_series_specific_constraints(
            function, waveform_length, frequency, load_impedance
        )

        return ExtendedSourceDeviceConstants(
            amplitude_range=amplitude_range,
            frequency_range=frequency_range,
            offset_range=offset_range,
            sample_rate_range=sample_rate_range,
        )

    ################################################################################################
    # Private Methods
    ################################################################################################
    @abstractmethod
    def _get_series_specific_constraints(
        self,
        function: SignalGeneratorFunctionsAFG,
        waveform_length: Optional[int] = None,
        frequency: Optional[float] = None,
        load_impedance: LoadImpedanceAFG = LoadImpedanceAFG.HIGHZ,
    ) -> Tuple[ParameterBounds, ParameterBounds, ParameterBounds, ParameterBounds]:
        """Get constraints which are dependent on the model series.

        Args:
            function: The function that needs to be generated.
            waveform_length: The length of the waveform if no function or arbitrary is provided.
            frequency: The frequency of the waveform that needs to be generated.
            load_impedance: The suggested impedance on the source.

        Returns:
            Ranges for amplitude, frequency, offset, and sample rate.
        """


class AFGSourceChannel(BaseAFGSourceChannel):
    """AFG signal source channel composite."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(self, afg: AFG, channel_name: str) -> None:
        """Create an AFG source channel.

        Args:
            afg: An AFG.
            channel_name: The channel name for the AFG source channel.
        """
        super().__init__(pi_control=afg, channel_name=channel_name)
        self._afg = afg

    ################################################################################################
    # Public Methods
    ################################################################################################
    def initiate_phase_sync(self) -> None:
        """Initialize a phase sync between SOURCE1 and SOURCE2 on the device.

        Does the same operation if called on SOURCE1 or SOURCE2.
        """
        self._afg.write(f"{self.name}:PHASE:INITIATE")

    def set_function_properties(  # noqa: PLR0913  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        frequency: float,
        function: SignalGeneratorFunctionsAFG,
        amplitude: float,
        offset: float,
        burst_count: int = 0,
        termination: Literal["FIFTY", "HIGHZ"] = "FIFTY",
        duty_cycle: float = 50.0,
        polarity: Literal["NORMAL", "INVERTED"] = "NORMAL",
        symmetry: float = 100.0,
    ) -> None:
        """Set the given parameters on the provided source channel.

        Args:
            frequency: The frequency of the waveform to generate.
            function: The waveform shape to generate.
            amplitude: The amplitude of the signal to generate.
            offset: The offset of the signal to generate.
            burst_count: The number of wavelengths to be generated.
            termination: The impedance this device's ``channel`` expects to see at the received end.
            duty_cycle: The duty cycle percentage within [0.4, 99.6].
            polarity: The polarity to set the signal to.
            symmetry: The symmetry to set the signal to, only applicable to certain functions.
        """
        # Termination
        if termination == "FIFTY":
            self.set_impedance(50)
        elif termination == "HIGHZ":  # pragma: no cover
            self.set_impedance("INFINITY")
        else:  # pragma: no cover
            # if termination is MAXIMUM or MINIMUM or INFINITY
            self._afg.set_if_needed(f"OUTPUT{self.num}:IMPEDANCE", termination)
        # Frequency
        self.set_frequency(frequency)
        # Offset
        self.set_offset(offset, absolute_tolerance=0.01)
        if function == SignalGeneratorFunctionsAFG.PULSE:
            # Duty cycle is only valid for pulse
            self.set_pulse_duty_cycle(duty_cycle)
        # Polarity
        self.set_polarity(polarity)
        # Function
        if function == SignalGeneratorFunctionsAFG.RAMP:
            self.set_ramp_symmetry(symmetry)
        self.set_function(function)
        # Amplitude, needs to be after termination so that the amplitude is properly adjusted
        self.set_amplitude(amplitude, absolute_tolerance=0.01)
        if burst_count > 0:
            self.setup_burst_waveform(burst_count)

    def set_amplitude(self, value: float, absolute_tolerance: float = 0) -> None:
        """Set the amplitude on the source channel.

        Args:
            value: The amplitude value to set.
            absolute_tolerance: The acceptable difference between two floating point values.
        """
        self._afg.set_if_needed(
            f"{self._name}:VOLTAGE:AMPLITUDE",
            value,
            tolerance=absolute_tolerance,
        )

    def set_burst_state(self, value: int) -> None:
        """Set the burst mode to ON/OFF (1/0) on the source channel.

        Args:
            value: The burst state.
        """
        if value not in [0, 1]:
            error_message = "Burst state value must be 1 (ON) or 0 (OFF)."
            raise ValueError(error_message)
        self._afg.set_if_needed(f"{self.name}:BURST:STATE", value)

    def set_burst_mode(self, value: Literal["TRIGGERED", "GATED"]) -> None:
        """Set the burst mode on the source channel.

        Args:
            value: The burst mode (Options: "TRIGGERED", "GATED").
        """
        burst_mode_mapping = {
            "TRIGGERED": "TRIG",
            "GATED": "GAT",
        }
        self._afg.set_if_needed(f"{self.name}:BURST:MODE", burst_mode_mapping[value])

    def set_burst_count(self, value: int) -> None:
        """Set the number of wavelengths to be generated when the source channel is set to burst.

        Args:
            value: The number of wavelengths to be generated within [1, 1000000].
        """
        self._afg.set_if_needed(f"{self.name}:BURST:NCYCLES", value)

    def set_frequency(self, value: float, absolute_tolerance: float = 0) -> None:
        """Set the frequency on the source channel.

        Args:
            value: The frequency value to set.
            absolute_tolerance: The acceptable difference between two floating point values.
        """
        self._afg.set_if_needed(
            f"{self._name}:FREQUENCY:FIXED",
            value,
            tolerance=absolute_tolerance,
        )

    def set_function(self, value: SignalGeneratorFunctionsAFG) -> None:  # pyright: ignore[reportIncompatibleMethodOverride]
        """Set the function to output on the source channel.

        Args:
            value: The name of the function to output.
        """
        self._afg.set_if_needed(f"{self.name}:FUNCTION", str(value.value))

    def set_impedance(self, value: Union[float, Literal["INFINITY"]]) -> None:
        """Set the output load impedance on the source channel.

        Args:
            value: The impedance value to set within [1, 10e3] or "INFINITY".
        """
        # The AFG only accepts float values within [1, 10e3] so "INFINITY" must be passed in.
        if value == "INFINITY":  # pragma: no cover
            impedance_value = "INF"
            expected_value = 9.9e37
        else:
            impedance_value = value
            expected_value = value
        self._afg.set_if_needed(
            f"OUTPUT{self.num}:IMPEDANCE", impedance_value, expected_value=expected_value
        )

    def set_offset(self, value: float, absolute_tolerance: float = 0) -> None:
        """Set the offset on the source channel.

        Args:
            value: The offset value to set.
            absolute_tolerance: The acceptable difference between two floating point values.
        """
        self._afg.set_if_needed(
            f"{self._name}:VOLTAGE:OFFSET",
            value,
            tolerance=absolute_tolerance,
        )

    def set_polarity(self, value: Literal["NORMAL", "INVERTED"]) -> None:
        """Set the polarity on the source channel.

        An "INVERTED" polarity inverts the specific output waveform relative to the offset level.

        Args:
            value: The polarity value to set (Options: "NORMAL", "INVERTED").
        """
        polarity_mapping = {
            "NORMAL": "NORM",
            "INVERTED": "INV",
        }
        self._afg.set_if_needed(f"OUTPUT{self.num}:POLARITY", polarity_mapping[value])

    def set_pulse_duty_cycle(self, value: float) -> None:
        """Set the duty cycle of the pulse waveform on the source channel.

        Args:
            value: The duty cycle percentage within [0.4, 99.6].
        """
        self._afg.set_if_needed(f"{self.name}:PULSE:DCYCLE", value)

    def set_ramp_symmetry(self, value: float) -> None:
        """Set the symmetry of the ramp waveform on the source channel.

        Args:
            value: The symmetry value to set within [0, 100].
        """
        self._afg.set_if_needed(f"{self.name}:FUNCTION:RAMP:SYMMETRY", value)

    def set_state(self, value: int) -> None:
        """Set the output state to ON/OFF (1/0) on the source channel.

        Args:
            value: The output state.
        """
        if value not in [0, 1]:
            error_message = "Output state value must be 1 (ON) or 0 (OFF)."
            raise ValueError(error_message)
        self._afg.set_if_needed(f"OUTPUT{self.num}:STATE", value)

    def setup_burst_waveform(self, burst_count: int) -> None:
        """Prepare the source channel for a burst waveform.

        Args:
            burst_count: The number of wavelengths to be generated.
        """
        # set to external as to not burst every millisecond
        self._afg.set_if_needed("TRIGGER:SEQUENCE:SOURCE", "EXT")
        self.set_burst_state(1)
        self.set_burst_mode("TRIGGERED")
        self.set_burst_count(burst_count)
