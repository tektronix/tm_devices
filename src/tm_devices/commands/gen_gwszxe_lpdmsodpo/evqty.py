"""The evqty commands module.

These commands are used in the following models:
DPO7AX, LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - EVQty?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Evqty(SCPICmdRead):
    """The ``EVQty`` command.

    Description:
        - This query-only command returns the number of events that are enabled in the queue. This
          is useful when using the ALLEv? query, since it lets you know exactly how many events will
          be returned.

    Usage:
        - Using the ``.query()`` method will send the ``EVQty?`` query.
        - Using the ``.verify(value)`` method will send the ``EVQty?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - EVQty?
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "EVQty") -> None:
        super().__init__(device, cmd_syntax)
