"""MSO4 device driver module."""
from tm_devices.commands import MSO4Mixin
from tm_devices.drivers.pi.scopes.tekscope.tekscope import TekScope


class MSO4(MSO4Mixin, TekScope):
    """MSO4 device driver."""
