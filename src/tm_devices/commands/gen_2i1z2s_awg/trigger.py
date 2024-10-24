"""The trigger commands module.

These commands are used in the following models:
AWG5200

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - TRIGger:IMMediate {ATRigger|BTRigger}
    - TRIGger:IMPedance <impedance>[,<input_trigger>]
    - TRIGger:IMPedance? [<input_trigger>]
    - TRIGger:INTerval <NR3>
    - TRIGger:INTerval?
    - TRIGger:LEVel <NRf>[,ATRigger|BTRigger]
    - TRIGger:LEVel? [ATRigger|BTRigger]
    - TRIGger:MODE {SYNChronous}[,<input_trigger>]
    - TRIGger:MODE? <input_trigger>
    - TRIGger:SLOPe {POSitive|NEGative}[,<input_trigger>]
    - TRIGger:SLOPe? [<input_trigger>]
    - TRIGger:SOURce {EXTernal|INTernal}
    - TRIGger:SOURce?
    - TRIGger:WVALue {FIRSt}
    - TRIGger:WVALue?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdReadWithArguments, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class TriggerWvalue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:WVALue`` command.

    Description:
        - This command sets or returns the channel's output state when in the Waiting-for-trigger
          mode. This value is applied to all channels and markers.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:WVALue?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:WVALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:WVALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:WVALue {FIRSt}
        - TRIGger:WVALue?
        ```

    Info:
        - ``FIRSt`` specifies the first value of the waveform as the output level.
        - ``*RST`` sets this to ZERO.
    """


class TriggerSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:SOURce`` command.

    Description:
        - This command sets or returns the trigger source.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:SOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:SOURce?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:SOURce value`` command.

    SCPI Syntax:
        ```
        - TRIGger:SOURce {EXTernal|INTernal}
        - TRIGger:SOURce?
        ```

    Info:
        - ``EXTernal`` selects external trigger as the trigger source.INTernal select internal
          interval timing as the trigger source.
        - ``*RST`` sets this to EXT.
    """


class TriggerSlope(SCPICmdWrite, SCPICmdReadWithArguments):
    r"""The ``TRIGger:SLOPe`` command.

    Description:
        - This command sets or returns the polarity of the external trigger slope. Use this command
          to set the polarity in modes other than gated mode.

    Usage:
        - Using the ``.query(argument)`` method will send the ``TRIGger:SLOPe? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the ``TRIGger:SLOPe? argument``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:SLOPe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:SLOPe {POSitive|NEGative}[,<input_trigger>]
        - TRIGger:SLOPe? [<input_trigger>]
        ```

    Info:
        - ``POSitive`` specifies a trigger on the rising edge of the external trigger
          signal.NEGative specifies a trigger on the falling edge of the external trigger
          signal.``<input_trigger>`` ::= {ATRigger\|BTRigger}, defaults to ATR if not specified.
        - ``*RST`` sets all external trigger slopes to POSitive.
    """


class TriggerMode(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``TRIGger:MODE`` command.

    Description:
        - This command sets or returns the trigger timing used for the specified A or B external
          trigger source. SYNChronous is the only available trigger mode.

    Usage:
        - Using the ``.query(argument)`` method will send the ``TRIGger:MODE? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the ``TRIGger:MODE? argument``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:MODE value`` command.

    SCPI Syntax:
        ```
        - TRIGger:MODE {SYNChronous}[,<input_trigger>]
        - TRIGger:MODE? <input_trigger>
        ```

    Info:
        - ``SYNChronous`` : Synchronous triggering. This trigger type is used to synchronize with
          external devices.
        - ``*RST`` sets this to SYNchronous.
    """


class TriggerLevel(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``TRIGger:LEVel`` command.

    Description:
        - This command sets or returns the external trigger input level (threshold).

    Usage:
        - Using the ``.query(argument)`` method will send the ``TRIGger:LEVel? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the ``TRIGger:LEVel? argument``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:LEVel value`` command.

    SCPI Syntax:
        ```
        - TRIGger:LEVel <NRf>[,ATRigger|BTRigger]
        - TRIGger:LEVel? [ATRigger|BTRigger]
        ```

    Info:
        - ``ATRigger`` selects trigger input A. BTRigger selects trigger input B. Defaults to ATR if
          not specified.
        - ``*RST`` sets this to 1.4 V.
    """


class TriggerInterval(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:INTerval`` command.

    Description:
        - This command sets or returns the internal trigger interval.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:INTerval?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:INTerval?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:INTerval value`` command.

    SCPI Syntax:
        ```
        - TRIGger:INTerval <NR3>
        - TRIGger:INTerval?
        ```
    """


class TriggerImpedance(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``TRIGger:IMPedance`` command.

    Description:
        - This command sets or returns the external trigger impedance. It applies only to the
          external trigger.

    Usage:
        - Using the ``.query(argument)`` method will send the ``TRIGger:IMPedance? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``TRIGger:IMPedance? argument`` query and raise an AssertionError if the returned value
          does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:IMPedance value`` command.

    SCPI Syntax:
        ```
        - TRIGger:IMPedance <impedance>[,<input_trigger>]
        - TRIGger:IMPedance? [<input_trigger>]
        ```

    Info:
        - ``*RST`` sets this to 50.
    """


class TriggerImmediate(SCPICmdWrite):
    """The ``TRIGger:IMMediate`` command.

    Description:
        - This command generates a trigger A or B event. If a trigger is not specified, the command
          is then equivalent to the TRG command.

    Usage:
        - Using the ``.write(value)`` method will send the ``TRIGger:IMMediate value`` command.

    SCPI Syntax:
        ```
        - TRIGger:IMMediate {ATRigger|BTRigger}
        ```
    """


#  pylint: disable=too-many-instance-attributes
class Trigger(SCPICmdRead):
    """The ``TRIGger`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.impedance``: The ``TRIGger:IMPedance`` command.
        - ``.interval``: The ``TRIGger:INTerval`` command.
        - ``.level``: The ``TRIGger:LEVel`` command.
        - ``.mode``: The ``TRIGger:MODE`` command.
        - ``.slope``: The ``TRIGger:SLOPe`` command.
        - ``.source``: The ``TRIGger:SOURce`` command.
        - ``.wvalue``: The ``TRIGger:WVALue`` command.
        - ``.immediate``: The ``TRIGger:IMMediate`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "TRIGger") -> None:
        super().__init__(device, cmd_syntax)
        self._impedance = TriggerImpedance(device, f"{self._cmd_syntax}:IMPedance")
        self._interval = TriggerInterval(device, f"{self._cmd_syntax}:INTerval")
        self._level = TriggerLevel(device, f"{self._cmd_syntax}:LEVel")
        self._mode = TriggerMode(device, f"{self._cmd_syntax}:MODE")
        self._slope = TriggerSlope(device, f"{self._cmd_syntax}:SLOPe")
        self._source = TriggerSource(device, f"{self._cmd_syntax}:SOURce")
        self._wvalue = TriggerWvalue(device, f"{self._cmd_syntax}:WVALue")
        self._immediate = TriggerImmediate(device, f"{self._cmd_syntax}:IMMediate")

    @property
    def impedance(self) -> TriggerImpedance:
        """Return the ``TRIGger:IMPedance`` command.

        Description:
            - This command sets or returns the external trigger impedance. It applies only to the
              external trigger.

        Usage:
            - Using the ``.query(argument)`` method will send the ``TRIGger:IMPedance? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``TRIGger:IMPedance? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:IMPedance value`` command.

        SCPI Syntax:
            ```
            - TRIGger:IMPedance <impedance>[,<input_trigger>]
            - TRIGger:IMPedance? [<input_trigger>]
            ```

        Info:
            - ``*RST`` sets this to 50.
        """
        return self._impedance

    @property
    def interval(self) -> TriggerInterval:
        """Return the ``TRIGger:INTerval`` command.

        Description:
            - This command sets or returns the internal trigger interval.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:INTerval?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:INTerval?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:INTerval value`` command.

        SCPI Syntax:
            ```
            - TRIGger:INTerval <NR3>
            - TRIGger:INTerval?
            ```
        """
        return self._interval

    @property
    def level(self) -> TriggerLevel:
        """Return the ``TRIGger:LEVel`` command.

        Description:
            - This command sets or returns the external trigger input level (threshold).

        Usage:
            - Using the ``.query(argument)`` method will send the ``TRIGger:LEVel? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``TRIGger:LEVel? argument`` query and raise an AssertionError if the returned value
              does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:LEVel value`` command.

        SCPI Syntax:
            ```
            - TRIGger:LEVel <NRf>[,ATRigger|BTRigger]
            - TRIGger:LEVel? [ATRigger|BTRigger]
            ```

        Info:
            - ``ATRigger`` selects trigger input A. BTRigger selects trigger input B. Defaults to
              ATR if not specified.
            - ``*RST`` sets this to 1.4 V.
        """
        return self._level

    @property
    def mode(self) -> TriggerMode:
        """Return the ``TRIGger:MODE`` command.

        Description:
            - This command sets or returns the trigger timing used for the specified A or B external
              trigger source. SYNChronous is the only available trigger mode.

        Usage:
            - Using the ``.query(argument)`` method will send the ``TRIGger:MODE? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the ``TRIGger:MODE? argument``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:MODE value`` command.

        SCPI Syntax:
            ```
            - TRIGger:MODE {SYNChronous}[,<input_trigger>]
            - TRIGger:MODE? <input_trigger>
            ```

        Info:
            - ``SYNChronous`` : Synchronous triggering. This trigger type is used to synchronize
              with external devices.
            - ``*RST`` sets this to SYNchronous.
        """
        return self._mode

    @property
    def slope(self) -> TriggerSlope:
        r"""Return the ``TRIGger:SLOPe`` command.

        Description:
            - This command sets or returns the polarity of the external trigger slope. Use this
              command to set the polarity in modes other than gated mode.

        Usage:
            - Using the ``.query(argument)`` method will send the ``TRIGger:SLOPe? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``TRIGger:SLOPe? argument`` query and raise an AssertionError if the returned value
              does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:SLOPe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:SLOPe {POSitive|NEGative}[,<input_trigger>]
            - TRIGger:SLOPe? [<input_trigger>]
            ```

        Info:
            - ``POSitive`` specifies a trigger on the rising edge of the external trigger
              signal.NEGative specifies a trigger on the falling edge of the external trigger
              signal.``<input_trigger>`` ::= {ATRigger\|BTRigger}, defaults to ATR if not specified.
            - ``*RST`` sets all external trigger slopes to POSitive.
        """
        return self._slope

    @property
    def source(self) -> TriggerSource:
        """Return the ``TRIGger:SOURce`` command.

        Description:
            - This command sets or returns the trigger source.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:SOURce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:SOURce?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:SOURce value`` command.

        SCPI Syntax:
            ```
            - TRIGger:SOURce {EXTernal|INTernal}
            - TRIGger:SOURce?
            ```

        Info:
            - ``EXTernal`` selects external trigger as the trigger source.INTernal select internal
              interval timing as the trigger source.
            - ``*RST`` sets this to EXT.
        """
        return self._source

    @property
    def wvalue(self) -> TriggerWvalue:
        """Return the ``TRIGger:WVALue`` command.

        Description:
            - This command sets or returns the channel's output state when in the
              Waiting-for-trigger mode. This value is applied to all channels and markers.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:WVALue?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:WVALue?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:WVALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:WVALue {FIRSt}
            - TRIGger:WVALue?
            ```

        Info:
            - ``FIRSt`` specifies the first value of the waveform as the output level.
            - ``*RST`` sets this to ZERO.
        """
        return self._wvalue

    @property
    def immediate(self) -> TriggerImmediate:
        """Return the ``TRIGger:IMMediate`` command.

        Description:
            - This command generates a trigger A or B event. If a trigger is not specified, the
              command is then equivalent to the TRG command.

        Usage:
            - Using the ``.write(value)`` method will send the ``TRIGger:IMMediate value`` command.

        SCPI Syntax:
            ```
            - TRIGger:IMMediate {ATRigger|BTRigger}
            ```
        """
        return self._immediate
