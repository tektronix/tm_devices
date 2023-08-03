"""DPO70KD device driver module."""
from tm_devices.commands import DPO70KDMixin
from tm_devices.drivers.pi.scopes.tekscope_5k_7k_70k.dpo70kc import DPO70KC


class DPO70KD(DPO70KDMixin, DPO70KC):
    """DPO70KD device driver."""
