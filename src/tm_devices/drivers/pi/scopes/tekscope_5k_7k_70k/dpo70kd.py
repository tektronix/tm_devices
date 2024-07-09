"""DPO70KD device driver module."""

import pyvisa as visa

from tm_devices.commands import DPO70KDMixin
from tm_devices.drivers.pi.scopes.tekscope_5k_7k_70k.dpo70kc import DPO70KC
from tm_devices.helpers import DeviceConfigEntry


class DPO70KD(DPO70KDMixin, DPO70KC):  # pyright: ignore[reportIncompatibleMethodOverride]
    """DPO70KD device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create a DPO70KD device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        # NOTE: This method must be defined for the documentation to properly generate
        super().__init__(config_entry, verbose, visa_resource)
