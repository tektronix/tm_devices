"""TekScopePC device driver module."""
# TODO: rename file after TekScopeSW is fully removed

import pyvisa as visa

from tm_devices.commands import TekScopePCMixin
from tm_devices.drivers.pi.scopes.tekscope.tekscope import TekScope
from tm_devices.helpers import DeviceConfigEntry

# noinspection PyPep8Naming
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


class TekScopePC(TekScopePCMixin, TekScope):  # pyright: ignore[reportIncompatibleMethodOverride]
    """TekScopePC device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create a TekScopePC device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        super().__init__(config_entry, verbose, visa_resource)

    ################################################################################################
    # Properties
    ################################################################################################

    @cached_property
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""
        # TekScopePC supports a maximum of 8 channels
        return 8

    ################################################################################################
    # Private Methods
    ################################################################################################
    def _reboot(self) -> None:
        """Reboot the device."""
        # TODO: overwrite the reboot code here


# An alias for TekScopeSW driver
class TekScopeSW(TekScopePC):
    """TekScopeSW device driver.

    !!! danger "Deprecated"
        This device driver is deprecated, use [`TekScopePC`][tm_devices.drivers.TekScopePC] instead.
    """
