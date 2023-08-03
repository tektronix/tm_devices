"""SMU Model 2460 device driver module."""
from tm_devices.commands import SMU2460Mixin
from tm_devices.drivers.pi.source_measure_units.smu2400.smu2400_interactive import (
    SMU2400Interactive,
)


class SMU2460(SMU2460Mixin, SMU2400Interactive):
    """SMU2460 device driver."""
