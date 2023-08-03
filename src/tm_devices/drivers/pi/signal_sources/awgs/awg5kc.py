"""AWG5KC device driver module."""
from tm_devices.commands import AWG5KCMixin
from tm_devices.drivers.pi.signal_sources.awgs.awg5k import AWG5K


class AWG5KC(AWG5KCMixin, AWG5K):
    """AWG5KC device driver."""
