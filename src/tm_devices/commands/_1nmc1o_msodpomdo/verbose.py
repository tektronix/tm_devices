"""The verbose commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2K, MSO2KB, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:

::

    - VERBose {OFF|ON|<NR1>}
"""
from typing import Optional, TYPE_CHECKING

from .._helpers import SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.drivers.pi.pi_device import PIDevice


class Verbose(SCPICmdWrite):
    """The ``VERBose`` command.

    **Description:**
        - This command specifies the Verbose state that controls the length of keywords on query
          responses. Keywords can be both headers and arguments.

    **Usage:**
        - Using the ``.write(value)`` method will send the ``VERBose value`` command.

    **SCPI Syntax:**

    ::

        - VERBose {OFF|ON|<NR1>}

    **Info:**
        - ``OFF`` sets the Verbose state to false, which returns minimum-length keywords for
          applicable setting queries.
        - ``ON`` sets the Verbose state to true, which returns full-length keywords for applicable
          setting queries.
        - ``<NR1>`` a 0 returns minimum-length keywords for applicable setting queries; any other
          value returns full-length keywords.
    """

    def __init__(self, device: Optional["PIDevice"] = None, cmd_syntax: str = "VERBose") -> None:
        super().__init__(device, cmd_syntax)
