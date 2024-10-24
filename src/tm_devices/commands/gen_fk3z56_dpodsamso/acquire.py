"""The acquire commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - ACQuire:ENHANCEDEnob {OFF|AUTO}
    - ACQuire:ENHANCEDEnob:STATE?
    - ACQuire:INTERPEightbit {AUTO|ON|OFF}
    - ACQuire:INTERPEightbit?
    - ACQuire:MAGnivu {ON|OFF|<NR1>}
    - ACQuire:MAGnivu?
    - ACQuire:MODe {SAMple|PEAKdetect|HIRes|AVErage|WFMDB|ENVelope}
    - ACQuire:MODe:ACTUal?
    - ACQuire:MODe?
    - ACQuire:NUMACq?
    - ACQuire:NUMAVg <NR1>
    - ACQuire:NUMAVg?
    - ACQuire:NUMEnv {<NR1>|INFInite}
    - ACQuire:NUMEnv?
    - ACQuire:NUMFRAMESACQuired?
    - ACQuire:NUMSAMples <NR1>
    - ACQuire:NUMSAMples?
    - ACQuire:SAMPlingmode {RT|ET|IT}
    - ACQuire:SAMPlingmode?
    - ACQuire:STATE {<NR1>|OFF|ON|RUN|STOP}
    - ACQuire:STATE?
    - ACQuire:STOPAfter {RUNSTop|SEQuence}
    - ACQuire:STOPAfter?
    - ACQuire:SYNcsamples {ON|OFF}
    - ACQuire:SYNcsamples?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class AcquireSyncsamples(SCPICmdWrite, SCPICmdRead):
    """The ``ACQuire:SYNcsamples`` command.

    Description:
        - This command sets or queries whether the acquisition process is modified to sync up
          samples to trigger (for example, resample the waveform such that ttoff=0). This improves
          waveform jitter and skew in Average mode because each waveform is aligned to the trigger.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire:SYNcsamples?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire:SYNcsamples?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACQuire:SYNcsamples value`` command.

    SCPI Syntax:
        ```
        - ACQuire:SYNcsamples {ON|OFF}
        - ACQuire:SYNcsamples?
        ```

    Info:
        - ``ON`` sets the acquisition process to be modified to sync up samples to trigger.
        - ``OFF`` sets the system so that no modification of the acquisition process is performed.
    """


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


class AcquireSamplingmode(SCPICmdWrite, SCPICmdRead):
    """The ``ACQuire:SAMPlingmode`` command.

    Description:
        - This command sets or queries the sampling mode.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire:SAMPlingmode?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire:SAMPlingmode?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACQuire:SAMPlingmode value`` command.

    SCPI Syntax:
        ```
        - ACQuire:SAMPlingmode {RT|ET|IT}
        - ACQuire:SAMPlingmode?
        ```

    Info:
        - ``RT`` sets the sampling mode to real time only.
        - ``ET`` sets the sampling mode to equivalent time allowed (ON in REPET).
        - ``IT`` sets the sampling mode to interpolation allowed (OFF in REPET).
    """


class AcquireNumsamples(SCPICmdWrite, SCPICmdRead):
    """The ``ACQuire:NUMSAMples`` command.

    Description:
        - This command sets or queries the minimum number of acquired samples that make up a
          waveform database (WfmDB) waveform for single sequence mode and Mask Pass/Fail Completion
          Test. This is equivalent to setting the Waveform Database Samples in the Acquisition Mode
          side menu.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire:NUMSAMples?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire:NUMSAMples?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACQuire:NUMSAMples value`` command.

    SCPI Syntax:
        ```
        - ACQuire:NUMSAMples <NR1>
        - ACQuire:NUMSAMples?
        ```

    Info:
        - ``<NR1>`` is the minimum number of acquired samples that make up a waveform database
          (WfmDB) waveform for single sequence mode and Mask Pass/Fail Completion Test. The default
          value is 16,000 samples. The range is 5,000 to 2,147,400,000 samples.
    """


class AcquireNumframesacquired(SCPICmdRead):
    """The ``ACQuire:NUMFRAMESACQuired`` command.

    Description:
        - This query returns the number of FastFrame frames which have been acquired.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire:NUMFRAMESACQuired?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire:NUMFRAMESACQuired?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ACQuire:NUMFRAMESACQuired?
        ```
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


class AcquireModeActual(SCPICmdRead):
    """The ``ACQuire:MODe:ACTUal`` command.

    Description:
        - This query returns the acquisition mode that the instrument is actually using for
          acquisitions, as opposed to the ``ACQuire:MODe`` query, which returns the currently
          selected acquisition mode. The acquisition mode that the instrument is using may differ
          from the selected mode in cases where the HIRes or PkDetect mode has been selected and the
          sample rate is greater than or equal to the base sampling rate (that is 6.25 Gs/s for 70K
          oscilloscopes and 5 Gs/s for 5K and 7K oscilloscopes). This is because the HIRes and
          PkDetect modes are not available at such high sampling rates. In these cases, the
          instrument uses sampling mode, and this query returns SAMPLe, regardless of the mode
          selected. In other words, when either HIRes or PkDetect mode has been selected, and the
          sample rate is greater than or equal to the base sampling rate (that is 6.25 Gs/s for 70K
          scopes and 5 Gs/s for 5K and 7K oscilloscopes), use the ``ACQUIRE:MODE`` query to
          determine the current mode selection; use ``ACQuire:MODe:ACTUal?`` to determine which mode
          the instrument is actually using. For other modes, use either query, as they will return
          the same mode.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire:MODe:ACTUal?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire:MODe:ACTUal?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ACQuire:MODe:ACTUal?
        ```
    """


class AcquireMode(SCPICmdWrite, SCPICmdRead):
    """The ``ACQuire:MODe`` command.

    Description:
        - This command sets or queries the selected acquisition mode of the instrument. This affects
          all live waveforms. This command is equivalent to selecting Horizontal/Acquisition from
          the Horiz/Acq menu, and then choosing the desired mode from the Acquisition Mode group
          box. ``ACQuire:MODe`` is the desired acquisition mode. Waveforms are the displayed data
          point values taken from acquisition intervals. Each acquisition interval represents a time
          duration set by the horizontal scale (time per division). The instrument sampling system
          always samples at the maximum rate and so an acquisition interval can include more than
          one sample. The acquisition mode (which you set using this ``ACQuire:MODe`` command)
          determines how the final value of the acquisition interval is generated from the many data
          samples.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire:MODe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACQuire:MODe value`` command.

    SCPI Syntax:
        ```
        - ACQuire:MODe {SAMple|PEAKdetect|HIRes|AVErage|WFMDB|ENVelope}
        - ACQuire:MODe?
        ```

    Info:
        - ``SAMple`` specifies that the displayed data point value is the first sampled value that
          is taken during the acquisition interval. In sample mode, all waveform data has 8 bits of
          precision. You can request 16 bit data with a CURVE query but the lower-order 8 bits of
          data will be zero. SAMple is the default mode.
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
          making up the average waveform is set or queried using the ``ACQUIRE:NUMENV`` command.
        - ``WFMDB`` (Waveform Database) mode acquires and displays a waveform pixmap. A pixmap is
          the accumulation of one or more acquisitions.
        - ``ENVelope`` specifies envelope mode, where the resulting waveform shows the PEAKdetect
          range of data points from several separate waveform acquisitions. The number of waveform
          acquisitions that go into making up the envelope waveform is set or queried using the
          ``ACQUIRE:NUMENV`` command.

    Properties:
        - ``.actual``: The ``ACQuire:MODe:ACTUal`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._actual = AcquireModeActual(device, f"{self._cmd_syntax}:ACTUal")

    @property
    def actual(self) -> AcquireModeActual:
        """Return the ``ACQuire:MODe:ACTUal`` command.

        Description:
            - This query returns the acquisition mode that the instrument is actually using for
              acquisitions, as opposed to the ``ACQuire:MODe`` query, which returns the currently
              selected acquisition mode. The acquisition mode that the instrument is using may
              differ from the selected mode in cases where the HIRes or PkDetect mode has been
              selected and the sample rate is greater than or equal to the base sampling rate (that
              is 6.25 Gs/s for 70K oscilloscopes and 5 Gs/s for 5K and 7K oscilloscopes). This is
              because the HIRes and PkDetect modes are not available at such high sampling rates. In
              these cases, the instrument uses sampling mode, and this query returns SAMPLe,
              regardless of the mode selected. In other words, when either HIRes or PkDetect mode
              has been selected, and the sample rate is greater than or equal to the base sampling
              rate (that is 6.25 Gs/s for 70K scopes and 5 Gs/s for 5K and 7K oscilloscopes), use
              the ``ACQUIRE:MODE`` query to determine the current mode selection; use
              ``ACQuire:MODe:ACTUal?`` to determine which mode the instrument is actually using. For
              other modes, use either query, as they will return the same mode.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire:MODe:ACTUal?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire:MODe:ACTUal?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ACQuire:MODe:ACTUal?
            ```
        """
        return self._actual


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


class AcquireInterpeightbit(SCPICmdWrite, SCPICmdRead):
    """The ``ACQuire:INTERPEightbit`` command.

    Description:
        - This command sets or queries the interpolation acquisition mode of the instrument.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire:INTERPEightbit?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire:INTERPEightbit?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACQuire:INTERPEightbit value`` command.

    SCPI Syntax:
        ```
        - ACQuire:INTERPEightbit {AUTO|ON|OFF}
        - ACQuire:INTERPEightbit?
        ```

    Info:
        - ``AUTO`` lets the instrument automatically select the interpolation acquisition mode.
        - ``ON`` turns on the eight bit interpolation mode.
        - ``OFF`` turns off the eight bit interpolation mode.
    """


class AcquireEnhancedenobState(SCPICmdRead):
    """The ``ACQuire:ENHANCEDEnob:STATE`` command.

    Description:
        - This command queries the state of the enhanced effective number of bits.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire:ENHANCEDEnob:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire:ENHANCEDEnob:STATE?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ACQuire:ENHANCEDEnob:STATE?
        ```
    """


class AcquireEnhancedenob(SCPICmdWrite, SCPICmdRead):
    """The ``ACQuire:ENHANCEDEnob`` command.

    Description:
        - This command sets or queries the state of the enhanced effective number of bits.

    Usage:
        - Using the ``.write(value)`` method will send the ``ACQuire:ENHANCEDEnob value`` command.

    SCPI Syntax:
        ```
        - ACQuire:ENHANCEDEnob {OFF|AUTO}
        ```

    Info:
        - ``OFF`` turns off enhanced effective number of bits.
        - ``AUTO`` turns enhanced effective number of bits to AUTO.

    Properties:
        - ``.state``: The ``ACQuire:ENHANCEDEnob:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = AcquireEnhancedenobState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> AcquireEnhancedenobState:
        """Return the ``ACQuire:ENHANCEDEnob:STATE`` command.

        Description:
            - This command queries the state of the enhanced effective number of bits.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire:ENHANCEDEnob:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire:ENHANCEDEnob:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ACQuire:ENHANCEDEnob:STATE?
            ```
        """
        return self._state


#  pylint: disable=too-many-instance-attributes
class Acquire(SCPICmdRead):
    """The ``ACQuire`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACQuire?`` query.
        - Using the ``.verify(value)`` method will send the ``ACQuire?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.enhancedenob``: The ``ACQuire:ENHANCEDEnob`` command.
        - ``.interpeightbit``: The ``ACQuire:INTERPEightbit`` command.
        - ``.magnivu``: The ``ACQuire:MAGnivu`` command.
        - ``.mode``: The ``ACQuire:MODe`` command.
        - ``.numacq``: The ``ACQuire:NUMACq`` command.
        - ``.numavg``: The ``ACQuire:NUMAVg`` command.
        - ``.numenv``: The ``ACQuire:NUMEnv`` command.
        - ``.numframesacquired``: The ``ACQuire:NUMFRAMESACQuired`` command.
        - ``.numsamples``: The ``ACQuire:NUMSAMples`` command.
        - ``.samplingmode``: The ``ACQuire:SAMPlingmode`` command.
        - ``.state``: The ``ACQuire:STATE`` command.
        - ``.stopafter``: The ``ACQuire:STOPAfter`` command.
        - ``.syncsamples``: The ``ACQuire:SYNcsamples`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "ACQuire") -> None:
        super().__init__(device, cmd_syntax)
        self._enhancedenob = AcquireEnhancedenob(device, f"{self._cmd_syntax}:ENHANCEDEnob")
        self._interpeightbit = AcquireInterpeightbit(device, f"{self._cmd_syntax}:INTERPEightbit")
        self._magnivu = AcquireMagnivu(device, f"{self._cmd_syntax}:MAGnivu")
        self._mode = AcquireMode(device, f"{self._cmd_syntax}:MODe")
        self._numacq = AcquireNumacq(device, f"{self._cmd_syntax}:NUMACq")
        self._numavg = AcquireNumavg(device, f"{self._cmd_syntax}:NUMAVg")
        self._numenv = AcquireNumenv(device, f"{self._cmd_syntax}:NUMEnv")
        self._numframesacquired = AcquireNumframesacquired(
            device, f"{self._cmd_syntax}:NUMFRAMESACQuired"
        )
        self._numsamples = AcquireNumsamples(device, f"{self._cmd_syntax}:NUMSAMples")
        self._samplingmode = AcquireSamplingmode(device, f"{self._cmd_syntax}:SAMPlingmode")
        self._state = AcquireState(device, f"{self._cmd_syntax}:STATE")
        self._stopafter = AcquireStopafter(device, f"{self._cmd_syntax}:STOPAfter")
        self._syncsamples = AcquireSyncsamples(device, f"{self._cmd_syntax}:SYNcsamples")

    @property
    def enhancedenob(self) -> AcquireEnhancedenob:
        """Return the ``ACQuire:ENHANCEDEnob`` command.

        Description:
            - This command sets or queries the state of the enhanced effective number of bits.

        Usage:
            - Using the ``.write(value)`` method will send the ``ACQuire:ENHANCEDEnob value``
              command.

        SCPI Syntax:
            ```
            - ACQuire:ENHANCEDEnob {OFF|AUTO}
            ```

        Info:
            - ``OFF`` turns off enhanced effective number of bits.
            - ``AUTO`` turns enhanced effective number of bits to AUTO.

        Sub-properties:
            - ``.state``: The ``ACQuire:ENHANCEDEnob:STATE`` command.
        """
        return self._enhancedenob

    @property
    def interpeightbit(self) -> AcquireInterpeightbit:
        """Return the ``ACQuire:INTERPEightbit`` command.

        Description:
            - This command sets or queries the interpolation acquisition mode of the instrument.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire:INTERPEightbit?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire:INTERPEightbit?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACQuire:INTERPEightbit value``
              command.

        SCPI Syntax:
            ```
            - ACQuire:INTERPEightbit {AUTO|ON|OFF}
            - ACQuire:INTERPEightbit?
            ```

        Info:
            - ``AUTO`` lets the instrument automatically select the interpolation acquisition mode.
            - ``ON`` turns on the eight bit interpolation mode.
            - ``OFF`` turns off the eight bit interpolation mode.
        """
        return self._interpeightbit

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
    def mode(self) -> AcquireMode:
        """Return the ``ACQuire:MODe`` command.

        Description:
            - This command sets or queries the selected acquisition mode of the instrument. This
              affects all live waveforms. This command is equivalent to selecting
              Horizontal/Acquisition from the Horiz/Acq menu, and then choosing the desired mode
              from the Acquisition Mode group box. ``ACQuire:MODe`` is the desired acquisition mode.
              Waveforms are the displayed data point values taken from acquisition intervals. Each
              acquisition interval represents a time duration set by the horizontal scale (time per
              division). The instrument sampling system always samples at the maximum rate and so an
              acquisition interval can include more than one sample. The acquisition mode (which you
              set using this ``ACQuire:MODe`` command) determines how the final value of the
              acquisition interval is generated from the many data samples.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire:MODe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACQuire:MODe value`` command.

        SCPI Syntax:
            ```
            - ACQuire:MODe {SAMple|PEAKdetect|HIRes|AVErage|WFMDB|ENVelope}
            - ACQuire:MODe?
            ```

        Info:
            - ``SAMple`` specifies that the displayed data point value is the first sampled value
              that is taken during the acquisition interval. In sample mode, all waveform data has 8
              bits of precision. You can request 16 bit data with a CURVE query but the lower-order
              8 bits of data will be zero. SAMple is the default mode.
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
              ``ACQUIRE:NUMENV`` command.
            - ``WFMDB`` (Waveform Database) mode acquires and displays a waveform pixmap. A pixmap
              is the accumulation of one or more acquisitions.
            - ``ENVelope`` specifies envelope mode, where the resulting waveform shows the
              PEAKdetect range of data points from several separate waveform acquisitions. The
              number of waveform acquisitions that go into making up the envelope waveform is set or
              queried using the ``ACQUIRE:NUMENV`` command.

        Sub-properties:
            - ``.actual``: The ``ACQuire:MODe:ACTUal`` command.
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
    def numframesacquired(self) -> AcquireNumframesacquired:
        """Return the ``ACQuire:NUMFRAMESACQuired`` command.

        Description:
            - This query returns the number of FastFrame frames which have been acquired.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire:NUMFRAMESACQuired?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire:NUMFRAMESACQuired?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ACQuire:NUMFRAMESACQuired?
            ```
        """
        return self._numframesacquired

    @property
    def numsamples(self) -> AcquireNumsamples:
        """Return the ``ACQuire:NUMSAMples`` command.

        Description:
            - This command sets or queries the minimum number of acquired samples that make up a
              waveform database (WfmDB) waveform for single sequence mode and Mask Pass/Fail
              Completion Test. This is equivalent to setting the Waveform Database Samples in the
              Acquisition Mode side menu.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire:NUMSAMples?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire:NUMSAMples?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACQuire:NUMSAMples value`` command.

        SCPI Syntax:
            ```
            - ACQuire:NUMSAMples <NR1>
            - ACQuire:NUMSAMples?
            ```

        Info:
            - ``<NR1>`` is the minimum number of acquired samples that make up a waveform database
              (WfmDB) waveform for single sequence mode and Mask Pass/Fail Completion Test. The
              default value is 16,000 samples. The range is 5,000 to 2,147,400,000 samples.
        """
        return self._numsamples

    @property
    def samplingmode(self) -> AcquireSamplingmode:
        """Return the ``ACQuire:SAMPlingmode`` command.

        Description:
            - This command sets or queries the sampling mode.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire:SAMPlingmode?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire:SAMPlingmode?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACQuire:SAMPlingmode value``
              command.

        SCPI Syntax:
            ```
            - ACQuire:SAMPlingmode {RT|ET|IT}
            - ACQuire:SAMPlingmode?
            ```

        Info:
            - ``RT`` sets the sampling mode to real time only.
            - ``ET`` sets the sampling mode to equivalent time allowed (ON in REPET).
            - ``IT`` sets the sampling mode to interpolation allowed (OFF in REPET).
        """
        return self._samplingmode

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

    @property
    def syncsamples(self) -> AcquireSyncsamples:
        """Return the ``ACQuire:SYNcsamples`` command.

        Description:
            - This command sets or queries whether the acquisition process is modified to sync up
              samples to trigger (for example, resample the waveform such that ttoff=0). This
              improves waveform jitter and skew in Average mode because each waveform is aligned to
              the trigger.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire:SYNcsamples?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire:SYNcsamples?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACQuire:SYNcsamples value``
              command.

        SCPI Syntax:
            ```
            - ACQuire:SYNcsamples {ON|OFF}
            - ACQuire:SYNcsamples?
            ```

        Info:
            - ``ON`` sets the acquisition process to be modified to sync up samples to trigger.
            - ``OFF`` sets the system so that no modification of the acquisition process is
              performed.
        """
        return self._syncsamples
