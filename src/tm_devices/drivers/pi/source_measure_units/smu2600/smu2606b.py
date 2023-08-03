"""SMU Model 2606B device driver module."""
from tm_devices.commands import SMU2606BMixin
from tm_devices.drivers.pi.source_measure_units.smu2600.smu2600b import SMU2600B


class SMU2606B(SMU2606BMixin, SMU2600B):
    """SMU2606B device driver."""
