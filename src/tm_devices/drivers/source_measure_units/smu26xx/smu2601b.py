"""SMU Model 2601B device driver module."""

from tm_devices.commands import SMU2601BMixin
from tm_devices.drivers.source_measure_units.smu26xx.smu26xxb import SMU26xxB


class SMU2601B(SMU2601BMixin, SMU26xxB):  # pyright: ignore[reportIncompatibleVariableOverride]
    """SMU2601B device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
