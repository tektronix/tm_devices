"""SMU Model 2634B device driver module."""
from tm_devices.commands import SMU2634BMixin
from tm_devices.drivers.pi.source_measure_units.smu2600.smu2600b import SMU2600B


class SMU2634B(SMU2634BMixin, SMU2600B):
    """SMU2634B device driver."""
