"""TekScopePC device driver module."""

import warnings

import pyvisa as visa

from tm_devices.commands import TekScopePCMixin
from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.scopes.tekscope.tekscope import AbstractTekScope
from tm_devices.helpers import DeviceConfigEntry
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


@family_base_class
class TekScopePC(TekScopePCMixin, AbstractTekScope):  # pyright: ignore[reportIncompatibleMethodOverride]
    """TekScopePC device driver."""

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
        """Create a TekScopePC device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
            default_visa_timeout: The default VISA timeout value in milliseconds.
        """
        super().__init__(config_entry, verbose, visa_resource, default_visa_timeout)

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
        warnings.warn(
            f"Rebooting is not supported for the {self.__class__.__name__} driver, "
            f"{self._name_and_alias} will not be rebooted.",
            stacklevel=3,
        )
