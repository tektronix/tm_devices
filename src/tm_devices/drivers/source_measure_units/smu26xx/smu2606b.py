"""SMU Model 2606B device driver module."""

from tm_devices.commands import SMU2606BMixin
from tm_devices.drivers.source_measure_units.smu26xx.smu26xxb import SMU26xxB


class SMU2606B(SMU2606BMixin, SMU26xxB):  # pyright: ignore[reportIncompatibleVariableOverride]
    """SMU2606B device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
