"""The set commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7KC, DSA70KC,
DSA70KD, LPD6, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2, MSO2K, MSO2KB, MSO4, MSO4K, MSO4KB, MSO5,
MSO5B, MSO5KB, MSO5LP, MSO6, MSO6B, MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:

::

    - SET?
"""
from typing import Optional, TYPE_CHECKING

from .._helpers import SCPICmdRead

if TYPE_CHECKING:
    from tm_devices.drivers.pi.pi_device import PIDevice


class Set(SCPICmdRead):
    """The ``SET`` command.

    **Description:**
        - This query-only command returns the commands that list the instrument settings, except for
          configuration information for the calibration values. You can use these commands to return
          the instrument to the state it was in when you made the ``SET?`` query. The ``SET?`` query
          always returns command headers, regardless of the setting of the HEADER command. This is
          because the returned commands are intended to be sent back to the instrument as a command
          string. The VERBOSE command can still be used to specify whether the returned headers
          should be abbreviated or full-length. This command is identical to the LRN command.

    **Usage:**
        - Using the ``.query()`` method will send the ``SET?`` query.
        - Using the ``.verify(value)`` method will send the ``SET?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    **SCPI Syntax:**

    ::

        - SET?
    """

    def __init__(self, device: Optional["PIDevice"] = None, cmd_syntax: str = "SET") -> None:
        super().__init__(device, cmd_syntax)
