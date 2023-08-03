"""AWG7K device driver module."""
from tm_devices.commands import AWG7KMixin
from tm_devices.drivers.pi.signal_sources.awgs.awg import AWG, AWGSourceDeviceConstants


class AWG7K(AWG7KMixin, AWG):
    """AWG7K device driver."""

    _DEVICE_CONSTANTS = AWGSourceDeviceConstants(
        memory_page_size=1,
        memory_max_record_length=32400000,
        memory_min_record_length=2,
    )

    ################################################################################################
    # Public Methods
    ################################################################################################
