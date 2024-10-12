"""2200 Base device driver for the 22xx family of power supplies."""

from packaging.version import Version

from tm_devices.driver_mixins.device_control.pi_control import PIControl
from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.power_supplies.power_supply import PowerSupplyUnit
from tm_devices.helpers import get_version

# noinspection PyPep8Naming
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


@family_base_class
class PSU2200(PowerSupplyUnit, PIControl):
    """2200 Base device driver for the 22xx family of power supplies."""

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################

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
