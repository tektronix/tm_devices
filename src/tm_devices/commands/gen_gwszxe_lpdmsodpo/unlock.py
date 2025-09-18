"""The unlock commands module.

These commands are used in the following models:
DPO7AX, LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - UNLock ALL
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Unlock(SCPICmdWrite):
    """The ``UNLock`` command.

    Description:
        - This command (no query form) unlocks the front panel controls only. To unlock the front
          panel controls and the touch screen use the LOCk NONe command. The command
          ``TOUCHSCReen:STATE ON`` enables the touch screen only. Note: If the instrument is in the
          Remote With Lockout State (RWLS), the ``UNLock`` command has no effect. For more
          information, see the ANSI-IEEE Std 488.1-1987Standard Digital Interface for Programmable
          Instrumentation, section 2.8.3 on RL State Descriptions.

    Usage:
        - Using the ``.write(value)`` method will send the ``UNLock value`` command.

    SCPI Syntax:
        ```
        - UNLock ALL
        ```

    Info:
        - ``ALL`` specifies that all front panel buttons and knobs are unlocked.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "UNLock") -> None:
        super().__init__(device, cmd_syntax)
