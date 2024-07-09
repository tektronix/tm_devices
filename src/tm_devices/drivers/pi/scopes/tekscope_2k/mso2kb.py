"""MSO2KB device driver module."""

import pyvisa as visa

from tm_devices.commands import MSO2KBMixin
from tm_devices.drivers.pi.scopes.tekscope_2k.mso2k import MSO2K
from tm_devices.helpers import DeviceConfigEntry


class MSO2KB(MSO2KBMixin, MSO2K):  # pyright: ignore[reportIncompatibleMethodOverride]
    """MSO2KB device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create a MSO2KB device.

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
