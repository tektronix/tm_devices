"""MSO2 device driver module."""
from functools import cached_property
from typing import Tuple

import pyvisa as visa

from tm_devices.commands import MSO2Mixin
from tm_devices.drivers.pi.scopes.tekscope.tekscope import TekScope
from tm_devices.helpers import DeviceConfigEntry


class MSO2(MSO2Mixin, TekScope):
    """MSO2 device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create a MSO2 device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        super().__init__(config_entry, verbose, visa_resource)
        # MSO2 takes 15-20 seconds for shutdown, needs more time before opening visa connection.
        self._reboot_quiet_period = 20
        # the DCH1 channel has 16 bit lanes
        self._num_dig_bits_in_ch = 16

    ################################################################################################
    # Public Methods
    ################################################################################################
    @property
    def all_channel_names_list(self) -> Tuple[str, ...]:
        """Return a tuple containing all the channel names.

        Notes:
            Includes the dedicated digital channel ``DCH1`` if ``MSO`` license is present.
        """
        retval = super().all_channel_names_list
        if self.has_license("MSO"):
            # replace last index CH3 or CH5 with DCH1
            retval = (*retval[:-1], "DCH1")
        return retval

    @cached_property
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""
        retval = super().total_channels
        if self.has_license("MSO"):
            retval += 1
        return retval
