"""The set commands module.

These commands are used in the following models:
DPO7AX, LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SET?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Set(SCPICmdRead):
    """The ``SET`` command.

    Description:
        - This query-only command returns the commands that list the instrument settings, except for
          configuration information for the calibration values. You can use these commands to return
          the instrument to the state it was in when you made the ``SET?`` query. The ``SET?`` query
          always returns command headers, regardless of the setting of the HEADer command. This is
          because the returned commands are intended to be sent back to the instrument as a command
          string. The VERBose command can still be used to specify whether the returned headers
          should be abbreviated or full-length. This command is identical to the ``*LRN?`` command.

    Usage:
        - Using the ``.query()`` method will send the ``SET?`` query.
        - Using the ``.verify(value)`` method will send the ``SET?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SET?
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SET") -> None:
        super().__init__(device, cmd_syntax)
