"""The clear commands module.

These commands are used in the following models:
LPD6, MDO3, MSO2, MSO4, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:

::

    - CLEAR
"""
from typing import Optional, TYPE_CHECKING

from .._helpers import SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.drivers.pi.pi_device import PIDevice


class Clear(SCPICmdWriteNoArguments):
    """The ``CLEAR`` command.

    **Description:**
        - This command  clears acquisitions, measurements, and waveforms.

    **Usage:**
        - Using the ``.write()`` method will send the ``CLEAR`` command.

    **SCPI Syntax:**

    ::

        - CLEAR
    """

    def __init__(self, device: Optional["PIDevice"] = None, cmd_syntax: str = "CLEAR") -> None:
        super().__init__(device, cmd_syntax)
