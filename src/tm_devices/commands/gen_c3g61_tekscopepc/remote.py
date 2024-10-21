"""The remote commands module.

These commands are used in the following models:
TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - REMOTE:ACQMethod {CONTINuous|SINGLE|SEQuence}
    - REMOTE:ACQMethod?
    - REMOTE:ACQStatus?
    - REMOTE:ACQUIRE <NR1>
    - REMOTE:ADDNew <Qstring>
    - REMOTE:COMMInter {Visa|Socket}
    - REMOTE:COMMInter?
    - REMOTE:CONTROL <NR1>
    - REMOTE:CONTROL?
    - REMOTE:DELEte <Qstring>
    - REMOTE:LOGGING {START|PAUSE|STOP}
    - REMOTE:LOGGING?
    - REMOTE:NUMACq?
    - REMOTE:S<x>_CH<x>:DIGGRP:D<x>:THReshold <NR3>
    - REMOTE:S<x>_CH<x>:DIGGRP:D<x>:THReshold?
    - REMOTE:S<x>_CH<x>:DIGGRP:THReshold <NR3>
    - REMOTE:S<x>_CH<x>:DIGGRP:THReshold?
    - REMOTE:S<x>_CH<x>:PROBETYPE?
    - REMOTE:S<x>_CH<x>:SELect:DIGGRP:Dall {ON|OFF|<NR1>}
    - REMOTE:S<x>_CH<x>:SELect:DIGGRP:Dall?
    - REMOTE:S<x>_CH<x>:STAte <NR1>
    - REMOTE:S<x>_CH<x>:STAte?
    - REMOTE:S<x>_CH<x>:SV:CENTERFrequency <NR3>
    - REMOTE:S<x>_CH<x>:SV:CENTERFrequency?
    - REMOTE:S<x>_CH<x>:SV:POSition <NR3>
    - REMOTE:S<x>_CH<x>:SV:POSition?
    - REMOTE:S<x>_CH<x>:SV:STARTFrequency?
    - REMOTE:S<x>_CH<x>:SV:STATE {ON|OFF}
    - REMOTE:S<x>_CH<x>:SV:STATE?
    - REMOTE:S<x>_CH<x>:SV:STOPFrequency?
    - REMOTE:S<x>_DCH<x>:D<x>:THReshold <NR3>
    - REMOTE:S<x>_DCH<x>:D<x>:THReshold?
    - REMOTE:S<x>_DCH<x>:GROUP<x>THReshold <NR3>
    - REMOTE:S<x>_DCH<x>:GROUP<x>THReshold?
    - REMOTE:S<x>_DCH<x>:SELect:DAll {ON|OFF|<NR1>}
    - REMOTE:S<x>_DCH<x>:SELect:DAll?
    - REMOTE:SCOPe<x>:BANDWidth?
    - REMOTE:SCOPe<x>:CONNECT <NR1>
    - REMOTE:SCOPe<x>:CONNECTIONMessage?
    - REMOTE:SCOPe<x>:CONNECTIONState?
    - REMOTE:SCOPe<x>:DISCONNECT
    - REMOTE:SCOPe<x>:HORizontal:FASTframe:COUNt?
    - REMOTE:SCOPe<x>:HORizontal:FASTframe:MAXFrames?
    - REMOTE:SCOPe<x>:HORizontal:FASTframe:SELECTED?
    - REMOTE:SCOPe<x>:HORizontal:FASTframe:STATE?
    - REMOTE:SCOPe<x>:HORizontal:FASTframe:SUMFrame:STATE?
    - REMOTE:SCOPe<x>:HORizontal:FASTframe:SUMFrame?
    - REMOTE:SCOPe<x>:IPADDress <Qstring>
    - REMOTE:SCOPe<x>:IPADDress?
    - REMOTE:SCOPe<x>:MODELname?
    - REMOTE:SCOPe<x>:PORT <NR1>
    - REMOTE:SCOPe<x>:PORT?
    - REMOTE:SCOPe<x>:SYNC <NR1>
    - REMOTE:SCOPe<x>:State?
    - REMOTE:SCOPe<x>:VISACONNectiontype {Network|USB}
    - REMOTE:SCOPe<x>:VISACONNectiontype?
    - REMOTE:SEQuence:CURrent?
    - REMOTE:SEQuence:NUMSEQuence <NR1>
    - REMOTE:SEQuence:NUMSEQuence?
    - REMOTE:SV:RBW <NR3>
    - REMOTE:SV:RBW?
    - REMOTE:SV:RBWMode {AUTOmatic|MANual}
    - REMOTE:SV:RBWMode?
    - REMOTE:SV:SPAN <NR3>
    - REMOTE:SV:SPAN?
    - REMOTE:SV:SPANRBWRatio <NR3>
    - REMOTE:SV:SPANRBWRatio?
    - REMOTE:SV:WINDOW {KAISerbessel|RECTangular|HAMMing|HANNing|BLACkmanharris|FLATtop2}
    - REMOTE:SV:WINDOW?
    - REMOTE:USBDEscriptors {Usb<x>}
    - REMOTE:USBDEscriptors?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    SCPICmdWriteNoArguments,
    ValidatedChannel,
    ValidatedDigitalBit,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class RemoteUsbdescriptors(SCPICmdWrite, SCPICmdRead):
    """The ``REMOTE:USBDEscriptors`` command.

    Description:
        - This command sets or queries the USB descriptors available for remote connection.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:USBDEscriptors?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:USBDEscriptors?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REMOTE:USBDEscriptors value`` command.

    SCPI Syntax:
        ```
        - REMOTE:USBDEscriptors {Usb<x>}
        - REMOTE:USBDEscriptors?
        ```

    Info:
        - ``Usb0`` sets the usb address of the first specified scope.
        - ``Usb1`` sets the usb address of the second specified scope.
    """


class RemoteSvWindow(SCPICmdWrite, SCPICmdRead):
    """The ``REMOTE:SV:WINDOW`` command.

    Description:
        - This command sets or queries the window type used by the windowing function of the
          Spectrum View. The windowing function is a Fast Fourier Transform (FFT) technique used to
          minimize the discontinuities between successive frames of an RF time domain signal. The
          default window type is Blackman-Harris.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:SV:WINDOW?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:SV:WINDOW?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REMOTE:SV:WINDOW value`` command.

    SCPI Syntax:
        ```
        - REMOTE:SV:WINDOW {KAISerbessel|RECTangular|HAMMing|HANNing|BLACkmanharris|FLATtop2}
        - REMOTE:SV:WINDOW?
        ```

    Info:
        - ``KAISerbessel`` specifies the Kaiser-Bessel window type (a high or moderate resolution
          window).
        - ``RECTangular`` specifies the Rectangular window type (a window function is equivalent to
          multiplying all gate data by one).
        - ``HAMMing`` specifies the Hamming window type (a high or moderate resolution window based
          on a cosine series).
        - ``HANNing`` specifies the Hanning window type (a high or moderate resolution window based
          on a cosine series).
        - ``BLACkmanharris`` specifies the Blackman-Harris window type (a low-resolution (high
          dynamic range) window based on a cosine series).
        - ``FLATtop2`` specifies the Flattop2 window type (a low-resolution (high dynamic range)
          window).
    """


class RemoteSvSpanrbwratio(SCPICmdWrite, SCPICmdRead):
    """The ``REMOTE:SV:SPANRBWRatio`` command.

    Description:
        - This command sets or queries the ratio of the span to the resolution bandwidth (RBW) that
          will be used when the RBW Mode is set to AUTO. The span is the width of the frequency
          domain trace in Hz, which is equal to the stop frequency minus the start frequency. The
          RBW is the width of the narrowest measurable band of frequencies in a frequency domain
          trace. The default RBW ratio is 1000 : 1. Use the command ``REMOTE:SV:RBWMode`` to set the
          RBW Mode to Automatic.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:SV:SPANRBWRatio?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:SV:SPANRBWRatio?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REMOTE:SV:SPANRBWRatio value`` command.

    SCPI Syntax:
        ```
        - REMOTE:SV:SPANRBWRatio <NR3>
        - REMOTE:SV:SPANRBWRatio?
        ```

    Info:
        - ``<NR3>`` specifies the span-to-RBW ratio.
    """


class RemoteSvSpan(SCPICmdWrite, SCPICmdRead):
    """The ``REMOTE:SV:SPAN`` command.

    Description:
        - This command sets or queries the span setting for all channels in the Spectrum View. The
          span is the range of frequencies that can be observed centered on the center frequency.
          This is the width of the frequency domain trace, which is from the center frequency -
          ½span to the center frequency + ½ span.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:SV:SPAN?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:SV:SPAN?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REMOTE:SV:SPAN value`` command.

    SCPI Syntax:
        ```
        - REMOTE:SV:SPAN <NR3>
        - REMOTE:SV:SPAN?
        ```

    Info:
        - ``<NR3>`` specifies the span value in Hz.
    """


class RemoteSvRbwmode(SCPICmdWrite, SCPICmdRead):
    """The ``REMOTE:SV:RBWMode`` command.

    Description:
        - This command sets or queries the resolution bandwidth (RBW) mode, either Automatic or
          Manual.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:SV:RBWMode?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:SV:RBWMode?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REMOTE:SV:RBWMode value`` command.

    SCPI Syntax:
        ```
        - REMOTE:SV:RBWMode {AUTOmatic|MANual}
        - REMOTE:SV:RBWMode?
        ```

    Info:
        - ``AUTOmatic`` specifies the resolution bandwidth automatically as the span is changed. The
          default behavior is ``1000:1``, but you can set it to other values in a 1-2-5 sequence
          (e.g. 10000, 20000, 50000). To specify the RBW ratio that will be used when the mode is
          set to automatic, use the command ``REMOTE:SV:SPANRBWRatio``.
        - ``MANual`` specifies to set the resolution bandwidth, independently from the span, using
          the command ``REMOTE:SV:RBW``.
    """


class RemoteSvRbw(SCPICmdWrite, SCPICmdRead):
    """The ``REMOTE:SV:RBW`` command.

    Description:
        - This command sets or queries the resolution bandwidth (RBW) when the RBW mode has been set
          to MANUAL (using the command ``REMOTE:SV:RBWMode``). The resolution bandwidth is the width
          of the narrowest measurable band of frequencies in a Spectrum View trace. By default, the
          RBW tracks the span value in a ``1000:1`` ratio. The RBW determines the level to which the
          instrument can resolve individual frequencies in the frequency domain. For example, if the
          input signal contains two carriers separated by 1 kHz, you will not be able to
          discriminate between them unless the RBW is less than 1 kHz.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:SV:RBW?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:SV:RBW?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REMOTE:SV:RBW value`` command.

    SCPI Syntax:
        ```
        - REMOTE:SV:RBW <NR3>
        - REMOTE:SV:RBW?
        ```

    Info:
        - ``<NR3>`` specifies the width of the narrowest measurable band of frequencies in a
          Spectrum View trace, in Hz.
    """


class RemoteSv(SCPICmdRead):
    """The ``REMOTE:SV`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:SV?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:SV?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.rbw``: The ``REMOTE:SV:RBW`` command.
        - ``.rbwmode``: The ``REMOTE:SV:RBWMode`` command.
        - ``.span``: The ``REMOTE:SV:SPAN`` command.
        - ``.spanrbwratio``: The ``REMOTE:SV:SPANRBWRatio`` command.
        - ``.window``: The ``REMOTE:SV:WINDOW`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._rbw = RemoteSvRbw(device, f"{self._cmd_syntax}:RBW")
        self._rbwmode = RemoteSvRbwmode(device, f"{self._cmd_syntax}:RBWMode")
        self._span = RemoteSvSpan(device, f"{self._cmd_syntax}:SPAN")
        self._spanrbwratio = RemoteSvSpanrbwratio(device, f"{self._cmd_syntax}:SPANRBWRatio")
        self._window = RemoteSvWindow(device, f"{self._cmd_syntax}:WINDOW")

    @property
    def rbw(self) -> RemoteSvRbw:
        """Return the ``REMOTE:SV:RBW`` command.

        Description:
            - This command sets or queries the resolution bandwidth (RBW) when the RBW mode has been
              set to MANUAL (using the command ``REMOTE:SV:RBWMode``). The resolution bandwidth is
              the width of the narrowest measurable band of frequencies in a Spectrum View trace. By
              default, the RBW tracks the span value in a ``1000:1`` ratio. The RBW determines the
              level to which the instrument can resolve individual frequencies in the frequency
              domain. For example, if the input signal contains two carriers separated by 1 kHz, you
              will not be able to discriminate between them unless the RBW is less than 1 kHz.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:SV:RBW?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:SV:RBW?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REMOTE:SV:RBW value`` command.

        SCPI Syntax:
            ```
            - REMOTE:SV:RBW <NR3>
            - REMOTE:SV:RBW?
            ```

        Info:
            - ``<NR3>`` specifies the width of the narrowest measurable band of frequencies in a
              Spectrum View trace, in Hz.
        """
        return self._rbw

    @property
    def rbwmode(self) -> RemoteSvRbwmode:
        """Return the ``REMOTE:SV:RBWMode`` command.

        Description:
            - This command sets or queries the resolution bandwidth (RBW) mode, either Automatic or
              Manual.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:SV:RBWMode?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:SV:RBWMode?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REMOTE:SV:RBWMode value`` command.

        SCPI Syntax:
            ```
            - REMOTE:SV:RBWMode {AUTOmatic|MANual}
            - REMOTE:SV:RBWMode?
            ```

        Info:
            - ``AUTOmatic`` specifies the resolution bandwidth automatically as the span is changed.
              The default behavior is ``1000:1``, but you can set it to other values in a 1-2-5
              sequence (e.g. 10000, 20000, 50000). To specify the RBW ratio that will be used when
              the mode is set to automatic, use the command ``REMOTE:SV:SPANRBWRatio``.
            - ``MANual`` specifies to set the resolution bandwidth, independently from the span,
              using the command ``REMOTE:SV:RBW``.
        """
        return self._rbwmode

    @property
    def span(self) -> RemoteSvSpan:
        """Return the ``REMOTE:SV:SPAN`` command.

        Description:
            - This command sets or queries the span setting for all channels in the Spectrum View.
              The span is the range of frequencies that can be observed centered on the center
              frequency. This is the width of the frequency domain trace, which is from the center
              frequency - ½span to the center frequency + ½ span.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:SV:SPAN?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:SV:SPAN?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REMOTE:SV:SPAN value`` command.

        SCPI Syntax:
            ```
            - REMOTE:SV:SPAN <NR3>
            - REMOTE:SV:SPAN?
            ```

        Info:
            - ``<NR3>`` specifies the span value in Hz.
        """
        return self._span

    @property
    def spanrbwratio(self) -> RemoteSvSpanrbwratio:
        """Return the ``REMOTE:SV:SPANRBWRatio`` command.

        Description:
            - This command sets or queries the ratio of the span to the resolution bandwidth (RBW)
              that will be used when the RBW Mode is set to AUTO. The span is the width of the
              frequency domain trace in Hz, which is equal to the stop frequency minus the start
              frequency. The RBW is the width of the narrowest measurable band of frequencies in a
              frequency domain trace. The default RBW ratio is 1000 : 1. Use the command
              ``REMOTE:SV:RBWMode`` to set the RBW Mode to Automatic.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:SV:SPANRBWRatio?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:SV:SPANRBWRatio?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REMOTE:SV:SPANRBWRatio value``
              command.

        SCPI Syntax:
            ```
            - REMOTE:SV:SPANRBWRatio <NR3>
            - REMOTE:SV:SPANRBWRatio?
            ```

        Info:
            - ``<NR3>`` specifies the span-to-RBW ratio.
        """
        return self._spanrbwratio

    @property
    def window(self) -> RemoteSvWindow:
        """Return the ``REMOTE:SV:WINDOW`` command.

        Description:
            - This command sets or queries the window type used by the windowing function of the
              Spectrum View. The windowing function is a Fast Fourier Transform (FFT) technique used
              to minimize the discontinuities between successive frames of an RF time domain signal.
              The default window type is Blackman-Harris.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:SV:WINDOW?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:SV:WINDOW?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REMOTE:SV:WINDOW value`` command.

        SCPI Syntax:
            ```
            - REMOTE:SV:WINDOW {KAISerbessel|RECTangular|HAMMing|HANNing|BLACkmanharris|FLATtop2}
            - REMOTE:SV:WINDOW?
            ```

        Info:
            - ``KAISerbessel`` specifies the Kaiser-Bessel window type (a high or moderate
              resolution window).
            - ``RECTangular`` specifies the Rectangular window type (a window function is equivalent
              to multiplying all gate data by one).
            - ``HAMMing`` specifies the Hamming window type (a high or moderate resolution window
              based on a cosine series).
            - ``HANNing`` specifies the Hanning window type (a high or moderate resolution window
              based on a cosine series).
            - ``BLACkmanharris`` specifies the Blackman-Harris window type (a low-resolution (high
              dynamic range) window based on a cosine series).
            - ``FLATtop2`` specifies the Flattop2 window type (a low-resolution (high dynamic range)
              window).
        """
        return self._window


class RemoteSequenceNumsequence(SCPICmdWrite, SCPICmdRead):
    """The ``REMOTE:SEQuence:NUMSEQuence`` command.

    Description:
        - In single sequence acquisition mode, specify the number of acquisitions or measurements
          that comprise the sequence. The default is 1.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:SEQuence:NUMSEQuence?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:SEQuence:NUMSEQuence?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REMOTE:SEQuence:NUMSEQuence value``
          command.

    SCPI Syntax:
        ```
        - REMOTE:SEQuence:NUMSEQuence <NR1>
        - REMOTE:SEQuence:NUMSEQuence?
        ```

    Info:
        - ``<NR1>`` is the number of acquisitions or measurements that comprise the sequence.
    """


class RemoteSequenceCurrent(SCPICmdRead):
    """The ``REMOTE:SEQuence:CURrent`` command.

    Description:
        - In single sequence acquisition mode, this query returns the number of acquisitions or
          measurements in the sequence completed so far.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:SEQuence:CURrent?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:SEQuence:CURrent?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - REMOTE:SEQuence:CURrent?
        ```
    """


class RemoteSequence(SCPICmdRead):
    """The ``REMOTE:SEQuence`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:SEQuence?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:SEQuence?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.current``: The ``REMOTE:SEQuence:CURrent`` command.
        - ``.numsequence``: The ``REMOTE:SEQuence:NUMSEQuence`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._current = RemoteSequenceCurrent(device, f"{self._cmd_syntax}:CURrent")
        self._numsequence = RemoteSequenceNumsequence(device, f"{self._cmd_syntax}:NUMSEQuence")

    @property
    def current(self) -> RemoteSequenceCurrent:
        """Return the ``REMOTE:SEQuence:CURrent`` command.

        Description:
            - In single sequence acquisition mode, this query returns the number of acquisitions or
              measurements in the sequence completed so far.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:SEQuence:CURrent?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:SEQuence:CURrent?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - REMOTE:SEQuence:CURrent?
            ```
        """
        return self._current

    @property
    def numsequence(self) -> RemoteSequenceNumsequence:
        """Return the ``REMOTE:SEQuence:NUMSEQuence`` command.

        Description:
            - In single sequence acquisition mode, specify the number of acquisitions or
              measurements that comprise the sequence. The default is 1.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:SEQuence:NUMSEQuence?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:SEQuence:NUMSEQuence?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REMOTE:SEQuence:NUMSEQuence value``
              command.

        SCPI Syntax:
            ```
            - REMOTE:SEQuence:NUMSEQuence <NR1>
            - REMOTE:SEQuence:NUMSEQuence?
            ```

        Info:
            - ``<NR1>`` is the number of acquisitions or measurements that comprise the sequence.
        """
        return self._numsequence


class RemoteScopeItemVisaconnectiontype(SCPICmdWrite, SCPICmdRead):
    """The ``REMOTE:SCOPe<x>:VISACONNectiontype`` command.

    Description:
        - This command sets or queries VISA connection type for remote scope connection.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:SCOPe<x>:VISACONNectiontype?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:SCOPe<x>:VISACONNectiontype?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``REMOTE:SCOPe<x>:VISACONNectiontype value`` command.

    SCPI Syntax:
        ```
        - REMOTE:SCOPe<x>:VISACONNectiontype {Network|USB}
        - REMOTE:SCOPe<x>:VISACONNectiontype?
        ```

    Info:
        - ``SCOPe<x>`` specifies the remote scope number.
        - ``Network`` sets the remote scope connection type to Network.
        - ``USB`` sets the remote scope connection type to USB.
    """


class RemoteScopeItemState(SCPICmdRead):
    """The ``REMOTE:SCOPe<x>:State`` command.

    Description:
        - This command queries the connected state for the specified remote scope.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:SCOPe<x>:State?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:SCOPe<x>:State?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - REMOTE:SCOPe<x>:State?
        ```

    Info:
        - ``SCOPe<x>`` specifies the remote scope number.
    """


class RemoteScopeItemSync(SCPICmdWrite):
    """The ``REMOTE:SCOPe<x>:SYNC`` command.

    Description:
        - This command refreshes the channel data from the specified remote scope.

    Usage:
        - Using the ``.write(value)`` method will send the ``REMOTE:SCOPe<x>:SYNC value`` command.

    SCPI Syntax:
        ```
        - REMOTE:SCOPe<x>:SYNC <NR1>
        ```

    Info:
        - ``SCOPe<x>`` specifies the remote scope number.
        - ``<NR1>`` is the remote scope port number. The argument is of the form <NR1> where NR1 ≥
          1.
    """


class RemoteScopeItemPort(SCPICmdWrite, SCPICmdRead):
    """The ``REMOTE:SCOPe<x>:PORT`` command.

    Description:
        - This command sets or queries the port number for the specified remote scope.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:SCOPe<x>:PORT?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:SCOPe<x>:PORT?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REMOTE:SCOPe<x>:PORT value`` command.

    SCPI Syntax:
        ```
        - REMOTE:SCOPe<x>:PORT <NR1>
        - REMOTE:SCOPe<x>:PORT?
        ```

    Info:
        - ``SCOPe<x>`` specifies the remote scope number.
        - ``<NR1>`` is the remote scope port number. The argument is of the form <NR1> where NR1 ≥
          1.
    """


class RemoteScopeItemModelname(SCPICmdRead):
    """The ``REMOTE:SCOPe<x>:MODELname`` command.

    Description:
        - This command returns model name of the specified remote scope.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:SCOPe<x>:MODELname?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:SCOPe<x>:MODELname?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - REMOTE:SCOPe<x>:MODELname?
        ```

    Info:
        - ``SCOPe<x>`` specifies the remote scope number.
    """


class RemoteScopeItemIpaddress(SCPICmdWrite, SCPICmdRead):
    """The ``REMOTE:SCOPe<x>:IPADDress`` command.

    Description:
        - This command sets or queries the IP Address or host name for the specified remote scope.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:SCOPe<x>:IPADDress?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:SCOPe<x>:IPADDress?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REMOTE:SCOPe<x>:IPADDress value``
          command.

    SCPI Syntax:
        ```
        - REMOTE:SCOPe<x>:IPADDress <Qstring>
        - REMOTE:SCOPe<x>:IPADDress?
        ```

    Info:
        - ``SCOPe<x>`` specifies the remote scope number.
        - ``<Qstring>`` is the remote scope IP Address or host name. The argument is of the form
          'ScopeIPAddress'.
    """


class RemoteScopeItemHorizontalFastframeSumframeState(SCPICmdRead):
    """The ``REMOTE:SCOPe<x>:HORizontal:FASTframe:SUMFrame:STATE`` command.

    Description:
        - This command returns the state of FastFrame summary frame. Summary frame mode is set
          automatically based on the acquisition mode. When in Sample mode, the summary frame type
          is set to Average. When in Peak Detect mode, the summary frame type is set to Envelope.
          When in High Res mode, the summary frame type is set to Average. FastFrame on the Remote
          scope should be turned ON before connecting from TekScope.

    Usage:
        - Using the ``.query()`` method will send the
          ``REMOTE:SCOPe<x>:HORizontal:FASTframe:SUMFrame:STATE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``REMOTE:SCOPe<x>:HORizontal:FASTframe:SUMFrame:STATE?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - REMOTE:SCOPe<x>:HORizontal:FASTframe:SUMFrame:STATE?
        ```

    Info:
        - ``SCOPe<x>`` specifies the remote scope number.
    """


class RemoteScopeItemHorizontalFastframeSumframe(SCPICmdRead):
    """The ``REMOTE:SCOPe<x>:HORizontal:FASTframe:SUMFrame`` command.

    Description:
        - This command returns the summary frame type. Turning on Summary Frame does not adjust the
          numberFrames value as long as there is room for an additional frame. If there is not
          enough room then numberFrames will be reduced by 1. The numberFrames value is always the
          number of frames to acquire. FastFrame on the Remote scope should be turned ON before
          connecting from TekScope.

    Usage:
        - Using the ``.query()`` method will send the
          ``REMOTE:SCOPe<x>:HORizontal:FASTframe:SUMFrame?`` query.
        - Using the ``.verify(value)`` method will send the
          ``REMOTE:SCOPe<x>:HORizontal:FASTframe:SUMFrame?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - REMOTE:SCOPe<x>:HORizontal:FASTframe:SUMFrame?
        ```

    Info:
        - ``SCOPe<x>`` specifies the remote scope number.

    Properties:
        - ``.state``: The ``REMOTE:SCOPe<x>:HORizontal:FASTframe:SUMFrame:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = RemoteScopeItemHorizontalFastframeSumframeState(
            device, f"{self._cmd_syntax}:STATE"
        )

    @property
    def state(self) -> RemoteScopeItemHorizontalFastframeSumframeState:
        """Return the ``REMOTE:SCOPe<x>:HORizontal:FASTframe:SUMFrame:STATE`` command.

        Description:
            - This command returns the state of FastFrame summary frame. Summary frame mode is set
              automatically based on the acquisition mode. When in Sample mode, the summary frame
              type is set to Average. When in Peak Detect mode, the summary frame type is set to
              Envelope. When in High Res mode, the summary frame type is set to Average. FastFrame
              on the Remote scope should be turned ON before connecting from TekScope.

        Usage:
            - Using the ``.query()`` method will send the
              ``REMOTE:SCOPe<x>:HORizontal:FASTframe:SUMFrame:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``REMOTE:SCOPe<x>:HORizontal:FASTframe:SUMFrame:STATE?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - REMOTE:SCOPe<x>:HORizontal:FASTframe:SUMFrame:STATE?
            ```

        Info:
            - ``SCOPe<x>`` specifies the remote scope number.
        """
        return self._state


class RemoteScopeItemHorizontalFastframeState(SCPICmdRead):
    """The ``REMOTE:SCOPe<x>:HORizontal:FASTframe:STATE`` command.

    Description:
        - This command returns the state of FastFrame. Acquisition modes Envelope and Average are
          not compatible with FastFrame. If FastFrame is on, an attempted set to those acquisition
          modes will fail and revert to Sample mode. If FastFrame is turned on while in one of those
          acquisition modes, the acquisition mode is changed to Sample. FastFrame on the Remote
          scope should be turned ON before connecting from TekScope.

    Usage:
        - Using the ``.query()`` method will send the
          ``REMOTE:SCOPe<x>:HORizontal:FASTframe:STATE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``REMOTE:SCOPe<x>:HORizontal:FASTframe:STATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - REMOTE:SCOPe<x>:HORizontal:FASTframe:STATE?
        ```

    Info:
        - ``SCOPe<x>`` specifies the remote scope number.
    """


class RemoteScopeItemHorizontalFastframeSelected(SCPICmdRead):
    """The ``REMOTE:SCOPe<x>:HORizontal:FASTframe:SELECTED`` command.

    Description:
        - This command returns the selected frame number for acquired frames. Refs have their own
          selected frames. FastFrame on the Remote scope should be turned ON before connecting from
          TekScope.

    Usage:
        - Using the ``.query()`` method will send the
          ``REMOTE:SCOPe<x>:HORizontal:FASTframe:SELECTED?`` query.
        - Using the ``.verify(value)`` method will send the
          ``REMOTE:SCOPe<x>:HORizontal:FASTframe:SELECTED?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - REMOTE:SCOPe<x>:HORizontal:FASTframe:SELECTED?
        ```

    Info:
        - ``SCOPe<x>`` specifies the remote scope number.
    """


class RemoteScopeItemHorizontalFastframeMaxframes(SCPICmdRead):
    """The ``REMOTE:SCOPe<x>:HORizontal:FASTframe:MAXFrames`` command.

    Description:
        - This query returns the maximum number of frames. FastFrame on the Remote scope should be
          turned ON before connecting from TekScope.

    Usage:
        - Using the ``.query()`` method will send the
          ``REMOTE:SCOPe<x>:HORizontal:FASTframe:MAXFrames?`` query.
        - Using the ``.verify(value)`` method will send the
          ``REMOTE:SCOPe<x>:HORizontal:FASTframe:MAXFrames?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - REMOTE:SCOPe<x>:HORizontal:FASTframe:MAXFrames?
        ```

    Info:
        - ``SCOPe<x>`` specifies the remote scope number.
    """


class RemoteScopeItemHorizontalFastframeCount(SCPICmdRead):
    """The ``REMOTE:SCOPe<x>:HORizontal:FASTframe:COUNt`` command.

    Description:
        - This command returns the number of frames. FastFrame on the Remote scope should be turned
          ON before connecting from TekScope.

    Usage:
        - Using the ``.query()`` method will send the
          ``REMOTE:SCOPe<x>:HORizontal:FASTframe:COUNt?`` query.
        - Using the ``.verify(value)`` method will send the
          ``REMOTE:SCOPe<x>:HORizontal:FASTframe:COUNt?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - REMOTE:SCOPe<x>:HORizontal:FASTframe:COUNt?
        ```

    Info:
        - ``SCOPe<x>`` specifies the remote scope number.
    """


class RemoteScopeItemHorizontalFastframe(SCPICmdRead):
    """The ``REMOTE:SCOPe<x>:HORizontal:FASTframe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:SCOPe<x>:HORizontal:FASTframe?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``REMOTE:SCOPe<x>:HORizontal:FASTframe?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Info:
        - ``SCOPe<x>`` specifies the remote scope number.

    Properties:
        - ``.count``: The ``REMOTE:SCOPe<x>:HORizontal:FASTframe:COUNt`` command.
        - ``.maxframes``: The ``REMOTE:SCOPe<x>:HORizontal:FASTframe:MAXFrames`` command.
        - ``.selected``: The ``REMOTE:SCOPe<x>:HORizontal:FASTframe:SELECTED`` command.
        - ``.state``: The ``REMOTE:SCOPe<x>:HORizontal:FASTframe:STATE`` command.
        - ``.sumframe``: The ``REMOTE:SCOPe<x>:HORizontal:FASTframe:SUMFrame`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._count = RemoteScopeItemHorizontalFastframeCount(device, f"{self._cmd_syntax}:COUNt")
        self._maxframes = RemoteScopeItemHorizontalFastframeMaxframes(
            device, f"{self._cmd_syntax}:MAXFrames"
        )
        self._selected = RemoteScopeItemHorizontalFastframeSelected(
            device, f"{self._cmd_syntax}:SELECTED"
        )
        self._state = RemoteScopeItemHorizontalFastframeState(device, f"{self._cmd_syntax}:STATE")
        self._sumframe = RemoteScopeItemHorizontalFastframeSumframe(
            device, f"{self._cmd_syntax}:SUMFrame"
        )

    @property
    def count(self) -> RemoteScopeItemHorizontalFastframeCount:
        """Return the ``REMOTE:SCOPe<x>:HORizontal:FASTframe:COUNt`` command.

        Description:
            - This command returns the number of frames. FastFrame on the Remote scope should be
              turned ON before connecting from TekScope.

        Usage:
            - Using the ``.query()`` method will send the
              ``REMOTE:SCOPe<x>:HORizontal:FASTframe:COUNt?`` query.
            - Using the ``.verify(value)`` method will send the
              ``REMOTE:SCOPe<x>:HORizontal:FASTframe:COUNt?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - REMOTE:SCOPe<x>:HORizontal:FASTframe:COUNt?
            ```

        Info:
            - ``SCOPe<x>`` specifies the remote scope number.
        """
        return self._count

    @property
    def maxframes(self) -> RemoteScopeItemHorizontalFastframeMaxframes:
        """Return the ``REMOTE:SCOPe<x>:HORizontal:FASTframe:MAXFrames`` command.

        Description:
            - This query returns the maximum number of frames. FastFrame on the Remote scope should
              be turned ON before connecting from TekScope.

        Usage:
            - Using the ``.query()`` method will send the
              ``REMOTE:SCOPe<x>:HORizontal:FASTframe:MAXFrames?`` query.
            - Using the ``.verify(value)`` method will send the
              ``REMOTE:SCOPe<x>:HORizontal:FASTframe:MAXFrames?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - REMOTE:SCOPe<x>:HORizontal:FASTframe:MAXFrames?
            ```

        Info:
            - ``SCOPe<x>`` specifies the remote scope number.
        """
        return self._maxframes

    @property
    def selected(self) -> RemoteScopeItemHorizontalFastframeSelected:
        """Return the ``REMOTE:SCOPe<x>:HORizontal:FASTframe:SELECTED`` command.

        Description:
            - This command returns the selected frame number for acquired frames. Refs have their
              own selected frames. FastFrame on the Remote scope should be turned ON before
              connecting from TekScope.

        Usage:
            - Using the ``.query()`` method will send the
              ``REMOTE:SCOPe<x>:HORizontal:FASTframe:SELECTED?`` query.
            - Using the ``.verify(value)`` method will send the
              ``REMOTE:SCOPe<x>:HORizontal:FASTframe:SELECTED?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - REMOTE:SCOPe<x>:HORizontal:FASTframe:SELECTED?
            ```

        Info:
            - ``SCOPe<x>`` specifies the remote scope number.
        """
        return self._selected

    @property
    def state(self) -> RemoteScopeItemHorizontalFastframeState:
        """Return the ``REMOTE:SCOPe<x>:HORizontal:FASTframe:STATE`` command.

        Description:
            - This command returns the state of FastFrame. Acquisition modes Envelope and Average
              are not compatible with FastFrame. If FastFrame is on, an attempted set to those
              acquisition modes will fail and revert to Sample mode. If FastFrame is turned on while
              in one of those acquisition modes, the acquisition mode is changed to Sample.
              FastFrame on the Remote scope should be turned ON before connecting from TekScope.

        Usage:
            - Using the ``.query()`` method will send the
              ``REMOTE:SCOPe<x>:HORizontal:FASTframe:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``REMOTE:SCOPe<x>:HORizontal:FASTframe:STATE?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - REMOTE:SCOPe<x>:HORizontal:FASTframe:STATE?
            ```

        Info:
            - ``SCOPe<x>`` specifies the remote scope number.
        """
        return self._state

    @property
    def sumframe(self) -> RemoteScopeItemHorizontalFastframeSumframe:
        """Return the ``REMOTE:SCOPe<x>:HORizontal:FASTframe:SUMFrame`` command.

        Description:
            - This command returns the summary frame type. Turning on Summary Frame does not adjust
              the numberFrames value as long as there is room for an additional frame. If there is
              not enough room then numberFrames will be reduced by 1. The numberFrames value is
              always the number of frames to acquire. FastFrame on the Remote scope should be turned
              ON before connecting from TekScope.

        Usage:
            - Using the ``.query()`` method will send the
              ``REMOTE:SCOPe<x>:HORizontal:FASTframe:SUMFrame?`` query.
            - Using the ``.verify(value)`` method will send the
              ``REMOTE:SCOPe<x>:HORizontal:FASTframe:SUMFrame?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - REMOTE:SCOPe<x>:HORizontal:FASTframe:SUMFrame?
            ```

        Info:
            - ``SCOPe<x>`` specifies the remote scope number.

        Sub-properties:
            - ``.state``: The ``REMOTE:SCOPe<x>:HORizontal:FASTframe:SUMFrame:STATE`` command.
        """
        return self._sumframe


class RemoteScopeItemHorizontal(SCPICmdRead):
    """The ``REMOTE:SCOPe<x>:HORizontal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:SCOPe<x>:HORizontal?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:SCOPe<x>:HORizontal?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``SCOPe<x>`` specifies the remote scope number.

    Properties:
        - ``.fastframe``: The ``REMOTE:SCOPe<x>:HORizontal:FASTframe`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fastframe = RemoteScopeItemHorizontalFastframe(
            device, f"{self._cmd_syntax}:FASTframe"
        )

    @property
    def fastframe(self) -> RemoteScopeItemHorizontalFastframe:
        """Return the ``REMOTE:SCOPe<x>:HORizontal:FASTframe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:SCOPe<x>:HORizontal:FASTframe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``REMOTE:SCOPe<x>:HORizontal:FASTframe?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Info:
            - ``SCOPe<x>`` specifies the remote scope number.

        Sub-properties:
            - ``.count``: The ``REMOTE:SCOPe<x>:HORizontal:FASTframe:COUNt`` command.
            - ``.maxframes``: The ``REMOTE:SCOPe<x>:HORizontal:FASTframe:MAXFrames`` command.
            - ``.selected``: The ``REMOTE:SCOPe<x>:HORizontal:FASTframe:SELECTED`` command.
            - ``.state``: The ``REMOTE:SCOPe<x>:HORizontal:FASTframe:STATE`` command.
            - ``.sumframe``: The ``REMOTE:SCOPe<x>:HORizontal:FASTframe:SUMFrame`` command.
        """
        return self._fastframe


class RemoteScopeItemDisconnect(SCPICmdWriteNoArguments):
    """The ``REMOTE:SCOPe<x>:DISCONNECT`` command.

    Description:
        - This command disconnects the specified Remote Scope.

    Usage:
        - Using the ``.write()`` method will send the ``REMOTE:SCOPe<x>:DISCONNECT`` command.

    SCPI Syntax:
        ```
        - REMOTE:SCOPe<x>:DISCONNECT
        ```

    Info:
        - ``SCOPe<x>`` specifies the remote scope number.
        - ``<NR1>`` sets the Remote Scope to disconnect.
    """


class RemoteScopeItemConnectionstate(SCPICmdRead):
    """The ``REMOTE:SCOPe<x>:CONNECTIONState`` command.

    Description:
        - This command queries the connected state for the specified remote scope.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:SCOPe<x>:CONNECTIONState?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:SCOPe<x>:CONNECTIONState?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - REMOTE:SCOPe<x>:CONNECTIONState?
        ```

    Info:
        - ``SCOPe<x>`` specifies the remote scope number.
    """


class RemoteScopeItemConnectionmessage(SCPICmdRead):
    """The ``REMOTE:SCOPe<x>:CONNECTIONMessage`` command.

    Description:
        - This command queries the connection status message for the specified remote scope.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:SCOPe<x>:CONNECTIONMessage?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:SCOPe<x>:CONNECTIONMessage?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - REMOTE:SCOPe<x>:CONNECTIONMessage?
        ```

    Info:
        - ``SCOPe<x>`` specifies the remote scope number.
    """


class RemoteScopeItemConnect(SCPICmdWrite):
    """The ``REMOTE:SCOPe<x>:CONNECT`` command.

    Description:
        - This command connects the specified Remote Scope.

    Usage:
        - Using the ``.write(value)`` method will send the ``REMOTE:SCOPe<x>:CONNECT value``
          command.

    SCPI Syntax:
        ```
        - REMOTE:SCOPe<x>:CONNECT <NR1>
        ```

    Info:
        - ``SCOPe<x>`` specifies the remote scope number.
        - ``<NR1>`` sets the Remote Scope to connect to.
    """


class RemoteScopeItemBandwidth(SCPICmdRead):
    """The ``REMOTE:SCOPe<x>:BANDWidth`` command.

    Description:
        - This command queries the maximum licensed bandwidth of the specified remote scope.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:SCOPe<x>:BANDWidth?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:SCOPe<x>:BANDWidth?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - REMOTE:SCOPe<x>:BANDWidth?
        ```

    Info:
        - ``SCOPe<x>`` specifies the remote scope number.
    """


#  pylint: disable=too-many-instance-attributes
class RemoteScopeItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``REMOTE:SCOPe<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:SCOPe<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:SCOPe<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``SCOPe<x>`` specifies the remote scope number.

    Properties:
        - ``.bandwidth``: The ``REMOTE:SCOPe<x>:BANDWidth`` command.
        - ``.connect``: The ``REMOTE:SCOPe<x>:CONNECT`` command.
        - ``.connectionmessage``: The ``REMOTE:SCOPe<x>:CONNECTIONMessage`` command.
        - ``.connectionstate``: The ``REMOTE:SCOPe<x>:CONNECTIONState`` command.
        - ``.disconnect``: The ``REMOTE:SCOPe<x>:DISCONNECT`` command.
        - ``.horizontal``: The ``REMOTE:SCOPe<x>:HORizontal`` command tree.
        - ``.ipaddress``: The ``REMOTE:SCOPe<x>:IPADDress`` command.
        - ``.modelname``: The ``REMOTE:SCOPe<x>:MODELname`` command.
        - ``.port``: The ``REMOTE:SCOPe<x>:PORT`` command.
        - ``.sync``: The ``REMOTE:SCOPe<x>:SYNC`` command.
        - ``.state``: The ``REMOTE:SCOPe<x>:State`` command.
        - ``.visaconnectiontype``: The ``REMOTE:SCOPe<x>:VISACONNectiontype`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bandwidth = RemoteScopeItemBandwidth(device, f"{self._cmd_syntax}:BANDWidth")
        self._connect = RemoteScopeItemConnect(device, f"{self._cmd_syntax}:CONNECT")
        self._connectionmessage = RemoteScopeItemConnectionmessage(
            device, f"{self._cmd_syntax}:CONNECTIONMessage"
        )
        self._connectionstate = RemoteScopeItemConnectionstate(
            device, f"{self._cmd_syntax}:CONNECTIONState"
        )
        self._disconnect = RemoteScopeItemDisconnect(device, f"{self._cmd_syntax}:DISCONNECT")
        self._horizontal = RemoteScopeItemHorizontal(device, f"{self._cmd_syntax}:HORizontal")
        self._ipaddress = RemoteScopeItemIpaddress(device, f"{self._cmd_syntax}:IPADDress")
        self._modelname = RemoteScopeItemModelname(device, f"{self._cmd_syntax}:MODELname")
        self._port = RemoteScopeItemPort(device, f"{self._cmd_syntax}:PORT")
        self._sync = RemoteScopeItemSync(device, f"{self._cmd_syntax}:SYNC")
        self._state = RemoteScopeItemState(device, f"{self._cmd_syntax}:State")
        self._visaconnectiontype = RemoteScopeItemVisaconnectiontype(
            device, f"{self._cmd_syntax}:VISACONNectiontype"
        )

    @property
    def bandwidth(self) -> RemoteScopeItemBandwidth:
        """Return the ``REMOTE:SCOPe<x>:BANDWidth`` command.

        Description:
            - This command queries the maximum licensed bandwidth of the specified remote scope.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:SCOPe<x>:BANDWidth?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:SCOPe<x>:BANDWidth?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - REMOTE:SCOPe<x>:BANDWidth?
            ```

        Info:
            - ``SCOPe<x>`` specifies the remote scope number.
        """
        return self._bandwidth

    @property
    def connect(self) -> RemoteScopeItemConnect:
        """Return the ``REMOTE:SCOPe<x>:CONNECT`` command.

        Description:
            - This command connects the specified Remote Scope.

        Usage:
            - Using the ``.write(value)`` method will send the ``REMOTE:SCOPe<x>:CONNECT value``
              command.

        SCPI Syntax:
            ```
            - REMOTE:SCOPe<x>:CONNECT <NR1>
            ```

        Info:
            - ``SCOPe<x>`` specifies the remote scope number.
            - ``<NR1>`` sets the Remote Scope to connect to.
        """
        return self._connect

    @property
    def connectionmessage(self) -> RemoteScopeItemConnectionmessage:
        """Return the ``REMOTE:SCOPe<x>:CONNECTIONMessage`` command.

        Description:
            - This command queries the connection status message for the specified remote scope.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:SCOPe<x>:CONNECTIONMessage?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``REMOTE:SCOPe<x>:CONNECTIONMessage?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - REMOTE:SCOPe<x>:CONNECTIONMessage?
            ```

        Info:
            - ``SCOPe<x>`` specifies the remote scope number.
        """
        return self._connectionmessage

    @property
    def connectionstate(self) -> RemoteScopeItemConnectionstate:
        """Return the ``REMOTE:SCOPe<x>:CONNECTIONState`` command.

        Description:
            - This command queries the connected state for the specified remote scope.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:SCOPe<x>:CONNECTIONState?``
              query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:SCOPe<x>:CONNECTIONState?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - REMOTE:SCOPe<x>:CONNECTIONState?
            ```

        Info:
            - ``SCOPe<x>`` specifies the remote scope number.
        """
        return self._connectionstate

    @property
    def disconnect(self) -> RemoteScopeItemDisconnect:
        """Return the ``REMOTE:SCOPe<x>:DISCONNECT`` command.

        Description:
            - This command disconnects the specified Remote Scope.

        Usage:
            - Using the ``.write()`` method will send the ``REMOTE:SCOPe<x>:DISCONNECT`` command.

        SCPI Syntax:
            ```
            - REMOTE:SCOPe<x>:DISCONNECT
            ```

        Info:
            - ``SCOPe<x>`` specifies the remote scope number.
            - ``<NR1>`` sets the Remote Scope to disconnect.
        """
        return self._disconnect

    @property
    def horizontal(self) -> RemoteScopeItemHorizontal:
        """Return the ``REMOTE:SCOPe<x>:HORizontal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:SCOPe<x>:HORizontal?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:SCOPe<x>:HORizontal?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``SCOPe<x>`` specifies the remote scope number.

        Sub-properties:
            - ``.fastframe``: The ``REMOTE:SCOPe<x>:HORizontal:FASTframe`` command tree.
        """
        return self._horizontal

    @property
    def ipaddress(self) -> RemoteScopeItemIpaddress:
        """Return the ``REMOTE:SCOPe<x>:IPADDress`` command.

        Description:
            - This command sets or queries the IP Address or host name for the specified remote
              scope.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:SCOPe<x>:IPADDress?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:SCOPe<x>:IPADDress?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REMOTE:SCOPe<x>:IPADDress value``
              command.

        SCPI Syntax:
            ```
            - REMOTE:SCOPe<x>:IPADDress <Qstring>
            - REMOTE:SCOPe<x>:IPADDress?
            ```

        Info:
            - ``SCOPe<x>`` specifies the remote scope number.
            - ``<Qstring>`` is the remote scope IP Address or host name. The argument is of the form
              'ScopeIPAddress'.
        """
        return self._ipaddress

    @property
    def modelname(self) -> RemoteScopeItemModelname:
        """Return the ``REMOTE:SCOPe<x>:MODELname`` command.

        Description:
            - This command returns model name of the specified remote scope.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:SCOPe<x>:MODELname?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:SCOPe<x>:MODELname?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - REMOTE:SCOPe<x>:MODELname?
            ```

        Info:
            - ``SCOPe<x>`` specifies the remote scope number.
        """
        return self._modelname

    @property
    def port(self) -> RemoteScopeItemPort:
        """Return the ``REMOTE:SCOPe<x>:PORT`` command.

        Description:
            - This command sets or queries the port number for the specified remote scope.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:SCOPe<x>:PORT?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:SCOPe<x>:PORT?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REMOTE:SCOPe<x>:PORT value``
              command.

        SCPI Syntax:
            ```
            - REMOTE:SCOPe<x>:PORT <NR1>
            - REMOTE:SCOPe<x>:PORT?
            ```

        Info:
            - ``SCOPe<x>`` specifies the remote scope number.
            - ``<NR1>`` is the remote scope port number. The argument is of the form <NR1> where NR1
              ≥ 1.
        """
        return self._port

    @property
    def sync(self) -> RemoteScopeItemSync:
        """Return the ``REMOTE:SCOPe<x>:SYNC`` command.

        Description:
            - This command refreshes the channel data from the specified remote scope.

        Usage:
            - Using the ``.write(value)`` method will send the ``REMOTE:SCOPe<x>:SYNC value``
              command.

        SCPI Syntax:
            ```
            - REMOTE:SCOPe<x>:SYNC <NR1>
            ```

        Info:
            - ``SCOPe<x>`` specifies the remote scope number.
            - ``<NR1>`` is the remote scope port number. The argument is of the form <NR1> where NR1
              ≥ 1.
        """
        return self._sync

    @property
    def state(self) -> RemoteScopeItemState:
        """Return the ``REMOTE:SCOPe<x>:State`` command.

        Description:
            - This command queries the connected state for the specified remote scope.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:SCOPe<x>:State?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:SCOPe<x>:State?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - REMOTE:SCOPe<x>:State?
            ```

        Info:
            - ``SCOPe<x>`` specifies the remote scope number.
        """
        return self._state

    @property
    def visaconnectiontype(self) -> RemoteScopeItemVisaconnectiontype:
        """Return the ``REMOTE:SCOPe<x>:VISACONNectiontype`` command.

        Description:
            - This command sets or queries VISA connection type for remote scope connection.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:SCOPe<x>:VISACONNectiontype?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``REMOTE:SCOPe<x>:VISACONNectiontype?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``REMOTE:SCOPe<x>:VISACONNectiontype value`` command.

        SCPI Syntax:
            ```
            - REMOTE:SCOPe<x>:VISACONNectiontype {Network|USB}
            - REMOTE:SCOPe<x>:VISACONNectiontype?
            ```

        Info:
            - ``SCOPe<x>`` specifies the remote scope number.
            - ``Network`` sets the remote scope connection type to Network.
            - ``USB`` sets the remote scope connection type to USB.
        """
        return self._visaconnectiontype


class RemoteSItemDchItemSelectDall(SCPICmdWrite, SCPICmdRead):
    """The ``REMOTE:S<x>_DCH<x>:SELect:DAll`` command.

    Description:
        - This command turns on or off all constituent digital channels (D0 through D15) of the
          specified source channel. The scope and channel are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:S<x>_DCH<x>:SELect:DAll?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_DCH<x>:SELect:DAll?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REMOTE:S<x>_DCH<x>:SELect:DAll value``
          command.

    SCPI Syntax:
        ```
        - REMOTE:S<x>_DCH<x>:SELect:DAll {ON|OFF|<NR1>}
        - REMOTE:S<x>_DCH<x>:SELect:DAll?
        ```
    """


class RemoteSItemDchItemSelect(SCPICmdRead):
    """The ``REMOTE:S<x>_DCH<x>:SELect`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:S<x>_DCH<x>:SELect?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_DCH<x>:SELect?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.dall``: The ``REMOTE:S<x>_DCH<x>:SELect:DAll`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._dall = RemoteSItemDchItemSelectDall(device, f"{self._cmd_syntax}:DAll")

    @property
    def dall(self) -> RemoteSItemDchItemSelectDall:
        """Return the ``REMOTE:S<x>_DCH<x>:SELect:DAll`` command.

        Description:
            - This command turns on or off all constituent digital channels (D0 through D15) of the
              specified source channel. The scope and channel are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:S<x>_DCH<x>:SELect:DAll?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_DCH<x>:SELect:DAll?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``REMOTE:S<x>_DCH<x>:SELect:DAll value`` command.

        SCPI Syntax:
            ```
            - REMOTE:S<x>_DCH<x>:SELect:DAll {ON|OFF|<NR1>}
            - REMOTE:S<x>_DCH<x>:SELect:DAll?
            ```
        """
        return self._dall


class RemoteSItemDchItemGroupthresholdItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``REMOTE:S<x>_DCH<x>:GROUP<x>THReshold`` command.

    Description:
        - This command sets or queries the digital threshold of all bits in digital group 0 (D0-D7)
          or group 1 (D8-D15) on ``S<x>_DCH<x>``. The scope and channel are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:S<x>_DCH<x>:GROUP<x>THReshold?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``REMOTE:S<x>_DCH<x>:GROUP<x>THReshold?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``REMOTE:S<x>_DCH<x>:GROUP<x>THReshold value`` command.

    SCPI Syntax:
        ```
        - REMOTE:S<x>_DCH<x>:GROUP<x>THReshold <NR3>
        - REMOTE:S<x>_DCH<x>:GROUP<x>THReshold?
        ```
    """


class RemoteSItemDchItemDigitalBitThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``REMOTE:S<x>_DCH<x>:D<x>:THReshold`` command.

    Description:
        - This command sets or queries the threshold level in volts for the specified digital
          channel. The scope, channel, and digital channel bit number (0-15) are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:S<x>_DCH<x>:D<x>:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_DCH<x>:D<x>:THReshold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``REMOTE:S<x>_DCH<x>:D<x>:THReshold value`` command.

    SCPI Syntax:
        ```
        - REMOTE:S<x>_DCH<x>:D<x>:THReshold <NR3>
        - REMOTE:S<x>_DCH<x>:D<x>:THReshold?
        ```
    """


class RemoteSItemDchItemDigitalBit(ValidatedDigitalBit, SCPICmdRead):
    """The ``REMOTE:S<x>_DCH<x>:D<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:S<x>_DCH<x>:D<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_DCH<x>:D<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.threshold``: The ``REMOTE:S<x>_DCH<x>:D<x>:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._threshold = RemoteSItemDchItemDigitalBitThreshold(
            device, f"{self._cmd_syntax}:THReshold"
        )

    @property
    def threshold(self) -> RemoteSItemDchItemDigitalBitThreshold:
        """Return the ``REMOTE:S<x>_DCH<x>:D<x>:THReshold`` command.

        Description:
            - This command sets or queries the threshold level in volts for the specified digital
              channel. The scope, channel, and digital channel bit number (0-15) are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:S<x>_DCH<x>:D<x>:THReshold?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``REMOTE:S<x>_DCH<x>:D<x>:THReshold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``REMOTE:S<x>_DCH<x>:D<x>:THReshold value`` command.

        SCPI Syntax:
            ```
            - REMOTE:S<x>_DCH<x>:D<x>:THReshold <NR3>
            - REMOTE:S<x>_DCH<x>:D<x>:THReshold?
            ```
        """
        return self._threshold


class RemoteSItemDchItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``REMOTE:S<x>_DCH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:S<x>_DCH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_DCH<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.d``: The ``REMOTE:S<x>_DCH<x>:D<x>`` command tree.
        - ``.groupthreshold``: The ``REMOTE:S<x>_DCH<x>:GROUP<x>THReshold`` command.
        - ``.select``: The ``REMOTE:S<x>_DCH<x>:SELect`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._d: Dict[int, RemoteSItemDchItemDigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: RemoteSItemDchItemDigitalBit(device, f"{self._cmd_syntax}:D{x}")
        )
        self._groupthreshold: Dict[int, RemoteSItemDchItemGroupthresholdItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: RemoteSItemDchItemGroupthresholdItem(
                    device, f"{self._cmd_syntax}:GROUP{x}THReshold"
                )
            )
        )
        self._select = RemoteSItemDchItemSelect(device, f"{self._cmd_syntax}:SELect")

    @property
    def d(self) -> Dict[int, RemoteSItemDchItemDigitalBit]:
        """Return the ``REMOTE:S<x>_DCH<x>:D<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:S<x>_DCH<x>:D<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_DCH<x>:D<x>?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.threshold``: The ``REMOTE:S<x>_DCH<x>:D<x>:THReshold`` command.
        """
        return self._d

    @property
    def groupthreshold(self) -> Dict[int, RemoteSItemDchItemGroupthresholdItem]:
        """Return the ``REMOTE:S<x>_DCH<x>:GROUP<x>THReshold`` command.

        Description:
            - This command sets or queries the digital threshold of all bits in digital group 0
              (D0-D7) or group 1 (D8-D15) on ``S<x>_DCH<x>``. The scope and channel are specified by
              x.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:S<x>_DCH<x>:GROUP<x>THReshold?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``REMOTE:S<x>_DCH<x>:GROUP<x>THReshold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``REMOTE:S<x>_DCH<x>:GROUP<x>THReshold value`` command.

        SCPI Syntax:
            ```
            - REMOTE:S<x>_DCH<x>:GROUP<x>THReshold <NR3>
            - REMOTE:S<x>_DCH<x>:GROUP<x>THReshold?
            ```
        """
        return self._groupthreshold

    @property
    def select(self) -> RemoteSItemDchItemSelect:
        """Return the ``REMOTE:S<x>_DCH<x>:SELect`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:S<x>_DCH<x>:SELect?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_DCH<x>:SELect?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.dall``: The ``REMOTE:S<x>_DCH<x>:SELect:DAll`` command.
        """
        return self._select


class RemoteSItemChannelSvStopfrequency(SCPICmdRead):
    """The ``REMOTE:S<x>_CH<x>:SV:STOPFrequency`` command.

    Description:
        - This command queries the stop frequency of the specified spectrum trace channel in the
          Spectrum View window. S<x> is the remote scope number and Ch<x> is the channel number.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:SV:STOPFrequency?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_CH<x>:SV:STOPFrequency?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - REMOTE:S<x>_CH<x>:SV:STOPFrequency?
        ```
    """


class RemoteSItemChannelSvState(SCPICmdWrite, SCPICmdRead):
    """The ``REMOTE:S<x>_CH<x>:SV:STATE`` command.

    Description:
        - This command sets or queries the on/off setting of data acquisition for the specified
          spectrum trace channel. S<x> is the remote scope number and Ch<x> is the channel number.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:SV:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_CH<x>:SV:STATE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REMOTE:S<x>_CH<x>:SV:STATE value``
          command.

    SCPI Syntax:
        ```
        - REMOTE:S<x>_CH<x>:SV:STATE {ON|OFF}
        - REMOTE:S<x>_CH<x>:SV:STATE?
        ```

    Info:
        - ``ON`` enables spectrum data acquisition for the specified spectrum trace channel source.
        - ``OFF`` disables spectrum data acquisition for the specified spectrum trace channel
          source.
    """


class RemoteSItemChannelSvStartfrequency(SCPICmdRead):
    """The ``REMOTE:S<x>_CH<x>:SV:STARTFrequency`` command.

    Description:
        - This command queries the start frequency of the specified spectrum trace channel in the
          Spectrum View window. S<x> is the remote scope number and Ch<x> is the channel number.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:SV:STARTFrequency?``
          query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_CH<x>:SV:STARTFrequency?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - REMOTE:S<x>_CH<x>:SV:STARTFrequency?
        ```
    """


class RemoteSItemChannelSvPosition(SCPICmdWrite, SCPICmdRead):
    """The ``REMOTE:S<x>_CH<x>:SV:POSition`` command.

    Description:
        - This command sets or queries the Spectrum Time setting of the specified spectrum trace
          channel in the Spectrum View. Remote scope and channel are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:SV:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_CH<x>:SV:POSition?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REMOTE:S<x>_CH<x>:SV:POSition value``
          command.

    SCPI Syntax:
        ```
        - REMOTE:S<x>_CH<x>:SV:POSition <NR3>
        - REMOTE:S<x>_CH<x>:SV:POSition?
        ```

    Info:
        - ``<NR3>`` specifies the spectrum time location, as a percentage of the record length. The
          range of values is 0.0% to 100%.
    """


class RemoteSItemChannelSvCenterfrequency(SCPICmdWrite, SCPICmdRead):
    """The ``REMOTE:S<x>_CH<x>:SV:CENTERFrequency`` command.

    Description:
        - This command sets or queries the center frequency of the specified spectrum trace channel
          for Spectrum View. The scope and channel are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:SV:CENTERFrequency?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``REMOTE:S<x>_CH<x>:SV:CENTERFrequency?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``REMOTE:S<x>_CH<x>:SV:CENTERFrequency value`` command.

    SCPI Syntax:
        ```
        - REMOTE:S<x>_CH<x>:SV:CENTERFrequency <NR3>
        - REMOTE:S<x>_CH<x>:SV:CENTERFrequency?
        ```

    Info:
        - ``<NR3>`` specifies the spectrum trace center frequency for the specified channel, in
          hertz. The range of values is 0.0 to the maximum licensed bandwidth of the instrument.
    """


class RemoteSItemChannelSv(SCPICmdRead):
    """The ``REMOTE:S<x>_CH<x>:SV`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:SV?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_CH<x>:SV?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.centerfrequency``: The ``REMOTE:S<x>_CH<x>:SV:CENTERFrequency`` command.
        - ``.position``: The ``REMOTE:S<x>_CH<x>:SV:POSition`` command.
        - ``.startfrequency``: The ``REMOTE:S<x>_CH<x>:SV:STARTFrequency`` command.
        - ``.state``: The ``REMOTE:S<x>_CH<x>:SV:STATE`` command.
        - ``.stopfrequency``: The ``REMOTE:S<x>_CH<x>:SV:STOPFrequency`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._centerfrequency = RemoteSItemChannelSvCenterfrequency(
            device, f"{self._cmd_syntax}:CENTERFrequency"
        )
        self._position = RemoteSItemChannelSvPosition(device, f"{self._cmd_syntax}:POSition")
        self._startfrequency = RemoteSItemChannelSvStartfrequency(
            device, f"{self._cmd_syntax}:STARTFrequency"
        )
        self._state = RemoteSItemChannelSvState(device, f"{self._cmd_syntax}:STATE")
        self._stopfrequency = RemoteSItemChannelSvStopfrequency(
            device, f"{self._cmd_syntax}:STOPFrequency"
        )

    @property
    def centerfrequency(self) -> RemoteSItemChannelSvCenterfrequency:
        """Return the ``REMOTE:S<x>_CH<x>:SV:CENTERFrequency`` command.

        Description:
            - This command sets or queries the center frequency of the specified spectrum trace
              channel for Spectrum View. The scope and channel are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:SV:CENTERFrequency?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``REMOTE:S<x>_CH<x>:SV:CENTERFrequency?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``REMOTE:S<x>_CH<x>:SV:CENTERFrequency value`` command.

        SCPI Syntax:
            ```
            - REMOTE:S<x>_CH<x>:SV:CENTERFrequency <NR3>
            - REMOTE:S<x>_CH<x>:SV:CENTERFrequency?
            ```

        Info:
            - ``<NR3>`` specifies the spectrum trace center frequency for the specified channel, in
              hertz. The range of values is 0.0 to the maximum licensed bandwidth of the instrument.
        """
        return self._centerfrequency

    @property
    def position(self) -> RemoteSItemChannelSvPosition:
        """Return the ``REMOTE:S<x>_CH<x>:SV:POSition`` command.

        Description:
            - This command sets or queries the Spectrum Time setting of the specified spectrum trace
              channel in the Spectrum View. Remote scope and channel are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:SV:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_CH<x>:SV:POSition?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``REMOTE:S<x>_CH<x>:SV:POSition value`` command.

        SCPI Syntax:
            ```
            - REMOTE:S<x>_CH<x>:SV:POSition <NR3>
            - REMOTE:S<x>_CH<x>:SV:POSition?
            ```

        Info:
            - ``<NR3>`` specifies the spectrum time location, as a percentage of the record length.
              The range of values is 0.0% to 100%.
        """
        return self._position

    @property
    def startfrequency(self) -> RemoteSItemChannelSvStartfrequency:
        """Return the ``REMOTE:S<x>_CH<x>:SV:STARTFrequency`` command.

        Description:
            - This command queries the start frequency of the specified spectrum trace channel in
              the Spectrum View window. S<x> is the remote scope number and Ch<x> is the channel
              number.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:SV:STARTFrequency?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``REMOTE:S<x>_CH<x>:SV:STARTFrequency?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - REMOTE:S<x>_CH<x>:SV:STARTFrequency?
            ```
        """
        return self._startfrequency

    @property
    def state(self) -> RemoteSItemChannelSvState:
        """Return the ``REMOTE:S<x>_CH<x>:SV:STATE`` command.

        Description:
            - This command sets or queries the on/off setting of data acquisition for the specified
              spectrum trace channel. S<x> is the remote scope number and Ch<x> is the channel
              number.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:SV:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_CH<x>:SV:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REMOTE:S<x>_CH<x>:SV:STATE value``
              command.

        SCPI Syntax:
            ```
            - REMOTE:S<x>_CH<x>:SV:STATE {ON|OFF}
            - REMOTE:S<x>_CH<x>:SV:STATE?
            ```

        Info:
            - ``ON`` enables spectrum data acquisition for the specified spectrum trace channel
              source.
            - ``OFF`` disables spectrum data acquisition for the specified spectrum trace channel
              source.
        """
        return self._state

    @property
    def stopfrequency(self) -> RemoteSItemChannelSvStopfrequency:
        """Return the ``REMOTE:S<x>_CH<x>:SV:STOPFrequency`` command.

        Description:
            - This command queries the stop frequency of the specified spectrum trace channel in the
              Spectrum View window. S<x> is the remote scope number and Ch<x> is the channel number.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:SV:STOPFrequency?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``REMOTE:S<x>_CH<x>:SV:STOPFrequency?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - REMOTE:S<x>_CH<x>:SV:STOPFrequency?
            ```
        """
        return self._stopfrequency


class RemoteSItemChannelState(SCPICmdWrite, SCPICmdRead):
    """The ``REMOTE:S<x>_CH<x>:STAte`` command.

    Description:
        - This command sets or queries the state of the specified remote channel in the specified
          Waveform View.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:STAte?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_CH<x>:STAte?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REMOTE:S<x>_CH<x>:STAte value``
          command.

    SCPI Syntax:
        ```
        - REMOTE:S<x>_CH<x>:STAte <NR1>
        - REMOTE:S<x>_CH<x>:STAte?
        ```

    Info:
        - ``S<x>`` indicates the remote scope.
        - ``CH<x>`` indicates the channel number associated with remote scope.
        - ``<NR1>`` sets the channel state value 0 or 1. 0 sets the channel state to false. 1 sets
          the channel state to true.
    """


class RemoteSItemChannelSelectDiggrpDall(SCPICmdWrite, SCPICmdRead):
    """The ``REMOTE:S<x>_CH<x>:SELect:DIGGRP:Dall`` command.

    Description:
        - This command sets or queries the display state of the specified digital channel in the
          specified Waveform View. The scope and channel are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:SELect:DIGGRP:Dall?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``REMOTE:S<x>_CH<x>:SELect:DIGGRP:Dall?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``REMOTE:S<x>_CH<x>:SELect:DIGGRP:Dall value`` command.

    SCPI Syntax:
        ```
        - REMOTE:S<x>_CH<x>:SELect:DIGGRP:Dall {ON|OFF|<NR1>}
        - REMOTE:S<x>_CH<x>:SELect:DIGGRP:Dall?
        ```

    Info:
        - ``<NR1>`` sets the display state. 0 disables the display of the specified channels on the
          specified Waveform View; any other value turns this feature on.
        - ``OFF`` disables the display of the specified channels on the specified Waveform View.
        - ``ON`` enables the display of the specified channels on the specified Waveform View.
    """


class RemoteSItemChannelSelectDiggrp(SCPICmdRead):
    """The ``REMOTE:S<x>_CH<x>:SELect:DIGGRP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:SELect:DIGGRP?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_CH<x>:SELect:DIGGRP?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.dall``: The ``REMOTE:S<x>_CH<x>:SELect:DIGGRP:Dall`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._dall = RemoteSItemChannelSelectDiggrpDall(device, f"{self._cmd_syntax}:Dall")

    @property
    def dall(self) -> RemoteSItemChannelSelectDiggrpDall:
        """Return the ``REMOTE:S<x>_CH<x>:SELect:DIGGRP:Dall`` command.

        Description:
            - This command sets or queries the display state of the specified digital channel in the
              specified Waveform View. The scope and channel are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:SELect:DIGGRP:Dall?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``REMOTE:S<x>_CH<x>:SELect:DIGGRP:Dall?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``REMOTE:S<x>_CH<x>:SELect:DIGGRP:Dall value`` command.

        SCPI Syntax:
            ```
            - REMOTE:S<x>_CH<x>:SELect:DIGGRP:Dall {ON|OFF|<NR1>}
            - REMOTE:S<x>_CH<x>:SELect:DIGGRP:Dall?
            ```

        Info:
            - ``<NR1>`` sets the display state. 0 disables the display of the specified channels on
              the specified Waveform View; any other value turns this feature on.
            - ``OFF`` disables the display of the specified channels on the specified Waveform View.
            - ``ON`` enables the display of the specified channels on the specified Waveform View.
        """
        return self._dall


class RemoteSItemChannelSelect(SCPICmdRead):
    """The ``REMOTE:S<x>_CH<x>:SELect`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:SELect?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_CH<x>:SELect?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.diggrp``: The ``REMOTE:S<x>_CH<x>:SELect:DIGGRP`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._diggrp = RemoteSItemChannelSelectDiggrp(device, f"{self._cmd_syntax}:DIGGRP")

    @property
    def diggrp(self) -> RemoteSItemChannelSelectDiggrp:
        """Return the ``REMOTE:S<x>_CH<x>:SELect:DIGGRP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:SELect:DIGGRP?``
              query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_CH<x>:SELect:DIGGRP?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.dall``: The ``REMOTE:S<x>_CH<x>:SELect:DIGGRP:Dall`` command.
        """
        return self._diggrp


class RemoteSItemChannelProbetype(SCPICmdRead):
    """The ``REMOTE:S<x>_CH<x>:PROBETYPE`` command.

    Description:
        - This command returns the probe type connected to the specified channel. Remote scope and
          channel are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:PROBETYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_CH<x>:PROBETYPE?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - REMOTE:S<x>_CH<x>:PROBETYPE?
        ```
    """


class RemoteSItemChannelDiggrpThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``REMOTE:S<x>_CH<x>:DIGGRP:THReshold`` command.

    Description:
        - This command sets or queries the threshold level in volts for the specified remote scope
          channel. The scope and channel are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:DIGGRP:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_CH<x>:DIGGRP:THReshold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``REMOTE:S<x>_CH<x>:DIGGRP:THReshold value`` command.

    SCPI Syntax:
        ```
        - REMOTE:S<x>_CH<x>:DIGGRP:THReshold <NR3>
        - REMOTE:S<x>_CH<x>:DIGGRP:THReshold?
        ```

    Info:
        - ``<NR3>`` is the threshold level in volts for the specified remote scope digital channel.
    """


class RemoteSItemChannelDiggrpDigitalBitThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``REMOTE:S<x>_CH<x>:DIGGRP:D<x>:THReshold`` command.

    Description:
        - This command sets or queries the threshold level in volts for the specified digital
          channel. If the source channel doesn't exist, a hardware missing error event is set. The
          scope, channel, and digital channel bit number (0-7) are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:DIGGRP:D<x>:THReshold?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``REMOTE:S<x>_CH<x>:DIGGRP:D<x>:THReshold?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``REMOTE:S<x>_CH<x>:DIGGRP:D<x>:THReshold value`` command.

    SCPI Syntax:
        ```
        - REMOTE:S<x>_CH<x>:DIGGRP:D<x>:THReshold <NR3>
        - REMOTE:S<x>_CH<x>:DIGGRP:D<x>:THReshold?
        ```

    Info:
        - ``<NR3>`` is the threshold level in volts for the specified digital channel.
    """


class RemoteSItemChannelDiggrpDigitalBit(ValidatedDigitalBit, SCPICmdRead):
    """The ``REMOTE:S<x>_CH<x>:DIGGRP:D<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:DIGGRP:D<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_CH<x>:DIGGRP:D<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.threshold``: The ``REMOTE:S<x>_CH<x>:DIGGRP:D<x>:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._threshold = RemoteSItemChannelDiggrpDigitalBitThreshold(
            device, f"{self._cmd_syntax}:THReshold"
        )

    @property
    def threshold(self) -> RemoteSItemChannelDiggrpDigitalBitThreshold:
        """Return the ``REMOTE:S<x>_CH<x>:DIGGRP:D<x>:THReshold`` command.

        Description:
            - This command sets or queries the threshold level in volts for the specified digital
              channel. If the source channel doesn't exist, a hardware missing error event is set.
              The scope, channel, and digital channel bit number (0-7) are specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``REMOTE:S<x>_CH<x>:DIGGRP:D<x>:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the
              ``REMOTE:S<x>_CH<x>:DIGGRP:D<x>:THReshold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``REMOTE:S<x>_CH<x>:DIGGRP:D<x>:THReshold value`` command.

        SCPI Syntax:
            ```
            - REMOTE:S<x>_CH<x>:DIGGRP:D<x>:THReshold <NR3>
            - REMOTE:S<x>_CH<x>:DIGGRP:D<x>:THReshold?
            ```

        Info:
            - ``<NR3>`` is the threshold level in volts for the specified digital channel.
        """
        return self._threshold


class RemoteSItemChannelDiggrp(SCPICmdRead):
    """The ``REMOTE:S<x>_CH<x>:DIGGRP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:DIGGRP?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_CH<x>:DIGGRP?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.d``: The ``REMOTE:S<x>_CH<x>:DIGGRP:D<x>`` command tree.
        - ``.threshold``: The ``REMOTE:S<x>_CH<x>:DIGGRP:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._d: Dict[int, RemoteSItemChannelDiggrpDigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: RemoteSItemChannelDiggrpDigitalBit(device, f"{self._cmd_syntax}:D{x}")
        )
        self._threshold = RemoteSItemChannelDiggrpThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def d(self) -> Dict[int, RemoteSItemChannelDiggrpDigitalBit]:
        """Return the ``REMOTE:S<x>_CH<x>:DIGGRP:D<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:DIGGRP:D<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_CH<x>:DIGGRP:D<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.threshold``: The ``REMOTE:S<x>_CH<x>:DIGGRP:D<x>:THReshold`` command.
        """
        return self._d

    @property
    def threshold(self) -> RemoteSItemChannelDiggrpThreshold:
        """Return the ``REMOTE:S<x>_CH<x>:DIGGRP:THReshold`` command.

        Description:
            - This command sets or queries the threshold level in volts for the specified remote
              scope channel. The scope and channel are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:DIGGRP:THReshold?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``REMOTE:S<x>_CH<x>:DIGGRP:THReshold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``REMOTE:S<x>_CH<x>:DIGGRP:THReshold value`` command.

        SCPI Syntax:
            ```
            - REMOTE:S<x>_CH<x>:DIGGRP:THReshold <NR3>
            - REMOTE:S<x>_CH<x>:DIGGRP:THReshold?
            ```

        Info:
            - ``<NR3>`` is the threshold level in volts for the specified remote scope digital
              channel.
        """
        return self._threshold


class RemoteSItemChannel(ValidatedChannel, SCPICmdRead):
    """The ``REMOTE:S<x>_CH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_CH<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.diggrp``: The ``REMOTE:S<x>_CH<x>:DIGGRP`` command tree.
        - ``.probetype``: The ``REMOTE:S<x>_CH<x>:PROBETYPE`` command.
        - ``.select``: The ``REMOTE:S<x>_CH<x>:SELect`` command tree.
        - ``.state``: The ``REMOTE:S<x>_CH<x>:STAte`` command.
        - ``.sv``: The ``REMOTE:S<x>_CH<x>:SV`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._diggrp = RemoteSItemChannelDiggrp(device, f"{self._cmd_syntax}:DIGGRP")
        self._probetype = RemoteSItemChannelProbetype(device, f"{self._cmd_syntax}:PROBETYPE")
        self._select = RemoteSItemChannelSelect(device, f"{self._cmd_syntax}:SELect")
        self._state = RemoteSItemChannelState(device, f"{self._cmd_syntax}:STAte")
        self._sv = RemoteSItemChannelSv(device, f"{self._cmd_syntax}:SV")

    @property
    def diggrp(self) -> RemoteSItemChannelDiggrp:
        """Return the ``REMOTE:S<x>_CH<x>:DIGGRP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:DIGGRP?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_CH<x>:DIGGRP?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.d``: The ``REMOTE:S<x>_CH<x>:DIGGRP:D<x>`` command tree.
            - ``.threshold``: The ``REMOTE:S<x>_CH<x>:DIGGRP:THReshold`` command.
        """
        return self._diggrp

    @property
    def probetype(self) -> RemoteSItemChannelProbetype:
        """Return the ``REMOTE:S<x>_CH<x>:PROBETYPE`` command.

        Description:
            - This command returns the probe type connected to the specified channel. Remote scope
              and channel are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:PROBETYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_CH<x>:PROBETYPE?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - REMOTE:S<x>_CH<x>:PROBETYPE?
            ```
        """
        return self._probetype

    @property
    def select(self) -> RemoteSItemChannelSelect:
        """Return the ``REMOTE:S<x>_CH<x>:SELect`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:SELect?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_CH<x>:SELect?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.diggrp``: The ``REMOTE:S<x>_CH<x>:SELect:DIGGRP`` command tree.
        """
        return self._select

    @property
    def state(self) -> RemoteSItemChannelState:
        """Return the ``REMOTE:S<x>_CH<x>:STAte`` command.

        Description:
            - This command sets or queries the state of the specified remote channel in the
              specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:STAte?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_CH<x>:STAte?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REMOTE:S<x>_CH<x>:STAte value``
              command.

        SCPI Syntax:
            ```
            - REMOTE:S<x>_CH<x>:STAte <NR1>
            - REMOTE:S<x>_CH<x>:STAte?
            ```

        Info:
            - ``S<x>`` indicates the remote scope.
            - ``CH<x>`` indicates the channel number associated with remote scope.
            - ``<NR1>`` sets the channel state value 0 or 1. 0 sets the channel state to false. 1
              sets the channel state to true.
        """
        return self._state

    @property
    def sv(self) -> RemoteSItemChannelSv:
        """Return the ``REMOTE:S<x>_CH<x>:SV`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>:SV?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_CH<x>:SV?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.centerfrequency``: The ``REMOTE:S<x>_CH<x>:SV:CENTERFrequency`` command.
            - ``.position``: The ``REMOTE:S<x>_CH<x>:SV:POSition`` command.
            - ``.startfrequency``: The ``REMOTE:S<x>_CH<x>:SV:STARTFrequency`` command.
            - ``.state``: The ``REMOTE:S<x>_CH<x>:SV:STATE`` command.
            - ``.stopfrequency``: The ``REMOTE:S<x>_CH<x>:SV:STOPFrequency`` command.
        """
        return self._sv


class RemoteSItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``REMOTE:S<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:S<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``REMOTE:S<x>_CH<x>`` command tree.
        - ``.dch``: The ``REMOTE:S<x>_DCH<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, RemoteSItemChannel] = DefaultDictPassKeyToFactory(
            lambda x: RemoteSItemChannel(device, f"{self._cmd_syntax}_CH{x}")
        )
        self._dch: Dict[int, RemoteSItemDchItem] = DefaultDictPassKeyToFactory(
            lambda x: RemoteSItemDchItem(device, f"{self._cmd_syntax}_DCH{x}")
        )

    @property
    def ch(self) -> Dict[int, RemoteSItemChannel]:
        """Return the ``REMOTE:S<x>_CH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:S<x>_CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_CH<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.diggrp``: The ``REMOTE:S<x>_CH<x>:DIGGRP`` command tree.
            - ``.probetype``: The ``REMOTE:S<x>_CH<x>:PROBETYPE`` command.
            - ``.select``: The ``REMOTE:S<x>_CH<x>:SELect`` command tree.
            - ``.state``: The ``REMOTE:S<x>_CH<x>:STAte`` command.
            - ``.sv``: The ``REMOTE:S<x>_CH<x>:SV`` command tree.
        """
        return self._ch

    @property
    def dch(self) -> Dict[int, RemoteSItemDchItem]:
        """Return the ``REMOTE:S<x>_DCH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:S<x>_DCH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>_DCH<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.d``: The ``REMOTE:S<x>_DCH<x>:D<x>`` command tree.
            - ``.groupthreshold``: The ``REMOTE:S<x>_DCH<x>:GROUP<x>THReshold`` command.
            - ``.select``: The ``REMOTE:S<x>_DCH<x>:SELect`` command tree.
        """
        return self._dch


class RemoteNumacq(SCPICmdRead):
    """The ``REMOTE:NUMACq`` command.

    Description:
        - This query-only command returns the number of waveform acquisitions that have occurred
          since the last time acquisitions were stopped.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:NUMACq?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:NUMACq?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - REMOTE:NUMACq?
        ```
    """


class RemoteLogging(SCPICmdWrite, SCPICmdRead):
    """The ``REMOTE:LOGGING`` command.

    Description:
        - This command sets or queries the act on event data logging feature.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:LOGGING?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:LOGGING?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REMOTE:LOGGING value`` command.

    SCPI Syntax:
        ```
        - REMOTE:LOGGING {START|PAUSE|STOP}
        - REMOTE:LOGGING?
        ```

    Info:
        - ``START`` specifies that the act on event data logging feature is started, if
          ``REMOTE:ACQStatus`` is set to Acquire.
        - ``PAUSE`` specifies that the act on event data logging feature is paused.
        - ``STOP`` specifies that the act on event data logging feature is stopped.
    """


class RemoteDelete(SCPICmdWrite):
    """The ``REMOTE:DELEte`` command.

    Description:
        - This command delete the specified remote scope.

    Usage:
        - Using the ``.write(value)`` method will send the ``REMOTE:DELEte value`` command.

    SCPI Syntax:
        ```
        - REMOTE:DELEte <Qstring>
        ```

    Info:
        - ``<Qstring>`` is the remote scope to delete. The argument is of the form 'Scope<NR1>'
          where NR1 ≥ 1.
    """


class RemoteControl(SCPICmdWrite, SCPICmdRead):
    """The ``REMOTE:CONTROL`` command.

    Description:
        - This command sets or queries control the settings on the remote scope.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:CONTROL?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:CONTROL?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REMOTE:CONTROL value`` command.

    SCPI Syntax:
        ```
        - REMOTE:CONTROL <NR1>
        - REMOTE:CONTROL?
        ```

    Info:
        - ``<NR1>`` sets the control to 0 or 1. 0 sets the remote control to off. 1 sets the remote
          control to on.
    """


class RemoteComminter(SCPICmdWrite, SCPICmdRead):
    """The ``REMOTE:COMMInter`` command.

    Description:
        - This command sets or queries communication Interface for remote connection.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:COMMInter?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:COMMInter?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REMOTE:COMMInter value`` command.

    SCPI Syntax:
        ```
        - REMOTE:COMMInter {Visa|Socket}
        - REMOTE:COMMInter?
        ```

    Info:
        - ``Visa`` sets the remote communication interface to Visa.
        - ``Socket`` sets the remote communication interface to Socket.
    """


class RemoteAddnew(SCPICmdWrite):
    """The ``REMOTE:ADDNew`` command.

    Description:
        - This command adds the specified remote scope.

    Usage:
        - Using the ``.write(value)`` method will send the ``REMOTE:ADDNew value`` command.

    SCPI Syntax:
        ```
        - REMOTE:ADDNew <Qstring>
        ```

    Info:
        - ``<Qstring>`` is the remote scope to add. The argument is of the form 'Scope<NR1>' where
          NR1 ≥ 1.
    """


class RemoteAcquire(SCPICmdWrite):
    """The ``REMOTE:ACQUIRE`` command.

    Description:
        - This command acquires a single sequence on the specified remote Scope.

    Usage:
        - Using the ``.write(value)`` method will send the ``REMOTE:ACQUIRE value`` command.

    SCPI Syntax:
        ```
        - REMOTE:ACQUIRE <NR1>
        ```

    Info:
        - ``<NR1>`` specifies the Remote Scope.
    """


class RemoteAcqstatus(SCPICmdRead):
    """The ``REMOTE:ACQStatus`` command.

    Description:
        - This command queries the status of the remote scope acquisition.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:ACQStatus?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:ACQStatus?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - REMOTE:ACQStatus?
        ```
    """


class RemoteAcqmethod(SCPICmdWrite, SCPICmdRead):
    """The ``REMOTE:ACQMethod`` command.

    Description:
        - This command sets or queries whether the instrument continually acquires acquisitions or
          acquires a single sequence.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE:ACQMethod?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE:ACQMethod?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REMOTE:ACQMethod value`` command.

    SCPI Syntax:
        ```
        - REMOTE:ACQMethod {CONTINuous|SINGLE|SEQuence}
        - REMOTE:ACQMethod?
        ```

    Info:
        - ``CONTINuous`` specifies that the instrument will continually acquire data if
          ``:REMOTE:RUNStop`` is set to RUN.
        - ``SINGLE`` specifies that the next acquisition will be a single-sequence acquisition if
          ``:REMOTE:RUNStop`` is set to RUN.
        - ``SEQuence`` specifies that the next acquisition will bea single-sequence acquisition if
          ``REMOTE:ACQUIRE`` is set to 1.
    """


#  pylint: disable=too-many-instance-attributes
class Remote(SCPICmdRead):
    """The ``REMOTE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``REMOTE?`` query.
        - Using the ``.verify(value)`` method will send the ``REMOTE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.acqmethod``: The ``REMOTE:ACQMethod`` command.
        - ``.acqstatus``: The ``REMOTE:ACQStatus`` command.
        - ``.acquire``: The ``REMOTE:ACQUIRE`` command.
        - ``.addnew``: The ``REMOTE:ADDNew`` command.
        - ``.comminter``: The ``REMOTE:COMMInter`` command.
        - ``.control``: The ``REMOTE:CONTROL`` command.
        - ``.delete``: The ``REMOTE:DELEte`` command.
        - ``.logging``: The ``REMOTE:LOGGING`` command.
        - ``.numacq``: The ``REMOTE:NUMACq`` command.
        - ``.s``: The ``REMOTE:S<x>`` command tree.
        - ``.scope``: The ``REMOTE:SCOPe<x>`` command tree.
        - ``.sequence``: The ``REMOTE:SEQuence`` command tree.
        - ``.sv``: The ``REMOTE:SV`` command tree.
        - ``.usbdescriptors``: The ``REMOTE:USBDEscriptors`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "REMOTE") -> None:
        super().__init__(device, cmd_syntax)
        self._acqmethod = RemoteAcqmethod(device, f"{self._cmd_syntax}:ACQMethod")
        self._acqstatus = RemoteAcqstatus(device, f"{self._cmd_syntax}:ACQStatus")
        self._acquire = RemoteAcquire(device, f"{self._cmd_syntax}:ACQUIRE")
        self._addnew = RemoteAddnew(device, f"{self._cmd_syntax}:ADDNew")
        self._comminter = RemoteComminter(device, f"{self._cmd_syntax}:COMMInter")
        self._control = RemoteControl(device, f"{self._cmd_syntax}:CONTROL")
        self._delete = RemoteDelete(device, f"{self._cmd_syntax}:DELEte")
        self._logging = RemoteLogging(device, f"{self._cmd_syntax}:LOGGING")
        self._numacq = RemoteNumacq(device, f"{self._cmd_syntax}:NUMACq")
        self._s: Dict[int, RemoteSItem] = DefaultDictPassKeyToFactory(
            lambda x: RemoteSItem(device, f"{self._cmd_syntax}:S{x}")
        )
        self._scope: Dict[int, RemoteScopeItem] = DefaultDictPassKeyToFactory(
            lambda x: RemoteScopeItem(device, f"{self._cmd_syntax}:SCOPe{x}")
        )
        self._sequence = RemoteSequence(device, f"{self._cmd_syntax}:SEQuence")
        self._sv = RemoteSv(device, f"{self._cmd_syntax}:SV")
        self._usbdescriptors = RemoteUsbdescriptors(device, f"{self._cmd_syntax}:USBDEscriptors")

    @property
    def acqmethod(self) -> RemoteAcqmethod:
        """Return the ``REMOTE:ACQMethod`` command.

        Description:
            - This command sets or queries whether the instrument continually acquires acquisitions
              or acquires a single sequence.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:ACQMethod?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:ACQMethod?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REMOTE:ACQMethod value`` command.

        SCPI Syntax:
            ```
            - REMOTE:ACQMethod {CONTINuous|SINGLE|SEQuence}
            - REMOTE:ACQMethod?
            ```

        Info:
            - ``CONTINuous`` specifies that the instrument will continually acquire data if
              ``:REMOTE:RUNStop`` is set to RUN.
            - ``SINGLE`` specifies that the next acquisition will be a single-sequence acquisition
              if ``:REMOTE:RUNStop`` is set to RUN.
            - ``SEQuence`` specifies that the next acquisition will bea single-sequence acquisition
              if ``REMOTE:ACQUIRE`` is set to 1.
        """
        return self._acqmethod

    @property
    def acqstatus(self) -> RemoteAcqstatus:
        """Return the ``REMOTE:ACQStatus`` command.

        Description:
            - This command queries the status of the remote scope acquisition.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:ACQStatus?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:ACQStatus?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - REMOTE:ACQStatus?
            ```
        """
        return self._acqstatus

    @property
    def acquire(self) -> RemoteAcquire:
        """Return the ``REMOTE:ACQUIRE`` command.

        Description:
            - This command acquires a single sequence on the specified remote Scope.

        Usage:
            - Using the ``.write(value)`` method will send the ``REMOTE:ACQUIRE value`` command.

        SCPI Syntax:
            ```
            - REMOTE:ACQUIRE <NR1>
            ```

        Info:
            - ``<NR1>`` specifies the Remote Scope.
        """
        return self._acquire

    @property
    def addnew(self) -> RemoteAddnew:
        """Return the ``REMOTE:ADDNew`` command.

        Description:
            - This command adds the specified remote scope.

        Usage:
            - Using the ``.write(value)`` method will send the ``REMOTE:ADDNew value`` command.

        SCPI Syntax:
            ```
            - REMOTE:ADDNew <Qstring>
            ```

        Info:
            - ``<Qstring>`` is the remote scope to add. The argument is of the form 'Scope<NR1>'
              where NR1 ≥ 1.
        """
        return self._addnew

    @property
    def comminter(self) -> RemoteComminter:
        """Return the ``REMOTE:COMMInter`` command.

        Description:
            - This command sets or queries communication Interface for remote connection.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:COMMInter?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:COMMInter?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REMOTE:COMMInter value`` command.

        SCPI Syntax:
            ```
            - REMOTE:COMMInter {Visa|Socket}
            - REMOTE:COMMInter?
            ```

        Info:
            - ``Visa`` sets the remote communication interface to Visa.
            - ``Socket`` sets the remote communication interface to Socket.
        """
        return self._comminter

    @property
    def control(self) -> RemoteControl:
        """Return the ``REMOTE:CONTROL`` command.

        Description:
            - This command sets or queries control the settings on the remote scope.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:CONTROL?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:CONTROL?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REMOTE:CONTROL value`` command.

        SCPI Syntax:
            ```
            - REMOTE:CONTROL <NR1>
            - REMOTE:CONTROL?
            ```

        Info:
            - ``<NR1>`` sets the control to 0 or 1. 0 sets the remote control to off. 1 sets the
              remote control to on.
        """
        return self._control

    @property
    def delete(self) -> RemoteDelete:
        """Return the ``REMOTE:DELEte`` command.

        Description:
            - This command delete the specified remote scope.

        Usage:
            - Using the ``.write(value)`` method will send the ``REMOTE:DELEte value`` command.

        SCPI Syntax:
            ```
            - REMOTE:DELEte <Qstring>
            ```

        Info:
            - ``<Qstring>`` is the remote scope to delete. The argument is of the form 'Scope<NR1>'
              where NR1 ≥ 1.
        """
        return self._delete

    @property
    def logging(self) -> RemoteLogging:
        """Return the ``REMOTE:LOGGING`` command.

        Description:
            - This command sets or queries the act on event data logging feature.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:LOGGING?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:LOGGING?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REMOTE:LOGGING value`` command.

        SCPI Syntax:
            ```
            - REMOTE:LOGGING {START|PAUSE|STOP}
            - REMOTE:LOGGING?
            ```

        Info:
            - ``START`` specifies that the act on event data logging feature is started, if
              ``REMOTE:ACQStatus`` is set to Acquire.
            - ``PAUSE`` specifies that the act on event data logging feature is paused.
            - ``STOP`` specifies that the act on event data logging feature is stopped.
        """
        return self._logging

    @property
    def numacq(self) -> RemoteNumacq:
        """Return the ``REMOTE:NUMACq`` command.

        Description:
            - This query-only command returns the number of waveform acquisitions that have occurred
              since the last time acquisitions were stopped.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:NUMACq?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:NUMACq?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - REMOTE:NUMACq?
            ```
        """
        return self._numacq

    @property
    def s(self) -> Dict[int, RemoteSItem]:
        """Return the ``REMOTE:S<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:S<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:S<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``REMOTE:S<x>_CH<x>`` command tree.
            - ``.dch``: The ``REMOTE:S<x>_DCH<x>`` command tree.
        """
        return self._s

    @property
    def scope(self) -> Dict[int, RemoteScopeItem]:
        """Return the ``REMOTE:SCOPe<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:SCOPe<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:SCOPe<x>?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``SCOPe<x>`` specifies the remote scope number.

        Sub-properties:
            - ``.bandwidth``: The ``REMOTE:SCOPe<x>:BANDWidth`` command.
            - ``.connect``: The ``REMOTE:SCOPe<x>:CONNECT`` command.
            - ``.connectionmessage``: The ``REMOTE:SCOPe<x>:CONNECTIONMessage`` command.
            - ``.connectionstate``: The ``REMOTE:SCOPe<x>:CONNECTIONState`` command.
            - ``.disconnect``: The ``REMOTE:SCOPe<x>:DISCONNECT`` command.
            - ``.horizontal``: The ``REMOTE:SCOPe<x>:HORizontal`` command tree.
            - ``.ipaddress``: The ``REMOTE:SCOPe<x>:IPADDress`` command.
            - ``.modelname``: The ``REMOTE:SCOPe<x>:MODELname`` command.
            - ``.port``: The ``REMOTE:SCOPe<x>:PORT`` command.
            - ``.sync``: The ``REMOTE:SCOPe<x>:SYNC`` command.
            - ``.state``: The ``REMOTE:SCOPe<x>:State`` command.
            - ``.visaconnectiontype``: The ``REMOTE:SCOPe<x>:VISACONNectiontype`` command.
        """
        return self._scope

    @property
    def sequence(self) -> RemoteSequence:
        """Return the ``REMOTE:SEQuence`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:SEQuence?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:SEQuence?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.current``: The ``REMOTE:SEQuence:CURrent`` command.
            - ``.numsequence``: The ``REMOTE:SEQuence:NUMSEQuence`` command.
        """
        return self._sequence

    @property
    def sv(self) -> RemoteSv:
        """Return the ``REMOTE:SV`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:SV?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:SV?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.rbw``: The ``REMOTE:SV:RBW`` command.
            - ``.rbwmode``: The ``REMOTE:SV:RBWMode`` command.
            - ``.span``: The ``REMOTE:SV:SPAN`` command.
            - ``.spanrbwratio``: The ``REMOTE:SV:SPANRBWRatio`` command.
            - ``.window``: The ``REMOTE:SV:WINDOW`` command.
        """
        return self._sv

    @property
    def usbdescriptors(self) -> RemoteUsbdescriptors:
        """Return the ``REMOTE:USBDEscriptors`` command.

        Description:
            - This command sets or queries the USB descriptors available for remote connection.

        Usage:
            - Using the ``.query()`` method will send the ``REMOTE:USBDEscriptors?`` query.
            - Using the ``.verify(value)`` method will send the ``REMOTE:USBDEscriptors?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REMOTE:USBDEscriptors value``
              command.

        SCPI Syntax:
            ```
            - REMOTE:USBDEscriptors {Usb<x>}
            - REMOTE:USBDEscriptors?
            ```

        Info:
            - ``Usb0`` sets the usb address of the first specified scope.
            - ``Usb1`` sets the usb address of the second specified scope.
        """
        return self._usbdescriptors
