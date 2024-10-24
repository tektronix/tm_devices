"""DPO70KC device driver module."""

from tm_devices.commands import DPO70KCMixin
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.dpo70k import DPO70K


class DPO70KC(DPO70KCMixin, DPO70K):
    """DPO70KC device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
