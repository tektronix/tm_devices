"""MSO5LP device driver module."""

import pyvisa as visa

from tm_devices.commands import MSO5LPMixin
from tm_devices.drivers.pi.scopes.tekscope.mso5 import MSO5
from tm_devices.helpers import DeviceConfigEntry


class MSO5LP(MSO5LPMixin, MSO5):
    """MSO5LP device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create a MSO5LP device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        # NOTE: This method must be defined for the documentation to properly generate
        super().__init__(config_entry, verbose, visa_resource)
