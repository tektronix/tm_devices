"""The cursor commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CURSor:FUNCtion {OFF|HBArs|VBArs|SCREEN|WAVEform}
    - CURSor:FUNCtion?
    - CURSor:HBArs:DELTa?
    - CURSor:HBArs:POSITION<x> <NR3>
    - CURSor:HBArs:POSITION<x>?
    - CURSor:HBArs:UNIts?
    - CURSor:HBArs?
    - CURSor:LINESTyle {DASHed|SDASHed|SOLID}
    - CURSor:LINESTyle?
    - CURSor:MODe {TRACk|INDependent}
    - CURSor:MODe?
    - CURSor:SCREEN:STYle {LINE_X|LINES|X}
    - CURSor:SCREEN:STYle?
    - CURSor:SCREEN:XPOSITION<x> <NR3>
    - CURSor:SCREEN:XPOSITION<x>?
    - CURSor:SCREEN:YPOSITION<x> <NR3>
    - CURSor:SCREEN:YPOSITION<x>?
    - CURSor:SOUrce1 {CH<x>|MATH<x>|REF1|REF1|REF3|REF4}
    - CURSor:SOUrce1?
    - CURSor:STATE {ON|OFF|<NR1>}
    - CURSor:STATE?
    - CURSor:VBArs SNAp
    - CURSor:VBArs:DELTa?
    - CURSor:VBArs:POS<x> <NR3>
    - CURSor:VBArs:POS<x>?
    - CURSor:VBArs:POSITION<x> <NR3>
    - CURSor:VBArs:POSITION<x>?
    - CURSor:VBArs:UNIts {SECOnds|HERtz}
    - CURSor:VBArs:UNIts?
    - CURSor:VBArs?
    - CURSor:WAVEform SNAp
    - CURSor:WAVEform:HDELTA?
    - CURSor:WAVEform:HPOS<x>?
    - CURSor:WAVEform:POSition<x> {<NR3>}
    - CURSor:WAVEform:POSition<x>?
    - CURSor:WAVEform:SOUrce1 {CH<x>|MATH<x>|REF<x>}
    - CURSor:WAVEform:SOUrce1?
    - CURSor:WAVEform:STYle {LINE_X|LINES|X}
    - CURSor:WAVEform:STYle?
    - CURSor:WAVEform:UNIts BASe
    - CURSor:WAVEform:UNIts?
    - CURSor:WAVEform:VDELTA?
    - CURSor:WAVEform?
    - CURSor:XY:PRODDELta?
    - CURSor:XY:PRODUCT<x>?
    - CURSor:XY:RADIUS<x>?
    - CURSor:XY:RATDELta?
    - CURSor:XY:RATIO<x>?
    - CURSor:XY:RDELta?
    - CURSor:XY:READOUT {RATio|RECTangular|POLARCoord|PRODuct}
    - CURSor:XY:READOUT?
    - CURSor:XY:RECTX<x> {<NR3>}
    - CURSor:XY:RECTX<x>?
    - CURSor:XY:RECTY<x> {<NR3>}
    - CURSor:XY:RECTY<x>?
    - CURSor:XY:THDELta?
    - CURSor:XY:THETA<x>?
    - CURSor:XY:XDELta?
    - CURSor:XY:YDELta?
    - CURSor:XY?
    - CURSor?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class CursorXyYdelta(SCPICmdRead):
    """The ``CURSor:XY:YDELta`` command.

    Description:
        - This query-only command returns the XY cursor Y delta value in rectangular coordinates.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:YDELta?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:YDELta?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY:YDELta?
        ```
    """


class CursorXyXdelta(SCPICmdRead):
    """The ``CURSor:XY:XDELta`` command.

    Description:
        - This query-only command returns the XY cursor X delta value in rectangular coordinates.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:XDELta?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:XDELta?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY:XDELta?
        ```
    """


class CursorXyThetaItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``CURSor:XY:THETA<x>`` command.

    Description:
        - This query-only command returns the XY cursor angle in polar coordinates. The cursor is
          specified by x, which can be 1 or 2.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:THETA<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:THETA<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY:THETA<x>?
        ```
    """


class CursorXyThdelta(SCPICmdRead):
    """The ``CURSor:XY:THDELta`` command.

    Description:
        - This query-only command returns the XY cursor angle delta in polar coordinates.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:THDELta?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:THDELta?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY:THDELta?
        ```
    """


class CursorXyRectyItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:XY:RECTY<x>`` command.

    Description:
        - This command sets or queries the Y cursor position in rectangular coordinates. The cursor
          is specified by x, which can be 1 or 2.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:RECTY<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:RECTY<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CURSor:XY:RECTY<x> value`` command.

    SCPI Syntax:
        ```
        - CURSor:XY:RECTY<x> {<NR3>}
        - CURSor:XY:RECTY<x>?
        ```

    Info:
        - ``<NR3>`` is the Y position of the specified cursor in rectangular coordinates.
    """


class CursorXyRectxItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:XY:RECTX<x>`` command.

    Description:
        - This command sets or queries the X cursor position in rectangular coordinates. The cursor
          is specified by x, which can be 1 or 2.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:RECTX<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:RECTX<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CURSor:XY:RECTX<x> value`` command.

    SCPI Syntax:
        ```
        - CURSor:XY:RECTX<x> {<NR3>}
        - CURSor:XY:RECTX<x>?
        ```

    Info:
        - ``<NR3>`` is the X position of the specified cursor in rectangular coordinates.
    """


class CursorXyReadout(SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:XY:READOUT`` command.

    Description:
        - This command sets or queries the XY cursor readout (available when ``DISplay:FORMat`` is
          set to XY).

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:READOUT?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:READOUT?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CURSor:XY:READOUT value`` command.

    SCPI Syntax:
        ```
        - CURSor:XY:READOUT {RATio|RECTangular|POLARCoord|PRODuct}
        - CURSor:XY:READOUT?
        ```

    Info:
        - ``POLARCoord`` displays the following values: r1, r2, Δr, q1, q2, Δq, t1, t2, Δt.
        - ``PRODuct`` displays the following values: X1 x Y1, X2 xY2, ΔX x ΔY, t1, t2, ΔDt.
        - ``RATio`` displays the following values: Y1 ¸ X1, Y2 ¸ X2, ΔY ¸ x ΔX, t1, t2, Δt.
        - ``RECTangular`` displays the following values: X1, X2, ΔX, Y1, Y2, ΔY, t1, t2, Δt.
    """


class CursorXyRdelta(SCPICmdRead):
    """The ``CURSor:XY:RDELta`` command.

    Description:
        - This query-only command returns the delta radius (Δr) value when the ``CURSOR:XY:READOUT``
          is set to POLARCoord.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:RDELta?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:RDELta?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY:RDELta?
        ```
    """


class CursorXyRatioItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``CURSor:XY:RATIO<x>`` command.

    Description:
        - This query-only command returns ratio the of the X (horizontal) and Y (vertical) position
          for the specified cursor when the ``CURSor:XY:READOUT`` is set to RATio. The cursor is
          specified by x, which can be 1 or 2. The ratio is calculated as Y ÷ X.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:RATIO<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:RATIO<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY:RATIO<x>?
        ```
    """


class CursorXyRatdelta(SCPICmdRead):
    """The ``CURSor:XY:RATDELta`` command.

    Description:
        - This query-only command returns ratio of the difference between the cursors X position and
          Y position (ΔY ¸ ΔX) when the ``CURSor:XY:READOUT`` is set to RATio. The ratio is
          calculated as (Cursor 2 Y - Cursor 1 Y) ÷ (Cursor 2 X - Cursor 1 X).

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:RATDELta?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:RATDELta?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY:RATDELta?
        ```
    """


class CursorXyRadiusItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``CURSor:XY:RADIUS<x>`` command.

    Description:
        - This query-only command returns the radius of the specified cursor when the
          ``CURSor:XY:READOUT`` is set to POLARCoord. The cursor is specified by x, which can be 1
          or 2.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:RADIUS<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:RADIUS<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY:RADIUS<x>?
        ```
    """


class CursorXyProductItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``CURSor:XY:PRODUCT<x>`` command.

    Description:
        - This query-only command returns the product of the X and Y positions for the specified
          cursor when the ``CURSor:XY:READOUT`` is set to PRODuct. The cursor is specified by x,
          which can be 1 or 2.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:PRODUCT<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:PRODUCT<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY:PRODUCT<x>?
        ```
    """


class CursorXyProddelta(SCPICmdRead):
    """The ``CURSor:XY:PRODDELta`` command.

    Description:
        - This query-only command returns the product of the difference between the cursors X
          positions and Y positions when the ``CURSor:XY:READOUT`` is set to PRODuct. The ΔX × ΔY
          value is calculated as (Cursor 2 X - Cursor 1 X) × (Cursor 2 Y - Cursor 1 Y).

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:PRODDELta?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:PRODDELta?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY:PRODDELta?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class CursorXy(SCPICmdRead):
    """The ``CURSor:XY`` command.

    Description:
        - This query-only command returns all of the XY cursor parameters.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY?
        ```

    Properties:
        - ``.proddelta``: The ``CURSor:XY:PRODDELta`` command.
        - ``.product``: The ``CURSor:XY:PRODUCT<x>`` command.
        - ``.radius``: The ``CURSor:XY:RADIUS<x>`` command.
        - ``.ratdelta``: The ``CURSor:XY:RATDELta`` command.
        - ``.ratio``: The ``CURSor:XY:RATIO<x>`` command.
        - ``.rdelta``: The ``CURSor:XY:RDELta`` command.
        - ``.readout``: The ``CURSor:XY:READOUT`` command.
        - ``.rectx``: The ``CURSor:XY:RECTX<x>`` command.
        - ``.recty``: The ``CURSor:XY:RECTY<x>`` command.
        - ``.thdelta``: The ``CURSor:XY:THDELta`` command.
        - ``.theta``: The ``CURSor:XY:THETA<x>`` command.
        - ``.xdelta``: The ``CURSor:XY:XDELta`` command.
        - ``.ydelta``: The ``CURSor:XY:YDELta`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._proddelta = CursorXyProddelta(device, f"{self._cmd_syntax}:PRODDELta")
        self._product: Dict[int, CursorXyProductItem] = DefaultDictPassKeyToFactory(
            lambda x: CursorXyProductItem(device, f"{self._cmd_syntax}:PRODUCT{x}")
        )
        self._radius: Dict[int, CursorXyRadiusItem] = DefaultDictPassKeyToFactory(
            lambda x: CursorXyRadiusItem(device, f"{self._cmd_syntax}:RADIUS{x}")
        )
        self._ratdelta = CursorXyRatdelta(device, f"{self._cmd_syntax}:RATDELta")
        self._ratio: Dict[int, CursorXyRatioItem] = DefaultDictPassKeyToFactory(
            lambda x: CursorXyRatioItem(device, f"{self._cmd_syntax}:RATIO{x}")
        )
        self._rdelta = CursorXyRdelta(device, f"{self._cmd_syntax}:RDELta")
        self._readout = CursorXyReadout(device, f"{self._cmd_syntax}:READOUT")
        self._rectx: Dict[int, CursorXyRectxItem] = DefaultDictPassKeyToFactory(
            lambda x: CursorXyRectxItem(device, f"{self._cmd_syntax}:RECTX{x}")
        )
        self._recty: Dict[int, CursorXyRectyItem] = DefaultDictPassKeyToFactory(
            lambda x: CursorXyRectyItem(device, f"{self._cmd_syntax}:RECTY{x}")
        )
        self._thdelta = CursorXyThdelta(device, f"{self._cmd_syntax}:THDELta")
        self._theta: Dict[int, CursorXyThetaItem] = DefaultDictPassKeyToFactory(
            lambda x: CursorXyThetaItem(device, f"{self._cmd_syntax}:THETA{x}")
        )
        self._xdelta = CursorXyXdelta(device, f"{self._cmd_syntax}:XDELta")
        self._ydelta = CursorXyYdelta(device, f"{self._cmd_syntax}:YDELta")

    @property
    def proddelta(self) -> CursorXyProddelta:
        """Return the ``CURSor:XY:PRODDELta`` command.

        Description:
            - This query-only command returns the product of the difference between the cursors X
              positions and Y positions when the ``CURSor:XY:READOUT`` is set to PRODuct. The ΔX ×
              ΔY value is calculated as (Cursor 2 X - Cursor 1 X) × (Cursor 2 Y - Cursor 1 Y).

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:PRODDELta?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:PRODDELta?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY:PRODDELta?
            ```
        """
        return self._proddelta

    @property
    def product(self) -> Dict[int, CursorXyProductItem]:
        """Return the ``CURSor:XY:PRODUCT<x>`` command.

        Description:
            - This query-only command returns the product of the X and Y positions for the specified
              cursor when the ``CURSor:XY:READOUT`` is set to PRODuct. The cursor is specified by x,
              which can be 1 or 2.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:PRODUCT<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:PRODUCT<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY:PRODUCT<x>?
            ```
        """
        return self._product

    @property
    def radius(self) -> Dict[int, CursorXyRadiusItem]:
        """Return the ``CURSor:XY:RADIUS<x>`` command.

        Description:
            - This query-only command returns the radius of the specified cursor when the
              ``CURSor:XY:READOUT`` is set to POLARCoord. The cursor is specified by x, which can be
              1 or 2.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:RADIUS<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:RADIUS<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY:RADIUS<x>?
            ```
        """
        return self._radius

    @property
    def ratdelta(self) -> CursorXyRatdelta:
        """Return the ``CURSor:XY:RATDELta`` command.

        Description:
            - This query-only command returns ratio of the difference between the cursors X position
              and Y position (ΔY ¸ ΔX) when the ``CURSor:XY:READOUT`` is set to RATio. The ratio is
              calculated as (Cursor 2 Y - Cursor 1 Y) ÷ (Cursor 2 X - Cursor 1 X).

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:RATDELta?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:RATDELta?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY:RATDELta?
            ```
        """
        return self._ratdelta

    @property
    def ratio(self) -> Dict[int, CursorXyRatioItem]:
        """Return the ``CURSor:XY:RATIO<x>`` command.

        Description:
            - This query-only command returns ratio the of the X (horizontal) and Y (vertical)
              position for the specified cursor when the ``CURSor:XY:READOUT`` is set to RATio. The
              cursor is specified by x, which can be 1 or 2. The ratio is calculated as Y ÷ X.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:RATIO<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:RATIO<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY:RATIO<x>?
            ```
        """
        return self._ratio

    @property
    def rdelta(self) -> CursorXyRdelta:
        """Return the ``CURSor:XY:RDELta`` command.

        Description:
            - This query-only command returns the delta radius (Δr) value when the
              ``CURSOR:XY:READOUT`` is set to POLARCoord.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:RDELta?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:RDELta?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY:RDELta?
            ```
        """
        return self._rdelta

    @property
    def readout(self) -> CursorXyReadout:
        """Return the ``CURSor:XY:READOUT`` command.

        Description:
            - This command sets or queries the XY cursor readout (available when ``DISplay:FORMat``
              is set to XY).

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:READOUT?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:READOUT?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURSor:XY:READOUT value`` command.

        SCPI Syntax:
            ```
            - CURSor:XY:READOUT {RATio|RECTangular|POLARCoord|PRODuct}
            - CURSor:XY:READOUT?
            ```

        Info:
            - ``POLARCoord`` displays the following values: r1, r2, Δr, q1, q2, Δq, t1, t2, Δt.
            - ``PRODuct`` displays the following values: X1 x Y1, X2 xY2, ΔX x ΔY, t1, t2, ΔDt.
            - ``RATio`` displays the following values: Y1 ¸ X1, Y2 ¸ X2, ΔY ¸ x ΔX, t1, t2, Δt.
            - ``RECTangular`` displays the following values: X1, X2, ΔX, Y1, Y2, ΔY, t1, t2, Δt.
        """
        return self._readout

    @property
    def rectx(self) -> Dict[int, CursorXyRectxItem]:
        """Return the ``CURSor:XY:RECTX<x>`` command.

        Description:
            - This command sets or queries the X cursor position in rectangular coordinates. The
              cursor is specified by x, which can be 1 or 2.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:RECTX<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:RECTX<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURSor:XY:RECTX<x> value`` command.

        SCPI Syntax:
            ```
            - CURSor:XY:RECTX<x> {<NR3>}
            - CURSor:XY:RECTX<x>?
            ```

        Info:
            - ``<NR3>`` is the X position of the specified cursor in rectangular coordinates.
        """
        return self._rectx

    @property
    def recty(self) -> Dict[int, CursorXyRectyItem]:
        """Return the ``CURSor:XY:RECTY<x>`` command.

        Description:
            - This command sets or queries the Y cursor position in rectangular coordinates. The
              cursor is specified by x, which can be 1 or 2.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:RECTY<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:RECTY<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURSor:XY:RECTY<x> value`` command.

        SCPI Syntax:
            ```
            - CURSor:XY:RECTY<x> {<NR3>}
            - CURSor:XY:RECTY<x>?
            ```

        Info:
            - ``<NR3>`` is the Y position of the specified cursor in rectangular coordinates.
        """
        return self._recty

    @property
    def thdelta(self) -> CursorXyThdelta:
        """Return the ``CURSor:XY:THDELta`` command.

        Description:
            - This query-only command returns the XY cursor angle delta in polar coordinates.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:THDELta?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:THDELta?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY:THDELta?
            ```
        """
        return self._thdelta

    @property
    def theta(self) -> Dict[int, CursorXyThetaItem]:
        """Return the ``CURSor:XY:THETA<x>`` command.

        Description:
            - This query-only command returns the XY cursor angle in polar coordinates. The cursor
              is specified by x, which can be 1 or 2.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:THETA<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:THETA<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY:THETA<x>?
            ```
        """
        return self._theta

    @property
    def xdelta(self) -> CursorXyXdelta:
        """Return the ``CURSor:XY:XDELta`` command.

        Description:
            - This query-only command returns the XY cursor X delta value in rectangular
              coordinates.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:XDELta?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:XDELta?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY:XDELta?
            ```
        """
        return self._xdelta

    @property
    def ydelta(self) -> CursorXyYdelta:
        """Return the ``CURSor:XY:YDELta`` command.

        Description:
            - This query-only command returns the XY cursor Y delta value in rectangular
              coordinates.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:YDELta?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:YDELta?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY:YDELta?
            ```
        """
        return self._ydelta


class CursorWaveformVdelta(SCPICmdRead):
    """The ``CURSor:WAVEform:VDELTA`` command.

    Description:
        - This query-only command returns the vertical difference between the waveform cursors. This
          is the absolute value of the vertical position of the first cursor minus the vertical
          position of the second cursor. This is equivalent to the waveform delta-voltage readout
          value.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:WAVEform:VDELTA?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:WAVEform:VDELTA?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:WAVEform:VDELTA?
        ```
    """


class CursorWaveformUnits(SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:WAVEform:UNIts`` command.

    Description:
        - This command sets or queries the units for waveform cursors.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:WAVEform:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:WAVEform:UNIts?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CURSor:WAVEform:UNIts value`` command.

    SCPI Syntax:
        ```
        - CURSor:WAVEform:UNIts BASe
        - CURSor:WAVEform:UNIts?
        ```

    Info:
        - ``BASe`` sets cursor units to base.
    """


class CursorWaveformStyle(SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:WAVEform:STYle`` command.

    Description:
        - This command sets or queries the cursor type for Waveform mode.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:WAVEform:STYle?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:WAVEform:STYle?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CURSor:WAVEform:STYle value`` command.

    SCPI Syntax:
        ```
        - CURSor:WAVEform:STYle {LINE_X|LINES|X}
        - CURSor:WAVEform:STYle?
        ```

    Info:
        - ``LINE_X`` specifies the cursor style to be a line with superimposed X.
        - ``LINES`` specifies the cursor style to be a line.
        - ``X`` specifies the cursor style to be an X.
    """


class CursorWaveformSource1(SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:WAVEform:SOUrce1`` command.

    Description:
        - This command sets or queries the source for a waveform cursor. The cursor is specified by
          x, which can only be 2.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:WAVEform:SOUrce1?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:WAVEform:SOUrce1?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CURSor:WAVEform:SOUrce1 value``
          command.

    SCPI Syntax:
        ```
        - CURSor:WAVEform:SOUrce1 {CH<x>|MATH<x>|REF<x>}
        - CURSor:WAVEform:SOUrce1?
        ```

    Info:
        - ``CH<x>`` sets an input channel waveform as the cursor source. The valid channel waveform
          range is from 1 through 4.
        - ``MATH<x>`` sets a math waveform as the cursor source. The valid math waveform range is
          from 1 through 4.
        - ``REF<x>`` sets a reference waveform as the cursor source. The valid reference waveform
          range is from 1 through 4.
    """


class CursorWaveformPositionItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:WAVEform:POSition<x>`` command.

    Description:
        - This command sets or queries the position of a waveform cursor, which is constrained to be
          visible in the selected time base. (Use the ``CURSOR:FUNCTION`` command to set the cursor
          function to Waveform.) The cursor is specified by x, which can be 1 or 2. This is
          equivalent to setting a value in the Position control in the Cursor1 or Cursor2 sections
          of the Cursor Setup dialog box (when Waveform is selected in the Function section).

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:WAVEform:POSition<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:WAVEform:POSition<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CURSor:WAVEform:POSition<x> value``
          command.

    SCPI Syntax:
        ```
        - CURSor:WAVEform:POSition<x> {<NR3>}
        - CURSor:WAVEform:POSition<x>?
        ```

    Info:
        - ``<NR3>`` specifies the cursor position measured relative to the time of the trigger point
          of the source waveform.
    """


class CursorWaveformHposItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``CURSor:WAVEform:HPOS<x>`` command.

    Description:
        - This query-only command returns the position of the specified waveform cursor. The cursor
          is specified by x, which can be 1 or 2. This corresponds to the v1 or v2 (cursor 1 or
          cursor 2) cursor readout.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:WAVEform:HPOS<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:WAVEform:HPOS<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:WAVEform:HPOS<x>?
        ```
    """


class CursorWaveformHdelta(SCPICmdRead):
    """The ``CURSor:WAVEform:HDELTA`` command.

    Description:
        - This query-only command returns the horizontal difference between the waveform cursors.
          This is the absolute value of the horizontal position of the first cursor minus the
          horizontal position of the second cursor. This is equivalent to the waveform delta-time
          readout value.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:WAVEform:HDELTA?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:WAVEform:HDELTA?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:WAVEform:HDELTA?
        ```
    """


class CursorWaveform(SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:WAVEform`` command.

    Description:
        - This command sets or queries the current settings for the waveform cursors or forces them
          to snap to positions specified by the ``DATA:START`` and ``DATA:STOP`` commands.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:WAVEform?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:WAVEform?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CURSor:WAVEform value`` command.

    SCPI Syntax:
        ```
        - CURSor:WAVEform SNAp
        - CURSor:WAVEform?
        ```

    Info:
        - ``SNAp`` forces the position of waveform cursor 1 and 2 to snap to the waveform record
          points specified by the ``DATA:START`` and ``DATA:STOP`` commands, respectively.

    Properties:
        - ``.hdelta``: The ``CURSor:WAVEform:HDELTA`` command.
        - ``.hpos``: The ``CURSor:WAVEform:HPOS<x>`` command.
        - ``.position``: The ``CURSor:WAVEform:POSition<x>`` command.
        - ``.source1``: The ``CURSor:WAVEform:SOUrce1`` command.
        - ``.style``: The ``CURSor:WAVEform:STYle`` command.
        - ``.units``: The ``CURSor:WAVEform:UNIts`` command.
        - ``.vdelta``: The ``CURSor:WAVEform:VDELTA`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hdelta = CursorWaveformHdelta(device, f"{self._cmd_syntax}:HDELTA")
        self._hpos: Dict[int, CursorWaveformHposItem] = DefaultDictPassKeyToFactory(
            lambda x: CursorWaveformHposItem(device, f"{self._cmd_syntax}:HPOS{x}")
        )
        self._position: Dict[int, CursorWaveformPositionItem] = DefaultDictPassKeyToFactory(
            lambda x: CursorWaveformPositionItem(device, f"{self._cmd_syntax}:POSition{x}")
        )
        self._source1 = CursorWaveformSource1(device, f"{self._cmd_syntax}:SOUrce1")
        self._style = CursorWaveformStyle(device, f"{self._cmd_syntax}:STYle")
        self._units = CursorWaveformUnits(device, f"{self._cmd_syntax}:UNIts")
        self._vdelta = CursorWaveformVdelta(device, f"{self._cmd_syntax}:VDELTA")

    @property
    def hdelta(self) -> CursorWaveformHdelta:
        """Return the ``CURSor:WAVEform:HDELTA`` command.

        Description:
            - This query-only command returns the horizontal difference between the waveform
              cursors. This is the absolute value of the horizontal position of the first cursor
              minus the horizontal position of the second cursor. This is equivalent to the waveform
              delta-time readout value.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:WAVEform:HDELTA?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:WAVEform:HDELTA?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:WAVEform:HDELTA?
            ```
        """
        return self._hdelta

    @property
    def hpos(self) -> Dict[int, CursorWaveformHposItem]:
        """Return the ``CURSor:WAVEform:HPOS<x>`` command.

        Description:
            - This query-only command returns the position of the specified waveform cursor. The
              cursor is specified by x, which can be 1 or 2. This corresponds to the v1 or v2
              (cursor 1 or cursor 2) cursor readout.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:WAVEform:HPOS<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:WAVEform:HPOS<x>?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:WAVEform:HPOS<x>?
            ```
        """
        return self._hpos

    @property
    def position(self) -> Dict[int, CursorWaveformPositionItem]:
        """Return the ``CURSor:WAVEform:POSition<x>`` command.

        Description:
            - This command sets or queries the position of a waveform cursor, which is constrained
              to be visible in the selected time base. (Use the ``CURSOR:FUNCTION`` command to set
              the cursor function to Waveform.) The cursor is specified by x, which can be 1 or 2.
              This is equivalent to setting a value in the Position control in the Cursor1 or
              Cursor2 sections of the Cursor Setup dialog box (when Waveform is selected in the
              Function section).

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:WAVEform:POSition<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:WAVEform:POSition<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURSor:WAVEform:POSition<x> value``
              command.

        SCPI Syntax:
            ```
            - CURSor:WAVEform:POSition<x> {<NR3>}
            - CURSor:WAVEform:POSition<x>?
            ```

        Info:
            - ``<NR3>`` specifies the cursor position measured relative to the time of the trigger
              point of the source waveform.
        """
        return self._position

    @property
    def source1(self) -> CursorWaveformSource1:
        """Return the ``CURSor:WAVEform:SOUrce1`` command.

        Description:
            - This command sets or queries the source for a waveform cursor. The cursor is specified
              by x, which can only be 2.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:WAVEform:SOUrce1?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:WAVEform:SOUrce1?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURSor:WAVEform:SOUrce1 value``
              command.

        SCPI Syntax:
            ```
            - CURSor:WAVEform:SOUrce1 {CH<x>|MATH<x>|REF<x>}
            - CURSor:WAVEform:SOUrce1?
            ```

        Info:
            - ``CH<x>`` sets an input channel waveform as the cursor source. The valid channel
              waveform range is from 1 through 4.
            - ``MATH<x>`` sets a math waveform as the cursor source. The valid math waveform range
              is from 1 through 4.
            - ``REF<x>`` sets a reference waveform as the cursor source. The valid reference
              waveform range is from 1 through 4.
        """
        return self._source1

    @property
    def style(self) -> CursorWaveformStyle:
        """Return the ``CURSor:WAVEform:STYle`` command.

        Description:
            - This command sets or queries the cursor type for Waveform mode.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:WAVEform:STYle?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:WAVEform:STYle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURSor:WAVEform:STYle value``
              command.

        SCPI Syntax:
            ```
            - CURSor:WAVEform:STYle {LINE_X|LINES|X}
            - CURSor:WAVEform:STYle?
            ```

        Info:
            - ``LINE_X`` specifies the cursor style to be a line with superimposed X.
            - ``LINES`` specifies the cursor style to be a line.
            - ``X`` specifies the cursor style to be an X.
        """
        return self._style

    @property
    def units(self) -> CursorWaveformUnits:
        """Return the ``CURSor:WAVEform:UNIts`` command.

        Description:
            - This command sets or queries the units for waveform cursors.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:WAVEform:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:WAVEform:UNIts?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURSor:WAVEform:UNIts value``
              command.

        SCPI Syntax:
            ```
            - CURSor:WAVEform:UNIts BASe
            - CURSor:WAVEform:UNIts?
            ```

        Info:
            - ``BASe`` sets cursor units to base.
        """
        return self._units

    @property
    def vdelta(self) -> CursorWaveformVdelta:
        """Return the ``CURSor:WAVEform:VDELTA`` command.

        Description:
            - This query-only command returns the vertical difference between the waveform cursors.
              This is the absolute value of the vertical position of the first cursor minus the
              vertical position of the second cursor. This is equivalent to the waveform
              delta-voltage readout value.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:WAVEform:VDELTA?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:WAVEform:VDELTA?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:WAVEform:VDELTA?
            ```
        """
        return self._vdelta


class CursorVbarsUnits(SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:VBArs:UNIts`` command.

    Description:
        - This command sets or queries the units for the vertical bar cursors.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:VBArs:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:VBArs:UNIts?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CURSor:VBArs:UNIts value`` command.

    SCPI Syntax:
        ```
        - CURSor:VBArs:UNIts {SECOnds|HERtz}
        - CURSor:VBArs:UNIts?
        ```

    Info:
        - ``SECOnds`` sets the units of the vertical bar cursors for the time domain (seconds).
        - ``HERtz`` sets the units of the vertical bar cursors for the frequency domain (Hertz).
    """


class CursorVbarsPositionItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:VBArs:POSITION<x>`` command.

    Description:
        - This command specifies the horizontal position for the specified vertical bar cursor. The
          cursor is specified by <x>, which can be 1 or 2. Values are with respect to trigger
          position or the zero reference point for the designated waveform (if horizontal units are
          not set to time). Use the ``CURSOR:VBARS:UNITS`` command to specify units.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:VBArs:POSITION<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:VBArs:POSITION<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CURSor:VBArs:POSITION<x> value``
          command.

    SCPI Syntax:
        ```
        - CURSor:VBArs:POSITION<x> <NR3>
        - CURSor:VBArs:POSITION<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the cursor position.
    """


class CursorVbarsPosItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:VBArs:POS<x>`` command.

    Description:
        - This command sets or queries the horizontal position for vertical bar cursors. The cursor
          is specified by x, which can be 1 or 2. Values are with respect to trigger position or the
          zero reference point for the designated waveform (if horizontal units are not set to
          time). Use the ``CURSOR:VBARS:UNITS`` command to specify units. The position can appear in
          units of base or 1/base. This command is the equivalent of selecting Cursor Setup from the
          Cursors menu, selecting V Bars Cursor Type, and then viewing or editing the desired cursor
          position.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:VBArs:POS<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:VBArs:POS<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CURSor:VBArs:POS<x> value`` command.

    SCPI Syntax:
        ```
        - CURSor:VBArs:POS<x> <NR3>
        - CURSor:VBArs:POS<x>?
        ```

    Info:
        - ``<NR3>`` specifies the cursor position.
    """


class CursorVbarsDelta(SCPICmdRead):
    """The ``CURSor:VBArs:DELTa`` command.

    Description:
        - Returns the horizontal difference between the two vertical bar cursors. The units are
          specified by the ``CURSor:VBArs:UNIts`` command.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:VBArs:DELTa?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:VBArs:DELTa?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:VBArs:DELTa?
        ```
    """


class CursorVbars(SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:VBArs`` command.

    Description:
        - This command sets or queries the current settings for the vertical bar cursors or forces
          them to snap to positions specified by the ``DATA:START`` and ``DATA:STOP`` commands.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:VBArs?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:VBArs?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CURSor:VBArs value`` command.

    SCPI Syntax:
        ```
        - CURSor:VBArs SNAp
        - CURSor:VBArs?
        ```

    Info:
        - ``SNAp`` forces the position of vertical bar cursor 1 and 2 to snap to the waveform record
          points specified by the ``DATA:START`` and ``DATA:STOP`` commands, respectively.

    Properties:
        - ``.delta``: The ``CURSor:VBArs:DELTa`` command.
        - ``.pos``: The ``CURSor:VBArs:POS<x>`` command.
        - ``.position``: The ``CURSor:VBArs:POSITION<x>`` command.
        - ``.units``: The ``CURSor:VBArs:UNIts`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._delta = CursorVbarsDelta(device, f"{self._cmd_syntax}:DELTa")
        self._pos: Dict[int, CursorVbarsPosItem] = DefaultDictPassKeyToFactory(
            lambda x: CursorVbarsPosItem(device, f"{self._cmd_syntax}:POS{x}")
        )
        self._position: Dict[int, CursorVbarsPositionItem] = DefaultDictPassKeyToFactory(
            lambda x: CursorVbarsPositionItem(device, f"{self._cmd_syntax}:POSITION{x}")
        )
        self._units = CursorVbarsUnits(device, f"{self._cmd_syntax}:UNIts")

    @property
    def delta(self) -> CursorVbarsDelta:
        """Return the ``CURSor:VBArs:DELTa`` command.

        Description:
            - Returns the horizontal difference between the two vertical bar cursors. The units are
              specified by the ``CURSor:VBArs:UNIts`` command.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:VBArs:DELTa?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:VBArs:DELTa?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:VBArs:DELTa?
            ```
        """
        return self._delta

    @property
    def pos(self) -> Dict[int, CursorVbarsPosItem]:
        """Return the ``CURSor:VBArs:POS<x>`` command.

        Description:
            - This command sets or queries the horizontal position for vertical bar cursors. The
              cursor is specified by x, which can be 1 or 2. Values are with respect to trigger
              position or the zero reference point for the designated waveform (if horizontal units
              are not set to time). Use the ``CURSOR:VBARS:UNITS`` command to specify units. The
              position can appear in units of base or 1/base. This command is the equivalent of
              selecting Cursor Setup from the Cursors menu, selecting V Bars Cursor Type, and then
              viewing or editing the desired cursor position.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:VBArs:POS<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:VBArs:POS<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURSor:VBArs:POS<x> value``
              command.

        SCPI Syntax:
            ```
            - CURSor:VBArs:POS<x> <NR3>
            - CURSor:VBArs:POS<x>?
            ```

        Info:
            - ``<NR3>`` specifies the cursor position.
        """
        return self._pos

    @property
    def position(self) -> Dict[int, CursorVbarsPositionItem]:
        """Return the ``CURSor:VBArs:POSITION<x>`` command.

        Description:
            - This command specifies the horizontal position for the specified vertical bar cursor.
              The cursor is specified by <x>, which can be 1 or 2. Values are with respect to
              trigger position or the zero reference point for the designated waveform (if
              horizontal units are not set to time). Use the ``CURSOR:VBARS:UNITS`` command to
              specify units.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:VBArs:POSITION<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:VBArs:POSITION<x>?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURSor:VBArs:POSITION<x> value``
              command.

        SCPI Syntax:
            ```
            - CURSor:VBArs:POSITION<x> <NR3>
            - CURSor:VBArs:POSITION<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the cursor position.
        """
        return self._position

    @property
    def units(self) -> CursorVbarsUnits:
        """Return the ``CURSor:VBArs:UNIts`` command.

        Description:
            - This command sets or queries the units for the vertical bar cursors.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:VBArs:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:VBArs:UNIts?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURSor:VBArs:UNIts value`` command.

        SCPI Syntax:
            ```
            - CURSor:VBArs:UNIts {SECOnds|HERtz}
            - CURSor:VBArs:UNIts?
            ```

        Info:
            - ``SECOnds`` sets the units of the vertical bar cursors for the time domain (seconds).
            - ``HERtz`` sets the units of the vertical bar cursors for the frequency domain (Hertz).
        """
        return self._units


class CursorState(SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:STATE`` command.

    Description:
        - This command sets or queries the state of cursors. Note that setting the cursor state does
          not modify the cursor type. This command is equivalent to pressing the CURSOR button on
          the front panel.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CURSor:STATE value`` command.

    SCPI Syntax:
        ```
        - CURSor:STATE {ON|OFF|<NR1>}
        - CURSor:STATE?
        ```

    Info:
        - ``<NR1>`` = 0 disables the display cursors; any other value enables the display cursors.
        - ``ON`` displays the cursors.
        - ``OFF`` removes cursors from the display.
    """


class CursorSource1(SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:SOUrce1`` command.

    Description:
        - This command sets or queries the source(s) for the currently selected cursor type. The
          cursor is specified by x, which can be 1 or 2. If the cursor is not specified, it defaults
          to cursor 1. This command is equivalent to selecting Cursor Setup from the Cursors menu,
          and then choosing the desired cursor source.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:SOUrce1?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:SOUrce1?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CURSor:SOUrce1 value`` command.

    SCPI Syntax:
        ```
        - CURSor:SOUrce1 {CH<x>|MATH<x>|REF1|REF1|REF3|REF4}
        - CURSor:SOUrce1?
        ```

    Info:
        - ``CH<x>`` sets an input channel waveform as the cursor source. The valid channel waveform
          range is from 1 through 4. x has a minimum of 1 and a maximum of 4.
        - ``MATH<x>`` sets a math waveform as the cursor source. The valid math waveform range is
          from 1 through 4. x has a minimum of 1 and a maximum of 4.
        - ``REF<x>`` sets a reference waveform as the cursor source. The valid reference waveform
          range is from 1 through 4. x has a minimum of 1 and a maximum of 4.
    """


class CursorScreenYpositionItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:SCREEN:YPOSITION<x>`` command.

    Description:
        - This command sets or queries the y position of the specified screen cursor. The cursor is
          specified by x, which can be 1 or 2. If the cursor is not specified, it defaults to cursor
          1.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:SCREEN:YPOSITION<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:SCREEN:YPOSITION<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CURSor:SCREEN:YPOSITION<x> value``
          command.

    SCPI Syntax:
        ```
        - CURSor:SCREEN:YPOSITION<x> <NR3>
        - CURSor:SCREEN:YPOSITION<x>?
        ```

    Info:
        - ``<NR3>`` specifies the y position of the specified screen cursor.
    """


class CursorScreenXpositionItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:SCREEN:XPOSITION<x>`` command.

    Description:
        - This command sets or queries the x position of the specified screen cursor. The cursor is
          specified by x, which can be 1 or 2. If the cursor is not specified, it defaults to cursor
          1.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:SCREEN:XPOSITION<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:SCREEN:XPOSITION<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CURSor:SCREEN:XPOSITION<x> value``
          command.

    SCPI Syntax:
        ```
        - CURSor:SCREEN:XPOSITION<x> <NR3>
        - CURSor:SCREEN:XPOSITION<x>?
        ```

    Info:
        - ``<NR3>`` specifies the x position of the specified screen cursor.
    """


class CursorScreenStyle(SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:SCREEN:STYle`` command.

    Description:
        - This command sets or queries the cursor type for Screen mode.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:SCREEN:STYle?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:SCREEN:STYle?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CURSor:SCREEN:STYle value`` command.

    SCPI Syntax:
        ```
        - CURSor:SCREEN:STYle {LINE_X|LINES|X}
        - CURSor:SCREEN:STYle?
        ```

    Info:
        - ``LINE_X`` specifies the cursor style to be a line with superimposed X.
        - ``LINES`` specifies the cursor style to be a line.
        - ``X`` specifies the cursor style to be an X.
    """


class CursorScreen(SCPICmdRead):
    """The ``CURSor:SCREEN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:SCREEN?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:SCREEN?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.style``: The ``CURSor:SCREEN:STYle`` command.
        - ``.xposition``: The ``CURSor:SCREEN:XPOSITION<x>`` command.
        - ``.yposition``: The ``CURSor:SCREEN:YPOSITION<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._style = CursorScreenStyle(device, f"{self._cmd_syntax}:STYle")
        self._xposition: Dict[int, CursorScreenXpositionItem] = DefaultDictPassKeyToFactory(
            lambda x: CursorScreenXpositionItem(device, f"{self._cmd_syntax}:XPOSITION{x}")
        )
        self._yposition: Dict[int, CursorScreenYpositionItem] = DefaultDictPassKeyToFactory(
            lambda x: CursorScreenYpositionItem(device, f"{self._cmd_syntax}:YPOSITION{x}")
        )

    @property
    def style(self) -> CursorScreenStyle:
        """Return the ``CURSor:SCREEN:STYle`` command.

        Description:
            - This command sets or queries the cursor type for Screen mode.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:SCREEN:STYle?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:SCREEN:STYle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURSor:SCREEN:STYle value``
              command.

        SCPI Syntax:
            ```
            - CURSor:SCREEN:STYle {LINE_X|LINES|X}
            - CURSor:SCREEN:STYle?
            ```

        Info:
            - ``LINE_X`` specifies the cursor style to be a line with superimposed X.
            - ``LINES`` specifies the cursor style to be a line.
            - ``X`` specifies the cursor style to be an X.
        """
        return self._style

    @property
    def xposition(self) -> Dict[int, CursorScreenXpositionItem]:
        """Return the ``CURSor:SCREEN:XPOSITION<x>`` command.

        Description:
            - This command sets or queries the x position of the specified screen cursor. The cursor
              is specified by x, which can be 1 or 2. If the cursor is not specified, it defaults to
              cursor 1.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:SCREEN:XPOSITION<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:SCREEN:XPOSITION<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURSor:SCREEN:XPOSITION<x> value``
              command.

        SCPI Syntax:
            ```
            - CURSor:SCREEN:XPOSITION<x> <NR3>
            - CURSor:SCREEN:XPOSITION<x>?
            ```

        Info:
            - ``<NR3>`` specifies the x position of the specified screen cursor.
        """
        return self._xposition

    @property
    def yposition(self) -> Dict[int, CursorScreenYpositionItem]:
        """Return the ``CURSor:SCREEN:YPOSITION<x>`` command.

        Description:
            - This command sets or queries the y position of the specified screen cursor. The cursor
              is specified by x, which can be 1 or 2. If the cursor is not specified, it defaults to
              cursor 1.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:SCREEN:YPOSITION<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:SCREEN:YPOSITION<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURSor:SCREEN:YPOSITION<x> value``
              command.

        SCPI Syntax:
            ```
            - CURSor:SCREEN:YPOSITION<x> <NR3>
            - CURSor:SCREEN:YPOSITION<x>?
            ```

        Info:
            - ``<NR3>`` specifies the y position of the specified screen cursor.
        """
        return self._yposition


class CursorMode(SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:MODe`` command.

    Description:
        - This command specifies whether the two cursors move linked together in unison or
          separately. This command is equivalent to setting Linked to On or Off in the Cursor menu.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:MODe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CURSor:MODe value`` command.

    SCPI Syntax:
        ```
        - CURSor:MODe {TRACk|INDependent}
        - CURSor:MODe?
        ```

    Info:
        - ``TRACk`` ties the navigational functionality of the two cursors together. For cursor 1
          adjustments, this ties the movement of the two cursors together; however, cursor 2
          continues to move independently of cursor 1. This mode only applies when the
          ``DISPLAY:XY:WITHYT`` is set to OFF.
        - ``INDependent`` allows independent adjustment of the two cursors.
    """


class CursorLinestyle(SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:LINESTyle`` command.

    Description:
        - This command sets or queries the cursors line style used when cursors are displayed.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:LINESTyle?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:LINESTyle?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CURSor:LINESTyle value`` command.

    SCPI Syntax:
        ```
        - CURSor:LINESTyle {DASHed|SDASHed|SOLID}
        - CURSor:LINESTyle?
        ```

    Info:
        - ``DASHed`` displays the cursors as dashed lines.
        - ``SDASHed`` displays the cursors as solid-dashed lines.
        - ``SOLID`` displays the cursors as solid lines.
    """


class CursorHbarsUnits(SCPICmdRead):
    """The ``CURSor:HBArs:UNIts`` command.

    Description:
        - This query-only command returns the units for the horizontal bar cursors. This query
          always returns BASE, indicating that the units for the horizontal bar cursors are those of
          the base waveform to which they were assigned.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:HBArs:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:HBArs:UNIts?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:HBArs:UNIts?
        ```
    """


class CursorHbarsPositionItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:HBArs:POSITION<x>`` command.

    Description:
        - This command specifies the horizontal bar cursor position relative to ground, which is
          expressed in vertical units (usually volts). The cursor is specified by x, which can be 1
          or 2.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:HBArs:POSITION<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:HBArs:POSITION<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CURSor:HBArs:POSITION<x> value``
          command.

    SCPI Syntax:
        ```
        - CURSor:HBArs:POSITION<x> <NR3>
        - CURSor:HBArs:POSITION<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the cursor position relative to
          ground.
    """


class CursorHbarsDelta(SCPICmdRead):
    """The ``CURSor:HBArs:DELTa`` command.

    Description:
        - Returns the vertical difference between the two horizontal bar cursors.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:HBArs:DELTa?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:HBArs:DELTa?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:HBArs:DELTa?
        ```
    """


class CursorHbars(SCPICmdRead):
    """The ``CURSor:HBArs`` command.

    Description:
        - Returns the current settings for the horizontal bar cursors.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:HBArs?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:HBArs?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:HBArs?
        ```

    Properties:
        - ``.delta``: The ``CURSor:HBArs:DELTa`` command.
        - ``.position``: The ``CURSor:HBArs:POSITION<x>`` command.
        - ``.units``: The ``CURSor:HBArs:UNIts`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._delta = CursorHbarsDelta(device, f"{self._cmd_syntax}:DELTa")
        self._position: Dict[int, CursorHbarsPositionItem] = DefaultDictPassKeyToFactory(
            lambda x: CursorHbarsPositionItem(device, f"{self._cmd_syntax}:POSITION{x}")
        )
        self._units = CursorHbarsUnits(device, f"{self._cmd_syntax}:UNIts")

    @property
    def delta(self) -> CursorHbarsDelta:
        """Return the ``CURSor:HBArs:DELTa`` command.

        Description:
            - Returns the vertical difference between the two horizontal bar cursors.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:HBArs:DELTa?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:HBArs:DELTa?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:HBArs:DELTa?
            ```
        """
        return self._delta

    @property
    def position(self) -> Dict[int, CursorHbarsPositionItem]:
        """Return the ``CURSor:HBArs:POSITION<x>`` command.

        Description:
            - This command specifies the horizontal bar cursor position relative to ground, which is
              expressed in vertical units (usually volts). The cursor is specified by x, which can
              be 1 or 2.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:HBArs:POSITION<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:HBArs:POSITION<x>?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURSor:HBArs:POSITION<x> value``
              command.

        SCPI Syntax:
            ```
            - CURSor:HBArs:POSITION<x> <NR3>
            - CURSor:HBArs:POSITION<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the cursor position relative to
              ground.
        """
        return self._position

    @property
    def units(self) -> CursorHbarsUnits:
        """Return the ``CURSor:HBArs:UNIts`` command.

        Description:
            - This query-only command returns the units for the horizontal bar cursors. This query
              always returns BASE, indicating that the units for the horizontal bar cursors are
              those of the base waveform to which they were assigned.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:HBArs:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:HBArs:UNIts?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:HBArs:UNIts?
            ```
        """
        return self._units


class CursorFunction(SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:FUNCtion`` command.

    Description:
        - This command sets or queries the cursor type. Sending this command is equivalent to
          selecting Cursor Type from the Cursors menu, and then choosing from the drop-down list.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:FUNCtion?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:FUNCtion?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CURSor:FUNCtion value`` command.

    SCPI Syntax:
        ```
        - CURSor:FUNCtion {OFF|HBArs|VBArs|SCREEN|WAVEform}
        - CURSor:FUNCtion?
        ```

    Info:
        - ``OFF`` removes the cursors from the display but does not change the cursor type.
        - ``HBArs`` specifies horizontal bar cursors, which measure in vertical units.
        - ``VBArs`` specifies vertical bar cursors, which measure in horizontal units.
        - ``SCREEN`` specifies both horizontal and vertical bar cursors, which measure in horizontal
          and vertical units specified by the Cursor 1 and Cursor 2 Sources. Use these cursors to
          measure anywhere in the waveform display area.
        - ``WAVEform`` specifies paired or split cursors in YT display format for measuring waveform
          amplitude and time. In XY and XYZ format, these cursors indicate the amplitude positions
          of an XY pair (Ch1 vs Ch2 voltage, where Ch1 is the X axis and Ch2 is the Y axis) relative
          to the trigger.
    """


#  pylint: disable=too-many-instance-attributes
class Cursor(SCPICmdRead):
    """The ``CURSor`` command.

    Description:
        - Returns all of the current cursor settings.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor?
        ```

    Properties:
        - ``.function``: The ``CURSor:FUNCtion`` command.
        - ``.hbars``: The ``CURSor:HBArs`` command.
        - ``.linestyle``: The ``CURSor:LINESTyle`` command.
        - ``.mode``: The ``CURSor:MODe`` command.
        - ``.screen``: The ``CURSor:SCREEN`` command tree.
        - ``.source1``: The ``CURSor:SOUrce1`` command.
        - ``.state``: The ``CURSor:STATE`` command.
        - ``.vbars``: The ``CURSor:VBArs`` command.
        - ``.waveform``: The ``CURSor:WAVEform`` command.
        - ``.xy``: The ``CURSor:XY`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "CURSor") -> None:
        super().__init__(device, cmd_syntax)
        self._function = CursorFunction(device, f"{self._cmd_syntax}:FUNCtion")
        self._hbars = CursorHbars(device, f"{self._cmd_syntax}:HBArs")
        self._linestyle = CursorLinestyle(device, f"{self._cmd_syntax}:LINESTyle")
        self._mode = CursorMode(device, f"{self._cmd_syntax}:MODe")
        self._screen = CursorScreen(device, f"{self._cmd_syntax}:SCREEN")
        self._source1 = CursorSource1(device, f"{self._cmd_syntax}:SOUrce1")
        self._state = CursorState(device, f"{self._cmd_syntax}:STATE")
        self._vbars = CursorVbars(device, f"{self._cmd_syntax}:VBArs")
        self._waveform = CursorWaveform(device, f"{self._cmd_syntax}:WAVEform")
        self._xy = CursorXy(device, f"{self._cmd_syntax}:XY")

    @property
    def function(self) -> CursorFunction:
        """Return the ``CURSor:FUNCtion`` command.

        Description:
            - This command sets or queries the cursor type. Sending this command is equivalent to
              selecting Cursor Type from the Cursors menu, and then choosing from the drop-down
              list.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:FUNCtion?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:FUNCtion?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURSor:FUNCtion value`` command.

        SCPI Syntax:
            ```
            - CURSor:FUNCtion {OFF|HBArs|VBArs|SCREEN|WAVEform}
            - CURSor:FUNCtion?
            ```

        Info:
            - ``OFF`` removes the cursors from the display but does not change the cursor type.
            - ``HBArs`` specifies horizontal bar cursors, which measure in vertical units.
            - ``VBArs`` specifies vertical bar cursors, which measure in horizontal units.
            - ``SCREEN`` specifies both horizontal and vertical bar cursors, which measure in
              horizontal and vertical units specified by the Cursor 1 and Cursor 2 Sources. Use
              these cursors to measure anywhere in the waveform display area.
            - ``WAVEform`` specifies paired or split cursors in YT display format for measuring
              waveform amplitude and time. In XY and XYZ format, these cursors indicate the
              amplitude positions of an XY pair (Ch1 vs Ch2 voltage, where Ch1 is the X axis and Ch2
              is the Y axis) relative to the trigger.
        """
        return self._function

    @property
    def hbars(self) -> CursorHbars:
        """Return the ``CURSor:HBArs`` command.

        Description:
            - Returns the current settings for the horizontal bar cursors.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:HBArs?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:HBArs?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:HBArs?
            ```

        Sub-properties:
            - ``.delta``: The ``CURSor:HBArs:DELTa`` command.
            - ``.position``: The ``CURSor:HBArs:POSITION<x>`` command.
            - ``.units``: The ``CURSor:HBArs:UNIts`` command.
        """
        return self._hbars

    @property
    def linestyle(self) -> CursorLinestyle:
        """Return the ``CURSor:LINESTyle`` command.

        Description:
            - This command sets or queries the cursors line style used when cursors are displayed.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:LINESTyle?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:LINESTyle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURSor:LINESTyle value`` command.

        SCPI Syntax:
            ```
            - CURSor:LINESTyle {DASHed|SDASHed|SOLID}
            - CURSor:LINESTyle?
            ```

        Info:
            - ``DASHed`` displays the cursors as dashed lines.
            - ``SDASHed`` displays the cursors as solid-dashed lines.
            - ``SOLID`` displays the cursors as solid lines.
        """
        return self._linestyle

    @property
    def mode(self) -> CursorMode:
        """Return the ``CURSor:MODe`` command.

        Description:
            - This command specifies whether the two cursors move linked together in unison or
              separately. This command is equivalent to setting Linked to On or Off in the Cursor
              menu.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:MODe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURSor:MODe value`` command.

        SCPI Syntax:
            ```
            - CURSor:MODe {TRACk|INDependent}
            - CURSor:MODe?
            ```

        Info:
            - ``TRACk`` ties the navigational functionality of the two cursors together. For cursor
              1 adjustments, this ties the movement of the two cursors together; however, cursor 2
              continues to move independently of cursor 1. This mode only applies when the
              ``DISPLAY:XY:WITHYT`` is set to OFF.
            - ``INDependent`` allows independent adjustment of the two cursors.
        """
        return self._mode

    @property
    def screen(self) -> CursorScreen:
        """Return the ``CURSor:SCREEN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:SCREEN?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:SCREEN?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.style``: The ``CURSor:SCREEN:STYle`` command.
            - ``.xposition``: The ``CURSor:SCREEN:XPOSITION<x>`` command.
            - ``.yposition``: The ``CURSor:SCREEN:YPOSITION<x>`` command.
        """
        return self._screen

    @property
    def source1(self) -> CursorSource1:
        """Return the ``CURSor:SOUrce1`` command.

        Description:
            - This command sets or queries the source(s) for the currently selected cursor type. The
              cursor is specified by x, which can be 1 or 2. If the cursor is not specified, it
              defaults to cursor 1. This command is equivalent to selecting Cursor Setup from the
              Cursors menu, and then choosing the desired cursor source.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:SOUrce1?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:SOUrce1?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURSor:SOUrce1 value`` command.

        SCPI Syntax:
            ```
            - CURSor:SOUrce1 {CH<x>|MATH<x>|REF1|REF1|REF3|REF4}
            - CURSor:SOUrce1?
            ```

        Info:
            - ``CH<x>`` sets an input channel waveform as the cursor source. The valid channel
              waveform range is from 1 through 4. x has a minimum of 1 and a maximum of 4.
            - ``MATH<x>`` sets a math waveform as the cursor source. The valid math waveform range
              is from 1 through 4. x has a minimum of 1 and a maximum of 4.
            - ``REF<x>`` sets a reference waveform as the cursor source. The valid reference
              waveform range is from 1 through 4. x has a minimum of 1 and a maximum of 4.
        """
        return self._source1

    @property
    def state(self) -> CursorState:
        """Return the ``CURSor:STATE`` command.

        Description:
            - This command sets or queries the state of cursors. Note that setting the cursor state
              does not modify the cursor type. This command is equivalent to pressing the CURSOR
              button on the front panel.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:STATE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURSor:STATE value`` command.

        SCPI Syntax:
            ```
            - CURSor:STATE {ON|OFF|<NR1>}
            - CURSor:STATE?
            ```

        Info:
            - ``<NR1>`` = 0 disables the display cursors; any other value enables the display
              cursors.
            - ``ON`` displays the cursors.
            - ``OFF`` removes cursors from the display.
        """
        return self._state

    @property
    def vbars(self) -> CursorVbars:
        """Return the ``CURSor:VBArs`` command.

        Description:
            - This command sets or queries the current settings for the vertical bar cursors or
              forces them to snap to positions specified by the ``DATA:START`` and ``DATA:STOP``
              commands.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:VBArs?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:VBArs?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURSor:VBArs value`` command.

        SCPI Syntax:
            ```
            - CURSor:VBArs SNAp
            - CURSor:VBArs?
            ```

        Info:
            - ``SNAp`` forces the position of vertical bar cursor 1 and 2 to snap to the waveform
              record points specified by the ``DATA:START`` and ``DATA:STOP`` commands,
              respectively.

        Sub-properties:
            - ``.delta``: The ``CURSor:VBArs:DELTa`` command.
            - ``.pos``: The ``CURSor:VBArs:POS<x>`` command.
            - ``.position``: The ``CURSor:VBArs:POSITION<x>`` command.
            - ``.units``: The ``CURSor:VBArs:UNIts`` command.
        """
        return self._vbars

    @property
    def waveform(self) -> CursorWaveform:
        """Return the ``CURSor:WAVEform`` command.

        Description:
            - This command sets or queries the current settings for the waveform cursors or forces
              them to snap to positions specified by the ``DATA:START`` and ``DATA:STOP`` commands.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:WAVEform?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:WAVEform?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURSor:WAVEform value`` command.

        SCPI Syntax:
            ```
            - CURSor:WAVEform SNAp
            - CURSor:WAVEform?
            ```

        Info:
            - ``SNAp`` forces the position of waveform cursor 1 and 2 to snap to the waveform record
              points specified by the ``DATA:START`` and ``DATA:STOP`` commands, respectively.

        Sub-properties:
            - ``.hdelta``: The ``CURSor:WAVEform:HDELTA`` command.
            - ``.hpos``: The ``CURSor:WAVEform:HPOS<x>`` command.
            - ``.position``: The ``CURSor:WAVEform:POSition<x>`` command.
            - ``.source1``: The ``CURSor:WAVEform:SOUrce1`` command.
            - ``.style``: The ``CURSor:WAVEform:STYle`` command.
            - ``.units``: The ``CURSor:WAVEform:UNIts`` command.
            - ``.vdelta``: The ``CURSor:WAVEform:VDELTA`` command.
        """
        return self._waveform

    @property
    def xy(self) -> CursorXy:
        """Return the ``CURSor:XY`` command.

        Description:
            - This query-only command returns all of the XY cursor parameters.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY?
            ```

        Sub-properties:
            - ``.proddelta``: The ``CURSor:XY:PRODDELta`` command.
            - ``.product``: The ``CURSor:XY:PRODUCT<x>`` command.
            - ``.radius``: The ``CURSor:XY:RADIUS<x>`` command.
            - ``.ratdelta``: The ``CURSor:XY:RATDELta`` command.
            - ``.ratio``: The ``CURSor:XY:RATIO<x>`` command.
            - ``.rdelta``: The ``CURSor:XY:RDELta`` command.
            - ``.readout``: The ``CURSor:XY:READOUT`` command.
            - ``.rectx``: The ``CURSor:XY:RECTX<x>`` command.
            - ``.recty``: The ``CURSor:XY:RECTY<x>`` command.
            - ``.thdelta``: The ``CURSor:XY:THDELta`` command.
            - ``.theta``: The ``CURSor:XY:THETA<x>`` command.
            - ``.xdelta``: The ``CURSor:XY:XDELta`` command.
            - ``.ydelta``: The ``CURSor:XY:YDELta`` command.
        """
        return self._xy
