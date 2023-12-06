"""MSO4B device driver module."""
from tm_devices.commands import MSO4BMixin
from tm_devices.drivers.pi.scopes.tekscope.mso4 import MSO4


class MSO4B(MSO4BMixin, MSO4):
    """MSO4B device driver."""
