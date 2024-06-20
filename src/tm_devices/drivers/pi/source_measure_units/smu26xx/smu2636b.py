"""SMU Model 2636B device driver module."""

import pyvisa as visa

from tm_devices.commands import SMU2636BMixin
from tm_devices.drivers.pi.source_measure_units.smu26xx.smu26xxb import SMU26xxB
from tm_devices.helpers import DeviceConfigEntry


class SMU2636B(SMU2636BMixin, SMU26xxB):
    """SMU2636B device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create a SMU2636B device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        # NOTE: This method must be defined for the documentation to properly generate
        super().__init__(config_entry, verbose, visa_resource)
