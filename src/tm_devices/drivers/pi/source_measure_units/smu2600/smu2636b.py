"""SMU Model 2636B device driver module."""
from tm_devices.commands import SMU2636BMixin
from tm_devices.drivers.pi.source_measure_units.smu2600.smu2600b import SMU2600B


class SMU2636B(SMU2636BMixin, SMU2600B):
    """SMU2636B device driver."""
