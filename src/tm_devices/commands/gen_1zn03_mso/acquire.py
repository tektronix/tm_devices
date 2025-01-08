"""The acquire commands module.

These commands are used in the following models:
MSO2

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - ACQuire:FASTAcq:PALEtte {NORMal|TEMPerature|SPECtral|INVErted}
    - ACQuire:FASTAcq:PALEtte?
    - ACQuire:FASTAcq:STATE {ON|OFF|<NR1>}
    - ACQuire:FASTAcq:STATE?
    - ACQuire:MAXSamplerate?
    - ACQuire:MODe {SAMple|PEAKdetect|HIRes|AVErage|ENVelope}
    - ACQuire:MODe?
    - ACQuire:NUMACq?
    - ACQuire:NUMAVg <NR1>
    - ACQuire:NUMAVg?
    - ACQuire:SEQuence:CURrent?
    - ACQuire:SEQuence:MODe NUMACQs
    - ACQuire:SEQuence:NUMSEQuence <NR1>
    - ACQuire:SEQuence:NUMSEQuence?
    - ACQuire:STATE {<NR1>|OFF|ON|RUN|STOP}
    - ACQuire:STATE?
    - ACQuire:STOPAfter {RUNSTop|SEQuence}
    - ACQuire:STOPAfter?
    - ACQuire?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class AcquireStopafter(SCPICmdWrite, SCPICmdRead):
    """The ``ACQuire:STOPAfter`` command.

    Description:
        - This command sets or queries whether the instrument continually acquires acquisitions or
          acquires a single sequence. Pressing SINGLE on the front panel button is equivalent to
          sending these commands: ``ACQUIRE:STOPAFTER SEQUENCE`` and ``ACQUIRE:STATE 1``.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire:STOPAfter?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire:STOPAfter?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACQuire:STOPAfter value`` command.

    SCPI Syntax:
        ```
        - ACQuire:STOPAfter {RUNSTop|SEQuence}
        - ACQuire:STOPAfter?
        ```

    Info:
        - ``RUNSTop`` specifies that the instrument will continually acquire data, if
          ``ACQuire:STATE`` is turned on.
        - ``SEQuence`` specifies that the next acquisition will be a single-sequence acquisition.
    """


class AcquireState(SCPICmdWrite, SCPICmdRead):
    """The ``ACQuire:STATE`` command.

    Description:
        - This command starts or stops acquisitions. When state is set to ON or RUN, a new
          acquisition will be started. If the last acquisition was a single acquisition sequence, a
          new single sequence acquisition will be started. If the last acquisition was continuous, a
          new continuous acquisition will be started. If RUN is issued in the middle of completing a
          single sequence acquisition (for example, averaging or enveloping), the acquisition
          sequence is restarted, and any accumulated data is discarded. Also, the instrument resets
          the number of acquisitions. If the RUN argument is issued while in continuous mode, a
          reset occurs and acquired data continues to acquire. If ``acquire:stopafter`` is SEQUENCE,
          this command leaves the instrument in single sequence, unlike the run/stop button which
          takes the instrument out of single sequence.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACQuire:STATE value`` command.

    SCPI Syntax:
        ```
        - ACQuire:STATE {<NR1>|OFF|ON|RUN|STOP}
        - ACQuire:STATE?
        ```

    Info:
        - ``<NR1>`` = 0 stops acquisitions; any other value starts acquisitions.
        - ``OFF`` stops acquisitions.
        - ``ON`` starts acquisitions.
        - ``RUN`` starts acquisitions.
        - ``STOP`` stops acquisitions.
    """


class AcquireSequenceNumsequence(SCPICmdWrite, SCPICmdRead):
    """The ``ACQuire:SEQuence:NUMSEQuence`` command.

    Description:
        - In single sequence acquisition mode, specify the number of acquisitions or measurements
          that comprise the sequence. The default is 1.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire:SEQuence:NUMSEQuence?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire:SEQuence:NUMSEQuence?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACQuire:SEQuence:NUMSEQuence value``
          command.

    SCPI Syntax:
        ```
        - ACQuire:SEQuence:NUMSEQuence <NR1>
        - ACQuire:SEQuence:NUMSEQuence?
        ```

    Info:
        - ``<NR1>`` is the number of acquisitions or measurements that comprise the sequence.
    """


class AcquireSequenceMode(SCPICmdWrite):
    """The ``ACQuire:SEQuence:MODe`` command.

    Description:
        - In single sequence acquisition, the single sequence stop after count is based on the
          number of acquisitions.

    Usage:
        - Using the ``.write(value)`` method will send the ``ACQuire:SEQuence:MODe value`` command.

    SCPI Syntax:
        ```
        - ACQuire:SEQuence:MODe NUMACQs
        ```

    Info:
        - ``NUMACQs`` is the number of acquisitions.
    """


class AcquireSequenceCurrent(SCPICmdRead):
    """The ``ACQuire:SEQuence:CURrent`` command.

    Description:
        - In single sequence acquisition mode, this query returns the number of acquisitions or
          measurements in the sequence completed so far.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire:SEQuence:CURrent?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire:SEQuence:CURrent?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ACQuire:SEQuence:CURrent?
        ```
    """


class AcquireSequence(SCPICmdRead):
    """The ``ACQuire:SEQuence`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire:SEQuence?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire:SEQuence?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.current``: The ``ACQuire:SEQuence:CURrent`` command.
        - ``.mode``: The ``ACQuire:SEQuence:MODe`` command.
        - ``.numsequence``: The ``ACQuire:SEQuence:NUMSEQuence`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._current = AcquireSequenceCurrent(device, f"{self._cmd_syntax}:CURrent")
        self._mode = AcquireSequenceMode(device, f"{self._cmd_syntax}:MODe")
        self._numsequence = AcquireSequenceNumsequence(device, f"{self._cmd_syntax}:NUMSEQuence")

    @property
    def current(self) -> AcquireSequenceCurrent:
        """Return the ``ACQuire:SEQuence:CURrent`` command.

        Description:
            - In single sequence acquisition mode, this query returns the number of acquisitions or
              measurements in the sequence completed so far.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire:SEQuence:CURrent?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire:SEQuence:CURrent?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ACQuire:SEQuence:CURrent?
            ```
        """
        return self._current

    @property
    def mode(self) -> AcquireSequenceMode:
        """Return the ``ACQuire:SEQuence:MODe`` command.

        Description:
            - In single sequence acquisition, the single sequence stop after count is based on the
              number of acquisitions.

        Usage:
            - Using the ``.write(value)`` method will send the ``ACQuire:SEQuence:MODe value``
              command.

        SCPI Syntax:
            ```
            - ACQuire:SEQuence:MODe NUMACQs
            ```

        Info:
            - ``NUMACQs`` is the number of acquisitions.
        """
        return self._mode

    @property
    def numsequence(self) -> AcquireSequenceNumsequence:
        """Return the ``ACQuire:SEQuence:NUMSEQuence`` command.

        Description:
            - In single sequence acquisition mode, specify the number of acquisitions or
              measurements that comprise the sequence. The default is 1.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire:SEQuence:NUMSEQuence?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire:SEQuence:NUMSEQuence?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACQuire:SEQuence:NUMSEQuence value`` command.

        SCPI Syntax:
            ```
            - ACQuire:SEQuence:NUMSEQuence <NR1>
            - ACQuire:SEQuence:NUMSEQuence?
            ```

        Info:
            - ``<NR1>`` is the number of acquisitions or measurements that comprise the sequence.
        """
        return self._numsequence


class AcquireNumavg(SCPICmdWrite, SCPICmdRead):
    """The ``ACQuire:NUMAVg`` command.

    Description:
        - This command sets or queries the number of waveform acquisitions that make up an averaged
          waveform. Ranges from 2 to 10240.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire:NUMAVg?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire:NUMAVg?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACQuire:NUMAVg value`` command.

    SCPI Syntax:
        ```
        - ACQuire:NUMAVg <NR1>
        - ACQuire:NUMAVg?
        ```

    Info:
        - ``<NR1>`` is the number of waveform acquisitions to average.
    """


class AcquireNumacq(SCPICmdRead):
    """The ``ACQuire:NUMACq`` command.

    Description:
        - This query-only command returns the number of waveform acquisitions that have occurred
          since the last time acquisitions were stopped.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire:NUMACq?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire:NUMACq?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ACQuire:NUMACq?
        ```
    """


class AcquireMode(SCPICmdWrite, SCPICmdRead):
    """The ``ACQuire:MODe`` command.

    Description:
        - This command sets or queries the selected acquisition mode of the instrument.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire:MODe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACQuire:MODe value`` command.

    SCPI Syntax:
        ```
        - ACQuire:MODe {SAMple|PEAKdetect|HIRes|AVErage|ENVelope}
        - ACQuire:MODe?
        ```

    Info:
        - ``SAMple`` specifies that the displayed data point value is the first sampled value that
          is taken during the acquisition interval. The CURVE query, depending on sample rate, will
          result in either 8 bit or 16 bit data. In case of 8 bit data, the precision is also 8 bit.
          However, in case of 16 bit data, 12 bit precision data is zero padded in lower 4 bits.
          SAMple is the default mode.
        - ``PEAKdetect`` specifies the display of high-low range of the samples taken from a single
          waveform acquisition. The high-low range is displayed as a vertical column that extends
          from the highest to the lowest value sampled during the acquisition interval. PEAKdetect
          mode can reveal the presence of aliasing or narrow spikes.
        - ``HIRes`` specifies Hi Res mode where the displayed data point value is the average of all
          the samples taken during the acquisition interval. This is a form of averaging, where the
          average comes from a single waveform acquisition. The number of samples taken during the
          acquisition interval determines the number of data values that compose the average.
        - ``AVErage`` specifies averaging mode, in which the resulting waveform shows an average of
          SAMple data points from several separate waveform acquisitions. The instrument processes
          the number of waveforms you specify into the acquired waveform, creating a running
          exponential average of the input signal. The number of waveform acquisitions that go into
          making up the average waveform is set or queried using the ``ACQUIRE:NUMAVG`` command.
        - ``ENVelope`` specifies envelope mode, where the resulting waveform displays the range of
          PEAKdetect from continued waveform acquisitions.
    """


class AcquireMaxsamplerate(SCPICmdRead):
    """The ``ACQuire:MAXSamplerate`` command.

    Description:
        - This query returns the maximum real-time sample rate.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire:MAXSamplerate?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire:MAXSamplerate?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ACQuire:MAXSamplerate?
        ```
    """


class AcquireFastacqState(SCPICmdWrite, SCPICmdRead):
    """The ``ACQuire:FASTAcq:STATE`` command.

    Description:
        - Sets or queries the state of fast acquisition mode.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire:FASTAcq:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire:FASTAcq:STATE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACQuire:FASTAcq:STATE value`` command.

    SCPI Syntax:
        ```
        - ACQuire:FASTAcq:STATE {ON|OFF|<NR1>}
        - ACQuire:FASTAcq:STATE?
        ```

    Info:
        - ``<NR1>`` = 0 disables FASTAcq; any other value turns this feature on.
        - ``OFF`` disables the FASTAcq feature.
        - ``ON`` enables the FASTAcq feature.
    """


class AcquireFastacqPalette(SCPICmdWrite, SCPICmdRead):
    """The ``ACQuire:FASTAcq:PALEtte`` command.

    Description:
        - Sets or queries the waveform grading for fast acquisition mode.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire:FASTAcq:PALEtte?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire:FASTAcq:PALEtte?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACQuire:FASTAcq:PALEtte value``
          command.

    SCPI Syntax:
        ```
        - ACQuire:FASTAcq:PALEtte {NORMal|TEMPerature|SPECtral|INVErted}
        - ACQuire:FASTAcq:PALEtte?
        ```

    Info:
        - ``NORMal`` colors traces according to their channel.
        - ``TEMPerature`` colors all traces using a multicolored palette, where 'intensity' is
          represented by hue; blue for least frequently hit, red for most frequently hit. All traces
          share this palette. This is the default color palette.
        - ``SPECtral`` colors all traces using a multicolored palette, where 'intensity' is
          represented by hue; red for least frequently hit, blue for most frequently hit. All traces
          share this palette.
        - ``INVErted`` Inverts the normal display hues and lightness levels based on sample
          intensity. The areas of lowest sample density appear the brightest, while the areas with
          the highest sample density appear the darkest.
    """


class AcquireFastacq(SCPICmdRead):
    """The ``ACQuire:FASTAcq`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire:FASTAcq?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire:FASTAcq?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.palette``: The ``ACQuire:FASTAcq:PALEtte`` command.
        - ``.state``: The ``ACQuire:FASTAcq:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._palette = AcquireFastacqPalette(device, f"{self._cmd_syntax}:PALEtte")
        self._state = AcquireFastacqState(device, f"{self._cmd_syntax}:STATE")

    @property
    def palette(self) -> AcquireFastacqPalette:
        """Return the ``ACQuire:FASTAcq:PALEtte`` command.

        Description:
            - Sets or queries the waveform grading for fast acquisition mode.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire:FASTAcq:PALEtte?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire:FASTAcq:PALEtte?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACQuire:FASTAcq:PALEtte value``
              command.

        SCPI Syntax:
            ```
            - ACQuire:FASTAcq:PALEtte {NORMal|TEMPerature|SPECtral|INVErted}
            - ACQuire:FASTAcq:PALEtte?
            ```

        Info:
            - ``NORMal`` colors traces according to their channel.
            - ``TEMPerature`` colors all traces using a multicolored palette, where 'intensity' is
              represented by hue; blue for least frequently hit, red for most frequently hit. All
              traces share this palette. This is the default color palette.
            - ``SPECtral`` colors all traces using a multicolored palette, where 'intensity' is
              represented by hue; red for least frequently hit, blue for most frequently hit. All
              traces share this palette.
            - ``INVErted`` Inverts the normal display hues and lightness levels based on sample
              intensity. The areas of lowest sample density appear the brightest, while the areas
              with the highest sample density appear the darkest.
        """
        return self._palette

    @property
    def state(self) -> AcquireFastacqState:
        """Return the ``ACQuire:FASTAcq:STATE`` command.

        Description:
            - Sets or queries the state of fast acquisition mode.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire:FASTAcq:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire:FASTAcq:STATE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACQuire:FASTAcq:STATE value``
              command.

        SCPI Syntax:
            ```
            - ACQuire:FASTAcq:STATE {ON|OFF|<NR1>}
            - ACQuire:FASTAcq:STATE?
            ```

        Info:
            - ``<NR1>`` = 0 disables FASTAcq; any other value turns this feature on.
            - ``OFF`` disables the FASTAcq feature.
            - ``ON`` enables the FASTAcq feature.
        """
        return self._state


#  pylint: disable=too-many-instance-attributes
class Acquire(SCPICmdRead):
    """The ``ACQuire`` command.

    Description:
        - Queries the current acquisition state.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ACQuire?
        ```

    Properties:
        - ``.fastacq``: The ``ACQuire:FASTAcq`` command tree.
        - ``.maxsamplerate``: The ``ACQuire:MAXSamplerate`` command.
        - ``.mode``: The ``ACQuire:MODe`` command.
        - ``.numacq``: The ``ACQuire:NUMACq`` command.
        - ``.numavg``: The ``ACQuire:NUMAVg`` command.
        - ``.sequence``: The ``ACQuire:SEQuence`` command tree.
        - ``.state``: The ``ACQuire:STATE`` command.
        - ``.stopafter``: The ``ACQuire:STOPAfter`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "ACQuire") -> None:
        super().__init__(device, cmd_syntax)
        self._fastacq = AcquireFastacq(device, f"{self._cmd_syntax}:FASTAcq")
        self._maxsamplerate = AcquireMaxsamplerate(device, f"{self._cmd_syntax}:MAXSamplerate")
        self._mode = AcquireMode(device, f"{self._cmd_syntax}:MODe")
        self._numacq = AcquireNumacq(device, f"{self._cmd_syntax}:NUMACq")
        self._numavg = AcquireNumavg(device, f"{self._cmd_syntax}:NUMAVg")
        self._sequence = AcquireSequence(device, f"{self._cmd_syntax}:SEQuence")
        self._state = AcquireState(device, f"{self._cmd_syntax}:STATE")
        self._stopafter = AcquireStopafter(device, f"{self._cmd_syntax}:STOPAfter")

    @property
    def fastacq(self) -> AcquireFastacq:
        """Return the ``ACQuire:FASTAcq`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire:FASTAcq?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire:FASTAcq?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.palette``: The ``ACQuire:FASTAcq:PALEtte`` command.
            - ``.state``: The ``ACQuire:FASTAcq:STATE`` command.
        """
        return self._fastacq

    @property
    def maxsamplerate(self) -> AcquireMaxsamplerate:
        """Return the ``ACQuire:MAXSamplerate`` command.

        Description:
            - This query returns the maximum real-time sample rate.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire:MAXSamplerate?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire:MAXSamplerate?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ACQuire:MAXSamplerate?
            ```
        """
        return self._maxsamplerate

    @property
    def mode(self) -> AcquireMode:
        """Return the ``ACQuire:MODe`` command.

        Description:
            - This command sets or queries the selected acquisition mode of the instrument.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire:MODe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACQuire:MODe value`` command.

        SCPI Syntax:
            ```
            - ACQuire:MODe {SAMple|PEAKdetect|HIRes|AVErage|ENVelope}
            - ACQuire:MODe?
            ```

        Info:
            - ``SAMple`` specifies that the displayed data point value is the first sampled value
              that is taken during the acquisition interval. The CURVE query, depending on sample
              rate, will result in either 8 bit or 16 bit data. In case of 8 bit data, the precision
              is also 8 bit. However, in case of 16 bit data, 12 bit precision data is zero padded
              in lower 4 bits. SAMple is the default mode.
            - ``PEAKdetect`` specifies the display of high-low range of the samples taken from a
              single waveform acquisition. The high-low range is displayed as a vertical column that
              extends from the highest to the lowest value sampled during the acquisition interval.
              PEAKdetect mode can reveal the presence of aliasing or narrow spikes.
            - ``HIRes`` specifies Hi Res mode where the displayed data point value is the average of
              all the samples taken during the acquisition interval. This is a form of averaging,
              where the average comes from a single waveform acquisition. The number of samples
              taken during the acquisition interval determines the number of data values that
              compose the average.
            - ``AVErage`` specifies averaging mode, in which the resulting waveform shows an average
              of SAMple data points from several separate waveform acquisitions. The instrument
              processes the number of waveforms you specify into the acquired waveform, creating a
              running exponential average of the input signal. The number of waveform acquisitions
              that go into making up the average waveform is set or queried using the
              ``ACQUIRE:NUMAVG`` command.
            - ``ENVelope`` specifies envelope mode, where the resulting waveform displays the range
              of PEAKdetect from continued waveform acquisitions.
        """
        return self._mode

    @property
    def numacq(self) -> AcquireNumacq:
        """Return the ``ACQuire:NUMACq`` command.

        Description:
            - This query-only command returns the number of waveform acquisitions that have occurred
              since the last time acquisitions were stopped.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire:NUMACq?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire:NUMACq?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ACQuire:NUMACq?
            ```
        """
        return self._numacq

    @property
    def numavg(self) -> AcquireNumavg:
        """Return the ``ACQuire:NUMAVg`` command.

        Description:
            - This command sets or queries the number of waveform acquisitions that make up an
              averaged waveform. Ranges from 2 to 10240.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire:NUMAVg?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire:NUMAVg?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACQuire:NUMAVg value`` command.

        SCPI Syntax:
            ```
            - ACQuire:NUMAVg <NR1>
            - ACQuire:NUMAVg?
            ```

        Info:
            - ``<NR1>`` is the number of waveform acquisitions to average.
        """
        return self._numavg

    @property
    def sequence(self) -> AcquireSequence:
        """Return the ``ACQuire:SEQuence`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire:SEQuence?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire:SEQuence?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.current``: The ``ACQuire:SEQuence:CURrent`` command.
            - ``.mode``: The ``ACQuire:SEQuence:MODe`` command.
            - ``.numsequence``: The ``ACQuire:SEQuence:NUMSEQuence`` command.
        """
        return self._sequence

    @property
    def state(self) -> AcquireState:
        """Return the ``ACQuire:STATE`` command.

        Description:
            - This command starts or stops acquisitions. When state is set to ON or RUN, a new
              acquisition will be started. If the last acquisition was a single acquisition
              sequence, a new single sequence acquisition will be started. If the last acquisition
              was continuous, a new continuous acquisition will be started. If RUN is issued in the
              middle of completing a single sequence acquisition (for example, averaging or
              enveloping), the acquisition sequence is restarted, and any accumulated data is
              discarded. Also, the instrument resets the number of acquisitions. If the RUN argument
              is issued while in continuous mode, a reset occurs and acquired data continues to
              acquire. If ``acquire:stopafter`` is SEQUENCE, this command leaves the instrument in
              single sequence, unlike the run/stop button which takes the instrument out of single
              sequence.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire:STATE?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACQuire:STATE value`` command.

        SCPI Syntax:
            ```
            - ACQuire:STATE {<NR1>|OFF|ON|RUN|STOP}
            - ACQuire:STATE?
            ```

        Info:
            - ``<NR1>`` = 0 stops acquisitions; any other value starts acquisitions.
            - ``OFF`` stops acquisitions.
            - ``ON`` starts acquisitions.
            - ``RUN`` starts acquisitions.
            - ``STOP`` stops acquisitions.
        """
        return self._state

    @property
    def stopafter(self) -> AcquireStopafter:
        """Return the ``ACQuire:STOPAfter`` command.

        Description:
            - This command sets or queries whether the instrument continually acquires acquisitions
              or acquires a single sequence. Pressing SINGLE on the front panel button is equivalent
              to sending these commands: ``ACQUIRE:STOPAFTER SEQUENCE`` and ``ACQUIRE:STATE 1``.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire:STOPAfter?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire:STOPAfter?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACQuire:STOPAfter value`` command.

        SCPI Syntax:
            ```
            - ACQuire:STOPAfter {RUNSTop|SEQuence}
            - ACQuire:STOPAfter?
            ```

        Info:
            - ``RUNSTop`` specifies that the instrument will continually acquire data, if
              ``ACQuire:STATE`` is turned on.
            - ``SEQuence`` specifies that the next acquisition will be a single-sequence
              acquisition.
        """
        return self._stopafter
