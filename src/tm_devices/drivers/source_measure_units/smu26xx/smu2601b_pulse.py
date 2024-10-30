"""SMU Model 2601B-PULSE device driver module."""

from tm_devices.commands import SMU2601BPulseMixin
from tm_devices.drivers.source_measure_units.smu26xx.smu2601b import SMU2601B


class SMU2601BPulse(SMU2601BPulseMixin, SMU2601B):  # pyright: ignore[reportIncompatibleVariableOverride]
    """SMU2601B-PULSE device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
