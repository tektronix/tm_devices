"""The diag commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - DIAg:CONTROL:HALT {ON|OFF|<NR1>}
    - DIAg:CONTROL:HALT?
    - DIAg:CONTROL:LOOP {ON|OFF|<NR1>}
    - DIAg:CONTROL:LOOP?
    - DIAg:EXECUTE
    - DIAg:FAILURES:CLEAR {ON|OFF|<NR1>}
    - DIAg:FAILURES:CLEAR?
    - DIAg:ITEM:FAILURES? <NR1>
    - DIAg:ITEM:NAMe? <NR1>
    - DIAg:ITEM:RESULT? <NR1>
    - DIAg:ITEM:SUBITEMS? <NR1>
    - DIAg:ITEM? <NR1>
    - DIAg:LEVEL {AREA|SUBSYS|TEST}
    - DIAg:LEVEL?
    - DIAg:LOOPS?
    - DIAg:NAMe:AREA?
    - DIAg:NAMe:SUBSYS?
    - DIAg:NAMe:TEST?
    - DIAg:NAMe?
    - DIAg:NUMITEMS?
    - DIAg:RESults:VERBose?
    - DIAg:RESults?
    - DIAg:SELect:ALL ALL
    - DIAg:SELect:AREA <NR1>
    - DIAg:SELect:AREA?
    - DIAg:SELect:LAST <NR1>
    - DIAg:SELect:LAST?
    - DIAg:SELect:SUBSYS <NR1>
    - DIAg:SELect:SUBSYS?
    - DIAg:SELect:TEST <NR1>
    - DIAg:SELect:TEST?
    - DIAg:STATE {<NR1>|EXECUTE|ON|OFF}
    - DIAg:STATE?
    - DIAg:STOP
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdReadWithArguments, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class DiagStop(SCPICmdWriteNoArguments):
    """The ``DIAg:STOP`` command.

    Description:
        - This command (no query form) causes diagnostics (or test) execution to terminate at the
          end of the next low-level test. This command is equivalent to selecting Instrument
          Diagnostics from the Utilities menu and then clicking Abort.

    Usage:
        - Using the ``.write()`` method will send the ``DIAg:STOP`` command.

    SCPI Syntax:
        ```
        - DIAg:STOP
        ```
    """


class DiagState(SCPICmdWrite, SCPICmdRead):
    """The ``DIAg:STATE`` command.

    Description:
        - This command changes the instrument operating state. Depending on the argument,
          diagnostics capabilities are either turned on or off. This command is equivalent to
          opening the ``DIAg:STATE`` dialog (ON) or closing it (OFF).

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DIAg:STATE value`` command.

    SCPI Syntax:
        ```
        - DIAg:STATE {<NR1>|EXECUTE|ON|OFF}
        - DIAg:STATE?
        ```

    Info:
        - ``<NR1>`` = 0 disables diagnostics capabilities and returns the instrument to a normal
          operating state; any other value enables diagnostics.
        - ``EXECUTE`` starts execution of the diagnostics.
        - ``ON`` puts the instrument into the state in which diagnostics can be run. This argument
          is thrown automatically if the ``DIAG:EXECUTE`` command is executed.
        - ``OFF`` disables diagnostics capabilities and returns the instrument to a normal operating
          state.
    """


class DiagSelectTest(SCPICmdWrite, SCPICmdRead):
    """The ``DIAg:SELect:TEST`` command.

    Description:
        - This command selects or queries one of the available tests. This command is equivalent to
          selecting Instrument Diagnostics from the Utilities menu and then choosing a Test from the
          drop-down list.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:SELect:TEST?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:SELect:TEST?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DIAg:SELect:TEST value`` command.

    SCPI Syntax:
        ```
        - DIAg:SELect:TEST <NR1>
        - DIAg:SELect:TEST?
        ```

    Info:
        - ``<NR1>`` selects a test by number, which can range from 0 (zero selects ALL) through 15
          (as limited by the return from ``DIAG:NUMITEMS``).
    """


class DiagSelectSubsys(SCPICmdWrite, SCPICmdRead):
    """The ``DIAg:SELect:SUBSYS`` command.

    Description:
        - This command selects or queries the available subsystem. This command is equivalent to
          selecting Instrument Diagnostics from the Utilities menu and then choosing a Subsystem
          from the drop-down list.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:SELect:SUBSYS?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:SELect:SUBSYS?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DIAg:SELect:SUBSYS value`` command.

    SCPI Syntax:
        ```
        - DIAg:SELect:SUBSYS <NR1>
        - DIAg:SELect:SUBSYS?
        ```

    Info:
        - ``<NR1>`` selects a subsystem by number, which can range from 0 (zero selects ALL) through
          15 (as limited by the return from ``DIAG:NUMITEMS``).
    """


class DiagSelectLast(SCPICmdWrite, SCPICmdRead):
    """The ``DIAg:SELect:LAST`` command.

    Description:
        - This command selects one or more diagnostic menu items to be executed via the
          ``DIAG:EXECUTE`` command. If you specify ``DIAg:LEVEL SUBSYS``, then menu items come from
          this diagnostic level and are limited to the value returned by the ``DIAg:NUMITEMS?``
          query. For example, if the return from the ``DIAg:NUMITEMS?`` query is
          ``:DIAG:NUMITEMS 5``, specifying ``DIAg:SELECT:SUBSYS 2`` indicates that diagnostics will
          start from subsystem 2 and that you can specify a range from 2 through 5 for
          ``DIAg:SELect:LAST``. If you enter ``:DIAg:SELect:LAST 2``, only subsystem 2 will be
          executed. ``DIAg:SELect:LAST 4``, subsystems 2 through 4 will be executed.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:SELect:LAST?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:SELect:LAST?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DIAg:SELect:LAST value`` command.

    SCPI Syntax:
        ```
        - DIAg:SELect:LAST <NR1>
        - DIAg:SELect:LAST?
        ```

    Info:
        - ``<NR1>`` selects an integer that identifies the number of the last item that will be
          executed when the ``DIAG:EXECUTE`` command is run.
    """


class DiagSelectArea(SCPICmdWrite, SCPICmdRead):
    """The ``DIAg:SELect:AREA`` command.

    Description:
        - This command selects or queries an available diagnostic area. This command is equivalent
          to selecting Instrument Diagnostics from the Utilities menu and then selecting an Area
          from the pull-down list.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:SELect:AREA?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:SELect:AREA?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DIAg:SELect:AREA value`` command.

    SCPI Syntax:
        ```
        - DIAg:SELect:AREA <NR1>
        - DIAg:SELect:AREA?
        ```

    Info:
        - ``<NR1>`` selects a diagnostic area by number, which can range from 0 (zero selects all)
          through 15 (as specified by ``DIAG:NUMITEMS``).
    """


class DiagSelectAll(SCPICmdWrite):
    """The ``DIAg:SELect:ALL`` command.

    Description:
        - This command (no query form) selects all available diagnostics. This command is equivalent
          to selecting Instrument Diagnostics from the Utilities menu and then choosing ALL from the
          Subsystem, Area and Test pull-down lists.

    Usage:
        - Using the ``.write(value)`` method will send the ``DIAg:SELect:ALL value`` command.

    SCPI Syntax:
        ```
        - DIAg:SELect:ALL ALL
        ```

    Info:
        - ``ALL`` selects all available diagnostics.
    """


class DiagSelect(SCPICmdRead):
    """The ``DIAg:SELect`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:SELect?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:SELect?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.all``: The ``DIAg:SELect:ALL`` command.
        - ``.area``: The ``DIAg:SELect:AREA`` command.
        - ``.last``: The ``DIAg:SELect:LAST`` command.
        - ``.subsys``: The ``DIAg:SELect:SUBSYS`` command.
        - ``.test``: The ``DIAg:SELect:TEST`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._all = DiagSelectAll(device, f"{self._cmd_syntax}:ALL")
        self._area = DiagSelectArea(device, f"{self._cmd_syntax}:AREA")
        self._last = DiagSelectLast(device, f"{self._cmd_syntax}:LAST")
        self._subsys = DiagSelectSubsys(device, f"{self._cmd_syntax}:SUBSYS")
        self._test = DiagSelectTest(device, f"{self._cmd_syntax}:TEST")

    @property
    def all(self) -> DiagSelectAll:
        """Return the ``DIAg:SELect:ALL`` command.

        Description:
            - This command (no query form) selects all available diagnostics. This command is
              equivalent to selecting Instrument Diagnostics from the Utilities menu and then
              choosing ALL from the Subsystem, Area and Test pull-down lists.

        Usage:
            - Using the ``.write(value)`` method will send the ``DIAg:SELect:ALL value`` command.

        SCPI Syntax:
            ```
            - DIAg:SELect:ALL ALL
            ```

        Info:
            - ``ALL`` selects all available diagnostics.
        """
        return self._all

    @property
    def area(self) -> DiagSelectArea:
        """Return the ``DIAg:SELect:AREA`` command.

        Description:
            - This command selects or queries an available diagnostic area. This command is
              equivalent to selecting Instrument Diagnostics from the Utilities menu and then
              selecting an Area from the pull-down list.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:SELect:AREA?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:SELect:AREA?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DIAg:SELect:AREA value`` command.

        SCPI Syntax:
            ```
            - DIAg:SELect:AREA <NR1>
            - DIAg:SELect:AREA?
            ```

        Info:
            - ``<NR1>`` selects a diagnostic area by number, which can range from 0 (zero selects
              all) through 15 (as specified by ``DIAG:NUMITEMS``).
        """
        return self._area

    @property
    def last(self) -> DiagSelectLast:
        """Return the ``DIAg:SELect:LAST`` command.

        Description:
            - This command selects one or more diagnostic menu items to be executed via the
              ``DIAG:EXECUTE`` command. If you specify ``DIAg:LEVEL SUBSYS``, then menu items come
              from this diagnostic level and are limited to the value returned by the
              ``DIAg:NUMITEMS?`` query. For example, if the return from the ``DIAg:NUMITEMS?`` query
              is ``:DIAG:NUMITEMS 5``, specifying ``DIAg:SELECT:SUBSYS 2`` indicates that
              diagnostics will start from subsystem 2 and that you can specify a range from 2
              through 5 for ``DIAg:SELect:LAST``. If you enter ``:DIAg:SELect:LAST 2``, only
              subsystem 2 will be executed. ``DIAg:SELect:LAST 4``, subsystems 2 through 4 will be
              executed.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:SELect:LAST?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:SELect:LAST?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DIAg:SELect:LAST value`` command.

        SCPI Syntax:
            ```
            - DIAg:SELect:LAST <NR1>
            - DIAg:SELect:LAST?
            ```

        Info:
            - ``<NR1>`` selects an integer that identifies the number of the last item that will be
              executed when the ``DIAG:EXECUTE`` command is run.
        """
        return self._last

    @property
    def subsys(self) -> DiagSelectSubsys:
        """Return the ``DIAg:SELect:SUBSYS`` command.

        Description:
            - This command selects or queries the available subsystem. This command is equivalent to
              selecting Instrument Diagnostics from the Utilities menu and then choosing a Subsystem
              from the drop-down list.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:SELect:SUBSYS?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:SELect:SUBSYS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DIAg:SELect:SUBSYS value`` command.

        SCPI Syntax:
            ```
            - DIAg:SELect:SUBSYS <NR1>
            - DIAg:SELect:SUBSYS?
            ```

        Info:
            - ``<NR1>`` selects a subsystem by number, which can range from 0 (zero selects ALL)
              through 15 (as limited by the return from ``DIAG:NUMITEMS``).
        """
        return self._subsys

    @property
    def test(self) -> DiagSelectTest:
        """Return the ``DIAg:SELect:TEST`` command.

        Description:
            - This command selects or queries one of the available tests. This command is equivalent
              to selecting Instrument Diagnostics from the Utilities menu and then choosing a Test
              from the drop-down list.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:SELect:TEST?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:SELect:TEST?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DIAg:SELect:TEST value`` command.

        SCPI Syntax:
            ```
            - DIAg:SELect:TEST <NR1>
            - DIAg:SELect:TEST?
            ```

        Info:
            - ``<NR1>`` selects a test by number, which can range from 0 (zero selects ALL) through
              15 (as limited by the return from ``DIAG:NUMITEMS``).
        """
        return self._test


class DiagResultsVerbose(SCPICmdRead):
    """The ``DIAg:RESults:VERBose`` command.

    Description:
        - This query-only command returns a more explanatory message about the results of the last
          diagnostic (or test) execution than the ``DIAg:RESults?`` query. This command is
          equivalent to selecting Instrument Diagnostics from the Utilities menu and then reviewing
          the Diagnostic Status. This query-only command can be issued while diagnostics are still
          in progress.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:RESults:VERBose?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:RESults:VERBose?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DIAg:RESults:VERBose?
        ```
    """


class DiagResults(SCPICmdRead):
    """The ``DIAg:RESults`` command.

    Description:
        - This query-only command returns an abbreviated status about the results of the last
          diagnostic (or test) execution. For a more explanatory status message, use the
          ``DIAg:RESults:VERBose?`` query. This command is equivalent to selecting Instrument
          Diagnostics from the Utilities menu and then reviewing the Diagnostic Status. This
          query-only command can be issued while diagnostics are still in progress.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:RESults?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:RESults?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DIAg:RESults?
        ```

    Properties:
        - ``.verbose``: The ``DIAg:RESults:VERBose`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._verbose = DiagResultsVerbose(device, f"{self._cmd_syntax}:VERBose")

    @property
    def verbose(self) -> DiagResultsVerbose:
        """Return the ``DIAg:RESults:VERBose`` command.

        Description:
            - This query-only command returns a more explanatory message about the results of the
              last diagnostic (or test) execution than the ``DIAg:RESults?`` query. This command is
              equivalent to selecting Instrument Diagnostics from the Utilities menu and then
              reviewing the Diagnostic Status. This query-only command can be issued while
              diagnostics are still in progress.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:RESults:VERBose?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:RESults:VERBose?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAg:RESults:VERBose?
            ```
        """
        return self._verbose


class DiagNumitems(SCPICmdRead):
    """The ``DIAg:NUMITEMS`` command.

    Description:
        - This query-only command returns the number of items on the currently selected level of
          test hierarchy, which ranges from 1 through 15. This command is equivalent to selecting
          Instrument Diagnostics from the Utilities menu and then reviewing the Diagnostic Status.
          This query-only command can be issued while diagnostics are still in progress.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:NUMITEMS?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:NUMITEMS?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DIAg:NUMITEMS?
        ```
    """


class DiagNameTest(SCPICmdRead):
    """The ``DIAg:NAMe:TEST`` command.

    Description:
        - This query-only command returns the name of the current diagnostic test. This command is
          equivalent to selecting Instrument Diagnostics from the Utilities menu and then reviewing
          the Diagnostic Status. This query-only command can be issued while diagnostics are still
          in progress.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:NAMe:TEST?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:NAMe:TEST?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DIAg:NAMe:TEST?
        ```
    """


class DiagNameSubsys(SCPICmdRead):
    """The ``DIAg:NAMe:SUBSYS`` command.

    Description:
        - This query-only command returns the subsystem of the current diagnostic test. This command
          is equivalent to selecting Instrument Diagnostics from the Utilities menu and then
          reviewing the Diagnostic Status. This query-only command can be issued while diagnostics
          are still in progress.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:NAMe:SUBSYS?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:NAMe:SUBSYS?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DIAg:NAMe:SUBSYS?
        ```
    """


class DiagNameArea(SCPICmdRead):
    """The ``DIAg:NAMe:AREA`` command.

    Description:
        - This query-only command returns the selected area of the current diagnostic test. There
          are three levels of diagnostic test hierarchy: subsystem, area and test. This command is
          equivalent to selecting Instrument Diagnostics from the Utilities menu and then reviewing
          the Diagnostic Status. This query-only command can be issued while diagnostics are still
          in progress.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:NAMe:AREA?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:NAMe:AREA?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DIAg:NAMe:AREA?
        ```
    """


class DiagName(SCPICmdRead):
    """The ``DIAg:NAMe`` command.

    Description:
        - This query-only command returns the names of the subsystem, area, and test of the current
          diagnostic test. This command can be issued while diagnostics are still in progress.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:NAMe?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:NAMe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DIAg:NAMe?
        ```

    Properties:
        - ``.area``: The ``DIAg:NAMe:AREA`` command.
        - ``.subsys``: The ``DIAg:NAMe:SUBSYS`` command.
        - ``.test``: The ``DIAg:NAMe:TEST`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._area = DiagNameArea(device, f"{self._cmd_syntax}:AREA")
        self._subsys = DiagNameSubsys(device, f"{self._cmd_syntax}:SUBSYS")
        self._test = DiagNameTest(device, f"{self._cmd_syntax}:TEST")

    @property
    def area(self) -> DiagNameArea:
        """Return the ``DIAg:NAMe:AREA`` command.

        Description:
            - This query-only command returns the selected area of the current diagnostic test.
              There are three levels of diagnostic test hierarchy: subsystem, area and test. This
              command is equivalent to selecting Instrument Diagnostics from the Utilities menu and
              then reviewing the Diagnostic Status. This query-only command can be issued while
              diagnostics are still in progress.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:NAMe:AREA?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:NAMe:AREA?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAg:NAMe:AREA?
            ```
        """
        return self._area

    @property
    def subsys(self) -> DiagNameSubsys:
        """Return the ``DIAg:NAMe:SUBSYS`` command.

        Description:
            - This query-only command returns the subsystem of the current diagnostic test. This
              command is equivalent to selecting Instrument Diagnostics from the Utilities menu and
              then reviewing the Diagnostic Status. This query-only command can be issued while
              diagnostics are still in progress.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:NAMe:SUBSYS?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:NAMe:SUBSYS?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAg:NAMe:SUBSYS?
            ```
        """
        return self._subsys

    @property
    def test(self) -> DiagNameTest:
        """Return the ``DIAg:NAMe:TEST`` command.

        Description:
            - This query-only command returns the name of the current diagnostic test. This command
              is equivalent to selecting Instrument Diagnostics from the Utilities menu and then
              reviewing the Diagnostic Status. This query-only command can be issued while
              diagnostics are still in progress.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:NAMe:TEST?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:NAMe:TEST?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAg:NAMe:TEST?
            ```
        """
        return self._test


class DiagLoops(SCPICmdRead):
    """The ``DIAg:LOOPS`` command.

    Description:
        - This query-only command returns the number of times that the selected diagnostics set was
          completed during the last diagnostic execution. This command is equivalent to selecting
          Instrument Diagnostics from the Utilities menu and then reviewing the Elapsed Loops. This
          query-only command can be issued while diagnostics are still in progress.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:LOOPS?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:LOOPS?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DIAg:LOOPS?
        ```
    """


class DiagLevel(SCPICmdWrite, SCPICmdRead):
    """The ``DIAg:LEVEL`` command.

    Description:
        - This command sets or queries the selected level of diagnostic test hierarchy. This command
          is equivalent to selecting Instrument Diagnostics from the Utilities menu and then
          reviewing the Diagnostic Status.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:LEVEL?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:LEVEL?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DIAg:LEVEL value`` command.

    SCPI Syntax:
        ```
        - DIAg:LEVEL {AREA|SUBSYS|TEST}
        - DIAg:LEVEL?
        ```

    Info:
        - ``AREA`` sets diagnostic testing to the area level.
        - ``SUBSYS`` sets diagnostic testing to the subsystem level.
        - ``TEST`` sets diagnostic testing to the test level.
    """


class DiagItemSubitems(SCPICmdReadWithArguments):
    """The ``DIAg:ITEM:SUBITEMS`` command.

    Description:
        - This query-only command returns the number of subitems associated with the item. This
          command is equivalent to selecting Instrument Diagnostics from the Utilities menu,
          choosing the Subsystem, Area or Test setting and then reviewing the resulting subitems.
          This query-only command can be issued while diagnostics are still in progress.

    Usage:
        - Using the ``.query(argument)`` method will send the ``DIAg:ITEM:SUBITEMS? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``DIAg:ITEM:SUBITEMS? argument`` query and raise an AssertionError if the returned value
          does not match ``value``.

    SCPI Syntax:
        ```
        - DIAg:ITEM:SUBITEMS? <NR1>
        ```

    Info:
        - ``<NR1>`` sets the index item about which data will be returned, which ranges from 0
          through 15.
    """


class DiagItemResult(SCPICmdReadWithArguments):
    """The ``DIAg:ITEM:RESULT`` command.

    Description:
        - This query-only command returns the result from the last execution of the item. This
          command is equivalent to selecting Instrument Diagnostics from the Utilities menu and then
          reviewing the Diagnostic Status. This query-only command can be issued while diagnostics
          are still in progress.

    Usage:
        - Using the ``.query(argument)`` method will send the ``DIAg:ITEM:RESULT? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the ``DIAg:ITEM:RESULT? argument``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DIAg:ITEM:RESULT? <NR1>
        ```

    Info:
        - ``<NR1>`` sets the index item about which data will be returned, which ranges from 0
          through 15.
    """


class DiagItemName(SCPICmdReadWithArguments):
    """The ``DIAg:ITEM:NAMe`` command.

    Description:
        - This query-only command returns the name of the selected menu item. This command is
          equivalent to selecting Instrument Diagnostics from the Utilities menu and then reviewing
          the Subsystem, Area and Test settings. This query-only command can be issued while
          diagnostics are still in progress.

    Usage:
        - Using the ``.query(argument)`` method will send the ``DIAg:ITEM:NAMe? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the ``DIAg:ITEM:NAMe? argument``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DIAg:ITEM:NAMe? <NR1>
        ```

    Info:
        - ``<NR1>`` sets the index item about which data will be returned, which ranges from 0
          through 15.
    """


class DiagItemFailures(SCPICmdReadWithArguments):
    """The ``DIAg:ITEM:FAILURES`` command.

    Description:
        - This query-only command returns the total number of failures. This command is equivalent
          to selecting Instrument Diagnostics from the Utilities menu and then reviewing the
          Diagnostic Status. This query-only command can be issued while diagnostics are still in
          progress.

    Usage:
        - Using the ``.query(argument)`` method will send the ``DIAg:ITEM:FAILURES? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``DIAg:ITEM:FAILURES? argument`` query and raise an AssertionError if the returned value
          does not match ``value``.

    SCPI Syntax:
        ```
        - DIAg:ITEM:FAILURES? <NR1>
        ```

    Info:
        - ``<NR1>`` sets the index item about which data will be returned, which ranges from 0
          through 15.
    """


class DiagItem(SCPICmdReadWithArguments):
    """The ``DIAg:ITEM`` command.

    Description:
        - This query-only command returns the diagnostics settings. This command is equivalent to
          selecting Instrument Diagnostics from the Utilities menu, and then reviewing the
          diagnostics settings. This query-only command can be issued while diagnostics are still in
          progress.

    Usage:
        - Using the ``.query(argument)`` method will send the ``DIAg:ITEM? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the ``DIAg:ITEM? argument`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DIAg:ITEM? <NR1>
        ```

    Info:
        - ``<NR1>`` sets the index item about which data will be returned, which ranges from 0
          through 15.

    Properties:
        - ``.failures``: The ``DIAg:ITEM:FAILURES`` command.
        - ``.name``: The ``DIAg:ITEM:NAMe`` command.
        - ``.result``: The ``DIAg:ITEM:RESULT`` command.
        - ``.subitems``: The ``DIAg:ITEM:SUBITEMS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._failures = DiagItemFailures(device, f"{self._cmd_syntax}:FAILURES")
        self._name = DiagItemName(device, f"{self._cmd_syntax}:NAMe")
        self._result = DiagItemResult(device, f"{self._cmd_syntax}:RESULT")
        self._subitems = DiagItemSubitems(device, f"{self._cmd_syntax}:SUBITEMS")

    @property
    def failures(self) -> DiagItemFailures:
        """Return the ``DIAg:ITEM:FAILURES`` command.

        Description:
            - This query-only command returns the total number of failures. This command is
              equivalent to selecting Instrument Diagnostics from the Utilities menu and then
              reviewing the Diagnostic Status. This query-only command can be issued while
              diagnostics are still in progress.

        Usage:
            - Using the ``.query(argument)`` method will send the ``DIAg:ITEM:FAILURES? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``DIAg:ITEM:FAILURES? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAg:ITEM:FAILURES? <NR1>
            ```

        Info:
            - ``<NR1>`` sets the index item about which data will be returned, which ranges from 0
              through 15.
        """
        return self._failures

    @property
    def name(self) -> DiagItemName:
        """Return the ``DIAg:ITEM:NAMe`` command.

        Description:
            - This query-only command returns the name of the selected menu item. This command is
              equivalent to selecting Instrument Diagnostics from the Utilities menu and then
              reviewing the Subsystem, Area and Test settings. This query-only command can be issued
              while diagnostics are still in progress.

        Usage:
            - Using the ``.query(argument)`` method will send the ``DIAg:ITEM:NAMe? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``DIAg:ITEM:NAMe? argument`` query and raise an AssertionError if the returned value
              does not match ``value``.

        SCPI Syntax:
            ```
            - DIAg:ITEM:NAMe? <NR1>
            ```

        Info:
            - ``<NR1>`` sets the index item about which data will be returned, which ranges from 0
              through 15.
        """
        return self._name

    @property
    def result(self) -> DiagItemResult:
        """Return the ``DIAg:ITEM:RESULT`` command.

        Description:
            - This query-only command returns the result from the last execution of the item. This
              command is equivalent to selecting Instrument Diagnostics from the Utilities menu and
              then reviewing the Diagnostic Status. This query-only command can be issued while
              diagnostics are still in progress.

        Usage:
            - Using the ``.query(argument)`` method will send the ``DIAg:ITEM:RESULT? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``DIAg:ITEM:RESULT? argument`` query and raise an AssertionError if the returned value
              does not match ``value``.

        SCPI Syntax:
            ```
            - DIAg:ITEM:RESULT? <NR1>
            ```

        Info:
            - ``<NR1>`` sets the index item about which data will be returned, which ranges from 0
              through 15.
        """
        return self._result

    @property
    def subitems(self) -> DiagItemSubitems:
        """Return the ``DIAg:ITEM:SUBITEMS`` command.

        Description:
            - This query-only command returns the number of subitems associated with the item. This
              command is equivalent to selecting Instrument Diagnostics from the Utilities menu,
              choosing the Subsystem, Area or Test setting and then reviewing the resulting
              subitems. This query-only command can be issued while diagnostics are still in
              progress.

        Usage:
            - Using the ``.query(argument)`` method will send the ``DIAg:ITEM:SUBITEMS? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``DIAg:ITEM:SUBITEMS? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAg:ITEM:SUBITEMS? <NR1>
            ```

        Info:
            - ``<NR1>`` sets the index item about which data will be returned, which ranges from 0
              through 15.
        """
        return self._subitems


class DiagFailuresClear(SCPICmdWrite, SCPICmdRead):
    """The ``DIAg:FAILURES:CLEAR`` command.

    Description:
        - This command sets and queries the clearing of pass/fail information from data structures,
          not the Event Log, at the start of diagnostic tests.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:FAILURES:CLEAR?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:FAILURES:CLEAR?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DIAg:FAILURES:CLEAR value`` command.

    SCPI Syntax:
        ```
        - DIAg:FAILURES:CLEAR {ON|OFF|<NR1>}
        - DIAg:FAILURES:CLEAR?
        ```

    Info:
        - ``<NR1> = 0`` turns off the clearing the pass/fail information at the start of tests; any
          other value turns on the clearing of pass/fail information.
        - ``OFF`` does not clear pass/fail information at the start of tests.
        - ``ON`` clears pass/fail information from data structures, not the Event Log, at the start
          of tests.
    """


class DiagFailures(SCPICmdRead):
    """The ``DIAg:FAILURES`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:FAILURES?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:FAILURES?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.clear``: The ``DIAg:FAILURES:CLEAR`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._clear = DiagFailuresClear(device, f"{self._cmd_syntax}:CLEAR")

    @property
    def clear(self) -> DiagFailuresClear:
        """Return the ``DIAg:FAILURES:CLEAR`` command.

        Description:
            - This command sets and queries the clearing of pass/fail information from data
              structures, not the Event Log, at the start of diagnostic tests.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:FAILURES:CLEAR?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:FAILURES:CLEAR?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DIAg:FAILURES:CLEAR value``
              command.

        SCPI Syntax:
            ```
            - DIAg:FAILURES:CLEAR {ON|OFF|<NR1>}
            - DIAg:FAILURES:CLEAR?
            ```

        Info:
            - ``<NR1> = 0`` turns off the clearing the pass/fail information at the start of tests;
              any other value turns on the clearing of pass/fail information.
            - ``OFF`` does not clear pass/fail information at the start of tests.
            - ``ON`` clears pass/fail information from data structures, not the Event Log, at the
              start of tests.
        """
        return self._clear


class DiagExecute(SCPICmdWriteNoArguments):
    """The ``DIAg:EXECUTE`` command.

    Description:
        - This command (no query form) starts the execution of the currently selected set of
          diagnostics. This command is equivalent to selecting Instrument Diagnostics from the
          Utilities menu and then pressing Run.

    Usage:
        - Using the ``.write()`` method will send the ``DIAg:EXECUTE`` command.

    SCPI Syntax:
        ```
        - DIAg:EXECUTE
        ```
    """


class DiagControlLoop(SCPICmdWrite, SCPICmdRead):
    """The ``DIAg:CONTROL:LOOP`` command.

    Description:
        - This command determines or queries whether the next execution of diagnostics executes once
          or continuously loops on the selected set of diagnostics (assuming the halt control is set
          to off using the ``DIAG:CONTROL:HALT`` command or that the halt control is set to ON but
          no failures occur). This command is equivalent to selecting Instrument Diagnostics from
          the Utilities menu and then enabling Loop Control.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:CONTROL:LOOP?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:CONTROL:LOOP?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DIAg:CONTROL:LOOP value`` command.

    SCPI Syntax:
        ```
        - DIAg:CONTROL:LOOP {ON|OFF|<NR1>}
        - DIAg:CONTROL:LOOP?
        ```

    Info:
        - ``<NR1>`` = 1 enables the loop function; any other value disables the loop function.
        - ``ON`` enables the loop function, causing the execution of diagnostics to continuously
          loop.
        - ``OFF`` disables the loop function, causing the instrument to execute the entire set of
          diagnostics once and then halt.
    """


class DiagControlHalt(SCPICmdWrite, SCPICmdRead):
    """The ``DIAg:CONTROL:HALT`` command.

    Description:
        - This command determines or queries whether the next execution of diagnostics looping will
          stop on the first diagnostic failure that occurs or will continue to loop on the selected
          set of diagnostic functions. This command is equivalent to selecting Instrument
          Diagnostics from the Utilities menu and then enabling Halt on Fail.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:CONTROL:HALT?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:CONTROL:HALT?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DIAg:CONTROL:HALT value`` command.

    SCPI Syntax:
        ```
        - DIAg:CONTROL:HALT {ON|OFF|<NR1>}
        - DIAg:CONTROL:HALT?
        ```

    Info:
        - ``<NR1>`` = 1 enables the halt function; any other value disables the halt function.
        - ``ON`` enables the halt function, causing the execution of diagnostics looping to halt at
          the first diagnostic failure that occurs.
        - ``OFF`` disables the halt looping function, allowing the instrument to continue to loop on
          the entire set of diagnostics, even if diagnostic failure occurs.
    """


class DiagControl(SCPICmdRead):
    """The ``DIAg:CONTROL`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:CONTROL?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:CONTROL?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.halt``: The ``DIAg:CONTROL:HALT`` command.
        - ``.loop``: The ``DIAg:CONTROL:LOOP`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._halt = DiagControlHalt(device, f"{self._cmd_syntax}:HALT")
        self._loop = DiagControlLoop(device, f"{self._cmd_syntax}:LOOP")

    @property
    def halt(self) -> DiagControlHalt:
        """Return the ``DIAg:CONTROL:HALT`` command.

        Description:
            - This command determines or queries whether the next execution of diagnostics looping
              will stop on the first diagnostic failure that occurs or will continue to loop on the
              selected set of diagnostic functions. This command is equivalent to selecting
              Instrument Diagnostics from the Utilities menu and then enabling Halt on Fail.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:CONTROL:HALT?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:CONTROL:HALT?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DIAg:CONTROL:HALT value`` command.

        SCPI Syntax:
            ```
            - DIAg:CONTROL:HALT {ON|OFF|<NR1>}
            - DIAg:CONTROL:HALT?
            ```

        Info:
            - ``<NR1>`` = 1 enables the halt function; any other value disables the halt function.
            - ``ON`` enables the halt function, causing the execution of diagnostics looping to halt
              at the first diagnostic failure that occurs.
            - ``OFF`` disables the halt looping function, allowing the instrument to continue to
              loop on the entire set of diagnostics, even if diagnostic failure occurs.
        """
        return self._halt

    @property
    def loop(self) -> DiagControlLoop:
        """Return the ``DIAg:CONTROL:LOOP`` command.

        Description:
            - This command determines or queries whether the next execution of diagnostics executes
              once or continuously loops on the selected set of diagnostics (assuming the halt
              control is set to off using the ``DIAG:CONTROL:HALT`` command or that the halt control
              is set to ON but no failures occur). This command is equivalent to selecting
              Instrument Diagnostics from the Utilities menu and then enabling Loop Control.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:CONTROL:LOOP?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:CONTROL:LOOP?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DIAg:CONTROL:LOOP value`` command.

        SCPI Syntax:
            ```
            - DIAg:CONTROL:LOOP {ON|OFF|<NR1>}
            - DIAg:CONTROL:LOOP?
            ```

        Info:
            - ``<NR1>`` = 1 enables the loop function; any other value disables the loop function.
            - ``ON`` enables the loop function, causing the execution of diagnostics to continuously
              loop.
            - ``OFF`` disables the loop function, causing the instrument to execute the entire set
              of diagnostics once and then halt.
        """
        return self._loop


#  pylint: disable=too-many-instance-attributes
class Diag(SCPICmdRead):
    """The ``DIAg`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.control``: The ``DIAg:CONTROL`` command tree.
        - ``.execute``: The ``DIAg:EXECUTE`` command.
        - ``.failures``: The ``DIAg:FAILURES`` command tree.
        - ``.item``: The ``DIAg:ITEM`` command.
        - ``.level``: The ``DIAg:LEVEL`` command.
        - ``.loops``: The ``DIAg:LOOPS`` command.
        - ``.name``: The ``DIAg:NAMe`` command.
        - ``.numitems``: The ``DIAg:NUMITEMS`` command.
        - ``.results``: The ``DIAg:RESults`` command.
        - ``.select``: The ``DIAg:SELect`` command tree.
        - ``.state``: The ``DIAg:STATE`` command.
        - ``.stop``: The ``DIAg:STOP`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "DIAg") -> None:
        super().__init__(device, cmd_syntax)
        self._control = DiagControl(device, f"{self._cmd_syntax}:CONTROL")
        self._execute = DiagExecute(device, f"{self._cmd_syntax}:EXECUTE")
        self._failures = DiagFailures(device, f"{self._cmd_syntax}:FAILURES")
        self._item = DiagItem(device, f"{self._cmd_syntax}:ITEM")
        self._level = DiagLevel(device, f"{self._cmd_syntax}:LEVEL")
        self._loops = DiagLoops(device, f"{self._cmd_syntax}:LOOPS")
        self._name = DiagName(device, f"{self._cmd_syntax}:NAMe")
        self._numitems = DiagNumitems(device, f"{self._cmd_syntax}:NUMITEMS")
        self._results = DiagResults(device, f"{self._cmd_syntax}:RESults")
        self._select = DiagSelect(device, f"{self._cmd_syntax}:SELect")
        self._state = DiagState(device, f"{self._cmd_syntax}:STATE")
        self._stop = DiagStop(device, f"{self._cmd_syntax}:STOP")

    @property
    def control(self) -> DiagControl:
        """Return the ``DIAg:CONTROL`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:CONTROL?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:CONTROL?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.halt``: The ``DIAg:CONTROL:HALT`` command.
            - ``.loop``: The ``DIAg:CONTROL:LOOP`` command.
        """
        return self._control

    @property
    def execute(self) -> DiagExecute:
        """Return the ``DIAg:EXECUTE`` command.

        Description:
            - This command (no query form) starts the execution of the currently selected set of
              diagnostics. This command is equivalent to selecting Instrument Diagnostics from the
              Utilities menu and then pressing Run.

        Usage:
            - Using the ``.write()`` method will send the ``DIAg:EXECUTE`` command.

        SCPI Syntax:
            ```
            - DIAg:EXECUTE
            ```
        """
        return self._execute

    @property
    def failures(self) -> DiagFailures:
        """Return the ``DIAg:FAILURES`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:FAILURES?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:FAILURES?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.clear``: The ``DIAg:FAILURES:CLEAR`` command.
        """
        return self._failures

    @property
    def item(self) -> DiagItem:
        """Return the ``DIAg:ITEM`` command.

        Description:
            - This query-only command returns the diagnostics settings. This command is equivalent
              to selecting Instrument Diagnostics from the Utilities menu, and then reviewing the
              diagnostics settings. This query-only command can be issued while diagnostics are
              still in progress.

        Usage:
            - Using the ``.query(argument)`` method will send the ``DIAg:ITEM? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the ``DIAg:ITEM? argument``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAg:ITEM? <NR1>
            ```

        Info:
            - ``<NR1>`` sets the index item about which data will be returned, which ranges from 0
              through 15.

        Sub-properties:
            - ``.failures``: The ``DIAg:ITEM:FAILURES`` command.
            - ``.name``: The ``DIAg:ITEM:NAMe`` command.
            - ``.result``: The ``DIAg:ITEM:RESULT`` command.
            - ``.subitems``: The ``DIAg:ITEM:SUBITEMS`` command.
        """
        return self._item

    @property
    def level(self) -> DiagLevel:
        """Return the ``DIAg:LEVEL`` command.

        Description:
            - This command sets or queries the selected level of diagnostic test hierarchy. This
              command is equivalent to selecting Instrument Diagnostics from the Utilities menu and
              then reviewing the Diagnostic Status.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:LEVEL?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:LEVEL?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DIAg:LEVEL value`` command.

        SCPI Syntax:
            ```
            - DIAg:LEVEL {AREA|SUBSYS|TEST}
            - DIAg:LEVEL?
            ```

        Info:
            - ``AREA`` sets diagnostic testing to the area level.
            - ``SUBSYS`` sets diagnostic testing to the subsystem level.
            - ``TEST`` sets diagnostic testing to the test level.
        """
        return self._level

    @property
    def loops(self) -> DiagLoops:
        """Return the ``DIAg:LOOPS`` command.

        Description:
            - This query-only command returns the number of times that the selected diagnostics set
              was completed during the last diagnostic execution. This command is equivalent to
              selecting Instrument Diagnostics from the Utilities menu and then reviewing the
              Elapsed Loops. This query-only command can be issued while diagnostics are still in
              progress.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:LOOPS?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:LOOPS?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAg:LOOPS?
            ```
        """
        return self._loops

    @property
    def name(self) -> DiagName:
        """Return the ``DIAg:NAMe`` command.

        Description:
            - This query-only command returns the names of the subsystem, area, and test of the
              current diagnostic test. This command can be issued while diagnostics are still in
              progress.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:NAMe?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:NAMe?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAg:NAMe?
            ```

        Sub-properties:
            - ``.area``: The ``DIAg:NAMe:AREA`` command.
            - ``.subsys``: The ``DIAg:NAMe:SUBSYS`` command.
            - ``.test``: The ``DIAg:NAMe:TEST`` command.
        """
        return self._name

    @property
    def numitems(self) -> DiagNumitems:
        """Return the ``DIAg:NUMITEMS`` command.

        Description:
            - This query-only command returns the number of items on the currently selected level of
              test hierarchy, which ranges from 1 through 15. This command is equivalent to
              selecting Instrument Diagnostics from the Utilities menu and then reviewing the
              Diagnostic Status. This query-only command can be issued while diagnostics are still
              in progress.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:NUMITEMS?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:NUMITEMS?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAg:NUMITEMS?
            ```
        """
        return self._numitems

    @property
    def results(self) -> DiagResults:
        """Return the ``DIAg:RESults`` command.

        Description:
            - This query-only command returns an abbreviated status about the results of the last
              diagnostic (or test) execution. For a more explanatory status message, use the
              ``DIAg:RESults:VERBose?`` query. This command is equivalent to selecting Instrument
              Diagnostics from the Utilities menu and then reviewing the Diagnostic Status. This
              query-only command can be issued while diagnostics are still in progress.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:RESults?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:RESults?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAg:RESults?
            ```

        Sub-properties:
            - ``.verbose``: The ``DIAg:RESults:VERBose`` command.
        """
        return self._results

    @property
    def select(self) -> DiagSelect:
        """Return the ``DIAg:SELect`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:SELect?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:SELect?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.all``: The ``DIAg:SELect:ALL`` command.
            - ``.area``: The ``DIAg:SELect:AREA`` command.
            - ``.last``: The ``DIAg:SELect:LAST`` command.
            - ``.subsys``: The ``DIAg:SELect:SUBSYS`` command.
            - ``.test``: The ``DIAg:SELect:TEST`` command.
        """
        return self._select

    @property
    def state(self) -> DiagState:
        """Return the ``DIAg:STATE`` command.

        Description:
            - This command changes the instrument operating state. Depending on the argument,
              diagnostics capabilities are either turned on or off. This command is equivalent to
              opening the ``DIAg:STATE`` dialog (ON) or closing it (OFF).

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:STATE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DIAg:STATE value`` command.

        SCPI Syntax:
            ```
            - DIAg:STATE {<NR1>|EXECUTE|ON|OFF}
            - DIAg:STATE?
            ```

        Info:
            - ``<NR1>`` = 0 disables diagnostics capabilities and returns the instrument to a normal
              operating state; any other value enables diagnostics.
            - ``EXECUTE`` starts execution of the diagnostics.
            - ``ON`` puts the instrument into the state in which diagnostics can be run. This
              argument is thrown automatically if the ``DIAG:EXECUTE`` command is executed.
            - ``OFF`` disables diagnostics capabilities and returns the instrument to a normal
              operating state.
        """
        return self._state

    @property
    def stop(self) -> DiagStop:
        """Return the ``DIAg:STOP`` command.

        Description:
            - This command (no query form) causes diagnostics (or test) execution to terminate at
              the end of the next low-level test. This command is equivalent to selecting Instrument
              Diagnostics from the Utilities menu and then clicking Abort.

        Usage:
            - Using the ``.write()`` method will send the ``DIAg:STOP`` command.

        SCPI Syntax:
            ```
            - DIAg:STOP
            ```
        """
        return self._stop
