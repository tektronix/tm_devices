"""SMU Model 2470 device driver module."""

from tm_devices.commands import SMU2470Mixin
from tm_devices.drivers.source_measure_units.smu24xx.smu24xx_interactive import (
    SMU24xxInteractive,
)


class SMU2470(SMU2470Mixin, SMU24xxInteractive):
    """SMU2470 device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
