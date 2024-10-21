"""The calibrate commands module.

These commands are used in the following models:
LPD6, MSO2, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CALibrate:INTERNal
    - CALibrate:INTERNal:STARt
    - CALibrate:INTERNal:STATus?
    - CALibrate:PWRUpstatus?
    - CALibrate?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class CalibratePwrupstatus(SCPICmdRead):
    """The ``CALibrate:PWRUpstatus`` command.

    Description:
        - This query-only command returns the current status of the power-up calibration.

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:PWRUpstatus?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:PWRUpstatus?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibrate:PWRUpstatus?
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


class Calibrate(SCPICmdRead):
    """The ``CALibrate`` command.

    Description:
        - This query returns the status of signal path calibration.

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibrate?
        ```

    Properties:
        - ``.internal``: The ``CALibrate:INTERNal`` command.
        - ``.pwrupstatus``: The ``CALibrate:PWRUpstatus`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "CALibrate") -> None:
        super().__init__(device, cmd_syntax)
        self._internal = CalibrateInternal(device, f"{self._cmd_syntax}:INTERNal")
        self._pwrupstatus = CalibratePwrupstatus(device, f"{self._cmd_syntax}:PWRUpstatus")

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
    def pwrupstatus(self) -> CalibratePwrupstatus:
        """Return the ``CALibrate:PWRUpstatus`` command.

        Description:
            - This query-only command returns the current status of the power-up calibration.

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:PWRUpstatus?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:PWRUpstatus?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibrate:PWRUpstatus?
            ```
        """
        return self._pwrupstatus
