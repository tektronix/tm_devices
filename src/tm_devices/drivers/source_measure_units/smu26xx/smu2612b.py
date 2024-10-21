"""SMU Model 2612B device driver module."""

from tm_devices.commands import SMU2612BMixin
from tm_devices.drivers.source_measure_units.smu26xx.smu26xxb import SMU26xxB


class SMU2612B(SMU2612BMixin, SMU26xxB):  # pyright: ignore[reportIncompatibleVariableOverride]
    """SMU2612B device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
