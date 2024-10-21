"""The clearmenu commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2K, MSO2KB, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CLEARMenu
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Clearmenu(SCPICmdWriteNoArguments):
    """The ``CLEARMenu`` command.

    Description:
        - Clears the current menu from the display. This command is equivalent to pressing the front
          panel Menu off.

    Usage:
        - Using the ``.write()`` method will send the ``CLEARMenu`` command.

    SCPI Syntax:
        ```
        - CLEARMenu
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "CLEARMenu") -> None:
        super().__init__(device, cmd_syntax)
