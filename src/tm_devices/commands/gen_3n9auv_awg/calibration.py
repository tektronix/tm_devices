"""The calibration commands module.

These commands are used in the following models:
AWG5200, AWG70KA, AWG70KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CALibration:ABORt
    - CALibration:ALL
    - CALibration:ALL?
    - CALibration:CATalog? [{ALL|<subsystem>}[,{ALL|<area>}]]
    - CALibration:LOG:CLEar
    - CALibration:LOG:FAILuresonly {OFF|ON|0|1}
    - CALibration:LOG:FAILuresonly?
    - CALibration:LOG?
    - CALibration:RESTore
    - CALibration:RESult:TEMPerature?
    - CALibration:RESult:TIME?
    - CALibration:RESult?
    - CALibration:RUNNing?
    - CALibration:STARt
    - CALibration:STATe:FACTory? [<subsystem>][,<area>]]
    - CALibration:STATe:USER? [<subsystem>[,<area>]]
    - CALibration:STOP:STATe?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdReadWithArguments, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class CalibrationStopState(SCPICmdRead):
    """The ``CALibration:STOP:STATe`` command.

    Description:
        - This command returns the state of the calibration procedure.

    Usage:
        - Using the ``.query()`` method will send the ``CALibration:STOP:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibration:STOP:STATe?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibration:STOP:STATe?
        ```
    """


class CalibrationStop(SCPICmdRead):
    """The ``CALibration:STOP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CALibration:STOP?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibration:STOP?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``CALibration:STOP:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = CalibrationStopState(device, f"{self._cmd_syntax}:STATe")

    @property
    def state(self) -> CalibrationStopState:
        """Return the ``CALibration:STOP:STATe`` command.

        Description:
            - This command returns the state of the calibration procedure.

        Usage:
            - Using the ``.query()`` method will send the ``CALibration:STOP:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibration:STOP:STATe?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibration:STOP:STATe?
            ```
        """
        return self._state


class CalibrationStateUser(SCPICmdReadWithArguments):
    """The ``CALibration:STATe:USER`` command.

    Description:
        - This command returns the current user state of the calibration for the AWG. A calibration
          state will be Calibrated or Uncalibrated. Areas will be calibrated when all procedures for
          that area have been executed and passed. Subsystems will be calibrated when all areas for
          that subsystem are calibrated. Each calibrated (as opposed to uncalibrated) state will
          have a temperature and date time. An uncalibrated state will not have a valid temperature
          or date time and should be ignored.

    Usage:
        - Using the ``.query(argument)`` method will send the ``CALibration:STATe:USER? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``CALibration:STATe:USER? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibration:STATe:USER? [<subsystem>[,<area>]]
        ```
    """


class CalibrationStateFactory(SCPICmdReadWithArguments):
    """The ``CALibration:STATe:FACTory`` command.

    Description:
        - This command returns the current factory state of the calibration for the AWG. A
          calibration state will be Calibrated or Uncalibrated. Areas will be calibrated when all
          procedures for that area have been executed and passed. Subsystems will be calibrated when
          all areas for that subsystem are calibrated. Each calibrated (as opposed to uncalibrated)
          state will have a temperature and date time. An uncalibrated state will not have a valid
          temperature or date time and should be ignored.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``CALibration:STATe:FACTory? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``CALibration:STATe:FACTory? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibration:STATe:FACTory? [<subsystem>][,<area>]]
        ```
    """


class CalibrationState(SCPICmdRead):
    """The ``CALibration:STATe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CALibration:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibration:STATe?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.factory``: The ``CALibration:STATe:FACTory`` command.
        - ``.user``: The ``CALibration:STATe:USER`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._factory = CalibrationStateFactory(device, f"{self._cmd_syntax}:FACTory")
        self._user = CalibrationStateUser(device, f"{self._cmd_syntax}:USER")

    @property
    def factory(self) -> CalibrationStateFactory:
        """Return the ``CALibration:STATe:FACTory`` command.

        Description:
            - This command returns the current factory state of the calibration for the AWG. A
              calibration state will be Calibrated or Uncalibrated. Areas will be calibrated when
              all procedures for that area have been executed and passed. Subsystems will be
              calibrated when all areas for that subsystem are calibrated. Each calibrated (as
              opposed to uncalibrated) state will have a temperature and date time. An uncalibrated
              state will not have a valid temperature or date time and should be ignored.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``CALibration:STATe:FACTory? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``CALibration:STATe:FACTory? argument`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibration:STATe:FACTory? [<subsystem>][,<area>]]
            ```
        """
        return self._factory

    @property
    def user(self) -> CalibrationStateUser:
        """Return the ``CALibration:STATe:USER`` command.

        Description:
            - This command returns the current user state of the calibration for the AWG. A
              calibration state will be Calibrated or Uncalibrated. Areas will be calibrated when
              all procedures for that area have been executed and passed. Subsystems will be
              calibrated when all areas for that subsystem are calibrated. Each calibrated (as
              opposed to uncalibrated) state will have a temperature and date time. An uncalibrated
              state will not have a valid temperature or date time and should be ignored.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``CALibration:STATe:USER? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``CALibration:STATe:USER? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibration:STATe:USER? [<subsystem>[,<area>]]
            ```
        """
        return self._user


class CalibrationStart(SCPICmdWriteNoArguments):
    """The ``CALibration:STARt`` command.

    Description:
        - This command starts the calibration.

    Usage:
        - Using the ``.write()`` method will send the ``CALibration:STARt`` command.

    SCPI Syntax:
        ```
        - CALibration:STARt
        ```
    """


class CalibrationRunning(SCPICmdRead):
    """The ``CALibration:RUNNing`` command.

    Description:
        - This command returns the name of the subsystem, area, and procedure in progress. This
          command can be issued while procedure is in progress.

    Usage:
        - Using the ``.query()`` method will send the ``CALibration:RUNNing?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibration:RUNNing?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibration:RUNNing?
        ```
    """


class CalibrationResultTime(SCPICmdRead):
    """The ``CALibration:RESult:TIME`` command.

    Description:
        - This command returns the time of the last calibration.

    Usage:
        - Using the ``.query()`` method will send the ``CALibration:RESult:TIME?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibration:RESult:TIME?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibration:RESult:TIME?
        ```
    """


class CalibrationResultTemperature(SCPICmdRead):
    """The ``CALibration:RESult:TEMPerature`` command.

    Description:
        - This command returns the temperature of the last calibration. All temperatures are in °C.

    Usage:
        - Using the ``.query()`` method will send the ``CALibration:RESult:TEMPerature?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibration:RESult:TEMPerature?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibration:RESult:TEMPerature?
        ```
    """


class CalibrationResult(SCPICmdRead):
    """The ``CALibration:RESult`` command.

    Description:
        - This command returns the status of the last calibration procedure. This query-only command
          can be issued while calibration is in progress.

    Usage:
        - Using the ``.query()`` method will send the ``CALibration:RESult?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibration:RESult?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibration:RESult?
        ```

    Properties:
        - ``.temperature``: The ``CALibration:RESult:TEMPerature`` command.
        - ``.time``: The ``CALibration:RESult:TIME`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._temperature = CalibrationResultTemperature(device, f"{self._cmd_syntax}:TEMPerature")
        self._time = CalibrationResultTime(device, f"{self._cmd_syntax}:TIME")

    @property
    def temperature(self) -> CalibrationResultTemperature:
        """Return the ``CALibration:RESult:TEMPerature`` command.

        Description:
            - This command returns the temperature of the last calibration. All temperatures are in
              °C.

        Usage:
            - Using the ``.query()`` method will send the ``CALibration:RESult:TEMPerature?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibration:RESult:TEMPerature?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibration:RESult:TEMPerature?
            ```
        """
        return self._temperature

    @property
    def time(self) -> CalibrationResultTime:
        """Return the ``CALibration:RESult:TIME`` command.

        Description:
            - This command returns the time of the last calibration.

        Usage:
            - Using the ``.query()`` method will send the ``CALibration:RESult:TIME?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibration:RESult:TIME?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibration:RESult:TIME?
            ```
        """
        return self._time


class CalibrationRestore(SCPICmdWriteNoArguments):
    """The ``CALibration:RESTore`` command.

    Description:
        - This command restores the calibration constants from the factory non-volatile memory and
          copied to user storage.

    Usage:
        - Using the ``.write()`` method will send the ``CALibration:RESTore`` command.

    SCPI Syntax:
        ```
        - CALibration:RESTore
        ```
    """


class CalibrationLogFailuresonly(SCPICmdWrite, SCPICmdRead):
    """The ``CALibration:LOG:FAILuresonly`` command.

    Description:
        - This command sets or returns the flag that controls the amount of result information saved
          into the log. This controls all tests that pass or fail or only tests that fail. It is
          important to note, that details are generated during the test, and need to be saved during
          the test execution.

    Usage:
        - Using the ``.query()`` method will send the ``CALibration:LOG:FAILuresonly?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibration:LOG:FAILuresonly?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CALibration:LOG:FAILuresonly value``
          command.

    SCPI Syntax:
        ```
        - CALibration:LOG:FAILuresonly {OFF|ON|0|1}
        - CALibration:LOG:FAILuresonly?
        ```

    Info:
        - ``*RST`` sets this to 0.
    """


class CalibrationLogClear(SCPICmdWriteNoArguments):
    """The ``CALibration:LOG:CLEar`` command.

    Description:
        - This command clears the results log. The command works when in the active mode for
          calibration. See the ``ACTIVE:MODE`` command.

    Usage:
        - Using the ``.write()`` method will send the ``CALibration:LOG:CLEar`` command.

    SCPI Syntax:
        ```
        - CALibration:LOG:CLEar
        ```
    """


class CalibrationLog(SCPICmdRead):
    """The ``CALibration:LOG`` command.

    Description:
        - This command returns a string of continuous concatenated calibration results. The start
          time is recorded plus one or more <cal ``path>:<cal`` name> <result>. This command can be
          issued while calibration is still in progress. Use the ``CALIBRATION:LOG:CLEAR`` command
          to start a fresh log and provide additional information. Log results are still valid if
          the calibration is aborted and the calibration constants are restored.

    Usage:
        - Using the ``.query()`` method will send the ``CALibration:LOG?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibration:LOG?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibration:LOG?
        ```

    Properties:
        - ``.clear``: The ``CALibration:LOG:CLEar`` command.
        - ``.failuresonly``: The ``CALibration:LOG:FAILuresonly`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._clear = CalibrationLogClear(device, f"{self._cmd_syntax}:CLEar")
        self._failuresonly = CalibrationLogFailuresonly(device, f"{self._cmd_syntax}:FAILuresonly")

    @property
    def clear(self) -> CalibrationLogClear:
        """Return the ``CALibration:LOG:CLEar`` command.

        Description:
            - This command clears the results log. The command works when in the active mode for
              calibration. See the ``ACTIVE:MODE`` command.

        Usage:
            - Using the ``.write()`` method will send the ``CALibration:LOG:CLEar`` command.

        SCPI Syntax:
            ```
            - CALibration:LOG:CLEar
            ```
        """
        return self._clear

    @property
    def failuresonly(self) -> CalibrationLogFailuresonly:
        """Return the ``CALibration:LOG:FAILuresonly`` command.

        Description:
            - This command sets or returns the flag that controls the amount of result information
              saved into the log. This controls all tests that pass or fail or only tests that fail.
              It is important to note, that details are generated during the test, and need to be
              saved during the test execution.

        Usage:
            - Using the ``.query()`` method will send the ``CALibration:LOG:FAILuresonly?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibration:LOG:FAILuresonly?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CALibration:LOG:FAILuresonly value`` command.

        SCPI Syntax:
            ```
            - CALibration:LOG:FAILuresonly {OFF|ON|0|1}
            - CALibration:LOG:FAILuresonly?
            ```

        Info:
            - ``*RST`` sets this to 0.
        """
        return self._failuresonly


class CalibrationCatalog(SCPICmdReadWithArguments):
    """The ``CALibration:CATalog`` command.

    Description:
        - This command returns the list of calibration procedures. All tests are grouped by areas.
          All areas are grouped by subsystems. The available subsystems, areas, and tests depend on
          the type of testing (such as POST or ALL).

    Usage:
        - Using the ``.query(argument)`` method will send the ``CALibration:CATalog? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``CALibration:CATalog? argument`` query and raise an AssertionError if the returned value
          does not match ``value``.

    SCPI Syntax:
        ```
        - CALibration:CATalog? [{ALL|<subsystem>}[,{ALL|<area>}]]
        ```
    """


class CalibrationAll(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``CALibration:ALL`` command.

    Description:
        - The CALibration[``:ALL``] command performs an internal calibration. The
          CALibration[``:ALL``]? command performs an internal calibration and returns 0 (Pass) or a
          calibration error code.

    Usage:
        - Using the ``.query()`` method will send the ``CALibration:ALL?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibration:ALL?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``CALibration:ALL`` command.

    SCPI Syntax:
        ```
        - CALibration:ALL
        - CALibration:ALL?
        ```
    """


class CalibrationAbort(SCPICmdWriteNoArguments):
    """The ``CALibration:ABORt`` command.

    Description:
        - This command stops the self calibration process and restores the previous calibration
          constants.

    Usage:
        - Using the ``.write()`` method will send the ``CALibration:ABORt`` command.

    SCPI Syntax:
        ```
        - CALibration:ABORt
        ```
    """


#  pylint: disable=too-many-instance-attributes
class Calibration(SCPICmdRead):
    """The ``CALibration`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CALibration?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibration?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.abort``: The ``CALibration:ABORt`` command.
        - ``.catalog``: The ``CALibration:CATalog`` command.
        - ``.log``: The ``CALibration:LOG`` command.
        - ``.restore``: The ``CALibration:RESTore`` command.
        - ``.result``: The ``CALibration:RESult`` command.
        - ``.running``: The ``CALibration:RUNNing`` command.
        - ``.start``: The ``CALibration:STARt`` command.
        - ``.state``: The ``CALibration:STATe`` command tree.
        - ``.stop``: The ``CALibration:STOP`` command tree.
        - ``.all``: The ``CALibration:ALL`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "CALibration"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._abort = CalibrationAbort(device, f"{self._cmd_syntax}:ABORt")
        self._catalog = CalibrationCatalog(device, f"{self._cmd_syntax}:CATalog")
        self._log = CalibrationLog(device, f"{self._cmd_syntax}:LOG")
        self._restore = CalibrationRestore(device, f"{self._cmd_syntax}:RESTore")
        self._result = CalibrationResult(device, f"{self._cmd_syntax}:RESult")
        self._running = CalibrationRunning(device, f"{self._cmd_syntax}:RUNNing")
        self._start = CalibrationStart(device, f"{self._cmd_syntax}:STARt")
        self._state = CalibrationState(device, f"{self._cmd_syntax}:STATe")
        self._stop = CalibrationStop(device, f"{self._cmd_syntax}:STOP")
        self._all = CalibrationAll(device, f"{self._cmd_syntax}:ALL")

    @property
    def abort(self) -> CalibrationAbort:
        """Return the ``CALibration:ABORt`` command.

        Description:
            - This command stops the self calibration process and restores the previous calibration
              constants.

        Usage:
            - Using the ``.write()`` method will send the ``CALibration:ABORt`` command.

        SCPI Syntax:
            ```
            - CALibration:ABORt
            ```
        """
        return self._abort

    @property
    def catalog(self) -> CalibrationCatalog:
        """Return the ``CALibration:CATalog`` command.

        Description:
            - This command returns the list of calibration procedures. All tests are grouped by
              areas. All areas are grouped by subsystems. The available subsystems, areas, and tests
              depend on the type of testing (such as POST or ALL).

        Usage:
            - Using the ``.query(argument)`` method will send the ``CALibration:CATalog? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``CALibration:CATalog? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibration:CATalog? [{ALL|<subsystem>}[,{ALL|<area>}]]
            ```
        """
        return self._catalog

    @property
    def log(self) -> CalibrationLog:
        """Return the ``CALibration:LOG`` command.

        Description:
            - This command returns a string of continuous concatenated calibration results. The
              start time is recorded plus one or more <cal ``path>:<cal`` name> <result>. This
              command can be issued while calibration is still in progress. Use the
              ``CALIBRATION:LOG:CLEAR`` command to start a fresh log and provide additional
              information. Log results are still valid if the calibration is aborted and the
              calibration constants are restored.

        Usage:
            - Using the ``.query()`` method will send the ``CALibration:LOG?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibration:LOG?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibration:LOG?
            ```

        Sub-properties:
            - ``.clear``: The ``CALibration:LOG:CLEar`` command.
            - ``.failuresonly``: The ``CALibration:LOG:FAILuresonly`` command.
        """
        return self._log

    @property
    def restore(self) -> CalibrationRestore:
        """Return the ``CALibration:RESTore`` command.

        Description:
            - This command restores the calibration constants from the factory non-volatile memory
              and copied to user storage.

        Usage:
            - Using the ``.write()`` method will send the ``CALibration:RESTore`` command.

        SCPI Syntax:
            ```
            - CALibration:RESTore
            ```
        """
        return self._restore

    @property
    def result(self) -> CalibrationResult:
        """Return the ``CALibration:RESult`` command.

        Description:
            - This command returns the status of the last calibration procedure. This query-only
              command can be issued while calibration is in progress.

        Usage:
            - Using the ``.query()`` method will send the ``CALibration:RESult?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibration:RESult?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibration:RESult?
            ```

        Sub-properties:
            - ``.temperature``: The ``CALibration:RESult:TEMPerature`` command.
            - ``.time``: The ``CALibration:RESult:TIME`` command.
        """
        return self._result

    @property
    def running(self) -> CalibrationRunning:
        """Return the ``CALibration:RUNNing`` command.

        Description:
            - This command returns the name of the subsystem, area, and procedure in progress. This
              command can be issued while procedure is in progress.

        Usage:
            - Using the ``.query()`` method will send the ``CALibration:RUNNing?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibration:RUNNing?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibration:RUNNing?
            ```
        """
        return self._running

    @property
    def start(self) -> CalibrationStart:
        """Return the ``CALibration:STARt`` command.

        Description:
            - This command starts the calibration.

        Usage:
            - Using the ``.write()`` method will send the ``CALibration:STARt`` command.

        SCPI Syntax:
            ```
            - CALibration:STARt
            ```
        """
        return self._start

    @property
    def state(self) -> CalibrationState:
        """Return the ``CALibration:STATe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CALibration:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibration:STATe?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.factory``: The ``CALibration:STATe:FACTory`` command.
            - ``.user``: The ``CALibration:STATe:USER`` command.
        """
        return self._state

    @property
    def stop(self) -> CalibrationStop:
        """Return the ``CALibration:STOP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CALibration:STOP?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibration:STOP?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``CALibration:STOP:STATe`` command.
        """
        return self._stop

    @property
    def all(self) -> CalibrationAll:
        """Return the ``CALibration:ALL`` command.

        Description:
            - The CALibration[``:ALL``] command performs an internal calibration. The
              CALibration[``:ALL``]? command performs an internal calibration and returns 0 (Pass)
              or a calibration error code.

        Usage:
            - Using the ``.query()`` method will send the ``CALibration:ALL?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibration:ALL?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``CALibration:ALL`` command.

        SCPI Syntax:
            ```
            - CALibration:ALL
            - CALibration:ALL?
            ```
        """
        return self._all
