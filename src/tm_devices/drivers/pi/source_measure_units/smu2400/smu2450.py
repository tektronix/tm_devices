"""SMU Model 2450 device driver module."""
from tm_devices.commands import SMU2450Mixin
from tm_devices.drivers.pi.source_measure_units.smu2400.smu2400_interactive import (
    SMU2400Interactive,
)


class SMU2450(SMU2450Mixin, SMU2400Interactive):
    """SMU2450 device driver."""
