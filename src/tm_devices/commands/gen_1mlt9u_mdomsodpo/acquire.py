"""The acquire commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - ACQuire:FASTAcq
    - ACQuire:FASTAcq:PALEtte {NORMal|TEMPErature|SPECTral|INVERTed}
    - ACQuire:FASTAcq:PALEtte?
    - ACQuire:FASTAcq:STATE {0|1|OFF|ON}
    - ACQuire:FASTAcq:STATE?
    - ACQuire:MAGnivu {ON|OFF|<NR1>}
    - ACQuire:MAGnivu?
    - ACQuire:MAXSamplerate?
    - ACQuire:MODe {SAMple|PEAKdetect|HIRes|AVErage|ENVelope}
    - ACQuire:MODe?
    - ACQuire:NUMACq?
    - ACQuire:NUMAVg <NR1>
    - ACQuire:NUMAVg?
    - ACQuire:NUMEnv {<NR1>|INFInite}
    - ACQuire:NUMEnv?
    - ACQuire:STATE {OFF|ON|RUN|STOP|<NR1>}
    - ACQuire:STATE?
    - ACQuire:STOPAfter {RUNSTop|SEQuence}
    - ACQuire:STOPAfter?
    - ACQuire?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

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
        - Starts or stops acquisitions. When state is set to ON or RUN, a new acquisition will be
          started. If the last acquisition was a single acquisition sequence, a new single sequence
          acquisition will be started. If the last acquisition was continuous, a new continuous
          acquisition will be started. If RUN is issued in the process of completing a single
          sequence acquisition (for example, averaging or enveloping), the acquisition sequence is
          restarted, and any accumulated data is discarded. Also, the oscilloscope resets the number
          of acquisitions. If the RUN argument is issued while in continuous mode, acquisition
          continues.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACQuire:STATE value`` command.

    SCPI Syntax:
        ```
        - ACQuire:STATE {OFF|ON|RUN|STOP|<NR1>}
        - ACQuire:STATE?
        ```

    Info:
        - ``OFF`` stops acquisitions.
        - ``STOP`` stops acquisitions.
        - ``ON`` starts acquisitions.
        - ``RUN`` starts acquisitions.
        - ``<NR1>`` = 0 stops acquisitions; any other value starts acquisitions.
    """


class AcquireNumenv(SCPICmdWrite, SCPICmdRead):
    """The ``ACQuire:NUMEnv`` command.

    Description:
        - This command controls the number of envelopes (when acquisition mode has been set to
          ENVelope using ``ACQUIRE:MODE``). The number of envelopes can be set from 1 to 2000 in
          increments of 1, or to INFInite. Setting the value to a number greater than 2000 sets the
          number of envelopes to INFInite.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire:NUMEnv?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire:NUMEnv?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACQuire:NUMEnv value`` command.

    SCPI Syntax:
        ```
        - ACQuire:NUMEnv {<NR1>|INFInite}
        - ACQuire:NUMEnv?
        ```

    Info:
        - ``<NR1>`` is an integer that specifies the number of envelopes to use when the acquisition
          mode has been set to ENVelope.
        - ``INFInite`` specifies to use an infinite number of envelopes.
    """


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


class AcquireMagnivu(SCPICmdWrite, SCPICmdRead):
    """The ``ACQuire:MAGnivu`` command.

    Description:
        - Turns on the MagniVu feature, which provides up to 32 times signal detail for fast viewing
          of short events. This feature is not recommended for slow data formats such as RS-232.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire:MAGnivu?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire:MAGnivu?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACQuire:MAGnivu value`` command.

    SCPI Syntax:
        ```
        - ACQuire:MAGnivu {ON|OFF|<NR1>}
        - ACQuire:MAGnivu?
        ```

    Info:
        - ``<NR1> = 0`` disables the MagniVu feature; any other value turns this feature on.
        - ``ON`` enables the MagniVu feature.
        - ``OFF`` disables the MagniVu feature.
    """


class AcquireFastacqState(SCPICmdWrite, SCPICmdRead):
    """The ``ACQuire:FASTAcq:STATE`` command.

    Description:
        - Turns fast acquisition mode on or off, or queries the state of the mode.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire:FASTAcq:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire:FASTAcq:STATE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACQuire:FASTAcq:STATE value`` command.

    SCPI Syntax:
        ```
        - ACQuire:FASTAcq:STATE {0|1|OFF|ON}
        - ACQuire:FASTAcq:STATE?
        ```

    Info:
        - ``1`` or ON turns on fast acquisition mode.
        - ``0`` or OFF turns it off.
    """


class AcquireFastacqPalette(SCPICmdWrite, SCPICmdRead):
    """The ``ACQuire:FASTAcq:PALEtte`` command.

    Description:
        - Sets (or queries) which palette to use for fast acquisition mode.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire:FASTAcq:PALEtte?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire:FASTAcq:PALEtte?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACQuire:FASTAcq:PALEtte value``
          command.

    SCPI Syntax:
        ```
        - ACQuire:FASTAcq:PALEtte {NORMal|TEMPErature|SPECTral|INVERTed}
        - ACQuire:FASTAcq:PALEtte?
        ```

    Info:
        - ``NORMal`` - Normal displays hues and lightness levels for best overall viewing. The color
          of each channel waveform matches the color of the corresponding front-panel vertical knob.
        - ``TEMPErature`` - Temperature Grading displays areas of the waveform with the highest
          sample density in red shades. The areas of lowest sample density appear in blue shades.
        - ``SPECTra`` - Spectral Grading displays areas of the waveform with the highest sample
          density in blue shades. The areas of lowest sample density appear in red shades.
        - ``INVERTed`` - Inverts the normal display hues and lightness levels based on sample
          intensity. The areas of lowest sample density appear the brightest, while the areas with
          the highest sample density appear the darkest.
    """


class AcquireFastacq(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``ACQuire:FASTAcq`` command.

    Description:
        - Sets or queries the FastAcq feature. This feature provides a high-speed waveform capture
          rate to help capture signal anomalies.

    Usage:
        - Using the ``.write()`` method will send the ``ACQuire:FASTAcq`` command.

    SCPI Syntax:
        ```
        - ACQuire:FASTAcq
        ```

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
            - Sets (or queries) which palette to use for fast acquisition mode.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire:FASTAcq:PALEtte?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire:FASTAcq:PALEtte?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACQuire:FASTAcq:PALEtte value``
              command.

        SCPI Syntax:
            ```
            - ACQuire:FASTAcq:PALEtte {NORMal|TEMPErature|SPECTral|INVERTed}
            - ACQuire:FASTAcq:PALEtte?
            ```

        Info:
            - ``NORMal`` - Normal displays hues and lightness levels for best overall viewing. The
              color of each channel waveform matches the color of the corresponding front-panel
              vertical knob.
            - ``TEMPErature`` - Temperature Grading displays areas of the waveform with the highest
              sample density in red shades. The areas of lowest sample density appear in blue
              shades.
            - ``SPECTra`` - Spectral Grading displays areas of the waveform with the highest sample
              density in blue shades. The areas of lowest sample density appear in red shades.
            - ``INVERTed`` - Inverts the normal display hues and lightness levels based on sample
              intensity. The areas of lowest sample density appear the brightest, while the areas
              with the highest sample density appear the darkest.
        """
        return self._palette

    @property
    def state(self) -> AcquireFastacqState:
        """Return the ``ACQuire:FASTAcq:STATE`` command.

        Description:
            - Turns fast acquisition mode on or off, or queries the state of the mode.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire:FASTAcq:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire:FASTAcq:STATE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACQuire:FASTAcq:STATE value``
              command.

        SCPI Syntax:
            ```
            - ACQuire:FASTAcq:STATE {0|1|OFF|ON}
            - ACQuire:FASTAcq:STATE?
            ```

        Info:
            - ``1`` or ON turns on fast acquisition mode.
            - ``0`` or OFF turns it off.
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
        - ``.fastacq``: The ``ACQuire:FASTAcq`` command.
        - ``.magnivu``: The ``ACQuire:MAGnivu`` command.
        - ``.maxsamplerate``: The ``ACQuire:MAXSamplerate`` command.
        - ``.mode``: The ``ACQuire:MODe`` command.
        - ``.numacq``: The ``ACQuire:NUMACq`` command.
        - ``.numavg``: The ``ACQuire:NUMAVg`` command.
        - ``.numenv``: The ``ACQuire:NUMEnv`` command.
        - ``.state``: The ``ACQuire:STATE`` command.
        - ``.stopafter``: The ``ACQuire:STOPAfter`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "ACQuire") -> None:
        super().__init__(device, cmd_syntax)
        self._fastacq = AcquireFastacq(device, f"{self._cmd_syntax}:FASTAcq")
        self._magnivu = AcquireMagnivu(device, f"{self._cmd_syntax}:MAGnivu")
        self._maxsamplerate = AcquireMaxsamplerate(device, f"{self._cmd_syntax}:MAXSamplerate")
        self._mode = AcquireMode(device, f"{self._cmd_syntax}:MODe")
        self._numacq = AcquireNumacq(device, f"{self._cmd_syntax}:NUMACq")
        self._numavg = AcquireNumavg(device, f"{self._cmd_syntax}:NUMAVg")
        self._numenv = AcquireNumenv(device, f"{self._cmd_syntax}:NUMEnv")
        self._state = AcquireState(device, f"{self._cmd_syntax}:STATE")
        self._stopafter = AcquireStopafter(device, f"{self._cmd_syntax}:STOPAfter")

    @property
    def fastacq(self) -> AcquireFastacq:
        """Return the ``ACQuire:FASTAcq`` command.

        Description:
            - Sets or queries the FastAcq feature. This feature provides a high-speed waveform
              capture rate to help capture signal anomalies.

        Usage:
            - Using the ``.write()`` method will send the ``ACQuire:FASTAcq`` command.

        SCPI Syntax:
            ```
            - ACQuire:FASTAcq
            ```

        Sub-properties:
            - ``.palette``: The ``ACQuire:FASTAcq:PALEtte`` command.
            - ``.state``: The ``ACQuire:FASTAcq:STATE`` command.
        """
        return self._fastacq

    @property
    def magnivu(self) -> AcquireMagnivu:
        """Return the ``ACQuire:MAGnivu`` command.

        Description:
            - Turns on the MagniVu feature, which provides up to 32 times signal detail for fast
              viewing of short events. This feature is not recommended for slow data formats such as
              RS-232.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire:MAGnivu?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire:MAGnivu?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACQuire:MAGnivu value`` command.

        SCPI Syntax:
            ```
            - ACQuire:MAGnivu {ON|OFF|<NR1>}
            - ACQuire:MAGnivu?
            ```

        Info:
            - ``<NR1> = 0`` disables the MagniVu feature; any other value turns this feature on.
            - ``ON`` enables the MagniVu feature.
            - ``OFF`` disables the MagniVu feature.
        """
        return self._magnivu

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
    def numenv(self) -> AcquireNumenv:
        """Return the ``ACQuire:NUMEnv`` command.

        Description:
            - This command controls the number of envelopes (when acquisition mode has been set to
              ENVelope using ``ACQUIRE:MODE``). The number of envelopes can be set from 1 to 2000 in
              increments of 1, or to INFInite. Setting the value to a number greater than 2000 sets
              the number of envelopes to INFInite.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire:NUMEnv?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire:NUMEnv?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACQuire:NUMEnv value`` command.

        SCPI Syntax:
            ```
            - ACQuire:NUMEnv {<NR1>|INFInite}
            - ACQuire:NUMEnv?
            ```

        Info:
            - ``<NR1>`` is an integer that specifies the number of envelopes to use when the
              acquisition mode has been set to ENVelope.
            - ``INFInite`` specifies to use an infinite number of envelopes.
        """
        return self._numenv

    @property
    def state(self) -> AcquireState:
        """Return the ``ACQuire:STATE`` command.

        Description:
            - Starts or stops acquisitions. When state is set to ON or RUN, a new acquisition will
              be started. If the last acquisition was a single acquisition sequence, a new single
              sequence acquisition will be started. If the last acquisition was continuous, a new
              continuous acquisition will be started. If RUN is issued in the process of completing
              a single sequence acquisition (for example, averaging or enveloping), the acquisition
              sequence is restarted, and any accumulated data is discarded. Also, the oscilloscope
              resets the number of acquisitions. If the RUN argument is issued while in continuous
              mode, acquisition continues.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire:STATE?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACQuire:STATE value`` command.

        SCPI Syntax:
            ```
            - ACQuire:STATE {OFF|ON|RUN|STOP|<NR1>}
            - ACQuire:STATE?
            ```

        Info:
            - ``OFF`` stops acquisitions.
            - ``STOP`` stops acquisitions.
            - ``ON`` starts acquisitions.
            - ``RUN`` starts acquisitions.
            - ``<NR1>`` = 0 stops acquisitions; any other value starts acquisitions.
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
