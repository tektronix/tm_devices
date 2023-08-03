"""TEKSCOPESW device driver module."""
from functools import cached_property
from typing import Any

import pyvisa as visa

from tm_devices.drivers.pi.scopes.tekscope.tekscope import TekScope
from tm_devices.helpers import DeviceConfigEntry


class TekScopeSW(TekScope):
    """TEKSCOPESW device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create a TekScope device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        super().__init__(config_entry, verbose, visa_resource)

        # TODO: Remove once auto-generated commands are available for TekScopeSW
        self._commands: Any = NotImplemented
        self._command_argument_constants: Any = NotImplemented

    ################################################################################################
    # Properties
    ################################################################################################
    # TODO: Remove once auto-generated commands are available for TekScopeSW
    @property
    def command_argument_constants(self) -> Any:
        """Return the device command argument constants."""
        return self._command_argument_constants

    # TODO: Remove once auto-generated commands are available for TekScopeSW
    @property
    def commands(self) -> Any:
        """Return the device commands."""
        return self._commands

    @cached_property
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""
        return 0

    ################################################################################################
    # Private Methods
    ################################################################################################
    def _reboot(self) -> None:
        """Reboot the device."""
        # TODO: overwrite the reboot code here
