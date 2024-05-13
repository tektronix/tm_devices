"""SMU6517B device driver module."""

import pyvisa as visa

from tm_devices.drivers.pi.source_measure_units.smu60xx.smu6xxx import SMU6xxx
from tm_devices.helpers import DeviceConfigEntry


class SMU6517B(SMU6xxx):
    """SMU6517B device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(  # pylint: disable=useless-parent-delegation
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create a SMU6517B device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        # NOTE: This method must be defined for the documentation to properly generate
        super().__init__(config_entry, verbose, visa_resource)
