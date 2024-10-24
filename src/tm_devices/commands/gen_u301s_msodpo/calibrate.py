"""The calibrate commands module.

These commands are used in the following models:
DPO2K, DPO2KB, MSO2K, MSO2KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CALibrate:FACtory {STARt|CONTinue|PREVious|ABOrt|DUmp}
    - CALibrate:FACtory:STATus?
    - CALibrate:INTERNal
    - CALibrate:INTERNal:STARt
    - CALibrate:INTERNal:STATus?
    - CALibrate:POWerupstatus?
    - CALibrate:RESults:FACtory?
    - CALibrate:RESults:SPC?
    - CALibrate:RESults?
    - CALibrate:TEMPerature?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class CalibrateTemperature(SCPICmdRead):
    """The ``CALibrate:TEMPerature`` command.

    Description:
        - Returns the oscilloscope temperature at the time the SPC was run.

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:TEMPerature?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:TEMPerature?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibrate:TEMPerature?
        ```
    """


class CalibrateResultsSpc(SCPICmdRead):
    """The ``CALibrate:RESults:SPC`` command.

    Description:
        - Returns the status of the SPC operation. This query does not initiate a SPC.

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:RESults:SPC?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:RESults:SPC?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibrate:RESults:SPC?
        ```
    """


class CalibrateResultsFactory(SCPICmdRead):
    """The ``CALibrate:RESults:FACtory`` command.

    Description:
        - Returns the status of internal and factory calibration, without performing any calibration
          operations.

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:RESults:FACtory?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:RESults:FACtory?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibrate:RESults:FACtory?
        ```
    """


class CalibrateResults(SCPICmdRead):
    """The ``CALibrate:RESults`` command.

    Description:
        - Returns the status of internal and factory calibrations, without performing any
          calibration operations. The results returned do not include the calibration status of
          attached probes. The query is intended to support GO/NoGO testing of the oscilloscope
          calibration readiness: all returned results should indicate PASS status if the
          oscilloscope is 'fit for duty'. It is quite common, however, to use uncalibrated probes
          (particularly when the oscilloscope inputs are connected into a test system with coaxial
          cables).

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:RESults?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:RESults?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibrate:RESults?
        ```

    Properties:
        - ``.factory``: The ``CALibrate:RESults:FACtory`` command.
        - ``.spc``: The ``CALibrate:RESults:SPC`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._factory = CalibrateResultsFactory(device, f"{self._cmd_syntax}:FACtory")
        self._spc = CalibrateResultsSpc(device, f"{self._cmd_syntax}:SPC")

    @property
    def factory(self) -> CalibrateResultsFactory:
        """Return the ``CALibrate:RESults:FACtory`` command.

        Description:
            - Returns the status of internal and factory calibration, without performing any
              calibration operations.

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:RESults:FACtory?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:RESults:FACtory?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibrate:RESults:FACtory?
            ```
        """
        return self._factory

    @property
    def spc(self) -> CalibrateResultsSpc:
        """Return the ``CALibrate:RESults:SPC`` command.

        Description:
            - Returns the status of the SPC operation. This query does not initiate a SPC.

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:RESults:SPC?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:RESults:SPC?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibrate:RESults:SPC?
            ```
        """
        return self._spc


class CalibratePowerupstatus(SCPICmdRead):
    """The ``CALibrate:POWerupstatus`` command.

    Description:
        - Returns the status of the oscilloscope following power on.

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:POWerupstatus?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:POWerupstatus?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibrate:POWerupstatus?
        ```
    """


class CalibrateInternalStatus(SCPICmdRead):
    """The ``CALibrate:INTERNal:STATus`` command.

    Description:
        - This query-only command returns the current status of the signal path calibration.

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:INTERNal:STATus?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:INTERNal:STATus?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibrate:INTERNal:STATus?
        ```
    """


class CalibrateInternalStart(SCPICmdWriteNoArguments):
    """The ``CALibrate:INTERNal:STARt`` command.

    Description:
        - This command (no query form) starts the signal path calibration (SPC) of the analog
          channels. This command is the same as the ``CALIBRATE:INTERNAL`` command. You can use the
          ``CALIBRATE:INTERNAL:STATUS`` query to return the current status of the signal path
          calibration of the instrument.

    Usage:
        - Using the ``.write()`` method will send the ``CALibrate:INTERNal:STARt`` command.

    SCPI Syntax:
        ```
        - CALibrate:INTERNal:STARt
        ```
    """


class CalibrateInternal(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``CALibrate:INTERNal`` command.

    Description:
        - This command (no query form) starts the signal path calibration (SPC) of the instrument.
          You can use the ``CALIBRATE:INTERNAL:STATUS`` query to return the current status of the
          signal path calibration of the instrument.

    Usage:
        - Using the ``.write()`` method will send the ``CALibrate:INTERNal`` command.

    SCPI Syntax:
        ```
        - CALibrate:INTERNal
        ```

    Properties:
        - ``.start``: The ``CALibrate:INTERNal:STARt`` command.
        - ``.status``: The ``CALibrate:INTERNal:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._start = CalibrateInternalStart(device, f"{self._cmd_syntax}:STARt")
        self._status = CalibrateInternalStatus(device, f"{self._cmd_syntax}:STATus")

    @property
    def start(self) -> CalibrateInternalStart:
        """Return the ``CALibrate:INTERNal:STARt`` command.

        Description:
            - This command (no query form) starts the signal path calibration (SPC) of the analog
              channels. This command is the same as the ``CALIBRATE:INTERNAL`` command. You can use
              the ``CALIBRATE:INTERNAL:STATUS`` query to return the current status of the signal
              path calibration of the instrument.

        Usage:
            - Using the ``.write()`` method will send the ``CALibrate:INTERNal:STARt`` command.

        SCPI Syntax:
            ```
            - CALibrate:INTERNal:STARt
            ```
        """
        return self._start

    @property
    def status(self) -> CalibrateInternalStatus:
        """Return the ``CALibrate:INTERNal:STATus`` command.

        Description:
            - This query-only command returns the current status of the signal path calibration.

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:INTERNal:STATus?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:INTERNal:STATus?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibrate:INTERNal:STATus?
            ```
        """
        return self._status


class CalibrateFactoryStatus(SCPICmdRead):
    """The ``CALibrate:FACtory:STATus`` command.

    Description:
        - Returns the factory calibration status value saved in nonvolatile memory.

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:FACtory:STATus?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:FACtory:STATus?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibrate:FACtory:STATus?
        ```
    """


class CalibrateFactory(SCPICmdWrite, SCPICmdRead):
    """The ``CALibrate:FACtory`` command.

    Description:
        - Provides the controls for starting and stopping the factory calibration process. The
          factory calibration process consists of a series of steps.

    Usage:
        - Using the ``.write(value)`` method will send the ``CALibrate:FACtory value`` command.

    SCPI Syntax:
        ```
        - CALibrate:FACtory {STARt|CONTinue|PREVious|ABOrt|DUmp}
        ```

    Info:
        - ``STARt`` initializes the factory calibration sequence and starts the first calibration
          step.
        - ``CONTinue`` begins the next factory calibration step.
        - ``PREVious`` attempts to run the most recent factory calibration step again.
        - ``ABOrt`` stops the calibration process.
        - ``DUmp`` stops the calibration and prints the calibration constants.

    Properties:
        - ``.status``: The ``CALibrate:FACtory:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._status = CalibrateFactoryStatus(device, f"{self._cmd_syntax}:STATus")

    @property
    def status(self) -> CalibrateFactoryStatus:
        """Return the ``CALibrate:FACtory:STATus`` command.

        Description:
            - Returns the factory calibration status value saved in nonvolatile memory.

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:FACtory:STATus?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:FACtory:STATus?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibrate:FACtory:STATus?
            ```
        """
        return self._status


class Calibrate(SCPICmdRead):
    """The ``CALibrate`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.factory``: The ``CALibrate:FACtory`` command.
        - ``.internal``: The ``CALibrate:INTERNal`` command.
        - ``.powerupstatus``: The ``CALibrate:POWerupstatus`` command.
        - ``.results``: The ``CALibrate:RESults`` command.
        - ``.temperature``: The ``CALibrate:TEMPerature`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "CALibrate") -> None:
        super().__init__(device, cmd_syntax)
        self._factory = CalibrateFactory(device, f"{self._cmd_syntax}:FACtory")
        self._internal = CalibrateInternal(device, f"{self._cmd_syntax}:INTERNal")
        self._powerupstatus = CalibratePowerupstatus(device, f"{self._cmd_syntax}:POWerupstatus")
        self._results = CalibrateResults(device, f"{self._cmd_syntax}:RESults")
        self._temperature = CalibrateTemperature(device, f"{self._cmd_syntax}:TEMPerature")

    @property
    def factory(self) -> CalibrateFactory:
        """Return the ``CALibrate:FACtory`` command.

        Description:
            - Provides the controls for starting and stopping the factory calibration process. The
              factory calibration process consists of a series of steps.

        Usage:
            - Using the ``.write(value)`` method will send the ``CALibrate:FACtory value`` command.

        SCPI Syntax:
            ```
            - CALibrate:FACtory {STARt|CONTinue|PREVious|ABOrt|DUmp}
            ```

        Info:
            - ``STARt`` initializes the factory calibration sequence and starts the first
              calibration step.
            - ``CONTinue`` begins the next factory calibration step.
            - ``PREVious`` attempts to run the most recent factory calibration step again.
            - ``ABOrt`` stops the calibration process.
            - ``DUmp`` stops the calibration and prints the calibration constants.

        Sub-properties:
            - ``.status``: The ``CALibrate:FACtory:STATus`` command.
        """
        return self._factory

    @property
    def internal(self) -> CalibrateInternal:
        """Return the ``CALibrate:INTERNal`` command.

        Description:
            - This command (no query form) starts the signal path calibration (SPC) of the
              instrument. You can use the ``CALIBRATE:INTERNAL:STATUS`` query to return the current
              status of the signal path calibration of the instrument.

        Usage:
            - Using the ``.write()`` method will send the ``CALibrate:INTERNal`` command.

        SCPI Syntax:
            ```
            - CALibrate:INTERNal
            ```

        Sub-properties:
            - ``.start``: The ``CALibrate:INTERNal:STARt`` command.
            - ``.status``: The ``CALibrate:INTERNal:STATus`` command.
        """
        return self._internal

    @property
    def powerupstatus(self) -> CalibratePowerupstatus:
        """Return the ``CALibrate:POWerupstatus`` command.

        Description:
            - Returns the status of the oscilloscope following power on.

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:POWerupstatus?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:POWerupstatus?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibrate:POWerupstatus?
            ```
        """
        return self._powerupstatus

    @property
    def results(self) -> CalibrateResults:
        """Return the ``CALibrate:RESults`` command.

        Description:
            - Returns the status of internal and factory calibrations, without performing any
              calibration operations. The results returned do not include the calibration status of
              attached probes. The query is intended to support GO/NoGO testing of the oscilloscope
              calibration readiness: all returned results should indicate PASS status if the
              oscilloscope is 'fit for duty'. It is quite common, however, to use uncalibrated
              probes (particularly when the oscilloscope inputs are connected into a test system
              with coaxial cables).

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:RESults?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:RESults?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibrate:RESults?
            ```

        Sub-properties:
            - ``.factory``: The ``CALibrate:RESults:FACtory`` command.
            - ``.spc``: The ``CALibrate:RESults:SPC`` command.
        """
        return self._results

    @property
    def temperature(self) -> CalibrateTemperature:
        """Return the ``CALibrate:TEMPerature`` command.

        Description:
            - Returns the oscilloscope temperature at the time the SPC was run.

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:TEMPerature?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:TEMPerature?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibrate:TEMPerature?
            ```
        """
        return self._temperature
