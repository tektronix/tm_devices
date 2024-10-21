"""The trigger commands module.

These commands are used in the following models:
AFG3K, AFG3KB, AFG3KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - TRIGger:SEQuence:IMMediate
    - TRIGger:SEQuence:SLOPe {POSitive|NEGative}
    - TRIGger:SEQuence:SLOPe?
    - TRIGger:SEQuence:SOURce {TIMer|EXTernal}
    - TRIGger:SEQuence:SOURce?
    - TRIGger:SEQuence:TIMer <seconds>
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class TriggerSequenceTimer(SCPICmdWrite):
    """The ``TRIGger:SEQuence:TIMer`` command.

    Description:
        - This command sets or queries the period of an internal clock when you select the internal
          clock as the trigger source with the TRIGger[``:SEQuence``]``:SOURce`` command. The
          setting range is 1 µs to 500.0 s.

    Usage:
        - Using the ``.write(value)`` method will send the ``TRIGger:SEQuence:TIMer value`` command.

    SCPI Syntax:
        ```
        - TRIGger:SEQuence:TIMer <seconds>
        ```

    Info:
        - ``<seconds>::=<NRf>[<units>]``
    """


class TriggerSequenceSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:SEQuence:SOURce`` command.

    Description:
        - This command sets or queries the trigger source for an external trigger signal.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:SEQuence:SOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:SEQuence:SOURce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:SEQuence:SOURce value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:SEQuence:SOURce {TIMer|EXTernal}
        - TRIGger:SEQuence:SOURce?
        ```

    Info:
        - ``TIMer`` specifies an internal clock as the trigger source.
        - ``EXTernal`` specifies an external trigger input as the trigger source.
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


class TriggerSequence(SCPICmdRead):
    """The ``TRIGger:SEQuence`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:SEQuence?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:SEQuence?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.slope``: The ``TRIGger:SEQuence:SLOPe`` command.
        - ``.source``: The ``TRIGger:SEQuence:SOURce`` command.
        - ``.timer``: The ``TRIGger:SEQuence:TIMer`` command.
        - ``.immediate``: The ``TRIGger:SEQuence:IMMediate`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._slope = TriggerSequenceSlope(device, f"{self._cmd_syntax}:SLOPe")
        self._source = TriggerSequenceSource(device, f"{self._cmd_syntax}:SOURce")
        self._timer = TriggerSequenceTimer(device, f"{self._cmd_syntax}:TIMer")
        self._immediate = TriggerSequenceImmediate(device, f"{self._cmd_syntax}:IMMediate")

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
            - This command sets or queries the trigger source for an external trigger signal.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:SEQuence:SOURce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:SEQuence:SOURce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:SEQuence:SOURce value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:SEQuence:SOURce {TIMer|EXTernal}
            - TRIGger:SEQuence:SOURce?
            ```

        Info:
            - ``TIMer`` specifies an internal clock as the trigger source.
            - ``EXTernal`` specifies an external trigger input as the trigger source.
        """
        return self._source

    @property
    def timer(self) -> TriggerSequenceTimer:
        """Return the ``TRIGger:SEQuence:TIMer`` command.

        Description:
            - This command sets or queries the period of an internal clock when you select the
              internal clock as the trigger source with the TRIGger[``:SEQuence``]``:SOURce``
              command. The setting range is 1 µs to 500.0 s.

        Usage:
            - Using the ``.write(value)`` method will send the ``TRIGger:SEQuence:TIMer value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:SEQuence:TIMer <seconds>
            ```

        Info:
            - ``<seconds>::=<NRf>[<units>]``
        """
        return self._timer

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
            - ``.slope``: The ``TRIGger:SEQuence:SLOPe`` command.
            - ``.source``: The ``TRIGger:SEQuence:SOURce`` command.
            - ``.timer``: The ``TRIGger:SEQuence:TIMer`` command.
            - ``.immediate``: The ``TRIGger:SEQuence:IMMediate`` command.
        """
        return self._sequence
