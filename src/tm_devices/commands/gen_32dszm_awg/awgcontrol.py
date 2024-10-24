"""The awgcontrol commands module.

These commands are used in the following models:
AWG5K, AWG5KC, AWG7K, AWG7KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - AWGControl:APPLication:RUN <application_name>
    - AWGControl:APPLication:STATe? <application_name>
    - AWGControl:CLOCk:DRATe <divider_rate>
    - AWGControl:CLOCk:DRATe?
    - AWGControl:CLOCk:PHASe:ADJust <NR3>
    - AWGControl:CLOCk:PHASe:ADJust?
    - AWGControl:CLOCk:SOURce <source>
    - AWGControl:CLOCk:SOURce?
    - AWGControl:COMPile <filename>
    - AWGControl:CONFigure:CNUMber?
    - AWGControl:DC[n]:STATe <state>
    - AWGControl:DC[n]:STATe?
    - AWGControl:DC[n]:VOLTage:LEVel:IMMediate:OFFSet <offset>
    - AWGControl:DC[n]:VOLTage:LEVel:IMMediate:OFFSet?
    - AWGControl:DOUTput[n]:STATe <state>
    - AWGControl:DOUTput[n]:STATe?
    - AWGControl:ENHanced:SEQuence:JMODe <jump_mode>
    - AWGControl:ENHanced:SEQuence:JMODe?
    - AWGControl:EVENt:DJUMp:DEFine <event_pattern>,<jump_target>
    - AWGControl:EVENt:DJUMp:DEFine? <event_pattern>
    - AWGControl:EVENt:JMODe <jump_mode>
    - AWGControl:EVENt:JMODe?
    - AWGControl:EVENt:SOFTware:IMMediate <target>
    - AWGControl:EVENt:TABLe:IMMediate
    - AWGControl:INTerleave:ADJustment:AMPLitude <NR3>
    - AWGControl:INTerleave:ADJustment:AMPLitude?
    - AWGControl:INTerleave:ADJustment:PHASe <NR3>
    - AWGControl:INTerleave:ADJustment:PHASe?
    - AWGControl:INTerleave:STATe <state>
    - AWGControl:INTerleave:STATe?
    - AWGControl:INTerleave:ZERoing <state>
    - AWGControl:INTerleave:ZERoing?
    - AWGControl:RMODe {CONTinuous|TRIGgered|GATed|SEQuence|ENHanced}
    - AWGControl:RMODe?
    - AWGControl:RRATe <repetition_rate>
    - AWGControl:RRATe:HOLD <hold_state>
    - AWGControl:RRATe:HOLD?
    - AWGControl:RRATe?
    - AWGControl:RSTate?
    - AWGControl:RUN:IMMediate
    - AWGControl:SEQuencer:POSition?
    - AWGControl:SEQuencer:TYPE?
    - AWGControl:SNAMe?
    - AWGControl:SREStore <file_name>[,<msus>]
    - AWGControl:SSAVe <file_name>[,<msus>]
    - AWGControl:STOP:IMMediate
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdReadWithArguments,
    SCPICmdWrite,
    SCPICmdWriteNoArguments,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


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
        - This command saves the arbitrary waveform generator's setting to a specified settings
          file. The drive may be a local or a network drive. If full path is not specified, the file
          will be stored in the current path.

    Usage:
        - Using the ``.write(value)`` method will send the ``AWGControl:SSAVe value`` command.

    SCPI Syntax:
        ```
        - AWGControl:SSAVe <file_name>[,<msus>]
        ```

    Info:
        - ``<file_name>`` ::=<string>.
        - ``<msus>`` (mass storage unit specifier)::=<string>.
    """


class AwgcontrolSrestore(SCPICmdWrite):
    """The ``AWGControl:SREStore`` command.

    Description:
        - This command restores the arbitrary waveform generator's setting from a specified settings
          file. The drive may be a local or a network drive. If the full path is not specified, the
          file will be stored in the current path.

    Usage:
        - Using the ``.write(value)`` method will send the ``AWGControl:SREStore value`` command.

    SCPI Syntax:
        ```
        - AWGControl:SREStore <file_name>[,<msus>]
        ```

    Info:
        - ``<file_name>`` ::=<string>.
        - ``<msus>`` (mass storage unit specifier)::=<string>.
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


class AwgcontrolSequencerType(SCPICmdRead):
    """The ``AWGControl:SEQuencer:TYPE`` command.

    Description:
        - This query returns the type of the arbitrary waveform generator's sequencer. The sequence
          is executed by the hardware sequencer whenever possible.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:SEQuencer:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:SEQuencer:TYPE?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - AWGControl:SEQuencer:TYPE?
        ```
    """


class AwgcontrolSequencerPosition(SCPICmdRead):
    """The ``AWGControl:SEQuencer:POSition`` command.

    Description:
        - This query returns the current position of the sequencer.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:SEQuencer:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:SEQuencer:POSition?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - AWGControl:SEQuencer:POSition?
        ```
    """


class AwgcontrolSequencer(SCPICmdRead):
    """The ``AWGControl:SEQuencer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:SEQuencer?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:SEQuencer?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``AWGControl:SEQuencer:POSition`` command.
        - ``.type``: The ``AWGControl:SEQuencer:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = AwgcontrolSequencerPosition(device, f"{self._cmd_syntax}:POSition")
        self._type = AwgcontrolSequencerType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def position(self) -> AwgcontrolSequencerPosition:
        """Return the ``AWGControl:SEQuencer:POSition`` command.

        Description:
            - This query returns the current position of the sequencer.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:SEQuencer:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:SEQuencer:POSition?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - AWGControl:SEQuencer:POSition?
            ```
        """
        return self._position

    @property
    def type(self) -> AwgcontrolSequencerType:
        """Return the ``AWGControl:SEQuencer:TYPE`` command.

        Description:
            - This query returns the type of the arbitrary waveform generator's sequencer. The
              sequence is executed by the hardware sequencer whenever possible.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:SEQuencer:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:SEQuencer:TYPE?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - AWGControl:SEQuencer:TYPE?
            ```
        """
        return self._type


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


class AwgcontrolRrateHold(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:RRATe:HOLD`` command.

    Description:
        - This command and query sets or returns the hold property of repetition rate. Setting this
          to ON keeps the repetition rate of the instrument constant even when the waveform size
          changes. This causes the sampling rate to change. When this is OFF, the repetition rate
          changes when the waveform length changes.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:RRATe:HOLD?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:RRATe:HOLD?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AWGControl:RRATe:HOLD value`` command.

    SCPI Syntax:
        ```
        - AWGControl:RRATe:HOLD <hold_state>
        - AWGControl:RRATe:HOLD?
        ```

    Info:
        - ``<hold_state>`` ::=<Boolean>.
        - ``0`` indicates OFF.
        - ``1`` indicates ON.
    """


class AwgcontrolRrate(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:RRATe`` command.

    Description:
        - This command and query sets or returns the repetition rate of the arbitrary waveform
          generator.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:RRATe?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:RRATe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AWGControl:RRATe value`` command.

    SCPI Syntax:
        ```
        - AWGControl:RRATe <repetition_rate>
        - AWGControl:RRATe?
        ```

    Info:
        - ``<repetition_rate>`` ::=<NR3>.

    Properties:
        - ``.hold``: The ``AWGControl:RRATe:HOLD`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hold = AwgcontrolRrateHold(device, f"{self._cmd_syntax}:HOLD")

    @property
    def hold(self) -> AwgcontrolRrateHold:
        """Return the ``AWGControl:RRATe:HOLD`` command.

        Description:
            - This command and query sets or returns the hold property of repetition rate. Setting
              this to ON keeps the repetition rate of the instrument constant even when the waveform
              size changes. This causes the sampling rate to change. When this is OFF, the
              repetition rate changes when the waveform length changes.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:RRATe:HOLD?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:RRATe:HOLD?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AWGControl:RRATe:HOLD value``
              command.

        SCPI Syntax:
            ```
            - AWGControl:RRATe:HOLD <hold_state>
            - AWGControl:RRATe:HOLD?
            ```

        Info:
            - ``<hold_state>`` ::=<Boolean>.
            - ``0`` indicates OFF.
            - ``1`` indicates ON.
        """
        return self._hold


class AwgcontrolRmode(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:RMODe`` command.

    Description:
        - This command and query sets or returns the run mode of the arbitrary waveform generator.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:RMODe?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:RMODe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AWGControl:RMODe value`` command.

    SCPI Syntax:
        ```
        - AWGControl:RMODe {CONTinuous|TRIGgered|GATed|SEQuence|ENHanced}
        - AWGControl:RMODe?
        ```

    Info:
        - ``CONTinuous`` sets Run Mode to Continuous.
        - ``TRIGgered`` sets Run Mode to Triggered.
        - ``GATed`` sets Run Mode to Gated.
        - ``SEQuence`` sets Run Mode to Sequence.
        - ``ENHanced`` is provided only for the compatibility with AWG400/500/600/700 series. In the
          response, SEQ is returned even if ENH is specified in the command.
        - ``CONTinuous``
    """


class AwgcontrolInterleaveZeroing(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:INTerleave:ZERoing`` command.

    Description:
        - This command and query sets or returns the state for zeroing when in the interleave mode.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:INTerleave:ZERoing?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:INTerleave:ZERoing?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AWGControl:INTerleave:ZERoing value``
          command.

    SCPI Syntax:
        ```
        - AWGControl:INTerleave:ZERoing <state>
        - AWGControl:INTerleave:ZERoing?
        ```

    Info:
        - ``<state>`` ::=<Boolean>.
        - ``0`` indicates OFF.
        - ``1`` indicates ON.
    """


class AwgcontrolInterleaveState(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:INTerleave:STATe`` command.

    Description:
        - This command and query sets or returns the interleave state for channels. This is
          available only on the AWG7000 series with option 06 instruments. When Interleave is ON,
          the output of CH1 and CH2 are mixed at the output circuit to achieve twice the sampling
          rate. When interleave state is switched on, then: Sampling rate is set to the nearest
          valid value Waveform remains as before Sequence pointing to CH2 waveform becomes 'Empty'
          Channel count becomes 1 Coupled channels lose the coupled state

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:INTerleave:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:INTerleave:STATe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AWGControl:INTerleave:STATe value``
          command.

    SCPI Syntax:
        ```
        - AWGControl:INTerleave:STATe <state>
        - AWGControl:INTerleave:STATe?
        ```

    Info:
        - ``<state>`` ::=<Boolean>.
        - ``0`` indicates OFF.
        - ``1`` indicates ON.
    """


class AwgcontrolInterleaveAdjustmentPhase(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:INTerleave:ADJustment:PHASe`` command.

    Description:
        - This command and query sets or returns the interleave adjustment phase. This command is
          available only for Option 06. This setting is only valid when the interleave state is On.

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
        - AWGControl:INTerleave:ADJustment:PHASe <NR3>
        - AWGControl:INTerleave:ADJustment:PHASe?
        ```

    Info:
        - ``<NR3>``
    """


class AwgcontrolInterleaveAdjustmentAmplitude(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:INTerleave:ADJustment:AMPLitude`` command.

    Description:
        - This command and query sets or returns the interleave adjustment amplitude. This command
          is available only for Option 06. This setting is only valid when the interleave state is
          On.

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
        - AWGControl:INTerleave:ADJustment:AMPLitude <NR3>
        - AWGControl:INTerleave:ADJustment:AMPLitude?
        ```

    Info:
        - ``<NR3>``
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
            - This command and query sets or returns the interleave adjustment amplitude. This
              command is available only for Option 06. This setting is only valid when the
              interleave state is On.

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
            - AWGControl:INTerleave:ADJustment:AMPLitude <NR3>
            - AWGControl:INTerleave:ADJustment:AMPLitude?
            ```

        Info:
            - ``<NR3>``
        """
        return self._amplitude

    @property
    def phase(self) -> AwgcontrolInterleaveAdjustmentPhase:
        """Return the ``AWGControl:INTerleave:ADJustment:PHASe`` command.

        Description:
            - This command and query sets or returns the interleave adjustment phase. This command
              is available only for Option 06. This setting is only valid when the interleave state
              is On.

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
            - AWGControl:INTerleave:ADJustment:PHASe <NR3>
            - AWGControl:INTerleave:ADJustment:PHASe?
            ```

        Info:
            - ``<NR3>``
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
        - ``.zeroing``: The ``AWGControl:INTerleave:ZERoing`` command.
        - ``.state``: The ``AWGControl:INTerleave:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._adjustment = AwgcontrolInterleaveAdjustment(device, f"{self._cmd_syntax}:ADJustment")
        self._zeroing = AwgcontrolInterleaveZeroing(device, f"{self._cmd_syntax}:ZERoing")
        self._state = AwgcontrolInterleaveState(device, f"{self._cmd_syntax}:STATe")

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

    @property
    def zeroing(self) -> AwgcontrolInterleaveZeroing:
        """Return the ``AWGControl:INTerleave:ZERoing`` command.

        Description:
            - This command and query sets or returns the state for zeroing when in the interleave
              mode.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:INTerleave:ZERoing?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:INTerleave:ZERoing?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``AWGControl:INTerleave:ZERoing value`` command.

        SCPI Syntax:
            ```
            - AWGControl:INTerleave:ZERoing <state>
            - AWGControl:INTerleave:ZERoing?
            ```

        Info:
            - ``<state>`` ::=<Boolean>.
            - ``0`` indicates OFF.
            - ``1`` indicates ON.
        """
        return self._zeroing

    @property
    def state(self) -> AwgcontrolInterleaveState:
        """Return the ``AWGControl:INTerleave:STATe`` command.

        Description:
            - This command and query sets or returns the interleave state for channels. This is
              available only on the AWG7000 series with option 06 instruments. When Interleave is
              ON, the output of CH1 and CH2 are mixed at the output circuit to achieve twice the
              sampling rate. When interleave state is switched on, then: Sampling rate is set to the
              nearest valid value Waveform remains as before Sequence pointing to CH2 waveform
              becomes 'Empty' Channel count becomes 1 Coupled channels lose the coupled state

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:INTerleave:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:INTerleave:STATe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AWGControl:INTerleave:STATe value``
              command.

        SCPI Syntax:
            ```
            - AWGControl:INTerleave:STATe <state>
            - AWGControl:INTerleave:STATe?
            ```

        Info:
            - ``<state>`` ::=<Boolean>.
            - ``0`` indicates OFF.
            - ``1`` indicates ON.
        """
        return self._state


class AwgcontrolEventTableImmediate(SCPICmdWriteNoArguments):
    """The ``AWGControl:EVENt:TABLe:IMMediate`` command.

    Description:
        - This command forcibly generates an event in the Table Jump mode. This command is available
          for the AWG5012B, AWG5000C, and AWG7000C with option 09. If the instrument (with option
          09) is not in the Table Jump mode, this command will generate a setting conflict error. To
          set the Jump mode, use the ``AWGCONTROL:ENHANCED:SEQUENCE:JMODE`` command. This command is
          provided for compatibility with the AWG400/500/600/700 series instruments. The same
          functionality can be invoked by the ``EVENT:IMMEDIATE`` command.

    Usage:
        - Using the ``.write()`` method will send the ``AWGControl:EVENt:TABLe:IMMediate`` command.

    SCPI Syntax:
        ```
        - AWGControl:EVENt:TABLe:IMMediate
        ```
    """


class AwgcontrolEventTable(SCPICmdRead):
    """The ``AWGControl:EVENt:TABLe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:EVENt:TABLe?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:EVENt:TABLe?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.immediate``: The ``AWGControl:EVENt:TABLe:IMMediate`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._immediate = AwgcontrolEventTableImmediate(device, f"{self._cmd_syntax}:IMMediate")

    @property
    def immediate(self) -> AwgcontrolEventTableImmediate:
        """Return the ``AWGControl:EVENt:TABLe:IMMediate`` command.

        Description:
            - This command forcibly generates an event in the Table Jump mode. This command is
              available for the AWG5012B, AWG5000C, and AWG7000C with option 09. If the instrument
              (with option 09) is not in the Table Jump mode, this command will generate a setting
              conflict error. To set the Jump mode, use the ``AWGCONTROL:ENHANCED:SEQUENCE:JMODE``
              command. This command is provided for compatibility with the AWG400/500/600/700 series
              instruments. The same functionality can be invoked by the ``EVENT:IMMEDIATE`` command.

        Usage:
            - Using the ``.write()`` method will send the ``AWGControl:EVENt:TABLe:IMMediate``
              command.

        SCPI Syntax:
            ```
            - AWGControl:EVENt:TABLe:IMMediate
            ```
        """
        return self._immediate


class AwgcontrolEventSoftwareImmediate(SCPICmdWrite):
    """The ``AWGControl:EVENt:SOFTware:IMMediate`` command.

    Description:
        - This command executes the sequencer jump to the specified element index.

    Usage:
        - Using the ``.write(value)`` method will send the
          ``AWGControl:EVENt:SOFTware:IMMediate value`` command.

    SCPI Syntax:
        ```
        - AWGControl:EVENt:SOFTware:IMMediate <target>
        ```

    Info:
        - ``<target>`` ::=<NR1>.
    """


class AwgcontrolEventSoftware(SCPICmdRead):
    """The ``AWGControl:EVENt:SOFTware`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:EVENt:SOFTware?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:EVENt:SOFTware?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.immediate``: The ``AWGControl:EVENt:SOFTware:IMMediate`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._immediate = AwgcontrolEventSoftwareImmediate(device, f"{self._cmd_syntax}:IMMediate")

    @property
    def immediate(self) -> AwgcontrolEventSoftwareImmediate:
        """Return the ``AWGControl:EVENt:SOFTware:IMMediate`` command.

        Description:
            - This command executes the sequencer jump to the specified element index.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``AWGControl:EVENt:SOFTware:IMMediate value`` command.

        SCPI Syntax:
            ```
            - AWGControl:EVENt:SOFTware:IMMediate <target>
            ```

        Info:
            - ``<target>`` ::=<NR1>.
        """
        return self._immediate


class AwgcontrolEventJmode(SCPICmdWrite, SCPICmdRead):
    r"""The ``AWGControl:EVENt:JMODe`` command.

    Description:
        - This command and query sets or returns the event jump mode.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:EVENt:JMODe?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:EVENt:JMODe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AWGControl:EVENt:JMODe value`` command.

    SCPI Syntax:
        ```
        - AWGControl:EVENt:JMODe <jump_mode>
        - AWGControl:EVENt:JMODe?
        ```

    Info:
        - ``jump_mode`` ::={EJUMp \| DJUMp}.
        - ``EJUMp`` sets the Jump Mode to Event Jump. The jump targets defined in the sequence
          definition table will be used as the jump target. In this mode, the instrument behavior
          for the event jump is the same as that of the AWG7000/AWG5000 series.
        - ``DJUMp`` sets the Jump Mode to Dynamic Jump. The Dynamic Jump target definitions are used
          as the jump target. This is also known as Table Jump.
    """


class AwgcontrolEventDjumpDefine(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``AWGControl:EVENt:DJUMp:DEFine`` command.

    Description:
        - This command associates an event pattern with the jump target for Dynamic Jump. The query
          returns the jump target associated to the specified ``<event_pattern>``.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``AWGControl:EVENt:DJUMp:DEFine? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``AWGControl:EVENt:DJUMp:DEFine? argument`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AWGControl:EVENt:DJUMp:DEFine value``
          command.

    SCPI Syntax:
        ```
        - AWGControl:EVENt:DJUMp:DEFine <event_pattern>,<jump_target>
        - AWGControl:EVENt:DJUMp:DEFine? <event_pattern>
        ```

    Info:
        - ``event_pattern`` ::=<NR1>. The values ranges between 0 and 511. This parameter specifies
          the event pattern to make an event jump. The event bits are mapped to the integer value as
          follows.
        - ``jump_target`` ::=<NR1>. The values are -1 and 1 to maximum sequence length. This
          parameter specifies the sequence index as the jump target. If -1 is specified, the event
          jump for the specified ``<event_pattern>`` is cancelled.
    """


class AwgcontrolEventDjump(SCPICmdRead):
    """The ``AWGControl:EVENt:DJUMp`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:EVENt:DJUMp?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:EVENt:DJUMp?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.define``: The ``AWGControl:EVENt:DJUMp:DEFine`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._define = AwgcontrolEventDjumpDefine(device, f"{self._cmd_syntax}:DEFine")

    @property
    def define(self) -> AwgcontrolEventDjumpDefine:
        """Return the ``AWGControl:EVENt:DJUMp:DEFine`` command.

        Description:
            - This command associates an event pattern with the jump target for Dynamic Jump. The
              query returns the jump target associated to the specified ``<event_pattern>``.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``AWGControl:EVENt:DJUMp:DEFine? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``AWGControl:EVENt:DJUMp:DEFine? argument`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``AWGControl:EVENt:DJUMp:DEFine value`` command.

        SCPI Syntax:
            ```
            - AWGControl:EVENt:DJUMp:DEFine <event_pattern>,<jump_target>
            - AWGControl:EVENt:DJUMp:DEFine? <event_pattern>
            ```

        Info:
            - ``event_pattern`` ::=<NR1>. The values ranges between 0 and 511. This parameter
              specifies the event pattern to make an event jump. The event bits are mapped to the
              integer value as follows.
            - ``jump_target`` ::=<NR1>. The values are -1 and 1 to maximum sequence length. This
              parameter specifies the sequence index as the jump target. If -1 is specified, the
              event jump for the specified ``<event_pattern>`` is cancelled.
        """
        return self._define


class AwgcontrolEvent(SCPICmdRead):
    """The ``AWGControl:EVENt`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:EVENt?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:EVENt?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.djump``: The ``AWGControl:EVENt:DJUMp`` command tree.
        - ``.jmode``: The ``AWGControl:EVENt:JMODe`` command.
        - ``.software``: The ``AWGControl:EVENt:SOFTware`` command tree.
        - ``.table``: The ``AWGControl:EVENt:TABLe`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._djump = AwgcontrolEventDjump(device, f"{self._cmd_syntax}:DJUMp")
        self._jmode = AwgcontrolEventJmode(device, f"{self._cmd_syntax}:JMODe")
        self._software = AwgcontrolEventSoftware(device, f"{self._cmd_syntax}:SOFTware")
        self._table = AwgcontrolEventTable(device, f"{self._cmd_syntax}:TABLe")

    @property
    def djump(self) -> AwgcontrolEventDjump:
        """Return the ``AWGControl:EVENt:DJUMp`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:EVENt:DJUMp?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:EVENt:DJUMp?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.define``: The ``AWGControl:EVENt:DJUMp:DEFine`` command.
        """
        return self._djump

    @property
    def jmode(self) -> AwgcontrolEventJmode:
        r"""Return the ``AWGControl:EVENt:JMODe`` command.

        Description:
            - This command and query sets or returns the event jump mode.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:EVENt:JMODe?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:EVENt:JMODe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AWGControl:EVENt:JMODe value``
              command.

        SCPI Syntax:
            ```
            - AWGControl:EVENt:JMODe <jump_mode>
            - AWGControl:EVENt:JMODe?
            ```

        Info:
            - ``jump_mode`` ::={EJUMp \| DJUMp}.
            - ``EJUMp`` sets the Jump Mode to Event Jump. The jump targets defined in the sequence
              definition table will be used as the jump target. In this mode, the instrument
              behavior for the event jump is the same as that of the AWG7000/AWG5000 series.
            - ``DJUMp`` sets the Jump Mode to Dynamic Jump. The Dynamic Jump target definitions are
              used as the jump target. This is also known as Table Jump.
        """
        return self._jmode

    @property
    def software(self) -> AwgcontrolEventSoftware:
        """Return the ``AWGControl:EVENt:SOFTware`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:EVENt:SOFTware?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:EVENt:SOFTware?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.immediate``: The ``AWGControl:EVENt:SOFTware:IMMediate`` command.
        """
        return self._software

    @property
    def table(self) -> AwgcontrolEventTable:
        """Return the ``AWGControl:EVENt:TABLe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:EVENt:TABLe?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:EVENt:TABLe?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.immediate``: The ``AWGControl:EVENt:TABLe:IMMediate`` command.
        """
        return self._table


class AwgcontrolEnhancedSequenceJmode(SCPICmdWrite, SCPICmdRead):
    r"""The ``AWGControl:ENHanced:SEQuence:JMODe`` command.

    Description:
        - This command and query sets or returns the jump mode. This command is available for the
          AWG5012B, AWG5000C, and AWG7000C with option 09. This command is provided for
          compatibility with the AWG400/500/600/700 series instruments. The query form will return
          TABL when the instrument is in the Table Jump mode, otherwise LOG will be returned.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:ENHanced:SEQuence:JMODe?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:ENHanced:SEQuence:JMODe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``AWGControl:ENHanced:SEQuence:JMODe value`` command.

    SCPI Syntax:
        ```
        - AWGControl:ENHanced:SEQuence:JMODe <jump_mode>
        - AWGControl:ENHanced:SEQuence:JMODe?
        ```

    Info:
        - ``<jump_mode>`` ::={LOGic\|TABLe\|SOFTware}.
        - ``LOGic or SOFTware`` activates Event Jump. The jump target defined in the sequence
          definition will be the target of Event Jump.
        - ``TABLe`` activates Table Jump. The Table Jump definition is used as the jump target.
    """


class AwgcontrolEnhancedSequence(SCPICmdRead):
    """The ``AWGControl:ENHanced:SEQuence`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:ENHanced:SEQuence?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:ENHanced:SEQuence?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.jmode``: The ``AWGControl:ENHanced:SEQuence:JMODe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._jmode = AwgcontrolEnhancedSequenceJmode(device, f"{self._cmd_syntax}:JMODe")

    @property
    def jmode(self) -> AwgcontrolEnhancedSequenceJmode:
        r"""Return the ``AWGControl:ENHanced:SEQuence:JMODe`` command.

        Description:
            - This command and query sets or returns the jump mode. This command is available for
              the AWG5012B, AWG5000C, and AWG7000C with option 09. This command is provided for
              compatibility with the AWG400/500/600/700 series instruments. The query form will
              return TABL when the instrument is in the Table Jump mode, otherwise LOG will be
              returned.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:ENHanced:SEQuence:JMODe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``AWGControl:ENHanced:SEQuence:JMODe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``AWGControl:ENHanced:SEQuence:JMODe value`` command.

        SCPI Syntax:
            ```
            - AWGControl:ENHanced:SEQuence:JMODe <jump_mode>
            - AWGControl:ENHanced:SEQuence:JMODe?
            ```

        Info:
            - ``<jump_mode>`` ::={LOGic\|TABLe\|SOFTware}.
            - ``LOGic or SOFTware`` activates Event Jump. The jump target defined in the sequence
              definition will be the target of Event Jump.
            - ``TABLe`` activates Table Jump. The Table Jump definition is used as the jump target.
        """
        return self._jmode


class AwgcontrolEnhanced(SCPICmdRead):
    """The ``AWGControl:ENHanced`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:ENHanced?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:ENHanced?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.sequence``: The ``AWGControl:ENHanced:SEQuence`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._sequence = AwgcontrolEnhancedSequence(device, f"{self._cmd_syntax}:SEQuence")

    @property
    def sequence(self) -> AwgcontrolEnhancedSequence:
        """Return the ``AWGControl:ENHanced:SEQuence`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:ENHanced:SEQuence?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:ENHanced:SEQuence?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.jmode``: The ``AWGControl:ENHanced:SEQuence:JMODe`` command.
        """
        return self._sequence


class AwgcontrolDoutputItemState(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:DOUTput[n]:STATe`` command.

    Description:
        - This command enables the raw DAC waveform outputs for the specified channel. The query
          form of this command returns the status of raw DAC waveform output for the specified
          channel. When the state is ON, offset and filter settings for the channel are ignored.
          This command is not supported on the instruments with Option 02 or Option 06.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:DOUTput[n]:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:DOUTput[n]:STATe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AWGControl:DOUTput[n]:STATe value``
          command.

    SCPI Syntax:
        ```
        - AWGControl:DOUTput[n]:STATe <state>
        - AWGControl:DOUTput[n]:STATe?
        ```

    Info:
        - ``<state>`` ::= <Boolean>.
        - ``0`` indicates OFF.
        - ``1`` indicates ON.
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
            - This command enables the raw DAC waveform outputs for the specified channel. The query
              form of this command returns the status of raw DAC waveform output for the specified
              channel. When the state is ON, offset and filter settings for the channel are ignored.
              This command is not supported on the instruments with Option 02 or Option 06.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:DOUTput[n]:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:DOUTput[n]:STATe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AWGControl:DOUTput[n]:STATe value``
              command.

        SCPI Syntax:
            ```
            - AWGControl:DOUTput[n]:STATe <state>
            - AWGControl:DOUTput[n]:STATe?
            ```

        Info:
            - ``<state>`` ::= <Boolean>.
            - ``0`` indicates OFF.
            - ``1`` indicates ON.
        """
        return self._state


class AwgcontrolDcItemVoltageLevelImmediateOffset(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:DC[n]:VOLTage:LEVel:IMMediate:OFFSet`` command.

    Description:
        - This command and query sets or returns the DC output level. The value of n = 1|2|3|4.

    Usage:
        - Using the ``.query()`` method will send the
          ``AWGControl:DC[n]:VOLTage:LEVel:IMMediate:OFFSet?`` query.
        - Using the ``.verify(value)`` method will send the
          ``AWGControl:DC[n]:VOLTage:LEVel:IMMediate:OFFSet?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``AWGControl:DC[n]:VOLTage:LEVel:IMMediate:OFFSet value`` command.

    SCPI Syntax:
        ```
        - AWGControl:DC[n]:VOLTage:LEVel:IMMediate:OFFSet <offset>
        - AWGControl:DC[n]:VOLTage:LEVel:IMMediate:OFFSet?
        ```

    Info:
        - ``<offset>`` ::=<NR3> the value will be between -3.0 V to +5.0 V.
    """


class AwgcontrolDcItemVoltageLevelImmediate(SCPICmdRead):
    """The ``AWGControl:DC[n]:VOLTage:LEVel:IMMediate`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:DC[n]:VOLTage:LEVel:IMMediate?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``AWGControl:DC[n]:VOLTage:LEVel:IMMediate?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.offset``: The ``AWGControl:DC[n]:VOLTage:LEVel:IMMediate:OFFSet`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._offset = AwgcontrolDcItemVoltageLevelImmediateOffset(
            device, f"{self._cmd_syntax}:OFFSet"
        )

    @property
    def offset(self) -> AwgcontrolDcItemVoltageLevelImmediateOffset:
        """Return the ``AWGControl:DC[n]:VOLTage:LEVel:IMMediate:OFFSet`` command.

        Description:
            - This command and query sets or returns the DC output level. The value of n = 1|2|3|4.

        Usage:
            - Using the ``.query()`` method will send the
              ``AWGControl:DC[n]:VOLTage:LEVel:IMMediate:OFFSet?`` query.
            - Using the ``.verify(value)`` method will send the
              ``AWGControl:DC[n]:VOLTage:LEVel:IMMediate:OFFSet?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``AWGControl:DC[n]:VOLTage:LEVel:IMMediate:OFFSet value`` command.

        SCPI Syntax:
            ```
            - AWGControl:DC[n]:VOLTage:LEVel:IMMediate:OFFSet <offset>
            - AWGControl:DC[n]:VOLTage:LEVel:IMMediate:OFFSet?
            ```

        Info:
            - ``<offset>`` ::=<NR3> the value will be between -3.0 V to +5.0 V.
        """
        return self._offset


class AwgcontrolDcItemVoltageLevel(SCPICmdRead):
    """The ``AWGControl:DC[n]:VOLTage:LEVel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:DC[n]:VOLTage:LEVel?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:DC[n]:VOLTage:LEVel?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.immediate``: The ``AWGControl:DC[n]:VOLTage:LEVel:IMMediate`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._immediate = AwgcontrolDcItemVoltageLevelImmediate(
            device, f"{self._cmd_syntax}:IMMediate"
        )

    @property
    def immediate(self) -> AwgcontrolDcItemVoltageLevelImmediate:
        """Return the ``AWGControl:DC[n]:VOLTage:LEVel:IMMediate`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``AWGControl:DC[n]:VOLTage:LEVel:IMMediate?`` query.
            - Using the ``.verify(value)`` method will send the
              ``AWGControl:DC[n]:VOLTage:LEVel:IMMediate?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.offset``: The ``AWGControl:DC[n]:VOLTage:LEVel:IMMediate:OFFSet`` command.
        """
        return self._immediate


class AwgcontrolDcItemVoltage(SCPICmdRead):
    """The ``AWGControl:DC[n]:VOLTage`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:DC[n]:VOLTage?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:DC[n]:VOLTage?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.level``: The ``AWGControl:DC[n]:VOLTage:LEVel`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._level = AwgcontrolDcItemVoltageLevel(device, f"{self._cmd_syntax}:LEVel")

    @property
    def level(self) -> AwgcontrolDcItemVoltageLevel:
        """Return the ``AWGControl:DC[n]:VOLTage:LEVel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:DC[n]:VOLTage:LEVel?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:DC[n]:VOLTage:LEVel?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.immediate``: The ``AWGControl:DC[n]:VOLTage:LEVel:IMMediate`` command tree.
        """
        return self._level


class AwgcontrolDcItemState(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:DC[n]:STATe`` command.

    Description:
        - This commands and query sets or returns the output state of one of the four DC outputs.
          Use this command to turn off or turn on the DC outputs. The value of n = 1|2|3|4 The
          output state is common for all DC outputs. Therefore, irrespective of the value used for
          'n' in the command, all DC outputs are switched on or switched off at once.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:DC[n]:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:DC[n]:STATe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AWGControl:DC[n]:STATe value`` command.

    SCPI Syntax:
        ```
        - AWGControl:DC[n]:STATe <state>
        - AWGControl:DC[n]:STATe?
        ```

    Info:
        - ``<state>`` ::= <Boolean>.
        - ``0`` indicates OFF.
        - ``1`` indicates ON.
    """


class AwgcontrolDcItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``AWGControl:DC[n]`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:DC[n]?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:DC[n]?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.voltage``: The ``AWGControl:DC[n]:VOLTage`` command tree.
        - ``.state``: The ``AWGControl:DC[n]:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._voltage = AwgcontrolDcItemVoltage(device, f"{self._cmd_syntax}:VOLTage")
        self._state = AwgcontrolDcItemState(device, f"{self._cmd_syntax}:STATe")

    @property
    def voltage(self) -> AwgcontrolDcItemVoltage:
        """Return the ``AWGControl:DC[n]:VOLTage`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:DC[n]:VOLTage?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:DC[n]:VOLTage?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.level``: The ``AWGControl:DC[n]:VOLTage:LEVel`` command tree.
        """
        return self._voltage

    @property
    def state(self) -> AwgcontrolDcItemState:
        """Return the ``AWGControl:DC[n]:STATe`` command.

        Description:
            - This commands and query sets or returns the output state of one of the four DC
              outputs. Use this command to turn off or turn on the DC outputs. The value of n =
              1|2|3|4 The output state is common for all DC outputs. Therefore, irrespective of the
              value used for 'n' in the command, all DC outputs are switched on or switched off at
              once.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:DC[n]:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:DC[n]:STATe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AWGControl:DC[n]:STATe value``
              command.

        SCPI Syntax:
            ```
            - AWGControl:DC[n]:STATe <state>
            - AWGControl:DC[n]:STATe?
            ```

        Info:
            - ``<state>`` ::= <Boolean>.
            - ``0`` indicates OFF.
            - ``1`` indicates ON.
        """
        return self._state


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
    r"""The ``AWGControl:CLOCk:SOURce`` command.

    Description:
        - This command and query sets or returns the clock source. When the clock source is
          internal, the arbitrary waveform generator's internal clock is used to generate the clock
          signal. If the clock source is external, the clock signal from an external oscillator is
          used.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:CLOCk:SOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:CLOCk:SOURce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AWGControl:CLOCk:SOURce value``
          command.

    SCPI Syntax:
        ```
        - AWGControl:CLOCk:SOURce <source>
        - AWGControl:CLOCk:SOURce?
        ```

    Info:
        - ``<source>`` ::={EXTernal\|INTernal}.
        - ``EXTernal`` specifies that the clock signal from external oscillator is used.
        - ``INTernal`` specifies that the clock signal is generated internally.
    """


class AwgcontrolClockPhaseAdjust(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:CLOCk:PHASe:ADJust`` command.

    Description:
        - (AWG7000B and AWG7000C Series only) This command and query sets or returns the clock phase
          adjust. It is used to adjust the internal clock phase of the instrument to synchronize or
          align timing with external devices. When the sampling rate is below 375 MS/s, the
          instrument may take a few minutes to execute the command or to set the sampling rate.
          Spurious in the output signal may increase if you set the clock phase to any value other
          than 0 (zero) with the interleave in On state.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:CLOCk:PHASe:ADJust?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:CLOCk:PHASe:ADJust?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AWGControl:CLOCk:PHASe:ADJust value``
          command.

    SCPI Syntax:
        ```
        - AWGControl:CLOCk:PHASe:ADJust <NR3>
        - AWGControl:CLOCk:PHASe:ADJust?
        ```

    Info:
        - ``<NR3>``
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
            - (AWG7000B and AWG7000C Series only) This command and query sets or returns the clock
              phase adjust. It is used to adjust the internal clock phase of the instrument to
              synchronize or align timing with external devices. When the sampling rate is below 375
              MS/s, the instrument may take a few minutes to execute the command or to set the
              sampling rate. Spurious in the output signal may increase if you set the clock phase
              to any value other than 0 (zero) with the interleave in On state.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:CLOCk:PHASe:ADJust?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:CLOCk:PHASe:ADJust?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``AWGControl:CLOCk:PHASe:ADJust value`` command.

        SCPI Syntax:
            ```
            - AWGControl:CLOCk:PHASe:ADJust <NR3>
            - AWGControl:CLOCk:PHASe:ADJust?
            ```

        Info:
            - ``<NR3>``
        """
        return self._adjust


class AwgcontrolClockDrate(SCPICmdWrite, SCPICmdRead):
    """The ``AWGControl:CLOCk:DRATe`` command.

    Description:
        - This command and query sets or returns the divider rate for the external oscillator.
          Divider rate is applicable only when the reference oscillator source is external. Only 1,
          2, 4, 8… are valid values. Errors for the AWG5000 series are -222 and -224. The -222,
          which is out of range, is produced when a value is greater than 32 and less than or equal
          to 256. Any non-power of 2 value creates a -224 error. For the AWG7000 series, there is no
          out of range error and any non-power of 2 and greater than 256 produces a -224.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:CLOCk:DRATe?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:CLOCk:DRATe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AWGControl:CLOCk:DRATe value`` command.

    SCPI Syntax:
        ```
        - AWGControl:CLOCk:DRATe <divider_rate>
        - AWGControl:CLOCk:DRATe?
        ```

    Info:
        - ``<divider_rate>`` ::=<NR1>.
    """


class AwgcontrolClock(SCPICmdRead):
    """The ``AWGControl:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:CLOCk?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.drate``: The ``AWGControl:CLOCk:DRATe`` command.
        - ``.phase``: The ``AWGControl:CLOCk:PHASe`` command tree.
        - ``.source``: The ``AWGControl:CLOCk:SOURce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._drate = AwgcontrolClockDrate(device, f"{self._cmd_syntax}:DRATe")
        self._phase = AwgcontrolClockPhase(device, f"{self._cmd_syntax}:PHASe")
        self._source = AwgcontrolClockSource(device, f"{self._cmd_syntax}:SOURce")

    @property
    def drate(self) -> AwgcontrolClockDrate:
        """Return the ``AWGControl:CLOCk:DRATe`` command.

        Description:
            - This command and query sets or returns the divider rate for the external oscillator.
              Divider rate is applicable only when the reference oscillator source is external. Only
              1, 2, 4, 8… are valid values. Errors for the AWG5000 series are -222 and -224. The
              -222, which is out of range, is produced when a value is greater than 32 and less than
              or equal to 256. Any non-power of 2 value creates a -224 error. For the AWG7000
              series, there is no out of range error and any non-power of 2 and greater than 256
              produces a -224.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:CLOCk:DRATe?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:CLOCk:DRATe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AWGControl:CLOCk:DRATe value``
              command.

        SCPI Syntax:
            ```
            - AWGControl:CLOCk:DRATe <divider_rate>
            - AWGControl:CLOCk:DRATe?
            ```

        Info:
            - ``<divider_rate>`` ::=<NR1>.
        """
        return self._drate

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
    def source(self) -> AwgcontrolClockSource:
        r"""Return the ``AWGControl:CLOCk:SOURce`` command.

        Description:
            - This command and query sets or returns the clock source. When the clock source is
              internal, the arbitrary waveform generator's internal clock is used to generate the
              clock signal. If the clock source is external, the clock signal from an external
              oscillator is used.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:CLOCk:SOURce?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:CLOCk:SOURce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AWGControl:CLOCk:SOURce value``
              command.

        SCPI Syntax:
            ```
            - AWGControl:CLOCk:SOURce <source>
            - AWGControl:CLOCk:SOURce?
            ```

        Info:
            - ``<source>`` ::={EXTernal\|INTernal}.
            - ``EXTernal`` specifies that the clock signal from external oscillator is used.
            - ``INTernal`` specifies that the clock signal is generated internally.
        """
        return self._source


class AwgcontrolApplicationState(SCPICmdReadWithArguments):
    """The ``AWGControl:APPLication:STATe`` command.

    Description:
        - This query returns the running state of the specified application.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``AWGControl:APPLication:STATe? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``AWGControl:APPLication:STATe? argument`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - AWGControl:APPLication:STATe? <application_name>
        ```

    Info:
        - ``<application_name>`` ::=<string>.
    """


class AwgcontrolApplicationRun(SCPICmdWrite):
    """The ``AWGControl:APPLication:RUN`` command.

    Description:
        - This command executes the specified application.

    Usage:
        - Using the ``.write(value)`` method will send the ``AWGControl:APPLication:RUN value``
          command.

    SCPI Syntax:
        ```
        - AWGControl:APPLication:RUN <application_name>
        ```

    Info:
        - ``<application_name>`` ::=<string> specifies the application to be executed.
    """


class AwgcontrolApplication(SCPICmdRead):
    """The ``AWGControl:APPLication`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl:APPLication?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl:APPLication?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.run``: The ``AWGControl:APPLication:RUN`` command.
        - ``.state``: The ``AWGControl:APPLication:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._run = AwgcontrolApplicationRun(device, f"{self._cmd_syntax}:RUN")
        self._state = AwgcontrolApplicationState(device, f"{self._cmd_syntax}:STATe")

    @property
    def run(self) -> AwgcontrolApplicationRun:
        """Return the ``AWGControl:APPLication:RUN`` command.

        Description:
            - This command executes the specified application.

        Usage:
            - Using the ``.write(value)`` method will send the ``AWGControl:APPLication:RUN value``
              command.

        SCPI Syntax:
            ```
            - AWGControl:APPLication:RUN <application_name>
            ```

        Info:
            - ``<application_name>`` ::=<string> specifies the application to be executed.
        """
        return self._run

    @property
    def state(self) -> AwgcontrolApplicationState:
        """Return the ``AWGControl:APPLication:STATe`` command.

        Description:
            - This query returns the running state of the specified application.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``AWGControl:APPLication:STATe? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``AWGControl:APPLication:STATe? argument`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - AWGControl:APPLication:STATe? <application_name>
            ```

        Info:
            - ``<application_name>`` ::=<string>.
        """
        return self._state


#  pylint: disable=too-many-instance-attributes
class Awgcontrol(SCPICmdRead):
    """The ``AWGControl`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AWGControl?`` query.
        - Using the ``.verify(value)`` method will send the ``AWGControl?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.application``: The ``AWGControl:APPLication`` command tree.
        - ``.clock``: The ``AWGControl:CLOCk`` command tree.
        - ``.compile``: The ``AWGControl:COMPile`` command.
        - ``.configure``: The ``AWGControl:CONFigure`` command tree.
        - ``.dc``: The ``AWGControl:DC[n]`` command tree.
        - ``.doutput``: The ``AWGControl:DOUTput[n]`` command tree.
        - ``.enhanced``: The ``AWGControl:ENHanced`` command tree.
        - ``.event``: The ``AWGControl:EVENt`` command tree.
        - ``.interleave``: The ``AWGControl:INTerleave`` command tree.
        - ``.rmode``: The ``AWGControl:RMODe`` command.
        - ``.rrate``: The ``AWGControl:RRATe`` command.
        - ``.rstate``: The ``AWGControl:RSTate`` command.
        - ``.run``: The ``AWGControl:RUN`` command tree.
        - ``.sequencer``: The ``AWGControl:SEQuencer`` command tree.
        - ``.sname``: The ``AWGControl:SNAMe`` command.
        - ``.srestore``: The ``AWGControl:SREStore`` command.
        - ``.ssave``: The ``AWGControl:SSAVe`` command.
        - ``.stop``: The ``AWGControl:STOP`` command tree.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "AWGControl"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._application = AwgcontrolApplication(device, f"{self._cmd_syntax}:APPLication")
        self._clock = AwgcontrolClock(device, f"{self._cmd_syntax}:CLOCk")
        self._compile = AwgcontrolCompile(device, f"{self._cmd_syntax}:COMPile")
        self._configure = AwgcontrolConfigure(device, f"{self._cmd_syntax}:CONFigure")
        self._dc: Dict[int, AwgcontrolDcItem] = DefaultDictPassKeyToFactory(
            lambda x: AwgcontrolDcItem(device, f"{self._cmd_syntax}:DC{x}")
        )
        self._doutput: Dict[int, AwgcontrolDoutputItem] = DefaultDictPassKeyToFactory(
            lambda x: AwgcontrolDoutputItem(device, f"{self._cmd_syntax}:DOUTput{x}")
        )
        self._enhanced = AwgcontrolEnhanced(device, f"{self._cmd_syntax}:ENHanced")
        self._event = AwgcontrolEvent(device, f"{self._cmd_syntax}:EVENt")
        self._interleave = AwgcontrolInterleave(device, f"{self._cmd_syntax}:INTerleave")
        self._rmode = AwgcontrolRmode(device, f"{self._cmd_syntax}:RMODe")
        self._rrate = AwgcontrolRrate(device, f"{self._cmd_syntax}:RRATe")
        self._rstate = AwgcontrolRstate(device, f"{self._cmd_syntax}:RSTate")
        self._run = AwgcontrolRun(device, f"{self._cmd_syntax}:RUN")
        self._sequencer = AwgcontrolSequencer(device, f"{self._cmd_syntax}:SEQuencer")
        self._sname = AwgcontrolSname(device, f"{self._cmd_syntax}:SNAMe")
        self._srestore = AwgcontrolSrestore(device, f"{self._cmd_syntax}:SREStore")
        self._ssave = AwgcontrolSsave(device, f"{self._cmd_syntax}:SSAVe")
        self._stop = AwgcontrolStop(device, f"{self._cmd_syntax}:STOP")

    @property
    def application(self) -> AwgcontrolApplication:
        """Return the ``AWGControl:APPLication`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:APPLication?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:APPLication?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.run``: The ``AWGControl:APPLication:RUN`` command.
            - ``.state``: The ``AWGControl:APPLication:STATe`` command.
        """
        return self._application

    @property
    def clock(self) -> AwgcontrolClock:
        """Return the ``AWGControl:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:CLOCk?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.drate``: The ``AWGControl:CLOCk:DRATe`` command.
            - ``.phase``: The ``AWGControl:CLOCk:PHASe`` command tree.
            - ``.source``: The ``AWGControl:CLOCk:SOURce`` command.
        """
        return self._clock

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
    def dc(self) -> Dict[int, AwgcontrolDcItem]:
        """Return the ``AWGControl:DC[n]`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:DC[n]?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:DC[n]?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.voltage``: The ``AWGControl:DC[n]:VOLTage`` command tree.
            - ``.state``: The ``AWGControl:DC[n]:STATe`` command.
        """
        return self._dc

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
    def enhanced(self) -> AwgcontrolEnhanced:
        """Return the ``AWGControl:ENHanced`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:ENHanced?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:ENHanced?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.sequence``: The ``AWGControl:ENHanced:SEQuence`` command tree.
        """
        return self._enhanced

    @property
    def event(self) -> AwgcontrolEvent:
        """Return the ``AWGControl:EVENt`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:EVENt?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:EVENt?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.djump``: The ``AWGControl:EVENt:DJUMp`` command tree.
            - ``.jmode``: The ``AWGControl:EVENt:JMODe`` command.
            - ``.software``: The ``AWGControl:EVENt:SOFTware`` command tree.
            - ``.table``: The ``AWGControl:EVENt:TABLe`` command tree.
        """
        return self._event

    @property
    def interleave(self) -> AwgcontrolInterleave:
        """Return the ``AWGControl:INTerleave`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:INTerleave?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:INTerleave?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.adjustment``: The ``AWGControl:INTerleave:ADJustment`` command tree.
            - ``.zeroing``: The ``AWGControl:INTerleave:ZERoing`` command.
            - ``.state``: The ``AWGControl:INTerleave:STATe`` command.
        """
        return self._interleave

    @property
    def rmode(self) -> AwgcontrolRmode:
        """Return the ``AWGControl:RMODe`` command.

        Description:
            - This command and query sets or returns the run mode of the arbitrary waveform
              generator.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:RMODe?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:RMODe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AWGControl:RMODe value`` command.

        SCPI Syntax:
            ```
            - AWGControl:RMODe {CONTinuous|TRIGgered|GATed|SEQuence|ENHanced}
            - AWGControl:RMODe?
            ```

        Info:
            - ``CONTinuous`` sets Run Mode to Continuous.
            - ``TRIGgered`` sets Run Mode to Triggered.
            - ``GATed`` sets Run Mode to Gated.
            - ``SEQuence`` sets Run Mode to Sequence.
            - ``ENHanced`` is provided only for the compatibility with AWG400/500/600/700 series. In
              the response, SEQ is returned even if ENH is specified in the command.
            - ``CONTinuous``
        """
        return self._rmode

    @property
    def rrate(self) -> AwgcontrolRrate:
        """Return the ``AWGControl:RRATe`` command.

        Description:
            - This command and query sets or returns the repetition rate of the arbitrary waveform
              generator.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:RRATe?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:RRATe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AWGControl:RRATe value`` command.

        SCPI Syntax:
            ```
            - AWGControl:RRATe <repetition_rate>
            - AWGControl:RRATe?
            ```

        Info:
            - ``<repetition_rate>`` ::=<NR3>.

        Sub-properties:
            - ``.hold``: The ``AWGControl:RRATe:HOLD`` command.
        """
        return self._rrate

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
    def sequencer(self) -> AwgcontrolSequencer:
        """Return the ``AWGControl:SEQuencer`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl:SEQuencer?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl:SEQuencer?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``AWGControl:SEQuencer:POSition`` command.
            - ``.type``: The ``AWGControl:SEQuencer:TYPE`` command.
        """
        return self._sequencer

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
            - This command restores the arbitrary waveform generator's setting from a specified
              settings file. The drive may be a local or a network drive. If the full path is not
              specified, the file will be stored in the current path.

        Usage:
            - Using the ``.write(value)`` method will send the ``AWGControl:SREStore value``
              command.

        SCPI Syntax:
            ```
            - AWGControl:SREStore <file_name>[,<msus>]
            ```

        Info:
            - ``<file_name>`` ::=<string>.
            - ``<msus>`` (mass storage unit specifier)::=<string>.
        """
        return self._srestore

    @property
    def ssave(self) -> AwgcontrolSsave:
        """Return the ``AWGControl:SSAVe`` command.

        Description:
            - This command saves the arbitrary waveform generator's setting to a specified settings
              file. The drive may be a local or a network drive. If full path is not specified, the
              file will be stored in the current path.

        Usage:
            - Using the ``.write(value)`` method will send the ``AWGControl:SSAVe value`` command.

        SCPI Syntax:
            ```
            - AWGControl:SSAVe <file_name>[,<msus>]
            ```

        Info:
            - ``<file_name>`` ::=<string>.
            - ``<msus>`` (mass storage unit specifier)::=<string>.
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
