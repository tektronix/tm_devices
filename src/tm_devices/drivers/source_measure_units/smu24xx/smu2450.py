"""SMU Model 2450 device driver module."""

from tm_devices.commands import SMU2450Mixin
from tm_devices.drivers.source_measure_units.smu24xx.smu24xx_interactive import (
    SMU24xxInteractive,
)


class SMU2450(SMU2450Mixin, SMU24xxInteractive):
    """SMU2450 device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
