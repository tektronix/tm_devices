"""SMU Model 2602B device driver module."""

from tm_devices.commands import SMU2602BMixin
from tm_devices.drivers.source_measure_units.smu26xx.smu26xxb import SMU26xxB


class SMU2602B(SMU2602BMixin, SMU26xxB):  # pyright: ignore[reportIncompatibleVariableOverride]
    """SMU2602B device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
