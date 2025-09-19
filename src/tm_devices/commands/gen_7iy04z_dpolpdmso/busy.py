"""The busy commands module.

These commands are used in the following models:
DPO7AX, LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - BUSY?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Busy(SCPICmdRead):
    """The ``BUSY`` command.

    Description:
        - This query-only command returns the status of the instrument. This command allows you to
          synchronize the operation of the instrument with your application program.

    Usage:
        - Using the ``.query()`` method will send the ``BUSY?`` query.
        - Using the ``.verify(value)`` method will send the ``BUSY?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - BUSY?
        ```

    Info:
        - ``<NR1> = 0`` means that the instrument is not busy processing a command whose execution
          time is extensive.
        - ``<NR1> = 1`` means that the instrument is busy processing Commands that Generate an OPC
          Message.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "BUSY") -> None:
        super().__init__(device, cmd_syntax)
