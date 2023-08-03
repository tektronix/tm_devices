"""SMU Model 2635B device driver module."""
from tm_devices.commands import SMU2635BMixin
from tm_devices.drivers.pi.source_measure_units.smu2600.smu2600b import SMU2600B


class SMU2635B(SMU2635BMixin, SMU2600B):
    """SMU2635B device driver."""
