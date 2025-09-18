"""The autosaveuitimeout commands module.

These commands are used in the following models:
DPO7AX, LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - AUTOSAVEUITIMEOUT <NR1>
    - AUTOSAVEUITIMEOUT?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Autosaveuitimeout(SCPICmdWrite, SCPICmdRead):
    """The ``AUTOSAVEUITIMEOUT`` command.

    Description:
        - This command sets or queries the idle time from the user interface before auto-save
          occurs.

    Usage:
        - Using the ``.query()`` method will send the ``AUTOSAVEUITIMEOUT?`` query.
        - Using the ``.verify(value)`` method will send the ``AUTOSAVEUITIMEOUT?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUTOSAVEUITIMEOUT value`` command.

    SCPI Syntax:
        ```
        - AUTOSAVEUITIMEOUT <NR1>
        - AUTOSAVEUITIMEOUT?
        ```

    Info:
        - ``<NR1>`` sets the timeout time.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "AUTOSAVEUITIMEOUT"
    ) -> None:
        super().__init__(device, cmd_syntax)
