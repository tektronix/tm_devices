"""PSU2231A device driver."""

import pyvisa as visa

from tm_devices.drivers.pi.power_supplies.psu2200.psu2231 import PSU2231
from tm_devices.helpers import DeviceConfigEntry


class PSU2231A(PSU2231):
    """PSU2231A device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(  # pylint: disable=useless-parent-delegation
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create a PSU2231A device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        # NOTE: This method must be defined for the documentation to properly generate
        super().__init__(config_entry, verbose, visa_resource)
