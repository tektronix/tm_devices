"""PSU2230 device driver."""

import pyvisa as visa

from tm_devices.drivers.pi.power_supplies.psu2200.psu2200 import PSU2200
from tm_devices.helpers import DeviceConfigEntry


class PSU2230(PSU2200):
    """PSU2230 device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(  # pylint: disable=useless-parent-delegation
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create a PSU2230 device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        # NOTE: This method must be defined for the documentation to properly generate
        super().__init__(config_entry, verbose, visa_resource)
