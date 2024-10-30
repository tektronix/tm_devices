"""SMU Model 2636B device driver module."""

from tm_devices.commands import SMU2636BMixin
from tm_devices.drivers.source_measure_units.smu26xx.smu26xxb import SMU26xxB


class SMU2636B(SMU2636BMixin, SMU26xxB):  # pyright: ignore[reportIncompatibleVariableOverride]
    """SMU2636B device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
