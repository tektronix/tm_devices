"""The event commands module.

These commands are used in the following models:
AWG5K, AWG5KC, AWG7K, AWG7KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - EVENt:IMMediate
    - EVENt:IMPedance <ohms>
    - EVENt:IMPedance?
    - EVENt:JTIMing <jump_type>
    - EVENt:JTIMing?
    - EVENt:LEVel <level>
    - EVENt:LEVel?
    - EVENt:POLarity {POSitive|NEGative}
    - EVENt:POLarity?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class EventPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``EVENt:POLarity`` command.

    Description:
        - This command and query sets or returns the polarity of event signal. The Event Jump is the
          function to change the sequencing of the waveform by an event signal.

    Usage:
        - Using the ``.query()`` method will send the ``EVENt:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``EVENt:POLarity?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EVENt:POLarity value`` command.

    SCPI Syntax:
        ```
        - EVENt:POLarity {POSitive|NEGative}
        - EVENt:POLarity?
        ```

    Info:
        - ``POSitive`` indicates that event jump occurs when the instrument receives a positive
          pulse.
        - ``NEGative`` indicates that event jump occurs when the instrument receives a negative
          pulse.
    """


class EventLevel(SCPICmdWrite, SCPICmdRead):
    """The ``EVENt:LEVel`` command.

    Description:
        - This command and query sets or returns the event level.

    Usage:
        - Using the ``.query()`` method will send the ``EVENt:LEVel?`` query.
        - Using the ``.verify(value)`` method will send the ``EVENt:LEVel?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EVENt:LEVel value`` command.

    SCPI Syntax:
        ```
        - EVENt:LEVel <level>
        - EVENt:LEVel?
        ```

    Info:
        - ``<level>`` ::=<NR3>.
    """


class EventJtiming(SCPICmdWrite, SCPICmdRead):
    r"""The ``EVENt:JTIMing`` command.

    Description:
        - This command and query sets or returns the jump timing. Refer to the User Online Help for
          more information on jump timing.

    Usage:
        - Using the ``.query()`` method will send the ``EVENt:JTIMing?`` query.
        - Using the ``.verify(value)`` method will send the ``EVENt:JTIMing?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EVENt:JTIMing value`` command.

    SCPI Syntax:
        ```
        - EVENt:JTIMing <jump_type>
        - EVENt:JTIMing?
        ```

    Info:
        - ``<jump_type>`` ::={SYNChronous\|ASYNchronous}.
        - ``SYNChronous`` indicates jump occurs immediately.
        - ``ASYNchronous`` indicates jump occurs after the signal generation is finished.
    """


class EventImpedance(SCPICmdWrite, SCPICmdRead):
    """The ``EVENt:IMPedance`` command.

    Description:
        - This command and query sets or returns the impedance of the external event input. Valid
          values are 50 ohm or 1 kohm.

    Usage:
        - Using the ``.query()`` method will send the ``EVENt:IMPedance?`` query.
        - Using the ``.verify(value)`` method will send the ``EVENt:IMPedance?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EVENt:IMPedance value`` command.

    SCPI Syntax:
        ```
        - EVENt:IMPedance <ohms>
        - EVENt:IMPedance?
        ```

    Info:
        - ``<ohms>`` ::=<NR3>.
    """


class EventImmediate(SCPICmdWriteNoArguments):
    """The ``EVENt:IMMediate`` command.

    Description:
        - This command generates a forced event. This is used to generate the event when the
          sequence is waiting for an event jump (See ``SEQUENCE:ELEMENTN:JTARGET:TYPE``). This is
          equivalent to pressing the Force Event button on the front panel of the instrument.

    Usage:
        - Using the ``.write()`` method will send the ``EVENt:IMMediate`` command.

    SCPI Syntax:
        ```
        - EVENt:IMMediate
        ```
    """


class Event(SCPICmdRead):
    """The ``EVENt`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``EVENt?`` query.
        - Using the ``.verify(value)`` method will send the ``EVENt?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.impedance``: The ``EVENt:IMPedance`` command.
        - ``.jtiming``: The ``EVENt:JTIMing`` command.
        - ``.level``: The ``EVENt:LEVel`` command.
        - ``.polarity``: The ``EVENt:POLarity`` command.
        - ``.immediate``: The ``EVENt:IMMediate`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "EVENt") -> None:
        super().__init__(device, cmd_syntax)
        self._impedance = EventImpedance(device, f"{self._cmd_syntax}:IMPedance")
        self._jtiming = EventJtiming(device, f"{self._cmd_syntax}:JTIMing")
        self._level = EventLevel(device, f"{self._cmd_syntax}:LEVel")
        self._polarity = EventPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._immediate = EventImmediate(device, f"{self._cmd_syntax}:IMMediate")

    @property
    def impedance(self) -> EventImpedance:
        """Return the ``EVENt:IMPedance`` command.

        Description:
            - This command and query sets or returns the impedance of the external event input.
              Valid values are 50 ohm or 1 kohm.

        Usage:
            - Using the ``.query()`` method will send the ``EVENt:IMPedance?`` query.
            - Using the ``.verify(value)`` method will send the ``EVENt:IMPedance?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EVENt:IMPedance value`` command.

        SCPI Syntax:
            ```
            - EVENt:IMPedance <ohms>
            - EVENt:IMPedance?
            ```

        Info:
            - ``<ohms>`` ::=<NR3>.
        """
        return self._impedance

    @property
    def jtiming(self) -> EventJtiming:
        r"""Return the ``EVENt:JTIMing`` command.

        Description:
            - This command and query sets or returns the jump timing. Refer to the User Online Help
              for more information on jump timing.

        Usage:
            - Using the ``.query()`` method will send the ``EVENt:JTIMing?`` query.
            - Using the ``.verify(value)`` method will send the ``EVENt:JTIMing?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EVENt:JTIMing value`` command.

        SCPI Syntax:
            ```
            - EVENt:JTIMing <jump_type>
            - EVENt:JTIMing?
            ```

        Info:
            - ``<jump_type>`` ::={SYNChronous\|ASYNchronous}.
            - ``SYNChronous`` indicates jump occurs immediately.
            - ``ASYNchronous`` indicates jump occurs after the signal generation is finished.
        """
        return self._jtiming

    @property
    def level(self) -> EventLevel:
        """Return the ``EVENt:LEVel`` command.

        Description:
            - This command and query sets or returns the event level.

        Usage:
            - Using the ``.query()`` method will send the ``EVENt:LEVel?`` query.
            - Using the ``.verify(value)`` method will send the ``EVENt:LEVel?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EVENt:LEVel value`` command.

        SCPI Syntax:
            ```
            - EVENt:LEVel <level>
            - EVENt:LEVel?
            ```

        Info:
            - ``<level>`` ::=<NR3>.
        """
        return self._level

    @property
    def polarity(self) -> EventPolarity:
        """Return the ``EVENt:POLarity`` command.

        Description:
            - This command and query sets or returns the polarity of event signal. The Event Jump is
              the function to change the sequencing of the waveform by an event signal.

        Usage:
            - Using the ``.query()`` method will send the ``EVENt:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``EVENt:POLarity?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EVENt:POLarity value`` command.

        SCPI Syntax:
            ```
            - EVENt:POLarity {POSitive|NEGative}
            - EVENt:POLarity?
            ```

        Info:
            - ``POSitive`` indicates that event jump occurs when the instrument receives a positive
              pulse.
            - ``NEGative`` indicates that event jump occurs when the instrument receives a negative
              pulse.
        """
        return self._polarity

    @property
    def immediate(self) -> EventImmediate:
        """Return the ``EVENt:IMMediate`` command.

        Description:
            - This command generates a forced event. This is used to generate the event when the
              sequence is waiting for an event jump (See ``SEQUENCE:ELEMENTN:JTARGET:TYPE``). This
              is equivalent to pressing the Force Event button on the front panel of the instrument.

        Usage:
            - Using the ``.write()`` method will send the ``EVENt:IMMediate`` command.

        SCPI Syntax:
            ```
            - EVENt:IMMediate
            ```
        """
        return self._immediate
