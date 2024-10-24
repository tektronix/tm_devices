"""SMU Model 2635B device driver module."""

from tm_devices.commands import SMU2635BMixin
from tm_devices.drivers.source_measure_units.smu26xx.smu26xxb import SMU26xxB


class SMU2635B(SMU2635BMixin, SMU26xxB):  # pyright: ignore[reportIncompatibleVariableOverride]
    """SMU2635B device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
