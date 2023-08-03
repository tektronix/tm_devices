"""The verbose commands module.

These commands are used in the following models:
DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7KC, DSA70KC, DSA70KD, LPD6, MSO2, MSO4, MSO5,
MSO5B, MSO5KB, MSO5LP, MSO6, MSO6B, MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:

::

    - VERBose {<NR1>|OFF|ON}
"""
from typing import Optional, TYPE_CHECKING

from .._helpers import SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.drivers.pi.pi_device import PIDevice


class Verbose(SCPICmdWrite):
    """The ``VERBose`` command.

    **Description:**
        - This command sets or queries the Verbose state that controls the length of keywords on
          query responses. Keywords can be both headers and arguments.

    **Usage:**
        - Using the ``.write(value)`` method will send the ``VERBose value`` command.

    **SCPI Syntax:**

    ::

        - VERBose {<NR1>|OFF|ON}

    **Info:**
        - ``<NR1>`` = 0 disables Verbose, any other value enables Verbose.
        - ``OFF`` sets the Verbose state to false, which returns minimum-length keywords for
          applicable setting queries.
        - ``ON`` sets the Verbose state to true, which returns full-length keywords for applicable
          setting queries.
    """

    def __init__(self, device: Optional["PIDevice"] = None, cmd_syntax: str = "VERBose") -> None:
        super().__init__(device, cmd_syntax)
