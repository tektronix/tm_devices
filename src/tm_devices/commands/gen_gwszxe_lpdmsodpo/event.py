"""The event commands module.

These commands are used in the following models:
DPO7AX, LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - EVENT?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Event(SCPICmdRead):
    """The ``EVENT`` command.

    Description:
        - This query-only command returns an event code from the Event Queue that provides
          information about the results of the last ``*ESR?`` read. ``EVENT?`` also removes the
          returned value from the Event Queue.

    Usage:
        - Using the ``.query()`` method will send the ``EVENT?`` query.
        - Using the ``.verify(value)`` method will send the ``EVENT?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - EVENT?
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "EVENT") -> None:
        super().__init__(device, cmd_syntax)
