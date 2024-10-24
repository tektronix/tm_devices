"""MSO5KB device driver module."""

from tm_devices.commands import MSO5KBMixin
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.mso5k import MSO5K


class MSO5KB(MSO5KBMixin, MSO5K):  # pyright: ignore[reportIncompatibleVariableOverride]
    """MSO5KB device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
