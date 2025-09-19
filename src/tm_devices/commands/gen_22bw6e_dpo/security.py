"""The security commands module.

These commands are used in the following models:
DPO7AX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SECurity:LOGger:STATe {ON|OFF|<NR1>}
    - SECurity:LOGger:STATe?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class SecurityLoggerState(SCPICmdWrite, SCPICmdRead):
    """The ``SECurity:LOGger:STATe`` command.

    Description:
        - This command sets or queries the state of the security log. The security log records
          security activities to the securitylog.txt file, which is present when exporting log
          files. When OFF, the security log stops recording new activity, but all previous activity
          is still present when exporting log files.

    Usage:
        - Using the ``.query()`` method will send the ``SECurity:LOGger:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``SECurity:LOGger:STATe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SECurity:LOGger:STATe value`` command.

    SCPI Syntax:
        ```
        - SECurity:LOGger:STATe {ON|OFF|<NR1>}
        - SECurity:LOGger:STATe?
        ```

    Info:
        - ``<NR1>`` 0 disables the security logger; any other value enables the security logger.
        - ``OFF`` disables the security logger.
        - ``ON`` enables the security logger.
    """


class SecurityLogger(SCPICmdRead):
    """The ``SECurity:LOGger`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SECurity:LOGger?`` query.
        - Using the ``.verify(value)`` method will send the ``SECurity:LOGger?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``SECurity:LOGger:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = SecurityLoggerState(device, f"{self._cmd_syntax}:STATe")

    @property
    def state(self) -> SecurityLoggerState:
        """Return the ``SECurity:LOGger:STATe`` command.

        Description:
            - This command sets or queries the state of the security log. The security log records
              security activities to the securitylog.txt file, which is present when exporting log
              files. When OFF, the security log stops recording new activity, but all previous
              activity is still present when exporting log files.

        Usage:
            - Using the ``.query()`` method will send the ``SECurity:LOGger:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``SECurity:LOGger:STATe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SECurity:LOGger:STATe value``
              command.

        SCPI Syntax:
            ```
            - SECurity:LOGger:STATe {ON|OFF|<NR1>}
            - SECurity:LOGger:STATe?
            ```

        Info:
            - ``<NR1>`` 0 disables the security logger; any other value enables the security logger.
            - ``OFF`` disables the security logger.
            - ``ON`` enables the security logger.
        """
        return self._state


class Security(SCPICmdRead):
    """The ``SECurity`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SECurity?`` query.
        - Using the ``.verify(value)`` method will send the ``SECurity?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.logger``: The ``SECurity:LOGger`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SECurity") -> None:
        super().__init__(device, cmd_syntax)
        self._logger = SecurityLogger(device, f"{self._cmd_syntax}:LOGger")

    @property
    def logger(self) -> SecurityLogger:
        """Return the ``SECurity:LOGger`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SECurity:LOGger?`` query.
            - Using the ``.verify(value)`` method will send the ``SECurity:LOGger?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``SECurity:LOGger:STATe`` command.
        """
        return self._logger
