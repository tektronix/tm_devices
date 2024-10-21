"""The ref commands module.

These commands are used in the following models:
DPO2K, DPO2KB, MSO2K, MSO2KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - REF<x>:DATE?
    - REF<x>:HORizontal:DELay:TIMe <NR3>
    - REF<x>:HORizontal:DELay:TIMe?
    - REF<x>:HORizontal:SCAle <NR3>
    - REF<x>:HORizontal:SCAle?
    - REF<x>:LABel <Qstring>
    - REF<x>:LABel?
    - REF<x>:POSition <NR3>
    - REF<x>:POSition?
    - REF<x>:SCAle <NR3>
    - REF<x>:SCAle?
    - REF<x>:TIMe?
    - REF<x>:VERTical:POSition <NR3>
    - REF<x>:VERTical:POSition?
    - REF<x>:VERTical:SCAle <NR3>
    - REF<x>:VERTical:SCAle?
    - REF<x>?
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


class RefItemTime(SCPICmdRead):
    """The ``REF<x>:TIMe`` command.

    Description:
        - Returns the time that reference waveform data was copied into the internal reference
          memory for reference waveform <x>.

    Usage:
        - Using the ``.query()`` method will send the ``REF<x>:TIMe?`` query.
        - Using the ``.verify(value)`` method will send the ``REF<x>:TIMe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - REF<x>:TIMe?
        ```
    """


class RefItemScale(SCPICmdWrite, SCPICmdRead):
    """The ``REF<x>:SCAle`` command.

    Description:
        - Sets or returns the vertical scale for the channel specified by <x>, where x is the
          reference channel number.

    Usage:
        - Using the ``.query()`` method will send the ``REF<x>:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``REF<x>:SCAle?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REF<x>:SCAle value`` command.

    SCPI Syntax:
        ```
        - REF<x>:SCAle <NR3>
        - REF<x>:SCAle?
        ```

    Info:
        - ``NR3`` is the vertical scale in volts.
    """


class RefItemPosition(SCPICmdWrite, SCPICmdRead):
    """The ``REF<x>:POSition`` command.

    Description:
        - Sets or returns the vertical position for channel <x>, where x is the reference channel
          number.

    Usage:
        - Using the ``.query()`` method will send the ``REF<x>:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``REF<x>:POSition?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REF<x>:POSition value`` command.

    SCPI Syntax:
        ```
        - REF<x>:POSition <NR3>
        - REF<x>:POSition?
        ```

    Info:
        - ``<NR3>`` is the vertical position in volts.
    """


class RefItemLabel(SCPICmdWrite, SCPICmdRead):
    """The ``REF<x>:LABel`` command.

    Description:
        - This command specifies the label for the reference waveform specified by <x>.

    Usage:
        - Using the ``.query()`` method will send the ``REF<x>:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``REF<x>:LABel?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REF<x>:LABel value`` command.

    SCPI Syntax:
        ```
        - REF<x>:LABel <Qstring>
        - REF<x>:LABel?
        ```

    Info:
        - ``<Qstring>`` is an alphanumeric string of text, enclosed in quotes, that contains the
          label text for the reference channel <x> waveform. The text string is limited to 30
          characters.
    """


class RefItemHorizontalScale(SCPICmdWrite, SCPICmdRead):
    """The ``REF<x>:HORizontal:SCAle`` command.

    Description:
        - This command specifies the horizontal scale for the reference waveform specified by <x>.

    Usage:
        - Using the ``.query()`` method will send the ``REF<x>:HORizontal:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``REF<x>:HORizontal:SCAle?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REF<x>:HORizontal:SCAle value``
          command.

    SCPI Syntax:
        ```
        - REF<x>:HORizontal:SCAle <NR3>
        - REF<x>:HORizontal:SCAle?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the horizontal scale in seconds.
    """


class RefItemHorizontalDelayTime(SCPICmdWrite, SCPICmdRead):
    """The ``REF<x>:HORizontal:DELay:TIMe`` command.

    Description:
        - This command specifies the horizontal delay time for reference waveform <x>. The delay
          time is expressed in seconds and is limited to ±5 times the reference horizontal scale.

    Usage:
        - Using the ``.query()`` method will send the ``REF<x>:HORizontal:DELay:TIMe?`` query.
        - Using the ``.verify(value)`` method will send the ``REF<x>:HORizontal:DELay:TIMe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REF<x>:HORizontal:DELay:TIMe value``
          command.

    SCPI Syntax:
        ```
        - REF<x>:HORizontal:DELay:TIMe <NR3>
        - REF<x>:HORizontal:DELay:TIMe?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the delay time, in seconds.
    """


class RefItemHorizontalDelay(SCPICmdRead):
    """The ``REF<x>:HORizontal:DELay`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``REF<x>:HORizontal:DELay?`` query.
        - Using the ``.verify(value)`` method will send the ``REF<x>:HORizontal:DELay?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.time``: The ``REF<x>:HORizontal:DELay:TIMe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._time = RefItemHorizontalDelayTime(device, f"{self._cmd_syntax}:TIMe")

    @property
    def time(self) -> RefItemHorizontalDelayTime:
        """Return the ``REF<x>:HORizontal:DELay:TIMe`` command.

        Description:
            - This command specifies the horizontal delay time for reference waveform <x>. The delay
              time is expressed in seconds and is limited to ±5 times the reference horizontal
              scale.

        Usage:
            - Using the ``.query()`` method will send the ``REF<x>:HORizontal:DELay:TIMe?`` query.
            - Using the ``.verify(value)`` method will send the ``REF<x>:HORizontal:DELay:TIMe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``REF<x>:HORizontal:DELay:TIMe value`` command.

        SCPI Syntax:
            ```
            - REF<x>:HORizontal:DELay:TIMe <NR3>
            - REF<x>:HORizontal:DELay:TIMe?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the delay time, in seconds.
        """
        return self._time


class RefItemHorizontal(SCPICmdRead):
    """The ``REF<x>:HORizontal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``REF<x>:HORizontal?`` query.
        - Using the ``.verify(value)`` method will send the ``REF<x>:HORizontal?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.delay``: The ``REF<x>:HORizontal:DELay`` command tree.
        - ``.scale``: The ``REF<x>:HORizontal:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._delay = RefItemHorizontalDelay(device, f"{self._cmd_syntax}:DELay")
        self._scale = RefItemHorizontalScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def delay(self) -> RefItemHorizontalDelay:
        """Return the ``REF<x>:HORizontal:DELay`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``REF<x>:HORizontal:DELay?`` query.
            - Using the ``.verify(value)`` method will send the ``REF<x>:HORizontal:DELay?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.time``: The ``REF<x>:HORizontal:DELay:TIMe`` command.
        """
        return self._delay

    @property
    def scale(self) -> RefItemHorizontalScale:
        """Return the ``REF<x>:HORizontal:SCAle`` command.

        Description:
            - This command specifies the horizontal scale for the reference waveform specified by
              <x>.

        Usage:
            - Using the ``.query()`` method will send the ``REF<x>:HORizontal:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``REF<x>:HORizontal:SCAle?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REF<x>:HORizontal:SCAle value``
              command.

        SCPI Syntax:
            ```
            - REF<x>:HORizontal:SCAle <NR3>
            - REF<x>:HORizontal:SCAle?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the horizontal scale in seconds.
        """
        return self._scale


class RefItemDate(SCPICmdRead):
    """The ``REF<x>:DATE`` command.

    Description:
        - Returns the date that reference waveform data for reference waveform <x> was copied into
          the internal reference memory.

    Usage:
        - Using the ``.query()`` method will send the ``REF<x>:DATE?`` query.
        - Using the ``.verify(value)`` method will send the ``REF<x>:DATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - REF<x>:DATE?
        ```
    """


class RefItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``REF<x>`` command.

    Description:
        - This query returns data for the reference waveform specified by <x>.

    Usage:
        - Using the ``.query()`` method will send the ``REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``REF<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - REF<x>?
        ```

    Properties:
        - ``.date``: The ``REF<x>:DATE`` command.
        - ``.horizontal``: The ``REF<x>:HORizontal`` command tree.
        - ``.label``: The ``REF<x>:LABel`` command.
        - ``.position``: The ``REF<x>:POSition`` command.
        - ``.scale``: The ``REF<x>:SCAle`` command.
        - ``.time``: The ``REF<x>:TIMe`` command.
        - ``.vertical``: The ``REF<x>:VERTical`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "REF<x>") -> None:
        super().__init__(device, cmd_syntax)
        self._date = RefItemDate(device, f"{self._cmd_syntax}:DATE")
        self._horizontal = RefItemHorizontal(device, f"{self._cmd_syntax}:HORizontal")
        self._label = RefItemLabel(device, f"{self._cmd_syntax}:LABel")
        self._position = RefItemPosition(device, f"{self._cmd_syntax}:POSition")
        self._scale = RefItemScale(device, f"{self._cmd_syntax}:SCAle")
        self._time = RefItemTime(device, f"{self._cmd_syntax}:TIMe")
        self._vertical = RefItemVertical(device, f"{self._cmd_syntax}:VERTical")

    @property
    def date(self) -> RefItemDate:
        """Return the ``REF<x>:DATE`` command.

        Description:
            - Returns the date that reference waveform data for reference waveform <x> was copied
              into the internal reference memory.

        Usage:
            - Using the ``.query()`` method will send the ``REF<x>:DATE?`` query.
            - Using the ``.verify(value)`` method will send the ``REF<x>:DATE?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - REF<x>:DATE?
            ```
        """
        return self._date

    @property
    def horizontal(self) -> RefItemHorizontal:
        """Return the ``REF<x>:HORizontal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``REF<x>:HORizontal?`` query.
            - Using the ``.verify(value)`` method will send the ``REF<x>:HORizontal?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.delay``: The ``REF<x>:HORizontal:DELay`` command tree.
            - ``.scale``: The ``REF<x>:HORizontal:SCAle`` command.
        """
        return self._horizontal

    @property
    def label(self) -> RefItemLabel:
        """Return the ``REF<x>:LABel`` command.

        Description:
            - This command specifies the label for the reference waveform specified by <x>.

        Usage:
            - Using the ``.query()`` method will send the ``REF<x>:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``REF<x>:LABel?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REF<x>:LABel value`` command.

        SCPI Syntax:
            ```
            - REF<x>:LABel <Qstring>
            - REF<x>:LABel?
            ```

        Info:
            - ``<Qstring>`` is an alphanumeric string of text, enclosed in quotes, that contains the
              label text for the reference channel <x> waveform. The text string is limited to 30
              characters.
        """
        return self._label

    @property
    def position(self) -> RefItemPosition:
        """Return the ``REF<x>:POSition`` command.

        Description:
            - Sets or returns the vertical position for channel <x>, where x is the reference
              channel number.

        Usage:
            - Using the ``.query()`` method will send the ``REF<x>:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``REF<x>:POSition?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REF<x>:POSition value`` command.

        SCPI Syntax:
            ```
            - REF<x>:POSition <NR3>
            - REF<x>:POSition?
            ```

        Info:
            - ``<NR3>`` is the vertical position in volts.
        """
        return self._position

    @property
    def scale(self) -> RefItemScale:
        """Return the ``REF<x>:SCAle`` command.

        Description:
            - Sets or returns the vertical scale for the channel specified by <x>, where x is the
              reference channel number.

        Usage:
            - Using the ``.query()`` method will send the ``REF<x>:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``REF<x>:SCAle?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REF<x>:SCAle value`` command.

        SCPI Syntax:
            ```
            - REF<x>:SCAle <NR3>
            - REF<x>:SCAle?
            ```

        Info:
            - ``NR3`` is the vertical scale in volts.
        """
        return self._scale

    @property
    def time(self) -> RefItemTime:
        """Return the ``REF<x>:TIMe`` command.

        Description:
            - Returns the time that reference waveform data was copied into the internal reference
              memory for reference waveform <x>.

        Usage:
            - Using the ``.query()`` method will send the ``REF<x>:TIMe?`` query.
            - Using the ``.verify(value)`` method will send the ``REF<x>:TIMe?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - REF<x>:TIMe?
            ```
        """
        return self._time

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
