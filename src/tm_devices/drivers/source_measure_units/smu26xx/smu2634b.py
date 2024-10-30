"""SMU Model 2634B device driver module."""

from tm_devices.commands import SMU2634BMixin
from tm_devices.drivers.source_measure_units.smu26xx.smu26xxb import SMU26xxB


class SMU2634B(SMU2634BMixin, SMU26xxB):  # pyright: ignore[reportIncompatibleVariableOverride]
    """SMU2634B device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
