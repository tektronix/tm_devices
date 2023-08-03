"""The unlock commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7KC, DSA70KC,
DSA70KD, LPD6, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2, MSO2K, MSO2KB, MSO4, MSO4K, MSO4KB, MSO5, MSO5B,
MSO5KB, MSO5LP, MSO6, MSO6B, MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:

::

    - UNLock ALL
"""
from typing import Optional, TYPE_CHECKING

from .._helpers import SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.drivers.pi.pi_device import PIDevice


class Unlock(SCPICmdWrite):
    """The ``UNLock`` command.

    **Description:**
        - This command (no query form) unlocks the front panel controls only. To unlock the front
          panel controls and the touch screen use the LOCk NONe command. The command
          ``TOUCHSCReen:STATE ON`` enables the touch screen only.

    **Usage:**
        - Using the ``.write(value)`` method will send the ``UNLock value`` command.

    **SCPI Syntax:**

    ::

        - UNLock ALL

    **Info:**
        - ``ALL`` specifies that all front panel buttons and knobs are unlocked.
    """

    def __init__(self, device: Optional["PIDevice"] = None, cmd_syntax: str = "UNLock") -> None:
        super().__init__(device, cmd_syntax)
