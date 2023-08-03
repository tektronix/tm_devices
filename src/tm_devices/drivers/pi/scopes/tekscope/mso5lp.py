"""MSO5LP device driver module."""
from tm_devices.commands import MSO5LPMixin
from tm_devices.drivers.pi.scopes.tekscope.mso5 import MSO5


class MSO5LP(MSO5LPMixin, MSO5):
    """MSO5LP device driver."""
