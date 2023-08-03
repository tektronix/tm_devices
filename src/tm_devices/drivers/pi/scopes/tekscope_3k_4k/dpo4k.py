"""DPO4K device driver module."""

import pyvisa as visa

from tm_devices.commands import DPO4KMixin
from tm_devices.drivers.pi.scopes.tekscope_3k_4k.tekscope_3k_4k import TekScope3k4k
from tm_devices.helpers import DeviceConfigEntry


class DPO4K(DPO4KMixin, TekScope3k4k):
    """DPO4K device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create a DPO4K device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        super().__init__(config_entry, verbose, visa_resource)

    ################################################################################################
    # Properties
    ################################################################################################

    ################################################################################################
    # Public Methods
    ################################################################################################

    ################################################################################################
    # Private Methods
    ################################################################################################
