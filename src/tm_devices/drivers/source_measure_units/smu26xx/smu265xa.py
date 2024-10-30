"""SMU Model 265xA device driver module."""

from abc import ABC

from tm_devices.drivers.source_measure_units.smu26xx.smu26xx import SMU26xx


class SMU265xA(SMU26xx, ABC):
    """Base SMU265xA device driver."""

    ################################################################################################
    # Properties
    ################################################################################################
