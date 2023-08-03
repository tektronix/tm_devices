"""The newpass commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7KC, DSA70KC,
DSA70KD, LPD6, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2, MSO2K, MSO2KB, MSO4, MSO4K, MSO4KB, MSO5,
MSO5B, MSO5KB, MSO5LP, MSO6, MSO6B, MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:

::

    - NEWpass <QString>
"""
from typing import Optional, TYPE_CHECKING

from .._helpers import SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.drivers.pi.pi_device import PIDevice


class Newpass(SCPICmdWrite):
    """The ``NEWpass`` command.

    **Description:**
        - This command (no query form) changes the password that enables access to password
          protected data. The PASSWord command must be successfully executed before using this
          command or an execution error will be generated.

    **Usage:**
        - Using the ``.write(value)`` method will send the ``NEWpass value`` command.

    **SCPI Syntax:**

    ::

        - NEWpass <QString>

    **Info:**
        - ``<QString>`` is the new password, which can contain up to 10 characters.
    """

    _WRAP_ARG_WITH_QUOTES = True

    def __init__(self, device: Optional["PIDevice"] = None, cmd_syntax: str = "NEWpass") -> None:
        super().__init__(device, cmd_syntax)
