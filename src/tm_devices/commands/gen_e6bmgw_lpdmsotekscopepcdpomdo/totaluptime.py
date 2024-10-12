"""The totaluptime commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, LPD6, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2, MSO2K, MSO2KB, MSO4,
MSO4B, MSO4K, MSO4KB, MSO5, MSO5B, MSO5LP, MSO6, MSO6B, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - TOTaluptime?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Totaluptime(SCPICmdRead):
    """The ``TOTaluptime`` command.

    Description:
        - Total number of hours the instrument has been turned on since the NV memory was last
          programmed, usually during the initial manufacturing process.

    Usage:
        - Using the ``.query()`` method will send the ``TOTaluptime?`` query.
        - Using the ``.verify(value)`` method will send the ``TOTaluptime?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TOTaluptime?
        ```
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "TOTaluptime"
    ) -> None:
        super().__init__(device, cmd_syntax)
