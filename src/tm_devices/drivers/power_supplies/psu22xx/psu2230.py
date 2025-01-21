"""PSU2230 device driver."""

from packaging.version import Version

from tm_devices.drivers.power_supplies.psu22xx.psu2200 import PSU2200
from tm_devices.helpers import get_version
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


class PSU2230(PSU2200):
    """PSU2230 device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Cached Properties
    ################################################################################################
    @cached_property
    def sw_version(self) -> Version:
        """Return the software version of the device."""
        id_string_parts = self.idn_string.split(",")
        sw_version = id_string_parts[-1].split("-")[0]
        return get_version(sw_version)
