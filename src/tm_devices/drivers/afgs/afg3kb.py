"""AFG3KB device driver module."""

from tm_devices.commands import AFG3KBMixin
from tm_devices.drivers.afgs.afg3k import AFG3K


class AFG3KB(AFG3KBMixin, AFG3K):  # pyright: ignore[reportIncompatibleVariableOverride]
    """AFG3KB device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Public Methods
    ################################################################################################
