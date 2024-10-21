"""AFG31K device driver module."""

from typing import Optional, Tuple

from tm_devices.drivers.afgs.afg3k import (
    AFG,
    AFGSourceDeviceConstants,
    LoadImpedanceAFG,
    ParameterBounds,
    SignalGeneratorFunctionsAFG,
)


class AFG31K(AFG):
    """AFG31K device driver."""

    _DEVICE_CONSTANTS = AFGSourceDeviceConstants(
        memory_page_size=2,
        memory_max_record_length=131072,
        memory_min_record_length=2,
    )

    _PRE_15_FREQ_THRESHOLD_1 = 60.0e6
    _PRE_15_FREQ_THRESHOLD_2 = 80.0e6
    _POST_15_FREQ_THRESHOLD = 200.0e6
    _16KB_THRESHOLD = 16 * 1024

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################

    ################################################################################################
    # Public Methods
    ################################################################################################

    ################################################################################################
    # Private Methods
    ################################################################################################
    @staticmethod
    def _get_driver_specific_multipliers(model_number: str) -> Tuple[float, float, float]:
        """Get multipliers for frequency dependent on the function.

        Args:
            model_number: The numbers not pertaining to series or channel count in the name.
                ie: AFG31 ->25<- 1

        Returns:
            The necessary values to multiply the frequency by dependent on the function.
        """
        # the square wave constraints are difference for model 25
        square_wave_multiplier = 0.64 if model_number == "25" else 0.8

        # other wave constraints are 1% of the SIN wave constraints, except for models 02 and 05
        if model_number == "02":
            other_wave_multiplier = 0.025
        elif model_number == "05":
            other_wave_multiplier = 0.016
        else:
            other_wave_multiplier = 0.01

        # the arbitrary waveform constraints are half og the SIN wave constraints
        arbitrary_multiplier = 0.5
        return square_wave_multiplier, other_wave_multiplier, arbitrary_multiplier

    # pylint: disable=too-many-locals
    def _get_series_specific_constraints(
        self,
        function: SignalGeneratorFunctionsAFG,
        waveform_length: Optional[int] = None,
        frequency: Optional[float] = None,
        load_impedance: LoadImpedanceAFG = LoadImpedanceAFG.HIGHZ,
    ) -> Tuple[ParameterBounds, ParameterBounds, ParameterBounds, ParameterBounds]:
        """Get constraints which are dependent on the model series and parameters.

        Args:
            function: The function that needs to be generated.
            waveform_length: The length of the waveform if no function or arbitrary is provided.
            frequency: The frequency of the waveform that needs to be generated.
            load_impedance: The suggested impedance on the source.

        Returns:
            Ranges for amplitude, frequency, offset, and sample rate.
        """
        # the model number is the third and fourth digit of the model serial, ex. 31(25)2
        model_number = self.model[5:7]

        load_impedance_multiplier = 1.0 if load_impedance == LoadImpedanceAFG.HIGHZ else 0.5

        freq_base = 10.0e6

        lower_amplitude = 2.0e-3
        # the higher the frequency, the lower the maximum amplitude can be
        if model_number in {"02", "05", "10"}:
            if frequency and frequency <= self._PRE_15_FREQ_THRESHOLD_1:
                upper_amplitude = 20.0
            elif frequency and frequency <= self._PRE_15_FREQ_THRESHOLD_2:
                upper_amplitude = 16.0
            else:
                upper_amplitude = 12.0
            # offset bound is always 10.0
            offset_bound = 10.0
        else:
            upper_amplitude = (
                10.0 if (frequency and frequency <= self._POST_15_FREQ_THRESHOLD) else 8.0
            )
            # offset bound is always 5.0
            offset_bound = 5.0

        # special case for 02
        model_multiplier = 2.5 if "02" in model_number else float(model_number)

        sample_rate = 250.0e6
        # if the waveform length is less than 16 KB, than the AFG can use a higher sample rate
        if waveform_length and waveform_length < self._16KB_THRESHOLD:
            if model_number in {"05", "10"}:
                sample_rate = 1.0e9
            elif model_number in {"15", "25"}:
                sample_rate = 2.0e9

        square_mult, other_mult, arb_mult = self._get_driver_specific_multipliers(model_number)
        low_freq_range = 1.0e-6
        # the maximum frequency of the SIN wave depends on the model mumber
        if function.name in {SignalGeneratorFunctionsAFG.SIN.name}:
            high_freq_range = model_multiplier * freq_base
        # each waveform has a maximum frequency which is a multiple of SIN wave constraints
        elif function.name == SignalGeneratorFunctionsAFG.ARBITRARY.name:
            high_freq_range = model_multiplier * arb_mult * freq_base
        elif function.name in {
            SignalGeneratorFunctionsAFG.PULSE.name,
            SignalGeneratorFunctionsAFG.SQUARE.name,
        }:
            high_freq_range = model_multiplier * square_mult * freq_base
        else:
            high_freq_range = model_multiplier * other_mult * freq_base

        # load impedance can double the amplitude and offset range
        amplitude_range = ParameterBounds(
            lower=lower_amplitude * load_impedance_multiplier,
            upper=upper_amplitude * load_impedance_multiplier,
        )

        frequency_range = ParameterBounds(
            lower=low_freq_range,
            upper=high_freq_range,
        )

        offset_range = ParameterBounds(
            lower=-offset_bound * load_impedance_multiplier,
            upper=offset_bound * load_impedance_multiplier,
        )

        sample_rate_range = ParameterBounds(lower=sample_rate, upper=sample_rate)

        return amplitude_range, frequency_range, offset_range, sample_rate_range

    def _reboot(self) -> None:
        """Reboot the device."""
        self.write("SYSTem:RESTart")
