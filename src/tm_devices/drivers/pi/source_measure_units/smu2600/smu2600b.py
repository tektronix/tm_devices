"""SMU Model 2600B device driver module."""
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
from tm_devices.drivers.pi.source_measure_units.smu2600.smu2600 import SMU2600


class SMU2600B(SMU2600, ABC):
    """Base SMU2600B device driver."""

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
