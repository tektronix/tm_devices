"""The histogram commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - HIStogram:BOX <NR3>, <NR3>, <NR3>, <NR3>
    - HIStogram:BOX?
    - HIStogram:BOXPcnt <NR2>, <NR2>, <NR2>, <NR2>
    - HIStogram:BOXPcnt?
    - HIStogram:COUNt RESET
    - HIStogram:DATa?
    - HIStogram:DISplay {OFF|LOG|LINEAr}
    - HIStogram:DISplay?
    - HIStogram:END?
    - HIStogram:MODe {HORizontal|VERTical|OFF}
    - HIStogram:MODe?
    - HIStogram:SOUrce {CH1|CH2|CH3|CH4|MATH|REF1|CH2|CH3|CH4}
    - HIStogram:SOUrce?
    - HIStogram:STARt?
    - HIStogram?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class HistogramStart(SCPICmdRead):
    """The ``HIStogram:STARt`` command.

    Description:
        - Returns the time (horizontal) or vertical units value (vertical) of the first bin where
          the histogram data starts. The ``HISTOGRAM:MODE`` must be either HORizontal or VERTical
          for a value to be returned. If the mode is OFF, an error event is set and nothing is
          returned. If the ``HISTOGRAM:MODE`` is HORizontal, the value returned is the time of the
          left bin. If the ``HISTOGRAM:MODE`` is VERTical the value returned is the vertical units
          value of the top bin. The returned value is an <NR3>.

    Usage:
        - Using the ``.query()`` method will send the ``HIStogram:STARt?`` query.
        - Using the ``.verify(value)`` method will send the ``HIStogram:STARt?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HIStogram:STARt?
        ```
    """


class HistogramSource(SCPICmdWrite, SCPICmdRead):
    """The ``HIStogram:SOUrce`` command.

    Description:
        - This command sets or queries which source will be compared against the histogram box when
          the histogram testing is enabled.

    Usage:
        - Using the ``.query()`` method will send the ``HIStogram:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``HIStogram:SOUrce?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HIStogram:SOUrce value`` command.

    SCPI Syntax:
        ```
        - HIStogram:SOUrce {CH1|CH2|CH3|CH4|MATH|REF1|CH2|CH3|CH4}
        - HIStogram:SOUrce?
        ```

    Info:
        - ``CH<x>`` selects the analog channel waveform to use as the source for the histogram. The
          x variable can be expressed as an integer ranging from 1 through 4. x has a minimum of 1
          and a maximum of 4.
        - ``MATH`` selects the math waveform as the source for the histogram.
        - ``REF<1-4>`` selects a reference waveform as the source for the histogram. The x variable
          can be expressed as an integer ranging from 1 through 4.
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


class HistogramEnd(SCPICmdRead):
    """The ``HIStogram:END`` command.

    Description:
        - Returns the time (horizontal) or vertical units value (vertical) of the last bin where the
          histogram data ends. The ``HISTOGRAM:MODE`` must be either HORizontal or VERTical for a
          value to be returned. If the mode is OFF, an error event is set and nothing is returned.
          If the ``HISTOGRAM:MODE`` is HORizontal, the value returned is the time of the right bin.
          If the ``HISTOGRAM:MODE`` is VERTical the value returned is the vertical units value of
          the bottom bin. The returned value is an <NR3>.

    Usage:
        - Using the ``.query()`` method will send the ``HIStogram:END?`` query.
        - Using the ``.verify(value)`` method will send the ``HIStogram:END?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HIStogram:END?
        ```
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
        - This command specifies the histogram box coordinates in terms of source waveform vertical
          and horizontal units.

    Usage:
        - Using the ``.query()`` method will send the ``HIStogram:BOX?`` query.
        - Using the ``.verify(value)`` method will send the ``HIStogram:BOX?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HIStogram:BOX value`` command.

    SCPI Syntax:
        ```
        - HIStogram:BOX <NR3>, <NR3>, <NR3>, <NR3>
        - HIStogram:BOX?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the left position of the histogram box
          in source waveform horizontal units.
        - ``<NR3>`` specifies the top position of the histogram box in source waveform vertical
          units.
        - ``<NR3>`` specifies the right position of the histogram box in source waveform horizontal
          units.
        - ``<NR3>`` specifies the bottom position of the histogram box in source waveform vertical
          units.
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
        - ``.end``: The ``HIStogram:END`` command.
        - ``.mode``: The ``HIStogram:MODe`` command.
        - ``.source``: The ``HIStogram:SOUrce`` command.
        - ``.start``: The ``HIStogram:STARt`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "HIStogram") -> None:
        super().__init__(device, cmd_syntax)
        self._box = HistogramBox(device, f"{self._cmd_syntax}:BOX")
        self._boxpcnt = HistogramBoxpcnt(device, f"{self._cmd_syntax}:BOXPcnt")
        self._count = HistogramCount(device, f"{self._cmd_syntax}:COUNt")
        self._data = HistogramData(device, f"{self._cmd_syntax}:DATa")
        self._display = HistogramDisplay(device, f"{self._cmd_syntax}:DISplay")
        self._end = HistogramEnd(device, f"{self._cmd_syntax}:END")
        self._mode = HistogramMode(device, f"{self._cmd_syntax}:MODe")
        self._source = HistogramSource(device, f"{self._cmd_syntax}:SOUrce")
        self._start = HistogramStart(device, f"{self._cmd_syntax}:STARt")

    @property
    def box(self) -> HistogramBox:
        """Return the ``HIStogram:BOX`` command.

        Description:
            - This command specifies the histogram box coordinates in terms of source waveform
              vertical and horizontal units.

        Usage:
            - Using the ``.query()`` method will send the ``HIStogram:BOX?`` query.
            - Using the ``.verify(value)`` method will send the ``HIStogram:BOX?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HIStogram:BOX value`` command.

        SCPI Syntax:
            ```
            - HIStogram:BOX <NR3>, <NR3>, <NR3>, <NR3>
            - HIStogram:BOX?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the left position of the histogram
              box in source waveform horizontal units.
            - ``<NR3>`` specifies the top position of the histogram box in source waveform vertical
              units.
            - ``<NR3>`` specifies the right position of the histogram box in source waveform
              horizontal units.
            - ``<NR3>`` specifies the bottom position of the histogram box in source waveform
              vertical units.
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
    def end(self) -> HistogramEnd:
        """Return the ``HIStogram:END`` command.

        Description:
            - Returns the time (horizontal) or vertical units value (vertical) of the last bin where
              the histogram data ends. The ``HISTOGRAM:MODE`` must be either HORizontal or VERTical
              for a value to be returned. If the mode is OFF, an error event is set and nothing is
              returned. If the ``HISTOGRAM:MODE`` is HORizontal, the value returned is the time of
              the right bin. If the ``HISTOGRAM:MODE`` is VERTical the value returned is the
              vertical units value of the bottom bin. The returned value is an <NR3>.

        Usage:
            - Using the ``.query()`` method will send the ``HIStogram:END?`` query.
            - Using the ``.verify(value)`` method will send the ``HIStogram:END?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HIStogram:END?
            ```
        """
        return self._end

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
    def source(self) -> HistogramSource:
        """Return the ``HIStogram:SOUrce`` command.

        Description:
            - This command sets or queries which source will be compared against the histogram box
              when the histogram testing is enabled.

        Usage:
            - Using the ``.query()`` method will send the ``HIStogram:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``HIStogram:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HIStogram:SOUrce value`` command.

        SCPI Syntax:
            ```
            - HIStogram:SOUrce {CH1|CH2|CH3|CH4|MATH|REF1|CH2|CH3|CH4}
            - HIStogram:SOUrce?
            ```

        Info:
            - ``CH<x>`` selects the analog channel waveform to use as the source for the histogram.
              The x variable can be expressed as an integer ranging from 1 through 4. x has a
              minimum of 1 and a maximum of 4.
            - ``MATH`` selects the math waveform as the source for the histogram.
            - ``REF<1-4>`` selects a reference waveform as the source for the histogram. The x
              variable can be expressed as an integer ranging from 1 through 4.
        """
        return self._source

    @property
    def start(self) -> HistogramStart:
        """Return the ``HIStogram:STARt`` command.

        Description:
            - Returns the time (horizontal) or vertical units value (vertical) of the first bin
              where the histogram data starts. The ``HISTOGRAM:MODE`` must be either HORizontal or
              VERTical for a value to be returned. If the mode is OFF, an error event is set and
              nothing is returned. If the ``HISTOGRAM:MODE`` is HORizontal, the value returned is
              the time of the left bin. If the ``HISTOGRAM:MODE`` is VERTical the value returned is
              the vertical units value of the top bin. The returned value is an <NR3>.

        Usage:
            - Using the ``.query()`` method will send the ``HIStogram:STARt?`` query.
            - Using the ``.verify(value)`` method will send the ``HIStogram:STARt?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HIStogram:STARt?
            ```
        """
        return self._start
