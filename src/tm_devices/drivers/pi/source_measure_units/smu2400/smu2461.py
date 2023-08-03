"""SMU Model 2461 device driver module."""
from tm_devices.commands import SMU2461Mixin
from tm_devices.drivers.pi.source_measure_units.smu2400.smu2400_interactive import (
    SMU2400Interactive,
)


class SMU2461(SMU2461Mixin, SMU2400Interactive):
    """SMU2461 device driver."""
