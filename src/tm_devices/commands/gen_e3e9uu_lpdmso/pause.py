"""The pause commands module.

These commands are used in the following models:
LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - PAUSe PEAKSTABle:ADDNew <QString>
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Pause(SCPICmdWrite):
    """The ``PAUSe`` command.

    Description:
        - This command causes the interface to pause the specified number of seconds before
          processing any other commands.

    Usage:
        - Using the ``.write(value)`` method will send the ``PAUSe value`` command.

    SCPI Syntax:
        ```
        - PAUSe PEAKSTABle:ADDNew <QString>
        ```

    Info:
        - ``<QString>`` is a quoted string that is the name of the new peak markers table. The
          argument is of the form “.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "PAUSe") -> None:
        super().__init__(device, cmd_syntax)
