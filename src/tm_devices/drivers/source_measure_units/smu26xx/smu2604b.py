"""SMU Model 2604B device driver module."""

from tm_devices.commands import SMU2604BMixin
from tm_devices.drivers.source_measure_units.smu26xx.smu26xxb import SMU26xxB


class SMU2604B(SMU2604BMixin, SMU26xxB):  # pyright: ignore[reportIncompatibleVariableOverride]
    """SMU2604B device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
