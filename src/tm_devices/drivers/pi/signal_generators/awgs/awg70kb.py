"""AWG70KB device driver module."""

import pyvisa as visa

from tm_devices.commands import AWG70KBMixin
from tm_devices.drivers.pi.signal_generators.awgs.awg70ka import AWG70KA
from tm_devices.helpers import DeviceConfigEntry


class AWG70KB(AWG70KBMixin, AWG70KA):  # pyright: ignore[reportIncompatibleMethodOverride]
    """AWG70KB device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create an AWG70KB device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        # NOTE: This method must be defined for the documentation to properly generate
        super().__init__(config_entry, verbose, visa_resource)
