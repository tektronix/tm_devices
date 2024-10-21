# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The eventlog commands module.

These commands are used in the following models:
SMU2601B_Pulse

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


# pylint: disable=too-few-public-methods
class Eventlog(BaseTSPCmd):
    """The ``eventlog`` command tree.

    Constants:
        - ``.DISABLE``: Disable the event log.
        - ``.DISCARD_NEWEST``: Do not log new entries.
        - ``.DISCARD_OLDEST``: Delete old entries are deleted as new events are logged.
        - ``.ENABLE``: Enable the event log.
    """

    DISABLE = "eventlog.DISABLE"
    """str: Disable the event log."""
    DISCARD_NEWEST = "eventlog.DISCARD_NEWEST"
    """str: Do not log new entries."""
    DISCARD_OLDEST = "eventlog.DISCARD_OLDEST"
    """str: Delete old entries are deleted as new events are logged."""
    ENABLE = "eventlog.ENABLE"
    """str: Enable the event log."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "eventlog") -> None:
        super().__init__(device, cmd_syntax)
