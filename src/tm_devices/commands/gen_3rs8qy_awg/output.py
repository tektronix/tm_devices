"""The output commands module.

These commands are used in the following models:
AWG70KA, AWG70KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - OUTPut[n]:ATTenuator:A1 <NR1>
    - OUTPut[n]:ATTenuator:A1?
    - OUTPut[n]:ATTenuator:A2 <NR1>
    - OUTPut[n]:ATTenuator:A2?
    - OUTPut[n]:ATTenuator:A3 <NR1>
    - OUTPut[n]:ATTenuator:A3?
    - OUTPut[n]:ATTenuator:DAC <NRf>
    - OUTPut[n]:ATTenuator:DAC?
    - OUTPut[n]:FILTer {NONE|BPASs|LPASs}
    - OUTPut[n]:FILTer:BPASs:RANGe {R10TO14GHZ|R13TO18GHZ}
    - OUTPut[n]:FILTer:BPASs:RANGe?
    - OUTPut[n]:FILTer?
    - OUTPut[n]:PATH {DIRect|AC|DCAmplified}
    - OUTPut[n]:PATH?
    - OUTPut[n]:STATe {0|1|OFF|ON}
    - OUTPut[n]:STATe?
    - OUTPut[n]:SVALue:ANALog:STATe {OFF|ZERO}
    - OUTPut[n]:SVALue:ANALog:STATe?
    - OUTPut[n]:SVALue:MARKer[m] {OFF|LOW}
    - OUTPut[n]:SVALue:MARKer[m]?
    - OUTPut[n]:WVALue:ANALog:STATe {FIRSt|ZERO}
    - OUTPut[n]:WVALue:ANALog:STATe?
    - OUTPut[n]:WVALue:MARKer[m] {FIRSt|LOW|HIGH}
    - OUTPut[n]:WVALue:MARKer[m]?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class OutputItemWvalueMarkerItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``OUTPut[n]:WVALue:MARKer[m]`` command.

    Description:
        - This command sets or returns the output condition of the specified marker of the specified
          channel while the instrument is in the waiting-for-trigger state or for a brief period
          after the waveform loads to the DAC and before the first point plays.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut[n]:WVALue:MARKer[m]?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut[n]:WVALue:MARKer[m]?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``OUTPut[n]:WVALue:MARKer[m] value``
          command.

    SCPI Syntax:
        ```
        - OUTPut[n]:WVALue:MARKer[m] {FIRSt|LOW|HIGH}
        - OUTPut[n]:WVALue:MARKer[m]?
        ```

    Info:
        - ``FIRSt`` sets the marker output level to match the first point in the waveform when the
          channel is in the waiting-for-trigger state.LOW sets the marker output to a logic level
          low for when the channel is in the waiting-for-trigger state.HIGH sets the marker output
          to a logic level high when the channel is in the waiting-for-trigger state.[n] determines
          the channel number. If omitted, interpreted as 1.[m] determines the marker number. If
          omitted, interpreted as 1.
        - ``*RST`` sets all channels to LOW.
    """


class OutputItemWvalueAnalogState(SCPICmdWrite, SCPICmdRead):
    """The ``OUTPut[n]:WVALue:ANALog:STATe`` command.

    Description:
        - This command sets or returns the output condition of a waveform of the specified channel
          while the instrument is in the waiting-for-trigger state or for a brief period after the
          waveform loads to the DAC and before the first point plays.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut[n]:WVALue:ANALog:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut[n]:WVALue:ANALog:STATe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``OUTPut[n]:WVALue:ANALog:STATe value``
          command.

    SCPI Syntax:
        ```
        - OUTPut[n]:WVALue:ANALog:STATe {FIRSt|ZERO}
        - OUTPut[n]:WVALue:ANALog:STATe?
        ```

    Info:
        - ``FIRSt`` sets the output level for channel 'n' to match the first point in the waveform
          when channel 'n' is in the Waiting-for-trigger state.ZERO sets the output level for
          channel 'n' to 0 volts when channel 'n' is in the Waiting-for-trigger state.[n] determines
          the channel number. If omitted, interpreted as 1.
        - ``*RST`` sets all channels to ZERO.
    """


class OutputItemWvalueAnalog(SCPICmdRead):
    """The ``OUTPut[n]:WVALue:ANALog`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut[n]:WVALue:ANALog?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut[n]:WVALue:ANALog?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``OUTPut[n]:WVALue:ANALog:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = OutputItemWvalueAnalogState(device, f"{self._cmd_syntax}:STATe")

    @property
    def state(self) -> OutputItemWvalueAnalogState:
        """Return the ``OUTPut[n]:WVALue:ANALog:STATe`` command.

        Description:
            - This command sets or returns the output condition of a waveform of the specified
              channel while the instrument is in the waiting-for-trigger state or for a brief period
              after the waveform loads to the DAC and before the first point plays.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut[n]:WVALue:ANALog:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut[n]:WVALue:ANALog:STATe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``OUTPut[n]:WVALue:ANALog:STATe value`` command.

        SCPI Syntax:
            ```
            - OUTPut[n]:WVALue:ANALog:STATe {FIRSt|ZERO}
            - OUTPut[n]:WVALue:ANALog:STATe?
            ```

        Info:
            - ``FIRSt`` sets the output level for channel 'n' to match the first point in the
              waveform when channel 'n' is in the Waiting-for-trigger state.ZERO sets the output
              level for channel 'n' to 0 volts when channel 'n' is in the Waiting-for-trigger
              state.[n] determines the channel number. If omitted, interpreted as 1.
            - ``*RST`` sets all channels to ZERO.
        """
        return self._state


class OutputItemWvalue(SCPICmdRead):
    """The ``OUTPut[n]:WVALue`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut[n]:WVALue?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut[n]:WVALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.marker``: The ``OUTPut[n]:WVALue:MARKer[m]`` command.
        - ``.analog``: The ``OUTPut[n]:WVALue:ANALog`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._marker: Dict[int, OutputItemWvalueMarkerItem] = DefaultDictPassKeyToFactory(
            lambda x: OutputItemWvalueMarkerItem(device, f"{self._cmd_syntax}:MARKer{x}")
        )
        self._analog = OutputItemWvalueAnalog(device, f"{self._cmd_syntax}:ANALog")

    @property
    def marker(self) -> Dict[int, OutputItemWvalueMarkerItem]:
        """Return the ``OUTPut[n]:WVALue:MARKer[m]`` command.

        Description:
            - This command sets or returns the output condition of the specified marker of the
              specified channel while the instrument is in the waiting-for-trigger state or for a
              brief period after the waveform loads to the DAC and before the first point plays.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut[n]:WVALue:MARKer[m]?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut[n]:WVALue:MARKer[m]?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``OUTPut[n]:WVALue:MARKer[m] value``
              command.

        SCPI Syntax:
            ```
            - OUTPut[n]:WVALue:MARKer[m] {FIRSt|LOW|HIGH}
            - OUTPut[n]:WVALue:MARKer[m]?
            ```

        Info:
            - ``FIRSt`` sets the marker output level to match the first point in the waveform when
              the channel is in the waiting-for-trigger state.LOW sets the marker output to a logic
              level low for when the channel is in the waiting-for-trigger state.HIGH sets the
              marker output to a logic level high when the channel is in the waiting-for-trigger
              state.[n] determines the channel number. If omitted, interpreted as 1.[m] determines
              the marker number. If omitted, interpreted as 1.
            - ``*RST`` sets all channels to LOW.
        """
        return self._marker

    @property
    def analog(self) -> OutputItemWvalueAnalog:
        """Return the ``OUTPut[n]:WVALue:ANALog`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut[n]:WVALue:ANALog?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut[n]:WVALue:ANALog?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``OUTPut[n]:WVALue:ANALog:STATe`` command.
        """
        return self._analog


class OutputItemSvalueMarkerItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``OUTPut[n]:SVALue:MARKer[m]`` command.

    Description:
        - This command sets or returns the output data position of the specified marker of the
          specified channel when in the stopped state.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut[n]:SVALue:MARKer[m]?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut[n]:SVALue:MARKer[m]?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``OUTPut[n]:SVALue:MARKer[m] value``
          command.

    SCPI Syntax:
        ```
        - OUTPut[n]:SVALue:MARKer[m] {OFF|LOW}
        - OUTPut[n]:SVALue:MARKer[m]?
        ```

    Info:
        - ``OFF`` sets the stop state marker output for channel 'n' to open (electrically
          disconnected).LOW sets the stop state marker output for channel 'n' value to 0 volts.[n]
          determines the channel number. If omitted, interpreted as 1.[m] determines the marker
          number. If omitted, interpreted as 1.
        - ``*RST`` sets all channel markers to LOW.
    """


class OutputItemSvalueAnalogState(SCPICmdWrite, SCPICmdRead):
    """The ``OUTPut[n]:SVALue:ANALog:STATe`` command.

    Description:
        - This command sets or returns the output condition of a waveform of the specified channel
          while the instrument is in the stopped state.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut[n]:SVALue:ANALog:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut[n]:SVALue:ANALog:STATe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``OUTPut[n]:SVALue:ANALog:STATe value``
          command.

    SCPI Syntax:
        ```
        - OUTPut[n]:SVALue:ANALog:STATe {OFF|ZERO}
        - OUTPut[n]:SVALue:ANALog:STATe?
        ```

    Info:
        - ``OFF`` sets the stop state output for channel 'n' to open (electrically
          disconnected).ZERO sets the stop state output value for channel 'n' to 0 volts.[n]
          determines the channel number. If omitted, interpreted as 1.
        - ``*RST`` sets all channels to ZERO.
    """


class OutputItemSvalueAnalog(SCPICmdRead):
    """The ``OUTPut[n]:SVALue:ANALog`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut[n]:SVALue:ANALog?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut[n]:SVALue:ANALog?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``OUTPut[n]:SVALue:ANALog:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = OutputItemSvalueAnalogState(device, f"{self._cmd_syntax}:STATe")

    @property
    def state(self) -> OutputItemSvalueAnalogState:
        """Return the ``OUTPut[n]:SVALue:ANALog:STATe`` command.

        Description:
            - This command sets or returns the output condition of a waveform of the specified
              channel while the instrument is in the stopped state.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut[n]:SVALue:ANALog:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut[n]:SVALue:ANALog:STATe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``OUTPut[n]:SVALue:ANALog:STATe value`` command.

        SCPI Syntax:
            ```
            - OUTPut[n]:SVALue:ANALog:STATe {OFF|ZERO}
            - OUTPut[n]:SVALue:ANALog:STATe?
            ```

        Info:
            - ``OFF`` sets the stop state output for channel 'n' to open (electrically
              disconnected).ZERO sets the stop state output value for channel 'n' to 0 volts.[n]
              determines the channel number. If omitted, interpreted as 1.
            - ``*RST`` sets all channels to ZERO.
        """
        return self._state


class OutputItemSvalue(SCPICmdRead):
    """The ``OUTPut[n]:SVALue`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut[n]:SVALue?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut[n]:SVALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.marker``: The ``OUTPut[n]:SVALue:MARKer[m]`` command.
        - ``.analog``: The ``OUTPut[n]:SVALue:ANALog`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._marker: Dict[int, OutputItemSvalueMarkerItem] = DefaultDictPassKeyToFactory(
            lambda x: OutputItemSvalueMarkerItem(device, f"{self._cmd_syntax}:MARKer{x}")
        )
        self._analog = OutputItemSvalueAnalog(device, f"{self._cmd_syntax}:ANALog")

    @property
    def marker(self) -> Dict[int, OutputItemSvalueMarkerItem]:
        """Return the ``OUTPut[n]:SVALue:MARKer[m]`` command.

        Description:
            - This command sets or returns the output data position of the specified marker of the
              specified channel when in the stopped state.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut[n]:SVALue:MARKer[m]?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut[n]:SVALue:MARKer[m]?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``OUTPut[n]:SVALue:MARKer[m] value``
              command.

        SCPI Syntax:
            ```
            - OUTPut[n]:SVALue:MARKer[m] {OFF|LOW}
            - OUTPut[n]:SVALue:MARKer[m]?
            ```

        Info:
            - ``OFF`` sets the stop state marker output for channel 'n' to open (electrically
              disconnected).LOW sets the stop state marker output for channel 'n' value to 0
              volts.[n] determines the channel number. If omitted, interpreted as 1.[m] determines
              the marker number. If omitted, interpreted as 1.
            - ``*RST`` sets all channel markers to LOW.
        """
        return self._marker

    @property
    def analog(self) -> OutputItemSvalueAnalog:
        """Return the ``OUTPut[n]:SVALue:ANALog`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut[n]:SVALue:ANALog?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut[n]:SVALue:ANALog?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``OUTPut[n]:SVALue:ANALog:STATe`` command.
        """
        return self._analog


class OutputItemState(SCPICmdWrite, SCPICmdRead):
    """The ``OUTPut[n]:STATe`` command.

    Description:
        - This command sets or returns the output state of the specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut[n]:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut[n]:STATe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``OUTPut[n]:STATe value`` command.

    SCPI Syntax:
        ```
        - OUTPut[n]:STATe {0|1|OFF|ON}
        - OUTPut[n]:STATe?
        ```

    Info:
        - ``0`` or OFF disables the channel's output.1 or ON enables the channel's output.[n]
          determines the channel number. If omitted, interpreted as 1.
        - ``*RST`` sets all channels to 0.
    """


class OutputItemPath(SCPICmdWrite, SCPICmdRead):
    """The ``OUTPut[n]:PATH`` command.

    Description:
        - This command sets or returns the output signal path of the specified channel. The command
          is only valid when Option AC is installed (AWG70001 only) or an MDC4500 is connected to
          the AWG70000 Series instrument.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut[n]:PATH?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut[n]:PATH?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``OUTPut[n]:PATH value`` command.

    SCPI Syntax:
        ```
        - OUTPut[n]:PATH {DIRect|AC|DCAmplified}
        - OUTPut[n]:PATH?
        ```

    Info:
        - ``DIRect`` sets the signal path to go directly from the DAC to the + and - differential
          outputs.AC sets signal path to go through the attenuators and amplifiers, then to the
          single-ended AC output. Available only for the AWG70001 with Option AC.DCAmplified sets
          the signal path to go directly from the DAC to the + and - differential outputs that must
          be connected to the inputs of an MDC4500. The DCAmplified setting provides additional
          output range and output offset adjustment from the MDC4500 outputs.
    """


class OutputItemFilterBpassRange(SCPICmdWrite, SCPICmdRead):
    """The ``OUTPut[n]:FILTer:BPASs:RANGe`` command.

    Description:
        - This command sets or returns the filter range of the band pass filter for the signal path.
          Option AC is required. This command does not change the filter hardware cutoff
          frequencies, but selects an already available filter range with the specified cutoff
          frequencies. If Option AC is not installed, sending the command causes an error message.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut[n]:FILTer:BPASs:RANGe?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut[n]:FILTer:BPASs:RANGe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``OUTPut[n]:FILTer:BPASs:RANGe value``
          command.

    SCPI Syntax:
        ```
        - OUTPut[n]:FILTer:BPASs:RANGe {R10TO14GHZ|R13TO18GHZ}
        - OUTPut[n]:FILTer:BPASs:RANGe?
        ```
    """


class OutputItemFilterBpass(SCPICmdRead):
    """The ``OUTPut[n]:FILTer:BPASs`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut[n]:FILTer:BPASs?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut[n]:FILTer:BPASs?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.range``: The ``OUTPut[n]:FILTer:BPASs:RANGe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._range = OutputItemFilterBpassRange(device, f"{self._cmd_syntax}:RANGe")

    @property
    def range(self) -> OutputItemFilterBpassRange:
        """Return the ``OUTPut[n]:FILTer:BPASs:RANGe`` command.

        Description:
            - This command sets or returns the filter range of the band pass filter for the signal
              path. Option AC is required. This command does not change the filter hardware cutoff
              frequencies, but selects an already available filter range with the specified cutoff
              frequencies. If Option AC is not installed, sending the command causes an error
              message.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut[n]:FILTer:BPASs:RANGe?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut[n]:FILTer:BPASs:RANGe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``OUTPut[n]:FILTer:BPASs:RANGe value`` command.

        SCPI Syntax:
            ```
            - OUTPut[n]:FILTer:BPASs:RANGe {R10TO14GHZ|R13TO18GHZ}
            - OUTPut[n]:FILTer:BPASs:RANGe?
            ```
        """
        return self._range


class OutputItemFilter(SCPICmdWrite, SCPICmdRead):
    """The ``OUTPut[n]:FILTer`` command.

    Description:
        - This command sets or returns the filter type for the signal path. Option AC is required.
          If Option AC is not installed, sending the command causes an error message.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut[n]:FILTer?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut[n]:FILTer?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``OUTPut[n]:FILTer value`` command.

    SCPI Syntax:
        ```
        - OUTPut[n]:FILTer {NONE|BPASs|LPASs}
        - OUTPut[n]:FILTer?
        ```

    Properties:
        - ``.bpass``: The ``OUTPut[n]:FILTer:BPASs`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bpass = OutputItemFilterBpass(device, f"{self._cmd_syntax}:BPASs")

    @property
    def bpass(self) -> OutputItemFilterBpass:
        """Return the ``OUTPut[n]:FILTer:BPASs`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut[n]:FILTer:BPASs?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut[n]:FILTer:BPASs?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.range``: The ``OUTPut[n]:FILTer:BPASs:RANGe`` command.
        """
        return self._bpass


class OutputItemAttenuatorDac(SCPICmdWrite, SCPICmdRead):
    """The ``OUTPut[n]:ATTenuator:DAC`` command.

    Description:
        - This command sets or returns the DAC output power level (in units of dBm) when the Channel
          1 Output is set to AC. Option AC is required. If Option AC is not installed, sending the
          command causes an error message. See a diagram of the AC output path in the instrument's
          User Interface under Setup>Channel1>Advanced.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut[n]:ATTenuator:DAC?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut[n]:ATTenuator:DAC?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``OUTPut[n]:ATTenuator:DAC value``
          command.

    SCPI Syntax:
        ```
        - OUTPut[n]:ATTenuator:DAC <NRf>
        - OUTPut[n]:ATTenuator:DAC?
        ```
    """


class OutputItemAttenuatorA3(SCPICmdWrite, SCPICmdRead):
    """The ``OUTPut[n]:ATTenuator:A3`` command.

    Description:
        - This command sets or returns the step value setting for the A3 attenuator (in units of dB)
          in the Band Pass Filter path when the Channel 1 Output Path is set to AC. Option AC is
          required. If Option AC is not installed, sending the command causes an error message. See
          a diagram of the AC output path in the instrument's User Interface under
          Setup>Channel1>Advanced.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut[n]:ATTenuator:A3?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut[n]:ATTenuator:A3?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``OUTPut[n]:ATTenuator:A3 value``
          command.

    SCPI Syntax:
        ```
        - OUTPut[n]:ATTenuator:A3 <NR1>
        - OUTPut[n]:ATTenuator:A3?
        ```
    """


class OutputItemAttenuatorA2(SCPICmdWrite, SCPICmdRead):
    """The ``OUTPut[n]:ATTenuator:A2`` command.

    Description:
        - This command sets or returns the step value setting for the A2 attenuator (in units of dB)
          in the Band Pass Filter path when the Channel 1 Output Path is set to AC. Option AC is
          required. If Option AC is not installed, sending the command causes an error message. See
          a diagram of the AC output path in the instrument's User Interface under
          Setup>Channel1>Advanced.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut[n]:ATTenuator:A2?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut[n]:ATTenuator:A2?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``OUTPut[n]:ATTenuator:A2 value``
          command.

    SCPI Syntax:
        ```
        - OUTPut[n]:ATTenuator:A2 <NR1>
        - OUTPut[n]:ATTenuator:A2?
        ```
    """


class OutputItemAttenuatorA1(SCPICmdWrite, SCPICmdRead):
    """The ``OUTPut[n]:ATTenuator:A1`` command.

    Description:
        - This command sets or returns the step value setting for the A1 attenuator in (units of dB)
          in the Band Pass Filter path when the Channel 1 Output Path is set to AC and the Band Pass
          Range is set to 13 - 18 GHz. Option AC is required. If Option AC is not installed, sending
          the command causes an error message. See a diagram of the AC output path in the
          instrument's User Interface under Setup>Channel1>Advanced.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut[n]:ATTenuator:A1?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut[n]:ATTenuator:A1?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``OUTPut[n]:ATTenuator:A1 value``
          command.

    SCPI Syntax:
        ```
        - OUTPut[n]:ATTenuator:A1 <NR1>
        - OUTPut[n]:ATTenuator:A1?
        ```
    """


class OutputItemAttenuator(SCPICmdRead):
    """The ``OUTPut[n]:ATTenuator`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut[n]:ATTenuator?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut[n]:ATTenuator?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.a1``: The ``OUTPut[n]:ATTenuator:A1`` command.
        - ``.a2``: The ``OUTPut[n]:ATTenuator:A2`` command.
        - ``.a3``: The ``OUTPut[n]:ATTenuator:A3`` command.
        - ``.dac``: The ``OUTPut[n]:ATTenuator:DAC`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._a1 = OutputItemAttenuatorA1(device, f"{self._cmd_syntax}:A1")
        self._a2 = OutputItemAttenuatorA2(device, f"{self._cmd_syntax}:A2")
        self._a3 = OutputItemAttenuatorA3(device, f"{self._cmd_syntax}:A3")
        self._dac = OutputItemAttenuatorDac(device, f"{self._cmd_syntax}:DAC")

    @property
    def a1(self) -> OutputItemAttenuatorA1:
        """Return the ``OUTPut[n]:ATTenuator:A1`` command.

        Description:
            - This command sets or returns the step value setting for the A1 attenuator in (units of
              dB) in the Band Pass Filter path when the Channel 1 Output Path is set to AC and the
              Band Pass Range is set to 13 - 18 GHz. Option AC is required. If Option AC is not
              installed, sending the command causes an error message. See a diagram of the AC output
              path in the instrument's User Interface under Setup>Channel1>Advanced.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut[n]:ATTenuator:A1?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut[n]:ATTenuator:A1?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``OUTPut[n]:ATTenuator:A1 value``
              command.

        SCPI Syntax:
            ```
            - OUTPut[n]:ATTenuator:A1 <NR1>
            - OUTPut[n]:ATTenuator:A1?
            ```
        """
        return self._a1

    @property
    def a2(self) -> OutputItemAttenuatorA2:
        """Return the ``OUTPut[n]:ATTenuator:A2`` command.

        Description:
            - This command sets or returns the step value setting for the A2 attenuator (in units of
              dB) in the Band Pass Filter path when the Channel 1 Output Path is set to AC. Option
              AC is required. If Option AC is not installed, sending the command causes an error
              message. See a diagram of the AC output path in the instrument's User Interface under
              Setup>Channel1>Advanced.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut[n]:ATTenuator:A2?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut[n]:ATTenuator:A2?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``OUTPut[n]:ATTenuator:A2 value``
              command.

        SCPI Syntax:
            ```
            - OUTPut[n]:ATTenuator:A2 <NR1>
            - OUTPut[n]:ATTenuator:A2?
            ```
        """
        return self._a2

    @property
    def a3(self) -> OutputItemAttenuatorA3:
        """Return the ``OUTPut[n]:ATTenuator:A3`` command.

        Description:
            - This command sets or returns the step value setting for the A3 attenuator (in units of
              dB) in the Band Pass Filter path when the Channel 1 Output Path is set to AC. Option
              AC is required. If Option AC is not installed, sending the command causes an error
              message. See a diagram of the AC output path in the instrument's User Interface under
              Setup>Channel1>Advanced.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut[n]:ATTenuator:A3?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut[n]:ATTenuator:A3?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``OUTPut[n]:ATTenuator:A3 value``
              command.

        SCPI Syntax:
            ```
            - OUTPut[n]:ATTenuator:A3 <NR1>
            - OUTPut[n]:ATTenuator:A3?
            ```
        """
        return self._a3

    @property
    def dac(self) -> OutputItemAttenuatorDac:
        """Return the ``OUTPut[n]:ATTenuator:DAC`` command.

        Description:
            - This command sets or returns the DAC output power level (in units of dBm) when the
              Channel 1 Output is set to AC. Option AC is required. If Option AC is not installed,
              sending the command causes an error message. See a diagram of the AC output path in
              the instrument's User Interface under Setup>Channel1>Advanced.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut[n]:ATTenuator:DAC?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut[n]:ATTenuator:DAC?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``OUTPut[n]:ATTenuator:DAC value``
              command.

        SCPI Syntax:
            ```
            - OUTPut[n]:ATTenuator:DAC <NRf>
            - OUTPut[n]:ATTenuator:DAC?
            ```
        """
        return self._dac


class OutputItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``OUTPut[n]`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut[n]?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut[n]?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.attenuator``: The ``OUTPut[n]:ATTenuator`` command tree.
        - ``.filter``: The ``OUTPut[n]:FILTer`` command.
        - ``.path``: The ``OUTPut[n]:PATH`` command.
        - ``.svalue``: The ``OUTPut[n]:SVALue`` command tree.
        - ``.wvalue``: The ``OUTPut[n]:WVALue`` command tree.
        - ``.state``: The ``OUTPut[n]:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "OUTPut[n]") -> None:
        super().__init__(device, cmd_syntax)
        self._attenuator = OutputItemAttenuator(device, f"{self._cmd_syntax}:ATTenuator")
        self._filter = OutputItemFilter(device, f"{self._cmd_syntax}:FILTer")
        self._path = OutputItemPath(device, f"{self._cmd_syntax}:PATH")
        self._svalue = OutputItemSvalue(device, f"{self._cmd_syntax}:SVALue")
        self._wvalue = OutputItemWvalue(device, f"{self._cmd_syntax}:WVALue")
        self._state = OutputItemState(device, f"{self._cmd_syntax}:STATe")

    @property
    def attenuator(self) -> OutputItemAttenuator:
        """Return the ``OUTPut[n]:ATTenuator`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut[n]:ATTenuator?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut[n]:ATTenuator?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.a1``: The ``OUTPut[n]:ATTenuator:A1`` command.
            - ``.a2``: The ``OUTPut[n]:ATTenuator:A2`` command.
            - ``.a3``: The ``OUTPut[n]:ATTenuator:A3`` command.
            - ``.dac``: The ``OUTPut[n]:ATTenuator:DAC`` command.
        """
        return self._attenuator

    @property
    def filter(self) -> OutputItemFilter:
        """Return the ``OUTPut[n]:FILTer`` command.

        Description:
            - This command sets or returns the filter type for the signal path. Option AC is
              required. If Option AC is not installed, sending the command causes an error message.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut[n]:FILTer?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut[n]:FILTer?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``OUTPut[n]:FILTer value`` command.

        SCPI Syntax:
            ```
            - OUTPut[n]:FILTer {NONE|BPASs|LPASs}
            - OUTPut[n]:FILTer?
            ```

        Sub-properties:
            - ``.bpass``: The ``OUTPut[n]:FILTer:BPASs`` command tree.
        """
        return self._filter

    @property
    def path(self) -> OutputItemPath:
        """Return the ``OUTPut[n]:PATH`` command.

        Description:
            - This command sets or returns the output signal path of the specified channel. The
              command is only valid when Option AC is installed (AWG70001 only) or an MDC4500 is
              connected to the AWG70000 Series instrument.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut[n]:PATH?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut[n]:PATH?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``OUTPut[n]:PATH value`` command.

        SCPI Syntax:
            ```
            - OUTPut[n]:PATH {DIRect|AC|DCAmplified}
            - OUTPut[n]:PATH?
            ```

        Info:
            - ``DIRect`` sets the signal path to go directly from the DAC to the + and -
              differential outputs.AC sets signal path to go through the attenuators and amplifiers,
              then to the single-ended AC output. Available only for the AWG70001 with Option
              AC.DCAmplified sets the signal path to go directly from the DAC to the + and -
              differential outputs that must be connected to the inputs of an MDC4500. The
              DCAmplified setting provides additional output range and output offset adjustment from
              the MDC4500 outputs.
        """
        return self._path

    @property
    def svalue(self) -> OutputItemSvalue:
        """Return the ``OUTPut[n]:SVALue`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut[n]:SVALue?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut[n]:SVALue?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.marker``: The ``OUTPut[n]:SVALue:MARKer[m]`` command.
            - ``.analog``: The ``OUTPut[n]:SVALue:ANALog`` command tree.
        """
        return self._svalue

    @property
    def wvalue(self) -> OutputItemWvalue:
        """Return the ``OUTPut[n]:WVALue`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut[n]:WVALue?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut[n]:WVALue?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.marker``: The ``OUTPut[n]:WVALue:MARKer[m]`` command.
            - ``.analog``: The ``OUTPut[n]:WVALue:ANALog`` command tree.
        """
        return self._wvalue

    @property
    def state(self) -> OutputItemState:
        """Return the ``OUTPut[n]:STATe`` command.

        Description:
            - This command sets or returns the output state of the specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut[n]:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut[n]:STATe?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``OUTPut[n]:STATe value`` command.

        SCPI Syntax:
            ```
            - OUTPut[n]:STATe {0|1|OFF|ON}
            - OUTPut[n]:STATe?
            ```

        Info:
            - ``0`` or OFF disables the channel's output.1 or ON enables the channel's output.[n]
              determines the channel number. If omitted, interpreted as 1.
            - ``*RST`` sets all channels to 0.
        """
        return self._state
