"""AWG7KC device driver module."""

import pyvisa as visa

from tm_devices.commands import AWG7KCMixin
from tm_devices.drivers.pi.signal_generators.awgs.awg7kb import AWG7KB
from tm_devices.helpers import DeviceConfigEntry


class AWG7KC(AWG7KCMixin, AWG7KB):  # pyright: ignore[reportIncompatibleMethodOverride]
    """AWG7KC device driver."""

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
        """Create an AWG7KC device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
            default_visa_timeout: The default VISA timeout value in milliseconds.
        """
        # NOTE: This method must be defined for the documentation to properly generate
        super().__init__(config_entry, verbose, visa_resource, default_visa_timeout)

    ################################################################################################
    # Public Methods
    ################################################################################################
