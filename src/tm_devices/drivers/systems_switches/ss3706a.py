"""SS3706A device driver module."""

from tm_devices.commands import SS3706AMixin
from tm_devices.driver_mixins.device_control import TSPControl
from tm_devices.driver_mixins.shared_implementations.common_tsp_error_check_mixin import (
    CommonTSPErrorCheckMixin,
)
from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.systems_switches.systems_switch import SystemsSwitch
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


@family_base_class
class SS3706A(SS3706AMixin, CommonTSPErrorCheckMixin, TSPControl, SystemsSwitch):
    """SS3706A device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################

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
