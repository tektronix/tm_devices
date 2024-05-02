"""AFG31K device driver module."""

import pyvisa as visa

from tm_devices.drivers.pi.signal_sources.afgs.afg import AFG, AFGSourceDeviceConstants
from tm_devices.helpers import DeviceConfigEntry


class AFG31K(AFG):
    """AFG31K device driver."""

    _DEVICE_CONSTANTS = AFGSourceDeviceConstants(
        memory_page_size=2,
        memory_max_record_length=131072,
        memory_min_record_length=2,
    )

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(  # pylint: disable=useless-parent-delegation
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create an AFG31K device.

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
    def _reboot(self) -> None:
        """Reboot the device."""
        self.write("SYSTem:RESTart")
