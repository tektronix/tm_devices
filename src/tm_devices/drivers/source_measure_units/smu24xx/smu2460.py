"""SMU Model 2460 device driver module."""

from tm_devices.commands import SMU2460Mixin
from tm_devices.drivers.source_measure_units.smu24xx.smu24xx_interactive import (
    SMU24xxInteractive,
)


class SMU2460(SMU2460Mixin, SMU24xxInteractive):
    """SMU2460 device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
