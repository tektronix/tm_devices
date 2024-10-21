# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The smu commands module.

These commands are used in the following models:
DAQ6510, DMM6500, DMM7510

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


# pylint: disable=too-few-public-methods
class Smu(BaseTSPCmd):
    """The ``smu`` command tree.

    Constants:
        - ``.AUDIBLE_FAIL``: Beeper sound on test failure.
        - ``.AUDIBLE_NONE``: Beeper never sounds.
        - ``.AUDIBLE_PASS``: Beeper sound on test pass.
        - ``.OFF``: Allow the output to be turned on when the interlock is not engaged.
        - ``.ON``: Only allow the output to be turned on if the interlock is engaged.
    """

    AUDIBLE_FAIL = "smu.AUDIBLE_FAIL"
    """str: Beeper sound on test failure."""
    AUDIBLE_NONE = "smu.AUDIBLE_NONE"
    """str: Beeper never sounds."""
    AUDIBLE_PASS = "smu.AUDIBLE_PASS"
    """str: Beeper sound on test pass."""
    OFF = "smu.OFF"
    """str: Allow the output to be turned on when the interlock is not engaged."""
    ON = "smu.ON"
    """str: Only allow the output to be turned on if the interlock is engaged."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "smu") -> None:
        super().__init__(device, cmd_syntax)
