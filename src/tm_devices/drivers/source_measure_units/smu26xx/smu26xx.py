"""SMU Model 26xx device driver module."""

import string

from abc import ABC
from typing import Tuple, Union

from tm_devices.commands import (
    SMU2601BCommands,
    SMU2601BPulseCommands,
    SMU2602BCommands,
    SMU2604BCommands,
    SMU2606BCommands,
    SMU2611BCommands,
    SMU2612BCommands,
    SMU2614BCommands,
    SMU2634BCommands,
    SMU2635BCommands,
    SMU2636BCommands,
    SMU2651ACommands,
    SMU2657ACommands,
)
from tm_devices.driver_mixins.device_control import TSPControl
from tm_devices.driver_mixins.shared_implementations.common_tsp_error_check_mixin import (
    CommonTSPErrorCheckMixin,
)
from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.source_measure_units.source_measure_unit import SourceMeasureUnit
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


@family_base_class
class SMU26xx(CommonTSPErrorCheckMixin, TSPControl, SourceMeasureUnit, ABC):
    """Base SMU26xx device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################
    @property
    def all_channel_names_list(self) -> Tuple[str, ...]:
        """Return a tuple containing all the channel names."""
        return tuple(string.ascii_lowercase[: self.total_channels])  # pylint: disable=invalid-slice-index

    @cached_property
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""
        # Grab the total channel count based on whether the last digit in the model is even/odd
        return 2 if (not int([x for x in self.model if x.isdigit()][-1]) % 2) else 1

    @cached_property
    def commands(
        self,
    ) -> Union[
        SMU2601BCommands,
        SMU2602BCommands,
        SMU2604BCommands,
        SMU2606BCommands,
        SMU2611BCommands,
        SMU2612BCommands,
        SMU2614BCommands,
        SMU2634BCommands,
        SMU2635BCommands,
        SMU2636BCommands,
        SMU2601BPulseCommands,
        SMU2651ACommands,
        SMU2657ACommands,
    ]:
        """Return the device commands."""
        return super().commands

    ################################################################################################
    # Public Methods
    ################################################################################################

    ################################################################################################
    # Private Methods
    ################################################################################################
