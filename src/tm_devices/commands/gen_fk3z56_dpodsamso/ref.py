"""The ref commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - REF<x>:HORizontal:POSition <NR3>
    - REF<x>:HORizontal:POSition?
    - REF<x>:LABel:NAMe <QString>
    - REF<x>:LABel:NAMe?
    - REF<x>:LABel:XPOS <NR1>
    - REF<x>:LABel:XPOS?
    - REF<x>:LABel:YPOS <NR1>
    - REF<x>:LABel:YPOS?
    - REF<x>:LABel?
    - REF<x>:THRESHold <NR3>
    - REF<x>:THRESHold?
    - REF<x>:VERTical:POSition <NR3>
    - REF<x>:VERTical:POSition?
    - REF<x>:VERTical:SCAle <NR3>
    - REF<x>:VERTical:SCAle?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, ValidatedDynamicNumberCmd

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class RefItemVerticalScale(SCPICmdWrite, SCPICmdRead):
    """The ``REF<x>:VERTical:SCAle`` command.

    Description:
        - This command specifies the vertical scale for the reference waveform specified by <x>.
          This setting controls the display only. For a signal with constant amplitude, increasing
          the scale causes the waveform to be displayed smaller. Decreasing the scale causes the
          waveform to be displayed larger.

    Usage:
        - Using the ``.query()`` method will send the ``REF<x>:VERTical:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``REF<x>:VERTical:SCAle?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REF<x>:VERTical:SCAle value`` command.

    SCPI Syntax:
        ```
        - REF<x>:VERTical:SCAle <NR3>
        - REF<x>:VERTical:SCAle?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the gain in user units-per-division.
    """


class RefItemVerticalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``REF<x>:VERTical:POSition`` command.

    Description:
        - This command specifies the vertical position of the reference waveform specified by <x>.
          Increasing the position value of a waveform causes the waveform to move up, and decreasing
          the position value causes the waveform to move down. Position adjusts only the display
          position of a waveform. The position value determines the vertical graticule coordinate at
          which signal values are displayed. For example, if the position for Reference 3 is set to
          2.0, the signal represented by that reference will be displayed at 2.0 divisions above the
          center of the screen.

    Usage:
        - Using the ``.query()`` method will send the ``REF<x>:VERTical:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``REF<x>:VERTical:POSition?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REF<x>:VERTical:POSition value``
          command.

    SCPI Syntax:
        ```
        - REF<x>:VERTical:POSition <NR3>
        - REF<x>:VERTical:POSition?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the desired position, in divisions
          from the center horizontal graticule. The range is from -5.0 to 5.0 divisions.
    """


class RefItemVertical(SCPICmdRead):
    """The ``REF<x>:VERTical`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``REF<x>:VERTical?`` query.
        - Using the ``.verify(value)`` method will send the ``REF<x>:VERTical?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``REF<x>:VERTical:POSition`` command.
        - ``.scale``: The ``REF<x>:VERTical:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = RefItemVerticalPosition(device, f"{self._cmd_syntax}:POSition")
        self._scale = RefItemVerticalScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def position(self) -> RefItemVerticalPosition:
        """Return the ``REF<x>:VERTical:POSition`` command.

        Description:
            - This command specifies the vertical position of the reference waveform specified by
              <x>. Increasing the position value of a waveform causes the waveform to move up, and
              decreasing the position value causes the waveform to move down. Position adjusts only
              the display position of a waveform. The position value determines the vertical
              graticule coordinate at which signal values are displayed. For example, if the
              position for Reference 3 is set to 2.0, the signal represented by that reference will
              be displayed at 2.0 divisions above the center of the screen.

        Usage:
            - Using the ``.query()`` method will send the ``REF<x>:VERTical:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``REF<x>:VERTical:POSition?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REF<x>:VERTical:POSition value``
              command.

        SCPI Syntax:
            ```
            - REF<x>:VERTical:POSition <NR3>
            - REF<x>:VERTical:POSition?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the desired position, in divisions
              from the center horizontal graticule. The range is from -5.0 to 5.0 divisions.
        """
        return self._position

    @property
    def scale(self) -> RefItemVerticalScale:
        """Return the ``REF<x>:VERTical:SCAle`` command.

        Description:
            - This command specifies the vertical scale for the reference waveform specified by <x>.
              This setting controls the display only. For a signal with constant amplitude,
              increasing the scale causes the waveform to be displayed smaller. Decreasing the scale
              causes the waveform to be displayed larger.

        Usage:
            - Using the ``.query()`` method will send the ``REF<x>:VERTical:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``REF<x>:VERTical:SCAle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REF<x>:VERTical:SCAle value``
              command.

        SCPI Syntax:
            ```
            - REF<x>:VERTical:SCAle <NR3>
            - REF<x>:VERTical:SCAle?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the gain in user
              units-per-division.
        """
        return self._scale


class RefItemThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``REF<x>:THRESHold`` command.

    Description:
        - This command sets or queries the comparable threshold for converting the reference signal
          to digital form for the channel specified by x. The value of x can range from 1 through 4.

    Usage:
        - Using the ``.query()`` method will send the ``REF<x>:THRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``REF<x>:THRESHold?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REF<x>:THRESHold value`` command.

    SCPI Syntax:
        ```
        - REF<x>:THRESHold <NR3>
        - REF<x>:THRESHold?
        ```

    Info:
        - ``<NR3>`` specifies the reference threshold in volts.
    """


class RefItemLabelYpos(SCPICmdWrite, SCPICmdRead):
    """The ``REF<x>:LABel:YPOS`` command.

    Description:
        - This command sets or queries the Y screen offset at which the label (attached to the
          displayed waveform of the specified reference) is displayed, relative to the center of the
          screen. The reference waveform is specified by x. The value of x can range from 1 through
          4. This command is equivalent to selecting Reference Waveforms from the File menu,
          choosing Label from the drop-down list, selecting the tab associated with the reference
          for which you want to position a label, and entering a value in the Y Position box.

    Usage:
        - Using the ``.query()`` method will send the ``REF<x>:LABel:YPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``REF<x>:LABel:YPOS?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REF<x>:LABel:YPOS value`` command.

    SCPI Syntax:
        ```
        - REF<x>:LABel:YPOS <NR1>
        - REF<x>:LABel:YPOS?
        ```

    Info:
        - ``<NR1>`` is the location (in divisions) where the waveform label for the selected
          reference is displayed, relative to the waveform handle. Arguments should be integers
          ranging from 10 to -10.
    """


class RefItemLabelXpos(SCPICmdWrite, SCPICmdRead):
    """The ``REF<x>:LABel:XPOS`` command.

    Description:
        - This command sets or queries the X screen offset at which the label (attached to the
          displayed waveform of the specified reference) is displayed, relative to the left edge of
          the screen The reference waveform is specified by x. The value of x can range from 1
          through 4. This command is equivalent to selecting Reference Waveforms from the File menu,
          choosing Label from the drop-down list, selecting the tab associated with the reference
          for which you want to position a label, and entering a value in the X Position box.

    Usage:
        - Using the ``.query()`` method will send the ``REF<x>:LABel:XPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``REF<x>:LABel:XPOS?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REF<x>:LABel:XPOS value`` command.

    SCPI Syntax:
        ```
        - REF<x>:LABel:XPOS <NR1>
        - REF<x>:LABel:XPOS?
        ```

    Info:
        - ``<NR1>`` is the location (control in divisions) where the waveform label for the selected
          reference is displayed, relative to the left edge of the screen. Arguments should be
          integers ranging from 0 through 10.
    """


class RefItemLabelName(SCPICmdWrite, SCPICmdRead):
    """The ``REF<x>:LABel:NAMe`` command.

    Description:
        - This command sets or queries the label of the designated waveform. The reference waveform
          is specified by x. The value of x can range from 1 through 4. This command is equivalent
          to selecting Reference Waveforms from the File menu, choosing Label from the drop-down
          list, selecting the tab associated with the reference for which you want to create a
          label, and entering a label in the Label box.

    Usage:
        - Using the ``.query()`` method will send the ``REF<x>:LABel:NAMe?`` query.
        - Using the ``.verify(value)`` method will send the ``REF<x>:LABel:NAMe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REF<x>:LABel:NAMe value`` command.

    SCPI Syntax:
        ```
        - REF<x>:LABel:NAMe <QString>
        - REF<x>:LABel:NAMe?
        ```

    Info:
        - ``<QString>`` is the character string that will be used for the reference waveform label
          name.
    """

    _WRAP_ARG_WITH_QUOTES = True


class RefItemLabel(SCPICmdRead):
    """The ``REF<x>:LABel`` command.

    Description:
        - This query-only command returns a branch query containing the waveform label name and the
          coordinates at which the label (attached to the displayed waveform of the specified
          reference) is displayed. The reference waveform is specified by x. The value of x can
          range from 1 through 4. This command is equivalent to selecting Reference Waveforms from
          the File menu and then choosing Label from the drop-down list.

    Usage:
        - Using the ``.query()`` method will send the ``REF<x>:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``REF<x>:LABel?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - REF<x>:LABel?
        ```

    Properties:
        - ``.name``: The ``REF<x>:LABel:NAMe`` command.
        - ``.xpos``: The ``REF<x>:LABel:XPOS`` command.
        - ``.ypos``: The ``REF<x>:LABel:YPOS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._name = RefItemLabelName(device, f"{self._cmd_syntax}:NAMe")
        self._xpos = RefItemLabelXpos(device, f"{self._cmd_syntax}:XPOS")
        self._ypos = RefItemLabelYpos(device, f"{self._cmd_syntax}:YPOS")

    @property
    def name(self) -> RefItemLabelName:
        """Return the ``REF<x>:LABel:NAMe`` command.

        Description:
            - This command sets or queries the label of the designated waveform. The reference
              waveform is specified by x. The value of x can range from 1 through 4. This command is
              equivalent to selecting Reference Waveforms from the File menu, choosing Label from
              the drop-down list, selecting the tab associated with the reference for which you want
              to create a label, and entering a label in the Label box.

        Usage:
            - Using the ``.query()`` method will send the ``REF<x>:LABel:NAMe?`` query.
            - Using the ``.verify(value)`` method will send the ``REF<x>:LABel:NAMe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REF<x>:LABel:NAMe value`` command.

        SCPI Syntax:
            ```
            - REF<x>:LABel:NAMe <QString>
            - REF<x>:LABel:NAMe?
            ```

        Info:
            - ``<QString>`` is the character string that will be used for the reference waveform
              label name.
        """
        return self._name

    @property
    def xpos(self) -> RefItemLabelXpos:
        """Return the ``REF<x>:LABel:XPOS`` command.

        Description:
            - This command sets or queries the X screen offset at which the label (attached to the
              displayed waveform of the specified reference) is displayed, relative to the left edge
              of the screen The reference waveform is specified by x. The value of x can range from
              1 through 4. This command is equivalent to selecting Reference Waveforms from the File
              menu, choosing Label from the drop-down list, selecting the tab associated with the
              reference for which you want to position a label, and entering a value in the X
              Position box.

        Usage:
            - Using the ``.query()`` method will send the ``REF<x>:LABel:XPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``REF<x>:LABel:XPOS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REF<x>:LABel:XPOS value`` command.

        SCPI Syntax:
            ```
            - REF<x>:LABel:XPOS <NR1>
            - REF<x>:LABel:XPOS?
            ```

        Info:
            - ``<NR1>`` is the location (control in divisions) where the waveform label for the
              selected reference is displayed, relative to the left edge of the screen. Arguments
              should be integers ranging from 0 through 10.
        """
        return self._xpos

    @property
    def ypos(self) -> RefItemLabelYpos:
        """Return the ``REF<x>:LABel:YPOS`` command.

        Description:
            - This command sets or queries the Y screen offset at which the label (attached to the
              displayed waveform of the specified reference) is displayed, relative to the center of
              the screen. The reference waveform is specified by x. The value of x can range from 1
              through 4. This command is equivalent to selecting Reference Waveforms from the File
              menu, choosing Label from the drop-down list, selecting the tab associated with the
              reference for which you want to position a label, and entering a value in the Y
              Position box.

        Usage:
            - Using the ``.query()`` method will send the ``REF<x>:LABel:YPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``REF<x>:LABel:YPOS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REF<x>:LABel:YPOS value`` command.

        SCPI Syntax:
            ```
            - REF<x>:LABel:YPOS <NR1>
            - REF<x>:LABel:YPOS?
            ```

        Info:
            - ``<NR1>`` is the location (in divisions) where the waveform label for the selected
              reference is displayed, relative to the waveform handle. Arguments should be integers
              ranging from 10 to -10.
        """
        return self._ypos


class RefItemHorizontalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``REF<x>:HORizontal:POSition`` command.

    Description:
        - This command sets or queries the horizontal display position of the reference waveform.
          The reference waveform is specified by x. The value of x can range from 1 through 4. This
          command is equivalent to selecting Reference Waveforms from the File menu, choosing
          Reference Setup¼ from the drop-down list, selecting a reference waveform, and then
          entering the horizontal position value using the multipurpose knob.

    Usage:
        - Using the ``.query()`` method will send the ``REF<x>:HORizontal:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``REF<x>:HORizontal:POSition?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REF<x>:HORizontal:POSition value``
          command.

    SCPI Syntax:
        ```
        - REF<x>:HORizontal:POSition <NR3>
        - REF<x>:HORizontal:POSition?
        ```

    Info:
        - ``<NR3>`` argument specifies the horizontal position of the specified reference waveform
          in percentage of the waveform that is displayed to the right of the center vertical
          graticule. The range of this argument is from 0 through 100.
    """


class RefItemHorizontal(SCPICmdRead):
    """The ``REF<x>:HORizontal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``REF<x>:HORizontal?`` query.
        - Using the ``.verify(value)`` method will send the ``REF<x>:HORizontal?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``REF<x>:HORizontal:POSition`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = RefItemHorizontalPosition(device, f"{self._cmd_syntax}:POSition")

    @property
    def position(self) -> RefItemHorizontalPosition:
        """Return the ``REF<x>:HORizontal:POSition`` command.

        Description:
            - This command sets or queries the horizontal display position of the reference
              waveform. The reference waveform is specified by x. The value of x can range from 1
              through 4. This command is equivalent to selecting Reference Waveforms from the File
              menu, choosing Reference Setup¼ from the drop-down list, selecting a reference
              waveform, and then entering the horizontal position value using the multipurpose knob.

        Usage:
            - Using the ``.query()`` method will send the ``REF<x>:HORizontal:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``REF<x>:HORizontal:POSition?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REF<x>:HORizontal:POSition value``
              command.

        SCPI Syntax:
            ```
            - REF<x>:HORizontal:POSition <NR3>
            - REF<x>:HORizontal:POSition?
            ```

        Info:
            - ``<NR3>`` argument specifies the horizontal position of the specified reference
              waveform in percentage of the waveform that is displayed to the right of the center
              vertical graticule. The range of this argument is from 0 through 100.
        """
        return self._position


class RefItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``REF<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``REF<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.horizontal``: The ``REF<x>:HORizontal`` command tree.
        - ``.label``: The ``REF<x>:LABel`` command.
        - ``.threshold``: The ``REF<x>:THRESHold`` command.
        - ``.vertical``: The ``REF<x>:VERTical`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "REF<x>") -> None:
        super().__init__(device, cmd_syntax)
        self._horizontal = RefItemHorizontal(device, f"{self._cmd_syntax}:HORizontal")
        self._label = RefItemLabel(device, f"{self._cmd_syntax}:LABel")
        self._threshold = RefItemThreshold(device, f"{self._cmd_syntax}:THRESHold")
        self._vertical = RefItemVertical(device, f"{self._cmd_syntax}:VERTical")

    @property
    def horizontal(self) -> RefItemHorizontal:
        """Return the ``REF<x>:HORizontal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``REF<x>:HORizontal?`` query.
            - Using the ``.verify(value)`` method will send the ``REF<x>:HORizontal?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``REF<x>:HORizontal:POSition`` command.
        """
        return self._horizontal

    @property
    def label(self) -> RefItemLabel:
        """Return the ``REF<x>:LABel`` command.

        Description:
            - This query-only command returns a branch query containing the waveform label name and
              the coordinates at which the label (attached to the displayed waveform of the
              specified reference) is displayed. The reference waveform is specified by x. The value
              of x can range from 1 through 4. This command is equivalent to selecting Reference
              Waveforms from the File menu and then choosing Label from the drop-down list.

        Usage:
            - Using the ``.query()`` method will send the ``REF<x>:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``REF<x>:LABel?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - REF<x>:LABel?
            ```

        Sub-properties:
            - ``.name``: The ``REF<x>:LABel:NAMe`` command.
            - ``.xpos``: The ``REF<x>:LABel:XPOS`` command.
            - ``.ypos``: The ``REF<x>:LABel:YPOS`` command.
        """
        return self._label

    @property
    def threshold(self) -> RefItemThreshold:
        """Return the ``REF<x>:THRESHold`` command.

        Description:
            - This command sets or queries the comparable threshold for converting the reference
              signal to digital form for the channel specified by x. The value of x can range from 1
              through 4.

        Usage:
            - Using the ``.query()`` method will send the ``REF<x>:THRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``REF<x>:THRESHold?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REF<x>:THRESHold value`` command.

        SCPI Syntax:
            ```
            - REF<x>:THRESHold <NR3>
            - REF<x>:THRESHold?
            ```

        Info:
            - ``<NR3>`` specifies the reference threshold in volts.
        """
        return self._threshold

    @property
    def vertical(self) -> RefItemVertical:
        """Return the ``REF<x>:VERTical`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``REF<x>:VERTical?`` query.
            - Using the ``.verify(value)`` method will send the ``REF<x>:VERTical?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``REF<x>:VERTical:POSition`` command.
            - ``.scale``: The ``REF<x>:VERTical:SCAle`` command.
        """
        return self._vertical
