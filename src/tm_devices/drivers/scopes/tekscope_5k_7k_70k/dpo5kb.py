"""DPO5KB device driver module."""

from tm_devices.commands import DPO5KBMixin
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.dpo5k import DPO5K


class DPO5KB(DPO5KBMixin, DPO5K):  # pyright: ignore[reportIncompatibleVariableOverride]
    """DPO5KB device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
