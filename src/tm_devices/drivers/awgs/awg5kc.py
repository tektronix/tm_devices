"""AWG5KC device driver module."""

from tm_devices.commands import AWG5KCMixin
from tm_devices.drivers.awgs.awg5kb import AWG5KB


class AWG5KC(AWG5KCMixin, AWG5KB):  # pyright: ignore[reportIncompatibleVariableOverride]
    """AWG5KC device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
