"""The histogram commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - HIStogram:BOX <NR3>,<NR3>,<NR3>,<NR3>
    - HIStogram:BOX?
    - HIStogram:BOXPcnt <NR2>, <NR2>, <NR2>, <NR2>
    - HIStogram:BOXPcnt?
    - HIStogram:COUNt RESET
    - HIStogram:DATa?
    - HIStogram:DISplay {OFF|LOG|LINEAr}
    - HIStogram:DISplay?
    - HIStogram:FUNCtion {HORizontal|VERTical}
    - HIStogram:FUNCtion?
    - HIStogram:MODe {HORizontal|VERTical|OFF}
    - HIStogram:MODe?
    - HIStogram:SIZe <NR3>
    - HIStogram:SIZe?
    - HIStogram:SOUrce {CH<x>|MATH<x>|REF<x>}
    - HIStogram:SOUrce?
    - HIStogram:STATE {ON|OFF|<NR1>}
    - HIStogram:STATE?
    - HIStogram?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class HistogramState(SCPICmdWrite, SCPICmdRead):
    """The ``HIStogram:STATE`` command.

    Description:
        - This command sets or queries whether the histogram calculations are enabled. This is
          equivalent to selecting Waveform Histograms from the Measure menu.

    Usage:
        - Using the ``.query()`` method will send the ``HIStogram:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``HIStogram:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HIStogram:STATE value`` command.

    SCPI Syntax:
        ```
        - HIStogram:STATE {ON|OFF|<NR1>}
        - HIStogram:STATE?
        ```

    Info:
        - ``<NR1>`` = 0 disables histogram calculations; any other value enables histogram
          calculations.
        - ``<ON>`` enables histogram calculations.
        - ``<OFF>`` disables the histogram calculations.
    """


class HistogramSource(SCPICmdWrite, SCPICmdRead):
    """The ``HIStogram:SOUrce`` command.

    Description:
        - This command sets or queries which source will be compared against the histogram box when
          the histogram testing is enabled. This is equivalent to selecting Waveform Histograms from
          the Measure menu and then choosing the desired waveform source. The waveform need not be
          displayed for histograms to run. You might want the channel displays disabled so you can
          see a full-screen histogram and not have waveform data confuse the display.

    Usage:
        - Using the ``.query()`` method will send the ``HIStogram:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``HIStogram:SOUrce?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HIStogram:SOUrce value`` command.

    SCPI Syntax:
        ```
        - HIStogram:SOUrce {CH<x>|MATH<x>|REF<x>}
        - HIStogram:SOUrce?
        ```

    Info:
        - ``CH<x>`` selects a channel waveform as the source for the histogram. The x variable can
          be expressed as an integer ranging from 1 through 4.
        - ``MATH<x>`` selects a math waveform as the source for the histogram. The x variable can be
          expressed as an integer ranging from 1 through 4.
        - ``REF<x>`` selects a reference waveform as the source for the histogram. The x variable
          can be expressed as an integer ranging from 1 through 4.
    """


class HistogramSize(SCPICmdWrite, SCPICmdRead):
    """The ``HIStogram:SIZe`` command.

    Description:
        - This command sets or queries the width or height of the histogram on the screen. This is
          equivalent to selecting Waveform Histograms from the Measure menu and then entering a
          value in the Histogram Size box.

    Usage:
        - Using the ``.query()`` method will send the ``HIStogram:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the ``HIStogram:SIZe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HIStogram:SIZe value`` command.

    SCPI Syntax:
        ```
        - HIStogram:SIZe <NR3>
        - HIStogram:SIZe?
        ```

    Info:
        - ``<NR3>`` specifies the histogram size. The value can vary from 0.1 to 8.0 divisions in
          HORizontal mode and from 0.1 to 10.0 divisions in VERTical mode. Resolution is to the
          nearest pixel.
    """


class HistogramMode(SCPICmdWrite, SCPICmdRead):
    """The ``HIStogram:MODe`` command.

    Description:
        - This command selects the type of histogram to create or disables the histogram display.
          The query form either returns the current histogram type or that the histogram display is
          disabled.

    Usage:
        - Using the ``.query()`` method will send the ``HIStogram:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``HIStogram:MODe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HIStogram:MODe value`` command.

    SCPI Syntax:
        ```
        - HIStogram:MODe {HORizontal|VERTical|OFF}
        - HIStogram:MODe?
        ```

    Info:
        - ``HORizontal`` enables a horizontally positioned histogram that shows time distribution.
        - ``VERTical`` enables a vertically positioned histogram that shows a voltage distribution,
          or another distribution such as amperes.
        - ``OFF`` disables the collection of the histogram measurement.
    """


class HistogramFunction(SCPICmdWrite, SCPICmdRead):
    """The ``HIStogram:FUNCtion`` command.

    Description:
        - This command either selects the type of histogram to create or returns the current
          histogram type. This command is equivalent to selecting Waveform Histogram from the
          Measure menu and then choosing either Horizontal or Vertical from the Histogram Mode group
          box.

    Usage:
        - Using the ``.query()`` method will send the ``HIStogram:FUNCtion?`` query.
        - Using the ``.verify(value)`` method will send the ``HIStogram:FUNCtion?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HIStogram:FUNCtion value`` command.

    SCPI Syntax:
        ```
        - HIStogram:FUNCtion {HORizontal|VERTical}
        - HIStogram:FUNCtion?
        ```

    Info:
        - ``HORizontal`` displays a horizontally positioned histogram that shows time distribution.
        - ``VERTical`` displays a vertically positioned histogram that shows a voltage distribution
          (or another distribution such as amperes).
    """


class HistogramDisplay(SCPICmdWrite, SCPICmdRead):
    """The ``HIStogram:DISplay`` command.

    Description:
        - This command sets the scaling of the histogram data display to be the count of each
          histogram bin or the log of that count. The default scaling is linear.

    Usage:
        - Using the ``.query()`` method will send the ``HIStogram:DISplay?`` query.
        - Using the ``.verify(value)`` method will send the ``HIStogram:DISplay?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HIStogram:DISplay value`` command.

    SCPI Syntax:
        ```
        - HIStogram:DISplay {OFF|LOG|LINEAr}
        - HIStogram:DISplay?
        ```

    Info:
        - ``<LOG>`` sets the histogram display to logarithmic scaling.
        - ``<LINEAr>`` sets the histogram display to linear scaling. This is the default setting.
    """


class HistogramData(SCPICmdRead):
    """The ``HIStogram:DATa`` command.

    Description:
        - This query returns the histogram data when ``HIStogram:MODe`` is HORizontal or VERTical.
          If the mode is OFF, then no data is returned and an error event is set. The data values
          returned for this query represent the number of times the histogram source waveform
          samples were coincident with a particular histogram bin. For vertical histograms, this
          query returns 256 values, representing the number of times the histogram source waveform
          samples were coincident with each of the 256 digitizing levels. Of these 256 values, the
          first 2 and last 3 are always 0, as they represent digitizing levels that fall above and
          beneath the waveform graticule, respectively. For horizontal histograms, this query
          returns 1000 values, representing the number of times the histogram source waveform
          samples were coincident with each horizontal pixel column. The time of occurrence for each
          of the horizontal bins can be derived using the ``HISTOGRAM:START`` and ``HISTOGRAM:END``
          queries.

    Usage:
        - Using the ``.query()`` method will send the ``HIStogram:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``HIStogram:DATa?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HIStogram:DATa?
        ```
    """


class HistogramCount(SCPICmdWrite):
    """The ``HIStogram:COUNt`` command.

    Description:
        - This command (no query form) clears the count and statistics for the histogram and the
          histogram source data. If the histogram is on, then counting restarts.

    Usage:
        - Using the ``.write(value)`` method will send the ``HIStogram:COUNt value`` command.

    SCPI Syntax:
        ```
        - HIStogram:COUNt RESET
        ```

    Info:
        - ``RESET``
    """


class HistogramBoxpcnt(SCPICmdWrite, SCPICmdRead):
    """The ``HIStogram:BOXPcnt`` command.

    Description:
        - This command specifies the histogram box coordinates in terms of percentages of the full
          screen extents of the source waveform. The arguments refer to the left (percent of the
          horizontal screen extent), top (percent of the vertical screen extent), right (percent of
          the horizontal screen extent), bottom (percent of the vertical screen extent). The valid
          range for these values is 0.0 to 100.0.

    Usage:
        - Using the ``.query()`` method will send the ``HIStogram:BOXPcnt?`` query.
        - Using the ``.verify(value)`` method will send the ``HIStogram:BOXPcnt?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HIStogram:BOXPcnt value`` command.

    SCPI Syntax:
        ```
        - HIStogram:BOXPcnt <NR2>, <NR2>, <NR2>, <NR2>
        - HIStogram:BOXPcnt?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the left position of the histogram box
          in percentage coordinates. The default value is 20%.
        - ``<NR3>`` specifies the top position of the histogram box in percentage coordinates. The
          default value is 80%.
        - ``<NR3>`` specifies the right position of the histogram box in percentage coordinates. The
          default value is 80%.
        - ``<NR3>`` specifies the bottom position of the histogram box in percentage coordinates.
          The default value is 20%.
    """


class HistogramBox(SCPICmdWrite, SCPICmdRead):
    """The ``HIStogram:BOX`` command.

    Description:
        - This command defines or returns the left, top, right, and bottom boundaries of the
          histogram box, in source waveform coordinates. This command is equivalent to selecting
          Waveform Histograms from the Measure menu and then setting Limits for Left, Right, Top,
          and Bottom in the appropriate boxes. The command is similar to the ``HISTOGRAM:BOXPCNT``
          command except that command uses percentage coordinates to define the boundaries of the
          histogram box.

    Usage:
        - Using the ``.query()`` method will send the ``HIStogram:BOX?`` query.
        - Using the ``.verify(value)`` method will send the ``HIStogram:BOX?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HIStogram:BOX value`` command.

    SCPI Syntax:
        ```
        - HIStogram:BOX <NR3>,<NR3>,<NR3>,<NR3>
        - HIStogram:BOX?
        ```

    Info:
        - ``<NR3>`` specifies the left position of the histogram box in source waveform coordinates.
        - ``<NR3>`` specifies the top position of the histogram box in source waveform coordinates.
        - ``<NR3>`` specifies the right position of the histogram box in source waveform
          coordinates.
        - ``<NR3>`` specifies the bottom position of the histogram box in source waveform
          coordinates.
    """


#  pylint: disable=too-many-instance-attributes
class Histogram(SCPICmdRead):
    """The ``HIStogram`` command.

    Description:
        - This query-only query returns all histogram parameters; it queries the state of all
          histogram parameters that the user can set. This command is equivalent to selecting
          Waveform Histograms from the Measure menu.

    Usage:
        - Using the ``.query()`` method will send the ``HIStogram?`` query.
        - Using the ``.verify(value)`` method will send the ``HIStogram?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HIStogram?
        ```

    Properties:
        - ``.box``: The ``HIStogram:BOX`` command.
        - ``.boxpcnt``: The ``HIStogram:BOXPcnt`` command.
        - ``.count``: The ``HIStogram:COUNt`` command.
        - ``.data``: The ``HIStogram:DATa`` command.
        - ``.display``: The ``HIStogram:DISplay`` command.
        - ``.function``: The ``HIStogram:FUNCtion`` command.
        - ``.mode``: The ``HIStogram:MODe`` command.
        - ``.size``: The ``HIStogram:SIZe`` command.
        - ``.source``: The ``HIStogram:SOUrce`` command.
        - ``.state``: The ``HIStogram:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "HIStogram") -> None:
        super().__init__(device, cmd_syntax)
        self._box = HistogramBox(device, f"{self._cmd_syntax}:BOX")
        self._boxpcnt = HistogramBoxpcnt(device, f"{self._cmd_syntax}:BOXPcnt")
        self._count = HistogramCount(device, f"{self._cmd_syntax}:COUNt")
        self._data = HistogramData(device, f"{self._cmd_syntax}:DATa")
        self._display = HistogramDisplay(device, f"{self._cmd_syntax}:DISplay")
        self._function = HistogramFunction(device, f"{self._cmd_syntax}:FUNCtion")
        self._mode = HistogramMode(device, f"{self._cmd_syntax}:MODe")
        self._size = HistogramSize(device, f"{self._cmd_syntax}:SIZe")
        self._source = HistogramSource(device, f"{self._cmd_syntax}:SOUrce")
        self._state = HistogramState(device, f"{self._cmd_syntax}:STATE")

    @property
    def box(self) -> HistogramBox:
        """Return the ``HIStogram:BOX`` command.

        Description:
            - This command defines or returns the left, top, right, and bottom boundaries of the
              histogram box, in source waveform coordinates. This command is equivalent to selecting
              Waveform Histograms from the Measure menu and then setting Limits for Left, Right,
              Top, and Bottom in the appropriate boxes. The command is similar to the
              ``HISTOGRAM:BOXPCNT`` command except that command uses percentage coordinates to
              define the boundaries of the histogram box.

        Usage:
            - Using the ``.query()`` method will send the ``HIStogram:BOX?`` query.
            - Using the ``.verify(value)`` method will send the ``HIStogram:BOX?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HIStogram:BOX value`` command.

        SCPI Syntax:
            ```
            - HIStogram:BOX <NR3>,<NR3>,<NR3>,<NR3>
            - HIStogram:BOX?
            ```

        Info:
            - ``<NR3>`` specifies the left position of the histogram box in source waveform
              coordinates.
            - ``<NR3>`` specifies the top position of the histogram box in source waveform
              coordinates.
            - ``<NR3>`` specifies the right position of the histogram box in source waveform
              coordinates.
            - ``<NR3>`` specifies the bottom position of the histogram box in source waveform
              coordinates.
        """
        return self._box

    @property
    def boxpcnt(self) -> HistogramBoxpcnt:
        """Return the ``HIStogram:BOXPcnt`` command.

        Description:
            - This command specifies the histogram box coordinates in terms of percentages of the
              full screen extents of the source waveform. The arguments refer to the left (percent
              of the horizontal screen extent), top (percent of the vertical screen extent), right
              (percent of the horizontal screen extent), bottom (percent of the vertical screen
              extent). The valid range for these values is 0.0 to 100.0.

        Usage:
            - Using the ``.query()`` method will send the ``HIStogram:BOXPcnt?`` query.
            - Using the ``.verify(value)`` method will send the ``HIStogram:BOXPcnt?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HIStogram:BOXPcnt value`` command.

        SCPI Syntax:
            ```
            - HIStogram:BOXPcnt <NR2>, <NR2>, <NR2>, <NR2>
            - HIStogram:BOXPcnt?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the left position of the histogram
              box in percentage coordinates. The default value is 20%.
            - ``<NR3>`` specifies the top position of the histogram box in percentage coordinates.
              The default value is 80%.
            - ``<NR3>`` specifies the right position of the histogram box in percentage coordinates.
              The default value is 80%.
            - ``<NR3>`` specifies the bottom position of the histogram box in percentage
              coordinates. The default value is 20%.
        """
        return self._boxpcnt

    @property
    def count(self) -> HistogramCount:
        """Return the ``HIStogram:COUNt`` command.

        Description:
            - This command (no query form) clears the count and statistics for the histogram and the
              histogram source data. If the histogram is on, then counting restarts.

        Usage:
            - Using the ``.write(value)`` method will send the ``HIStogram:COUNt value`` command.

        SCPI Syntax:
            ```
            - HIStogram:COUNt RESET
            ```

        Info:
            - ``RESET``
        """
        return self._count

    @property
    def data(self) -> HistogramData:
        """Return the ``HIStogram:DATa`` command.

        Description:
            - This query returns the histogram data when ``HIStogram:MODe`` is HORizontal or
              VERTical. If the mode is OFF, then no data is returned and an error event is set. The
              data values returned for this query represent the number of times the histogram source
              waveform samples were coincident with a particular histogram bin. For vertical
              histograms, this query returns 256 values, representing the number of times the
              histogram source waveform samples were coincident with each of the 256 digitizing
              levels. Of these 256 values, the first 2 and last 3 are always 0, as they represent
              digitizing levels that fall above and beneath the waveform graticule, respectively.
              For horizontal histograms, this query returns 1000 values, representing the number of
              times the histogram source waveform samples were coincident with each horizontal pixel
              column. The time of occurrence for each of the horizontal bins can be derived using
              the ``HISTOGRAM:START`` and ``HISTOGRAM:END`` queries.

        Usage:
            - Using the ``.query()`` method will send the ``HIStogram:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``HIStogram:DATa?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HIStogram:DATa?
            ```
        """
        return self._data

    @property
    def display(self) -> HistogramDisplay:
        """Return the ``HIStogram:DISplay`` command.

        Description:
            - This command sets the scaling of the histogram data display to be the count of each
              histogram bin or the log of that count. The default scaling is linear.

        Usage:
            - Using the ``.query()`` method will send the ``HIStogram:DISplay?`` query.
            - Using the ``.verify(value)`` method will send the ``HIStogram:DISplay?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HIStogram:DISplay value`` command.

        SCPI Syntax:
            ```
            - HIStogram:DISplay {OFF|LOG|LINEAr}
            - HIStogram:DISplay?
            ```

        Info:
            - ``<LOG>`` sets the histogram display to logarithmic scaling.
            - ``<LINEAr>`` sets the histogram display to linear scaling. This is the default
              setting.
        """
        return self._display

    @property
    def function(self) -> HistogramFunction:
        """Return the ``HIStogram:FUNCtion`` command.

        Description:
            - This command either selects the type of histogram to create or returns the current
              histogram type. This command is equivalent to selecting Waveform Histogram from the
              Measure menu and then choosing either Horizontal or Vertical from the Histogram Mode
              group box.

        Usage:
            - Using the ``.query()`` method will send the ``HIStogram:FUNCtion?`` query.
            - Using the ``.verify(value)`` method will send the ``HIStogram:FUNCtion?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HIStogram:FUNCtion value`` command.

        SCPI Syntax:
            ```
            - HIStogram:FUNCtion {HORizontal|VERTical}
            - HIStogram:FUNCtion?
            ```

        Info:
            - ``HORizontal`` displays a horizontally positioned histogram that shows time
              distribution.
            - ``VERTical`` displays a vertically positioned histogram that shows a voltage
              distribution (or another distribution such as amperes).
        """
        return self._function

    @property
    def mode(self) -> HistogramMode:
        """Return the ``HIStogram:MODe`` command.

        Description:
            - This command selects the type of histogram to create or disables the histogram
              display. The query form either returns the current histogram type or that the
              histogram display is disabled.

        Usage:
            - Using the ``.query()`` method will send the ``HIStogram:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``HIStogram:MODe?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HIStogram:MODe value`` command.

        SCPI Syntax:
            ```
            - HIStogram:MODe {HORizontal|VERTical|OFF}
            - HIStogram:MODe?
            ```

        Info:
            - ``HORizontal`` enables a horizontally positioned histogram that shows time
              distribution.
            - ``VERTical`` enables a vertically positioned histogram that shows a voltage
              distribution, or another distribution such as amperes.
            - ``OFF`` disables the collection of the histogram measurement.
        """
        return self._mode

    @property
    def size(self) -> HistogramSize:
        """Return the ``HIStogram:SIZe`` command.

        Description:
            - This command sets or queries the width or height of the histogram on the screen. This
              is equivalent to selecting Waveform Histograms from the Measure menu and then entering
              a value in the Histogram Size box.

        Usage:
            - Using the ``.query()`` method will send the ``HIStogram:SIZe?`` query.
            - Using the ``.verify(value)`` method will send the ``HIStogram:SIZe?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HIStogram:SIZe value`` command.

        SCPI Syntax:
            ```
            - HIStogram:SIZe <NR3>
            - HIStogram:SIZe?
            ```

        Info:
            - ``<NR3>`` specifies the histogram size. The value can vary from 0.1 to 8.0 divisions
              in HORizontal mode and from 0.1 to 10.0 divisions in VERTical mode. Resolution is to
              the nearest pixel.
        """
        return self._size

    @property
    def source(self) -> HistogramSource:
        """Return the ``HIStogram:SOUrce`` command.

        Description:
            - This command sets or queries which source will be compared against the histogram box
              when the histogram testing is enabled. This is equivalent to selecting Waveform
              Histograms from the Measure menu and then choosing the desired waveform source. The
              waveform need not be displayed for histograms to run. You might want the channel
              displays disabled so you can see a full-screen histogram and not have waveform data
              confuse the display.

        Usage:
            - Using the ``.query()`` method will send the ``HIStogram:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``HIStogram:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HIStogram:SOUrce value`` command.

        SCPI Syntax:
            ```
            - HIStogram:SOUrce {CH<x>|MATH<x>|REF<x>}
            - HIStogram:SOUrce?
            ```

        Info:
            - ``CH<x>`` selects a channel waveform as the source for the histogram. The x variable
              can be expressed as an integer ranging from 1 through 4.
            - ``MATH<x>`` selects a math waveform as the source for the histogram. The x variable
              can be expressed as an integer ranging from 1 through 4.
            - ``REF<x>`` selects a reference waveform as the source for the histogram. The x
              variable can be expressed as an integer ranging from 1 through 4.
        """
        return self._source

    @property
    def state(self) -> HistogramState:
        """Return the ``HIStogram:STATE`` command.

        Description:
            - This command sets or queries whether the histogram calculations are enabled. This is
              equivalent to selecting Waveform Histograms from the Measure menu.

        Usage:
            - Using the ``.query()`` method will send the ``HIStogram:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``HIStogram:STATE?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HIStogram:STATE value`` command.

        SCPI Syntax:
            ```
            - HIStogram:STATE {ON|OFF|<NR1>}
            - HIStogram:STATE?
            ```

        Info:
            - ``<NR1>`` = 0 disables histogram calculations; any other value enables histogram
              calculations.
            - ``<ON>`` enables histogram calculations.
            - ``<OFF>`` disables the histogram calculations.
        """
        return self._state
