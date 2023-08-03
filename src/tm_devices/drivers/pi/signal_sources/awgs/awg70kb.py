"""AWG70KB device driver module."""
from tm_devices.commands import AWG70KBMixin
from tm_devices.drivers.pi.signal_sources.awgs.awg70ka import AWG70KA


class AWG70KB(AWG70KBMixin, AWG70KA):
    """AWG70KB device driver."""
