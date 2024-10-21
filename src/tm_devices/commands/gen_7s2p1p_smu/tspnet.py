# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The tspnet commands module.

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
class Tspnet(BaseTSPCmd):
    """The ``tspnet`` command tree.

    Constants:
        - ``.TERM_CR``: Set the device line termination sequence to CR.
        - ``.TERM_CRLF``: Set the device line termination sequence to CRLF.
        - ``.TERM_LF``: Set the device line termination sequence to LF.
        - ``.TERM_LFCR``: Set the device line termination sequence to LFCR.
    """

    TERM_CR = "tspnet.TERM_CR"
    """str: Set the device line termination sequence to CR."""
    TERM_CRLF = "tspnet.TERM_CRLF"
    """str: Set the device line termination sequence to CRLF."""
    TERM_LF = "tspnet.TERM_LF"
    """str: Set the device line termination sequence to LF."""
    TERM_LFCR = "tspnet.TERM_LFCR"
    """str: Set the device line termination sequence to LFCR."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "tspnet") -> None:
        super().__init__(device, cmd_syntax)
