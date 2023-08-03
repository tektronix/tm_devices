"""SMU Model 2651A device driver module."""
from tm_devices.commands import SMU2651AMixin
from tm_devices.drivers.pi.source_measure_units.smu2600.smu2650a import SMU2650A


class SMU2651A(SMU2651AMixin, SMU2650A):
    """SMU2651A device driver."""
