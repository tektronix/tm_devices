"""MSO5B device driver module."""

import pyvisa as visa

from tm_devices.commands import MSO5BMixin
from tm_devices.drivers.pi.scopes.tekscope.mso5 import MSO5
from tm_devices.helpers import DeviceConfigEntry


class MSO5B(MSO5BMixin, MSO5):  # pyright: ignore[reportIncompatibleMethodOverride]
    """MSO5B device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create a MSO5B device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        # NOTE: This method must be defined for the documentation to properly generate
        super().__init__(config_entry, verbose, visa_resource)

    ################################################################################################
    # Private Methods
    ################################################################################################
    @staticmethod
    def _get_driver_specific_multipliers() -> float:
        """Return a value to multiply the original Tekscope IAFG frequency by."""
        return 2.0
