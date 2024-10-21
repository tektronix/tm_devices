# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The format commands module.

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
class Format(BaseTSPCmd):
    """The ``format`` command tree.

    Constants:
        - ``.ASCII``: Sets the data format for data that is printed using the printnumber() and
          printbuffer() functions to be ASCII format.
        - ``.BIGENDIAN``: Sets the binary byte order for the data that is printed using the
          printnumber() and
          printbuffer() functions to be most significant byte first.
        - ``.DREAL``: Sets the data format for data that is printed using the printnumber() and
          printbuffer() functions to be double-precision IEEE Std 754 binary format.
        - ``.LITTLEENDIAN``: Sets the binary byte order for the data that is printed using the
          printnumber() and
          printbuffer() functions to be least significant byte first.
        - ``.NETWORK``: Sets the binary byte order for the data that is printed using the
          printnumber() and
          printbuffer() functions to be most significant byte first.
        - ``.NORMAL``: Sets the binary byte order for the data that is printed using the
          printnumber() and
          printbuffer() functions to be most significant byte first.
        - ``.REAL``: Sets the data format for data that is printed using the printnumber() and
          printbuffer() functions to be double-precision IEEE Std 754 binary format.
        - ``.REAL32``: Sets the data format for data that is printed using the printnumber() and
          printbuffer() functions to be single-precision IEEE Std 754 binary format.
        - ``.REAL64``: Sets the data format for data that is printed using the printnumber() and
          printbuffer() functions to be double-precision IEEE Std 754 binary format.
        - ``.SREAL``: Sets the data format for data that is printed using the printnumber() and
          printbuffer() functions to be single-precision IEEE Std 754 binary format.
        - ``.SWAPPED``: Sets the binary byte order for the data that is printed using the
          printnumber() and
          printbuffer() functions to be least significant byte first.
    """

    ASCII = "format.ASCII"
    """str: Sets the data format for data that is printed using the printnumber() and
printbuffer() functions to be ASCII format."""
    BIGENDIAN = "format.BIGENDIAN"
    """str: Sets the binary byte order for the data that is printed using the printnumber() and
printbuffer() functions to be most significant byte first."""
    DREAL = "format.DREAL"
    """str: Sets the data format for data that is printed using the printnumber() and
printbuffer() functions to be double-precision IEEE Std 754 binary format."""
    LITTLEENDIAN = "format.LITTLEENDIAN"
    """str: Sets the binary byte order for the data that is printed using the printnumber() and
printbuffer() functions to be least significant byte first."""
    NETWORK = "format.NETWORK"
    """str: Sets the binary byte order for the data that is printed using the printnumber() and
printbuffer() functions to be most significant byte first."""
    NORMAL = "format.NORMAL"
    """str: Sets the binary byte order for the data that is printed using the printnumber() and
printbuffer() functions to be most significant byte first."""
    REAL = "format.REAL"
    """str: Sets the data format for data that is printed using the printnumber() and
printbuffer() functions to be double-precision IEEE Std 754 binary format."""
    REAL32 = "format.REAL32"
    """str: Sets the data format for data that is printed using the printnumber() and
printbuffer() functions to be single-precision IEEE Std 754 binary format."""
    REAL64 = "format.REAL64"
    """str: Sets the data format for data that is printed using the printnumber() and
printbuffer() functions to be double-precision IEEE Std 754 binary format."""
    SREAL = "format.SREAL"
    """str: Sets the data format for data that is printed using the printnumber() and
printbuffer() functions to be single-precision IEEE Std 754 binary format."""
    SWAPPED = "format.SWAPPED"
    """str: Sets the binary byte order for the data that is printed using the printnumber() and
printbuffer() functions to be least significant byte first."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "format") -> None:
        super().__init__(device, cmd_syntax)
