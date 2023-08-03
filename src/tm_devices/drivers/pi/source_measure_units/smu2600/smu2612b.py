"""SMU Model 2612B device driver module."""
from tm_devices.commands import SMU2612BMixin
from tm_devices.drivers.pi.source_measure_units.smu2600.smu2600b import SMU2600B


class SMU2612B(SMU2612BMixin, SMU2600B):
    """SMU2612B device driver."""
