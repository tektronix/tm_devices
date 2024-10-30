"""MSO70KDX device driver module."""

from tm_devices.commands import MSO70KDXMixin
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.mso70k import MSO70K


class MSO70KDX(MSO70KDXMixin, MSO70K):
    """MSO70KDX device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
