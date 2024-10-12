"""The clock commands module.

These commands are used in the following models:
AWG5200

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CLOCk:ECLock:DIVider <NR1>
    - CLOCk:ECLock:DIVider?
    - CLOCk:ECLock:FREQuency <NR3>
    - CLOCk:ECLock:FREQuency:DETect
    - CLOCk:ECLock:FREQuency?
    - CLOCk:ECLock:MULTiplier <NR1>
    - CLOCk:ECLock:MULTiplier?
    - CLOCk:EREFerence:DIVider <NR1>
    - CLOCk:EREFerence:DIVider?
    - CLOCk:EREFerence:FREQuency <NRf>
    - CLOCk:EREFerence:FREQuency:DETect
    - CLOCk:EREFerence:FREQuency?
    - CLOCk:EREFerence:MULTiplier <NR1>
    - CLOCk:EREFerence:MULTiplier?
    - CLOCk:JITTer {0|1|OFF|ON}
    - CLOCk:OUTPut:FREQuency?
    - CLOCk:OUTPut:STATe {0|1|OFF|ON}
    - CLOCk:OUTPut:STATe?
    - CLOCk:PHASe:ADJust:DEGRees <NR1>
    - CLOCk:PHASe:ADJust:DEGRees?
    - CLOCk:PHASe:ADJust:TIMe <NRf>
    - CLOCk:PHASe:ADJust:TIMe?
    - CLOCk:SOURce {INTernal|EFIXed|EVARiable|EXTernal}
    - CLOCk:SOURce?
    - CLOCk:SOUT:STATe {0|1|OFF|ON}
    - CLOCk:SOUT:STATe?
    - CLOCk:SRATe <NRf>
    - CLOCk:SRATe?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class ClockSrate(SCPICmdWrite, SCPICmdRead):
    r"""The ``CLOCk:SRATe`` command.

    Description:
        - This command sets or returns the sample rate for the clock. When ``CLOCk:SOURce`` is set
          to EXTernal, the maximum sample rate is: 4 \* External Clock In frequency (AWG70001)2 \*
          External Clock In frequency (AWG70002)

    Usage:
        - Using the ``.query()`` method will send the ``CLOCk:SRATe?`` query.
        - Using the ``.verify(value)`` method will send the ``CLOCk:SRATe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CLOCk:SRATe value`` command.

    SCPI Syntax:
        ```
        - CLOCk:SRATe <NRf>
        - CLOCk:SRATe?
        ```

    Info:
        - ``*RST`` sets this to the maximum value.
    """


class ClockSoutState(SCPICmdWrite, SCPICmdRead):
    """The ``CLOCk:SOUT:STATe`` command.

    Description:
        - This command sets or returns the state of the Sync Clock Out output.

    Usage:
        - Using the ``.query()`` method will send the ``CLOCk:SOUT:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``CLOCk:SOUT:STATe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CLOCk:SOUT:STATe value`` command.

    SCPI Syntax:
        ```
        - CLOCk:SOUT:STATe {0|1|OFF|ON}
        - CLOCk:SOUT:STATe?
        ```

    Info:
        - ``*RST`` sets this to 0.
    """


class ClockSout(SCPICmdRead):
    """The ``CLOCk:SOUT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CLOCk:SOUT?`` query.
        - Using the ``.verify(value)`` method will send the ``CLOCk:SOUT?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``CLOCk:SOUT:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ClockSoutState(device, f"{self._cmd_syntax}:STATe")

    @property
    def state(self) -> ClockSoutState:
        """Return the ``CLOCk:SOUT:STATe`` command.

        Description:
            - This command sets or returns the state of the Sync Clock Out output.

        Usage:
            - Using the ``.query()`` method will send the ``CLOCk:SOUT:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``CLOCk:SOUT:STATe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CLOCk:SOUT:STATe value`` command.

        SCPI Syntax:
            ```
            - CLOCk:SOUT:STATe {0|1|OFF|ON}
            - CLOCk:SOUT:STATe?
            ```

        Info:
            - ``*RST`` sets this to 0.
        """
        return self._state


class ClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``CLOCk:SOURce`` command.

    Description:
        - This command sets or returns the source of the clock.

    Usage:
        - Using the ``.query()`` method will send the ``CLOCk:SOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``CLOCk:SOURce?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CLOCk:SOURce value`` command.

    SCPI Syntax:
        ```
        - CLOCk:SOURce {INTernal|EFIXed|EVARiable|EXTernal}
        - CLOCk:SOURce?
        ```

    Info:
        - ``*RST`` sets this to INT.
    """


class ClockPhaseAdjustTime(SCPICmdWrite, SCPICmdRead):
    """The ``CLOCk:PHASe:ADJust:TIMe`` command.

    Description:
        - This command sets or returns the phase adjustment, in units of time, to synchronize
          multiple AWGs when using an external trigger. Setting the phase adjusts the phase of all
          signal outputs relative to the system clock.

    Usage:
        - Using the ``.query()`` method will send the ``CLOCk:PHASe:ADJust:TIMe?`` query.
        - Using the ``.verify(value)`` method will send the ``CLOCk:PHASe:ADJust:TIMe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CLOCk:PHASe:ADJust:TIMe value``
          command.

    SCPI Syntax:
        ```
        - CLOCk:PHASe:ADJust:TIMe <NRf>
        - CLOCk:PHASe:ADJust:TIMe?
        ```

    Info:
        - ``*RST`` sets this to 0 ps.
    """


class ClockPhaseAdjustDegrees(SCPICmdWrite, SCPICmdRead):
    """The ``CLOCk:PHASe:ADJust:DEGRees`` command.

    Description:
        - This command sets or returns the phase adjustment, in units of degrees, to synchronize
          multiple AWGs when using an external trigger. Setting the phase adjusts the phase of all
          signal outputs relative to the system clock.

    Usage:
        - Using the ``.query()`` method will send the ``CLOCk:PHASe:ADJust:DEGRees?`` query.
        - Using the ``.verify(value)`` method will send the ``CLOCk:PHASe:ADJust:DEGRees?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CLOCk:PHASe:ADJust:DEGRees value``
          command.

    SCPI Syntax:
        ```
        - CLOCk:PHASe:ADJust:DEGRees <NR1>
        - CLOCk:PHASe:ADJust:DEGRees?
        ```

    Info:
        - ``*RST`` sets this to 0.
    """


class ClockPhaseAdjust(SCPICmdRead):
    """The ``CLOCk:PHASe:ADJust`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CLOCk:PHASe:ADJust?`` query.
        - Using the ``.verify(value)`` method will send the ``CLOCk:PHASe:ADJust?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.degrees``: The ``CLOCk:PHASe:ADJust:DEGRees`` command.
        - ``.time``: The ``CLOCk:PHASe:ADJust:TIMe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._degrees = ClockPhaseAdjustDegrees(device, f"{self._cmd_syntax}:DEGRees")
        self._time = ClockPhaseAdjustTime(device, f"{self._cmd_syntax}:TIMe")

    @property
    def degrees(self) -> ClockPhaseAdjustDegrees:
        """Return the ``CLOCk:PHASe:ADJust:DEGRees`` command.

        Description:
            - This command sets or returns the phase adjustment, in units of degrees, to synchronize
              multiple AWGs when using an external trigger. Setting the phase adjusts the phase of
              all signal outputs relative to the system clock.

        Usage:
            - Using the ``.query()`` method will send the ``CLOCk:PHASe:ADJust:DEGRees?`` query.
            - Using the ``.verify(value)`` method will send the ``CLOCk:PHASe:ADJust:DEGRees?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CLOCk:PHASe:ADJust:DEGRees value``
              command.

        SCPI Syntax:
            ```
            - CLOCk:PHASe:ADJust:DEGRees <NR1>
            - CLOCk:PHASe:ADJust:DEGRees?
            ```

        Info:
            - ``*RST`` sets this to 0.
        """
        return self._degrees

    @property
    def time(self) -> ClockPhaseAdjustTime:
        """Return the ``CLOCk:PHASe:ADJust:TIMe`` command.

        Description:
            - This command sets or returns the phase adjustment, in units of time, to synchronize
              multiple AWGs when using an external trigger. Setting the phase adjusts the phase of
              all signal outputs relative to the system clock.

        Usage:
            - Using the ``.query()`` method will send the ``CLOCk:PHASe:ADJust:TIMe?`` query.
            - Using the ``.verify(value)`` method will send the ``CLOCk:PHASe:ADJust:TIMe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CLOCk:PHASe:ADJust:TIMe value``
              command.

        SCPI Syntax:
            ```
            - CLOCk:PHASe:ADJust:TIMe <NRf>
            - CLOCk:PHASe:ADJust:TIMe?
            ```

        Info:
            - ``*RST`` sets this to 0 ps.
        """
        return self._time


class ClockPhase(SCPICmdRead):
    """The ``CLOCk:PHASe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CLOCk:PHASe?`` query.
        - Using the ``.verify(value)`` method will send the ``CLOCk:PHASe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.adjust``: The ``CLOCk:PHASe:ADJust`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._adjust = ClockPhaseAdjust(device, f"{self._cmd_syntax}:ADJust")

    @property
    def adjust(self) -> ClockPhaseAdjust:
        """Return the ``CLOCk:PHASe:ADJust`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CLOCk:PHASe:ADJust?`` query.
            - Using the ``.verify(value)`` method will send the ``CLOCk:PHASe:ADJust?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.degrees``: The ``CLOCk:PHASe:ADJust:DEGRees`` command.
            - ``.time``: The ``CLOCk:PHASe:ADJust:TIMe`` command.
        """
        return self._adjust


class ClockOutputState(SCPICmdWrite, SCPICmdRead):
    """The ``CLOCk:OUTPut:STATe`` command.

    Description:
        - This command sets or returns the state of the output clock (enabled or disabled). Enabling
          Clock Out provides a high speed clock (that is related to sample rate) to drive other
          devices or to measure.

    Usage:
        - Using the ``.query()`` method will send the ``CLOCk:OUTPut:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``CLOCk:OUTPut:STATe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CLOCk:OUTPut:STATe value`` command.

    SCPI Syntax:
        ```
        - CLOCk:OUTPut:STATe {0|1|OFF|ON}
        - CLOCk:OUTPut:STATe?
        ```

    Info:
        - ``*RST`` sets this to 0.
    """


class ClockOutputFrequency(SCPICmdRead):
    """The ``CLOCk:OUTPut:FREQuency`` command.

    Description:
        - This command returns the frequency of the output clock on the Clock Out connector.

    Usage:
        - Using the ``.query()`` method will send the ``CLOCk:OUTPut:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``CLOCk:OUTPut:FREQuency?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CLOCk:OUTPut:FREQuency?
        ```
    """


class ClockOutput(SCPICmdRead):
    """The ``CLOCk:OUTPut`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CLOCk:OUTPut?`` query.
        - Using the ``.verify(value)`` method will send the ``CLOCk:OUTPut?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.frequency``: The ``CLOCk:OUTPut:FREQuency`` command.
        - ``.state``: The ``CLOCk:OUTPut:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._frequency = ClockOutputFrequency(device, f"{self._cmd_syntax}:FREQuency")
        self._state = ClockOutputState(device, f"{self._cmd_syntax}:STATe")

    @property
    def frequency(self) -> ClockOutputFrequency:
        """Return the ``CLOCk:OUTPut:FREQuency`` command.

        Description:
            - This command returns the frequency of the output clock on the Clock Out connector.

        Usage:
            - Using the ``.query()`` method will send the ``CLOCk:OUTPut:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``CLOCk:OUTPut:FREQuency?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CLOCk:OUTPut:FREQuency?
            ```
        """
        return self._frequency

    @property
    def state(self) -> ClockOutputState:
        """Return the ``CLOCk:OUTPut:STATe`` command.

        Description:
            - This command sets or returns the state of the output clock (enabled or disabled).
              Enabling Clock Out provides a high speed clock (that is related to sample rate) to
              drive other devices or to measure.

        Usage:
            - Using the ``.query()`` method will send the ``CLOCk:OUTPut:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``CLOCk:OUTPut:STATe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CLOCk:OUTPut:STATe value`` command.

        SCPI Syntax:
            ```
            - CLOCk:OUTPut:STATe {0|1|OFF|ON}
            - CLOCk:OUTPut:STATe?
            ```

        Info:
            - ``*RST`` sets this to 0.
        """
        return self._state


class ClockJitter(SCPICmdWrite):
    """The ``CLOCk:JITTer`` command.

    Description:
        - This command sets or returns the state (enabled or disabled) to apply or not apply jitter
          reduction to the internal system clock or the clock signal applied to the Reference In
          connector. When enabled, the chosen sample rate value will be adjusted to achieve the best
          performance.

    Usage:
        - Using the ``.write(value)`` method will send the ``CLOCk:JITTer value`` command.

    SCPI Syntax:
        ```
        - CLOCk:JITTer {0|1|OFF|ON}
        ```

    Info:
        - ``*RST`` sets this to 0.
    """


class ClockEreferenceMultiplier(SCPICmdWrite, SCPICmdRead):
    """The ``CLOCk:EREFerence:MULTiplier`` command.

    Description:
        - This command sets or returns the multiplier rate of the variable external reference
          signal.

    Usage:
        - Using the ``.query()`` method will send the ``CLOCk:EREFerence:MULTiplier?`` query.
        - Using the ``.verify(value)`` method will send the ``CLOCk:EREFerence:MULTiplier?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CLOCk:EREFerence:MULTiplier value``
          command.

    SCPI Syntax:
        ```
        - CLOCk:EREFerence:MULTiplier <NR1>
        - CLOCk:EREFerence:MULTiplier?
        ```

    Info:
        - ``*RST`` sets this to 1.
    """


class ClockEreferenceFrequencyDetect(SCPICmdWriteNoArguments):
    """The ``CLOCk:EREFerence:FREQuency:DETect`` command.

    Description:
        - This command detects the frequency of the signal applied to the Reference In connector and
          adjusts the system to use the signal. The frequency is detected once each time the command
          executes. An error message is generated if no frequency is detected, is out of range, or
          if the adjustment fails. This command is only valid when the clock source is external.
          Errors are not returned. They are added to the system error queue which can be accessed
          with ``SYSTEM:ERROR:NEXT``.

    Usage:
        - Using the ``.write()`` method will send the ``CLOCk:EREFerence:FREQuency:DETect`` command.

    SCPI Syntax:
        ```
        - CLOCk:EREFerence:FREQuency:DETect
        ```
    """


class ClockEreferenceFrequency(SCPICmdWrite, SCPICmdRead):
    """The ``CLOCk:EREFerence:FREQuency`` command.

    Description:
        - This command sets or returns the expected frequency of the signal applied to the Reference
          In connector.

    Usage:
        - Using the ``.query()`` method will send the ``CLOCk:EREFerence:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``CLOCk:EREFerence:FREQuency?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CLOCk:EREFerence:FREQuency value``
          command.

    SCPI Syntax:
        ```
        - CLOCk:EREFerence:FREQuency <NRf>
        - CLOCk:EREFerence:FREQuency?
        ```

    Info:
        - ``*RST`` sets this to 35 MHz.

    Properties:
        - ``.detect``: The ``CLOCk:EREFerence:FREQuency:DETect`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._detect = ClockEreferenceFrequencyDetect(device, f"{self._cmd_syntax}:DETect")

    @property
    def detect(self) -> ClockEreferenceFrequencyDetect:
        """Return the ``CLOCk:EREFerence:FREQuency:DETect`` command.

        Description:
            - This command detects the frequency of the signal applied to the Reference In connector
              and adjusts the system to use the signal. The frequency is detected once each time the
              command executes. An error message is generated if no frequency is detected, is out of
              range, or if the adjustment fails. This command is only valid when the clock source is
              external. Errors are not returned. They are added to the system error queue which can
              be accessed with ``SYSTEM:ERROR:NEXT``.

        Usage:
            - Using the ``.write()`` method will send the ``CLOCk:EREFerence:FREQuency:DETect``
              command.

        SCPI Syntax:
            ```
            - CLOCk:EREFerence:FREQuency:DETect
            ```
        """
        return self._detect


class ClockEreferenceDivider(SCPICmdWrite, SCPICmdRead):
    """The ``CLOCk:EREFerence:DIVider`` command.

    Description:
        - This command sets or returns the divider rate of the external reference signal when the
          external reference is variable.

    Usage:
        - Using the ``.query()`` method will send the ``CLOCk:EREFerence:DIVider?`` query.
        - Using the ``.verify(value)`` method will send the ``CLOCk:EREFerence:DIVider?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CLOCk:EREFerence:DIVider value``
          command.

    SCPI Syntax:
        ```
        - CLOCk:EREFerence:DIVider <NR1>
        - CLOCk:EREFerence:DIVider?
        ```

    Info:
        - ``*RST`` sets this to 1.
    """


class ClockEreference(SCPICmdRead):
    """The ``CLOCk:EREFerence`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CLOCk:EREFerence?`` query.
        - Using the ``.verify(value)`` method will send the ``CLOCk:EREFerence?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.divider``: The ``CLOCk:EREFerence:DIVider`` command.
        - ``.frequency``: The ``CLOCk:EREFerence:FREQuency`` command.
        - ``.multiplier``: The ``CLOCk:EREFerence:MULTiplier`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._divider = ClockEreferenceDivider(device, f"{self._cmd_syntax}:DIVider")
        self._frequency = ClockEreferenceFrequency(device, f"{self._cmd_syntax}:FREQuency")
        self._multiplier = ClockEreferenceMultiplier(device, f"{self._cmd_syntax}:MULTiplier")

    @property
    def divider(self) -> ClockEreferenceDivider:
        """Return the ``CLOCk:EREFerence:DIVider`` command.

        Description:
            - This command sets or returns the divider rate of the external reference signal when
              the external reference is variable.

        Usage:
            - Using the ``.query()`` method will send the ``CLOCk:EREFerence:DIVider?`` query.
            - Using the ``.verify(value)`` method will send the ``CLOCk:EREFerence:DIVider?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CLOCk:EREFerence:DIVider value``
              command.

        SCPI Syntax:
            ```
            - CLOCk:EREFerence:DIVider <NR1>
            - CLOCk:EREFerence:DIVider?
            ```

        Info:
            - ``*RST`` sets this to 1.
        """
        return self._divider

    @property
    def frequency(self) -> ClockEreferenceFrequency:
        """Return the ``CLOCk:EREFerence:FREQuency`` command.

        Description:
            - This command sets or returns the expected frequency of the signal applied to the
              Reference In connector.

        Usage:
            - Using the ``.query()`` method will send the ``CLOCk:EREFerence:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``CLOCk:EREFerence:FREQuency?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CLOCk:EREFerence:FREQuency value``
              command.

        SCPI Syntax:
            ```
            - CLOCk:EREFerence:FREQuency <NRf>
            - CLOCk:EREFerence:FREQuency?
            ```

        Info:
            - ``*RST`` sets this to 35 MHz.

        Sub-properties:
            - ``.detect``: The ``CLOCk:EREFerence:FREQuency:DETect`` command.
        """
        return self._frequency

    @property
    def multiplier(self) -> ClockEreferenceMultiplier:
        """Return the ``CLOCk:EREFerence:MULTiplier`` command.

        Description:
            - This command sets or returns the multiplier rate of the variable external reference
              signal.

        Usage:
            - Using the ``.query()`` method will send the ``CLOCk:EREFerence:MULTiplier?`` query.
            - Using the ``.verify(value)`` method will send the ``CLOCk:EREFerence:MULTiplier?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CLOCk:EREFerence:MULTiplier value``
              command.

        SCPI Syntax:
            ```
            - CLOCk:EREFerence:MULTiplier <NR1>
            - CLOCk:EREFerence:MULTiplier?
            ```

        Info:
            - ``*RST`` sets this to 1.
        """
        return self._multiplier


class ClockEclockMultiplier(SCPICmdWrite, SCPICmdRead):
    """The ``CLOCk:ECLock:MULTiplier`` command.

    Description:
        - This command sets or returns the multiplier rate of the external clock.

    Usage:
        - Using the ``.query()`` method will send the ``CLOCk:ECLock:MULTiplier?`` query.
        - Using the ``.verify(value)`` method will send the ``CLOCk:ECLock:MULTiplier?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CLOCk:ECLock:MULTiplier value``
          command.

    SCPI Syntax:
        ```
        - CLOCk:ECLock:MULTiplier <NR1>
        - CLOCk:ECLock:MULTiplier?
        ```

    Info:
        - ``*RST`` sets this to 1.
    """


class ClockEclockFrequencyDetect(SCPICmdWriteNoArguments):
    """The ``CLOCk:ECLock:FREQuency:DETect`` command.

    Description:
        - This command detects the frequency of the signal applied to the Clock In connector and
          adjusts the system to use the signal. The frequency is detected once each time the command
          executes. An error message is generated if no frequency is detected or is out of range.

    Usage:
        - Using the ``.write()`` method will send the ``CLOCk:ECLock:FREQuency:DETect`` command.

    SCPI Syntax:
        ```
        - CLOCk:ECLock:FREQuency:DETect
        ```
    """


class ClockEclockFrequency(SCPICmdWrite, SCPICmdRead):
    """The ``CLOCk:ECLock:FREQuency`` command.

    Description:
        - This command sets or returns the expected frequency being provided by the external clock.

    Usage:
        - Using the ``.query()`` method will send the ``CLOCk:ECLock:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``CLOCk:ECLock:FREQuency?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CLOCk:ECLock:FREQuency value`` command.

    SCPI Syntax:
        ```
        - CLOCk:ECLock:FREQuency <NR3>
        - CLOCk:ECLock:FREQuency?
        ```

    Info:
        - ``*RST`` sets this to 6.25 GHz.

    Properties:
        - ``.detect``: The ``CLOCk:ECLock:FREQuency:DETect`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._detect = ClockEclockFrequencyDetect(device, f"{self._cmd_syntax}:DETect")

    @property
    def detect(self) -> ClockEclockFrequencyDetect:
        """Return the ``CLOCk:ECLock:FREQuency:DETect`` command.

        Description:
            - This command detects the frequency of the signal applied to the Clock In connector and
              adjusts the system to use the signal. The frequency is detected once each time the
              command executes. An error message is generated if no frequency is detected or is out
              of range.

        Usage:
            - Using the ``.write()`` method will send the ``CLOCk:ECLock:FREQuency:DETect`` command.

        SCPI Syntax:
            ```
            - CLOCk:ECLock:FREQuency:DETect
            ```
        """
        return self._detect


class ClockEclockDivider(SCPICmdWrite, SCPICmdRead):
    """The ``CLOCk:ECLock:DIVider`` command.

    Description:
        - This command sets or returns the divider rate for the external clock.

    Usage:
        - Using the ``.query()`` method will send the ``CLOCk:ECLock:DIVider?`` query.
        - Using the ``.verify(value)`` method will send the ``CLOCk:ECLock:DIVider?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CLOCk:ECLock:DIVider value`` command.

    SCPI Syntax:
        ```
        - CLOCk:ECLock:DIVider <NR1>
        - CLOCk:ECLock:DIVider?
        ```

    Info:
        - ``*RST`` sets this to 1.
    """


class ClockEclock(SCPICmdRead):
    """The ``CLOCk:ECLock`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CLOCk:ECLock?`` query.
        - Using the ``.verify(value)`` method will send the ``CLOCk:ECLock?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.divider``: The ``CLOCk:ECLock:DIVider`` command.
        - ``.frequency``: The ``CLOCk:ECLock:FREQuency`` command.
        - ``.multiplier``: The ``CLOCk:ECLock:MULTiplier`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._divider = ClockEclockDivider(device, f"{self._cmd_syntax}:DIVider")
        self._frequency = ClockEclockFrequency(device, f"{self._cmd_syntax}:FREQuency")
        self._multiplier = ClockEclockMultiplier(device, f"{self._cmd_syntax}:MULTiplier")

    @property
    def divider(self) -> ClockEclockDivider:
        """Return the ``CLOCk:ECLock:DIVider`` command.

        Description:
            - This command sets or returns the divider rate for the external clock.

        Usage:
            - Using the ``.query()`` method will send the ``CLOCk:ECLock:DIVider?`` query.
            - Using the ``.verify(value)`` method will send the ``CLOCk:ECLock:DIVider?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CLOCk:ECLock:DIVider value``
              command.

        SCPI Syntax:
            ```
            - CLOCk:ECLock:DIVider <NR1>
            - CLOCk:ECLock:DIVider?
            ```

        Info:
            - ``*RST`` sets this to 1.
        """
        return self._divider

    @property
    def frequency(self) -> ClockEclockFrequency:
        """Return the ``CLOCk:ECLock:FREQuency`` command.

        Description:
            - This command sets or returns the expected frequency being provided by the external
              clock.

        Usage:
            - Using the ``.query()`` method will send the ``CLOCk:ECLock:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``CLOCk:ECLock:FREQuency?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CLOCk:ECLock:FREQuency value``
              command.

        SCPI Syntax:
            ```
            - CLOCk:ECLock:FREQuency <NR3>
            - CLOCk:ECLock:FREQuency?
            ```

        Info:
            - ``*RST`` sets this to 6.25 GHz.

        Sub-properties:
            - ``.detect``: The ``CLOCk:ECLock:FREQuency:DETect`` command.
        """
        return self._frequency

    @property
    def multiplier(self) -> ClockEclockMultiplier:
        """Return the ``CLOCk:ECLock:MULTiplier`` command.

        Description:
            - This command sets or returns the multiplier rate of the external clock.

        Usage:
            - Using the ``.query()`` method will send the ``CLOCk:ECLock:MULTiplier?`` query.
            - Using the ``.verify(value)`` method will send the ``CLOCk:ECLock:MULTiplier?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CLOCk:ECLock:MULTiplier value``
              command.

        SCPI Syntax:
            ```
            - CLOCk:ECLock:MULTiplier <NR1>
            - CLOCk:ECLock:MULTiplier?
            ```

        Info:
            - ``*RST`` sets this to 1.
        """
        return self._multiplier


#  pylint: disable=too-many-instance-attributes
class Clock(SCPICmdRead):
    """The ``CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``CLOCk?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.eclock``: The ``CLOCk:ECLock`` command tree.
        - ``.ereference``: The ``CLOCk:EREFerence`` command tree.
        - ``.jitter``: The ``CLOCk:JITTer`` command.
        - ``.output``: The ``CLOCk:OUTPut`` command tree.
        - ``.phase``: The ``CLOCk:PHASe`` command tree.
        - ``.source``: The ``CLOCk:SOURce`` command.
        - ``.sout``: The ``CLOCk:SOUT`` command tree.
        - ``.srate``: The ``CLOCk:SRATe`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "CLOCk") -> None:
        super().__init__(device, cmd_syntax)
        self._eclock = ClockEclock(device, f"{self._cmd_syntax}:ECLock")
        self._ereference = ClockEreference(device, f"{self._cmd_syntax}:EREFerence")
        self._jitter = ClockJitter(device, f"{self._cmd_syntax}:JITTer")
        self._output = ClockOutput(device, f"{self._cmd_syntax}:OUTPut")
        self._phase = ClockPhase(device, f"{self._cmd_syntax}:PHASe")
        self._source = ClockSource(device, f"{self._cmd_syntax}:SOURce")
        self._sout = ClockSout(device, f"{self._cmd_syntax}:SOUT")
        self._srate = ClockSrate(device, f"{self._cmd_syntax}:SRATe")

    @property
    def eclock(self) -> ClockEclock:
        """Return the ``CLOCk:ECLock`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CLOCk:ECLock?`` query.
            - Using the ``.verify(value)`` method will send the ``CLOCk:ECLock?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.divider``: The ``CLOCk:ECLock:DIVider`` command.
            - ``.frequency``: The ``CLOCk:ECLock:FREQuency`` command.
            - ``.multiplier``: The ``CLOCk:ECLock:MULTiplier`` command.
        """
        return self._eclock

    @property
    def ereference(self) -> ClockEreference:
        """Return the ``CLOCk:EREFerence`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CLOCk:EREFerence?`` query.
            - Using the ``.verify(value)`` method will send the ``CLOCk:EREFerence?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.divider``: The ``CLOCk:EREFerence:DIVider`` command.
            - ``.frequency``: The ``CLOCk:EREFerence:FREQuency`` command.
            - ``.multiplier``: The ``CLOCk:EREFerence:MULTiplier`` command.
        """
        return self._ereference

    @property
    def jitter(self) -> ClockJitter:
        """Return the ``CLOCk:JITTer`` command.

        Description:
            - This command sets or returns the state (enabled or disabled) to apply or not apply
              jitter reduction to the internal system clock or the clock signal applied to the
              Reference In connector. When enabled, the chosen sample rate value will be adjusted to
              achieve the best performance.

        Usage:
            - Using the ``.write(value)`` method will send the ``CLOCk:JITTer value`` command.

        SCPI Syntax:
            ```
            - CLOCk:JITTer {0|1|OFF|ON}
            ```

        Info:
            - ``*RST`` sets this to 0.
        """
        return self._jitter

    @property
    def output(self) -> ClockOutput:
        """Return the ``CLOCk:OUTPut`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CLOCk:OUTPut?`` query.
            - Using the ``.verify(value)`` method will send the ``CLOCk:OUTPut?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.frequency``: The ``CLOCk:OUTPut:FREQuency`` command.
            - ``.state``: The ``CLOCk:OUTPut:STATe`` command.
        """
        return self._output

    @property
    def phase(self) -> ClockPhase:
        """Return the ``CLOCk:PHASe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CLOCk:PHASe?`` query.
            - Using the ``.verify(value)`` method will send the ``CLOCk:PHASe?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.adjust``: The ``CLOCk:PHASe:ADJust`` command tree.
        """
        return self._phase

    @property
    def source(self) -> ClockSource:
        """Return the ``CLOCk:SOURce`` command.

        Description:
            - This command sets or returns the source of the clock.

        Usage:
            - Using the ``.query()`` method will send the ``CLOCk:SOURce?`` query.
            - Using the ``.verify(value)`` method will send the ``CLOCk:SOURce?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CLOCk:SOURce value`` command.

        SCPI Syntax:
            ```
            - CLOCk:SOURce {INTernal|EFIXed|EVARiable|EXTernal}
            - CLOCk:SOURce?
            ```

        Info:
            - ``*RST`` sets this to INT.
        """
        return self._source

    @property
    def sout(self) -> ClockSout:
        """Return the ``CLOCk:SOUT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CLOCk:SOUT?`` query.
            - Using the ``.verify(value)`` method will send the ``CLOCk:SOUT?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``CLOCk:SOUT:STATe`` command.
        """
        return self._sout

    @property
    def srate(self) -> ClockSrate:
        r"""Return the ``CLOCk:SRATe`` command.

        Description:
            - This command sets or returns the sample rate for the clock. When ``CLOCk:SOURce`` is
              set to EXTernal, the maximum sample rate is: 4 \* External Clock In frequency
              (AWG70001)2 \* External Clock In frequency (AWG70002)

        Usage:
            - Using the ``.query()`` method will send the ``CLOCk:SRATe?`` query.
            - Using the ``.verify(value)`` method will send the ``CLOCk:SRATe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CLOCk:SRATe value`` command.

        SCPI Syntax:
            ```
            - CLOCk:SRATe <NRf>
            - CLOCk:SRATe?
            ```

        Info:
            - ``*RST`` sets this to the maximum value.
        """
        return self._srate
