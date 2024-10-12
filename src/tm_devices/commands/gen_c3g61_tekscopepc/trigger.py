"""The trigger commands module.

These commands are used in the following models:
TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - TRIGger:A:EDGE:COUPling {DC|HFRej|LFRej|NOISErej}
    - TRIGger:A:EDGE:COUPling?
    - TRIGger:A:EDGE:SLOpe {RISe|FALL|EITher}
    - TRIGger:A:EDGE:SLOpe?
    - TRIGger:A:EDGE:SOUrce {CH<x>|CH<x>_D<y>|LINE|AUXiliary}
    - TRIGger:A:EDGE:SOUrce?
    - TRIGger:A:LEVel:CH<x> <NR3>
    - TRIGger:A:LEVel:CH<x>?
    - TRIGger:A:TYPe {EDGE|WIDth|TIMEOut|RUNt|WINdow|LOGIc|SETHold|TRANsition|BUS}
    - TRIGger:A:TYPe?
    - TRIGger:B:EDGE:COUPling {DC|HFRej|LFRej|NOISErej}
    - TRIGger:B:EDGE:COUPling?
    - TRIGger:B:EDGE:SLOpe {RISe|FALL|EITher}
    - TRIGger:B:EDGE:SLOpe?
    - TRIGger:B:EDGE:SOUrce {CH<x>|CH<x>_D<y>|LINE|AUXiliary}
    - TRIGger:B:EDGE:SOUrce?
    - TRIGger:B:LEVel:CH<x> <NR3>
    - TRIGger:B:LEVel:CH<x>?
    - TRIGger:B:TYPe {EDGE|WIDth|TIMEOut|RUNt|WINdow|LOGIc|SETHold|TRANsition|BUS}
    - TRIGger:B:TYPe?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import DefaultDictPassKeyToFactory, SCPICmdRead, SCPICmdWrite, ValidatedChannel

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class TriggerBType(SCPICmdWrite, SCPICmdRead):
    r"""The ``TRIGger:B:TYPe`` command.

    Description:
        - This command sets or queries the type of A or B trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B:TYPe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:B:TYPe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:B:TYPe {EDGE|WIDth|TIMEOut|RUNt|WINdow|LOGIc|SETHold|TRANsition|BUS}
        - TRIGger:B:TYPe?
        ```

    Info:
        - ``EDGE`` is a normal trigger. A trigger event occurs when a signal passes through a
          specified voltage level in a specified direction and is controlled by the
          ``TRIGger:A:EDGE`` commands.
        - ``WIDth`` specifies that the trigger occurs when a pulse with a specified with is found.
        - ``TIMEOut`` specifies that a trigger occurs when a pulse with the specified timeout is
          found.
        - ``RUNt`` specifies that a trigger occurs when a pulse with the specified parameters is
          found.
        - ``WINdow`` specifies that a trigger occurs when a signal with the specified window
          parameters is found.
        - ``LOGIc`` specifies that a trigger occurs when specified conditions are met and is
          controlled by the TRIGger:{A\|B}``:LOGIc`` commands.
        - ``SETHold`` specifies that a trigger occurs when a signal is found that meets the setup
          and hold parameters.
        - ``BUS`` specifies that a trigger occurs when a signal is found that meets the specified
          bus setup parameters.
    """


class TriggerBLevelChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:B:LEVel:CH<x>`` command.

    Description:
        - This command sets or queries the CH<x> trigger level for an Edge, Pulse Width, Runt or
          Rise/Fall (Transition and Slew Rate) trigger when triggering on an analog channel
          waveform. Each channel can have an independent trigger level. The <x> is the channel
          number.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B:LEVel:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B:LEVel:CH<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:B:LEVel:CH<x> value`` command.

    SCPI Syntax:
        ```
        - TRIGger:B:LEVel:CH<x> <NR3>
        - TRIGger:B:LEVel:CH<x>?
        ```

    Info:
        - ``<NR3>`` specifies the trigger level in user units (usually volts).
    """


class TriggerBLevel(SCPICmdRead):
    """The ``TRIGger:B:LEVel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B:LEVel?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B:LEVel?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``TRIGger:B:LEVel:CH<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, TriggerBLevelChannel] = DefaultDictPassKeyToFactory(
            lambda x: TriggerBLevelChannel(device, f"{self._cmd_syntax}:CH{x}")
        )

    @property
    def ch(self) -> Dict[int, TriggerBLevelChannel]:
        """Return the ``TRIGger:B:LEVel:CH<x>`` command.

        Description:
            - This command sets or queries the CH<x> trigger level for an Edge, Pulse Width, Runt or
              Rise/Fall (Transition and Slew Rate) trigger when triggering on an analog channel
              waveform. Each channel can have an independent trigger level. The <x> is the channel
              number.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B:LEVel:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B:LEVel:CH<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:B:LEVel:CH<x> value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:B:LEVel:CH<x> <NR3>
            - TRIGger:B:LEVel:CH<x>?
            ```

        Info:
            - ``<NR3>`` specifies the trigger level in user units (usually volts).
        """
        return self._ch


class TriggerBEdgeSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:B:EDGE:SOUrce`` command.

    Description:
        - This command sets or queries the source for the edge trigger. For instruments that have an
          Auxiliary Input (such as the MSO58LP), AUXiliary can be selected as trigger source.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B:EDGE:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B:EDGE:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:B:EDGE:SOUrce value`` command.

    SCPI Syntax:
        ```
        - TRIGger:B:EDGE:SOUrce {CH<x>|CH<x>_D<y>|LINE|AUXiliary}
        - TRIGger:B:EDGE:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the edge trigger source.
        - ``CH<x>_D<y>`` specifies a digital channel as the edge trigger source.
        - ``LINE`` specifies AC line voltage, and is a valid source when B trigger is inactive.
        - ``AUXiliary`` specifies the Auxiliary Input.
    """


class TriggerBEdgeSlope(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:B:EDGE:SLOpe`` command.

    Description:
        - This command sets or queries the slope for the edge trigger. This command is equivalent to
          selecting Edge from the Trigger Type drop-down in the Trigger setup context menu, and then
          choosing the desired Slope. This command is also equivalent to pressing the front-panel
          Slope button.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B:EDGE:SLOpe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B:EDGE:SLOpe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:B:EDGE:SLOpe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:B:EDGE:SLOpe {RISe|FALL|EITher}
        - TRIGger:B:EDGE:SLOpe?
        ```

    Info:
        - ``RISe`` specifies to trigger on the rising or positive edge of a signal.
        - ``FALL`` specifies to trigger on the falling or negative edge of a signal.
    """


class TriggerBEdgeCoupling(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:B:EDGE:COUPling`` command.

    Description:
        - This command sets or queries the type of coupling for the edge trigger. This command is
          equivalent to selecting Edge from the Trigger Type drop-down in the Trigger setup context
          menu, and choosing from the Coupling drop-down list.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B:EDGE:COUPling?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B:EDGE:COUPling?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:B:EDGE:COUPling value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:B:EDGE:COUPling {DC|HFRej|LFRej|NOISErej}
        - TRIGger:B:EDGE:COUPling?
        ```

    Info:
        - ``DC`` selects DC trigger coupling, which passes all input signals to the trigger
          circuitry.
        - ``HFRej`` coupling attenuates signals above 50 kHz before passing the signals to the
          trigger circuitry.
        - ``LFRej`` coupling attenuates signals below 80 kHz before passing the signals to the
          trigger circuitry.
        - ``NOISErej`` coupling provides stable triggering by increasing the trigger hysteresis.
          Increased hysteresis reduces the trigger sensitivity to noise but can require greater
          trigger signal amplitude.
    """


class TriggerBEdge(SCPICmdRead):
    """The ``TRIGger:B:EDGE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B:EDGE?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B:EDGE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.coupling``: The ``TRIGger:B:EDGE:COUPling`` command.
        - ``.slope``: The ``TRIGger:B:EDGE:SLOpe`` command.
        - ``.source``: The ``TRIGger:B:EDGE:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._coupling = TriggerBEdgeCoupling(device, f"{self._cmd_syntax}:COUPling")
        self._slope = TriggerBEdgeSlope(device, f"{self._cmd_syntax}:SLOpe")
        self._source = TriggerBEdgeSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def coupling(self) -> TriggerBEdgeCoupling:
        """Return the ``TRIGger:B:EDGE:COUPling`` command.

        Description:
            - This command sets or queries the type of coupling for the edge trigger. This command
              is equivalent to selecting Edge from the Trigger Type drop-down in the Trigger setup
              context menu, and choosing from the Coupling drop-down list.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B:EDGE:COUPling?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B:EDGE:COUPling?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:B:EDGE:COUPling value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:B:EDGE:COUPling {DC|HFRej|LFRej|NOISErej}
            - TRIGger:B:EDGE:COUPling?
            ```

        Info:
            - ``DC`` selects DC trigger coupling, which passes all input signals to the trigger
              circuitry.
            - ``HFRej`` coupling attenuates signals above 50 kHz before passing the signals to the
              trigger circuitry.
            - ``LFRej`` coupling attenuates signals below 80 kHz before passing the signals to the
              trigger circuitry.
            - ``NOISErej`` coupling provides stable triggering by increasing the trigger hysteresis.
              Increased hysteresis reduces the trigger sensitivity to noise but can require greater
              trigger signal amplitude.
        """
        return self._coupling

    @property
    def slope(self) -> TriggerBEdgeSlope:
        """Return the ``TRIGger:B:EDGE:SLOpe`` command.

        Description:
            - This command sets or queries the slope for the edge trigger. This command is
              equivalent to selecting Edge from the Trigger Type drop-down in the Trigger setup
              context menu, and then choosing the desired Slope. This command is also equivalent to
              pressing the front-panel Slope button.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B:EDGE:SLOpe?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B:EDGE:SLOpe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:B:EDGE:SLOpe value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:B:EDGE:SLOpe {RISe|FALL|EITher}
            - TRIGger:B:EDGE:SLOpe?
            ```

        Info:
            - ``RISe`` specifies to trigger on the rising or positive edge of a signal.
            - ``FALL`` specifies to trigger on the falling or negative edge of a signal.
        """
        return self._slope

    @property
    def source(self) -> TriggerBEdgeSource:
        """Return the ``TRIGger:B:EDGE:SOUrce`` command.

        Description:
            - This command sets or queries the source for the edge trigger. For instruments that
              have an Auxiliary Input (such as the MSO58LP), AUXiliary can be selected as trigger
              source.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B:EDGE:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B:EDGE:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:B:EDGE:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:B:EDGE:SOUrce {CH<x>|CH<x>_D<y>|LINE|AUXiliary}
            - TRIGger:B:EDGE:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the edge trigger source.
            - ``CH<x>_D<y>`` specifies a digital channel as the edge trigger source.
            - ``LINE`` specifies AC line voltage, and is a valid source when B trigger is inactive.
            - ``AUXiliary`` specifies the Auxiliary Input.
        """
        return self._source


class TriggerB(SCPICmdRead):
    """The ``TRIGger:B`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.edge``: The ``TRIGger:B:EDGE`` command tree.
        - ``.level``: The ``TRIGger:B:LEVel`` command tree.
        - ``.type``: The ``TRIGger:B:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._edge = TriggerBEdge(device, f"{self._cmd_syntax}:EDGE")
        self._level = TriggerBLevel(device, f"{self._cmd_syntax}:LEVel")
        self._type = TriggerBType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def edge(self) -> TriggerBEdge:
        """Return the ``TRIGger:B:EDGE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B:EDGE?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B:EDGE?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.coupling``: The ``TRIGger:B:EDGE:COUPling`` command.
            - ``.slope``: The ``TRIGger:B:EDGE:SLOpe`` command.
            - ``.source``: The ``TRIGger:B:EDGE:SOUrce`` command.
        """
        return self._edge

    @property
    def level(self) -> TriggerBLevel:
        """Return the ``TRIGger:B:LEVel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B:LEVel?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B:LEVel?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``TRIGger:B:LEVel:CH<x>`` command.
        """
        return self._level

    @property
    def type(self) -> TriggerBType:
        r"""Return the ``TRIGger:B:TYPe`` command.

        Description:
            - This command sets or queries the type of A or B trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B:TYPe?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:B:TYPe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:B:TYPe {EDGE|WIDth|TIMEOut|RUNt|WINdow|LOGIc|SETHold|TRANsition|BUS}
            - TRIGger:B:TYPe?
            ```

        Info:
            - ``EDGE`` is a normal trigger. A trigger event occurs when a signal passes through a
              specified voltage level in a specified direction and is controlled by the
              ``TRIGger:A:EDGE`` commands.
            - ``WIDth`` specifies that the trigger occurs when a pulse with a specified with is
              found.
            - ``TIMEOut`` specifies that a trigger occurs when a pulse with the specified timeout is
              found.
            - ``RUNt`` specifies that a trigger occurs when a pulse with the specified parameters is
              found.
            - ``WINdow`` specifies that a trigger occurs when a signal with the specified window
              parameters is found.
            - ``LOGIc`` specifies that a trigger occurs when specified conditions are met and is
              controlled by the TRIGger:{A\|B}``:LOGIc`` commands.
            - ``SETHold`` specifies that a trigger occurs when a signal is found that meets the
              setup and hold parameters.
            - ``BUS`` specifies that a trigger occurs when a signal is found that meets the
              specified bus setup parameters.
        """
        return self._type


class TriggerAType(SCPICmdWrite, SCPICmdRead):
    r"""The ``TRIGger:A:TYPe`` command.

    Description:
        - This command sets or queries the type of A or B trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:TYPe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:TYPe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:TYPe {EDGE|WIDth|TIMEOut|RUNt|WINdow|LOGIc|SETHold|TRANsition|BUS}
        - TRIGger:A:TYPe?
        ```

    Info:
        - ``EDGE`` is a normal trigger. A trigger event occurs when a signal passes through a
          specified voltage level in a specified direction and is controlled by the
          ``TRIGger:A:EDGE`` commands.
        - ``WIDth`` specifies that the trigger occurs when a pulse with a specified with is found.
        - ``TIMEOut`` specifies that a trigger occurs when a pulse with the specified timeout is
          found.
        - ``RUNt`` specifies that a trigger occurs when a pulse with the specified parameters is
          found.
        - ``WINdow`` specifies that a trigger occurs when a signal with the specified window
          parameters is found.
        - ``LOGIc`` specifies that a trigger occurs when specified conditions are met and is
          controlled by the TRIGger:{A\|B}``:LOGIc`` commands.
        - ``SETHold`` specifies that a trigger occurs when a signal is found that meets the setup
          and hold parameters.
        - ``BUS`` specifies that a trigger occurs when a signal is found that meets the specified
          bus setup parameters.
    """


class TriggerALevelChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LEVel:CH<x>`` command.

    Description:
        - This command sets or queries the CH<x> trigger level for an Edge, Pulse Width, Runt or
          Rise/Fall (Transition and Slew Rate) trigger when triggering on an analog channel
          waveform. Each channel can have an independent trigger level. The <x> is the channel
          number.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LEVel:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LEVel:CH<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LEVel:CH<x> value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:LEVel:CH<x> <NR3>
        - TRIGger:A:LEVel:CH<x>?
        ```

    Info:
        - ``<NR3>`` specifies the trigger level in user units (usually volts).
    """


class TriggerALevel(SCPICmdRead):
    """The ``TRIGger:A:LEVel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LEVel?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LEVel?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``TRIGger:A:LEVel:CH<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, TriggerALevelChannel] = DefaultDictPassKeyToFactory(
            lambda x: TriggerALevelChannel(device, f"{self._cmd_syntax}:CH{x}")
        )

    @property
    def ch(self) -> Dict[int, TriggerALevelChannel]:
        """Return the ``TRIGger:A:LEVel:CH<x>`` command.

        Description:
            - This command sets or queries the CH<x> trigger level for an Edge, Pulse Width, Runt or
              Rise/Fall (Transition and Slew Rate) trigger when triggering on an analog channel
              waveform. Each channel can have an independent trigger level. The <x> is the channel
              number.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LEVel:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LEVel:CH<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:LEVel:CH<x> value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:LEVel:CH<x> <NR3>
            - TRIGger:A:LEVel:CH<x>?
            ```

        Info:
            - ``<NR3>`` specifies the trigger level in user units (usually volts).
        """
        return self._ch


class TriggerAEdgeSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:EDGE:SOUrce`` command.

    Description:
        - This command sets or queries the source for the edge trigger. For instruments that have an
          Auxiliary Input (such as the MSO58LP), AUXiliary can be selected as trigger source.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:EDGE:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:EDGE:SOUrce value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:EDGE:SOUrce {CH<x>|CH<x>_D<y>|LINE|AUXiliary}
        - TRIGger:A:EDGE:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the edge trigger source.
        - ``CH<x>_D<y>`` specifies a digital channel as the edge trigger source.
        - ``LINE`` specifies AC line voltage, and is a valid source when B trigger is inactive.
        - ``AUXiliary`` specifies the Auxiliary Input.
    """


class TriggerAEdgeSlope(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:EDGE:SLOpe`` command.

    Description:
        - This command sets or queries the slope for the edge trigger. This command is equivalent to
          selecting Edge from the Trigger Type drop-down in the Trigger setup context menu, and then
          choosing the desired Slope. This command is also equivalent to pressing the front-panel
          Slope button.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:EDGE:SLOpe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE:SLOpe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:EDGE:SLOpe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:EDGE:SLOpe {RISe|FALL|EITher}
        - TRIGger:A:EDGE:SLOpe?
        ```

    Info:
        - ``RISe`` specifies to trigger on the rising or positive edge of a signal.
        - ``FALL`` specifies to trigger on the falling or negative edge of a signal.
    """


class TriggerAEdgeCoupling(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:EDGE:COUPling`` command.

    Description:
        - This command sets or queries the type of coupling for the edge trigger. This command is
          equivalent to selecting Edge from the Trigger Type drop-down in the Trigger setup context
          menu, and choosing from the Coupling drop-down list.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:EDGE:COUPling?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE:COUPling?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:EDGE:COUPling value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:EDGE:COUPling {DC|HFRej|LFRej|NOISErej}
        - TRIGger:A:EDGE:COUPling?
        ```

    Info:
        - ``DC`` selects DC trigger coupling, which passes all input signals to the trigger
          circuitry.
        - ``HFRej`` coupling attenuates signals above 50 kHz before passing the signals to the
          trigger circuitry.
        - ``LFRej`` coupling attenuates signals below 80 kHz before passing the signals to the
          trigger circuitry.
        - ``NOISErej`` coupling provides stable triggering by increasing the trigger hysteresis.
          Increased hysteresis reduces the trigger sensitivity to noise but can require greater
          trigger signal amplitude.
    """


class TriggerAEdge(SCPICmdRead):
    """The ``TRIGger:A:EDGE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:EDGE?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.coupling``: The ``TRIGger:A:EDGE:COUPling`` command.
        - ``.slope``: The ``TRIGger:A:EDGE:SLOpe`` command.
        - ``.source``: The ``TRIGger:A:EDGE:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._coupling = TriggerAEdgeCoupling(device, f"{self._cmd_syntax}:COUPling")
        self._slope = TriggerAEdgeSlope(device, f"{self._cmd_syntax}:SLOpe")
        self._source = TriggerAEdgeSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def coupling(self) -> TriggerAEdgeCoupling:
        """Return the ``TRIGger:A:EDGE:COUPling`` command.

        Description:
            - This command sets or queries the type of coupling for the edge trigger. This command
              is equivalent to selecting Edge from the Trigger Type drop-down in the Trigger setup
              context menu, and choosing from the Coupling drop-down list.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:EDGE:COUPling?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE:COUPling?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:EDGE:COUPling value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:EDGE:COUPling {DC|HFRej|LFRej|NOISErej}
            - TRIGger:A:EDGE:COUPling?
            ```

        Info:
            - ``DC`` selects DC trigger coupling, which passes all input signals to the trigger
              circuitry.
            - ``HFRej`` coupling attenuates signals above 50 kHz before passing the signals to the
              trigger circuitry.
            - ``LFRej`` coupling attenuates signals below 80 kHz before passing the signals to the
              trigger circuitry.
            - ``NOISErej`` coupling provides stable triggering by increasing the trigger hysteresis.
              Increased hysteresis reduces the trigger sensitivity to noise but can require greater
              trigger signal amplitude.
        """
        return self._coupling

    @property
    def slope(self) -> TriggerAEdgeSlope:
        """Return the ``TRIGger:A:EDGE:SLOpe`` command.

        Description:
            - This command sets or queries the slope for the edge trigger. This command is
              equivalent to selecting Edge from the Trigger Type drop-down in the Trigger setup
              context menu, and then choosing the desired Slope. This command is also equivalent to
              pressing the front-panel Slope button.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:EDGE:SLOpe?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE:SLOpe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:EDGE:SLOpe value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:EDGE:SLOpe {RISe|FALL|EITher}
            - TRIGger:A:EDGE:SLOpe?
            ```

        Info:
            - ``RISe`` specifies to trigger on the rising or positive edge of a signal.
            - ``FALL`` specifies to trigger on the falling or negative edge of a signal.
        """
        return self._slope

    @property
    def source(self) -> TriggerAEdgeSource:
        """Return the ``TRIGger:A:EDGE:SOUrce`` command.

        Description:
            - This command sets or queries the source for the edge trigger. For instruments that
              have an Auxiliary Input (such as the MSO58LP), AUXiliary can be selected as trigger
              source.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:EDGE:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:EDGE:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:EDGE:SOUrce {CH<x>|CH<x>_D<y>|LINE|AUXiliary}
            - TRIGger:A:EDGE:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the edge trigger source.
            - ``CH<x>_D<y>`` specifies a digital channel as the edge trigger source.
            - ``LINE`` specifies AC line voltage, and is a valid source when B trigger is inactive.
            - ``AUXiliary`` specifies the Auxiliary Input.
        """
        return self._source


class TriggerA(SCPICmdRead):
    """The ``TRIGger:A`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.edge``: The ``TRIGger:A:EDGE`` command tree.
        - ``.level``: The ``TRIGger:A:LEVel`` command tree.
        - ``.type``: The ``TRIGger:A:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._edge = TriggerAEdge(device, f"{self._cmd_syntax}:EDGE")
        self._level = TriggerALevel(device, f"{self._cmd_syntax}:LEVel")
        self._type = TriggerAType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def edge(self) -> TriggerAEdge:
        """Return the ``TRIGger:A:EDGE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:EDGE?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.coupling``: The ``TRIGger:A:EDGE:COUPling`` command.
            - ``.slope``: The ``TRIGger:A:EDGE:SLOpe`` command.
            - ``.source``: The ``TRIGger:A:EDGE:SOUrce`` command.
        """
        return self._edge

    @property
    def level(self) -> TriggerALevel:
        """Return the ``TRIGger:A:LEVel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LEVel?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LEVel?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``TRIGger:A:LEVel:CH<x>`` command.
        """
        return self._level

    @property
    def type(self) -> TriggerAType:
        r"""Return the ``TRIGger:A:TYPe`` command.

        Description:
            - This command sets or queries the type of A or B trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:TYPe?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:TYPe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:TYPe {EDGE|WIDth|TIMEOut|RUNt|WINdow|LOGIc|SETHold|TRANsition|BUS}
            - TRIGger:A:TYPe?
            ```

        Info:
            - ``EDGE`` is a normal trigger. A trigger event occurs when a signal passes through a
              specified voltage level in a specified direction and is controlled by the
              ``TRIGger:A:EDGE`` commands.
            - ``WIDth`` specifies that the trigger occurs when a pulse with a specified with is
              found.
            - ``TIMEOut`` specifies that a trigger occurs when a pulse with the specified timeout is
              found.
            - ``RUNt`` specifies that a trigger occurs when a pulse with the specified parameters is
              found.
            - ``WINdow`` specifies that a trigger occurs when a signal with the specified window
              parameters is found.
            - ``LOGIc`` specifies that a trigger occurs when specified conditions are met and is
              controlled by the TRIGger:{A\|B}``:LOGIc`` commands.
            - ``SETHold`` specifies that a trigger occurs when a signal is found that meets the
              setup and hold parameters.
            - ``BUS`` specifies that a trigger occurs when a signal is found that meets the
              specified bus setup parameters.
        """
        return self._type


class Trigger(SCPICmdRead):
    """The ``TRIGger`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.a``: The ``TRIGger:A`` command tree.
        - ``.b``: The ``TRIGger:B`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "TRIGger") -> None:
        super().__init__(device, cmd_syntax)
        self._a = TriggerA(device, f"{self._cmd_syntax}:A")
        self._b = TriggerB(device, f"{self._cmd_syntax}:B")

    @property
    def a(self) -> TriggerA:
        """Return the ``TRIGger:A`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.edge``: The ``TRIGger:A:EDGE`` command tree.
            - ``.level``: The ``TRIGger:A:LEVel`` command tree.
            - ``.type``: The ``TRIGger:A:TYPe`` command.
        """
        return self._a

    @property
    def b(self) -> TriggerB:
        """Return the ``TRIGger:B`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.edge``: The ``TRIGger:B:EDGE`` command tree.
            - ``.level``: The ``TRIGger:B:LEVel`` command tree.
            - ``.type``: The ``TRIGger:B:TYPe`` command.
        """
        return self._b
