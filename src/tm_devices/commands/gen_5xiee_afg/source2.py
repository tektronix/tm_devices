# pylint: disable=line-too-long
"""The source2 commands module.

These commands are used in the following models:
AFG3K, AFG3KB, AFG3KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SOURce2:AM:DEPTh {<depth>|MINimum|MAXimum}
    - SOURce2:AM:DEPTh?
    - SOURce2:AM:INTernal:FREQuency {<frequency>|MINimum|MAXimum}
    - SOURce2:AM:INTernal:FREQuency?
    - SOURce2:AM:INTernal:FUNCtion {SINusoid|SQUare|TRIangle|RAMP|NRAMp|PRNoise|USER[1]|USER<x>|EMEMory[1]|EMEMory2|EFILe}
    - SOURce2:AM:INTernal:FUNCtion:EFILe <file_name>
    - SOURce2:AM:INTernal:FUNCtion:EFILe?
    - SOURce2:AM:INTernal:FUNCtion?
    - SOURce2:AM:SOURce [INTernal|EXTernal]
    - SOURce2:AM:SOURce?
    - SOURce2:AM:STATe {ON|OFF|<NR1>}
    - SOURce2:AM:STATe?
    - SOURce2:BURSt:MODE {TRIGgered|GATed}
    - SOURce2:BURSt:MODE?
    - SOURce2:BURSt:NCYCles {<cycles>|INFinity|MINimum|MAXimum}
    - SOURce2:BURSt:NCYCles?
    - SOURce2:BURSt:STATe {ON|OFF|<NR1>}
    - SOURce2:BURSt:STATe?
    - SOURce2:BURSt:TDELay {<delay>|MINimum|MAXimum}
    - SOURce2:BURSt:TDELay?
    - SOURce2:COMBine:FEED ['NOISe'|'EXTernal'|'BOTH'|'']
    - SOURce2:COMBine:FEED?
    - SOURce2:FM:DEViation {<deviation>|MINimum|MAXimum}
    - SOURce2:FM:DEViation?
    - SOURce2:FM:INTernal:FREQuency {<frequency>|MINimum|MAXimum}
    - SOURce2:FM:INTernal:FREQuency?
    - SOURce2:FM:INTernal:FUNCtion {SINusoid|SQUare|TRIangle|RAMP|NRAMp|PRNoise|USER[1]|USER<x>|EMEMory[1]|EMEMory2|EFILe}
    - SOURce2:FM:INTernal:FUNCtion:EFILe <file_name>
    - SOURce2:FM:INTernal:FUNCtion:EFILe?
    - SOURce2:FM:INTernal:FUNCtion?
    - SOURce2:FM:SOURce [INTernal|EXTernal]
    - SOURce2:FM:SOURce?
    - SOURce2:FM:STATe {ON|OFF|<NR1>}
    - SOURce2:FM:STATe?
    - SOURce2:FREQuency:CENTer {<frequency>|MINimum|MAXimum}
    - SOURce2:FREQuency:CENTer?
    - SOURce2:FREQuency:CONCurrent:STATe {ON|OFF|<NR1>}
    - SOURce2:FREQuency:CONCurrent:STATe?
    - SOURce2:FREQuency:CW {<frequency>|MINimum|MAXimum}
    - SOURce2:FREQuency:CW?
    - SOURce2:FREQuency:FIXed {<frequency>|MINimum|MAXimum}
    - SOURce2:FREQuency:FIXed?
    - SOURce2:FREQuency:MODE {CW|FIXed|SWEep}
    - SOURce2:FREQuency:MODE?
    - SOURce2:FREQuency:SPAN {<frequency>|MINimum|MAXimum}
    - SOURce2:FREQuency:STARt {<frequency>|MINimum|MAXimum}
    - SOURce2:FREQuency:STARt?
    - SOURce2:FREQuency:STOP {<frequency>|MINimum|MAXimum}
    - SOURce2:FREQuency:STOP?
    - SOURce2:FSKey:FREQuency {<frequency>|MINimum|MAXimum}
    - SOURce2:FSKey:FREQuency?
    - SOURce2:FSKey:INTernal:RATE {<rate>|MINimum|MAXimum}
    - SOURce2:FSKey:INTernal:RATE?
    - SOURce2:FSKey:SOURce [INTernal|EXTernal]
    - SOURce2:FSKey:SOURce?
    - SOURce2:FSKey:STATe {ON|OFF|<NR1>}
    - SOURce2:FSKey:STATe?
    - SOURce2:FUNCtion:EFILe <file_name>
    - SOURce2:FUNCtion:EFILe?
    - SOURce2:FUNCtion:RAMP:SYMMetry {<symmetry>|MINimum|MAXimum}
    - SOURce2:FUNCtion:RAMP:SYMMetry?
    - SOURce2:FUNCtion:SHAPe {SINusoid|SQUare|PULSe|RAMP|PRNoise|DC|SINC|GAUSsian|LORentz|ERISe|EDECay|HAVersine|USER[1]|USER<x>|EMEMory[1]|EMEMory2|EFILe}
    - SOURce2:FUNCtion:SHAPe?
    - SOURce2:PHASe:ADJust {<phase>|MINimum|MAXimum}
    - SOURce2:PHASe:ADJust?
    - SOURce2:PHASe:INITiate
    - SOURce2:PM:DEViation {<deviation>|MINimum|MAXimum}
    - SOURce2:PM:DEViation?
    - SOURce2:PM:INTernal:FREQuency {<frequency>|MINimum|MAXimum}
    - SOURce2:PM:INTernal:FREQuency?
    - SOURce2:PM:INTernal:FUNCtion {SINusoid|SQUare|TRIangle|RAMP|NRAMp|PRNoise|USER[1]|USER<x>|EMEMory[1]|EMEMory2|EFILe}
    - SOURce2:PM:INTernal:FUNCtion:EFILe <file_name>
    - SOURce2:PM:INTernal:FUNCtion:EFILe?
    - SOURce2:PM:INTernal:FUNCtion?
    - SOURce2:PM:SOURce [INTernal|EXTernal]
    - SOURce2:PM:SOURce?
    - SOURce2:PM:STATe {ON|OFF|<NR1>}
    - SOURce2:PM:STATe?
    - SOURce2:PULSe:DCYCle {<percent>|MINimum|MAXimum}
    - SOURce2:PULSe:DCYCle?
    - SOURce2:PULSe:DELay {<delay>|MINimum|MAXimum}
    - SOURce2:PULSe:DELay?
    - SOURce2:PULSe:HOLD {WIDTh|DUTY}
    - SOURce2:PULSe:HOLD?
    - SOURce2:PULSe:PERiod {<period>|MINimum|MAXimum}
    - SOURce2:PULSe:PERiod?
    - SOURce2:PULSe:TRANsition:LEADing {<seconds>|MINimum|MAXimum}
    - SOURce2:PULSe:TRANsition:LEADing?
    - SOURce2:PULSe:TRANsition:TRAiling {<seconds>|MINimum|MAXimum}
    - SOURce2:PULSe:TRANsition:TRAiling?
    - SOURce2:PULSe:WIDTh {<seconds>|MINimum|MAXimum}
    - SOURce2:PULSe:WIDTh?
    - SOURce2:PWM:DEViation:DCYCle {<percent>|MINimum|MAXimum}
    - SOURce2:PWM:DEViation:DCYCle?
    - SOURce2:PWM:INTernal:FREQuency {<frequency>|MINimum|MAXimum}
    - SOURce2:PWM:INTernal:FREQuency?
    - SOURce2:PWM:INTernal:FUNCtion {SINusoid|SQUare|TRIangle|RAMP|NRAMp|PRNoise|USER[1]|USER<x>|EMEMory[1]|EMEMory2|EFILe}
    - SOURce2:PWM:INTernal:FUNCtion:EFILe <file_name>
    - SOURce2:PWM:INTernal:FUNCtion:EFILe?
    - SOURce2:PWM:INTernal:FUNCtion?
    - SOURce2:PWM:SOURce [INTernal|EXTernal]
    - SOURce2:PWM:SOURce?
    - SOURce2:PWM:STATe {ON|OFF|<NR1>}
    - SOURce2:PWM:STATe?
    - SOURce2:SWEep:HTIMe {<seconds>|MINimum|MAXimum}
    - SOURce2:SWEep:HTIMe?
    - SOURce2:SWEep:MODE {AUTO|MANual}
    - SOURce2:SWEep:MODE?
    - SOURce2:SWEep:RTIMe {<seconds>|MINimum|MAXimum}
    - SOURce2:SWEep:RTIMe?
    - SOURce2:SWEep:SPACing {LINear|LOGarithmic}
    - SOURce2:SWEep:SPACing?
    - SOURce2:SWEep:TIME {<seconds>|MINimum|MAXimum}
    - SOURce2:SWEep:TIME?
    - SOURce2:VOLTage:CONCurrent:STATe {ON|OFF|<NR1>}
    - SOURce2:VOLTage:CONCurrent:STATe?
    - SOURce2:VOLTage:LEVel:IMMediate:AMPLitude {<amplitude>|MINimum|MAXimum}
    - SOURce2:VOLTage:LEVel:IMMediate:AMPLitude?
    - SOURce2:VOLTage:LEVel:IMMediate:HIGH {<voltage>|MINimum|MAXimum}
    - SOURce2:VOLTage:LEVel:IMMediate:HIGH?
    - SOURce2:VOLTage:LEVel:IMMediate:LOW {<voltage>|MINimum|MAXimum}
    - SOURce2:VOLTage:LEVel:IMMediate:LOW?
    - SOURce2:VOLTage:LEVel:IMMediate:OFFSet {<voltage>|MINimum|MAXimum}
    - SOURce2:VOLTage:LEVel:IMMediate:OFFSet?
    - SOURce2:VOLTage:LIMit:HIGH {<voltage>|MINimum|MAXimum}
    - SOURce2:VOLTage:LIMit:HIGH?
    - SOURce2:VOLTage:LIMit:LOW {<voltage>|MINimum|MAXimum}
    - SOURce2:VOLTage:LIMit:LOW?
    - SOURce2:VOLTage:UNIT {VPP|VRMS|DBM}
    - SOURce2:VOLTage:UNIT?
    ```
"""  # noqa: E501

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Source2VoltageUnit(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:VOLTage:UNIT`` command.

    Description:
        - This command sets or queries the units of output amplitude for the specified channel. This
          command does not affect the offset, High level, or Low level of output. The setting of
          this command is not affected by the units setting of
          [SOURce[1|2]]``:VOLTage``[``:LEVel``][``:IMMediate``][``:AMPLitude``] command. V rms = × V
          pp 2 sin dBm = 10 × log P 0.001 P = V 2 rms R L R L load impedance V rms = V pp 2 3
          triangle If your instrument is a dual-channel model and the
          [SOURce[1|2]]``:VOLTage:CONCurrent``[``:STATe``] command is set to ON, then the units of
          the other channel are set the same.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:VOLTage:UNIT?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:VOLTage:UNIT?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:VOLTage:UNIT value`` command.

    SCPI Syntax:
        ```
        - SOURce2:VOLTage:UNIT {VPP|VRMS|DBM}
        - SOURce2:VOLTage:UNIT?
        ```
    """


class Source2VoltageLimitLow(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:VOLTage:LIMit:LOW`` command.

    Description:
        - This command sets or queries the lower limit of the output amplitude low level for the
          specified channel. If your instrument is a dual-channel model and the
          [SOURce[1|2]]``:VOLTage:CONCurrent``[``:STATe``] command is set to ON, then the low level
          lower limit of the other channel is the same value.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:VOLTage:LIMit:LOW?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:VOLTage:LIMit:LOW?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:VOLTage:LIMit:LOW value``
          command.

    SCPI Syntax:
        ```
        - SOURce2:VOLTage:LIMit:LOW {<voltage>|MINimum|MAXimum}
        - SOURce2:VOLTage:LIMit:LOW?
        ```
    """


class Source2VoltageLimitHigh(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:VOLTage:LIMit:HIGH`` command.

    Description:
        - This command sets or queries the higher limit of the output amplitude high level for the
          specified channel. If your instrument is a dual-channel model and the
          [SOURce[1|2]]``:VOLTage:CONCurrent``[``:STATe``] command is set to ON, then the higher
          level limit of the other channel is the same value.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:VOLTage:LIMit:HIGH?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:VOLTage:LIMit:HIGH?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:VOLTage:LIMit:HIGH value``
          command.

    SCPI Syntax:
        ```
        - SOURce2:VOLTage:LIMit:HIGH {<voltage>|MINimum|MAXimum}
        - SOURce2:VOLTage:LIMit:HIGH?
        ```
    """


class Source2VoltageLimit(SCPICmdRead):
    """The ``SOURce2:VOLTage:LIMit`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:VOLTage:LIMit?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:VOLTage:LIMit?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.high``: The ``SOURce2:VOLTage:LIMit:HIGH`` command.
        - ``.low``: The ``SOURce2:VOLTage:LIMit:LOW`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._high = Source2VoltageLimitHigh(device, f"{self._cmd_syntax}:HIGH")
        self._low = Source2VoltageLimitLow(device, f"{self._cmd_syntax}:LOW")

    @property
    def high(self) -> Source2VoltageLimitHigh:
        """Return the ``SOURce2:VOLTage:LIMit:HIGH`` command.

        Description:
            - This command sets or queries the higher limit of the output amplitude high level for
              the specified channel. If your instrument is a dual-channel model and the
              [SOURce[1|2]]``:VOLTage:CONCurrent``[``:STATe``] command is set to ON, then the higher
              level limit of the other channel is the same value.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:VOLTage:LIMit:HIGH?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:VOLTage:LIMit:HIGH?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:VOLTage:LIMit:HIGH value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:VOLTage:LIMit:HIGH {<voltage>|MINimum|MAXimum}
            - SOURce2:VOLTage:LIMit:HIGH?
            ```
        """
        return self._high

    @property
    def low(self) -> Source2VoltageLimitLow:
        """Return the ``SOURce2:VOLTage:LIMit:LOW`` command.

        Description:
            - This command sets or queries the lower limit of the output amplitude low level for the
              specified channel. If your instrument is a dual-channel model and the
              [SOURce[1|2]]``:VOLTage:CONCurrent``[``:STATe``] command is set to ON, then the low
              level lower limit of the other channel is the same value.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:VOLTage:LIMit:LOW?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:VOLTage:LIMit:LOW?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:VOLTage:LIMit:LOW value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:VOLTage:LIMit:LOW {<voltage>|MINimum|MAXimum}
            - SOURce2:VOLTage:LIMit:LOW?
            ```
        """
        return self._low


class Source2VoltageLevelImmediateOffset(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:VOLTage:LEVel:IMMediate:OFFSet`` command.

    Description:
        - This command sets or queries the offset level for the specified channel. If your
          instrument is a dual-channel model and the
          [SOURce[1|2]]``:VOLTage:CONCurrent``[``:STATe``] command is set to ON, then the offset
          level of the other channel is also the same value.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:VOLTage:LEVel:IMMediate:OFFSet?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce2:VOLTage:LEVel:IMMediate:OFFSet?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce2:VOLTage:LEVel:IMMediate:OFFSet value`` command.

    SCPI Syntax:
        ```
        - SOURce2:VOLTage:LEVel:IMMediate:OFFSet {<voltage>|MINimum|MAXimum}
        - SOURce2:VOLTage:LEVel:IMMediate:OFFSet?
        ```
    """


class Source2VoltageLevelImmediateLow(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:VOLTage:LEVel:IMMediate:LOW`` command.

    Description:
        - This command sets or queries the low level of output amplitude for the specified channel.
          If your instrument is a dual-channel model and the
          [SOURce[1|2]]``:VOLTage:CONCurrent``[``:STATe``] command is set to ON, then the low level
          of other channel is also the same value.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:VOLTage:LEVel:IMMediate:LOW?``
          query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:VOLTage:LEVel:IMMediate:LOW?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce2:VOLTage:LEVel:IMMediate:LOW value`` command.

    SCPI Syntax:
        ```
        - SOURce2:VOLTage:LEVel:IMMediate:LOW {<voltage>|MINimum|MAXimum}
        - SOURce2:VOLTage:LEVel:IMMediate:LOW?
        ```
    """


class Source2VoltageLevelImmediateHigh(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:VOLTage:LEVel:IMMediate:HIGH`` command.

    Description:
        - This command sets or queries the high level of output amplitude for the specified channel.
          If your instrument is a dual-channel model and the
          [SOURce[1|2]]``:VOLTage:CONCurrent``[``:STATe``] command is set to ON, then the high level
          of other channel is also the same value.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:VOLTage:LEVel:IMMediate:HIGH?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce2:VOLTage:LEVel:IMMediate:HIGH?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce2:VOLTage:LEVel:IMMediate:HIGH value`` command.

    SCPI Syntax:
        ```
        - SOURce2:VOLTage:LEVel:IMMediate:HIGH {<voltage>|MINimum|MAXimum}
        - SOURce2:VOLTage:LEVel:IMMediate:HIGH?
        ```
    """


class Source2VoltageLevelImmediateAmplitude(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:VOLTage:LEVel:IMMediate:AMPLitude`` command.

    Description:
        - This command sets or queries the output amplitude for the specified channel. Units
          Amplitude resolution VPP 0.1 mVp-p or four digits VRMS 0.1 mVrms or four digits DBM 0.1
          dBm You can set the units of output amplitude by using either the bezel menu selection or
          the [SOURce[1|2]]``:VOLTage:UNIT`` command. The selection by bezel menu has priority over
          the remote command.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:VOLTage:LEVel:IMMediate:AMPLitude?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce2:VOLTage:LEVel:IMMediate:AMPLitude?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce2:VOLTage:LEVel:IMMediate:AMPLitude value`` command.

    SCPI Syntax:
        ```
        - SOURce2:VOLTage:LEVel:IMMediate:AMPLitude {<amplitude>|MINimum|MAXimum}
        - SOURce2:VOLTage:LEVel:IMMediate:AMPLitude?
        ```
    """


class Source2VoltageLevelImmediate(SCPICmdRead):
    """The ``SOURce2:VOLTage:LEVel:IMMediate`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:VOLTage:LEVel:IMMediate?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:VOLTage:LEVel:IMMediate?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.high``: The ``SOURce2:VOLTage:LEVel:IMMediate:HIGH`` command.
        - ``.low``: The ``SOURce2:VOLTage:LEVel:IMMediate:LOW`` command.
        - ``.offset``: The ``SOURce2:VOLTage:LEVel:IMMediate:OFFSet`` command.
        - ``.amplitude``: The ``SOURce2:VOLTage:LEVel:IMMediate:AMPLitude`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._high = Source2VoltageLevelImmediateHigh(device, f"{self._cmd_syntax}:HIGH")
        self._low = Source2VoltageLevelImmediateLow(device, f"{self._cmd_syntax}:LOW")
        self._offset = Source2VoltageLevelImmediateOffset(device, f"{self._cmd_syntax}:OFFSet")
        self._amplitude = Source2VoltageLevelImmediateAmplitude(
            device, f"{self._cmd_syntax}:AMPLitude"
        )

    @property
    def high(self) -> Source2VoltageLevelImmediateHigh:
        """Return the ``SOURce2:VOLTage:LEVel:IMMediate:HIGH`` command.

        Description:
            - This command sets or queries the high level of output amplitude for the specified
              channel. If your instrument is a dual-channel model and the
              [SOURce[1|2]]``:VOLTage:CONCurrent``[``:STATe``] command is set to ON, then the high
              level of other channel is also the same value.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:VOLTage:LEVel:IMMediate:HIGH?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce2:VOLTage:LEVel:IMMediate:HIGH?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce2:VOLTage:LEVel:IMMediate:HIGH value`` command.

        SCPI Syntax:
            ```
            - SOURce2:VOLTage:LEVel:IMMediate:HIGH {<voltage>|MINimum|MAXimum}
            - SOURce2:VOLTage:LEVel:IMMediate:HIGH?
            ```
        """
        return self._high

    @property
    def low(self) -> Source2VoltageLevelImmediateLow:
        """Return the ``SOURce2:VOLTage:LEVel:IMMediate:LOW`` command.

        Description:
            - This command sets or queries the low level of output amplitude for the specified
              channel. If your instrument is a dual-channel model and the
              [SOURce[1|2]]``:VOLTage:CONCurrent``[``:STATe``] command is set to ON, then the low
              level of other channel is also the same value.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:VOLTage:LEVel:IMMediate:LOW?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce2:VOLTage:LEVel:IMMediate:LOW?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce2:VOLTage:LEVel:IMMediate:LOW value`` command.

        SCPI Syntax:
            ```
            - SOURce2:VOLTage:LEVel:IMMediate:LOW {<voltage>|MINimum|MAXimum}
            - SOURce2:VOLTage:LEVel:IMMediate:LOW?
            ```
        """
        return self._low

    @property
    def offset(self) -> Source2VoltageLevelImmediateOffset:
        """Return the ``SOURce2:VOLTage:LEVel:IMMediate:OFFSet`` command.

        Description:
            - This command sets or queries the offset level for the specified channel. If your
              instrument is a dual-channel model and the
              [SOURce[1|2]]``:VOLTage:CONCurrent``[``:STATe``] command is set to ON, then the offset
              level of the other channel is also the same value.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce2:VOLTage:LEVel:IMMediate:OFFSet?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce2:VOLTage:LEVel:IMMediate:OFFSet?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce2:VOLTage:LEVel:IMMediate:OFFSet value`` command.

        SCPI Syntax:
            ```
            - SOURce2:VOLTage:LEVel:IMMediate:OFFSet {<voltage>|MINimum|MAXimum}
            - SOURce2:VOLTage:LEVel:IMMediate:OFFSet?
            ```
        """
        return self._offset

    @property
    def amplitude(self) -> Source2VoltageLevelImmediateAmplitude:
        """Return the ``SOURce2:VOLTage:LEVel:IMMediate:AMPLitude`` command.

        Description:
            - This command sets or queries the output amplitude for the specified channel. Units
              Amplitude resolution VPP 0.1 mVp-p or four digits VRMS 0.1 mVrms or four digits DBM
              0.1 dBm You can set the units of output amplitude by using either the bezel menu
              selection or the [SOURce[1|2]]``:VOLTage:UNIT`` command. The selection by bezel menu
              has priority over the remote command.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce2:VOLTage:LEVel:IMMediate:AMPLitude?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce2:VOLTage:LEVel:IMMediate:AMPLitude?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce2:VOLTage:LEVel:IMMediate:AMPLitude value`` command.

        SCPI Syntax:
            ```
            - SOURce2:VOLTage:LEVel:IMMediate:AMPLitude {<amplitude>|MINimum|MAXimum}
            - SOURce2:VOLTage:LEVel:IMMediate:AMPLitude?
            ```
        """
        return self._amplitude


class Source2VoltageLevel(SCPICmdRead):
    """The ``SOURce2:VOLTage:LEVel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:VOLTage:LEVel?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:VOLTage:LEVel?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.immediate``: The ``SOURce2:VOLTage:LEVel:IMMediate`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._immediate = Source2VoltageLevelImmediate(device, f"{self._cmd_syntax}:IMMediate")

    @property
    def immediate(self) -> Source2VoltageLevelImmediate:
        """Return the ``SOURce2:VOLTage:LEVel:IMMediate`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:VOLTage:LEVel:IMMediate?``
              query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:VOLTage:LEVel:IMMediate?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.high``: The ``SOURce2:VOLTage:LEVel:IMMediate:HIGH`` command.
            - ``.low``: The ``SOURce2:VOLTage:LEVel:IMMediate:LOW`` command.
            - ``.offset``: The ``SOURce2:VOLTage:LEVel:IMMediate:OFFSet`` command.
            - ``.amplitude``: The ``SOURce2:VOLTage:LEVel:IMMediate:AMPLitude`` command.
        """
        return self._immediate


class Source2VoltageConcurrentState(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:VOLTage:CONCurrent:STATe`` command.

    Description:
        - This command enables or disables the function to copy the voltage level of one channel to
          another channel. The[SOURce[1|2]]``:VOLTage:CONCurrent``[``:STATe``] command copies the
          voltage level of the channel specified by the header suffix to another channel. If you
          specify CH 1 with the header, the CH 1 voltage level will be copied to CH 2. The query
          command returns '0' (off) or '1' (on). If your arbitrary function generator is a
          single-channel model, this command is not supported.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:VOLTage:CONCurrent:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:VOLTage:CONCurrent:STATe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce2:VOLTage:CONCurrent:STATe value`` command.

    SCPI Syntax:
        ```
        - SOURce2:VOLTage:CONCurrent:STATe {ON|OFF|<NR1>}
        - SOURce2:VOLTage:CONCurrent:STATe?
        ```
    """


class Source2VoltageConcurrent(SCPICmdRead):
    """The ``SOURce2:VOLTage:CONCurrent`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:VOLTage:CONCurrent?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:VOLTage:CONCurrent?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``SOURce2:VOLTage:CONCurrent:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = Source2VoltageConcurrentState(device, f"{self._cmd_syntax}:STATe")

    @property
    def state(self) -> Source2VoltageConcurrentState:
        """Return the ``SOURce2:VOLTage:CONCurrent:STATe`` command.

        Description:
            - This command enables or disables the function to copy the voltage level of one channel
              to another channel. The[SOURce[1|2]]``:VOLTage:CONCurrent``[``:STATe``] command copies
              the voltage level of the channel specified by the header suffix to another channel. If
              you specify CH 1 with the header, the CH 1 voltage level will be copied to CH 2. The
              query command returns '0' (off) or '1' (on). If your arbitrary function generator is a
              single-channel model, this command is not supported.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:VOLTage:CONCurrent:STATe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce2:VOLTage:CONCurrent:STATe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce2:VOLTage:CONCurrent:STATe value`` command.

        SCPI Syntax:
            ```
            - SOURce2:VOLTage:CONCurrent:STATe {ON|OFF|<NR1>}
            - SOURce2:VOLTage:CONCurrent:STATe?
            ```
        """
        return self._state


class Source2Voltage(SCPICmdRead):
    """The ``SOURce2:VOLTage`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:VOLTage?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:VOLTage?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.concurrent``: The ``SOURce2:VOLTage:CONCurrent`` command tree.
        - ``.limit``: The ``SOURce2:VOLTage:LIMit`` command tree.
        - ``.unit``: The ``SOURce2:VOLTage:UNIT`` command.
        - ``.level``: The ``SOURce2:VOLTage:LEVel`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._concurrent = Source2VoltageConcurrent(device, f"{self._cmd_syntax}:CONCurrent")
        self._limit = Source2VoltageLimit(device, f"{self._cmd_syntax}:LIMit")
        self._unit = Source2VoltageUnit(device, f"{self._cmd_syntax}:UNIT")
        self._level = Source2VoltageLevel(device, f"{self._cmd_syntax}:LEVel")

    @property
    def concurrent(self) -> Source2VoltageConcurrent:
        """Return the ``SOURce2:VOLTage:CONCurrent`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:VOLTage:CONCurrent?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:VOLTage:CONCurrent?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``SOURce2:VOLTage:CONCurrent:STATe`` command.
        """
        return self._concurrent

    @property
    def limit(self) -> Source2VoltageLimit:
        """Return the ``SOURce2:VOLTage:LIMit`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:VOLTage:LIMit?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:VOLTage:LIMit?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.high``: The ``SOURce2:VOLTage:LIMit:HIGH`` command.
            - ``.low``: The ``SOURce2:VOLTage:LIMit:LOW`` command.
        """
        return self._limit

    @property
    def unit(self) -> Source2VoltageUnit:
        """Return the ``SOURce2:VOLTage:UNIT`` command.

        Description:
            - This command sets or queries the units of output amplitude for the specified channel.
              This command does not affect the offset, High level, or Low level of output. The
              setting of this command is not affected by the units setting of
              [SOURce[1|2]]``:VOLTage``[``:LEVel``][``:IMMediate``][``:AMPLitude``] command. V rms =
              × V pp 2 sin dBm = 10 × log P 0.001 P = V 2 rms R L R L load impedance V rms = V pp 2
              3 triangle If your instrument is a dual-channel model and the
              [SOURce[1|2]]``:VOLTage:CONCurrent``[``:STATe``] command is set to ON, then the units
              of the other channel are set the same.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:VOLTage:UNIT?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:VOLTage:UNIT?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:VOLTage:UNIT value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:VOLTage:UNIT {VPP|VRMS|DBM}
            - SOURce2:VOLTage:UNIT?
            ```
        """
        return self._unit

    @property
    def level(self) -> Source2VoltageLevel:
        """Return the ``SOURce2:VOLTage:LEVel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:VOLTage:LEVel?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:VOLTage:LEVel?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.immediate``: The ``SOURce2:VOLTage:LEVel:IMMediate`` command tree.
        """
        return self._level


class Source2SweepTime(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:SWEep:TIME`` command.

    Description:
        - This command sets or queries the sweep time for the sweep for the specified channel. The
          sweep time does not include hold time and return time. The setting range is 1 ms to 300 s.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:SWEep:TIME?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:SWEep:TIME?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:SWEep:TIME value`` command.

    SCPI Syntax:
        ```
        - SOURce2:SWEep:TIME {<seconds>|MINimum|MAXimum}
        - SOURce2:SWEep:TIME?
        ```
    """


class Source2SweepSpacing(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:SWEep:SPACing`` command.

    Description:
        - The [SOURce[1|2]]``:SWEep:SPACing`` command selects linear or logarithmic spacing for the
          sweep for the specified channel. The query command returns the type for the sweep spacing
          for the specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:SWEep:SPACing?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:SWEep:SPACing?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:SWEep:SPACing value`` command.

    SCPI Syntax:
        ```
        - SOURce2:SWEep:SPACing {LINear|LOGarithmic}
        - SOURce2:SWEep:SPACing?
        ```
    """


class Source2SweepRtime(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:SWEep:RTIMe`` command.

    Description:
        - This command sets or queries the sweep return time. Return time represents the amount of
          time from stop frequency through start frequency. Return time does not include hold time.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:SWEep:RTIMe?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:SWEep:RTIMe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:SWEep:RTIMe value`` command.

    SCPI Syntax:
        ```
        - SOURce2:SWEep:RTIMe {<seconds>|MINimum|MAXimum}
        - SOURce2:SWEep:RTIMe?
        ```
    """


class Source2SweepMode(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:SWEep:MODE`` command.

    Description:
        - The [SOURce[1|2]]``:SWEep:MODE`` command selects auto or manual for the sweep mode for the
          specified channel. The query command returns the sweep mode for the specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:SWEep:MODE?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:SWEep:MODE?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:SWEep:MODE value`` command.

    SCPI Syntax:
        ```
        - SOURce2:SWEep:MODE {AUTO|MANual}
        - SOURce2:SWEep:MODE?
        ```
    """


class Source2SweepHtime(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:SWEep:HTIMe`` command.

    Description:
        - This command sets or queries the sweep hold time. Hold time represents the amount of time
          that the frequency must remain stable after reaching the stop frequency.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:SWEep:HTIMe?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:SWEep:HTIMe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:SWEep:HTIMe value`` command.

    SCPI Syntax:
        ```
        - SOURce2:SWEep:HTIMe {<seconds>|MINimum|MAXimum}
        - SOURce2:SWEep:HTIMe?
        ```
    """


class Source2Sweep(SCPICmdRead):
    """The ``SOURce2:SWEep`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:SWEep?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:SWEep?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.htime``: The ``SOURce2:SWEep:HTIMe`` command.
        - ``.mode``: The ``SOURce2:SWEep:MODE`` command.
        - ``.rtime``: The ``SOURce2:SWEep:RTIMe`` command.
        - ``.spacing``: The ``SOURce2:SWEep:SPACing`` command.
        - ``.time``: The ``SOURce2:SWEep:TIME`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._htime = Source2SweepHtime(device, f"{self._cmd_syntax}:HTIMe")
        self._mode = Source2SweepMode(device, f"{self._cmd_syntax}:MODE")
        self._rtime = Source2SweepRtime(device, f"{self._cmd_syntax}:RTIMe")
        self._spacing = Source2SweepSpacing(device, f"{self._cmd_syntax}:SPACing")
        self._time = Source2SweepTime(device, f"{self._cmd_syntax}:TIME")

    @property
    def htime(self) -> Source2SweepHtime:
        """Return the ``SOURce2:SWEep:HTIMe`` command.

        Description:
            - This command sets or queries the sweep hold time. Hold time represents the amount of
              time that the frequency must remain stable after reaching the stop frequency.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:SWEep:HTIMe?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:SWEep:HTIMe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:SWEep:HTIMe value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:SWEep:HTIMe {<seconds>|MINimum|MAXimum}
            - SOURce2:SWEep:HTIMe?
            ```
        """
        return self._htime

    @property
    def mode(self) -> Source2SweepMode:
        """Return the ``SOURce2:SWEep:MODE`` command.

        Description:
            - The [SOURce[1|2]]``:SWEep:MODE`` command selects auto or manual for the sweep mode for
              the specified channel. The query command returns the sweep mode for the specified
              channel.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:SWEep:MODE?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:SWEep:MODE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:SWEep:MODE value`` command.

        SCPI Syntax:
            ```
            - SOURce2:SWEep:MODE {AUTO|MANual}
            - SOURce2:SWEep:MODE?
            ```
        """
        return self._mode

    @property
    def rtime(self) -> Source2SweepRtime:
        """Return the ``SOURce2:SWEep:RTIMe`` command.

        Description:
            - This command sets or queries the sweep return time. Return time represents the amount
              of time from stop frequency through start frequency. Return time does not include hold
              time.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:SWEep:RTIMe?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:SWEep:RTIMe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:SWEep:RTIMe value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:SWEep:RTIMe {<seconds>|MINimum|MAXimum}
            - SOURce2:SWEep:RTIMe?
            ```
        """
        return self._rtime

    @property
    def spacing(self) -> Source2SweepSpacing:
        """Return the ``SOURce2:SWEep:SPACing`` command.

        Description:
            - The [SOURce[1|2]]``:SWEep:SPACing`` command selects linear or logarithmic spacing for
              the sweep for the specified channel. The query command returns the type for the sweep
              spacing for the specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:SWEep:SPACing?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:SWEep:SPACing?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:SWEep:SPACing value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:SWEep:SPACing {LINear|LOGarithmic}
            - SOURce2:SWEep:SPACing?
            ```
        """
        return self._spacing

    @property
    def time(self) -> Source2SweepTime:
        """Return the ``SOURce2:SWEep:TIME`` command.

        Description:
            - This command sets or queries the sweep time for the sweep for the specified channel.
              The sweep time does not include hold time and return time. The setting range is 1 ms
              to 300 s.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:SWEep:TIME?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:SWEep:TIME?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:SWEep:TIME value`` command.

        SCPI Syntax:
            ```
            - SOURce2:SWEep:TIME {<seconds>|MINimum|MAXimum}
            - SOURce2:SWEep:TIME?
            ```
        """
        return self._time


class Source2PwmState(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:PWM:STATe`` command.

    Description:
        - This command enables or disables PWM modulation. The query command returns the state of
          PWM modulation. You can select only pulse waveform as a carrier waveform for PWM.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PWM:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PWM:STATe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:PWM:STATe value`` command.

    SCPI Syntax:
        ```
        - SOURce2:PWM:STATe {ON|OFF|<NR1>}
        - SOURce2:PWM:STATe?
        ```
    """


class Source2PwmSource(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:PWM:SOURce`` command.

    Description:
        - This command sets or queries the source of modulating signal of PWM modulation for the
          specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PWM:SOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PWM:SOURce?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:PWM:SOURce value`` command.

    SCPI Syntax:
        ```
        - SOURce2:PWM:SOURce [INTernal|EXTernal]
        - SOURce2:PWM:SOURce?
        ```
    """


class Source2PwmInternalFunctionEfile(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:PWM:INTernal:FUNCtion:EFILe`` command.

    Description:
        - This command sets or queries an EFILe name used as a modulating waveform for PWM
          modulation. A file name must be specified in the mass storage system. This command returns
          ' ' if there is no file in the mass storage.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PWM:INTernal:FUNCtion:EFILe?``
          query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PWM:INTernal:FUNCtion:EFILe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce2:PWM:INTernal:FUNCtion:EFILe value`` command.

    SCPI Syntax:
        ```
        - SOURce2:PWM:INTernal:FUNCtion:EFILe <file_name>
        - SOURce2:PWM:INTernal:FUNCtion:EFILe?
        ```
    """


class Source2PwmInternalFunction(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:PWM:INTernal:FUNCtion`` command.

    Description:
        - This command sets or queries the modulating waveform of PWM modulation for the specified
          channel. You can use this command only when the internal modulation source is selected. If
          you specify EFILe when there is no EFILe or the EFILe is not yet defined, this command
          causes an error.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PWM:INTernal:FUNCtion?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PWM:INTernal:FUNCtion?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:PWM:INTernal:FUNCtion value``
          command.

    SCPI Syntax:
        ```
        - SOURce2:PWM:INTernal:FUNCtion {SINusoid|SQUare|TRIangle|RAMP|NRAMp|PRNoise|USER[1]|USER<x>|EMEMory[1]|EMEMory2|EFILe}
        - SOURce2:PWM:INTernal:FUNCtion?
        ```

    Info:
        - ``SINusoid``
        - ``SQUare``
        - ``TRIangle``
        - ``RAMP``
        - ``NRAMp``
        - ``PRNoise``
        - ``USER[1]``
        - ``USER2``
        - ``USER3``
        - ``USER4``
        - ``EMEMory[1]``
        - ``EMEMory2``
        - ``EFILe``

    Properties:
        - ``.efile``: The ``SOURce2:PWM:INTernal:FUNCtion:EFILe`` command.
    """  # noqa: E501

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._efile = Source2PwmInternalFunctionEfile(device, f"{self._cmd_syntax}:EFILe")

    @property
    def efile(self) -> Source2PwmInternalFunctionEfile:
        """Return the ``SOURce2:PWM:INTernal:FUNCtion:EFILe`` command.

        Description:
            - This command sets or queries an EFILe name used as a modulating waveform for PWM
              modulation. A file name must be specified in the mass storage system. This command
              returns ' ' if there is no file in the mass storage.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PWM:INTernal:FUNCtion:EFILe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce2:PWM:INTernal:FUNCtion:EFILe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce2:PWM:INTernal:FUNCtion:EFILe value`` command.

        SCPI Syntax:
            ```
            - SOURce2:PWM:INTernal:FUNCtion:EFILe <file_name>
            - SOURce2:PWM:INTernal:FUNCtion:EFILe?
            ```
        """
        return self._efile


class Source2PwmInternalFrequency(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:PWM:INTernal:FREQuency`` command.

    Description:
        - This command sets or queries the internal modulation frequency of PWM modulation for the
          specified channel. You can use this command only when the internal modulation source is
          selected. You can set the internal modulation frequency from 2 mHz to 50.00 kHz with
          resolution of 1 mHz. You can select the source of modulating signal by using the
          [SOURce[1|2]]``:PWM:SOURce`` [INTernal|EXTernal] command.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PWM:INTernal:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PWM:INTernal:FREQuency?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:PWM:INTernal:FREQuency value``
          command.

    SCPI Syntax:
        ```
        - SOURce2:PWM:INTernal:FREQuency {<frequency>|MINimum|MAXimum}
        - SOURce2:PWM:INTernal:FREQuency?
        ```
    """


class Source2PwmInternal(SCPICmdRead):
    """The ``SOURce2:PWM:INTernal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PWM:INTernal?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PWM:INTernal?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.frequency``: The ``SOURce2:PWM:INTernal:FREQuency`` command.
        - ``.function``: The ``SOURce2:PWM:INTernal:FUNCtion`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._frequency = Source2PwmInternalFrequency(device, f"{self._cmd_syntax}:FREQuency")
        self._function = Source2PwmInternalFunction(device, f"{self._cmd_syntax}:FUNCtion")

    @property
    def frequency(self) -> Source2PwmInternalFrequency:
        """Return the ``SOURce2:PWM:INTernal:FREQuency`` command.

        Description:
            - This command sets or queries the internal modulation frequency of PWM modulation for
              the specified channel. You can use this command only when the internal modulation
              source is selected. You can set the internal modulation frequency from 2 mHz to 50.00
              kHz with resolution of 1 mHz. You can select the source of modulating signal by using
              the [SOURce[1|2]]``:PWM:SOURce`` [INTernal|EXTernal] command.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PWM:INTernal:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:PWM:INTernal:FREQuency?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce2:PWM:INTernal:FREQuency value`` command.

        SCPI Syntax:
            ```
            - SOURce2:PWM:INTernal:FREQuency {<frequency>|MINimum|MAXimum}
            - SOURce2:PWM:INTernal:FREQuency?
            ```
        """
        return self._frequency

    @property
    def function(self) -> Source2PwmInternalFunction:
        """Return the ``SOURce2:PWM:INTernal:FUNCtion`` command.

        Description:
            - This command sets or queries the modulating waveform of PWM modulation for the
              specified channel. You can use this command only when the internal modulation source
              is selected. If you specify EFILe when there is no EFILe or the EFILe is not yet
              defined, this command causes an error.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PWM:INTernal:FUNCtion?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:PWM:INTernal:FUNCtion?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce2:PWM:INTernal:FUNCtion value`` command.

        SCPI Syntax:
            ```
            - SOURce2:PWM:INTernal:FUNCtion {SINusoid|SQUare|TRIangle|RAMP|NRAMp|PRNoise|USER[1]|USER<x>|EMEMory[1]|EMEMory2|EFILe}
            - SOURce2:PWM:INTernal:FUNCtion?
            ```

        Info:
            - ``SINusoid``
            - ``SQUare``
            - ``TRIangle``
            - ``RAMP``
            - ``NRAMp``
            - ``PRNoise``
            - ``USER[1]``
            - ``USER2``
            - ``USER3``
            - ``USER4``
            - ``EMEMory[1]``
            - ``EMEMory2``
            - ``EFILe``

        Sub-properties:
            - ``.efile``: The ``SOURce2:PWM:INTernal:FUNCtion:EFILe`` command.
        """  # noqa: E501
        return self._function


class Source2PwmDeviationDcycle(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:PWM:DEViation:DCYCle`` command.

    Description:
        - This command sets or queries the PWM deviation in percent for the specified channel. The
          setting range must meet the following conditions: Deviation ≤ Pulse Width - PWmin
          Deviation ≤ Pulse Period - Pulse Width - PWmin Deviation ≤ Pulse Width - 0.8 × (Leading
          Edge Time + Trailing Edge Time) Deviation ≤ Pulse Period - Pulse Width - 0.8 × (Leading
          Edge Time + Trailing Edge Time) where PWmin is the minimum pulse width.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PWM:DEViation:DCYCle?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PWM:DEViation:DCYCle?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:PWM:DEViation:DCYCle value``
          command.

    SCPI Syntax:
        ```
        - SOURce2:PWM:DEViation:DCYCle {<percent>|MINimum|MAXimum}
        - SOURce2:PWM:DEViation:DCYCle?
        ```
    """


class Source2PwmDeviation(SCPICmdRead):
    """The ``SOURce2:PWM:DEViation`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PWM:DEViation?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PWM:DEViation?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.dcycle``: The ``SOURce2:PWM:DEViation:DCYCle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._dcycle = Source2PwmDeviationDcycle(device, f"{self._cmd_syntax}:DCYCle")

    @property
    def dcycle(self) -> Source2PwmDeviationDcycle:
        """Return the ``SOURce2:PWM:DEViation:DCYCle`` command.

        Description:
            - This command sets or queries the PWM deviation in percent for the specified channel.
              The setting range must meet the following conditions: Deviation ≤ Pulse Width - PWmin
              Deviation ≤ Pulse Period - Pulse Width - PWmin Deviation ≤ Pulse Width - 0.8 ×
              (Leading Edge Time + Trailing Edge Time) Deviation ≤ Pulse Period - Pulse Width - 0.8
              × (Leading Edge Time + Trailing Edge Time) where PWmin is the minimum pulse width.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PWM:DEViation:DCYCle?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:PWM:DEViation:DCYCle?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce2:PWM:DEViation:DCYCle value`` command.

        SCPI Syntax:
            ```
            - SOURce2:PWM:DEViation:DCYCle {<percent>|MINimum|MAXimum}
            - SOURce2:PWM:DEViation:DCYCle?
            ```
        """
        return self._dcycle


class Source2Pwm(SCPICmdRead):
    """The ``SOURce2:PWM`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PWM?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PWM?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.internal``: The ``SOURce2:PWM:INTernal`` command tree.
        - ``.source``: The ``SOURce2:PWM:SOURce`` command.
        - ``.state``: The ``SOURce2:PWM:STATe`` command.
        - ``.deviation``: The ``SOURce2:PWM:DEViation`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._internal = Source2PwmInternal(device, f"{self._cmd_syntax}:INTernal")
        self._source = Source2PwmSource(device, f"{self._cmd_syntax}:SOURce")
        self._state = Source2PwmState(device, f"{self._cmd_syntax}:STATe")
        self._deviation = Source2PwmDeviation(device, f"{self._cmd_syntax}:DEViation")

    @property
    def internal(self) -> Source2PwmInternal:
        """Return the ``SOURce2:PWM:INTernal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PWM:INTernal?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:PWM:INTernal?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.frequency``: The ``SOURce2:PWM:INTernal:FREQuency`` command.
            - ``.function``: The ``SOURce2:PWM:INTernal:FUNCtion`` command.
        """
        return self._internal

    @property
    def source(self) -> Source2PwmSource:
        """Return the ``SOURce2:PWM:SOURce`` command.

        Description:
            - This command sets or queries the source of modulating signal of PWM modulation for the
              specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PWM:SOURce?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:PWM:SOURce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:PWM:SOURce value`` command.

        SCPI Syntax:
            ```
            - SOURce2:PWM:SOURce [INTernal|EXTernal]
            - SOURce2:PWM:SOURce?
            ```
        """
        return self._source

    @property
    def state(self) -> Source2PwmState:
        """Return the ``SOURce2:PWM:STATe`` command.

        Description:
            - This command enables or disables PWM modulation. The query command returns the state
              of PWM modulation. You can select only pulse waveform as a carrier waveform for PWM.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PWM:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:PWM:STATe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:PWM:STATe value`` command.

        SCPI Syntax:
            ```
            - SOURce2:PWM:STATe {ON|OFF|<NR1>}
            - SOURce2:PWM:STATe?
            ```
        """
        return self._state

    @property
    def deviation(self) -> Source2PwmDeviation:
        """Return the ``SOURce2:PWM:DEViation`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PWM:DEViation?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:PWM:DEViation?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.dcycle``: The ``SOURce2:PWM:DEViation:DCYCle`` command.
        """
        return self._deviation


class Source2PulseWidth(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:PULSe:WIDTh`` command.

    Description:
        - This command sets or queries the pulse width for the specified channel. Pulse Width =
          Period ∞ Duty Cycle / 100 The pulse width must be less than the period. The setting range
          is 0.001% to 99.999% in terms of duty cycle. AFG3011 / 3011C: 80 ns to 999.99 s AFG3021B /
          3021C / 3022B / 3022C: 16 ns to 999.99 s AFG3051C / 3052C: 12 ns to 999.99 s AFG3101 /
          3101C / 3102 / 3102C: 8 ns to 999.99 s AFG3151C / 3152C: 5 ns to 999.99 s AFG3251 / 3251C
          / 3252 / 3252C: 4 ns to 999.99 s Pulse Width ≤ Pulse Period - 0.8 ∞ (Leading Edge Time +
          Trailing Edge Time) Pulse Width ≥ 0.625 ∞ (Leading Edge Time + Trailing Edge Time)

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PULSe:WIDTh?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PULSe:WIDTh?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:PULSe:WIDTh value`` command.

    SCPI Syntax:
        ```
        - SOURce2:PULSe:WIDTh {<seconds>|MINimum|MAXimum}
        - SOURce2:PULSe:WIDTh?
        ```
    """


class Source2PulseTransitionTrailing(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:PULSe:TRANsition:TRAiling`` command.

    Description:
        - This command sets or queries the trailing edge time of pulse waveform.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PULSe:TRANsition:TRAiling?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PULSe:TRANsition:TRAiling?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce2:PULSe:TRANsition:TRAiling value`` command.

    SCPI Syntax:
        ```
        - SOURce2:PULSe:TRANsition:TRAiling {<seconds>|MINimum|MAXimum}
        - SOURce2:PULSe:TRANsition:TRAiling?
        ```
    """


class Source2PulseTransitionLeading(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:PULSe:TRANsition:LEADing`` command.

    Description:
        - This command sets or queries the leading edge time of pulse waveform.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PULSe:TRANsition:LEADing?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PULSe:TRANsition:LEADing?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce2:PULSe:TRANsition:LEADing value`` command.

    SCPI Syntax:
        ```
        - SOURce2:PULSe:TRANsition:LEADing {<seconds>|MINimum|MAXimum}
        - SOURce2:PULSe:TRANsition:LEADing?
        ```
    """


class Source2PulseTransition(SCPICmdRead):
    """The ``SOURce2:PULSe:TRANsition`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PULSe:TRANsition?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PULSe:TRANsition?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.trailing``: The ``SOURce2:PULSe:TRANsition:TRAiling`` command.
        - ``.leading``: The ``SOURce2:PULSe:TRANsition:LEADing`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._trailing = Source2PulseTransitionTrailing(device, f"{self._cmd_syntax}:TRAiling")
        self._leading = Source2PulseTransitionLeading(device, f"{self._cmd_syntax}:LEADing")

    @property
    def trailing(self) -> Source2PulseTransitionTrailing:
        """Return the ``SOURce2:PULSe:TRANsition:TRAiling`` command.

        Description:
            - This command sets or queries the trailing edge time of pulse waveform.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PULSe:TRANsition:TRAiling?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce2:PULSe:TRANsition:TRAiling?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce2:PULSe:TRANsition:TRAiling value`` command.

        SCPI Syntax:
            ```
            - SOURce2:PULSe:TRANsition:TRAiling {<seconds>|MINimum|MAXimum}
            - SOURce2:PULSe:TRANsition:TRAiling?
            ```
        """
        return self._trailing

    @property
    def leading(self) -> Source2PulseTransitionLeading:
        """Return the ``SOURce2:PULSe:TRANsition:LEADing`` command.

        Description:
            - This command sets or queries the leading edge time of pulse waveform.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PULSe:TRANsition:LEADing?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce2:PULSe:TRANsition:LEADing?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce2:PULSe:TRANsition:LEADing value`` command.

        SCPI Syntax:
            ```
            - SOURce2:PULSe:TRANsition:LEADing {<seconds>|MINimum|MAXimum}
            - SOURce2:PULSe:TRANsition:LEADing?
            ```
        """
        return self._leading


class Source2PulsePeriod(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:PULSe:PERiod`` command.

    Description:
        - This command sets or queries the period for pulse waveform.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PULSe:PERiod?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PULSe:PERiod?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:PULSe:PERiod value`` command.

    SCPI Syntax:
        ```
        - SOURce2:PULSe:PERiod {<period>|MINimum|MAXimum}
        - SOURce2:PULSe:PERiod?
        ```
    """


class Source2PulseHold(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:PULSe:HOLD`` command.

    Description:
        - The [SOURce[1|2]]``:PULSe:HOLD`` command sets the arbitrary function generator to hold
          either pulse width or pulse duty. The [SOURce[1|2]]``:PULSe:HOLD?`` query returns WIDTh or
          DUTY.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PULSe:HOLD?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PULSe:HOLD?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:PULSe:HOLD value`` command.

    SCPI Syntax:
        ```
        - SOURce2:PULSe:HOLD {WIDTh|DUTY}
        - SOURce2:PULSe:HOLD?
        ```
    """


class Source2PulseDelay(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:PULSe:DELay`` command.

    Description:
        - This command sets or queries the lead delay of the pulse waveform for the specified
          channel.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PULSe:DELay?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PULSe:DELay?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:PULSe:DELay value`` command.

    SCPI Syntax:
        ```
        - SOURce2:PULSe:DELay {<delay>|MINimum|MAXimum}
        - SOURce2:PULSe:DELay?
        ```
    """


class Source2PulseDcycle(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:PULSe:DCYCle`` command.

    Description:
        - This command sets or queries the duty cycle of the pulse waveform for the specified
          channel. The setting range is 0.001% to 99.999% in increments of 0.001. The arbitrary
          function generator will hold the settings of leading edge and trailing edge when the duty
          cycle is varied. Refer to the [SOURce[1|2]]``:PULSe:WIDTh`` command for the setting range.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PULSe:DCYCle?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PULSe:DCYCle?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:PULSe:DCYCle value`` command.

    SCPI Syntax:
        ```
        - SOURce2:PULSe:DCYCle {<percent>|MINimum|MAXimum}
        - SOURce2:PULSe:DCYCle?
        ```
    """


class Source2Pulse(SCPICmdRead):
    """The ``SOURce2:PULSe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PULSe?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PULSe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.dcycle``: The ``SOURce2:PULSe:DCYCle`` command.
        - ``.delay``: The ``SOURce2:PULSe:DELay`` command.
        - ``.hold``: The ``SOURce2:PULSe:HOLD`` command.
        - ``.period``: The ``SOURce2:PULSe:PERiod`` command.
        - ``.transition``: The ``SOURce2:PULSe:TRANsition`` command tree.
        - ``.width``: The ``SOURce2:PULSe:WIDTh`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._dcycle = Source2PulseDcycle(device, f"{self._cmd_syntax}:DCYCle")
        self._delay = Source2PulseDelay(device, f"{self._cmd_syntax}:DELay")
        self._hold = Source2PulseHold(device, f"{self._cmd_syntax}:HOLD")
        self._period = Source2PulsePeriod(device, f"{self._cmd_syntax}:PERiod")
        self._transition = Source2PulseTransition(device, f"{self._cmd_syntax}:TRANsition")
        self._width = Source2PulseWidth(device, f"{self._cmd_syntax}:WIDTh")

    @property
    def dcycle(self) -> Source2PulseDcycle:
        """Return the ``SOURce2:PULSe:DCYCle`` command.

        Description:
            - This command sets or queries the duty cycle of the pulse waveform for the specified
              channel. The setting range is 0.001% to 99.999% in increments of 0.001. The arbitrary
              function generator will hold the settings of leading edge and trailing edge when the
              duty cycle is varied. Refer to the [SOURce[1|2]]``:PULSe:WIDTh`` command for the
              setting range.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PULSe:DCYCle?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:PULSe:DCYCle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:PULSe:DCYCle value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:PULSe:DCYCle {<percent>|MINimum|MAXimum}
            - SOURce2:PULSe:DCYCle?
            ```
        """
        return self._dcycle

    @property
    def delay(self) -> Source2PulseDelay:
        """Return the ``SOURce2:PULSe:DELay`` command.

        Description:
            - This command sets or queries the lead delay of the pulse waveform for the specified
              channel.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PULSe:DELay?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:PULSe:DELay?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:PULSe:DELay value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:PULSe:DELay {<delay>|MINimum|MAXimum}
            - SOURce2:PULSe:DELay?
            ```
        """
        return self._delay

    @property
    def hold(self) -> Source2PulseHold:
        """Return the ``SOURce2:PULSe:HOLD`` command.

        Description:
            - The [SOURce[1|2]]``:PULSe:HOLD`` command sets the arbitrary function generator to hold
              either pulse width or pulse duty. The [SOURce[1|2]]``:PULSe:HOLD?`` query returns
              WIDTh or DUTY.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PULSe:HOLD?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:PULSe:HOLD?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:PULSe:HOLD value`` command.

        SCPI Syntax:
            ```
            - SOURce2:PULSe:HOLD {WIDTh|DUTY}
            - SOURce2:PULSe:HOLD?
            ```
        """
        return self._hold

    @property
    def period(self) -> Source2PulsePeriod:
        """Return the ``SOURce2:PULSe:PERiod`` command.

        Description:
            - This command sets or queries the period for pulse waveform.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PULSe:PERiod?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:PULSe:PERiod?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:PULSe:PERiod value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:PULSe:PERiod {<period>|MINimum|MAXimum}
            - SOURce2:PULSe:PERiod?
            ```
        """
        return self._period

    @property
    def transition(self) -> Source2PulseTransition:
        """Return the ``SOURce2:PULSe:TRANsition`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PULSe:TRANsition?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:PULSe:TRANsition?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.trailing``: The ``SOURce2:PULSe:TRANsition:TRAiling`` command.
            - ``.leading``: The ``SOURce2:PULSe:TRANsition:LEADing`` command.
        """
        return self._transition

    @property
    def width(self) -> Source2PulseWidth:
        """Return the ``SOURce2:PULSe:WIDTh`` command.

        Description:
            - This command sets or queries the pulse width for the specified channel. Pulse Width =
              Period ∞ Duty Cycle / 100 The pulse width must be less than the period. The setting
              range is 0.001% to 99.999% in terms of duty cycle. AFG3011 / 3011C: 80 ns to 999.99 s
              AFG3021B / 3021C / 3022B / 3022C: 16 ns to 999.99 s AFG3051C / 3052C: 12 ns to 999.99
              s AFG3101 / 3101C / 3102 / 3102C: 8 ns to 999.99 s AFG3151C / 3152C: 5 ns to 999.99 s
              AFG3251 / 3251C / 3252 / 3252C: 4 ns to 999.99 s Pulse Width ≤ Pulse Period - 0.8 ∞
              (Leading Edge Time + Trailing Edge Time) Pulse Width ≥ 0.625 ∞ (Leading Edge Time +
              Trailing Edge Time)

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PULSe:WIDTh?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:PULSe:WIDTh?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:PULSe:WIDTh value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:PULSe:WIDTh {<seconds>|MINimum|MAXimum}
            - SOURce2:PULSe:WIDTh?
            ```
        """
        return self._width


class Source2PmState(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:PM:STATe`` command.

    Description:
        - This command enables or disables PM modulation. The query command returns the state of PM
          modulation. You can select a sine, square, ramp, or arbitrary waveform for the carrier
          waveform.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PM:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PM:STATe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:PM:STATe value`` command.

    SCPI Syntax:
        ```
        - SOURce2:PM:STATe {ON|OFF|<NR1>}
        - SOURce2:PM:STATe?
        ```
    """


class Source2PmSource(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:PM:SOURce`` command.

    Description:
        - This command sets or queries the source of modulation signal of PM modulation for the
          specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PM:SOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PM:SOURce?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:PM:SOURce value`` command.

    SCPI Syntax:
        ```
        - SOURce2:PM:SOURce [INTernal|EXTernal]
        - SOURce2:PM:SOURce?
        ```
    """


class Source2PmInternalFunctionEfile(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:PM:INTernal:FUNCtion:EFILe`` command.

    Description:
        - This command sets or queries an EFILe name used as a modulating waveform for PM
          modulation. A file name must be specified in the mass storage system. This command returns
          ' ' if there is no file in the mass storage.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PM:INTernal:FUNCtion:EFILe?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PM:INTernal:FUNCtion:EFILe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce2:PM:INTernal:FUNCtion:EFILe value`` command.

    SCPI Syntax:
        ```
        - SOURce2:PM:INTernal:FUNCtion:EFILe <file_name>
        - SOURce2:PM:INTernal:FUNCtion:EFILe?
        ```
    """


class Source2PmInternalFunction(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:PM:INTernal:FUNCtion`` command.

    Description:
        - This command sets or queries the modulating waveform of PM modulation for the specified
          channel. You can use this command only when the internal modulation source is selected.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PM:INTernal:FUNCtion?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PM:INTernal:FUNCtion?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:PM:INTernal:FUNCtion value``
          command.

    SCPI Syntax:
        ```
        - SOURce2:PM:INTernal:FUNCtion {SINusoid|SQUare|TRIangle|RAMP|NRAMp|PRNoise|USER[1]|USER<x>|EMEMory[1]|EMEMory2|EFILe}
        - SOURce2:PM:INTernal:FUNCtion?
        ```

    Info:
        - ``SINusoid``
        - ``SQUare``
        - ``TRIangle``
        - ``RAMP``
        - ``NRAMp``
        - ``PRNoise``
        - ``USER[1]``
        - ``USER2``
        - ``USER3``
        - ``USER4``
        - ``EMEMory[1]``
        - ``EMEMory2``
        - ``EFILe EFILe``

    Properties:
        - ``.efile``: The ``SOURce2:PM:INTernal:FUNCtion:EFILe`` command.
    """  # noqa: E501

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._efile = Source2PmInternalFunctionEfile(device, f"{self._cmd_syntax}:EFILe")

    @property
    def efile(self) -> Source2PmInternalFunctionEfile:
        """Return the ``SOURce2:PM:INTernal:FUNCtion:EFILe`` command.

        Description:
            - This command sets or queries an EFILe name used as a modulating waveform for PM
              modulation. A file name must be specified in the mass storage system. This command
              returns ' ' if there is no file in the mass storage.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PM:INTernal:FUNCtion:EFILe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce2:PM:INTernal:FUNCtion:EFILe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce2:PM:INTernal:FUNCtion:EFILe value`` command.

        SCPI Syntax:
            ```
            - SOURce2:PM:INTernal:FUNCtion:EFILe <file_name>
            - SOURce2:PM:INTernal:FUNCtion:EFILe?
            ```
        """
        return self._efile


class Source2PmInternalFrequency(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:PM:INTernal:FREQuency`` command.

    Description:
        - This command sets or queries the internal modulation frequency of PM modulation for the
          specified channel. You can use this command only when the internal modulation source is
          selected. You can set the internal modulation frequency from 2 mHz to 50.00 kHz with
          resolution of 1 mHz. You can select the source of modulating signal by using the
          [SOURce[1|2]]``:PM:SOURce`` [INTernal|EXTernal] command.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PM:INTernal:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PM:INTernal:FREQuency?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:PM:INTernal:FREQuency value``
          command.

    SCPI Syntax:
        ```
        - SOURce2:PM:INTernal:FREQuency {<frequency>|MINimum|MAXimum}
        - SOURce2:PM:INTernal:FREQuency?
        ```
    """


class Source2PmInternal(SCPICmdRead):
    """The ``SOURce2:PM:INTernal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PM:INTernal?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PM:INTernal?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.frequency``: The ``SOURce2:PM:INTernal:FREQuency`` command.
        - ``.function``: The ``SOURce2:PM:INTernal:FUNCtion`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._frequency = Source2PmInternalFrequency(device, f"{self._cmd_syntax}:FREQuency")
        self._function = Source2PmInternalFunction(device, f"{self._cmd_syntax}:FUNCtion")

    @property
    def frequency(self) -> Source2PmInternalFrequency:
        """Return the ``SOURce2:PM:INTernal:FREQuency`` command.

        Description:
            - This command sets or queries the internal modulation frequency of PM modulation for
              the specified channel. You can use this command only when the internal modulation
              source is selected. You can set the internal modulation frequency from 2 mHz to 50.00
              kHz with resolution of 1 mHz. You can select the source of modulating signal by using
              the [SOURce[1|2]]``:PM:SOURce`` [INTernal|EXTernal] command.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PM:INTernal:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:PM:INTernal:FREQuency?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce2:PM:INTernal:FREQuency value`` command.

        SCPI Syntax:
            ```
            - SOURce2:PM:INTernal:FREQuency {<frequency>|MINimum|MAXimum}
            - SOURce2:PM:INTernal:FREQuency?
            ```
        """
        return self._frequency

    @property
    def function(self) -> Source2PmInternalFunction:
        """Return the ``SOURce2:PM:INTernal:FUNCtion`` command.

        Description:
            - This command sets or queries the modulating waveform of PM modulation for the
              specified channel. You can use this command only when the internal modulation source
              is selected.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PM:INTernal:FUNCtion?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:PM:INTernal:FUNCtion?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce2:PM:INTernal:FUNCtion value`` command.

        SCPI Syntax:
            ```
            - SOURce2:PM:INTernal:FUNCtion {SINusoid|SQUare|TRIangle|RAMP|NRAMp|PRNoise|USER[1]|USER<x>|EMEMory[1]|EMEMory2|EFILe}
            - SOURce2:PM:INTernal:FUNCtion?
            ```

        Info:
            - ``SINusoid``
            - ``SQUare``
            - ``TRIangle``
            - ``RAMP``
            - ``NRAMp``
            - ``PRNoise``
            - ``USER[1]``
            - ``USER2``
            - ``USER3``
            - ``USER4``
            - ``EMEMory[1]``
            - ``EMEMory2``
            - ``EFILe EFILe``

        Sub-properties:
            - ``.efile``: The ``SOURce2:PM:INTernal:FUNCtion:EFILe`` command.
        """  # noqa: E501
        return self._function


class Source2PmDeviation(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:PM:DEViation`` command.

    Description:
        - This command sets or queries the peak frequency deviation of PM modulation for the
          specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PM:DEViation?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PM:DEViation?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:PM:DEViation value`` command.

    SCPI Syntax:
        ```
        - SOURce2:PM:DEViation {<deviation>|MINimum|MAXimum}
        - SOURce2:PM:DEViation?
        ```
    """


class Source2Pm(SCPICmdRead):
    """The ``SOURce2:PM`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PM?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PM?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.internal``: The ``SOURce2:PM:INTernal`` command tree.
        - ``.source``: The ``SOURce2:PM:SOURce`` command.
        - ``.state``: The ``SOURce2:PM:STATe`` command.
        - ``.deviation``: The ``SOURce2:PM:DEViation`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._internal = Source2PmInternal(device, f"{self._cmd_syntax}:INTernal")
        self._source = Source2PmSource(device, f"{self._cmd_syntax}:SOURce")
        self._state = Source2PmState(device, f"{self._cmd_syntax}:STATe")
        self._deviation = Source2PmDeviation(device, f"{self._cmd_syntax}:DEViation")

    @property
    def internal(self) -> Source2PmInternal:
        """Return the ``SOURce2:PM:INTernal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PM:INTernal?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:PM:INTernal?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.frequency``: The ``SOURce2:PM:INTernal:FREQuency`` command.
            - ``.function``: The ``SOURce2:PM:INTernal:FUNCtion`` command.
        """
        return self._internal

    @property
    def source(self) -> Source2PmSource:
        """Return the ``SOURce2:PM:SOURce`` command.

        Description:
            - This command sets or queries the source of modulation signal of PM modulation for the
              specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PM:SOURce?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:PM:SOURce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:PM:SOURce value`` command.

        SCPI Syntax:
            ```
            - SOURce2:PM:SOURce [INTernal|EXTernal]
            - SOURce2:PM:SOURce?
            ```
        """
        return self._source

    @property
    def state(self) -> Source2PmState:
        """Return the ``SOURce2:PM:STATe`` command.

        Description:
            - This command enables or disables PM modulation. The query command returns the state of
              PM modulation. You can select a sine, square, ramp, or arbitrary waveform for the
              carrier waveform.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PM:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:PM:STATe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:PM:STATe value`` command.

        SCPI Syntax:
            ```
            - SOURce2:PM:STATe {ON|OFF|<NR1>}
            - SOURce2:PM:STATe?
            ```
        """
        return self._state

    @property
    def deviation(self) -> Source2PmDeviation:
        """Return the ``SOURce2:PM:DEViation`` command.

        Description:
            - This command sets or queries the peak frequency deviation of PM modulation for the
              specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PM:DEViation?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:PM:DEViation?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:PM:DEViation value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:PM:DEViation {<deviation>|MINimum|MAXimum}
            - SOURce2:PM:DEViation?
            ```
        """
        return self._deviation


class Source2PhaseInitiate(SCPICmdWriteNoArguments):
    """The ``SOURce2:PHASe:INITiate`` command.

    Description:
        - This command synchronizes the phase of CH 1 and CH 2 output waveforms. The arbitrary
          function generator performs the same operation if you specify either SOURce1 or SOURce2.
          If your arbitrary function generator is single-channel model, this command is not
          supported.

    Usage:
        - Using the ``.write()`` method will send the ``SOURce2:PHASe:INITiate`` command.

    SCPI Syntax:
        ```
        - SOURce2:PHASe:INITiate
        ```
    """


class Source2PhaseAdjust(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:PHASe:ADJust`` command.

    Description:
        - This command sets or queries the phase of output waveform for the specified channel. You
          can set the value in radians or degrees. If no units are specified, the default is RAD.
          The query command returns the value in RAD. This command is supported when you select a
          waveform other than DC, Noise, and Pulse.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PHASe:ADJust?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PHASe:ADJust?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:PHASe:ADJust value`` command.

    SCPI Syntax:
        ```
        - SOURce2:PHASe:ADJust {<phase>|MINimum|MAXimum}
        - SOURce2:PHASe:ADJust?
        ```
    """


class Source2Phase(SCPICmdRead):
    """The ``SOURce2:PHASe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:PHASe?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:PHASe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.initiate``: The ``SOURce2:PHASe:INITiate`` command.
        - ``.adjust``: The ``SOURce2:PHASe:ADJust`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._initiate = Source2PhaseInitiate(device, f"{self._cmd_syntax}:INITiate")
        self._adjust = Source2PhaseAdjust(device, f"{self._cmd_syntax}:ADJust")

    @property
    def initiate(self) -> Source2PhaseInitiate:
        """Return the ``SOURce2:PHASe:INITiate`` command.

        Description:
            - This command synchronizes the phase of CH 1 and CH 2 output waveforms. The arbitrary
              function generator performs the same operation if you specify either SOURce1 or
              SOURce2. If your arbitrary function generator is single-channel model, this command is
              not supported.

        Usage:
            - Using the ``.write()`` method will send the ``SOURce2:PHASe:INITiate`` command.

        SCPI Syntax:
            ```
            - SOURce2:PHASe:INITiate
            ```
        """
        return self._initiate

    @property
    def adjust(self) -> Source2PhaseAdjust:
        """Return the ``SOURce2:PHASe:ADJust`` command.

        Description:
            - This command sets or queries the phase of output waveform for the specified channel.
              You can set the value in radians or degrees. If no units are specified, the default is
              RAD. The query command returns the value in RAD. This command is supported when you
              select a waveform other than DC, Noise, and Pulse.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PHASe:ADJust?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:PHASe:ADJust?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:PHASe:ADJust value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:PHASe:ADJust {<phase>|MINimum|MAXimum}
            - SOURce2:PHASe:ADJust?
            ```
        """
        return self._adjust


class Source2FunctionShape(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:FUNCtion:SHAPe`` command.

    Description:
        - This command sets or queries the shape of the output waveform. When the specified user
          memory is deleted, this command causes an error if you select the user memory.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FUNCtion:SHAPe?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FUNCtion:SHAPe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:FUNCtion:SHAPe value`` command.

    SCPI Syntax:
        ```
        - SOURce2:FUNCtion:SHAPe {SINusoid|SQUare|PULSe|RAMP|PRNoise|DC|SINC|GAUSsian|LORentz|ERISe|EDECay|HAVersine|USER[1]|USER<x>|EMEMory[1]|EMEMory2|EFILe}
        - SOURce2:FUNCtion:SHAPe?
        ```

    Info:
        - ``USER[1]`` A user defined waveform saved in the user waveform memory or the EMEMory can
          be selected as an output waveform.
        - ``USER2`` A user defined waveform saved in the user waveform memory or the EMEMory can be
          selected as an output waveform.
        - ``USER3`` A user defined waveform saved in the user waveform memory or the EMEMory can be
          selected as an output waveform.
        - ``USER4`` A user defined waveform saved in the user waveform memory or the EMEMory can be
          selected as an output waveform.
        - ``EMEMory[1]`` A user defined waveform saved in the user waveform memory or the EMEMory
          can be selected as an output waveform.
        - ``EMEMory2`` A user defined waveform saved in the user waveform memory or the EMEMory can
          be selected as an output waveform.
    """  # noqa: E501


class Source2FunctionRampSymmetry(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:FUNCtion:RAMP:SYMMetry`` command.

    Description:
        - This command sets or queries the symmetry of ramp waveform for the specified channel. The
          setting range is 0.0% to 100.0%.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FUNCtion:RAMP:SYMMetry?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FUNCtion:RAMP:SYMMetry?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:FUNCtion:RAMP:SYMMetry value``
          command.

    SCPI Syntax:
        ```
        - SOURce2:FUNCtion:RAMP:SYMMetry {<symmetry>|MINimum|MAXimum}
        - SOURce2:FUNCtion:RAMP:SYMMetry?
        ```
    """


class Source2FunctionRamp(SCPICmdRead):
    """The ``SOURce2:FUNCtion:RAMP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FUNCtion:RAMP?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FUNCtion:RAMP?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.symmetry``: The ``SOURce2:FUNCtion:RAMP:SYMMetry`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._symmetry = Source2FunctionRampSymmetry(device, f"{self._cmd_syntax}:SYMMetry")

    @property
    def symmetry(self) -> Source2FunctionRampSymmetry:
        """Return the ``SOURce2:FUNCtion:RAMP:SYMMetry`` command.

        Description:
            - This command sets or queries the symmetry of ramp waveform for the specified channel.
              The setting range is 0.0% to 100.0%.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FUNCtion:RAMP:SYMMetry?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:FUNCtion:RAMP:SYMMetry?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce2:FUNCtion:RAMP:SYMMetry value`` command.

        SCPI Syntax:
            ```
            - SOURce2:FUNCtion:RAMP:SYMMetry {<symmetry>|MINimum|MAXimum}
            - SOURce2:FUNCtion:RAMP:SYMMetry?
            ```
        """
        return self._symmetry


class Source2FunctionEfile(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:FUNCtion:EFILe`` command.

    Description:
        - This command sets or queries an EFILe name used as an output waveform. A file name must be
          specified in the mass storage system. This command returns ' ' if there is no file in the
          mass storage.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FUNCtion:EFILe?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FUNCtion:EFILe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:FUNCtion:EFILe value`` command.

    SCPI Syntax:
        ```
        - SOURce2:FUNCtion:EFILe <file_name>
        - SOURce2:FUNCtion:EFILe?
        ```
    """


class Source2Function(SCPICmdRead):
    """The ``SOURce2:FUNCtion`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FUNCtion?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FUNCtion?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.efile``: The ``SOURce2:FUNCtion:EFILe`` command.
        - ``.ramp``: The ``SOURce2:FUNCtion:RAMP`` command tree.
        - ``.shape``: The ``SOURce2:FUNCtion:SHAPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._efile = Source2FunctionEfile(device, f"{self._cmd_syntax}:EFILe")
        self._ramp = Source2FunctionRamp(device, f"{self._cmd_syntax}:RAMP")
        self._shape = Source2FunctionShape(device, f"{self._cmd_syntax}:SHAPe")

    @property
    def efile(self) -> Source2FunctionEfile:
        """Return the ``SOURce2:FUNCtion:EFILe`` command.

        Description:
            - This command sets or queries an EFILe name used as an output waveform. A file name
              must be specified in the mass storage system. This command returns ' ' if there is no
              file in the mass storage.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FUNCtion:EFILe?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:FUNCtion:EFILe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:FUNCtion:EFILe value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:FUNCtion:EFILe <file_name>
            - SOURce2:FUNCtion:EFILe?
            ```
        """
        return self._efile

    @property
    def ramp(self) -> Source2FunctionRamp:
        """Return the ``SOURce2:FUNCtion:RAMP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FUNCtion:RAMP?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:FUNCtion:RAMP?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.symmetry``: The ``SOURce2:FUNCtion:RAMP:SYMMetry`` command.
        """
        return self._ramp

    @property
    def shape(self) -> Source2FunctionShape:
        """Return the ``SOURce2:FUNCtion:SHAPe`` command.

        Description:
            - This command sets or queries the shape of the output waveform. When the specified user
              memory is deleted, this command causes an error if you select the user memory.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FUNCtion:SHAPe?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:FUNCtion:SHAPe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:FUNCtion:SHAPe value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:FUNCtion:SHAPe {SINusoid|SQUare|PULSe|RAMP|PRNoise|DC|SINC|GAUSsian|LORentz|ERISe|EDECay|HAVersine|USER[1]|USER<x>|EMEMory[1]|EMEMory2|EFILe}
            - SOURce2:FUNCtion:SHAPe?
            ```

        Info:
            - ``USER[1]`` A user defined waveform saved in the user waveform memory or the EMEMory
              can be selected as an output waveform.
            - ``USER2`` A user defined waveform saved in the user waveform memory or the EMEMory can
              be selected as an output waveform.
            - ``USER3`` A user defined waveform saved in the user waveform memory or the EMEMory can
              be selected as an output waveform.
            - ``USER4`` A user defined waveform saved in the user waveform memory or the EMEMory can
              be selected as an output waveform.
            - ``EMEMory[1]`` A user defined waveform saved in the user waveform memory or the
              EMEMory can be selected as an output waveform.
            - ``EMEMory2`` A user defined waveform saved in the user waveform memory or the EMEMory
              can be selected as an output waveform.
        """  # noqa: E501
        return self._shape


class Source2FskeyState(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:FSKey:STATe`` command.

    Description:
        - This command enables or disables FSK modulation. The query command returns the state of
          FSK modulation. You can select a sine, square, ramp, or arbitrary waveform for the carrier
          waveform.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FSKey:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FSKey:STATe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:FSKey:STATe value`` command.

    SCPI Syntax:
        ```
        - SOURce2:FSKey:STATe {ON|OFF|<NR1>}
        - SOURce2:FSKey:STATe?
        ```
    """


class Source2FskeySource(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:FSKey:SOURce`` command.

    Description:
        - This command sets or queries the source of modulation signal of FSK modulation for the
          specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FSKey:SOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FSKey:SOURce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:FSKey:SOURce value`` command.

    SCPI Syntax:
        ```
        - SOURce2:FSKey:SOURce [INTernal|EXTernal]
        - SOURce2:FSKey:SOURce?
        ```
    """


class Source2FskeyInternalRate(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:FSKey:INTernal:RATE`` command.

    Description:
        - This command sets or queries the internal modulation rate of FSK modulation for the
          specified channel. You can use this command only when the internal modulation source is
          selected.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FSKey:INTernal:RATE?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FSKey:INTernal:RATE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:FSKey:INTernal:RATE value``
          command.

    SCPI Syntax:
        ```
        - SOURce2:FSKey:INTernal:RATE {<rate>|MINimum|MAXimum}
        - SOURce2:FSKey:INTernal:RATE?
        ```
    """


class Source2FskeyInternal(SCPICmdRead):
    """The ``SOURce2:FSKey:INTernal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FSKey:INTernal?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FSKey:INTernal?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.rate``: The ``SOURce2:FSKey:INTernal:RATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._rate = Source2FskeyInternalRate(device, f"{self._cmd_syntax}:RATE")

    @property
    def rate(self) -> Source2FskeyInternalRate:
        """Return the ``SOURce2:FSKey:INTernal:RATE`` command.

        Description:
            - This command sets or queries the internal modulation rate of FSK modulation for the
              specified channel. You can use this command only when the internal modulation source
              is selected.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FSKey:INTernal:RATE?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:FSKey:INTernal:RATE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:FSKey:INTernal:RATE value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:FSKey:INTernal:RATE {<rate>|MINimum|MAXimum}
            - SOURce2:FSKey:INTernal:RATE?
            ```
        """
        return self._rate


class Source2FskeyFrequency(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:FSKey:FREQuency`` command.

    Description:
        - This command sets or queries the hop frequency of FSK modulation for the specified
          channel.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FSKey:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FSKey:FREQuency?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:FSKey:FREQuency value``
          command.

    SCPI Syntax:
        ```
        - SOURce2:FSKey:FREQuency {<frequency>|MINimum|MAXimum}
        - SOURce2:FSKey:FREQuency?
        ```
    """


class Source2Fskey(SCPICmdRead):
    """The ``SOURce2:FSKey`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FSKey?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FSKey?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.internal``: The ``SOURce2:FSKey:INTernal`` command tree.
        - ``.source``: The ``SOURce2:FSKey:SOURce`` command.
        - ``.state``: The ``SOURce2:FSKey:STATe`` command.
        - ``.frequency``: The ``SOURce2:FSKey:FREQuency`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._internal = Source2FskeyInternal(device, f"{self._cmd_syntax}:INTernal")
        self._source = Source2FskeySource(device, f"{self._cmd_syntax}:SOURce")
        self._state = Source2FskeyState(device, f"{self._cmd_syntax}:STATe")
        self._frequency = Source2FskeyFrequency(device, f"{self._cmd_syntax}:FREQuency")

    @property
    def internal(self) -> Source2FskeyInternal:
        """Return the ``SOURce2:FSKey:INTernal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FSKey:INTernal?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:FSKey:INTernal?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.rate``: The ``SOURce2:FSKey:INTernal:RATE`` command.
        """
        return self._internal

    @property
    def source(self) -> Source2FskeySource:
        """Return the ``SOURce2:FSKey:SOURce`` command.

        Description:
            - This command sets or queries the source of modulation signal of FSK modulation for the
              specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FSKey:SOURce?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:FSKey:SOURce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:FSKey:SOURce value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:FSKey:SOURce [INTernal|EXTernal]
            - SOURce2:FSKey:SOURce?
            ```
        """
        return self._source

    @property
    def state(self) -> Source2FskeyState:
        """Return the ``SOURce2:FSKey:STATe`` command.

        Description:
            - This command enables or disables FSK modulation. The query command returns the state
              of FSK modulation. You can select a sine, square, ramp, or arbitrary waveform for the
              carrier waveform.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FSKey:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:FSKey:STATe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:FSKey:STATe value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:FSKey:STATe {ON|OFF|<NR1>}
            - SOURce2:FSKey:STATe?
            ```
        """
        return self._state

    @property
    def frequency(self) -> Source2FskeyFrequency:
        """Return the ``SOURce2:FSKey:FREQuency`` command.

        Description:
            - This command sets or queries the hop frequency of FSK modulation for the specified
              channel.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FSKey:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:FSKey:FREQuency?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:FSKey:FREQuency value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:FSKey:FREQuency {<frequency>|MINimum|MAXimum}
            - SOURce2:FSKey:FREQuency?
            ```
        """
        return self._frequency


class Source2FrequencyStop(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:FREQuency:STOP`` command.

    Description:
        - This command sets or queries the start frequency of sweep for the specified channel. This
          command is always used with the [SOURce[1|2]]``:FREQuency:STARt`` command. The setting
          range of stop frequency depends on the waveform selected for sweep. For more information
          on the setting range, refer to the AFG3000 Series Specifications and Performance
          Verification Technical Reference, which can be found on the Tektronix Web site
          (www.tektronix.com/downloads).

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FREQuency:STOP?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FREQuency:STOP?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:FREQuency:STOP value`` command.

    SCPI Syntax:
        ```
        - SOURce2:FREQuency:STOP {<frequency>|MINimum|MAXimum}
        - SOURce2:FREQuency:STOP?
        ```
    """


class Source2FrequencyStart(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:FREQuency:STARt`` command.

    Description:
        - This command sets or queries the start frequency of sweep for the specified channel. This
          command is always used with the [SOURce[1|2]]``:FREQuency:STOP`` command. The setting
          range of start frequency depends on the waveform selected for sweep. For more information
          on the setting range, refer to the specifications page of Quick Start User Manual.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FREQuency:STARt?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FREQuency:STARt?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:FREQuency:STARt value``
          command.

    SCPI Syntax:
        ```
        - SOURce2:FREQuency:STARt {<frequency>|MINimum|MAXimum}
        - SOURce2:FREQuency:STARt?
        ```
    """


class Source2FrequencySpan(SCPICmdWrite):
    """The ``SOURce2:FREQuency:SPAN`` command.

    Description:
        - This command sets or queries the span of frequency sweep for the specified channel. This
          command is always used with the [SOURce[1|2]]``:FREQuency:CENTer`` command. The setting
          range of frequency span depends on the waveform selected for sweep.

    Usage:
        - Using the ``.write(value)`` method will send the ``SOURce2:FREQuency:SPAN value`` command.

    SCPI Syntax:
        ```
        - SOURce2:FREQuency:SPAN {<frequency>|MINimum|MAXimum}
        ```
    """


class Source2FrequencyMode(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:FREQuency:MODE`` command.

    Description:
        - This command sets or queries the frequency sweep state. You can select sine, square, ramp,
          or arbitrary waveform for sweep. The arbitrary function generator automatically changes to
          the Continuous mode if any waveform is selected other than sine, square, ramp, or an
          arbitrary waveform.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FREQuency:MODE?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FREQuency:MODE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:FREQuency:MODE value`` command.

    SCPI Syntax:
        ```
        - SOURce2:FREQuency:MODE {CW|FIXed|SWEep}
        - SOURce2:FREQuency:MODE?
        ```
    """


class Source2FrequencyFixed(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:FREQuency:FIXed`` command.

    Description:
        - This command sets or queries the frequency of output waveform for the specified channel.
          This command is available when the Run Mode is set to other than Sweep. The setting range
          of output frequency depends on the type of output waveform. If you change the type of
          output waveform, it might change the output frequency because changing waveform types
          impacts on the setting range of output frequency. The resolution is 1 µHz or 12 digits.
          For more information on the setting range, refer to the AFG3000 Series Specifications and
          Performance Verification Technical Reference, which can be found on the Tektronix Web site
          (www.tektronix.com/downloads).

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FREQuency:FIXed?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FREQuency:FIXed?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:FREQuency:FIXed value``
          command.

    SCPI Syntax:
        ```
        - SOURce2:FREQuency:FIXed {<frequency>|MINimum|MAXimum}
        - SOURce2:FREQuency:FIXed?
        ```
    """


class Source2FrequencyCw(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:FREQuency:CW`` command.

    Description:
        - This command sets or queries the frequency of output waveform for the specified channel.
          This command is available when the Run Mode is set to other than Sweep. The setting range
          of output frequency depends on the type of output waveform. If you change the type of
          output waveform, it might change the output frequency because changing waveform types
          impacts on the setting range of output frequency. The resolution is 1 µHz or 12 digits.
          For more information on the setting range, refer to the AFG3000 Series Specifications and
          Performance Verification Technical Reference, which can be found on the Tektronix Web site
          (www.tektronix.com/downloads).

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FREQuency:CW?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FREQuency:CW?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:FREQuency:CW value`` command.

    SCPI Syntax:
        ```
        - SOURce2:FREQuency:CW {<frequency>|MINimum|MAXimum}
        - SOURce2:FREQuency:CW?
        ```
    """


class Source2FrequencyConcurrentState(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:FREQuency:CONCurrent:STATe`` command.

    Description:
        - This command enables or disables the function to copy the frequency (or period) of one
          channel to another channel. The [SOURce[1|2]]``:FREQuency:CONCurrent`` command copies the
          frequency (or period) of the channel specified by the header suffix to another channel. If
          you specify CH 1 with the header, the CH 1 frequency will be copied to CH 2. The
          [SOURce[1|2]]``:FREQuency:CONCurrent?`` command returns '0' (off) or '1' (on). If your
          arbitrary function generator is single-channel model, this command is not supported.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FREQuency:CONCurrent:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FREQuency:CONCurrent:STATe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce2:FREQuency:CONCurrent:STATe value`` command.

    SCPI Syntax:
        ```
        - SOURce2:FREQuency:CONCurrent:STATe {ON|OFF|<NR1>}
        - SOURce2:FREQuency:CONCurrent:STATe?
        ```
    """


class Source2FrequencyConcurrent(SCPICmdRead):
    """The ``SOURce2:FREQuency:CONCurrent`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FREQuency:CONCurrent?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FREQuency:CONCurrent?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``SOURce2:FREQuency:CONCurrent:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = Source2FrequencyConcurrentState(device, f"{self._cmd_syntax}:STATe")

    @property
    def state(self) -> Source2FrequencyConcurrentState:
        """Return the ``SOURce2:FREQuency:CONCurrent:STATe`` command.

        Description:
            - This command enables or disables the function to copy the frequency (or period) of one
              channel to another channel. The [SOURce[1|2]]``:FREQuency:CONCurrent`` command copies
              the frequency (or period) of the channel specified by the header suffix to another
              channel. If you specify CH 1 with the header, the CH 1 frequency will be copied to CH
              2. The [SOURce[1|2]]``:FREQuency:CONCurrent?`` command returns '0' (off) or '1' (on).
              If your arbitrary function generator is single-channel model, this command is not
              supported.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FREQuency:CONCurrent:STATe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce2:FREQuency:CONCurrent:STATe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce2:FREQuency:CONCurrent:STATe value`` command.

        SCPI Syntax:
            ```
            - SOURce2:FREQuency:CONCurrent:STATe {ON|OFF|<NR1>}
            - SOURce2:FREQuency:CONCurrent:STATe?
            ```
        """
        return self._state


class Source2FrequencyCenter(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:FREQuency:CENTer`` command.

    Description:
        - This command sets or queries the center frequency of sweep for the specified channel. This
          command is always used with the [SOURce[1|2]]``:FREQuency:SPAN`` command. The setting
          range of center frequency depends on the waveform selected for sweep.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FREQuency:CENTer?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FREQuency:CENTer?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:FREQuency:CENTer value``
          command.

    SCPI Syntax:
        ```
        - SOURce2:FREQuency:CENTer {<frequency>|MINimum|MAXimum}
        - SOURce2:FREQuency:CENTer?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class Source2Frequency(SCPICmdRead):
    """The ``SOURce2:FREQuency`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FREQuency?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.center``: The ``SOURce2:FREQuency:CENTer`` command.
        - ``.concurrent``: The ``SOURce2:FREQuency:CONCurrent`` command tree.
        - ``.mode``: The ``SOURce2:FREQuency:MODE`` command.
        - ``.span``: The ``SOURce2:FREQuency:SPAN`` command.
        - ``.start``: The ``SOURce2:FREQuency:STARt`` command.
        - ``.stop``: The ``SOURce2:FREQuency:STOP`` command.
        - ``.cw``: The ``SOURce2:FREQuency:CW`` command.
        - ``.fixed``: The ``SOURce2:FREQuency:FIXed`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._center = Source2FrequencyCenter(device, f"{self._cmd_syntax}:CENTer")
        self._concurrent = Source2FrequencyConcurrent(device, f"{self._cmd_syntax}:CONCurrent")
        self._mode = Source2FrequencyMode(device, f"{self._cmd_syntax}:MODE")
        self._span = Source2FrequencySpan(device, f"{self._cmd_syntax}:SPAN")
        self._start = Source2FrequencyStart(device, f"{self._cmd_syntax}:STARt")
        self._stop = Source2FrequencyStop(device, f"{self._cmd_syntax}:STOP")
        self._cw = Source2FrequencyCw(device, f"{self._cmd_syntax}:CW")
        self._fixed = Source2FrequencyFixed(device, f"{self._cmd_syntax}:FIXed")

    @property
    def center(self) -> Source2FrequencyCenter:
        """Return the ``SOURce2:FREQuency:CENTer`` command.

        Description:
            - This command sets or queries the center frequency of sweep for the specified channel.
              This command is always used with the [SOURce[1|2]]``:FREQuency:SPAN`` command. The
              setting range of center frequency depends on the waveform selected for sweep.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FREQuency:CENTer?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:FREQuency:CENTer?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:FREQuency:CENTer value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:FREQuency:CENTer {<frequency>|MINimum|MAXimum}
            - SOURce2:FREQuency:CENTer?
            ```
        """
        return self._center

    @property
    def concurrent(self) -> Source2FrequencyConcurrent:
        """Return the ``SOURce2:FREQuency:CONCurrent`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FREQuency:CONCurrent?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:FREQuency:CONCurrent?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``SOURce2:FREQuency:CONCurrent:STATe`` command.
        """
        return self._concurrent

    @property
    def mode(self) -> Source2FrequencyMode:
        """Return the ``SOURce2:FREQuency:MODE`` command.

        Description:
            - This command sets or queries the frequency sweep state. You can select sine, square,
              ramp, or arbitrary waveform for sweep. The arbitrary function generator automatically
              changes to the Continuous mode if any waveform is selected other than sine, square,
              ramp, or an arbitrary waveform.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FREQuency:MODE?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:FREQuency:MODE?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:FREQuency:MODE value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:FREQuency:MODE {CW|FIXed|SWEep}
            - SOURce2:FREQuency:MODE?
            ```
        """
        return self._mode

    @property
    def span(self) -> Source2FrequencySpan:
        """Return the ``SOURce2:FREQuency:SPAN`` command.

        Description:
            - This command sets or queries the span of frequency sweep for the specified channel.
              This command is always used with the [SOURce[1|2]]``:FREQuency:CENTer`` command. The
              setting range of frequency span depends on the waveform selected for sweep.

        Usage:
            - Using the ``.write(value)`` method will send the ``SOURce2:FREQuency:SPAN value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:FREQuency:SPAN {<frequency>|MINimum|MAXimum}
            ```
        """
        return self._span

    @property
    def start(self) -> Source2FrequencyStart:
        """Return the ``SOURce2:FREQuency:STARt`` command.

        Description:
            - This command sets or queries the start frequency of sweep for the specified channel.
              This command is always used with the [SOURce[1|2]]``:FREQuency:STOP`` command. The
              setting range of start frequency depends on the waveform selected for sweep. For more
              information on the setting range, refer to the specifications page of Quick Start User
              Manual.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FREQuency:STARt?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:FREQuency:STARt?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:FREQuency:STARt value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:FREQuency:STARt {<frequency>|MINimum|MAXimum}
            - SOURce2:FREQuency:STARt?
            ```
        """
        return self._start

    @property
    def stop(self) -> Source2FrequencyStop:
        """Return the ``SOURce2:FREQuency:STOP`` command.

        Description:
            - This command sets or queries the start frequency of sweep for the specified channel.
              This command is always used with the [SOURce[1|2]]``:FREQuency:STARt`` command. The
              setting range of stop frequency depends on the waveform selected for sweep. For more
              information on the setting range, refer to the AFG3000 Series Specifications and
              Performance Verification Technical Reference, which can be found on the Tektronix Web
              site (www.tektronix.com/downloads).

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FREQuency:STOP?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:FREQuency:STOP?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:FREQuency:STOP value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:FREQuency:STOP {<frequency>|MINimum|MAXimum}
            - SOURce2:FREQuency:STOP?
            ```
        """
        return self._stop

    @property
    def cw(self) -> Source2FrequencyCw:
        """Return the ``SOURce2:FREQuency:CW`` command.

        Description:
            - This command sets or queries the frequency of output waveform for the specified
              channel. This command is available when the Run Mode is set to other than Sweep. The
              setting range of output frequency depends on the type of output waveform. If you
              change the type of output waveform, it might change the output frequency because
              changing waveform types impacts on the setting range of output frequency. The
              resolution is 1 µHz or 12 digits. For more information on the setting range, refer to
              the AFG3000 Series Specifications and Performance Verification Technical Reference,
              which can be found on the Tektronix Web site (www.tektronix.com/downloads).

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FREQuency:CW?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:FREQuency:CW?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:FREQuency:CW value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:FREQuency:CW {<frequency>|MINimum|MAXimum}
            - SOURce2:FREQuency:CW?
            ```
        """
        return self._cw

    @property
    def fixed(self) -> Source2FrequencyFixed:
        """Return the ``SOURce2:FREQuency:FIXed`` command.

        Description:
            - This command sets or queries the frequency of output waveform for the specified
              channel. This command is available when the Run Mode is set to other than Sweep. The
              setting range of output frequency depends on the type of output waveform. If you
              change the type of output waveform, it might change the output frequency because
              changing waveform types impacts on the setting range of output frequency. The
              resolution is 1 µHz or 12 digits. For more information on the setting range, refer to
              the AFG3000 Series Specifications and Performance Verification Technical Reference,
              which can be found on the Tektronix Web site (www.tektronix.com/downloads).

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FREQuency:FIXed?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:FREQuency:FIXed?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:FREQuency:FIXed value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:FREQuency:FIXed {<frequency>|MINimum|MAXimum}
            - SOURce2:FREQuency:FIXed?
            ```
        """
        return self._fixed


class Source2FmState(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:FM:STATe`` command.

    Description:
        - This command enables or disables FM modulation. The query command returns the state of FM
          modulation.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FM:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FM:STATe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:FM:STATe value`` command.

    SCPI Syntax:
        ```
        - SOURce2:FM:STATe {ON|OFF|<NR1>}
        - SOURce2:FM:STATe?
        ```
    """


class Source2FmSource(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:FM:SOURce`` command.

    Description:
        - This command sets or queries the source of modulating signal of FM modulation for the
          specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FM:SOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FM:SOURce?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:FM:SOURce value`` command.

    SCPI Syntax:
        ```
        - SOURce2:FM:SOURce [INTernal|EXTernal]
        - SOURce2:FM:SOURce?
        ```
    """


class Source2FmInternalFunctionEfile(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:FM:INTernal:FUNCtion:EFILe`` command.

    Description:
        - This command sets or queries an EFILe name used as a modulating waveform for FM
          modulation. A file name must be specified in the mass storage system. This command returns
          ' ' if there is no file in the mass storage.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FM:INTernal:FUNCtion:EFILe?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FM:INTernal:FUNCtion:EFILe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce2:FM:INTernal:FUNCtion:EFILe value`` command.

    SCPI Syntax:
        ```
        - SOURce2:FM:INTernal:FUNCtion:EFILe <file_name>
        - SOURce2:FM:INTernal:FUNCtion:EFILe?
        ```
    """


class Source2FmInternalFunction(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:FM:INTernal:FUNCtion`` command.

    Description:
        - This command sets or queries the modulating waveform of FM modulation for the specified
          channel. You can use this command only when the internal modulation source is selected. If
          you specify EFILe when there is no EFILe or the EFILe is not yet defined, this command
          causes an error.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FM:INTernal:FUNCtion?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FM:INTernal:FUNCtion?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:FM:INTernal:FUNCtion value``
          command.

    SCPI Syntax:
        ```
        - SOURce2:FM:INTernal:FUNCtion {SINusoid|SQUare|TRIangle|RAMP|NRAMp|PRNoise|USER[1]|USER<x>|EMEMory[1]|EMEMory2|EFILe}
        - SOURce2:FM:INTernal:FUNCtion?
        ```

    Info:
        - ``SINusoid``
        - ``SQUare``
        - ``TRIangle``
        - ``RAMP``
        - ``NRAMp``
        - ``PRNoise``
        - ``USER[1]``
        - ``USER2``
        - ``USER3``
        - ``USER4``
        - ``EMEMory[1]``
        - ``EMEMory2``
        - ``EFILe``

    Properties:
        - ``.efile``: The ``SOURce2:FM:INTernal:FUNCtion:EFILe`` command.
    """  # noqa: E501

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._efile = Source2FmInternalFunctionEfile(device, f"{self._cmd_syntax}:EFILe")

    @property
    def efile(self) -> Source2FmInternalFunctionEfile:
        """Return the ``SOURce2:FM:INTernal:FUNCtion:EFILe`` command.

        Description:
            - This command sets or queries an EFILe name used as a modulating waveform for FM
              modulation. A file name must be specified in the mass storage system. This command
              returns ' ' if there is no file in the mass storage.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FM:INTernal:FUNCtion:EFILe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce2:FM:INTernal:FUNCtion:EFILe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce2:FM:INTernal:FUNCtion:EFILe value`` command.

        SCPI Syntax:
            ```
            - SOURce2:FM:INTernal:FUNCtion:EFILe <file_name>
            - SOURce2:FM:INTernal:FUNCtion:EFILe?
            ```
        """
        return self._efile


class Source2FmInternalFrequency(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:FM:INTernal:FREQuency`` command.

    Description:
        - This command sets or queries the internal modulation frequency of FM modulation for the
          specified channel. You can use this command only when the internal modulation source is
          selected. You can set the internal modulation frequency from 2 mHz to 50.00 kHz with
          resolution of 1 mHz. You can select the source of modulating signal by using the
          [SOURce[1|2]]``:FM:SOURce`` [INTernal|EXTernal] command.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FM:INTernal:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FM:INTernal:FREQuency?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:FM:INTernal:FREQuency value``
          command.

    SCPI Syntax:
        ```
        - SOURce2:FM:INTernal:FREQuency {<frequency>|MINimum|MAXimum}
        - SOURce2:FM:INTernal:FREQuency?
        ```
    """


class Source2FmInternal(SCPICmdRead):
    """The ``SOURce2:FM:INTernal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FM:INTernal?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FM:INTernal?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.frequency``: The ``SOURce2:FM:INTernal:FREQuency`` command.
        - ``.function``: The ``SOURce2:FM:INTernal:FUNCtion`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._frequency = Source2FmInternalFrequency(device, f"{self._cmd_syntax}:FREQuency")
        self._function = Source2FmInternalFunction(device, f"{self._cmd_syntax}:FUNCtion")

    @property
    def frequency(self) -> Source2FmInternalFrequency:
        """Return the ``SOURce2:FM:INTernal:FREQuency`` command.

        Description:
            - This command sets or queries the internal modulation frequency of FM modulation for
              the specified channel. You can use this command only when the internal modulation
              source is selected. You can set the internal modulation frequency from 2 mHz to 50.00
              kHz with resolution of 1 mHz. You can select the source of modulating signal by using
              the [SOURce[1|2]]``:FM:SOURce`` [INTernal|EXTernal] command.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FM:INTernal:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:FM:INTernal:FREQuency?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce2:FM:INTernal:FREQuency value`` command.

        SCPI Syntax:
            ```
            - SOURce2:FM:INTernal:FREQuency {<frequency>|MINimum|MAXimum}
            - SOURce2:FM:INTernal:FREQuency?
            ```
        """
        return self._frequency

    @property
    def function(self) -> Source2FmInternalFunction:
        """Return the ``SOURce2:FM:INTernal:FUNCtion`` command.

        Description:
            - This command sets or queries the modulating waveform of FM modulation for the
              specified channel. You can use this command only when the internal modulation source
              is selected. If you specify EFILe when there is no EFILe or the EFILe is not yet
              defined, this command causes an error.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FM:INTernal:FUNCtion?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:FM:INTernal:FUNCtion?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce2:FM:INTernal:FUNCtion value`` command.

        SCPI Syntax:
            ```
            - SOURce2:FM:INTernal:FUNCtion {SINusoid|SQUare|TRIangle|RAMP|NRAMp|PRNoise|USER[1]|USER<x>|EMEMory[1]|EMEMory2|EFILe}
            - SOURce2:FM:INTernal:FUNCtion?
            ```

        Info:
            - ``SINusoid``
            - ``SQUare``
            - ``TRIangle``
            - ``RAMP``
            - ``NRAMp``
            - ``PRNoise``
            - ``USER[1]``
            - ``USER2``
            - ``USER3``
            - ``USER4``
            - ``EMEMory[1]``
            - ``EMEMory2``
            - ``EFILe``

        Sub-properties:
            - ``.efile``: The ``SOURce2:FM:INTernal:FUNCtion:EFILe`` command.
        """  # noqa: E501
        return self._function


class Source2FmDeviation(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:FM:DEViation`` command.

    Description:
        - This command sets or queries the peak frequency deviation of FM modulation for the
          specified channel. The setting range of frequency deviation depends on the waveform
          selected as the carrier. For more information, refer to the specifications in the AFG3000
          Series Specifications and Performance Verification Technical Reference, which can be found
          on the Tektronix Web site (www.tektronix.com/downloads).

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FM:DEViation?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FM:DEViation?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:FM:DEViation value`` command.

    SCPI Syntax:
        ```
        - SOURce2:FM:DEViation {<deviation>|MINimum|MAXimum}
        - SOURce2:FM:DEViation?
        ```
    """


class Source2Fm(SCPICmdRead):
    """The ``SOURce2:FM`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:FM?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:FM?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.internal``: The ``SOURce2:FM:INTernal`` command tree.
        - ``.source``: The ``SOURce2:FM:SOURce`` command.
        - ``.state``: The ``SOURce2:FM:STATe`` command.
        - ``.deviation``: The ``SOURce2:FM:DEViation`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._internal = Source2FmInternal(device, f"{self._cmd_syntax}:INTernal")
        self._source = Source2FmSource(device, f"{self._cmd_syntax}:SOURce")
        self._state = Source2FmState(device, f"{self._cmd_syntax}:STATe")
        self._deviation = Source2FmDeviation(device, f"{self._cmd_syntax}:DEViation")

    @property
    def internal(self) -> Source2FmInternal:
        """Return the ``SOURce2:FM:INTernal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FM:INTernal?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:FM:INTernal?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.frequency``: The ``SOURce2:FM:INTernal:FREQuency`` command.
            - ``.function``: The ``SOURce2:FM:INTernal:FUNCtion`` command.
        """
        return self._internal

    @property
    def source(self) -> Source2FmSource:
        """Return the ``SOURce2:FM:SOURce`` command.

        Description:
            - This command sets or queries the source of modulating signal of FM modulation for the
              specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FM:SOURce?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:FM:SOURce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:FM:SOURce value`` command.

        SCPI Syntax:
            ```
            - SOURce2:FM:SOURce [INTernal|EXTernal]
            - SOURce2:FM:SOURce?
            ```
        """
        return self._source

    @property
    def state(self) -> Source2FmState:
        """Return the ``SOURce2:FM:STATe`` command.

        Description:
            - This command enables or disables FM modulation. The query command returns the state of
              FM modulation.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FM:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:FM:STATe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:FM:STATe value`` command.

        SCPI Syntax:
            ```
            - SOURce2:FM:STATe {ON|OFF|<NR1>}
            - SOURce2:FM:STATe?
            ```
        """
        return self._state

    @property
    def deviation(self) -> Source2FmDeviation:
        """Return the ``SOURce2:FM:DEViation`` command.

        Description:
            - This command sets or queries the peak frequency deviation of FM modulation for the
              specified channel. The setting range of frequency deviation depends on the waveform
              selected as the carrier. For more information, refer to the specifications in the
              AFG3000 Series Specifications and Performance Verification Technical Reference, which
              can be found on the Tektronix Web site (www.tektronix.com/downloads).

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FM:DEViation?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:FM:DEViation?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:FM:DEViation value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:FM:DEViation {<deviation>|MINimum|MAXimum}
            - SOURce2:FM:DEViation?
            ```
        """
        return self._deviation


class Source2CombineFeed(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:COMBine:FEED`` command.

    Description:
        - This command sets or queries whether to add the internal noise or an external signal to an
          output signal for the specified channel. When you specify the internal noise, you can set
          or query the noise level by
          SOURce<3|``4>:POWer``[``:LEVel``][``:IMMediate``][``:AMPLitude``] command. To disable the
          internal noise add or the external signal add function, specify ''. You can add an
          external signal to the CH 1 output signal of the AFG3100 and AFG3200 series arbitrary
          function generators. The CH 2 output is not available for adding external signal. Both the
          internal noise and an external signal can be added simultaneously to the arbitrary
          function generator.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:COMBine:FEED?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:COMBine:FEED?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:COMBine:FEED value`` command.

    SCPI Syntax:
        ```
        - SOURce2:COMBine:FEED ['NOISe'|'EXTernal'|'BOTH'|'']
        - SOURce2:COMBine:FEED?
        ```
    """


class Source2Combine(SCPICmdRead):
    """The ``SOURce2:COMBine`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:COMBine?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:COMBine?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.feed``: The ``SOURce2:COMBine:FEED`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._feed = Source2CombineFeed(device, f"{self._cmd_syntax}:FEED")

    @property
    def feed(self) -> Source2CombineFeed:
        """Return the ``SOURce2:COMBine:FEED`` command.

        Description:
            - This command sets or queries whether to add the internal noise or an external signal
              to an output signal for the specified channel. When you specify the internal noise,
              you can set or query the noise level by
              SOURce<3|``4>:POWer``[``:LEVel``][``:IMMediate``][``:AMPLitude``] command. To disable
              the internal noise add or the external signal add function, specify ''. You can add an
              external signal to the CH 1 output signal of the AFG3100 and AFG3200 series arbitrary
              function generators. The CH 2 output is not available for adding external signal. Both
              the internal noise and an external signal can be added simultaneously to the arbitrary
              function generator.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:COMBine:FEED?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:COMBine:FEED?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:COMBine:FEED value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:COMBine:FEED ['NOISe'|'EXTernal'|'BOTH'|'']
            - SOURce2:COMBine:FEED?
            ```
        """
        return self._feed


class Source2BurstTdelay(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:BURSt:TDELay`` command.

    Description:
        - This command sets or queries delay time in the burst mode for the specified channel. It
          specifies a time delay between the trigger and the signal output. This command is
          available only in the Triggered burst mode. The setting range is 0.0 ns to 85.000 s with
          resolution of 100 ps or 5 digits.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:BURSt:TDELay?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:BURSt:TDELay?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:BURSt:TDELay value`` command.

    SCPI Syntax:
        ```
        - SOURce2:BURSt:TDELay {<delay>|MINimum|MAXimum}
        - SOURce2:BURSt:TDELay?
        ```
    """


class Source2BurstState(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:BURSt:STATe`` command.

    Description:
        - This command enables or disables the burst mode for the specified channel. The query
          command returns the state of burst mode.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:BURSt:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:BURSt:STATe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:BURSt:STATe value`` command.

    SCPI Syntax:
        ```
        - SOURce2:BURSt:STATe {ON|OFF|<NR1>}
        - SOURce2:BURSt:STATe?
        ```
    """


class Source2BurstNcycles(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:BURSt:NCYCles`` command.

    Description:
        - This command sets or queries the number of cycles (burst count) to be output in burst mode
          for the specified channel. The query command returns 9.9E+37 if the burst count is set to
          INFinity.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:BURSt:NCYCles?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:BURSt:NCYCles?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:BURSt:NCYCles value`` command.

    SCPI Syntax:
        ```
        - SOURce2:BURSt:NCYCles {<cycles>|INFinity|MINimum|MAXimum}
        - SOURce2:BURSt:NCYCles?
        ```
    """


class Source2BurstMode(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:BURSt:MODE`` command.

    Description:
        - This command sets or queries the burst mode for the specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:BURSt:MODE?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:BURSt:MODE?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:BURSt:MODE value`` command.

    SCPI Syntax:
        ```
        - SOURce2:BURSt:MODE {TRIGgered|GATed}
        - SOURce2:BURSt:MODE?
        ```
    """


class Source2Burst(SCPICmdRead):
    """The ``SOURce2:BURSt`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:BURSt?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:BURSt?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.mode``: The ``SOURce2:BURSt:MODE`` command.
        - ``.ncycles``: The ``SOURce2:BURSt:NCYCles`` command.
        - ``.tdelay``: The ``SOURce2:BURSt:TDELay`` command.
        - ``.state``: The ``SOURce2:BURSt:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = Source2BurstMode(device, f"{self._cmd_syntax}:MODE")
        self._ncycles = Source2BurstNcycles(device, f"{self._cmd_syntax}:NCYCles")
        self._tdelay = Source2BurstTdelay(device, f"{self._cmd_syntax}:TDELay")
        self._state = Source2BurstState(device, f"{self._cmd_syntax}:STATe")

    @property
    def mode(self) -> Source2BurstMode:
        """Return the ``SOURce2:BURSt:MODE`` command.

        Description:
            - This command sets or queries the burst mode for the specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:BURSt:MODE?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:BURSt:MODE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:BURSt:MODE value`` command.

        SCPI Syntax:
            ```
            - SOURce2:BURSt:MODE {TRIGgered|GATed}
            - SOURce2:BURSt:MODE?
            ```
        """
        return self._mode

    @property
    def ncycles(self) -> Source2BurstNcycles:
        """Return the ``SOURce2:BURSt:NCYCles`` command.

        Description:
            - This command sets or queries the number of cycles (burst count) to be output in burst
              mode for the specified channel. The query command returns 9.9E+37 if the burst count
              is set to INFinity.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:BURSt:NCYCles?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:BURSt:NCYCles?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:BURSt:NCYCles value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:BURSt:NCYCles {<cycles>|INFinity|MINimum|MAXimum}
            - SOURce2:BURSt:NCYCles?
            ```
        """
        return self._ncycles

    @property
    def tdelay(self) -> Source2BurstTdelay:
        """Return the ``SOURce2:BURSt:TDELay`` command.

        Description:
            - This command sets or queries delay time in the burst mode for the specified channel.
              It specifies a time delay between the trigger and the signal output. This command is
              available only in the Triggered burst mode. The setting range is 0.0 ns to 85.000 s
              with resolution of 100 ps or 5 digits.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:BURSt:TDELay?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:BURSt:TDELay?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:BURSt:TDELay value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:BURSt:TDELay {<delay>|MINimum|MAXimum}
            - SOURce2:BURSt:TDELay?
            ```
        """
        return self._tdelay

    @property
    def state(self) -> Source2BurstState:
        """Return the ``SOURce2:BURSt:STATe`` command.

        Description:
            - This command enables or disables the burst mode for the specified channel. The query
              command returns the state of burst mode.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:BURSt:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:BURSt:STATe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:BURSt:STATe value``
              command.

        SCPI Syntax:
            ```
            - SOURce2:BURSt:STATe {ON|OFF|<NR1>}
            - SOURce2:BURSt:STATe?
            ```
        """
        return self._state


class Source2AmState(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:AM:STATe`` command.

    Description:
        - This command enables or disables AM modulation for the specified channel. The query
          command returns the state of AM modulation.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:AM:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:AM:STATe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:AM:STATe value`` command.

    SCPI Syntax:
        ```
        - SOURce2:AM:STATe {ON|OFF|<NR1>}
        - SOURce2:AM:STATe?
        ```
    """


class Source2AmSource(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:AM:SOURce`` command.

    Description:
        - This command sets or queries the source of modulating signal of AM modulation for the
          specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:AM:SOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:AM:SOURce?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:AM:SOURce value`` command.

    SCPI Syntax:
        ```
        - SOURce2:AM:SOURce [INTernal|EXTernal]
        - SOURce2:AM:SOURce?
        ```
    """


class Source2AmInternalFunctionEfile(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:AM:INTernal:FUNCtion:EFILe`` command.

    Description:
        - This command sets or queries an EFILe name used as a modulating waveform for AM
          modulation. A file name must be specified in the mass storage system. This command returns
          ' ' if there is no file in the mass storage.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:AM:INTernal:FUNCtion:EFILe?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:AM:INTernal:FUNCtion:EFILe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce2:AM:INTernal:FUNCtion:EFILe value`` command.

    SCPI Syntax:
        ```
        - SOURce2:AM:INTernal:FUNCtion:EFILe <file_name>
        - SOURce2:AM:INTernal:FUNCtion:EFILe?
        ```
    """


class Source2AmInternalFunction(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:AM:INTernal:FUNCtion`` command.

    Description:
        - This command sets or queries the modulating waveform of AM modulation for the specified
          channel. You can use this command only when the internal modulation source is selected. If
          you specify EFILe when there is no EFILe or the EFILe is not yet defined, this command
          causes an error.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:AM:INTernal:FUNCtion?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:AM:INTernal:FUNCtion?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:AM:INTernal:FUNCtion value``
          command.

    SCPI Syntax:
        ```
        - SOURce2:AM:INTernal:FUNCtion {SINusoid|SQUare|TRIangle|RAMP|NRAMp|PRNoise|USER[1]|USER<x>|EMEMory[1]|EMEMory2|EFILe}
        - SOURce2:AM:INTernal:FUNCtion?
        ```

    Info:
        - ``SINusoid``
        - ``SQUare``
        - ``TRIangle``
        - ``RAMP``
        - ``NRAMp``
        - ``PRNoise``
        - ``USER[1]``
        - ``USER2``
        - ``USER3``
        - ``USER4``
        - ``EMEMory[1]``
        - ``EMEMory2``
        - ``EFILe``

    Properties:
        - ``.efile``: The ``SOURce2:AM:INTernal:FUNCtion:EFILe`` command.
    """  # noqa: E501

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._efile = Source2AmInternalFunctionEfile(device, f"{self._cmd_syntax}:EFILe")

    @property
    def efile(self) -> Source2AmInternalFunctionEfile:
        """Return the ``SOURce2:AM:INTernal:FUNCtion:EFILe`` command.

        Description:
            - This command sets or queries an EFILe name used as a modulating waveform for AM
              modulation. A file name must be specified in the mass storage system. This command
              returns ' ' if there is no file in the mass storage.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:AM:INTernal:FUNCtion:EFILe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce2:AM:INTernal:FUNCtion:EFILe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce2:AM:INTernal:FUNCtion:EFILe value`` command.

        SCPI Syntax:
            ```
            - SOURce2:AM:INTernal:FUNCtion:EFILe <file_name>
            - SOURce2:AM:INTernal:FUNCtion:EFILe?
            ```
        """
        return self._efile


class Source2AmInternalFrequency(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:AM:INTernal:FREQuency`` command.

    Description:
        - This command sets or queries the internal modulation frequency of AM modulation for the
          specified channel. You can use this command only when the internal modulation source is
          selected. You can set the internal modulation frequency from 2 mHz to 50.00 kHz with
          resolution of 1 mHz. You can select the source of modulating signal by using the
          [SOURce[1|2]]``:AM:SOURce`` [INTernal|EXTernal] command.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:AM:INTernal:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:AM:INTernal:FREQuency?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:AM:INTernal:FREQuency value``
          command.

    SCPI Syntax:
        ```
        - SOURce2:AM:INTernal:FREQuency {<frequency>|MINimum|MAXimum}
        - SOURce2:AM:INTernal:FREQuency?
        ```
    """


class Source2AmInternal(SCPICmdRead):
    """The ``SOURce2:AM:INTernal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:AM:INTernal?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:AM:INTernal?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.frequency``: The ``SOURce2:AM:INTernal:FREQuency`` command.
        - ``.function``: The ``SOURce2:AM:INTernal:FUNCtion`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._frequency = Source2AmInternalFrequency(device, f"{self._cmd_syntax}:FREQuency")
        self._function = Source2AmInternalFunction(device, f"{self._cmd_syntax}:FUNCtion")

    @property
    def frequency(self) -> Source2AmInternalFrequency:
        """Return the ``SOURce2:AM:INTernal:FREQuency`` command.

        Description:
            - This command sets or queries the internal modulation frequency of AM modulation for
              the specified channel. You can use this command only when the internal modulation
              source is selected. You can set the internal modulation frequency from 2 mHz to 50.00
              kHz with resolution of 1 mHz. You can select the source of modulating signal by using
              the [SOURce[1|2]]``:AM:SOURce`` [INTernal|EXTernal] command.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:AM:INTernal:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:AM:INTernal:FREQuency?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce2:AM:INTernal:FREQuency value`` command.

        SCPI Syntax:
            ```
            - SOURce2:AM:INTernal:FREQuency {<frequency>|MINimum|MAXimum}
            - SOURce2:AM:INTernal:FREQuency?
            ```
        """
        return self._frequency

    @property
    def function(self) -> Source2AmInternalFunction:
        """Return the ``SOURce2:AM:INTernal:FUNCtion`` command.

        Description:
            - This command sets or queries the modulating waveform of AM modulation for the
              specified channel. You can use this command only when the internal modulation source
              is selected. If you specify EFILe when there is no EFILe or the EFILe is not yet
              defined, this command causes an error.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:AM:INTernal:FUNCtion?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:AM:INTernal:FUNCtion?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce2:AM:INTernal:FUNCtion value`` command.

        SCPI Syntax:
            ```
            - SOURce2:AM:INTernal:FUNCtion {SINusoid|SQUare|TRIangle|RAMP|NRAMp|PRNoise|USER[1]|USER<x>|EMEMory[1]|EMEMory2|EFILe}
            - SOURce2:AM:INTernal:FUNCtion?
            ```

        Info:
            - ``SINusoid``
            - ``SQUare``
            - ``TRIangle``
            - ``RAMP``
            - ``NRAMp``
            - ``PRNoise``
            - ``USER[1]``
            - ``USER2``
            - ``USER3``
            - ``USER4``
            - ``EMEMory[1]``
            - ``EMEMory2``
            - ``EFILe``

        Sub-properties:
            - ``.efile``: The ``SOURce2:AM:INTernal:FUNCtion:EFILe`` command.
        """  # noqa: E501
        return self._function


class Source2AmDepth(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce2:AM:DEPTh`` command.

    Description:
        - This command sets or queries the modulation depth of AM modulation for the specified
          channel. You can set the modulation depth from 0.0% to 120.0% with resolution of 0.1%.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:AM:DEPTh?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:AM:DEPTh?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce2:AM:DEPTh value`` command.

    SCPI Syntax:
        ```
        - SOURce2:AM:DEPTh {<depth>|MINimum|MAXimum}
        - SOURce2:AM:DEPTh?
        ```
    """


class Source2Am(SCPICmdRead):
    """The ``SOURce2:AM`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2:AM?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2:AM?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.internal``: The ``SOURce2:AM:INTernal`` command tree.
        - ``.source``: The ``SOURce2:AM:SOURce`` command.
        - ``.state``: The ``SOURce2:AM:STATe`` command.
        - ``.depth``: The ``SOURce2:AM:DEPTh`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._internal = Source2AmInternal(device, f"{self._cmd_syntax}:INTernal")
        self._source = Source2AmSource(device, f"{self._cmd_syntax}:SOURce")
        self._state = Source2AmState(device, f"{self._cmd_syntax}:STATe")
        self._depth = Source2AmDepth(device, f"{self._cmd_syntax}:DEPTh")

    @property
    def internal(self) -> Source2AmInternal:
        """Return the ``SOURce2:AM:INTernal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:AM:INTernal?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:AM:INTernal?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.frequency``: The ``SOURce2:AM:INTernal:FREQuency`` command.
            - ``.function``: The ``SOURce2:AM:INTernal:FUNCtion`` command.
        """
        return self._internal

    @property
    def source(self) -> Source2AmSource:
        """Return the ``SOURce2:AM:SOURce`` command.

        Description:
            - This command sets or queries the source of modulating signal of AM modulation for the
              specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:AM:SOURce?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:AM:SOURce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:AM:SOURce value`` command.

        SCPI Syntax:
            ```
            - SOURce2:AM:SOURce [INTernal|EXTernal]
            - SOURce2:AM:SOURce?
            ```
        """
        return self._source

    @property
    def state(self) -> Source2AmState:
        """Return the ``SOURce2:AM:STATe`` command.

        Description:
            - This command enables or disables AM modulation for the specified channel. The query
              command returns the state of AM modulation.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:AM:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:AM:STATe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:AM:STATe value`` command.

        SCPI Syntax:
            ```
            - SOURce2:AM:STATe {ON|OFF|<NR1>}
            - SOURce2:AM:STATe?
            ```
        """
        return self._state

    @property
    def depth(self) -> Source2AmDepth:
        """Return the ``SOURce2:AM:DEPTh`` command.

        Description:
            - This command sets or queries the modulation depth of AM modulation for the specified
              channel. You can set the modulation depth from 0.0% to 120.0% with resolution of 0.1%.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:AM:DEPTh?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:AM:DEPTh?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce2:AM:DEPTh value`` command.

        SCPI Syntax:
            ```
            - SOURce2:AM:DEPTh {<depth>|MINimum|MAXimum}
            - SOURce2:AM:DEPTh?
            ```
        """
        return self._depth


#  pylint: disable=too-many-instance-attributes
class Source2(SCPICmdRead):
    """The ``SOURce2`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce2?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce2?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.am``: The ``SOURce2:AM`` command tree.
        - ``.burst``: The ``SOURce2:BURSt`` command tree.
        - ``.combine``: The ``SOURce2:COMBine`` command tree.
        - ``.fm``: The ``SOURce2:FM`` command tree.
        - ``.frequency``: The ``SOURce2:FREQuency`` command tree.
        - ``.fskey``: The ``SOURce2:FSKey`` command tree.
        - ``.function``: The ``SOURce2:FUNCtion`` command tree.
        - ``.phase``: The ``SOURce2:PHASe`` command tree.
        - ``.pm``: The ``SOURce2:PM`` command tree.
        - ``.pulse``: The ``SOURce2:PULSe`` command tree.
        - ``.pwm``: The ``SOURce2:PWM`` command tree.
        - ``.sweep``: The ``SOURce2:SWEep`` command tree.
        - ``.voltage``: The ``SOURce2:VOLTage`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SOURce2") -> None:
        super().__init__(device, cmd_syntax)
        self._am = Source2Am(device, f"{self._cmd_syntax}:AM")
        self._burst = Source2Burst(device, f"{self._cmd_syntax}:BURSt")
        self._combine = Source2Combine(device, f"{self._cmd_syntax}:COMBine")
        self._fm = Source2Fm(device, f"{self._cmd_syntax}:FM")
        self._frequency = Source2Frequency(device, f"{self._cmd_syntax}:FREQuency")
        self._fskey = Source2Fskey(device, f"{self._cmd_syntax}:FSKey")
        self._function = Source2Function(device, f"{self._cmd_syntax}:FUNCtion")
        self._phase = Source2Phase(device, f"{self._cmd_syntax}:PHASe")
        self._pm = Source2Pm(device, f"{self._cmd_syntax}:PM")
        self._pulse = Source2Pulse(device, f"{self._cmd_syntax}:PULSe")
        self._pwm = Source2Pwm(device, f"{self._cmd_syntax}:PWM")
        self._sweep = Source2Sweep(device, f"{self._cmd_syntax}:SWEep")
        self._voltage = Source2Voltage(device, f"{self._cmd_syntax}:VOLTage")

    @property
    def am(self) -> Source2Am:
        """Return the ``SOURce2:AM`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:AM?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:AM?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.internal``: The ``SOURce2:AM:INTernal`` command tree.
            - ``.source``: The ``SOURce2:AM:SOURce`` command.
            - ``.state``: The ``SOURce2:AM:STATe`` command.
            - ``.depth``: The ``SOURce2:AM:DEPTh`` command.
        """
        return self._am

    @property
    def burst(self) -> Source2Burst:
        """Return the ``SOURce2:BURSt`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:BURSt?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:BURSt?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.mode``: The ``SOURce2:BURSt:MODE`` command.
            - ``.ncycles``: The ``SOURce2:BURSt:NCYCles`` command.
            - ``.tdelay``: The ``SOURce2:BURSt:TDELay`` command.
            - ``.state``: The ``SOURce2:BURSt:STATe`` command.
        """
        return self._burst

    @property
    def combine(self) -> Source2Combine:
        """Return the ``SOURce2:COMBine`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:COMBine?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:COMBine?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.feed``: The ``SOURce2:COMBine:FEED`` command.
        """
        return self._combine

    @property
    def fm(self) -> Source2Fm:
        """Return the ``SOURce2:FM`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FM?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:FM?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.internal``: The ``SOURce2:FM:INTernal`` command tree.
            - ``.source``: The ``SOURce2:FM:SOURce`` command.
            - ``.state``: The ``SOURce2:FM:STATe`` command.
            - ``.deviation``: The ``SOURce2:FM:DEViation`` command.
        """
        return self._fm

    @property
    def frequency(self) -> Source2Frequency:
        """Return the ``SOURce2:FREQuency`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:FREQuency?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.center``: The ``SOURce2:FREQuency:CENTer`` command.
            - ``.concurrent``: The ``SOURce2:FREQuency:CONCurrent`` command tree.
            - ``.mode``: The ``SOURce2:FREQuency:MODE`` command.
            - ``.span``: The ``SOURce2:FREQuency:SPAN`` command.
            - ``.start``: The ``SOURce2:FREQuency:STARt`` command.
            - ``.stop``: The ``SOURce2:FREQuency:STOP`` command.
            - ``.cw``: The ``SOURce2:FREQuency:CW`` command.
            - ``.fixed``: The ``SOURce2:FREQuency:FIXed`` command.
        """
        return self._frequency

    @property
    def fskey(self) -> Source2Fskey:
        """Return the ``SOURce2:FSKey`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FSKey?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:FSKey?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.internal``: The ``SOURce2:FSKey:INTernal`` command tree.
            - ``.source``: The ``SOURce2:FSKey:SOURce`` command.
            - ``.state``: The ``SOURce2:FSKey:STATe`` command.
            - ``.frequency``: The ``SOURce2:FSKey:FREQuency`` command.
        """
        return self._fskey

    @property
    def function(self) -> Source2Function:
        """Return the ``SOURce2:FUNCtion`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:FUNCtion?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:FUNCtion?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.efile``: The ``SOURce2:FUNCtion:EFILe`` command.
            - ``.ramp``: The ``SOURce2:FUNCtion:RAMP`` command tree.
            - ``.shape``: The ``SOURce2:FUNCtion:SHAPe`` command.
        """
        return self._function

    @property
    def phase(self) -> Source2Phase:
        """Return the ``SOURce2:PHASe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PHASe?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:PHASe?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.initiate``: The ``SOURce2:PHASe:INITiate`` command.
            - ``.adjust``: The ``SOURce2:PHASe:ADJust`` command.
        """
        return self._phase

    @property
    def pm(self) -> Source2Pm:
        """Return the ``SOURce2:PM`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PM?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:PM?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.internal``: The ``SOURce2:PM:INTernal`` command tree.
            - ``.source``: The ``SOURce2:PM:SOURce`` command.
            - ``.state``: The ``SOURce2:PM:STATe`` command.
            - ``.deviation``: The ``SOURce2:PM:DEViation`` command.
        """
        return self._pm

    @property
    def pulse(self) -> Source2Pulse:
        """Return the ``SOURce2:PULSe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PULSe?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:PULSe?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.dcycle``: The ``SOURce2:PULSe:DCYCle`` command.
            - ``.delay``: The ``SOURce2:PULSe:DELay`` command.
            - ``.hold``: The ``SOURce2:PULSe:HOLD`` command.
            - ``.period``: The ``SOURce2:PULSe:PERiod`` command.
            - ``.transition``: The ``SOURce2:PULSe:TRANsition`` command tree.
            - ``.width``: The ``SOURce2:PULSe:WIDTh`` command.
        """
        return self._pulse

    @property
    def pwm(self) -> Source2Pwm:
        """Return the ``SOURce2:PWM`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:PWM?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:PWM?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.internal``: The ``SOURce2:PWM:INTernal`` command tree.
            - ``.source``: The ``SOURce2:PWM:SOURce`` command.
            - ``.state``: The ``SOURce2:PWM:STATe`` command.
            - ``.deviation``: The ``SOURce2:PWM:DEViation`` command tree.
        """
        return self._pwm

    @property
    def sweep(self) -> Source2Sweep:
        """Return the ``SOURce2:SWEep`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:SWEep?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:SWEep?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.htime``: The ``SOURce2:SWEep:HTIMe`` command.
            - ``.mode``: The ``SOURce2:SWEep:MODE`` command.
            - ``.rtime``: The ``SOURce2:SWEep:RTIMe`` command.
            - ``.spacing``: The ``SOURce2:SWEep:SPACing`` command.
            - ``.time``: The ``SOURce2:SWEep:TIME`` command.
        """
        return self._sweep

    @property
    def voltage(self) -> Source2Voltage:
        """Return the ``SOURce2:VOLTage`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2:VOLTage?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2:VOLTage?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.concurrent``: The ``SOURce2:VOLTage:CONCurrent`` command tree.
            - ``.limit``: The ``SOURce2:VOLTage:LIMit`` command tree.
            - ``.unit``: The ``SOURce2:VOLTage:UNIT`` command.
            - ``.level``: The ``SOURce2:VOLTage:LEVel`` command tree.
        """
        return self._voltage
