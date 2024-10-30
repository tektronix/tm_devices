"""DPO70KDX device driver module."""

from tm_devices.commands import DPO70KDXMixin
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.dpo70k import DPO70K


class DPO70KDX(DPO70KDXMixin, DPO70K):
    """DPO70KDX device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
