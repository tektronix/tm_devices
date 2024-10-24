"""DPO70KD device driver module."""

from tm_devices.commands import DPO70KDMixin
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.dpo70kc import DPO70KC


class DPO70KD(DPO70KDMixin, DPO70KC):  # pyright: ignore[reportIncompatibleVariableOverride]
    """DPO70KD device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
