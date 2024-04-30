"""SMU Model 2460 device driver module."""

import pyvisa as visa

from tm_devices.commands import SMU2460Mixin
from tm_devices.drivers.pi.source_measure_units.smu2400.smu2400_interactive import (
    SMU2400Interactive,
)
from tm_devices.helpers import DeviceConfigEntry


class SMU2460(SMU2460Mixin, SMU2400Interactive):
    """SMU2460 device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create a SMU2460 device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        # NOTE: This method must be defined for the documentation to properly generate
        super().__init__(config_entry, verbose, visa_resource)
