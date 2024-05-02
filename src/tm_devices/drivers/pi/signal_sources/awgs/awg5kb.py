"""AWG5KB device driver module."""

import pyvisa as visa

from tm_devices.drivers.pi.signal_sources.awgs.awg5k import AWG5K
from tm_devices.helpers import DeviceConfigEntry


class AWG5KB(AWG5K):
    """AWG5KB device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(  # pylint: disable=useless-parent-delegation
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create an AWG5KB device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        # NOTE: This method must be defined for the documentation to properly generate
        super().__init__(config_entry, verbose, visa_resource)
