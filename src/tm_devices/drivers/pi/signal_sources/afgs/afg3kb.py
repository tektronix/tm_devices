"""AFG3KB device driver module."""
from tm_devices.commands import AFG3KBMixin
from tm_devices.drivers.pi.signal_sources.afgs.afg3k import AFG3K


class AFG3KB(AFG3KBMixin, AFG3K):
    """AFG3KB device driver."""

    ################################################################################################
    # Public Methods
    ################################################################################################
