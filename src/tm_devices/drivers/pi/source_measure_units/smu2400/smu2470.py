"""SMU Model 2470 device driver module."""
from tm_devices.commands import SMU2470Mixin
from tm_devices.drivers.pi.source_measure_units.smu2400.smu2400_interactive import (
    SMU2400Interactive,
)


class SMU2470(SMU2470Mixin, SMU2400Interactive):
    """SMU2470 device driver."""
