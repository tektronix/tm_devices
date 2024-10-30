"""DSA70KD device driver module."""

from tm_devices.commands import DSA70KDMixin
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.dsa70k import DSA70K


class DSA70KD(DSA70KDMixin, DSA70K):
    """DSA70KD device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
