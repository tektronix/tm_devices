"""The rem commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7KC, DSA70KC,
DSA70KD, LPD6, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2, MSO2K, MSO2KB, MSO4, MSO4K, MSO4KB, MSO5,
MSO5B, MSO5KB, MSO5LP, MSO6, MSO6B, MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:

::

    - REM <QString>
"""
from typing import Optional, TYPE_CHECKING

from .._helpers import SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.drivers.pi.pi_device import PIDevice


class Rem(SCPICmdWrite):
    """The ``REM`` command.

    **Description:**
        - This command (no query form) embeds a comment within programs as a means of internally
          documenting the programs. This is how to embed comments in a .set file. The instrument
          ignores these embedded comment lines.

    **Usage:**
        - Using the ``.write(value)`` method will send the ``REM value`` command.

    **SCPI Syntax:**

    ::

        - REM <QString>

    **Info:**
        - ``<QString>`` is a string that can contain a maximum of 80 characters.
    """

    _WRAP_ARG_WITH_QUOTES = True

    def __init__(self, device: Optional["PIDevice"] = None, cmd_syntax: str = "REM") -> None:
        super().__init__(device, cmd_syntax)
