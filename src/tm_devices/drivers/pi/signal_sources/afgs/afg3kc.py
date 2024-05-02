"""AFG3KC device driver module."""

import pyvisa as visa

from tm_devices.commands import AFG3KCMixin
from tm_devices.drivers.pi.signal_sources.afgs.afg3kb import AFG3KB
from tm_devices.helpers import DeviceConfigEntry


class AFG3KC(AFG3KCMixin, AFG3KB):
    """AFG3KC device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create an AFG3KC device.

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
