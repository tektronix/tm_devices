"""SMU Model 2657A device driver module."""

from tm_devices.commands import SMU2657AMixin
from tm_devices.drivers.source_measure_units.smu26xx.smu265xa import SMU265xA


class SMU2657A(SMU2657AMixin, SMU265xA):  # pyright: ignore[reportIncompatibleVariableOverride]
    """SMU2657A device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
