"""SMU Model 2600B device driver module."""
from abc import ABC
from typing import Union

from tm_devices.commands._smu2601b_commands import SMU2601BCommands
from tm_devices.commands._smu2601b_pulse_commands import SMU2601BPulseCommands
from tm_devices.commands._smu2602b_commands import SMU2602BCommands
from tm_devices.commands._smu2604b_commands import SMU2604BCommands
from tm_devices.commands._smu2606b_commands import SMU2606BCommands
from tm_devices.commands._smu2611b_commands import SMU2611BCommands
from tm_devices.commands._smu2612b_commands import SMU2612BCommands
from tm_devices.commands._smu2614b_commands import SMU2614BCommands
from tm_devices.commands._smu2634b_commands import SMU2634BCommands
from tm_devices.commands._smu2635b_commands import SMU2635BCommands
from tm_devices.commands._smu2636b_commands import SMU2636BCommands
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
