"""The diag commands module.

These commands are used in the following models:
MSO2

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - DIAg:LOOP:OPTion {FAIL|ONCE|ALWAYS|ONFAIL|NTIMES}
    - DIAg:LOOP:OPTion:NTIMes <NR1>
    - DIAg:LOOP:OPTion:NTIMes?
    - DIAg:LOOP:OPTion?
    - DIAg:LOOP:STOP
    - DIAg:MODe {POST|EXTENDED|SERVICE}
    - DIAg:MODe?
    - DIAg:RESUlt:FLAg?
    - DIAg:RESUlt:LOG?
    - DIAg:RESUlt?
    - DIAg:SELect {ALL|IO|ANALOG|SYSTEM|ASIC|ACQ|SIGNAL|MEMORY}
    - DIAg:SELect?
    - DIAg:STATE {EXECute|ABOrt}
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class DiagState(SCPICmdWrite):
    """The ``DIAg:STATE`` command.

    Description:
        - This command starts or aborts Self Test. Abort happens after group under test completes.

    Usage:
        - Using the ``.write(value)`` method will send the ``DIAg:STATE value`` command.

    SCPI Syntax:
        ```
        - DIAg:STATE {EXECute|ABOrt}
        ```

    Info:
        - ``EXECUTE`` starts execution of the diagnostics.
        - ``ABOrt`` disables diagnostics capabilities and returns the instrument to a normal
          operating state.
    """


class DiagSelect(SCPICmdWrite, SCPICmdRead):
    """The ``DIAg:SELect`` command.

    Description:
        - This command selects or queries an available diagnostic area.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:SELect?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:SELect?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DIAg:SELect value`` command.

    SCPI Syntax:
        ```
        - DIAg:SELect {ALL|IO|ANALOG|SYSTEM|ASIC|ACQ|SIGNAL|MEMORY}
        - DIAg:SELect?
        ```

    Info:
        - ``ALL``
        - ``IO``
        - ``ANALOG``
        - ``SYSTEM``
        - ``ASIC``
        - ``ACQ``
        - ``SIGNAL``
        - ``MEMORY``
    """


class DiagResultLog(SCPICmdRead):
    """The ``DIAg:RESUlt:LOG`` command.

    Description:
        - This query returns the test Pass/Fail status of each diagnostic area. It does not return
          the overall status.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:RESUlt:LOG?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:RESUlt:LOG?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DIAg:RESUlt:LOG?
        ```
    """


class DiagResultFlag(SCPICmdRead):
    """The ``DIAg:RESUlt:FLAg`` command.

    Description:
        - This query returns the status of the diagnostic test area that has been selected.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:RESUlt:FLAg?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:RESUlt:FLAg?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DIAg:RESUlt:FLAg?
        ```
    """


class DiagResult(SCPICmdRead):
    """The ``DIAg:RESUlt`` command.

    Description:
        - This query returns both the overall diagnostics test results and the results of each
          individual test area.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:RESUlt?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:RESUlt?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DIAg:RESUlt?
        ```

    Properties:
        - ``.flag``: The ``DIAg:RESUlt:FLAg`` command.
        - ``.log``: The ``DIAg:RESUlt:LOG`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._flag = DiagResultFlag(device, f"{self._cmd_syntax}:FLAg")
        self._log = DiagResultLog(device, f"{self._cmd_syntax}:LOG")

    @property
    def flag(self) -> DiagResultFlag:
        """Return the ``DIAg:RESUlt:FLAg`` command.

        Description:
            - This query returns the status of the diagnostic test area that has been selected.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:RESUlt:FLAg?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:RESUlt:FLAg?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAg:RESUlt:FLAg?
            ```
        """
        return self._flag

    @property
    def log(self) -> DiagResultLog:
        """Return the ``DIAg:RESUlt:LOG`` command.

        Description:
            - This query returns the test Pass/Fail status of each diagnostic area. It does not
              return the overall status.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:RESUlt:LOG?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:RESUlt:LOG?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAg:RESUlt:LOG?
            ```
        """
        return self._log


class DiagMode(SCPICmdWrite, SCPICmdRead):
    """The ``DIAg:MODe`` command.

    Description:
        - This command sets or queries the diagnostics mode.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:MODe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DIAg:MODe value`` command.

    SCPI Syntax:
        ```
        - DIAg:MODe {POST|EXTENDED|SERVICE}
        - DIAg:MODe?
        ```

    Info:
        - ``POST`` specifies the power on self test diagnostics.
        - ``EXTENDED`` specifies the extended diagnostics.
        - ``SERVICE`` specifies the service diagnostics.
    """


class DiagLoopStop(SCPICmdWriteNoArguments):
    """The ``DIAg:LOOP:STOP`` command.

    Description:
        - Request that diagnostics stop looping.

    Usage:
        - Using the ``.write()`` method will send the ``DIAg:LOOP:STOP`` command.

    SCPI Syntax:
        ```
        - DIAg:LOOP:STOP
        ```
    """


class DiagLoopOptionNtimes(SCPICmdWrite, SCPICmdRead):
    """The ``DIAg:LOOP:OPTion:NTIMes`` command.

    Description:
        - This command sets or queries how many loops to run, if N-times is being used.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:LOOP:OPTion:NTIMes?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:LOOP:OPTion:NTIMes?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DIAg:LOOP:OPTion:NTIMes value``
          command.

    SCPI Syntax:
        ```
        - DIAg:LOOP:OPTion:NTIMes <NR1>
        - DIAg:LOOP:OPTion:NTIMes?
        ```

    Info:
        - ``<NR1>`` is how many loops to run.
    """


class DiagLoopOption(SCPICmdWrite, SCPICmdRead):
    """The ``DIAg:LOOP:OPTion`` command.

    Description:
        - This command sets or queries the type of looping desired.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:LOOP:OPTion?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:LOOP:OPTion?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DIAg:LOOP:OPTion value`` command.

    SCPI Syntax:
        ```
        - DIAg:LOOP:OPTion {FAIL|ONCE|ALWAYS|ONFAIL|NTIMES}
        - DIAg:LOOP:OPTion?
        ```

    Info:
        - ``Fail`` - run until a failure is found, then halt.
        - ``Once`` - run through one loop.
        - ``Always`` - run forever.
        - ``Onfail`` - run until a failure is found, then loop on it.
        - ``Ntimes`` - run n number of loops.

    Properties:
        - ``.ntimes``: The ``DIAg:LOOP:OPTion:NTIMes`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ntimes = DiagLoopOptionNtimes(device, f"{self._cmd_syntax}:NTIMes")

    @property
    def ntimes(self) -> DiagLoopOptionNtimes:
        """Return the ``DIAg:LOOP:OPTion:NTIMes`` command.

        Description:
            - This command sets or queries how many loops to run, if N-times is being used.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:LOOP:OPTion:NTIMes?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:LOOP:OPTion:NTIMes?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DIAg:LOOP:OPTion:NTIMes value``
              command.

        SCPI Syntax:
            ```
            - DIAg:LOOP:OPTion:NTIMes <NR1>
            - DIAg:LOOP:OPTion:NTIMes?
            ```

        Info:
            - ``<NR1>`` is how many loops to run.
        """
        return self._ntimes


class DiagLoop(SCPICmdRead):
    """The ``DIAg:LOOP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:LOOP?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:LOOP?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.option``: The ``DIAg:LOOP:OPTion`` command.
        - ``.stop``: The ``DIAg:LOOP:STOP`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._option = DiagLoopOption(device, f"{self._cmd_syntax}:OPTion")
        self._stop = DiagLoopStop(device, f"{self._cmd_syntax}:STOP")

    @property
    def option(self) -> DiagLoopOption:
        """Return the ``DIAg:LOOP:OPTion`` command.

        Description:
            - This command sets or queries the type of looping desired.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:LOOP:OPTion?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:LOOP:OPTion?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DIAg:LOOP:OPTion value`` command.

        SCPI Syntax:
            ```
            - DIAg:LOOP:OPTion {FAIL|ONCE|ALWAYS|ONFAIL|NTIMES}
            - DIAg:LOOP:OPTion?
            ```

        Info:
            - ``Fail`` - run until a failure is found, then halt.
            - ``Once`` - run through one loop.
            - ``Always`` - run forever.
            - ``Onfail`` - run until a failure is found, then loop on it.
            - ``Ntimes`` - run n number of loops.

        Sub-properties:
            - ``.ntimes``: The ``DIAg:LOOP:OPTion:NTIMes`` command.
        """
        return self._option

    @property
    def stop(self) -> DiagLoopStop:
        """Return the ``DIAg:LOOP:STOP`` command.

        Description:
            - Request that diagnostics stop looping.

        Usage:
            - Using the ``.write()`` method will send the ``DIAg:LOOP:STOP`` command.

        SCPI Syntax:
            ```
            - DIAg:LOOP:STOP
            ```
        """
        return self._stop


class Diag(SCPICmdRead):
    """The ``DIAg`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.loop``: The ``DIAg:LOOP`` command tree.
        - ``.mode``: The ``DIAg:MODe`` command.
        - ``.result``: The ``DIAg:RESUlt`` command.
        - ``.select``: The ``DIAg:SELect`` command.
        - ``.state``: The ``DIAg:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "DIAg") -> None:
        super().__init__(device, cmd_syntax)
        self._loop = DiagLoop(device, f"{self._cmd_syntax}:LOOP")
        self._mode = DiagMode(device, f"{self._cmd_syntax}:MODe")
        self._result = DiagResult(device, f"{self._cmd_syntax}:RESUlt")
        self._select = DiagSelect(device, f"{self._cmd_syntax}:SELect")
        self._state = DiagState(device, f"{self._cmd_syntax}:STATE")

    @property
    def loop(self) -> DiagLoop:
        """Return the ``DIAg:LOOP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:LOOP?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:LOOP?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.option``: The ``DIAg:LOOP:OPTion`` command.
            - ``.stop``: The ``DIAg:LOOP:STOP`` command.
        """
        return self._loop

    @property
    def mode(self) -> DiagMode:
        """Return the ``DIAg:MODe`` command.

        Description:
            - This command sets or queries the diagnostics mode.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:MODe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DIAg:MODe value`` command.

        SCPI Syntax:
            ```
            - DIAg:MODe {POST|EXTENDED|SERVICE}
            - DIAg:MODe?
            ```

        Info:
            - ``POST`` specifies the power on self test diagnostics.
            - ``EXTENDED`` specifies the extended diagnostics.
            - ``SERVICE`` specifies the service diagnostics.
        """
        return self._mode

    @property
    def result(self) -> DiagResult:
        """Return the ``DIAg:RESUlt`` command.

        Description:
            - This query returns both the overall diagnostics test results and the results of each
              individual test area.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:RESUlt?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:RESUlt?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAg:RESUlt?
            ```

        Sub-properties:
            - ``.flag``: The ``DIAg:RESUlt:FLAg`` command.
            - ``.log``: The ``DIAg:RESUlt:LOG`` command.
        """
        return self._result

    @property
    def select(self) -> DiagSelect:
        """Return the ``DIAg:SELect`` command.

        Description:
            - This command selects or queries an available diagnostic area.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:SELect?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:SELect?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DIAg:SELect value`` command.

        SCPI Syntax:
            ```
            - DIAg:SELect {ALL|IO|ANALOG|SYSTEM|ASIC|ACQ|SIGNAL|MEMORY}
            - DIAg:SELect?
            ```

        Info:
            - ``ALL``
            - ``IO``
            - ``ANALOG``
            - ``SYSTEM``
            - ``ASIC``
            - ``ACQ``
            - ``SIGNAL``
            - ``MEMORY``
        """
        return self._select

    @property
    def state(self) -> DiagState:
        """Return the ``DIAg:STATE`` command.

        Description:
            - This command starts or aborts Self Test. Abort happens after group under test
              completes.

        Usage:
            - Using the ``.write(value)`` method will send the ``DIAg:STATE value`` command.

        SCPI Syntax:
            ```
            - DIAg:STATE {EXECute|ABOrt}
            ```

        Info:
            - ``EXECUTE`` starts execution of the diagnostics.
            - ``ABOrt`` disables diagnostics capabilities and returns the instrument to a normal
              operating state.
        """
        return self._state
