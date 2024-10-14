"""Base DMM75xx device driver module."""

from abc import ABC
from typing import Tuple

import pyvisa as visa

from tm_devices.driver_mixins.shared_implementations.common_tsp_error_check_mixin import (
    CommonTSPErrorCheckMixin,
)
from tm_devices.driver_mixins.shared_implementations.ieee488_2_commands import (
    LegacyTSPIEEE4882Commands,
)
from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.digital_multimeters.digital_multimeter import DigitalMultimeter
from tm_devices.helpers import DeviceConfigEntry


@family_base_class
class DMM75xx(CommonTSPErrorCheckMixin, DigitalMultimeter, ABC):
    """Base DMM75xx device driver."""

    _IEEE_COMMANDS_CLASS = LegacyTSPIEEE4882Commands

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(  # pylint: disable=useless-parent-delegation
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
        default_visa_timeout: int,
    ) -> None:
        """Create a DMM75xx device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
            default_visa_timeout: The default VISA timeout value in milliseconds.
        """
        # NOTE: This method must be defined for the documentation to properly generate
        super().__init__(config_entry, verbose, visa_resource, default_visa_timeout)

    ################################################################################################
    # Properties
    ################################################################################################

    @property
    def ieee_cmds(self) -> LegacyTSPIEEE4882Commands:
        """Return an internal class containing methods for the standard IEEE 488.2 command set."""
        return self._ieee_cmds  # pyright: ignore[reportReturnType]

    ################################################################################################
    # Public Methods
    ################################################################################################

    ################################################################################################
    # Private Methods
    ################################################################################################
    def _get_errors(self) -> Tuple[int, Tuple[str, ...]]:
        """Get the current errors from the device.

        !!! note
            This method will clear out the error queue after reading the current errors.

        Returns:
            A tuple containing the current error code alongside a tuple of the current error
            messages.
        """
        # instrument returns exponential numbers so converting to float before int
        err_count = int(self.query("print(eventlog.getcount(eventlog.SEV_ERROR))"))
        error_message_list = []
        if err_count:
            error_message_list = [self.query("print(eventlog.next())") for _ in range(err_count)]
        return err_count, tuple(filter(None, error_message_list))
