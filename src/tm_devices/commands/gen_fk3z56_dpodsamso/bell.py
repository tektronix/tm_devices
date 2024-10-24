"""The bell commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - BELl
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Bell(SCPICmdWriteNoArguments):
    """The ``BELl`` command.

    Description:
        - This command was previously used to beep an audio indicator and is provided for backward
          compatibility.

    Usage:
        - Using the ``.write()`` method will send the ``BELl`` command.

    SCPI Syntax:
        ```
        - BELl
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "BELl") -> None:
        super().__init__(device, cmd_syntax)
