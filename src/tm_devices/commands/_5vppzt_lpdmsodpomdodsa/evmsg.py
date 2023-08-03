"""The evmsg commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7KC, DSA70KC,
DSA70KD, LPD6, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2, MSO2K, MSO2KB, MSO4, MSO4K, MSO4KB, MSO5,
MSO5B, MSO5KB, MSO5LP, MSO6, MSO6B, MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:

::

    - EVMsg?
"""
from typing import Optional, TYPE_CHECKING

from .._helpers import SCPICmdRead

if TYPE_CHECKING:
    from tm_devices.drivers.pi.pi_device import PIDevice


class Evmsg(SCPICmdRead):
    """The ``EVMsg`` command.

    **Description:**
        - This query-only command removes a single event code from the Event Queue that is
          associated with the results of the last ESR read and returns the event code with an
          explanatory message. For more information, see Event Handling.

    **Usage:**
        - Using the ``.query()`` method will send the ``EVMsg?`` query.
        - Using the ``.verify(value)`` method will send the ``EVMsg?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    **SCPI Syntax:**

    ::

        - EVMsg?
    """

    def __init__(self, device: Optional["PIDevice"] = None, cmd_syntax: str = "EVMsg") -> None:
        super().__init__(device, cmd_syntax)
