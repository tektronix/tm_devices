"""The rf commands module.

These commands are used in the following models:
MDO3K

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - RF:CLIPPing?
    - RF:DETECTionmethod:MODe {AUTO|MANual}
    - RF:DETECTionmethod:MODe?
    - RF:DETECTionmethod:RF_AVErage {PLUSpeak|MINUSpeak|SAMple|AVErage}
    - RF:DETECTionmethod:RF_AVErage?
    - RF:DETECTionmethod:RF_MAXHold {PLUSpeak|MINUSpeak|SAMple|AVErage}
    - RF:DETECTionmethod:RF_MAXHold?
    - RF:DETECTionmethod:RF_MINHold {PLUSpeak|MINUSpeak|SAMple|AVErage}
    - RF:DETECTionmethod:RF_MINHold?
    - RF:DETECTionmethod:RF_NORMal {PLUSpeak|MINUSpeak|SAMple|AVErage}
    - RF:DETECTionmethod:RF_NORMal?
    - RF:FREQuency <NR3>
    - RF:FREQuency?
    - RF:LABel <QString>
    - RF:LABel?
    - RF:MEASUre:ACPR:ADJACENTPAIRs [1|2|3]
    - RF:MEASUre:ACPR:ADJACENTPAIRs?
    - RF:MEASUre:ACPR:CHANBW <NR3>
    - RF:MEASUre:ACPR:CHANBW?
    - RF:MEASUre:ACPR:CHANSPACing <NR3>
    - RF:MEASUre:ACPR:CHANSPACing?
    - RF:MEASUre:ACPR:LA1DB?
    - RF:MEASUre:ACPR:LA2DB?
    - RF:MEASUre:ACPR:LA3DB?
    - RF:MEASUre:ACPR:POWer?
    - RF:MEASUre:ACPR:UA1DB?
    - RF:MEASUre:ACPR:UA2DB?
    - RF:MEASUre:ACPR:UA3DB?
    - RF:MEASUre:CP:CHANBW <NR3>
    - RF:MEASUre:CP:CHANBW?
    - RF:MEASUre:CP:POWer?
    - RF:MEASUre:OBW:CHANBW <NR3>
    - RF:MEASUre:OBW:CHANBW?
    - RF:MEASUre:OBW:LOWERFreq?
    - RF:MEASUre:OBW:PERCENTdown <NR3>
    - RF:MEASUre:OBW:PERCENTdown?
    - RF:MEASUre:OBW:POWer?
    - RF:MEASUre:OBW:UPPERFreq?
    - RF:MEASUre:TYPe {NONe|CP|ACPR|OBW}
    - RF:MEASUre:TYPe?
    - RF:POSition <NR3>
    - RF:POSition?
    - RF:PRObe:AUTOZero EXECute
    - RF:PRObe:CALibrate {EXECute|INITialize}
    - RF:PRObe:CALibrate:CALIBRATABLe?
    - RF:PRObe:CALibrate:STATE?
    - RF:PRObe:COMMAND <QString>, <QString>
    - RF:PRObe:COMMAND? <QString>
    - RF:PRObe:DEGAUss EXECute
    - RF:PRObe:DEGAUss:STATE?
    - RF:PRObe:FORCEDRange <NR3>
    - RF:PRObe:FORCEDRange?
    - RF:PRObe:GAIN <NR3>
    - RF:PRObe:GAIN?
    - RF:PRObe:ID:SERnumber?
    - RF:PRObe:ID:TYPe?
    - RF:PRObe:PREAmp:MODe <BYPass|AUTO>
    - RF:PRObe:PREAmp:MODe?
    - RF:PRObe:PREAmp:STATus?
    - RF:PRObe:RESistance?
    - RF:PRObe:SIGnal {BYPass|PASS}
    - RF:PRObe:SIGnal?
    - RF:PRObe:UNIts?
    - RF:RBW <NR3>
    - RF:RBW:MODe {AUTO|MANual}
    - RF:RBW:MODe?
    - RF:RBW?
    - RF:REFLevel {<NR3>|AUTO}
    - RF:REFLevel?
    - RF:RF_AMPlitude:LABel <QString>
    - RF:RF_AMPlitude:LABel?
    - RF:RF_AMPlitude:VERTical:POSition <NR3>
    - RF:RF_AMPlitude:VERTical:POSition?
    - RF:RF_AMPlitude:VERTical:SCAle <NR3>
    - RF:RF_AMPlitude:VERTical:SCAle?
    - RF:RF_AVErage:COUNt?
    - RF:RF_AVErage:NUMAVg <NR1>
    - RF:RF_AVErage:NUMAVg?
    - RF:RF_PHASe:REFERence:DEGrees <NR3>
    - RF:RF_PHASe:REFERence:DEGrees?
    - RF:RF_PHASe:WRAP:DEGrees <NR3>
    - RF:RF_PHASe:WRAP:DEGrees?
    - RF:RF_PHASe:WRAP:STATE <Boolean>
    - RF:RF_PHASe:WRAP:STATE?
    - RF:RF_V_TIMe:BANDWidth
    - RF:RF_V_TIMe:BANDWidth?
    - RF:SCAle <NR3>
    - RF:SCAle?
    - RF:SPAN <NR3>
    - RF:SPAN?
    - RF:SPANRbwratio <NR3>
    - RF:SPANRbwratio?
    - RF:SPECTRUMMode {TRIGgered|FREErun}
    - RF:SPECTRUMMode?
    - RF:SPECTRUMTrace {RESET}
    - RF:SPECTRogram {CLEAR}
    - RF:SPECTRogram:NUMSLICEs?
    - RF:SPECTRogram:SLICESELect <NR1>
    - RF:SPECTRogram:SLICESELect?
    - RF:SPECTRogram:SLICETIMe?
    - RF:SPECTRogram:STATE {OFF|ON|0|1}
    - RF:SPECTRogram:STATE?
    - RF:SPECTRogram:TIMe?
    - RF:SQUELCH:STATE {OFF|ON|0|1}
    - RF:SQUELCH:STATE?
    - RF:SQUELCH:THReshold <NR3>
    - RF:SQUELCH:THReshold?
    - RF:STARt <NR3>
    - RF:STARt?
    - RF:STOP <NR3>
    - RF:STOP?
    - RF:UNIts {DBM|DBUW|DBMV|DBUV|DBMA|DBUA}
    - RF:UNIts?
    - RF:WINdow {RECTangular|HAMming|HANning|BLAckmanharris|KAIser|FLATtop}
    - RF:WINdow?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdReadWithArguments, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class RfWindow(SCPICmdWrite, SCPICmdRead):
    """The ``RF:WINdow`` command.

    Description:
        - This command specifies which window will be used for the windowing function, which is only
          used for the three time domain RF traces (RF Amplitude vs. Time, RF Frequency vs. Time and
          RF Phase vs. Time). The windowing function is a Fast Fourier Transform (FFT) technique
          used to minimize the discontinuities between successive frames of an RF time domain
          signal.

    Usage:
        - Using the ``.query()`` method will send the ``RF:WINdow?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:WINdow?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:WINdow value`` command.

    SCPI Syntax:
        ```
        - RF:WINdow {RECTangular|HAMming|HANning|BLAckmanharris|KAIser|FLATtop}
        - RF:WINdow?
        ```

    Info:
        - ``RECTangular`` - window function equivalent to multiplying all gate data by one
          (sometimes known as a Dirichlet window).
        - ``HAMming`` - a high or moderate resolution window based on a cosine series.
        - ``HANning`` - a high or moderate resolution window based on a cosine series.
        - ``BLAckmanharris`` - a low-resolution (high dynamic range) window based on a cosine
          series.
        - ``KAIser`` - a high or moderate resolution window.
        - ``FLATtop`` - a low-resolution (high dynamic range) window.
    """


class RfUnits(SCPICmdWrite, SCPICmdRead):
    """The ``RF:UNIts`` command.

    Description:
        - This command specifies the vertical units to be used in all RF-related absolute
          logarithmic amplitudes.

    Usage:
        - Using the ``.query()`` method will send the ``RF:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:UNIts?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:UNIts value`` command.

    SCPI Syntax:
        ```
        - RF:UNIts {DBM|DBUW|DBMV|DBUV|DBMA|DBUA}
        - RF:UNIts?
        ```

    Info:
        - ``DBM`` - Decibel milliwatts.
        - ``DBUW`` - Decibel microwatts.
        - ``DBMV`` - Decibel millivolts.
        - ``DBUV`` - Decibel microvolts.
        - ``DBMA`` - Decibel milliamperes.
        - ``DBUA`` - Decibel microamperes.
    """


class RfStop(SCPICmdWrite, SCPICmdRead):
    """The ``RF:STOP`` command.

    Description:
        - This command specifies to exclude frequencies above a certain level from use.

    Usage:
        - Using the ``.query()`` method will send the ``RF:STOP?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:STOP?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:STOP value`` command.

    SCPI Syntax:
        ```
        - RF:STOP <NR3>
        - RF:STOP?
        ```

    Info:
        - ``<NR3>`` is a floating point value.
    """


class RfStart(SCPICmdWrite, SCPICmdRead):
    """The ``RF:STARt`` command.

    Description:
        - This command specifies to exclude frequencies below a certain level from use.

    Usage:
        - Using the ``.query()`` method will send the ``RF:STARt?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:STARt?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:STARt value`` command.

    SCPI Syntax:
        ```
        - RF:STARt <NR3>
        - RF:STARt?
        ```

    Info:
        - ``<NR3>`` is a floating point value that represents the Start frequency.
    """


class RfSquelchThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``RF:SQUELCH:THReshold`` command.

    Description:
        - This command specifies the squelch threshold level, in volts, for the RF Frequency vs.
          Time and RF Phase vs. Time traces.

    Usage:
        - Using the ``.query()`` method will send the ``RF:SQUELCH:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:SQUELCH:THReshold?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:SQUELCH:THReshold value`` command.

    SCPI Syntax:
        ```
        - RF:SQUELCH:THReshold <NR3>
        - RF:SQUELCH:THReshold?
        ```

    Info:
        - ``<NR3>`` is a floating point number.
    """


class RfSquelchState(SCPICmdWrite, SCPICmdRead):
    """The ``RF:SQUELCH:STATE`` command.

    Description:
        - This command turns the squelch control on or off for the RF Frequency vs. Time and RF
          Phase vs. Time traces. When squelch is on, only the portions of these traces where the
          amplitude exceeds the squelch threshold are displayed. This prevents the display of Phase
          and/or Frequency for signals that are at or near noise levels. The RF amplitude can be
          observed in the RF Amplitude vs. Time trace.

    Usage:
        - Using the ``.query()`` method will send the ``RF:SQUELCH:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:SQUELCH:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:SQUELCH:STATE value`` command.

    SCPI Syntax:
        ```
        - RF:SQUELCH:STATE {OFF|ON|0|1}
        - RF:SQUELCH:STATE?
        ```
    """


class RfSquelch(SCPICmdRead):
    """The ``RF:SQUELCH`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``RF:SQUELCH?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:SQUELCH?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``RF:SQUELCH:STATE`` command.
        - ``.threshold``: The ``RF:SQUELCH:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = RfSquelchState(device, f"{self._cmd_syntax}:STATE")
        self._threshold = RfSquelchThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def state(self) -> RfSquelchState:
        """Return the ``RF:SQUELCH:STATE`` command.

        Description:
            - This command turns the squelch control on or off for the RF Frequency vs. Time and RF
              Phase vs. Time traces. When squelch is on, only the portions of these traces where the
              amplitude exceeds the squelch threshold are displayed. This prevents the display of
              Phase and/or Frequency for signals that are at or near noise levels. The RF amplitude
              can be observed in the RF Amplitude vs. Time trace.

        Usage:
            - Using the ``.query()`` method will send the ``RF:SQUELCH:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:SQUELCH:STATE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:SQUELCH:STATE value`` command.

        SCPI Syntax:
            ```
            - RF:SQUELCH:STATE {OFF|ON|0|1}
            - RF:SQUELCH:STATE?
            ```
        """
        return self._state

    @property
    def threshold(self) -> RfSquelchThreshold:
        """Return the ``RF:SQUELCH:THReshold`` command.

        Description:
            - This command specifies the squelch threshold level, in volts, for the RF Frequency vs.
              Time and RF Phase vs. Time traces.

        Usage:
            - Using the ``.query()`` method will send the ``RF:SQUELCH:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:SQUELCH:THReshold?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:SQUELCH:THReshold value``
              command.

        SCPI Syntax:
            ```
            - RF:SQUELCH:THReshold <NR3>
            - RF:SQUELCH:THReshold?
            ```

        Info:
            - ``<NR3>`` is a floating point number.
        """
        return self._threshold


class RfSpectrogramTime(SCPICmdRead):
    """The ``RF:SPECTRogram:TIMe`` command.

    Description:
        - Queries the number of seconds in the spectrogram since continuous acquisition started. The
          value returned is always <= 0.

    Usage:
        - Using the ``.query()`` method will send the ``RF:SPECTRogram:TIMe?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:SPECTRogram:TIMe?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - RF:SPECTRogram:TIMe?
        ```
    """


class RfSpectrogramState(SCPICmdWrite, SCPICmdRead):
    """The ``RF:SPECTRogram:STATE`` command.

    Description:
        - This command switches the frequency domain spectrogram display on or off. The spectrogram
          illustrates how frequency and amplitude change over time. It is useful for monitoring
          slowly-changing RF events, and for identifying low amplitude signals too subtle for the
          eye to catch in a regular frequency domain display. The x-axis shows frequency, and the
          y-axis shows time. Amplitude is represented by the color of the trace. Cold colors (blue,
          green) indicate low amplitude, and hot colors (red, yellow) indicate high amplitude. When
          acquisitions are stopped, you can navigate back through each spectrum slice in the
          spectrogram by using the ``RF:SPECTROGRAM:NUMSLICES`` and ``RF:SPECTROGRAM:SLICESELECT``
          commands.

    Usage:
        - Using the ``.query()`` method will send the ``RF:SPECTRogram:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:SPECTRogram:STATE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:SPECTRogram:STATE value`` command.

    SCPI Syntax:
        ```
        - RF:SPECTRogram:STATE {OFF|ON|0|1}
        - RF:SPECTRogram:STATE?
        ```
    """


class RfSpectrogramSlicetime(SCPICmdRead):
    """The ``RF:SPECTRogram:SLICETIMe`` command.

    Description:
        - Returns the time stamp of the selected spectrogram slice (specified using
          ``:RF:SPECTRogram:SLICESELect``). The value represents the number of seconds since
          spectrogram acquisitions were started after the instrument was powered up, or since the
          spectrogram was cleared (see ``RF:SPECTROGRAM``).

    Usage:
        - Using the ``.query()`` method will send the ``RF:SPECTRogram:SLICETIMe?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:SPECTRogram:SLICETIMe?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - RF:SPECTRogram:SLICETIMe?
        ```
    """


class RfSpectrogramSliceselect(SCPICmdWrite, SCPICmdRead):
    """The ``RF:SPECTRogram:SLICESELect`` command.

    Description:
        - This command specifies the spectrogram slice number that is to be displayed. The slice can
          only be selected or changed when acquisitions have been stopped. As soon as acquisitions
          start again, the slice number is reset to 0 (the latest slice). Attempts to select a slice
          number outside of range, or when acquisitions are running, are ignored. The query form
          returns the currently selected spectrogram slice. To use this command, first turn on the
          spectrogram (``RF:SPECTROGRAM:STATE``). Then query the number of slices
          (``RF:SPECTROGRAM:NUMSLICES``). Stop the acquisition when you've reached the number of
          desired slices. Then select the slice to display (``RF:SPECTROGRAM:SLICESELECT``). Each
          slice of the spectrogram corresponds to a single RF acquisition. The FFT samples the
          entire spectrum for the incoming signal (at the rate with which new spectrums are
          acquired). The newest spectrum is on the bottom edge of the spectrogram, and the oldest is
          on the top edge. When the oscilloscope is stopped, you can scroll 'back in time' through
          the spectrogram using the spectrum slice control. When you select a spectrogram slice, it
          is displayed in the bottom window as the RF Normal trace.

    Usage:
        - Using the ``.query()`` method will send the ``RF:SPECTRogram:SLICESELect?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:SPECTRogram:SLICESELect?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:SPECTRogram:SLICESELect value``
          command.

    SCPI Syntax:
        ```
        - RF:SPECTRogram:SLICESELect <NR1>
        - RF:SPECTRogram:SLICESELect?
        ```

    Info:
        - ``<NR1>`` is an integer that specifies the spectrogram slice number that is to be
          displayed.
    """


class RfSpectrogramNumslices(SCPICmdRead):
    """The ``RF:SPECTRogram:NUMSLICEs`` command.

    Description:
        - This query returns the number of spectrogram slices that are currently being rendered. A
          spectrogram slice is a section of the spectrogram representing one interval, or slice, of
          time in the spectrogram record.

    Usage:
        - Using the ``.query()`` method will send the ``RF:SPECTRogram:NUMSLICEs?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:SPECTRogram:NUMSLICEs?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - RF:SPECTRogram:NUMSLICEs?
        ```
    """


class RfSpectrogram(SCPICmdWrite, SCPICmdRead):
    """The ``RF:SPECTRogram`` command.

    Description:
        - Clears the spectrogram.

    Usage:
        - Using the ``.write(value)`` method will send the ``RF:SPECTRogram value`` command.

    SCPI Syntax:
        ```
        - RF:SPECTRogram {CLEAR}
        ```

    Info:
        - ``CLEAR`` clears the spectrogram.

    Properties:
        - ``.numslices``: The ``RF:SPECTRogram:NUMSLICEs`` command.
        - ``.sliceselect``: The ``RF:SPECTRogram:SLICESELect`` command.
        - ``.slicetime``: The ``RF:SPECTRogram:SLICETIMe`` command.
        - ``.state``: The ``RF:SPECTRogram:STATE`` command.
        - ``.time``: The ``RF:SPECTRogram:TIMe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._numslices = RfSpectrogramNumslices(device, f"{self._cmd_syntax}:NUMSLICEs")
        self._sliceselect = RfSpectrogramSliceselect(device, f"{self._cmd_syntax}:SLICESELect")
        self._slicetime = RfSpectrogramSlicetime(device, f"{self._cmd_syntax}:SLICETIMe")
        self._state = RfSpectrogramState(device, f"{self._cmd_syntax}:STATE")
        self._time = RfSpectrogramTime(device, f"{self._cmd_syntax}:TIMe")

    @property
    def numslices(self) -> RfSpectrogramNumslices:
        """Return the ``RF:SPECTRogram:NUMSLICEs`` command.

        Description:
            - This query returns the number of spectrogram slices that are currently being rendered.
              A spectrogram slice is a section of the spectrogram representing one interval, or
              slice, of time in the spectrogram record.

        Usage:
            - Using the ``.query()`` method will send the ``RF:SPECTRogram:NUMSLICEs?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:SPECTRogram:NUMSLICEs?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - RF:SPECTRogram:NUMSLICEs?
            ```
        """
        return self._numslices

    @property
    def sliceselect(self) -> RfSpectrogramSliceselect:
        """Return the ``RF:SPECTRogram:SLICESELect`` command.

        Description:
            - This command specifies the spectrogram slice number that is to be displayed. The slice
              can only be selected or changed when acquisitions have been stopped. As soon as
              acquisitions start again, the slice number is reset to 0 (the latest slice). Attempts
              to select a slice number outside of range, or when acquisitions are running, are
              ignored. The query form returns the currently selected spectrogram slice. To use this
              command, first turn on the spectrogram (``RF:SPECTROGRAM:STATE``). Then query the
              number of slices (``RF:SPECTROGRAM:NUMSLICES``). Stop the acquisition when you've
              reached the number of desired slices. Then select the slice to display
              (``RF:SPECTROGRAM:SLICESELECT``). Each slice of the spectrogram corresponds to a
              single RF acquisition. The FFT samples the entire spectrum for the incoming signal (at
              the rate with which new spectrums are acquired). The newest spectrum is on the bottom
              edge of the spectrogram, and the oldest is on the top edge. When the oscilloscope is
              stopped, you can scroll 'back in time' through the spectrogram using the spectrum
              slice control. When you select a spectrogram slice, it is displayed in the bottom
              window as the RF Normal trace.

        Usage:
            - Using the ``.query()`` method will send the ``RF:SPECTRogram:SLICESELect?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:SPECTRogram:SLICESELect?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:SPECTRogram:SLICESELect value``
              command.

        SCPI Syntax:
            ```
            - RF:SPECTRogram:SLICESELect <NR1>
            - RF:SPECTRogram:SLICESELect?
            ```

        Info:
            - ``<NR1>`` is an integer that specifies the spectrogram slice number that is to be
              displayed.
        """
        return self._sliceselect

    @property
    def slicetime(self) -> RfSpectrogramSlicetime:
        """Return the ``RF:SPECTRogram:SLICETIMe`` command.

        Description:
            - Returns the time stamp of the selected spectrogram slice (specified using
              ``:RF:SPECTRogram:SLICESELect``). The value represents the number of seconds since
              spectrogram acquisitions were started after the instrument was powered up, or since
              the spectrogram was cleared (see ``RF:SPECTROGRAM``).

        Usage:
            - Using the ``.query()`` method will send the ``RF:SPECTRogram:SLICETIMe?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:SPECTRogram:SLICETIMe?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - RF:SPECTRogram:SLICETIMe?
            ```
        """
        return self._slicetime

    @property
    def state(self) -> RfSpectrogramState:
        """Return the ``RF:SPECTRogram:STATE`` command.

        Description:
            - This command switches the frequency domain spectrogram display on or off. The
              spectrogram illustrates how frequency and amplitude change over time. It is useful for
              monitoring slowly-changing RF events, and for identifying low amplitude signals too
              subtle for the eye to catch in a regular frequency domain display. The x-axis shows
              frequency, and the y-axis shows time. Amplitude is represented by the color of the
              trace. Cold colors (blue, green) indicate low amplitude, and hot colors (red, yellow)
              indicate high amplitude. When acquisitions are stopped, you can navigate back through
              each spectrum slice in the spectrogram by using the ``RF:SPECTROGRAM:NUMSLICES`` and
              ``RF:SPECTROGRAM:SLICESELECT`` commands.

        Usage:
            - Using the ``.query()`` method will send the ``RF:SPECTRogram:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:SPECTRogram:STATE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:SPECTRogram:STATE value``
              command.

        SCPI Syntax:
            ```
            - RF:SPECTRogram:STATE {OFF|ON|0|1}
            - RF:SPECTRogram:STATE?
            ```
        """
        return self._state

    @property
    def time(self) -> RfSpectrogramTime:
        """Return the ``RF:SPECTRogram:TIMe`` command.

        Description:
            - Queries the number of seconds in the spectrogram since continuous acquisition started.
              The value returned is always <= 0.

        Usage:
            - Using the ``.query()`` method will send the ``RF:SPECTRogram:TIMe?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:SPECTRogram:TIMe?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - RF:SPECTRogram:TIMe?
            ```
        """
        return self._time


class RfSpectrumtrace(SCPICmdWrite):
    """The ``RF:SPECTRUMTrace`` command.

    Description:
        - Resets the spectrum traces, ``RF_MINHold``, ``RF_MAXHold`` and ``RF_AVErage``.

    Usage:
        - Using the ``.write(value)`` method will send the ``RF:SPECTRUMTrace value`` command.

    SCPI Syntax:
        ```
        - RF:SPECTRUMTrace {RESET}
        ```
    """


class RfSpectrummode(SCPICmdWrite, SCPICmdRead):
    """The ``RF:SPECTRUMMode`` command.

    Description:
        - When only the frequency domain waveforms are displayed (no time domain waveforms), you can
          choose whether the MDO4000/B/C should use Triggered mode or Free Run mode. (3 Series MDO
          only uses Free Run mode.) When Free Run mode is selected, the oscilloscope generates RF
          acquisitions as fast as possible. The default is FREErun.

    Usage:
        - Using the ``.query()`` method will send the ``RF:SPECTRUMMode?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:SPECTRUMMode?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:SPECTRUMMode value`` command.

    SCPI Syntax:
        ```
        - RF:SPECTRUMMode {TRIGgered|FREErun}
        - RF:SPECTRUMMode?
        ```

    Info:
        - ``TRIGgered`` ties RF acquisitions to the scope's unified triggering system for all
          channels.
        - ``FREErun`` acquires RF data as often as processing allows, without waiting for trigger
          events.
    """


class RfSpanrbwratio(SCPICmdWrite, SCPICmdRead):
    """The ``RF:SPANRbwratio`` command.

    Description:
        - This command specifies the ratio of the span to the resolution bandwidth (RBW) that will
          be used when the RBW Mode is set to AUTO. (In order to set the RBW Mode to AUTO, use the
          command ``RF:RBW:MODE``.) The span is the width of the frequency domain trace in Hz, which
          is equal to the stop frequency minus the start frequency. The RBW is the width of the
          narrowest measurable band of frequencies in a frequency domain trace. The default RBW
          ratio is a factor of 1000.

    Usage:
        - Using the ``.query()`` method will send the ``RF:SPANRbwratio?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:SPANRbwratio?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:SPANRbwratio value`` command.

    SCPI Syntax:
        ```
        - RF:SPANRbwratio <NR3>
        - RF:SPANRbwratio?
        ```

    Info:
        - ``<NR3>`` is a floating point number.
    """


class RfSpan(SCPICmdWrite, SCPICmdRead):
    """The ``RF:SPAN`` command.

    Description:
        - This command specifies the span setting. The span is the range of frequencies that can be
          observed around the center frequency. This is the width of the frequency domain trace,
          which is equal to the stop frequency minus the start frequency. The maximum span varies
          according to the oscilloscope model. The maximum span for the 3 Series MDO matches the
          analog bandwidth rating; however, if the option 3-SA3 is installed, then the maximum span
          is 3 GHz.

    Usage:
        - Using the ``.query()`` method will send the ``RF:SPAN?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:SPAN?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:SPAN value`` command.

    SCPI Syntax:
        ```
        - RF:SPAN <NR3>
        - RF:SPAN?
        ```

    Info:
        - ``<NR3>`` is a floating point number.
    """


class RfScale(SCPICmdWrite, SCPICmdRead):
    """The ``RF:SCAle`` command.

    Description:
        - This command specifies the overall vertical scale setting of the frequency domain window.
          The lower limit is 0.1 dB/division. The upper limit is 100dB/division. The vertical scale
          is adjustable in a 1-2-5 sequence.

    Usage:
        - Using the ``.query()`` method will send the ``RF:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:SCAle?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:SCAle value`` command.

    SCPI Syntax:
        ```
        - RF:SCAle <NR3>
        - RF:SCAle?
        ```

    Info:
        - ``<NR3>`` is a floating point number.
    """


class RfRfVTimeBandwidth(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``RF:RF_V_TIMe:BANDWidth`` command.

    Description:
        - Sets or returns the RF versus time bandwidth as an NR3 value in Hz. This is the same as
          the 'RF v T BW' readout, which is displayed when at least one of the RF Versus Time traces
          is on.

    Usage:
        - Using the ``.query()`` method will send the ``RF:RF_V_TIMe:BANDWidth?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:RF_V_TIMe:BANDWidth?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``RF:RF_V_TIMe:BANDWidth`` command.

    SCPI Syntax:
        ```
        - RF:RF_V_TIMe:BANDWidth
        - RF:RF_V_TIMe:BANDWidth?
        ```
    """


class RfRfVTime(SCPICmdRead):
    """The ``RF:RF_V_TIMe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``RF:RF_V_TIMe?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:RF_V_TIMe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bandwidth``: The ``RF:RF_V_TIMe:BANDWidth`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bandwidth = RfRfVTimeBandwidth(device, f"{self._cmd_syntax}:BANDWidth")

    @property
    def bandwidth(self) -> RfRfVTimeBandwidth:
        """Return the ``RF:RF_V_TIMe:BANDWidth`` command.

        Description:
            - Sets or returns the RF versus time bandwidth as an NR3 value in Hz. This is the same
              as the 'RF v T BW' readout, which is displayed when at least one of the RF Versus Time
              traces is on.

        Usage:
            - Using the ``.query()`` method will send the ``RF:RF_V_TIMe:BANDWidth?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:RF_V_TIMe:BANDWidth?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``RF:RF_V_TIMe:BANDWidth`` command.

        SCPI Syntax:
            ```
            - RF:RF_V_TIMe:BANDWidth
            - RF:RF_V_TIMe:BANDWidth?
            ```
        """
        return self._bandwidth


class RfRfPhaseWrapState(SCPICmdWrite, SCPICmdRead):
    """The ``RF:RF_PHASe:WRAP:STATE`` command.

    Description:
        - Sets or returns the state of the phase wrap control for the ``RF_PHASE`` time domain
          trace. The default is 1, meaning that wrapping the ``RF_PHASe`` time domain trace is
          enabled.

    Usage:
        - Using the ``.query()`` method will send the ``RF:RF_PHASe:WRAP:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:RF_PHASe:WRAP:STATE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:RF_PHASe:WRAP:STATE value`` command.

    SCPI Syntax:
        ```
        - RF:RF_PHASe:WRAP:STATE <Boolean>
        - RF:RF_PHASe:WRAP:STATE?
        ```
    """


class RfRfPhaseWrapDegrees(SCPICmdWrite, SCPICmdRead):
    """The ``RF:RF_PHASe:WRAP:DEGrees`` command.

    Description:
        - Sets or returns the number of degrees to wrap the ``RF_PHASe`` time domain trace. The
          value can range from -180.0 to 54,000.0 degrees. The default is 360.0 degrees and the
          resolution is 180.0 degrees.

    Usage:
        - Using the ``.query()`` method will send the ``RF:RF_PHASe:WRAP:DEGrees?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:RF_PHASe:WRAP:DEGrees?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:RF_PHASe:WRAP:DEGrees value``
          command.

    SCPI Syntax:
        ```
        - RF:RF_PHASe:WRAP:DEGrees <NR3>
        - RF:RF_PHASe:WRAP:DEGrees?
        ```
    """


class RfRfPhaseWrap(SCPICmdRead):
    """The ``RF:RF_PHASe:WRAP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``RF:RF_PHASe:WRAP?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:RF_PHASe:WRAP?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.degrees``: The ``RF:RF_PHASe:WRAP:DEGrees`` command.
        - ``.state``: The ``RF:RF_PHASe:WRAP:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._degrees = RfRfPhaseWrapDegrees(device, f"{self._cmd_syntax}:DEGrees")
        self._state = RfRfPhaseWrapState(device, f"{self._cmd_syntax}:STATE")

    @property
    def degrees(self) -> RfRfPhaseWrapDegrees:
        """Return the ``RF:RF_PHASe:WRAP:DEGrees`` command.

        Description:
            - Sets or returns the number of degrees to wrap the ``RF_PHASe`` time domain trace. The
              value can range from -180.0 to 54,000.0 degrees. The default is 360.0 degrees and the
              resolution is 180.0 degrees.

        Usage:
            - Using the ``.query()`` method will send the ``RF:RF_PHASe:WRAP:DEGrees?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:RF_PHASe:WRAP:DEGrees?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:RF_PHASe:WRAP:DEGrees value``
              command.

        SCPI Syntax:
            ```
            - RF:RF_PHASe:WRAP:DEGrees <NR3>
            - RF:RF_PHASe:WRAP:DEGrees?
            ```
        """
        return self._degrees

    @property
    def state(self) -> RfRfPhaseWrapState:
        """Return the ``RF:RF_PHASe:WRAP:STATE`` command.

        Description:
            - Sets or returns the state of the phase wrap control for the ``RF_PHASE`` time domain
              trace. The default is 1, meaning that wrapping the ``RF_PHASe`` time domain trace is
              enabled.

        Usage:
            - Using the ``.query()`` method will send the ``RF:RF_PHASe:WRAP:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:RF_PHASe:WRAP:STATE?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:RF_PHASe:WRAP:STATE value``
              command.

        SCPI Syntax:
            ```
            - RF:RF_PHASe:WRAP:STATE <Boolean>
            - RF:RF_PHASe:WRAP:STATE?
            ```
        """
        return self._state


class RfRfPhaseReferenceDegrees(SCPICmdWrite, SCPICmdRead):
    """The ``RF:RF_PHASe:REFERence:DEGrees`` command.

    Description:
        - This command sets or returns the phase, in degrees, at the trigger point for the
          ``RF_PHASe`` time domain trace. The value can range from -180 to +180 degrees. The default
          is 0.0 degrees and the resolution is 1.0 degrees.

    Usage:
        - Using the ``.query()`` method will send the ``RF:RF_PHASe:REFERence:DEGrees?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:RF_PHASe:REFERence:DEGrees?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:RF_PHASe:REFERence:DEGrees value``
          command.

    SCPI Syntax:
        ```
        - RF:RF_PHASe:REFERence:DEGrees <NR3>
        - RF:RF_PHASe:REFERence:DEGrees?
        ```
    """


class RfRfPhaseReference(SCPICmdRead):
    """The ``RF:RF_PHASe:REFERence`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``RF:RF_PHASe:REFERence?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:RF_PHASe:REFERence?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.degrees``: The ``RF:RF_PHASe:REFERence:DEGrees`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._degrees = RfRfPhaseReferenceDegrees(device, f"{self._cmd_syntax}:DEGrees")

    @property
    def degrees(self) -> RfRfPhaseReferenceDegrees:
        """Return the ``RF:RF_PHASe:REFERence:DEGrees`` command.

        Description:
            - This command sets or returns the phase, in degrees, at the trigger point for the
              ``RF_PHASe`` time domain trace. The value can range from -180 to +180 degrees. The
              default is 0.0 degrees and the resolution is 1.0 degrees.

        Usage:
            - Using the ``.query()`` method will send the ``RF:RF_PHASe:REFERence:DEGrees?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:RF_PHASe:REFERence:DEGrees?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``RF:RF_PHASe:REFERence:DEGrees value`` command.

        SCPI Syntax:
            ```
            - RF:RF_PHASe:REFERence:DEGrees <NR3>
            - RF:RF_PHASe:REFERence:DEGrees?
            ```
        """
        return self._degrees


class RfRfPhase(SCPICmdRead):
    """The ``RF:RF_PHASe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``RF:RF_PHASe?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:RF_PHASe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.reference``: The ``RF:RF_PHASe:REFERence`` command tree.
        - ``.wrap``: The ``RF:RF_PHASe:WRAP`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._reference = RfRfPhaseReference(device, f"{self._cmd_syntax}:REFERence")
        self._wrap = RfRfPhaseWrap(device, f"{self._cmd_syntax}:WRAP")

    @property
    def reference(self) -> RfRfPhaseReference:
        """Return the ``RF:RF_PHASe:REFERence`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``RF:RF_PHASe:REFERence?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:RF_PHASe:REFERence?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.degrees``: The ``RF:RF_PHASe:REFERence:DEGrees`` command.
        """
        return self._reference

    @property
    def wrap(self) -> RfRfPhaseWrap:
        """Return the ``RF:RF_PHASe:WRAP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``RF:RF_PHASe:WRAP?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:RF_PHASe:WRAP?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.degrees``: The ``RF:RF_PHASe:WRAP:DEGrees`` command.
            - ``.state``: The ``RF:RF_PHASe:WRAP:STATE`` command.
        """
        return self._wrap


class RfRfAverageNumavg(SCPICmdWrite, SCPICmdRead):
    """The ``RF:RF_AVErage:NUMAVg`` command.

    Description:
        - This command specifies the number of acquisitions to be used when creating the RF Average
          frequency domain trace, which displays the average of values from multiple acquisitions at
          each trace point. The range is 2 - 512, in exponential increments.

    Usage:
        - Using the ``.query()`` method will send the ``RF:RF_AVErage:NUMAVg?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:RF_AVErage:NUMAVg?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:RF_AVErage:NUMAVg value`` command.

    SCPI Syntax:
        ```
        - RF:RF_AVErage:NUMAVg <NR1>
        - RF:RF_AVErage:NUMAVg?
        ```

    Info:
        - ``<NR1>`` is an integer.
    """


class RfRfAverageCount(SCPICmdRead):
    """The ``RF:RF_AVErage:COUNt`` command.

    Description:
        - This query returns the number of RF traces that have been accumulated to create the RF
          Average frequency domain trace.

    Usage:
        - Using the ``.query()`` method will send the ``RF:RF_AVErage:COUNt?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:RF_AVErage:COUNt?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - RF:RF_AVErage:COUNt?
        ```
    """


class RfRfAverage(SCPICmdRead):
    """The ``RF:RF_AVErage`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``RF:RF_AVErage?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:RF_AVErage?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.count``: The ``RF:RF_AVErage:COUNt`` command.
        - ``.numavg``: The ``RF:RF_AVErage:NUMAVg`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._count = RfRfAverageCount(device, f"{self._cmd_syntax}:COUNt")
        self._numavg = RfRfAverageNumavg(device, f"{self._cmd_syntax}:NUMAVg")

    @property
    def count(self) -> RfRfAverageCount:
        """Return the ``RF:RF_AVErage:COUNt`` command.

        Description:
            - This query returns the number of RF traces that have been accumulated to create the RF
              Average frequency domain trace.

        Usage:
            - Using the ``.query()`` method will send the ``RF:RF_AVErage:COUNt?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:RF_AVErage:COUNt?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - RF:RF_AVErage:COUNt?
            ```
        """
        return self._count

    @property
    def numavg(self) -> RfRfAverageNumavg:
        """Return the ``RF:RF_AVErage:NUMAVg`` command.

        Description:
            - This command specifies the number of acquisitions to be used when creating the RF
              Average frequency domain trace, which displays the average of values from multiple
              acquisitions at each trace point. The range is 2 - 512, in exponential increments.

        Usage:
            - Using the ``.query()`` method will send the ``RF:RF_AVErage:NUMAVg?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:RF_AVErage:NUMAVg?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:RF_AVErage:NUMAVg value``
              command.

        SCPI Syntax:
            ```
            - RF:RF_AVErage:NUMAVg <NR1>
            - RF:RF_AVErage:NUMAVg?
            ```

        Info:
            - ``<NR1>`` is an integer.
        """
        return self._numavg


class RfRfAmplitudeVerticalScale(SCPICmdWrite, SCPICmdRead):
    """The ``RF:RF_AMPlitude:VERTical:SCAle`` command.

    Description:
        - This command specifies the vertical scale for the RF Amplitude vs. Time trace. For a
          signal with constant amplitude, increasing the scale causes the waveform to be displayed
          smaller. Decreasing the scale causes the waveform to be displayed larger.

    Usage:
        - Using the ``.query()`` method will send the ``RF:RF_AMPlitude:VERTical:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:RF_AMPlitude:VERTical:SCAle?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:RF_AMPlitude:VERTical:SCAle value``
          command.

    SCPI Syntax:
        ```
        - RF:RF_AMPlitude:VERTical:SCAle <NR3>
        - RF:RF_AMPlitude:VERTical:SCAle?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the vertical scale.
    """


class RfRfAmplitudeVerticalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``RF:RF_AMPlitude:VERTical:POSition`` command.

    Description:
        - This command specifies the vertical position of the RF Amplitude vs. Time trace. The
          position value determines the vertical graticule location at which the trace is displayed.
          Increasing the position value of a waveform causes the waveform to move up. Decreasing the
          position value causes the waveform to move down. The minimum is -50 divisions and the
          maximum is 50 divisions with a resolution of 0.02 divisions.

    Usage:
        - Using the ``.query()`` method will send the ``RF:RF_AMPlitude:VERTical:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:RF_AMPlitude:VERTical:POSition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``RF:RF_AMPlitude:VERTical:POSition value`` command.

    SCPI Syntax:
        ```
        - RF:RF_AMPlitude:VERTical:POSition <NR3>
        - RF:RF_AMPlitude:VERTical:POSition?
        ```

    Info:
        - ``<NR3>`` is a floating point number.
    """


class RfRfAmplitudeVertical(SCPICmdRead):
    """The ``RF:RF_AMPlitude:VERTical`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``RF:RF_AMPlitude:VERTical?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:RF_AMPlitude:VERTical?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``RF:RF_AMPlitude:VERTical:POSition`` command.
        - ``.scale``: The ``RF:RF_AMPlitude:VERTical:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = RfRfAmplitudeVerticalPosition(device, f"{self._cmd_syntax}:POSition")
        self._scale = RfRfAmplitudeVerticalScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def position(self) -> RfRfAmplitudeVerticalPosition:
        """Return the ``RF:RF_AMPlitude:VERTical:POSition`` command.

        Description:
            - This command specifies the vertical position of the RF Amplitude vs. Time trace. The
              position value determines the vertical graticule location at which the trace is
              displayed. Increasing the position value of a waveform causes the waveform to move up.
              Decreasing the position value causes the waveform to move down. The minimum is -50
              divisions and the maximum is 50 divisions with a resolution of 0.02 divisions.

        Usage:
            - Using the ``.query()`` method will send the ``RF:RF_AMPlitude:VERTical:POSition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``RF:RF_AMPlitude:VERTical:POSition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``RF:RF_AMPlitude:VERTical:POSition value`` command.

        SCPI Syntax:
            ```
            - RF:RF_AMPlitude:VERTical:POSition <NR3>
            - RF:RF_AMPlitude:VERTical:POSition?
            ```

        Info:
            - ``<NR3>`` is a floating point number.
        """
        return self._position

    @property
    def scale(self) -> RfRfAmplitudeVerticalScale:
        """Return the ``RF:RF_AMPlitude:VERTical:SCAle`` command.

        Description:
            - This command specifies the vertical scale for the RF Amplitude vs. Time trace. For a
              signal with constant amplitude, increasing the scale causes the waveform to be
              displayed smaller. Decreasing the scale causes the waveform to be displayed larger.

        Usage:
            - Using the ``.query()`` method will send the ``RF:RF_AMPlitude:VERTical:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:RF_AMPlitude:VERTical:SCAle?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``RF:RF_AMPlitude:VERTical:SCAle value`` command.

        SCPI Syntax:
            ```
            - RF:RF_AMPlitude:VERTical:SCAle <NR3>
            - RF:RF_AMPlitude:VERTical:SCAle?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the vertical scale.
        """
        return self._scale


class RfRfAmplitudeLabel(SCPICmdWrite, SCPICmdRead):
    """The ``RF:RF_AMPlitude:LABel`` command.

    Description:
        - This command specifies the label for the RF Amplitude vs. Time trace.

    Usage:
        - Using the ``.query()`` method will send the ``RF:RF_AMPlitude:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:RF_AMPlitude:LABel?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:RF_AMPlitude:LABel value`` command.

    SCPI Syntax:
        ```
        - RF:RF_AMPlitude:LABel <QString>
        - RF:RF_AMPlitude:LABel?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class RfRfAmplitude(SCPICmdRead):
    """The ``RF:RF_AMPlitude`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``RF:RF_AMPlitude?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:RF_AMPlitude?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.label``: The ``RF:RF_AMPlitude:LABel`` command.
        - ``.vertical``: The ``RF:RF_AMPlitude:VERTical`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._label = RfRfAmplitudeLabel(device, f"{self._cmd_syntax}:LABel")
        self._vertical = RfRfAmplitudeVertical(device, f"{self._cmd_syntax}:VERTical")

    @property
    def label(self) -> RfRfAmplitudeLabel:
        """Return the ``RF:RF_AMPlitude:LABel`` command.

        Description:
            - This command specifies the label for the RF Amplitude vs. Time trace.

        Usage:
            - Using the ``.query()`` method will send the ``RF:RF_AMPlitude:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:RF_AMPlitude:LABel?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:RF_AMPlitude:LABel value``
              command.

        SCPI Syntax:
            ```
            - RF:RF_AMPlitude:LABel <QString>
            - RF:RF_AMPlitude:LABel?
            ```
        """
        return self._label

    @property
    def vertical(self) -> RfRfAmplitudeVertical:
        """Return the ``RF:RF_AMPlitude:VERTical`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``RF:RF_AMPlitude:VERTical?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:RF_AMPlitude:VERTical?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``RF:RF_AMPlitude:VERTical:POSition`` command.
            - ``.scale``: The ``RF:RF_AMPlitude:VERTical:SCAle`` command.
        """
        return self._vertical


class RfReflevel(SCPICmdWrite, SCPICmdRead):
    """The ``RF:REFLevel`` command.

    Description:
        - This command sets the Reference Level of the RF input. The Reference Level can either be
          specified as a numeric floating point value, or set automatically.

    Usage:
        - Using the ``.query()`` method will send the ``RF:REFLevel?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:REFLevel?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:REFLevel value`` command.

    SCPI Syntax:
        ```
        - RF:REFLevel {<NR3>|AUTO}
        - RF:REFLevel?
        ```

    Info:
        - ``<NR3>`` is a floating point number.
        - ``AUTO`` directs the oscilloscope to automatically calculate and set the Reference Level.
          This is a one-time calculation based on the content of the RF input signal. It is not a
          'mode'.
    """


class RfRbwMode(SCPICmdWrite, SCPICmdRead):
    """The ``RF:RBW:MODe`` command.

    Description:
        - This command specifies the resolution bandwidth (RBW) mode, either automatic or manual.

    Usage:
        - Using the ``.query()`` method will send the ``RF:RBW:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:RBW:MODe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:RBW:MODe value`` command.

    SCPI Syntax:
        ```
        - RF:RBW:MODe {AUTO|MANual}
        - RF:RBW:MODe?
        ```

    Info:
        - ``AUTO`` sets the resolution bandwidth automatically as the span is changed. The default
          behavior is ``1000:1``, but you can set it to other values in a 1-2-5 sequence (e.g.
          10000, 20000, 50000). To specify the RBW ratio that will be used when the mode is set to
          automatic, use the command ``RF:SPANRBWRATIO``.
        - ``MANual`` allows you to set the resolution bandwidth, independently from the span, using
          the command ``RF:RBW``.
    """


class RfRbw(SCPICmdWrite, SCPICmdRead):
    """The ``RF:RBW`` command.

    Description:
        - This command specifies the resolution bandwidth (RBW) when the RBW mode has been set to
          MANUAL (using the command ``RF:RBW:MODE``). The resolution bandwidth is the width of the
          narrowest measurable band of frequencies in a frequency domain trace. The RBW is
          adjustable down to 20Hz. By default, the RBW tracks the span value in a ``1000:1`` ratio.
          The RBW determines the level to which the oscilloscope can resolve individual frequencies
          in the frequency domain. For example, if the input signal contains two carriers separated
          by 1 kHz, you will not be able to discriminate between them unless the RBW is less than 1
          kHz.

    Usage:
        - Using the ``.query()`` method will send the ``RF:RBW?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:RBW?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:RBW value`` command.

    SCPI Syntax:
        ```
        - RF:RBW <NR3>
        - RF:RBW?
        ```

    Info:
        - ``<NR3>`` is a floating point number that represents the width of the narrowest measurable
          band of frequencies in a frequency domain trace.

    Properties:
        - ``.mode``: The ``RF:RBW:MODe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = RfRbwMode(device, f"{self._cmd_syntax}:MODe")

    @property
    def mode(self) -> RfRbwMode:
        """Return the ``RF:RBW:MODe`` command.

        Description:
            - This command specifies the resolution bandwidth (RBW) mode, either automatic or
              manual.

        Usage:
            - Using the ``.query()`` method will send the ``RF:RBW:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:RBW:MODe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:RBW:MODe value`` command.

        SCPI Syntax:
            ```
            - RF:RBW:MODe {AUTO|MANual}
            - RF:RBW:MODe?
            ```

        Info:
            - ``AUTO`` sets the resolution bandwidth automatically as the span is changed. The
              default behavior is ``1000:1``, but you can set it to other values in a 1-2-5 sequence
              (e.g. 10000, 20000, 50000). To specify the RBW ratio that will be used when the mode
              is set to automatic, use the command ``RF:SPANRBWRATIO``.
            - ``MANual`` allows you to set the resolution bandwidth, independently from the span,
              using the command ``RF:RBW``.
        """
        return self._mode


class RfProbeUnits(SCPICmdRead):
    """The ``RF:PRObe:UNIts`` command.

    Description:
        - This query returns a quoted string that describes the units of measure for the probe
          attached to the RF input.

    Usage:
        - Using the ``.query()`` method will send the ``RF:PRObe:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:PRObe:UNIts?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - RF:PRObe:UNIts?
        ```
    """


class RfProbeSignal(SCPICmdWrite, SCPICmdRead):
    """The ``RF:PRObe:SIGnal`` command.

    Description:
        - This command specifies the input bypass setting of a TekVPI probe attached to the RF
          input. The probe must support input bypass (for example, TCP0001).

    Usage:
        - Using the ``.query()`` method will send the ``RF:PRObe:SIGnal?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:PRObe:SIGnal?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:PRObe:SIGnal value`` command.

    SCPI Syntax:
        ```
        - RF:PRObe:SIGnal {BYPass|PASS}
        - RF:PRObe:SIGnal?
        ```

    Info:
        - ``BYPass`` sets the probe to Bypass mode.
        - ``PASS`` sets the probe to Pass mode.
    """


class RfProbeResistance(SCPICmdRead):
    """The ``RF:PRObe:RESistance`` command.

    Description:
        - This query returns the input resistance of the probe attached to the RF input, if the
          probe supports it (otherwise, it returns 0.0). The RF input is 50 Ω impedance.

    Usage:
        - Using the ``.query()`` method will send the ``RF:PRObe:RESistance?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:PRObe:RESistance?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - RF:PRObe:RESistance?
        ```
    """


class RfProbePreampStatus(SCPICmdRead):
    """The ``RF:PRObe:PREAmp:STATus`` command.

    Description:
        - Returns the actual status of the RF pre-amp connected to the RF input. The returned status
          enumerations are: NONe - no pre-amp is connected. ON - the pre-amp is connected and is in
          the amplification (non-bypassed) state. BYPass - the pre-amp is connected but is in the
          bypassed state because the mode is set to BYPass, or the mode is set to AUTO and the RF
          reference level is at or above the RF reference level threshold. You can set the mode for
          the pre-amp (either BYPass or AUTO ) using the command ``RF:PROBE:PREAMP:MODE``.

    Usage:
        - Using the ``.query()`` method will send the ``RF:PRObe:PREAmp:STATus?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:PRObe:PREAmp:STATus?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - RF:PRObe:PREAmp:STATus?
        ```
    """


class RfProbePreampMode(SCPICmdWrite, SCPICmdRead):
    """The ``RF:PRObe:PREAmp:MODe`` command.

    Description:
        - Sets or returns the user-selected mode for an RF pre-amp connected to the RF input -
          either BYPass or AUTO. Note that the actual status of the pre-amp (either NONE, ON or
          BYPass ) is determined by the selected mode along with the RF reference level. You can
          query the status of the pre-amp using the command ``RF:PROBE:PREAMP:STATUS``

    Usage:
        - Using the ``.query()`` method will send the ``RF:PRObe:PREAmp:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:PRObe:PREAmp:MODe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:PRObe:PREAmp:MODe value`` command.

    SCPI Syntax:
        ```
        - RF:PRObe:PREAmp:MODe <BYPass|AUTO>
        - RF:PRObe:PREAmp:MODe?
        ```

    Info:
        - ``BYPass`` means the pre-amp will not amplify the signal. When the mode is set to BYPass,
          the pre-amp amplification is always off, regardless of the RF reference level.
        - ``AUTO`` means the pre-amp will turn its amplification on or off based on the RF reference
          level. When the MODe is set to AUTO and the RF reference level is below the RF reference
          level threshold, then the pre-amp amplification is automatically turned on, and the STATus
          is set to ON. When the RF reference level is at or above the RF reference level threshold,
          then the pre-amp amplification is automatically turned off, and the STATus is set to
          BYPass.
    """


class RfProbePreamp(SCPICmdRead):
    """The ``RF:PRObe:PREAmp`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``RF:PRObe:PREAmp?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:PRObe:PREAmp?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.mode``: The ``RF:PRObe:PREAmp:MODe`` command.
        - ``.status``: The ``RF:PRObe:PREAmp:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = RfProbePreampMode(device, f"{self._cmd_syntax}:MODe")
        self._status = RfProbePreampStatus(device, f"{self._cmd_syntax}:STATus")

    @property
    def mode(self) -> RfProbePreampMode:
        """Return the ``RF:PRObe:PREAmp:MODe`` command.

        Description:
            - Sets or returns the user-selected mode for an RF pre-amp connected to the RF input -
              either BYPass or AUTO. Note that the actual status of the pre-amp (either NONE, ON or
              BYPass ) is determined by the selected mode along with the RF reference level. You can
              query the status of the pre-amp using the command ``RF:PROBE:PREAMP:STATUS``

        Usage:
            - Using the ``.query()`` method will send the ``RF:PRObe:PREAmp:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:PRObe:PREAmp:MODe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:PRObe:PREAmp:MODe value``
              command.

        SCPI Syntax:
            ```
            - RF:PRObe:PREAmp:MODe <BYPass|AUTO>
            - RF:PRObe:PREAmp:MODe?
            ```

        Info:
            - ``BYPass`` means the pre-amp will not amplify the signal. When the mode is set to
              BYPass, the pre-amp amplification is always off, regardless of the RF reference level.
            - ``AUTO`` means the pre-amp will turn its amplification on or off based on the RF
              reference level. When the MODe is set to AUTO and the RF reference level is below the
              RF reference level threshold, then the pre-amp amplification is automatically turned
              on, and the STATus is set to ON. When the RF reference level is at or above the RF
              reference level threshold, then the pre-amp amplification is automatically turned off,
              and the STATus is set to BYPass.
        """
        return self._mode

    @property
    def status(self) -> RfProbePreampStatus:
        """Return the ``RF:PRObe:PREAmp:STATus`` command.

        Description:
            - Returns the actual status of the RF pre-amp connected to the RF input. The returned
              status enumerations are: NONe - no pre-amp is connected. ON - the pre-amp is connected
              and is in the amplification (non-bypassed) state. BYPass - the pre-amp is connected
              but is in the bypassed state because the mode is set to BYPass, or the mode is set to
              AUTO and the RF reference level is at or above the RF reference level threshold. You
              can set the mode for the pre-amp (either BYPass or AUTO ) using the command
              ``RF:PROBE:PREAMP:MODE``.

        Usage:
            - Using the ``.query()`` method will send the ``RF:PRObe:PREAmp:STATus?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:PRObe:PREAmp:STATus?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - RF:PRObe:PREAmp:STATus?
            ```
        """
        return self._status


class RfProbeIdType(SCPICmdRead):
    r"""The ``RF:PRObe:ID:TYPe`` command.

    Description:
        - This query returns the type of probe attached to the RF input. Level 2 (or higher) probes
          supply their exact product nomenclature; for Level 0 or 1 probes, a generic \* 'No Probe
          Detected' message is returned.

    Usage:
        - Using the ``.query()`` method will send the ``RF:PRObe:ID:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:PRObe:ID:TYPe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - RF:PRObe:ID:TYPe?
        ```
    """


class RfProbeIdSernumber(SCPICmdRead):
    """The ``RF:PRObe:ID:SERnumber`` command.

    Description:
        - This query returns the serial number of the probe attached to the RF input.

    Usage:
        - Using the ``.query()`` method will send the ``RF:PRObe:ID:SERnumber?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:PRObe:ID:SERnumber?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - RF:PRObe:ID:SERnumber?
        ```
    """


class RfProbeId(SCPICmdRead):
    """The ``RF:PRObe:ID`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``RF:PRObe:ID?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:PRObe:ID?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.sernumber``: The ``RF:PRObe:ID:SERnumber`` command.
        - ``.type``: The ``RF:PRObe:ID:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._sernumber = RfProbeIdSernumber(device, f"{self._cmd_syntax}:SERnumber")
        self._type = RfProbeIdType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def sernumber(self) -> RfProbeIdSernumber:
        """Return the ``RF:PRObe:ID:SERnumber`` command.

        Description:
            - This query returns the serial number of the probe attached to the RF input.

        Usage:
            - Using the ``.query()`` method will send the ``RF:PRObe:ID:SERnumber?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:PRObe:ID:SERnumber?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - RF:PRObe:ID:SERnumber?
            ```
        """
        return self._sernumber

    @property
    def type(self) -> RfProbeIdType:
        r"""Return the ``RF:PRObe:ID:TYPe`` command.

        Description:
            - This query returns the type of probe attached to the RF input. Level 2 (or higher)
              probes supply their exact product nomenclature; for Level 0 or 1 probes, a generic \*
              'No Probe Detected' message is returned.

        Usage:
            - Using the ``.query()`` method will send the ``RF:PRObe:ID:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:PRObe:ID:TYPe?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - RF:PRObe:ID:TYPe?
            ```
        """
        return self._type


class RfProbeGain(SCPICmdWrite, SCPICmdRead):
    """The ``RF:PRObe:GAIN`` command.

    Description:
        - This command specifies the scale factor for the probe attached to the RF input.

    Usage:
        - Using the ``.query()`` method will send the ``RF:PRObe:GAIN?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:PRObe:GAIN?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:PRObe:GAIN value`` command.

    SCPI Syntax:
        ```
        - RF:PRObe:GAIN <NR3>
        - RF:PRObe:GAIN?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the probe scale factor. Allowed values
          depend on the specific probe.
    """


class RfProbeForcedrange(SCPICmdWrite, SCPICmdRead):
    """The ``RF:PRObe:FORCEDRange`` command.

    Description:
        - This command specifies the range of a TekVPI probe attached to the RF input.

    Usage:
        - Using the ``.query()`` method will send the ``RF:PRObe:FORCEDRange?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:PRObe:FORCEDRange?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:PRObe:FORCEDRange value`` command.

    SCPI Syntax:
        ```
        - RF:PRObe:FORCEDRange <NR3>
        - RF:PRObe:FORCEDRange?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the range, which is probe specific.
    """


class RfProbeDegaussState(SCPICmdRead):
    """The ``RF:PRObe:DEGAUss:STATE`` command.

    Description:
        - This command returns the state of the probe degauss for the RF input.

    Usage:
        - Using the ``.query()`` method will send the ``RF:PRObe:DEGAUss:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:PRObe:DEGAUss:STATE?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - RF:PRObe:DEGAUss:STATE?
        ```
    """


class RfProbeDegauss(SCPICmdWrite, SCPICmdRead):
    """The ``RF:PRObe:DEGAUss`` command.

    Description:
        - This command starts a degauss/AutoZero cycle on a TekVPI current probe attached to the RF
          input.

    Usage:
        - Using the ``.write(value)`` method will send the ``RF:PRObe:DEGAUss value`` command.

    SCPI Syntax:
        ```
        - RF:PRObe:DEGAUss EXECute
        ```

    Properties:
        - ``.state``: The ``RF:PRObe:DEGAUss:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = RfProbeDegaussState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> RfProbeDegaussState:
        """Return the ``RF:PRObe:DEGAUss:STATE`` command.

        Description:
            - This command returns the state of the probe degauss for the RF input.

        Usage:
            - Using the ``.query()`` method will send the ``RF:PRObe:DEGAUss:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:PRObe:DEGAUss:STATE?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - RF:PRObe:DEGAUss:STATE?
            ```
        """
        return self._state


class RfProbeCommand(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``RF:PRObe:COMMAND`` command.

    Description:
        - This command sets the state of the probe control specified with the first argument to the
          state specified with the second argument. The commands and states are unique to the
          attached probe type. See the probe documentation for how to set these string arguments.
          The command form takes 2 string arguments: the first is the probe command enumeration and
          the second is the data value. The query form requires a single quoted string argument to
          specify the probe command enumeration for which the response data is requested.

    Usage:
        - Using the ``.query(argument)`` method will send the ``RF:PRObe:COMMAND? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the ``RF:PRObe:COMMAND? argument``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:PRObe:COMMAND value`` command.

    SCPI Syntax:
        ```
        - RF:PRObe:COMMAND <QString>, <QString>
        - RF:PRObe:COMMAND? <QString>
        ```

    Info:
        - ``<QString>`` are quoted strings specifying the probe command and value to set in the
          probe attached to the specified channel.
    """


class RfProbeCalibrateState(SCPICmdRead):
    """The ``RF:PRObe:CALibrate:STATE`` command.

    Description:
        - This command returns the calibration state of the probe connected to the RF input.

    Usage:
        - Using the ``.query()`` method will send the ``RF:PRObe:CALibrate:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:PRObe:CALibrate:STATE?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - RF:PRObe:CALibrate:STATE?
        ```
    """


class RfProbeCalibrateCalibratable(SCPICmdRead):
    """The ``RF:PRObe:CALibrate:CALIBRATABLe`` command.

    Description:
        - This query returns a boolean value that indicates whether the attached probe is
          calibratable.

    Usage:
        - Using the ``.query()`` method will send the ``RF:PRObe:CALibrate:CALIBRATABLe?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:PRObe:CALibrate:CALIBRATABLe?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - RF:PRObe:CALibrate:CALIBRATABLe?
        ```
    """


class RfProbeCalibrate(SCPICmdWrite, SCPICmdRead):
    """The ``RF:PRObe:CALibrate`` command.

    Description:
        - This command executes a calibration or initialization for a probe attached to the RF
          input, if the probe is calibratable. To determine whether the probe is calibratable, use
          ``RF:PROBE:CALIBRATE:CALIBRATABLE``.

    Usage:
        - Using the ``.write(value)`` method will send the ``RF:PRObe:CALibrate value`` command.

    SCPI Syntax:
        ```
        - RF:PRObe:CALibrate {EXECute|INITialize}
        ```

    Info:
        - ``EXECute`` - executes a calibration for the attached probe.
        - ``INITialize`` - initializes the attached probe.

    Properties:
        - ``.calibratable``: The ``RF:PRObe:CALibrate:CALIBRATABLe`` command.
        - ``.state``: The ``RF:PRObe:CALibrate:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._calibratable = RfProbeCalibrateCalibratable(
            device, f"{self._cmd_syntax}:CALIBRATABLe"
        )
        self._state = RfProbeCalibrateState(device, f"{self._cmd_syntax}:STATE")

    @property
    def calibratable(self) -> RfProbeCalibrateCalibratable:
        """Return the ``RF:PRObe:CALibrate:CALIBRATABLe`` command.

        Description:
            - This query returns a boolean value that indicates whether the attached probe is
              calibratable.

        Usage:
            - Using the ``.query()`` method will send the ``RF:PRObe:CALibrate:CALIBRATABLe?``
              query.
            - Using the ``.verify(value)`` method will send the ``RF:PRObe:CALibrate:CALIBRATABLe?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - RF:PRObe:CALibrate:CALIBRATABLe?
            ```
        """
        return self._calibratable

    @property
    def state(self) -> RfProbeCalibrateState:
        """Return the ``RF:PRObe:CALibrate:STATE`` command.

        Description:
            - This command returns the calibration state of the probe connected to the RF input.

        Usage:
            - Using the ``.query()`` method will send the ``RF:PRObe:CALibrate:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:PRObe:CALibrate:STATE?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - RF:PRObe:CALibrate:STATE?
            ```
        """
        return self._state


class RfProbeAutozero(SCPICmdWrite):
    """The ``RF:PRObe:AUTOZero`` command.

    Description:
        - This command executes the attached probe's AutoZero function, for probes that support this
          feature. See your probe documentation for more details.

    Usage:
        - Using the ``.write(value)`` method will send the ``RF:PRObe:AUTOZero value`` command.

    SCPI Syntax:
        ```
        - RF:PRObe:AUTOZero EXECute
        ```
    """


#  pylint: disable=too-many-instance-attributes
class RfProbe(SCPICmdRead):
    """The ``RF:PRObe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``RF:PRObe?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:PRObe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.autozero``: The ``RF:PRObe:AUTOZero`` command.
        - ``.calibrate``: The ``RF:PRObe:CALibrate`` command.
        - ``.command``: The ``RF:PRObe:COMMAND`` command.
        - ``.degauss``: The ``RF:PRObe:DEGAUss`` command.
        - ``.forcedrange``: The ``RF:PRObe:FORCEDRange`` command.
        - ``.gain``: The ``RF:PRObe:GAIN`` command.
        - ``.id``: The ``RF:PRObe:ID`` command tree.
        - ``.preamp``: The ``RF:PRObe:PREAmp`` command tree.
        - ``.resistance``: The ``RF:PRObe:RESistance`` command.
        - ``.signal``: The ``RF:PRObe:SIGnal`` command.
        - ``.units``: The ``RF:PRObe:UNIts`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autozero = RfProbeAutozero(device, f"{self._cmd_syntax}:AUTOZero")
        self._calibrate = RfProbeCalibrate(device, f"{self._cmd_syntax}:CALibrate")
        self._command = RfProbeCommand(device, f"{self._cmd_syntax}:COMMAND")
        self._degauss = RfProbeDegauss(device, f"{self._cmd_syntax}:DEGAUss")
        self._forcedrange = RfProbeForcedrange(device, f"{self._cmd_syntax}:FORCEDRange")
        self._gain = RfProbeGain(device, f"{self._cmd_syntax}:GAIN")
        self._id = RfProbeId(device, f"{self._cmd_syntax}:ID")
        self._preamp = RfProbePreamp(device, f"{self._cmd_syntax}:PREAmp")
        self._resistance = RfProbeResistance(device, f"{self._cmd_syntax}:RESistance")
        self._signal = RfProbeSignal(device, f"{self._cmd_syntax}:SIGnal")
        self._units = RfProbeUnits(device, f"{self._cmd_syntax}:UNIts")

    @property
    def autozero(self) -> RfProbeAutozero:
        """Return the ``RF:PRObe:AUTOZero`` command.

        Description:
            - This command executes the attached probe's AutoZero function, for probes that support
              this feature. See your probe documentation for more details.

        Usage:
            - Using the ``.write(value)`` method will send the ``RF:PRObe:AUTOZero value`` command.

        SCPI Syntax:
            ```
            - RF:PRObe:AUTOZero EXECute
            ```
        """
        return self._autozero

    @property
    def calibrate(self) -> RfProbeCalibrate:
        """Return the ``RF:PRObe:CALibrate`` command.

        Description:
            - This command executes a calibration or initialization for a probe attached to the RF
              input, if the probe is calibratable. To determine whether the probe is calibratable,
              use ``RF:PROBE:CALIBRATE:CALIBRATABLE``.

        Usage:
            - Using the ``.write(value)`` method will send the ``RF:PRObe:CALibrate value`` command.

        SCPI Syntax:
            ```
            - RF:PRObe:CALibrate {EXECute|INITialize}
            ```

        Info:
            - ``EXECute`` - executes a calibration for the attached probe.
            - ``INITialize`` - initializes the attached probe.

        Sub-properties:
            - ``.calibratable``: The ``RF:PRObe:CALibrate:CALIBRATABLe`` command.
            - ``.state``: The ``RF:PRObe:CALibrate:STATE`` command.
        """
        return self._calibrate

    @property
    def command(self) -> RfProbeCommand:
        """Return the ``RF:PRObe:COMMAND`` command.

        Description:
            - This command sets the state of the probe control specified with the first argument to
              the state specified with the second argument. The commands and states are unique to
              the attached probe type. See the probe documentation for how to set these string
              arguments. The command form takes 2 string arguments: the first is the probe command
              enumeration and the second is the data value. The query form requires a single quoted
              string argument to specify the probe command enumeration for which the response data
              is requested.

        Usage:
            - Using the ``.query(argument)`` method will send the ``RF:PRObe:COMMAND? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``RF:PRObe:COMMAND? argument`` query and raise an AssertionError if the returned value
              does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:PRObe:COMMAND value`` command.

        SCPI Syntax:
            ```
            - RF:PRObe:COMMAND <QString>, <QString>
            - RF:PRObe:COMMAND? <QString>
            ```

        Info:
            - ``<QString>`` are quoted strings specifying the probe command and value to set in the
              probe attached to the specified channel.
        """
        return self._command

    @property
    def degauss(self) -> RfProbeDegauss:
        """Return the ``RF:PRObe:DEGAUss`` command.

        Description:
            - This command starts a degauss/AutoZero cycle on a TekVPI current probe attached to the
              RF input.

        Usage:
            - Using the ``.write(value)`` method will send the ``RF:PRObe:DEGAUss value`` command.

        SCPI Syntax:
            ```
            - RF:PRObe:DEGAUss EXECute
            ```

        Sub-properties:
            - ``.state``: The ``RF:PRObe:DEGAUss:STATE`` command.
        """
        return self._degauss

    @property
    def forcedrange(self) -> RfProbeForcedrange:
        """Return the ``RF:PRObe:FORCEDRange`` command.

        Description:
            - This command specifies the range of a TekVPI probe attached to the RF input.

        Usage:
            - Using the ``.query()`` method will send the ``RF:PRObe:FORCEDRange?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:PRObe:FORCEDRange?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:PRObe:FORCEDRange value``
              command.

        SCPI Syntax:
            ```
            - RF:PRObe:FORCEDRange <NR3>
            - RF:PRObe:FORCEDRange?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the range, which is probe
              specific.
        """
        return self._forcedrange

    @property
    def gain(self) -> RfProbeGain:
        """Return the ``RF:PRObe:GAIN`` command.

        Description:
            - This command specifies the scale factor for the probe attached to the RF input.

        Usage:
            - Using the ``.query()`` method will send the ``RF:PRObe:GAIN?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:PRObe:GAIN?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:PRObe:GAIN value`` command.

        SCPI Syntax:
            ```
            - RF:PRObe:GAIN <NR3>
            - RF:PRObe:GAIN?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the probe scale factor. Allowed
              values depend on the specific probe.
        """
        return self._gain

    @property
    def id(self) -> RfProbeId:
        """Return the ``RF:PRObe:ID`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``RF:PRObe:ID?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:PRObe:ID?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.sernumber``: The ``RF:PRObe:ID:SERnumber`` command.
            - ``.type``: The ``RF:PRObe:ID:TYPe`` command.
        """
        return self._id

    @property
    def preamp(self) -> RfProbePreamp:
        """Return the ``RF:PRObe:PREAmp`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``RF:PRObe:PREAmp?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:PRObe:PREAmp?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.mode``: The ``RF:PRObe:PREAmp:MODe`` command.
            - ``.status``: The ``RF:PRObe:PREAmp:STATus`` command.
        """
        return self._preamp

    @property
    def resistance(self) -> RfProbeResistance:
        """Return the ``RF:PRObe:RESistance`` command.

        Description:
            - This query returns the input resistance of the probe attached to the RF input, if the
              probe supports it (otherwise, it returns 0.0). The RF input is 50 Ω impedance.

        Usage:
            - Using the ``.query()`` method will send the ``RF:PRObe:RESistance?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:PRObe:RESistance?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - RF:PRObe:RESistance?
            ```
        """
        return self._resistance

    @property
    def signal(self) -> RfProbeSignal:
        """Return the ``RF:PRObe:SIGnal`` command.

        Description:
            - This command specifies the input bypass setting of a TekVPI probe attached to the RF
              input. The probe must support input bypass (for example, TCP0001).

        Usage:
            - Using the ``.query()`` method will send the ``RF:PRObe:SIGnal?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:PRObe:SIGnal?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:PRObe:SIGnal value`` command.

        SCPI Syntax:
            ```
            - RF:PRObe:SIGnal {BYPass|PASS}
            - RF:PRObe:SIGnal?
            ```

        Info:
            - ``BYPass`` sets the probe to Bypass mode.
            - ``PASS`` sets the probe to Pass mode.
        """
        return self._signal

    @property
    def units(self) -> RfProbeUnits:
        """Return the ``RF:PRObe:UNIts`` command.

        Description:
            - This query returns a quoted string that describes the units of measure for the probe
              attached to the RF input.

        Usage:
            - Using the ``.query()`` method will send the ``RF:PRObe:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:PRObe:UNIts?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - RF:PRObe:UNIts?
            ```
        """
        return self._units


class RfPosition(SCPICmdWrite, SCPICmdRead):
    """The ``RF:POSition`` command.

    Description:
        - This command specifies the vertical position for the frequency domain traces. The vertical
          position is the location of the Reference Level with respect to the top of the graticule,
          in divisions. The lower limit is -10 divisions. The upper limit is +10 divisions.

    Usage:
        - Using the ``.query()`` method will send the ``RF:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:POSition?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:POSition value`` command.

    SCPI Syntax:
        ```
        - RF:POSition <NR3>
        - RF:POSition?
        ```

    Info:
        - ``<NR3>`` is a floating point number.
    """


class RfMeasureType(SCPICmdWrite, SCPICmdRead):
    """The ``RF:MEASUre:TYPe`` command.

    Description:
        - This command specifies the RF measurement type: Channel Power, Adjacent Channel Power
          Ratio, Occupied Bandwidth, or none.

    Usage:
        - Using the ``.query()`` method will send the ``RF:MEASUre:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:MEASUre:TYPe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:MEASUre:TYPe value`` command.

    SCPI Syntax:
        ```
        - RF:MEASUre:TYPe {NONe|CP|ACPR|OBW}
        - RF:MEASUre:TYPe?
        ```

    Info:
        - ``CP`` - Channel Power is the total power within the bandwidth defined by the channel
          width. When this measurement is active, the span is automatically set 10% wider than the
          channel width, and the auto detection method is set to Average. To configure the channel
          width, use the command ``RF:MEASURE:CP:CHANBW``. To query the total power within the
          channel bandwidth, use the command ``RF:MEASURE:CP:POWER``.
        - ``ACPR`` - The Adjacent Channel Power Ratio returns the power in the main channel and the
          ratio of channel power to main power for the upper and lower halves of each adjacent
          channel. When this measurement is active, the span is automatically set 10% larger than
          required to capture all channels, and the auto detection method is set to Average. To
          configure the number of adjacent channels, use the command
          ``RF:MEASURE:ACPR:ADJACENTPAIRS``. To configure the channel width, use the command
          ``RF:MEASURE:ACPR:CHANBW``. To configure the channel spacing, use the command
          ``RF:MEASURE:ACPR:CHANSPACING``.
        - ``OBW`` - Occupied Bandwidth (OBW) is the bandwidth that contains the specified % of power
          within the Analysis Bandwidth. The OBW is the difference between the Upper Frequency and
          the Lower Frequency. When this measurement is active, the span is automatically set 10%
          larger than required to capture all channels, and the auto detection method is set to
          Average. To specify the Analysis Bandwidth, use the command ``RF:MEASURE:OBW:CHANBW``. To
          specify the % of power, use the command ``RF:MEASURE:OBW:PERCENTDOWN``.
        - ``NONe``
    """


class RfMeasureObwUpperfreq(SCPICmdRead):
    """The ``RF:MEASUre:OBW:UPPERFreq`` command.

    Description:
        - This query returns the upper frequency threshold (on the display, the white line to the
          right bracketing OBW power). The RF measurement type must be set to OBW using the command
          ``RF:MEASURE:TYPE``. This frequency will locate the position where (100% -
          ``OBW:PERCENTdown``)/2 power is above this frequency.

    Usage:
        - Using the ``.query()`` method will send the ``RF:MEASUre:OBW:UPPERFreq?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:MEASUre:OBW:UPPERFreq?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - RF:MEASUre:OBW:UPPERFreq?
        ```
    """


class RfMeasureObwPower(SCPICmdRead):
    """The ``RF:MEASUre:OBW:POWer`` command.

    Description:
        - This query returns the total channel power within the occupied bandwidth, when the RF
          measurement type has been set to OBW (using the command ``RF:MEASURE:TYPE``). The units
          are user-set (with the command ``RF:UNITS``).

    Usage:
        - Using the ``.query()`` method will send the ``RF:MEASUre:OBW:POWer?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:MEASUre:OBW:POWer?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - RF:MEASUre:OBW:POWer?
        ```
    """


class RfMeasureObwPercentdown(SCPICmdWrite, SCPICmdRead):
    """The ``RF:MEASUre:OBW:PERCENTdown`` command.

    Description:
        - This command specifies the percentage of total power within the Analysis Bandwidth (the
          OBW power) such that half of the remaining power will be below the ``OBW:LOWERFreq`` level
          and the other half of the remaining power will be above the ``OBW:UPPERFreq`` level. The
          value can be set from 99.9 down to 60.0 in 0.1 increments. The RF measurement type must be
          set to OBW using the command ``RF:MEASURE:TYPE``.

    Usage:
        - Using the ``.query()`` method will send the ``RF:MEASUre:OBW:PERCENTdown?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:MEASUre:OBW:PERCENTdown?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:MEASUre:OBW:PERCENTdown value``
          command.

    SCPI Syntax:
        ```
        - RF:MEASUre:OBW:PERCENTdown <NR3>
        - RF:MEASUre:OBW:PERCENTdown?
        ```

    Info:
        - ``<NR3>`` is a floating point number.
    """


class RfMeasureObwLowerfreq(SCPICmdRead):
    """The ``RF:MEASUre:OBW:LOWERFreq`` command.

    Description:
        - This query returns the lower frequency threshold (on the display, the white line to the
          left bracketing OBW power). The RF measurement type must be set to OBW using the command
          ``RF:MEASURE:TYPE``.

    Usage:
        - Using the ``.query()`` method will send the ``RF:MEASUre:OBW:LOWERFreq?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:MEASUre:OBW:LOWERFreq?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - RF:MEASUre:OBW:LOWERFreq?
        ```
    """


class RfMeasureObwChanbw(SCPICmdWrite, SCPICmdRead):
    """The ``RF:MEASUre:OBW:CHANBW`` command.

    Description:
        - This command specifies the Analysis Bandwidth to use, when the RF measurement type has
          been set to OBW (using the command ``RF:MEASURE:TYPE``). Note that the span automatically
          increases or decreases to be 10% more than the Analysis Bandwidth (providing some room
          around the signal of interest).

    Usage:
        - Using the ``.query()`` method will send the ``RF:MEASUre:OBW:CHANBW?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:MEASUre:OBW:CHANBW?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:MEASUre:OBW:CHANBW value`` command.

    SCPI Syntax:
        ```
        - RF:MEASUre:OBW:CHANBW <NR3>
        - RF:MEASUre:OBW:CHANBW?
        ```
    """


class RfMeasureObw(SCPICmdRead):
    """The ``RF:MEASUre:OBW`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``RF:MEASUre:OBW?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:MEASUre:OBW?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.chanbw``: The ``RF:MEASUre:OBW:CHANBW`` command.
        - ``.lowerfreq``: The ``RF:MEASUre:OBW:LOWERFreq`` command.
        - ``.percentdown``: The ``RF:MEASUre:OBW:PERCENTdown`` command.
        - ``.power``: The ``RF:MEASUre:OBW:POWer`` command.
        - ``.upperfreq``: The ``RF:MEASUre:OBW:UPPERFreq`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._chanbw = RfMeasureObwChanbw(device, f"{self._cmd_syntax}:CHANBW")
        self._lowerfreq = RfMeasureObwLowerfreq(device, f"{self._cmd_syntax}:LOWERFreq")
        self._percentdown = RfMeasureObwPercentdown(device, f"{self._cmd_syntax}:PERCENTdown")
        self._power = RfMeasureObwPower(device, f"{self._cmd_syntax}:POWer")
        self._upperfreq = RfMeasureObwUpperfreq(device, f"{self._cmd_syntax}:UPPERFreq")

    @property
    def chanbw(self) -> RfMeasureObwChanbw:
        """Return the ``RF:MEASUre:OBW:CHANBW`` command.

        Description:
            - This command specifies the Analysis Bandwidth to use, when the RF measurement type has
              been set to OBW (using the command ``RF:MEASURE:TYPE``). Note that the span
              automatically increases or decreases to be 10% more than the Analysis Bandwidth
              (providing some room around the signal of interest).

        Usage:
            - Using the ``.query()`` method will send the ``RF:MEASUre:OBW:CHANBW?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:MEASUre:OBW:CHANBW?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:MEASUre:OBW:CHANBW value``
              command.

        SCPI Syntax:
            ```
            - RF:MEASUre:OBW:CHANBW <NR3>
            - RF:MEASUre:OBW:CHANBW?
            ```
        """
        return self._chanbw

    @property
    def lowerfreq(self) -> RfMeasureObwLowerfreq:
        """Return the ``RF:MEASUre:OBW:LOWERFreq`` command.

        Description:
            - This query returns the lower frequency threshold (on the display, the white line to
              the left bracketing OBW power). The RF measurement type must be set to OBW using the
              command ``RF:MEASURE:TYPE``.

        Usage:
            - Using the ``.query()`` method will send the ``RF:MEASUre:OBW:LOWERFreq?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:MEASUre:OBW:LOWERFreq?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - RF:MEASUre:OBW:LOWERFreq?
            ```
        """
        return self._lowerfreq

    @property
    def percentdown(self) -> RfMeasureObwPercentdown:
        """Return the ``RF:MEASUre:OBW:PERCENTdown`` command.

        Description:
            - This command specifies the percentage of total power within the Analysis Bandwidth
              (the OBW power) such that half of the remaining power will be below the
              ``OBW:LOWERFreq`` level and the other half of the remaining power will be above the
              ``OBW:UPPERFreq`` level. The value can be set from 99.9 down to 60.0 in 0.1
              increments. The RF measurement type must be set to OBW using the command
              ``RF:MEASURE:TYPE``.

        Usage:
            - Using the ``.query()`` method will send the ``RF:MEASUre:OBW:PERCENTdown?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:MEASUre:OBW:PERCENTdown?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:MEASUre:OBW:PERCENTdown value``
              command.

        SCPI Syntax:
            ```
            - RF:MEASUre:OBW:PERCENTdown <NR3>
            - RF:MEASUre:OBW:PERCENTdown?
            ```

        Info:
            - ``<NR3>`` is a floating point number.
        """
        return self._percentdown

    @property
    def power(self) -> RfMeasureObwPower:
        """Return the ``RF:MEASUre:OBW:POWer`` command.

        Description:
            - This query returns the total channel power within the occupied bandwidth, when the RF
              measurement type has been set to OBW (using the command ``RF:MEASURE:TYPE``). The
              units are user-set (with the command ``RF:UNITS``).

        Usage:
            - Using the ``.query()`` method will send the ``RF:MEASUre:OBW:POWer?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:MEASUre:OBW:POWer?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - RF:MEASUre:OBW:POWer?
            ```
        """
        return self._power

    @property
    def upperfreq(self) -> RfMeasureObwUpperfreq:
        """Return the ``RF:MEASUre:OBW:UPPERFreq`` command.

        Description:
            - This query returns the upper frequency threshold (on the display, the white line to
              the right bracketing OBW power). The RF measurement type must be set to OBW using the
              command ``RF:MEASURE:TYPE``. This frequency will locate the position where (100% -
              ``OBW:PERCENTdown``)/2 power is above this frequency.

        Usage:
            - Using the ``.query()`` method will send the ``RF:MEASUre:OBW:UPPERFreq?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:MEASUre:OBW:UPPERFreq?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - RF:MEASUre:OBW:UPPERFreq?
            ```
        """
        return self._upperfreq


class RfMeasureCpPower(SCPICmdRead):
    """The ``RF:MEASUre:CP:POWer`` command.

    Description:
        - This query returns the total channel power within the displayed channel bandwidth, when
          the RF measurement type has been set to CP (using the command ``RF:MEASURE:TYPE``).

    Usage:
        - Using the ``.query()`` method will send the ``RF:MEASUre:CP:POWer?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:MEASUre:CP:POWer?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - RF:MEASUre:CP:POWer?
        ```
    """


class RfMeasureCpChanbw(SCPICmdWrite, SCPICmdRead):
    """The ``RF:MEASUre:CP:CHANBW`` command.

    Description:
        - This command specifies the channel bandwidth to use when the RF measurement type has been
          set to Channel Power (CP) using the command ``RF:MEASURE:TYPE``. The channel bandwidth is
          centered about the CF (center frequency). Note that the span is automatically controlled
          to be 10% wider than the channel width.

    Usage:
        - Using the ``.query()`` method will send the ``RF:MEASUre:CP:CHANBW?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:MEASUre:CP:CHANBW?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:MEASUre:CP:CHANBW value`` command.

    SCPI Syntax:
        ```
        - RF:MEASUre:CP:CHANBW <NR3>
        - RF:MEASUre:CP:CHANBW?
        ```

    Info:
        - ``<NR3>`` is a floating point number.
    """


class RfMeasureCp(SCPICmdRead):
    """The ``RF:MEASUre:CP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``RF:MEASUre:CP?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:MEASUre:CP?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.chanbw``: The ``RF:MEASUre:CP:CHANBW`` command.
        - ``.power``: The ``RF:MEASUre:CP:POWer`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._chanbw = RfMeasureCpChanbw(device, f"{self._cmd_syntax}:CHANBW")
        self._power = RfMeasureCpPower(device, f"{self._cmd_syntax}:POWer")

    @property
    def chanbw(self) -> RfMeasureCpChanbw:
        """Return the ``RF:MEASUre:CP:CHANBW`` command.

        Description:
            - This command specifies the channel bandwidth to use when the RF measurement type has
              been set to Channel Power (CP) using the command ``RF:MEASURE:TYPE``. The channel
              bandwidth is centered about the CF (center frequency). Note that the span is
              automatically controlled to be 10% wider than the channel width.

        Usage:
            - Using the ``.query()`` method will send the ``RF:MEASUre:CP:CHANBW?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:MEASUre:CP:CHANBW?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:MEASUre:CP:CHANBW value``
              command.

        SCPI Syntax:
            ```
            - RF:MEASUre:CP:CHANBW <NR3>
            - RF:MEASUre:CP:CHANBW?
            ```

        Info:
            - ``<NR3>`` is a floating point number.
        """
        return self._chanbw

    @property
    def power(self) -> RfMeasureCpPower:
        """Return the ``RF:MEASUre:CP:POWer`` command.

        Description:
            - This query returns the total channel power within the displayed channel bandwidth,
              when the RF measurement type has been set to CP (using the command
              ``RF:MEASURE:TYPE``).

        Usage:
            - Using the ``.query()`` method will send the ``RF:MEASUre:CP:POWer?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:MEASUre:CP:POWer?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - RF:MEASUre:CP:POWer?
            ```
        """
        return self._power


class RfMeasureAcprUa3db(SCPICmdRead):
    """The ``RF:MEASUre:ACPR:UA3DB`` command.

    Description:
        - This query measures a ratio between the third upper side channel and the Main channel when
          performing ACPR measurements using a frequency domain trace. The power in the adjacent
          channel is equivalent to the power in the main channel (dBm) added to the power ratio (dB)
          of the adjacent channel. (The RF measurement type must be set to ACPR using the command
          ``RF:MEASURE:TYPE``.)

    Usage:
        - Using the ``.query()`` method will send the ``RF:MEASUre:ACPR:UA3DB?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:MEASUre:ACPR:UA3DB?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - RF:MEASUre:ACPR:UA3DB?
        ```
    """


class RfMeasureAcprUa2db(SCPICmdRead):
    """The ``RF:MEASUre:ACPR:UA2DB`` command.

    Description:
        - This query measures a ratio between the second upper side channel and the Main channel
          when performing ACPR measurements using a frequency domain trace. The power in the
          adjacent channel is equivalent to the power in the main channel (dBm) added to the power
          ratio (dB) of the adjacent channel. (The RF measurement type must be set to ACPR using the
          command ``RF:MEASURE:TYPE``.)

    Usage:
        - Using the ``.query()`` method will send the ``RF:MEASUre:ACPR:UA2DB?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:MEASUre:ACPR:UA2DB?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - RF:MEASUre:ACPR:UA2DB?
        ```
    """


class RfMeasureAcprUa1db(SCPICmdRead):
    """The ``RF:MEASUre:ACPR:UA1DB`` command.

    Description:
        - This query measures a ratio between the first upper side channel and the Main channel when
          performing ACPR measurements using a frequency domain trace. The power in the adjacent
          channel is equivalent to the power in the main channel (dBm) added to the power ratio (dB)
          of the adjacent channel. (The RF measurement type must be set to ACPR using the command
          ``RF:MEASURE:TYPE``.)

    Usage:
        - Using the ``.query()`` method will send the ``RF:MEASUre:ACPR:UA1DB?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:MEASUre:ACPR:UA1DB?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - RF:MEASUre:ACPR:UA1DB?
        ```
    """


class RfMeasureAcprPower(SCPICmdRead):
    """The ``RF:MEASUre:ACPR:POWer`` command.

    Description:
        - This query returns the measure of the total RF power in the Main channel within the
          channel bandwidth when performing ACPR measurements using a frequency domain trace. It
          uses the units that have been selected with the command ``RF:UNITS``. The RF measurement
          type must be set to ACPR using the command ``RF:MEASURE:TYPE``.

    Usage:
        - Using the ``.query()`` method will send the ``RF:MEASUre:ACPR:POWer?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:MEASUre:ACPR:POWer?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - RF:MEASUre:ACPR:POWer?
        ```
    """


class RfMeasureAcprLa3db(SCPICmdRead):
    """The ``RF:MEASUre:ACPR:LA3DB`` command.

    Description:
        - This query measures a ratio between the third lower side channel and the Main channel when
          performing ACPR measurements using a frequency domain trace. The power in the adjacent
          channel is equivalent to the power in the main channel (dBm) added to the power ratio (dB)
          of the adjacent channel. (The RF measurement type must be set to ACPR using the command
          ``RF:MEASURE:TYPE``.)

    Usage:
        - Using the ``.query()`` method will send the ``RF:MEASUre:ACPR:LA3DB?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:MEASUre:ACPR:LA3DB?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - RF:MEASUre:ACPR:LA3DB?
        ```
    """


class RfMeasureAcprLa2db(SCPICmdRead):
    """The ``RF:MEASUre:ACPR:LA2DB`` command.

    Description:
        - This query measures a ratio between the second lower side channel and the Main channel
          when performing ACPR measurements using a frequency domain trace. The power in the
          adjacent channel is equivalent to the power in the main channel (dBm) added to the power
          ratio (dB) of the adjacent channel. (The RF measurement type must be set to ACPR using the
          command ``RF:MEASURE:TYPE``.)

    Usage:
        - Using the ``.query()`` method will send the ``RF:MEASUre:ACPR:LA2DB?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:MEASUre:ACPR:LA2DB?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - RF:MEASUre:ACPR:LA2DB?
        ```
    """


class RfMeasureAcprLa1db(SCPICmdRead):
    """The ``RF:MEASUre:ACPR:LA1DB`` command.

    Description:
        - This query measures a ratio between the first lower adjacent side channel and the Main
          channel when performing ACPR measurements. The power in the adjacent channel is equivalent
          to the power in the main channel (dBm) added to the power ratio (dB) of the adjacent
          channel. (The RF measurement type must be set to ACPR using the command
          ``RF:MEASURE:TYPE``.)

    Usage:
        - Using the ``.query()`` method will send the ``RF:MEASUre:ACPR:LA1DB?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:MEASUre:ACPR:LA1DB?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - RF:MEASUre:ACPR:LA1DB?
        ```
    """


class RfMeasureAcprChanspacing(SCPICmdWrite, SCPICmdRead):
    """The ``RF:MEASUre:ACPR:CHANSPACing`` command.

    Description:
        - This command specifies the center-to-center spacing between the Main channel and adjacent
          channels when performing ACPR measurements using a frequency domain trace. (The RF
          measurement type must be set to ACPR using the command ``RF:MEASURE:TYPE``.) Note that if
          the channel spacing is adjusted to be more narrow than the channel bandwidth, then the
          oscilloscope will automatically decrease the channel bandwidth.

    Usage:
        - Using the ``.query()`` method will send the ``RF:MEASUre:ACPR:CHANSPACing?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:MEASUre:ACPR:CHANSPACing?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:MEASUre:ACPR:CHANSPACing value``
          command.

    SCPI Syntax:
        ```
        - RF:MEASUre:ACPR:CHANSPACing <NR3>
        - RF:MEASUre:ACPR:CHANSPACing?
        ```

    Info:
        - ``<NR3>`` is a floating point number.
    """


class RfMeasureAcprChanbw(SCPICmdWrite, SCPICmdRead):
    """The ``RF:MEASUre:ACPR:CHANBW`` command.

    Description:
        - This command configures the measurement bandwidth to use for the Main channel, as well as
          the adjacent side channels, when performing ACPR measurements using a frequency domain
          trace. The RF measurement type must first be set to ACPR using the command
          ``RFMEASUre:TYPe ACPR``. Note that adjusting the channel bandwidth automatically adjusts
          the channel spacing. If the bandwidth is adjusted to be wider than the channel spacing,
          the oscilloscope will automatically increase the channel spacing and the span.

    Usage:
        - Using the ``.query()`` method will send the ``RF:MEASUre:ACPR:CHANBW?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:MEASUre:ACPR:CHANBW?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:MEASUre:ACPR:CHANBW value`` command.

    SCPI Syntax:
        ```
        - RF:MEASUre:ACPR:CHANBW <NR3>
        - RF:MEASUre:ACPR:CHANBW?
        ```

    Info:
        - ``<NR3>`` is a floating point number.
    """


class RfMeasureAcprAdjacentpairs(SCPICmdWrite, SCPICmdRead):
    """The ``RF:MEASUre:ACPR:ADJACENTPAIRs`` command.

    Description:
        - When the RF measurement type has been set to ACPR, the frequency domain displays a Main
          channel in the center (``Ch:Main``), and a side channel group on either side of the Main
          Channel. There can be either 1, 2 or 3 channels within each side group; this command
          specifies that number. (Lower Area 1, 2 and 3 would be on the left side of the Main
          channel; Upper Area 1, 2 and 3 would be on the right side). To set the measurement type to
          ACPR, use the command ``RFMEASUre:TYPe ACPR``. The Adjacent Channel Power Ratio (ACPR) is
          the ratio of channel power between two user-selected channels (a side channel and a main
          channel).

    Usage:
        - Using the ``.query()`` method will send the ``RF:MEASUre:ACPR:ADJACENTPAIRs?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:MEASUre:ACPR:ADJACENTPAIRs?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:MEASUre:ACPR:ADJACENTPAIRs value``
          command.

    SCPI Syntax:
        ```
        - RF:MEASUre:ACPR:ADJACENTPAIRs [1|2|3]
        - RF:MEASUre:ACPR:ADJACENTPAIRs?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class RfMeasureAcpr(SCPICmdRead):
    """The ``RF:MEASUre:ACPR`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``RF:MEASUre:ACPR?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:MEASUre:ACPR?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.adjacentpairs``: The ``RF:MEASUre:ACPR:ADJACENTPAIRs`` command.
        - ``.chanbw``: The ``RF:MEASUre:ACPR:CHANBW`` command.
        - ``.chanspacing``: The ``RF:MEASUre:ACPR:CHANSPACing`` command.
        - ``.la1db``: The ``RF:MEASUre:ACPR:LA1DB`` command.
        - ``.la2db``: The ``RF:MEASUre:ACPR:LA2DB`` command.
        - ``.la3db``: The ``RF:MEASUre:ACPR:LA3DB`` command.
        - ``.power``: The ``RF:MEASUre:ACPR:POWer`` command.
        - ``.ua1db``: The ``RF:MEASUre:ACPR:UA1DB`` command.
        - ``.ua2db``: The ``RF:MEASUre:ACPR:UA2DB`` command.
        - ``.ua3db``: The ``RF:MEASUre:ACPR:UA3DB`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._adjacentpairs = RfMeasureAcprAdjacentpairs(
            device, f"{self._cmd_syntax}:ADJACENTPAIRs"
        )
        self._chanbw = RfMeasureAcprChanbw(device, f"{self._cmd_syntax}:CHANBW")
        self._chanspacing = RfMeasureAcprChanspacing(device, f"{self._cmd_syntax}:CHANSPACing")
        self._la1db = RfMeasureAcprLa1db(device, f"{self._cmd_syntax}:LA1DB")
        self._la2db = RfMeasureAcprLa2db(device, f"{self._cmd_syntax}:LA2DB")
        self._la3db = RfMeasureAcprLa3db(device, f"{self._cmd_syntax}:LA3DB")
        self._power = RfMeasureAcprPower(device, f"{self._cmd_syntax}:POWer")
        self._ua1db = RfMeasureAcprUa1db(device, f"{self._cmd_syntax}:UA1DB")
        self._ua2db = RfMeasureAcprUa2db(device, f"{self._cmd_syntax}:UA2DB")
        self._ua3db = RfMeasureAcprUa3db(device, f"{self._cmd_syntax}:UA3DB")

    @property
    def adjacentpairs(self) -> RfMeasureAcprAdjacentpairs:
        """Return the ``RF:MEASUre:ACPR:ADJACENTPAIRs`` command.

        Description:
            - When the RF measurement type has been set to ACPR, the frequency domain displays a
              Main channel in the center (``Ch:Main``), and a side channel group on either side of
              the Main Channel. There can be either 1, 2 or 3 channels within each side group; this
              command specifies that number. (Lower Area 1, 2 and 3 would be on the left side of the
              Main channel; Upper Area 1, 2 and 3 would be on the right side). To set the
              measurement type to ACPR, use the command ``RFMEASUre:TYPe ACPR``. The Adjacent
              Channel Power Ratio (ACPR) is the ratio of channel power between two user-selected
              channels (a side channel and a main channel).

        Usage:
            - Using the ``.query()`` method will send the ``RF:MEASUre:ACPR:ADJACENTPAIRs?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:MEASUre:ACPR:ADJACENTPAIRs?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``RF:MEASUre:ACPR:ADJACENTPAIRs value`` command.

        SCPI Syntax:
            ```
            - RF:MEASUre:ACPR:ADJACENTPAIRs [1|2|3]
            - RF:MEASUre:ACPR:ADJACENTPAIRs?
            ```
        """
        return self._adjacentpairs

    @property
    def chanbw(self) -> RfMeasureAcprChanbw:
        """Return the ``RF:MEASUre:ACPR:CHANBW`` command.

        Description:
            - This command configures the measurement bandwidth to use for the Main channel, as well
              as the adjacent side channels, when performing ACPR measurements using a frequency
              domain trace. The RF measurement type must first be set to ACPR using the command
              ``RFMEASUre:TYPe ACPR``. Note that adjusting the channel bandwidth automatically
              adjusts the channel spacing. If the bandwidth is adjusted to be wider than the channel
              spacing, the oscilloscope will automatically increase the channel spacing and the
              span.

        Usage:
            - Using the ``.query()`` method will send the ``RF:MEASUre:ACPR:CHANBW?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:MEASUre:ACPR:CHANBW?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:MEASUre:ACPR:CHANBW value``
              command.

        SCPI Syntax:
            ```
            - RF:MEASUre:ACPR:CHANBW <NR3>
            - RF:MEASUre:ACPR:CHANBW?
            ```

        Info:
            - ``<NR3>`` is a floating point number.
        """
        return self._chanbw

    @property
    def chanspacing(self) -> RfMeasureAcprChanspacing:
        """Return the ``RF:MEASUre:ACPR:CHANSPACing`` command.

        Description:
            - This command specifies the center-to-center spacing between the Main channel and
              adjacent channels when performing ACPR measurements using a frequency domain trace.
              (The RF measurement type must be set to ACPR using the command ``RF:MEASURE:TYPE``.)
              Note that if the channel spacing is adjusted to be more narrow than the channel
              bandwidth, then the oscilloscope will automatically decrease the channel bandwidth.

        Usage:
            - Using the ``.query()`` method will send the ``RF:MEASUre:ACPR:CHANSPACing?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:MEASUre:ACPR:CHANSPACing?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:MEASUre:ACPR:CHANSPACing value``
              command.

        SCPI Syntax:
            ```
            - RF:MEASUre:ACPR:CHANSPACing <NR3>
            - RF:MEASUre:ACPR:CHANSPACing?
            ```

        Info:
            - ``<NR3>`` is a floating point number.
        """
        return self._chanspacing

    @property
    def la1db(self) -> RfMeasureAcprLa1db:
        """Return the ``RF:MEASUre:ACPR:LA1DB`` command.

        Description:
            - This query measures a ratio between the first lower adjacent side channel and the Main
              channel when performing ACPR measurements. The power in the adjacent channel is
              equivalent to the power in the main channel (dBm) added to the power ratio (dB) of the
              adjacent channel. (The RF measurement type must be set to ACPR using the command
              ``RF:MEASURE:TYPE``.)

        Usage:
            - Using the ``.query()`` method will send the ``RF:MEASUre:ACPR:LA1DB?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:MEASUre:ACPR:LA1DB?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - RF:MEASUre:ACPR:LA1DB?
            ```
        """
        return self._la1db

    @property
    def la2db(self) -> RfMeasureAcprLa2db:
        """Return the ``RF:MEASUre:ACPR:LA2DB`` command.

        Description:
            - This query measures a ratio between the second lower side channel and the Main channel
              when performing ACPR measurements using a frequency domain trace. The power in the
              adjacent channel is equivalent to the power in the main channel (dBm) added to the
              power ratio (dB) of the adjacent channel. (The RF measurement type must be set to ACPR
              using the command ``RF:MEASURE:TYPE``.)

        Usage:
            - Using the ``.query()`` method will send the ``RF:MEASUre:ACPR:LA2DB?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:MEASUre:ACPR:LA2DB?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - RF:MEASUre:ACPR:LA2DB?
            ```
        """
        return self._la2db

    @property
    def la3db(self) -> RfMeasureAcprLa3db:
        """Return the ``RF:MEASUre:ACPR:LA3DB`` command.

        Description:
            - This query measures a ratio between the third lower side channel and the Main channel
              when performing ACPR measurements using a frequency domain trace. The power in the
              adjacent channel is equivalent to the power in the main channel (dBm) added to the
              power ratio (dB) of the adjacent channel. (The RF measurement type must be set to ACPR
              using the command ``RF:MEASURE:TYPE``.)

        Usage:
            - Using the ``.query()`` method will send the ``RF:MEASUre:ACPR:LA3DB?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:MEASUre:ACPR:LA3DB?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - RF:MEASUre:ACPR:LA3DB?
            ```
        """
        return self._la3db

    @property
    def power(self) -> RfMeasureAcprPower:
        """Return the ``RF:MEASUre:ACPR:POWer`` command.

        Description:
            - This query returns the measure of the total RF power in the Main channel within the
              channel bandwidth when performing ACPR measurements using a frequency domain trace. It
              uses the units that have been selected with the command ``RF:UNITS``. The RF
              measurement type must be set to ACPR using the command ``RF:MEASURE:TYPE``.

        Usage:
            - Using the ``.query()`` method will send the ``RF:MEASUre:ACPR:POWer?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:MEASUre:ACPR:POWer?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - RF:MEASUre:ACPR:POWer?
            ```
        """
        return self._power

    @property
    def ua1db(self) -> RfMeasureAcprUa1db:
        """Return the ``RF:MEASUre:ACPR:UA1DB`` command.

        Description:
            - This query measures a ratio between the first upper side channel and the Main channel
              when performing ACPR measurements using a frequency domain trace. The power in the
              adjacent channel is equivalent to the power in the main channel (dBm) added to the
              power ratio (dB) of the adjacent channel. (The RF measurement type must be set to ACPR
              using the command ``RF:MEASURE:TYPE``.)

        Usage:
            - Using the ``.query()`` method will send the ``RF:MEASUre:ACPR:UA1DB?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:MEASUre:ACPR:UA1DB?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - RF:MEASUre:ACPR:UA1DB?
            ```
        """
        return self._ua1db

    @property
    def ua2db(self) -> RfMeasureAcprUa2db:
        """Return the ``RF:MEASUre:ACPR:UA2DB`` command.

        Description:
            - This query measures a ratio between the second upper side channel and the Main channel
              when performing ACPR measurements using a frequency domain trace. The power in the
              adjacent channel is equivalent to the power in the main channel (dBm) added to the
              power ratio (dB) of the adjacent channel. (The RF measurement type must be set to ACPR
              using the command ``RF:MEASURE:TYPE``.)

        Usage:
            - Using the ``.query()`` method will send the ``RF:MEASUre:ACPR:UA2DB?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:MEASUre:ACPR:UA2DB?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - RF:MEASUre:ACPR:UA2DB?
            ```
        """
        return self._ua2db

    @property
    def ua3db(self) -> RfMeasureAcprUa3db:
        """Return the ``RF:MEASUre:ACPR:UA3DB`` command.

        Description:
            - This query measures a ratio between the third upper side channel and the Main channel
              when performing ACPR measurements using a frequency domain trace. The power in the
              adjacent channel is equivalent to the power in the main channel (dBm) added to the
              power ratio (dB) of the adjacent channel. (The RF measurement type must be set to ACPR
              using the command ``RF:MEASURE:TYPE``.)

        Usage:
            - Using the ``.query()`` method will send the ``RF:MEASUre:ACPR:UA3DB?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:MEASUre:ACPR:UA3DB?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - RF:MEASUre:ACPR:UA3DB?
            ```
        """
        return self._ua3db


class RfMeasure(SCPICmdRead):
    """The ``RF:MEASUre`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``RF:MEASUre?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:MEASUre?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.acpr``: The ``RF:MEASUre:ACPR`` command tree.
        - ``.cp``: The ``RF:MEASUre:CP`` command tree.
        - ``.obw``: The ``RF:MEASUre:OBW`` command tree.
        - ``.type``: The ``RF:MEASUre:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._acpr = RfMeasureAcpr(device, f"{self._cmd_syntax}:ACPR")
        self._cp = RfMeasureCp(device, f"{self._cmd_syntax}:CP")
        self._obw = RfMeasureObw(device, f"{self._cmd_syntax}:OBW")
        self._type = RfMeasureType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def acpr(self) -> RfMeasureAcpr:
        """Return the ``RF:MEASUre:ACPR`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``RF:MEASUre:ACPR?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:MEASUre:ACPR?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.adjacentpairs``: The ``RF:MEASUre:ACPR:ADJACENTPAIRs`` command.
            - ``.chanbw``: The ``RF:MEASUre:ACPR:CHANBW`` command.
            - ``.chanspacing``: The ``RF:MEASUre:ACPR:CHANSPACing`` command.
            - ``.la1db``: The ``RF:MEASUre:ACPR:LA1DB`` command.
            - ``.la2db``: The ``RF:MEASUre:ACPR:LA2DB`` command.
            - ``.la3db``: The ``RF:MEASUre:ACPR:LA3DB`` command.
            - ``.power``: The ``RF:MEASUre:ACPR:POWer`` command.
            - ``.ua1db``: The ``RF:MEASUre:ACPR:UA1DB`` command.
            - ``.ua2db``: The ``RF:MEASUre:ACPR:UA2DB`` command.
            - ``.ua3db``: The ``RF:MEASUre:ACPR:UA3DB`` command.
        """
        return self._acpr

    @property
    def cp(self) -> RfMeasureCp:
        """Return the ``RF:MEASUre:CP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``RF:MEASUre:CP?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:MEASUre:CP?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.chanbw``: The ``RF:MEASUre:CP:CHANBW`` command.
            - ``.power``: The ``RF:MEASUre:CP:POWer`` command.
        """
        return self._cp

    @property
    def obw(self) -> RfMeasureObw:
        """Return the ``RF:MEASUre:OBW`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``RF:MEASUre:OBW?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:MEASUre:OBW?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.chanbw``: The ``RF:MEASUre:OBW:CHANBW`` command.
            - ``.lowerfreq``: The ``RF:MEASUre:OBW:LOWERFreq`` command.
            - ``.percentdown``: The ``RF:MEASUre:OBW:PERCENTdown`` command.
            - ``.power``: The ``RF:MEASUre:OBW:POWer`` command.
            - ``.upperfreq``: The ``RF:MEASUre:OBW:UPPERFreq`` command.
        """
        return self._obw

    @property
    def type(self) -> RfMeasureType:
        """Return the ``RF:MEASUre:TYPe`` command.

        Description:
            - This command specifies the RF measurement type: Channel Power, Adjacent Channel Power
              Ratio, Occupied Bandwidth, or none.

        Usage:
            - Using the ``.query()`` method will send the ``RF:MEASUre:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:MEASUre:TYPe?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:MEASUre:TYPe value`` command.

        SCPI Syntax:
            ```
            - RF:MEASUre:TYPe {NONe|CP|ACPR|OBW}
            - RF:MEASUre:TYPe?
            ```

        Info:
            - ``CP`` - Channel Power is the total power within the bandwidth defined by the channel
              width. When this measurement is active, the span is automatically set 10% wider than
              the channel width, and the auto detection method is set to Average. To configure the
              channel width, use the command ``RF:MEASURE:CP:CHANBW``. To query the total power
              within the channel bandwidth, use the command ``RF:MEASURE:CP:POWER``.
            - ``ACPR`` - The Adjacent Channel Power Ratio returns the power in the main channel and
              the ratio of channel power to main power for the upper and lower halves of each
              adjacent channel. When this measurement is active, the span is automatically set 10%
              larger than required to capture all channels, and the auto detection method is set to
              Average. To configure the number of adjacent channels, use the command
              ``RF:MEASURE:ACPR:ADJACENTPAIRS``. To configure the channel width, use the command
              ``RF:MEASURE:ACPR:CHANBW``. To configure the channel spacing, use the command
              ``RF:MEASURE:ACPR:CHANSPACING``.
            - ``OBW`` - Occupied Bandwidth (OBW) is the bandwidth that contains the specified % of
              power within the Analysis Bandwidth. The OBW is the difference between the Upper
              Frequency and the Lower Frequency. When this measurement is active, the span is
              automatically set 10% larger than required to capture all channels, and the auto
              detection method is set to Average. To specify the Analysis Bandwidth, use the command
              ``RF:MEASURE:OBW:CHANBW``. To specify the % of power, use the command
              ``RF:MEASURE:OBW:PERCENTDOWN``.
            - ``NONe``
        """
        return self._type


class RfLabel(SCPICmdWrite, SCPICmdRead):
    """The ``RF:LABel`` command.

    Description:
        - This command specifies (or queries) a label for the RF frequency domain waveform.

    Usage:
        - Using the ``.query()`` method will send the ``RF:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:LABel?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:LABel value`` command.

    SCPI Syntax:
        ```
        - RF:LABel <QString>
        - RF:LABel?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class RfFrequency(SCPICmdWrite, SCPICmdRead):
    """The ``RF:FREQuency`` command.

    Description:
        - This command specifies the center frequency of the RF acquisition system.

    Usage:
        - Using the ``.query()`` method will send the ``RF:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:FREQuency?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:FREQuency value`` command.

    SCPI Syntax:
        ```
        - RF:FREQuency <NR3>
        - RF:FREQuency?
        ```

    Info:
        - ``<NR3>`` is a floating point value.
    """


class RfDetectionmethodRfNormal(SCPICmdWrite, SCPICmdRead):
    """The ``RF:DETECTionmethod:RF_NORMal`` command.

    Description:
        - This command specifies the detection method the oscilloscope should use when acquiring an
          RF Normal frequency domain trace. The Normal trace displays the most recently acquired
          sample at each trace point. . In order to change the detection method, you must first
          change the detection method mode to MANUAL using the command ``RF:DETECTIONMETHOD:MODE``.
          The detection method is the internal calculation that decimates (reduces) a long frequency
          domain waveform down to display resolution, by dividing the waveform into intervals and
          choosing a single value to represent each interval on screen.

    Usage:
        - Using the ``.query()`` method will send the ``RF:DETECTionmethod:RF_NORMal?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:DETECTionmethod:RF_NORMal?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:DETECTionmethod:RF_NORMal value``
          command.

    SCPI Syntax:
        ```
        - RF:DETECTionmethod:RF_NORMal {PLUSpeak|MINUSpeak|SAMple|AVErage}
        - RF:DETECTionmethod:RF_NORMal?
        ```

    Info:
        - ``PLUSpeak`` - Detection method that selects the largest value in each interval.
        - ``MINUSpeak`` - Detection method that selects the smallest value in each interval.
        - ``SAMple`` - Detection method that selects the first point in each interval.
        - ``AVErage`` - Detection method that selects the mean value within an interval.
    """


class RfDetectionmethodRfMinhold(SCPICmdWrite, SCPICmdRead):
    """The ``RF:DETECTionmethod:RF_MINHold`` command.

    Description:
        - This command specifies the detection method the oscilloscope should use when acquiring an
          RF Min Hold frequency domain trace. The Min Hold trace displays the smallest value
          throughout the acquisition history at each trace point. In order to change the detection
          method, you must first change the detection method mode to MANUAL using the command
          ``RF:DETECTIONMETHOD:MODE``. The detection method is the internal calculation that
          decimates (reduces) a long frequency domain waveform down to display resolution, by
          dividing the waveform into intervals and choosing a single value to represent each
          interval on screen.

    Usage:
        - Using the ``.query()`` method will send the ``RF:DETECTionmethod:RF_MINHold?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:DETECTionmethod:RF_MINHold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:DETECTionmethod:RF_MINHold value``
          command.

    SCPI Syntax:
        ```
        - RF:DETECTionmethod:RF_MINHold {PLUSpeak|MINUSpeak|SAMple|AVErage}
        - RF:DETECTionmethod:RF_MINHold?
        ```

    Info:
        - ``PLUSpeak`` - Detection method that selects the largest value in each interval.
        - ``MINUSpeak`` - Detection method that selects the smallest value in each interval.
        - ``SAMple`` - Detection method that selects the first point in each interval.
        - ``AVErage`` - Detection method that selects the mean value within an interval.
    """


class RfDetectionmethodRfMaxhold(SCPICmdWrite, SCPICmdRead):
    """The ``RF:DETECTionmethod:RF_MAXHold`` command.

    Description:
        - This command specifies the detection method the oscilloscope should use when acquiring an
          RF Max Hold frequency domain trace. The Max Hold trace displays the largest value in all
          acquisition history at each trace point. In order to change the detection method, you must
          first change the detection method mode to MANUAL using the command
          ``RF:DETECTIONMETHOD:MODE``. The detection method is the internal calculation that
          decimates (reduces) a long frequency domain waveform down to display resolution, by
          dividing the waveform into intervals and choosing a single value to represent each
          interval on screen.

    Usage:
        - Using the ``.query()`` method will send the ``RF:DETECTionmethod:RF_MAXHold?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:DETECTionmethod:RF_MAXHold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:DETECTionmethod:RF_MAXHold value``
          command.

    SCPI Syntax:
        ```
        - RF:DETECTionmethod:RF_MAXHold {PLUSpeak|MINUSpeak|SAMple|AVErage}
        - RF:DETECTionmethod:RF_MAXHold?
        ```

    Info:
        - ``PLUSpeak`` - Detection method that selects the largest value in each interval.
        - ``MINUSpeak`` - Detection method that selects the smallest value in each interval.
        - ``SAMple`` - Detection method that selects the first point in each interval.
        - ``AVErage`` - Detection method that selects the mean value within an interval.
    """


class RfDetectionmethodRfAverage(SCPICmdWrite, SCPICmdRead):
    """The ``RF:DETECTionmethod:RF_AVErage`` command.

    Description:
        - This command specifies the detection method the oscilloscope should use when acquiring an
          RF Average frequency domain trace. In order to change the detection method, you must first
          change the detection method mode to MANUAL using the command ``RF:DETECTIONMETHOD:MODE``.
          The detection method is the internal calculation that decimates (reduces) a long frequency
          domain waveform down to display resolution, by dividing the waveform into intervals and
          choosing a single value to represent each interval on screen.

    Usage:
        - Using the ``.query()`` method will send the ``RF:DETECTionmethod:RF_AVErage?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:DETECTionmethod:RF_AVErage?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:DETECTionmethod:RF_AVErage value``
          command.

    SCPI Syntax:
        ```
        - RF:DETECTionmethod:RF_AVErage {PLUSpeak|MINUSpeak|SAMple|AVErage}
        - RF:DETECTionmethod:RF_AVErage?
        ```

    Info:
        - ``PLUSpeak`` - Detection method that selects the largest value in each interval.
        - ``MINUSpeak`` - Detection method that selects the smallest value in each interval.
        - ``SAMple`` - Detection method that selects the first point in each interval.
        - ``AVErage`` - Detection method that selects the mean value within an interval.
    """


class RfDetectionmethodMode(SCPICmdWrite, SCPICmdRead):
    """The ``RF:DETECTionmethod:MODe`` command.

    Description:
        - This command specifies whether the RF detection within the oscilloscope occurs
          automatically or manually. If you set the detection method mode to MANual, you are able to
          use the related ``RF:DETECTionmethod`` commands to specify detection method options for
          the frequency domain traces (the options are MINUSpeak, SAMple, PLUSpeak and AVErage ).
          The detection method is the internal calculation that decimates (reduces) a long frequency
          domain waveform down to display resolution, by dividing the waveform into intervals and
          choosing a single value to represent each interval on screen.

    Usage:
        - Using the ``.query()`` method will send the ``RF:DETECTionmethod:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:DETECTionmethod:MODe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RF:DETECTionmethod:MODe value``
          command.

    SCPI Syntax:
        ```
        - RF:DETECTionmethod:MODe {AUTO|MANual}
        - RF:DETECTionmethod:MODe?
        ```
    """


class RfDetectionmethod(SCPICmdRead):
    """The ``RF:DETECTionmethod`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``RF:DETECTionmethod?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:DETECTionmethod?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.mode``: The ``RF:DETECTionmethod:MODe`` command.
        - ``.rf_average``: The ``RF:DETECTionmethod:RF_AVErage`` command.
        - ``.rf_maxhold``: The ``RF:DETECTionmethod:RF_MAXHold`` command.
        - ``.rf_minhold``: The ``RF:DETECTionmethod:RF_MINHold`` command.
        - ``.rf_normal``: The ``RF:DETECTionmethod:RF_NORMal`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = RfDetectionmethodMode(device, f"{self._cmd_syntax}:MODe")
        self._rf_average = RfDetectionmethodRfAverage(device, f"{self._cmd_syntax}:RF_AVErage")
        self._rf_maxhold = RfDetectionmethodRfMaxhold(device, f"{self._cmd_syntax}:RF_MAXHold")
        self._rf_minhold = RfDetectionmethodRfMinhold(device, f"{self._cmd_syntax}:RF_MINHold")
        self._rf_normal = RfDetectionmethodRfNormal(device, f"{self._cmd_syntax}:RF_NORMal")

    @property
    def mode(self) -> RfDetectionmethodMode:
        """Return the ``RF:DETECTionmethod:MODe`` command.

        Description:
            - This command specifies whether the RF detection within the oscilloscope occurs
              automatically or manually. If you set the detection method mode to MANual, you are
              able to use the related ``RF:DETECTionmethod`` commands to specify detection method
              options for the frequency domain traces (the options are MINUSpeak, SAMple, PLUSpeak
              and AVErage ). The detection method is the internal calculation that decimates
              (reduces) a long frequency domain waveform down to display resolution, by dividing the
              waveform into intervals and choosing a single value to represent each interval on
              screen.

        Usage:
            - Using the ``.query()`` method will send the ``RF:DETECTionmethod:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:DETECTionmethod:MODe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:DETECTionmethod:MODe value``
              command.

        SCPI Syntax:
            ```
            - RF:DETECTionmethod:MODe {AUTO|MANual}
            - RF:DETECTionmethod:MODe?
            ```
        """
        return self._mode

    @property
    def rf_average(self) -> RfDetectionmethodRfAverage:
        """Return the ``RF:DETECTionmethod:RF_AVErage`` command.

        Description:
            - This command specifies the detection method the oscilloscope should use when acquiring
              an RF Average frequency domain trace. In order to change the detection method, you
              must first change the detection method mode to MANUAL using the command
              ``RF:DETECTIONMETHOD:MODE``. The detection method is the internal calculation that
              decimates (reduces) a long frequency domain waveform down to display resolution, by
              dividing the waveform into intervals and choosing a single value to represent each
              interval on screen.

        Usage:
            - Using the ``.query()`` method will send the ``RF:DETECTionmethod:RF_AVErage?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:DETECTionmethod:RF_AVErage?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``RF:DETECTionmethod:RF_AVErage value`` command.

        SCPI Syntax:
            ```
            - RF:DETECTionmethod:RF_AVErage {PLUSpeak|MINUSpeak|SAMple|AVErage}
            - RF:DETECTionmethod:RF_AVErage?
            ```

        Info:
            - ``PLUSpeak`` - Detection method that selects the largest value in each interval.
            - ``MINUSpeak`` - Detection method that selects the smallest value in each interval.
            - ``SAMple`` - Detection method that selects the first point in each interval.
            - ``AVErage`` - Detection method that selects the mean value within an interval.
        """
        return self._rf_average

    @property
    def rf_maxhold(self) -> RfDetectionmethodRfMaxhold:
        """Return the ``RF:DETECTionmethod:RF_MAXHold`` command.

        Description:
            - This command specifies the detection method the oscilloscope should use when acquiring
              an RF Max Hold frequency domain trace. The Max Hold trace displays the largest value
              in all acquisition history at each trace point. In order to change the detection
              method, you must first change the detection method mode to MANUAL using the command
              ``RF:DETECTIONMETHOD:MODE``. The detection method is the internal calculation that
              decimates (reduces) a long frequency domain waveform down to display resolution, by
              dividing the waveform into intervals and choosing a single value to represent each
              interval on screen.

        Usage:
            - Using the ``.query()`` method will send the ``RF:DETECTionmethod:RF_MAXHold?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:DETECTionmethod:RF_MAXHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``RF:DETECTionmethod:RF_MAXHold value`` command.

        SCPI Syntax:
            ```
            - RF:DETECTionmethod:RF_MAXHold {PLUSpeak|MINUSpeak|SAMple|AVErage}
            - RF:DETECTionmethod:RF_MAXHold?
            ```

        Info:
            - ``PLUSpeak`` - Detection method that selects the largest value in each interval.
            - ``MINUSpeak`` - Detection method that selects the smallest value in each interval.
            - ``SAMple`` - Detection method that selects the first point in each interval.
            - ``AVErage`` - Detection method that selects the mean value within an interval.
        """
        return self._rf_maxhold

    @property
    def rf_minhold(self) -> RfDetectionmethodRfMinhold:
        """Return the ``RF:DETECTionmethod:RF_MINHold`` command.

        Description:
            - This command specifies the detection method the oscilloscope should use when acquiring
              an RF Min Hold frequency domain trace. The Min Hold trace displays the smallest value
              throughout the acquisition history at each trace point. In order to change the
              detection method, you must first change the detection method mode to MANUAL using the
              command ``RF:DETECTIONMETHOD:MODE``. The detection method is the internal calculation
              that decimates (reduces) a long frequency domain waveform down to display resolution,
              by dividing the waveform into intervals and choosing a single value to represent each
              interval on screen.

        Usage:
            - Using the ``.query()`` method will send the ``RF:DETECTionmethod:RF_MINHold?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:DETECTionmethod:RF_MINHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``RF:DETECTionmethod:RF_MINHold value`` command.

        SCPI Syntax:
            ```
            - RF:DETECTionmethod:RF_MINHold {PLUSpeak|MINUSpeak|SAMple|AVErage}
            - RF:DETECTionmethod:RF_MINHold?
            ```

        Info:
            - ``PLUSpeak`` - Detection method that selects the largest value in each interval.
            - ``MINUSpeak`` - Detection method that selects the smallest value in each interval.
            - ``SAMple`` - Detection method that selects the first point in each interval.
            - ``AVErage`` - Detection method that selects the mean value within an interval.
        """
        return self._rf_minhold

    @property
    def rf_normal(self) -> RfDetectionmethodRfNormal:
        """Return the ``RF:DETECTionmethod:RF_NORMal`` command.

        Description:
            - This command specifies the detection method the oscilloscope should use when acquiring
              an RF Normal frequency domain trace. The Normal trace displays the most recently
              acquired sample at each trace point. . In order to change the detection method, you
              must first change the detection method mode to MANUAL using the command
              ``RF:DETECTIONMETHOD:MODE``. The detection method is the internal calculation that
              decimates (reduces) a long frequency domain waveform down to display resolution, by
              dividing the waveform into intervals and choosing a single value to represent each
              interval on screen.

        Usage:
            - Using the ``.query()`` method will send the ``RF:DETECTionmethod:RF_NORMal?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:DETECTionmethod:RF_NORMal?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``RF:DETECTionmethod:RF_NORMal value`` command.

        SCPI Syntax:
            ```
            - RF:DETECTionmethod:RF_NORMal {PLUSpeak|MINUSpeak|SAMple|AVErage}
            - RF:DETECTionmethod:RF_NORMal?
            ```

        Info:
            - ``PLUSpeak`` - Detection method that selects the largest value in each interval.
            - ``MINUSpeak`` - Detection method that selects the smallest value in each interval.
            - ``SAMple`` - Detection method that selects the first point in each interval.
            - ``AVErage`` - Detection method that selects the mean value within an interval.
        """
        return self._rf_normal


class RfClipping(SCPICmdRead):
    """The ``RF:CLIPPing`` command.

    Description:
        - Returns a boolean indicating whether the RF input is 'clipping' due to input
          over/under-range detection.

    Usage:
        - Using the ``.query()`` method will send the ``RF:CLIPPing?`` query.
        - Using the ``.verify(value)`` method will send the ``RF:CLIPPing?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - RF:CLIPPing?
        ```
    """


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class Rf(SCPICmdRead):
    """The ``RF`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``RF?`` query.
        - Using the ``.verify(value)`` method will send the ``RF?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.clipping``: The ``RF:CLIPPing`` command.
        - ``.detectionmethod``: The ``RF:DETECTionmethod`` command tree.
        - ``.frequency``: The ``RF:FREQuency`` command.
        - ``.label``: The ``RF:LABel`` command.
        - ``.measure``: The ``RF:MEASUre`` command tree.
        - ``.position``: The ``RF:POSition`` command.
        - ``.probe``: The ``RF:PRObe`` command tree.
        - ``.rbw``: The ``RF:RBW`` command.
        - ``.reflevel``: The ``RF:REFLevel`` command.
        - ``.rf_amplitude``: The ``RF:RF_AMPlitude`` command tree.
        - ``.rf_average``: The ``RF:RF_AVErage`` command tree.
        - ``.rf_phase``: The ``RF:RF_PHASe`` command tree.
        - ``.rf_v_time``: The ``RF:RF_V_TIMe`` command tree.
        - ``.scale``: The ``RF:SCAle`` command.
        - ``.span``: The ``RF:SPAN`` command.
        - ``.spanrbwratio``: The ``RF:SPANRbwratio`` command.
        - ``.spectrummode``: The ``RF:SPECTRUMMode`` command.
        - ``.spectrumtrace``: The ``RF:SPECTRUMTrace`` command.
        - ``.spectrogram``: The ``RF:SPECTRogram`` command.
        - ``.squelch``: The ``RF:SQUELCH`` command tree.
        - ``.start``: The ``RF:STARt`` command.
        - ``.stop``: The ``RF:STOP`` command.
        - ``.units``: The ``RF:UNIts`` command.
        - ``.window``: The ``RF:WINdow`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "RF") -> None:
        super().__init__(device, cmd_syntax)
        self._clipping = RfClipping(device, f"{self._cmd_syntax}:CLIPPing")
        self._detectionmethod = RfDetectionmethod(device, f"{self._cmd_syntax}:DETECTionmethod")
        self._frequency = RfFrequency(device, f"{self._cmd_syntax}:FREQuency")
        self._label = RfLabel(device, f"{self._cmd_syntax}:LABel")
        self._measure = RfMeasure(device, f"{self._cmd_syntax}:MEASUre")
        self._position = RfPosition(device, f"{self._cmd_syntax}:POSition")
        self._probe = RfProbe(device, f"{self._cmd_syntax}:PRObe")
        self._rbw = RfRbw(device, f"{self._cmd_syntax}:RBW")
        self._reflevel = RfReflevel(device, f"{self._cmd_syntax}:REFLevel")
        self._rf_amplitude = RfRfAmplitude(device, f"{self._cmd_syntax}:RF_AMPlitude")
        self._rf_average = RfRfAverage(device, f"{self._cmd_syntax}:RF_AVErage")
        self._rf_phase = RfRfPhase(device, f"{self._cmd_syntax}:RF_PHASe")
        self._rf_v_time = RfRfVTime(device, f"{self._cmd_syntax}:RF_V_TIMe")
        self._scale = RfScale(device, f"{self._cmd_syntax}:SCAle")
        self._span = RfSpan(device, f"{self._cmd_syntax}:SPAN")
        self._spanrbwratio = RfSpanrbwratio(device, f"{self._cmd_syntax}:SPANRbwratio")
        self._spectrummode = RfSpectrummode(device, f"{self._cmd_syntax}:SPECTRUMMode")
        self._spectrumtrace = RfSpectrumtrace(device, f"{self._cmd_syntax}:SPECTRUMTrace")
        self._spectrogram = RfSpectrogram(device, f"{self._cmd_syntax}:SPECTRogram")
        self._squelch = RfSquelch(device, f"{self._cmd_syntax}:SQUELCH")
        self._start = RfStart(device, f"{self._cmd_syntax}:STARt")
        self._stop = RfStop(device, f"{self._cmd_syntax}:STOP")
        self._units = RfUnits(device, f"{self._cmd_syntax}:UNIts")
        self._window = RfWindow(device, f"{self._cmd_syntax}:WINdow")

    @property
    def clipping(self) -> RfClipping:
        """Return the ``RF:CLIPPing`` command.

        Description:
            - Returns a boolean indicating whether the RF input is 'clipping' due to input
              over/under-range detection.

        Usage:
            - Using the ``.query()`` method will send the ``RF:CLIPPing?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:CLIPPing?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - RF:CLIPPing?
            ```
        """
        return self._clipping

    @property
    def detectionmethod(self) -> RfDetectionmethod:
        """Return the ``RF:DETECTionmethod`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``RF:DETECTionmethod?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:DETECTionmethod?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.mode``: The ``RF:DETECTionmethod:MODe`` command.
            - ``.rf_average``: The ``RF:DETECTionmethod:RF_AVErage`` command.
            - ``.rf_maxhold``: The ``RF:DETECTionmethod:RF_MAXHold`` command.
            - ``.rf_minhold``: The ``RF:DETECTionmethod:RF_MINHold`` command.
            - ``.rf_normal``: The ``RF:DETECTionmethod:RF_NORMal`` command.
        """
        return self._detectionmethod

    @property
    def frequency(self) -> RfFrequency:
        """Return the ``RF:FREQuency`` command.

        Description:
            - This command specifies the center frequency of the RF acquisition system.

        Usage:
            - Using the ``.query()`` method will send the ``RF:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:FREQuency?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:FREQuency value`` command.

        SCPI Syntax:
            ```
            - RF:FREQuency <NR3>
            - RF:FREQuency?
            ```

        Info:
            - ``<NR3>`` is a floating point value.
        """
        return self._frequency

    @property
    def label(self) -> RfLabel:
        """Return the ``RF:LABel`` command.

        Description:
            - This command specifies (or queries) a label for the RF frequency domain waveform.

        Usage:
            - Using the ``.query()`` method will send the ``RF:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:LABel?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:LABel value`` command.

        SCPI Syntax:
            ```
            - RF:LABel <QString>
            - RF:LABel?
            ```
        """
        return self._label

    @property
    def measure(self) -> RfMeasure:
        """Return the ``RF:MEASUre`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``RF:MEASUre?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:MEASUre?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.acpr``: The ``RF:MEASUre:ACPR`` command tree.
            - ``.cp``: The ``RF:MEASUre:CP`` command tree.
            - ``.obw``: The ``RF:MEASUre:OBW`` command tree.
            - ``.type``: The ``RF:MEASUre:TYPe`` command.
        """
        return self._measure

    @property
    def position(self) -> RfPosition:
        """Return the ``RF:POSition`` command.

        Description:
            - This command specifies the vertical position for the frequency domain traces. The
              vertical position is the location of the Reference Level with respect to the top of
              the graticule, in divisions. The lower limit is -10 divisions. The upper limit is +10
              divisions.

        Usage:
            - Using the ``.query()`` method will send the ``RF:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:POSition?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:POSition value`` command.

        SCPI Syntax:
            ```
            - RF:POSition <NR3>
            - RF:POSition?
            ```

        Info:
            - ``<NR3>`` is a floating point number.
        """
        return self._position

    @property
    def probe(self) -> RfProbe:
        """Return the ``RF:PRObe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``RF:PRObe?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:PRObe?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.autozero``: The ``RF:PRObe:AUTOZero`` command.
            - ``.calibrate``: The ``RF:PRObe:CALibrate`` command.
            - ``.command``: The ``RF:PRObe:COMMAND`` command.
            - ``.degauss``: The ``RF:PRObe:DEGAUss`` command.
            - ``.forcedrange``: The ``RF:PRObe:FORCEDRange`` command.
            - ``.gain``: The ``RF:PRObe:GAIN`` command.
            - ``.id``: The ``RF:PRObe:ID`` command tree.
            - ``.preamp``: The ``RF:PRObe:PREAmp`` command tree.
            - ``.resistance``: The ``RF:PRObe:RESistance`` command.
            - ``.signal``: The ``RF:PRObe:SIGnal`` command.
            - ``.units``: The ``RF:PRObe:UNIts`` command.
        """
        return self._probe

    @property
    def rbw(self) -> RfRbw:
        """Return the ``RF:RBW`` command.

        Description:
            - This command specifies the resolution bandwidth (RBW) when the RBW mode has been set
              to MANUAL (using the command ``RF:RBW:MODE``). The resolution bandwidth is the width
              of the narrowest measurable band of frequencies in a frequency domain trace. The RBW
              is adjustable down to 20Hz. By default, the RBW tracks the span value in a ``1000:1``
              ratio. The RBW determines the level to which the oscilloscope can resolve individual
              frequencies in the frequency domain. For example, if the input signal contains two
              carriers separated by 1 kHz, you will not be able to discriminate between them unless
              the RBW is less than 1 kHz.

        Usage:
            - Using the ``.query()`` method will send the ``RF:RBW?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:RBW?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:RBW value`` command.

        SCPI Syntax:
            ```
            - RF:RBW <NR3>
            - RF:RBW?
            ```

        Info:
            - ``<NR3>`` is a floating point number that represents the width of the narrowest
              measurable band of frequencies in a frequency domain trace.

        Sub-properties:
            - ``.mode``: The ``RF:RBW:MODe`` command.
        """
        return self._rbw

    @property
    def reflevel(self) -> RfReflevel:
        """Return the ``RF:REFLevel`` command.

        Description:
            - This command sets the Reference Level of the RF input. The Reference Level can either
              be specified as a numeric floating point value, or set automatically.

        Usage:
            - Using the ``.query()`` method will send the ``RF:REFLevel?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:REFLevel?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:REFLevel value`` command.

        SCPI Syntax:
            ```
            - RF:REFLevel {<NR3>|AUTO}
            - RF:REFLevel?
            ```

        Info:
            - ``<NR3>`` is a floating point number.
            - ``AUTO`` directs the oscilloscope to automatically calculate and set the Reference
              Level. This is a one-time calculation based on the content of the RF input signal. It
              is not a 'mode'.
        """
        return self._reflevel

    @property
    def rf_amplitude(self) -> RfRfAmplitude:
        """Return the ``RF:RF_AMPlitude`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``RF:RF_AMPlitude?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:RF_AMPlitude?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.label``: The ``RF:RF_AMPlitude:LABel`` command.
            - ``.vertical``: The ``RF:RF_AMPlitude:VERTical`` command tree.
        """
        return self._rf_amplitude

    @property
    def rf_average(self) -> RfRfAverage:
        """Return the ``RF:RF_AVErage`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``RF:RF_AVErage?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:RF_AVErage?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.count``: The ``RF:RF_AVErage:COUNt`` command.
            - ``.numavg``: The ``RF:RF_AVErage:NUMAVg`` command.
        """
        return self._rf_average

    @property
    def rf_phase(self) -> RfRfPhase:
        """Return the ``RF:RF_PHASe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``RF:RF_PHASe?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:RF_PHASe?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.reference``: The ``RF:RF_PHASe:REFERence`` command tree.
            - ``.wrap``: The ``RF:RF_PHASe:WRAP`` command tree.
        """
        return self._rf_phase

    @property
    def rf_v_time(self) -> RfRfVTime:
        """Return the ``RF:RF_V_TIMe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``RF:RF_V_TIMe?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:RF_V_TIMe?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bandwidth``: The ``RF:RF_V_TIMe:BANDWidth`` command.
        """
        return self._rf_v_time

    @property
    def scale(self) -> RfScale:
        """Return the ``RF:SCAle`` command.

        Description:
            - This command specifies the overall vertical scale setting of the frequency domain
              window. The lower limit is 0.1 dB/division. The upper limit is 100dB/division. The
              vertical scale is adjustable in a 1-2-5 sequence.

        Usage:
            - Using the ``.query()`` method will send the ``RF:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:SCAle?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:SCAle value`` command.

        SCPI Syntax:
            ```
            - RF:SCAle <NR3>
            - RF:SCAle?
            ```

        Info:
            - ``<NR3>`` is a floating point number.
        """
        return self._scale

    @property
    def span(self) -> RfSpan:
        """Return the ``RF:SPAN`` command.

        Description:
            - This command specifies the span setting. The span is the range of frequencies that can
              be observed around the center frequency. This is the width of the frequency domain
              trace, which is equal to the stop frequency minus the start frequency. The maximum
              span varies according to the oscilloscope model. The maximum span for the 3 Series MDO
              matches the analog bandwidth rating; however, if the option 3-SA3 is installed, then
              the maximum span is 3 GHz.

        Usage:
            - Using the ``.query()`` method will send the ``RF:SPAN?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:SPAN?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:SPAN value`` command.

        SCPI Syntax:
            ```
            - RF:SPAN <NR3>
            - RF:SPAN?
            ```

        Info:
            - ``<NR3>`` is a floating point number.
        """
        return self._span

    @property
    def spanrbwratio(self) -> RfSpanrbwratio:
        """Return the ``RF:SPANRbwratio`` command.

        Description:
            - This command specifies the ratio of the span to the resolution bandwidth (RBW) that
              will be used when the RBW Mode is set to AUTO. (In order to set the RBW Mode to AUTO,
              use the command ``RF:RBW:MODE``.) The span is the width of the frequency domain trace
              in Hz, which is equal to the stop frequency minus the start frequency. The RBW is the
              width of the narrowest measurable band of frequencies in a frequency domain trace. The
              default RBW ratio is a factor of 1000.

        Usage:
            - Using the ``.query()`` method will send the ``RF:SPANRbwratio?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:SPANRbwratio?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:SPANRbwratio value`` command.

        SCPI Syntax:
            ```
            - RF:SPANRbwratio <NR3>
            - RF:SPANRbwratio?
            ```

        Info:
            - ``<NR3>`` is a floating point number.
        """
        return self._spanrbwratio

    @property
    def spectrummode(self) -> RfSpectrummode:
        """Return the ``RF:SPECTRUMMode`` command.

        Description:
            - When only the frequency domain waveforms are displayed (no time domain waveforms), you
              can choose whether the MDO4000/B/C should use Triggered mode or Free Run mode. (3
              Series MDO only uses Free Run mode.) When Free Run mode is selected, the oscilloscope
              generates RF acquisitions as fast as possible. The default is FREErun.

        Usage:
            - Using the ``.query()`` method will send the ``RF:SPECTRUMMode?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:SPECTRUMMode?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:SPECTRUMMode value`` command.

        SCPI Syntax:
            ```
            - RF:SPECTRUMMode {TRIGgered|FREErun}
            - RF:SPECTRUMMode?
            ```

        Info:
            - ``TRIGgered`` ties RF acquisitions to the scope's unified triggering system for all
              channels.
            - ``FREErun`` acquires RF data as often as processing allows, without waiting for
              trigger events.
        """
        return self._spectrummode

    @property
    def spectrumtrace(self) -> RfSpectrumtrace:
        """Return the ``RF:SPECTRUMTrace`` command.

        Description:
            - Resets the spectrum traces, ``RF_MINHold``, ``RF_MAXHold`` and ``RF_AVErage``.

        Usage:
            - Using the ``.write(value)`` method will send the ``RF:SPECTRUMTrace value`` command.

        SCPI Syntax:
            ```
            - RF:SPECTRUMTrace {RESET}
            ```
        """
        return self._spectrumtrace

    @property
    def spectrogram(self) -> RfSpectrogram:
        """Return the ``RF:SPECTRogram`` command.

        Description:
            - Clears the spectrogram.

        Usage:
            - Using the ``.write(value)`` method will send the ``RF:SPECTRogram value`` command.

        SCPI Syntax:
            ```
            - RF:SPECTRogram {CLEAR}
            ```

        Info:
            - ``CLEAR`` clears the spectrogram.

        Sub-properties:
            - ``.numslices``: The ``RF:SPECTRogram:NUMSLICEs`` command.
            - ``.sliceselect``: The ``RF:SPECTRogram:SLICESELect`` command.
            - ``.slicetime``: The ``RF:SPECTRogram:SLICETIMe`` command.
            - ``.state``: The ``RF:SPECTRogram:STATE`` command.
            - ``.time``: The ``RF:SPECTRogram:TIMe`` command.
        """
        return self._spectrogram

    @property
    def squelch(self) -> RfSquelch:
        """Return the ``RF:SQUELCH`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``RF:SQUELCH?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:SQUELCH?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``RF:SQUELCH:STATE`` command.
            - ``.threshold``: The ``RF:SQUELCH:THReshold`` command.
        """
        return self._squelch

    @property
    def start(self) -> RfStart:
        """Return the ``RF:STARt`` command.

        Description:
            - This command specifies to exclude frequencies below a certain level from use.

        Usage:
            - Using the ``.query()`` method will send the ``RF:STARt?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:STARt?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:STARt value`` command.

        SCPI Syntax:
            ```
            - RF:STARt <NR3>
            - RF:STARt?
            ```

        Info:
            - ``<NR3>`` is a floating point value that represents the Start frequency.
        """
        return self._start

    @property
    def stop(self) -> RfStop:
        """Return the ``RF:STOP`` command.

        Description:
            - This command specifies to exclude frequencies above a certain level from use.

        Usage:
            - Using the ``.query()`` method will send the ``RF:STOP?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:STOP?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:STOP value`` command.

        SCPI Syntax:
            ```
            - RF:STOP <NR3>
            - RF:STOP?
            ```

        Info:
            - ``<NR3>`` is a floating point value.
        """
        return self._stop

    @property
    def units(self) -> RfUnits:
        """Return the ``RF:UNIts`` command.

        Description:
            - This command specifies the vertical units to be used in all RF-related absolute
              logarithmic amplitudes.

        Usage:
            - Using the ``.query()`` method will send the ``RF:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:UNIts?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:UNIts value`` command.

        SCPI Syntax:
            ```
            - RF:UNIts {DBM|DBUW|DBMV|DBUV|DBMA|DBUA}
            - RF:UNIts?
            ```

        Info:
            - ``DBM`` - Decibel milliwatts.
            - ``DBUW`` - Decibel microwatts.
            - ``DBMV`` - Decibel millivolts.
            - ``DBUV`` - Decibel microvolts.
            - ``DBMA`` - Decibel milliamperes.
            - ``DBUA`` - Decibel microamperes.
        """
        return self._units

    @property
    def window(self) -> RfWindow:
        """Return the ``RF:WINdow`` command.

        Description:
            - This command specifies which window will be used for the windowing function, which is
              only used for the three time domain RF traces (RF Amplitude vs. Time, RF Frequency vs.
              Time and RF Phase vs. Time). The windowing function is a Fast Fourier Transform (FFT)
              technique used to minimize the discontinuities between successive frames of an RF time
              domain signal.

        Usage:
            - Using the ``.query()`` method will send the ``RF:WINdow?`` query.
            - Using the ``.verify(value)`` method will send the ``RF:WINdow?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RF:WINdow value`` command.

        SCPI Syntax:
            ```
            - RF:WINdow {RECTangular|HAMming|HANning|BLAckmanharris|KAIser|FLATtop}
            - RF:WINdow?
            ```

        Info:
            - ``RECTangular`` - window function equivalent to multiplying all gate data by one
              (sometimes known as a Dirichlet window).
            - ``HAMming`` - a high or moderate resolution window based on a cosine series.
            - ``HANning`` - a high or moderate resolution window based on a cosine series.
            - ``BLAckmanharris`` - a low-resolution (high dynamic range) window based on a cosine
              series.
            - ``KAIser`` - a high or moderate resolution window.
            - ``FLATtop`` - a low-resolution (high dynamic range) window.
        """
        return self._window
