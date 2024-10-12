"""The pilogger commands module.

These commands are used in the following models:
LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - PILOGger:FILEName <QString>
    - PILOGger:FILEName?
    - PILOGger:STATE {ON|OFF|<NR1>}
    - PILOGger:STATE?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class PiloggerState(SCPICmdWrite, SCPICmdRead):
    """The ``PILOGger:STATE`` command.

    Description:
        - This command sets or queries the state of the programmatic interface command log. If the
          location specified by ``PILOGGER:FILENAME`` does not exist or is not writable, attempts to
          turn the PI command logger ON will fail, and the state will be set to 0 (OFF).

    Usage:
        - Using the ``.query()`` method will send the ``PILOGger:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``PILOGger:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PILOGger:STATE value`` command.

    SCPI Syntax:
        ```
        - PILOGger:STATE {ON|OFF|<NR1>}
        - PILOGger:STATE?
        ```

    Info:
        - ``<NR1>`` = 0 disables the PI command logger; any other value turns the PI command logger
          on.
        - ``OFF`` disables the PI command logger.
        - ``ON`` enables the PI command logger.
    """


class PiloggerFilename(SCPICmdWrite, SCPICmdRead):
    """The ``PILOGger:FILEName`` command.

    Description:
        - This command sets or queries the location where the programmatic interface command log
          will be saved.

    Usage:
        - Using the ``.query()`` method will send the ``PILOGger:FILEName?`` query.
        - Using the ``.verify(value)`` method will send the ``PILOGger:FILEName?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PILOGger:FILEName value`` command.

    SCPI Syntax:
        ```
        - PILOGger:FILEName <QString>
        - PILOGger:FILEName?
        ```

    Info:
        - ``<QString>`` is a quoted string that defines the file path that specifies the location to
          save the command log, in the format '[<path>]<filename.ext>'. Specifying a path is
          optional. If no path is entered, the instrument will search in the current working
          directory as set in ``FILESYSTEM:CWD``.
    """

    _WRAP_ARG_WITH_QUOTES = True


class Pilogger(SCPICmdRead):
    """The ``PILOGger`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``PILOGger?`` query.
        - Using the ``.verify(value)`` method will send the ``PILOGger?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.filename``: The ``PILOGger:FILEName`` command.
        - ``.state``: The ``PILOGger:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "PILOGger") -> None:
        super().__init__(device, cmd_syntax)
        self._filename = PiloggerFilename(device, f"{self._cmd_syntax}:FILEName")
        self._state = PiloggerState(device, f"{self._cmd_syntax}:STATE")

    @property
    def filename(self) -> PiloggerFilename:
        """Return the ``PILOGger:FILEName`` command.

        Description:
            - This command sets or queries the location where the programmatic interface command log
              will be saved.

        Usage:
            - Using the ``.query()`` method will send the ``PILOGger:FILEName?`` query.
            - Using the ``.verify(value)`` method will send the ``PILOGger:FILEName?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PILOGger:FILEName value`` command.

        SCPI Syntax:
            ```
            - PILOGger:FILEName <QString>
            - PILOGger:FILEName?
            ```

        Info:
            - ``<QString>`` is a quoted string that defines the file path that specifies the
              location to save the command log, in the format '[<path>]<filename.ext>'. Specifying a
              path is optional. If no path is entered, the instrument will search in the current
              working directory as set in ``FILESYSTEM:CWD``.
        """
        return self._filename

    @property
    def state(self) -> PiloggerState:
        """Return the ``PILOGger:STATE`` command.

        Description:
            - This command sets or queries the state of the programmatic interface command log. If
              the location specified by ``PILOGGER:FILENAME`` does not exist or is not writable,
              attempts to turn the PI command logger ON will fail, and the state will be set to 0
              (OFF).

        Usage:
            - Using the ``.query()`` method will send the ``PILOGger:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``PILOGger:STATE?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PILOGger:STATE value`` command.

        SCPI Syntax:
            ```
            - PILOGger:STATE {ON|OFF|<NR1>}
            - PILOGger:STATE?
            ```

        Info:
            - ``<NR1>`` = 0 disables the PI command logger; any other value turns the PI command
              logger on.
            - ``OFF`` disables the PI command logger.
            - ``ON`` enables the PI command logger.
        """
        return self._state
