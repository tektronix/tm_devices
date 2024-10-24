"""SMU Model 26xxB device driver module."""

from abc import ABC

from tm_devices.drivers.source_measure_units.smu26xx.smu26xx import SMU26xx


class SMU26xxB(SMU26xx, ABC):
    """Base SMU26xxB device driver."""

    ################################################################################################
    # Properties
    ################################################################################################
