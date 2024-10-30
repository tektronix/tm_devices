"""The reboot commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - REBOOT
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Reboot(SCPICmdWriteNoArguments):
    """The ``REBOOT`` command.

    Description:
        - Reboots the system after a short delay, emulating the front panel power button push. The
          system will power back on after a 5 second delay.

    Usage:
        - Using the ``.write()`` method will send the ``REBOOT`` command.

    SCPI Syntax:
        ```
        - REBOOT
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "REBOOT") -> None:
        super().__init__(device, cmd_syntax)
