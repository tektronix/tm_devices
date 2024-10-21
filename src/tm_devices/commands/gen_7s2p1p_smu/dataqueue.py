# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The dataqueue commands module.

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
class Dataqueue(BaseTSPCmd):
    """The ``dataqueue`` command tree.

    Constants:
        - ``.CAPACITY``: The maximum number of entries that you can store in the data queue.
    """

    CAPACITY = "dataqueue.CAPACITY"
    """str: The maximum number of entries that you can store in the data queue."""

    def __init__(
        self, device: Optional["TSPControl"] = None, cmd_syntax: str = "dataqueue"
    ) -> None:
        super().__init__(device, cmd_syntax)
