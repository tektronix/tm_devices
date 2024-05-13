"""SMU Model 26xxB device driver module."""

from abc import ABC
from typing import Union

from tm_devices.commands import (
    SMU2601BCommands,
    SMU2601BPulseCommands,
    SMU2602BCommands,
    SMU2604BCommands,
    SMU2606BCommands,
    SMU2611BCommands,
    SMU2612BCommands,
    SMU2614BCommands,
    SMU2634BCommands,
    SMU2635BCommands,
    SMU2636BCommands,
)
from tm_devices.drivers.pi.source_measure_units.smu26xx.smu26xx import SMU26xx


class SMU26xxB(SMU26xx, ABC):
    """Base SMU26xxB device driver."""

    ################################################################################################
    # Properties
    ################################################################################################
    @property
    def commands(
        self,
    ) -> Union[
        SMU2601BCommands,
        SMU2602BCommands,
        SMU2604BCommands,
        SMU2606BCommands,
        SMU2611BCommands,
        SMU2612BCommands,
        SMU2614BCommands,
        SMU2634BCommands,
        SMU2635BCommands,
        SMU2636BCommands,
        SMU2601BPulseCommands,
    ]:
        """Return the device commands."""
        return self._commands  # pragma: no cover
