"""The pause commands module.

These commands are used in the following models:
DPO4K, DPO4KB, LPD6, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2, MSO4, MSO4B, MSO4K, MSO4KB, MSO5,
MSO5B, MSO5LP, MSO6, MSO6B, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - PAUSe <NR3>
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
        - PAUSe <NR3>
        ```

    Info:
        - ``<NR3>`` is the specified number of seconds the interface is to pause before processing
          any other commands. The pause time is specified as a floating point value in seconds and
          must be > 0.0 and ≥1800.0.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "PAUSe") -> None:
        super().__init__(device, cmd_syntax)
