"""DPO2K device driver module."""

from tm_devices.commands import DPO2KMixin
from tm_devices.drivers.pi.scopes.tekscope_2k.tekscope_2k import TekScope2k


class DPO2K(DPO2KMixin, TekScope2k):
    """DPO2K device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################

    ################################################################################################
    # Public Methods
    ################################################################################################

    ################################################################################################
    # Private Methods
    ################################################################################################
