"""The source commands module.

These commands are used in the following models:
AWG70KA, AWG70KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SOURce:FREQuency <frequency>
    - SOURce:FREQuency?
    - SOURce:RCCouple {0|1|ON|OFF}
    - SOURce:RCCouple?
    - SOURce:ROSCillator:MULTiplier <NR1>
    - SOURce:ROSCillator:MULTiplier?
    - SOURce[n]:CASSet:SEQuence <sequence_name>, <track_number>[,<component_type>]
    - SOURce[n]:CASSet:TYPE?
    - SOURce[n]:CASSet:WAVeform <wfm_name>[, <component_type>]
    - SOURce[n]:CASSet?
    - SOURce[n]:DAC:RESolution {8|9|10}
    - SOURce[n]:DAC:RESolution?
    - SOURce[n]:JUMP:FORCe {FIRSt|CURRent|LAST|END|<NR1>}
    - SOURce[n]:JUMP:PATTern:FORCe <pattern>
    - SOURce[n]:MARKer[m]:DELay <NR3>
    - SOURce[n]:MARKer[m]:DELay?
    - SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:AMPLitude <NRf>
    - SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:AMPLitude?
    - SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:HIGH <NRf>
    - SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:HIGH?
    - SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:LOW <NRf>
    - SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:LOW?
    - SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:OFFSet <NR3>
    - SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:OFFSet?
    - SOURce[n]:POWer:LEVel:IMMediate:AMPLitude <NRf>
    - SOURce[n]:POWer:LEVel:IMMediate:AMPLitude?
    - SOURce[n]:RMODe {CONTinuous|TRIGgered|TCONtinuous}
    - SOURce[n]:RMODe?
    - SOURce[n]:SCSTep?
    - SOURce[n]:SKEW <skew>
    - SOURce[n]:SKEW?
    - SOURce[n]:TINPut {ITRigger|ATRigger|BTRigger}
    - SOURce[n]:TINPut?
    - SOURce[n]:VOLTage:LEVel:IMMediate:AMPLitude <NR3>
    - SOURce[n]:VOLTage:LEVel:IMMediate:AMPLitude?
    - SOURce[n]:VOLTage:LEVel:IMMediate:HIGH <NRf>
    - SOURce[n]:VOLTage:LEVel:IMMediate:HIGH?
    - SOURce[n]:VOLTage:LEVel:IMMediate:LOW <NRf>
    - SOURce[n]:VOLTage:LEVel:IMMediate:LOW?
    - SOURce[n]:VOLTage:LEVel:IMMediate:OFFSet <NRf>
    - SOURce[n]:VOLTage:LEVel:IMMediate:OFFSet?
    - SOURce[n]:WAVeform <wfm_name>
    - SOURce[n]:WAVeform?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    ValidatedChannel,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class SourceItemWaveform(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:WAVeform`` command.

    Description:
        - This command sets or returns the name of the waveform assigned to the specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:WAVeform?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:WAVeform?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce[n]:WAVeform value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:WAVeform <wfm_name>
        - SOURce[n]:WAVeform?
        ```
    """


class SourceItemVoltageLevelImmediateOffset(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:VOLTage:LEVel:IMMediate:OFFSet`` command.

    Description:
        - This command sets or returns the offset for the waveform associated with the specified
          channel. This command is only valid when the output path is set to DC Amplified.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:VOLTage:LEVel:IMMediate:OFFSet?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce[n]:VOLTage:LEVel:IMMediate:OFFSet?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce[n]:VOLTage:LEVel:IMMediate:OFFSet value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:VOLTage:LEVel:IMMediate:OFFSet <NRf>
        - SOURce[n]:VOLTage:LEVel:IMMediate:OFFSet?
        ```
    """


class SourceItemVoltageLevelImmediateLow(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:VOLTage:LEVel:IMMediate:LOW`` command.

    Description:
        - This command sets or returns the low voltage level for the waveform associated with a
          channel. This command is only valid when the output path is set to Direct.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:VOLTage:LEVel:IMMediate:LOW?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce[n]:VOLTage:LEVel:IMMediate:LOW?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce[n]:VOLTage:LEVel:IMMediate:LOW value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:VOLTage:LEVel:IMMediate:LOW <NRf>
        - SOURce[n]:VOLTage:LEVel:IMMediate:LOW?
        ```

    Info:
        - ``*RST`` sets this to -250 mV.
    """


class SourceItemVoltageLevelImmediateHigh(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:VOLTage:LEVel:IMMediate:HIGH`` command.

    Description:
        - This command sets or returns the high voltage level for the waveform associated with the
          specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:VOLTage:LEVel:IMMediate:HIGH?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce[n]:VOLTage:LEVel:IMMediate:HIGH?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce[n]:VOLTage:LEVel:IMMediate:HIGH value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:VOLTage:LEVel:IMMediate:HIGH <NRf>
        - SOURce[n]:VOLTage:LEVel:IMMediate:HIGH?
        ```

    Info:
        - ``*RST`` sets this to 250 mV.
    """


class SourceItemVoltageLevelImmediateAmplitude(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:VOLTage:LEVel:IMMediate:AMPLitude`` command.

    Description:
        - This command sets or returns the amplitude for the waveform associated with a channel.

    Usage:
        - Using the ``.query()`` method will send the
          ``SOURce[n]:VOLTage:LEVel:IMMediate:AMPLitude?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce[n]:VOLTage:LEVel:IMMediate:AMPLitude?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce[n]:VOLTage:LEVel:IMMediate:AMPLitude value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:VOLTage:LEVel:IMMediate:AMPLitude <NR3>
        - SOURce[n]:VOLTage:LEVel:IMMediate:AMPLitude?
        ```
    """


class SourceItemVoltageLevelImmediate(SCPICmdRead):
    """The ``SOURce[n]:VOLTage:LEVel:IMMediate`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:VOLTage:LEVel:IMMediate?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:VOLTage:LEVel:IMMediate?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.high``: The ``SOURce[n]:VOLTage:LEVel:IMMediate:HIGH`` command.
        - ``.low``: The ``SOURce[n]:VOLTage:LEVel:IMMediate:LOW`` command.
        - ``.offset``: The ``SOURce[n]:VOLTage:LEVel:IMMediate:OFFSet`` command.
        - ``.amplitude``: The ``SOURce[n]:VOLTage:LEVel:IMMediate:AMPLitude`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._high = SourceItemVoltageLevelImmediateHigh(device, f"{self._cmd_syntax}:HIGH")
        self._low = SourceItemVoltageLevelImmediateLow(device, f"{self._cmd_syntax}:LOW")
        self._offset = SourceItemVoltageLevelImmediateOffset(device, f"{self._cmd_syntax}:OFFSet")
        self._amplitude = SourceItemVoltageLevelImmediateAmplitude(
            device, f"{self._cmd_syntax}:AMPLitude"
        )

    @property
    def high(self) -> SourceItemVoltageLevelImmediateHigh:
        """Return the ``SOURce[n]:VOLTage:LEVel:IMMediate:HIGH`` command.

        Description:
            - This command sets or returns the high voltage level for the waveform associated with
              the specified channel.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce[n]:VOLTage:LEVel:IMMediate:HIGH?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:VOLTage:LEVel:IMMediate:HIGH?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce[n]:VOLTage:LEVel:IMMediate:HIGH value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:VOLTage:LEVel:IMMediate:HIGH <NRf>
            - SOURce[n]:VOLTage:LEVel:IMMediate:HIGH?
            ```

        Info:
            - ``*RST`` sets this to 250 mV.
        """
        return self._high

    @property
    def low(self) -> SourceItemVoltageLevelImmediateLow:
        """Return the ``SOURce[n]:VOLTage:LEVel:IMMediate:LOW`` command.

        Description:
            - This command sets or returns the low voltage level for the waveform associated with a
              channel. This command is only valid when the output path is set to Direct.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:VOLTage:LEVel:IMMediate:LOW?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:VOLTage:LEVel:IMMediate:LOW?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce[n]:VOLTage:LEVel:IMMediate:LOW value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:VOLTage:LEVel:IMMediate:LOW <NRf>
            - SOURce[n]:VOLTage:LEVel:IMMediate:LOW?
            ```

        Info:
            - ``*RST`` sets this to -250 mV.
        """
        return self._low

    @property
    def offset(self) -> SourceItemVoltageLevelImmediateOffset:
        """Return the ``SOURce[n]:VOLTage:LEVel:IMMediate:OFFSet`` command.

        Description:
            - This command sets or returns the offset for the waveform associated with the specified
              channel. This command is only valid when the output path is set to DC Amplified.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce[n]:VOLTage:LEVel:IMMediate:OFFSet?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:VOLTage:LEVel:IMMediate:OFFSet?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce[n]:VOLTage:LEVel:IMMediate:OFFSet value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:VOLTage:LEVel:IMMediate:OFFSet <NRf>
            - SOURce[n]:VOLTage:LEVel:IMMediate:OFFSet?
            ```
        """
        return self._offset

    @property
    def amplitude(self) -> SourceItemVoltageLevelImmediateAmplitude:
        """Return the ``SOURce[n]:VOLTage:LEVel:IMMediate:AMPLitude`` command.

        Description:
            - This command sets or returns the amplitude for the waveform associated with a channel.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce[n]:VOLTage:LEVel:IMMediate:AMPLitude?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:VOLTage:LEVel:IMMediate:AMPLitude?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce[n]:VOLTage:LEVel:IMMediate:AMPLitude value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:VOLTage:LEVel:IMMediate:AMPLitude <NR3>
            - SOURce[n]:VOLTage:LEVel:IMMediate:AMPLitude?
            ```
        """
        return self._amplitude


class SourceItemVoltageLevel(SCPICmdRead):
    """The ``SOURce[n]:VOLTage:LEVel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:VOLTage:LEVel?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:VOLTage:LEVel?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.immediate``: The ``SOURce[n]:VOLTage:LEVel:IMMediate`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._immediate = SourceItemVoltageLevelImmediate(device, f"{self._cmd_syntax}:IMMediate")

    @property
    def immediate(self) -> SourceItemVoltageLevelImmediate:
        """Return the ``SOURce[n]:VOLTage:LEVel:IMMediate`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:VOLTage:LEVel:IMMediate?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:VOLTage:LEVel:IMMediate?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.high``: The ``SOURce[n]:VOLTage:LEVel:IMMediate:HIGH`` command.
            - ``.low``: The ``SOURce[n]:VOLTage:LEVel:IMMediate:LOW`` command.
            - ``.offset``: The ``SOURce[n]:VOLTage:LEVel:IMMediate:OFFSet`` command.
            - ``.amplitude``: The ``SOURce[n]:VOLTage:LEVel:IMMediate:AMPLitude`` command.
        """
        return self._immediate


class SourceItemVoltage(SCPICmdRead):
    """The ``SOURce[n]:VOLTage`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:VOLTage?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:VOLTage?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.level``: The ``SOURce[n]:VOLTage:LEVel`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._level = SourceItemVoltageLevel(device, f"{self._cmd_syntax}:LEVel")

    @property
    def level(self) -> SourceItemVoltageLevel:
        """Return the ``SOURce[n]:VOLTage:LEVel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:VOLTage:LEVel?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:VOLTage:LEVel?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.immediate``: The ``SOURce[n]:VOLTage:LEVel:IMMediate`` command tree.
        """
        return self._level


class SourceItemTinput(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:TINPut`` command.

    Description:
        - This command sets or returns the trigger input source of the specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:TINPut?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:TINPut?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce[n]:TINPut value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:TINPut {ITRigger|ATRigger|BTRigger}
        - SOURce[n]:TINPut?
        ```

    Info:
        - ``ITRigger`` selects the internal trigger signal as the trigger source. (The A and B Force
          Trigger buttons are not active.) ATRigger selects trigger input A. BTRigger selects
          trigger input B. [n] determines the channel number. If omitted, interpreted as 1.
        - ``*RST`` sets this to ATR.
    """


class SourceItemSkew(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:SKEW`` command.

    Description:
        - This command sets or returns the skew (relative timing of the analog output) for the
          waveform associated with the specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:SKEW?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:SKEW?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce[n]:SKEW value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:SKEW <skew>
        - SOURce[n]:SKEW?
        ```

    Info:
        - ``*RST`` sets this to 0.
    """


class SourceItemScstep(SCPICmdRead):
    """The ``SOURce[n]:SCSTep`` command.

    Description:
        - This command allows you to read the current step of the sequence while the system is
          running.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:SCSTep?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:SCSTep?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SOURce[n]:SCSTep?
        ```
    """


class SourceItemRmode(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:RMODe`` command.

    Description:
        - This command sets or returns the run mode of the specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:RMODe?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:RMODe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce[n]:RMODe value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:RMODe {CONTinuous|TRIGgered|TCONtinuous}
        - SOURce[n]:RMODe?
        ```

    Info:
        - ``CONTinuous`` sets the Run Mode to Continuous (not waiting for trigger). TRIGgered sets
          the Run Mode to Triggered, waiting for a trigger event. One waveform play out cycle
          completes, then play out stops, waiting for the next trigger event.TCONtinuous sets the
          Run Mode to Triggered Continuous, waiting for a trigger. Once a trigger is received, the
          waveform plays out continuously.[n] determines the channel number. If omitted, interpreted
          as 1.
        - ``*RST`` sets this to CONT.
    """


class SourceItemPowerLevelImmediateAmplitude(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:POWer:LEVel:IMMediate:AMPLitude`` command.

    Description:
        - This command sets or returns the amplitude for the waveform associated with the specified
          channel in units of dBm for the filtered path. This command is only valid when the output
          path is set to AC. Option AC is required. If Option AC is not installed, sending the
          command causes an error message.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:POWer:LEVel:IMMediate:AMPLitude?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce[n]:POWer:LEVel:IMMediate:AMPLitude?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce[n]:POWer:LEVel:IMMediate:AMPLitude value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:POWer:LEVel:IMMediate:AMPLitude <NRf>
        - SOURce[n]:POWer:LEVel:IMMediate:AMPLitude?
        ```
    """


class SourceItemPowerLevelImmediate(SCPICmdRead):
    """The ``SOURce[n]:POWer:LEVel:IMMediate`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:POWer:LEVel:IMMediate?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:POWer:LEVel:IMMediate?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.amplitude``: The ``SOURce[n]:POWer:LEVel:IMMediate:AMPLitude`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._amplitude = SourceItemPowerLevelImmediateAmplitude(
            device, f"{self._cmd_syntax}:AMPLitude"
        )

    @property
    def amplitude(self) -> SourceItemPowerLevelImmediateAmplitude:
        """Return the ``SOURce[n]:POWer:LEVel:IMMediate:AMPLitude`` command.

        Description:
            - This command sets or returns the amplitude for the waveform associated with the
              specified channel in units of dBm for the filtered path. This command is only valid
              when the output path is set to AC. Option AC is required. If Option AC is not
              installed, sending the command causes an error message.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce[n]:POWer:LEVel:IMMediate:AMPLitude?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:POWer:LEVel:IMMediate:AMPLitude?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce[n]:POWer:LEVel:IMMediate:AMPLitude value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:POWer:LEVel:IMMediate:AMPLitude <NRf>
            - SOURce[n]:POWer:LEVel:IMMediate:AMPLitude?
            ```
        """
        return self._amplitude


class SourceItemPowerLevel(SCPICmdRead):
    """The ``SOURce[n]:POWer:LEVel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:POWer:LEVel?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:POWer:LEVel?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.immediate``: The ``SOURce[n]:POWer:LEVel:IMMediate`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._immediate = SourceItemPowerLevelImmediate(device, f"{self._cmd_syntax}:IMMediate")

    @property
    def immediate(self) -> SourceItemPowerLevelImmediate:
        """Return the ``SOURce[n]:POWer:LEVel:IMMediate`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:POWer:LEVel:IMMediate?``
              query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:POWer:LEVel:IMMediate?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.amplitude``: The ``SOURce[n]:POWer:LEVel:IMMediate:AMPLitude`` command.
        """
        return self._immediate


class SourceItemPower(SCPICmdRead):
    """The ``SOURce[n]:POWer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:POWer?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:POWer?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.level``: The ``SOURce[n]:POWer:LEVel`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._level = SourceItemPowerLevel(device, f"{self._cmd_syntax}:LEVel")

    @property
    def level(self) -> SourceItemPowerLevel:
        """Return the ``SOURce[n]:POWer:LEVel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:POWer:LEVel?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:POWer:LEVel?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.immediate``: The ``SOURce[n]:POWer:LEVel:IMMediate`` command tree.
        """
        return self._level


class SourceItemMarkerItemVoltageLevelImmediateOffset(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:OFFSet`` command.

    Description:
        - This command sets or returns the offset voltage of the selected marker of the selected
          channel.

    Usage:
        - Using the ``.query()`` method will send the
          ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:OFFSet?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:OFFSet?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:OFFSet value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:OFFSet <NR3>
        - SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:OFFSet?
        ```

    Info:
        - ``*RST`` sets this to 500 mV.
    """


class SourceItemMarkerItemVoltageLevelImmediateLow(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:LOW`` command.

    Description:
        - This command sets or returns the marker low voltage level of the specified marker of the
          specified channel.

    Usage:
        - Using the ``.query()`` method will send the
          ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:LOW?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:LOW?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:LOW value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:LOW <NRf>
        - SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:LOW?
        ```

    Info:
        - ``*RST`` sets this to 0 V.
    """


class SourceItemMarkerItemVoltageLevelImmediateHigh(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:HIGH`` command.

    Description:
        - This command sets or returns the marker high voltage level of the specified marker of the
          specified channel.

    Usage:
        - Using the ``.query()`` method will send the
          ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:HIGH?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:HIGH?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:HIGH value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:HIGH <NRf>
        - SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:HIGH?
        ```

    Info:
        - ``*RST`` sets all markers to 1 V.
    """


class SourceItemMarkerItemVoltageLevelImmediateAmplitude(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:AMPLitude`` command.

    Description:
        - This command sets or returns the marker voltage amplitude of the specified marker of the
          specified channel.

    Usage:
        - Using the ``.query()`` method will send the
          ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:AMPLitude?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:AMPLitude?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:AMPLitude value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:AMPLitude <NRf>
        - SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:AMPLitude?
        ```

    Info:
        - ``*RST`` sets this to 1 V for all markers.
    """


class SourceItemMarkerItemVoltageLevelImmediate(SCPICmdRead):
    """The ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.high``: The ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:HIGH`` command.
        - ``.low``: The ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:LOW`` command.
        - ``.offset``: The ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:OFFSet`` command.
        - ``.amplitude``: The ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:AMPLitude`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._high = SourceItemMarkerItemVoltageLevelImmediateHigh(
            device, f"{self._cmd_syntax}:HIGH"
        )
        self._low = SourceItemMarkerItemVoltageLevelImmediateLow(device, f"{self._cmd_syntax}:LOW")
        self._offset = SourceItemMarkerItemVoltageLevelImmediateOffset(
            device, f"{self._cmd_syntax}:OFFSet"
        )
        self._amplitude = SourceItemMarkerItemVoltageLevelImmediateAmplitude(
            device, f"{self._cmd_syntax}:AMPLitude"
        )

    @property
    def high(self) -> SourceItemMarkerItemVoltageLevelImmediateHigh:
        """Return the ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:HIGH`` command.

        Description:
            - This command sets or returns the marker high voltage level of the specified marker of
              the specified channel.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:HIGH?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:HIGH?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:HIGH value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:HIGH <NRf>
            - SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:HIGH?
            ```

        Info:
            - ``*RST`` sets all markers to 1 V.
        """
        return self._high

    @property
    def low(self) -> SourceItemMarkerItemVoltageLevelImmediateLow:
        """Return the ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:LOW`` command.

        Description:
            - This command sets or returns the marker low voltage level of the specified marker of
              the specified channel.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:LOW?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:LOW?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:LOW value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:LOW <NRf>
            - SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:LOW?
            ```

        Info:
            - ``*RST`` sets this to 0 V.
        """
        return self._low

    @property
    def offset(self) -> SourceItemMarkerItemVoltageLevelImmediateOffset:
        """Return the ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:OFFSet`` command.

        Description:
            - This command sets or returns the offset voltage of the selected marker of the selected
              channel.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:OFFSet?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:OFFSet?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:OFFSet value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:OFFSet <NR3>
            - SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:OFFSet?
            ```

        Info:
            - ``*RST`` sets this to 500 mV.
        """
        return self._offset

    @property
    def amplitude(self) -> SourceItemMarkerItemVoltageLevelImmediateAmplitude:
        """Return the ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:AMPLitude`` command.

        Description:
            - This command sets or returns the marker voltage amplitude of the specified marker of
              the specified channel.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:AMPLitude?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:AMPLitude?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:AMPLitude value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:AMPLitude <NRf>
            - SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:AMPLitude?
            ```

        Info:
            - ``*RST`` sets this to 1 V for all markers.
        """
        return self._amplitude


class SourceItemMarkerItemVoltageLevel(SCPICmdRead):
    """The ``SOURce[n]:MARKer[m]:VOLTage:LEVel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:MARKer[m]:VOLTage:LEVel?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:MARKer[m]:VOLTage:LEVel?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.immediate``: The ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._immediate = SourceItemMarkerItemVoltageLevelImmediate(
            device, f"{self._cmd_syntax}:IMMediate"
        )

    @property
    def immediate(self) -> SourceItemMarkerItemVoltageLevelImmediate:
        """Return the ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.high``: The ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:HIGH`` command.
            - ``.low``: The ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:LOW`` command.
            - ``.offset``: The ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:OFFSet`` command.
            - ``.amplitude``: The ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate:AMPLitude`` command.
        """
        return self._immediate


class SourceItemMarkerItemVoltage(SCPICmdRead):
    """The ``SOURce[n]:MARKer[m]:VOLTage`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:MARKer[m]:VOLTage?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:MARKer[m]:VOLTage?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.level``: The ``SOURce[n]:MARKer[m]:VOLTage:LEVel`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._level = SourceItemMarkerItemVoltageLevel(device, f"{self._cmd_syntax}:LEVel")

    @property
    def level(self) -> SourceItemMarkerItemVoltageLevel:
        """Return the ``SOURce[n]:MARKer[m]:VOLTage:LEVel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:MARKer[m]:VOLTage:LEVel?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:MARKer[m]:VOLTage:LEVel?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.immediate``: The ``SOURce[n]:MARKer[m]:VOLTage:LEVel:IMMediate`` command tree.
        """
        return self._level


class SourceItemMarkerItemDelay(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:MARKer[m]:DELay`` command.

    Description:
        - This command sets or returns the delay for the specified marker of the specified channel.
          Marker delay is independent for each channel.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:MARKer[m]:DELay?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:MARKer[m]:DELay?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce[n]:MARKer[m]:DELay value``
          command.

    SCPI Syntax:
        ```
        - SOURce[n]:MARKer[m]:DELay <NR3>
        - SOURce[n]:MARKer[m]:DELay?
        ```

    Info:
        - ``*RST`` sets all channel marker delays to 0.
    """


class SourceItemMarkerItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``SOURce[n]:MARKer[m]`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:MARKer[m]?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:MARKer[m]?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.delay``: The ``SOURce[n]:MARKer[m]:DELay`` command.
        - ``.voltage``: The ``SOURce[n]:MARKer[m]:VOLTage`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._delay = SourceItemMarkerItemDelay(device, f"{self._cmd_syntax}:DELay")
        self._voltage = SourceItemMarkerItemVoltage(device, f"{self._cmd_syntax}:VOLTage")

    @property
    def delay(self) -> SourceItemMarkerItemDelay:
        """Return the ``SOURce[n]:MARKer[m]:DELay`` command.

        Description:
            - This command sets or returns the delay for the specified marker of the specified
              channel. Marker delay is independent for each channel.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:MARKer[m]:DELay?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:MARKer[m]:DELay?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce[n]:MARKer[m]:DELay value``
              command.

        SCPI Syntax:
            ```
            - SOURce[n]:MARKer[m]:DELay <NR3>
            - SOURce[n]:MARKer[m]:DELay?
            ```

        Info:
            - ``*RST`` sets all channel marker delays to 0.
        """
        return self._delay

    @property
    def voltage(self) -> SourceItemMarkerItemVoltage:
        """Return the ``SOURce[n]:MARKer[m]:VOLTage`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:MARKer[m]:VOLTage?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:MARKer[m]:VOLTage?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.level``: The ``SOURce[n]:MARKer[m]:VOLTage:LEVel`` command tree.
        """
        return self._voltage


class SourceItemJumpPatternForce(SCPICmdWrite):
    """The ``SOURce[n]:JUMP:PATTern:FORCe`` command.

    Description:
        - This command generates an event, forcing the sequencer to the step specified by the
          pattern in the pattern jump table. If the sequence is playing on both channels, the force
          jump is applied to both channels simultaneously.

    Usage:
        - Using the ``.write(value)`` method will send the ``SOURce[n]:JUMP:PATTern:FORCe value``
          command.

    SCPI Syntax:
        ```
        - SOURce[n]:JUMP:PATTern:FORCe <pattern>
        ```
    """


class SourceItemJumpPattern(SCPICmdRead):
    """The ``SOURce[n]:JUMP:PATTern`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:JUMP:PATTern?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:JUMP:PATTern?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.force``: The ``SOURce[n]:JUMP:PATTern:FORCe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._force = SourceItemJumpPatternForce(device, f"{self._cmd_syntax}:FORCe")

    @property
    def force(self) -> SourceItemJumpPatternForce:
        """Return the ``SOURce[n]:JUMP:PATTern:FORCe`` command.

        Description:
            - This command generates an event, forcing the sequencer to the step specified by the
              pattern in the pattern jump table. If the sequence is playing on both channels, the
              force jump is applied to both channels simultaneously.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``SOURce[n]:JUMP:PATTern:FORCe value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:JUMP:PATTern:FORCe <pattern>
            ```
        """
        return self._force


class SourceItemJumpForce(SCPICmdWrite):
    """The ``SOURce[n]:JUMP:FORCe`` command.

    Description:
        - This command forces the sequencer to jump to a specific sequence step for the specified
          channel. A force jump does not require a trigger event to execute the jump.

    Usage:
        - Using the ``.write(value)`` method will send the ``SOURce[n]:JUMP:FORCe value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:JUMP:FORCe {FIRSt|CURRent|LAST|END|<NR1>}
        ```
    """


class SourceItemJump(SCPICmdRead):
    """The ``SOURce[n]:JUMP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:JUMP?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:JUMP?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.force``: The ``SOURce[n]:JUMP:FORCe`` command.
        - ``.pattern``: The ``SOURce[n]:JUMP:PATTern`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._force = SourceItemJumpForce(device, f"{self._cmd_syntax}:FORCe")
        self._pattern = SourceItemJumpPattern(device, f"{self._cmd_syntax}:PATTern")

    @property
    def force(self) -> SourceItemJumpForce:
        """Return the ``SOURce[n]:JUMP:FORCe`` command.

        Description:
            - This command forces the sequencer to jump to a specific sequence step for the
              specified channel. A force jump does not require a trigger event to execute the jump.

        Usage:
            - Using the ``.write(value)`` method will send the ``SOURce[n]:JUMP:FORCe value``
              command.

        SCPI Syntax:
            ```
            - SOURce[n]:JUMP:FORCe {FIRSt|CURRent|LAST|END|<NR1>}
            ```
        """
        return self._force

    @property
    def pattern(self) -> SourceItemJumpPattern:
        """Return the ``SOURce[n]:JUMP:PATTern`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:JUMP:PATTern?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:JUMP:PATTern?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.force``: The ``SOURce[n]:JUMP:PATTern:FORCe`` command.
        """
        return self._pattern


class SourceItemDacResolution(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:DAC:RESolution`` command.

    Description:
        - This command sets or returns the DAC resolution.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:DAC:RESolution?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:DAC:RESolution?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce[n]:DAC:RESolution value``
          command.

    SCPI Syntax:
        ```
        - SOURce[n]:DAC:RESolution {8|9|10}
        - SOURce[n]:DAC:RESolution?
        ```

    Info:
        - ``*RST`` sets this to 10.
    """


class SourceItemDac(SCPICmdRead):
    """The ``SOURce[n]:DAC`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:DAC?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:DAC?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.resolution``: The ``SOURce[n]:DAC:RESolution`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._resolution = SourceItemDacResolution(device, f"{self._cmd_syntax}:RESolution")

    @property
    def resolution(self) -> SourceItemDacResolution:
        """Return the ``SOURce[n]:DAC:RESolution`` command.

        Description:
            - This command sets or returns the DAC resolution.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:DAC:RESolution?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:DAC:RESolution?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce[n]:DAC:RESolution value``
              command.

        SCPI Syntax:
            ```
            - SOURce[n]:DAC:RESolution {8|9|10}
            - SOURce[n]:DAC:RESolution?
            ```

        Info:
            - ``*RST`` sets this to 10.
        """
        return self._resolution


class SourceItemCassetWaveform(SCPICmdWrite):
    """The ``SOURce[n]:CASSet:WAVeform`` command.

    Description:
        - This command assigns a waveform (from the waveform list) to the specified channel.

    Usage:
        - Using the ``.write(value)`` method will send the ``SOURce[n]:CASSet:WAVeform value``
          command.

    SCPI Syntax:
        ```
        - SOURce[n]:CASSet:WAVeform <wfm_name>[, <component_type>]
        ```
    """


class SourceItemCassetType(SCPICmdRead):
    """The ``SOURce[n]:CASSet:TYPE`` command.

    Description:
        - This command returns the type of the asset (waveform or sequence) assigned to a channel.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:CASSet:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:CASSet:TYPE?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SOURce[n]:CASSet:TYPE?
        ```
    """


class SourceItemCassetSequence(SCPICmdWrite):
    """The ``SOURce[n]:CASSet:SEQuence`` command.

    Description:
        - This command assigns a track of a sequence (from the sequence list) to the specified
          channel.

    Usage:
        - Using the ``.write(value)`` method will send the ``SOURce[n]:CASSet:SEQuence value``
          command.

    SCPI Syntax:
        ```
        - SOURce[n]:CASSet:SEQuence <sequence_name>, <track_number>[,<component_type>]
        ```
    """


class SourceItemCasset(SCPICmdRead):
    """The ``SOURce[n]:CASSet`` command.

    Description:
        - This command returns the asset (waveform or sequence) assigned to the specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:CASSet?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:CASSet?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SOURce[n]:CASSet?
        ```

    Properties:
        - ``.sequence``: The ``SOURce[n]:CASSet:SEQuence`` command.
        - ``.type``: The ``SOURce[n]:CASSet:TYPE`` command.
        - ``.waveform``: The ``SOURce[n]:CASSet:WAVeform`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._sequence = SourceItemCassetSequence(device, f"{self._cmd_syntax}:SEQuence")
        self._type = SourceItemCassetType(device, f"{self._cmd_syntax}:TYPE")
        self._waveform = SourceItemCassetWaveform(device, f"{self._cmd_syntax}:WAVeform")

    @property
    def sequence(self) -> SourceItemCassetSequence:
        """Return the ``SOURce[n]:CASSet:SEQuence`` command.

        Description:
            - This command assigns a track of a sequence (from the sequence list) to the specified
              channel.

        Usage:
            - Using the ``.write(value)`` method will send the ``SOURce[n]:CASSet:SEQuence value``
              command.

        SCPI Syntax:
            ```
            - SOURce[n]:CASSet:SEQuence <sequence_name>, <track_number>[,<component_type>]
            ```
        """
        return self._sequence

    @property
    def type(self) -> SourceItemCassetType:
        """Return the ``SOURce[n]:CASSet:TYPE`` command.

        Description:
            - This command returns the type of the asset (waveform or sequence) assigned to a
              channel.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:CASSet:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:CASSet:TYPE?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SOURce[n]:CASSet:TYPE?
            ```
        """
        return self._type

    @property
    def waveform(self) -> SourceItemCassetWaveform:
        """Return the ``SOURce[n]:CASSet:WAVeform`` command.

        Description:
            - This command assigns a waveform (from the waveform list) to the specified channel.

        Usage:
            - Using the ``.write(value)`` method will send the ``SOURce[n]:CASSet:WAVeform value``
              command.

        SCPI Syntax:
            ```
            - SOURce[n]:CASSet:WAVeform <wfm_name>[, <component_type>]
            ```
        """
        return self._waveform


#  pylint: disable=too-many-instance-attributes
class SourceItem(ValidatedChannel, SCPICmdRead):
    """The ``SOURce[n]`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.casset``: The ``SOURce[n]:CASSet`` command.
        - ``.dac``: The ``SOURce[n]:DAC`` command tree.
        - ``.marker``: The ``SOURce[n]:MARKer[m]`` command tree.
        - ``.power``: The ``SOURce[n]:POWer`` command tree.
        - ``.rmode``: The ``SOURce[n]:RMODe`` command.
        - ``.scstep``: The ``SOURce[n]:SCSTep`` command.
        - ``.skew``: The ``SOURce[n]:SKEW`` command.
        - ``.tinput``: The ``SOURce[n]:TINPut`` command.
        - ``.voltage``: The ``SOURce[n]:VOLTage`` command tree.
        - ``.waveform``: The ``SOURce[n]:WAVeform`` command.
        - ``.jump``: The ``SOURce[n]:JUMP`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SOURce[n]") -> None:
        super().__init__(device, cmd_syntax)
        self._casset = SourceItemCasset(device, f"{self._cmd_syntax}:CASSet")
        self._dac = SourceItemDac(device, f"{self._cmd_syntax}:DAC")
        self._marker: Dict[int, SourceItemMarkerItem] = DefaultDictPassKeyToFactory(
            lambda x: SourceItemMarkerItem(device, f"{self._cmd_syntax}:MARKer{x}")
        )
        self._power = SourceItemPower(device, f"{self._cmd_syntax}:POWer")
        self._rmode = SourceItemRmode(device, f"{self._cmd_syntax}:RMODe")
        self._scstep = SourceItemScstep(device, f"{self._cmd_syntax}:SCSTep")
        self._skew = SourceItemSkew(device, f"{self._cmd_syntax}:SKEW")
        self._tinput = SourceItemTinput(device, f"{self._cmd_syntax}:TINPut")
        self._voltage = SourceItemVoltage(device, f"{self._cmd_syntax}:VOLTage")
        self._waveform = SourceItemWaveform(device, f"{self._cmd_syntax}:WAVeform")
        self._jump = SourceItemJump(device, f"{self._cmd_syntax}:JUMP")

    @property
    def casset(self) -> SourceItemCasset:
        """Return the ``SOURce[n]:CASSet`` command.

        Description:
            - This command returns the asset (waveform or sequence) assigned to the specified
              channel.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:CASSet?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:CASSet?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SOURce[n]:CASSet?
            ```

        Sub-properties:
            - ``.sequence``: The ``SOURce[n]:CASSet:SEQuence`` command.
            - ``.type``: The ``SOURce[n]:CASSet:TYPE`` command.
            - ``.waveform``: The ``SOURce[n]:CASSet:WAVeform`` command.
        """
        return self._casset

    @property
    def dac(self) -> SourceItemDac:
        """Return the ``SOURce[n]:DAC`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:DAC?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:DAC?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.resolution``: The ``SOURce[n]:DAC:RESolution`` command.
        """
        return self._dac

    @property
    def marker(self) -> Dict[int, SourceItemMarkerItem]:
        """Return the ``SOURce[n]:MARKer[m]`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:MARKer[m]?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:MARKer[m]?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.delay``: The ``SOURce[n]:MARKer[m]:DELay`` command.
            - ``.voltage``: The ``SOURce[n]:MARKer[m]:VOLTage`` command tree.
        """
        return self._marker

    @property
    def power(self) -> SourceItemPower:
        """Return the ``SOURce[n]:POWer`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:POWer?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:POWer?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.level``: The ``SOURce[n]:POWer:LEVel`` command tree.
        """
        return self._power

    @property
    def rmode(self) -> SourceItemRmode:
        """Return the ``SOURce[n]:RMODe`` command.

        Description:
            - This command sets or returns the run mode of the specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:RMODe?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:RMODe?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce[n]:RMODe value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:RMODe {CONTinuous|TRIGgered|TCONtinuous}
            - SOURce[n]:RMODe?
            ```

        Info:
            - ``CONTinuous`` sets the Run Mode to Continuous (not waiting for trigger). TRIGgered
              sets the Run Mode to Triggered, waiting for a trigger event. One waveform play out
              cycle completes, then play out stops, waiting for the next trigger event.TCONtinuous
              sets the Run Mode to Triggered Continuous, waiting for a trigger. Once a trigger is
              received, the waveform plays out continuously.[n] determines the channel number. If
              omitted, interpreted as 1.
            - ``*RST`` sets this to CONT.
        """
        return self._rmode

    @property
    def scstep(self) -> SourceItemScstep:
        """Return the ``SOURce[n]:SCSTep`` command.

        Description:
            - This command allows you to read the current step of the sequence while the system is
              running.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:SCSTep?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:SCSTep?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SOURce[n]:SCSTep?
            ```
        """
        return self._scstep

    @property
    def skew(self) -> SourceItemSkew:
        """Return the ``SOURce[n]:SKEW`` command.

        Description:
            - This command sets or returns the skew (relative timing of the analog output) for the
              waveform associated with the specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:SKEW?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:SKEW?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce[n]:SKEW value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:SKEW <skew>
            - SOURce[n]:SKEW?
            ```

        Info:
            - ``*RST`` sets this to 0.
        """
        return self._skew

    @property
    def tinput(self) -> SourceItemTinput:
        """Return the ``SOURce[n]:TINPut`` command.

        Description:
            - This command sets or returns the trigger input source of the specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:TINPut?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:TINPut?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce[n]:TINPut value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:TINPut {ITRigger|ATRigger|BTRigger}
            - SOURce[n]:TINPut?
            ```

        Info:
            - ``ITRigger`` selects the internal trigger signal as the trigger source. (The A and B
              Force Trigger buttons are not active.) ATRigger selects trigger input A. BTRigger
              selects trigger input B. [n] determines the channel number. If omitted, interpreted as
              1.
            - ``*RST`` sets this to ATR.
        """
        return self._tinput

    @property
    def voltage(self) -> SourceItemVoltage:
        """Return the ``SOURce[n]:VOLTage`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:VOLTage?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:VOLTage?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.level``: The ``SOURce[n]:VOLTage:LEVel`` command tree.
        """
        return self._voltage

    @property
    def waveform(self) -> SourceItemWaveform:
        """Return the ``SOURce[n]:WAVeform`` command.

        Description:
            - This command sets or returns the name of the waveform assigned to the specified
              channel.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:WAVeform?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:WAVeform?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce[n]:WAVeform value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:WAVeform <wfm_name>
            - SOURce[n]:WAVeform?
            ```
        """
        return self._waveform

    @property
    def jump(self) -> SourceItemJump:
        """Return the ``SOURce[n]:JUMP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:JUMP?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:JUMP?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.force``: The ``SOURce[n]:JUMP:FORCe`` command.
            - ``.pattern``: The ``SOURce[n]:JUMP:PATTern`` command tree.
        """
        return self._jump


class SourceRoscillatorMultiplier(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce:ROSCillator:MULTiplier`` command.

    Description:
        - This command sets or returns the multiplier of the external reference signal when the
          external reference is variable.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce:ROSCillator:MULTiplier?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce:ROSCillator:MULTiplier?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce:ROSCillator:MULTiplier value``
          command.

    SCPI Syntax:
        ```
        - SOURce:ROSCillator:MULTiplier <NR1>
        - SOURce:ROSCillator:MULTiplier?
        ```
    """


class SourceRoscillator(SCPICmdRead):
    """The ``SOURce:ROSCillator`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce:ROSCillator?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce:ROSCillator?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.multiplier``: The ``SOURce:ROSCillator:MULTiplier`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._multiplier = SourceRoscillatorMultiplier(device, f"{self._cmd_syntax}:MULTiplier")

    @property
    def multiplier(self) -> SourceRoscillatorMultiplier:
        """Return the ``SOURce:ROSCillator:MULTiplier`` command.

        Description:
            - This command sets or returns the multiplier of the external reference signal when the
              external reference is variable.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce:ROSCillator:MULTiplier?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce:ROSCillator:MULTiplier?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce:ROSCillator:MULTiplier value`` command.

        SCPI Syntax:
            ```
            - SOURce:ROSCillator:MULTiplier <NR1>
            - SOURce:ROSCillator:MULTiplier?
            ```
        """
        return self._multiplier


class SourceRccouple(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce:RCCouple`` command.

    Description:
        - This command sets or returns the Coupled state (enabled or disabled) of the Run Mode
          control of a multi-channel instrument. The Run controls consist of the Run Mode and
          Trigger Input. The set form of the command forces all channels to match channel 1. After
          the initial coupling of the settings, changes made to the Run Mode of any channel affects
          all channels.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce:RCCouple?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce:RCCouple?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce:RCCouple value`` command.

    SCPI Syntax:
        ```
        - SOURce:RCCouple {0|1|ON|OFF}
        - SOURce:RCCouple?
        ```

    Info:
        - ``*RST`` sets this to 0.
    """


class SourceFrequency(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce:FREQuency`` command.

    Description:
        - This command sets or returns the clock sample rate of the AWG. [``:CW``] and [``:FIXed``]
          are optional to provide legacy support but provide no added functionality.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce:FREQuency?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce:FREQuency value`` command.

    SCPI Syntax:
        ```
        - SOURce:FREQuency <frequency>
        - SOURce:FREQuency?
        ```

    Info:
        - ``*RST`` sets the frequency to 25 GHz.
    """


class Source(SCPICmdRead):
    """The ``SOURce`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.frequency``: The ``SOURce:FREQuency`` command.
        - ``.rccouple``: The ``SOURce:RCCouple`` command.
        - ``.roscillator``: The ``SOURce:ROSCillator`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SOURce") -> None:
        super().__init__(device, cmd_syntax)
        self._frequency = SourceFrequency(device, f"{self._cmd_syntax}:FREQuency")
        self._rccouple = SourceRccouple(device, f"{self._cmd_syntax}:RCCouple")
        self._roscillator = SourceRoscillator(device, f"{self._cmd_syntax}:ROSCillator")

    @property
    def frequency(self) -> SourceFrequency:
        """Return the ``SOURce:FREQuency`` command.

        Description:
            - This command sets or returns the clock sample rate of the AWG. [``:CW``] and
              [``:FIXed``] are optional to provide legacy support but provide no added
              functionality.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce:FREQuency?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce:FREQuency value`` command.

        SCPI Syntax:
            ```
            - SOURce:FREQuency <frequency>
            - SOURce:FREQuency?
            ```

        Info:
            - ``*RST`` sets the frequency to 25 GHz.
        """
        return self._frequency

    @property
    def rccouple(self) -> SourceRccouple:
        """Return the ``SOURce:RCCouple`` command.

        Description:
            - This command sets or returns the Coupled state (enabled or disabled) of the Run Mode
              control of a multi-channel instrument. The Run controls consist of the Run Mode and
              Trigger Input. The set form of the command forces all channels to match channel 1.
              After the initial coupling of the settings, changes made to the Run Mode of any
              channel affects all channels.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce:RCCouple?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce:RCCouple?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce:RCCouple value`` command.

        SCPI Syntax:
            ```
            - SOURce:RCCouple {0|1|ON|OFF}
            - SOURce:RCCouple?
            ```

        Info:
            - ``*RST`` sets this to 0.
        """
        return self._rccouple

    @property
    def roscillator(self) -> SourceRoscillator:
        """Return the ``SOURce:ROSCillator`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce:ROSCillator?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce:ROSCillator?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.multiplier``: The ``SOURce:ROSCillator:MULTiplier`` command.
        """
        return self._roscillator
