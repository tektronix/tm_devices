"""DPO70KSX device driver module."""

from tm_devices.commands import DPO70KSXMixin
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.dpo70k import DPO70K


class DPO70KSX(DPO70KSXMixin, DPO70K):
    """DPO70KSX device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
