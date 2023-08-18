"""2200 Base device driver for the 22xx family of power supplies."""
from functools import cached_property
from typing import Tuple

from packaging.version import Version

from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.pi.power_supplies.power_supply import PowerSupplyUnit
from tm_devices.helpers import get_version


@family_base_class
class PSU2200(PowerSupplyUnit):
    """2200 Base device driver for the 22xx family of power supplies."""

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################
    @property
    def all_channel_names_list(self) -> Tuple[str, ...]:
        """Return a tuple containing all the channel names."""
        return tuple(f"SOURCE{x+1}" for x in range(self.total_channels))

    @cached_property
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""
        return max(1, int(self.model[2])) if self.model[2].isdecimal() else 1

    ################################################################################################
    # Public Methods
    ################################################################################################
    @cached_property
    def fpga_version(self) -> Version:
        """Return the fpga version of the device."""
        id_string_parts = self.idn_string.split(",")
        sw_version = id_string_parts[-1]
        if "-" in sw_version:
            split_sw = sw_version.split("-")
            return get_version(split_sw[1])
        return Version("0")  # pragma: no cover

    ################################################################################################
    # Private Methods
    ################################################################################################
    def _reboot(self) -> None:
        """Perform the actual rebooting code."""
        # TODO: implement
        raise NotImplementedError(
            f"``.reboot()`` is not yet implemented for the {self.__class__.__name__} driver"
        )
