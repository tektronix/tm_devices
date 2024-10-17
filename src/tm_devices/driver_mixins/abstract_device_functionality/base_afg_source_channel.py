"""Base AFG source channel module."""

from abc import ABC, abstractmethod
from typing import Literal

from tm_devices.driver_mixins.abstract_device_functionality.base_source_channel import (
    BaseSourceChannel,
)
from tm_devices.driver_mixins.device_control import PIControl
from tm_devices.helpers.enums import SignalGeneratorFunctionBase


class BaseAFGSourceChannel(BaseSourceChannel, ABC):
    """Base AFG source channel."""

    def __init__(self, pi_control: PIControl, channel_name: str) -> None:
        """Create an AFG source channel.

        Args:
            pi_control: A PI device.
            channel_name: The channel name for the AFG source channel.
        """
        super().__init__(pi_control=pi_control, channel_name=channel_name)

    @abstractmethod
    def set_function_properties(  # noqa: PLR0913
        self,
        frequency: float,
        function: SignalGeneratorFunctionBase,
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
        raise NotImplementedError

    @abstractmethod
    def set_burst_count(self, value: int) -> None:
        """Set the number of wavelengths to be generated when the source channel is set to burst.

        Args:
            value: The number of wavelengths to be generated within [1, 1000000].
        """
        raise NotImplementedError

    @abstractmethod
    def set_frequency(self, value: float, absolute_tolerance: float = 0) -> None:
        """Set the frequency on the source channel.

        Args:
            value: The frequency value to set.
            absolute_tolerance: The acceptable difference between two floating point values.
        """
        raise NotImplementedError

    @abstractmethod
    def set_function(self, value: SignalGeneratorFunctionBase) -> None:
        """Set the function to output on the source channel.

        Args:
            value: The name of the function to output.
        """
        raise NotImplementedError

    @abstractmethod
    def set_ramp_symmetry(self, value: float) -> None:
        """Set the symmetry of the ramp waveform on the source channel.

        Args:
            value: The symmetry value to set within [0, 100].
        """
        raise NotImplementedError

    @abstractmethod
    def setup_burst_waveform(self, burst_count: int) -> None:
        """Prepare the source channel for a burst waveform.

        Args:
            burst_count: The number of wavelengths to be generated.
        """
        raise NotImplementedError
