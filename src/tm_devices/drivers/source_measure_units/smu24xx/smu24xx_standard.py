"""SMU24xxStandard device driver module."""

from __future__ import annotations

from abc import ABC
from typing import Tuple, TYPE_CHECKING

from tm_devices.driver_mixins.device_control import PIControl
from tm_devices.driver_mixins.shared_implementations.common_pi_system_error_check_mixin import (
    CommonPISystemErrorCheckMixin,
)
from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.source_measure_units.source_measure_unit import SourceMeasureUnit
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

if TYPE_CHECKING:
    from tm_devices.driver_mixins.shared_implementations.ieee488_2_commands import IEEE4882Commands


@family_base_class
class SMU24xxStandard(CommonPISystemErrorCheckMixin, PIControl, SourceMeasureUnit, ABC):
    """Base SMU24xxStandard device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################
    @property
    def all_channel_names_list(self) -> Tuple[str, ...]:
        """Return a tuple containing all the channel names."""
        return tuple(f"OUTPUT{x + 1}" for x in range(self.total_channels))

    @property
    def ieee_cmds(self) -> IEEE4882Commands:
        """Return an internal class containing methods for the standard IEEE 488.2 command set."""
        return self._ieee_cmds

    @cached_property
    def total_channels(self) -> int:  # pylint: disable=no-self-use
        """Return the total number of channels (all types)."""
        return 1

    ################################################################################################
    # Public Methods
    ################################################################################################

    ################################################################################################
    # Private Methods
    ################################################################################################
