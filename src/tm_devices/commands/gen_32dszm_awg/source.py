"""The source commands module.

These commands are used in the following models:
AWG5K, AWG5KC, AWG7K, AWG7KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SOURce[n]:COMBine:FEED {'ESIGnal'|''}
    - SOURce[n]:COMBine:FEED?
    - SOURce[n]:DAC:RESolution <NR1>
    - SOURce[n]:DAC:RESolution?
    - SOURce[n]:DELay:ADJust <NR3>
    - SOURce[n]:DELay:ADJust?
    - SOURce[n]:DELay:POINts <NR3>
    - SOURce[n]:DELay:POINts?
    - SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:AMPLitude <NR3>
    - SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:AMPLitude?
    - SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:HIGH <NR3>
    - SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:HIGH?
    - SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:LOW <NR3>
    - SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:LOW?
    - SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:OFFSet <NR3>
    - SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:OFFSet?
    - SOURce[n]:FREQuency:CW <NR3>
    - SOURce[n]:FREQuency:CW?
    - SOURce[n]:FREQuency:FIXed <NR3>
    - SOURce[n]:FREQuency:FIXed?
    - SOURce[n]:FUNCtion:USER <Waveform file_name>[,<msus>]
    - SOURce[n]:FUNCtion:USER?
    - SOURce[n]:MARKer1:DELay <NR3>
    - SOURce[n]:MARKer1:DELay?
    - SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:AMPLitude <NR3>
    - SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:AMPLitude?
    - SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:HIGH <NR3>
    - SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:HIGH?
    - SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:LOW <NR3>
    - SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:LOW?
    - SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:OFFSet <NR3>
    - SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:OFFSet?
    - SOURce[n]:MARKer2:DELay <NR3>
    - SOURce[n]:MARKer2:DELay?
    - SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:AMPLitude <NR3>
    - SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:AMPLitude?
    - SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:HIGH <NR3>
    - SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:HIGH?
    - SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:LOW <NR3>
    - SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:LOW?
    - SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:OFFSet <NR3>
    - SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:OFFSet?
    - SOURce[n]:PDELay:HOLD {PHASe|DELay|POINt}
    - SOURce[n]:PDELay:HOLD?
    - SOURce[n]:PHASe:ADJust <NR3>
    - SOURce[n]:PHASe:ADJust?
    - SOURce[n]:ROSCillator:FREQuency <NR3>
    - SOURce[n]:ROSCillator:FREQuency?
    - SOURce[n]:ROSCillator:MULTiplier <NR1>
    - SOURce[n]:ROSCillator:MULTiplier?
    - SOURce[n]:ROSCillator:SOURce {INTernal|EXTernal}
    - SOURce[n]:ROSCillator:SOURce?
    - SOURce[n]:ROSCillator:TYPE {FIXed|VARiable}
    - SOURce[n]:ROSCillator:TYPE?
    - SOURce[n]:SKEW <NR3>
    - SOURce[n]:SKEW?
    - SOURce[n]:VOLTage:LEVel:IMMediate:AMPLitude <NR3>
    - SOURce[n]:VOLTage:LEVel:IMMediate:AMPLitude?
    - SOURce[n]:VOLTage:LEVel:IMMediate:HIGH <NR3>
    - SOURce[n]:VOLTage:LEVel:IMMediate:HIGH?
    - SOURce[n]:VOLTage:LEVel:IMMediate:LOW <NR3>
    - SOURce[n]:VOLTage:LEVel:IMMediate:LOW?
    - SOURce[n]:VOLTage:LEVel:IMMediate:OFFSet <NR3>
    - SOURce[n]:VOLTage:LEVel:IMMediate:OFFSet?
    - SOURce[n]:WAVeform <wfm_name>
    - SOURce[n]:WAVeform?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, ValidatedChannel

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class SourceItemWaveform(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:WAVeform`` command.

    Description:
        - This command and query sets or returns the output waveform from the current waveform list
          for each channel when Run Mode is not Sequence. However, this command cannot be used to
          load a waveform stored in an AWG400/500/600/700 waveform or pattern file. To load a
          waveform stored in an AWG400/500/600/700 waveform or pattern file, use the
          ``SOURCEN:FUNCTION:USER`` command.

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

    Info:
        - ``<wfm_name>`` ::=<string>.
    """


class SourceItemVoltageLevelImmediateOffset(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:VOLTage:LEVel:IMMediate:OFFSet`` command.

    Description:
        - This command and query sets or returns the offset for the waveform associated with a
          channel. The command is not available on instruments with Option 02 or Option 06
          installed.

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
        - SOURce[n]:VOLTage:LEVel:IMMediate:OFFSet <NR3>
        - SOURce[n]:VOLTage:LEVel:IMMediate:OFFSet?
        ```

    Info:
        - ``<NR3>``
    """


class SourceItemVoltageLevelImmediateLow(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:VOLTage:LEVel:IMMediate:LOW`` command.

    Description:
        - This command and query sets or returns the low voltage level for the waveform associated
          with a channel. The command is not available on instruments with Option 02 or Option 06
          installed.

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
        - SOURce[n]:VOLTage:LEVel:IMMediate:LOW <NR3>
        - SOURce[n]:VOLTage:LEVel:IMMediate:LOW?
        ```

    Info:
        - ``<NR3>``
    """


class SourceItemVoltageLevelImmediateHigh(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:VOLTage:LEVel:IMMediate:HIGH`` command.

    Description:
        - This command and query sets or returns the high voltage level for the waveform associated
          with a channel. The command is not available on instruments with the Option 02 or Option
          06 installed.

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
        - SOURce[n]:VOLTage:LEVel:IMMediate:HIGH <NR3>
        - SOURce[n]:VOLTage:LEVel:IMMediate:HIGH?
        ```

    Info:
        - ``<NR3>``
    """


class SourceItemVoltageLevelImmediateAmplitude(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:VOLTage:LEVel:IMMediate:AMPLitude`` command.

    Description:
        - This command and query sets or returns the amplitude for the waveform associated with a
          channel.

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

    Info:
        - ``<NR3>`` in the range 50 mV to 2V pk-pk.
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
            - This command and query sets or returns the high voltage level for the waveform
              associated with a channel. The command is not available on instruments with the Option
              02 or Option 06 installed.

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
            - SOURce[n]:VOLTage:LEVel:IMMediate:HIGH <NR3>
            - SOURce[n]:VOLTage:LEVel:IMMediate:HIGH?
            ```

        Info:
            - ``<NR3>``
        """
        return self._high

    @property
    def low(self) -> SourceItemVoltageLevelImmediateLow:
        """Return the ``SOURce[n]:VOLTage:LEVel:IMMediate:LOW`` command.

        Description:
            - This command and query sets or returns the low voltage level for the waveform
              associated with a channel. The command is not available on instruments with Option 02
              or Option 06 installed.

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
            - SOURce[n]:VOLTage:LEVel:IMMediate:LOW <NR3>
            - SOURce[n]:VOLTage:LEVel:IMMediate:LOW?
            ```

        Info:
            - ``<NR3>``
        """
        return self._low

    @property
    def offset(self) -> SourceItemVoltageLevelImmediateOffset:
        """Return the ``SOURce[n]:VOLTage:LEVel:IMMediate:OFFSet`` command.

        Description:
            - This command and query sets or returns the offset for the waveform associated with a
              channel. The command is not available on instruments with Option 02 or Option 06
              installed.

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
            - SOURce[n]:VOLTage:LEVel:IMMediate:OFFSet <NR3>
            - SOURce[n]:VOLTage:LEVel:IMMediate:OFFSet?
            ```

        Info:
            - ``<NR3>``
        """
        return self._offset

    @property
    def amplitude(self) -> SourceItemVoltageLevelImmediateAmplitude:
        """Return the ``SOURce[n]:VOLTage:LEVel:IMMediate:AMPLitude`` command.

        Description:
            - This command and query sets or returns the amplitude for the waveform associated with
              a channel.

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

        Info:
            - ``<NR3>`` in the range 50 mV to 2V pk-pk.
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


class SourceItemSkew(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:SKEW`` command.

    Description:
        - This command and query sets or returns the skew for the waveform associated with a
          channel.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:SKEW?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:SKEW?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce[n]:SKEW value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:SKEW <NR3>
        - SOURce[n]:SKEW?
        ```

    Info:
        - ``<NR3>``
    """


class SourceItemRoscillatorType(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:ROSCillator:TYPE`` command.

    Description:
        - This command selects the type of the reference oscillator. This parameter is valid only
          when Clock Source is Internal and Reference Source is External.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:ROSCillator:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:ROSCillator:TYPE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce[n]:ROSCillator:TYPE value``
          command.

    SCPI Syntax:
        ```
        - SOURce[n]:ROSCillator:TYPE {FIXed|VARiable}
        - SOURce[n]:ROSCillator:TYPE?
        ```

    Info:
        - ``FIXed``
        - ``VARiable``
        - ``FIXed`` : Selects a reference source whose frequency is fixed to 10MHz, 20MHz, or
          100MHz. Select one of these frequencies using the [SOURce[1]]``:ROSCillator:FREQuency``
          command.
        - ``VARiable`` : Selects a reference source whose frequency is not fixed.
    """


class SourceItemRoscillatorSource(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:ROSCillator:SOURce`` command.

    Description:
        - This command selects the reference oscillator source. INTernal means that the reference
          frequency is derived from the internal precision oscillator. EXTernal means the reference
          frequency is derived from an external signal supplied through the Reference Clock Input
          connector.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:ROSCillator:SOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:ROSCillator:SOURce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce[n]:ROSCillator:SOURce value``
          command.

    SCPI Syntax:
        ```
        - SOURce[n]:ROSCillator:SOURce {INTernal|EXTernal}
        - SOURce[n]:ROSCillator:SOURce?
        ```

    Info:
        - ``<INTernal``
        - ``EXTernal>``
        - ``INTernal`` - The reference frequency is derived from the internal precision oscillator.
        - ``EXTernal`` - The reference frequency is derived from an external signal supplied through
          the reference clock input.
    """


class SourceItemRoscillatorMultiplier(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:ROSCillator:MULTiplier`` command.

    Description:
        - This command and query sets or returns the ROSCillator multiplier rate. This parameter is
          valid only when Clock Source is Internal and Reference Source is External and External
          Reference Type is Variable.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:ROSCillator:MULTiplier?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:ROSCillator:MULTiplier?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce[n]:ROSCillator:MULTiplier value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:ROSCillator:MULTiplier <NR1>
        - SOURce[n]:ROSCillator:MULTiplier?
        ```

    Info:
        - ``<NR1>``
    """


class SourceItemRoscillatorFrequency(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:ROSCillator:FREQuency`` command.

    Description:
        - This command selects the reference oscillator frequency. Valid values are 10 MHz, 20 MHz
          and 100 MHz. This command is used when the Clock Source is Internal and Reference Input is
          External and External Reference Type is Fixed.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:ROSCillator:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:ROSCillator:FREQuency?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce[n]:ROSCillator:FREQuency value``
          command.

    SCPI Syntax:
        ```
        - SOURce[n]:ROSCillator:FREQuency <NR3>
        - SOURce[n]:ROSCillator:FREQuency?
        ```

    Info:
        - ``<NR3>``
    """


class SourceItemRoscillator(SCPICmdRead):
    """The ``SOURce[n]:ROSCillator`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:ROSCillator?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:ROSCillator?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.frequency``: The ``SOURce[n]:ROSCillator:FREQuency`` command.
        - ``.multiplier``: The ``SOURce[n]:ROSCillator:MULTiplier`` command.
        - ``.source``: The ``SOURce[n]:ROSCillator:SOURce`` command.
        - ``.type``: The ``SOURce[n]:ROSCillator:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._frequency = SourceItemRoscillatorFrequency(device, f"{self._cmd_syntax}:FREQuency")
        self._multiplier = SourceItemRoscillatorMultiplier(device, f"{self._cmd_syntax}:MULTiplier")
        self._source = SourceItemRoscillatorSource(device, f"{self._cmd_syntax}:SOURce")
        self._type = SourceItemRoscillatorType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def frequency(self) -> SourceItemRoscillatorFrequency:
        """Return the ``SOURce[n]:ROSCillator:FREQuency`` command.

        Description:
            - This command selects the reference oscillator frequency. Valid values are 10 MHz, 20
              MHz and 100 MHz. This command is used when the Clock Source is Internal and Reference
              Input is External and External Reference Type is Fixed.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:ROSCillator:FREQuency?``
              query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:ROSCillator:FREQuency?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce[n]:ROSCillator:FREQuency value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:ROSCillator:FREQuency <NR3>
            - SOURce[n]:ROSCillator:FREQuency?
            ```

        Info:
            - ``<NR3>``
        """
        return self._frequency

    @property
    def multiplier(self) -> SourceItemRoscillatorMultiplier:
        """Return the ``SOURce[n]:ROSCillator:MULTiplier`` command.

        Description:
            - This command and query sets or returns the ROSCillator multiplier rate. This parameter
              is valid only when Clock Source is Internal and Reference Source is External and
              External Reference Type is Variable.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:ROSCillator:MULTiplier?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:ROSCillator:MULTiplier?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce[n]:ROSCillator:MULTiplier value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:ROSCillator:MULTiplier <NR1>
            - SOURce[n]:ROSCillator:MULTiplier?
            ```

        Info:
            - ``<NR1>``
        """
        return self._multiplier

    @property
    def source(self) -> SourceItemRoscillatorSource:
        """Return the ``SOURce[n]:ROSCillator:SOURce`` command.

        Description:
            - This command selects the reference oscillator source. INTernal means that the
              reference frequency is derived from the internal precision oscillator. EXTernal means
              the reference frequency is derived from an external signal supplied through the
              Reference Clock Input connector.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:ROSCillator:SOURce?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:ROSCillator:SOURce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce[n]:ROSCillator:SOURce value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:ROSCillator:SOURce {INTernal|EXTernal}
            - SOURce[n]:ROSCillator:SOURce?
            ```

        Info:
            - ``<INTernal``
            - ``EXTernal>``
            - ``INTernal`` - The reference frequency is derived from the internal precision
              oscillator.
            - ``EXTernal`` - The reference frequency is derived from an external signal supplied
              through the reference clock input.
        """
        return self._source

    @property
    def type(self) -> SourceItemRoscillatorType:
        """Return the ``SOURce[n]:ROSCillator:TYPE`` command.

        Description:
            - This command selects the type of the reference oscillator. This parameter is valid
              only when Clock Source is Internal and Reference Source is External.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:ROSCillator:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:ROSCillator:TYPE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce[n]:ROSCillator:TYPE value``
              command.

        SCPI Syntax:
            ```
            - SOURce[n]:ROSCillator:TYPE {FIXed|VARiable}
            - SOURce[n]:ROSCillator:TYPE?
            ```

        Info:
            - ``FIXed``
            - ``VARiable``
            - ``FIXed`` : Selects a reference source whose frequency is fixed to 10MHz, 20MHz, or
              100MHz. Select one of these frequencies using the
              [SOURce[1]]``:ROSCillator:FREQuency`` command.
            - ``VARiable`` : Selects a reference source whose frequency is not fixed.
        """
        return self._type


class SourceItemPhaseAdjust(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:PHASe:ADJust`` command.

    Description:
        - (AWG5000 Series only) This command and query sets or returns the phase of the analog
          output.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:PHASe:ADJust?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:PHASe:ADJust?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce[n]:PHASe:ADJust value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:PHASe:ADJust <NR3>
        - SOURce[n]:PHASe:ADJust?
        ```

    Info:
        - ``<NR3>``
    """


class SourceItemPhase(SCPICmdRead):
    """The ``SOURce[n]:PHASe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:PHASe?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:PHASe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.adjust``: The ``SOURce[n]:PHASe:ADJust`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._adjust = SourceItemPhaseAdjust(device, f"{self._cmd_syntax}:ADJust")

    @property
    def adjust(self) -> SourceItemPhaseAdjust:
        """Return the ``SOURce[n]:PHASe:ADJust`` command.

        Description:
            - (AWG5000 Series only) This command and query sets or returns the phase of the analog
              output.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:PHASe:ADJust?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:PHASe:ADJust?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce[n]:PHASe:ADJust value``
              command.

        SCPI Syntax:
            ```
            - SOURce[n]:PHASe:ADJust <NR3>
            - SOURce[n]:PHASe:ADJust?
            ```

        Info:
            - ``<NR3>``
        """
        return self._adjust


class SourceItemPdelayHold(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:PDELay:HOLD`` command.

    Description:
        - This command and query sets or returns the parameter that is retained when sampling rate
          or waveform length is changed.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:PDELay:HOLD?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:PDELay:HOLD?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce[n]:PDELay:HOLD value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:PDELay:HOLD {PHASe|DELay|POINt}
        - SOURce[n]:PDELay:HOLD?
        ```

    Info:
        - ``PHASe``
        - ``DELay``
        - ``POINt``
    """


class SourceItemPdelay(SCPICmdRead):
    """The ``SOURce[n]:PDELay`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:PDELay?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:PDELay?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.hold``: The ``SOURce[n]:PDELay:HOLD`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hold = SourceItemPdelayHold(device, f"{self._cmd_syntax}:HOLD")

    @property
    def hold(self) -> SourceItemPdelayHold:
        """Return the ``SOURce[n]:PDELay:HOLD`` command.

        Description:
            - This command and query sets or returns the parameter that is retained when sampling
              rate or waveform length is changed.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:PDELay:HOLD?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:PDELay:HOLD?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce[n]:PDELay:HOLD value``
              command.

        SCPI Syntax:
            ```
            - SOURce[n]:PDELay:HOLD {PHASe|DELay|POINt}
            - SOURce[n]:PDELay:HOLD?
            ```

        Info:
            - ``PHASe``
            - ``DELay``
            - ``POINt``
        """
        return self._hold


class SourceItemMarker2VoltageLevelImmediateOffset(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:OFFSet`` command.

    Description:
        - This command sets the marker offset. In the AWG7000 Series, when the DAC resolution is
          changed to 10 bits, marker output is not available. However, marker related parameters can
          be modified using SCPI commands.

    Usage:
        - Using the ``.query()`` method will send the
          ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:OFFSet?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:OFFSet?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:OFFSet value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:OFFSet <NR3>
        - SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:OFFSet?
        ```

    Info:
        - ``<NR3>``
    """


class SourceItemMarker2VoltageLevelImmediateLow(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:LOW`` command.

    Description:
        - This command sets the marker low level. In the AWG7000 Series, when the DAC resolution is
          changed to 10 bits, marker output is not available. However, marker related parameters can
          be modified using SCPI commands. Refer to the User Online Help for the setting range of
          marker high and marker low.

    Usage:
        - Using the ``.query()`` method will send the
          ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:LOW?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:LOW?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:LOW value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:LOW <NR3>
        - SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:LOW?
        ```

    Info:
        - ``<NR3>``
    """


class SourceItemMarker2VoltageLevelImmediateHigh(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:HIGH`` command.

    Description:
        - This command sets the marker high level. In the AWG7000 Series, when DAC resolution is
          changed to 10 bits, marker output is not available. However, marker related parameters can
          be modified using SCPI commands. Refer to the User Online Help for the setting range of
          marker high and marker low.

    Usage:
        - Using the ``.query()`` method will send the
          ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:HIGH?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:HIGH?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:HIGH value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:HIGH <NR3>
        - SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:HIGH?
        ```

    Info:
        - ``<NR3>``
    """


class SourceItemMarker2VoltageLevelImmediateAmplitude(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:AMPLitude`` command.

    Description:
        - This command sets the marker amplitude. In the AWG7000 Series, when the DAC resolution is
          changed to 10 bits, marker output is not available. However, marker related parameters can
          be modified using SCPI commands.

    Usage:
        - Using the ``.query()`` method will send the
          ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:AMPLitude?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:AMPLitude?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:AMPLitude value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:AMPLitude <NR3>
        - SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:AMPLitude?
        ```

    Info:
        - ``<NR3>``
    """


class SourceItemMarker2VoltageLevelImmediate(SCPICmdRead):
    """The ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.high``: The ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:HIGH`` command.
        - ``.low``: The ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:LOW`` command.
        - ``.offset``: The ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:OFFSet`` command.
        - ``.amplitude``: The ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:AMPLitude`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._high = SourceItemMarker2VoltageLevelImmediateHigh(device, f"{self._cmd_syntax}:HIGH")
        self._low = SourceItemMarker2VoltageLevelImmediateLow(device, f"{self._cmd_syntax}:LOW")
        self._offset = SourceItemMarker2VoltageLevelImmediateOffset(
            device, f"{self._cmd_syntax}:OFFSet"
        )
        self._amplitude = SourceItemMarker2VoltageLevelImmediateAmplitude(
            device, f"{self._cmd_syntax}:AMPLitude"
        )

    @property
    def high(self) -> SourceItemMarker2VoltageLevelImmediateHigh:
        """Return the ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:HIGH`` command.

        Description:
            - This command sets the marker high level. In the AWG7000 Series, when DAC resolution is
              changed to 10 bits, marker output is not available. However, marker related parameters
              can be modified using SCPI commands. Refer to the User Online Help for the setting
              range of marker high and marker low.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:HIGH?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:HIGH?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:HIGH value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:HIGH <NR3>
            - SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:HIGH?
            ```

        Info:
            - ``<NR3>``
        """
        return self._high

    @property
    def low(self) -> SourceItemMarker2VoltageLevelImmediateLow:
        """Return the ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:LOW`` command.

        Description:
            - This command sets the marker low level. In the AWG7000 Series, when the DAC resolution
              is changed to 10 bits, marker output is not available. However, marker related
              parameters can be modified using SCPI commands. Refer to the User Online Help for the
              setting range of marker high and marker low.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:LOW?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:LOW?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:LOW value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:LOW <NR3>
            - SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:LOW?
            ```

        Info:
            - ``<NR3>``
        """
        return self._low

    @property
    def offset(self) -> SourceItemMarker2VoltageLevelImmediateOffset:
        """Return the ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:OFFSet`` command.

        Description:
            - This command sets the marker offset. In the AWG7000 Series, when the DAC resolution is
              changed to 10 bits, marker output is not available. However, marker related parameters
              can be modified using SCPI commands.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:OFFSet?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:OFFSet?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:OFFSet value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:OFFSet <NR3>
            - SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:OFFSet?
            ```

        Info:
            - ``<NR3>``
        """
        return self._offset

    @property
    def amplitude(self) -> SourceItemMarker2VoltageLevelImmediateAmplitude:
        """Return the ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:AMPLitude`` command.

        Description:
            - This command sets the marker amplitude. In the AWG7000 Series, when the DAC resolution
              is changed to 10 bits, marker output is not available. However, marker related
              parameters can be modified using SCPI commands.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:AMPLitude?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:AMPLitude?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:AMPLitude value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:AMPLitude <NR3>
            - SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:AMPLitude?
            ```

        Info:
            - ``<NR3>``
        """
        return self._amplitude


class SourceItemMarker2VoltageLevel(SCPICmdRead):
    """The ``SOURce[n]:MARKer2:VOLTage:LEVel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:MARKer2:VOLTage:LEVel?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:MARKer2:VOLTage:LEVel?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.immediate``: The ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._immediate = SourceItemMarker2VoltageLevelImmediate(
            device, f"{self._cmd_syntax}:IMMediate"
        )

    @property
    def immediate(self) -> SourceItemMarker2VoltageLevelImmediate:
        """Return the ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.high``: The ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:HIGH`` command.
            - ``.low``: The ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:LOW`` command.
            - ``.offset``: The ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:OFFSet`` command.
            - ``.amplitude``: The ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate:AMPLitude`` command.
        """
        return self._immediate


class SourceItemMarker2Voltage(SCPICmdRead):
    """The ``SOURce[n]:MARKer2:VOLTage`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:MARKer2:VOLTage?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:MARKer2:VOLTage?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.level``: The ``SOURce[n]:MARKer2:VOLTage:LEVel`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._level = SourceItemMarker2VoltageLevel(device, f"{self._cmd_syntax}:LEVel")

    @property
    def level(self) -> SourceItemMarker2VoltageLevel:
        """Return the ``SOURce[n]:MARKer2:VOLTage:LEVel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:MARKer2:VOLTage:LEVel?``
              query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:MARKer2:VOLTage:LEVel?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.immediate``: The ``SOURce[n]:MARKer2:VOLTage:LEVel:IMMediate`` command tree.
        """
        return self._level


class SourceItemMarker2Delay(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:MARKer2:DELay`` command.

    Description:
        - This command and query sets or returns the marker delay. Marker delay is independent for
          each channel. In the AWG7000 Series when DAC resolution is changed to 10 bits, marker
          output is not available. However, marker related parameters can be modified using SCPI
          commands.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:MARKer2:DELay?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:MARKer2:DELay?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce[n]:MARKer2:DELay value``
          command.

    SCPI Syntax:
        ```
        - SOURce[n]:MARKer2:DELay <NR3>
        - SOURce[n]:MARKer2:DELay?
        ```

    Info:
        - ``<NR3>``
    """


class SourceItemMarker2(SCPICmdRead):
    """The ``SOURce[n]:MARKer2`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:MARKer2?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:MARKer2?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.delay``: The ``SOURce[n]:MARKer2:DELay`` command.
        - ``.voltage``: The ``SOURce[n]:MARKer2:VOLTage`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._delay = SourceItemMarker2Delay(device, f"{self._cmd_syntax}:DELay")
        self._voltage = SourceItemMarker2Voltage(device, f"{self._cmd_syntax}:VOLTage")

    @property
    def delay(self) -> SourceItemMarker2Delay:
        """Return the ``SOURce[n]:MARKer2:DELay`` command.

        Description:
            - This command and query sets or returns the marker delay. Marker delay is independent
              for each channel. In the AWG7000 Series when DAC resolution is changed to 10 bits,
              marker output is not available. However, marker related parameters can be modified
              using SCPI commands.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:MARKer2:DELay?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:MARKer2:DELay?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce[n]:MARKer2:DELay value``
              command.

        SCPI Syntax:
            ```
            - SOURce[n]:MARKer2:DELay <NR3>
            - SOURce[n]:MARKer2:DELay?
            ```

        Info:
            - ``<NR3>``
        """
        return self._delay

    @property
    def voltage(self) -> SourceItemMarker2Voltage:
        """Return the ``SOURce[n]:MARKer2:VOLTage`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:MARKer2:VOLTage?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:MARKer2:VOLTage?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.level``: The ``SOURce[n]:MARKer2:VOLTage:LEVel`` command tree.
        """
        return self._voltage


class SourceItemMarker1VoltageLevelImmediateOffset(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:OFFSet`` command.

    Description:
        - This command sets the marker offset. In the AWG7000 Series, when the DAC resolution is
          changed to 10 bits, marker output is not available. However, marker related parameters can
          be modified using SCPI commands.

    Usage:
        - Using the ``.query()`` method will send the
          ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:OFFSet?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:OFFSet?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:OFFSet value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:OFFSet <NR3>
        - SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:OFFSet?
        ```

    Info:
        - ``<NR3>``
    """


class SourceItemMarker1VoltageLevelImmediateLow(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:LOW`` command.

    Description:
        - This command sets the marker low level. In the AWG7000 Series, when the DAC resolution is
          changed to 10 bits, marker output is not available. However, marker related parameters can
          be modified using SCPI commands. Refer to the User Online Help for the setting range of
          marker high and marker low.

    Usage:
        - Using the ``.query()`` method will send the
          ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:LOW?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:LOW?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:LOW value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:LOW <NR3>
        - SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:LOW?
        ```

    Info:
        - ``<NR3>``
    """


class SourceItemMarker1VoltageLevelImmediateHigh(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:HIGH`` command.

    Description:
        - This command sets the marker high level. In the AWG7000 Series, when DAC resolution is
          changed to 10 bits, marker output is not available. However, marker related parameters can
          be modified using SCPI commands. Refer to the User Online Help for the setting range of
          marker high and marker low.

    Usage:
        - Using the ``.query()`` method will send the
          ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:HIGH?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:HIGH?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:HIGH value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:HIGH <NR3>
        - SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:HIGH?
        ```

    Info:
        - ``<NR3>``
    """


class SourceItemMarker1VoltageLevelImmediateAmplitude(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:AMPLitude`` command.

    Description:
        - This command sets the marker amplitude. In the AWG7000 Series, when the DAC resolution is
          changed to 10 bits, marker output is not available. However, marker related parameters can
          be modified using SCPI commands.

    Usage:
        - Using the ``.query()`` method will send the
          ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:AMPLitude?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:AMPLitude?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:AMPLitude value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:AMPLitude <NR3>
        - SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:AMPLitude?
        ```

    Info:
        - ``<NR3>``
    """


class SourceItemMarker1VoltageLevelImmediate(SCPICmdRead):
    """The ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.high``: The ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:HIGH`` command.
        - ``.low``: The ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:LOW`` command.
        - ``.offset``: The ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:OFFSet`` command.
        - ``.amplitude``: The ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:AMPLitude`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._high = SourceItemMarker1VoltageLevelImmediateHigh(device, f"{self._cmd_syntax}:HIGH")
        self._low = SourceItemMarker1VoltageLevelImmediateLow(device, f"{self._cmd_syntax}:LOW")
        self._offset = SourceItemMarker1VoltageLevelImmediateOffset(
            device, f"{self._cmd_syntax}:OFFSet"
        )
        self._amplitude = SourceItemMarker1VoltageLevelImmediateAmplitude(
            device, f"{self._cmd_syntax}:AMPLitude"
        )

    @property
    def high(self) -> SourceItemMarker1VoltageLevelImmediateHigh:
        """Return the ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:HIGH`` command.

        Description:
            - This command sets the marker high level. In the AWG7000 Series, when DAC resolution is
              changed to 10 bits, marker output is not available. However, marker related parameters
              can be modified using SCPI commands. Refer to the User Online Help for the setting
              range of marker high and marker low.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:HIGH?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:HIGH?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:HIGH value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:HIGH <NR3>
            - SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:HIGH?
            ```

        Info:
            - ``<NR3>``
        """
        return self._high

    @property
    def low(self) -> SourceItemMarker1VoltageLevelImmediateLow:
        """Return the ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:LOW`` command.

        Description:
            - This command sets the marker low level. In the AWG7000 Series, when the DAC resolution
              is changed to 10 bits, marker output is not available. However, marker related
              parameters can be modified using SCPI commands. Refer to the User Online Help for the
              setting range of marker high and marker low.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:LOW?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:LOW?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:LOW value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:LOW <NR3>
            - SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:LOW?
            ```

        Info:
            - ``<NR3>``
        """
        return self._low

    @property
    def offset(self) -> SourceItemMarker1VoltageLevelImmediateOffset:
        """Return the ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:OFFSet`` command.

        Description:
            - This command sets the marker offset. In the AWG7000 Series, when the DAC resolution is
              changed to 10 bits, marker output is not available. However, marker related parameters
              can be modified using SCPI commands.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:OFFSet?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:OFFSet?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:OFFSet value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:OFFSet <NR3>
            - SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:OFFSet?
            ```

        Info:
            - ``<NR3>``
        """
        return self._offset

    @property
    def amplitude(self) -> SourceItemMarker1VoltageLevelImmediateAmplitude:
        """Return the ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:AMPLitude`` command.

        Description:
            - This command sets the marker amplitude. In the AWG7000 Series, when the DAC resolution
              is changed to 10 bits, marker output is not available. However, marker related
              parameters can be modified using SCPI commands.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:AMPLitude?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:AMPLitude?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:AMPLitude value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:AMPLitude <NR3>
            - SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:AMPLitude?
            ```

        Info:
            - ``<NR3>``
        """
        return self._amplitude


class SourceItemMarker1VoltageLevel(SCPICmdRead):
    """The ``SOURce[n]:MARKer1:VOLTage:LEVel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:MARKer1:VOLTage:LEVel?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:MARKer1:VOLTage:LEVel?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.immediate``: The ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._immediate = SourceItemMarker1VoltageLevelImmediate(
            device, f"{self._cmd_syntax}:IMMediate"
        )

    @property
    def immediate(self) -> SourceItemMarker1VoltageLevelImmediate:
        """Return the ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.high``: The ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:HIGH`` command.
            - ``.low``: The ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:LOW`` command.
            - ``.offset``: The ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:OFFSet`` command.
            - ``.amplitude``: The ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate:AMPLitude`` command.
        """
        return self._immediate


class SourceItemMarker1Voltage(SCPICmdRead):
    """The ``SOURce[n]:MARKer1:VOLTage`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:MARKer1:VOLTage?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:MARKer1:VOLTage?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.level``: The ``SOURce[n]:MARKer1:VOLTage:LEVel`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._level = SourceItemMarker1VoltageLevel(device, f"{self._cmd_syntax}:LEVel")

    @property
    def level(self) -> SourceItemMarker1VoltageLevel:
        """Return the ``SOURce[n]:MARKer1:VOLTage:LEVel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:MARKer1:VOLTage:LEVel?``
              query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:MARKer1:VOLTage:LEVel?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.immediate``: The ``SOURce[n]:MARKer1:VOLTage:LEVel:IMMediate`` command tree.
        """
        return self._level


class SourceItemMarker1Delay(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:MARKer1:DELay`` command.

    Description:
        - This command and query sets or returns the marker delay. Marker delay is independent for
          each channel. In the AWG7000 Series when DAC resolution is changed to 10 bits, marker
          output is not available. However, marker related parameters can be modified using SCPI
          commands.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:MARKer1:DELay?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:MARKer1:DELay?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce[n]:MARKer1:DELay value``
          command.

    SCPI Syntax:
        ```
        - SOURce[n]:MARKer1:DELay <NR3>
        - SOURce[n]:MARKer1:DELay?
        ```

    Info:
        - ``<NR3>``
    """


class SourceItemMarker1(SCPICmdRead):
    """The ``SOURce[n]:MARKer1`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:MARKer1?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:MARKer1?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.delay``: The ``SOURce[n]:MARKer1:DELay`` command.
        - ``.voltage``: The ``SOURce[n]:MARKer1:VOLTage`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._delay = SourceItemMarker1Delay(device, f"{self._cmd_syntax}:DELay")
        self._voltage = SourceItemMarker1Voltage(device, f"{self._cmd_syntax}:VOLTage")

    @property
    def delay(self) -> SourceItemMarker1Delay:
        """Return the ``SOURce[n]:MARKer1:DELay`` command.

        Description:
            - This command and query sets or returns the marker delay. Marker delay is independent
              for each channel. In the AWG7000 Series when DAC resolution is changed to 10 bits,
              marker output is not available. However, marker related parameters can be modified
              using SCPI commands.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:MARKer1:DELay?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:MARKer1:DELay?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce[n]:MARKer1:DELay value``
              command.

        SCPI Syntax:
            ```
            - SOURce[n]:MARKer1:DELay <NR3>
            - SOURce[n]:MARKer1:DELay?
            ```

        Info:
            - ``<NR3>``
        """
        return self._delay

    @property
    def voltage(self) -> SourceItemMarker1Voltage:
        """Return the ``SOURce[n]:MARKer1:VOLTage`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:MARKer1:VOLTage?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:MARKer1:VOLTage?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.level``: The ``SOURce[n]:MARKer1:VOLTage:LEVel`` command tree.
        """
        return self._voltage


class SourceItemFunctionUser(SCPICmdWrite, SCPICmdRead):
    r"""The ``SOURce[n]:FUNCtion:USER`` command.

    Description:
        - This command and query sets or returns the waveform to waveform memory. Use this command
          to directly load an AWG400/500/600/700 series waveform (WFM), pattern file (PAT), or
          sequence (SEQ) file from mass memory to a specified channel. However, when loading a
          sequence file, the SOURce's suffix is ignored. The waveform is internally converted to the
          AWG5000/AWG7000 series format and inserted into the current waveform list. To successfully
          load a waveform, the waveform name should conform to AWG5000/AWG7000 series waveform
          naming conventions. If you specify the SEQ file, Run Mode is changed to Sequence. If you
          specify a WFM or PAT file while the Run Mode is Sequence, Run Mode is changed to
          Continuous. When you import a sequence file (\*.SEQ) for the AWG400/500/600/700 series
          using this command, all the user-defined waveforms are deleted before the import
          operation.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:FUNCtion:USER?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:FUNCtion:USER?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce[n]:FUNCtion:USER value``
          command.

    SCPI Syntax:
        ```
        - SOURce[n]:FUNCtion:USER <Waveform file_name>[,<msus>]
        - SOURce[n]:FUNCtion:USER?
        ```

    Info:
        - ``<Waveform file_name>`` :: = <string>.
    """


class SourceItemFunction(SCPICmdRead):
    """The ``SOURce[n]:FUNCtion`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:FUNCtion?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:FUNCtion?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.user``: The ``SOURce[n]:FUNCtion:USER`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._user = SourceItemFunctionUser(device, f"{self._cmd_syntax}:USER")

    @property
    def user(self) -> SourceItemFunctionUser:
        r"""Return the ``SOURce[n]:FUNCtion:USER`` command.

        Description:
            - This command and query sets or returns the waveform to waveform memory. Use this
              command to directly load an AWG400/500/600/700 series waveform (WFM), pattern file
              (PAT), or sequence (SEQ) file from mass memory to a specified channel. However, when
              loading a sequence file, the SOURce's suffix is ignored. The waveform is internally
              converted to the AWG5000/AWG7000 series format and inserted into the current waveform
              list. To successfully load a waveform, the waveform name should conform to
              AWG5000/AWG7000 series waveform naming conventions. If you specify the SEQ file, Run
              Mode is changed to Sequence. If you specify a WFM or PAT file while the Run Mode is
              Sequence, Run Mode is changed to Continuous. When you import a sequence file (\*.SEQ)
              for the AWG400/500/600/700 series using this command, all the user-defined waveforms
              are deleted before the import operation.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:FUNCtion:USER?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:FUNCtion:USER?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce[n]:FUNCtion:USER value``
              command.

        SCPI Syntax:
            ```
            - SOURce[n]:FUNCtion:USER <Waveform file_name>[,<msus>]
            - SOURce[n]:FUNCtion:USER?
            ```

        Info:
            - ``<Waveform file_name>`` :: = <string>.
        """
        return self._user


class SourceItemFrequencyFixed(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:FREQuency:FIXed`` command.

    Description:
        - This command and query sets or returns the sampling frequency of the arbitrary waveform
          generator. Sampling frequency can be set when the internal clock source is selected and
          one of the following conditions is met: Internal is selected as Reference Source. External
          is selected as Reference Source and Fixed is selected as External Reference Type. CW and
          FIXed are aliases and have the same effect. Note that the frequency of the waveform output
          by the instrument is calculated as: The minimum number of points in a waveform for the
          instrument is 1.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:FREQuency:FIXed?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:FREQuency:FIXed?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce[n]:FREQuency:FIXed value``
          command.

    SCPI Syntax:
        ```
        - SOURce[n]:FREQuency:FIXed <NR3>
        - SOURce[n]:FREQuency:FIXed?
        ```

    Info:
        - ``<NR3>`` . The value must be between 10 MHz to 10 GHz.
    """


class SourceItemFrequencyCw(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:FREQuency:CW`` command.

    Description:
        - This command and query sets or returns the sampling frequency of the arbitrary waveform
          generator. Sampling frequency can be set when the internal clock source is selected and
          one of the following conditions is met: Internal is selected as Reference Source. External
          is selected as Reference Source and Fixed is selected as External Reference Type. CW and
          FIXed are aliases and have the same effect. Note that the frequency of the waveform output
          by the instrument is calculated as: The minimum number of points in a waveform for the
          instrument is 1.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:FREQuency:CW?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:FREQuency:CW?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce[n]:FREQuency:CW value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:FREQuency:CW <NR3>
        - SOURce[n]:FREQuency:CW?
        ```

    Info:
        - ``<NR3>`` . The value must be between 10 MHz to 10 GHz.
    """


class SourceItemFrequency(SCPICmdRead):
    """The ``SOURce[n]:FREQuency`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:FREQuency?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.cw``: The ``SOURce[n]:FREQuency:CW`` command.
        - ``.fixed``: The ``SOURce[n]:FREQuency:FIXed`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._cw = SourceItemFrequencyCw(device, f"{self._cmd_syntax}:CW")
        self._fixed = SourceItemFrequencyFixed(device, f"{self._cmd_syntax}:FIXed")

    @property
    def cw(self) -> SourceItemFrequencyCw:
        """Return the ``SOURce[n]:FREQuency:CW`` command.

        Description:
            - This command and query sets or returns the sampling frequency of the arbitrary
              waveform generator. Sampling frequency can be set when the internal clock source is
              selected and one of the following conditions is met: Internal is selected as Reference
              Source. External is selected as Reference Source and Fixed is selected as External
              Reference Type. CW and FIXed are aliases and have the same effect. Note that the
              frequency of the waveform output by the instrument is calculated as: The minimum
              number of points in a waveform for the instrument is 1.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:FREQuency:CW?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:FREQuency:CW?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce[n]:FREQuency:CW value``
              command.

        SCPI Syntax:
            ```
            - SOURce[n]:FREQuency:CW <NR3>
            - SOURce[n]:FREQuency:CW?
            ```

        Info:
            - ``<NR3>`` . The value must be between 10 MHz to 10 GHz.
        """
        return self._cw

    @property
    def fixed(self) -> SourceItemFrequencyFixed:
        """Return the ``SOURce[n]:FREQuency:FIXed`` command.

        Description:
            - This command and query sets or returns the sampling frequency of the arbitrary
              waveform generator. Sampling frequency can be set when the internal clock source is
              selected and one of the following conditions is met: Internal is selected as Reference
              Source. External is selected as Reference Source and Fixed is selected as External
              Reference Type. CW and FIXed are aliases and have the same effect. Note that the
              frequency of the waveform output by the instrument is calculated as: The minimum
              number of points in a waveform for the instrument is 1.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:FREQuency:FIXed?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:FREQuency:FIXed?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce[n]:FREQuency:FIXed value``
              command.

        SCPI Syntax:
            ```
            - SOURce[n]:FREQuency:FIXed <NR3>
            - SOURce[n]:FREQuency:FIXed?
            ```

        Info:
            - ``<NR3>`` . The value must be between 10 MHz to 10 GHz.
        """
        return self._fixed


class SourceItemDigitalVoltageLevelImmediateOffset(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:OFFSet`` command.

    Description:
        - (AWG5000 Series only) This command and query sets or returns the offset of digital output.
          This command is available only for AWG5000B and AWG5000C instruments with option 03.

    Usage:
        - Using the ``.query()`` method will send the
          ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:OFFSet?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:OFFSet?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:OFFSet value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:OFFSet <NR3>
        - SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:OFFSet?
        ```

    Info:
        - ``<NR3>``
    """


class SourceItemDigitalVoltageLevelImmediateLow(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:LOW`` command.

    Description:
        - (AWG5000 Series only) This command and query sets or returns the low digital output. This
          command is available only for AWG5000B and AWG5000C instruments with option 03.

    Usage:
        - Using the ``.query()`` method will send the
          ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:LOW?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:LOW?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:LOW value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:LOW <NR3>
        - SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:LOW?
        ```

    Info:
        - ``<NR3>``
    """


class SourceItemDigitalVoltageLevelImmediateHigh(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:HIGH`` command.

    Description:
        - (AWG5000 Series only) This command and query sets or returns the high digital output. This
          command is available only for AWG5000B and AWG5000C instruments with option 03.

    Usage:
        - Using the ``.query()`` method will send the
          ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:HIGH?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:HIGH?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:HIGH value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:HIGH <NR3>
        - SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:HIGH?
        ```

    Info:
        - ``<NR3>``
    """


class SourceItemDigitalVoltageLevelImmediateAmplitude(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:AMPLitude`` command.

    Description:
        - (AWG5000 Series only) This command and query sets or returns the amplitude of digital
          output. This command is available only for AWG500B and AWG5000C instruments with option
          03.

    Usage:
        - Using the ``.query()`` method will send the
          ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:AMPLitude?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:AMPLitude?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:AMPLitude value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:AMPLitude <NR3>
        - SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:AMPLitude?
        ```

    Info:
        - ``<NR3>``
        - ``pp``
    """


class SourceItemDigitalVoltageLevelImmediate(SCPICmdRead):
    """The ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.high``: The ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:HIGH`` command.
        - ``.low``: The ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:LOW`` command.
        - ``.offset``: The ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:OFFSet`` command.
        - ``.amplitude``: The ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:AMPLitude`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._high = SourceItemDigitalVoltageLevelImmediateHigh(device, f"{self._cmd_syntax}:HIGH")
        self._low = SourceItemDigitalVoltageLevelImmediateLow(device, f"{self._cmd_syntax}:LOW")
        self._offset = SourceItemDigitalVoltageLevelImmediateOffset(
            device, f"{self._cmd_syntax}:OFFSet"
        )
        self._amplitude = SourceItemDigitalVoltageLevelImmediateAmplitude(
            device, f"{self._cmd_syntax}:AMPLitude"
        )

    @property
    def high(self) -> SourceItemDigitalVoltageLevelImmediateHigh:
        """Return the ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:HIGH`` command.

        Description:
            - (AWG5000 Series only) This command and query sets or returns the high digital output.
              This command is available only for AWG5000B and AWG5000C instruments with option 03.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:HIGH?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:HIGH?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:HIGH value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:HIGH <NR3>
            - SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:HIGH?
            ```

        Info:
            - ``<NR3>``
        """
        return self._high

    @property
    def low(self) -> SourceItemDigitalVoltageLevelImmediateLow:
        """Return the ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:LOW`` command.

        Description:
            - (AWG5000 Series only) This command and query sets or returns the low digital output.
              This command is available only for AWG5000B and AWG5000C instruments with option 03.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:LOW?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:LOW?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:LOW value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:LOW <NR3>
            - SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:LOW?
            ```

        Info:
            - ``<NR3>``
        """
        return self._low

    @property
    def offset(self) -> SourceItemDigitalVoltageLevelImmediateOffset:
        """Return the ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:OFFSet`` command.

        Description:
            - (AWG5000 Series only) This command and query sets or returns the offset of digital
              output. This command is available only for AWG5000B and AWG5000C instruments with
              option 03.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:OFFSet?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:OFFSet?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:OFFSet value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:OFFSet <NR3>
            - SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:OFFSet?
            ```

        Info:
            - ``<NR3>``
        """
        return self._offset

    @property
    def amplitude(self) -> SourceItemDigitalVoltageLevelImmediateAmplitude:
        """Return the ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:AMPLitude`` command.

        Description:
            - (AWG5000 Series only) This command and query sets or returns the amplitude of digital
              output. This command is available only for AWG500B and AWG5000C instruments with
              option 03.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:AMPLitude?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:AMPLitude?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:AMPLitude value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:AMPLitude <NR3>
            - SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:AMPLitude?
            ```

        Info:
            - ``<NR3>``
            - ``pp``
        """
        return self._amplitude


class SourceItemDigitalVoltageLevel(SCPICmdRead):
    """The ``SOURce[n]:DIGital:VOLTage:LEVel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:DIGital:VOLTage:LEVel?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:DIGital:VOLTage:LEVel?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.immediate``: The ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._immediate = SourceItemDigitalVoltageLevelImmediate(
            device, f"{self._cmd_syntax}:IMMediate"
        )

    @property
    def immediate(self) -> SourceItemDigitalVoltageLevelImmediate:
        """Return the ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.high``: The ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:HIGH`` command.
            - ``.low``: The ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:LOW`` command.
            - ``.offset``: The ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:OFFSet`` command.
            - ``.amplitude``: The ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate:AMPLitude`` command.
        """
        return self._immediate


class SourceItemDigitalVoltage(SCPICmdRead):
    """The ``SOURce[n]:DIGital:VOLTage`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:DIGital:VOLTage?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:DIGital:VOLTage?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.level``: The ``SOURce[n]:DIGital:VOLTage:LEVel`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._level = SourceItemDigitalVoltageLevel(device, f"{self._cmd_syntax}:LEVel")

    @property
    def level(self) -> SourceItemDigitalVoltageLevel:
        """Return the ``SOURce[n]:DIGital:VOLTage:LEVel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:DIGital:VOLTage:LEVel?``
              query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:DIGital:VOLTage:LEVel?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.immediate``: The ``SOURce[n]:DIGital:VOLTage:LEVel:IMMediate`` command tree.
        """
        return self._level


class SourceItemDigital(SCPICmdRead):
    """The ``SOURce[n]:DIGital`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:DIGital?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:DIGital?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.voltage``: The ``SOURce[n]:DIGital:VOLTage`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._voltage = SourceItemDigitalVoltage(device, f"{self._cmd_syntax}:VOLTage")

    @property
    def voltage(self) -> SourceItemDigitalVoltage:
        """Return the ``SOURce[n]:DIGital:VOLTage`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:DIGital:VOLTage?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:DIGital:VOLTage?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.level``: The ``SOURce[n]:DIGital:VOLTage:LEVel`` command tree.
        """
        return self._voltage


class SourceItemDelayPoints(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:DELay:POINts`` command.

    Description:
        - This command and query sets or returns the delay (in points) of the analog output.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:DELay:POINts?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:DELay:POINts?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce[n]:DELay:POINts value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:DELay:POINts <NR3>
        - SOURce[n]:DELay:POINts?
        ```

    Info:
        - ``<NR3>``
    """


class SourceItemDelayAdjust(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:DELay:ADJust`` command.

    Description:
        - This command and query sets or returns the delay (in seconds) of the analog output.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:DELay:ADJust?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:DELay:ADJust?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce[n]:DELay:ADJust value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:DELay:ADJust <NR3>
        - SOURce[n]:DELay:ADJust?
        ```

    Info:
        - ``<NR3>``
    """


class SourceItemDelay(SCPICmdRead):
    """The ``SOURce[n]:DELay`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:DELay?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:DELay?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.points``: The ``SOURce[n]:DELay:POINts`` command.
        - ``.adjust``: The ``SOURce[n]:DELay:ADJust`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._points = SourceItemDelayPoints(device, f"{self._cmd_syntax}:POINts")
        self._adjust = SourceItemDelayAdjust(device, f"{self._cmd_syntax}:ADJust")

    @property
    def points(self) -> SourceItemDelayPoints:
        """Return the ``SOURce[n]:DELay:POINts`` command.

        Description:
            - This command and query sets or returns the delay (in points) of the analog output.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:DELay:POINts?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:DELay:POINts?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce[n]:DELay:POINts value``
              command.

        SCPI Syntax:
            ```
            - SOURce[n]:DELay:POINts <NR3>
            - SOURce[n]:DELay:POINts?
            ```

        Info:
            - ``<NR3>``
        """
        return self._points

    @property
    def adjust(self) -> SourceItemDelayAdjust:
        """Return the ``SOURce[n]:DELay:ADJust`` command.

        Description:
            - This command and query sets or returns the delay (in seconds) of the analog output.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:DELay:ADJust?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:DELay:ADJust?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce[n]:DELay:ADJust value``
              command.

        SCPI Syntax:
            ```
            - SOURce[n]:DELay:ADJust <NR3>
            - SOURce[n]:DELay:ADJust?
            ```

        Info:
            - ``<NR3>``
        """
        return self._adjust


class SourceItemDacResolution(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:DAC:RESolution`` command.

    Description:
        - This command and query sets or returns the DAC resolution.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:DAC:RESolution?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:DAC:RESolution?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce[n]:DAC:RESolution value``
          command.

    SCPI Syntax:
        ```
        - SOURce[n]:DAC:RESolution <NR1>
        - SOURce[n]:DAC:RESolution?
        ```

    Info:
        - ``<NR1>``
        - ``8`` sets the DAC resolution to 8 bits.
        - ``10`` sets the DAC resolution to 10 bits.
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
            - This command and query sets or returns the DAC resolution.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:DAC:RESolution?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:DAC:RESolution?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce[n]:DAC:RESolution value``
              command.

        SCPI Syntax:
            ```
            - SOURce[n]:DAC:RESolution <NR1>
            - SOURce[n]:DAC:RESolution?
            ```

        Info:
            - ``<NR1>``
            - ``8`` sets the DAC resolution to 8 bits.
            - ``10`` sets the DAC resolution to 10 bits.
        """
        return self._resolution


class SourceItemCombineFeed(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce[n]:COMBine:FEED`` command.

    Description:
        - (AWG5000 Series only) This command adds the signal from an external input to the output of
          the channel.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:COMBine:FEED?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:COMBine:FEED?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce[n]:COMBine:FEED value`` command.

    SCPI Syntax:
        ```
        - SOURce[n]:COMBine:FEED {'ESIGnal'|''}
        - SOURce[n]:COMBine:FEED?
        ```

    Info:
        - ``'ESIGnal'`` - Adds the input from the external signal.
        - ``''`` - Removes the signal feed.
    """


class SourceItemCombine(SCPICmdRead):
    """The ``SOURce[n]:COMBine`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]:COMBine?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]:COMBine?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.feed``: The ``SOURce[n]:COMBine:FEED`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._feed = SourceItemCombineFeed(device, f"{self._cmd_syntax}:FEED")

    @property
    def feed(self) -> SourceItemCombineFeed:
        """Return the ``SOURce[n]:COMBine:FEED`` command.

        Description:
            - (AWG5000 Series only) This command adds the signal from an external input to the
              output of the channel.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:COMBine:FEED?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:COMBine:FEED?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce[n]:COMBine:FEED value``
              command.

        SCPI Syntax:
            ```
            - SOURce[n]:COMBine:FEED {'ESIGnal'|''}
            - SOURce[n]:COMBine:FEED?
            ```

        Info:
            - ``'ESIGnal'`` - Adds the input from the external signal.
            - ``''`` - Removes the signal feed.
        """
        return self._feed


#  pylint: disable=too-many-instance-attributes
class SourceItem(ValidatedChannel, SCPICmdRead):
    """The ``SOURce[n]`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce[n]?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce[n]?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.frequency``: The ``SOURce[n]:FREQuency`` command tree.
        - ``.roscillator``: The ``SOURce[n]:ROSCillator`` command tree.
        - ``.combine``: The ``SOURce[n]:COMBine`` command tree.
        - ``.dac``: The ``SOURce[n]:DAC`` command tree.
        - ``.delay``: The ``SOURce[n]:DELay`` command tree.
        - ``.digital``: The ``SOURce[n]:DIGital`` command tree.
        - ``.function``: The ``SOURce[n]:FUNCtion`` command tree.
        - ``.marker1``: The ``SOURce[n]:MARKer1`` command tree.
        - ``.marker2``: The ``SOURce[n]:MARKer2`` command tree.
        - ``.pdelay``: The ``SOURce[n]:PDELay`` command tree.
        - ``.phase``: The ``SOURce[n]:PHASe`` command tree.
        - ``.skew``: The ``SOURce[n]:SKEW`` command.
        - ``.voltage``: The ``SOURce[n]:VOLTage`` command tree.
        - ``.waveform``: The ``SOURce[n]:WAVeform`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SOURce[n]") -> None:
        super().__init__(device, cmd_syntax)
        self._frequency = SourceItemFrequency(device, f"{self._cmd_syntax}:FREQuency")
        self._roscillator = SourceItemRoscillator(device, f"{self._cmd_syntax}:ROSCillator")
        self._combine = SourceItemCombine(device, f"{self._cmd_syntax}:COMBine")
        self._dac = SourceItemDac(device, f"{self._cmd_syntax}:DAC")
        self._delay = SourceItemDelay(device, f"{self._cmd_syntax}:DELay")
        self._digital = SourceItemDigital(device, f"{self._cmd_syntax}:DIGital")
        self._function = SourceItemFunction(device, f"{self._cmd_syntax}:FUNCtion")
        self._marker1 = SourceItemMarker1(device, f"{self._cmd_syntax}:MARKer1")
        self._marker2 = SourceItemMarker2(device, f"{self._cmd_syntax}:MARKer2")
        self._pdelay = SourceItemPdelay(device, f"{self._cmd_syntax}:PDELay")
        self._phase = SourceItemPhase(device, f"{self._cmd_syntax}:PHASe")
        self._skew = SourceItemSkew(device, f"{self._cmd_syntax}:SKEW")
        self._voltage = SourceItemVoltage(device, f"{self._cmd_syntax}:VOLTage")
        self._waveform = SourceItemWaveform(device, f"{self._cmd_syntax}:WAVeform")

    @property
    def frequency(self) -> SourceItemFrequency:
        """Return the ``SOURce[n]:FREQuency`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:FREQuency?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.cw``: The ``SOURce[n]:FREQuency:CW`` command.
            - ``.fixed``: The ``SOURce[n]:FREQuency:FIXed`` command.
        """
        return self._frequency

    @property
    def roscillator(self) -> SourceItemRoscillator:
        """Return the ``SOURce[n]:ROSCillator`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:ROSCillator?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:ROSCillator?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.frequency``: The ``SOURce[n]:ROSCillator:FREQuency`` command.
            - ``.multiplier``: The ``SOURce[n]:ROSCillator:MULTiplier`` command.
            - ``.source``: The ``SOURce[n]:ROSCillator:SOURce`` command.
            - ``.type``: The ``SOURce[n]:ROSCillator:TYPE`` command.
        """
        return self._roscillator

    @property
    def combine(self) -> SourceItemCombine:
        """Return the ``SOURce[n]:COMBine`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:COMBine?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:COMBine?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.feed``: The ``SOURce[n]:COMBine:FEED`` command.
        """
        return self._combine

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
    def delay(self) -> SourceItemDelay:
        """Return the ``SOURce[n]:DELay`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:DELay?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:DELay?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.points``: The ``SOURce[n]:DELay:POINts`` command.
            - ``.adjust``: The ``SOURce[n]:DELay:ADJust`` command.
        """
        return self._delay

    @property
    def digital(self) -> SourceItemDigital:
        """Return the ``SOURce[n]:DIGital`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:DIGital?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:DIGital?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.voltage``: The ``SOURce[n]:DIGital:VOLTage`` command tree.
        """
        return self._digital

    @property
    def function(self) -> SourceItemFunction:
        """Return the ``SOURce[n]:FUNCtion`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:FUNCtion?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:FUNCtion?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.user``: The ``SOURce[n]:FUNCtion:USER`` command.
        """
        return self._function

    @property
    def marker1(self) -> SourceItemMarker1:
        """Return the ``SOURce[n]:MARKer1`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:MARKer1?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:MARKer1?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.delay``: The ``SOURce[n]:MARKer1:DELay`` command.
            - ``.voltage``: The ``SOURce[n]:MARKer1:VOLTage`` command tree.
        """
        return self._marker1

    @property
    def marker2(self) -> SourceItemMarker2:
        """Return the ``SOURce[n]:MARKer2`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:MARKer2?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:MARKer2?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.delay``: The ``SOURce[n]:MARKer2:DELay`` command.
            - ``.voltage``: The ``SOURce[n]:MARKer2:VOLTage`` command tree.
        """
        return self._marker2

    @property
    def pdelay(self) -> SourceItemPdelay:
        """Return the ``SOURce[n]:PDELay`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:PDELay?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:PDELay?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.hold``: The ``SOURce[n]:PDELay:HOLD`` command.
        """
        return self._pdelay

    @property
    def phase(self) -> SourceItemPhase:
        """Return the ``SOURce[n]:PHASe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:PHASe?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:PHASe?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.adjust``: The ``SOURce[n]:PHASe:ADJust`` command.
        """
        return self._phase

    @property
    def skew(self) -> SourceItemSkew:
        """Return the ``SOURce[n]:SKEW`` command.

        Description:
            - This command and query sets or returns the skew for the waveform associated with a
              channel.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]:SKEW?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]:SKEW?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce[n]:SKEW value`` command.

        SCPI Syntax:
            ```
            - SOURce[n]:SKEW <NR3>
            - SOURce[n]:SKEW?
            ```

        Info:
            - ``<NR3>``
        """
        return self._skew

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
            - This command and query sets or returns the output waveform from the current waveform
              list for each channel when Run Mode is not Sequence. However, this command cannot be
              used to load a waveform stored in an AWG400/500/600/700 waveform or pattern file. To
              load a waveform stored in an AWG400/500/600/700 waveform or pattern file, use the
              ``SOURCEN:FUNCTION:USER`` command.

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

        Info:
            - ``<wfm_name>`` ::=<string>.
        """
        return self._waveform
