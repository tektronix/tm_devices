"""AFG3KB device driver module."""

import pyvisa as visa

from tm_devices.commands import AFG3KBMixin
from tm_devices.drivers.pi.signal_generators.afgs.afg3k import AFG3K
from tm_devices.helpers import DeviceConfigEntry


class AFG3KB(AFG3KBMixin, AFG3K):  # pyright: ignore[reportIncompatibleMethodOverride]
    """AFG3KB device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create an AFG3KB device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        # NOTE: This method must be defined for the documentation to properly generate
        super().__init__(config_entry, verbose, visa_resource)

    ################################################################################################
    # Public Methods
    ################################################################################################
