"""SMU24xxStandard device driver module."""

from __future__ import annotations

from abc import ABC
from typing import Tuple, TYPE_CHECKING, Union

from tm_devices.driver_mixins.device_control.pi_control import PIControl
from tm_devices.driver_mixins.shared_implementations.tek_afg_awg_mixin import TekAFGAWG
from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.source_measure_units.source_measure_unit import SourceMeasureUnit

# noinspection PyPep8Naming
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

if TYPE_CHECKING:
    from tm_devices.driver_mixins.shared_implementations.ieee488_2_commands import IEEE4882Commands


@family_base_class
class SMU24xxStandard(PIControl, SourceMeasureUnit, ABC):
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
        return tuple(f"OUTPUT{x+1}" for x in range(self.total_channels))

    @property
    def ieee_cmds(self) -> IEEE4882Commands:
        """Return an internal class containing methods for the standard IEEE 488.2 command set."""
        return self._ieee_cmds

    @cached_property
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""
        return 1

    ################################################################################################
    # Public Methods
    ################################################################################################
    def expect_esr(self, esr: Union[int, str], error_string: str = "") -> Tuple[bool, str]:
        r"""Check for the expected number of errors and output string.

        Sends the ``*ESR?`` and SYSTEM:ERROR? queries.

        Args:
            esr: Expected ``*ESR?`` value
            error_string: Expected error buffer string.
                Multiple errors should be separated by a \n character

        Returns:
            Boolean indicating if the check passed or failed and a string with the results.
        """
        # TODO: nfelt14: Move this shared implementation into a mixin for all classes that use it
        return TekAFGAWG.expect_esr(self, esr, error_string)  # type: ignore[arg-type]

    def get_eventlog_status(self) -> Tuple[bool, str]:
        """Help function for getting the eventlog status.

        Returns:
            Boolean indicating no error, String containing concatenated contents of event log.
        """
        # TODO: nfelt14: Move this shared implementation into a mixin for all classes that use it
        return TekAFGAWG.get_eventlog_status(self)  # type: ignore[arg-type]

    ################################################################################################
    # Private Methods
    ################################################################################################
