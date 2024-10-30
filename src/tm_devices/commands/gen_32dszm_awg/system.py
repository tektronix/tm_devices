"""The system commands module.

These commands are used in the following models:
AWG5K, AWG5KC, AWG7K, AWG7KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SYSTem:DATE <year>,<month>,<day>
    - SYSTem:DATE?
    - SYSTem:ERRor:NEXT?
    - SYSTem:KLOCk <state>
    - SYSTem:KLOCk?
    - SYSTem:TIME <hour>,<minute>,<second>
    - SYSTem:TIME?
    - SYSTem:VERSion?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class SystemVersion(SCPICmdRead):
    """The ``SYSTem:VERSion`` command.

    Description:
        - This query-only command returns the conformed SCPI version of the instrument.

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem:VERSion?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:VERSion?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SYSTem:VERSion?
        ```
    """


class SystemTime(SCPICmdWrite, SCPICmdRead):
    """The ``SYSTem:TIME`` command.

    Description:
        - This command sets or returns the system time (hours, minutes and seconds). This command is
          equivalent to the time setting through the Windows Control Panel.

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem:TIME?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:TIME?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SYSTem:TIME value`` command.

    SCPI Syntax:
        ```
        - SYSTem:TIME <hour>,<minute>,<second>
        - SYSTem:TIME?
        ```
    """


class SystemKlock(SCPICmdWrite, SCPICmdRead):
    """The ``SYSTem:KLOCk`` command.

    Description:
        - This command locks or unlocks the keyboard and front panel of the arbitrary waveform
          generator.

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem:KLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:KLOCk?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SYSTem:KLOCk value`` command.

    SCPI Syntax:
        ```
        - SYSTem:KLOCk <state>
        - SYSTem:KLOCk?
        ```

    Info:
        - ``<state>`` ::=<Boolean>.
        - ``0`` indicates False. The front panel and keyboard are unlocked.
        - ``1`` indicates True. The front panel and keyboard are locked.
    """


class SystemErrorNext(SCPICmdRead):
    """The ``SYSTem:ERRor:NEXT`` command.

    Description:
        - This query-only command returns the contents of the Error/Event queue.

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem:ERRor:NEXT?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:ERRor:NEXT?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SYSTem:ERRor:NEXT?
        ```
    """


class SystemErrorCmd(SCPICmdRead):
    """The ``SYSTem:ERRor`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem:ERRor?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:ERRor?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.next``: The ``SYSTem:ERRor:NEXT`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._next = SystemErrorNext(device, f"{self._cmd_syntax}:NEXT")

    @property
    def next(self) -> SystemErrorNext:
        """Return the ``SYSTem:ERRor:NEXT`` command.

        Description:
            - This query-only command returns the contents of the Error/Event queue.

        Usage:
            - Using the ``.query()`` method will send the ``SYSTem:ERRor:NEXT?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem:ERRor:NEXT?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SYSTem:ERRor:NEXT?
            ```
        """
        return self._next


class SystemDate(SCPICmdWrite, SCPICmdRead):
    """The ``SYSTem:DATE`` command.

    Description:
        - This command sets or returns the system date. When the values are nonintegers, they are
          rounded off to nearest integral values.

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem:DATE?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:DATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SYSTem:DATE value`` command.

    SCPI Syntax:
        ```
        - SYSTem:DATE <year>,<month>,<day>
        - SYSTem:DATE?
        ```
    """


class System(SCPICmdRead):
    """The ``SYSTem`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.date``: The ``SYSTem:DATE`` command.
        - ``.error``: The ``SYSTem:ERRor`` command tree.
        - ``.klock``: The ``SYSTem:KLOCk`` command.
        - ``.time``: The ``SYSTem:TIME`` command.
        - ``.version``: The ``SYSTem:VERSion`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SYSTem") -> None:
        super().__init__(device, cmd_syntax)
        self._date = SystemDate(device, f"{self._cmd_syntax}:DATE")
        self._error = SystemError(device, f"{self._cmd_syntax}:ERRor")
        self._klock = SystemKlock(device, f"{self._cmd_syntax}:KLOCk")
        self._time = SystemTime(device, f"{self._cmd_syntax}:TIME")
        self._version = SystemVersion(device, f"{self._cmd_syntax}:VERSion")

    @property
    def date(self) -> SystemDate:
        """Return the ``SYSTem:DATE`` command.

        Description:
            - This command sets or returns the system date. When the values are nonintegers, they
              are rounded off to nearest integral values.

        Usage:
            - Using the ``.query()`` method will send the ``SYSTem:DATE?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem:DATE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SYSTem:DATE value`` command.

        SCPI Syntax:
            ```
            - SYSTem:DATE <year>,<month>,<day>
            - SYSTem:DATE?
            ```
        """
        return self._date

    @property
    def error(self) -> SystemError:
        """Return the ``SYSTem:ERRor`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SYSTem:ERRor?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem:ERRor?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.next``: The ``SYSTem:ERRor:NEXT`` command.
        """
        return self._error

    @property
    def klock(self) -> SystemKlock:
        """Return the ``SYSTem:KLOCk`` command.

        Description:
            - This command locks or unlocks the keyboard and front panel of the arbitrary waveform
              generator.

        Usage:
            - Using the ``.query()`` method will send the ``SYSTem:KLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem:KLOCk?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SYSTem:KLOCk value`` command.

        SCPI Syntax:
            ```
            - SYSTem:KLOCk <state>
            - SYSTem:KLOCk?
            ```

        Info:
            - ``<state>`` ::=<Boolean>.
            - ``0`` indicates False. The front panel and keyboard are unlocked.
            - ``1`` indicates True. The front panel and keyboard are locked.
        """
        return self._klock

    @property
    def time(self) -> SystemTime:
        """Return the ``SYSTem:TIME`` command.

        Description:
            - This command sets or returns the system time (hours, minutes and seconds). This
              command is equivalent to the time setting through the Windows Control Panel.

        Usage:
            - Using the ``.query()`` method will send the ``SYSTem:TIME?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem:TIME?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SYSTem:TIME value`` command.

        SCPI Syntax:
            ```
            - SYSTem:TIME <hour>,<minute>,<second>
            - SYSTem:TIME?
            ```
        """
        return self._time

    @property
    def version(self) -> SystemVersion:
        """Return the ``SYSTem:VERSion`` command.

        Description:
            - This query-only command returns the conformed SCPI version of the instrument.

        Usage:
            - Using the ``.query()`` method will send the ``SYSTem:VERSion?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem:VERSion?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SYSTem:VERSion?
            ```
        """
        return self._version
