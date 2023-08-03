"""SMU Model 2600A device driver module."""
from abc import ABC

from tm_devices.drivers.pi.source_measure_units.smu2600.smu2600 import SMU2600


class SMU2600A(SMU2600, ABC):
    """Base SMU2600A device driver."""
