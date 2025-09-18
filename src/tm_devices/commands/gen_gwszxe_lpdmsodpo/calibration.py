"""The calibration commands module.

These commands are used in the following models:
DPO7AX, LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - *CAL?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Cal(SCPICmdRead):
    """The ``*CAL`` command.

    Description:
        - This query-only command starts signal path calibration (SPC) and returns the status upon
          completion. Note: When running SPC through the remote interface, calibration status cannot
          be obtained until after the SPC completes. SPC takes approximately 15 minutes per channel
          which means a total of 2 hours on an 8-channel model. Any remote command that performs an
          action on the instrument is also disabled until the SPC is complete.

    Usage:
        - Using the ``.query()`` method will send the ``*CAL?`` query.
        - Using the ``.verify(value)`` method will send the ``*CAL?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - *CAL?
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*CAL") -> None:
        super().__init__(device, cmd_syntax)
