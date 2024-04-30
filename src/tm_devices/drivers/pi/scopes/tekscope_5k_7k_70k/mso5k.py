"""MSO5K device driver module."""

import pyvisa as visa

from tm_devices.commands import MSO5KMixin
from tm_devices.drivers.pi.scopes.tekscope_5k_7k_70k.tekscope_5k_7k_70k import TekScope5k7k70k
from tm_devices.helpers import DeviceConfigEntry


class MSO5K(MSO5KMixin, TekScope5k7k70k):
    """MSO5K device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create a MSO5K device.

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

    ################################################################################################
    # Public Methods
    ################################################################################################

    ################################################################################################
    # Private Methods
    ################################################################################################
