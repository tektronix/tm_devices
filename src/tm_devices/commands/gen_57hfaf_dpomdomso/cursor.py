"""The cursor commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO4K, MSO4K

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CURSor:DDT?
    - CURSor:FUNCtion {SCREEN|WAVEform|OFF}
    - CURSor:FUNCtion?
    - CURSor:HBArs:DELTa?
    - CURSor:HBArs:POSITION<x> <NR3>
    - CURSor:HBArs:POSITION<x>?
    - CURSor:HBArs:UNIts {BASE|PERcent}
    - CURSor:HBArs:UNIts?
    - CURSor:HBArs:USE {CURrent|HALFgrat}
    - CURSor:HBArs?
    - CURSor:MODe {TRACk|INDependent}
    - CURSor:MODe?
    - CURSor:VBArs:ALTERNATE<x>?
    - CURSor:VBArs:DELTa?
    - CURSor:VBArs:HPOS<x>?
    - CURSor:VBArs:POSITION<x> <NR3>
    - CURSor:VBArs:POSITION<x>?
    - CURSor:VBArs:UNIts {SEConds|HERtz|DEGrees|PERcent}
    - CURSor:VBArs:UNIts?
    - CURSor:VBArs:USE {CURrent|HALFgrat|FIVEdivs}
    - CURSor:VBArs:VDELTa?
    - CURSor:VBArs?
    - CURSor:XY:POLar:RADIUS:DELta?
    - CURSor:XY:POLar:RADIUS:POSITION<x>?
    - CURSor:XY:POLar:RADIUS:UNIts?
    - CURSor:XY:POLar:THETA:DELta?
    - CURSor:XY:POLar:THETA:POSITION<x>?
    - CURSor:XY:POLar:THETA:UNIts?
    - CURSor:XY:PRODUCT:DELta?
    - CURSor:XY:PRODUCT:POSITION<x>?
    - CURSor:XY:PRODUCT:UNIts?
    - CURSor:XY:RATIO:DELta?
    - CURSor:XY:RATIO:POSITION<x>?
    - CURSor:XY:RATIO:UNIts?
    - CURSor:XY:READOUT {RECTangular|POLARCord|PRODuct|RATio}
    - CURSor:XY:READOUT?
    - CURSor:XY:RECTangular:X:DELta?
    - CURSor:XY:RECTangular:X:POSITION<x> <NR3>
    - CURSor:XY:RECTangular:X:POSITION<x>?
    - CURSor:XY:RECTangular:X:UNIts?
    - CURSor:XY:RECTangular:Y:DELta?
    - CURSor:XY:RECTangular:Y:POSITION<x> <NR3>
    - CURSor:XY:RECTangular:Y:POSITION<x>?
    - CURSor:XY:RECTangular:Y:UNIts?
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


class CursorXyRectangularYUnits(SCPICmdRead):
    """The ``CURSor:XY:RECTangular:Y:UNIts`` command.

    Description:
        - Returns the cursor Y rectangular units.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:RECTangular:Y:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:RECTangular:Y:UNIts?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY:RECTangular:Y:UNIts?
        ```
    """


class CursorXyRectangularYPositionItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:XY:RECTangular:Y:POSITION<x>`` command.

    Description:
        - This command specifies the Y rectangular coordinate for cursor 1 or cursor 2. The cursor
          is specified by x and can be either 1 or 2.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:RECTangular:Y:POSITION<x>?``
          query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:RECTangular:Y:POSITION<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``CURSor:XY:RECTangular:Y:POSITION<x> value`` command.

    SCPI Syntax:
        ```
        - CURSor:XY:RECTangular:Y:POSITION<x> <NR3>
        - CURSor:XY:RECTangular:Y:POSITION<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the coordinate in volts.
    """


class CursorXyRectangularYDelta(SCPICmdRead):
    """The ``CURSor:XY:RECTangular:Y:DELta`` command.

    Description:
        - Returns The cursor Y delta value in rectangular coordinates.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:RECTangular:Y:DELta?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:RECTangular:Y:DELta?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY:RECTangular:Y:DELta?
        ```
    """


class CursorXyRectangularY(SCPICmdRead):
    """The ``CURSor:XY:RECTangular:Y`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:RECTangular:Y?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:RECTangular:Y?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.delta``: The ``CURSor:XY:RECTangular:Y:DELta`` command.
        - ``.position``: The ``CURSor:XY:RECTangular:Y:POSITION<x>`` command.
        - ``.units``: The ``CURSor:XY:RECTangular:Y:UNIts`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._delta = CursorXyRectangularYDelta(device, f"{self._cmd_syntax}:DELta")
        self._position: Dict[int, CursorXyRectangularYPositionItem] = DefaultDictPassKeyToFactory(
            lambda x: CursorXyRectangularYPositionItem(device, f"{self._cmd_syntax}:POSITION{x}")
        )
        self._units = CursorXyRectangularYUnits(device, f"{self._cmd_syntax}:UNIts")

    @property
    def delta(self) -> CursorXyRectangularYDelta:
        """Return the ``CURSor:XY:RECTangular:Y:DELta`` command.

        Description:
            - Returns The cursor Y delta value in rectangular coordinates.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:RECTangular:Y:DELta?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:RECTangular:Y:DELta?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY:RECTangular:Y:DELta?
            ```
        """
        return self._delta

    @property
    def position(self) -> Dict[int, CursorXyRectangularYPositionItem]:
        """Return the ``CURSor:XY:RECTangular:Y:POSITION<x>`` command.

        Description:
            - This command specifies the Y rectangular coordinate for cursor 1 or cursor 2. The
              cursor is specified by x and can be either 1 or 2.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:RECTangular:Y:POSITION<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CURSor:XY:RECTangular:Y:POSITION<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CURSor:XY:RECTangular:Y:POSITION<x> value`` command.

        SCPI Syntax:
            ```
            - CURSor:XY:RECTangular:Y:POSITION<x> <NR3>
            - CURSor:XY:RECTangular:Y:POSITION<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the coordinate in volts.
        """
        return self._position

    @property
    def units(self) -> CursorXyRectangularYUnits:
        """Return the ``CURSor:XY:RECTangular:Y:UNIts`` command.

        Description:
            - Returns the cursor Y rectangular units.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:RECTangular:Y:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:RECTangular:Y:UNIts?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY:RECTangular:Y:UNIts?
            ```
        """
        return self._units


class CursorXyRectangularXUnits(SCPICmdRead):
    """The ``CURSor:XY:RECTangular:X:UNIts`` command.

    Description:
        - Returns the cursor X rectangular units.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:RECTangular:X:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:RECTangular:X:UNIts?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY:RECTangular:X:UNIts?
        ```
    """


class CursorXyRectangularXPositionItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:XY:RECTangular:X:POSITION<x>`` command.

    Description:
        - This command specifies the X rectangular coordinate for cursor 1 or cursor 2. The cursor
          is specified by x and can be either 1 or 2.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:RECTangular:X:POSITION<x>?``
          query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:RECTangular:X:POSITION<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``CURSor:XY:RECTangular:X:POSITION<x> value`` command.

    SCPI Syntax:
        ```
        - CURSor:XY:RECTangular:X:POSITION<x> <NR3>
        - CURSor:XY:RECTangular:X:POSITION<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the coordinate in volts.
    """


class CursorXyRectangularXDelta(SCPICmdRead):
    """The ``CURSor:XY:RECTangular:X:DELta`` command.

    Description:
        - Returns the cursor X delta value in rectangular coordinates.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:RECTangular:X:DELta?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:RECTangular:X:DELta?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY:RECTangular:X:DELta?
        ```
    """


class CursorXyRectangularX(SCPICmdRead):
    """The ``CURSor:XY:RECTangular:X`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:RECTangular:X?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:RECTangular:X?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.delta``: The ``CURSor:XY:RECTangular:X:DELta`` command.
        - ``.position``: The ``CURSor:XY:RECTangular:X:POSITION<x>`` command.
        - ``.units``: The ``CURSor:XY:RECTangular:X:UNIts`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._delta = CursorXyRectangularXDelta(device, f"{self._cmd_syntax}:DELta")
        self._position: Dict[int, CursorXyRectangularXPositionItem] = DefaultDictPassKeyToFactory(
            lambda x: CursorXyRectangularXPositionItem(device, f"{self._cmd_syntax}:POSITION{x}")
        )
        self._units = CursorXyRectangularXUnits(device, f"{self._cmd_syntax}:UNIts")

    @property
    def delta(self) -> CursorXyRectangularXDelta:
        """Return the ``CURSor:XY:RECTangular:X:DELta`` command.

        Description:
            - Returns the cursor X delta value in rectangular coordinates.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:RECTangular:X:DELta?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:RECTangular:X:DELta?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY:RECTangular:X:DELta?
            ```
        """
        return self._delta

    @property
    def position(self) -> Dict[int, CursorXyRectangularXPositionItem]:
        """Return the ``CURSor:XY:RECTangular:X:POSITION<x>`` command.

        Description:
            - This command specifies the X rectangular coordinate for cursor 1 or cursor 2. The
              cursor is specified by x and can be either 1 or 2.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:RECTangular:X:POSITION<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CURSor:XY:RECTangular:X:POSITION<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CURSor:XY:RECTangular:X:POSITION<x> value`` command.

        SCPI Syntax:
            ```
            - CURSor:XY:RECTangular:X:POSITION<x> <NR3>
            - CURSor:XY:RECTangular:X:POSITION<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the coordinate in volts.
        """
        return self._position

    @property
    def units(self) -> CursorXyRectangularXUnits:
        """Return the ``CURSor:XY:RECTangular:X:UNIts`` command.

        Description:
            - Returns the cursor X rectangular units.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:RECTangular:X:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:RECTangular:X:UNIts?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY:RECTangular:X:UNIts?
            ```
        """
        return self._units


class CursorXyRectangular(SCPICmdRead):
    """The ``CURSor:XY:RECTangular`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:RECTangular?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:RECTangular?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.x``: The ``CURSor:XY:RECTangular:X`` command tree.
        - ``.y``: The ``CURSor:XY:RECTangular:Y`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._x = CursorXyRectangularX(device, f"{self._cmd_syntax}:X")
        self._y = CursorXyRectangularY(device, f"{self._cmd_syntax}:Y")

    @property
    def x(self) -> CursorXyRectangularX:
        """Return the ``CURSor:XY:RECTangular:X`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:RECTangular:X?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:RECTangular:X?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.delta``: The ``CURSor:XY:RECTangular:X:DELta`` command.
            - ``.position``: The ``CURSor:XY:RECTangular:X:POSITION<x>`` command.
            - ``.units``: The ``CURSor:XY:RECTangular:X:UNIts`` command.
        """
        return self._x

    @property
    def y(self) -> CursorXyRectangularY:
        """Return the ``CURSor:XY:RECTangular:Y`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:RECTangular:Y?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:RECTangular:Y?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.delta``: The ``CURSor:XY:RECTangular:Y:DELta`` command.
            - ``.position``: The ``CURSor:XY:RECTangular:Y:POSITION<x>`` command.
            - ``.units``: The ``CURSor:XY:RECTangular:Y:UNIts`` command.
        """
        return self._y


class CursorXyReadout(SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:XY:READOUT`` command.

    Description:
        - This command specifies the XY cursor readout selection.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:READOUT?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:READOUT?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CURSor:XY:READOUT value`` command.

    SCPI Syntax:
        ```
        - CURSor:XY:READOUT {RECTangular|POLARCord|PRODuct|RATio}
        - CURSor:XY:READOUT?
        ```

    Info:
        - ``RECTangular`` specifies the XY readout as rectangular coordinates.
        - ``POLARCord`` specifies the XY readout as polar coordinates.
        - ``PRODuct`` specifies the XY readout in X``*Y`` format.
        - ``RATio`` specifies the XY readout in ``X:Y`` format.
    """


class CursorXyRatioUnits(SCPICmdRead):
    """The ``CURSor:XY:RATIO:UNIts`` command.

    Description:
        - Returns the cursor X and cursor Y units for the ratio measurement.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:RATIO:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:RATIO:UNIts?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY:RATIO:UNIts?
        ```
    """


class CursorXyRatioPositionItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``CURSor:XY:RATIO:POSITION<x>`` command.

    Description:
        - Returns the X (horizontal) or Y (vertical) position for the specified cursor, which can be
          1 (X) or 2 (Y). The ratio is calculated as Position 1 = (Y1/X1); Position 2 = (Y2/X2).

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:RATIO:POSITION<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:RATIO:POSITION<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY:RATIO:POSITION<x>?
        ```
    """


class CursorXyRatioDelta(SCPICmdRead):
    """The ``CURSor:XY:RATIO:DELta`` command.

    Description:
        - Returns the ratio of the difference between the cursors X position and cursor Y position
          (ΔY¸ ΔX). The ratio is calculated as (Y2 - Y1) / (X2 - X1).

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:RATIO:DELta?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:RATIO:DELta?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY:RATIO:DELta?
        ```
    """


class CursorXyRatio(SCPICmdRead):
    """The ``CURSor:XY:RATIO`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:RATIO?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:RATIO?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.delta``: The ``CURSor:XY:RATIO:DELta`` command.
        - ``.position``: The ``CURSor:XY:RATIO:POSITION<x>`` command.
        - ``.units``: The ``CURSor:XY:RATIO:UNIts`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._delta = CursorXyRatioDelta(device, f"{self._cmd_syntax}:DELta")
        self._position: Dict[int, CursorXyRatioPositionItem] = DefaultDictPassKeyToFactory(
            lambda x: CursorXyRatioPositionItem(device, f"{self._cmd_syntax}:POSITION{x}")
        )
        self._units = CursorXyRatioUnits(device, f"{self._cmd_syntax}:UNIts")

    @property
    def delta(self) -> CursorXyRatioDelta:
        """Return the ``CURSor:XY:RATIO:DELta`` command.

        Description:
            - Returns the ratio of the difference between the cursors X position and cursor Y
              position (ΔY¸ ΔX). The ratio is calculated as (Y2 - Y1) / (X2 - X1).

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:RATIO:DELta?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:RATIO:DELta?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY:RATIO:DELta?
            ```
        """
        return self._delta

    @property
    def position(self) -> Dict[int, CursorXyRatioPositionItem]:
        """Return the ``CURSor:XY:RATIO:POSITION<x>`` command.

        Description:
            - Returns the X (horizontal) or Y (vertical) position for the specified cursor, which
              can be 1 (X) or 2 (Y). The ratio is calculated as Position 1 = (Y1/X1); Position 2 =
              (Y2/X2).

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:RATIO:POSITION<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:RATIO:POSITION<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY:RATIO:POSITION<x>?
            ```
        """
        return self._position

    @property
    def units(self) -> CursorXyRatioUnits:
        """Return the ``CURSor:XY:RATIO:UNIts`` command.

        Description:
            - Returns the cursor X and cursor Y units for the ratio measurement.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:RATIO:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:RATIO:UNIts?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY:RATIO:UNIts?
            ```
        """
        return self._units


class CursorXyProductUnits(SCPICmdRead):
    """The ``CURSor:XY:PRODUCT:UNIts`` command.

    Description:
        - Returns the XY cursor product units.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:PRODUCT:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:PRODUCT:UNIts?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY:PRODUCT:UNIts?
        ```
    """


class CursorXyProductPositionItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``CURSor:XY:PRODUCT:POSITION<x>`` command.

    Description:
        - Returns the position of the X or Y cursor used to calculate the X × Y cursor measurement,
          Position 1 = (X1 × Y1); Position 2 = (X2 × Y2). The cursor is specified by x, which can be
          1 or 2.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:PRODUCT:POSITION<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:PRODUCT:POSITION<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY:PRODUCT:POSITION<x>?
        ```
    """


class CursorXyProductDelta(SCPICmdRead):
    """The ``CURSor:XY:PRODUCT:DELta`` command.

    Description:
        - Returns the difference between the cursors X position and cursor Y position. The ΔX × ΔY
          value is calculated as (X2 - X1) × (Y2 - Y1).

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:PRODUCT:DELta?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:PRODUCT:DELta?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY:PRODUCT:DELta?
        ```
    """


class CursorXyProduct(SCPICmdRead):
    """The ``CURSor:XY:PRODUCT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:PRODUCT?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:PRODUCT?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.delta``: The ``CURSor:XY:PRODUCT:DELta`` command.
        - ``.position``: The ``CURSor:XY:PRODUCT:POSITION<x>`` command.
        - ``.units``: The ``CURSor:XY:PRODUCT:UNIts`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._delta = CursorXyProductDelta(device, f"{self._cmd_syntax}:DELta")
        self._position: Dict[int, CursorXyProductPositionItem] = DefaultDictPassKeyToFactory(
            lambda x: CursorXyProductPositionItem(device, f"{self._cmd_syntax}:POSITION{x}")
        )
        self._units = CursorXyProductUnits(device, f"{self._cmd_syntax}:UNIts")

    @property
    def delta(self) -> CursorXyProductDelta:
        """Return the ``CURSor:XY:PRODUCT:DELta`` command.

        Description:
            - Returns the difference between the cursors X position and cursor Y position. The ΔX ×
              ΔY value is calculated as (X2 - X1) × (Y2 - Y1).

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:PRODUCT:DELta?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:PRODUCT:DELta?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY:PRODUCT:DELta?
            ```
        """
        return self._delta

    @property
    def position(self) -> Dict[int, CursorXyProductPositionItem]:
        """Return the ``CURSor:XY:PRODUCT:POSITION<x>`` command.

        Description:
            - Returns the position of the X or Y cursor used to calculate the X × Y cursor
              measurement, Position 1 = (X1 × Y1); Position 2 = (X2 × Y2). The cursor is specified
              by x, which can be 1 or 2.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:PRODUCT:POSITION<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:PRODUCT:POSITION<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY:PRODUCT:POSITION<x>?
            ```
        """
        return self._position

    @property
    def units(self) -> CursorXyProductUnits:
        """Return the ``CURSor:XY:PRODUCT:UNIts`` command.

        Description:
            - Returns the XY cursor product units.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:PRODUCT:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:PRODUCT:UNIts?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY:PRODUCT:UNIts?
            ```
        """
        return self._units


class CursorXyPolarThetaUnits(SCPICmdRead):
    """The ``CURSor:XY:POLar:THETA:UNIts`` command.

    Description:
        - Returns the cursor coordinate units.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:POLar:THETA:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:POLar:THETA:UNIts?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY:POLar:THETA:UNIts?
        ```
    """


class CursorXyPolarThetaPositionItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``CURSor:XY:POLar:THETA:POSITION<x>`` command.

    Description:
        - Returns the cursor X or cursor Y polar coordinate, where x is either 1 or 2.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:POLar:THETA:POSITION<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:POLar:THETA:POSITION<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY:POLar:THETA:POSITION<x>?
        ```
    """


class CursorXyPolarThetaDelta(SCPICmdRead):
    """The ``CURSor:XY:POLar:THETA:DELta`` command.

    Description:
        - Returns the XY cursor polar angle delta.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:POLar:THETA:DELta?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:POLar:THETA:DELta?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY:POLar:THETA:DELta?
        ```
    """


class CursorXyPolarTheta(SCPICmdRead):
    """The ``CURSor:XY:POLar:THETA`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:POLar:THETA?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:POLar:THETA?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.delta``: The ``CURSor:XY:POLar:THETA:DELta`` command.
        - ``.position``: The ``CURSor:XY:POLar:THETA:POSITION<x>`` command.
        - ``.units``: The ``CURSor:XY:POLar:THETA:UNIts`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._delta = CursorXyPolarThetaDelta(device, f"{self._cmd_syntax}:DELta")
        self._position: Dict[int, CursorXyPolarThetaPositionItem] = DefaultDictPassKeyToFactory(
            lambda x: CursorXyPolarThetaPositionItem(device, f"{self._cmd_syntax}:POSITION{x}")
        )
        self._units = CursorXyPolarThetaUnits(device, f"{self._cmd_syntax}:UNIts")

    @property
    def delta(self) -> CursorXyPolarThetaDelta:
        """Return the ``CURSor:XY:POLar:THETA:DELta`` command.

        Description:
            - Returns the XY cursor polar angle delta.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:POLar:THETA:DELta?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:POLar:THETA:DELta?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY:POLar:THETA:DELta?
            ```
        """
        return self._delta

    @property
    def position(self) -> Dict[int, CursorXyPolarThetaPositionItem]:
        """Return the ``CURSor:XY:POLar:THETA:POSITION<x>`` command.

        Description:
            - Returns the cursor X or cursor Y polar coordinate, where x is either 1 or 2.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:POLar:THETA:POSITION<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CURSor:XY:POLar:THETA:POSITION<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY:POLar:THETA:POSITION<x>?
            ```
        """
        return self._position

    @property
    def units(self) -> CursorXyPolarThetaUnits:
        """Return the ``CURSor:XY:POLar:THETA:UNIts`` command.

        Description:
            - Returns the cursor coordinate units.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:POLar:THETA:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:POLar:THETA:UNIts?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY:POLar:THETA:UNIts?
            ```
        """
        return self._units


class CursorXyPolarRadiusUnits(SCPICmdRead):
    """The ``CURSor:XY:POLar:RADIUS:UNIts`` command.

    Description:
        - Returns the polar radius units.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:POLar:RADIUS:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:POLar:RADIUS:UNIts?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY:POLar:RADIUS:UNIts?
        ```
    """


class CursorXyPolarRadiusPositionItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``CURSor:XY:POLar:RADIUS:POSITION<x>`` command.

    Description:
        - Returns the polar radius for the specified cursor, where x can be either 1 or 2.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:POLar:RADIUS:POSITION<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:POLar:RADIUS:POSITION<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY:POLar:RADIUS:POSITION<x>?
        ```
    """


class CursorXyPolarRadiusDelta(SCPICmdRead):
    """The ``CURSor:XY:POLar:RADIUS:DELta`` command.

    Description:
        - Returns the difference between the cursors X radius and the cursor Y radius (ΔY¸ ΔX). The
          ratio is calculated as (cursor 2 Y - cursor 1 Y) ÷ (cursor 2 X - cursor 1 X).

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:POLar:RADIUS:DELta?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:POLar:RADIUS:DELta?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:XY:POLar:RADIUS:DELta?
        ```
    """


class CursorXyPolarRadius(SCPICmdRead):
    """The ``CURSor:XY:POLar:RADIUS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:POLar:RADIUS?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:POLar:RADIUS?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.delta``: The ``CURSor:XY:POLar:RADIUS:DELta`` command.
        - ``.position``: The ``CURSor:XY:POLar:RADIUS:POSITION<x>`` command.
        - ``.units``: The ``CURSor:XY:POLar:RADIUS:UNIts`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._delta = CursorXyPolarRadiusDelta(device, f"{self._cmd_syntax}:DELta")
        self._position: Dict[int, CursorXyPolarRadiusPositionItem] = DefaultDictPassKeyToFactory(
            lambda x: CursorXyPolarRadiusPositionItem(device, f"{self._cmd_syntax}:POSITION{x}")
        )
        self._units = CursorXyPolarRadiusUnits(device, f"{self._cmd_syntax}:UNIts")

    @property
    def delta(self) -> CursorXyPolarRadiusDelta:
        """Return the ``CURSor:XY:POLar:RADIUS:DELta`` command.

        Description:
            - Returns the difference between the cursors X radius and the cursor Y radius (ΔY¸ ΔX).
              The ratio is calculated as (cursor 2 Y - cursor 1 Y) ÷ (cursor 2 X - cursor 1 X).

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:POLar:RADIUS:DELta?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:POLar:RADIUS:DELta?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY:POLar:RADIUS:DELta?
            ```
        """
        return self._delta

    @property
    def position(self) -> Dict[int, CursorXyPolarRadiusPositionItem]:
        """Return the ``CURSor:XY:POLar:RADIUS:POSITION<x>`` command.

        Description:
            - Returns the polar radius for the specified cursor, where x can be either 1 or 2.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:POLar:RADIUS:POSITION<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CURSor:XY:POLar:RADIUS:POSITION<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY:POLar:RADIUS:POSITION<x>?
            ```
        """
        return self._position

    @property
    def units(self) -> CursorXyPolarRadiusUnits:
        """Return the ``CURSor:XY:POLar:RADIUS:UNIts`` command.

        Description:
            - Returns the polar radius units.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:POLar:RADIUS:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:POLar:RADIUS:UNIts?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:XY:POLar:RADIUS:UNIts?
            ```
        """
        return self._units


class CursorXyPolar(SCPICmdRead):
    """The ``CURSor:XY:POLar`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY:POLar?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY:POLar?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.radius``: The ``CURSor:XY:POLar:RADIUS`` command tree.
        - ``.theta``: The ``CURSor:XY:POLar:THETA`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._radius = CursorXyPolarRadius(device, f"{self._cmd_syntax}:RADIUS")
        self._theta = CursorXyPolarTheta(device, f"{self._cmd_syntax}:THETA")

    @property
    def radius(self) -> CursorXyPolarRadius:
        """Return the ``CURSor:XY:POLar:RADIUS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:POLar:RADIUS?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:POLar:RADIUS?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.delta``: The ``CURSor:XY:POLar:RADIUS:DELta`` command.
            - ``.position``: The ``CURSor:XY:POLar:RADIUS:POSITION<x>`` command.
            - ``.units``: The ``CURSor:XY:POLar:RADIUS:UNIts`` command.
        """
        return self._radius

    @property
    def theta(self) -> CursorXyPolarTheta:
        """Return the ``CURSor:XY:POLar:THETA`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:POLar:THETA?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:POLar:THETA?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.delta``: The ``CURSor:XY:POLar:THETA:DELta`` command.
            - ``.position``: The ``CURSor:XY:POLar:THETA:POSITION<x>`` command.
            - ``.units``: The ``CURSor:XY:POLar:THETA:UNIts`` command.
        """
        return self._theta


class CursorXy(SCPICmdRead):
    """The ``CURSor:XY`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:XY?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:XY?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.polar``: The ``CURSor:XY:POLar`` command tree.
        - ``.product``: The ``CURSor:XY:PRODUCT`` command tree.
        - ``.ratio``: The ``CURSor:XY:RATIO`` command tree.
        - ``.readout``: The ``CURSor:XY:READOUT`` command.
        - ``.rectangular``: The ``CURSor:XY:RECTangular`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polar = CursorXyPolar(device, f"{self._cmd_syntax}:POLar")
        self._product = CursorXyProduct(device, f"{self._cmd_syntax}:PRODUCT")
        self._ratio = CursorXyRatio(device, f"{self._cmd_syntax}:RATIO")
        self._readout = CursorXyReadout(device, f"{self._cmd_syntax}:READOUT")
        self._rectangular = CursorXyRectangular(device, f"{self._cmd_syntax}:RECTangular")

    @property
    def polar(self) -> CursorXyPolar:
        """Return the ``CURSor:XY:POLar`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:POLar?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:POLar?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.radius``: The ``CURSor:XY:POLar:RADIUS`` command tree.
            - ``.theta``: The ``CURSor:XY:POLar:THETA`` command tree.
        """
        return self._polar

    @property
    def product(self) -> CursorXyProduct:
        """Return the ``CURSor:XY:PRODUCT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:PRODUCT?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:PRODUCT?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.delta``: The ``CURSor:XY:PRODUCT:DELta`` command.
            - ``.position``: The ``CURSor:XY:PRODUCT:POSITION<x>`` command.
            - ``.units``: The ``CURSor:XY:PRODUCT:UNIts`` command.
        """
        return self._product

    @property
    def ratio(self) -> CursorXyRatio:
        """Return the ``CURSor:XY:RATIO`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:RATIO?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:RATIO?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.delta``: The ``CURSor:XY:RATIO:DELta`` command.
            - ``.position``: The ``CURSor:XY:RATIO:POSITION<x>`` command.
            - ``.units``: The ``CURSor:XY:RATIO:UNIts`` command.
        """
        return self._ratio

    @property
    def readout(self) -> CursorXyReadout:
        """Return the ``CURSor:XY:READOUT`` command.

        Description:
            - This command specifies the XY cursor readout selection.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:READOUT?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:READOUT?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURSor:XY:READOUT value`` command.

        SCPI Syntax:
            ```
            - CURSor:XY:READOUT {RECTangular|POLARCord|PRODuct|RATio}
            - CURSor:XY:READOUT?
            ```

        Info:
            - ``RECTangular`` specifies the XY readout as rectangular coordinates.
            - ``POLARCord`` specifies the XY readout as polar coordinates.
            - ``PRODuct`` specifies the XY readout in X``*Y`` format.
            - ``RATio`` specifies the XY readout in ``X:Y`` format.
        """
        return self._readout

    @property
    def rectangular(self) -> CursorXyRectangular:
        """Return the ``CURSor:XY:RECTangular`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY:RECTangular?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY:RECTangular?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.x``: The ``CURSor:XY:RECTangular:X`` command tree.
            - ``.y``: The ``CURSor:XY:RECTangular:Y`` command tree.
        """
        return self._rectangular


class CursorVbarsVdelta(SCPICmdRead):
    """The ``CURSor:VBArs:VDELTa`` command.

    Description:
        - Returns the vertical difference between the two vertical bar cursor ticks.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:VBArs:VDELTa?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:VBArs:VDELTa?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:VBArs:VDELTa?
        ```
    """


class CursorVbarsUse(SCPICmdWrite):
    """The ``CURSor:VBArs:USE`` command.

    Description:
        - Sets the vertical bar cursor measurement scale.

    Usage:
        - Using the ``.write(value)`` method will send the ``CURSor:VBArs:USE value`` command.

    SCPI Syntax:
        ```
        - CURSor:VBArs:USE {CURrent|HALFgrat|FIVEdivs}
        ```

    Info:
        - ``CURrent`` sets the V Bar measurement scale so that 0% is the current position of the
          left-most V Bar cursor and 100% is the current position of the right-most V Bar cursor.
        - ``HALFgrat`` resets the ratio range to the default positions on the screen, half of the
          number of horizontal divisions, from 25% to 75% of the screen.
        - ``FIVEdivs`` sets V Bar measurement scale so that 5 screen major divisions is 100%, where
          0% is -2.5 divisions and 100% is +2.5 divisions from the center vertical graticule.
    """


class CursorVbarsUnits(SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:VBArs:UNIts`` command.

    Description:
        - This command specifies the units for the vertical bar cursors.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:VBArs:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:VBArs:UNIts?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CURSor:VBArs:UNIts value`` command.

    SCPI Syntax:
        ```
        - CURSor:VBArs:UNIts {SEConds|HERtz|DEGrees|PERcent}
        - CURSor:VBArs:UNIts?
        ```

    Info:
        - ``SEConds`` sets the units of the vertical bar cursors for the time domain (seconds).
        - ``HERtz`` sets the units of the vertical bar cursors for the frequency domain (hertz).
        - ``DEGrees`` sets the units to degrees for measuring phase.
        - ``PERcent`` sets the units to percent for use with ratio cursors.
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


class CursorVbarsHposItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``CURSor:VBArs:HPOS<x>`` command.

    Description:
        - Returns the vertical value of the specified vertical bar ticks for cursor <x>.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:VBArs:HPOS<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:VBArs:HPOS<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:VBArs:HPOS<x>?
        ```

    Info:
        - ``<x>`` specifies the cursor. Valid values are 1 and 2.
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


class CursorVbarsAlternateItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``CURSor:VBArs:ALTERNATE<x>`` command.

    Description:
        - Returns the alternate readout for the waveform (Vbar) cursors specified by <x>. This
          alternate readout is in effect when the selected waveform is a bus or digital channel.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:VBArs:ALTERNATE<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:VBArs:ALTERNATE<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:VBArs:ALTERNATE<x>?
        ```

    Info:
        - ``X = 1`` specifies vertical bar cursor1.
        - ``X = 2`` specifies vertical bar cursor2.
    """


class CursorVbars(SCPICmdRead):
    """The ``CURSor:VBArs`` command.

    Description:
        - Returns the current settings for the vertical bar cursors.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:VBArs?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:VBArs?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:VBArs?
        ```

    Properties:
        - ``.alternate``: The ``CURSor:VBArs:ALTERNATE<x>`` command.
        - ``.delta``: The ``CURSor:VBArs:DELTa`` command.
        - ``.hpos``: The ``CURSor:VBArs:HPOS<x>`` command.
        - ``.position``: The ``CURSor:VBArs:POSITION<x>`` command.
        - ``.units``: The ``CURSor:VBArs:UNIts`` command.
        - ``.use``: The ``CURSor:VBArs:USE`` command.
        - ``.vdelta``: The ``CURSor:VBArs:VDELTa`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._alternate: Dict[int, CursorVbarsAlternateItem] = DefaultDictPassKeyToFactory(
            lambda x: CursorVbarsAlternateItem(device, f"{self._cmd_syntax}:ALTERNATE{x}")
        )
        self._delta = CursorVbarsDelta(device, f"{self._cmd_syntax}:DELTa")
        self._hpos: Dict[int, CursorVbarsHposItem] = DefaultDictPassKeyToFactory(
            lambda x: CursorVbarsHposItem(device, f"{self._cmd_syntax}:HPOS{x}")
        )
        self._position: Dict[int, CursorVbarsPositionItem] = DefaultDictPassKeyToFactory(
            lambda x: CursorVbarsPositionItem(device, f"{self._cmd_syntax}:POSITION{x}")
        )
        self._units = CursorVbarsUnits(device, f"{self._cmd_syntax}:UNIts")
        self._use = CursorVbarsUse(device, f"{self._cmd_syntax}:USE")
        self._vdelta = CursorVbarsVdelta(device, f"{self._cmd_syntax}:VDELTa")

    @property
    def alternate(self) -> Dict[int, CursorVbarsAlternateItem]:
        """Return the ``CURSor:VBArs:ALTERNATE<x>`` command.

        Description:
            - Returns the alternate readout for the waveform (Vbar) cursors specified by <x>. This
              alternate readout is in effect when the selected waveform is a bus or digital channel.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:VBArs:ALTERNATE<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:VBArs:ALTERNATE<x>?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:VBArs:ALTERNATE<x>?
            ```

        Info:
            - ``X = 1`` specifies vertical bar cursor1.
            - ``X = 2`` specifies vertical bar cursor2.
        """
        return self._alternate

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
    def hpos(self) -> Dict[int, CursorVbarsHposItem]:
        """Return the ``CURSor:VBArs:HPOS<x>`` command.

        Description:
            - Returns the vertical value of the specified vertical bar ticks for cursor <x>.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:VBArs:HPOS<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:VBArs:HPOS<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:VBArs:HPOS<x>?
            ```

        Info:
            - ``<x>`` specifies the cursor. Valid values are 1 and 2.
        """
        return self._hpos

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
            - This command specifies the units for the vertical bar cursors.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:VBArs:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:VBArs:UNIts?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURSor:VBArs:UNIts value`` command.

        SCPI Syntax:
            ```
            - CURSor:VBArs:UNIts {SEConds|HERtz|DEGrees|PERcent}
            - CURSor:VBArs:UNIts?
            ```

        Info:
            - ``SEConds`` sets the units of the vertical bar cursors for the time domain (seconds).
            - ``HERtz`` sets the units of the vertical bar cursors for the frequency domain (hertz).
            - ``DEGrees`` sets the units to degrees for measuring phase.
            - ``PERcent`` sets the units to percent for use with ratio cursors.
        """
        return self._units

    @property
    def use(self) -> CursorVbarsUse:
        """Return the ``CURSor:VBArs:USE`` command.

        Description:
            - Sets the vertical bar cursor measurement scale.

        Usage:
            - Using the ``.write(value)`` method will send the ``CURSor:VBArs:USE value`` command.

        SCPI Syntax:
            ```
            - CURSor:VBArs:USE {CURrent|HALFgrat|FIVEdivs}
            ```

        Info:
            - ``CURrent`` sets the V Bar measurement scale so that 0% is the current position of the
              left-most V Bar cursor and 100% is the current position of the right-most V Bar
              cursor.
            - ``HALFgrat`` resets the ratio range to the default positions on the screen, half of
              the number of horizontal divisions, from 25% to 75% of the screen.
            - ``FIVEdivs`` sets V Bar measurement scale so that 5 screen major divisions is 100%,
              where 0% is -2.5 divisions and 100% is +2.5 divisions from the center vertical
              graticule.
        """
        return self._use

    @property
    def vdelta(self) -> CursorVbarsVdelta:
        """Return the ``CURSor:VBArs:VDELTa`` command.

        Description:
            - Returns the vertical difference between the two vertical bar cursor ticks.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:VBArs:VDELTa?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:VBArs:VDELTa?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:VBArs:VDELTa?
            ```
        """
        return self._vdelta


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


class CursorHbarsUse(SCPICmdWrite):
    """The ``CURSor:HBArs:USE`` command.

    Description:
        - This command specifies the horizontal bar cursor measurement scale. This command is only
          applicable when the ratio cursors are turned on.

    Usage:
        - Using the ``.write(value)`` method will send the ``CURSor:HBArs:USE value`` command.

    SCPI Syntax:
        ```
        - CURSor:HBArs:USE {CURrent|HALFgrat}
        ```

    Info:
        - ``CURrent`` sets the H Bar measurement scale so that 0% is the current position of the
          lowest H Bar cursor and 100% is the current position of the highest H Bar cursor.
        - ``HALFgrat`` sets H Bar measurement scale so that half the screen major divisions is 100%,
          where 0% is -2.5 divisions and 100% is +2.5 divisions from the center horizontal
          graticule.
    """


class CursorHbarsUnits(SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:HBArs:UNIts`` command.

    Description:
        - This command specifies the units for the horizontal bar cursors.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:HBArs:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:HBArs:UNIts?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CURSor:HBArs:UNIts value`` command.

    SCPI Syntax:
        ```
        - CURSor:HBArs:UNIts {BASE|PERcent}
        - CURSor:HBArs:UNIts?
        ```

    Info:
        - ``BASE`` selects the vertical units for the selected waveform.
        - ``PERcent`` selects ratio cursors.
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
        - ``.use``: The ``CURSor:HBArs:USE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._delta = CursorHbarsDelta(device, f"{self._cmd_syntax}:DELTa")
        self._position: Dict[int, CursorHbarsPositionItem] = DefaultDictPassKeyToFactory(
            lambda x: CursorHbarsPositionItem(device, f"{self._cmd_syntax}:POSITION{x}")
        )
        self._units = CursorHbarsUnits(device, f"{self._cmd_syntax}:UNIts")
        self._use = CursorHbarsUse(device, f"{self._cmd_syntax}:USE")

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
            - This command specifies the units for the horizontal bar cursors.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:HBArs:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:HBArs:UNIts?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURSor:HBArs:UNIts value`` command.

        SCPI Syntax:
            ```
            - CURSor:HBArs:UNIts {BASE|PERcent}
            - CURSor:HBArs:UNIts?
            ```

        Info:
            - ``BASE`` selects the vertical units for the selected waveform.
            - ``PERcent`` selects ratio cursors.
        """
        return self._units

    @property
    def use(self) -> CursorHbarsUse:
        """Return the ``CURSor:HBArs:USE`` command.

        Description:
            - This command specifies the horizontal bar cursor measurement scale. This command is
              only applicable when the ratio cursors are turned on.

        Usage:
            - Using the ``.write(value)`` method will send the ``CURSor:HBArs:USE value`` command.

        SCPI Syntax:
            ```
            - CURSor:HBArs:USE {CURrent|HALFgrat}
            ```

        Info:
            - ``CURrent`` sets the H Bar measurement scale so that 0% is the current position of the
              lowest H Bar cursor and 100% is the current position of the highest H Bar cursor.
            - ``HALFgrat`` sets H Bar measurement scale so that half the screen major divisions is
              100%, where 0% is -2.5 divisions and 100% is +2.5 divisions from the center horizontal
              graticule.
        """
        return self._use


class CursorFunction(SCPICmdWrite, SCPICmdRead):
    """The ``CURSor:FUNCtion`` command.

    Description:
        - This command selects the cursor mode. In Waveform mode, the cursors are attached to the
          selected waveform; in Screen mode, cursors are attached to the display area .

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:FUNCtion?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:FUNCtion?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CURSor:FUNCtion value`` command.

    SCPI Syntax:
        ```
        - CURSor:FUNCtion {SCREEN|WAVEform|OFF}
        - CURSor:FUNCtion?
        ```

    Info:
        - ``SCREEN`` specifies to display both horizontal and vertical bar cursors, which measure
          the selected waveform in horizontal and vertical units. Use these cursors to measure
          anywhere in the waveform display area.
        - ``WAVEform`` specifies to display the paired cursors in YT display format for measuring
          waveform amplitude and time. In XY and XYZ format, these cursors indicate the amplitude
          positions of an XY pair (Ch1 vs Ch2 voltage, where Ch1 is the X axis and Ch2 is the Y
          axis) relative to the trigger.
        - ``OFF`` removes the cursors from the display.
    """


class CursorDdt(SCPICmdRead):
    """The ``CURSor:DDT`` command.

    Description:
        - Returns the cursor deltaY/deltaT (dY/dT) readout.

    Usage:
        - Using the ``.query()`` method will send the ``CURSor:DDT?`` query.
        - Using the ``.verify(value)`` method will send the ``CURSor:DDT?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURSor:DDT?
        ```
    """


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
        - ``.ddt``: The ``CURSor:DDT`` command.
        - ``.function``: The ``CURSor:FUNCtion`` command.
        - ``.hbars``: The ``CURSor:HBArs`` command.
        - ``.mode``: The ``CURSor:MODe`` command.
        - ``.vbars``: The ``CURSor:VBArs`` command.
        - ``.xy``: The ``CURSor:XY`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "CURSor") -> None:
        super().__init__(device, cmd_syntax)
        self._ddt = CursorDdt(device, f"{self._cmd_syntax}:DDT")
        self._function = CursorFunction(device, f"{self._cmd_syntax}:FUNCtion")
        self._hbars = CursorHbars(device, f"{self._cmd_syntax}:HBArs")
        self._mode = CursorMode(device, f"{self._cmd_syntax}:MODe")
        self._vbars = CursorVbars(device, f"{self._cmd_syntax}:VBArs")
        self._xy = CursorXy(device, f"{self._cmd_syntax}:XY")

    @property
    def ddt(self) -> CursorDdt:
        """Return the ``CURSor:DDT`` command.

        Description:
            - Returns the cursor deltaY/deltaT (dY/dT) readout.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:DDT?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:DDT?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:DDT?
            ```
        """
        return self._ddt

    @property
    def function(self) -> CursorFunction:
        """Return the ``CURSor:FUNCtion`` command.

        Description:
            - This command selects the cursor mode. In Waveform mode, the cursors are attached to
              the selected waveform; in Screen mode, cursors are attached to the display area .

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:FUNCtion?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:FUNCtion?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURSor:FUNCtion value`` command.

        SCPI Syntax:
            ```
            - CURSor:FUNCtion {SCREEN|WAVEform|OFF}
            - CURSor:FUNCtion?
            ```

        Info:
            - ``SCREEN`` specifies to display both horizontal and vertical bar cursors, which
              measure the selected waveform in horizontal and vertical units. Use these cursors to
              measure anywhere in the waveform display area.
            - ``WAVEform`` specifies to display the paired cursors in YT display format for
              measuring waveform amplitude and time. In XY and XYZ format, these cursors indicate
              the amplitude positions of an XY pair (Ch1 vs Ch2 voltage, where Ch1 is the X axis and
              Ch2 is the Y axis) relative to the trigger.
            - ``OFF`` removes the cursors from the display.
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
            - ``.use``: The ``CURSor:HBArs:USE`` command.
        """
        return self._hbars

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
    def vbars(self) -> CursorVbars:
        """Return the ``CURSor:VBArs`` command.

        Description:
            - Returns the current settings for the vertical bar cursors.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:VBArs?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:VBArs?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor:VBArs?
            ```

        Sub-properties:
            - ``.alternate``: The ``CURSor:VBArs:ALTERNATE<x>`` command.
            - ``.delta``: The ``CURSor:VBArs:DELTa`` command.
            - ``.hpos``: The ``CURSor:VBArs:HPOS<x>`` command.
            - ``.position``: The ``CURSor:VBArs:POSITION<x>`` command.
            - ``.units``: The ``CURSor:VBArs:UNIts`` command.
            - ``.use``: The ``CURSor:VBArs:USE`` command.
            - ``.vdelta``: The ``CURSor:VBArs:VDELTa`` command.
        """
        return self._vbars

    @property
    def xy(self) -> CursorXy:
        """Return the ``CURSor:XY`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor:XY?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor:XY?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.polar``: The ``CURSor:XY:POLar`` command tree.
            - ``.product``: The ``CURSor:XY:PRODUCT`` command tree.
            - ``.ratio``: The ``CURSor:XY:RATIO`` command tree.
            - ``.readout``: The ``CURSor:XY:READOUT`` command.
            - ``.rectangular``: The ``CURSor:XY:RECTangular`` command tree.
        """
        return self._xy
