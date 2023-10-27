"""SMU Model 2650A device driver module."""
from abc import ABC
from typing import Union

from tm_devices.commands._smu2651a_commands import SMU2651ACommands
from tm_devices.commands._smu2657a_commands import SMU2657ACommands
from tm_devices.drivers.pi.source_measure_units.smu2600.smu2600 import SMU2600


class SMU2650A(SMU2600, ABC):
    """Base SMU2650A device driver."""

    ################################################################################################
    # Properties
    ################################################################################################
    @property
    def commands(
        self,
    ) -> Union[SMU2651ACommands, SMU2657ACommands]:
        """Return the device commands."""
        return self._commands  # pragma: no cover
