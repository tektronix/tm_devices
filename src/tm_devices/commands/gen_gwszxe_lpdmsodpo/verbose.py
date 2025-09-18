"""The verbose commands module.

These commands are used in the following models:
DPO7AX, LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - VERBose {ON|OFF|<NR1>}
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Verbose(SCPICmdWrite):
    """The ``VERBose`` command.

    Description:
        - This command sets or queries the Verbose state that controls the length of keywords on
          query responses. Keywords can be both headers and arguments.

    Usage:
        - Using the ``.write(value)`` method will send the ``VERBose value`` command.

    SCPI Syntax:
        ```
        - VERBose {ON|OFF|<NR1>}
        ```

    Info:
        - ``<NR1>`` = 0 disables Verbose, any other value enables Verbose.
        - ``OFF`` sets the Verbose state to false, which returns minimum-length keywords for
          applicable setting queries.
        - ``ON`` sets the Verbose state to true, which returns full-length keywords for applicable
          setting queries.
        - ``0`` returns minimum-length keywords for applicable setting queries; any other value
          returns full-length keywords.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "VERBose") -> None:
        super().__init__(device, cmd_syntax)
