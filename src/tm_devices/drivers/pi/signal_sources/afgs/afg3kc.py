"""AFG3KC device driver module."""
from tm_devices.commands import AFG3KCMixin
from tm_devices.drivers.pi.signal_sources.afgs.afg3kb import AFG3KB


class AFG3KC(AFG3KCMixin, AFG3KB):
    """AFG3KC device driver."""

    ################################################################################################
    # Public Methods
    ################################################################################################
