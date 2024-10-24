"""SMU Model 26xxA device driver module."""

from abc import ABC

from tm_devices.drivers.source_measure_units.smu26xx.smu26xx import SMU26xx


class SMU26xxA(SMU26xx, ABC):
    """Base SMU26xxA device driver."""
