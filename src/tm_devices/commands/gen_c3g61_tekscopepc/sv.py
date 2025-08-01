"""The sv commands module.

These commands are used in the following models:
TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SV:CH<x>:SELect:SPECtrogram {ON|OFF}
    - SV:CH<x>:SELect:SPECtrogram?
    - SV:LOCKCenter {ON|OFF|1|0}
    - SV:LOCKCenter?
    - SV:LOCKSpectrum {ON|OFF|1|0}
    - SV:LOCKSpectrum?
    - SV:MARKER:PEAK:EXCURsion <NR3>
    - SV:MARKER:PEAK:EXCURsion?
    - SV:MARKER:PEAK:MAXimum <NR1>
    - SV:MARKER:PEAK:MAXimum?
    - SV:MARKER:PEAK:STATE {CH<x>}
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
    - SV:RF_PHASe:REFerence:MASTer {CH<x>|NONE}
    - SV:RF_PHASe:REFerence:MASTer?
    - SV:S<x>_CH<x>:RF_AVErage:NUMAVg <NR1>
    - SV:S<x>_CH<x>:RF_AVErage:NUMAVg?
    - SV:S<x>_CH<x>:RF_MAGnitude:FORMat {AMPLINear|POWLINear|POWLOG}
    - SV:S<x>_CH<x>:RF_MAGnitude:FORMat?
    - SV:S<x>_CH<x>:RF_PHASe:REFerence:DEGrees <NR3>
    - SV:S<x>_CH<x>:RF_PHASe:REFerence:DEGrees?
    - SV:S<x>_CH<x>:RF_PHASe:REFerence:POSition {TRIGger|CURSor}
    - SV:S<x>_CH<x>:RF_PHASe:REFerence:POSition?
    - SV:S<x>_CH<x>:RF_PHASe:REFerence:TIMe <NR3>
    - SV:S<x>_CH<x>:RF_PHASe:REFerence:TIMe?
    - SV:S<x>_CH<x>:RF_PHASe:WRAP:DEGrees <NR3>
    - SV:S<x>_CH<x>:RF_PHASe:WRAP:DEGrees?
    - SV:S<x>_CH<x>:RF_PHASe:WRAP:STATE {ON|OFF}
    - SV:S<x>_CH<x>:RF_PHASe:WRAP:STATE?
    - SV:S<x>_CH<x>:SELTrace {NORMal|MAXHold|MINHold|AVErage}
    - SV:S<x>_CH<x>:SELTrace?
    - SV:S<x>_CH<x>:SELect:RF_AVErage {ON|OFF|1|0}
    - SV:S<x>_CH<x>:SELect:RF_AVErage?
    - SV:S<x>_CH<x>:SELect:RF_FREQuency {ON|OFF}
    - SV:S<x>_CH<x>:SELect:RF_FREQuency?
    - SV:S<x>_CH<x>:SELect:RF_MAGnitude {ON|OFF}
    - SV:S<x>_CH<x>:SELect:RF_MAGnitude?
    - SV:S<x>_CH<x>:SELect:RF_MAXHold {ON|OFF|1|0}
    - SV:S<x>_CH<x>:SELect:RF_MAXHold?
    - SV:S<x>_CH<x>:SELect:RF_MINHold {ON|OFF|1|0}
    - SV:S<x>_CH<x>:SELect:RF_MINHold?
    - SV:S<x>_CH<x>:SELect:RF_NORMal {ON|OFF|1|0}
    - SV:S<x>_CH<x>:SELect:RF_NORMal?
    - SV:S<x>_CH<x>:SELect:RF_PHASe {ON|OFF}
    - SV:S<x>_CH<x>:SELect:RF_PHASe?
    - SV:S<x>_CH<x>:SELect:SPECtrogram {ON|OFF}
    - SV:S<x>_CH<x>:SELect:SPECtrogram?
    - SV:S<x>_CH<x>:SQUELCH:STATE {ON|OFF}
    - SV:S<x>_CH<x>:SQUELCH:STATE?
    - SV:S<x>_CH<x>:SQUELCH:THReshold <NR3>
    - SV:S<x>_CH<x>:SQUELCH:THReshold?
    - SV:S<x>_CH<x>:UNIts {DBM|DBUW|DBMV|DBUV|DBMA|DBUA}
    - SV:S<x>_CH<x>:UNIts?
    - SV:SPECtrogram:CSCale:MAX <NR3>
    - SV:SPECtrogram:CSCale:MAX?
    - SV:SPECtrogram:CSCale:MIN <NR3>
    - SV:SPECtrogram:CSCale:MIN?
    - SV:SPECtrogram:CURSor:A {ON|OFF|1|0}
    - SV:SPECtrogram:CURSor:A?
    - SV:SPECtrogram:CURSor:B {ON|OFF|1|0}
    - SV:SPECtrogram:CURSor:B?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    SCPICmdWriteNoArguments,
    ValidatedChannel,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


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
        - SV:SPECtrogram:CURSor:B {ON|OFF|1|0}
        - SV:SPECtrogram:CURSor:B?
        ```

    Info:
        - ``1`` turns on the spectrum trace for cursor B position.
        - ``0`` turns off the spectrum trace for cursor B position. Off is the default.
        - ``ON`` turns on the spectrum trace for cursor B position.
        - ``OFF`` turns off the spectrum trace for cursor B position. Off is the default.
    """


class SvSpectrogramCursorA(SCPICmdWrite, SCPICmdRead):
    """The ``SV:SPECtrogram:CURSor:A`` command.

    Description:
        - This command sets or queries whether the spectrum trace at cursor A position is selected
          or not.

    Usage:
        - Using the ``.query()`` method will send the ``SV:SPECtrogram:CURSor:A?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:SPECtrogram:CURSor:A?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:SPECtrogram:CURSor:A value``
          command.

    SCPI Syntax:
        ```
        - SV:SPECtrogram:CURSor:A {ON|OFF|1|0}
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
            - This command sets or queries whether the spectrum trace at cursor A position is
              selected or not.

        Usage:
            - Using the ``.query()`` method will send the ``SV:SPECtrogram:CURSor:A?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:SPECtrogram:CURSor:A?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:SPECtrogram:CURSor:A value``
              command.

        SCPI Syntax:
            ```
            - SV:SPECtrogram:CURSor:A {ON|OFF|1|0}
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
            - SV:SPECtrogram:CURSor:B {ON|OFF|1|0}
            - SV:SPECtrogram:CURSor:B?
            ```

        Info:
            - ``1`` turns on the spectrum trace for cursor B position.
            - ``0`` turns off the spectrum trace for cursor B position. Off is the default.
            - ``ON`` turns on the spectrum trace for cursor B position.
            - ``OFF`` turns off the spectrum trace for cursor B position. Off is the default.
        """
        return self._b


class SvSpectrogramCscaleMin(SCPICmdWrite, SCPICmdRead):
    """The ``SV:SPECtrogram:CSCale:MIN`` command.

    Description:
        - This command sets or queries the minimum color scale value. Minimum must be < Maximum. If
          the user is adjusting Minimum up to the point where it would be the same as Minimum, then
          Maximum begins incrementing as needed to stay 1 dB above minimum.

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
        - ``<NR3>`` sets the maximum color scale value. The default value is 0.0 and the valid range
          is -169.0 to 100.0.
    """


class SvSpectrogramCscaleMax(SCPICmdWrite, SCPICmdRead):
    """The ``SV:SPECtrogram:CSCale:MAX`` command.

    Description:
        - This command sets or queries the maximum color scale value. Maximum must be > Minimum. If
          the user is adjusting Maximum down to the point where it would be the same as Minimum,
          then Minimum begins decrementing as needed to stay 1 dB below Maximum.

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
              If the user is adjusting Maximum down to the point where it would be the same as
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
              If the user is adjusting Minimum up to the point where it would be the same as
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
            - ``<NR3>`` sets the maximum color scale value. The default value is 0.0 and the valid
              range is -169.0 to 100.0.
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


class SvSItemChannelUnits(SCPICmdWrite, SCPICmdRead):
    """The ``SV:S<x>_CH<x>:UNIts`` command.

    Description:
        - This command sets or queries the absolute logarithmic amplitude vertical scale units to
          show in the specified spectrum trace remote scope channel of the Spectrum View. S<x> is
          the remote scope number and Ch<x> is the channel number to use as the Spectrum View
          source.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:UNIts?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:S<x>_CH<x>:UNIts value`` command.

    SCPI Syntax:
        ```
        - SV:S<x>_CH<x>:UNIts {DBM|DBUW|DBMV|DBUV|DBMA|DBUA}
        - SV:S<x>_CH<x>:UNIts?
        ```

    Info:
        - ``DBM`` specifies Decibel milliwatts (dBm).
        - ``DBUW`` specifies Decibel microwatts (dBµW).
        - ``DBMV`` specifies Decibel millivolts (dBmV).
        - ``DBUV`` specifies Decibel microvolts (dBµV).
        - ``DBMA`` specifies Decibel milliamperes (dBmA).
        - ``DBUA`` specifies Decibel microamperes (dBµA).
    """


class SvSItemChannelSquelchThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``SV:S<x>_CH<x>:SQUELCH:THReshold`` command.

    Description:
        - This command sets or queries the Squelch threshold value for the RF vs Time traces for the
          specified channel. S<x> is the remote scope number and Ch<x> is the channel number to use
          as the Spectrum View source.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SQUELCH:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:SQUELCH:THReshold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:S<x>_CH<x>:SQUELCH:THReshold value``
          command.

    SCPI Syntax:
        ```
        - SV:S<x>_CH<x>:SQUELCH:THReshold <NR3>
        - SV:S<x>_CH<x>:SQUELCH:THReshold?
        ```

    Info:
        - ``NR3`` sets the threshold value, in volts, applied to the Magnitude vs. Time trace that
          determines whether or not to show the Frequency and Phase vs. Time traces for the same
          channel.
    """


class SvSItemChannelSquelchState(SCPICmdWrite, SCPICmdRead):
    """The ``SV:S<x>_CH<x>:SQUELCH:STATE`` command.

    Description:
        - This command sets or queries whether Squelch is enabled for the RF vs Time traces for the
          specified channel. The frequency vs. time and phase vs. time traces aren't meaningful when
          the transmitting signal is turned off, as they just show broadband noise that clutters up
          the display. With squelch, a threshold may be defined for the magnitude vs. time trace to
          indicate when the transmitter is on/off. Then the frequency and phase vs. time traces are
          shown only when the magnitude vs. time trace is above the threshold and they are blanked
          out when it's below the threshold. S<x> is the remote scope number and Ch<x> is the
          channel number to use as the Spectrum View source.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SQUELCH:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:SQUELCH:STATE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:S<x>_CH<x>:SQUELCH:STATE value``
          command.

    SCPI Syntax:
        ```
        - SV:S<x>_CH<x>:SQUELCH:STATE {ON|OFF}
        - SV:S<x>_CH<x>:SQUELCH:STATE?
        ```

    Info:
        - ``ON`` enables (turns on) Squelch calculations.
        - ``OFF`` disables (turns off) Squelch calculations.
    """


class SvSItemChannelSquelch(SCPICmdRead):
    """The ``SV:S<x>_CH<x>:SQUELCH`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SQUELCH?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:SQUELCH?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``SV:S<x>_CH<x>:SQUELCH:STATE`` command.
        - ``.threshold``: The ``SV:S<x>_CH<x>:SQUELCH:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = SvSItemChannelSquelchState(device, f"{self._cmd_syntax}:STATE")
        self._threshold = SvSItemChannelSquelchThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def state(self) -> SvSItemChannelSquelchState:
        """Return the ``SV:S<x>_CH<x>:SQUELCH:STATE`` command.

        Description:
            - This command sets or queries whether Squelch is enabled for the RF vs Time traces for
              the specified channel. The frequency vs. time and phase vs. time traces aren't
              meaningful when the transmitting signal is turned off, as they just show broadband
              noise that clutters up the display. With squelch, a threshold may be defined for the
              magnitude vs. time trace to indicate when the transmitter is on/off. Then the
              frequency and phase vs. time traces are shown only when the magnitude vs. time trace
              is above the threshold and they are blanked out when it's below the threshold. S<x> is
              the remote scope number and Ch<x> is the channel number to use as the Spectrum View
              source.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SQUELCH:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:SQUELCH:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:S<x>_CH<x>:SQUELCH:STATE value``
              command.

        SCPI Syntax:
            ```
            - SV:S<x>_CH<x>:SQUELCH:STATE {ON|OFF}
            - SV:S<x>_CH<x>:SQUELCH:STATE?
            ```

        Info:
            - ``ON`` enables (turns on) Squelch calculations.
            - ``OFF`` disables (turns off) Squelch calculations.
        """
        return self._state

    @property
    def threshold(self) -> SvSItemChannelSquelchThreshold:
        """Return the ``SV:S<x>_CH<x>:SQUELCH:THReshold`` command.

        Description:
            - This command sets or queries the Squelch threshold value for the RF vs Time traces for
              the specified channel. S<x> is the remote scope number and Ch<x> is the channel number
              to use as the Spectrum View source.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SQUELCH:THReshold?``
              query.
            - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:SQUELCH:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SV:S<x>_CH<x>:SQUELCH:THReshold value`` command.

        SCPI Syntax:
            ```
            - SV:S<x>_CH<x>:SQUELCH:THReshold <NR3>
            - SV:S<x>_CH<x>:SQUELCH:THReshold?
            ```

        Info:
            - ``NR3`` sets the threshold value, in volts, applied to the Magnitude vs. Time trace
              that determines whether or not to show the Frequency and Phase vs. Time traces for the
              same channel.
        """
        return self._threshold


class SvSItemChannelSelectSpectrogram(SCPICmdWrite, SCPICmdRead):
    """The ``SV:S<x>_CH<x>:SELect:SPECtrogram`` command.

    Description:
        - This command sets or queries whether the spectrogram plot for the specified channel is
          displayed in the Spectrum View.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SELect:SPECtrogram?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:SELect:SPECtrogram?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SV:S<x>_CH<x>:SELect:SPECtrogram value`` command.

    SCPI Syntax:
        ```
        - SV:S<x>_CH<x>:SELect:SPECtrogram {ON|OFF}
        - SV:S<x>_CH<x>:SELect:SPECtrogram?
        ```

    Info:
        - ``S<x>`` is the remote scope number and CH<x> specifies the analog channel as source.
        - ``ON`` turns on spectrogram.
        - ``OFF`` turns of spectrogram.
    """


class SvSItemChannelSelectRfPhase(SCPICmdWrite, SCPICmdRead):
    """The ``SV:S<x>_CH<x>:SELect:RF_PHASe`` command.

    Description:
        - This command sets or queries whether the Phase vs. Time trace for the specified channel is
          displayed in the Waveform View. S<x> is the remote scope number and Ch<x> is the channel
          number to use as the Spectrum View source.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SELect:RF_PHASe?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:SELect:RF_PHASe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:S<x>_CH<x>:SELect:RF_PHASe value``
          command.

    SCPI Syntax:
        ```
        - SV:S<x>_CH<x>:SELect:RF_PHASe {ON|OFF}
        - SV:S<x>_CH<x>:SELect:RF_PHASe?
        ```

    Info:
        - ``ON`` enables display of the Phase vs. Time trace.
        - ``OFF`` disables display of the Phase vs. Time trace.
    """


class SvSItemChannelSelectRfNormal(SCPICmdWrite, SCPICmdRead):
    """The ``SV:S<x>_CH<x>:SELect:RF_NORMal`` command.

    Description:
        - This command sets or queries whether the Normal trace is displayed for the specified
          spectrum trace channel in the Spectrum View. S<x> is the remote scope number and Ch<x> is
          the channel number to use as the Spectrum View source.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SELect:RF_NORMal?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:SELect:RF_NORMal?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:S<x>_CH<x>:SELect:RF_NORMal value``
          command.

    SCPI Syntax:
        ```
        - SV:S<x>_CH<x>:SELect:RF_NORMal {ON|OFF|1|0}
        - SV:S<x>_CH<x>:SELect:RF_NORMal?
        ```

    Info:
        - ``ON, 1`` enables the display of the Normal trace for the specified spectrum trace
          channel.
        - ``OFF, 0`` disables the display of the Normal trace for the specified spectrum trace
          channel.
    """


class SvSItemChannelSelectRfMinhold(SCPICmdWrite, SCPICmdRead):
    """The ``SV:S<x>_CH<x>:SELect:RF_MINHold`` command.

    Description:
        - This command sets or queries whether the Min Hold trace is displayed for the specified
          spectrum trace channel in the Spectrum View. S<x> is the remote scope number and Ch<x> is
          the channel number to use as the Spectrum View source.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SELect:RF_MINHold?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:SELect:RF_MINHold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:S<x>_CH<x>:SELect:RF_MINHold value``
          command.

    SCPI Syntax:
        ```
        - SV:S<x>_CH<x>:SELect:RF_MINHold {ON|OFF|1|0}
        - SV:S<x>_CH<x>:SELect:RF_MINHold?
        ```

    Info:
        - ``ON, 1`` enables the display of the Min Hold trace for the specified spectrum trace
          channel.
        - ``OFF, 0`` disables the display of the Min Hold trace for the specified spectrum trace
          channel.
    """


class SvSItemChannelSelectRfMaxhold(SCPICmdWrite, SCPICmdRead):
    """The ``SV:S<x>_CH<x>:SELect:RF_MAXHold`` command.

    Description:
        - This command sets or queries whether the Max Hold trace is displayed for the specified
          spectrum trace channel in the Spectrum View. S<x> is the remote scope number and Ch<x> is
          the channel number to use as the Spectrum View source.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SELect:RF_MAXHold?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:SELect:RF_MAXHold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:S<x>_CH<x>:SELect:RF_MAXHold value``
          command.

    SCPI Syntax:
        ```
        - SV:S<x>_CH<x>:SELect:RF_MAXHold {ON|OFF|1|0}
        - SV:S<x>_CH<x>:SELect:RF_MAXHold?
        ```

    Info:
        - ``ON, 1`` enables the display of the Max Hold trace for the specified spectrum trace
          channel.
        - ``OFF, 0`` disables the display of the Max Hold trace for the specified spectrum trace
          channel.
    """


class SvSItemChannelSelectRfMagnitude(SCPICmdWrite, SCPICmdRead):
    """The ``SV:S<x>_CH<x>:SELect:RF_MAGnitude`` command.

    Description:
        - This command sets or queries whether the Magnitude vs. Time trace for the specified
          channel is displayed in the Waveform View. S<x> is the remote scope number and Ch<x> is
          the channel number to use as the Spectrum View source.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SELect:RF_MAGnitude?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:SELect:RF_MAGnitude?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SV:S<x>_CH<x>:SELect:RF_MAGnitude value`` command.

    SCPI Syntax:
        ```
        - SV:S<x>_CH<x>:SELect:RF_MAGnitude {ON|OFF}
        - SV:S<x>_CH<x>:SELect:RF_MAGnitude?
        ```

    Info:
        - ``ON`` enables display of the Magnitude vs. Time trace.
        - ``OFF`` disables display of the Magnitude vs. Time trace.
    """


class SvSItemChannelSelectRfFrequency(SCPICmdWrite, SCPICmdRead):
    """The ``SV:S<x>_CH<x>:SELect:RF_FREQuency`` command.

    Description:
        - This command sets or queries whether the Frequency vs. Time trace for the specified
          channel is displayed in the Waveform View. S<x> is the remote scope number and Ch<x> is
          the channel number to use as the Spectrum View source.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SELect:RF_FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:SELect:RF_FREQuency?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SV:S<x>_CH<x>:SELect:RF_FREQuency value`` command.

    SCPI Syntax:
        ```
        - SV:S<x>_CH<x>:SELect:RF_FREQuency {ON|OFF}
        - SV:S<x>_CH<x>:SELect:RF_FREQuency?
        ```

    Info:
        - ``ON`` enables display of the Frequency vs. Time trace.
        - ``OFF`` disables display of the Frequency vs. Time trace.
    """


class SvSItemChannelSelectRfAverage(SCPICmdWrite, SCPICmdRead):
    """The ``SV:S<x>_CH<x>:SELect:RF_AVErage`` command.

    Description:
        - This command sets or queries whether the Average trace is displayed for the specified
          spectrum trace channel in the Spectrum View. S<x> is the remote scope number and Ch<x> is
          the channel number to use as the Spectrum View source.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SELect:RF_AVErage?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:SELect:RF_AVErage?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:S<x>_CH<x>:SELect:RF_AVErage value``
          command.

    SCPI Syntax:
        ```
        - SV:S<x>_CH<x>:SELect:RF_AVErage {ON|OFF|1|0}
        - SV:S<x>_CH<x>:SELect:RF_AVErage?
        ```

    Info:
        - ``ON, 1`` enables the display of the Average trace for the specified spectrum trace
          channel.
        - ``OFF, 0`` disables the display of the Average trace for the specified spectrum trace
          channel.
    """


class SvSItemChannelSelectRf(SCPICmdRead):
    """The ``SV:S<x>_CH<x>:SELect:RF`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SELect:RF?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:SELect:RF?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.average``: The ``SV:S<x>_CH<x>:SELect:RF_AVErage`` command.
        - ``.frequency``: The ``SV:S<x>_CH<x>:SELect:RF_FREQuency`` command.
        - ``.magnitude``: The ``SV:S<x>_CH<x>:SELect:RF_MAGnitude`` command.
        - ``.maxhold``: The ``SV:S<x>_CH<x>:SELect:RF_MAXHold`` command.
        - ``.minhold``: The ``SV:S<x>_CH<x>:SELect:RF_MINHold`` command.
        - ``.normal``: The ``SV:S<x>_CH<x>:SELect:RF_NORMal`` command.
        - ``.phase``: The ``SV:S<x>_CH<x>:SELect:RF_PHASe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._average = SvSItemChannelSelectRfAverage(device, f"{self._cmd_syntax}_AVErage")
        self._frequency = SvSItemChannelSelectRfFrequency(device, f"{self._cmd_syntax}_FREQuency")
        self._magnitude = SvSItemChannelSelectRfMagnitude(device, f"{self._cmd_syntax}_MAGnitude")
        self._maxhold = SvSItemChannelSelectRfMaxhold(device, f"{self._cmd_syntax}_MAXHold")
        self._minhold = SvSItemChannelSelectRfMinhold(device, f"{self._cmd_syntax}_MINHold")
        self._normal = SvSItemChannelSelectRfNormal(device, f"{self._cmd_syntax}_NORMal")
        self._phase = SvSItemChannelSelectRfPhase(device, f"{self._cmd_syntax}_PHASe")

    @property
    def average(self) -> SvSItemChannelSelectRfAverage:
        """Return the ``SV:S<x>_CH<x>:SELect:RF_AVErage`` command.

        Description:
            - This command sets or queries whether the Average trace is displayed for the specified
              spectrum trace channel in the Spectrum View. S<x> is the remote scope number and Ch<x>
              is the channel number to use as the Spectrum View source.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SELect:RF_AVErage?``
              query.
            - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:SELect:RF_AVErage?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SV:S<x>_CH<x>:SELect:RF_AVErage value`` command.

        SCPI Syntax:
            ```
            - SV:S<x>_CH<x>:SELect:RF_AVErage {ON|OFF|1|0}
            - SV:S<x>_CH<x>:SELect:RF_AVErage?
            ```

        Info:
            - ``ON, 1`` enables the display of the Average trace for the specified spectrum trace
              channel.
            - ``OFF, 0`` disables the display of the Average trace for the specified spectrum trace
              channel.
        """
        return self._average

    @property
    def frequency(self) -> SvSItemChannelSelectRfFrequency:
        """Return the ``SV:S<x>_CH<x>:SELect:RF_FREQuency`` command.

        Description:
            - This command sets or queries whether the Frequency vs. Time trace for the specified
              channel is displayed in the Waveform View. S<x> is the remote scope number and Ch<x>
              is the channel number to use as the Spectrum View source.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SELect:RF_FREQuency?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SV:S<x>_CH<x>:SELect:RF_FREQuency?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SV:S<x>_CH<x>:SELect:RF_FREQuency value`` command.

        SCPI Syntax:
            ```
            - SV:S<x>_CH<x>:SELect:RF_FREQuency {ON|OFF}
            - SV:S<x>_CH<x>:SELect:RF_FREQuency?
            ```

        Info:
            - ``ON`` enables display of the Frequency vs. Time trace.
            - ``OFF`` disables display of the Frequency vs. Time trace.
        """
        return self._frequency

    @property
    def magnitude(self) -> SvSItemChannelSelectRfMagnitude:
        """Return the ``SV:S<x>_CH<x>:SELect:RF_MAGnitude`` command.

        Description:
            - This command sets or queries whether the Magnitude vs. Time trace for the specified
              channel is displayed in the Waveform View. S<x> is the remote scope number and Ch<x>
              is the channel number to use as the Spectrum View source.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SELect:RF_MAGnitude?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SV:S<x>_CH<x>:SELect:RF_MAGnitude?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SV:S<x>_CH<x>:SELect:RF_MAGnitude value`` command.

        SCPI Syntax:
            ```
            - SV:S<x>_CH<x>:SELect:RF_MAGnitude {ON|OFF}
            - SV:S<x>_CH<x>:SELect:RF_MAGnitude?
            ```

        Info:
            - ``ON`` enables display of the Magnitude vs. Time trace.
            - ``OFF`` disables display of the Magnitude vs. Time trace.
        """
        return self._magnitude

    @property
    def maxhold(self) -> SvSItemChannelSelectRfMaxhold:
        """Return the ``SV:S<x>_CH<x>:SELect:RF_MAXHold`` command.

        Description:
            - This command sets or queries whether the Max Hold trace is displayed for the specified
              spectrum trace channel in the Spectrum View. S<x> is the remote scope number and Ch<x>
              is the channel number to use as the Spectrum View source.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SELect:RF_MAXHold?``
              query.
            - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:SELect:RF_MAXHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SV:S<x>_CH<x>:SELect:RF_MAXHold value`` command.

        SCPI Syntax:
            ```
            - SV:S<x>_CH<x>:SELect:RF_MAXHold {ON|OFF|1|0}
            - SV:S<x>_CH<x>:SELect:RF_MAXHold?
            ```

        Info:
            - ``ON, 1`` enables the display of the Max Hold trace for the specified spectrum trace
              channel.
            - ``OFF, 0`` disables the display of the Max Hold trace for the specified spectrum trace
              channel.
        """
        return self._maxhold

    @property
    def minhold(self) -> SvSItemChannelSelectRfMinhold:
        """Return the ``SV:S<x>_CH<x>:SELect:RF_MINHold`` command.

        Description:
            - This command sets or queries whether the Min Hold trace is displayed for the specified
              spectrum trace channel in the Spectrum View. S<x> is the remote scope number and Ch<x>
              is the channel number to use as the Spectrum View source.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SELect:RF_MINHold?``
              query.
            - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:SELect:RF_MINHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SV:S<x>_CH<x>:SELect:RF_MINHold value`` command.

        SCPI Syntax:
            ```
            - SV:S<x>_CH<x>:SELect:RF_MINHold {ON|OFF|1|0}
            - SV:S<x>_CH<x>:SELect:RF_MINHold?
            ```

        Info:
            - ``ON, 1`` enables the display of the Min Hold trace for the specified spectrum trace
              channel.
            - ``OFF, 0`` disables the display of the Min Hold trace for the specified spectrum trace
              channel.
        """
        return self._minhold

    @property
    def normal(self) -> SvSItemChannelSelectRfNormal:
        """Return the ``SV:S<x>_CH<x>:SELect:RF_NORMal`` command.

        Description:
            - This command sets or queries whether the Normal trace is displayed for the specified
              spectrum trace channel in the Spectrum View. S<x> is the remote scope number and Ch<x>
              is the channel number to use as the Spectrum View source.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SELect:RF_NORMal?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:SELect:RF_NORMal?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SV:S<x>_CH<x>:SELect:RF_NORMal value`` command.

        SCPI Syntax:
            ```
            - SV:S<x>_CH<x>:SELect:RF_NORMal {ON|OFF|1|0}
            - SV:S<x>_CH<x>:SELect:RF_NORMal?
            ```

        Info:
            - ``ON, 1`` enables the display of the Normal trace for the specified spectrum trace
              channel.
            - ``OFF, 0`` disables the display of the Normal trace for the specified spectrum trace
              channel.
        """
        return self._normal

    @property
    def phase(self) -> SvSItemChannelSelectRfPhase:
        """Return the ``SV:S<x>_CH<x>:SELect:RF_PHASe`` command.

        Description:
            - This command sets or queries whether the Phase vs. Time trace for the specified
              channel is displayed in the Waveform View. S<x> is the remote scope number and Ch<x>
              is the channel number to use as the Spectrum View source.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SELect:RF_PHASe?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:SELect:RF_PHASe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SV:S<x>_CH<x>:SELect:RF_PHASe value`` command.

        SCPI Syntax:
            ```
            - SV:S<x>_CH<x>:SELect:RF_PHASe {ON|OFF}
            - SV:S<x>_CH<x>:SELect:RF_PHASe?
            ```

        Info:
            - ``ON`` enables display of the Phase vs. Time trace.
            - ``OFF`` disables display of the Phase vs. Time trace.
        """
        return self._phase


class SvSItemChannelSelect(SCPICmdRead):
    """The ``SV:S<x>_CH<x>:SELect`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SELect?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:SELect?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.rf``: The ``SV:S<x>_CH<x>:SELect:RF`` command tree.
        - ``.spectrogram``: The ``SV:S<x>_CH<x>:SELect:SPECtrogram`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._rf = SvSItemChannelSelectRf(device, f"{self._cmd_syntax}:RF")
        self._spectrogram = SvSItemChannelSelectSpectrogram(
            device, f"{self._cmd_syntax}:SPECtrogram"
        )

    @property
    def rf(self) -> SvSItemChannelSelectRf:
        """Return the ``SV:S<x>_CH<x>:SELect:RF`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SELect:RF?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:SELect:RF?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.average``: The ``SV:S<x>_CH<x>:SELect:RF_AVErage`` command.
            - ``.frequency``: The ``SV:S<x>_CH<x>:SELect:RF_FREQuency`` command.
            - ``.magnitude``: The ``SV:S<x>_CH<x>:SELect:RF_MAGnitude`` command.
            - ``.maxhold``: The ``SV:S<x>_CH<x>:SELect:RF_MAXHold`` command.
            - ``.minhold``: The ``SV:S<x>_CH<x>:SELect:RF_MINHold`` command.
            - ``.normal``: The ``SV:S<x>_CH<x>:SELect:RF_NORMal`` command.
            - ``.phase``: The ``SV:S<x>_CH<x>:SELect:RF_PHASe`` command.
        """
        return self._rf

    @property
    def spectrogram(self) -> SvSItemChannelSelectSpectrogram:
        """Return the ``SV:S<x>_CH<x>:SELect:SPECtrogram`` command.

        Description:
            - This command sets or queries whether the spectrogram plot for the specified channel is
              displayed in the Spectrum View.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SELect:SPECtrogram?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SV:S<x>_CH<x>:SELect:SPECtrogram?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SV:S<x>_CH<x>:SELect:SPECtrogram value`` command.

        SCPI Syntax:
            ```
            - SV:S<x>_CH<x>:SELect:SPECtrogram {ON|OFF}
            - SV:S<x>_CH<x>:SELect:SPECtrogram?
            ```

        Info:
            - ``S<x>`` is the remote scope number and CH<x> specifies the analog channel as source.
            - ``ON`` turns on spectrogram.
            - ``OFF`` turns of spectrogram.
        """
        return self._spectrogram


class SvSItemChannelSeltrace(SCPICmdWrite, SCPICmdRead):
    """The ``SV:S<x>_CH<x>:SELTrace`` command.

    Description:
        - This command sets or queries the spectrum trace type to show for the specified channel in
          the Spectrum View. Each channel's spectrum trace can display up to four traces; a Normal
          trace (default), a Max Hold trace, a Min Hold trace and an Average trace. S<x> is the
          remote scope number and Ch<x> is the channel number to use as the Spectrum View source.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SELTrace?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:SELTrace?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:S<x>_CH<x>:SELTrace value`` command.

    SCPI Syntax:
        ```
        - SV:S<x>_CH<x>:SELTrace {NORMal|MAXHold|MINHold|AVErage}
        - SV:S<x>_CH<x>:SELTrace?
        ```

    Info:
        - ``NORMal`` selects the Normal trace for the specified spectrum trace channel. If the
          specified spectrum trace channel does not have a Normal trace, this command is ignored.
        - ``MAXHold`` selects the Max Hold trace for the specified spectrum trace channel. If the
          specified spectrum trace channel does not have a Max Hold trace, this command is ignored.
        - ``MINHold`` selects the Min Hold trace for the specified spectrum trace channel. If the
          specified spectrum trace channel does not have a Min Hold trace, this command is ignored.
        - ``AVErage`` selects the Average trace for the specified spectrum trace channel. If the
          specified spectrum trace channel does not have an Average trace, this command is ignored.
    """


class SvSItemChannelRfPhaseWrapState(SCPICmdWrite, SCPICmdRead):
    """The ``SV:S<x>_CH<x>:RF_PHASe:WRAP:STATE`` command.

    Description:
        - This command sets or queries whether Phase Wrap is applied to the Phase vs. Time trace for
          the specified channel. S<x> is the remote scope number and Ch<x> is the channel number to
          use as the Spectrum View source.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:RF_PHASe:WRAP:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:RF_PHASe:WRAP:STATE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SV:S<x>_CH<x>:RF_PHASe:WRAP:STATE value`` command.

    SCPI Syntax:
        ```
        - SV:S<x>_CH<x>:RF_PHASe:WRAP:STATE {ON|OFF}
        - SV:S<x>_CH<x>:RF_PHASe:WRAP:STATE?
        ```

    Info:
        - ``ON`` enables applying phase wrap on the specified Phase vs. Time channel trace.
        - ``OFF`` disables applying phase wrap on the specified Phase vs. Time channel trace.
    """


class SvSItemChannelRfPhaseWrapDegrees(SCPICmdWrite, SCPICmdRead):
    """The ``SV:S<x>_CH<x>:RF_PHASe:WRAP:DEGrees`` command.

    Description:
        - This command sets or queries the Phase Wrap limit for the Phase vs. Time trace for the
          specified channel. S<x> is the remote scope number and Ch<x> is the channel number to use
          as the Spectrum View source.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:RF_PHASe:WRAP:DEGrees?``
          query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:RF_PHASe:WRAP:DEGrees?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SV:S<x>_CH<x>:RF_PHASe:WRAP:DEGrees value`` command.

    SCPI Syntax:
        ```
        - SV:S<x>_CH<x>:RF_PHASe:WRAP:DEGrees <NR3>
        - SV:S<x>_CH<x>:RF_PHASe:WRAP:DEGrees?
        ```

    Info:
        - ``CH<x>`` is the channel number of the Phase vs. Time trace.
        - ``NR3`` sets the number of wrap degrees, from 180 degrees to infinity. When Phase Wrap is
          enabled, the phase values in the Phase vs Time waveform are constrained to be within ± the
          specified limit. Phase values below or above the limit are wrapped by repeatedly adding or
          subtracting 360 degrees until they are within range.
    """


class SvSItemChannelRfPhaseWrap(SCPICmdRead):
    """The ``SV:S<x>_CH<x>:RF_PHASe:WRAP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:RF_PHASe:WRAP?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:RF_PHASe:WRAP?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` is the channel number of the Phase vs. Time trace.

    Properties:
        - ``.degrees``: The ``SV:S<x>_CH<x>:RF_PHASe:WRAP:DEGrees`` command.
        - ``.state``: The ``SV:S<x>_CH<x>:RF_PHASe:WRAP:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._degrees = SvSItemChannelRfPhaseWrapDegrees(device, f"{self._cmd_syntax}:DEGrees")
        self._state = SvSItemChannelRfPhaseWrapState(device, f"{self._cmd_syntax}:STATE")

    @property
    def degrees(self) -> SvSItemChannelRfPhaseWrapDegrees:
        """Return the ``SV:S<x>_CH<x>:RF_PHASe:WRAP:DEGrees`` command.

        Description:
            - This command sets or queries the Phase Wrap limit for the Phase vs. Time trace for the
              specified channel. S<x> is the remote scope number and Ch<x> is the channel number to
              use as the Spectrum View source.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:RF_PHASe:WRAP:DEGrees?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SV:S<x>_CH<x>:RF_PHASe:WRAP:DEGrees?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SV:S<x>_CH<x>:RF_PHASe:WRAP:DEGrees value`` command.

        SCPI Syntax:
            ```
            - SV:S<x>_CH<x>:RF_PHASe:WRAP:DEGrees <NR3>
            - SV:S<x>_CH<x>:RF_PHASe:WRAP:DEGrees?
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
    def state(self) -> SvSItemChannelRfPhaseWrapState:
        """Return the ``SV:S<x>_CH<x>:RF_PHASe:WRAP:STATE`` command.

        Description:
            - This command sets or queries whether Phase Wrap is applied to the Phase vs. Time trace
              for the specified channel. S<x> is the remote scope number and Ch<x> is the channel
              number to use as the Spectrum View source.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:RF_PHASe:WRAP:STATE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SV:S<x>_CH<x>:RF_PHASe:WRAP:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SV:S<x>_CH<x>:RF_PHASe:WRAP:STATE value`` command.

        SCPI Syntax:
            ```
            - SV:S<x>_CH<x>:RF_PHASe:WRAP:STATE {ON|OFF}
            - SV:S<x>_CH<x>:RF_PHASe:WRAP:STATE?
            ```

        Info:
            - ``ON`` enables applying phase wrap on the specified Phase vs. Time channel trace.
            - ``OFF`` disables applying phase wrap on the specified Phase vs. Time channel trace.
        """
        return self._state


class SvSItemChannelRfPhaseReferenceTime(SCPICmdWrite, SCPICmdRead):
    """The ``SV:S<x>_CH<x>:RF_PHASe:REFerence:TIMe`` command.

    Description:
        - This command sets or queries the channel Phase Reference time in seconds. S<x> is the
          remote scope number and Ch<x> is the channel number to use as the Spectrum View source.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:RF_PHASe:REFerence:TIMe?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SV:S<x>_CH<x>:RF_PHASe:REFerence:TIMe?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SV:S<x>_CH<x>:RF_PHASe:REFerence:TIMe value`` command.

    SCPI Syntax:
        ```
        - SV:S<x>_CH<x>:RF_PHASe:REFerence:TIMe <NR3>
        - SV:S<x>_CH<x>:RF_PHASe:REFerence:TIMe?
        ```

    Info:
        - ``NR3`` is the Phase Reference time, in seconds. This indicates the time at which the
          phase value set by ``SV:S<x>_CH<x>:RF_PHASe:REFerence:DEGrees`` is applied. If the phase
          position set by ``SV:S<x>_CH<x>:RF_PHASe:REFerence:POSition`` is TRIGger, then the phase
          time is fixed at 0 seconds and cannot be changed. If the phase position is CURSor, then
          the phase time may be set to any value, and is initialized to the position of Cursor A. If
          CH<x> is the master phase reference, then the time is used to calculate the phase values
          of all other channels.
    """


class SvSItemChannelRfPhaseReferencePosition(SCPICmdWrite, SCPICmdRead):
    """The ``SV:S<x>_CH<x>:RF_PHASe:REFerence:POSition`` command.

    Description:
        - This command sets or queries whether the channel Phase Reference is located at the Trigger
          position or at the Cursor A position. S<x> is the remote scope number and Ch<x> is the
          channel number to use as the Spectrum View source.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:RF_PHASe:REFerence:POSition?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SV:S<x>_CH<x>:RF_PHASe:REFerence:POSition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SV:S<x>_CH<x>:RF_PHASe:REFerence:POSition value`` command.

    SCPI Syntax:
        ```
        - SV:S<x>_CH<x>:RF_PHASe:REFerence:POSition {TRIGger|CURSor}
        - SV:S<x>_CH<x>:RF_PHASe:REFerence:POSition?
        ```

    Info:
        - ``TRIGger`` sets the Phase Reference location to the Trigger position.
        - ``CURSor`` sets the channel Phase Reference location to the phase time set by
          ``SV:S<x>_CH<x>:RF_PHASe:REFerence:TIMe``, which defaults to the Cursor A position.
    """


class SvSItemChannelRfPhaseReferenceDegrees(SCPICmdWrite, SCPICmdRead):
    """The ``SV:S<x>_CH<x>:RF_PHASe:REFerence:DEGrees`` command.

    Description:
        - This command sets or queries the channel Phase Reference value in degrees. S<x> is the
          remote scope number and Ch<x> is the channel number to use as the Spectrum View source.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:RF_PHASe:REFerence:DEGrees?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SV:S<x>_CH<x>:RF_PHASe:REFerence:DEGrees?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SV:S<x>_CH<x>:RF_PHASe:REFerence:DEGrees value`` command.

    SCPI Syntax:
        ```
        - SV:S<x>_CH<x>:RF_PHASe:REFerence:DEGrees <NR3>
        - SV:S<x>_CH<x>:RF_PHASe:REFerence:DEGrees?
        ```

    Info:
        - ``NR3`` is the Phase Reference value, in degrees. This indicates a fixed phase value at
          the phase time set by ``SV:S<x>_CH<x>:RF_PHASe:REFerence:TIMe``. If CH<x> is the master
          phase reference, then the value is used to calculate the phase values of all other
          channels.
    """


class SvSItemChannelRfPhaseReference(SCPICmdRead):
    """The ``SV:S<x>_CH<x>:RF_PHASe:REFerence`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:RF_PHASe:REFerence?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:RF_PHASe:REFerence?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.degrees``: The ``SV:S<x>_CH<x>:RF_PHASe:REFerence:DEGrees`` command.
        - ``.position``: The ``SV:S<x>_CH<x>:RF_PHASe:REFerence:POSition`` command.
        - ``.time``: The ``SV:S<x>_CH<x>:RF_PHASe:REFerence:TIMe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._degrees = SvSItemChannelRfPhaseReferenceDegrees(device, f"{self._cmd_syntax}:DEGrees")
        self._position = SvSItemChannelRfPhaseReferencePosition(
            device, f"{self._cmd_syntax}:POSition"
        )
        self._time = SvSItemChannelRfPhaseReferenceTime(device, f"{self._cmd_syntax}:TIMe")

    @property
    def degrees(self) -> SvSItemChannelRfPhaseReferenceDegrees:
        """Return the ``SV:S<x>_CH<x>:RF_PHASe:REFerence:DEGrees`` command.

        Description:
            - This command sets or queries the channel Phase Reference value in degrees. S<x> is the
              remote scope number and Ch<x> is the channel number to use as the Spectrum View
              source.

        Usage:
            - Using the ``.query()`` method will send the
              ``SV:S<x>_CH<x>:RF_PHASe:REFerence:DEGrees?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SV:S<x>_CH<x>:RF_PHASe:REFerence:DEGrees?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SV:S<x>_CH<x>:RF_PHASe:REFerence:DEGrees value`` command.

        SCPI Syntax:
            ```
            - SV:S<x>_CH<x>:RF_PHASe:REFerence:DEGrees <NR3>
            - SV:S<x>_CH<x>:RF_PHASe:REFerence:DEGrees?
            ```

        Info:
            - ``NR3`` is the Phase Reference value, in degrees. This indicates a fixed phase value
              at the phase time set by ``SV:S<x>_CH<x>:RF_PHASe:REFerence:TIMe``. If CH<x> is the
              master phase reference, then the value is used to calculate the phase values of all
              other channels.
        """
        return self._degrees

    @property
    def position(self) -> SvSItemChannelRfPhaseReferencePosition:
        """Return the ``SV:S<x>_CH<x>:RF_PHASe:REFerence:POSition`` command.

        Description:
            - This command sets or queries whether the channel Phase Reference is located at the
              Trigger position or at the Cursor A position. S<x> is the remote scope number and
              Ch<x> is the channel number to use as the Spectrum View source.

        Usage:
            - Using the ``.query()`` method will send the
              ``SV:S<x>_CH<x>:RF_PHASe:REFerence:POSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SV:S<x>_CH<x>:RF_PHASe:REFerence:POSition?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SV:S<x>_CH<x>:RF_PHASe:REFerence:POSition value`` command.

        SCPI Syntax:
            ```
            - SV:S<x>_CH<x>:RF_PHASe:REFerence:POSition {TRIGger|CURSor}
            - SV:S<x>_CH<x>:RF_PHASe:REFerence:POSition?
            ```

        Info:
            - ``TRIGger`` sets the Phase Reference location to the Trigger position.
            - ``CURSor`` sets the channel Phase Reference location to the phase time set by
              ``SV:S<x>_CH<x>:RF_PHASe:REFerence:TIMe``, which defaults to the Cursor A position.
        """
        return self._position

    @property
    def time(self) -> SvSItemChannelRfPhaseReferenceTime:
        """Return the ``SV:S<x>_CH<x>:RF_PHASe:REFerence:TIMe`` command.

        Description:
            - This command sets or queries the channel Phase Reference time in seconds. S<x> is the
              remote scope number and Ch<x> is the channel number to use as the Spectrum View
              source.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:RF_PHASe:REFerence:TIMe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SV:S<x>_CH<x>:RF_PHASe:REFerence:TIMe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SV:S<x>_CH<x>:RF_PHASe:REFerence:TIMe value`` command.

        SCPI Syntax:
            ```
            - SV:S<x>_CH<x>:RF_PHASe:REFerence:TIMe <NR3>
            - SV:S<x>_CH<x>:RF_PHASe:REFerence:TIMe?
            ```

        Info:
            - ``NR3`` is the Phase Reference time, in seconds. This indicates the time at which the
              phase value set by ``SV:S<x>_CH<x>:RF_PHASe:REFerence:DEGrees`` is applied. If the
              phase position set by ``SV:S<x>_CH<x>:RF_PHASe:REFerence:POSition`` is TRIGger, then
              the phase time is fixed at 0 seconds and cannot be changed. If the phase position is
              CURSor, then the phase time may be set to any value, and is initialized to the
              position of Cursor A. If CH<x> is the master phase reference, then the time is used to
              calculate the phase values of all other channels.
        """
        return self._time


class SvSItemChannelRfPhase(SCPICmdRead):
    """The ``SV:S<x>_CH<x>:RF_PHASe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:RF_PHASe?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:RF_PHASe?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.reference``: The ``SV:S<x>_CH<x>:RF_PHASe:REFerence`` command tree.
        - ``.wrap``: The ``SV:S<x>_CH<x>:RF_PHASe:WRAP`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._reference = SvSItemChannelRfPhaseReference(device, f"{self._cmd_syntax}:REFerence")
        self._wrap = SvSItemChannelRfPhaseWrap(device, f"{self._cmd_syntax}:WRAP")

    @property
    def reference(self) -> SvSItemChannelRfPhaseReference:
        """Return the ``SV:S<x>_CH<x>:RF_PHASe:REFerence`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:RF_PHASe:REFerence?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SV:S<x>_CH<x>:RF_PHASe:REFerence?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.degrees``: The ``SV:S<x>_CH<x>:RF_PHASe:REFerence:DEGrees`` command.
            - ``.position``: The ``SV:S<x>_CH<x>:RF_PHASe:REFerence:POSition`` command.
            - ``.time``: The ``SV:S<x>_CH<x>:RF_PHASe:REFerence:TIMe`` command.
        """
        return self._reference

    @property
    def wrap(self) -> SvSItemChannelRfPhaseWrap:
        """Return the ``SV:S<x>_CH<x>:RF_PHASe:WRAP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:RF_PHASe:WRAP?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:RF_PHASe:WRAP?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` is the channel number of the Phase vs. Time trace.

        Sub-properties:
            - ``.degrees``: The ``SV:S<x>_CH<x>:RF_PHASe:WRAP:DEGrees`` command.
            - ``.state``: The ``SV:S<x>_CH<x>:RF_PHASe:WRAP:STATE`` command.
        """
        return self._wrap


class SvSItemChannelRfMagnitudeFormat(SCPICmdWrite, SCPICmdRead):
    """The ``SV:S<x>_CH<x>:RF_MAGnitude:FORMat`` command.

    Description:
        - This command sets or queries the format of the Magnitude vs. Time trace for the specified
          channel. S<x> is the remote scope number and Ch<x> is the channel number to use as the
          Spectrum View source.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:RF_MAGnitude:FORMat?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:RF_MAGnitude:FORMat?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SV:S<x>_CH<x>:RF_MAGnitude:FORMat value`` command.

    SCPI Syntax:
        ```
        - SV:S<x>_CH<x>:RF_MAGnitude:FORMat {AMPLINear|POWLINear|POWLOG}
        - SV:S<x>_CH<x>:RF_MAGnitude:FORMat?
        ```

    Info:
        - ``AMPLINear`` (Amplitude (linear)) sets the magnitude in Volts with square root conversion
          of linear power values.
        - ``POWLINear`` (Power (linear) sets the magnitude in Watts with direct use of linear power
          values.
        - ``POWLOG`` (Power (log) sets the magnitude in dB using log conversion of linear power
          values.
    """


class SvSItemChannelRfMagnitude(SCPICmdRead):
    """The ``SV:S<x>_CH<x>:RF_MAGnitude`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:RF_MAGnitude?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:RF_MAGnitude?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.format``: The ``SV:S<x>_CH<x>:RF_MAGnitude:FORMat`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._format = SvSItemChannelRfMagnitudeFormat(device, f"{self._cmd_syntax}:FORMat")

    @property
    def format(self) -> SvSItemChannelRfMagnitudeFormat:
        """Return the ``SV:S<x>_CH<x>:RF_MAGnitude:FORMat`` command.

        Description:
            - This command sets or queries the format of the Magnitude vs. Time trace for the
              specified channel. S<x> is the remote scope number and Ch<x> is the channel number to
              use as the Spectrum View source.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:RF_MAGnitude:FORMat?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SV:S<x>_CH<x>:RF_MAGnitude:FORMat?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SV:S<x>_CH<x>:RF_MAGnitude:FORMat value`` command.

        SCPI Syntax:
            ```
            - SV:S<x>_CH<x>:RF_MAGnitude:FORMat {AMPLINear|POWLINear|POWLOG}
            - SV:S<x>_CH<x>:RF_MAGnitude:FORMat?
            ```

        Info:
            - ``AMPLINear`` (Amplitude (linear)) sets the magnitude in Volts with square root
              conversion of linear power values.
            - ``POWLINear`` (Power (linear) sets the magnitude in Watts with direct use of linear
              power values.
            - ``POWLOG`` (Power (log) sets the magnitude in dB using log conversion of linear power
              values.
        """
        return self._format


class SvSItemChannelRfAverageNumavg(SCPICmdWrite, SCPICmdRead):
    """The ``SV:S<x>_CH<x>:RF_AVErage:NUMAVg`` command.

    Description:
        - This command sets or queries the number of acquisitions to be used when creating the
          Average trace for the specified spectrum trace channel in the Spectrum View. The Average
          spectrum trace shows the average of values from multiple acquisitions at each trace point.
          S<x> is the remote scope number and Ch<x> is the channel number to use as the Spectrum
          View source.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:RF_AVErage:NUMAVg?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:RF_AVErage:NUMAVg?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:S<x>_CH<x>:RF_AVErage:NUMAVg value``
          command.

    SCPI Syntax:
        ```
        - SV:S<x>_CH<x>:RF_AVErage:NUMAVg <NR1>
        - SV:S<x>_CH<x>:RF_AVErage:NUMAVg?
        ```

    Info:
        - ``<NR1>`` specifies the number of acquisitions to average. The range is 2 - 512, in
          exponential increments.
    """


class SvSItemChannelRfAverage(SCPICmdRead):
    """The ``SV:S<x>_CH<x>:RF_AVErage`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:RF_AVErage?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:RF_AVErage?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.numavg``: The ``SV:S<x>_CH<x>:RF_AVErage:NUMAVg`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._numavg = SvSItemChannelRfAverageNumavg(device, f"{self._cmd_syntax}:NUMAVg")

    @property
    def numavg(self) -> SvSItemChannelRfAverageNumavg:
        """Return the ``SV:S<x>_CH<x>:RF_AVErage:NUMAVg`` command.

        Description:
            - This command sets or queries the number of acquisitions to be used when creating the
              Average trace for the specified spectrum trace channel in the Spectrum View. The
              Average spectrum trace shows the average of values from multiple acquisitions at each
              trace point. S<x> is the remote scope number and Ch<x> is the channel number to use as
              the Spectrum View source.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:RF_AVErage:NUMAVg?``
              query.
            - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:RF_AVErage:NUMAVg?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SV:S<x>_CH<x>:RF_AVErage:NUMAVg value`` command.

        SCPI Syntax:
            ```
            - SV:S<x>_CH<x>:RF_AVErage:NUMAVg <NR1>
            - SV:S<x>_CH<x>:RF_AVErage:NUMAVg?
            ```

        Info:
            - ``<NR1>`` specifies the number of acquisitions to average. The range is 2 - 512, in
              exponential increments.
        """
        return self._numavg


class SvSItemChannelRf(SCPICmdRead):
    """The ``SV:S<x>_CH<x>:RF`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:RF?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:RF?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.average``: The ``SV:S<x>_CH<x>:RF_AVErage`` command tree.
        - ``.magnitude``: The ``SV:S<x>_CH<x>:RF_MAGnitude`` command tree.
        - ``.phase``: The ``SV:S<x>_CH<x>:RF_PHASe`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._average = SvSItemChannelRfAverage(device, f"{self._cmd_syntax}_AVErage")
        self._magnitude = SvSItemChannelRfMagnitude(device, f"{self._cmd_syntax}_MAGnitude")
        self._phase = SvSItemChannelRfPhase(device, f"{self._cmd_syntax}_PHASe")

    @property
    def average(self) -> SvSItemChannelRfAverage:
        """Return the ``SV:S<x>_CH<x>:RF_AVErage`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:RF_AVErage?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:RF_AVErage?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.numavg``: The ``SV:S<x>_CH<x>:RF_AVErage:NUMAVg`` command.
        """
        return self._average

    @property
    def magnitude(self) -> SvSItemChannelRfMagnitude:
        """Return the ``SV:S<x>_CH<x>:RF_MAGnitude`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:RF_MAGnitude?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:RF_MAGnitude?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.format``: The ``SV:S<x>_CH<x>:RF_MAGnitude:FORMat`` command.
        """
        return self._magnitude

    @property
    def phase(self) -> SvSItemChannelRfPhase:
        """Return the ``SV:S<x>_CH<x>:RF_PHASe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:RF_PHASe?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:RF_PHASe?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.reference``: The ``SV:S<x>_CH<x>:RF_PHASe:REFerence`` command tree.
            - ``.wrap``: The ``SV:S<x>_CH<x>:RF_PHASe:WRAP`` command tree.
        """
        return self._phase


class SvSItemChannel(ValidatedChannel, SCPICmdRead):
    """The ``SV:S<x>_CH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.rf``: The ``SV:S<x>_CH<x>:RF`` command tree.
        - ``.seltrace``: The ``SV:S<x>_CH<x>:SELTrace`` command.
        - ``.select``: The ``SV:S<x>_CH<x>:SELect`` command tree.
        - ``.squelch``: The ``SV:S<x>_CH<x>:SQUELCH`` command tree.
        - ``.units``: The ``SV:S<x>_CH<x>:UNIts`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._rf = SvSItemChannelRf(device, f"{self._cmd_syntax}:RF")
        self._seltrace = SvSItemChannelSeltrace(device, f"{self._cmd_syntax}:SELTrace")
        self._select = SvSItemChannelSelect(device, f"{self._cmd_syntax}:SELect")
        self._squelch = SvSItemChannelSquelch(device, f"{self._cmd_syntax}:SQUELCH")
        self._units = SvSItemChannelUnits(device, f"{self._cmd_syntax}:UNIts")

    @property
    def rf(self) -> SvSItemChannelRf:
        """Return the ``SV:S<x>_CH<x>:RF`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:RF?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:RF?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.average``: The ``SV:S<x>_CH<x>:RF_AVErage`` command tree.
            - ``.magnitude``: The ``SV:S<x>_CH<x>:RF_MAGnitude`` command tree.
            - ``.phase``: The ``SV:S<x>_CH<x>:RF_PHASe`` command tree.
        """
        return self._rf

    @property
    def seltrace(self) -> SvSItemChannelSeltrace:
        """Return the ``SV:S<x>_CH<x>:SELTrace`` command.

        Description:
            - This command sets or queries the spectrum trace type to show for the specified channel
              in the Spectrum View. Each channel's spectrum trace can display up to four traces; a
              Normal trace (default), a Max Hold trace, a Min Hold trace and an Average trace. S<x>
              is the remote scope number and Ch<x> is the channel number to use as the Spectrum View
              source.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SELTrace?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:SELTrace?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:S<x>_CH<x>:SELTrace value``
              command.

        SCPI Syntax:
            ```
            - SV:S<x>_CH<x>:SELTrace {NORMal|MAXHold|MINHold|AVErage}
            - SV:S<x>_CH<x>:SELTrace?
            ```

        Info:
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
    def select(self) -> SvSItemChannelSelect:
        """Return the ``SV:S<x>_CH<x>:SELect`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SELect?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:SELect?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.rf``: The ``SV:S<x>_CH<x>:SELect:RF`` command tree.
            - ``.spectrogram``: The ``SV:S<x>_CH<x>:SELect:SPECtrogram`` command.
        """
        return self._select

    @property
    def squelch(self) -> SvSItemChannelSquelch:
        """Return the ``SV:S<x>_CH<x>:SQUELCH`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:SQUELCH?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:SQUELCH?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``SV:S<x>_CH<x>:SQUELCH:STATE`` command.
            - ``.threshold``: The ``SV:S<x>_CH<x>:SQUELCH:THReshold`` command.
        """
        return self._squelch

    @property
    def units(self) -> SvSItemChannelUnits:
        """Return the ``SV:S<x>_CH<x>:UNIts`` command.

        Description:
            - This command sets or queries the absolute logarithmic amplitude vertical scale units
              to show in the specified spectrum trace remote scope channel of the Spectrum View.
              S<x> is the remote scope number and Ch<x> is the channel number to use as the Spectrum
              View source.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>:UNIts?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:S<x>_CH<x>:UNIts value``
              command.

        SCPI Syntax:
            ```
            - SV:S<x>_CH<x>:UNIts {DBM|DBUW|DBMV|DBUV|DBMA|DBUA}
            - SV:S<x>_CH<x>:UNIts?
            ```

        Info:
            - ``DBM`` specifies Decibel milliwatts (dBm).
            - ``DBUW`` specifies Decibel microwatts (dBµW).
            - ``DBMV`` specifies Decibel millivolts (dBmV).
            - ``DBUV`` specifies Decibel microvolts (dBµV).
            - ``DBMA`` specifies Decibel milliamperes (dBmA).
            - ``DBUA`` specifies Decibel microamperes (dBµA).
        """
        return self._units


class SvSItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``SV:S<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:S<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:S<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``SV:S<x>_CH<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, SvSItemChannel] = DefaultDictPassKeyToFactory(
            lambda x: SvSItemChannel(device, f"{self._cmd_syntax}_CH{x}")
        )

    @property
    def ch(self) -> Dict[int, SvSItemChannel]:
        """Return the ``SV:S<x>_CH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>_CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:S<x>_CH<x>?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.rf``: The ``SV:S<x>_CH<x>:RF`` command tree.
            - ``.seltrace``: The ``SV:S<x>_CH<x>:SELTrace`` command.
            - ``.select``: The ``SV:S<x>_CH<x>:SELect`` command tree.
            - ``.squelch``: The ``SV:S<x>_CH<x>:SQUELCH`` command tree.
            - ``.units``: The ``SV:S<x>_CH<x>:UNIts`` command.
        """
        return self._ch


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
        - SV:MARKER:PEAK:STATE {CH<x>}
        - SV:MARKER:PEAK:STATE?
        ```

    Info:
        - ``ON, 1`` enables showing peak marker icons on spectrum trace waveforms.
        - ``OFF, 0`` disables showing peak marker icons on spectrum trace waveforms.
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
            - SV:MARKER:PEAK:STATE {CH<x>}
            - SV:MARKER:PEAK:STATE?
            ```

        Info:
            - ``ON, 1`` enables showing peak marker icons on spectrum trace waveforms.
            - ``OFF, 0`` disables showing peak marker icons on spectrum trace waveforms.
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
        - SV:LOCKSpectrum {ON|OFF|1|0}
        - SV:LOCKSpectrum?
        ```

    Info:
        - ``ON, 1`` sets all spectrum traces channels in the Spectrum View window to use the same
          Spectrum Time value. When the Spectrum Time of any channel is changed, the Spectrum Time
          of all other channels is automatically changed to match that value.
        - ``OFF, 0`` enables use of different Spectrum Time values for each spectrum trace channel.
          The Spectrum Time of all channels are independent.
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
        - SV:LOCKCenter {ON|OFF|1|0}
        - SV:LOCKCenter?
        ```

    Info:
        - ``ON, 1`` sets all spectrum traces channels in the Spectrum View window to use the same
          center frequency value. When the center frequency of any channel is changed, the center
          frequency of all other channels is automatically changed to match that value.
        - ``OFF, 0`` enables use of different center frequency values for each spectrum trace
          channel. The center frequencies of all channels are independent.
    """


class SvChannelSelectSpectrogram(SCPICmdWrite, SCPICmdRead):
    """The ``SV:CH<x>:SELect:SPECtrogram`` command.

    Description:
        - This command sets or queries whether the spectrogram plot for the specified channel is
          displayed in the Spectrum View.

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
        - ``CH<x>`` specifies the channel number.
        - ``ON`` turns on spectrogram.
        - ``OFF`` turns off spectrogram.
    """


class SvChannelSelect(SCPICmdRead):
    """The ``SV:CH<x>:SELect`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>:SELect?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SELect?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` specifies the channel number.

    Properties:
        - ``.spectrogram``: The ``SV:CH<x>:SELect:SPECtrogram`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._spectrogram = SvChannelSelectSpectrogram(device, f"{self._cmd_syntax}:SPECtrogram")

    @property
    def spectrogram(self) -> SvChannelSelectSpectrogram:
        """Return the ``SV:CH<x>:SELect:SPECtrogram`` command.

        Description:
            - This command sets or queries whether the spectrogram plot for the specified channel is
              displayed in the Spectrum View.

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
            - ``CH<x>`` specifies the channel number.
            - ``ON`` turns on spectrogram.
            - ``OFF`` turns off spectrogram.
        """
        return self._spectrogram


class SvChannel(ValidatedChannel, SCPICmdRead):
    """The ``SV:CH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:CH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` specifies the channel number.

    Properties:
        - ``.select``: The ``SV:CH<x>:SELect`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._select = SvChannelSelect(device, f"{self._cmd_syntax}:SELect")

    @property
    def select(self) -> SvChannelSelect:
        """Return the ``SV:CH<x>:SELect`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>:SELect?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:CH<x>:SELect?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` specifies the channel number.

        Sub-properties:
            - ``.spectrogram``: The ``SV:CH<x>:SELect:SPECtrogram`` command.
        """
        return self._select


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
        - ``.rf_phase``: The ``SV:RF_PHASe`` command tree.
        - ``.s``: The ``SV:S<x>`` command tree.
        - ``.spectrogram``: The ``SV:SPECtrogram`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SV") -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, SvChannel] = DefaultDictPassKeyToFactory(
            lambda x: SvChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._lockcenter = SvLockcenter(device, f"{self._cmd_syntax}:LOCKCenter")
        self._lockspectrum = SvLockspectrum(device, f"{self._cmd_syntax}:LOCKSpectrum")
        self._marker = SvMarker(device, f"{self._cmd_syntax}:MARKER")
        self._rf_phase = SvRfPhase(device, f"{self._cmd_syntax}:RF_PHASe")
        self._s: Dict[int, SvSItem] = DefaultDictPassKeyToFactory(
            lambda x: SvSItem(device, f"{self._cmd_syntax}:S{x}")
        )
        self._spectrogram = SvSpectrogram(device, f"{self._cmd_syntax}:SPECtrogram")

    @property
    def ch(self) -> Dict[int, SvChannel]:
        """Return the ``SV:CH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:CH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` specifies the channel number.

        Sub-properties:
            - ``.select``: The ``SV:CH<x>:SELect`` command tree.
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
            - SV:LOCKCenter {ON|OFF|1|0}
            - SV:LOCKCenter?
            ```

        Info:
            - ``ON, 1`` sets all spectrum traces channels in the Spectrum View window to use the
              same center frequency value. When the center frequency of any channel is changed, the
              center frequency of all other channels is automatically changed to match that value.
            - ``OFF, 0`` enables use of different center frequency values for each spectrum trace
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
            - SV:LOCKSpectrum {ON|OFF|1|0}
            - SV:LOCKSpectrum?
            ```

        Info:
            - ``ON, 1`` sets all spectrum traces channels in the Spectrum View window to use the
              same Spectrum Time value. When the Spectrum Time of any channel is changed, the
              Spectrum Time of all other channels is automatically changed to match that value.
            - ``OFF, 0`` enables use of different Spectrum Time values for each spectrum trace
              channel. The Spectrum Time of all channels are independent.
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
    def s(self) -> Dict[int, SvSItem]:
        """Return the ``SV:S<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SV:S<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:S<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``SV:S<x>_CH<x>`` command tree.
        """
        return self._s

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
