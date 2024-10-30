"""DPO7KC device driver module."""

from tm_devices.commands import DPO7KCMixin
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.dpo7k import DPO7K


class DPO7KC(DPO7KCMixin, DPO7K):  # pyright: ignore[reportIncompatibleVariableOverride]
    """DPO7KC device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
