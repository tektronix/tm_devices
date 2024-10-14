"""SMU Model 2460 device driver module."""

import pyvisa as visa

from tm_devices.commands import SMU2460Mixin
from tm_devices.drivers.source_measure_units.smu24xx.smu24xx_interactive import (
    SMU24xxInteractive,
)
from tm_devices.helpers import DeviceConfigEntry


class SMU2460(SMU2460Mixin, SMU24xxInteractive):
    """SMU2460 device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
        default_visa_timeout: int,
    ) -> None:
        """Create a SMU2460 device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
            default_visa_timeout: The default VISA timeout value in milliseconds.
        """
        # NOTE: This method must be defined for the documentation to properly generate
        super().__init__(config_entry, verbose, visa_resource, default_visa_timeout)