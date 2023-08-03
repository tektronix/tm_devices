"""AWG7K device driver module."""
from tm_devices.commands import AWG7KCMixin
from tm_devices.drivers.pi.signal_sources.awgs.awg7k import AWG7K


class AWG7KC(AWG7KCMixin, AWG7K):
    """AWG7KC device driver."""

    ################################################################################################
    # Public Methods
    ################################################################################################
