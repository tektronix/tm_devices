"""AWG7KC device driver module."""

from tm_devices.commands import AWG7KCMixin
from tm_devices.drivers.awgs.awg7kb import AWG7KB


class AWG7KC(AWG7KCMixin, AWG7KB):  # pyright: ignore[reportIncompatibleVariableOverride]
    """AWG7KC device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Public Methods
    ################################################################################################
