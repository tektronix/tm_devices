"""MP5103 device driver module."""

from tm_devices.commands import MP5103Mixin
from tm_devices.drivers.mainframes.mp5xxx.mp5xxx import MP5xxx


class MP5103(MP5103Mixin, MP5xxx):
    """MP5103 device driver."""
