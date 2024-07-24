"""AWG5KC device driver module."""

import pyvisa as visa

from tm_devices.commands import AWG5KCMixin
from tm_devices.drivers.pi.signal_generators.awgs.awg5kb import AWG5KB
from tm_devices.helpers import DeviceConfigEntry


class AWG5KC(AWG5KCMixin, AWG5KB):  # pyright: ignore[reportIncompatibleMethodOverride]
    """AWG5KC device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create an AWG5KC device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        # NOTE: This method must be defined for the documentation to properly generate
        super().__init__(config_entry, verbose, visa_resource)
