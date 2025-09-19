"""The trigger commands module.

These commands are used in the following models:
AWG5K, AWG5KC, AWG7K, AWG7KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - TRIGger:SEQuence:IMMediate
    - TRIGger:SEQuence:IMPedance <impedance>
    - TRIGger:SEQuence:IMPedance?
    - TRIGger:SEQuence:LEVel <NR3>
    - TRIGger:SEQuence:LEVel?
    - TRIGger:SEQuence:MODE <trigger_type>
    - TRIGger:SEQuence:MODE?
    - TRIGger:SEQuence:POLarity {POSitive|NEGative}
    - TRIGger:SEQuence:POLarity?
    - TRIGger:SEQuence:SLOPe {POSitive|NEGative}
    - TRIGger:SEQuence:SLOPe?
    - TRIGger:SEQuence:SOURce {INTernal|EXTernal}
    - TRIGger:SEQuence:SOURce?
    - TRIGger:SEQuence:TIMer <NR3>
    - TRIGger:SEQuence:TIMer?
    - TRIGger:SEQuence:WVALue {FIRSt|LAST}
    - TRIGger:SEQuence:WVALue?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class TriggerSequenceWvalue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:SEQuence:WVALue`` command.

    Description:
        - This command and query sets or returns the output data position of a waveform while the
          instrument is in the waiting-for-trigger state. This is valid only when Run Mode is
          Triggered or Gated.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:SEQuence:WVALue?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:SEQuence:WVALue?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:SEQuence:WVALue value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:SEQuence:WVALue {FIRSt|LAST}
        - TRIGger:SEQuence:WVALue?
        ```

    Info:
        - ``FIRSt`` specifies the first value of the waveform as the output level.
        - ``LAST`` specifies the last value of the waveform as the output level.
    """


class TriggerSequenceTimer(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:SEQuence:TIMer`` command.

    Description:
        - This command and query sets or returns the internal trigger rate (trigger interval).

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:SEQuence:TIMer?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:SEQuence:TIMer?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:SEQuence:TIMer value`` command.

    SCPI Syntax:
        ```
        - TRIGger:SEQuence:TIMer <NR3>
        - TRIGger:SEQuence:TIMer?
        ```

    Info:
        - ``<NR3>``
    """


class TriggerSequenceSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:SEQuence:SOURce`` command.

    Description:
        - This command and query sets or returns the trigger source.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:SEQuence:SOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:SEQuence:SOURce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:SEQuence:SOURce value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:SEQuence:SOURce {INTernal|EXTernal}
        - TRIGger:SEQuence:SOURce?
        ```

    Info:
        - ``INTernal`` selects internal clock as the trigger source.
        - ``EXTernal`` selects external clock as the trigger source.
    """


class TriggerSequenceSlope(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:SEQuence:SLOPe`` command.

    Description:
        - This command sets or queries the slope of trigger signal.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:SEQuence:SLOPe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:SEQuence:SLOPe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:SEQuence:SLOPe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:SEQuence:SLOPe {POSitive|NEGative}
        - TRIGger:SEQuence:SLOPe?
        ```

    Info:
        - ``POSitive`` indicates that the event occurs on the rising edge of the external trigger
          signal.
        - ``NEGative`` indicates that the event occurs on the falling edge of the external trigger
          signal.
    """


class TriggerSequencePolarity(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:SEQuence:POLarity`` command.

    Description:
        - This command and query sets or returns the trigger input polarity. It is used to set
          polarity in gated mode.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:SEQuence:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:SEQuence:POLarity?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:SEQuence:POLarity value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:SEQuence:POLarity {POSitive|NEGative}
        - TRIGger:SEQuence:POLarity?
        ```

    Info:
        - ``POSitive`` means the gate signal is activated when the external trigger signal is
          greater (more Positive) than the trigger level.
        - ``NEGative`` means the gate signal is activated when the external trigger signal is less
          (more Negative) than the trigger level.
    """


class TriggerSequenceMode(SCPICmdWrite, SCPICmdRead):
    r"""The ``TRIGger:SEQuence:MODE`` command.

    Description:
        - (AWG7000B and AWG7000C Series only) This command and query sets or returns the trigger
          timing. It is used in the Triggered or Sequence mode. Trigger timing can be set when the
          external trigger source is selected.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:SEQuence:MODE?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:SEQuence:MODE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:SEQuence:MODE value`` command.

    SCPI Syntax:
        ```
        - TRIGger:SEQuence:MODE <trigger_type>
        - TRIGger:SEQuence:MODE?
        ```

    Info:
        - ``<trigger_type`` >::={SYNChronous\|ASYNchronous}.
    """


class TriggerSequenceLevel(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:SEQuence:LEVel`` command.

    Description:
        - This command and query sets or returns the trigger input level (threshold).

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:SEQuence:LEVel?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:SEQuence:LEVel?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:SEQuence:LEVel value`` command.

    SCPI Syntax:
        ```
        - TRIGger:SEQuence:LEVel <NR3>
        - TRIGger:SEQuence:LEVel?
        ```

    Info:
        - ``<NR3>``
    """


class TriggerSequenceImpedance(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:SEQuence:IMPedance`` command.

    Description:
        - This command and query sets or returns the trigger impedance. It applies only to the
          external trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:SEQuence:IMPedance?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:SEQuence:IMPedance?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:SEQuence:IMPedance value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:SEQuence:IMPedance <impedance>
        - TRIGger:SEQuence:IMPedance?
        ```

    Info:
        - ``<impedance>`` ::=<NR3> the value will be 50 and 1000.
    """


class TriggerSequenceImmediate(SCPICmdWriteNoArguments):
    """The ``TRIGger:SEQuence:IMMediate`` command.

    Description:
        - This command forces a trigger event to occur.

    Usage:
        - Using the ``.write()`` method will send the ``TRIGger:SEQuence:IMMediate`` command.

    SCPI Syntax:
        ```
        - TRIGger:SEQuence:IMMediate
        ```
    """


#  pylint: disable=too-many-instance-attributes
class TriggerSequence(SCPICmdRead):
    """The ``TRIGger:SEQuence`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:SEQuence?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:SEQuence?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.impedance``: The ``TRIGger:SEQuence:IMPedance`` command.
        - ``.level``: The ``TRIGger:SEQuence:LEVel`` command.
        - ``.mode``: The ``TRIGger:SEQuence:MODE`` command.
        - ``.polarity``: The ``TRIGger:SEQuence:POLarity`` command.
        - ``.slope``: The ``TRIGger:SEQuence:SLOPe`` command.
        - ``.source``: The ``TRIGger:SEQuence:SOURce`` command.
        - ``.timer``: The ``TRIGger:SEQuence:TIMer`` command.
        - ``.wvalue``: The ``TRIGger:SEQuence:WVALue`` command.
        - ``.immediate``: The ``TRIGger:SEQuence:IMMediate`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._impedance = TriggerSequenceImpedance(device, f"{self._cmd_syntax}:IMPedance")
        self._level = TriggerSequenceLevel(device, f"{self._cmd_syntax}:LEVel")
        self._mode = TriggerSequenceMode(device, f"{self._cmd_syntax}:MODE")
        self._polarity = TriggerSequencePolarity(device, f"{self._cmd_syntax}:POLarity")
        self._slope = TriggerSequenceSlope(device, f"{self._cmd_syntax}:SLOPe")
        self._source = TriggerSequenceSource(device, f"{self._cmd_syntax}:SOURce")
        self._timer = TriggerSequenceTimer(device, f"{self._cmd_syntax}:TIMer")
        self._wvalue = TriggerSequenceWvalue(device, f"{self._cmd_syntax}:WVALue")
        self._immediate = TriggerSequenceImmediate(device, f"{self._cmd_syntax}:IMMediate")

    @property
    def impedance(self) -> TriggerSequenceImpedance:
        """Return the ``TRIGger:SEQuence:IMPedance`` command.

        Description:
            - This command and query sets or returns the trigger impedance. It applies only to the
              external trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:SEQuence:IMPedance?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:SEQuence:IMPedance?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:SEQuence:IMPedance value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:SEQuence:IMPedance <impedance>
            - TRIGger:SEQuence:IMPedance?
            ```

        Info:
            - ``<impedance>`` ::=<NR3> the value will be 50 and 1000.
        """
        return self._impedance

    @property
    def level(self) -> TriggerSequenceLevel:
        """Return the ``TRIGger:SEQuence:LEVel`` command.

        Description:
            - This command and query sets or returns the trigger input level (threshold).

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:SEQuence:LEVel?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:SEQuence:LEVel?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:SEQuence:LEVel value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:SEQuence:LEVel <NR3>
            - TRIGger:SEQuence:LEVel?
            ```

        Info:
            - ``<NR3>``
        """
        return self._level

    @property
    def mode(self) -> TriggerSequenceMode:
        r"""Return the ``TRIGger:SEQuence:MODE`` command.

        Description:
            - (AWG7000B and AWG7000C Series only) This command and query sets or returns the trigger
              timing. It is used in the Triggered or Sequence mode. Trigger timing can be set when
              the external trigger source is selected.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:SEQuence:MODE?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:SEQuence:MODE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:SEQuence:MODE value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:SEQuence:MODE <trigger_type>
            - TRIGger:SEQuence:MODE?
            ```

        Info:
            - ``<trigger_type`` >::={SYNChronous\|ASYNchronous}.
        """
        return self._mode

    @property
    def polarity(self) -> TriggerSequencePolarity:
        """Return the ``TRIGger:SEQuence:POLarity`` command.

        Description:
            - This command and query sets or returns the trigger input polarity. It is used to set
              polarity in gated mode.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:SEQuence:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:SEQuence:POLarity?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:SEQuence:POLarity value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:SEQuence:POLarity {POSitive|NEGative}
            - TRIGger:SEQuence:POLarity?
            ```

        Info:
            - ``POSitive`` means the gate signal is activated when the external trigger signal is
              greater (more Positive) than the trigger level.
            - ``NEGative`` means the gate signal is activated when the external trigger signal is
              less (more Negative) than the trigger level.
        """
        return self._polarity

    @property
    def slope(self) -> TriggerSequenceSlope:
        """Return the ``TRIGger:SEQuence:SLOPe`` command.

        Description:
            - This command sets or queries the slope of trigger signal.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:SEQuence:SLOPe?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:SEQuence:SLOPe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:SEQuence:SLOPe value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:SEQuence:SLOPe {POSitive|NEGative}
            - TRIGger:SEQuence:SLOPe?
            ```

        Info:
            - ``POSitive`` indicates that the event occurs on the rising edge of the external
              trigger signal.
            - ``NEGative`` indicates that the event occurs on the falling edge of the external
              trigger signal.
        """
        return self._slope

    @property
    def source(self) -> TriggerSequenceSource:
        """Return the ``TRIGger:SEQuence:SOURce`` command.

        Description:
            - This command and query sets or returns the trigger source.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:SEQuence:SOURce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:SEQuence:SOURce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:SEQuence:SOURce value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:SEQuence:SOURce {INTernal|EXTernal}
            - TRIGger:SEQuence:SOURce?
            ```

        Info:
            - ``INTernal`` selects internal clock as the trigger source.
            - ``EXTernal`` selects external clock as the trigger source.
        """
        return self._source

    @property
    def timer(self) -> TriggerSequenceTimer:
        """Return the ``TRIGger:SEQuence:TIMer`` command.

        Description:
            - This command and query sets or returns the internal trigger rate (trigger interval).

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:SEQuence:TIMer?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:SEQuence:TIMer?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:SEQuence:TIMer value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:SEQuence:TIMer <NR3>
            - TRIGger:SEQuence:TIMer?
            ```

        Info:
            - ``<NR3>``
        """
        return self._timer

    @property
    def wvalue(self) -> TriggerSequenceWvalue:
        """Return the ``TRIGger:SEQuence:WVALue`` command.

        Description:
            - This command and query sets or returns the output data position of a waveform while
              the instrument is in the waiting-for-trigger state. This is valid only when Run Mode
              is Triggered or Gated.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:SEQuence:WVALue?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:SEQuence:WVALue?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:SEQuence:WVALue value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:SEQuence:WVALue {FIRSt|LAST}
            - TRIGger:SEQuence:WVALue?
            ```

        Info:
            - ``FIRSt`` specifies the first value of the waveform as the output level.
            - ``LAST`` specifies the last value of the waveform as the output level.
        """
        return self._wvalue

    @property
    def immediate(self) -> TriggerSequenceImmediate:
        """Return the ``TRIGger:SEQuence:IMMediate`` command.

        Description:
            - This command forces a trigger event to occur.

        Usage:
            - Using the ``.write()`` method will send the ``TRIGger:SEQuence:IMMediate`` command.

        SCPI Syntax:
            ```
            - TRIGger:SEQuence:IMMediate
            ```
        """
        return self._immediate


class Trigger(SCPICmdRead):
    """The ``TRIGger`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.sequence``: The ``TRIGger:SEQuence`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "TRIGger") -> None:
        super().__init__(device, cmd_syntax)
        self._sequence = TriggerSequence(device, f"{self._cmd_syntax}:SEQuence")

    @property
    def sequence(self) -> TriggerSequence:
        """Return the ``TRIGger:SEQuence`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:SEQuence?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:SEQuence?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.impedance``: The ``TRIGger:SEQuence:IMPedance`` command.
            - ``.level``: The ``TRIGger:SEQuence:LEVel`` command.
            - ``.mode``: The ``TRIGger:SEQuence:MODE`` command.
            - ``.polarity``: The ``TRIGger:SEQuence:POLarity`` command.
            - ``.slope``: The ``TRIGger:SEQuence:SLOPe`` command.
            - ``.source``: The ``TRIGger:SEQuence:SOURce`` command.
            - ``.timer``: The ``TRIGger:SEQuence:TIMer`` command.
            - ``.wvalue``: The ``TRIGger:SEQuence:WVALue`` command.
            - ``.immediate``: The ``TRIGger:SEQuence:IMMediate`` command.
        """
        return self._sequence
