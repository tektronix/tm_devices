"""LPD6 device driver module."""

from tm_devices.commands import LPD6Mixin
from tm_devices.drivers.scopes.tekscope.mso6 import MSO6


class LPD6(LPD6Mixin, MSO6):  # pyright: ignore[reportIncompatibleVariableOverride]
    """LPD6 device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
