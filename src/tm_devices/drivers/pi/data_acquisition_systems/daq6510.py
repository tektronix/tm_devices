"""DAQ6510 device driver module."""
from functools import cached_property
from typing import Tuple

import pyvisa as visa

from tm_devices.commands import DAQ6510Mixin
from tm_devices.drivers.pi._ieee488_2_commands import LegacyTSPIEEE4882Commands
from tm_devices.drivers.pi.data_acquisition_systems.data_acquisition_system import (
    DataAcquisitionSystem,
)
from tm_devices.helpers import DeviceConfigEntry


class DAQ6510(DAQ6510Mixin, DataAcquisitionSystem):
    """DAQ6510 device driver."""

    _IEEE_COMMANDS_CLASS = LegacyTSPIEEE4882Commands

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create a DAQ6510 device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        super().__init__(config_entry, verbose, visa_resource)

    ################################################################################################
    # Properties
    ################################################################################################
    @property
    def all_channel_names_list(self) -> Tuple[str, ...]:
        """Return a tuple containing all the channel names."""
        return tuple(f"{x+1}" for x in range(self.total_channels))

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
