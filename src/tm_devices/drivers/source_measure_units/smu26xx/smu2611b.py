"""SMU Model 2611B device driver module."""

from tm_devices.commands import SMU2611BMixin
from tm_devices.drivers.source_measure_units.smu26xx.smu26xxb import SMU26xxB


class SMU2611B(SMU2611BMixin, SMU26xxB):  # pyright: ignore[reportIncompatibleVariableOverride]
    """SMU2611B device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
