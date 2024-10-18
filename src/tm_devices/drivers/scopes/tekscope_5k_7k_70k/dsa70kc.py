"""DSA70KC device driver module."""

from tm_devices.commands import DSA70KCMixin
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.dsa70k import DSA70K


class DSA70KC(DSA70KCMixin, DSA70K):
    """DSA70KC device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
