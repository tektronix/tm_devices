"""SMU Model 2461 device driver module."""

from tm_devices.commands import SMU2461Mixin
from tm_devices.drivers.source_measure_units.smu24xx.smu24xx_interactive import (
    SMU24xxInteractive,
)


class SMU2461(SMU2461Mixin, SMU24xxInteractive):
    """SMU2461 device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
