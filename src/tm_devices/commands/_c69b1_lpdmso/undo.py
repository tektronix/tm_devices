"""The undo commands module.

These commands are used in the following models:
LPD6, MSO2, MSO4, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:

::

    - UNDO
"""
from typing import Optional, TYPE_CHECKING

from .._helpers import SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.drivers.pi.pi_device import PIDevice


class Undo(SCPICmdWriteNoArguments):
    """The ``UNDO`` command.

    **Description:**
        - Reverts the instrument settings to a state before the previous command or user interface
          action.

    **Usage:**
        - Using the ``.write()`` method will send the ``UNDO`` command.

    **SCPI Syntax:**

    ::

        - UNDO
    """

    def __init__(self, device: Optional["PIDevice"] = None, cmd_syntax: str = "UNDO") -> None:
        super().__init__(device, cmd_syntax)
