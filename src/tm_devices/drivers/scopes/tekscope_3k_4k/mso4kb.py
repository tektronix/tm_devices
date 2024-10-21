"""MSO4KB device driver module."""

from tm_devices.commands import MSO4KBMixin
from tm_devices.drivers.scopes.tekscope_3k_4k.mso4k import MSO4K


class MSO4KB(MSO4KBMixin, MSO4K):  # pyright: ignore[reportIncompatibleVariableOverride]
    """MSO4KB device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################

    ################################################################################################
    # Public Methods
    ################################################################################################

    ################################################################################################
    # Private Methods
    ################################################################################################
