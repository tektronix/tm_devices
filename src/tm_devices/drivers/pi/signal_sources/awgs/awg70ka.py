"""AWG70KA device driver module."""
from tm_devices.commands import AWG70KAMixin
from tm_devices.drivers.pi.signal_sources.awgs.awg import AWG, AWGSourceDeviceConstants


class AWG70KA(AWG70KAMixin, AWG):
    """AWG70KA device driver."""

    _DEVICE_CONSTANTS = AWGSourceDeviceConstants(
        memory_page_size=1,
        memory_max_record_length=2000000000,
        memory_min_record_length=1,
    )

    ################################################################################################
    # Public Methods
    ################################################################################################
