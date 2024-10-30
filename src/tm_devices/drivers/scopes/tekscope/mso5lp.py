"""MSO5LP device driver module."""

from tm_devices.commands import MSO5LPMixin
from tm_devices.drivers.scopes.tekscope.mso5 import MSO5


class MSO5LP(MSO5LPMixin, MSO5):  # pyright: ignore[reportIncompatibleVariableOverride]
    """MSO5LP device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
