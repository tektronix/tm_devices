"""The output commands module.

These commands are used in the following models:
AWG5200

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - OUTPut[n]:PATH {DCHB|ACDirect|ACAMplified|DCHV}
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
        - This command sets or returns the output signal path of the specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut[n]:PATH?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut[n]:PATH?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``OUTPut[n]:PATH value`` command.

    SCPI Syntax:
        ```
        - OUTPut[n]:PATH {DCHB|ACDirect|ACAMplified|DCHV}
        - OUTPut[n]:PATH?
        ```

    Info:
        - ``DCHB`` sets the signal path to DC High Bandwidth, going directly from the DAC to the
          channel's (+) and (-) differential outputs. DCHV sets the signal path toDC High Voltage,
          going from the DAC through an additional amplifier, then to the channel's (+) and (-)
          differential outputs. ACDirect sets signal path to go to the channel's (+) connector
          (single-ended AC output). ACAMplified sets signal path to go through the attenuators and
          amplifiers, then to the channel's (+) connector (single-ended AC output). Option AC is
          required.
    """


class OutputItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``OUTPut[n]`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut[n]?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut[n]?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.path``: The ``OUTPut[n]:PATH`` command.
        - ``.svalue``: The ``OUTPut[n]:SVALue`` command tree.
        - ``.wvalue``: The ``OUTPut[n]:WVALue`` command tree.
        - ``.state``: The ``OUTPut[n]:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "OUTPut[n]") -> None:
        super().__init__(device, cmd_syntax)
        self._path = OutputItemPath(device, f"{self._cmd_syntax}:PATH")
        self._svalue = OutputItemSvalue(device, f"{self._cmd_syntax}:SVALue")
        self._wvalue = OutputItemWvalue(device, f"{self._cmd_syntax}:WVALue")
        self._state = OutputItemState(device, f"{self._cmd_syntax}:STATe")

    @property
    def path(self) -> OutputItemPath:
        """Return the ``OUTPut[n]:PATH`` command.

        Description:
            - This command sets or returns the output signal path of the specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut[n]:PATH?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut[n]:PATH?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``OUTPut[n]:PATH value`` command.

        SCPI Syntax:
            ```
            - OUTPut[n]:PATH {DCHB|ACDirect|ACAMplified|DCHV}
            - OUTPut[n]:PATH?
            ```

        Info:
            - ``DCHB`` sets the signal path to DC High Bandwidth, going directly from the DAC to the
              channel's (+) and (-) differential outputs. DCHV sets the signal path toDC High
              Voltage, going from the DAC through an additional amplifier, then to the channel's (+)
              and (-) differential outputs. ACDirect sets signal path to go to the channel's (+)
              connector (single-ended AC output). ACAMplified sets signal path to go through the
              attenuators and amplifiers, then to the channel's (+) connector (single-ended AC
              output). Option AC is required.
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
