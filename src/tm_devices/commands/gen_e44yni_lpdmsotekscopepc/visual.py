# pylint: disable=line-too-long
"""The visual commands module.

These commands are used in the following models:
LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - VISual:AREA<x>:ASPEctratio {ON|OFF|<NR1>}
    - VISual:AREA<x>:ASPEctratio?
    - VISual:AREA<x>:FLIP:HORizontal
    - VISual:AREA<x>:FLIP:VERTical
    - VISual:AREA<x>:HEIGht <NR3>
    - VISual:AREA<x>:HEIGht?
    - VISual:AREA<x>:HITType {IN|OUT|DONTcare}
    - VISual:AREA<x>:HITType?
    - VISual:AREA<x>:RESET
    - VISual:AREA<x>:ROTAtion <NR3>
    - VISual:AREA<x>:ROTAtion?
    - VISual:AREA<x>:SHAPE {TRIAngle|RECTangle|TRAPezoid|HEXAgon}
    - VISual:AREA<x>:SHAPE?
    - VISual:AREA<x>:SOUrce {CH<x>}
    - VISual:AREA<x>:SOUrce?
    - VISual:AREA<x>:VERTICES '<NR3>, <NR3>, <NR3>, <NR3>, <NR3>, <NR3> [,<NR3>, <NR3>, ...]'
    - VISual:AREA<x>:VERTICES?
    - VISual:AREA<x>:WIDTH <NR3>
    - VISual:AREA<x>:WIDTH?
    - VISual:AREA<x>:XPOSition <NR3>
    - VISual:AREA<x>:XPOSition?
    - VISual:AREA<x>:YPOSition <NR3>
    - VISual:AREA<x>:YPOSition?
    - VISual:DELETEALL
    - VISual:ENAble {ON|OFF|<NR1>}
    - VISual:ENAble?
    - VISual:EQUation <Qstring>
    - VISual:EQUation?
    - VISual:SHOWAReas {ON|OFF|<NR1>}
    - VISual:SHOWAReas?
    - VISual:SHOWCRiteria {ON|OFF|<NR1>}
    - VISual:SHOWCRiteria?
    - VISual:SHOWEQuation {ON|OFF|<NR1>}
    - VISual:SHOWEQuation?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    SCPICmdWriteNoArguments,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class VisualShowequation(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:SHOWEQuation`` command.

    Description:
        - Shows or hides the Visual Trigger area combination logic equation.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:SHOWEQuation?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:SHOWEQuation?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:SHOWEQuation value`` command.

    SCPI Syntax:
        ```
        - VISual:SHOWEQuation {ON|OFF|<NR1>}
        - VISual:SHOWEQuation?
        ```

    Info:
        - ``ON`` shows the Visual Trigger area combination logic equation.
        - ``OFF`` hides the Visual Trigger area combination logic equation.
        - ``<NR1>`` is an integer number. 0 hides the area combination logic equation; any other
          value displays the area combination logic equation.
    """


class VisualShowcriteria(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:SHOWCRiteria`` command.

    Description:
        - Sets or queries display of the area names and hit criteria for all visual trigger areas.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:SHOWCRiteria?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:SHOWCRiteria?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:SHOWCRiteria value`` command.

    SCPI Syntax:
        ```
        - VISual:SHOWCRiteria {ON|OFF|<NR1>}
        - VISual:SHOWCRiteria?
        ```

    Info:
        - ``ON`` enables display of the area name and hit criteria labels (In, Out, Don't care
          icons) of all Visual Trigger areas.
        - ``OFF`` hides the area name and hit criteria labels (In, Out, Don't care icons) of all
          Visual Trigger areas.
        - ``<NR1>`` is an integer number. 0 hides the area name and hit criteria of all Visual
          Trigger areas; any other value enables displaying the area name and hit criteria of all
          Visual Trigger areas.
    """


class VisualShowareas(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:SHOWAReas`` command.

    Description:
        - Shows or hides all Visual Trigger areas.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:SHOWAReas?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:SHOWAReas?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:SHOWAReas value`` command.

    SCPI Syntax:
        ```
        - VISual:SHOWAReas {ON|OFF|<NR1>}
        - VISual:SHOWAReas?
        ```

    Info:
        - ``ON`` shows all Visual Trigger areas.
        - ``OFF`` hides all Visual Trigger areas.
        - ``<NR1>`` is an integer number. 0 hides all Visual Trigger areas; any other value shows
          all Visual Trigger areas.
    """


class VisualEquation(SCPICmdWrite, SCPICmdRead):
    r"""The ``VISual:EQUation`` command.

    Description:
        - Sets or queries the Visual Trigger area combination logic equation.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:EQUation?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:EQUation?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:EQUation value`` command.

    SCPI Syntax:
        ```
        - VISual:EQUation <Qstring>
        - VISual:EQUation?
        ```

    Info:
        - ``<Qstring>`` defines the Visual Trigger area combination logic equation. The equation is
          made up of area names (A<x>) combined with logic operators AND, OR, or XOR (&, \|, ^). It
          may also contain parentheses for grouping. The equation must be true to have a valid
          Visual Trigger event and display a waveform. Each area's true state depends on the area's
          condition setting (In, Out or Don't Care).
    """


class VisualEnable(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:ENAble`` command.

    Description:
        - Sets or queries the status (on or off) of the Visual Trigger mode.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:ENAble?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:ENAble?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:ENAble value`` command.

    SCPI Syntax:
        ```
        - VISual:ENAble {ON|OFF|<NR1>}
        - VISual:ENAble?
        ```

    Info:
        - ``ON`` enables the Visual Trigger mode.
        - ``OFF`` disables the Visual Trigger mode.
        - ``<NR1>`` is an integer number. 0 turns off the Visual Trigger mode; any other value
          enables Visual Trigger mode.
    """


class VisualDeleteall(SCPICmdWriteNoArguments):
    """The ``VISual:DELETEALL`` command.

    Description:
        - Deletes all Visual Trigger areas.

    Usage:
        - Using the ``.write()`` method will send the ``VISual:DELETEALL`` command.

    SCPI Syntax:
        ```
        - VISual:DELETEALL
        ```
    """


class VisualAreaItemYposition(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:AREA<x>:YPOSition`` command.

    Description:
        - Sets or queries the vertical (Y-axis) center position of the specified Visual Trigger
          area.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:AREA<x>:YPOSition?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:YPOSition?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:YPOSition value``
          command.

    SCPI Syntax:
        ```
        - VISual:AREA<x>:YPOSition <NR3>
        - VISual:AREA<x>:YPOSition?
        ```

    Info:
        - ``Area<x>`` specifies the integer number of a Visual Trigger area.
        - ``<NR3>`` specifies the vertical position of the center of the Visual Trigger area, in
          amplitude (volts, amps).
    """


class VisualAreaItemXposition(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:AREA<x>:XPOSition`` command.

    Description:
        - Sets or queries the horizontal (X-axis) center position of the specified Visual Trigger
          area.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:AREA<x>:XPOSition?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:XPOSition?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:XPOSition value``
          command.

    SCPI Syntax:
        ```
        - VISual:AREA<x>:XPOSition <NR3>
        - VISual:AREA<x>:XPOSition?
        ```

    Info:
        - ``Area<x>`` specifies the integer number of a Visual Trigger area.
        - ``<NR3>`` specifies the horizontal position of the center of the Visual Trigger area, in
          seconds.
    """


class VisualAreaItemWidth(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:AREA<x>:WIDTH`` command.

    Description:
        - Sets or queries the width of the specified Visual Trigger area.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:AREA<x>:WIDTH?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:WIDTH?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:WIDTH value`` command.

    SCPI Syntax:
        ```
        - VISual:AREA<x>:WIDTH <NR3>
        - VISual:AREA<x>:WIDTH?
        ```

    Info:
        - ``Area<x>`` specifies the integer number of a Visual Trigger area.
        - ``<NR3>`` specifies the width of the Visual Trigger area in seconds.
    """


class VisualAreaItemVertices(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:AREA<x>:VERTICES`` command.

    Description:
        - Sets or queries the X and Y vertex coordinate values for all vertices of the specified
          Visual Trigger area. Vertex values must be set in pairs.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:AREA<x>:VERTICES?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:VERTICES?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:VERTICES value``
          command.

    SCPI Syntax:
        ```
        - VISual:AREA<x>:VERTICES '<NR3>, <NR3>, <NR3>, <NR3>, <NR3>, <NR3> [,<NR3>, <NR3>, ...]'
        - VISual:AREA<x>:VERTICES?
        ```

    Info:
        - ``Area<x>`` specifies the integer number of a Visual Trigger area.
        - ``<NR3>, <NR3>`` specifies the X, Y coordinate pair of each vertex in an area. The first
          value is X (time) and the second value is Y (amplitude). There must be a minimum of three
          vertex pairs to create an area. If the specified area exists, the area is changed to the
          shape specified in the arguments. If the specified area does not exist, a new area is
          created and assigned the specified vertices.
    """


class VisualAreaItemSource(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:AREA<x>:SOUrce`` command.

    Description:
        - Sets or queries the signal source for the specified Visual Trigger area. The source can
          only be an analog channel.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:AREA<x>:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:SOUrce value`` command.

    SCPI Syntax:
        ```
        - VISual:AREA<x>:SOUrce {CH<x>}
        - VISual:AREA<x>:SOUrce?
        ```

    Info:
        - ``Area<x>`` specifies the integer number of a Visual Trigger area.
        - ``CH<x>`` sets the source channel number for the specified area. The channel number is
          specified by <x>.
    """


class VisualAreaItemShape(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:AREA<x>:SHAPE`` command.

    Description:
        - Sets or queries the current shape of the area.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:AREA<x>:SHAPE?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:SHAPE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:SHAPE value`` command.

    SCPI Syntax:
        ```
        - VISual:AREA<x>:SHAPE {TRIAngle|RECTangle|TRAPezoid|HEXAgon}
        - VISual:AREA<x>:SHAPE?
        ```

    Info:
        - ``Area<x>`` specifies the integer number of a Visual Trigger area.
        - ``TRIAngle`` sets the specified area to a triangular shape (three vertices). If the area
          does not exist, the instrument creates a new triangular area with the specified area
          number.
        - ``RECTangle`` sets the specified area to a rectangular shape (four vertices, right angles
          at each corner). If the area does not exist, the instrument creates a new triangular area
          with the specified area number.
        - ``TRAPezoid`` sets the specified area to a trapezoidal shape (four vertices, two parallel
          sides). If the area does not exist, the instrument creates a new triangular area with the
          specified area number.
        - ``HEXAgon`` sets the specified area to a hexagonal shape (six vertices). If the area does
          not exist, the instrument creates a new hexagonal area with the specified area number.
    """


class VisualAreaItemRotation(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:AREA<x>:ROTAtion`` command.

    Description:
        - Sets or queries the rotation angle of the specified Visual Trigger area.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:AREA<x>:ROTAtion?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:ROTAtion?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:ROTAtion value``
          command.

    SCPI Syntax:
        ```
        - VISual:AREA<x>:ROTAtion <NR3>
        - VISual:AREA<x>:ROTAtion?
        ```

    Info:
        - ``Area<x>`` specifies the integer number of a Visual Trigger area.
        - ``<NR3>`` specifies the rotation angle of the Visual Trigger area, in positive degrees
          from 0 to 360. Zero degrees is referenced from when the area was created.
    """


class VisualAreaItemReset(SCPICmdWriteNoArguments):
    """The ``VISual:AREA<x>:RESET`` command.

    Description:
        - Sets the specified Visual Trigger area shape to a default-sized triangle.

    Usage:
        - Using the ``.write()`` method will send the ``VISual:AREA<x>:RESET`` command.

    SCPI Syntax:
        ```
        - VISual:AREA<x>:RESET
        ```

    Info:
        - ``Area<x>`` specifies the integer number of a Visual Trigger area.
    """


class VisualAreaItemHittype(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:AREA<x>:HITType`` command.

    Description:
        - Sets or queries the area hit logic true condition for the specified Visual Trigger area.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:AREA<x>:HITType?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:HITType?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:HITType value`` command.

    SCPI Syntax:
        ```
        - VISual:AREA<x>:HITType {IN|OUT|DONTcare}
        - VISual:AREA<x>:HITType?
        ```

    Info:
        - ``Area<x>`` specifies the integer number of a Visual Trigger area.
        - ``IN`` specifies that the waveform must intrude anywhere into the specified area to be
          true.
        - ``OUT`` specifies that the waveform must not intrude anywhere into the specified area to
          be true.
        - ``DONTcare`` sets the area to a don't care state, causing the area to be ignored. This is
          useful when you are developing a Visual Trigger condition and need to change the hit logic
          type of an area while keeping the area.
    """


class VisualAreaItemHeight(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:AREA<x>:HEIGht`` command.

    Description:
        - Sets or queries the height of the specified Visual Trigger area.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:AREA<x>:HEIGht?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:HEIGht?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:HEIGht value`` command.

    SCPI Syntax:
        ```
        - VISual:AREA<x>:HEIGht <NR3>
        - VISual:AREA<x>:HEIGht?
        ```

    Info:
        - ``Area<x>`` specifies the integer number of a Visual Trigger area.
        - ``<NR3>`` specifies the height of the Visual Trigger area in amplitude.
    """


class VisualAreaItemFlipVertical(SCPICmdWriteNoArguments):
    """The ``VISual:AREA<x>:FLIP:VERTical`` command.

    Description:
        - Flips the specified Visual Trigger area vertically around its center point.

    Usage:
        - Using the ``.write()`` method will send the ``VISual:AREA<x>:FLIP:VERTical`` command.

    SCPI Syntax:
        ```
        - VISual:AREA<x>:FLIP:VERTical
        ```

    Info:
        - ``Area<x>`` specifies the integer number of a Visual Trigger area.
    """


class VisualAreaItemFlipHorizontal(SCPICmdWriteNoArguments):
    """The ``VISual:AREA<x>:FLIP:HORizontal`` command.

    Description:
        - Flips the specified Visual Trigger area horizontally around its center point.

    Usage:
        - Using the ``.write()`` method will send the ``VISual:AREA<x>:FLIP:HORizontal`` command.

    SCPI Syntax:
        ```
        - VISual:AREA<x>:FLIP:HORizontal
        ```

    Info:
        - ``Area<x>`` specifies the integer number of a Visual Trigger area.
    """


class VisualAreaItemFlip(SCPICmdRead):
    """The ``VISual:AREA<x>:FLIP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:AREA<x>:FLIP?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:FLIP?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.horizontal``: The ``VISual:AREA<x>:FLIP:HORizontal`` command.
        - ``.vertical``: The ``VISual:AREA<x>:FLIP:VERTical`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._horizontal = VisualAreaItemFlipHorizontal(device, f"{self._cmd_syntax}:HORizontal")
        self._vertical = VisualAreaItemFlipVertical(device, f"{self._cmd_syntax}:VERTical")

    @property
    def horizontal(self) -> VisualAreaItemFlipHorizontal:
        """Return the ``VISual:AREA<x>:FLIP:HORizontal`` command.

        Description:
            - Flips the specified Visual Trigger area horizontally around its center point.

        Usage:
            - Using the ``.write()`` method will send the ``VISual:AREA<x>:FLIP:HORizontal``
              command.

        SCPI Syntax:
            ```
            - VISual:AREA<x>:FLIP:HORizontal
            ```

        Info:
            - ``Area<x>`` specifies the integer number of a Visual Trigger area.
        """
        return self._horizontal

    @property
    def vertical(self) -> VisualAreaItemFlipVertical:
        """Return the ``VISual:AREA<x>:FLIP:VERTical`` command.

        Description:
            - Flips the specified Visual Trigger area vertically around its center point.

        Usage:
            - Using the ``.write()`` method will send the ``VISual:AREA<x>:FLIP:VERTical`` command.

        SCPI Syntax:
            ```
            - VISual:AREA<x>:FLIP:VERTical
            ```

        Info:
            - ``Area<x>`` specifies the integer number of a Visual Trigger area.
        """
        return self._vertical


class VisualAreaItemAspectratio(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:AREA<x>:ASPEctratio`` command.

    Description:
        - Sets or queries whether the aspect ratio of the specified Visual Trigger area is locked.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:AREA<x>:ASPEctratio?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:ASPEctratio?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:ASPEctratio value``
          command.

    SCPI Syntax:
        ```
        - VISual:AREA<x>:ASPEctratio {ON|OFF|<NR1>}
        - VISual:AREA<x>:ASPEctratio?
        ```

    Info:
        - ``Area<x>`` specifies the integer number of a Visual Trigger area.
        - ``ON`` locks the aspect ratio of the specified Visual Trigger area. The aspect ratio is
          kept constant when the height or width of the area changes.
        - ``OFF`` unlocks the aspect ratio of the specified Visual Trigger area.
        - ``<NR1>`` is an integer number. 1 locks the aspect ratio of the specified Visual Trigger
          area; any other value unlocks the aspect ratio of the specified Visual Trigger area.
    """


#  pylint: disable=too-many-instance-attributes
class VisualAreaItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``VISual:AREA<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:AREA<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.aspectratio``: The ``VISual:AREA<x>:ASPEctratio`` command.
        - ``.flip``: The ``VISual:AREA<x>:FLIP`` command tree.
        - ``.height``: The ``VISual:AREA<x>:HEIGht`` command.
        - ``.hittype``: The ``VISual:AREA<x>:HITType`` command.
        - ``.reset``: The ``VISual:AREA<x>:RESET`` command.
        - ``.rotation``: The ``VISual:AREA<x>:ROTAtion`` command.
        - ``.shape``: The ``VISual:AREA<x>:SHAPE`` command.
        - ``.source``: The ``VISual:AREA<x>:SOUrce`` command.
        - ``.vertices``: The ``VISual:AREA<x>:VERTICES`` command.
        - ``.width``: The ``VISual:AREA<x>:WIDTH`` command.
        - ``.xposition``: The ``VISual:AREA<x>:XPOSition`` command.
        - ``.yposition``: The ``VISual:AREA<x>:YPOSition`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._aspectratio = VisualAreaItemAspectratio(device, f"{self._cmd_syntax}:ASPEctratio")
        self._flip = VisualAreaItemFlip(device, f"{self._cmd_syntax}:FLIP")
        self._height = VisualAreaItemHeight(device, f"{self._cmd_syntax}:HEIGht")
        self._hittype = VisualAreaItemHittype(device, f"{self._cmd_syntax}:HITType")
        self._reset = VisualAreaItemReset(device, f"{self._cmd_syntax}:RESET")
        self._rotation = VisualAreaItemRotation(device, f"{self._cmd_syntax}:ROTAtion")
        self._shape = VisualAreaItemShape(device, f"{self._cmd_syntax}:SHAPE")
        self._source = VisualAreaItemSource(device, f"{self._cmd_syntax}:SOUrce")
        self._vertices = VisualAreaItemVertices(device, f"{self._cmd_syntax}:VERTICES")
        self._width = VisualAreaItemWidth(device, f"{self._cmd_syntax}:WIDTH")
        self._xposition = VisualAreaItemXposition(device, f"{self._cmd_syntax}:XPOSition")
        self._yposition = VisualAreaItemYposition(device, f"{self._cmd_syntax}:YPOSition")

    @property
    def aspectratio(self) -> VisualAreaItemAspectratio:
        """Return the ``VISual:AREA<x>:ASPEctratio`` command.

        Description:
            - Sets or queries whether the aspect ratio of the specified Visual Trigger area is
              locked.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:AREA<x>:ASPEctratio?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:ASPEctratio?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:ASPEctratio value``
              command.

        SCPI Syntax:
            ```
            - VISual:AREA<x>:ASPEctratio {ON|OFF|<NR1>}
            - VISual:AREA<x>:ASPEctratio?
            ```

        Info:
            - ``Area<x>`` specifies the integer number of a Visual Trigger area.
            - ``ON`` locks the aspect ratio of the specified Visual Trigger area. The aspect ratio
              is kept constant when the height or width of the area changes.
            - ``OFF`` unlocks the aspect ratio of the specified Visual Trigger area.
            - ``<NR1>`` is an integer number. 1 locks the aspect ratio of the specified Visual
              Trigger area; any other value unlocks the aspect ratio of the specified Visual Trigger
              area.
        """
        return self._aspectratio

    @property
    def flip(self) -> VisualAreaItemFlip:
        """Return the ``VISual:AREA<x>:FLIP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:AREA<x>:FLIP?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:FLIP?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.horizontal``: The ``VISual:AREA<x>:FLIP:HORizontal`` command.
            - ``.vertical``: The ``VISual:AREA<x>:FLIP:VERTical`` command.
        """
        return self._flip

    @property
    def height(self) -> VisualAreaItemHeight:
        """Return the ``VISual:AREA<x>:HEIGht`` command.

        Description:
            - Sets or queries the height of the specified Visual Trigger area.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:AREA<x>:HEIGht?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:HEIGht?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:HEIGht value``
              command.

        SCPI Syntax:
            ```
            - VISual:AREA<x>:HEIGht <NR3>
            - VISual:AREA<x>:HEIGht?
            ```

        Info:
            - ``Area<x>`` specifies the integer number of a Visual Trigger area.
            - ``<NR3>`` specifies the height of the Visual Trigger area in amplitude.
        """
        return self._height

    @property
    def hittype(self) -> VisualAreaItemHittype:
        """Return the ``VISual:AREA<x>:HITType`` command.

        Description:
            - Sets or queries the area hit logic true condition for the specified Visual Trigger
              area.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:AREA<x>:HITType?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:HITType?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:HITType value``
              command.

        SCPI Syntax:
            ```
            - VISual:AREA<x>:HITType {IN|OUT|DONTcare}
            - VISual:AREA<x>:HITType?
            ```

        Info:
            - ``Area<x>`` specifies the integer number of a Visual Trigger area.
            - ``IN`` specifies that the waveform must intrude anywhere into the specified area to be
              true.
            - ``OUT`` specifies that the waveform must not intrude anywhere into the specified area
              to be true.
            - ``DONTcare`` sets the area to a don't care state, causing the area to be ignored. This
              is useful when you are developing a Visual Trigger condition and need to change the
              hit logic type of an area while keeping the area.
        """
        return self._hittype

    @property
    def reset(self) -> VisualAreaItemReset:
        """Return the ``VISual:AREA<x>:RESET`` command.

        Description:
            - Sets the specified Visual Trigger area shape to a default-sized triangle.

        Usage:
            - Using the ``.write()`` method will send the ``VISual:AREA<x>:RESET`` command.

        SCPI Syntax:
            ```
            - VISual:AREA<x>:RESET
            ```

        Info:
            - ``Area<x>`` specifies the integer number of a Visual Trigger area.
        """
        return self._reset

    @property
    def rotation(self) -> VisualAreaItemRotation:
        """Return the ``VISual:AREA<x>:ROTAtion`` command.

        Description:
            - Sets or queries the rotation angle of the specified Visual Trigger area.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:AREA<x>:ROTAtion?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:ROTAtion?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:ROTAtion value``
              command.

        SCPI Syntax:
            ```
            - VISual:AREA<x>:ROTAtion <NR3>
            - VISual:AREA<x>:ROTAtion?
            ```

        Info:
            - ``Area<x>`` specifies the integer number of a Visual Trigger area.
            - ``<NR3>`` specifies the rotation angle of the Visual Trigger area, in positive degrees
              from 0 to 360. Zero degrees is referenced from when the area was created.
        """
        return self._rotation

    @property
    def shape(self) -> VisualAreaItemShape:
        """Return the ``VISual:AREA<x>:SHAPE`` command.

        Description:
            - Sets or queries the current shape of the area.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:AREA<x>:SHAPE?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:SHAPE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:SHAPE value``
              command.

        SCPI Syntax:
            ```
            - VISual:AREA<x>:SHAPE {TRIAngle|RECTangle|TRAPezoid|HEXAgon}
            - VISual:AREA<x>:SHAPE?
            ```

        Info:
            - ``Area<x>`` specifies the integer number of a Visual Trigger area.
            - ``TRIAngle`` sets the specified area to a triangular shape (three vertices). If the
              area does not exist, the instrument creates a new triangular area with the specified
              area number.
            - ``RECTangle`` sets the specified area to a rectangular shape (four vertices, right
              angles at each corner). If the area does not exist, the instrument creates a new
              triangular area with the specified area number.
            - ``TRAPezoid`` sets the specified area to a trapezoidal shape (four vertices, two
              parallel sides). If the area does not exist, the instrument creates a new triangular
              area with the specified area number.
            - ``HEXAgon`` sets the specified area to a hexagonal shape (six vertices). If the area
              does not exist, the instrument creates a new hexagonal area with the specified area
              number.
        """
        return self._shape

    @property
    def source(self) -> VisualAreaItemSource:
        """Return the ``VISual:AREA<x>:SOUrce`` command.

        Description:
            - Sets or queries the signal source for the specified Visual Trigger area. The source
              can only be an analog channel.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:AREA<x>:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - VISual:AREA<x>:SOUrce {CH<x>}
            - VISual:AREA<x>:SOUrce?
            ```

        Info:
            - ``Area<x>`` specifies the integer number of a Visual Trigger area.
            - ``CH<x>`` sets the source channel number for the specified area. The channel number is
              specified by <x>.
        """
        return self._source

    @property
    def vertices(self) -> VisualAreaItemVertices:
        """Return the ``VISual:AREA<x>:VERTICES`` command.

        Description:
            - Sets or queries the X and Y vertex coordinate values for all vertices of the specified
              Visual Trigger area. Vertex values must be set in pairs.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:AREA<x>:VERTICES?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:VERTICES?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:VERTICES value``
              command.

        SCPI Syntax:
            ```
            - VISual:AREA<x>:VERTICES '<NR3>, <NR3>, <NR3>, <NR3>, <NR3>, <NR3> [,<NR3>, <NR3>, ...]'
            - VISual:AREA<x>:VERTICES?
            ```

        Info:
            - ``Area<x>`` specifies the integer number of a Visual Trigger area.
            - ``<NR3>, <NR3>`` specifies the X, Y coordinate pair of each vertex in an area. The
              first value is X (time) and the second value is Y (amplitude). There must be a minimum
              of three vertex pairs to create an area. If the specified area exists, the area is
              changed to the shape specified in the arguments. If the specified area does not exist,
              a new area is created and assigned the specified vertices.
        """  # noqa: E501
        return self._vertices

    @property
    def width(self) -> VisualAreaItemWidth:
        """Return the ``VISual:AREA<x>:WIDTH`` command.

        Description:
            - Sets or queries the width of the specified Visual Trigger area.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:AREA<x>:WIDTH?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:WIDTH?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:WIDTH value``
              command.

        SCPI Syntax:
            ```
            - VISual:AREA<x>:WIDTH <NR3>
            - VISual:AREA<x>:WIDTH?
            ```

        Info:
            - ``Area<x>`` specifies the integer number of a Visual Trigger area.
            - ``<NR3>`` specifies the width of the Visual Trigger area in seconds.
        """
        return self._width

    @property
    def xposition(self) -> VisualAreaItemXposition:
        """Return the ``VISual:AREA<x>:XPOSition`` command.

        Description:
            - Sets or queries the horizontal (X-axis) center position of the specified Visual
              Trigger area.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:AREA<x>:XPOSition?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:XPOSition?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:XPOSition value``
              command.

        SCPI Syntax:
            ```
            - VISual:AREA<x>:XPOSition <NR3>
            - VISual:AREA<x>:XPOSition?
            ```

        Info:
            - ``Area<x>`` specifies the integer number of a Visual Trigger area.
            - ``<NR3>`` specifies the horizontal position of the center of the Visual Trigger area,
              in seconds.
        """
        return self._xposition

    @property
    def yposition(self) -> VisualAreaItemYposition:
        """Return the ``VISual:AREA<x>:YPOSition`` command.

        Description:
            - Sets or queries the vertical (Y-axis) center position of the specified Visual Trigger
              area.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:AREA<x>:YPOSition?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:YPOSition?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:YPOSition value``
              command.

        SCPI Syntax:
            ```
            - VISual:AREA<x>:YPOSition <NR3>
            - VISual:AREA<x>:YPOSition?
            ```

        Info:
            - ``Area<x>`` specifies the integer number of a Visual Trigger area.
            - ``<NR3>`` specifies the vertical position of the center of the Visual Trigger area, in
              amplitude (volts, amps).
        """
        return self._yposition


class Visual(SCPICmdRead):
    """The ``VISual`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``VISual?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.area``: The ``VISual:AREA<x>`` command tree.
        - ``.deleteall``: The ``VISual:DELETEALL`` command.
        - ``.enable``: The ``VISual:ENAble`` command.
        - ``.equation``: The ``VISual:EQUation`` command.
        - ``.showareas``: The ``VISual:SHOWAReas`` command.
        - ``.showcriteria``: The ``VISual:SHOWCRiteria`` command.
        - ``.showequation``: The ``VISual:SHOWEQuation`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "VISual") -> None:
        super().__init__(device, cmd_syntax)
        self._area: Dict[int, VisualAreaItem] = DefaultDictPassKeyToFactory(
            lambda x: VisualAreaItem(device, f"{self._cmd_syntax}:AREA{x}")
        )
        self._deleteall = VisualDeleteall(device, f"{self._cmd_syntax}:DELETEALL")
        self._enable = VisualEnable(device, f"{self._cmd_syntax}:ENAble")
        self._equation = VisualEquation(device, f"{self._cmd_syntax}:EQUation")
        self._showareas = VisualShowareas(device, f"{self._cmd_syntax}:SHOWAReas")
        self._showcriteria = VisualShowcriteria(device, f"{self._cmd_syntax}:SHOWCRiteria")
        self._showequation = VisualShowequation(device, f"{self._cmd_syntax}:SHOWEQuation")

    @property
    def area(self) -> Dict[int, VisualAreaItem]:
        """Return the ``VISual:AREA<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:AREA<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.aspectratio``: The ``VISual:AREA<x>:ASPEctratio`` command.
            - ``.flip``: The ``VISual:AREA<x>:FLIP`` command tree.
            - ``.height``: The ``VISual:AREA<x>:HEIGht`` command.
            - ``.hittype``: The ``VISual:AREA<x>:HITType`` command.
            - ``.reset``: The ``VISual:AREA<x>:RESET`` command.
            - ``.rotation``: The ``VISual:AREA<x>:ROTAtion`` command.
            - ``.shape``: The ``VISual:AREA<x>:SHAPE`` command.
            - ``.source``: The ``VISual:AREA<x>:SOUrce`` command.
            - ``.vertices``: The ``VISual:AREA<x>:VERTICES`` command.
            - ``.width``: The ``VISual:AREA<x>:WIDTH`` command.
            - ``.xposition``: The ``VISual:AREA<x>:XPOSition`` command.
            - ``.yposition``: The ``VISual:AREA<x>:YPOSition`` command.
        """
        return self._area

    @property
    def deleteall(self) -> VisualDeleteall:
        """Return the ``VISual:DELETEALL`` command.

        Description:
            - Deletes all Visual Trigger areas.

        Usage:
            - Using the ``.write()`` method will send the ``VISual:DELETEALL`` command.

        SCPI Syntax:
            ```
            - VISual:DELETEALL
            ```
        """
        return self._deleteall

    @property
    def enable(self) -> VisualEnable:
        """Return the ``VISual:ENAble`` command.

        Description:
            - Sets or queries the status (on or off) of the Visual Trigger mode.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:ENAble?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:ENAble?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:ENAble value`` command.

        SCPI Syntax:
            ```
            - VISual:ENAble {ON|OFF|<NR1>}
            - VISual:ENAble?
            ```

        Info:
            - ``ON`` enables the Visual Trigger mode.
            - ``OFF`` disables the Visual Trigger mode.
            - ``<NR1>`` is an integer number. 0 turns off the Visual Trigger mode; any other value
              enables Visual Trigger mode.
        """
        return self._enable

    @property
    def equation(self) -> VisualEquation:
        r"""Return the ``VISual:EQUation`` command.

        Description:
            - Sets or queries the Visual Trigger area combination logic equation.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:EQUation?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:EQUation?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:EQUation value`` command.

        SCPI Syntax:
            ```
            - VISual:EQUation <Qstring>
            - VISual:EQUation?
            ```

        Info:
            - ``<Qstring>`` defines the Visual Trigger area combination logic equation. The equation
              is made up of area names (A<x>) combined with logic operators AND, OR, or XOR (&, \|,
              ^). It may also contain parentheses for grouping. The equation must be true to have a
              valid Visual Trigger event and display a waveform. Each area's true state depends on
              the area's condition setting (In, Out or Don't Care).
        """
        return self._equation

    @property
    def showareas(self) -> VisualShowareas:
        """Return the ``VISual:SHOWAReas`` command.

        Description:
            - Shows or hides all Visual Trigger areas.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:SHOWAReas?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:SHOWAReas?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:SHOWAReas value`` command.

        SCPI Syntax:
            ```
            - VISual:SHOWAReas {ON|OFF|<NR1>}
            - VISual:SHOWAReas?
            ```

        Info:
            - ``ON`` shows all Visual Trigger areas.
            - ``OFF`` hides all Visual Trigger areas.
            - ``<NR1>`` is an integer number. 0 hides all Visual Trigger areas; any other value
              shows all Visual Trigger areas.
        """
        return self._showareas

    @property
    def showcriteria(self) -> VisualShowcriteria:
        """Return the ``VISual:SHOWCRiteria`` command.

        Description:
            - Sets or queries display of the area names and hit criteria for all visual trigger
              areas.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:SHOWCRiteria?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:SHOWCRiteria?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:SHOWCRiteria value``
              command.

        SCPI Syntax:
            ```
            - VISual:SHOWCRiteria {ON|OFF|<NR1>}
            - VISual:SHOWCRiteria?
            ```

        Info:
            - ``ON`` enables display of the area name and hit criteria labels (In, Out, Don't care
              icons) of all Visual Trigger areas.
            - ``OFF`` hides the area name and hit criteria labels (In, Out, Don't care icons) of all
              Visual Trigger areas.
            - ``<NR1>`` is an integer number. 0 hides the area name and hit criteria of all Visual
              Trigger areas; any other value enables displaying the area name and hit criteria of
              all Visual Trigger areas.
        """
        return self._showcriteria

    @property
    def showequation(self) -> VisualShowequation:
        """Return the ``VISual:SHOWEQuation`` command.

        Description:
            - Shows or hides the Visual Trigger area combination logic equation.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:SHOWEQuation?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:SHOWEQuation?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:SHOWEQuation value``
              command.

        SCPI Syntax:
            ```
            - VISual:SHOWEQuation {ON|OFF|<NR1>}
            - VISual:SHOWEQuation?
            ```

        Info:
            - ``ON`` shows the Visual Trigger area combination logic equation.
            - ``OFF`` hides the Visual Trigger area combination logic equation.
            - ``<NR1>`` is an integer number. 0 hides the area combination logic equation; any other
              value displays the area combination logic equation.
        """
        return self._showequation
