"""AWG7K device driver module."""
from tm_devices.commands import AWG7KCMixin
from tm_devices.drivers.pi.signal_sources.awgs.awg7kb import AWG7KB


class AWG7KC(AWG7KCMixin, AWG7KB):
    """AWG7KC device driver."""

    ################################################################################################
    # Public Methods
    ################################################################################################
