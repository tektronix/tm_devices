"""DMM7510 device driver module."""

import pyvisa as visa

from tm_devices.commands import DMM7510Mixin
from tm_devices.drivers.pi.digital_multimeters.dmm75xx.dmm75xx import DMM75xx
from tm_devices.helpers import DeviceConfigEntry


class DMM7510(DMM7510Mixin, DMM75xx):
    """DMM7510 device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create a DMM7510 device.

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
