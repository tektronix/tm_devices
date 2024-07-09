"""DPO5KB device driver module."""

import pyvisa as visa

from tm_devices.commands import DPO5KBMixin
from tm_devices.drivers.pi.scopes.tekscope_5k_7k_70k.dpo5k import DPO5K
from tm_devices.helpers import DeviceConfigEntry


class DPO5KB(DPO5KBMixin, DPO5K):  # pyright: ignore[reportIncompatibleMethodOverride]
    """DPO5KB device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create a DPO5KB device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        # NOTE: This method must be defined for the documentation to properly generate
        super().__init__(config_entry, verbose, visa_resource)
