"""SMU Model 2611B device driver module."""
from tm_devices.commands import SMU2611BMixin
from tm_devices.drivers.pi.source_measure_units.smu2600.smu2600b import SMU2600B


class SMU2611B(SMU2611BMixin, SMU2600B):
    """SMU2611B device driver."""
