"""Base DMM75xx device driver module."""

from abc import ABC
from typing import Tuple

import pyvisa as visa

from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.pi.digital_multimeters.digital_multimeter import DigitalMultimeter
from tm_devices.drivers.pi.ieee488_2_commands import LegacyTSPIEEE4882Commands
from tm_devices.helpers import DeviceConfigEntry


@family_base_class
class DMM75xx(DigitalMultimeter, ABC):
    """Base DMM75xx device driver."""

    _IEEE_COMMANDS_CLASS = LegacyTSPIEEE4882Commands

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(  # pylint: disable=useless-parent-delegation
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create a DMM75xx device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        # NOTE: This method must be defined for the documentation to properly generate
        super().__init__(config_entry, verbose, visa_resource)

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
        return self._ieee_cmds  # pyright: ignore[reportReturnType]

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
