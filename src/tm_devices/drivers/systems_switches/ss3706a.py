"""SS3706A device driver module."""

import pyvisa as visa

from tm_devices.commands import SS3706AMixin
from tm_devices.driver_mixins.shared_implementations.common_tsp_error_check_mixin import (
    CommonTSPErrorCheckMixin,
)
from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.systems_switches.systems_switch import SystemsSwitch
from tm_devices.helpers import DeviceConfigEntry
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


@family_base_class
class SS3706A(SS3706AMixin, CommonTSPErrorCheckMixin, SystemsSwitch):
    """SS3706A device driver."""

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
        """Create a SS3706A device.

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
    @cached_property
    def total_channels(self) -> int:  # pylint: disable=no-self-use
        """Return the total number of channels (all types)."""
        return 576

    ################################################################################################
    # Public Methods
    ################################################################################################

    ################################################################################################
    # Private Methods
    ################################################################################################
