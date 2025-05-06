"""The scopeappreboot commands module.

These commands are used in the following models:
LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SCOPEAppREBOOT SCOPEApp REBOOT
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Scopeappreboot(SCPICmdWrite):
    """The ``SCOPEAppREBOOT`` command.

    Description:
        - This command reboots the scope.

    Usage:
        - Using the ``.write(value)`` method will send the ``SCOPEAppREBOOT value`` command.

    SCPI Syntax:
        ```
        - SCOPEAppREBOOT SCOPEApp REBOOT
        ```
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "SCOPEAppREBOOT"
    ) -> None:
        super().__init__(device, cmd_syntax)
