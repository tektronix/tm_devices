"""The abort commands module.

These commands are used in the following models:
AWG5200

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - ABORt [{ATRigger|BTRigger}]
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Abort(SCPICmdWrite):
    """The ``ABORt`` command.

    Description:
        - This command stops waveform playout when the Run Mode is set to Gated. This is equivalent
          to releasing the Force Trig button on the front panel when the instrument is in gated
          mode.

    Usage:
        - Using the ``.write(value)`` method will send the ``ABORt value`` command.

    SCPI Syntax:
        ```
        - ABORt [{ATRigger|BTRigger}]
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "ABORt") -> None:
        super().__init__(device, cmd_syntax)
