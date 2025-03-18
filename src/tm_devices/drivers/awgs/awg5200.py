"""AWG5200 device driver module."""

from pathlib import Path
from types import MappingProxyType
from typing import cast, Dict, Literal, Optional, Tuple

from tm_devices.commands import AWG5200Mixin
from tm_devices.drivers.awgs.awg import (
    AWG,
    AWGSourceChannel,
    AWGSourceDeviceConstants,
    ParameterBounds,
)
from tm_devices.drivers.device import family_base_class
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813
from tm_devices.helpers import (
    SASSetWaveformFileTypes,
)
from tm_devices.helpers.enums import (
    SignalGeneratorFunctionsAWG,
    SignalGeneratorOutputPaths5200,
    SignalGeneratorOutputPathsBase,
)


@family_base_class
class AWG5200(AWG5200Mixin, AWG):
    """AWG5200 device driver."""

    OutputSignalPath = SignalGeneratorOutputPaths5200

    _DEVICE_CONSTANTS = AWGSourceDeviceConstants(
        memory_page_size=1,
        memory_max_record_length=16200000,
        memory_min_record_length=1,
    )
    sample_waveform_set_file = (
        "C:\\Program Files\\Tektronix\\AWG5200\\Samples\\AWG5k7k Predefined Waveforms.awgx"
    )

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################
    @cached_property
    def source_channel(self) -> "MappingProxyType[str, AWGSourceChannel]":
        """Mapping of channel names to AWG5200SourceChannel objects."""
        channel_map: Dict[str, AWG5200SourceChannel] = {}
        for channel_name in self.all_channel_names_list:
            channel_map[channel_name] = AWG5200SourceChannel(self, channel_name)
        return MappingProxyType(channel_map)

    ################################################################################################
    # Public Methods
    ################################################################################################
    def load_waveform_set(self, waveform_set_file: Optional[str] = None) -> None:
        """Load a waveform set into the memory of the AWG.

        Arguments:
            waveform_set_file: The waveform set file to load
                (The default is defined in the ``sample_wave_file`` attribute).
        """
        self._load_waveform_or_set(waveform_set_file=waveform_set_file, waveform_name=None)

    def load_waveform_from_set(
        self,
        waveform_name: str,
        waveform_set_file: Optional[str] = None,
    ) -> None:
        """Load in a specific waveform from a waveform set into the memory of the AWG.

        Arguments:
            waveform_name: The waveform name to load from the waveform set file.
            waveform_set_file: The waveform set file to load
                (The default is defined in the ``sample_wave_file`` attribute).
        """
        self._load_waveform_or_set(waveform_set_file=waveform_set_file, waveform_name=waveform_name)

    def generate_function(  # noqa: PLR0913
        self,
        frequency: float,
        function: SignalGeneratorFunctionsAWG,
        amplitude: float,
        offset: float,
        channel: str = "all",
        output_signal_path: Optional[SignalGeneratorOutputPathsBase] = None,
        termination: Literal["FIFTY", "HIGHZ"] = "FIFTY",
        duty_cycle: float = 50.0,
        polarity: Literal["NORMAL", "INVERTED"] = "NORMAL",
        symmetry: float = 50.0,
    ) -> None:
        """Generate a predefined waveform given the following parameters.

        Args:
            frequency: The frequency of the waveform to generate.
            function: The waveform shape to generate.
            amplitude: The amplitude of the signal to generate.
            offset: The offset of the signal to generate.
            channel: The channel name to output the signal from, or 'all'.
            output_signal_path: The output signal path of the specified channel.
            termination: The impedance this device's ``channel`` expects to see at the received end.
            duty_cycle: The duty cycle percentage within [10.0, 90.0].
            polarity: The polarity to set the signal to.
            symmetry: The symmetry to set the signal to, only applicable to certain functions.
        """
        predefined_name, needed_sample_rate = self._get_predefined_waveform_name(
            frequency, function, output_signal_path, symmetry
        )
        self.generate_waveform(
            needed_sample_rate=needed_sample_rate,
            waveform_name=predefined_name,
            amplitude=amplitude,
            offset=offset,
            channel=channel,
            output_signal_path=output_signal_path,
            termination=termination,
            duty_cycle=duty_cycle,
            polarity=polarity,
            symmetry=symmetry,
        )

    def generate_waveform(  # noqa: PLR0913
        self,
        needed_sample_rate: float,
        waveform_name: str,
        amplitude: float,
        offset: float,
        channel: str = "all",
        output_signal_path: Optional[SignalGeneratorOutputPathsBase] = None,
        termination: Literal["FIFTY", "HIGHZ"] = "FIFTY",  # noqa: ARG002
        duty_cycle: float = 50.0,  # noqa: ARG002
        polarity: Literal["NORMAL", "INVERTED"] = "NORMAL",  # noqa: ARG002
        symmetry: float = 50.0,  # noqa: ARG002
    ) -> None:
        """Generate a waveform given the following parameters.

        Args:
            needed_sample_rate: The required sample rate.
            waveform_name: The name of the waveform to generate.
            amplitude: The amplitude of the signal to generate.
            offset: The offset of the signal to generate.
            channel: The channel name to output the signal from, or 'all'.
            output_signal_path: The output signal path of the specified channel.
            termination: The impedance this device's ``channel`` expects to see at the received end.
            duty_cycle: The duty cycle percentage within [10.0, 90.0].
            polarity: The polarity to set the signal to.
            symmetry: The symmetry to set the signal to, only applicable to certain functions.
        """
        # If the waveform is not in the waveform list, load in the waveform set defined at
        # self.sample_waveform_set_file
        if waveform_name not in self.query("WLISt:LIST?", allow_empty=True).replace('"', "").split(
            ","
        ):
            self.load_waveform_set()
        for channel_name in self._validate_channels(channel):
            self.set_sample_rate(needed_sample_rate)
            source_channel = cast("AWG5200SourceChannel", self.source_channel[channel_name])
            # turn channel off
            self.set_and_check(f"OUTPUT{source_channel.num}:STATE", "0")
            source_channel.set_waveform_properties(
                output_signal_path=output_signal_path,
                waveform_name=waveform_name,
                amplitude=amplitude,
                offset=offset,
            )
            self.set_if_needed(f"OUTPUT{source_channel.num}:STATE", "1")
        # this is an overlapping command
        self.write("AWGCONTROL:RUN")
        self.ieee_cmds.opc()
        # we expect no errors
        self.expect_esr(0)

    def set_sample_rate(self, value: float, absolute_tolerance: Optional[float] = None) -> None:
        """Set the rate at which samples are generated/transmitted.

        Args:
            value: The sample rate to set.
            absolute_tolerance: The acceptable difference between two floating point values.
                                Default value is 0.1% of the provided value.
        """
        if absolute_tolerance is None:
            # Default the absolute tolerance to 0.1% of the provided frequency value
            # due to 32 bit rounding.
            absolute_tolerance = value * 0.001
        # This is an overlapping command for the AWG5200, and will overlap the
        # next command and/or overlap the previous if it is still running.
        self.set_if_needed("CLOCK:SRATE", value, verify_value=False, tolerance=absolute_tolerance)

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
            output_signal_path = self.OutputSignalPath.DCHB
        # Direct Current High Bandwidth with the DC options has 1.5 V amplitude
        if "DC" in self.opt_string and output_signal_path == self.OutputSignalPath.DCHB:
            amplitude_range = ParameterBounds(lower=25.0e-3, upper=1.5)
        # Direct Current High Voltage path connected has an even higher amplitude, 5 V
        elif output_signal_path == self.OutputSignalPath.DCHV:
            amplitude_range = ParameterBounds(lower=10.0e-3, upper=5.0)
        # Else, the upper bound is 750 mV
        else:
            amplitude_range = ParameterBounds(lower=25.0e-3, upper=750.0e-3)

        offset_range = ParameterBounds(lower=-2.0, upper=2.0)
        # option is the sample rate in hundreds of Mega Hertz
        max_sample_rate = 25.0 if "25" in self.opt_string else 50.0
        # option 50 would have 5.0 GHz, option 2.5 would have 2.5 GHz
        sample_rate_range = ParameterBounds(lower=300.0, upper=max_sample_rate * 100.0e6)

        return amplitude_range, offset_range, sample_rate_range

    def _load_waveform_or_set(
        self,
        waveform_set_file: Optional[str] = None,
        waveform_name: Optional[str] = None,
    ) -> None:
        """Load in a waveform set or a specific waveform from a waveform set into memory.

        Arguments:
            waveform_set_file: The waveform set file to load.
                (The default is defined in the ``sample_wave_file`` attribute).
            waveform_name: The waveform name to load from the waveform set file.
        """
        # This function is identical to the one in the AWG70KA.
        if not waveform_set_file:
            waveform_set_file = self.sample_waveform_set_file
        waveform_file_type = Path(waveform_set_file).suffix.lower()
        try:
            SASSetWaveformFileTypes(waveform_file_type)
            if not waveform_name:
                self.write(f'MMEMORY:OPEN:SASSET "{waveform_set_file}"', opc=True)
            else:
                self.write(
                    f'MMEMORY:OPEN:SASSET:WAVEFORM "{waveform_set_file}", "{waveform_name}"',
                    opc=True,
                )
        except ValueError as err:
            waveform_file_type_error = (
                f"{waveform_file_type} is an invalid waveform file extension."
            )
            raise ValueError(waveform_file_type_error) from err

        self.expect_esr(0)


class AWG5200SourceChannel(AWGSourceChannel):
    """AWG5200 signal source channel composite."""

    _awg: AWG5200

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Public Methods
    ################################################################################################
    def load_waveform(self, waveform_name: str) -> None:
        """Load in a waveform from the waveform list to the source channel.

        Args:
            waveform_name: The name of the waveform to load.
        """
        self._awg.ieee_cmds.opc()
        self._awg.set_if_needed(f"{self.name}:WAVEFORM", f'"{waveform_name}"', allow_empty=True)

    def set_offset(self, value: float, absolute_tolerance: float = 0) -> None:
        """Set the offset on the source channel.

        Args:
            value: The offset value to set.
            absolute_tolerance: The acceptable difference between two floating point values.
        """
        self._awg.set_if_needed(
            f"{self.name}:VOLTAGE:OFFSET",
            value,
            tolerance=absolute_tolerance,
        )

    def set_output_signal_path(
        self, value: Optional[SignalGeneratorOutputPathsBase] = None
    ) -> None:
        """Set the output signal path on the source channel.

        Args:
            value: The output signal path.
        """
        if not value:
            value = self._awg.OutputSignalPath.DCHB
        if value not in self._awg.OutputSignalPath:
            output_signal_path_error = (
                f"{value.value} is an invalid output signal path for {self._awg.model}."
            )
            raise ValueError(output_signal_path_error)
        self._awg.set_if_needed(f"OUTPUT{self.num}:PATH", value.value)
