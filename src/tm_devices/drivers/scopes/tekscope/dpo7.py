"""DPO7 device driver module."""

from abc import ABC

import pyvisa as visa

from tm_devices.drivers.scopes.tekscope.tekscope import TekScope
from tm_devices.helpers import (
    DeviceConfigEntry,
)
from tm_devices.helpers import (
    ReadOnlyCachedProperty as cached_property,  # noqa: N813
)


class DPO7(TekScope, ABC):
    """DPO7 device driver."""

    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
        default_visa_timeout: int,
    ) -> None:
        """Create a DPO7 device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
            default_visa_timeout: The default VISA timeout value in milliseconds.
        """
        super().__init__(config_entry, verbose, visa_resource, default_visa_timeout)
        self._reboot_quiet_period = 180

    @cached_property
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""
        return int(self.model[5])

    ################################################################################################
    # Private Methods
    ################################################################################################
    @staticmethod
    def _get_driver_specific_multipliers() -> float:
        """Return a value to multiply the original Tekscope IAFG frequency by."""
        return 2.0
