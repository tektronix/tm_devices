"""SMU Model 2614B device driver module."""

from tm_devices.commands import SMU2614BMixin
from tm_devices.drivers.source_measure_units.smu26xx.smu26xxb import SMU26xxB


class SMU2614B(SMU2614BMixin, SMU26xxB):  # pyright: ignore[reportIncompatibleVariableOverride]
    """SMU2614B device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
