"""SMU Model 2651A device driver module."""

from tm_devices.commands import SMU2651AMixin
from tm_devices.drivers.source_measure_units.smu26xx.smu265xa import SMU265xA


class SMU2651A(SMU2651AMixin, SMU265xA):  # pyright: ignore[reportIncompatibleVariableOverride]
    """SMU2651A device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
