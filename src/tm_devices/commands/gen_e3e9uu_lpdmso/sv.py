"""The sv commands module.

These commands are used in the following models:
LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SV:CH<x>:RF_AVErage:NUMAVg <NR1>
    - SV:CH<x>:RF_AVErage:NUMAVg?
    - SV:CH<x>:RF_MAGnitude:FORMat {AMPLINear|POWLINear|POWLOG}
    - SV:CH<x>:RF_MAGnitude:FORMat?
    - SV:CH<x>:RF_PHASe:REFerence:DEGrees <NR3>
    - SV:CH<x>:RF_PHASe:REFerence:DEGrees?
    - SV:CH<x>:RF_PHASe:REFerence:POSition {TRIGger|CURSor}
    - SV:CH<x>:RF_PHASe:REFerence:POSition?
    - SV:CH<x>:RF_PHASe:REFerence:TIMe <NR3>
    - SV:CH<x>:RF_PHASe:REFerence:TIMe?
    - SV:CH<x>:RF_PHASe:WRAP:DEGrees <NR3>
    - SV:CH<x>:RF_PHASe:WRAP:DEGrees?
    - SV:CH<x>:RF_PHASe:WRAP:STATE {ON|OFF}
    - SV:CH<x>:RF_PHASe:WRAP:STATE?
    - SV:CH<x>:SELTrace {NORMal|MAXHold|MINHold|AVErage}
    - SV:CH<x>:SELTrace?
    - SV:CH<x>:SELect:RF_AVErage {ON|1|OFF|0}
    - SV:CH<x>:SELect:RF_AVErage?
    - SV:CH<x>:SELect:RF_FREQuency {ON|OFF}
    - SV:CH<x>:SELect:RF_FREQuency?
    - SV:CH<x>:SELect:RF_MAGnitude {ON|OFF}
    - SV:CH<x>:SELect:RF_MAGnitude?
    - SV:CH<x>:SELect:RF_MAXHold {ON|1|OFF|0}
    - SV:CH<x>:SELect:RF_MAXHold?
    - SV:CH<x>:SELect:RF_MINHold {ON|1|OFF|0}
    - SV:CH<x>:SELect:RF_MINHold?
    - SV:CH<x>:SELect:RF_NORMal {ON|1|OFF|0}
    - SV:CH<x>:SELect:RF_NORMal?
    - SV:CH<x>:SELect:RF_PHASe {ON|OFF}
    - SV:CH<x>:SELect:RF_PHASe?
    - SV:CH<x>:SELect:SPECtrogram {ON|OFF}
    - SV:CH<x>:SELect:SPECtrogram?
    - SV:CH<x>:SQUELCH:STATE {ON|OFF}
    - SV:CH<x>:SQUELCH:STATE?
    - SV:CH<x>:SQUELCH:THReshold <NR3>
    - SV:CH<x>:SQUELCH:THReshold?
    - SV:CH<x>:UNIts {DBM|DBUW|DBMV|DBUV|DBMA|DBUA}
    - SV:CH<x>:UNIts?
    - SV:LOCKCenter {ON|1|OFF|0}
    - SV:LOCKCenter?
    - SV:LOCKSpectrum {ON|1|OFF|0}
    - SV:LOCKSpectrum?
    - SV:MARKER:PEAK:EXCURsion <NR3>
    - SV:MARKER:PEAK:EXCURsion?
    - SV:MARKER:PEAK:MAXimum <NR1>
    - SV:MARKER:PEAK:MAXimum?
    - SV:MARKER:PEAK:STATE {ON|1|OFF|0}
    - SV:MARKER:PEAK:STATE?
    - SV:MARKER:PEAK:THReshold <NR3>
    - SV:MARKER:PEAK:THReshold?
    - SV:MARKER:PEAKS:AMPLITUDE?
    - SV:MARKER:PEAKS:FREQuency?
    - SV:MARKER:REFERence
    - SV:MARKER:REFERence:AMPLITUDE?
    - SV:MARKER:REFERence:FREQuency?
    - SV:MARKER:TYPe {DELta|ABSolute}
    - SV:MARKER:TYPe?
    - SV:RBW <NR3>
    - SV:RBW?
    - SV:RBWMode {AUTOmatic|MANual}
    - SV:RBWMode?
    - SV:RF_PHASe:REFerence:MASTer {CH<x>|NONE}
    - SV:RF_PHASe:REFerence:MASTer?
    - SV:SPAN <NR3>
    - SV:SPAN?
    - SV:SPANRBWRatio <NR3>
    - SV:SPANRBWRatio?
    - SV:SPECtrogram:CSCale:MAX <NR3>
    - SV:SPECtrogram:CSCale:MAX?
    - SV:SPECtrogram:CSCale:MIN <NR3>
    - SV:SPECtrogram:CSCale:MIN?
    - SV:SPECtrogram:CURSor:A {1|0|ON|OFF}
    - SV:SPECtrogram:CURSor:A?
    - SV:SPECtrogram:CURSor:B {1|0|ON|OFF}
    - SV:SPECtrogram:CURSor:B?
    - SV:WINDOW {KAISerbessel|RECTangular|HAMMing|HANNing|BLACkmanharris|FLATtop2}
    - SV:WINDOW?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    SCPICmdWriteNoArguments,
    ValidatedChannel,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class SvWindow(SCPICmdWrite, SCPICmdRead):
    """The ``SV:WINDOW`` command.

    Description:
        - This command sets or queries the window type used by the windowing function of the
          Spectrum View. The windowing function is a Fast Fourier Transform (FFT) technique used to
          minimize the discontinuities between successive frames of an RF time domain signal. The
          default window type is Blackman-Harris.

    Usage:
        - Using the ``.query()`` method will send the ``SV:WINDOW?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:WINDOW?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:WINDOW value`` command.

    SCPI Syntax:
        ```
        - SV:WINDOW {KAISerbessel|RECTangular|HAMMing|HANNing|BLACkmanharris|FLATtop2}
        - SV:WINDOW?
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


class SvSpectrogramCursorB(SCPICmdWrite, SCPICmdRead):
    """The ``SV:SPECtrogram:CURSor:B`` command.

    Description:
        - This command sets or queries whether the spectrum trace at cursor B position is selected
          or not.

    Usage:
        - Using the ``.query()`` method will send the ``SV:SPECtrogram:CURSor:B?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:SPECtrogram:CURSor:B?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:SPECtrogram:CURSor:B value``
          command.

    SCPI Syntax:
        ```
        - SV:SPECtrogram:CURSor:B {1|0|ON|OFF}
        - SV:SPECtrogram:CURSor:B?
        ```

    Info:
        - ``1`` on the spectrum trace for cursor B position.
        - ``0`` turns off the spectrum trace for cursor B position. Off is the default.
        - ``ON`` turns on the spectrum trace for cursor B position.
        - ``OFF`` turns off the spectrum trace for cursor B position. Off is the default.
    """


class SvSpectrogramCursorA(SCPICmdWrite, SCPICmdRead):
    """The ``SV:SPECtrogram:CURSor:A`` command.

    Description:
        - This command sets or Queries whether the spectrum trace at cursor A position is selected
          or not.

    Usage:
        - Using the ``.query()`` method will send the ``SV:SPECtrogram:CURSor:A?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:SPECtrogram:CURSor:A?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:SPECtrogram:CURSor:A value``
          command.

    SCPI Syntax:
        ```
        - SV:SPECtrogram:CURSor:A {1|0|ON|OFF}
        - SV:SPECtrogram:CURSor:A?
        ```

    Info:
        - ``1`` turns on the spectrum trace for cursor A position.
        - ``0`` turns off the spectrum trace for cursor A position. Off is the default.
        - ``ON`` turns on the spectrum trace for cursor A position.
        - ``OFF`` turns off the spectrum trace for cursor A position. Off is the default.
    """


class SvSpectrogramCursor(SCPICmdRead):
    """The ``SV:SPECtrogram:CURSor`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:SPECtrogram:CURSor?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:SPECtrogram:CURSor?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.a``: The ``SV:SPECtrogram:CURSor:A`` command.
        - ``.b``: The ``SV:SPECtrogram:CURSor:B`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._a = SvSpectrogramCursorA(device, f"{self._cmd_syntax}:A")
        self._b = SvSpectrogramCursorB(device, f"{self._cmd_syntax}:B")

    @property
    def a(self) -> SvSpectrogramCursorA:
        """Return the ``SV:SPECtrogram:CURSor:A`` command.

        Description:
            - This command sets or Queries whether the spectrum trace at cursor A position is
              selected or not.

        Usage:
            - Using the ``.query()`` method will send the ``SV:SPECtrogram:CURSor:A?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:SPECtrogram:CURSor:A?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:SPECtrogram:CURSor:A value``
              command.

        SCPI Syntax:
            ```
            - SV:SPECtrogram:CURSor:A {1|0|ON|OFF}
            - SV:SPECtrogram:CURSor:A?
            ```

        Info:
            - ``1`` turns on the spectrum trace for cursor A position.
            - ``0`` turns off the spectrum trace for cursor A position. Off is the default.
            - ``ON`` turns on the spectrum trace for cursor A position.
            - ``OFF`` turns off the spectrum trace for cursor A position. Off is the default.
        """
        return self._a

    @property
    def b(self) -> SvSpectrogramCursorB:
        """Return the ``SV:SPECtrogram:CURSor:B`` command.

        Description:
            - This command sets or queries whether the spectrum trace at cursor B position is
              selected or not.

        Usage:
            - Using the ``.query()`` method will send the ``SV:SPECtrogram:CURSor:B?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:SPECtrogram:CURSor:B?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:SPECtrogram:CURSor:B value``
              command.

        SCPI Syntax:
            ```
            - SV:SPECtrogram:CURSor:B {1|0|ON|OFF}
            - SV:SPECtrogram:CURSor:B?
            ```

        Info:
            - ``1`` on the spectrum trace for cursor B position.
            - ``0`` turns off the spectrum trace for cursor B position. Off is the default.
            - ``ON`` turns on the spectrum trace for cursor B position.
            - ``OFF`` turns off the spectrum trace for cursor B position. Off is the default.
        """
        return self._b


class SvSpectrogramCscaleMin(SCPICmdWrite, SCPICmdRead):
    """The ``SV:SPECtrogram:CSCale:MIN`` command.

    Description:
        - This command sets or queries the minimum color scale value. Minimum must be < Maximum.
          Thus, if the user is adjusting Minimum up to the point where it would be the same as
          Minimum, then Maximum begins incrementing as needed to stay 1 dB above minimum.

    Usage:
        - Using the ``.query()`` method will send the ``SV:SPECtrogram:CSCale:MIN?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:SPECtrogram:CSCale:MIN?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:SPECtrogram:CSCale:MIN value``
          command.

    SCPI Syntax:
        ```
        - SV:SPECtrogram:CSCale:MIN <NR3>
        - SV:SPECtrogram:CSCale:MIN?
        ```

    Info:
        - ``<NR3>`` sets the minimum color scale value. The default value is -100.0 and the valid
          range is -170.0 to 99.0.
    """


class SvSpectrogramCscaleMax(SCPICmdWrite, SCPICmdRead):
    """The ``SV:SPECtrogram:CSCale:MAX`` command.

    Description:
        - This command sets or queries the maximum color scale value. Maximum must be > Minimum.
          Thus, if the user is adjusting Maximum down to the point where it would be the same as
          Minimum, then Minimum begins decrementing as needed to stay 1 dB below Maximum.

    Usage:
        - Using the ``.query()`` method will send the ``SV:SPECtrogram:CSCale:MAX?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:SPECtrogram:CSCale:MAX?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:SPECtrogram:CSCale:MAX value``
          command.

    SCPI Syntax:
        ```
        - SV:SPECtrogram:CSCale:MAX <NR3>
        - SV:SPECtrogram:CSCale:MAX?
        ```

    Info:
        - ``<NR3>`` sets the maximum color scale value. The default value is 0.0 and the valid range
          is -169.0 to 100.0.
    """


class SvSpectrogramCscale(SCPICmdRead):
    """The ``SV:SPECtrogram:CSCale`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:SPECtrogram:CSCale?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:SPECtrogram:CSCale?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.max``: The ``SV:SPECtrogram:CSCale:MAX`` command.
        - ``.min``: The ``SV:SPECtrogram:CSCale:MIN`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._max = SvSpectrogramCscaleMax(device, f"{self._cmd_syntax}:MAX")
        self._min = SvSpectrogramCscaleMin(device, f"{self._cmd_syntax}:MIN")

    @property
    def max(self) -> SvSpectrogramCscaleMax:
        """Return the ``SV:SPECtrogram:CSCale:MAX`` command.

        Description:
            - This command sets or queries the maximum color scale value. Maximum must be > Minimum.
              Thus, if the user is adjusting Maximum down to the point where it would be the same as
              Minimum, then Minimum begins decrementing as needed to stay 1 dB below Maximum.

        Usage:
            - Using the ``.query()`` method will send the ``SV:SPECtrogram:CSCale:MAX?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:SPECtrogram:CSCale:MAX?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:SPECtrogram:CSCale:MAX value``
              command.

        SCPI Syntax:
            ```
            - SV:SPECtrogram:CSCale:MAX <NR3>
            - SV:SPECtrogram:CSCale:MAX?
            ```

        Info:
            - ``<NR3>`` sets the maximum color scale value. The default value is 0.0 and the valid
              range is -169.0 to 100.0.
        """
        return self._max

    @property
    def min(self) -> SvSpectrogramCscaleMin:
        """Return the ``SV:SPECtrogram:CSCale:MIN`` command.

        Description:
            - This command sets or queries the minimum color scale value. Minimum must be < Maximum.
              Thus, if the user is adjusting Minimum up to the point where it would be the same as
              Minimum, then Maximum begins incrementing as needed to stay 1 dB above minimum.

        Usage:
            - Using the ``.query()`` method will send the ``SV:SPECtrogram:CSCale:MIN?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:SPECtrogram:CSCale:MIN?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:SPECtrogram:CSCale:MIN value``
              command.

        SCPI Syntax:
            ```
            - SV:SPECtrogram:CSCale:MIN <NR3>
            - SV:SPECtrogram:CSCale:MIN?
            ```

        Info:
            - ``<NR3>`` sets the minimum color scale value. The default value is -100.0 and the
              valid range is -170.0 to 99.0.
        """
        return self._min


class SvSpectrogram(SCPICmdRead):
    """The ``SV:SPECtrogram`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:SPECtrogram?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:SPECtrogram?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.cscale``: The ``SV:SPECtrogram:CSCale`` command tree.
        - ``.cursor``: The ``SV:SPECtrogram:CURSor`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._cscale = SvSpectrogramCscale(device, f"{self._cmd_syntax}:CSCale")
        self._cursor = SvSpectrogramCursor(device, f"{self._cmd_syntax}:CURSor")

    @property
    def cscale(self) -> SvSpectrogramCscale:
        """Return the ``SV:SPECtrogram:CSCale`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:SPECtrogram:CSCale?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:SPECtrogram:CSCale?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.max``: The ``SV:SPECtrogram:CSCale:MAX`` command.
            - ``.min``: The ``SV:SPECtrogram:CSCale:MIN`` command.
        """
        return self._cscale

    @property
    def cursor(self) -> SvSpectrogramCursor:
        """Return the ``SV:SPECtrogram:CURSor`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:SPECtrogram:CURSor?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:SPECtrogram:CURSor?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.a``: The ``SV:SPECtrogram:CURSor:A`` command.
            - ``.b``: The ``SV:SPECtrogram:CURSor:B`` command.
        """
        return self._cursor


class SvSpanrbwratio(SCPICmdWrite, SCPICmdRead):
    """The ``SV:SPANRBWRatio`` command.

    Description:
        - This command sets or queries the ratio of the span to the resolution bandwidth (RBW) that
          will be used when the RBW Mode is set to AUTO. The span is the width of the frequency
          domain trace in Hz, which is equal to the stop frequency minus the start frequency. The
          RBW is the width of the narrowest measurable band of frequencies in a frequency domain
          trace. The default RBW ratio is 1000 : 1. Use the command ``SV:RBWMode`` to set the RBW
          Mode to Automatic.

    Usage:
        - Using the ``.query()`` method will send the ``SV:SPANRBWRatio?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:SPANRBWRatio?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:SPANRBWRatio value`` command.

    SCPI Syntax:
        ```
        - SV:SPANRBWRatio <NR3>
        - SV:SPANRBWRatio?
        ```

    Info:
        - ``<NR3>`` specifies the span-to-RBW ratio.
    """


class SvSpan(SCPICmdWrite, SCPICmdRead):
    """The ``SV:SPAN`` command.

    Description:
        - This command sets or queries the span setting for all channels in the Spectrum View. The
          span is the range of frequencies that can be observed centered on the center frequency.
          This is the width of the frequency domain trace, which is from the center frequency -
          ½span to the center frequency + ½ span.

    Usage:
        - Using the ``.query()`` method will send the ``SV:SPAN?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:SPAN?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:SPAN value`` command.

    SCPI Syntax:
        ```
        - SV:SPAN <NR3>
        - SV:SPAN?
        ```

    Info:
        - ``<NR3>`` specifies the span value in Hz.
    """


class SvRfPhaseReferenceMaster(SCPICmdWrite, SCPICmdRead):
    """The ``SV:RF_PHASe:REFerence:MASTer`` command.

    Description:
        - This command sets or queries the channel used as the Master Phase Reference.

    Usage:
        - Using the ``.query()`` method will send the ``SV:RF_PHASe:REFerence:MASTer?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:RF_PHASe:REFerence:MASTer?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:RF_PHASe:REFerence:MASTer value``
          command.

    SCPI Syntax:
        ```
        - SV:RF_PHASe:REFerence:MASTer {CH<x>|NONE}
        - SV:RF_PHASe:REFerence:MASTer?
        ```

    Info:
        - ``CH<x>`` sets the specified channel as the Master Phase Reference source.
        - ``NONE`` indicates that there is no Master Phase Reference.
    """


class SvRfPhaseReference(SCPICmdRead):
    """The ``SV:RF_PHASe:REFerence`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:RF_PHASe:REFerence?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:RF_PHASe:REFerence?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.master``: The ``SV:RF_PHASe:REFerence:MASTer`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._master = SvRfPhaseReferenceMaster(device, f"{self._cmd_syntax}:MASTer")

    @property
    def master(self) -> SvRfPhaseReferenceMaster:
        """Return the ``SV:RF_PHASe:REFerence:MASTer`` command.

        Description:
            - This command sets or queries the channel used as the Master Phase Reference.

        Usage:
            - Using the ``.query()`` method will send the ``SV:RF_PHASe:REFerence:MASTer?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:RF_PHASe:REFerence:MASTer?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SV:RF_PHASe:REFerence:MASTer value`` command.

        SCPI Syntax:
            ```
            - SV:RF_PHASe:REFerence:MASTer {CH<x>|NONE}
            - SV:RF_PHASe:REFerence:MASTer?
            ```

        Info:
            - ``CH<x>`` sets the specified channel as the Master Phase Reference source.
            - ``NONE`` indicates that there is no Master Phase Reference.
        """
        return self._master


class SvRfPhase(SCPICmdRead):
    """The ``SV:RF_PHASe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:RF_PHASe?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:RF_PHASe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.reference``: The ``SV:RF_PHASe:REFerence`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._reference = SvRfPhaseReference(device, f"{self._cmd_syntax}:REFerence")

    @property
    def reference(self) -> SvRfPhaseReference:
        """Return the ``SV:RF_PHASe:REFerence`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:RF_PHASe:REFerence?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:RF_PHASe:REFerence?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.master``: The ``SV:RF_PHASe:REFerence:MASTer`` command.
        """
        return self._reference


class SvRbwmode(SCPICmdWrite, SCPICmdRead):
    """The ``SV:RBWMode`` command.

    Description:
        - This command sets or queries the resolution bandwidth (RBW) mode, either Automatic or
          Manual.

    Usage:
        - Using the ``.query()`` method will send the ``SV:RBWMode?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:RBWMode?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:RBWMode value`` command.

    SCPI Syntax:
        ```
        - SV:RBWMode {AUTOmatic|MANual}
        - SV:RBWMode?
        ```

    Info:
        - ``AUTOmatic`` specifies the resolution bandwidth automatically as the span is changed. The
          default behavior is ``1000:1``, but you can set it to other values in a 1-2-5 sequence
          (e.g. 10000, 20000, 50000). To specify the RBW ratio that will be used when the mode is
          set to automatic, use the command ``SV:SPANRBWRatio``.
        - ``MANual`` specifies to set the resolution bandwidth, independently from the span, using
          the command ``SV:RBW``.
    """


class SvRbw(SCPICmdWrite, SCPICmdRead):
    """The ``SV:RBW`` command.

    Description:
        - This command sets or queries the resolution bandwidth (RBW) when the RBW mode has been set
          to MANUAL (using the command ``SV:RBWMode``). The resolution bandwidth is the width of the
          narrowest measurable band of frequencies in a Spectrum View trace. By default, the RBW
          tracks the span value in a ``1000:1`` ratio. The RBW determines the level to which the
          instrument can resolve individual frequencies in the frequency domain. For example, if the
          input signal contains two carriers separated by 1 kHz, you will not be able to
          discriminate between them unless the RBW is less than 1 kHz.

    Usage:
        - Using the ``.query()`` method will send the ``SV:RBW?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:RBW?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:RBW value`` command.

    SCPI Syntax:
        ```
        - SV:RBW <NR3>
        - SV:RBW?
        ```

    Info:
        - ``<NR3>`` specifies the width of the narrowest measurable band of frequencies in a
          Spectrum View trace, in Hz.
    """


class SvMarkerType(SCPICmdWrite, SCPICmdRead):
    """The ``SV:MARKER:TYPe`` command.

    Description:
        - This command sets or queries the peak marker type (either DELTa or ABSolute). An Absolute
          marker shows the frequency and amplitude at the location of the marker. A Delta marker
          shows the frequency and amplitude of the marker relative to the Reference Marker. The
          Reference Marker shows the absolute frequency and amplitude, regardless of this command.
          The marker amplitude measurements are in dBm for Absolute, or in dBc (dB below carrier
          amplitude) for Delta.

    Usage:
        - Using the ``.query()`` method will send the ``SV:MARKER:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:MARKER:TYPe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:MARKER:TYPe value`` command.

    SCPI Syntax:
        ```
        - SV:MARKER:TYPe {DELta|ABSolute}
        - SV:MARKER:TYPe?
        ```

    Info:
        - ``DELTa`` specifies to display the frequency and amplitude of the peak markers relative to
          the Reference Marker. The relative amplitude is in dBc (dB below carrier amplitude); the
          relative frequency is in Hz.
        - ``ABSolute`` specifies to display the actual frequency and amplitude of each peak marker.
          The absolute amplitude is in user-set units; the absolute frequency is in Hz.
    """


class SvMarkerReferenceFrequency(SCPICmdRead):
    """The ``SV:MARKER:REFERence:FREQuency`` command.

    Description:
        - This command queries the frequency of the Reference Marker, in Hz, when the Spectrum View
          trace markers are on.

    Usage:
        - Using the ``.query()`` method will send the ``SV:MARKER:REFERence:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:MARKER:REFERence:FREQuency?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SV:MARKER:REFERence:FREQuency?
        ```
    """


class SvMarkerReferenceAmplitude(SCPICmdRead):
    """The ``SV:MARKER:REFERence:AMPLITUDE`` command.

    Description:
        - This command queries the amplitude (vertical) value of the Reference Marker in user-set
          units. This value indicates the absolute amplitude of the Reference Marker, regardless of
          whether the other markers are manual or automatic.

    Usage:
        - Using the ``.query()`` method will send the ``SV:MARKER:REFERence:AMPLITUDE?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:MARKER:REFERence:AMPLITUDE?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SV:MARKER:REFERence:AMPLITUDE?
        ```
    """


class SvMarkerReference(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``SV:MARKER:REFERence`` command.

    Description:
        - This command sets the Center Frequency of the currently selected Spectrum View channel to
          the frequency indicated by the Reference Marker, in effect moving the Reference Marker to
          the center of the screen.

    Usage:
        - Using the ``.write()`` method will send the ``SV:MARKER:REFERence`` command.

    SCPI Syntax:
        ```
        - SV:MARKER:REFERence
        ```

    Properties:
        - ``.amplitude``: The ``SV:MARKER:REFERence:AMPLITUDE`` command.
        - ``.frequency``: The ``SV:MARKER:REFERence:FREQuency`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._amplitude = SvMarkerReferenceAmplitude(device, f"{self._cmd_syntax}:AMPLITUDE")
        self._frequency = SvMarkerReferenceFrequency(device, f"{self._cmd_syntax}:FREQuency")

    @property
    def amplitude(self) -> SvMarkerReferenceAmplitude:
        """Return the ``SV:MARKER:REFERence:AMPLITUDE`` command.

        Description:
            - This command queries the amplitude (vertical) value of the Reference Marker in
              user-set units. This value indicates the absolute amplitude of the Reference Marker,
              regardless of whether the other markers are manual or automatic.

        Usage:
            - Using the ``.query()`` method will send the ``SV:MARKER:REFERence:AMPLITUDE?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:MARKER:REFERence:AMPLITUDE?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SV:MARKER:REFERence:AMPLITUDE?
            ```
        """
        return self._amplitude

    @property
    def frequency(self) -> SvMarkerReferenceFrequency:
        """Return the ``SV:MARKER:REFERence:FREQuency`` command.

        Description:
            - This command queries the frequency of the Reference Marker, in Hz, when the Spectrum
              View trace markers are on.

        Usage:
            - Using the ``.query()`` method will send the ``SV:MARKER:REFERence:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:MARKER:REFERence:FREQuency?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SV:MARKER:REFERence:FREQuency?
            ```
        """
        return self._frequency


class SvMarkerPeaksFrequency(SCPICmdRead):
    """The ``SV:MARKER:PEAKS:FREQuency`` command.

    Description:
        - This command queries the peak frequencies for the Spectrum View trace peak markers.

    Usage:
        - Using the ``.query()`` method will send the ``SV:MARKER:PEAKS:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:MARKER:PEAKS:FREQuency?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SV:MARKER:PEAKS:FREQuency?
        ```
    """


class SvMarkerPeaksAmplitude(SCPICmdRead):
    """The ``SV:MARKER:PEAKS:AMPLITUDE`` command.

    Description:
        - This command queries the peak amplitudes for the Spectrum View trace peak markers.

    Usage:
        - Using the ``.query()`` method will send the ``SV:MARKER:PEAKS:AMPLITUDE?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:MARKER:PEAKS:AMPLITUDE?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SV:MARKER:PEAKS:AMPLITUDE?
        ```
    """


class SvMarkerPeaks(SCPICmdRead):
    """The ``SV:MARKER:PEAKS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:MARKER:PEAKS?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:MARKER:PEAKS?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.amplitude``: The ``SV:MARKER:PEAKS:AMPLITUDE`` command.
        - ``.frequency``: The ``SV:MARKER:PEAKS:FREQuency`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._amplitude = SvMarkerPeaksAmplitude(device, f"{self._cmd_syntax}:AMPLITUDE")
        self._frequency = SvMarkerPeaksFrequency(device, f"{self._cmd_syntax}:FREQuency")

    @property
    def amplitude(self) -> SvMarkerPeaksAmplitude:
        """Return the ``SV:MARKER:PEAKS:AMPLITUDE`` command.

        Description:
            - This command queries the peak amplitudes for the Spectrum View trace peak markers.

        Usage:
            - Using the ``.query()`` method will send the ``SV:MARKER:PEAKS:AMPLITUDE?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:MARKER:PEAKS:AMPLITUDE?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SV:MARKER:PEAKS:AMPLITUDE?
            ```
        """
        return self._amplitude

    @property
    def frequency(self) -> SvMarkerPeaksFrequency:
        """Return the ``SV:MARKER:PEAKS:FREQuency`` command.

        Description:
            - This command queries the peak frequencies for the Spectrum View trace peak markers.

        Usage:
            - Using the ``.query()`` method will send the ``SV:MARKER:PEAKS:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:MARKER:PEAKS:FREQuency?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SV:MARKER:PEAKS:FREQuency?
            ```
        """
        return self._frequency


class SvMarkerPeakThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``SV:MARKER:PEAK:THReshold`` command.

    Description:
        - This command sets or queries the minimum peak threshold value required to mark a peak.
          Only peaks with an amplitude greater than the threshold value will qualify for peak marker
          placement. Applies to all spectrum traces, and to each trace in its own vertical units.

    Usage:
        - Using the ``.query()`` method will send the ``SV:MARKER:PEAK:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:MARKER:PEAK:THReshold?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:MARKER:PEAK:THReshold value``
          command.

    SCPI Syntax:
        ```
        - SV:MARKER:PEAK:THReshold <NR3>
        - SV:MARKER:PEAK:THReshold?
        ```

    Info:
        - ``<NR3>`` specifies the peak marker threshold value. The range of values is -200.0 to
          200.0.
    """


class SvMarkerPeakState(SCPICmdWrite, SCPICmdRead):
    """The ``SV:MARKER:PEAK:STATE`` command.

    Description:
        - This command sets or queries showing peak markers on spectrum traces in the Spectrum View
          window. There are up to 11 markers. The maximum number of markers can be set using the
          command ``SV:MARKER:PEAK:MAXimum``. The peak markers find amplitude peaks based upon
          threshold and excursion settings (set with the ``SV:MARKER:PEAK:EXCURsion`` and
          ``SV:MARKER:PEAK:THReshold`` commands.) Each peak marker has a readout associated with it.
          These can be absolute or delta readouts (set with the ``SV:MARKER:TYPe`` command.)

    Usage:
        - Using the ``.query()`` method will send the ``SV:MARKER:PEAK:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:MARKER:PEAK:STATE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:MARKER:PEAK:STATE value`` command.

    SCPI Syntax:
        ```
        - SV:MARKER:PEAK:STATE {ON|1|OFF|0}
        - SV:MARKER:PEAK:STATE?
        ```

    Info:
        - ``1`` enables showing peak marker icons on spectrum trace waveforms.
        - ``ON`` enables showing peak marker icons on spectrum trace waveforms.
        - ``0`` disables showing peak marker icons on spectrum trace waveforms.
        - ``OFF`` disables showing peak marker icons on spectrum trace waveforms.
    """


class SvMarkerPeakMaximum(SCPICmdWrite, SCPICmdRead):
    """The ``SV:MARKER:PEAK:MAXimum`` command.

    Description:
        - This command sets or queries the maximum number of Spectrum View peak markers that can be
          placed on spectrum traces. the Spectrum View window can show between 1 and 11 peak markers
          on all spectrum traces. The default is 5. To turn on the peak markers, use the command
          ``SV:MARKER:PEAK:STATE``. The actual number of peak markers may be less than the maximum,
          depending on the threshold and excursion values and the spectral content of the RF signal.
          If more peaks than the maximum are detected that meet the threshold and excursion
          criteria, only the highest amplitude peaks will have markers placed on them.

    Usage:
        - Using the ``.query()`` method will send the ``SV:MARKER:PEAK:MAXimum?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:MARKER:PEAK:MAXimum?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:MARKER:PEAK:MAXimum value`` command.

    SCPI Syntax:
        ```
        - SV:MARKER:PEAK:MAXimum <NR1>
        - SV:MARKER:PEAK:MAXimum?
        ```

    Info:
        - ``<NR1>`` is an integer value that specifies the maximum number of peak markers to display
          on spectrum traces. he range of values is 1 to 11.
    """


class SvMarkerPeakExcursion(SCPICmdWrite, SCPICmdRead):
    """The ``SV:MARKER:PEAK:EXCURsion`` command.

    Description:
        - This command sets or queries the minimum peak excursion value, in dB, for the Spectrum
          View trace peak markers. Peak excursion refers to the minimum amount a spectrum signal
          needs to fall in amplitude between marked peaks to be considered another valid peak. If
          the peak excursion value is low, more peaks will tend to qualify as valid peaks and have
          associated markers. If the peak excursion value is high, fewer peaks will have associated
          markers.

    Usage:
        - Using the ``.query()`` method will send the ``SV:MARKER:PEAK:EXCURsion?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:MARKER:PEAK:EXCURsion?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:MARKER:PEAK:EXCURsion value``
          command.

    SCPI Syntax:
        ```
        - SV:MARKER:PEAK:EXCURsion <NR3>
        - SV:MARKER:PEAK:EXCURsion?
        ```

    Info:
        - ``<NR3>`` specifies the peak marker excursion value in dB. The range of values is 0.0 dB
          to 200.0 dB.
    """


class SvMarkerPeak(SCPICmdRead):
    """The ``SV:MARKER:PEAK`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:MARKER:PEAK?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:MARKER:PEAK?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.excursion``: The ``SV:MARKER:PEAK:EXCURsion`` command.
        - ``.maximum``: The ``SV:MARKER:PEAK:MAXimum`` command.
        - ``.state``: The ``SV:MARKER:PEAK:STATE`` command.
        - ``.threshold``: The ``SV:MARKER:PEAK:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._excursion = SvMarkerPeakExcursion(device, f"{self._cmd_syntax}:EXCURsion")
        self._maximum = SvMarkerPeakMaximum(device, f"{self._cmd_syntax}:MAXimum")
        self._state = SvMarkerPeakState(device, f"{self._cmd_syntax}:STATE")
        self._threshold = SvMarkerPeakThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def excursion(self) -> SvMarkerPeakExcursion:
        """Return the ``SV:MARKER:PEAK:EXCURsion`` command.

        Description:
            - This command sets or queries the minimum peak excursion value, in dB, for the Spectrum
              View trace peak markers. Peak excursion refers to the minimum amount a spectrum signal
              needs to fall in amplitude between marked peaks to be considered another valid peak.
              If the peak excursion value is low, more peaks will tend to qualify as valid peaks and
              have associated markers. If the peak excursion value is high, fewer peaks will have
              associated markers.

        Usage:
            - Using the ``.query()`` method will send the ``SV:MARKER:PEAK:EXCURsion?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:MARKER:PEAK:EXCURsion?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:MARKER:PEAK:EXCURsion value``
              command.

        SCPI Syntax:
            ```
            - SV:MARKER:PEAK:EXCURsion <NR3>
            - SV:MARKER:PEAK:EXCURsion?
            ```

        Info:
            - ``<NR3>`` specifies the peak marker excursion value in dB. The range of values is 0.0
              dB to 200.0 dB.
        """
        return self._excursion

    @property
    def maximum(self) -> SvMarkerPeakMaximum:
        """Return the ``SV:MARKER:PEAK:MAXimum`` command.

        Description:
            - This command sets or queries the maximum number of Spectrum View peak markers that can
              be placed on spectrum traces. the Spectrum View window can show between 1 and 11 peak
              markers on all spectrum traces. The default is 5. To turn on the peak markers, use the
              command ``SV:MARKER:PEAK:STATE``. The actual number of peak markers may be less than
              the maximum, depending on the threshold and excursion values and the spectral content
              of the RF signal. If more peaks than the maximum are detected that meet the threshold
              and excursion criteria, only the highest amplitude peaks will have markers placed on
              them.

        Usage:
            - Using the ``.query()`` method will send the ``SV:MARKER:PEAK:MAXimum?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:MARKER:PEAK:MAXimum?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:MARKER:PEAK:MAXimum value``
              command.

        SCPI Syntax:
            ```
            - SV:MARKER:PEAK:MAXimum <NR1>
            - SV:MARKER:PEAK:MAXimum?
            ```

        Info:
            - ``<NR1>`` is an integer value that specifies the maximum number of peak markers to
              display on spectrum traces. he range of values is 1 to 11.
        """
        return self._maximum

    @property
    def state(self) -> SvMarkerPeakState:
        """Return the ``SV:MARKER:PEAK:STATE`` command.

        Description:
            - This command sets or queries showing peak markers on spectrum traces in the Spectrum
              View window. There are up to 11 markers. The maximum number of markers can be set
              using the command ``SV:MARKER:PEAK:MAXimum``. The peak markers find amplitude peaks
              based upon threshold and excursion settings (set with the ``SV:MARKER:PEAK:EXCURsion``
              and ``SV:MARKER:PEAK:THReshold`` commands.) Each peak marker has a readout associated
              with it. These can be absolute or delta readouts (set with the ``SV:MARKER:TYPe``
              command.)

        Usage:
            - Using the ``.query()`` method will send the ``SV:MARKER:PEAK:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:MARKER:PEAK:STATE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:MARKER:PEAK:STATE value``
              command.

        SCPI Syntax:
            ```
            - SV:MARKER:PEAK:STATE {ON|1|OFF|0}
            - SV:MARKER:PEAK:STATE?
            ```

        Info:
            - ``1`` enables showing peak marker icons on spectrum trace waveforms.
            - ``ON`` enables showing peak marker icons on spectrum trace waveforms.
            - ``0`` disables showing peak marker icons on spectrum trace waveforms.
            - ``OFF`` disables showing peak marker icons on spectrum trace waveforms.
        """
        return self._state

    @property
    def threshold(self) -> SvMarkerPeakThreshold:
        """Return the ``SV:MARKER:PEAK:THReshold`` command.

        Description:
            - This command sets or queries the minimum peak threshold value required to mark a peak.
              Only peaks with an amplitude greater than the threshold value will qualify for peak
              marker placement. Applies to all spectrum traces, and to each trace in its own
              vertical units.

        Usage:
            - Using the ``.query()`` method will send the ``SV:MARKER:PEAK:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:MARKER:PEAK:THReshold?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:MARKER:PEAK:THReshold value``
              command.

        SCPI Syntax:
            ```
            - SV:MARKER:PEAK:THReshold <NR3>
            - SV:MARKER:PEAK:THReshold?
            ```

        Info:
            - ``<NR3>`` specifies the peak marker threshold value. The range of values is -200.0 to
              200.0.
        """
        return self._threshold


class SvMarker(SCPICmdRead):
    """The ``SV:MARKER`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:MARKER?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:MARKER?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.peak``: The ``SV:MARKER:PEAK`` command tree.
        - ``.peaks``: The ``SV:MARKER:PEAKS`` command tree.
        - ``.reference``: The ``SV:MARKER:REFERence`` command.
        - ``.type``: The ``SV:MARKER:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._peak = SvMarkerPeak(device, f"{self._cmd_syntax}:PEAK")
        self._peaks = SvMarkerPeaks(device, f"{self._cmd_syntax}:PEAKS")
        self._reference = SvMarkerReference(device, f"{self._cmd_syntax}:REFERence")
        self._type = SvMarkerType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def peak(self) -> SvMarkerPeak:
        """Return the ``SV:MARKER:PEAK`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:MARKER:PEAK?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:MARKER:PEAK?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.excursion``: The ``SV:MARKER:PEAK:EXCURsion`` command.
            - ``.maximum``: The ``SV:MARKER:PEAK:MAXimum`` command.
            - ``.state``: The ``SV:MARKER:PEAK:STATE`` command.
            - ``.threshold``: The ``SV:MARKER:PEAK:THReshold`` command.
        """
        return self._peak

    @property
    def peaks(self) -> SvMarkerPeaks:
        """Return the ``SV:MARKER:PEAKS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:MARKER:PEAKS?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:MARKER:PEAKS?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.amplitude``: The ``SV:MARKER:PEAKS:AMPLITUDE`` command.
            - ``.frequency``: The ``SV:MARKER:PEAKS:FREQuency`` command.
        """
        return self._peaks

    @property
    def reference(self) -> SvMarkerReference:
        """Return the ``SV:MARKER:REFERence`` command.

        Description:
            - This command sets the Center Frequency of the currently selected Spectrum View channel
              to the frequency indicated by the Reference Marker, in effect moving the Reference
              Marker to the center of the screen.

        Usage:
            - Using the ``.write()`` method will send the ``SV:MARKER:REFERence`` command.

        SCPI Syntax:
            ```
            - SV:MARKER:REFERence
            ```

        Sub-properties:
            - ``.amplitude``: The ``SV:MARKER:REFERence:AMPLITUDE`` command.
            - ``.frequency``: The ``SV:MARKER:REFERence:FREQuency`` command.
        """
        return self._reference

    @property
    def type(self) -> SvMarkerType:
        """Return the ``SV:MARKER:TYPe`` command.

        Description:
            - This command sets or queries the peak marker type (either DELTa or ABSolute). An
              Absolute marker shows the frequency and amplitude at the location of the marker. A
              Delta marker shows the frequency and amplitude of the marker relative to the Reference
              Marker. The Reference Marker shows the absolute frequency and amplitude, regardless of
              this command. The marker amplitude measurements are in dBm for Absolute, or in dBc (dB
              below carrier amplitude) for Delta.

        Usage:
            - Using the ``.query()`` method will send the ``SV:MARKER:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:MARKER:TYPe?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:MARKER:TYPe value`` command.

        SCPI Syntax:
            ```
            - SV:MARKER:TYPe {DELta|ABSolute}
            - SV:MARKER:TYPe?
            ```

        Info:
            - ``DELTa`` specifies to display the frequency and amplitude of the peak markers
              relative to the Reference Marker. The relative amplitude is in dBc (dB below carrier
              amplitude); the relative frequency is in Hz.
            - ``ABSolute`` specifies to display the actual frequency and amplitude of each peak
              marker. The absolute amplitude is in user-set units; the absolute frequency is in Hz.
        """
        return self._type


class SvLockspectrum(SCPICmdWrite, SCPICmdRead):
    """The ``SV:LOCKSpectrum`` command.

    Description:
        - This command sets or queries whether the Spectrum Time value is locked across all spectrum
          trace channels in the Spectrum View.

    Usage:
        - Using the ``.query()`` method will send the ``SV:LOCKSpectrum?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:LOCKSpectrum?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:LOCKSpectrum value`` command.

    SCPI Syntax:
        ```
        - SV:LOCKSpectrum {ON|1|OFF|0}
        - SV:LOCKSpectrum?
        ```

    Info:
        - ``ON`` sets all spectrum traces channels in the Spectrum View window to use the same
          Spectrum Time value. When the Spectrum Time of any channel is changed, the Spectrum Time
          of all other channels is automatically changed to match that value.
        - ``1`` sets all spectrum traces channels in the Spectrum View window to use the same
          Spectrum Time value. When the Spectrum Time of any channel is changed, the Spectrum Time
          of all other channels is automatically changed to match that value.
        - ``0`` enables use of different Spectrum Time values for each spectrum trace channel. The
          Spectrum Time of all channels are independent.
        - ``OFF`` enables use of different Spectrum Time values for each spectrum trace channel. The
          Spectrum Time of all channels are independent.
    """


class SvLockcenter(SCPICmdWrite, SCPICmdRead):
    """The ``SV:LOCKCenter`` command.

    Description:
        - This command sets or queries whether the Center Frequency setting is locked across all
          channels in the Spectrum View.

    Usage:
        - Using the ``.query()`` method will send the ``SV:LOCKCenter?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:LOCKCenter?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:LOCKCenter value`` command.

    SCPI Syntax:
        ```
        - SV:LOCKCenter {ON|1|OFF|0}
        - SV:LOCKCenter?
        ```

    Info:
        - ``ON`` sets all spectrum traces channels in the Spectrum View window to use the same
          center frequency value. When the center frequency of any channel is changed, the center
          frequency of all other channels is automatically changed to match that value.
        - ``1`` sets all spectrum traces channels in the Spectrum View window to use the same center
          frequency value. When the center frequency of any channel is changed, the center frequency
          of all other channels is automatically changed to match that value.
        - ``0`` enables use of different center frequency values for each spectrum trace channel.
          The center frequencies of all channels are independent.
        - ``OFF`` enables use of different center frequency values for each spectrum trace channel.
          The center frequencies of all channels are independent.
    """


class SvChannelUnits(SCPICmdWrite, SCPICmdRead):
    """The ``SV:CH<x>:UNIts`` command.

    Description:
        - This command sets or queries the absolute logarithmic amplitude vertical scale units to
          show in the specified spectrum trace channel of the Spectrum View.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>:UNIts?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:CH<x>:UNIts value`` command.

    SCPI Syntax:
        ```
        - SV:CH<x>:UNIts {DBM|DBUW|DBMV|DBUV|DBMA|DBUA}
        - SV:CH<x>:UNIts?
        ```

    Info:
        - ``CH<x>`` specifies the analog channel to use as the Spectrum View source.
        - ``DBM`` specifies Decibel milliwatts (dBm).
        - ``DBUW`` specifies Decibel microwatts (dBµW).
        - ``DBMV`` specifies Decibel millivolts (dBmV).
        - ``DBUV`` specifies Decibel microvolts (dBµV).
        - ``DBMA`` specifies Decibel milliamperes (dBmA).
        - ``DBUA`` specifies Decibel microamperes (dBµA).
    """


class SvChannelSquelchThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``SV:CH<x>:SQUELCH:THReshold`` command.

    Description:
        - This command sets or queries the Squelch threshold value for the RF vs Time traces for the
          specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:SQUELCH:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SQUELCH:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:CH<x>:SQUELCH:THReshold value``
          command.

    SCPI Syntax:
        ```
        - SV:CH<x>:SQUELCH:THReshold <NR3>
        - SV:CH<x>:SQUELCH:THReshold?
        ```

    Info:
        - ``CH<x>`` is the channel number of the Magnitude vs. Time trace.
        - ``NR3`` sets the threshold value, in volts, applied to the Magnitude vs. Time trace that
          determines whether or not to show the Frequency and Phase vs. Time traces for the same
          channel.
    """


class SvChannelSquelchState(SCPICmdWrite, SCPICmdRead):
    """The ``SV:CH<x>:SQUELCH:STATE`` command.

    Description:
        - This command sets or queries whether Squelch is enabled for the RF vs Time traces for the
          specified channel. The frequency vs. time and phase vs. time traces aren't meaningful when
          the transmitting signal is turned off, as they just show broadband noise that clutters up
          the display. With squelch, a threshold may be defined for the magnitude vs. time trace to
          indicate when the transmitter is on/off. Then the frequency and phase vs. time traces are
          shown only when the magnitude vs. time trace is above the threshold and they are blanked
          out when it's below the threshold.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:SQUELCH:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SQUELCH:STATE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:CH<x>:SQUELCH:STATE value`` command.

    SCPI Syntax:
        ```
        - SV:CH<x>:SQUELCH:STATE {ON|OFF}
        - SV:CH<x>:SQUELCH:STATE?
        ```

    Info:
        - ``CH<x>`` is the channel number of the Frequency or Phase vs. Time trace.
        - ``ON`` enables (turns on) Squelch calculations.
        - ``OFF`` disables (turns off) Squelch calculations.
    """


class SvChannelSquelch(SCPICmdRead):
    """The ``SV:CH<x>:SQUELCH`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:SQUELCH?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SQUELCH?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` is the channel number of the Frequency or Phase vs. Time trace.

    Properties:
        - ``.state``: The ``SV:CH<x>:SQUELCH:STATE`` command.
        - ``.threshold``: The ``SV:CH<x>:SQUELCH:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = SvChannelSquelchState(device, f"{self._cmd_syntax}:STATE")
        self._threshold = SvChannelSquelchThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def state(self) -> SvChannelSquelchState:
        """Return the ``SV:CH<x>:SQUELCH:STATE`` command.

        Description:
            - This command sets or queries whether Squelch is enabled for the RF vs Time traces for
              the specified channel. The frequency vs. time and phase vs. time traces aren't
              meaningful when the transmitting signal is turned off, as they just show broadband
              noise that clutters up the display. With squelch, a threshold may be defined for the
              magnitude vs. time trace to indicate when the transmitter is on/off. Then the
              frequency and phase vs. time traces are shown only when the magnitude vs. time trace
              is above the threshold and they are blanked out when it's below the threshold.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:SQUELCH:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SQUELCH:STATE?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:CH<x>:SQUELCH:STATE value``
              command.

        SCPI Syntax:
            ```
            - SV:CH<x>:SQUELCH:STATE {ON|OFF}
            - SV:CH<x>:SQUELCH:STATE?
            ```

        Info:
            - ``CH<x>`` is the channel number of the Frequency or Phase vs. Time trace.
            - ``ON`` enables (turns on) Squelch calculations.
            - ``OFF`` disables (turns off) Squelch calculations.
        """
        return self._state

    @property
    def threshold(self) -> SvChannelSquelchThreshold:
        """Return the ``SV:CH<x>:SQUELCH:THReshold`` command.

        Description:
            - This command sets or queries the Squelch threshold value for the RF vs Time traces for
              the specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:SQUELCH:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SQUELCH:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:CH<x>:SQUELCH:THReshold value``
              command.

        SCPI Syntax:
            ```
            - SV:CH<x>:SQUELCH:THReshold <NR3>
            - SV:CH<x>:SQUELCH:THReshold?
            ```

        Info:
            - ``CH<x>`` is the channel number of the Magnitude vs. Time trace.
            - ``NR3`` sets the threshold value, in volts, applied to the Magnitude vs. Time trace
              that determines whether or not to show the Frequency and Phase vs. Time traces for the
              same channel.
        """
        return self._threshold


class SvChannelSelectSpectrogram(SCPICmdWrite, SCPICmdRead):
    """The ``SV:CH<x>:SELect:SPECtrogram`` command.

    Description:
        - This command sets or queries whether the spectrogram plot for the specified channel is
          displayed in the Spectrum View. The channel number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:SELect:SPECtrogram?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SELect:SPECtrogram?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:CH<x>:SELect:SPECtrogram value``
          command.

    SCPI Syntax:
        ```
        - SV:CH<x>:SELect:SPECtrogram {ON|OFF}
        - SV:CH<x>:SELect:SPECtrogram?
        ```

    Info:
        - ``ON`` turns on spectrogram.
        - ``OFF`` turns of spectrogram.
    """


class SvChannelSelectRfPhase(SCPICmdWrite, SCPICmdRead):
    """The ``SV:CH<x>:SELect:RF_PHASe`` command.

    Description:
        - This command sets or queries whether the Phase vs. Time trace for the specified channel is
          displayed in the Waveform View.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:SELect:RF_PHASe?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SELect:RF_PHASe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:CH<x>:SELect:RF_PHASe value``
          command.

    SCPI Syntax:
        ```
        - SV:CH<x>:SELect:RF_PHASe {ON|OFF}
        - SV:CH<x>:SELect:RF_PHASe?
        ```

    Info:
        - ``CH<x>`` is the channel number of the Phase vs. Time trace.
        - ``ON`` enables display of the Phase vs. Time trace.
        - ``OFF`` disables display of the Phase vs. Time trace.
    """


class SvChannelSelectRfNormal(SCPICmdWrite, SCPICmdRead):
    """The ``SV:CH<x>:SELect:RF_NORMal`` command.

    Description:
        - This command sets or queries whether the Normal trace is displayed for the specified
          spectrum trace channel in the Spectrum View.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:SELect:RF_NORMal?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SELect:RF_NORMal?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:CH<x>:SELect:RF_NORMal value``
          command.

    SCPI Syntax:
        ```
        - SV:CH<x>:SELect:RF_NORMal {ON|1|OFF|0}
        - SV:CH<x>:SELect:RF_NORMal?
        ```

    Info:
        - ``CH<x>`` specifies the spectrum trace channel source.
        - ``ON`` enables the display of the Normal trace for the specified spectrum trace channel.
        - ``OFF`` disables the display of the Normal trace for the specified spectrum trace channel.
        - ``1`` enables the display of the Normal trace for the specified spectrum trace channel.
        - ``0`` disables the display of the Normal trace for the specified spectrum trace channel.
    """


class SvChannelSelectRfMinhold(SCPICmdWrite, SCPICmdRead):
    """The ``SV:CH<x>:SELect:RF_MINHold`` command.

    Description:
        - This command sets or queries whether the Min Hold trace is displayed for the specified
          spectrum trace channel in the Spectrum View.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:SELect:RF_MINHold?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SELect:RF_MINHold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:CH<x>:SELect:RF_MINHold value``
          command.

    SCPI Syntax:
        ```
        - SV:CH<x>:SELect:RF_MINHold {ON|1|OFF|0}
        - SV:CH<x>:SELect:RF_MINHold?
        ```

    Info:
        - ``CH<x>`` specifies the spectrum trace channel source.
        - ``ON`` enables the display of the Min Hold trace for the specified spectrum trace channel.
        - ``OFF`` disables the display of the Min Hold trace for the specified spectrum trace
          channel.
        - ``1`` enables the display of the Min Hold trace for the specified spectrum trace channel.
        - ``0`` disables the display of the Min Hold trace for the specified spectrum trace channel.
    """


class SvChannelSelectRfMaxhold(SCPICmdWrite, SCPICmdRead):
    """The ``SV:CH<x>:SELect:RF_MAXHold`` command.

    Description:
        - This command sets or queries whether the Max Hold trace is displayed for the specified
          spectrum trace channel in the Spectrum View.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:SELect:RF_MAXHold?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SELect:RF_MAXHold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:CH<x>:SELect:RF_MAXHold value``
          command.

    SCPI Syntax:
        ```
        - SV:CH<x>:SELect:RF_MAXHold {ON|1|OFF|0}
        - SV:CH<x>:SELect:RF_MAXHold?
        ```

    Info:
        - ``CH<x>`` specifies the spectrum trace channel source.
        - ``ON`` enables the display of the Max Hold trace for the specified spectrum trace channel.
        - ``OFF`` disables the display of the Max Hold trace for the specified spectrum trace
          channel.
        - ``1`` enables the display of the Max Hold trace for the specified spectrum trace channel.
        - ``0`` disables the display of the Max Hold trace for the specified spectrum trace channel.
    """


class SvChannelSelectRfMagnitude(SCPICmdWrite, SCPICmdRead):
    """The ``SV:CH<x>:SELect:RF_MAGnitude`` command.

    Description:
        - This command sets or queries whether the Magnitude vs. Time trace for the specified
          channel is displayed in the Waveform View.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:SELect:RF_MAGnitude?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SELect:RF_MAGnitude?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:CH<x>:SELect:RF_MAGnitude value``
          command.

    SCPI Syntax:
        ```
        - SV:CH<x>:SELect:RF_MAGnitude {ON|OFF}
        - SV:CH<x>:SELect:RF_MAGnitude?
        ```

    Info:
        - ``CH<x>`` is the channel number of the Magnitude vs. Time trace.
        - ``ON`` enables display of the Magnitude vs. Time trace.
        - ``OFF`` disables display of the Magnitude vs. Time trace.
    """


class SvChannelSelectRfFrequency(SCPICmdWrite, SCPICmdRead):
    """The ``SV:CH<x>:SELect:RF_FREQuency`` command.

    Description:
        - This command sets or queries whether the Frequency vs. Time trace for the specified
          channel is displayed in the Waveform View.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:SELect:RF_FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SELect:RF_FREQuency?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:CH<x>:SELect:RF_FREQuency value``
          command.

    SCPI Syntax:
        ```
        - SV:CH<x>:SELect:RF_FREQuency {ON|OFF}
        - SV:CH<x>:SELect:RF_FREQuency?
        ```

    Info:
        - ``CH<x>`` is the channel number of the Frequency vs. Time trace.
        - ``ON`` enables display of the Frequency vs. Time trace.
        - ``OFF`` disables display of the Frequency vs. Time trace.
    """


class SvChannelSelectRfAverage(SCPICmdWrite, SCPICmdRead):
    """The ``SV:CH<x>:SELect:RF_AVErage`` command.

    Description:
        - This command sets or queries whether the Average trace is displayed for the specified
          spectrum trace channel in the Spectrum View.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:SELect:RF_AVErage?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SELect:RF_AVErage?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:CH<x>:SELect:RF_AVErage value``
          command.

    SCPI Syntax:
        ```
        - SV:CH<x>:SELect:RF_AVErage {ON|1|OFF|0}
        - SV:CH<x>:SELect:RF_AVErage?
        ```

    Info:
        - ``CH<x>`` specifies the spectrum trace channel source.
        - ``ON`` enables the display of the Average trace for the specified spectrum trace channel.
        - ``OFF`` disables the display of the Average trace for the specified spectrum trace
          channel.
        - ``1`` enables the display of the Average trace for the specified spectrum trace channel.
        - ``0`` disables the display of the Average trace for the specified spectrum trace channel.
    """


#  pylint: disable=too-many-instance-attributes
class SvChannelSelect(SCPICmdRead):
    """The ``SV:CH<x>:SELect`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:SELect?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SELect?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` specifies the spectrum trace channel source.

    Properties:
        - ``.rf_average``: The ``SV:CH<x>:SELect:RF_AVErage`` command.
        - ``.rf_frequency``: The ``SV:CH<x>:SELect:RF_FREQuency`` command.
        - ``.rf_magnitude``: The ``SV:CH<x>:SELect:RF_MAGnitude`` command.
        - ``.rf_maxhold``: The ``SV:CH<x>:SELect:RF_MAXHold`` command.
        - ``.rf_minhold``: The ``SV:CH<x>:SELect:RF_MINHold`` command.
        - ``.rf_normal``: The ``SV:CH<x>:SELect:RF_NORMal`` command.
        - ``.rf_phase``: The ``SV:CH<x>:SELect:RF_PHASe`` command.
        - ``.spectrogram``: The ``SV:CH<x>:SELect:SPECtrogram`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._rf_average = SvChannelSelectRfAverage(device, f"{self._cmd_syntax}:RF_AVErage")
        self._rf_frequency = SvChannelSelectRfFrequency(device, f"{self._cmd_syntax}:RF_FREQuency")
        self._rf_magnitude = SvChannelSelectRfMagnitude(device, f"{self._cmd_syntax}:RF_MAGnitude")
        self._rf_maxhold = SvChannelSelectRfMaxhold(device, f"{self._cmd_syntax}:RF_MAXHold")
        self._rf_minhold = SvChannelSelectRfMinhold(device, f"{self._cmd_syntax}:RF_MINHold")
        self._rf_normal = SvChannelSelectRfNormal(device, f"{self._cmd_syntax}:RF_NORMal")
        self._rf_phase = SvChannelSelectRfPhase(device, f"{self._cmd_syntax}:RF_PHASe")
        self._spectrogram = SvChannelSelectSpectrogram(device, f"{self._cmd_syntax}:SPECtrogram")

    @property
    def rf_average(self) -> SvChannelSelectRfAverage:
        """Return the ``SV:CH<x>:SELect:RF_AVErage`` command.

        Description:
            - This command sets or queries whether the Average trace is displayed for the specified
              spectrum trace channel in the Spectrum View.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:SELect:RF_AVErage?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SELect:RF_AVErage?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:CH<x>:SELect:RF_AVErage value``
              command.

        SCPI Syntax:
            ```
            - SV:CH<x>:SELect:RF_AVErage {ON|1|OFF|0}
            - SV:CH<x>:SELect:RF_AVErage?
            ```

        Info:
            - ``CH<x>`` specifies the spectrum trace channel source.
            - ``ON`` enables the display of the Average trace for the specified spectrum trace
              channel.
            - ``OFF`` disables the display of the Average trace for the specified spectrum trace
              channel.
            - ``1`` enables the display of the Average trace for the specified spectrum trace
              channel.
            - ``0`` disables the display of the Average trace for the specified spectrum trace
              channel.
        """
        return self._rf_average

    @property
    def rf_frequency(self) -> SvChannelSelectRfFrequency:
        """Return the ``SV:CH<x>:SELect:RF_FREQuency`` command.

        Description:
            - This command sets or queries whether the Frequency vs. Time trace for the specified
              channel is displayed in the Waveform View.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:SELect:RF_FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SELect:RF_FREQuency?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SV:CH<x>:SELect:RF_FREQuency value`` command.

        SCPI Syntax:
            ```
            - SV:CH<x>:SELect:RF_FREQuency {ON|OFF}
            - SV:CH<x>:SELect:RF_FREQuency?
            ```

        Info:
            - ``CH<x>`` is the channel number of the Frequency vs. Time trace.
            - ``ON`` enables display of the Frequency vs. Time trace.
            - ``OFF`` disables display of the Frequency vs. Time trace.
        """
        return self._rf_frequency

    @property
    def rf_magnitude(self) -> SvChannelSelectRfMagnitude:
        """Return the ``SV:CH<x>:SELect:RF_MAGnitude`` command.

        Description:
            - This command sets or queries whether the Magnitude vs. Time trace for the specified
              channel is displayed in the Waveform View.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:SELect:RF_MAGnitude?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SELect:RF_MAGnitude?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SV:CH<x>:SELect:RF_MAGnitude value`` command.

        SCPI Syntax:
            ```
            - SV:CH<x>:SELect:RF_MAGnitude {ON|OFF}
            - SV:CH<x>:SELect:RF_MAGnitude?
            ```

        Info:
            - ``CH<x>`` is the channel number of the Magnitude vs. Time trace.
            - ``ON`` enables display of the Magnitude vs. Time trace.
            - ``OFF`` disables display of the Magnitude vs. Time trace.
        """
        return self._rf_magnitude

    @property
    def rf_maxhold(self) -> SvChannelSelectRfMaxhold:
        """Return the ``SV:CH<x>:SELect:RF_MAXHold`` command.

        Description:
            - This command sets or queries whether the Max Hold trace is displayed for the specified
              spectrum trace channel in the Spectrum View.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:SELect:RF_MAXHold?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SELect:RF_MAXHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:CH<x>:SELect:RF_MAXHold value``
              command.

        SCPI Syntax:
            ```
            - SV:CH<x>:SELect:RF_MAXHold {ON|1|OFF|0}
            - SV:CH<x>:SELect:RF_MAXHold?
            ```

        Info:
            - ``CH<x>`` specifies the spectrum trace channel source.
            - ``ON`` enables the display of the Max Hold trace for the specified spectrum trace
              channel.
            - ``OFF`` disables the display of the Max Hold trace for the specified spectrum trace
              channel.
            - ``1`` enables the display of the Max Hold trace for the specified spectrum trace
              channel.
            - ``0`` disables the display of the Max Hold trace for the specified spectrum trace
              channel.
        """
        return self._rf_maxhold

    @property
    def rf_minhold(self) -> SvChannelSelectRfMinhold:
        """Return the ``SV:CH<x>:SELect:RF_MINHold`` command.

        Description:
            - This command sets or queries whether the Min Hold trace is displayed for the specified
              spectrum trace channel in the Spectrum View.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:SELect:RF_MINHold?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SELect:RF_MINHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:CH<x>:SELect:RF_MINHold value``
              command.

        SCPI Syntax:
            ```
            - SV:CH<x>:SELect:RF_MINHold {ON|1|OFF|0}
            - SV:CH<x>:SELect:RF_MINHold?
            ```

        Info:
            - ``CH<x>`` specifies the spectrum trace channel source.
            - ``ON`` enables the display of the Min Hold trace for the specified spectrum trace
              channel.
            - ``OFF`` disables the display of the Min Hold trace for the specified spectrum trace
              channel.
            - ``1`` enables the display of the Min Hold trace for the specified spectrum trace
              channel.
            - ``0`` disables the display of the Min Hold trace for the specified spectrum trace
              channel.
        """
        return self._rf_minhold

    @property
    def rf_normal(self) -> SvChannelSelectRfNormal:
        """Return the ``SV:CH<x>:SELect:RF_NORMal`` command.

        Description:
            - This command sets or queries whether the Normal trace is displayed for the specified
              spectrum trace channel in the Spectrum View.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:SELect:RF_NORMal?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SELect:RF_NORMal?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:CH<x>:SELect:RF_NORMal value``
              command.

        SCPI Syntax:
            ```
            - SV:CH<x>:SELect:RF_NORMal {ON|1|OFF|0}
            - SV:CH<x>:SELect:RF_NORMal?
            ```

        Info:
            - ``CH<x>`` specifies the spectrum trace channel source.
            - ``ON`` enables the display of the Normal trace for the specified spectrum trace
              channel.
            - ``OFF`` disables the display of the Normal trace for the specified spectrum trace
              channel.
            - ``1`` enables the display of the Normal trace for the specified spectrum trace
              channel.
            - ``0`` disables the display of the Normal trace for the specified spectrum trace
              channel.
        """
        return self._rf_normal

    @property
    def rf_phase(self) -> SvChannelSelectRfPhase:
        """Return the ``SV:CH<x>:SELect:RF_PHASe`` command.

        Description:
            - This command sets or queries whether the Phase vs. Time trace for the specified
              channel is displayed in the Waveform View.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:SELect:RF_PHASe?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SELect:RF_PHASe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:CH<x>:SELect:RF_PHASe value``
              command.

        SCPI Syntax:
            ```
            - SV:CH<x>:SELect:RF_PHASe {ON|OFF}
            - SV:CH<x>:SELect:RF_PHASe?
            ```

        Info:
            - ``CH<x>`` is the channel number of the Phase vs. Time trace.
            - ``ON`` enables display of the Phase vs. Time trace.
            - ``OFF`` disables display of the Phase vs. Time trace.
        """
        return self._rf_phase

    @property
    def spectrogram(self) -> SvChannelSelectSpectrogram:
        """Return the ``SV:CH<x>:SELect:SPECtrogram`` command.

        Description:
            - This command sets or queries whether the spectrogram plot for the specified channel is
              displayed in the Spectrum View. The channel number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:SELect:SPECtrogram?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SELect:SPECtrogram?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:CH<x>:SELect:SPECtrogram value``
              command.

        SCPI Syntax:
            ```
            - SV:CH<x>:SELect:SPECtrogram {ON|OFF}
            - SV:CH<x>:SELect:SPECtrogram?
            ```

        Info:
            - ``ON`` turns on spectrogram.
            - ``OFF`` turns of spectrogram.
        """
        return self._spectrogram


class SvChannelSeltrace(SCPICmdWrite, SCPICmdRead):
    """The ``SV:CH<x>:SELTrace`` command.

    Description:
        - This command sets or queries the spectrum trace type to show for the specified channel in
          the Spectrum View. Each channel's spectrum trace can display up to four traces; a Normal
          trace (default), a Max Hold trace, a Min Hold trace and an Average trace.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:SELTrace?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SELTrace?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:CH<x>:SELTrace value`` command.

    SCPI Syntax:
        ```
        - SV:CH<x>:SELTrace {NORMal|MAXHold|MINHold|AVErage}
        - SV:CH<x>:SELTrace?
        ```

    Info:
        - ``CH<x>`` specifies the analog channel to use as the Spectrum View source.
        - ``NORMal`` selects the Normal trace for the specified spectrum trace channel. If the
          specified spectrum trace channel does not have a Normal trace, this command is ignored.
        - ``MAXHold`` selects the Max Hold trace for the specified spectrum trace channel. If the
          specified spectrum trace channel does not have a Max Hold trace, this command is ignored.
        - ``MINHold`` selects the Min Hold trace for the specified spectrum trace channel. If the
          specified spectrum trace channel does not have a Min Hold trace, this command is ignored.
        - ``AVErage`` selects the Average trace for the specified spectrum trace channel. If the
          specified spectrum trace channel does not have an Average trace, this command is ignored.
    """


class SvChannelRfPhaseWrapState(SCPICmdWrite, SCPICmdRead):
    """The ``SV:CH<x>:RF_PHASe:WRAP:STATE`` command.

    Description:
        - This command sets or queries whether Phase Wrap is applied to the Phase vs. Time trace for
          the specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:RF_PHASe:WRAP:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>:RF_PHASe:WRAP:STATE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:CH<x>:RF_PHASe:WRAP:STATE value``
          command.

    SCPI Syntax:
        ```
        - SV:CH<x>:RF_PHASe:WRAP:STATE {ON|OFF}
        - SV:CH<x>:RF_PHASe:WRAP:STATE?
        ```

    Info:
        - ``CH<x>`` is the channel number of the Phase vs. Time trace.
        - ``ON`` enables applying phase wrap on the specified Phase vs. Time channel trace.
        - ``OFF`` disables applying phase wrap on the specified Phase vs. Time channel trace.
    """


class SvChannelRfPhaseWrapDegrees(SCPICmdWrite, SCPICmdRead):
    """The ``SV:CH<x>:RF_PHASe:WRAP:DEGrees`` command.

    Description:
        - This command sets or queries the Phase Wrap limit for the Phase vs. Time trace for the
          specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:RF_PHASe:WRAP:DEGrees?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>:RF_PHASe:WRAP:DEGrees?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:CH<x>:RF_PHASe:WRAP:DEGrees value``
          command.

    SCPI Syntax:
        ```
        - SV:CH<x>:RF_PHASe:WRAP:DEGrees <NR3>
        - SV:CH<x>:RF_PHASe:WRAP:DEGrees?
        ```

    Info:
        - ``CH<x>`` is the channel number of the Phase vs. Time trace.
        - ``NR3`` sets the number of wrap degrees, from 180 degrees to infinity. When Phase Wrap is
          enabled, the phase values in the Phase vs Time waveform are constrained to be within ± the
          specified limit. Phase values below or above the limit are wrapped by repeatedly adding or
          subtracting 360 degrees until they are within range.
    """


class SvChannelRfPhaseWrap(SCPICmdRead):
    """The ``SV:CH<x>:RF_PHASe:WRAP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:RF_PHASe:WRAP?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>:RF_PHASe:WRAP?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` is the channel number of the Phase vs. Time trace.

    Properties:
        - ``.degrees``: The ``SV:CH<x>:RF_PHASe:WRAP:DEGrees`` command.
        - ``.state``: The ``SV:CH<x>:RF_PHASe:WRAP:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._degrees = SvChannelRfPhaseWrapDegrees(device, f"{self._cmd_syntax}:DEGrees")
        self._state = SvChannelRfPhaseWrapState(device, f"{self._cmd_syntax}:STATE")

    @property
    def degrees(self) -> SvChannelRfPhaseWrapDegrees:
        """Return the ``SV:CH<x>:RF_PHASe:WRAP:DEGrees`` command.

        Description:
            - This command sets or queries the Phase Wrap limit for the Phase vs. Time trace for the
              specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:RF_PHASe:WRAP:DEGrees?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:CH<x>:RF_PHASe:WRAP:DEGrees?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SV:CH<x>:RF_PHASe:WRAP:DEGrees value`` command.

        SCPI Syntax:
            ```
            - SV:CH<x>:RF_PHASe:WRAP:DEGrees <NR3>
            - SV:CH<x>:RF_PHASe:WRAP:DEGrees?
            ```

        Info:
            - ``CH<x>`` is the channel number of the Phase vs. Time trace.
            - ``NR3`` sets the number of wrap degrees, from 180 degrees to infinity. When Phase Wrap
              is enabled, the phase values in the Phase vs Time waveform are constrained to be
              within ± the specified limit. Phase values below or above the limit are wrapped by
              repeatedly adding or subtracting 360 degrees until they are within range.
        """
        return self._degrees

    @property
    def state(self) -> SvChannelRfPhaseWrapState:
        """Return the ``SV:CH<x>:RF_PHASe:WRAP:STATE`` command.

        Description:
            - This command sets or queries whether Phase Wrap is applied to the Phase vs. Time trace
              for the specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:RF_PHASe:WRAP:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:CH<x>:RF_PHASe:WRAP:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SV:CH<x>:RF_PHASe:WRAP:STATE value`` command.

        SCPI Syntax:
            ```
            - SV:CH<x>:RF_PHASe:WRAP:STATE {ON|OFF}
            - SV:CH<x>:RF_PHASe:WRAP:STATE?
            ```

        Info:
            - ``CH<x>`` is the channel number of the Phase vs. Time trace.
            - ``ON`` enables applying phase wrap on the specified Phase vs. Time channel trace.
            - ``OFF`` disables applying phase wrap on the specified Phase vs. Time channel trace.
        """
        return self._state


class SvChannelRfPhaseReferenceTime(SCPICmdWrite, SCPICmdRead):
    """The ``SV:CH<x>:RF_PHASe:REFerence:TIMe`` command.

    Description:
        - This command sets or queries the channel Phase Reference time in seconds.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:RF_PHASe:REFerence:TIMe?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>:RF_PHASe:REFerence:TIMe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SV:CH<x>:RF_PHASe:REFerence:TIMe value`` command.

    SCPI Syntax:
        ```
        - SV:CH<x>:RF_PHASe:REFerence:TIMe <NR3>
        - SV:CH<x>:RF_PHASe:REFerence:TIMe?
        ```

    Info:
        - ``CH<x>`` is the channel number of the Phase vs. Time trace.
        - ``NR3`` is the Phase Reference time, in seconds. This indicates the time at which the
          phase value set by ``SV:CH<x>:RF_PHASe:REFerence:DEGrees`` is applied. If the phase
          position set by ``SV:CH<x>:RF_PHASe:REFerence:POSition`` is TRIGger, then the phase time
          is fixed at 0 seconds and cannot be changed. If the phase position is CURSor, then the
          phase time may be set to any value, and is initialized to the position of Cursor A. If
          CH<x> is the master phase reference, then the time is used to calculate the phase values
          of all other channels.
    """


class SvChannelRfPhaseReferencePosition(SCPICmdWrite, SCPICmdRead):
    """The ``SV:CH<x>:RF_PHASe:REFerence:POSition`` command.

    Description:
        - This command sets or queries whether the channel Phase Reference is located at the Trigger
          position or at the Cursor A position.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:RF_PHASe:REFerence:POSition?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SV:CH<x>:RF_PHASe:REFerence:POSition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SV:CH<x>:RF_PHASe:REFerence:POSition value`` command.

    SCPI Syntax:
        ```
        - SV:CH<x>:RF_PHASe:REFerence:POSition {TRIGger|CURSor}
        - SV:CH<x>:RF_PHASe:REFerence:POSition?
        ```

    Info:
        - ``CH<x>`` is the channel number of the Phase vs. Time trace.
        - ``TRIGger`` sets the Phase Reference location to the Trigger position.
        - ``CURSor`` sets the channel Phase Reference location to the phase time set by
          ``SV:CH<x>:RF_PHASe:REFerence:TIMe``, which defaults to the Cursor A position.
    """


class SvChannelRfPhaseReferenceDegrees(SCPICmdWrite, SCPICmdRead):
    """The ``SV:CH<x>:RF_PHASe:REFerence:DEGrees`` command.

    Description:
        - This command sets or queries the channel Phase Reference value in degrees.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:RF_PHASe:REFerence:DEGrees?``
          query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>:RF_PHASe:REFerence:DEGrees?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SV:CH<x>:RF_PHASe:REFerence:DEGrees value`` command.

    SCPI Syntax:
        ```
        - SV:CH<x>:RF_PHASe:REFerence:DEGrees <NR3>
        - SV:CH<x>:RF_PHASe:REFerence:DEGrees?
        ```

    Info:
        - ``CH<x>`` is the channel number of the Phase vs. Time trace.
        - ``NR3`` is the Phase Reference value, in degrees. This indicates a fixed phase value at
          the phase time set by ``SV:CH<x>:RF_PHASe:REFerence:TIMe``. If CH<x> is the master phase
          reference, then the value is used to calculate the phase values of all other channels.
    """


class SvChannelRfPhaseReference(SCPICmdRead):
    """The ``SV:CH<x>:RF_PHASe:REFerence`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:RF_PHASe:REFerence?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>:RF_PHASe:REFerence?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` is the channel number of the Phase vs. Time trace.

    Properties:
        - ``.degrees``: The ``SV:CH<x>:RF_PHASe:REFerence:DEGrees`` command.
        - ``.position``: The ``SV:CH<x>:RF_PHASe:REFerence:POSition`` command.
        - ``.time``: The ``SV:CH<x>:RF_PHASe:REFerence:TIMe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._degrees = SvChannelRfPhaseReferenceDegrees(device, f"{self._cmd_syntax}:DEGrees")
        self._position = SvChannelRfPhaseReferencePosition(device, f"{self._cmd_syntax}:POSition")
        self._time = SvChannelRfPhaseReferenceTime(device, f"{self._cmd_syntax}:TIMe")

    @property
    def degrees(self) -> SvChannelRfPhaseReferenceDegrees:
        """Return the ``SV:CH<x>:RF_PHASe:REFerence:DEGrees`` command.

        Description:
            - This command sets or queries the channel Phase Reference value in degrees.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:RF_PHASe:REFerence:DEGrees?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SV:CH<x>:RF_PHASe:REFerence:DEGrees?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SV:CH<x>:RF_PHASe:REFerence:DEGrees value`` command.

        SCPI Syntax:
            ```
            - SV:CH<x>:RF_PHASe:REFerence:DEGrees <NR3>
            - SV:CH<x>:RF_PHASe:REFerence:DEGrees?
            ```

        Info:
            - ``CH<x>`` is the channel number of the Phase vs. Time trace.
            - ``NR3`` is the Phase Reference value, in degrees. This indicates a fixed phase value
              at the phase time set by ``SV:CH<x>:RF_PHASe:REFerence:TIMe``. If CH<x> is the master
              phase reference, then the value is used to calculate the phase values of all other
              channels.
        """
        return self._degrees

    @property
    def position(self) -> SvChannelRfPhaseReferencePosition:
        """Return the ``SV:CH<x>:RF_PHASe:REFerence:POSition`` command.

        Description:
            - This command sets or queries whether the channel Phase Reference is located at the
              Trigger position or at the Cursor A position.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:RF_PHASe:REFerence:POSition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SV:CH<x>:RF_PHASe:REFerence:POSition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SV:CH<x>:RF_PHASe:REFerence:POSition value`` command.

        SCPI Syntax:
            ```
            - SV:CH<x>:RF_PHASe:REFerence:POSition {TRIGger|CURSor}
            - SV:CH<x>:RF_PHASe:REFerence:POSition?
            ```

        Info:
            - ``CH<x>`` is the channel number of the Phase vs. Time trace.
            - ``TRIGger`` sets the Phase Reference location to the Trigger position.
            - ``CURSor`` sets the channel Phase Reference location to the phase time set by
              ``SV:CH<x>:RF_PHASe:REFerence:TIMe``, which defaults to the Cursor A position.
        """
        return self._position

    @property
    def time(self) -> SvChannelRfPhaseReferenceTime:
        """Return the ``SV:CH<x>:RF_PHASe:REFerence:TIMe`` command.

        Description:
            - This command sets or queries the channel Phase Reference time in seconds.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:RF_PHASe:REFerence:TIMe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SV:CH<x>:RF_PHASe:REFerence:TIMe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SV:CH<x>:RF_PHASe:REFerence:TIMe value`` command.

        SCPI Syntax:
            ```
            - SV:CH<x>:RF_PHASe:REFerence:TIMe <NR3>
            - SV:CH<x>:RF_PHASe:REFerence:TIMe?
            ```

        Info:
            - ``CH<x>`` is the channel number of the Phase vs. Time trace.
            - ``NR3`` is the Phase Reference time, in seconds. This indicates the time at which the
              phase value set by ``SV:CH<x>:RF_PHASe:REFerence:DEGrees`` is applied. If the phase
              position set by ``SV:CH<x>:RF_PHASe:REFerence:POSition`` is TRIGger, then the phase
              time is fixed at 0 seconds and cannot be changed. If the phase position is CURSor,
              then the phase time may be set to any value, and is initialized to the position of
              Cursor A. If CH<x> is the master phase reference, then the time is used to calculate
              the phase values of all other channels.
        """
        return self._time


class SvChannelRfPhase(SCPICmdRead):
    """The ``SV:CH<x>:RF_PHASe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:RF_PHASe?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>:RF_PHASe?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` is the channel number of the Phase vs. Time trace.

    Properties:
        - ``.reference``: The ``SV:CH<x>:RF_PHASe:REFerence`` command tree.
        - ``.wrap``: The ``SV:CH<x>:RF_PHASe:WRAP`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._reference = SvChannelRfPhaseReference(device, f"{self._cmd_syntax}:REFerence")
        self._wrap = SvChannelRfPhaseWrap(device, f"{self._cmd_syntax}:WRAP")

    @property
    def reference(self) -> SvChannelRfPhaseReference:
        """Return the ``SV:CH<x>:RF_PHASe:REFerence`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:RF_PHASe:REFerence?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:CH<x>:RF_PHASe:REFerence?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` is the channel number of the Phase vs. Time trace.

        Sub-properties:
            - ``.degrees``: The ``SV:CH<x>:RF_PHASe:REFerence:DEGrees`` command.
            - ``.position``: The ``SV:CH<x>:RF_PHASe:REFerence:POSition`` command.
            - ``.time``: The ``SV:CH<x>:RF_PHASe:REFerence:TIMe`` command.
        """
        return self._reference

    @property
    def wrap(self) -> SvChannelRfPhaseWrap:
        """Return the ``SV:CH<x>:RF_PHASe:WRAP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:RF_PHASe:WRAP?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:CH<x>:RF_PHASe:WRAP?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` is the channel number of the Phase vs. Time trace.

        Sub-properties:
            - ``.degrees``: The ``SV:CH<x>:RF_PHASe:WRAP:DEGrees`` command.
            - ``.state``: The ``SV:CH<x>:RF_PHASe:WRAP:STATE`` command.
        """
        return self._wrap


class SvChannelRfMagnitudeFormat(SCPICmdWrite, SCPICmdRead):
    """The ``SV:CH<x>:RF_MAGnitude:FORMat`` command.

    Description:
        - This command sets or queries the format of the Magnitude vs. Time trace for the specified
          channel.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:RF_MAGnitude:FORMat?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>:RF_MAGnitude:FORMat?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:CH<x>:RF_MAGnitude:FORMat value``
          command.

    SCPI Syntax:
        ```
        - SV:CH<x>:RF_MAGnitude:FORMat {AMPLINear|POWLINear|POWLOG}
        - SV:CH<x>:RF_MAGnitude:FORMat?
        ```

    Info:
        - ``CH<x>`` is the channel number of the Magnitude vs. Time trace.
        - ``AMPLINear`` (Amplitude (linear)) sets the magnitude in Volts with square root conversion
          of linear power values.
        - ``POWLINear`` (Power (linear) sets the magnitude in Watts with direct use of linear power
          values.
        - ``POWLOG`` (Power (log) sets the magnitude in dB using log conversion of linear power
          values.
    """


class SvChannelRfMagnitude(SCPICmdRead):
    """The ``SV:CH<x>:RF_MAGnitude`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:RF_MAGnitude?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>:RF_MAGnitude?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` is the channel number of the Magnitude vs. Time trace.

    Properties:
        - ``.format``: The ``SV:CH<x>:RF_MAGnitude:FORMat`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._format = SvChannelRfMagnitudeFormat(device, f"{self._cmd_syntax}:FORMat")

    @property
    def format(self) -> SvChannelRfMagnitudeFormat:
        """Return the ``SV:CH<x>:RF_MAGnitude:FORMat`` command.

        Description:
            - This command sets or queries the format of the Magnitude vs. Time trace for the
              specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:RF_MAGnitude:FORMat?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:CH<x>:RF_MAGnitude:FORMat?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SV:CH<x>:RF_MAGnitude:FORMat value`` command.

        SCPI Syntax:
            ```
            - SV:CH<x>:RF_MAGnitude:FORMat {AMPLINear|POWLINear|POWLOG}
            - SV:CH<x>:RF_MAGnitude:FORMat?
            ```

        Info:
            - ``CH<x>`` is the channel number of the Magnitude vs. Time trace.
            - ``AMPLINear`` (Amplitude (linear)) sets the magnitude in Volts with square root
              conversion of linear power values.
            - ``POWLINear`` (Power (linear) sets the magnitude in Watts with direct use of linear
              power values.
            - ``POWLOG`` (Power (log) sets the magnitude in dB using log conversion of linear power
              values.
        """
        return self._format


class SvChannelRfAverageNumavg(SCPICmdWrite, SCPICmdRead):
    """The ``SV:CH<x>:RF_AVErage:NUMAVg`` command.

    Description:
        - This command sets or queries the number of acquisitions to be used when creating the
          Average trace for the specified spectrum trace channel in the Spectrum View. The Average
          spectrum trace shows the average of values from multiple acquisitions at each trace point.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:RF_AVErage:NUMAVg?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>:RF_AVErage:NUMAVg?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:CH<x>:RF_AVErage:NUMAVg value``
          command.

    SCPI Syntax:
        ```
        - SV:CH<x>:RF_AVErage:NUMAVg <NR1>
        - SV:CH<x>:RF_AVErage:NUMAVg?
        ```

    Info:
        - ``CH<x>`` specifies the spectrum trace channel source.
        - ``<NR1>`` specifies the number of acquisitions to average. The range is 2 - 512, in
          exponential increments.
    """


class SvChannelRfAverage(SCPICmdRead):
    """The ``SV:CH<x>:RF_AVErage`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:RF_AVErage?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>:RF_AVErage?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` specifies the spectrum trace channel source.

    Properties:
        - ``.numavg``: The ``SV:CH<x>:RF_AVErage:NUMAVg`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._numavg = SvChannelRfAverageNumavg(device, f"{self._cmd_syntax}:NUMAVg")

    @property
    def numavg(self) -> SvChannelRfAverageNumavg:
        """Return the ``SV:CH<x>:RF_AVErage:NUMAVg`` command.

        Description:
            - This command sets or queries the number of acquisitions to be used when creating the
              Average trace for the specified spectrum trace channel in the Spectrum View. The
              Average spectrum trace shows the average of values from multiple acquisitions at each
              trace point.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:RF_AVErage:NUMAVg?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:CH<x>:RF_AVErage:NUMAVg?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:CH<x>:RF_AVErage:NUMAVg value``
              command.

        SCPI Syntax:
            ```
            - SV:CH<x>:RF_AVErage:NUMAVg <NR1>
            - SV:CH<x>:RF_AVErage:NUMAVg?
            ```

        Info:
            - ``CH<x>`` specifies the spectrum trace channel source.
            - ``<NR1>`` specifies the number of acquisitions to average. The range is 2 - 512, in
              exponential increments.
        """
        return self._numavg


class SvChannel(ValidatedChannel, SCPICmdRead):
    """The ``SV:CH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` specifies the spectrum trace channel source.

    Properties:
        - ``.rf_average``: The ``SV:CH<x>:RF_AVErage`` command tree.
        - ``.rf_magnitude``: The ``SV:CH<x>:RF_MAGnitude`` command tree.
        - ``.rf_phase``: The ``SV:CH<x>:RF_PHASe`` command tree.
        - ``.seltrace``: The ``SV:CH<x>:SELTrace`` command.
        - ``.select``: The ``SV:CH<x>:SELect`` command tree.
        - ``.squelch``: The ``SV:CH<x>:SQUELCH`` command tree.
        - ``.units``: The ``SV:CH<x>:UNIts`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._rf_average = SvChannelRfAverage(device, f"{self._cmd_syntax}:RF_AVErage")
        self._rf_magnitude = SvChannelRfMagnitude(device, f"{self._cmd_syntax}:RF_MAGnitude")
        self._rf_phase = SvChannelRfPhase(device, f"{self._cmd_syntax}:RF_PHASe")
        self._seltrace = SvChannelSeltrace(device, f"{self._cmd_syntax}:SELTrace")
        self._select = SvChannelSelect(device, f"{self._cmd_syntax}:SELect")
        self._squelch = SvChannelSquelch(device, f"{self._cmd_syntax}:SQUELCH")
        self._units = SvChannelUnits(device, f"{self._cmd_syntax}:UNIts")

    @property
    def rf_average(self) -> SvChannelRfAverage:
        """Return the ``SV:CH<x>:RF_AVErage`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:RF_AVErage?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:CH<x>:RF_AVErage?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` specifies the spectrum trace channel source.

        Sub-properties:
            - ``.numavg``: The ``SV:CH<x>:RF_AVErage:NUMAVg`` command.
        """
        return self._rf_average

    @property
    def rf_magnitude(self) -> SvChannelRfMagnitude:
        """Return the ``SV:CH<x>:RF_MAGnitude`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:RF_MAGnitude?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:CH<x>:RF_MAGnitude?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` is the channel number of the Magnitude vs. Time trace.

        Sub-properties:
            - ``.format``: The ``SV:CH<x>:RF_MAGnitude:FORMat`` command.
        """
        return self._rf_magnitude

    @property
    def rf_phase(self) -> SvChannelRfPhase:
        """Return the ``SV:CH<x>:RF_PHASe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:RF_PHASe?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:CH<x>:RF_PHASe?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` is the channel number of the Phase vs. Time trace.

        Sub-properties:
            - ``.reference``: The ``SV:CH<x>:RF_PHASe:REFerence`` command tree.
            - ``.wrap``: The ``SV:CH<x>:RF_PHASe:WRAP`` command tree.
        """
        return self._rf_phase

    @property
    def seltrace(self) -> SvChannelSeltrace:
        """Return the ``SV:CH<x>:SELTrace`` command.

        Description:
            - This command sets or queries the spectrum trace type to show for the specified channel
              in the Spectrum View. Each channel's spectrum trace can display up to four traces; a
              Normal trace (default), a Max Hold trace, a Min Hold trace and an Average trace.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:SELTrace?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SELTrace?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:CH<x>:SELTrace value`` command.

        SCPI Syntax:
            ```
            - SV:CH<x>:SELTrace {NORMal|MAXHold|MINHold|AVErage}
            - SV:CH<x>:SELTrace?
            ```

        Info:
            - ``CH<x>`` specifies the analog channel to use as the Spectrum View source.
            - ``NORMal`` selects the Normal trace for the specified spectrum trace channel. If the
              specified spectrum trace channel does not have a Normal trace, this command is
              ignored.
            - ``MAXHold`` selects the Max Hold trace for the specified spectrum trace channel. If
              the specified spectrum trace channel does not have a Max Hold trace, this command is
              ignored.
            - ``MINHold`` selects the Min Hold trace for the specified spectrum trace channel. If
              the specified spectrum trace channel does not have a Min Hold trace, this command is
              ignored.
            - ``AVErage`` selects the Average trace for the specified spectrum trace channel. If the
              specified spectrum trace channel does not have an Average trace, this command is
              ignored.
        """
        return self._seltrace

    @property
    def select(self) -> SvChannelSelect:
        """Return the ``SV:CH<x>:SELect`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:SELect?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SELect?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` specifies the spectrum trace channel source.

        Sub-properties:
            - ``.rf_average``: The ``SV:CH<x>:SELect:RF_AVErage`` command.
            - ``.rf_frequency``: The ``SV:CH<x>:SELect:RF_FREQuency`` command.
            - ``.rf_magnitude``: The ``SV:CH<x>:SELect:RF_MAGnitude`` command.
            - ``.rf_maxhold``: The ``SV:CH<x>:SELect:RF_MAXHold`` command.
            - ``.rf_minhold``: The ``SV:CH<x>:SELect:RF_MINHold`` command.
            - ``.rf_normal``: The ``SV:CH<x>:SELect:RF_NORMal`` command.
            - ``.rf_phase``: The ``SV:CH<x>:SELect:RF_PHASe`` command.
            - ``.spectrogram``: The ``SV:CH<x>:SELect:SPECtrogram`` command.
        """
        return self._select

    @property
    def squelch(self) -> SvChannelSquelch:
        """Return the ``SV:CH<x>:SQUELCH`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:SQUELCH?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SQUELCH?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` is the channel number of the Frequency or Phase vs. Time trace.

        Sub-properties:
            - ``.state``: The ``SV:CH<x>:SQUELCH:STATE`` command.
            - ``.threshold``: The ``SV:CH<x>:SQUELCH:THReshold`` command.
        """
        return self._squelch

    @property
    def units(self) -> SvChannelUnits:
        """Return the ``SV:CH<x>:UNIts`` command.

        Description:
            - This command sets or queries the absolute logarithmic amplitude vertical scale units
              to show in the specified spectrum trace channel of the Spectrum View.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:CH<x>:UNIts?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:CH<x>:UNIts value`` command.

        SCPI Syntax:
            ```
            - SV:CH<x>:UNIts {DBM|DBUW|DBMV|DBUV|DBMA|DBUA}
            - SV:CH<x>:UNIts?
            ```

        Info:
            - ``CH<x>`` specifies the analog channel to use as the Spectrum View source.
            - ``DBM`` specifies Decibel milliwatts (dBm).
            - ``DBUW`` specifies Decibel microwatts (dBµW).
            - ``DBMV`` specifies Decibel millivolts (dBmV).
            - ``DBUV`` specifies Decibel microvolts (dBµV).
            - ``DBMA`` specifies Decibel milliamperes (dBmA).
            - ``DBUA`` specifies Decibel microamperes (dBµA).
        """
        return self._units


#  pylint: disable=too-many-instance-attributes
class Sv(SCPICmdRead):
    """The ``SV`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV?`` query.
        - Using the ``.verify(value)`` method will send the ``SV?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``SV:CH<x>`` command tree.
        - ``.lockcenter``: The ``SV:LOCKCenter`` command.
        - ``.lockspectrum``: The ``SV:LOCKSpectrum`` command.
        - ``.marker``: The ``SV:MARKER`` command tree.
        - ``.rbw``: The ``SV:RBW`` command.
        - ``.rbwmode``: The ``SV:RBWMode`` command.
        - ``.rf_phase``: The ``SV:RF_PHASe`` command tree.
        - ``.span``: The ``SV:SPAN`` command.
        - ``.spanrbwratio``: The ``SV:SPANRBWRatio`` command.
        - ``.spectrogram``: The ``SV:SPECtrogram`` command tree.
        - ``.window``: The ``SV:WINDOW`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SV") -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, SvChannel] = DefaultDictPassKeyToFactory(
            lambda x: SvChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._lockcenter = SvLockcenter(device, f"{self._cmd_syntax}:LOCKCenter")
        self._lockspectrum = SvLockspectrum(device, f"{self._cmd_syntax}:LOCKSpectrum")
        self._marker = SvMarker(device, f"{self._cmd_syntax}:MARKER")
        self._rbw = SvRbw(device, f"{self._cmd_syntax}:RBW")
        self._rbwmode = SvRbwmode(device, f"{self._cmd_syntax}:RBWMode")
        self._rf_phase = SvRfPhase(device, f"{self._cmd_syntax}:RF_PHASe")
        self._span = SvSpan(device, f"{self._cmd_syntax}:SPAN")
        self._spanrbwratio = SvSpanrbwratio(device, f"{self._cmd_syntax}:SPANRBWRatio")
        self._spectrogram = SvSpectrogram(device, f"{self._cmd_syntax}:SPECtrogram")
        self._window = SvWindow(device, f"{self._cmd_syntax}:WINDOW")

    @property
    def ch(self) -> Dict[int, SvChannel]:
        """Return the ``SV:CH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:CH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` specifies the spectrum trace channel source.

        Sub-properties:
            - ``.rf_average``: The ``SV:CH<x>:RF_AVErage`` command tree.
            - ``.rf_magnitude``: The ``SV:CH<x>:RF_MAGnitude`` command tree.
            - ``.rf_phase``: The ``SV:CH<x>:RF_PHASe`` command tree.
            - ``.seltrace``: The ``SV:CH<x>:SELTrace`` command.
            - ``.select``: The ``SV:CH<x>:SELect`` command tree.
            - ``.squelch``: The ``SV:CH<x>:SQUELCH`` command tree.
            - ``.units``: The ``SV:CH<x>:UNIts`` command.
        """
        return self._ch

    @property
    def lockcenter(self) -> SvLockcenter:
        """Return the ``SV:LOCKCenter`` command.

        Description:
            - This command sets or queries whether the Center Frequency setting is locked across all
              channels in the Spectrum View.

        Usage:
            - Using the ``.query()`` method will send the ``SV:LOCKCenter?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:LOCKCenter?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:LOCKCenter value`` command.

        SCPI Syntax:
            ```
            - SV:LOCKCenter {ON|1|OFF|0}
            - SV:LOCKCenter?
            ```

        Info:
            - ``ON`` sets all spectrum traces channels in the Spectrum View window to use the same
              center frequency value. When the center frequency of any channel is changed, the
              center frequency of all other channels is automatically changed to match that value.
            - ``1`` sets all spectrum traces channels in the Spectrum View window to use the same
              center frequency value. When the center frequency of any channel is changed, the
              center frequency of all other channels is automatically changed to match that value.
            - ``0`` enables use of different center frequency values for each spectrum trace
              channel. The center frequencies of all channels are independent.
            - ``OFF`` enables use of different center frequency values for each spectrum trace
              channel. The center frequencies of all channels are independent.
        """
        return self._lockcenter

    @property
    def lockspectrum(self) -> SvLockspectrum:
        """Return the ``SV:LOCKSpectrum`` command.

        Description:
            - This command sets or queries whether the Spectrum Time value is locked across all
              spectrum trace channels in the Spectrum View.

        Usage:
            - Using the ``.query()`` method will send the ``SV:LOCKSpectrum?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:LOCKSpectrum?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:LOCKSpectrum value`` command.

        SCPI Syntax:
            ```
            - SV:LOCKSpectrum {ON|1|OFF|0}
            - SV:LOCKSpectrum?
            ```

        Info:
            - ``ON`` sets all spectrum traces channels in the Spectrum View window to use the same
              Spectrum Time value. When the Spectrum Time of any channel is changed, the Spectrum
              Time of all other channels is automatically changed to match that value.
            - ``1`` sets all spectrum traces channels in the Spectrum View window to use the same
              Spectrum Time value. When the Spectrum Time of any channel is changed, the Spectrum
              Time of all other channels is automatically changed to match that value.
            - ``0`` enables use of different Spectrum Time values for each spectrum trace channel.
              The Spectrum Time of all channels are independent.
            - ``OFF`` enables use of different Spectrum Time values for each spectrum trace channel.
              The Spectrum Time of all channels are independent.
        """
        return self._lockspectrum

    @property
    def marker(self) -> SvMarker:
        """Return the ``SV:MARKER`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:MARKER?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:MARKER?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.peak``: The ``SV:MARKER:PEAK`` command tree.
            - ``.peaks``: The ``SV:MARKER:PEAKS`` command tree.
            - ``.reference``: The ``SV:MARKER:REFERence`` command.
            - ``.type``: The ``SV:MARKER:TYPe`` command.
        """
        return self._marker

    @property
    def rbw(self) -> SvRbw:
        """Return the ``SV:RBW`` command.

        Description:
            - This command sets or queries the resolution bandwidth (RBW) when the RBW mode has been
              set to MANUAL (using the command ``SV:RBWMode``). The resolution bandwidth is the
              width of the narrowest measurable band of frequencies in a Spectrum View trace. By
              default, the RBW tracks the span value in a ``1000:1`` ratio. The RBW determines the
              level to which the instrument can resolve individual frequencies in the frequency
              domain. For example, if the input signal contains two carriers separated by 1 kHz, you
              will not be able to discriminate between them unless the RBW is less than 1 kHz.

        Usage:
            - Using the ``.query()`` method will send the ``SV:RBW?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:RBW?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:RBW value`` command.

        SCPI Syntax:
            ```
            - SV:RBW <NR3>
            - SV:RBW?
            ```

        Info:
            - ``<NR3>`` specifies the width of the narrowest measurable band of frequencies in a
              Spectrum View trace, in Hz.
        """
        return self._rbw

    @property
    def rbwmode(self) -> SvRbwmode:
        """Return the ``SV:RBWMode`` command.

        Description:
            - This command sets or queries the resolution bandwidth (RBW) mode, either Automatic or
              Manual.

        Usage:
            - Using the ``.query()`` method will send the ``SV:RBWMode?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:RBWMode?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:RBWMode value`` command.

        SCPI Syntax:
            ```
            - SV:RBWMode {AUTOmatic|MANual}
            - SV:RBWMode?
            ```

        Info:
            - ``AUTOmatic`` specifies the resolution bandwidth automatically as the span is changed.
              The default behavior is ``1000:1``, but you can set it to other values in a 1-2-5
              sequence (e.g. 10000, 20000, 50000). To specify the RBW ratio that will be used when
              the mode is set to automatic, use the command ``SV:SPANRBWRatio``.
            - ``MANual`` specifies to set the resolution bandwidth, independently from the span,
              using the command ``SV:RBW``.
        """
        return self._rbwmode

    @property
    def rf_phase(self) -> SvRfPhase:
        """Return the ``SV:RF_PHASe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:RF_PHASe?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:RF_PHASe?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.reference``: The ``SV:RF_PHASe:REFerence`` command tree.
        """
        return self._rf_phase

    @property
    def span(self) -> SvSpan:
        """Return the ``SV:SPAN`` command.

        Description:
            - This command sets or queries the span setting for all channels in the Spectrum View.
              The span is the range of frequencies that can be observed centered on the center
              frequency. This is the width of the frequency domain trace, which is from the center
              frequency - ½span to the center frequency + ½ span.

        Usage:
            - Using the ``.query()`` method will send the ``SV:SPAN?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:SPAN?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:SPAN value`` command.

        SCPI Syntax:
            ```
            - SV:SPAN <NR3>
            - SV:SPAN?
            ```

        Info:
            - ``<NR3>`` specifies the span value in Hz.
        """
        return self._span

    @property
    def spanrbwratio(self) -> SvSpanrbwratio:
        """Return the ``SV:SPANRBWRatio`` command.

        Description:
            - This command sets or queries the ratio of the span to the resolution bandwidth (RBW)
              that will be used when the RBW Mode is set to AUTO. The span is the width of the
              frequency domain trace in Hz, which is equal to the stop frequency minus the start
              frequency. The RBW is the width of the narrowest measurable band of frequencies in a
              frequency domain trace. The default RBW ratio is 1000 : 1. Use the command
              ``SV:RBWMode`` to set the RBW Mode to Automatic.

        Usage:
            - Using the ``.query()`` method will send the ``SV:SPANRBWRatio?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:SPANRBWRatio?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:SPANRBWRatio value`` command.

        SCPI Syntax:
            ```
            - SV:SPANRBWRatio <NR3>
            - SV:SPANRBWRatio?
            ```

        Info:
            - ``<NR3>`` specifies the span-to-RBW ratio.
        """
        return self._spanrbwratio

    @property
    def spectrogram(self) -> SvSpectrogram:
        """Return the ``SV:SPECtrogram`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:SPECtrogram?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:SPECtrogram?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.cscale``: The ``SV:SPECtrogram:CSCale`` command tree.
            - ``.cursor``: The ``SV:SPECtrogram:CURSor`` command tree.
        """
        return self._spectrogram

    @property
    def window(self) -> SvWindow:
        """Return the ``SV:WINDOW`` command.

        Description:
            - This command sets or queries the window type used by the windowing function of the
              Spectrum View. The windowing function is a Fast Fourier Transform (FFT) technique used
              to minimize the discontinuities between successive frames of an RF time domain signal.
              The default window type is Blackman-Harris.

        Usage:
            - Using the ``.query()`` method will send the ``SV:WINDOW?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:WINDOW?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:WINDOW value`` command.

        SCPI Syntax:
            ```
            - SV:WINDOW {KAISerbessel|RECTangular|HAMMing|HANNing|BLACkmanharris|FLATtop2}
            - SV:WINDOW?
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
