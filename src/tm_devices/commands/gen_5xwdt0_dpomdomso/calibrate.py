"""The calibrate commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CALibrate:FACtory:AFG:VALue <NR3>
    - CALibrate:FACtory:STATus:AFG?
    - CALibrate:FACtory:STATus:RF?
    - CALibrate:FACtory:STATus:SCOPE?
    - CALibrate:FACtory:STATus?
    - CALibrate:INTERNal
    - CALibrate:INTERNal:STARt
    - CALibrate:INTERNal:STATus:RF?
    - CALibrate:INTERNal:STATus:SCOPE?
    - CALibrate:INTERNal:STATus?
    - CALibrate:POWerupstatus?
    - CALibrate:RESults:FACtory:AFG?
    - CALibrate:RESults:FACtory:RF?
    - CALibrate:RESults:FACtory:SCOPE?
    - CALibrate:RESults:FACtory?
    - CALibrate:RESults:SPC:RF?
    - CALibrate:RESults:SPC:SCOPE?
    - CALibrate:RESults:SPC?
    - CALibrate:RESults?
    - CALibrate:RF
    - CALibrate:RF:STARt
    - CALibrate:RF:STATus?
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


class CalibrateRfStatus(SCPICmdRead):
    """The ``CALibrate:RF:STATus`` command.

    Description:
        - This query returns the status of the last RF calibration.

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:RF:STATus?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:RF:STATus?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibrate:RF:STATus?
        ```
    """


class CalibrateRfStart(SCPICmdWriteNoArguments):
    """The ``CALibrate:RF:STARt`` command.

    Description:
        - This command is identical to ``CALIBRATE:RF``.

    Usage:
        - Using the ``.write()`` method will send the ``CALibrate:RF:STARt`` command.

    SCPI Syntax:
        ```
        - CALibrate:RF:STARt
        ```
    """


class CalibrateRf(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``CALibrate:RF`` command.

    Description:
        - This command begins the RF calibration process. You should first disconnect all cables and
          probes from the RF input before using this command. The calibration process takes
          approximately 3 minutes. This command is identical to ``CALibrate:RF:STARt``.

    Usage:
        - Using the ``.write()`` method will send the ``CALibrate:RF`` command.

    SCPI Syntax:
        ```
        - CALibrate:RF
        ```

    Properties:
        - ``.start``: The ``CALibrate:RF:STARt`` command.
        - ``.status``: The ``CALibrate:RF:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._start = CalibrateRfStart(device, f"{self._cmd_syntax}:STARt")
        self._status = CalibrateRfStatus(device, f"{self._cmd_syntax}:STATus")

    @property
    def start(self) -> CalibrateRfStart:
        """Return the ``CALibrate:RF:STARt`` command.

        Description:
            - This command is identical to ``CALIBRATE:RF``.

        Usage:
            - Using the ``.write()`` method will send the ``CALibrate:RF:STARt`` command.

        SCPI Syntax:
            ```
            - CALibrate:RF:STARt
            ```
        """
        return self._start

    @property
    def status(self) -> CalibrateRfStatus:
        """Return the ``CALibrate:RF:STATus`` command.

        Description:
            - This query returns the status of the last RF calibration.

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:RF:STATus?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:RF:STATus?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibrate:RF:STATus?
            ```
        """
        return self._status


class CalibrateResultsSpcScope(SCPICmdRead):
    """The ``CALibrate:RESults:SPC:SCOPE`` command.

    Description:
        - This query returns the status of the last SPC run for the oscilloscope portion of the
          instrument (doesn't include the RF portion). This query is synonymous to
          ``CALibrate:INTERNal:STATus:SCOPE?``

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:RESults:SPC:SCOPE?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:RESults:SPC:SCOPE?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibrate:RESults:SPC:SCOPE?
        ```
    """


class CalibrateResultsSpcRf(SCPICmdRead):
    """The ``CALibrate:RESults:SPC:RF`` command.

    Description:
        - This query returns the status of the last SPC run for the RF portion of the instrument
          (doesn't include analog channels) . This query is synonymous with
          ``CALibrate:INTERNal:STATus:RF?``

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:RESults:SPC:RF?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:RESults:SPC:RF?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibrate:RESults:SPC:RF?
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

    Properties:
        - ``.rf``: The ``CALibrate:RESults:SPC:RF`` command.
        - ``.scope``: The ``CALibrate:RESults:SPC:SCOPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._rf = CalibrateResultsSpcRf(device, f"{self._cmd_syntax}:RF")
        self._scope = CalibrateResultsSpcScope(device, f"{self._cmd_syntax}:SCOPE")

    @property
    def rf(self) -> CalibrateResultsSpcRf:
        """Return the ``CALibrate:RESults:SPC:RF`` command.

        Description:
            - This query returns the status of the last SPC run for the RF portion of the instrument
              (doesn't include analog channels) . This query is synonymous with
              ``CALibrate:INTERNal:STATus:RF?``

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:RESults:SPC:RF?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:RESults:SPC:RF?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibrate:RESults:SPC:RF?
            ```
        """
        return self._rf

    @property
    def scope(self) -> CalibrateResultsSpcScope:
        """Return the ``CALibrate:RESults:SPC:SCOPE`` command.

        Description:
            - This query returns the status of the last SPC run for the oscilloscope portion of the
              instrument (doesn't include the RF portion). This query is synonymous to
              ``CALibrate:INTERNal:STATus:SCOPE?``

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:RESults:SPC:SCOPE?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:RESults:SPC:SCOPE?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibrate:RESults:SPC:SCOPE?
            ```
        """
        return self._scope


class CalibrateResultsFactoryScope(SCPICmdRead):
    """The ``CALibrate:RESults:FACtory:SCOPE`` command.

    Description:
        - This query returns the factory calibration status for the oscilloscope (doesn't include RF
          or AFG) of the instrument. This query is synonymous with the following query:
          ``:CALibrateFACtory:STATus:SCOPE?``

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:RESults:FACtory:SCOPE?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:RESults:FACtory:SCOPE?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibrate:RESults:FACtory:SCOPE?
        ```
    """


class CalibrateResultsFactoryRf(SCPICmdRead):
    """The ``CALibrate:RESults:FACtory:RF`` command.

    Description:
        - This query returns the factory calibration status for the RF portion of the instrument, if
          present. This query is synonymous with ``CALibrate:FACtory:STATus:RF?``

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:RESults:FACtory:RF?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:RESults:FACtory:RF?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibrate:RESults:FACtory:RF?
        ```
    """


class CalibrateResultsFactoryAfg(SCPICmdRead):
    """The ``CALibrate:RESults:FACtory:AFG`` command.

    Description:
        - This query returns the factory calibration status for the Arbitrary Function Generator
          portion of the instrument, if present. This query is synonymous with
          ``CALibrate:FACtory:STATus:AFG?``

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:RESults:FACtory:AFG?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:RESults:FACtory:AFG?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibrate:RESults:FACtory:AFG?
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

    Properties:
        - ``.afg``: The ``CALibrate:RESults:FACtory:AFG`` command.
        - ``.rf``: The ``CALibrate:RESults:FACtory:RF`` command.
        - ``.scope``: The ``CALibrate:RESults:FACtory:SCOPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._afg = CalibrateResultsFactoryAfg(device, f"{self._cmd_syntax}:AFG")
        self._rf = CalibrateResultsFactoryRf(device, f"{self._cmd_syntax}:RF")
        self._scope = CalibrateResultsFactoryScope(device, f"{self._cmd_syntax}:SCOPE")

    @property
    def afg(self) -> CalibrateResultsFactoryAfg:
        """Return the ``CALibrate:RESults:FACtory:AFG`` command.

        Description:
            - This query returns the factory calibration status for the Arbitrary Function Generator
              portion of the instrument, if present. This query is synonymous with
              ``CALibrate:FACtory:STATus:AFG?``

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:RESults:FACtory:AFG?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:RESults:FACtory:AFG?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibrate:RESults:FACtory:AFG?
            ```
        """
        return self._afg

    @property
    def rf(self) -> CalibrateResultsFactoryRf:
        """Return the ``CALibrate:RESults:FACtory:RF`` command.

        Description:
            - This query returns the factory calibration status for the RF portion of the
              instrument, if present. This query is synonymous with ``CALibrate:FACtory:STATus:RF?``

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:RESults:FACtory:RF?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:RESults:FACtory:RF?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibrate:RESults:FACtory:RF?
            ```
        """
        return self._rf

    @property
    def scope(self) -> CalibrateResultsFactoryScope:
        """Return the ``CALibrate:RESults:FACtory:SCOPE`` command.

        Description:
            - This query returns the factory calibration status for the oscilloscope (doesn't
              include RF or AFG) of the instrument. This query is synonymous with the following
              query: ``:CALibrateFACtory:STATus:SCOPE?``

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:RESults:FACtory:SCOPE?``
              query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:RESults:FACtory:SCOPE?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibrate:RESults:FACtory:SCOPE?
            ```
        """
        return self._scope


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

        Sub-properties:
            - ``.afg``: The ``CALibrate:RESults:FACtory:AFG`` command.
            - ``.rf``: The ``CALibrate:RESults:FACtory:RF`` command.
            - ``.scope``: The ``CALibrate:RESults:FACtory:SCOPE`` command.
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

        Sub-properties:
            - ``.rf``: The ``CALibrate:RESults:SPC:RF`` command.
            - ``.scope``: The ``CALibrate:RESults:SPC:SCOPE`` command.
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


class CalibrateInternalStatusScope(SCPICmdRead):
    """The ``CALibrate:INTERNal:STATus:SCOPE`` command.

    Description:
        - This query returns the status of the last SPC run for the oscilloscope portion of the
          instrument (doesn't include the RF portion). To query the status of the RF portions, use
          ``CALIBRATE:INTERNAL:STATUS:RF This`` query is synonymous to
          ``CALIBRATE:RESULTS:SPC:SCOPE``

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:INTERNal:STATus:SCOPE?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:INTERNal:STATus:SCOPE?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibrate:INTERNal:STATus:SCOPE?
        ```
    """


class CalibrateInternalStatusRf(SCPICmdRead):
    """The ``CALibrate:INTERNal:STATus:RF`` command.

    Description:
        - This query returns the status of the last SPC run for the RF portion of the instrument:
          (doesn't include the analog channels). This query is synonymous with
          ``CALibrate:RESults:SPC:RF?``

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:INTERNal:STATus:RF?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:INTERNal:STATus:RF?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibrate:INTERNal:STATus:RF?
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

    Properties:
        - ``.rf``: The ``CALibrate:INTERNal:STATus:RF`` command.
        - ``.scope``: The ``CALibrate:INTERNal:STATus:SCOPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._rf = CalibrateInternalStatusRf(device, f"{self._cmd_syntax}:RF")
        self._scope = CalibrateInternalStatusScope(device, f"{self._cmd_syntax}:SCOPE")

    @property
    def rf(self) -> CalibrateInternalStatusRf:
        """Return the ``CALibrate:INTERNal:STATus:RF`` command.

        Description:
            - This query returns the status of the last SPC run for the RF portion of the
              instrument: (doesn't include the analog channels). This query is synonymous with
              ``CALibrate:RESults:SPC:RF?``

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:INTERNal:STATus:RF?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:INTERNal:STATus:RF?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibrate:INTERNal:STATus:RF?
            ```
        """
        return self._rf

    @property
    def scope(self) -> CalibrateInternalStatusScope:
        """Return the ``CALibrate:INTERNal:STATus:SCOPE`` command.

        Description:
            - This query returns the status of the last SPC run for the oscilloscope portion of the
              instrument (doesn't include the RF portion). To query the status of the RF portions,
              use ``CALIBRATE:INTERNAL:STATUS:RF This`` query is synonymous to
              ``CALIBRATE:RESULTS:SPC:SCOPE``

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:INTERNal:STATus:SCOPE?``
              query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:INTERNal:STATus:SCOPE?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibrate:INTERNal:STATus:SCOPE?
            ```
        """
        return self._scope


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

        Sub-properties:
            - ``.rf``: The ``CALibrate:INTERNal:STATus:RF`` command.
            - ``.scope``: The ``CALibrate:INTERNal:STATus:SCOPE`` command.
        """
        return self._status


class CalibrateFactoryStatusScope(SCPICmdRead):
    """The ``CALibrate:FACtory:STATus:SCOPE`` command.

    Description:
        - Returns the factory calibration status value saved in nonvolatile memory for the non-RF
          portion of the oscilloscope. It is synonymous with the
          ``:CALibrate:RESults:FACtory:SCOPE?`` query.

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:FACtory:STATus:SCOPE?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:FACtory:STATus:SCOPE?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibrate:FACtory:STATus:SCOPE?
        ```
    """


class CalibrateFactoryStatusRf(SCPICmdRead):
    """The ``CALibrate:FACtory:STATus:RF`` command.

    Description:
        - Returns the factory calibration status value saved in nonvolatile memory for the RF
          portion of the oscilloscope. This query is synonymous with
          ``CALIBRATE:RESULTS:FACTORY:RF``.

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:FACtory:STATus:RF?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:FACtory:STATus:RF?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibrate:FACtory:STATus:RF?
        ```
    """


class CalibrateFactoryStatusAfg(SCPICmdRead):
    """The ``CALibrate:FACtory:STATus:AFG`` command.

    Description:
        - This query returns the factory calibration status for the Arbitrary Function Generator
          portion of the instrument, if present. This query is synonymous with
          ``CALIBRATE:RESULTS:FACTORY:AFG``

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:FACtory:STATus:AFG?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:FACtory:STATus:AFG?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibrate:FACtory:STATus:AFG?
        ```
    """


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

    Properties:
        - ``.afg``: The ``CALibrate:FACtory:STATus:AFG`` command.
        - ``.rf``: The ``CALibrate:FACtory:STATus:RF`` command.
        - ``.scope``: The ``CALibrate:FACtory:STATus:SCOPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._afg = CalibrateFactoryStatusAfg(device, f"{self._cmd_syntax}:AFG")
        self._rf = CalibrateFactoryStatusRf(device, f"{self._cmd_syntax}:RF")
        self._scope = CalibrateFactoryStatusScope(device, f"{self._cmd_syntax}:SCOPE")

    @property
    def afg(self) -> CalibrateFactoryStatusAfg:
        """Return the ``CALibrate:FACtory:STATus:AFG`` command.

        Description:
            - This query returns the factory calibration status for the Arbitrary Function Generator
              portion of the instrument, if present. This query is synonymous with
              ``CALIBRATE:RESULTS:FACTORY:AFG``

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:FACtory:STATus:AFG?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:FACtory:STATus:AFG?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibrate:FACtory:STATus:AFG?
            ```
        """
        return self._afg

    @property
    def rf(self) -> CalibrateFactoryStatusRf:
        """Return the ``CALibrate:FACtory:STATus:RF`` command.

        Description:
            - Returns the factory calibration status value saved in nonvolatile memory for the RF
              portion of the oscilloscope. This query is synonymous with
              ``CALIBRATE:RESULTS:FACTORY:RF``.

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:FACtory:STATus:RF?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:FACtory:STATus:RF?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibrate:FACtory:STATus:RF?
            ```
        """
        return self._rf

    @property
    def scope(self) -> CalibrateFactoryStatusScope:
        """Return the ``CALibrate:FACtory:STATus:SCOPE`` command.

        Description:
            - Returns the factory calibration status value saved in nonvolatile memory for the
              non-RF portion of the oscilloscope. It is synonymous with the
              ``:CALibrate:RESults:FACtory:SCOPE?`` query.

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:FACtory:STATus:SCOPE?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:FACtory:STATus:SCOPE?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibrate:FACtory:STATus:SCOPE?
            ```
        """
        return self._scope


class CalibrateFactoryAfgValue(SCPICmdWrite):
    """The ``CALibrate:FACtory:AFG:VALue`` command.

    Description:
        - For steps that require the measurement value of a connected DVM or frequency counter, this
          command is used to send those values to the scope calibration software.

    Usage:
        - Using the ``.write(value)`` method will send the ``CALibrate:FACtory:AFG:VALue value``
          command.

    SCPI Syntax:
        ```
        - CALibrate:FACtory:AFG:VALue <NR3>
        ```
    """


class CalibrateFactoryAfg(SCPICmdRead):
    """The ``CALibrate:FACtory:AFG`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:FACtory:AFG?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:FACtory:AFG?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``CALibrate:FACtory:AFG:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = CalibrateFactoryAfgValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> CalibrateFactoryAfgValue:
        """Return the ``CALibrate:FACtory:AFG:VALue`` command.

        Description:
            - For steps that require the measurement value of a connected DVM or frequency counter,
              this command is used to send those values to the scope calibration software.

        Usage:
            - Using the ``.write(value)`` method will send the ``CALibrate:FACtory:AFG:VALue value``
              command.

        SCPI Syntax:
            ```
            - CALibrate:FACtory:AFG:VALue <NR3>
            ```
        """
        return self._value


class CalibrateFactory(SCPICmdRead):
    """The ``CALibrate:FACtory`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:FACtory?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:FACtory?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.afg``: The ``CALibrate:FACtory:AFG`` command tree.
        - ``.status``: The ``CALibrate:FACtory:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._afg = CalibrateFactoryAfg(device, f"{self._cmd_syntax}:AFG")
        self._status = CalibrateFactoryStatus(device, f"{self._cmd_syntax}:STATus")

    @property
    def afg(self) -> CalibrateFactoryAfg:
        """Return the ``CALibrate:FACtory:AFG`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:FACtory:AFG?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:FACtory:AFG?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``CALibrate:FACtory:AFG:VALue`` command.
        """
        return self._afg

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

        Sub-properties:
            - ``.afg``: The ``CALibrate:FACtory:STATus:AFG`` command.
            - ``.rf``: The ``CALibrate:FACtory:STATus:RF`` command.
            - ``.scope``: The ``CALibrate:FACtory:STATus:SCOPE`` command.
        """
        return self._status


class Calibrate(SCPICmdRead):
    """The ``CALibrate`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.factory``: The ``CALibrate:FACtory`` command tree.
        - ``.internal``: The ``CALibrate:INTERNal`` command.
        - ``.powerupstatus``: The ``CALibrate:POWerupstatus`` command.
        - ``.results``: The ``CALibrate:RESults`` command.
        - ``.rf``: The ``CALibrate:RF`` command.
        - ``.temperature``: The ``CALibrate:TEMPerature`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "CALibrate") -> None:
        super().__init__(device, cmd_syntax)
        self._factory = CalibrateFactory(device, f"{self._cmd_syntax}:FACtory")
        self._internal = CalibrateInternal(device, f"{self._cmd_syntax}:INTERNal")
        self._powerupstatus = CalibratePowerupstatus(device, f"{self._cmd_syntax}:POWerupstatus")
        self._results = CalibrateResults(device, f"{self._cmd_syntax}:RESults")
        self._rf = CalibrateRf(device, f"{self._cmd_syntax}:RF")
        self._temperature = CalibrateTemperature(device, f"{self._cmd_syntax}:TEMPerature")

    @property
    def factory(self) -> CalibrateFactory:
        """Return the ``CALibrate:FACtory`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:FACtory?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:FACtory?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.afg``: The ``CALibrate:FACtory:AFG`` command tree.
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
    def rf(self) -> CalibrateRf:
        """Return the ``CALibrate:RF`` command.

        Description:
            - This command begins the RF calibration process. You should first disconnect all cables
              and probes from the RF input before using this command. The calibration process takes
              approximately 3 minutes. This command is identical to ``CALibrate:RF:STARt``.

        Usage:
            - Using the ``.write()`` method will send the ``CALibrate:RF`` command.

        SCPI Syntax:
            ```
            - CALibrate:RF
            ```

        Sub-properties:
            - ``.start``: The ``CALibrate:RF:STARt`` command.
            - ``.status``: The ``CALibrate:RF:STATus`` command.
        """
        return self._rf

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
