"""SMU Model 2600 device driver module."""
import string

from abc import ABC
from functools import cached_property
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
from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.pi.source_measure_units.source_measure_unit import SourceMeasureUnit


@family_base_class
class SMU2600(SourceMeasureUnit, ABC):
    """Base SMU2600 device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################
    @property
    def all_channel_names_list(self) -> Tuple[str, ...]:
        """Return a tuple containing all the channel names."""
        return tuple(string.ascii_lowercase[: self.total_channels])

    @cached_property
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""
        # Grab the total channel count based on whether the last digit in the model is even/odd
        return 2 if (not int([x for x in self.model if x.isdigit()][-1]) % 2) else 1

    @property
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
        return self._commands  # pragma: no cover

    ################################################################################################
    # Public Methods
    ################################################################################################
    def get_eventlog_status(self) -> Tuple[bool, str]:
        """Help function for getting the eventlog status.

        Returns:
            Boolean indicating no error, String containing concatenated contents of event log.
        """
        result_allev = False
        allev_result_str = '0,"No events to report - queue empty"'

        # instrument returns exponential numbers so converting to float before int
        # TODO: switch to auto-generated command once SMU2601B-PULSE is ready
        if not (err_count := int(float(self.query("print(errorqueue.count)")))):
            result_allev = True
        else:
            allev_result_list = [self.query("print(errorqueue.next())") for _ in range(err_count)]
            allev_result_str = ",".join(allev_result_list)
        return result_allev, allev_result_str

    ################################################################################################
    # Private Methods
    ################################################################################################
    def _reboot(self) -> None:
        """Perform the actual rebooting code."""
        # TODO: implement
        raise NotImplementedError(
            f"``.reboot()`` is not yet implemented for the {self.__class__.__name__} driver"
        )
