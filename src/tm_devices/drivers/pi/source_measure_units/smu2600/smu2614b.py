"""SMU Model 2614B device driver module."""
from tm_devices.commands import SMU2614BMixin
from tm_devices.drivers.pi.source_measure_units.smu2600.smu2600b import SMU2600B


class SMU2614B(SMU2614BMixin, SMU2600B):
    """SMU2614B device driver."""
