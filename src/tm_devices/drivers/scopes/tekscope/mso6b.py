"""MSO6B device driver module."""

from tm_devices.commands import MSO6BMixin
from tm_devices.drivers.scopes.tekscope.mso6 import MSO6


class MSO6B(MSO6BMixin, MSO6):  # pyright: ignore[reportIncompatibleVariableOverride]
    """MSO6B device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
