"""2200 Base device driver for the 22xx family of power supplies."""

from typing import Tuple, Union

from packaging.version import Version

from tm_devices.driver_mixins.device_control.pi_control import PIControl
from tm_devices.driver_mixins.shared_implementations.tek_afg_awg_mixin import TekAFGAWG
from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.power_supplies.power_supply import PowerSupplyUnit
from tm_devices.helpers import get_version

# noinspection PyPep8Naming
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


@family_base_class
class PSU2200(PIControl, PowerSupplyUnit):  # pyright: ignore[reportIncompatibleVariableOverride]  # TODO: nfelt14: figure out how to not need this
    """2200 Base device driver for the 22xx family of power supplies."""

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################
    @cached_property
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""
        return max(1, int(self.model[2])) if self.model[2].isdecimal() else 1

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

    @cached_property
    def fpga_version(self) -> Version:
        """Return the fpga version of the device."""
        id_string_parts = self.idn_string.split(",")
        sw_version = id_string_parts[-1]
        if "-" in sw_version:
            split_sw = sw_version.split("-")
            return get_version(split_sw[1])
        return Version("0")  # pragma: no cover

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
