"""The awgcontrol commands module.

These commands are used in the following models:
AWG70KA, AWG70KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - AWGControl:ARSettings {0|1|ON|OFF}
    - AWGControl:ARSettings?
    - AWGControl:CLOCk:DRATe <NR1>
    - AWGControl:CLOCk:DRATe?
    - AWGControl:CLOCk:PHASe:ADJust <NR1>
    - AWGControl:CLOCk:PHASe:ADJust?
    - AWGControl:CLOCk:SOURce {INTernal|EXTernal|EFIXed|EVARiable}
    - AWGControl:CLOCk:SOURce?
    - AWGControl:COMPile <filename>
    - AWGControl:CONFigure:CNUMber?
    - AWGControl:DLOading:ENABle {OFF|ON|0|1}
    - AWGControl:DLOading:ENABle?
    - AWGControl:DOUTput[n]:STATe {OFF|ON|0|1}
    - AWGControl:DOUTput[n]:STATe?
    - AWGControl:INTerleave:ADJustment:AMPLitude <NRf>
    - AWGControl:INTerleave:ADJustment:AMPLitude?
    - AWGControl:INTerleave:ADJustment:PHASe <NRf>
    - AWGControl:INTerleave:ADJustment:PHASe?
    - AWGControl:LSTate?
    - AWGControl:PJUMp:JSTRobe {0|1|OFF|ON}
    - AWGControl:PJUMp:JSTRobe?
    - AWGControl:PJUMp:SEDGe {FALLing|RISing}
    - AWGControl:PJUMp:SEDGe?
    - AWGControl:RMODe {CONTinuous|TRIGgered}
    - AWGControl:RMODe?
    - AWGControl:RSTate?
    - AWGControl:RUN:IMMediate
    - AWGControl:SNAMe?
    - AWGControl:SREStore <filepath>[,<msus>]
    - AWGControl:SSAVe <filepath>[,<msus>]
    - AWGControl:STOP:IMMediate
    - AWGControl:STReaming:ENABle {OFF|ON|0|1}
    - AWGControl:STReaming:ENABle?
    - AWGControl:STReaming:JEVent {ATRigger|BTRigger|T1}
    - AWGControl:STReaming:JEVent?
    - AWGControl:TIMer:INTerval:HZ <period>
    - AWGControl:TIMer:INTerval:HZ?
    - AWGControl:TIMer:INTerval:SEConds <period>
    - AWGControl:TIMer:INTerval:SEConds?
    - AWGControl:TIMer:RSTate?
    - AWGControl:TIMer:RUN
    - AWGControl:TIMer:SOPLay {OFF|ON|0|1}
    - AWGControl:TIMer:SOPLay?
    - AWGControl:TIMer:STOP
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    SCPICmdWriteNoArguments,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class AwgcontrolTimerStop(SCPICmdWriteNoArguments):
    """The ``AWGControl:TIMer:STOP`` command.

    Description:
        - This command stops the internal timer immediately.

    Usage:
        - Using the ``.write()`` method will send the ``AWGControl:TIMer:STOP`` command.

    SCPI Syntax:
        ```
        - AWGControl:TIMer:STOP
        ```
    """


class AwgcontrolTimerSoplay(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:TIMer:SOPLay`` command.

    Description:
        - This command sets or returns the state (enabled or disabled) of the timer to start and
          stop when waveform playout starts and stops.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:TIMer:SOPLay?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:TIMer:SOPLay?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AWGControl:TIMer:SOPLay value``
          command.

    SCPI Syntax:
        ```
        - AWGControl:TIMer:SOPLay {OFF|ON|0|1}
        - AWGControl:TIMer:SOPLay?
        ```
    """


class AwgcontrolTimerRun(SCPICmdWriteNoArguments):
    """The ``AWGControl:TIMer:RUN`` command.

    Description:
        - This command starts the internal timer immediately.

    Usage:
        - Using the ``.write()`` method will send the ``AWGControl:TIMer:RUN`` command.

    SCPI Syntax:
        ```
        - AWGControl:TIMer:RUN
        ```
    """


class AwgcontrolTimerRstate(SCPICmdRead):
    """The ``AWGControl:TIMer:RSTate`` command.

    Description:
        - This command returns the state of the internal timer (running or stopped). The timer can
          be stopped and started manually or automatically when the waveform playout starts and
          stops.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:TIMer:RSTate?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:TIMer:RSTate?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - AWGControl:TIMer:RSTate?
        ```
    """


class AwgcontrolTimerIntervalSeconds(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:TIMer:INTerval:SEConds`` command.

    Description:
        - This command sets or returns the internal timer interval period in seconds. The timer
          stops running on any change to the interval period or the instrument sample rate.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:TIMer:INTerval:SEConds?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:TIMer:INTerval:SEConds?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``AWGControl:TIMer:INTerval:SEConds value`` command.

    SCPI Syntax:
        ```
        - AWGControl:TIMer:INTerval:SEConds <period>
        - AWGControl:TIMer:INTerval:SEConds?
        ```
    """


class AwgcontrolTimerIntervalHz(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:TIMer:INTerval:HZ`` command.

    Description:
        - This command sets or returns the internal timer interval period in Hertz. The timer stops
          running on any change to the interval period or the instrument sample rate.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:TIMer:INTerval:HZ?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:TIMer:INTerval:HZ?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AWGControl:TIMer:INTerval:HZ value``
          command.

    SCPI Syntax:
        ```
        - AWGControl:TIMer:INTerval:HZ <period>
        - AWGControl:TIMer:INTerval:HZ?
        ```
    """


class AwgcontrolTimerInterval(SCPICmdRead):
    """The ``AWGControl:TIMer:INTerval`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:TIMer:INTerval?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:TIMer:INTerval?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.hz``: The ``AWGControl:TIMer:INTerval:HZ`` command.
        - ``.seconds``: The ``AWGControl:TIMer:INTerval:SEConds`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hz = AwgcontrolTimerIntervalHz(device, f"{self._cmd_syntax}:HZ")
        self._seconds = AwgcontrolTimerIntervalSeconds(device, f"{self._cmd_syntax}:SEConds")

    @property
    def hz(self) -> AwgcontrolTimerIntervalHz:
        """Return the ``AWGControl:TIMer:INTerval:HZ`` command.

        Description:
            - This command sets or returns the internal timer interval period in Hertz. The timer
              stops running on any change to the interval period or the instrument sample rate.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:TIMer:INTerval:HZ?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:TIMer:INTerval:HZ?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``AWGControl:TIMer:INTerval:HZ value`` command.

        SCPI Syntax:
            ```
            - AWGControl:TIMer:INTerval:HZ <period>
            - AWGControl:TIMer:INTerval:HZ?
            ```
        """
        return self._hz

    @property
    def seconds(self) -> AwgcontrolTimerIntervalSeconds:
        """Return the ``AWGControl:TIMer:INTerval:SEConds`` command.

        Description:
            - This command sets or returns the internal timer interval period in seconds. The timer
              stops running on any change to the interval period or the instrument sample rate.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:TIMer:INTerval:SEConds?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``AWGControl:TIMer:INTerval:SEConds?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``AWGControl:TIMer:INTerval:SEConds value`` command.

        SCPI Syntax:
            ```
            - AWGControl:TIMer:INTerval:SEConds <period>
            - AWGControl:TIMer:INTerval:SEConds?
            ```
        """
        return self._seconds


class AwgcontrolTimer(SCPICmdRead):
    """The ``AWGControl:TIMer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:TIMer?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:TIMer?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.interval``: The ``AWGControl:TIMer:INTerval`` command tree.
        - ``.rstate``: The ``AWGControl:TIMer:RSTate`` command.
        - ``.run``: The ``AWGControl:TIMer:RUN`` command.
        - ``.soplay``: The ``AWGControl:TIMer:SOPLay`` command.
        - ``.stop``: The ``AWGControl:TIMer:STOP`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._interval = AwgcontrolTimerInterval(device, f"{self._cmd_syntax}:INTerval")
        self._rstate = AwgcontrolTimerRstate(device, f"{self._cmd_syntax}:RSTate")
        self._run = AwgcontrolTimerRun(device, f"{self._cmd_syntax}:RUN")
        self._soplay = AwgcontrolTimerSoplay(device, f"{self._cmd_syntax}:SOPLay")
        self._stop = AwgcontrolTimerStop(device, f"{self._cmd_syntax}:STOP")

    @property
    def interval(self) -> AwgcontrolTimerInterval:
        """Return the ``AWGControl:TIMer:INTerval`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:TIMer:INTerval?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:TIMer:INTerval?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.hz``: The ``AWGControl:TIMer:INTerval:HZ`` command.
            - ``.seconds``: The ``AWGControl:TIMer:INTerval:SEConds`` command.
        """
        return self._interval

    @property
    def rstate(self) -> AwgcontrolTimerRstate:
        """Return the ``AWGControl:TIMer:RSTate`` command.

        Description:
            - This command returns the state of the internal timer (running or stopped). The timer
              can be stopped and started manually or automatically when the waveform playout starts
              and stops.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:TIMer:RSTate?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:TIMer:RSTate?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - AWGControl:TIMer:RSTate?
            ```
        """
        return self._rstate

    @property
    def run(self) -> AwgcontrolTimerRun:
        """Return the ``AWGControl:TIMer:RUN`` command.

        Description:
            - This command starts the internal timer immediately.

        Usage:
            - Using the ``.write()`` method will send the ``AWGControl:TIMer:RUN`` command.

        SCPI Syntax:
            ```
            - AWGControl:TIMer:RUN
            ```
        """
        return self._run

    @property
    def soplay(self) -> AwgcontrolTimerSoplay:
        """Return the ``AWGControl:TIMer:SOPLay`` command.

        Description:
            - This command sets or returns the state (enabled or disabled) of the timer to start and
              stop when waveform playout starts and stops.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:TIMer:SOPLay?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:TIMer:SOPLay?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AWGControl:TIMer:SOPLay value``
              command.

        SCPI Syntax:
            ```
            - AWGControl:TIMer:SOPLay {OFF|ON|0|1}
            - AWGControl:TIMer:SOPLay?
            ```
        """
        return self._soplay

    @property
    def stop(self) -> AwgcontrolTimerStop:
        """Return the ``AWGControl:TIMer:STOP`` command.

        Description:
            - This command stops the internal timer immediately.

        Usage:
            - Using the ``.write()`` method will send the ``AWGControl:TIMer:STOP`` command.

        SCPI Syntax:
            ```
            - AWGControl:TIMer:STOP
            ```
        """
        return self._stop


class AwgcontrolStreamingJevent(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:STReaming:JEVent`` command.

    Description:
        - This command sets or returns the jump event for Streaming ID.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:STReaming:JEVent?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:STReaming:JEVent?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AWGControl:STReaming:JEVent value``
          command.

    SCPI Syntax:
        ```
        - AWGControl:STReaming:JEVent {ATRigger|BTRigger|T1}
        - AWGControl:STReaming:JEVent?
        ```
    """


class AwgcontrolStreamingEnable(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:STReaming:ENABle`` command.

    Description:
        - This command sets or returns the state (enabled or disabled) of Streaming ID .

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:STReaming:ENABle?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:STReaming:ENABle?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AWGControl:STReaming:ENABle value``
          command.

    SCPI Syntax:
        ```
        - AWGControl:STReaming:ENABle {OFF|ON|0|1}
        - AWGControl:STReaming:ENABle?
        ```
    """


class AwgcontrolStreaming(SCPICmdRead):
    """The ``AWGControl:STReaming`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:STReaming?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:STReaming?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.enable``: The ``AWGControl:STReaming:ENABle`` command.
        - ``.jevent``: The ``AWGControl:STReaming:JEVent`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._enable = AwgcontrolStreamingEnable(device, f"{self._cmd_syntax}:ENABle")
        self._jevent = AwgcontrolStreamingJevent(device, f"{self._cmd_syntax}:JEVent")

    @property
    def enable(self) -> AwgcontrolStreamingEnable:
        """Return the ``AWGControl:STReaming:ENABle`` command.

        Description:
            - This command sets or returns the state (enabled or disabled) of Streaming ID .

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:STReaming:ENABle?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:STReaming:ENABle?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AWGControl:STReaming:ENABle value``
              command.

        SCPI Syntax:
            ```
            - AWGControl:STReaming:ENABle {OFF|ON|0|1}
            - AWGControl:STReaming:ENABle?
            ```
        """
        return self._enable

    @property
    def jevent(self) -> AwgcontrolStreamingJevent:
        """Return the ``AWGControl:STReaming:JEVent`` command.

        Description:
            - This command sets or returns the jump event for Streaming ID.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:STReaming:JEVent?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:STReaming:JEVent?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AWGControl:STReaming:JEVent value``
              command.

        SCPI Syntax:
            ```
            - AWGControl:STReaming:JEVent {ATRigger|BTRigger|T1}
            - AWGControl:STReaming:JEVent?
            ```
        """
        return self._jevent


class AwgcontrolStopImmediate(SCPICmdWriteNoArguments):
    """The ``AWGControl:STOP:IMMediate`` command.

    Description:
        - This command stops the output of a waveform or a sequence.

    Usage:
        - Using the ``.write()`` method will send the ``AWGControl:STOP:IMMediate`` command.

    SCPI Syntax:
        ```
        - AWGControl:STOP:IMMediate
        ```
    """


class AwgcontrolStop(SCPICmdRead):
    """The ``AWGControl:STOP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:STOP?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:STOP?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.immediate``: The ``AWGControl:STOP:IMMediate`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._immediate = AwgcontrolStopImmediate(device, f"{self._cmd_syntax}:IMMediate")

    @property
    def immediate(self) -> AwgcontrolStopImmediate:
        """Return the ``AWGControl:STOP:IMMediate`` command.

        Description:
            - This command stops the output of a waveform or a sequence.

        Usage:
            - Using the ``.write()`` method will send the ``AWGControl:STOP:IMMediate`` command.

        SCPI Syntax:
            ```
            - AWGControl:STOP:IMMediate
            ```
        """
        return self._immediate


class AwgcontrolSsave(SCPICmdWrite):
    """The ``AWGControl:SSAVe`` command.

    Description:
        - This command saves the AWG's setup with waveforms.

    Usage:
        - Using the ``.write(value)`` method will send the ``AWGControl:SSAVe value`` command.

    SCPI Syntax:
        ```
        - AWGControl:SSAVe <filepath>[,<msus>]
        ```
    """


class AwgcontrolSrestore(SCPICmdWrite):
    """The ``AWGControl:SREStore`` command.

    Description:
        - This command opens a setup file into the AWG's setup memory.

    Usage:
        - Using the ``.write(value)`` method will send the ``AWGControl:SREStore value`` command.

    SCPI Syntax:
        ```
        - AWGControl:SREStore <filepath>[,<msus>]
        ```
    """


class AwgcontrolSname(SCPICmdRead):
    """The ``AWGControl:SNAMe`` command.

    Description:
        - This command returns the AWG's most recently saved setup location. The response contains
          the full path for the file, including the disk drive letter (msus or, mass storage unit
          specifier).

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:SNAMe?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:SNAMe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - AWGControl:SNAMe?
        ```
    """


class AwgcontrolRunImmediate(SCPICmdWriteNoArguments):
    """The ``AWGControl:RUN:IMMediate`` command.

    Description:
        - This command initiates the output of a waveform or sequence. This is equivalent to pushing
          the play button on the front-panel or display. The AWG can be put in the run state only
          when waveforms or sequences are assigned to channels.

    Usage:
        - Using the ``.write()`` method will send the ``AWGControl:RUN:IMMediate`` command.

    SCPI Syntax:
        ```
        - AWGControl:RUN:IMMediate
        ```
    """


class AwgcontrolRun(SCPICmdRead):
    """The ``AWGControl:RUN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:RUN?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:RUN?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.immediate``: The ``AWGControl:RUN:IMMediate`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._immediate = AwgcontrolRunImmediate(device, f"{self._cmd_syntax}:IMMediate")

    @property
    def immediate(self) -> AwgcontrolRunImmediate:
        """Return the ``AWGControl:RUN:IMMediate`` command.

        Description:
            - This command initiates the output of a waveform or sequence. This is equivalent to
              pushing the play button on the front-panel or display. The AWG can be put in the run
              state only when waveforms or sequences are assigned to channels.

        Usage:
            - Using the ``.write()`` method will send the ``AWGControl:RUN:IMMediate`` command.

        SCPI Syntax:
            ```
            - AWGControl:RUN:IMMediate
            ```
        """
        return self._immediate


class AwgcontrolRstate(SCPICmdRead):
    """The ``AWGControl:RSTate`` command.

    Description:
        - This command returns the run state of the AWG.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:RSTate?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:RSTate?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - AWGControl:RSTate?
        ```
    """


class AwgcontrolRmode(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:RMODe`` command.

    Description:
        - This command sets or returns the run mode of the AWG for Channel 1.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:RMODe?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:RMODe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AWGControl:RMODe value`` command.

    SCPI Syntax:
        ```
        - AWGControl:RMODe {CONTinuous|TRIGgered}
        - AWGControl:RMODe?
        ```

    Info:
        - ``CONTinuous`` sets the Run Mode to Continuous (not waiting for a trigger event).
        - ``TRIGgered`` sets the Run Mode to Triggered, waiting for a trigger event. One waveform
          play out cycle completes, then play out stops, waiting for the next trigger event.
        - ``*RST`` sets this to CONT.
    """


class AwgcontrolPjumpSedge(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:PJUMp:SEDGe`` command.

    Description:
        - This command sets or returns the active Strobe Edge to use for Pattern Jump when Pattern
          Jump is enabled for Sequencing.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:PJUMp:SEDGe?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:PJUMp:SEDGe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AWGControl:PJUMp:SEDGe value`` command.

    SCPI Syntax:
        ```
        - AWGControl:PJUMp:SEDGe {FALLing|RISing}
        - AWGControl:PJUMp:SEDGe?
        ```

    Info:
        - ``FALLing`` sets the falling edge of the strobe signal to the active edge. 256 input
          patterns are available.
        - ``RISing`` sets the rising edge of the strobe signal to the active edge. 256 input
          patterns are available.
    """


class AwgcontrolPjumpJstrobe(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:PJUMp:JSTRobe`` command.

    Description:
        - This command sets or returns if the pattern jump is set (enabled or disabled) to always
          occur on the strobe signal. With this setting disabled, the pattern jump requires a strobe
          signal and a pattern address change to initiate a jump. With this setting enabled, the
          pattern jump disregards the pattern address change condition, causing the jump to always
          occur on the strobe signal.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:PJUMp:JSTRobe?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:PJUMp:JSTRobe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AWGControl:PJUMp:JSTRobe value``
          command.

    SCPI Syntax:
        ```
        - AWGControl:PJUMp:JSTRobe {0|1|OFF|ON}
        - AWGControl:PJUMp:JSTRobe?
        ```
    """


class AwgcontrolPjump(SCPICmdRead):
    """The ``AWGControl:PJUMp`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:PJUMp?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:PJUMp?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.jstrobe``: The ``AWGControl:PJUMp:JSTRobe`` command.
        - ``.sedge``: The ``AWGControl:PJUMp:SEDGe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._jstrobe = AwgcontrolPjumpJstrobe(device, f"{self._cmd_syntax}:JSTRobe")
        self._sedge = AwgcontrolPjumpSedge(device, f"{self._cmd_syntax}:SEDGe")

    @property
    def jstrobe(self) -> AwgcontrolPjumpJstrobe:
        """Return the ``AWGControl:PJUMp:JSTRobe`` command.

        Description:
            - This command sets or returns if the pattern jump is set (enabled or disabled) to
              always occur on the strobe signal. With this setting disabled, the pattern jump
              requires a strobe signal and a pattern address change to initiate a jump. With this
              setting enabled, the pattern jump disregards the pattern address change condition,
              causing the jump to always occur on the strobe signal.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:PJUMp:JSTRobe?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:PJUMp:JSTRobe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AWGControl:PJUMp:JSTRobe value``
              command.

        SCPI Syntax:
            ```
            - AWGControl:PJUMp:JSTRobe {0|1|OFF|ON}
            - AWGControl:PJUMp:JSTRobe?
            ```
        """
        return self._jstrobe

    @property
    def sedge(self) -> AwgcontrolPjumpSedge:
        """Return the ``AWGControl:PJUMp:SEDGe`` command.

        Description:
            - This command sets or returns the active Strobe Edge to use for Pattern Jump when
              Pattern Jump is enabled for Sequencing.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:PJUMp:SEDGe?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:PJUMp:SEDGe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AWGControl:PJUMp:SEDGe value``
              command.

        SCPI Syntax:
            ```
            - AWGControl:PJUMp:SEDGe {FALLing|RISing}
            - AWGControl:PJUMp:SEDGe?
            ```

        Info:
            - ``FALLing`` sets the falling edge of the strobe signal to the active edge. 256 input
              patterns are available.
            - ``RISing`` sets the rising edge of the strobe signal to the active edge. 256 input
              patterns are available.
        """
        return self._sedge


class AwgcontrolLstate(SCPICmdRead):
    """The ``AWGControl:LSTate`` command.

    Description:
        - This command returns the waveform loading state of the arbitrary waveform generator when
          Dynamic Loading is enabled.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:LSTate?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:LSTate?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - AWGControl:LSTate?
        ```
    """


class AwgcontrolInterleaveAdjustmentPhase(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:INTerleave:ADJustment:PHASe`` command.

    Description:
        - This command sets or returns the interleave adjustment phase. The phase adjustment is
          applied to both of the channel's interleave DACs.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:INTerleave:ADJustment:PHASe?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``AWGControl:INTerleave:ADJustment:PHASe?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``AWGControl:INTerleave:ADJustment:PHASe value`` command.

    SCPI Syntax:
        ```
        - AWGControl:INTerleave:ADJustment:PHASe <NRf>
        - AWGControl:INTerleave:ADJustment:PHASe?
        ```

    Info:
        - ``*RST`` sets this to 0 degrees.
    """


class AwgcontrolInterleaveAdjustmentAmplitude(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:INTerleave:ADJustment:AMPLitude`` command.

    Description:
        - This command sets or returns the interleave amplitude adjustment as a percentage of the
          analog output voltage. The percentage is applied to both of the channel's interleave DACs
          such that the analog output voltage is minimally affected. When the analog output is
          changed, this amplitude percentage is applied at the same time.

    Usage:
        - Using the ``.query()`` method will send the
          ``AWGControl:INTerleave:ADJustment:AMPLitude?`` query.
        - Using the ``.verify(value)`` method will send the
          ``AWGControl:INTerleave:ADJustment:AMPLitude?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``AWGControl:INTerleave:ADJustment:AMPLitude value`` command.

    SCPI Syntax:
        ```
        - AWGControl:INTerleave:ADJustment:AMPLitude <NRf>
        - AWGControl:INTerleave:ADJustment:AMPLitude?
        ```

    Info:
        - ``*RST`` sets this to 0%.
    """


class AwgcontrolInterleaveAdjustment(SCPICmdRead):
    """The ``AWGControl:INTerleave:ADJustment`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:INTerleave:ADJustment?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:INTerleave:ADJustment?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.amplitude``: The ``AWGControl:INTerleave:ADJustment:AMPLitude`` command.
        - ``.phase``: The ``AWGControl:INTerleave:ADJustment:PHASe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._amplitude = AwgcontrolInterleaveAdjustmentAmplitude(
            device, f"{self._cmd_syntax}:AMPLitude"
        )
        self._phase = AwgcontrolInterleaveAdjustmentPhase(device, f"{self._cmd_syntax}:PHASe")

    @property
    def amplitude(self) -> AwgcontrolInterleaveAdjustmentAmplitude:
        """Return the ``AWGControl:INTerleave:ADJustment:AMPLitude`` command.

        Description:
            - This command sets or returns the interleave amplitude adjustment as a percentage of
              the analog output voltage. The percentage is applied to both of the channel's
              interleave DACs such that the analog output voltage is minimally affected. When the
              analog output is changed, this amplitude percentage is applied at the same time.

        Usage:
            - Using the ``.query()`` method will send the
              ``AWGControl:INTerleave:ADJustment:AMPLitude?`` query.
            - Using the ``.verify(value)`` method will send the
              ``AWGControl:INTerleave:ADJustment:AMPLitude?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``AWGControl:INTerleave:ADJustment:AMPLitude value`` command.

        SCPI Syntax:
            ```
            - AWGControl:INTerleave:ADJustment:AMPLitude <NRf>
            - AWGControl:INTerleave:ADJustment:AMPLitude?
            ```

        Info:
            - ``*RST`` sets this to 0%.
        """
        return self._amplitude

    @property
    def phase(self) -> AwgcontrolInterleaveAdjustmentPhase:
        """Return the ``AWGControl:INTerleave:ADJustment:PHASe`` command.

        Description:
            - This command sets or returns the interleave adjustment phase. The phase adjustment is
              applied to both of the channel's interleave DACs.

        Usage:
            - Using the ``.query()`` method will send the
              ``AWGControl:INTerleave:ADJustment:PHASe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``AWGControl:INTerleave:ADJustment:PHASe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``AWGControl:INTerleave:ADJustment:PHASe value`` command.

        SCPI Syntax:
            ```
            - AWGControl:INTerleave:ADJustment:PHASe <NRf>
            - AWGControl:INTerleave:ADJustment:PHASe?
            ```

        Info:
            - ``*RST`` sets this to 0 degrees.
        """
        return self._phase


class AwgcontrolInterleave(SCPICmdRead):
    """The ``AWGControl:INTerleave`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:INTerleave?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:INTerleave?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.adjustment``: The ``AWGControl:INTerleave:ADJustment`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._adjustment = AwgcontrolInterleaveAdjustment(device, f"{self._cmd_syntax}:ADJustment")

    @property
    def adjustment(self) -> AwgcontrolInterleaveAdjustment:
        """Return the ``AWGControl:INTerleave:ADJustment`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:INTerleave:ADJustment?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``AWGControl:INTerleave:ADJustment?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.amplitude``: The ``AWGControl:INTerleave:ADJustment:AMPLitude`` command.
            - ``.phase``: The ``AWGControl:INTerleave:ADJustment:PHASe`` command.
        """
        return self._adjustment


class AwgcontrolDoutputItemState(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:DOUTput[n]:STATe`` command.

    Description:
        - This command sets or returns the state of the Direct signal path output (enabled or
          disabled) for the specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:DOUTput[n]:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:DOUTput[n]:STATe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AWGControl:DOUTput[n]:STATe value``
          command.

    SCPI Syntax:
        ```
        - AWGControl:DOUTput[n]:STATe {OFF|ON|0|1}
        - AWGControl:DOUTput[n]:STATe?
        ```
    """


class AwgcontrolDoutputItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``AWGControl:DOUTput[n]`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:DOUTput[n]?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:DOUTput[n]?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``AWGControl:DOUTput[n]:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = AwgcontrolDoutputItemState(device, f"{self._cmd_syntax}:STATe")

    @property
    def state(self) -> AwgcontrolDoutputItemState:
        """Return the ``AWGControl:DOUTput[n]:STATe`` command.

        Description:
            - This command sets or returns the state of the Direct signal path output (enabled or
              disabled) for the specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:DOUTput[n]:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:DOUTput[n]:STATe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AWGControl:DOUTput[n]:STATe value``
              command.

        SCPI Syntax:
            ```
            - AWGControl:DOUTput[n]:STATe {OFF|ON|0|1}
            - AWGControl:DOUTput[n]:STATe?
            ```
        """
        return self._state


class AwgcontrolDloadingEnable(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:DLOading:ENABle`` command.

    Description:
        - This command sets or returns the state (enabled or disabled) to either allow or not allow
          dynamic loading of waveforms into a sequence while the sequence is playing.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:DLOading:ENABle?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:DLOading:ENABle?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AWGControl:DLOading:ENABle value``
          command.

    SCPI Syntax:
        ```
        - AWGControl:DLOading:ENABle {OFF|ON|0|1}
        - AWGControl:DLOading:ENABle?
        ```
    """


class AwgcontrolDloading(SCPICmdRead):
    """The ``AWGControl:DLOading`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:DLOading?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:DLOading?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.enable``: The ``AWGControl:DLOading:ENABle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._enable = AwgcontrolDloadingEnable(device, f"{self._cmd_syntax}:ENABle")

    @property
    def enable(self) -> AwgcontrolDloadingEnable:
        """Return the ``AWGControl:DLOading:ENABle`` command.

        Description:
            - This command sets or returns the state (enabled or disabled) to either allow or not
              allow dynamic loading of waveforms into a sequence while the sequence is playing.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:DLOading:ENABle?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:DLOading:ENABle?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AWGControl:DLOading:ENABle value``
              command.

        SCPI Syntax:
            ```
            - AWGControl:DLOading:ENABle {OFF|ON|0|1}
            - AWGControl:DLOading:ENABle?
            ```
        """
        return self._enable


class AwgcontrolConfigureCnumber(SCPICmdRead):
    """The ``AWGControl:CONFigure:CNUMber`` command.

    Description:
        - This command returns the number of channels available on the AWG.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:CONFigure:CNUMber?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:CONFigure:CNUMber?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - AWGControl:CONFigure:CNUMber?
        ```
    """


class AwgcontrolConfigure(SCPICmdRead):
    """The ``AWGControl:CONFigure`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:CONFigure?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:CONFigure?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.cnumber``: The ``AWGControl:CONFigure:CNUMber`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._cnumber = AwgcontrolConfigureCnumber(device, f"{self._cmd_syntax}:CNUMber")

    @property
    def cnumber(self) -> AwgcontrolConfigureCnumber:
        """Return the ``AWGControl:CONFigure:CNUMber`` command.

        Description:
            - This command returns the number of channels available on the AWG.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:CONFigure:CNUMber?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:CONFigure:CNUMber?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - AWGControl:CONFigure:CNUMber?
            ```
        """
        return self._cnumber


class AwgcontrolCompile(SCPICmdWrite):
    """The ``AWGControl:COMPile`` command.

    Description:
        - This command compiles an equation file and imports the waveforms (created by the equation
          file) into the arbitrary waveform generator.

    Usage:
        - Using the ``.write(value)`` method will send the ``AWGControl:COMPile value`` command.

    SCPI Syntax:
        ```
        - AWGControl:COMPile <filename>
        ```
    """


class AwgcontrolClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:CLOCk:SOURce`` command.

    Description:
        - This command sets or returns the source of the clock.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:CLOCk:SOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:CLOCk:SOURce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AWGControl:CLOCk:SOURce value``
          command.

    SCPI Syntax:
        ```
        - AWGControl:CLOCk:SOURce {INTernal|EXTernal|EFIXed|EVARiable}
        - AWGControl:CLOCk:SOURce?
        ```

    Info:
        - ``INTernal`` - clock signal is generated internally and the reference frequency is derived
          by the internal oscillator.EFIXed - clock is generated internally and the reference
          frequency is derived from a fixed 10 MHz reference supplied at the Reference In
          connector.EVARiable - clock is generated internally and the reference frequency is derived
          from a variable reference supplied at the Reference In connector.EXTernal - clock signal
          supplied by the Clock In connector and the reference frequency is derived from the
          internal precision oscillator.
        - ``*RST`` sets this to INT.
    """


class AwgcontrolClockPhaseAdjust(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:CLOCk:PHASe:ADJust`` command.

    Description:
        - This command sets or returns the internal clock phase adjustment of the AWG.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:CLOCk:PHASe:ADJust?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:CLOCk:PHASe:ADJust?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AWGControl:CLOCk:PHASe:ADJust value``
          command.

    SCPI Syntax:
        ```
        - AWGControl:CLOCk:PHASe:ADJust <NR1>
        - AWGControl:CLOCk:PHASe:ADJust?
        ```
    """


class AwgcontrolClockPhase(SCPICmdRead):
    """The ``AWGControl:CLOCk:PHASe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:CLOCk:PHASe?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:CLOCk:PHASe?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.adjust``: The ``AWGControl:CLOCk:PHASe:ADJust`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._adjust = AwgcontrolClockPhaseAdjust(device, f"{self._cmd_syntax}:ADJust")

    @property
    def adjust(self) -> AwgcontrolClockPhaseAdjust:
        """Return the ``AWGControl:CLOCk:PHASe:ADJust`` command.

        Description:
            - This command sets or returns the internal clock phase adjustment of the AWG.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:CLOCk:PHASe:ADJust?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:CLOCk:PHASe:ADJust?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``AWGControl:CLOCk:PHASe:ADJust value`` command.

        SCPI Syntax:
            ```
            - AWGControl:CLOCk:PHASe:ADJust <NR1>
            - AWGControl:CLOCk:PHASe:ADJust?
            ```
        """
        return self._adjust


class AwgcontrolClockDrate(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:CLOCk:DRATe`` command.

    Description:
        - This command sets or returns the divider rate for the external clock.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:CLOCk:DRATe?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:CLOCk:DRATe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AWGControl:CLOCk:DRATe value`` command.

    SCPI Syntax:
        ```
        - AWGControl:CLOCk:DRATe <NR1>
        - AWGControl:CLOCk:DRATe?
        ```

    Info:
        - ``*RST`` sets this to 1.
    """


class AwgcontrolClock(SCPICmdRead):
    """The ``AWGControl:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:CLOCk?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.phase``: The ``AWGControl:CLOCk:PHASe`` command tree.
        - ``.drate``: The ``AWGControl:CLOCk:DRATe`` command.
        - ``.source``: The ``AWGControl:CLOCk:SOURce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._phase = AwgcontrolClockPhase(device, f"{self._cmd_syntax}:PHASe")
        self._drate = AwgcontrolClockDrate(device, f"{self._cmd_syntax}:DRATe")
        self._source = AwgcontrolClockSource(device, f"{self._cmd_syntax}:SOURce")

    @property
    def phase(self) -> AwgcontrolClockPhase:
        """Return the ``AWGControl:CLOCk:PHASe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:CLOCk:PHASe?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:CLOCk:PHASe?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.adjust``: The ``AWGControl:CLOCk:PHASe:ADJust`` command.
        """
        return self._phase

    @property
    def drate(self) -> AwgcontrolClockDrate:
        """Return the ``AWGControl:CLOCk:DRATe`` command.

        Description:
            - This command sets or returns the divider rate for the external clock.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:CLOCk:DRATe?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:CLOCk:DRATe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AWGControl:CLOCk:DRATe value``
              command.

        SCPI Syntax:
            ```
            - AWGControl:CLOCk:DRATe <NR1>
            - AWGControl:CLOCk:DRATe?
            ```

        Info:
            - ``*RST`` sets this to 1.
        """
        return self._drate

    @property
    def source(self) -> AwgcontrolClockSource:
        """Return the ``AWGControl:CLOCk:SOURce`` command.

        Description:
            - This command sets or returns the source of the clock.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:CLOCk:SOURce?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:CLOCk:SOURce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AWGControl:CLOCk:SOURce value``
              command.

        SCPI Syntax:
            ```
            - AWGControl:CLOCk:SOURce {INTernal|EXTernal|EFIXed|EVARiable}
            - AWGControl:CLOCk:SOURce?
            ```

        Info:
            - ``INTernal`` - clock signal is generated internally and the reference frequency is
              derived by the internal oscillator.EFIXed - clock is generated internally and the
              reference frequency is derived from a fixed 10 MHz reference supplied at the Reference
              In connector.EVARiable - clock is generated internally and the reference frequency is
              derived from a variable reference supplied at the Reference In connector.EXTernal -
              clock signal supplied by the Clock In connector and the reference frequency is derived
              from the internal precision oscillator.
            - ``*RST`` sets this to INT.
        """
        return self._source


class AwgcontrolArsettings(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:ARSettings`` command.

    Description:
        - This command sets or returns the state (enabled or disabled) of whether or not to apply
          the recommended settings of waveforms and sequences when they are assigned to a channel.
          When enabled, the system attempts to use the waveform's recommended settings (sample rate,
          amplitude, and offset) when the waveform is assigned to a channel. This includes waveforms
          within sequence tracks assigned to a channel. Recommended settings are defined as part the
          waveform properties and sequence properties.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:ARSettings?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:ARSettings?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AWGControl:ARSettings value`` command.

    SCPI Syntax:
        ```
        - AWGControl:ARSettings {0|1|ON|OFF}
        - AWGControl:ARSettings?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class Awgcontrol(SCPICmdRead):
    """The ``AWGControl`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.arsettings``: The ``AWGControl:ARSettings`` command.
        - ``.clock``: The ``AWGControl:CLOCk`` command tree.
        - ``.compile``: The ``AWGControl:COMPile`` command.
        - ``.configure``: The ``AWGControl:CONFigure`` command tree.
        - ``.dloading``: The ``AWGControl:DLOading`` command tree.
        - ``.doutput``: The ``AWGControl:DOUTput[n]`` command tree.
        - ``.interleave``: The ``AWGControl:INTerleave`` command tree.
        - ``.lstate``: The ``AWGControl:LSTate`` command.
        - ``.pjump``: The ``AWGControl:PJUMp`` command tree.
        - ``.rmode``: The ``AWGControl:RMODe`` command.
        - ``.rstate``: The ``AWGControl:RSTate`` command.
        - ``.run``: The ``AWGControl:RUN`` command tree.
        - ``.sname``: The ``AWGControl:SNAMe`` command.
        - ``.srestore``: The ``AWGControl:SREStore`` command.
        - ``.ssave``: The ``AWGControl:SSAVe`` command.
        - ``.stop``: The ``AWGControl:STOP`` command tree.
        - ``.streaming``: The ``AWGControl:STReaming`` command tree.
        - ``.timer``: The ``AWGControl:TIMer`` command tree.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "AWGControl"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._arsettings = AwgcontrolArsettings(device, f"{self._cmd_syntax}:ARSettings")
        self._compile = AwgcontrolCompile(device, f"{self._cmd_syntax}:COMPile")
        self._configure = AwgcontrolConfigure(device, f"{self._cmd_syntax}:CONFigure")
        self._dloading = AwgcontrolDloading(device, f"{self._cmd_syntax}:DLOading")
        self._doutput: Dict[int, AwgcontrolDoutputItem] = DefaultDictPassKeyToFactory(
            lambda x: AwgcontrolDoutputItem(device, f"{self._cmd_syntax}:DOUTput{x}")
        )
        self._interleave = AwgcontrolInterleave(device, f"{self._cmd_syntax}:INTerleave")
        self._lstate = AwgcontrolLstate(device, f"{self._cmd_syntax}:LSTate")
        self._pjump = AwgcontrolPjump(device, f"{self._cmd_syntax}:PJUMp")
        self._rmode = AwgcontrolRmode(device, f"{self._cmd_syntax}:RMODe")
        self._rstate = AwgcontrolRstate(device, f"{self._cmd_syntax}:RSTate")
        self._run = AwgcontrolRun(device, f"{self._cmd_syntax}:RUN")
        self._sname = AwgcontrolSname(device, f"{self._cmd_syntax}:SNAMe")
        self._srestore = AwgcontrolSrestore(device, f"{self._cmd_syntax}:SREStore")
        self._ssave = AwgcontrolSsave(device, f"{self._cmd_syntax}:SSAVe")
        self._stop = AwgcontrolStop(device, f"{self._cmd_syntax}:STOP")
        self._streaming = AwgcontrolStreaming(device, f"{self._cmd_syntax}:STReaming")
        self._timer = AwgcontrolTimer(device, f"{self._cmd_syntax}:TIMer")
        self._clock = AwgcontrolClock(device, f"{self._cmd_syntax}:CLOCk")

    @property
    def arsettings(self) -> AwgcontrolArsettings:
        """Return the ``AWGControl:ARSettings`` command.

        Description:
            - This command sets or returns the state (enabled or disabled) of whether or not to
              apply the recommended settings of waveforms and sequences when they are assigned to a
              channel. When enabled, the system attempts to use the waveform's recommended settings
              (sample rate, amplitude, and offset) when the waveform is assigned to a channel. This
              includes waveforms within sequence tracks assigned to a channel. Recommended settings
              are defined as part the waveform properties and sequence properties.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:ARSettings?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:ARSettings?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AWGControl:ARSettings value``
              command.

        SCPI Syntax:
            ```
            - AWGControl:ARSettings {0|1|ON|OFF}
            - AWGControl:ARSettings?
            ```
        """
        return self._arsettings

    @property
    def compile(self) -> AwgcontrolCompile:
        """Return the ``AWGControl:COMPile`` command.

        Description:
            - This command compiles an equation file and imports the waveforms (created by the
              equation file) into the arbitrary waveform generator.

        Usage:
            - Using the ``.write(value)`` method will send the ``AWGControl:COMPile value`` command.

        SCPI Syntax:
            ```
            - AWGControl:COMPile <filename>
            ```
        """
        return self._compile

    @property
    def configure(self) -> AwgcontrolConfigure:
        """Return the ``AWGControl:CONFigure`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:CONFigure?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:CONFigure?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.cnumber``: The ``AWGControl:CONFigure:CNUMber`` command.
        """
        return self._configure

    @property
    def dloading(self) -> AwgcontrolDloading:
        """Return the ``AWGControl:DLOading`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:DLOading?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:DLOading?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.enable``: The ``AWGControl:DLOading:ENABle`` command.
        """
        return self._dloading

    @property
    def doutput(self) -> Dict[int, AwgcontrolDoutputItem]:
        """Return the ``AWGControl:DOUTput[n]`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:DOUTput[n]?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:DOUTput[n]?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``AWGControl:DOUTput[n]:STATe`` command.
        """
        return self._doutput

    @property
    def interleave(self) -> AwgcontrolInterleave:
        """Return the ``AWGControl:INTerleave`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:INTerleave?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:INTerleave?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.adjustment``: The ``AWGControl:INTerleave:ADJustment`` command tree.
        """
        return self._interleave

    @property
    def lstate(self) -> AwgcontrolLstate:
        """Return the ``AWGControl:LSTate`` command.

        Description:
            - This command returns the waveform loading state of the arbitrary waveform generator
              when Dynamic Loading is enabled.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:LSTate?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:LSTate?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - AWGControl:LSTate?
            ```
        """
        return self._lstate

    @property
    def pjump(self) -> AwgcontrolPjump:
        """Return the ``AWGControl:PJUMp`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:PJUMp?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:PJUMp?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.jstrobe``: The ``AWGControl:PJUMp:JSTRobe`` command.
            - ``.sedge``: The ``AWGControl:PJUMp:SEDGe`` command.
        """
        return self._pjump

    @property
    def rmode(self) -> AwgcontrolRmode:
        """Return the ``AWGControl:RMODe`` command.

        Description:
            - This command sets or returns the run mode of the AWG for Channel 1.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:RMODe?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:RMODe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AWGControl:RMODe value`` command.

        SCPI Syntax:
            ```
            - AWGControl:RMODe {CONTinuous|TRIGgered}
            - AWGControl:RMODe?
            ```

        Info:
            - ``CONTinuous`` sets the Run Mode to Continuous (not waiting for a trigger event).
            - ``TRIGgered`` sets the Run Mode to Triggered, waiting for a trigger event. One
              waveform play out cycle completes, then play out stops, waiting for the next trigger
              event.
            - ``*RST`` sets this to CONT.
        """
        return self._rmode

    @property
    def rstate(self) -> AwgcontrolRstate:
        """Return the ``AWGControl:RSTate`` command.

        Description:
            - This command returns the run state of the AWG.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:RSTate?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:RSTate?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - AWGControl:RSTate?
            ```
        """
        return self._rstate

    @property
    def run(self) -> AwgcontrolRun:
        """Return the ``AWGControl:RUN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:RUN?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:RUN?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.immediate``: The ``AWGControl:RUN:IMMediate`` command.
        """
        return self._run

    @property
    def sname(self) -> AwgcontrolSname:
        """Return the ``AWGControl:SNAMe`` command.

        Description:
            - This command returns the AWG's most recently saved setup location. The response
              contains the full path for the file, including the disk drive letter (msus or, mass
              storage unit specifier).

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:SNAMe?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:SNAMe?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - AWGControl:SNAMe?
            ```
        """
        return self._sname

    @property
    def srestore(self) -> AwgcontrolSrestore:
        """Return the ``AWGControl:SREStore`` command.

        Description:
            - This command opens a setup file into the AWG's setup memory.

        Usage:
            - Using the ``.write(value)`` method will send the ``AWGControl:SREStore value``
              command.

        SCPI Syntax:
            ```
            - AWGControl:SREStore <filepath>[,<msus>]
            ```
        """
        return self._srestore

    @property
    def ssave(self) -> AwgcontrolSsave:
        """Return the ``AWGControl:SSAVe`` command.

        Description:
            - This command saves the AWG's setup with waveforms.

        Usage:
            - Using the ``.write(value)`` method will send the ``AWGControl:SSAVe value`` command.

        SCPI Syntax:
            ```
            - AWGControl:SSAVe <filepath>[,<msus>]
            ```
        """
        return self._ssave

    @property
    def stop(self) -> AwgcontrolStop:
        """Return the ``AWGControl:STOP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:STOP?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:STOP?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.immediate``: The ``AWGControl:STOP:IMMediate`` command.
        """
        return self._stop

    @property
    def streaming(self) -> AwgcontrolStreaming:
        """Return the ``AWGControl:STReaming`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:STReaming?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:STReaming?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.enable``: The ``AWGControl:STReaming:ENABle`` command.
            - ``.jevent``: The ``AWGControl:STReaming:JEVent`` command.
        """
        return self._streaming

    @property
    def timer(self) -> AwgcontrolTimer:
        """Return the ``AWGControl:TIMer`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:TIMer?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:TIMer?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.interval``: The ``AWGControl:TIMer:INTerval`` command tree.
            - ``.rstate``: The ``AWGControl:TIMer:RSTate`` command.
            - ``.run``: The ``AWGControl:TIMer:RUN`` command.
            - ``.soplay``: The ``AWGControl:TIMer:SOPLay`` command.
            - ``.stop``: The ``AWGControl:TIMer:STOP`` command.
        """
        return self._timer

    @property
    def clock(self) -> AwgcontrolClock:
        """Return the ``AWGControl:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:CLOCk?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.phase``: The ``AWGControl:CLOCk:PHASe`` command tree.
            - ``.drate``: The ``AWGControl:CLOCk:DRATe`` command.
            - ``.source``: The ``AWGControl:CLOCk:SOURce`` command.
        """
        return self._clock
