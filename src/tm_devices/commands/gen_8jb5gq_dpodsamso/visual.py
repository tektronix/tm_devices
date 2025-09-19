# pylint: disable=line-too-long
"""The visual commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - VISual:AREA<x>:DISplay {ON|OFF}
    - VISual:AREA<x>:DISplay?
    - VISual:AREA<x>:FLIP {HORIZONTAL|VERTICAL}
    - VISual:AREA<x>:HEIGHT <nr3>
    - VISual:AREA<x>:HEIGHT?
    - VISual:AREA<x>:LABel <string>
    - VISual:AREA<x>:LABel?
    - VISual:AREA<x>:OPERATION<x> {IN|OUT}
    - VISual:AREA<x>:OPERATION<x>?
    - VISual:AREA<x>:ROTAtion <nr3>
    - VISual:AREA<x>:ROTAtion?
    - VISual:AREA<x>:SHAPE {HEXAgon|RECTangle|TRAPezoid|TRIAngle}
    - VISual:AREA<x>:SHAPE?
    - VISual:AREA<x>:SHOWLOGic {ON|OFF}
    - VISual:AREA<x>:SHOWLOGic?
    - VISual:AREA<x>:SOURCE<x> {WFMCH<x>}
    - VISual:AREA<x>:SOURCE<x>?
    - VISual:AREA<x>:VERTICES {<NR3>,<NR3>,<NR3>,<NR3>,<NR3>,<NR3> [,<NR3>,<NR3>,<NR3>,<NR3>[,<NR3>,<NR3>]]}
    - VISual:AREA<x>:VERTICES?
    - VISual:AREA<x>:WIDTH <nr3>
    - VISual:AREA<x>:WIDTH?
    - VISual:AREA<x>:XPOSition <nr3>
    - VISual:AREA<x>:XPOSition?
    - VISual:AREA<x>:YPOSition <nr3>
    - VISual:AREA<x>:YPOSition?
    - VISual:AREA<x>?
    - VISual:AREACOLOr {DEFAULT|INHERIT}
    - VISual:AREACOLOr?
    - VISual:ASPECTratio {ON|OFF|<NR1>}
    - VISual:ASPECTratio?
    - VISual:DELETEAREA <1-8>
    - VISual:ENAble {ON|OFF}
    - VISual:ENAble?
    - VISual:FILE:RECALL <string>
    - VISual:FILE:SAVE <string>
    - VISual?
    ```
"""  # noqa: E501

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class VisualFileSave(SCPICmdWrite):
    """The ``VISual:FILE:SAVE`` command.

    Description:
        - Saves only the Visual Trigger Parameters, to a file that you name in the <string>. The
          file is stored in the form of programmer interface commands, which are human readable.

    Usage:
        - Using the ``.write(value)`` method will send the ``VISual:FILE:SAVE value`` command.

    SCPI Syntax:
        ```
        - VISual:FILE:SAVE <string>
        ```

    Info:
        - ``<string>`` is the complete path and file name where you want to store the visual trigger
          parameters. This can be a local or network drive.
    """


class VisualFileRecall(SCPICmdWrite):
    """The ``VISual:FILE:RECALL`` command.

    Description:
        - Recalls a file of Visual Trigger Parameters, updating the database appropriately. The file
          is stored in the form of programmer interface commands, which are human readable.

    Usage:
        - Using the ``.write(value)`` method will send the ``VISual:FILE:RECALL value`` command.

    SCPI Syntax:
        ```
        - VISual:FILE:RECALL <string>
        ```
    """


class VisualFile(SCPICmdRead):
    """The ``VISual:FILE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:FILE?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:FILE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.recall``: The ``VISual:FILE:RECALL`` command.
        - ``.save``: The ``VISual:FILE:SAVE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._recall = VisualFileRecall(device, f"{self._cmd_syntax}:RECALL")
        self._save = VisualFileSave(device, f"{self._cmd_syntax}:SAVE")

    @property
    def recall(self) -> VisualFileRecall:
        """Return the ``VISual:FILE:RECALL`` command.

        Description:
            - Recalls a file of Visual Trigger Parameters, updating the database appropriately. The
              file is stored in the form of programmer interface commands, which are human readable.

        Usage:
            - Using the ``.write(value)`` method will send the ``VISual:FILE:RECALL value`` command.

        SCPI Syntax:
            ```
            - VISual:FILE:RECALL <string>
            ```
        """
        return self._recall

    @property
    def save(self) -> VisualFileSave:
        """Return the ``VISual:FILE:SAVE`` command.

        Description:
            - Saves only the Visual Trigger Parameters, to a file that you name in the <string>. The
              file is stored in the form of programmer interface commands, which are human readable.

        Usage:
            - Using the ``.write(value)`` method will send the ``VISual:FILE:SAVE value`` command.

        SCPI Syntax:
            ```
            - VISual:FILE:SAVE <string>
            ```

        Info:
            - ``<string>`` is the complete path and file name where you want to store the visual
              trigger parameters. This can be a local or network drive.
        """
        return self._save


class VisualEnable(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:ENAble`` command.

    Description:
        - Enables or disables the visual triggering. Queries the status (on or off) of the visual
          triggering. This does not refer to the option key.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:ENAble?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:ENAble?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:ENAble value`` command.

    SCPI Syntax:
        ```
        - VISual:ENAble {ON|OFF}
        - VISual:ENAble?
        ```

    Info:
        - ``ON`` enables the visual triggering feature.
        - ``OFF`` disables the visual triggering feature.
    """


class VisualDeletearea(SCPICmdWrite):
    """The ``VISual:DELETEAREA`` command.

    Description:
        - This command deletes the specified visual trigger area. The area is specified by x. The
          value of x can range from 1 to 8.

    Usage:
        - Using the ``.write(value)`` method will send the ``VISual:DELETEAREA value`` command.

    SCPI Syntax:
        ```
        - VISual:DELETEAREA <1-8>
        ```
    """


class VisualAspectratio(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:ASPECTratio`` command.

    Description:
        - This command sets or queries the aspect ratio setting of the visual trigger system.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:ASPECTratio?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:ASPECTratio?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:ASPECTratio value`` command.

    SCPI Syntax:
        ```
        - VISual:ASPECTratio {ON|OFF|<NR1>}
        - VISual:ASPECTratio?
        ```

    Info:
        - ``<NR1>`` = 0 disables the function; any other value enables it.
        - ``OFF`` disables the function.
        - ``ON`` enables keeping the aspect ratio constant.
    """


class VisualAreacolor(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:AREACOLOr`` command.

    Description:
        - This command sets or queries the colors used by visual trigger areas.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:AREACOLOr?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:AREACOLOr?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:AREACOLOr value`` command.

    SCPI Syntax:
        ```
        - VISual:AREACOLOr {DEFAULT|INHERIT}
        - VISual:AREACOLOr?
        ```

    Info:
        - ``DEFAULT`` sets visual trigger areas to use the default blue color.
        - ``INHERIT`` sets visual trigger areas to inherit the color of the channel.
    """


class VisualAreaItemYposition(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:AREA<x>:YPOSition`` command.

    Description:
        - This command sets or queries vertical position of the specified visual trigger area. The
          area is specified by x. The value of x can range from 1 to 8.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:AREA<x>:YPOSition?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:YPOSition?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:YPOSition value``
          command.

    SCPI Syntax:
        ```
        - VISual:AREA<x>:YPOSition <nr3>
        - VISual:AREA<x>:YPOSition?
        ```

    Info:
        - ``<NR3>`` specifies the vertical position of the center of the visual trigger area.
    """


class VisualAreaItemXposition(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:AREA<x>:XPOSition`` command.

    Description:
        - This command sets or queries horizontal position of specified visual trigger area. The
          area is specified by x. The value of x can range from 1 to 8.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:AREA<x>:XPOSition?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:XPOSition?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:XPOSition value``
          command.

    SCPI Syntax:
        ```
        - VISual:AREA<x>:XPOSition <nr3>
        - VISual:AREA<x>:XPOSition?
        ```

    Info:
        - ``<NR3>`` specifies the horizontal position of the center of the visual trigger area.
    """


class VisualAreaItemWidth(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:AREA<x>:WIDTH`` command.

    Description:
        - This command sets or queries the width of the specified visual trigger area. The area is
          specified by x. The value of x can range from 1 to 8.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:AREA<x>:WIDTH?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:WIDTH?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:WIDTH value`` command.

    SCPI Syntax:
        ```
        - VISual:AREA<x>:WIDTH <nr3>
        - VISual:AREA<x>:WIDTH?
        ```

    Info:
        - ``<NR3>`` specifies the width of the visual trigger area.
    """


class VisualAreaItemVertices(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:AREA<x>:VERTICES`` command.

    Description:
        - Sets or queries the polygon vertex x and y coordinate values for an area. You must set
          vertex values in pairs; you can set 3, 4, or 6 pairs (no pentagons are allowed).

    Usage:
        - Using the ``.query()`` method will send the ``VISual:AREA<x>:VERTICES?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:VERTICES?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:VERTICES value``
          command.

    SCPI Syntax:
        ```
        - VISual:AREA<x>:VERTICES {<NR3>,<NR3>,<NR3>,<NR3>,<NR3>,<NR3> [,<NR3>,<NR3>,<NR3>,<NR3>[,<NR3>,<NR3>]]}
        - VISual:AREA<x>:VERTICES?
        ```
    """  # noqa: E501


class VisualAreaItemSourceItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``VISual:AREA<x>:SOURCE<x>`` command.

    Description:
        - Selects or queries the signal source for the area <x>. The source can only be an analog
          channel. You can enter the command as ``VISUAL:AREA<x>:SOURCE`` or
          ``VISUAL:AREA<x>:SOURCE1``.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:AREA<x>:SOURCE<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:SOURCE<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:SOURCE<x> value``
          command.

    SCPI Syntax:
        ```
        - VISual:AREA<x>:SOURCE<x> {WFMCH<x>}
        - VISual:AREA<x>:SOURCE<x>?
        ```

    Info:
        - ``WFMCH1`` indicates that the analog channel 1 waveform is used as the signal source for
          the area <x>. The other three channels have the same syntax.
    """


class VisualAreaItemShowlogic(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:AREA<x>:SHOWLOGic`` command.

    Description:
        - Causes area Source and Operation indicators to be hidden or displayed on screen. Queries
          the status of this feature. All areas are turned on and off together. The <x> is reserved
          for future use.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:AREA<x>:SHOWLOGic?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:SHOWLOGic?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:SHOWLOGic value``
          command.

    SCPI Syntax:
        ```
        - VISual:AREA<x>:SHOWLOGic {ON|OFF}
        - VISual:AREA<x>:SHOWLOGic?
        ```

    Info:
        - ``ON`` shows the definition (source, operation, and area label) of each area within the
          graphical display of that area.
        - ``OFF`` removes the definitions from the display.
    """


class VisualAreaItemShape(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:AREA<x>:SHAPE`` command.

    Description:
        - Selects the initial shape of area <x>.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:AREA<x>:SHAPE?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:SHAPE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:SHAPE value`` command.

    SCPI Syntax:
        ```
        - VISual:AREA<x>:SHAPE {HEXAgon|RECTangle|TRAPezoid|TRIAngle}
        - VISual:AREA<x>:SHAPE?
        ```

    Info:
        - ``HEXAGON`` sets the initial shape of the selected area to a hexagon.
        - ``RECTANGLE`` sets the initial shape of the selected area to a rectangle.
        - ``TRAPEZOID`` sets the initial shape of the selected area to a trapezoid.
        - ``TRIANGLE`` sets the initial shape of the selected area to a triangle.
    """


class VisualAreaItemRotation(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:AREA<x>:ROTAtion`` command.

    Description:
        - This command sets or queries the rotation angle of the specified visual trigger area. The
          area is specified by x. The value of x can range from 1 to 8.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:AREA<x>:ROTAtion?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:ROTAtion?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:ROTAtion value``
          command.

    SCPI Syntax:
        ```
        - VISual:AREA<x>:ROTAtion <nr3>
        - VISual:AREA<x>:ROTAtion?
        ```

    Info:
        - ``<NR3>`` specifies the rotation angle of the specified visual trigger area.
    """


class VisualAreaItemOperationItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``VISual:AREA<x>:OPERATION<x>`` command.

    Description:
        - Sets or queries the operation of the area specified by <x>. You can enter the command as
          ``VISUAL:AREA<x>:OPERATION`` or ``VISUAL:AREA<x>:OPERATION1``.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:AREA<x>:OPERATION<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:OPERATION<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:OPERATION<x> value``
          command.

    SCPI Syntax:
        ```
        - VISual:AREA<x>:OPERATION<x> {IN|OUT}
        - VISual:AREA<x>:OPERATION<x>?
        ```

    Info:
        - ``IN`` specifies that the selected source must pass through the specified area.
        - ``OUT`` specifies that the selected source must NOT pass through the specified area.
    """


class VisualAreaItemLabel(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:AREA<x>:LABel`` command.

    Description:
        - This command sets or queries the label of the specified visual trigger area. The area is
          specified by x. The value of x can range from 1 to 8.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:AREA<x>:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:LABel?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:LABel value`` command.

    SCPI Syntax:
        ```
        - VISual:AREA<x>:LABel <string>
        - VISual:AREA<x>:LABel?
        ```

    Info:
        - ``<string>`` specifies the label for the area.
    """


class VisualAreaItemHeight(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:AREA<x>:HEIGHT`` command.

    Description:
        - This command sets or queries the height of the specified visual trigger area. The area is
          specified by x. The value of x can range from 1 to 8.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:AREA<x>:HEIGHT?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:HEIGHT?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:HEIGHT value`` command.

    SCPI Syntax:
        ```
        - VISual:AREA<x>:HEIGHT <nr3>
        - VISual:AREA<x>:HEIGHT?
        ```

    Info:
        - ``<NR3>`` specifies the height of the specified visual trigger area.
    """


class VisualAreaItemFlip(SCPICmdWrite):
    """The ``VISual:AREA<x>:FLIP`` command.

    Description:
        - This command flips the specified visual trigger area. The area is specified by x. The
          value of x can range from 1 to 8.

    Usage:
        - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:FLIP value`` command.

    SCPI Syntax:
        ```
        - VISual:AREA<x>:FLIP {HORIZONTAL|VERTICAL}
        ```

    Info:
        - ``HORIZONTAL`` specifies to flip the area in the horizontal direction.
        - ``VERTICAL`` specifies to flip the area in the vertical direction.
    """


class VisualAreaItemDisplay(SCPICmdWrite, SCPICmdRead):
    """The ``VISual:AREA<x>:DISplay`` command.

    Description:
        - Causes the areas to be hidden or displayed on the oscilloscope screen. Queries the status
          of the area display. All areas are set On or Off together. The <x> in the command is
          reserved for future use.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:AREA<x>:DISplay?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:DISplay?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:DISplay value`` command.

    SCPI Syntax:
        ```
        - VISual:AREA<x>:DISplay {ON|OFF}
        - VISual:AREA<x>:DISplay?
        ```

    Info:
        - ``ON`` causes the areas to appear on screen.
        - ``Off`` hides the areas.
    """


#  pylint: disable=too-many-instance-attributes
class VisualAreaItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``VISual:AREA<x>`` command.

    Description:
        - This query-only command returns the settings for the specified visual trigger area. The
          area is specified by x. The value of x can range from 1 through 8.

    Usage:
        - Using the ``.query()`` method will send the ``VISual:AREA<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - VISual:AREA<x>?
        ```

    Properties:
        - ``.display``: The ``VISual:AREA<x>:DISplay`` command.
        - ``.flip``: The ``VISual:AREA<x>:FLIP`` command.
        - ``.height``: The ``VISual:AREA<x>:HEIGHT`` command.
        - ``.label``: The ``VISual:AREA<x>:LABel`` command.
        - ``.operation``: The ``VISual:AREA<x>:OPERATION<x>`` command.
        - ``.rotation``: The ``VISual:AREA<x>:ROTAtion`` command.
        - ``.shape``: The ``VISual:AREA<x>:SHAPE`` command.
        - ``.showlogic``: The ``VISual:AREA<x>:SHOWLOGic`` command.
        - ``.source``: The ``VISual:AREA<x>:SOURCE<x>`` command.
        - ``.vertices``: The ``VISual:AREA<x>:VERTICES`` command.
        - ``.width``: The ``VISual:AREA<x>:WIDTH`` command.
        - ``.xposition``: The ``VISual:AREA<x>:XPOSition`` command.
        - ``.yposition``: The ``VISual:AREA<x>:YPOSition`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._display = VisualAreaItemDisplay(device, f"{self._cmd_syntax}:DISplay")
        self._flip = VisualAreaItemFlip(device, f"{self._cmd_syntax}:FLIP")
        self._height = VisualAreaItemHeight(device, f"{self._cmd_syntax}:HEIGHT")
        self._label = VisualAreaItemLabel(device, f"{self._cmd_syntax}:LABel")
        self._operation: Dict[int, VisualAreaItemOperationItem] = DefaultDictPassKeyToFactory(
            lambda x: VisualAreaItemOperationItem(device, f"{self._cmd_syntax}:OPERATION{x}")
        )
        self._rotation = VisualAreaItemRotation(device, f"{self._cmd_syntax}:ROTAtion")
        self._shape = VisualAreaItemShape(device, f"{self._cmd_syntax}:SHAPE")
        self._showlogic = VisualAreaItemShowlogic(device, f"{self._cmd_syntax}:SHOWLOGic")
        self._source: Dict[int, VisualAreaItemSourceItem] = DefaultDictPassKeyToFactory(
            lambda x: VisualAreaItemSourceItem(device, f"{self._cmd_syntax}:SOURCE{x}")
        )
        self._vertices = VisualAreaItemVertices(device, f"{self._cmd_syntax}:VERTICES")
        self._width = VisualAreaItemWidth(device, f"{self._cmd_syntax}:WIDTH")
        self._xposition = VisualAreaItemXposition(device, f"{self._cmd_syntax}:XPOSition")
        self._yposition = VisualAreaItemYposition(device, f"{self._cmd_syntax}:YPOSition")

    @property
    def display(self) -> VisualAreaItemDisplay:
        """Return the ``VISual:AREA<x>:DISplay`` command.

        Description:
            - Causes the areas to be hidden or displayed on the oscilloscope screen. Queries the
              status of the area display. All areas are set On or Off together. The <x> in the
              command is reserved for future use.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:AREA<x>:DISplay?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:DISplay?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:DISplay value``
              command.

        SCPI Syntax:
            ```
            - VISual:AREA<x>:DISplay {ON|OFF}
            - VISual:AREA<x>:DISplay?
            ```

        Info:
            - ``ON`` causes the areas to appear on screen.
            - ``Off`` hides the areas.
        """
        return self._display

    @property
    def flip(self) -> VisualAreaItemFlip:
        """Return the ``VISual:AREA<x>:FLIP`` command.

        Description:
            - This command flips the specified visual trigger area. The area is specified by x. The
              value of x can range from 1 to 8.

        Usage:
            - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:FLIP value``
              command.

        SCPI Syntax:
            ```
            - VISual:AREA<x>:FLIP {HORIZONTAL|VERTICAL}
            ```

        Info:
            - ``HORIZONTAL`` specifies to flip the area in the horizontal direction.
            - ``VERTICAL`` specifies to flip the area in the vertical direction.
        """
        return self._flip

    @property
    def height(self) -> VisualAreaItemHeight:
        """Return the ``VISual:AREA<x>:HEIGHT`` command.

        Description:
            - This command sets or queries the height of the specified visual trigger area. The area
              is specified by x. The value of x can range from 1 to 8.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:AREA<x>:HEIGHT?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:HEIGHT?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:HEIGHT value``
              command.

        SCPI Syntax:
            ```
            - VISual:AREA<x>:HEIGHT <nr3>
            - VISual:AREA<x>:HEIGHT?
            ```

        Info:
            - ``<NR3>`` specifies the height of the specified visual trigger area.
        """
        return self._height

    @property
    def label(self) -> VisualAreaItemLabel:
        """Return the ``VISual:AREA<x>:LABel`` command.

        Description:
            - This command sets or queries the label of the specified visual trigger area. The area
              is specified by x. The value of x can range from 1 to 8.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:AREA<x>:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:LABel?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:LABel value``
              command.

        SCPI Syntax:
            ```
            - VISual:AREA<x>:LABel <string>
            - VISual:AREA<x>:LABel?
            ```

        Info:
            - ``<string>`` specifies the label for the area.
        """
        return self._label

    @property
    def operation(self) -> Dict[int, VisualAreaItemOperationItem]:
        """Return the ``VISual:AREA<x>:OPERATION<x>`` command.

        Description:
            - Sets or queries the operation of the area specified by <x>. You can enter the command
              as ``VISUAL:AREA<x>:OPERATION`` or ``VISUAL:AREA<x>:OPERATION1``.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:AREA<x>:OPERATION<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:OPERATION<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:OPERATION<x> value``
              command.

        SCPI Syntax:
            ```
            - VISual:AREA<x>:OPERATION<x> {IN|OUT}
            - VISual:AREA<x>:OPERATION<x>?
            ```

        Info:
            - ``IN`` specifies that the selected source must pass through the specified area.
            - ``OUT`` specifies that the selected source must NOT pass through the specified area.
        """
        return self._operation

    @property
    def rotation(self) -> VisualAreaItemRotation:
        """Return the ``VISual:AREA<x>:ROTAtion`` command.

        Description:
            - This command sets or queries the rotation angle of the specified visual trigger area.
              The area is specified by x. The value of x can range from 1 to 8.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:AREA<x>:ROTAtion?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:ROTAtion?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:ROTAtion value``
              command.

        SCPI Syntax:
            ```
            - VISual:AREA<x>:ROTAtion <nr3>
            - VISual:AREA<x>:ROTAtion?
            ```

        Info:
            - ``<NR3>`` specifies the rotation angle of the specified visual trigger area.
        """
        return self._rotation

    @property
    def shape(self) -> VisualAreaItemShape:
        """Return the ``VISual:AREA<x>:SHAPE`` command.

        Description:
            - Selects the initial shape of area <x>.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:AREA<x>:SHAPE?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:SHAPE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:SHAPE value``
              command.

        SCPI Syntax:
            ```
            - VISual:AREA<x>:SHAPE {HEXAgon|RECTangle|TRAPezoid|TRIAngle}
            - VISual:AREA<x>:SHAPE?
            ```

        Info:
            - ``HEXAGON`` sets the initial shape of the selected area to a hexagon.
            - ``RECTANGLE`` sets the initial shape of the selected area to a rectangle.
            - ``TRAPEZOID`` sets the initial shape of the selected area to a trapezoid.
            - ``TRIANGLE`` sets the initial shape of the selected area to a triangle.
        """
        return self._shape

    @property
    def showlogic(self) -> VisualAreaItemShowlogic:
        """Return the ``VISual:AREA<x>:SHOWLOGic`` command.

        Description:
            - Causes area Source and Operation indicators to be hidden or displayed on screen.
              Queries the status of this feature. All areas are turned on and off together. The <x>
              is reserved for future use.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:AREA<x>:SHOWLOGic?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:SHOWLOGic?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:SHOWLOGic value``
              command.

        SCPI Syntax:
            ```
            - VISual:AREA<x>:SHOWLOGic {ON|OFF}
            - VISual:AREA<x>:SHOWLOGic?
            ```

        Info:
            - ``ON`` shows the definition (source, operation, and area label) of each area within
              the graphical display of that area.
            - ``OFF`` removes the definitions from the display.
        """
        return self._showlogic

    @property
    def source(self) -> Dict[int, VisualAreaItemSourceItem]:
        """Return the ``VISual:AREA<x>:SOURCE<x>`` command.

        Description:
            - Selects or queries the signal source for the area <x>. The source can only be an
              analog channel. You can enter the command as ``VISUAL:AREA<x>:SOURCE`` or
              ``VISUAL:AREA<x>:SOURCE1``.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:AREA<x>:SOURCE<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:SOURCE<x>?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:SOURCE<x> value``
              command.

        SCPI Syntax:
            ```
            - VISual:AREA<x>:SOURCE<x> {WFMCH<x>}
            - VISual:AREA<x>:SOURCE<x>?
            ```

        Info:
            - ``WFMCH1`` indicates that the analog channel 1 waveform is used as the signal source
              for the area <x>. The other three channels have the same syntax.
        """
        return self._source

    @property
    def vertices(self) -> VisualAreaItemVertices:
        """Return the ``VISual:AREA<x>:VERTICES`` command.

        Description:
            - Sets or queries the polygon vertex x and y coordinate values for an area. You must set
              vertex values in pairs; you can set 3, 4, or 6 pairs (no pentagons are allowed).

        Usage:
            - Using the ``.query()`` method will send the ``VISual:AREA<x>:VERTICES?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:VERTICES?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:VERTICES value``
              command.

        SCPI Syntax:
            ```
            - VISual:AREA<x>:VERTICES {<NR3>,<NR3>,<NR3>,<NR3>,<NR3>,<NR3> [,<NR3>,<NR3>,<NR3>,<NR3>[,<NR3>,<NR3>]]}
            - VISual:AREA<x>:VERTICES?
            ```
        """  # noqa: E501
        return self._vertices

    @property
    def width(self) -> VisualAreaItemWidth:
        """Return the ``VISual:AREA<x>:WIDTH`` command.

        Description:
            - This command sets or queries the width of the specified visual trigger area. The area
              is specified by x. The value of x can range from 1 to 8.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:AREA<x>:WIDTH?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:WIDTH?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:WIDTH value``
              command.

        SCPI Syntax:
            ```
            - VISual:AREA<x>:WIDTH <nr3>
            - VISual:AREA<x>:WIDTH?
            ```

        Info:
            - ``<NR3>`` specifies the width of the visual trigger area.
        """
        return self._width

    @property
    def xposition(self) -> VisualAreaItemXposition:
        """Return the ``VISual:AREA<x>:XPOSition`` command.

        Description:
            - This command sets or queries horizontal position of specified visual trigger area. The
              area is specified by x. The value of x can range from 1 to 8.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:AREA<x>:XPOSition?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:XPOSition?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:XPOSition value``
              command.

        SCPI Syntax:
            ```
            - VISual:AREA<x>:XPOSition <nr3>
            - VISual:AREA<x>:XPOSition?
            ```

        Info:
            - ``<NR3>`` specifies the horizontal position of the center of the visual trigger area.
        """
        return self._xposition

    @property
    def yposition(self) -> VisualAreaItemYposition:
        """Return the ``VISual:AREA<x>:YPOSition`` command.

        Description:
            - This command sets or queries vertical position of the specified visual trigger area.
              The area is specified by x. The value of x can range from 1 to 8.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:AREA<x>:YPOSition?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>:YPOSition?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:AREA<x>:YPOSition value``
              command.

        SCPI Syntax:
            ```
            - VISual:AREA<x>:YPOSition <nr3>
            - VISual:AREA<x>:YPOSition?
            ```

        Info:
            - ``<NR3>`` specifies the vertical position of the center of the visual trigger area.
        """
        return self._yposition


class Visual(SCPICmdRead):
    """The ``VISual`` command.

    Description:
        - This query-only command returns the settings for each visual trigger area.

    Usage:
        - Using the ``.query()`` method will send the ``VISual?`` query.
        - Using the ``.verify(value)`` method will send the ``VISual?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - VISual?
        ```

    Properties:
        - ``.area``: The ``VISual:AREA<x>`` command.
        - ``.areacolor``: The ``VISual:AREACOLOr`` command.
        - ``.aspectratio``: The ``VISual:ASPECTratio`` command.
        - ``.deletearea``: The ``VISual:DELETEAREA`` command.
        - ``.enable``: The ``VISual:ENAble`` command.
        - ``.file``: The ``VISual:FILE`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "VISual") -> None:
        super().__init__(device, cmd_syntax)
        self._area: Dict[int, VisualAreaItem] = DefaultDictPassKeyToFactory(
            lambda x: VisualAreaItem(device, f"{self._cmd_syntax}:AREA{x}")
        )
        self._areacolor = VisualAreacolor(device, f"{self._cmd_syntax}:AREACOLOr")
        self._aspectratio = VisualAspectratio(device, f"{self._cmd_syntax}:ASPECTratio")
        self._deletearea = VisualDeletearea(device, f"{self._cmd_syntax}:DELETEAREA")
        self._enable = VisualEnable(device, f"{self._cmd_syntax}:ENAble")
        self._file = VisualFile(device, f"{self._cmd_syntax}:FILE")

    @property
    def area(self) -> Dict[int, VisualAreaItem]:
        """Return the ``VISual:AREA<x>`` command.

        Description:
            - This query-only command returns the settings for the specified visual trigger area.
              The area is specified by x. The value of x can range from 1 through 8.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:AREA<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:AREA<x>?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - VISual:AREA<x>?
            ```

        Sub-properties:
            - ``.display``: The ``VISual:AREA<x>:DISplay`` command.
            - ``.flip``: The ``VISual:AREA<x>:FLIP`` command.
            - ``.height``: The ``VISual:AREA<x>:HEIGHT`` command.
            - ``.label``: The ``VISual:AREA<x>:LABel`` command.
            - ``.operation``: The ``VISual:AREA<x>:OPERATION<x>`` command.
            - ``.rotation``: The ``VISual:AREA<x>:ROTAtion`` command.
            - ``.shape``: The ``VISual:AREA<x>:SHAPE`` command.
            - ``.showlogic``: The ``VISual:AREA<x>:SHOWLOGic`` command.
            - ``.source``: The ``VISual:AREA<x>:SOURCE<x>`` command.
            - ``.vertices``: The ``VISual:AREA<x>:VERTICES`` command.
            - ``.width``: The ``VISual:AREA<x>:WIDTH`` command.
            - ``.xposition``: The ``VISual:AREA<x>:XPOSition`` command.
            - ``.yposition``: The ``VISual:AREA<x>:YPOSition`` command.
        """
        return self._area

    @property
    def areacolor(self) -> VisualAreacolor:
        """Return the ``VISual:AREACOLOr`` command.

        Description:
            - This command sets or queries the colors used by visual trigger areas.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:AREACOLOr?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:AREACOLOr?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:AREACOLOr value`` command.

        SCPI Syntax:
            ```
            - VISual:AREACOLOr {DEFAULT|INHERIT}
            - VISual:AREACOLOr?
            ```

        Info:
            - ``DEFAULT`` sets visual trigger areas to use the default blue color.
            - ``INHERIT`` sets visual trigger areas to inherit the color of the channel.
        """
        return self._areacolor

    @property
    def aspectratio(self) -> VisualAspectratio:
        """Return the ``VISual:ASPECTratio`` command.

        Description:
            - This command sets or queries the aspect ratio setting of the visual trigger system.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:ASPECTratio?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:ASPECTratio?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:ASPECTratio value`` command.

        SCPI Syntax:
            ```
            - VISual:ASPECTratio {ON|OFF|<NR1>}
            - VISual:ASPECTratio?
            ```

        Info:
            - ``<NR1>`` = 0 disables the function; any other value enables it.
            - ``OFF`` disables the function.
            - ``ON`` enables keeping the aspect ratio constant.
        """
        return self._aspectratio

    @property
    def deletearea(self) -> VisualDeletearea:
        """Return the ``VISual:DELETEAREA`` command.

        Description:
            - This command deletes the specified visual trigger area. The area is specified by x.
              The value of x can range from 1 to 8.

        Usage:
            - Using the ``.write(value)`` method will send the ``VISual:DELETEAREA value`` command.

        SCPI Syntax:
            ```
            - VISual:DELETEAREA <1-8>
            ```
        """
        return self._deletearea

    @property
    def enable(self) -> VisualEnable:
        """Return the ``VISual:ENAble`` command.

        Description:
            - Enables or disables the visual triggering. Queries the status (on or off) of the
              visual triggering. This does not refer to the option key.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:ENAble?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:ENAble?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VISual:ENAble value`` command.

        SCPI Syntax:
            ```
            - VISual:ENAble {ON|OFF}
            - VISual:ENAble?
            ```

        Info:
            - ``ON`` enables the visual triggering feature.
            - ``OFF`` disables the visual triggering feature.
        """
        return self._enable

    @property
    def file(self) -> VisualFile:
        """Return the ``VISual:FILE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``VISual:FILE?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual:FILE?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.recall``: The ``VISual:FILE:RECALL`` command.
            - ``.save``: The ``VISual:FILE:SAVE`` command.
        """
        return self._file
