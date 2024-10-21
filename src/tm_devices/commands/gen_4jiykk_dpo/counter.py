"""The counter commands module.

These commands are used in the following models:
DPO70KSX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - COUnter <REFerence|CLEAR|RESet>
    - COUnter:DURation <nr1>
    - COUnter:DURation?
    - COUnter:GAIn <nr2>
    - COUnter:GAIn?
    - COUnter:LOGAction <CLEAR>
    - COUnter:LOGNumber <nr1>
    - COUnter:LOGNumber?
    - COUnter:LOGTable <OFF|ON>
    - COUnter:LOGTable?
    - COUnter:PREscaler <OFF|ON>
    - COUnter:PREscaler?
    - COUnter:REFerence <nr3>
    - COUnter:REFerence?
    - COUnter:RESULTs:AVGmean?
    - COUnter:RESULTs:DEViation?
    - COUnter:RESULTs:MAXimum?
    - COUnter:RESULTs:MINimum?
    - COUnter:RESULTs:NUMber?
    - COUnter:RESULTs:VALue?
    - COUnter:RESULTs?
    - COUnter:SHOWLog <OFF|ON>
    - COUnter:SHOWLog?
    - COUnter:SHOWMeasurement <OFF|ON>
    - COUnter:SHOWMeasurement?
    - COUnter:STAte {ON|OFF|<NR1>}
    - COUnter:STAte?
    - COUnter:TYPe <TIME|FREQuency>
    - COUnter:TYPe?
    - COUnter:UPDate <AUTO|TIME|NUMBER>
    - COUnter:UPDate?
    - COUnter:VIEW <FREQuency|PERiod>
    - COUnter:VIEW?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class CounterView(SCPICmdWrite, SCPICmdRead):
    """The ``COUnter:VIEW`` command.

    Description:
        - Sets or queries the View of the Counter Trigger Source Frequency Application Data. When
          the ``COUnter:TYPe`` is FREQuency, the data may be viewed as Frequency (Hz) or Time
          (seconds). This command does not apply to the A-B Time Interval Application
          (``COUnter:TYPE TIME``). DPO70000SX Series only. This command is optional.

    Usage:
        - Using the ``.query()`` method will send the ``COUnter:VIEW?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter:VIEW?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``COUnter:VIEW value`` command.

    SCPI Syntax:
        ```
        - COUnter:VIEW <FREQuency|PERiod>
        - COUnter:VIEW?
        ```

    Info:
        - ``FREQuency`` displays the count in Hertz.
        - ``PERiod`` displays the count in seconds.
    """


class CounterUpdate(SCPICmdWrite, SCPICmdRead):
    """The ``COUnter:UPDate`` command.

    Description:
        - Sets or queries the parameter that controls the schedule for updating the Log Table of the
          Trigger Source Frequency or A-B Trigger Time Interval Application Data. The schedule for
          logging the data may be set to occur automatically, after a given time interval has
          elapsed, or after a given number of acquisitions have occurred. The default is AUTO.
          DPO70000SX Series only. This command is optional.

    Usage:
        - Using the ``.query()`` method will send the ``COUnter:UPDate?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter:UPDate?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``COUnter:UPDate value`` command.

    SCPI Syntax:
        ```
        - COUnter:UPDate <AUTO|TIME|NUMBER>
        - COUnter:UPDate?
        ```

    Info:
        - ``AUTO`` sets the data logging to automatic.
        - ``TIME`` sets the data logging to occur after a given time interval has elapsed.
        - ``NUMBER`` sets the data logging to occur after a given number of acquisitions have
          occurred.
    """


class CounterType(SCPICmdWrite, SCPICmdRead):
    """The ``COUnter:TYPe`` command.

    Description:
        - Sets or queries the Counter Application type as Trigger Source Frequency or A-B Trigger
          Time Interval. The Trigger Source Frequency Application is commonly referred to as
          Frequency Counting, and measures the frequency of the trigger source over a large number
          of events to obtain a very accurate result. The A-B Trigger Time Interval Application
          measures the A-Event to B-Event in an A->B Sequence Trigger, over a single A->B Trigger
          Sequence. DPO70000SX Series only. This command is optional.

    Usage:
        - Using the ``.query()`` method will send the ``COUnter:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter:TYPe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``COUnter:TYPe value`` command.

    SCPI Syntax:
        ```
        - COUnter:TYPe <TIME|FREQuency>
        - COUnter:TYPe?
        ```

    Info:
        - ``TIME`` sets the application type to frequency.
        - ``FREQuency`` sets the application type to time interval. The default value is Frequency.
    """


class CounterState(SCPICmdWrite, SCPICmdRead):
    """The ``COUnter:STAte`` command.

    Description:
        - Enables the Trigger Source Frequency or A-B Trigger Time Interval application, depending
          on the value of the ``COUnter:TYPe`` parameter. This command sets or queries the Counter
          State enumerated value (OFF/ON) used to enable/disable the display of frequency or time
          information in the graticule area or in the Results Table. The Trigger Source Frequency
          Application uses trigger hardware, rather than the acquired waveform, to measure the
          frequency of the signal on the trigger source to a very high precision. Best results are
          obtained when the External Reference is tied between the instrument and the source of the
          trigger signal. As a result of using the trigger hardware, the measurement update rate is
          very fast, 1/3 second by default. An A-Event Edge to B-Event Edge A->B Sequence must be
          used. Statistics are derived from the measured values: Minimum, Maximum, Average (mean),
          and Standard Deviation. The number of measurements made so far is also included. Note that
          long record lengths are NOT needed for this application, because the measurements are made
          from the trigger hardware, not from the acquired waveform. A Reference value may be taken
          by command or entered manually. When the Reference is non-zero, the measured value and the
          derived statistics are shown or queried as delta values from the Reference. The A-B
          Trigger Time Interval Application also uses trigger hardware to measure the time between
          the A-Event and the B-Event in an A-B Sequence trigger. The A- and B-Events may be any
          combination of trigger types: Edge, Glitch, Width, etc. A Reference value may be taken by
          command or entered manually. When the Reference value is non-zero, the measured value is
          displayed or queried as a delta from this Reference. For example, if the ``COUnter:TYPe``
          parameter is set to FREQuency, the ``COUnter:STAte ON`` command causes the display of the
          frequency of the triggered channel signal, which is assumed to be an infinitely repeating
          clock. Along with the frequency value, the minimum, maximum, average (mean), and standard
          deviation of the frequency are also displayed. Finally, a reference value is displayed.
          The reference is 0.0 by default, but may be captured as the last measured value at any
          time using the COUnter REF command. When the reference value is nonzero, the other values
          are deltas from the reference value. The displayed information is typical of products
          generally referred to by the industry as 'requency Counters. At the user's discretion, the
          ``COUnter:VIEW`` <PERiod | FREQuency> command can be used to view the information as the
          Frequency (Hz) or Period (seconds). The default view is Frequency. As a second example, if
          the ``COUnter:TYPe`` parameter is set to TIME, the ``COUnter:STAte ON`` command causes the
          display of the Time interval from the Trigger A-Event to the Trigger B-Event. These events
          can be from any trigger types in an A->B Trigger Sequence. In this case only the Time and
          the Reference value are displayed. The COUnter REF command takes the Reference value as
          before, but in this case the units relate to Time (seconds). DPO70000SX Series only. This
          command is optional.

    Usage:
        - Using the ``.query()`` method will send the ``COUnter:STAte?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter:STAte?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``COUnter:STAte value`` command.

    SCPI Syntax:
        ```
        - COUnter:STAte {ON|OFF|<NR1>}
        - COUnter:STAte?
        ```

    Info:
        - ``<NR1>`` , if 0 disables the counter function, if 1 enables the counter function.
        - ``OFF`` disables the counter function. The default value is OFF.
        - ``ON`` enables the counter function.
    """


class CounterShowmeasurement(SCPICmdWrite, SCPICmdRead):
    """The ``COUnter:SHOWMeasurement`` command.

    Description:
        - Sets or queries the parameter that controls the display of the Trigger Source Frequency or
          A-B Trigger Time Interval Application Data. The display of the data in the graticule area
          may be turned OFF or back ON as desired. A possible reason for turning it OFF is when the
          Log Table is enabled to record the data. DPO70000SX Series only. This command is optional.

    Usage:
        - Using the ``.query()`` method will send the ``COUnter:SHOWMeasurement?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter:SHOWMeasurement?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``COUnter:SHOWMeasurement value``
          command.

    SCPI Syntax:
        ```
        - COUnter:SHOWMeasurement <OFF|ON>
        - COUnter:SHOWMeasurement?
        ```

    Info:
        - ``OFF`` disables the display of the frequency or time interval data.
        - ``ON`` enables the display of the frequency or time interval data. The default is ON.
    """


class CounterShowlog(SCPICmdWrite, SCPICmdRead):
    """The ``COUnter:SHOWLog`` command.

    Description:
        - Sets or queries the parameter that controls the display of the Trigger Source Frequency or
          A-B Trigger Time Interval Application Data. The display of the data in the graticule area
          may be turned OFF or back ON as desired. A possible reason for turning it OFF is when the
          Log Table is enabled to record the data. DPO70000SX Series only. This command is optional.

    Usage:
        - Using the ``.query()`` method will send the ``COUnter:SHOWLog?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter:SHOWLog?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``COUnter:SHOWLog value`` command.

    SCPI Syntax:
        ```
        - COUnter:SHOWLog <OFF|ON>
        - COUnter:SHOWLog?
        ```

    Info:
        - ``OFF`` disables the display of the frequency or time interval data.
        - ``ON`` enables the display of the frequency or time interval data. The default is ON.
    """


class CounterResultsValue(SCPICmdRead):
    """The ``COUnter:RESULTs:VALue`` command.

    Description:
        - Queries the measured value obtained from the Trigger Source Frequency or A-B Trigger Time
          Interval Applications. The measured quantity is value.

    Usage:
        - Using the ``.query()`` method will send the ``COUnter:RESULTs:VALue?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs:VALue?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - COUnter:RESULTs:VALue?
        ```
    """


class CounterResultsNumber(SCPICmdRead):
    """The ``COUnter:RESULTs:NUMber`` command.

    Description:
        - Queries the derived value obtained from the Trigger Source Frequency or A-B Trigger Time
          Interval Applications. The value is the number of acquisitions (NUMber) taken at the time
          the command was given.

    Usage:
        - Using the ``.query()`` method will send the ``COUnter:RESULTs:NUMber?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs:NUMber?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - COUnter:RESULTs:NUMber?
        ```
    """


class CounterResultsMinimum(SCPICmdRead):
    """The ``COUnter:RESULTs:MINimum`` command.

    Description:
        - Queries the derived value obtained from the Trigger Source Frequency or A-B Trigger Time
          Interval Applications. The minimum is a statistical value accumulated over the number of
          acquisitions ('NUMber') taken at the time the command was given.

    Usage:
        - Using the ``.query()`` method will send the ``COUnter:RESULTs:MINimum?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs:MINimum?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - COUnter:RESULTs:MINimum?
        ```
    """


class CounterResultsMaximum(SCPICmdRead):
    """The ``COUnter:RESULTs:MAXimum`` command.

    Description:
        - Queries the derived value obtained from the Trigger Source Frequency or A-B Trigger Time
          Interval Applications. The maximum is a statistical value accumulated over the number of
          acquisitions (NUMber) taken at the time the command was given.

    Usage:
        - Using the ``.query()`` method will send the ``COUnter:RESULTs:MAXimum?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs:MAXimum?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - COUnter:RESULTs:MAXimum?
        ```
    """


class CounterResultsDeviation(SCPICmdRead):
    """The ``COUnter:RESULTs:DEViation`` command.

    Description:
        - Queries the derived value obtained from the Trigger Source Frequency or A-B Trigger Time
          Interval Applications. The Deviation is a statistical value accumulated over the number of
          acquisitions (NUMber) taken at the time the command was given.

    Usage:
        - Using the ``.query()`` method will send the ``COUnter:RESULTs:DEViation?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs:DEViation?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - COUnter:RESULTs:DEViation?
        ```
    """


class CounterResultsAvgmean(SCPICmdRead):
    """The ``COUnter:RESULTs:AVGmean`` command.

    Description:
        - Queries the derived value obtained from the Trigger Source Frequency or A-B Trigger Time
          Interval Applications. The AVGmean is a statistical value accumulated over the number of
          acquisitions (NUMber) taken at the time the command was given.

    Usage:
        - Using the ``.query()`` method will send the ``COUnter:RESULTs:AVGmean?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs:AVGmean?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - COUnter:RESULTs:AVGmean?
        ```
    """


class CounterResults(SCPICmdRead):
    """The ``COUnter:RESULTs`` command.

    Description:
        - Queries the measured and derived values obtained from the Trigger Source Frequency or A-B
          Trigger Time Interval Applications. The measured quantity is value. The minimum, maximum,
          AVGmean, and Deviation are statistical values accumulated over the number of acquisitions
          (NUMber) taken at the time the command is given. All results are returned with the single
          query ``COUnter:RESULTs?`` Individual results are returned by other queries

    Usage:
        - Using the ``.query()`` method will send the ``COUnter:RESULTs?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - COUnter:RESULTs?
        ```

    Properties:
        - ``.avgmean``: The ``COUnter:RESULTs:AVGmean`` command.
        - ``.deviation``: The ``COUnter:RESULTs:DEViation`` command.
        - ``.maximum``: The ``COUnter:RESULTs:MAXimum`` command.
        - ``.minimum``: The ``COUnter:RESULTs:MINimum`` command.
        - ``.number``: The ``COUnter:RESULTs:NUMber`` command.
        - ``.value``: The ``COUnter:RESULTs:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._avgmean = CounterResultsAvgmean(device, f"{self._cmd_syntax}:AVGmean")
        self._deviation = CounterResultsDeviation(device, f"{self._cmd_syntax}:DEViation")
        self._maximum = CounterResultsMaximum(device, f"{self._cmd_syntax}:MAXimum")
        self._minimum = CounterResultsMinimum(device, f"{self._cmd_syntax}:MINimum")
        self._number = CounterResultsNumber(device, f"{self._cmd_syntax}:NUMber")
        self._value = CounterResultsValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def avgmean(self) -> CounterResultsAvgmean:
        """Return the ``COUnter:RESULTs:AVGmean`` command.

        Description:
            - Queries the derived value obtained from the Trigger Source Frequency or A-B Trigger
              Time Interval Applications. The AVGmean is a statistical value accumulated over the
              number of acquisitions (NUMber) taken at the time the command was given.

        Usage:
            - Using the ``.query()`` method will send the ``COUnter:RESULTs:AVGmean?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs:AVGmean?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - COUnter:RESULTs:AVGmean?
            ```
        """
        return self._avgmean

    @property
    def deviation(self) -> CounterResultsDeviation:
        """Return the ``COUnter:RESULTs:DEViation`` command.

        Description:
            - Queries the derived value obtained from the Trigger Source Frequency or A-B Trigger
              Time Interval Applications. The Deviation is a statistical value accumulated over the
              number of acquisitions (NUMber) taken at the time the command was given.

        Usage:
            - Using the ``.query()`` method will send the ``COUnter:RESULTs:DEViation?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs:DEViation?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - COUnter:RESULTs:DEViation?
            ```
        """
        return self._deviation

    @property
    def maximum(self) -> CounterResultsMaximum:
        """Return the ``COUnter:RESULTs:MAXimum`` command.

        Description:
            - Queries the derived value obtained from the Trigger Source Frequency or A-B Trigger
              Time Interval Applications. The maximum is a statistical value accumulated over the
              number of acquisitions (NUMber) taken at the time the command was given.

        Usage:
            - Using the ``.query()`` method will send the ``COUnter:RESULTs:MAXimum?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs:MAXimum?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - COUnter:RESULTs:MAXimum?
            ```
        """
        return self._maximum

    @property
    def minimum(self) -> CounterResultsMinimum:
        """Return the ``COUnter:RESULTs:MINimum`` command.

        Description:
            - Queries the derived value obtained from the Trigger Source Frequency or A-B Trigger
              Time Interval Applications. The minimum is a statistical value accumulated over the
              number of acquisitions ('NUMber') taken at the time the command was given.

        Usage:
            - Using the ``.query()`` method will send the ``COUnter:RESULTs:MINimum?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs:MINimum?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - COUnter:RESULTs:MINimum?
            ```
        """
        return self._minimum

    @property
    def number(self) -> CounterResultsNumber:
        """Return the ``COUnter:RESULTs:NUMber`` command.

        Description:
            - Queries the derived value obtained from the Trigger Source Frequency or A-B Trigger
              Time Interval Applications. The value is the number of acquisitions (NUMber) taken at
              the time the command was given.

        Usage:
            - Using the ``.query()`` method will send the ``COUnter:RESULTs:NUMber?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs:NUMber?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - COUnter:RESULTs:NUMber?
            ```
        """
        return self._number

    @property
    def value(self) -> CounterResultsValue:
        """Return the ``COUnter:RESULTs:VALue`` command.

        Description:
            - Queries the measured value obtained from the Trigger Source Frequency or A-B Trigger
              Time Interval Applications. The measured quantity is value.

        Usage:
            - Using the ``.query()`` method will send the ``COUnter:RESULTs:VALue?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs:VALue?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - COUnter:RESULTs:VALue?
            ```
        """
        return self._value


class CounterReference(SCPICmdWrite, SCPICmdRead):
    """The ``COUnter:REFerence`` command.

    Description:
        - Sets or queries the Reference (offset) value for the Trigger Source Frequency or A-B
          Trigger Time Interval applications. When the time or frequency is measured the offset is
          subtracted from the measured value before the value is displayed, used to calculate
          statistics, or logged in the table. Considered along with ``COUNT:GAIn`` <nr3>. this
          applies the linear relationship y = mx + b, where b is the Reference (or offset) and m is
          the gain (or slope). This command may be used to zero the reference value
          (``COUnter:REFerence 0``.0), or to set it to any other value. The Reference can be taken
          automatically as the last measured value using the COUnter REF command (notice no
          semicolon here), and then queried to determine its value. DPO70000SX Series only. This
          command is optional.

    Usage:
        - Using the ``.query()`` method will send the ``COUnter:REFerence?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter:REFerence?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``COUnter:REFerence value`` command.

    SCPI Syntax:
        ```
        - COUnter:REFerence <nr3>
        - COUnter:REFerence?
        ```

    Info:
        - ``<nr3>`` is the Reference (offset) value for the Trigger Source Frequency or A-B Trigger
          Time Interval applications.
    """


class CounterPrescaler(SCPICmdWrite, SCPICmdRead):
    """The ``COUnter:PREscaler`` command.

    Description:
        - Sets or queries the parameter that enables/disables the Prescaler circuits that are needed
          when the signal frequency is greater than 4 GHz. The Default is OFF. DPO70000SX Series
          only. This command is optional.

    Usage:
        - Using the ``.query()`` method will send the ``COUnter:PREscaler?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter:PREscaler?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``COUnter:PREscaler value`` command.

    SCPI Syntax:
        ```
        - COUnter:PREscaler <OFF|ON>
        - COUnter:PREscaler?
        ```

    Info:
        - ``OFF`` disables use of the prescaler.
        - ``ON`` enables use of the prescaler.
    """


class CounterLogtable(SCPICmdWrite, SCPICmdRead):
    """The ``COUnter:LOGTable`` command.

    Description:
        - Sets or queries the parameter that enables/disables the Log Table of the Trigger Source
          Frequency or A-B Trigger Time Interval Application Data. When disabled, no log is kept.
          DPO70000SX Series only. This command is optional.

    Usage:
        - Using the ``.query()`` method will send the ``COUnter:LOGTable?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter:LOGTable?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``COUnter:LOGTable value`` command.

    SCPI Syntax:
        ```
        - COUnter:LOGTable <OFF|ON>
        - COUnter:LOGTable?
        ```

    Info:
        - ``OFF`` disables use of the log table.
        - ``ON`` enables use of the log table. The default is ON.
    """


class CounterLognumber(SCPICmdWrite, SCPICmdRead):
    """The ``COUnter:LOGNumber`` command.

    Description:
        - Sets or queries the parameter that controls the schedule for updating the Log Table of the
          Trigger Source Frequency or A-B Trigger Time Interval Application Data when the
          ``COUnter:UPDate`` is NUMBER. The number of acquisitions between log updates is set to the
          number specified in the argument of this command. DPO70000SX Series only. This command is
          optional.

    Usage:
        - Using the ``.query()`` method will send the ``COUnter:LOGNumber?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter:LOGNumber?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``COUnter:LOGNumber value`` command.

    SCPI Syntax:
        ```
        - COUnter:LOGNumber <nr1>
        - COUnter:LOGNumber?
        ```

    Info:
        - ``<nr1>`` is he number of acquisitions between log updates. The default is 100
          acquisitions.
    """


class CounterLogaction(SCPICmdWrite):
    """The ``COUnter:LOGAction`` command.

    Description:
        - This command clears all data from the Log Table of the Trigger Source Frequency or A-B
          Trigger Time Interval Application. DPO70000SX Series only. This command is optional.

    Usage:
        - Using the ``.write(value)`` method will send the ``COUnter:LOGAction value`` command.

    SCPI Syntax:
        ```
        - COUnter:LOGAction <CLEAR>
        ```

    Info:
        - ``CLEAR`` empties the log table.
    """


class CounterGain(SCPICmdWrite, SCPICmdRead):
    """The ``COUnter:GAIn`` command.

    Description:
        - Sets or queries the Gain (scale) value for the Trigger Source Frequency or A-B Trigger
          Time Interval applications. When the time or frequency is measured, it is multiplied by
          the Gain before the value is displayed, used to calculate statistics, or logged in the
          table. Considered along with ``COUNT:REFerence`` <nr3>, this applies the linear
          relationship y = mx + b, where b is the Reference (or offset) and m is the gain (or
          scale). The default gain is 1.0. The gain may never be 0.0. DPO70000SX Series only. This
          command is optional.

    Usage:
        - Using the ``.query()`` method will send the ``COUnter:GAIn?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter:GAIn?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``COUnter:GAIn value`` command.

    SCPI Syntax:
        ```
        - COUnter:GAIn <nr2>
        - COUnter:GAIn?
        ```

    Info:
        - ``<nr2>`` is the Gain (scale) value for the Trigger Source Frequency or A-B Trigger Time
          Interval applications.
    """


class CounterDuration(SCPICmdWrite, SCPICmdRead):
    """The ``COUnter:DURation`` command.

    Description:
        - Sets or queries the parameter that controls the schedule for updating the Log Table of the
          Trigger Source Frequency or A-B Trigger Time Interval Application Data when the
          ``COUnter:UPDate`` is TIME. The time interval between log updates is set to the number of
          seconds specified in the argument of this command. DPO70000SX Series only. This command is
          optional.

    Usage:
        - Using the ``.query()`` method will send the ``COUnter:DURation?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter:DURation?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``COUnter:DURation value`` command.

    SCPI Syntax:
        ```
        - COUnter:DURation <nr1>
        - COUnter:DURation?
        ```

    Info:
        - ``<nr1>`` is the time interval, in seconds, between log updates. The default is 60
          seconds.
    """


#  pylint: disable=too-many-instance-attributes
class Counter(SCPICmdWrite, SCPICmdRead):
    """The ``COUnter`` command.

    Description:
        - This command is used for three separate purposes. DPO70000SX Series only. This command is
          optional. First, the ``COUnter REFerence`` command takes the reference to be the last
          measured value when the command is received. After that, the displayed values are deltas
          from the reference value. In linear terms reference is just the offset. Second, the
          ``COUnter CLEAR`` command zeroes both the measured and derived statistical values, and
          zeroes the number of acquisitions used to accumulate the statistics. Third, the
          ``COUnter RESET`` command is only needed in the Trigger Source Frequency Application to
          recalculate the A->B Sequence Trig on Nth Event value. This is only necessary if the user
          has overridden the automatically calculated Trig on Nth Event value. The application
          automatically calculates the Trig on Nth Event value to achieve an acquisition update rate
          of about 1/3 second, to both maximize the number of digits in the measured result, and
          keep the acquisition rate lively.

    Usage:
        - Using the ``.write(value)`` method will send the ``COUnter value`` command.

    SCPI Syntax:
        ```
        - COUnter <REFerence|CLEAR|RESet>
        ```

    Info:
        - ``REFerence`` takes the reference to be the last measured value when the command is
          received. After that, the displayed values are deltas from the reference value.
        - ``CLEAR`` zeroes both the measured and derived statistical values, and zeroes the number
          of acquisitions used to accumulate the statistics.
        - ``RESet`` recalculates the A->B Sequence Trig on Nth Event value.

    Properties:
        - ``.duration``: The ``COUnter:DURation`` command.
        - ``.gain``: The ``COUnter:GAIn`` command.
        - ``.logaction``: The ``COUnter:LOGAction`` command.
        - ``.lognumber``: The ``COUnter:LOGNumber`` command.
        - ``.logtable``: The ``COUnter:LOGTable`` command.
        - ``.prescaler``: The ``COUnter:PREscaler`` command.
        - ``.reference``: The ``COUnter:REFerence`` command.
        - ``.results``: The ``COUnter:RESULTs`` command.
        - ``.showlog``: The ``COUnter:SHOWLog`` command.
        - ``.showmeasurement``: The ``COUnter:SHOWMeasurement`` command.
        - ``.state``: The ``COUnter:STAte`` command.
        - ``.type``: The ``COUnter:TYPe`` command.
        - ``.update``: The ``COUnter:UPDate`` command.
        - ``.view``: The ``COUnter:VIEW`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "COUnter") -> None:
        super().__init__(device, cmd_syntax)
        self._duration = CounterDuration(device, f"{self._cmd_syntax}:DURation")
        self._gain = CounterGain(device, f"{self._cmd_syntax}:GAIn")
        self._logaction = CounterLogaction(device, f"{self._cmd_syntax}:LOGAction")
        self._lognumber = CounterLognumber(device, f"{self._cmd_syntax}:LOGNumber")
        self._logtable = CounterLogtable(device, f"{self._cmd_syntax}:LOGTable")
        self._prescaler = CounterPrescaler(device, f"{self._cmd_syntax}:PREscaler")
        self._reference = CounterReference(device, f"{self._cmd_syntax}:REFerence")
        self._results = CounterResults(device, f"{self._cmd_syntax}:RESULTs")
        self._showlog = CounterShowlog(device, f"{self._cmd_syntax}:SHOWLog")
        self._showmeasurement = CounterShowmeasurement(
            device, f"{self._cmd_syntax}:SHOWMeasurement"
        )
        self._state = CounterState(device, f"{self._cmd_syntax}:STAte")
        self._type = CounterType(device, f"{self._cmd_syntax}:TYPe")
        self._update = CounterUpdate(device, f"{self._cmd_syntax}:UPDate")
        self._view = CounterView(device, f"{self._cmd_syntax}:VIEW")

    @property
    def duration(self) -> CounterDuration:
        """Return the ``COUnter:DURation`` command.

        Description:
            - Sets or queries the parameter that controls the schedule for updating the Log Table of
              the Trigger Source Frequency or A-B Trigger Time Interval Application Data when the
              ``COUnter:UPDate`` is TIME. The time interval between log updates is set to the number
              of seconds specified in the argument of this command. DPO70000SX Series only. This
              command is optional.

        Usage:
            - Using the ``.query()`` method will send the ``COUnter:DURation?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter:DURation?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``COUnter:DURation value`` command.

        SCPI Syntax:
            ```
            - COUnter:DURation <nr1>
            - COUnter:DURation?
            ```

        Info:
            - ``<nr1>`` is the time interval, in seconds, between log updates. The default is 60
              seconds.
        """
        return self._duration

    @property
    def gain(self) -> CounterGain:
        """Return the ``COUnter:GAIn`` command.

        Description:
            - Sets or queries the Gain (scale) value for the Trigger Source Frequency or A-B Trigger
              Time Interval applications. When the time or frequency is measured, it is multiplied
              by the Gain before the value is displayed, used to calculate statistics, or logged in
              the table. Considered along with ``COUNT:REFerence`` <nr3>, this applies the linear
              relationship y = mx + b, where b is the Reference (or offset) and m is the gain (or
              scale). The default gain is 1.0. The gain may never be 0.0. DPO70000SX Series only.
              This command is optional.

        Usage:
            - Using the ``.query()`` method will send the ``COUnter:GAIn?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter:GAIn?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``COUnter:GAIn value`` command.

        SCPI Syntax:
            ```
            - COUnter:GAIn <nr2>
            - COUnter:GAIn?
            ```

        Info:
            - ``<nr2>`` is the Gain (scale) value for the Trigger Source Frequency or A-B Trigger
              Time Interval applications.
        """
        return self._gain

    @property
    def logaction(self) -> CounterLogaction:
        """Return the ``COUnter:LOGAction`` command.

        Description:
            - This command clears all data from the Log Table of the Trigger Source Frequency or A-B
              Trigger Time Interval Application. DPO70000SX Series only. This command is optional.

        Usage:
            - Using the ``.write(value)`` method will send the ``COUnter:LOGAction value`` command.

        SCPI Syntax:
            ```
            - COUnter:LOGAction <CLEAR>
            ```

        Info:
            - ``CLEAR`` empties the log table.
        """
        return self._logaction

    @property
    def lognumber(self) -> CounterLognumber:
        """Return the ``COUnter:LOGNumber`` command.

        Description:
            - Sets or queries the parameter that controls the schedule for updating the Log Table of
              the Trigger Source Frequency or A-B Trigger Time Interval Application Data when the
              ``COUnter:UPDate`` is NUMBER. The number of acquisitions between log updates is set to
              the number specified in the argument of this command. DPO70000SX Series only. This
              command is optional.

        Usage:
            - Using the ``.query()`` method will send the ``COUnter:LOGNumber?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter:LOGNumber?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``COUnter:LOGNumber value`` command.

        SCPI Syntax:
            ```
            - COUnter:LOGNumber <nr1>
            - COUnter:LOGNumber?
            ```

        Info:
            - ``<nr1>`` is he number of acquisitions between log updates. The default is 100
              acquisitions.
        """
        return self._lognumber

    @property
    def logtable(self) -> CounterLogtable:
        """Return the ``COUnter:LOGTable`` command.

        Description:
            - Sets or queries the parameter that enables/disables the Log Table of the Trigger
              Source Frequency or A-B Trigger Time Interval Application Data. When disabled, no log
              is kept. DPO70000SX Series only. This command is optional.

        Usage:
            - Using the ``.query()`` method will send the ``COUnter:LOGTable?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter:LOGTable?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``COUnter:LOGTable value`` command.

        SCPI Syntax:
            ```
            - COUnter:LOGTable <OFF|ON>
            - COUnter:LOGTable?
            ```

        Info:
            - ``OFF`` disables use of the log table.
            - ``ON`` enables use of the log table. The default is ON.
        """
        return self._logtable

    @property
    def prescaler(self) -> CounterPrescaler:
        """Return the ``COUnter:PREscaler`` command.

        Description:
            - Sets or queries the parameter that enables/disables the Prescaler circuits that are
              needed when the signal frequency is greater than 4 GHz. The Default is OFF. DPO70000SX
              Series only. This command is optional.

        Usage:
            - Using the ``.query()`` method will send the ``COUnter:PREscaler?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter:PREscaler?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``COUnter:PREscaler value`` command.

        SCPI Syntax:
            ```
            - COUnter:PREscaler <OFF|ON>
            - COUnter:PREscaler?
            ```

        Info:
            - ``OFF`` disables use of the prescaler.
            - ``ON`` enables use of the prescaler.
        """
        return self._prescaler

    @property
    def reference(self) -> CounterReference:
        """Return the ``COUnter:REFerence`` command.

        Description:
            - Sets or queries the Reference (offset) value for the Trigger Source Frequency or A-B
              Trigger Time Interval applications. When the time or frequency is measured the offset
              is subtracted from the measured value before the value is displayed, used to calculate
              statistics, or logged in the table. Considered along with ``COUNT:GAIn`` <nr3>. this
              applies the linear relationship y = mx + b, where b is the Reference (or offset) and m
              is the gain (or slope). This command may be used to zero the reference value
              (``COUnter:REFerence 0``.0), or to set it to any other value. The Reference can be
              taken automatically as the last measured value using the COUnter REF command (notice
              no semicolon here), and then queried to determine its value. DPO70000SX Series only.
              This command is optional.

        Usage:
            - Using the ``.query()`` method will send the ``COUnter:REFerence?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter:REFerence?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``COUnter:REFerence value`` command.

        SCPI Syntax:
            ```
            - COUnter:REFerence <nr3>
            - COUnter:REFerence?
            ```

        Info:
            - ``<nr3>`` is the Reference (offset) value for the Trigger Source Frequency or A-B
              Trigger Time Interval applications.
        """
        return self._reference

    @property
    def results(self) -> CounterResults:
        """Return the ``COUnter:RESULTs`` command.

        Description:
            - Queries the measured and derived values obtained from the Trigger Source Frequency or
              A-B Trigger Time Interval Applications. The measured quantity is value. The minimum,
              maximum, AVGmean, and Deviation are statistical values accumulated over the number of
              acquisitions (NUMber) taken at the time the command is given. All results are returned
              with the single query ``COUnter:RESULTs?`` Individual results are returned by other
              queries

        Usage:
            - Using the ``.query()`` method will send the ``COUnter:RESULTs?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - COUnter:RESULTs?
            ```

        Sub-properties:
            - ``.avgmean``: The ``COUnter:RESULTs:AVGmean`` command.
            - ``.deviation``: The ``COUnter:RESULTs:DEViation`` command.
            - ``.maximum``: The ``COUnter:RESULTs:MAXimum`` command.
            - ``.minimum``: The ``COUnter:RESULTs:MINimum`` command.
            - ``.number``: The ``COUnter:RESULTs:NUMber`` command.
            - ``.value``: The ``COUnter:RESULTs:VALue`` command.
        """
        return self._results

    @property
    def showlog(self) -> CounterShowlog:
        """Return the ``COUnter:SHOWLog`` command.

        Description:
            - Sets or queries the parameter that controls the display of the Trigger Source
              Frequency or A-B Trigger Time Interval Application Data. The display of the data in
              the graticule area may be turned OFF or back ON as desired. A possible reason for
              turning it OFF is when the Log Table is enabled to record the data. DPO70000SX Series
              only. This command is optional.

        Usage:
            - Using the ``.query()`` method will send the ``COUnter:SHOWLog?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter:SHOWLog?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``COUnter:SHOWLog value`` command.

        SCPI Syntax:
            ```
            - COUnter:SHOWLog <OFF|ON>
            - COUnter:SHOWLog?
            ```

        Info:
            - ``OFF`` disables the display of the frequency or time interval data.
            - ``ON`` enables the display of the frequency or time interval data. The default is ON.
        """
        return self._showlog

    @property
    def showmeasurement(self) -> CounterShowmeasurement:
        """Return the ``COUnter:SHOWMeasurement`` command.

        Description:
            - Sets or queries the parameter that controls the display of the Trigger Source
              Frequency or A-B Trigger Time Interval Application Data. The display of the data in
              the graticule area may be turned OFF or back ON as desired. A possible reason for
              turning it OFF is when the Log Table is enabled to record the data. DPO70000SX Series
              only. This command is optional.

        Usage:
            - Using the ``.query()`` method will send the ``COUnter:SHOWMeasurement?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter:SHOWMeasurement?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``COUnter:SHOWMeasurement value``
              command.

        SCPI Syntax:
            ```
            - COUnter:SHOWMeasurement <OFF|ON>
            - COUnter:SHOWMeasurement?
            ```

        Info:
            - ``OFF`` disables the display of the frequency or time interval data.
            - ``ON`` enables the display of the frequency or time interval data. The default is ON.
        """
        return self._showmeasurement

    @property
    def state(self) -> CounterState:
        """Return the ``COUnter:STAte`` command.

        Description:
            - Enables the Trigger Source Frequency or A-B Trigger Time Interval application,
              depending on the value of the ``COUnter:TYPe`` parameter. This command sets or queries
              the Counter State enumerated value (OFF/ON) used to enable/disable the display of
              frequency or time information in the graticule area or in the Results Table. The
              Trigger Source Frequency Application uses trigger hardware, rather than the acquired
              waveform, to measure the frequency of the signal on the trigger source to a very high
              precision. Best results are obtained when the External Reference is tied between the
              instrument and the source of the trigger signal. As a result of using the trigger
              hardware, the measurement update rate is very fast, 1/3 second by default. An A-Event
              Edge to B-Event Edge A->B Sequence must be used. Statistics are derived from the
              measured values: Minimum, Maximum, Average (mean), and Standard Deviation. The number
              of measurements made so far is also included. Note that long record lengths are NOT
              needed for this application, because the measurements are made from the trigger
              hardware, not from the acquired waveform. A Reference value may be taken by command or
              entered manually. When the Reference is non-zero, the measured value and the derived
              statistics are shown or queried as delta values from the Reference. The A-B Trigger
              Time Interval Application also uses trigger hardware to measure the time between the
              A-Event and the B-Event in an A-B Sequence trigger. The A- and B-Events may be any
              combination of trigger types: Edge, Glitch, Width, etc. A Reference value may be taken
              by command or entered manually. When the Reference value is non-zero, the measured
              value is displayed or queried as a delta from this Reference. For example, if the
              ``COUnter:TYPe`` parameter is set to FREQuency, the ``COUnter:STAte ON`` command
              causes the display of the frequency of the triggered channel signal, which is assumed
              to be an infinitely repeating clock. Along with the frequency value, the minimum,
              maximum, average (mean), and standard deviation of the frequency are also displayed.
              Finally, a reference value is displayed. The reference is 0.0 by default, but may be
              captured as the last measured value at any time using the COUnter REF command. When
              the reference value is nonzero, the other values are deltas from the reference value.
              The displayed information is typical of products generally referred to by the industry
              as 'requency Counters. At the user's discretion, the ``COUnter:VIEW`` <PERiod |
              FREQuency> command can be used to view the information as the Frequency (Hz) or Period
              (seconds). The default view is Frequency. As a second example, if the ``COUnter:TYPe``
              parameter is set to TIME, the ``COUnter:STAte ON`` command causes the display of the
              Time interval from the Trigger A-Event to the Trigger B-Event. These events can be
              from any trigger types in an A->B Trigger Sequence. In this case only the Time and the
              Reference value are displayed. The COUnter REF command takes the Reference value as
              before, but in this case the units relate to Time (seconds). DPO70000SX Series only.
              This command is optional.

        Usage:
            - Using the ``.query()`` method will send the ``COUnter:STAte?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter:STAte?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``COUnter:STAte value`` command.

        SCPI Syntax:
            ```
            - COUnter:STAte {ON|OFF|<NR1>}
            - COUnter:STAte?
            ```

        Info:
            - ``<NR1>`` , if 0 disables the counter function, if 1 enables the counter function.
            - ``OFF`` disables the counter function. The default value is OFF.
            - ``ON`` enables the counter function.
        """
        return self._state

    @property
    def type(self) -> CounterType:
        """Return the ``COUnter:TYPe`` command.

        Description:
            - Sets or queries the Counter Application type as Trigger Source Frequency or A-B
              Trigger Time Interval. The Trigger Source Frequency Application is commonly referred
              to as Frequency Counting, and measures the frequency of the trigger source over a
              large number of events to obtain a very accurate result. The A-B Trigger Time Interval
              Application measures the A-Event to B-Event in an A->B Sequence Trigger, over a single
              A->B Trigger Sequence. DPO70000SX Series only. This command is optional.

        Usage:
            - Using the ``.query()`` method will send the ``COUnter:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter:TYPe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``COUnter:TYPe value`` command.

        SCPI Syntax:
            ```
            - COUnter:TYPe <TIME|FREQuency>
            - COUnter:TYPe?
            ```

        Info:
            - ``TIME`` sets the application type to frequency.
            - ``FREQuency`` sets the application type to time interval. The default value is
              Frequency.
        """
        return self._type

    @property
    def update(self) -> CounterUpdate:
        """Return the ``COUnter:UPDate`` command.

        Description:
            - Sets or queries the parameter that controls the schedule for updating the Log Table of
              the Trigger Source Frequency or A-B Trigger Time Interval Application Data. The
              schedule for logging the data may be set to occur automatically, after a given time
              interval has elapsed, or after a given number of acquisitions have occurred. The
              default is AUTO. DPO70000SX Series only. This command is optional.

        Usage:
            - Using the ``.query()`` method will send the ``COUnter:UPDate?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter:UPDate?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``COUnter:UPDate value`` command.

        SCPI Syntax:
            ```
            - COUnter:UPDate <AUTO|TIME|NUMBER>
            - COUnter:UPDate?
            ```

        Info:
            - ``AUTO`` sets the data logging to automatic.
            - ``TIME`` sets the data logging to occur after a given time interval has elapsed.
            - ``NUMBER`` sets the data logging to occur after a given number of acquisitions have
              occurred.
        """
        return self._update

    @property
    def view(self) -> CounterView:
        """Return the ``COUnter:VIEW`` command.

        Description:
            - Sets or queries the View of the Counter Trigger Source Frequency Application Data.
              When the ``COUnter:TYPe`` is FREQuency, the data may be viewed as Frequency (Hz) or
              Time (seconds). This command does not apply to the A-B Time Interval Application
              (``COUnter:TYPE TIME``). DPO70000SX Series only. This command is optional.

        Usage:
            - Using the ``.query()`` method will send the ``COUnter:VIEW?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter:VIEW?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``COUnter:VIEW value`` command.

        SCPI Syntax:
            ```
            - COUnter:VIEW <FREQuency|PERiod>
            - COUnter:VIEW?
            ```

        Info:
            - ``FREQuency`` displays the count in Hertz.
            - ``PERiod`` displays the count in seconds.
        """
        return self._view
