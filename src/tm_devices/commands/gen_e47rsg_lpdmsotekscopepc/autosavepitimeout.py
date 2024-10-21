"""The autosavepitimeout commands module.

These commands are used in the following models:
LPD6, MSO2, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - AUTOSAVEPITIMEOUT <NR1>
    - AUTOSAVEPITIMEOUT?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Autosavepitimeout(SCPICmdWrite, SCPICmdRead):
    """The ``AUTOSAVEPITIMEOUT`` command.

    Description:
        - This command sets or queries the idle time from the programmable interface before
          auto-save occurs.

    Usage:
        - Using the ``.query()`` method will send the ``AUTOSAVEPITIMEOUT?`` query.
        - Using the ``.verify(value)`` method will send the ``AUTOSAVEPITIMEOUT?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUTOSAVEPITIMEOUT value`` command.

    SCPI Syntax:
        ```
        - AUTOSAVEPITIMEOUT <NR1>
        - AUTOSAVEPITIMEOUT?
        ```

    Info:
        - ``<NR1>``
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "AUTOSAVEPITIMEOUT"
    ) -> None:
        super().__init__(device, cmd_syntax)
