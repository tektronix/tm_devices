"""SMU Model 2657A device driver module."""
from tm_devices.commands import SMU2657AMixin
from tm_devices.drivers.pi.source_measure_units.smu2600.smu2650a import SMU2650A


class SMU2657A(SMU2657AMixin, SMU2650A):
    """SMU2657A device driver."""
