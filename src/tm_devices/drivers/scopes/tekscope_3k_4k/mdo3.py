"""MDO3 device driver module."""

from tm_devices.commands import MDO3Mixin
from tm_devices.drivers.scopes.tekscope_3k_4k.tekscope_3k_4k import TekScope3k4k
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


class MDO3(MDO3Mixin, TekScope3k4k):
    """MDO3 device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################
    @cached_property
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""
        return int(self.model[-1])

    ################################################################################################
    # Public Methods
    ################################################################################################

    ################################################################################################
    # Private Methods
    ################################################################################################
