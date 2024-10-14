"""DPO70KDX device driver module."""

import pyvisa as visa

from tm_devices.commands import DPO70KDXMixin
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.dpo70k import DPO70K
from tm_devices.helpers import DeviceConfigEntry


class DPO70KDX(DPO70KDXMixin, DPO70K):
    """DPO70KDX device driver."""

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
        """Create a DPO70KDX device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
            default_visa_timeout: The default VISA timeout value in milliseconds.
        """
        # NOTE: This method must be defined for the documentation to properly generate
        super().__init__(config_entry, verbose, visa_resource, default_visa_timeout)