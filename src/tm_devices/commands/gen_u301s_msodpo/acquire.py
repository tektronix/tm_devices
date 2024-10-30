"""The acquire commands module.

These commands are used in the following models:
DPO2K, DPO2KB, MSO2K, MSO2KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - ACQuire:MAGnivu {ON|OFF|<NR1>}
    - ACQuire:MAGnivu?
    - ACQuire:MAXSamplerate?
    - ACQuire:MODe {SAMple|AVErage}
    - ACQuire:MODe?
    - ACQuire:NUMACq?
    - ACQuire:NUMAVg <NR1>
    - ACQuire:NUMAVg?
    - ACQuire:STATE {OFF|ON|RUN|STOP|<NR1>}
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
        - Sets or returns the acquisition mode of the oscilloscope for all live waveforms. Waveforms
          are the displayed data point values taken from acquisition intervals. Each acquisition
          interval represents a time duration set by the horizontal scale (time per division). The
          oscilloscope sampling system always samples at the maximum rate, so the acquisition
          interval may include than one sample. The acquisition mode (which you set using this
          ``ACQuire:MODe`` command) determines how the final value of the acquisition interval is
          generated from the many data samples.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire:MODe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACQuire:MODe value`` command.

    SCPI Syntax:
        ```
        - ACQuire:MODe {SAMple|AVErage}
        - ACQuire:MODe?
        ```

    Info:
        - ``SAMple`` specifies that the displayed data point value is the first sampled value that
          is taken during the acquisition interval. In sample mode, all waveform data has 8 bits of
          precision. You can request 16 bit data with a CURVE query but the lower-order 8 bits of
          data will be zero. SAMple is the default mode.
        - ``AVErage`` specifies averaging mode, in which the resulting waveform shows an average of
          SAMple data points from several separate waveform acquisitions. The oscilloscope processes
          the number of waveforms you specify into the acquired waveform, creating a running
          exponential average of the input signal. The number of waveform acquisitions that go into
          making up the average waveform is set or queried using the ``ACQuire:NUMAVg`` command.
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
        - ``.magnivu``: The ``ACQuire:MAGnivu`` command.
        - ``.maxsamplerate``: The ``ACQuire:MAXSamplerate`` command.
        - ``.mode``: The ``ACQuire:MODe`` command.
        - ``.numacq``: The ``ACQuire:NUMACq`` command.
        - ``.numavg``: The ``ACQuire:NUMAVg`` command.
        - ``.state``: The ``ACQuire:STATE`` command.
        - ``.stopafter``: The ``ACQuire:STOPAfter`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "ACQuire") -> None:
        super().__init__(device, cmd_syntax)
        self._magnivu = AcquireMagnivu(device, f"{self._cmd_syntax}:MAGnivu")
        self._maxsamplerate = AcquireMaxsamplerate(device, f"{self._cmd_syntax}:MAXSamplerate")
        self._mode = AcquireMode(device, f"{self._cmd_syntax}:MODe")
        self._numacq = AcquireNumacq(device, f"{self._cmd_syntax}:NUMACq")
        self._numavg = AcquireNumavg(device, f"{self._cmd_syntax}:NUMAVg")
        self._state = AcquireState(device, f"{self._cmd_syntax}:STATE")
        self._stopafter = AcquireStopafter(device, f"{self._cmd_syntax}:STOPAfter")

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
            - Sets or returns the acquisition mode of the oscilloscope for all live waveforms.
              Waveforms are the displayed data point values taken from acquisition intervals. Each
              acquisition interval represents a time duration set by the horizontal scale (time per
              division). The oscilloscope sampling system always samples at the maximum rate, so the
              acquisition interval may include than one sample. The acquisition mode (which you set
              using this ``ACQuire:MODe`` command) determines how the final value of the acquisition
              interval is generated from the many data samples.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire:MODe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACQuire:MODe value`` command.

        SCPI Syntax:
            ```
            - ACQuire:MODe {SAMple|AVErage}
            - ACQuire:MODe?
            ```

        Info:
            - ``SAMple`` specifies that the displayed data point value is the first sampled value
              that is taken during the acquisition interval. In sample mode, all waveform data has 8
              bits of precision. You can request 16 bit data with a CURVE query but the lower-order
              8 bits of data will be zero. SAMple is the default mode.
            - ``AVErage`` specifies averaging mode, in which the resulting waveform shows an average
              of SAMple data points from several separate waveform acquisitions. The oscilloscope
              processes the number of waveforms you specify into the acquired waveform, creating a
              running exponential average of the input signal. The number of waveform acquisitions
              that go into making up the average waveform is set or queried using the
              ``ACQuire:NUMAVg`` command.
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
