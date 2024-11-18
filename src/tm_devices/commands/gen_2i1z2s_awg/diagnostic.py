"""The diagnostic commands module.

These commands are used in the following models:
AWG5200

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - DIAGnostic:ABORt
    - DIAGnostic:CATalog? [{ALL|<subsystem>}[,{ALL|<area>}]]
    - DIAGnostic:CONTrol:COUNt <NR1>
    - DIAGnostic:CONTrol:COUNt?
    - DIAGnostic:CONTrol:HALT {0|1|OFF|ON}
    - DIAGnostic:CONTrol:LOOP {ONCE|CONTinuous|COUNt}
    - DIAGnostic:CONTrol:LOOP?
    - DIAGnostic:DATA?
    - DIAGnostic:IMMediate
    - DIAGnostic:IMMediate?
    - DIAGnostic:LOG:CLEar
    - DIAGnostic:LOG:FAILuresonly {0|1|OFF|ON}
    - DIAGnostic:LOG:FAILuresonly?
    - DIAGnostic:LOG?
    - DIAGnostic:LOOPs?
    - DIAGnostic:RESult:TEMPerature? '<subsystem>'[,'<area>'[,'<test>']]
    - DIAGnostic:RESult:TIME? '<subsystem>'[,'<area>'[,'<test>']]
    - DIAGnostic:RESult? [{ALL|<path>}]
    - DIAGnostic:RUNNing?
    - DIAGnostic:SELect {ALL|<path>}
    - DIAGnostic:SELect:VERify? <subsystem>,<area>,<test>
    - DIAGnostic:STARt
    - DIAGnostic:STOP
    - DIAGnostic:STOP:STATe?
    - DIAGnostic:TYPE {NORMal|POST}
    - DIAGnostic:TYPE:CATalog?
    - DIAGnostic:TYPE?
    - DIAGnostic:UNSelect {ALL|<'subsystem'>,<'area'>,<'test'>}
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdReadWithArguments, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class DiagnosticUnselect(SCPICmdWrite):
    """The ``DIAGnostic:UNSelect`` command.

    Description:
        - This command unselects one or more tests of the current test list. Tests can be unselected
          by the keyword ALL, by 'subsystem', by 'area', or by 'test'. To unselect an 'area', the
          'subsystem' is required. To unselect a 'test' requires both the 'subsystem' and 'area'.

    Usage:
        - Using the ``.write(value)`` method will send the ``DIAGnostic:UNSelect value`` command.

    SCPI Syntax:
        ```
        - DIAGnostic:UNSelect {ALL|<'subsystem'>,<'area'>,<'test'>}
        ```
    """


class DiagnosticTypeCatalog(SCPICmdRead):
    """The ``DIAGnostic:TYPE:CATalog`` command.

    Description:
        - This command returns a list of diagnostic types available.

    Usage:
        - Using the ``.query()`` method will send the ``DIAGnostic:TYPE:CATalog?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAGnostic:TYPE:CATalog?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DIAGnostic:TYPE:CATalog?
        ```
    """


class DiagnosticType(SCPICmdWrite, SCPICmdRead):
    """The ``DIAGnostic:TYPE`` command.

    Description:
        - This command sets or returns the diagnostic type. The diagnostics work on a list of tests
          that support different types of testing. This sets the context for other commands such as
          selecting a test to run.

    Usage:
        - Using the ``.query()`` method will send the ``DIAGnostic:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAGnostic:TYPE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DIAGnostic:TYPE value`` command.

    SCPI Syntax:
        ```
        - DIAGnostic:TYPE {NORMal|POST}
        - DIAGnostic:TYPE?
        ```

    Info:
        - ``NORMal`` - Normal operating mode POST - Power On Self Test.
        - ``*RST`` sets this to NORM.

    Properties:
        - ``.catalog``: The ``DIAGnostic:TYPE:CATalog`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._catalog = DiagnosticTypeCatalog(device, f"{self._cmd_syntax}:CATalog")

    @property
    def catalog(self) -> DiagnosticTypeCatalog:
        """Return the ``DIAGnostic:TYPE:CATalog`` command.

        Description:
            - This command returns a list of diagnostic types available.

        Usage:
            - Using the ``.query()`` method will send the ``DIAGnostic:TYPE:CATalog?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAGnostic:TYPE:CATalog?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAGnostic:TYPE:CATalog?
            ```
        """
        return self._catalog


class DiagnosticStopState(SCPICmdRead):
    """The ``DIAGnostic:STOP:STATe`` command.

    Description:
        - This command returns the current state of diagnostic testing.

    Usage:
        - Using the ``.query()`` method will send the ``DIAGnostic:STOP:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAGnostic:STOP:STATe?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DIAGnostic:STOP:STATe?
        ```
    """


class DiagnosticStop(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``DIAGnostic:STOP`` command.

    Description:
        - This command stops the diagnostic tests from running, after the diagnostic test currently
          in progress completes. This also terminates diagnostic test looping.

    Usage:
        - Using the ``.write()`` method will send the ``DIAGnostic:STOP`` command.

    SCPI Syntax:
        ```
        - DIAGnostic:STOP
        ```

    Properties:
        - ``.state``: The ``DIAGnostic:STOP:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = DiagnosticStopState(device, f"{self._cmd_syntax}:STATe")

    @property
    def state(self) -> DiagnosticStopState:
        """Return the ``DIAGnostic:STOP:STATe`` command.

        Description:
            - This command returns the current state of diagnostic testing.

        Usage:
            - Using the ``.query()`` method will send the ``DIAGnostic:STOP:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAGnostic:STOP:STATe?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAGnostic:STOP:STATe?
            ```
        """
        return self._state


class DiagnosticStart(SCPICmdWriteNoArguments):
    """The ``DIAGnostic:STARt`` command.

    Description:
        - This command starts the execution of the selected set of diagnostic tests.

    Usage:
        - Using the ``.write()`` method will send the ``DIAGnostic:STARt`` command.

    SCPI Syntax:
        ```
        - DIAGnostic:STARt
        ```
    """


class DiagnosticSelectVerify(SCPICmdReadWithArguments):
    """The ``DIAGnostic:SELect:VERify`` command.

    Description:
        - This command returns selection status of one specific test. A specific test requires the
          'subsystem', 'area', and 'test'. This is context sensitive and is dependent on the type as
          set with the command ``DIAGNOSTIC:TYPE``.

    Usage:
        - Using the ``.query(argument)`` method will send the ``DIAGnostic:SELect:VERify? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``DIAGnostic:SELect:VERify? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.

    SCPI Syntax:
        ```
        - DIAGnostic:SELect:VERify? <subsystem>,<area>,<test>
        ```
    """


class DiagnosticSelect(SCPICmdWrite, SCPICmdRead):
    """The ``DIAGnostic:SELect`` command.

    Description:
        - This command (no query form) selects one or more tests of the current test list. Tests can
          be selected by the keyword ALL, by 'subsystem', by 'area', or by 'test'. The selection by
          'area' requires 'subsystem' and a 'test' requires both the 'subsystem' and 'area'. This
          command requires that ``ACTIVE:MODE`` is set to DIAGnostic. If not, the following error is
          generated: -300,'Device-specific error; Not in Diagnostics mode - ``diag:sel``
          ''Channel1''' If in the proper active of DIAGnostic, then an invalid string generates the
          following error: -220,'Parameter error; Invalid subsystem - ``diag:sel`` ''Channel2'''

    Usage:
        - Using the ``.write(value)`` method will send the ``DIAGnostic:SELect value`` command.

    SCPI Syntax:
        ```
        - DIAGnostic:SELect {ALL|<path>}
        ```

    Properties:
        - ``.verify``: The ``DIAGnostic:SELect:VERify`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._verify = DiagnosticSelectVerify(device, f"{self._cmd_syntax}:VERify")

    @property
    def verify_(self) -> DiagnosticSelectVerify:
        """Return the ``DIAGnostic:SELect:VERify`` command.

        Description:
            - This command returns selection status of one specific test. A specific test requires
              the 'subsystem', 'area', and 'test'. This is context sensitive and is dependent on the
              type as set with the command ``DIAGNOSTIC:TYPE``.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``DIAGnostic:SELect:VERify? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``DIAGnostic:SELect:VERify? argument`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAGnostic:SELect:VERify? <subsystem>,<area>,<test>
            ```
        """
        return self._verify


class DiagnosticRunning(SCPICmdRead):
    """The ``DIAGnostic:RUNNing`` command.

    Description:
        - This command returns the name of the subsystem, area, and test of the current diagnostic
          test. This command can be issued at any time.

    Usage:
        - Using the ``.query()`` method will send the ``DIAGnostic:RUNNing?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAGnostic:RUNNing?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DIAGnostic:RUNNing?
        ```
    """


class DiagnosticResultTime(SCPICmdReadWithArguments):
    """The ``DIAGnostic:RESult:TIME`` command.

    Description:
        - This command returns the time from the results of the last start of a set of selected
          tests. Time is returned as a date time string as in the following example of '3/14/2013
          ``10:19 AM``'. Time for an area or subsystem have the following requirements: The time
          only reflects the 'selected' tests. The 'selected' tests must have results of pass or
          fail. As an example, if 3 of the 4 tests in an area has been selected, then only those 3
          contribute to the 'area' result. If only 2 of the selected 3 have run and completed (a
          stop event occurred) then only those 2 contribute to the result. The time returned, which
          is associated with the highest temperature of any selected test, is returned when the
          results for more than one test is requested as in an area.

    Usage:
        - Using the ``.query(argument)`` method will send the ``DIAGnostic:RESult:TIME? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``DIAGnostic:RESult:TIME? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.

    SCPI Syntax:
        ```
        - DIAGnostic:RESult:TIME? '<subsystem>'[,'<area>'[,'<test>']]
        ```
    """


class DiagnosticResultTemperature(SCPICmdReadWithArguments):
    """The ``DIAGnostic:RESult:TEMPerature`` command.

    Description:
        - This command returns the temperature from the results of the last start of a set of
          selected tests. All temperatures will be in °C. Temperature for an area or subsystem have
          the following requirements. The temperature only reflects the 'selected' tests. The
          'selected' tests must have results of pass or fail. As an example, if 3 of the 4 tests in
          an area has been selected, then only those 3 contribute to the 'area' result. If only 2 of
          the selected 3 have run and completed (a stop event occurred) then only those 2 contribute
          to the result. The highest temperature is returned when the results for more than one test
          is requested (as in an area). The time will also be recorded for the highest temperature
          and may be found with the ``Diag:Result:Time?`` query.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``DIAGnostic:RESult:TEMPerature? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``DIAGnostic:RESult:TEMPerature? argument`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DIAGnostic:RESult:TEMPerature? '<subsystem>'[,'<area>'[,'<test>']]
        ```
    """


class DiagnosticResult(SCPICmdReadWithArguments):
    """The ``DIAGnostic:RESult`` command.

    Description:
        - This command returns the status about the results of the last start of a set of selected
          tests. An individual test result can have a status of Pass, Fail or Running. Status for an
          area or a subsystem have the following requirements: The results only reflect the
          'selected' tests. The selected tests have to have results of pass or fail or be in the
          running state. Only selected tests in an area or subsystem contribute to the result. As an
          example, if 3 of the 4 tests in an area has been selected, then only those 3 contribute to
          the 'area' result. If only 2 of the selected 3 have run and completed (a stop event
          occurred) then only those 2 contribute to the result. If all contributors have passed,
          then the result is passed. If any contributor has failed, then the result is failed. If
          any contributor is running, then the result is running.

    Usage:
        - Using the ``.query(argument)`` method will send the ``DIAGnostic:RESult? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``DIAGnostic:RESult? argument`` query and raise an AssertionError if the returned value
          does not match ``value``.

    SCPI Syntax:
        ```
        - DIAGnostic:RESult? [{ALL|<path>}]
        ```

    Properties:
        - ``.temperature``: The ``DIAGnostic:RESult:TEMPerature`` command.
        - ``.time``: The ``DIAGnostic:RESult:TIME`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._temperature = DiagnosticResultTemperature(device, f"{self._cmd_syntax}:TEMPerature")
        self._time = DiagnosticResultTime(device, f"{self._cmd_syntax}:TIME")

    @property
    def temperature(self) -> DiagnosticResultTemperature:
        """Return the ``DIAGnostic:RESult:TEMPerature`` command.

        Description:
            - This command returns the temperature from the results of the last start of a set of
              selected tests. All temperatures will be in °C. Temperature for an area or subsystem
              have the following requirements. The temperature only reflects the 'selected' tests.
              The 'selected' tests must have results of pass or fail. As an example, if 3 of the 4
              tests in an area has been selected, then only those 3 contribute to the 'area' result.
              If only 2 of the selected 3 have run and completed (a stop event occurred) then only
              those 2 contribute to the result. The highest temperature is returned when the results
              for more than one test is requested (as in an area). The time will also be recorded
              for the highest temperature and may be found with the ``Diag:Result:Time?`` query.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``DIAGnostic:RESult:TEMPerature? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``DIAGnostic:RESult:TEMPerature? argument`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAGnostic:RESult:TEMPerature? '<subsystem>'[,'<area>'[,'<test>']]
            ```
        """
        return self._temperature

    @property
    def time(self) -> DiagnosticResultTime:
        """Return the ``DIAGnostic:RESult:TIME`` command.

        Description:
            - This command returns the time from the results of the last start of a set of selected
              tests. Time is returned as a date time string as in the following example of
              '3/14/2013 ``10:19 AM``'. Time for an area or subsystem have the following
              requirements: The time only reflects the 'selected' tests. The 'selected' tests must
              have results of pass or fail. As an example, if 3 of the 4 tests in an area has been
              selected, then only those 3 contribute to the 'area' result. If only 2 of the selected
              3 have run and completed (a stop event occurred) then only those 2 contribute to the
              result. The time returned, which is associated with the highest temperature of any
              selected test, is returned when the results for more than one test is requested as in
              an area.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``DIAGnostic:RESult:TIME? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``DIAGnostic:RESult:TIME? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAGnostic:RESult:TIME? '<subsystem>'[,'<area>'[,'<test>']]
            ```
        """
        return self._time


class DiagnosticLoops(SCPICmdRead):
    """The ``DIAGnostic:LOOPs`` command.

    Description:
        - This command returns the number of times that the selected diagnostics set was completed
          during the current running or the last diagnostic running of the set. The current loop is
          reset after every start. This command can be issued while diagnostics are still in
          progress.

    Usage:
        - Using the ``.query()`` method will send the ``DIAGnostic:LOOPs?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAGnostic:LOOPs?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DIAGnostic:LOOPs?
        ```
    """


class DiagnosticLogFailuresonly(SCPICmdWrite, SCPICmdRead):
    """The ``DIAGnostic:LOG:FAILuresonly`` command.

    Description:
        - This command sets or returns the flag that controls the amount of result information saved
          into the diagnostic log. This controls all tests that pass or fail or only tests that
          fail. The flag must be set before starting the diagnostic tests to obtain the expected
          data.

    Usage:
        - Using the ``.query()`` method will send the ``DIAGnostic:LOG:FAILuresonly?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAGnostic:LOG:FAILuresonly?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DIAGnostic:LOG:FAILuresonly value``
          command.

    SCPI Syntax:
        ```
        - DIAGnostic:LOG:FAILuresonly {0|1|OFF|ON}
        - DIAGnostic:LOG:FAILuresonly?
        ```

    Info:
        - ``*RST`` sets this to 0.
    """


class DiagnosticLogClear(SCPICmdWriteNoArguments):
    """The ``DIAGnostic:LOG:CLEar`` command.

    Description:
        - This command clears the diagnostics results log.

    Usage:
        - Using the ``.write()`` method will send the ``DIAGnostic:LOG:CLEar`` command.

    SCPI Syntax:
        ```
        - DIAGnostic:LOG:CLEar
        ```
    """


class DiagnosticLog(SCPICmdRead):
    """The ``DIAGnostic:LOG`` command.

    Description:
        - This command returns a string of continuous concatenated test results. The start time is
          recorded for each of the selected tests. This command can be issued at any time including
          while diagnostics are in progress.

    Usage:
        - Using the ``.query()`` method will send the ``DIAGnostic:LOG?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAGnostic:LOG?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DIAGnostic:LOG?
        ```

    Properties:
        - ``.clear``: The ``DIAGnostic:LOG:CLEar`` command.
        - ``.failuresonly``: The ``DIAGnostic:LOG:FAILuresonly`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._clear = DiagnosticLogClear(device, f"{self._cmd_syntax}:CLEar")
        self._failuresonly = DiagnosticLogFailuresonly(device, f"{self._cmd_syntax}:FAILuresonly")

    @property
    def clear(self) -> DiagnosticLogClear:
        """Return the ``DIAGnostic:LOG:CLEar`` command.

        Description:
            - This command clears the diagnostics results log.

        Usage:
            - Using the ``.write()`` method will send the ``DIAGnostic:LOG:CLEar`` command.

        SCPI Syntax:
            ```
            - DIAGnostic:LOG:CLEar
            ```
        """
        return self._clear

    @property
    def failuresonly(self) -> DiagnosticLogFailuresonly:
        """Return the ``DIAGnostic:LOG:FAILuresonly`` command.

        Description:
            - This command sets or returns the flag that controls the amount of result information
              saved into the diagnostic log. This controls all tests that pass or fail or only tests
              that fail. The flag must be set before starting the diagnostic tests to obtain the
              expected data.

        Usage:
            - Using the ``.query()`` method will send the ``DIAGnostic:LOG:FAILuresonly?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAGnostic:LOG:FAILuresonly?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DIAGnostic:LOG:FAILuresonly value``
              command.

        SCPI Syntax:
            ```
            - DIAGnostic:LOG:FAILuresonly {0|1|OFF|ON}
            - DIAGnostic:LOG:FAILuresonly?
            ```

        Info:
            - ``*RST`` sets this to 0.
        """
        return self._failuresonly


class DiagnosticImmediate(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``DIAGnostic:IMMediate`` command.

    Description:
        - This command executes all of the NORMal diagnostic tests. The query form of this command
          executes all of the NORMal diagnostics and returns the results in the form of numeric of
          values of 0 for no errors or -330 for one or more tests failed. This changes the active
          mode to DIAGnostic, if necessary, and returns back to the original active mode when done.
          This makes a single pass of all of the NORMal diagnostics.

    Usage:
        - Using the ``.query()`` method will send the ``DIAGnostic:IMMediate?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAGnostic:IMMediate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``DIAGnostic:IMMediate`` command.

    SCPI Syntax:
        ```
        - DIAGnostic:IMMediate
        - DIAGnostic:IMMediate?
        ```
    """


class DiagnosticData(SCPICmdRead):
    """The ``DIAGnostic:DATA`` command.

    Description:
        - This command returns the results of last executed tests for the NORMal diagnostic type in
          the form of a numeric value of 0 for no errors or -330 for one or more tests failed.
          Additional error details can be found by using the subsystem, area, and test queries such
          as ``DIAGnostic:RESult?`` <subsystem>[,<area>[,<test>]].

    Usage:
        - Using the ``.query()`` method will send the ``DIAGnostic:DATA?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAGnostic:DATA?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DIAGnostic:DATA?
        ```
    """


class DiagnosticControlLoop(SCPICmdWrite, SCPICmdRead):
    """The ``DIAGnostic:CONTrol:LOOP`` command.

    Description:
        - This command sets or returns whether the next start of diagnostics runs once, runs
          continuous loops, or loops for a number times for the selected set of tests. All loops may
          be affected by the ``DIAGNOSTIC:CONTROL:HALT`` command which determines what happens if an
          error occurs.

    Usage:
        - Using the ``.query()`` method will send the ``DIAGnostic:CONTrol:LOOP?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAGnostic:CONTrol:LOOP?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DIAGnostic:CONTrol:LOOP value``
          command.

    SCPI Syntax:
        ```
        - DIAGnostic:CONTrol:LOOP {ONCE|CONTinuous|COUNt}
        - DIAGnostic:CONTrol:LOOP?
        ```

    Info:
        - ``ONCE`` disables the loop function, causes the execution of selected test(s), which may
          be one or more, of diagnostics once and then halt.
        - ``CONTinuous`` enables the loop function, causing the execution of diagnostics to
          continuously loop.
        - ``COUNt`` enables the loop function, causing the execution of diagnostics to loop for a
          predefined count. Exit of the loop happens when the predefined loop count occurs.
        - ``*RST`` sets this to ONCE.
    """


class DiagnosticControlHalt(SCPICmdWrite):
    """The ``DIAGnostic:CONTrol:HALT`` command.

    Description:
        - This command sets or returns whether the next execution of diagnostics looping stops on
          the first diagnostic failure that occurs or continues to loop on the selected set of
          diagnostic functions.

    Usage:
        - Using the ``.write(value)`` method will send the ``DIAGnostic:CONTrol:HALT value``
          command.

    SCPI Syntax:
        ```
        - DIAGnostic:CONTrol:HALT {0|1|OFF|ON}
        ```

    Info:
        - ``*RST`` sets this to 0.
    """


class DiagnosticControlCount(SCPICmdWrite, SCPICmdRead):
    """The ``DIAGnostic:CONTrol:COUNt`` command.

    Description:
        - This command sets or returns the number of loop counts used when the loop mode is set to
          COUNt. See ``DIAGNOSTIC:CONTROL:LOOP``.

    Usage:
        - Using the ``.query()`` method will send the ``DIAGnostic:CONTrol:COUNt?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAGnostic:CONTrol:COUNt?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DIAGnostic:CONTrol:COUNt value``
          command.

    SCPI Syntax:
        ```
        - DIAGnostic:CONTrol:COUNt <NR1>
        - DIAGnostic:CONTrol:COUNt?
        ```

    Info:
        - ``*RST`` sets this to 0.
    """


class DiagnosticControl(SCPICmdRead):
    """The ``DIAGnostic:CONTrol`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DIAGnostic:CONTrol?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAGnostic:CONTrol?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.count``: The ``DIAGnostic:CONTrol:COUNt`` command.
        - ``.halt``: The ``DIAGnostic:CONTrol:HALT`` command.
        - ``.loop``: The ``DIAGnostic:CONTrol:LOOP`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._count = DiagnosticControlCount(device, f"{self._cmd_syntax}:COUNt")
        self._halt = DiagnosticControlHalt(device, f"{self._cmd_syntax}:HALT")
        self._loop = DiagnosticControlLoop(device, f"{self._cmd_syntax}:LOOP")

    @property
    def count(self) -> DiagnosticControlCount:
        """Return the ``DIAGnostic:CONTrol:COUNt`` command.

        Description:
            - This command sets or returns the number of loop counts used when the loop mode is set
              to COUNt. See ``DIAGNOSTIC:CONTROL:LOOP``.

        Usage:
            - Using the ``.query()`` method will send the ``DIAGnostic:CONTrol:COUNt?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAGnostic:CONTrol:COUNt?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DIAGnostic:CONTrol:COUNt value``
              command.

        SCPI Syntax:
            ```
            - DIAGnostic:CONTrol:COUNt <NR1>
            - DIAGnostic:CONTrol:COUNt?
            ```

        Info:
            - ``*RST`` sets this to 0.
        """
        return self._count

    @property
    def halt(self) -> DiagnosticControlHalt:
        """Return the ``DIAGnostic:CONTrol:HALT`` command.

        Description:
            - This command sets or returns whether the next execution of diagnostics looping stops
              on the first diagnostic failure that occurs or continues to loop on the selected set
              of diagnostic functions.

        Usage:
            - Using the ``.write(value)`` method will send the ``DIAGnostic:CONTrol:HALT value``
              command.

        SCPI Syntax:
            ```
            - DIAGnostic:CONTrol:HALT {0|1|OFF|ON}
            ```

        Info:
            - ``*RST`` sets this to 0.
        """
        return self._halt

    @property
    def loop(self) -> DiagnosticControlLoop:
        """Return the ``DIAGnostic:CONTrol:LOOP`` command.

        Description:
            - This command sets or returns whether the next start of diagnostics runs once, runs
              continuous loops, or loops for a number times for the selected set of tests. All loops
              may be affected by the ``DIAGNOSTIC:CONTROL:HALT`` command which determines what
              happens if an error occurs.

        Usage:
            - Using the ``.query()`` method will send the ``DIAGnostic:CONTrol:LOOP?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAGnostic:CONTrol:LOOP?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DIAGnostic:CONTrol:LOOP value``
              command.

        SCPI Syntax:
            ```
            - DIAGnostic:CONTrol:LOOP {ONCE|CONTinuous|COUNt}
            - DIAGnostic:CONTrol:LOOP?
            ```

        Info:
            - ``ONCE`` disables the loop function, causes the execution of selected test(s), which
              may be one or more, of diagnostics once and then halt.
            - ``CONTinuous`` enables the loop function, causing the execution of diagnostics to
              continuously loop.
            - ``COUNt`` enables the loop function, causing the execution of diagnostics to loop for
              a predefined count. Exit of the loop happens when the predefined loop count occurs.
            - ``*RST`` sets this to ONCE.
        """
        return self._loop


class DiagnosticCatalog(SCPICmdReadWithArguments):
    """The ``DIAGnostic:CATalog`` command.

    Description:
        - This command returns the list of all diagnostic tests per selected type per subsystems,
          areas, or ALL. All tests are grouped by areas. All areas are grouped by subsystems. The
          available subsystems, areas, and tests depend on the type of testing (such as POST only or
          Full diagnostics). The selected type is set with the command ``DIAGNOSTIC:TYPE``.

    Usage:
        - Using the ``.query(argument)`` method will send the ``DIAGnostic:CATalog? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``DIAGnostic:CATalog? argument`` query and raise an AssertionError if the returned value
          does not match ``value``.

    SCPI Syntax:
        ```
        - DIAGnostic:CATalog? [{ALL|<subsystem>}[,{ALL|<area>}]]
        ```
    """


class DiagnosticAbort(SCPICmdWriteNoArguments):
    """The ``DIAGnostic:ABORt`` command.

    Description:
        - This command attempts to stop the current diagnostic test and stops the execution of any
          additional selected tests. This may result in loss of logging information collected for
          the current test that responds to the abort event.

    Usage:
        - Using the ``.write()`` method will send the ``DIAGnostic:ABORt`` command.

    SCPI Syntax:
        ```
        - DIAGnostic:ABORt
        ```
    """


#  pylint: disable=too-many-instance-attributes
class Diagnostic(SCPICmdRead):
    """The ``DIAGnostic`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DIAGnostic?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAGnostic?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.abort``: The ``DIAGnostic:ABORt`` command.
        - ``.catalog``: The ``DIAGnostic:CATalog`` command.
        - ``.control``: The ``DIAGnostic:CONTrol`` command tree.
        - ``.data``: The ``DIAGnostic:DATA`` command.
        - ``.log``: The ``DIAGnostic:LOG`` command.
        - ``.loops``: The ``DIAGnostic:LOOPs`` command.
        - ``.result``: The ``DIAGnostic:RESult`` command.
        - ``.running``: The ``DIAGnostic:RUNNing`` command.
        - ``.select``: The ``DIAGnostic:SELect`` command.
        - ``.start``: The ``DIAGnostic:STARt`` command.
        - ``.stop``: The ``DIAGnostic:STOP`` command.
        - ``.type``: The ``DIAGnostic:TYPE`` command.
        - ``.unselect``: The ``DIAGnostic:UNSelect`` command.
        - ``.immediate``: The ``DIAGnostic:IMMediate`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "DIAGnostic"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._abort = DiagnosticAbort(device, f"{self._cmd_syntax}:ABORt")
        self._catalog = DiagnosticCatalog(device, f"{self._cmd_syntax}:CATalog")
        self._control = DiagnosticControl(device, f"{self._cmd_syntax}:CONTrol")
        self._data = DiagnosticData(device, f"{self._cmd_syntax}:DATA")
        self._log = DiagnosticLog(device, f"{self._cmd_syntax}:LOG")
        self._loops = DiagnosticLoops(device, f"{self._cmd_syntax}:LOOPs")
        self._result = DiagnosticResult(device, f"{self._cmd_syntax}:RESult")
        self._running = DiagnosticRunning(device, f"{self._cmd_syntax}:RUNNing")
        self._select = DiagnosticSelect(device, f"{self._cmd_syntax}:SELect")
        self._start = DiagnosticStart(device, f"{self._cmd_syntax}:STARt")
        self._stop = DiagnosticStop(device, f"{self._cmd_syntax}:STOP")
        self._type = DiagnosticType(device, f"{self._cmd_syntax}:TYPE")
        self._unselect = DiagnosticUnselect(device, f"{self._cmd_syntax}:UNSelect")
        self._immediate = DiagnosticImmediate(device, f"{self._cmd_syntax}:IMMediate")

    @property
    def abort(self) -> DiagnosticAbort:
        """Return the ``DIAGnostic:ABORt`` command.

        Description:
            - This command attempts to stop the current diagnostic test and stops the execution of
              any additional selected tests. This may result in loss of logging information
              collected for the current test that responds to the abort event.

        Usage:
            - Using the ``.write()`` method will send the ``DIAGnostic:ABORt`` command.

        SCPI Syntax:
            ```
            - DIAGnostic:ABORt
            ```
        """
        return self._abort

    @property
    def catalog(self) -> DiagnosticCatalog:
        """Return the ``DIAGnostic:CATalog`` command.

        Description:
            - This command returns the list of all diagnostic tests per selected type per
              subsystems, areas, or ALL. All tests are grouped by areas. All areas are grouped by
              subsystems. The available subsystems, areas, and tests depend on the type of testing
              (such as POST only or Full diagnostics). The selected type is set with the command
              ``DIAGNOSTIC:TYPE``.

        Usage:
            - Using the ``.query(argument)`` method will send the ``DIAGnostic:CATalog? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``DIAGnostic:CATalog? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAGnostic:CATalog? [{ALL|<subsystem>}[,{ALL|<area>}]]
            ```
        """
        return self._catalog

    @property
    def control(self) -> DiagnosticControl:
        """Return the ``DIAGnostic:CONTrol`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DIAGnostic:CONTrol?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAGnostic:CONTrol?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.count``: The ``DIAGnostic:CONTrol:COUNt`` command.
            - ``.halt``: The ``DIAGnostic:CONTrol:HALT`` command.
            - ``.loop``: The ``DIAGnostic:CONTrol:LOOP`` command.
        """
        return self._control

    @property
    def data(self) -> DiagnosticData:
        """Return the ``DIAGnostic:DATA`` command.

        Description:
            - This command returns the results of last executed tests for the NORMal diagnostic type
              in the form of a numeric value of 0 for no errors or -330 for one or more tests
              failed. Additional error details can be found by using the subsystem, area, and test
              queries such as ``DIAGnostic:RESult?`` <subsystem>[,<area>[,<test>]].

        Usage:
            - Using the ``.query()`` method will send the ``DIAGnostic:DATA?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAGnostic:DATA?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAGnostic:DATA?
            ```
        """
        return self._data

    @property
    def log(self) -> DiagnosticLog:
        """Return the ``DIAGnostic:LOG`` command.

        Description:
            - This command returns a string of continuous concatenated test results. The start time
              is recorded for each of the selected tests. This command can be issued at any time
              including while diagnostics are in progress.

        Usage:
            - Using the ``.query()`` method will send the ``DIAGnostic:LOG?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAGnostic:LOG?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAGnostic:LOG?
            ```

        Sub-properties:
            - ``.clear``: The ``DIAGnostic:LOG:CLEar`` command.
            - ``.failuresonly``: The ``DIAGnostic:LOG:FAILuresonly`` command.
        """
        return self._log

    @property
    def loops(self) -> DiagnosticLoops:
        """Return the ``DIAGnostic:LOOPs`` command.

        Description:
            - This command returns the number of times that the selected diagnostics set was
              completed during the current running or the last diagnostic running of the set. The
              current loop is reset after every start. This command can be issued while diagnostics
              are still in progress.

        Usage:
            - Using the ``.query()`` method will send the ``DIAGnostic:LOOPs?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAGnostic:LOOPs?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAGnostic:LOOPs?
            ```
        """
        return self._loops

    @property
    def result(self) -> DiagnosticResult:
        """Return the ``DIAGnostic:RESult`` command.

        Description:
            - This command returns the status about the results of the last start of a set of
              selected tests. An individual test result can have a status of Pass, Fail or Running.
              Status for an area or a subsystem have the following requirements: The results only
              reflect the 'selected' tests. The selected tests have to have results of pass or fail
              or be in the running state. Only selected tests in an area or subsystem contribute to
              the result. As an example, if 3 of the 4 tests in an area has been selected, then only
              those 3 contribute to the 'area' result. If only 2 of the selected 3 have run and
              completed (a stop event occurred) then only those 2 contribute to the result. If all
              contributors have passed, then the result is passed. If any contributor has failed,
              then the result is failed. If any contributor is running, then the result is running.

        Usage:
            - Using the ``.query(argument)`` method will send the ``DIAGnostic:RESult? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``DIAGnostic:RESult? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAGnostic:RESult? [{ALL|<path>}]
            ```

        Sub-properties:
            - ``.temperature``: The ``DIAGnostic:RESult:TEMPerature`` command.
            - ``.time``: The ``DIAGnostic:RESult:TIME`` command.
        """
        return self._result

    @property
    def running(self) -> DiagnosticRunning:
        """Return the ``DIAGnostic:RUNNing`` command.

        Description:
            - This command returns the name of the subsystem, area, and test of the current
              diagnostic test. This command can be issued at any time.

        Usage:
            - Using the ``.query()`` method will send the ``DIAGnostic:RUNNing?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAGnostic:RUNNing?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAGnostic:RUNNing?
            ```
        """
        return self._running

    @property
    def select(self) -> DiagnosticSelect:
        """Return the ``DIAGnostic:SELect`` command.

        Description:
            - This command (no query form) selects one or more tests of the current test list. Tests
              can be selected by the keyword ALL, by 'subsystem', by 'area', or by 'test'. The
              selection by 'area' requires 'subsystem' and a 'test' requires both the 'subsystem'
              and 'area'. This command requires that ``ACTIVE:MODE`` is set to DIAGnostic. If not,
              the following error is generated: -300,'Device-specific error; Not in Diagnostics mode
              - ``diag:sel`` ''Channel1''' If in the proper active of DIAGnostic, then an invalid
              string generates the following error: -220,'Parameter error; Invalid subsystem -
              ``diag:sel`` ''Channel2'''

        Usage:
            - Using the ``.write(value)`` method will send the ``DIAGnostic:SELect value`` command.

        SCPI Syntax:
            ```
            - DIAGnostic:SELect {ALL|<path>}
            ```

        Sub-properties:
            - ``.verify``: The ``DIAGnostic:SELect:VERify`` command.
        """
        return self._select

    @property
    def start(self) -> DiagnosticStart:
        """Return the ``DIAGnostic:STARt`` command.

        Description:
            - This command starts the execution of the selected set of diagnostic tests.

        Usage:
            - Using the ``.write()`` method will send the ``DIAGnostic:STARt`` command.

        SCPI Syntax:
            ```
            - DIAGnostic:STARt
            ```
        """
        return self._start

    @property
    def stop(self) -> DiagnosticStop:
        """Return the ``DIAGnostic:STOP`` command.

        Description:
            - This command stops the diagnostic tests from running, after the diagnostic test
              currently in progress completes. This also terminates diagnostic test looping.

        Usage:
            - Using the ``.write()`` method will send the ``DIAGnostic:STOP`` command.

        SCPI Syntax:
            ```
            - DIAGnostic:STOP
            ```

        Sub-properties:
            - ``.state``: The ``DIAGnostic:STOP:STATe`` command.
        """
        return self._stop

    @property
    def type(self) -> DiagnosticType:
        """Return the ``DIAGnostic:TYPE`` command.

        Description:
            - This command sets or returns the diagnostic type. The diagnostics work on a list of
              tests that support different types of testing. This sets the context for other
              commands such as selecting a test to run.

        Usage:
            - Using the ``.query()`` method will send the ``DIAGnostic:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAGnostic:TYPE?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DIAGnostic:TYPE value`` command.

        SCPI Syntax:
            ```
            - DIAGnostic:TYPE {NORMal|POST}
            - DIAGnostic:TYPE?
            ```

        Info:
            - ``NORMal`` - Normal operating mode POST - Power On Self Test.
            - ``*RST`` sets this to NORM.

        Sub-properties:
            - ``.catalog``: The ``DIAGnostic:TYPE:CATalog`` command.
        """
        return self._type

    @property
    def unselect(self) -> DiagnosticUnselect:
        """Return the ``DIAGnostic:UNSelect`` command.

        Description:
            - This command unselects one or more tests of the current test list. Tests can be
              unselected by the keyword ALL, by 'subsystem', by 'area', or by 'test'. To unselect an
              'area', the 'subsystem' is required. To unselect a 'test' requires both the
              'subsystem' and 'area'.

        Usage:
            - Using the ``.write(value)`` method will send the ``DIAGnostic:UNSelect value``
              command.

        SCPI Syntax:
            ```
            - DIAGnostic:UNSelect {ALL|<'subsystem'>,<'area'>,<'test'>}
            ```
        """
        return self._unselect

    @property
    def immediate(self) -> DiagnosticImmediate:
        """Return the ``DIAGnostic:IMMediate`` command.

        Description:
            - This command executes all of the NORMal diagnostic tests. The query form of this
              command executes all of the NORMal diagnostics and returns the results in the form of
              numeric of values of 0 for no errors or -330 for one or more tests failed. This
              changes the active mode to DIAGnostic, if necessary, and returns back to the original
              active mode when done. This makes a single pass of all of the NORMal diagnostics.

        Usage:
            - Using the ``.query()`` method will send the ``DIAGnostic:IMMediate?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAGnostic:IMMediate?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``DIAGnostic:IMMediate`` command.

        SCPI Syntax:
            ```
            - DIAGnostic:IMMediate
            - DIAGnostic:IMMediate?
            ```
        """
        return self._immediate
