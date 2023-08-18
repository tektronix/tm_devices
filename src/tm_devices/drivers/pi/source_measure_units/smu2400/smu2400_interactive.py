"""SMU2400Interactive device driver module."""

from abc import ABC
from functools import cached_property
from typing import Tuple, Union

from tm_devices.commands import (
    SMU2450Commands,
    SMU2460Commands,
    SMU2461Commands,
    SMU2470Commands,
)
from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.pi._ieee488_2_commands import LegacyTSPIEEE4882Commands
from tm_devices.drivers.pi.source_measure_units.source_measure_unit import SourceMeasureUnit


@family_base_class
class SMU2400Interactive(SourceMeasureUnit, ABC):
    """Base SMU2400Interactive device driver."""

    _IEEE_COMMANDS_CLASS = LegacyTSPIEEE4882Commands

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################
    @property
    def all_channel_names_list(self) -> Tuple[str, ...]:
        """Return a tuple containing all the channel names."""
        return tuple(f"OUTPUT{x+1}" for x in range(self.total_channels))

    @property
    def commands(
        self,
    ) -> Union[SMU2450Commands, SMU2460Commands, SMU2461Commands, SMU2470Commands]:
        """Return the device commands."""
        return self._commands  # pragma: no cover

    @property
    def ieee_cmds(self) -> LegacyTSPIEEE4882Commands:
        """Return an internal class containing methods for the standard IEEE 488.2 command set."""
        return self._ieee_cmds  # type: ignore

    @cached_property
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""
        return 1

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

        if not (err_count := int(self.query("print(eventlog.getcount(eventlog.SEV_ERROR))"))):
            result_allev = True
        else:
            allev_result_list = [self.query("print(eventlog.next())") for _ in range(err_count)]
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
