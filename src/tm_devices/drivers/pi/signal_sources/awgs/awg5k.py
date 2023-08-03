"""AWG5K device driver module."""
from tm_devices.commands import AWG5KMixin
from tm_devices.drivers.pi.signal_sources.awgs.awg import AWG, AWGSourceDeviceConstants


class AWG5K(AWG5KMixin, AWG):
    """AWG5K device driver."""

    _DEVICE_CONSTANTS = AWGSourceDeviceConstants(
        memory_page_size=1,
        memory_max_record_length=16200000,
        memory_min_record_length=1,
    )

    ################################################################################################
    # Public Methods
    ################################################################################################
