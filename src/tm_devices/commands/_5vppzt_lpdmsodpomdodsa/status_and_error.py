"""The status_and_error commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7KC, DSA70KC,
DSA70KD, LPD6, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2, MSO2K, MSO2KB, MSO4, MSO4K, MSO4KB, MSO5,
MSO5B, MSO5KB, MSO5LP, MSO6, MSO6B, MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:

::

    - *PUD {<Block>|<QString>}
    - *PUD?
"""
from typing import Optional, TYPE_CHECKING

from .._helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.drivers.pi.pi_device import PIDevice


class Pud(SCPICmdWrite, SCPICmdRead):
    """The ``*PUD`` command.

    **Description:**
        - This command sets or queries a string of Protected User Data. This data is protected by
          the PASSWord command. You can modify it only by first entering the correct password. This
          password is not necessary to query the data.

    **Usage:**
        - Using the ``.query()`` method will send the ``*PUD?`` query.
        - Using the ``.verify(value)`` method will send the ``*PUD?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``*PUD value`` command.

    **SCPI Syntax:**

    ::

        - *PUD {<Block>|<QString>}
        - *PUD?

    **Info:**
        - ``<Block>`` is a block containing up to 100 characters.
        - ``<QString>`` is a string containing up to 100 characters.
    """

    def __init__(self, device: Optional["PIDevice"] = None, cmd_syntax: str = "*PUD") -> None:
        super().__init__(device, cmd_syntax)
