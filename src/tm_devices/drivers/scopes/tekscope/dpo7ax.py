"""DPO7AX device driver module."""

from tm_devices.commands import DPO7AXMixin
from tm_devices.drivers.scopes.tekscope.dpo7 import DPO7


class DPO7AX(DPO7AXMixin, DPO7):  # pyright: ignore[reportIncompatibleVariableOverride]
    """DPO7AX device driver."""

    ################################################################################################
    # Properties
    ################################################################################################
