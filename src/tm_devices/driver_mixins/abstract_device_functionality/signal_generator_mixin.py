"""A mixin class providing common methods and attributes for signal generators."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, Literal, NamedTuple, Optional, Type, TypeVar, Union

from tm_devices.driver_mixins.shared_implementations._extension_mixin import (
    _ExtendableMixin,  # pyright: ignore[reportPrivateUsage]
)
from tm_devices.helpers.enums import (
    LoadImpedanceAFG,
    SignalGeneratorFunctionBase,
    SignalGeneratorOutputPathsBase,
)

_SourceDeviceConstantsTypeVar = TypeVar(
    "_SourceDeviceConstantsTypeVar", bound="SourceDeviceConstants"
)
_SignalGeneratorFunctionsTypeVar = TypeVar(
    "_SignalGeneratorFunctionsTypeVar", bound="SignalGeneratorFunctionBase"
)


class ParameterBounds(NamedTuple):
    """The upper and lower bounds of a parameter."""

    lower: float
    upper: float


@dataclass(frozen=True)
class ExtendedSourceDeviceConstants:
    """Class to hold source device constants."""

    amplitude_range: ParameterBounds
    offset_range: ParameterBounds
    frequency_range: ParameterBounds
    sample_rate_range: ParameterBounds
    square_duty_cycle_range: Optional[ParameterBounds] = None
    pulse_width_range: Optional[ParameterBounds] = None
    ramp_symmetry_range: Optional[ParameterBounds] = None


@dataclass(frozen=True)
class SourceDeviceConstants:
    """Class to hold source device constants."""

    memory_page_size: int
    memory_max_record_length: int
    memory_min_record_length: int
    functions: Type[SignalGeneratorFunctionBase]


class SignalGeneratorMixin(
    _ExtendableMixin, Generic[_SignalGeneratorFunctionsTypeVar, _SourceDeviceConstantsTypeVar], ABC
):
    """A mixin class which adds methods and properties for generating signals."""

    @staticmethod
    def _validate_generated_function(
        function: Union[str, _SignalGeneratorFunctionsTypeVar],
    ) -> _SignalGeneratorFunctionsTypeVar:
        """Validate the functions within the waveform generation method.

        Args:
            function: The function type to verify.

        Raises:
            TypeError: Tells the user that they are using an incorrect function type.
        """
        if not isinstance(function, SignalGeneratorFunctionBase):
            msg = (
                "Generate Waveform does not accept functions as non Enums. "
                "Please use 'source_device_constants.functions'."
            )
            raise TypeError(msg)
        return function

    @property
    @abstractmethod
    def source_device_constants(self) -> _SourceDeviceConstantsTypeVar:
        """The constants defining what functions and memory sizes are allowed for the device."""

    @abstractmethod
    def generate_function(  # noqa: PLR0913
        self,
        frequency: float,
        function: _SignalGeneratorFunctionsTypeVar,
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
        raise NotImplementedError

    @abstractmethod
    def setup_burst(  # noqa: PLR0913
        self,
        frequency: float,
        function: _SignalGeneratorFunctionsTypeVar,
        amplitude: float,
        offset: float,
        burst_count: int,
        channel: str = "all",
        output_signal_path: Optional[SignalGeneratorOutputPathsBase] = None,
        termination: Literal["FIFTY", "HIGHZ"] = "FIFTY",
        duty_cycle: float = 50.0,
        polarity: Literal["NORMAL", "INVERTED"] = "NORMAL",
        symmetry: float = 50.0,
    ) -> None:
        """Set up the device for sending a burst of waveforms given the following parameters.

        Args:
            frequency: The frequency of the waveform to generate.
            function: The function to generate.
            amplitude: The amplitude of the signal to generate.
            offset: The offset of the signal to generate.
            burst_count: The number of wavelengths to be generated.
            channel: The channel number to output the signal from, or 'all'.
            output_signal_path: The output signal path of the specified channel.
            termination: The impedance to set the channel to.
            duty_cycle: The duty cycle to set the signal to.
            polarity: The polarity to set the signal to.
            symmetry: The symmetry to set the signal to, only applicable to certain functions.
        """
        raise NotImplementedError

    @abstractmethod
    def generate_burst(self) -> None:
        """Generate a burst of waveforms by forcing trigger."""
        raise NotImplementedError

    @abstractmethod
    def get_waveform_constraints(
        self,
        function: Optional[SignalGeneratorFunctionBase] = None,
        waveform_length: Optional[int] = None,
        frequency: Optional[float] = None,
        output_signal_path: str = "DIR",
        load_impedance: LoadImpedanceAFG = LoadImpedanceAFG.HIGHZ,
    ) -> ExtendedSourceDeviceConstants:
        """Get the constraints that restrict the waveform to certain parameter ranges.

        Args:
            function: The function that needs to be generated.
            waveform_length: The length of the waveform if no function or arbitrary is provided.
            frequency: The frequency of the waveform that needs to be generated.
            output_signal_path: The output signal path that was set on the channel.
            load_impedance: The suggested impedance on the source.
        """
        raise NotImplementedError
