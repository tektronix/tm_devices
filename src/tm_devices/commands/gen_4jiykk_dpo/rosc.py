"""The rosc commands module.

These commands are used in the following models:
DPO70KSX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - ROSc:OUT:FREQuency {MHZ10|MHZ100}
    - ROSc:OUT:FREQuency?
    - ROSc:OUT:ULTRAsync {OFF|ON}
    - ROSc:OUT:ULTRAsync?
    - ROSc:SOUrce {EXTernal|INTERnal|TEKLink|ULTRAsync}
    - ROSc:SOUrce?
    - ROSc:STATE?
    - ROSc:TRACking {STABle|FAST}
    - ROSc:TRACking?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class RoscTracking(SCPICmdWrite, SCPICmdRead):
    """The ``ROSc:TRACking`` command.

    Description:
        - This command sets or queries the tracking mode for the time base reference oscillator. The
          reference oscillator locks to the source. Depending on the command argument that you
          specify, you can use an external reference signal that is fed through or bypasses the
          phase-locked loop. This command is also useful for synchronizing multiple instruments.

    Usage:
        - Using the ``.query()`` method will send the ``ROSc:TRACking?`` query.
        - Using the ``.verify(value)`` method will send the ``ROSc:TRACking?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ROSc:TRACking value`` command.

    SCPI Syntax:
        ```
        - ROSc:TRACking {STABle|FAST}
        - ROSc:TRACking?
        ```

    Info:
        - ``STABle`` tracking mode specifies that the external reference signal is fed through a
          phase-locked loop that removes jitter from the external reference.
        - ``FAST`` tracking mode specifies that the external reference signal bypasses the
          phase-locked loop.
    """


class RoscState(SCPICmdRead):
    """The ``ROSc:STATE`` command.

    Description:
        - This query-only command returns whether the time base reference oscillator is locked. This
          command will return either LOCKED or UNLOCKED.

    Usage:
        - Using the ``.query()`` method will send the ``ROSc:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``ROSc:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ROSc:STATE?
        ```
    """


class RoscSource(SCPICmdWrite, SCPICmdRead):
    """The ``ROSc:SOUrce`` command.

    Description:
        - This command sets or queries the selected source for the time base reference oscillator.
          The reference oscillator locks to this source. Depending on the command argument that you
          specify, you can use an external reference or use the internal crystal oscillator as the
          time base reference. This command is also useful for synchronizing multiple instruments.

    Usage:
        - Using the ``.query()`` method will send the ``ROSc:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``ROSc:SOUrce?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ROSc:SOUrce value`` command.

    SCPI Syntax:
        ```
        - ROSc:SOUrce {EXTernal|INTERnal|TEKLink|ULTRAsync}
        - ROSc:SOUrce?
        ```

    Info:
        - ``ULTRAsync`` specifies the 12.5 GHz UltraSync Clock as the time base reference.
        - ``INTERnal`` specifies the internal 10 MHz crystal oscillator as the time base reference.
        - ``EXTernal`` specifies the user-supplied external signal as the time base reference.
        - ``TEKLink`` specifies the TekLink signal as the time base reference.
    """


class RoscOutUltrasync(SCPICmdWrite, SCPICmdRead):
    """The ``ROSc:OUT:ULTRAsync`` command.

    Description:
        - This command sets or queries the state of the UltraSync 12.5 GHz Clock Out. DPO70000SX
          Series only.

    Usage:
        - Using the ``.query()`` method will send the ``ROSc:OUT:ULTRAsync?`` query.
        - Using the ``.verify(value)`` method will send the ``ROSc:OUT:ULTRAsync?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ROSc:OUT:ULTRAsync value`` command.

    SCPI Syntax:
        ```
        - ROSc:OUT:ULTRAsync {OFF|ON}
        - ROSc:OUT:ULTRAsync?
        ```

    Info:
        - ``OFF`` disables the 12.5 GHz Clock Out.
        - ``ON`` enables the 12.5 GHz Clock Out.
    """


class RoscOutFrequency(SCPICmdWrite, SCPICmdRead):
    """The ``ROSc:OUT:FREQuency`` command.

    Description:
        - This command sets or returns the selected frequency for the timebase reference output
          signal.

    Usage:
        - Using the ``.query()`` method will send the ``ROSc:OUT:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``ROSc:OUT:FREQuency?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ROSc:OUT:FREQuency value`` command.

    SCPI Syntax:
        ```
        - ROSc:OUT:FREQuency {MHZ10|MHZ100}
        - ROSc:OUT:FREQuency?
        ```

    Info:
        - ``MHZ10`` outputs a 10 MHz reference signal to the REF OUT connector.
        - ``MHZ100`` outputs a 100 MHz reference signal to the REF OUT connector.
    """


class RoscOut(SCPICmdRead):
    """The ``ROSc:OUT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ROSc:OUT?`` query.
        - Using the ``.verify(value)`` method will send the ``ROSc:OUT?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.frequency``: The ``ROSc:OUT:FREQuency`` command.
        - ``.ultrasync``: The ``ROSc:OUT:ULTRAsync`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._frequency = RoscOutFrequency(device, f"{self._cmd_syntax}:FREQuency")
        self._ultrasync = RoscOutUltrasync(device, f"{self._cmd_syntax}:ULTRAsync")

    @property
    def frequency(self) -> RoscOutFrequency:
        """Return the ``ROSc:OUT:FREQuency`` command.

        Description:
            - This command sets or returns the selected frequency for the timebase reference output
              signal.

        Usage:
            - Using the ``.query()`` method will send the ``ROSc:OUT:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``ROSc:OUT:FREQuency?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ROSc:OUT:FREQuency value`` command.

        SCPI Syntax:
            ```
            - ROSc:OUT:FREQuency {MHZ10|MHZ100}
            - ROSc:OUT:FREQuency?
            ```

        Info:
            - ``MHZ10`` outputs a 10 MHz reference signal to the REF OUT connector.
            - ``MHZ100`` outputs a 100 MHz reference signal to the REF OUT connector.
        """
        return self._frequency

    @property
    def ultrasync(self) -> RoscOutUltrasync:
        """Return the ``ROSc:OUT:ULTRAsync`` command.

        Description:
            - This command sets or queries the state of the UltraSync 12.5 GHz Clock Out. DPO70000SX
              Series only.

        Usage:
            - Using the ``.query()`` method will send the ``ROSc:OUT:ULTRAsync?`` query.
            - Using the ``.verify(value)`` method will send the ``ROSc:OUT:ULTRAsync?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ROSc:OUT:ULTRAsync value`` command.

        SCPI Syntax:
            ```
            - ROSc:OUT:ULTRAsync {OFF|ON}
            - ROSc:OUT:ULTRAsync?
            ```

        Info:
            - ``OFF`` disables the 12.5 GHz Clock Out.
            - ``ON`` enables the 12.5 GHz Clock Out.
        """
        return self._ultrasync


class Rosc(SCPICmdRead):
    """The ``ROSc`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ROSc?`` query.
        - Using the ``.verify(value)`` method will send the ``ROSc?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.out``: The ``ROSc:OUT`` command tree.
        - ``.source``: The ``ROSc:SOUrce`` command.
        - ``.state``: The ``ROSc:STATE`` command.
        - ``.tracking``: The ``ROSc:TRACking`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "ROSc") -> None:
        super().__init__(device, cmd_syntax)
        self._out = RoscOut(device, f"{self._cmd_syntax}:OUT")
        self._source = RoscSource(device, f"{self._cmd_syntax}:SOUrce")
        self._state = RoscState(device, f"{self._cmd_syntax}:STATE")
        self._tracking = RoscTracking(device, f"{self._cmd_syntax}:TRACking")

    @property
    def out(self) -> RoscOut:
        """Return the ``ROSc:OUT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ROSc:OUT?`` query.
            - Using the ``.verify(value)`` method will send the ``ROSc:OUT?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.frequency``: The ``ROSc:OUT:FREQuency`` command.
            - ``.ultrasync``: The ``ROSc:OUT:ULTRAsync`` command.
        """
        return self._out

    @property
    def source(self) -> RoscSource:
        """Return the ``ROSc:SOUrce`` command.

        Description:
            - This command sets or queries the selected source for the time base reference
              oscillator. The reference oscillator locks to this source. Depending on the command
              argument that you specify, you can use an external reference or use the internal
              crystal oscillator as the time base reference. This command is also useful for
              synchronizing multiple instruments.

        Usage:
            - Using the ``.query()`` method will send the ``ROSc:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``ROSc:SOUrce?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ROSc:SOUrce value`` command.

        SCPI Syntax:
            ```
            - ROSc:SOUrce {EXTernal|INTERnal|TEKLink|ULTRAsync}
            - ROSc:SOUrce?
            ```

        Info:
            - ``ULTRAsync`` specifies the 12.5 GHz UltraSync Clock as the time base reference.
            - ``INTERnal`` specifies the internal 10 MHz crystal oscillator as the time base
              reference.
            - ``EXTernal`` specifies the user-supplied external signal as the time base reference.
            - ``TEKLink`` specifies the TekLink signal as the time base reference.
        """
        return self._source

    @property
    def state(self) -> RoscState:
        """Return the ``ROSc:STATE`` command.

        Description:
            - This query-only command returns whether the time base reference oscillator is locked.
              This command will return either LOCKED or UNLOCKED.

        Usage:
            - Using the ``.query()`` method will send the ``ROSc:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``ROSc:STATE?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ROSc:STATE?
            ```
        """
        return self._state

    @property
    def tracking(self) -> RoscTracking:
        """Return the ``ROSc:TRACking`` command.

        Description:
            - This command sets or queries the tracking mode for the time base reference oscillator.
              The reference oscillator locks to the source. Depending on the command argument that
              you specify, you can use an external reference signal that is fed through or bypasses
              the phase-locked loop. This command is also useful for synchronizing multiple
              instruments.

        Usage:
            - Using the ``.query()`` method will send the ``ROSc:TRACking?`` query.
            - Using the ``.verify(value)`` method will send the ``ROSc:TRACking?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ROSc:TRACking value`` command.

        SCPI Syntax:
            ```
            - ROSc:TRACking {STABle|FAST}
            - ROSc:TRACking?
            ```

        Info:
            - ``STABle`` tracking mode specifies that the external reference signal is fed through a
              phase-locked loop that removes jitter from the external reference.
            - ``FAST`` tracking mode specifies that the external reference signal bypasses the
              phase-locked loop.
        """
        return self._tracking
