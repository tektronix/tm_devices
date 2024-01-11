"""Base TekScope3k4k scope device driver module."""
from abc import ABC

from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.pi.scopes.scope import Scope
from tm_devices.helpers import ReadOnlyCachedProperty


@family_base_class
class TekScope3k4k(Scope, ABC):
    """Base TekScope3k4k scope device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################

    @ReadOnlyCachedProperty
    def hostname(self) -> str:
        """Return the hostname of the device or an empty string if unable to fetch that."""
        return self.query(":ETHERNET:NAME?", verbose=False, remove_quotes=True)

    @ReadOnlyCachedProperty
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
