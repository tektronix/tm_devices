"""DPO7KC device driver module."""

import pyvisa as visa

from tm_devices.commands import DPO7KCMixin
from tm_devices.drivers.pi.scopes.tekscope_5k_7k_70k.dpo7k import DPO7K
from tm_devices.helpers import DeviceConfigEntry


class DPO7KC(DPO7KCMixin, DPO7K):  # pyright: ignore[reportIncompatibleMethodOverride]
    """DPO7KC device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create a DPO7KC device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        # NOTE: This method must be defined for the documentation to properly generate
        super().__init__(config_entry, verbose, visa_resource)
