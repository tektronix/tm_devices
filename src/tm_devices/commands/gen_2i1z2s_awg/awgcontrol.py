"""The awgcontrol commands module.

These commands are used in the following models:
AWG5200

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - AWGControl:ARSettings {0|1|ON|OFF}
    - AWGControl:CLOCk:DRATe <NR1>
    - AWGControl:CLOCk:DRATe?
    - AWGControl:CLOCk:PHASe:ADJust <NR1>
    - AWGControl:CLOCk:PHASe:ADJust?
    - AWGControl:CLOCk:SOURce {INTernal|EXTernal|EFIXed|EVARiable}
    - AWGControl:CLOCk:SOURce?
    - AWGControl:COMPile <filename>
    - AWGControl:CONFigure:CNUMber?
    - AWGControl:PJUMp:JSTRobe {0|1|OFF|ON}
    - AWGControl:PJUMp:JSTRobe?
    - AWGControl:PJUMp:SEDGe {FALLing|RISing}
    - AWGControl:PJUMp:SEDGe?
    - AWGControl:RMODe {CONTinuous|TRIGgered|GATed}
    - AWGControl:RMODe?
    - AWGControl:RSTate?
    - AWGControl:RUN:IMMediate
    - AWGControl:SNAMe?
    - AWGControl:SREStore <filepath>[,<msus>]
    - AWGControl:SSAVe <filepath>[,<msus>]
    - AWGControl:STOP:IMMediate
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

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
        - AWGControl:RMODe {CONTinuous|TRIGgered|GATed}
        - AWGControl:RMODe?
        ```

    Info:
        - ``CONTinuous`` sets the Run Mode to Continuous (not waiting for a trigger event).
          TRIGgered sets the Run Mode to Triggered, waiting for a trigger event. One waveform play
          out cycle completes, then play out stops, waiting for the next trigger event. GATed sets
          the Run Mode to only playout a waveform while the trigger is enabled.
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


class AwgcontrolArsettings(SCPICmdWrite):
    """The ``AWGControl:ARSettings`` command.

    Description:
        - This command sets or returns the state (enabled or disabled) of whether or not to apply
          the recommended settings of waveforms and sequences when they are assigned to a channel.
          When enabled, the system attempts to use the waveform's recommended settings (sample rate,
          amplitude, and offset) when the waveform is assigned to a channel. This includes waveforms
          within sequence tracks assigned to a channel. Recommended settings are defined as part the
          waveform properties and sequence properties.

    Usage:
        - Using the ``.write(value)`` method will send the ``AWGControl:ARSettings value`` command.

    SCPI Syntax:
        ```
        - AWGControl:ARSettings {0|1|ON|OFF}
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
        - ``.pjump``: The ``AWGControl:PJUMp`` command tree.
        - ``.rmode``: The ``AWGControl:RMODe`` command.
        - ``.rstate``: The ``AWGControl:RSTate`` command.
        - ``.run``: The ``AWGControl:RUN`` command tree.
        - ``.sname``: The ``AWGControl:SNAMe`` command.
        - ``.srestore``: The ``AWGControl:SREStore`` command.
        - ``.ssave``: The ``AWGControl:SSAVe`` command.
        - ``.stop``: The ``AWGControl:STOP`` command tree.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "AWGControl"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._arsettings = AwgcontrolArsettings(device, f"{self._cmd_syntax}:ARSettings")
        self._compile = AwgcontrolCompile(device, f"{self._cmd_syntax}:COMPile")
        self._configure = AwgcontrolConfigure(device, f"{self._cmd_syntax}:CONFigure")
        self._pjump = AwgcontrolPjump(device, f"{self._cmd_syntax}:PJUMp")
        self._rmode = AwgcontrolRmode(device, f"{self._cmd_syntax}:RMODe")
        self._rstate = AwgcontrolRstate(device, f"{self._cmd_syntax}:RSTate")
        self._run = AwgcontrolRun(device, f"{self._cmd_syntax}:RUN")
        self._sname = AwgcontrolSname(device, f"{self._cmd_syntax}:SNAMe")
        self._srestore = AwgcontrolSrestore(device, f"{self._cmd_syntax}:SREStore")
        self._ssave = AwgcontrolSsave(device, f"{self._cmd_syntax}:SSAVe")
        self._stop = AwgcontrolStop(device, f"{self._cmd_syntax}:STOP")
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
            - Using the ``.write(value)`` method will send the ``AWGControl:ARSettings value``
              command.

        SCPI Syntax:
            ```
            - AWGControl:ARSettings {0|1|ON|OFF}
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
            - AWGControl:RMODe {CONTinuous|TRIGgered|GATed}
            - AWGControl:RMODe?
            ```

        Info:
            - ``CONTinuous`` sets the Run Mode to Continuous (not waiting for a trigger event).
              TRIGgered sets the Run Mode to Triggered, waiting for a trigger event. One waveform
              play out cycle completes, then play out stops, waiting for the next trigger event.
              GATed sets the Run Mode to only playout a waveform while the trigger is enabled.
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
