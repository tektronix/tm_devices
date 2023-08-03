"""AFG3K device driver module."""
from tm_devices.commands import AFG3KMixin
from tm_devices.drivers.pi.signal_sources.afgs.afg import AFG, AFGSourceDeviceConstants


class AFG3K(AFG3KMixin, AFG):
    """AFG3K device driver."""

    _DEVICE_CONSTANTS = AFGSourceDeviceConstants(
        memory_page_size=2,
        memory_max_record_length=128 * 1024,
        memory_min_record_length=2,
    )
