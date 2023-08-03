"""SMU Model 2601B device driver module."""
from tm_devices.commands import SMU2601BMixin
from tm_devices.drivers.pi.source_measure_units.smu2600.smu2600b import SMU2600B


class SMU2601B(SMU2601BMixin, SMU2600B):
    """SMU2601B device driver."""
