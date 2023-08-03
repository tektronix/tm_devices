"""SMU Model 2602B device driver module."""
from tm_devices.commands import SMU2602BMixin
from tm_devices.drivers.pi.source_measure_units.smu2600.smu2600b import SMU2600B


class SMU2602B(SMU2602BMixin, SMU2600B):
    """SMU2602B device driver."""
