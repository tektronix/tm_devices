"""MSO70KC device driver module."""

from tm_devices.commands import MSO70KCMixin
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.mso70k import MSO70K


class MSO70KC(MSO70KCMixin, MSO70K):
    """MSO70KC device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
