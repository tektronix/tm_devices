"""AFG3K device driver module."""

import pyvisa as visa

from tm_devices.commands import AFG3KMixin
from tm_devices.drivers.pi.signal_sources.afgs.afg import AFG, AFGSourceDeviceConstants
from tm_devices.helpers import DeviceConfigEntry


class AFG3K(AFG3KMixin, AFG):
    """AFG3K device driver."""

    _DEVICE_CONSTANTS = AFGSourceDeviceConstants(
        memory_page_size=2,
        memory_max_record_length=128 * 1024,
        memory_min_record_length=2,
    )

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create an AFG3K device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        # NOTE: This method must be defined for the documentation to properly generate
        super().__init__(config_entry, verbose, visa_resource)
