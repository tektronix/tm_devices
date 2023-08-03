"""MSO6 device driver module."""
from tm_devices.commands import MSO6Mixin
from tm_devices.drivers.pi.scopes.tekscope.tekscope import TekScope


class MSO6(MSO6Mixin, TekScope):
    """MSO6 device driver."""
