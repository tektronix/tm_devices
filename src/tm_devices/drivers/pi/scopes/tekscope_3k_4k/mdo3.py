"""MDO3 device driver module."""
from functools import cached_property

import pyvisa as visa

from tm_devices.commands import MDO3Mixin
from tm_devices.drivers.pi.scopes.tekscope_3k_4k.tekscope_3k_4k import TekScope3k4k
from tm_devices.helpers import DeviceConfigEntry


class MDO3(MDO3Mixin, TekScope3k4k):
    """MDO3 device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create a MDO3 device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        super().__init__(config_entry, verbose, visa_resource)

    ################################################################################################
    # Properties
    ################################################################################################
    @cached_property
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""
        return int(self.model[-1])

    ################################################################################################
    # Public Methods
    ################################################################################################

    ################################################################################################
    # Private Methods
    ################################################################################################
