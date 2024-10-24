"""AFG31K device driver module."""

from typing import Tuple

from tm_devices.commands import AFG3KCMixin
from tm_devices.drivers.afgs.afg3kb import (
    AFG3KB,
)


class AFG3KC(AFG3KCMixin, AFG3KB):  # pyright: ignore[reportIncompatibleVariableOverride]
    """AFG3KC device driver."""

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
    def _get_driver_specific_multipliers(model_number: str) -> Tuple[float, float]:
        """Get multipliers for frequency dependent on the function.

        Args:
            model_number: The numbers not pertaining to series or channel count in the name.
                ie: AFG3 ->25<- 1C

        Returns:
            The necessary values to multiply the frequency by dependent on the function.
        """
        # the square wave and other wave constraints are difference for model 02 and 05
        if model_number == "02":
            square_wave_multiplier = 1
            other_wave_multiplier = 0.02
        elif model_number == "05":
            square_wave_multiplier = 0.8
            other_wave_multiplier = 0.016
        else:
            square_wave_multiplier = 0.5
            other_wave_multiplier = 0.01
        return square_wave_multiplier, other_wave_multiplier
