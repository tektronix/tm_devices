"""SMU Model 265xA device driver module."""

from abc import ABC
from typing import Union

from tm_devices.commands import SMU2651ACommands, SMU2657ACommands
from tm_devices.drivers.pi.source_measure_units.smu26xx.smu26xx import SMU26xx


class SMU265xA(SMU26xx, ABC):
    """Base SMU265xA device driver."""

    ################################################################################################
    # Properties
    ################################################################################################
    @property
    def commands(
        self,
    ) -> Union[SMU2651ACommands, SMU2657ACommands]:
        """Return the device commands."""
        return self._commands  # pragma: no cover
