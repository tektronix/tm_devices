"""SMU Model 2400 device driver module."""

import pyvisa as visa

from tm_devices.drivers.pi.source_measure_units.smu24xx.smu24xx_standard import SMU24xxStandard
from tm_devices.helpers import DeviceConfigEntry


class SMU2400(SMU24xxStandard):
    """SMU2400 device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(  # pylint: disable=useless-parent-delegation
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
        default_visa_timeout: int,
    ) -> None:
        """Create a SMU2400 device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
            default_visa_timeout: The default VISA timeout value in milliseconds.
        """
        # NOTE: This method must be defined for the documentation to properly generate
        super().__init__(config_entry, verbose, visa_resource, default_visa_timeout)
