"""LPD6 device driver module."""

import pyvisa as visa

from tm_devices.commands import LPD6Mixin
from tm_devices.drivers.pi.scopes.tekscope.mso6 import MSO6
from tm_devices.helpers import DeviceConfigEntry


class LPD6(LPD6Mixin, MSO6):  # pyright: ignore[reportIncompatibleMethodOverride]
    """LPD6 device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create a MSO6 device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        # NOTE: This method must be defined for the documentation to properly generate
        super().__init__(config_entry, verbose, visa_resource)
