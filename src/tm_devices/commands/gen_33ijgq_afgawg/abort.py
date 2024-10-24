"""The abort commands module.

These commands are used in the following models:
AFG3K, AFG3KB, AFG3KC, AWG5K, AWG5KC, AWG7K, AWG7KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - ABORt
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Abort(SCPICmdWriteNoArguments):
    """The ``ABORt`` command.

    Description:
        - Initializes all the current trigger system parameters and resets all trigger sequences.

    Usage:
        - Using the ``.write()`` method will send the ``ABORt`` command.

    SCPI Syntax:
        ```
        - ABORt
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "ABORt") -> None:
        super().__init__(device, cmd_syntax)
