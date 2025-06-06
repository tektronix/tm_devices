"""DPO2KB device driver module."""

from tm_devices.commands import DPO2KBMixin
from tm_devices.drivers.scopes.tekscope_2k.dpo2k import DPO2K


class DPO2KB(DPO2KBMixin, DPO2K):  # pyright: ignore[reportIncompatibleVariableOverride]
    """DPO2KB device driver."""

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
