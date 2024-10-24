# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The beeper commands module.

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
class Beeper(BaseTSPCmd):
    """The ``beeper`` command tree.

    Constants:
        - ``.OFF``: This command turns the beeper off.
        - ``.ON``: This command turns the beeper on.
    """

    OFF = "beeper.OFF"
    """str: This command turns the beeper off."""
    ON = "beeper.ON"
    """str: This command turns the beeper on."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "beeper") -> None:
        super().__init__(device, cmd_syntax)
