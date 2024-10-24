"""The test commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - TEST <QString>
    - TEST:RESults:VERBose?
    - TEST:RESults?
    - TEST:STOP
    - TEST?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class TestStop(SCPICmdWriteNoArguments):
    """The ``TEST:STOP`` command.

    Description:
        - This command (no query form) causes test (or diagnostics) execution to terminate at the
          end of the next low-level test. This command is equivalent to selecting Instrument
          Diagnostics from the Utilities menu and then clicking Abort.

    Usage:
        - Using the ``.write()`` method will send the ``TEST:STOP`` command.

    SCPI Syntax:
        ```
        - TEST:STOP
        ```
    """


class TestResultsVerbose(SCPICmdRead):
    """The ``TEST:RESults:VERBose`` command.

    Description:
        - This query-only command returns a more explanatory message about the results of the last
          TEST execution than the ``TEST:RESULTS`` query. This command is equivalent to selecting
          Instrument Diagnostics from the Utilities menu and then clicking the Error Log button.

    Usage:
        - Using the ``.query()`` method will send the ``TEST:RESults:VERBose?`` query.
        - Using the ``.verify(value)`` method will send the ``TEST:RESults:VERBose?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TEST:RESults:VERBose?
        ```
    """


class TestResults(SCPICmdRead):
    """The ``TEST:RESults`` command.

    Description:
        - This query-only command returns an abbreviated status about the results of the last TEST
          execution. This command is equivalent to selecting Instrument Diagnostics from the
          Utilities menu and then reviewing the Diagnostic Status.

    Usage:
        - Using the ``.query()`` method will send the ``TEST:RESults?`` query.
        - Using the ``.verify(value)`` method will send the ``TEST:RESults?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TEST:RESults?
        ```

    Properties:
        - ``.verbose``: The ``TEST:RESults:VERBose`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._verbose = TestResultsVerbose(device, f"{self._cmd_syntax}:VERBose")

    @property
    def verbose(self) -> TestResultsVerbose:
        """Return the ``TEST:RESults:VERBose`` command.

        Description:
            - This query-only command returns a more explanatory message about the results of the
              last TEST execution than the ``TEST:RESULTS`` query. This command is equivalent to
              selecting Instrument Diagnostics from the Utilities menu and then clicking the Error
              Log button.

        Usage:
            - Using the ``.query()`` method will send the ``TEST:RESults:VERBose?`` query.
            - Using the ``.verify(value)`` method will send the ``TEST:RESults:VERBose?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TEST:RESults:VERBose?
            ```
        """
        return self._verbose


class Test(SCPICmdWrite, SCPICmdRead):
    """The ``TEST`` command.

    Description:
        - This command provides the ability to select and execute an item at any level of the test
          hierarchy (Test, Area or Subsystem). The query returns the last command sent. This command
          is equivalent to selecting Instrument Diagnostics from the Utilities menu, choosing a test
          and then pressing Run.

    Usage:
        - Using the ``.query()`` method will send the ``TEST?`` query.
        - Using the ``.verify(value)`` method will send the ``TEST?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TEST value`` command.

    SCPI Syntax:
        ```
        - TEST <QString>
        - TEST?
        ```

    Info:
        - ``<QString>`` sets the test ID, which ranges from 0 through 3 characters. If no test ID is
          specified, all available diagnostics are executed.

    Properties:
        - ``.results``: The ``TEST:RESults`` command.
        - ``.stop``: The ``TEST:STOP`` command.
    """

    _WRAP_ARG_WITH_QUOTES = True

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "TEST") -> None:
        super().__init__(device, cmd_syntax)
        self._results = TestResults(device, f"{self._cmd_syntax}:RESults")
        self._stop = TestStop(device, f"{self._cmd_syntax}:STOP")

    @property
    def results(self) -> TestResults:
        """Return the ``TEST:RESults`` command.

        Description:
            - This query-only command returns an abbreviated status about the results of the last
              TEST execution. This command is equivalent to selecting Instrument Diagnostics from
              the Utilities menu and then reviewing the Diagnostic Status.

        Usage:
            - Using the ``.query()`` method will send the ``TEST:RESults?`` query.
            - Using the ``.verify(value)`` method will send the ``TEST:RESults?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TEST:RESults?
            ```

        Sub-properties:
            - ``.verbose``: The ``TEST:RESults:VERBose`` command.
        """
        return self._results

    @property
    def stop(self) -> TestStop:
        """Return the ``TEST:STOP`` command.

        Description:
            - This command (no query form) causes test (or diagnostics) execution to terminate at
              the end of the next low-level test. This command is equivalent to selecting Instrument
              Diagnostics from the Utilities menu and then clicking Abort.

        Usage:
            - Using the ``.write()`` method will send the ``TEST:STOP`` command.

        SCPI Syntax:
            ```
            - TEST:STOP
            ```
        """
        return self._stop
