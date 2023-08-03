"""MSO5 device driver module."""
from tm_devices.commands import MSO5Mixin
from tm_devices.drivers.pi.scopes.tekscope.tekscope import TekScope


class MSO5(MSO5Mixin, TekScope):
    """MSO5 device driver."""
