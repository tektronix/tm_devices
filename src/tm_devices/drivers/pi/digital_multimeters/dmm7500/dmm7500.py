"""Base DMM7500 device driver module."""
from abc import ABC
from typing import Tuple

from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.pi._ieee488_2_commands import LegacyTSPIEEE4882Commands
from tm_devices.drivers.pi.digital_multimeters.digital_multimeter import DigitalMultimeter


@family_base_class
class DMM7500(DigitalMultimeter, ABC):
    """Base DMM7500 device driver."""

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
        return ()

    @property
    def ieee_cmds(self) -> LegacyTSPIEEE4882Commands:
        """Return an internal class containing methods for the standard IEEE 488.2 command set."""
        return self._ieee_cmds  # type: ignore

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
