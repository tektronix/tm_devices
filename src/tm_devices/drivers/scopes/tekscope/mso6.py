"""MSO6 device driver module."""

from tm_devices.commands import MSO6Mixin
from tm_devices.drivers.scopes.tekscope.tekscope import TekScope


class MSO6(MSO6Mixin, TekScope):  # pyright: ignore[reportIncompatibleVariableOverride]
    """MSO6 device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
