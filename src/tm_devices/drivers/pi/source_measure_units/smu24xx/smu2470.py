"""SMU Model 2470 device driver module."""

import pyvisa as visa

from tm_devices.commands import SMU2470Mixin
from tm_devices.drivers.pi.source_measure_units.smu24xx.smu24xx_interactive import (
    SMU24xxInteractive,
)
from tm_devices.helpers import DeviceConfigEntry


class SMU2470(SMU2470Mixin, SMU24xxInteractive):
    """SMU2470 device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create a SMU2470 device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        # NOTE: This method must be defined for the documentation to properly generate
        super().__init__(config_entry, verbose, visa_resource)
