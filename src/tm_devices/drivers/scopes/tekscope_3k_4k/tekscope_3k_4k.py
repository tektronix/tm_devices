"""Base TekScope3k4k scope device driver module."""

from abc import ABC

from tm_devices.driver_mixins.device_control import PIControl
from tm_devices.driver_mixins.shared_implementations._tektronix_pi_scope_mixin import (
    _TektronixPIScopeMixin,  # pyright: ignore[reportPrivateUsage]
)
from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.scopes.scope import Scope
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


@family_base_class
class TekScope3k4k(_TektronixPIScopeMixin, PIControl, Scope, ABC):
    """Base TekScope3k4k scope device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################

    @cached_property
    def hostname(self) -> str:
        """Return the hostname of the device or an empty string if unable to fetch that."""
        return self.query(":ETHERNET:NAME?", verbose=False, remove_quotes=True)

    @cached_property
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""
        return int(self.model[6])

    ################################################################################################
    # Public Methods
    ################################################################################################

    ################################################################################################
    # Private Methods
    ################################################################################################
    def _reboot(self) -> None:
        """Perform the actual rebooting code."""
        self.write("REBOOT")
