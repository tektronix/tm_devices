"""The system commands module.

These commands are used in the following models:
AWG5200

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SYSTem:DATE <year>,<month>,<day>
    - SYSTem:ERRor:ALL?
    - SYSTem:ERRor:CODE:ALL?
    - SYSTem:ERRor:CODE:NEXT?
    - SYSTem:ERRor:COUNt?
    - SYSTem:ERRor:DIALog <show_dialog>
    - SYSTem:ERRor:DIALog?
    - SYSTem:ERRor:NEXT?
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


class SystemErrorDialog(SCPICmdWrite, SCPICmdRead):
    """The ``SYSTem:ERRor:DIALog`` command.

    Description:
        - This command enables or disables error dialogs from displaying on the UI when an error
          condition occurs on the AWG.

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem:ERRor:DIALog?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:ERRor:DIALog?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SYSTem:ERRor:DIALog value`` command.

    SCPI Syntax:
        ```
        - SYSTem:ERRor:DIALog <show_dialog>
        - SYSTem:ERRor:DIALog?
        ```

    Info:
        - ``*RST`` sets this value to 1.
    """


class SystemErrorCount(SCPICmdRead):
    """The ``SYSTem:ERRor:COUNt`` command.

    Description:
        - This command returns the error and event queue for the number of unread items.

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem:ERRor:COUNt?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:ERRor:COUNt?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SYSTem:ERRor:COUNt?
        ```
    """


class SystemErrorCodeNext(SCPICmdRead):
    """The ``SYSTem:ERRor:CODE:NEXT`` command.

    Description:
        - This command returns the error and event queue for the next item and removes it from the
          queue.

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem:ERRor:CODE:NEXT?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:ERRor:CODE:NEXT?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SYSTem:ERRor:CODE:NEXT?
        ```
    """


class SystemErrorCodeAll(SCPICmdRead):
    """The ``SYSTem:ERRor:CODE:ALL`` command.

    Description:
        - This command returns the error and event queue for the codes of all the unread items and
          removes them from the queue.

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem:ERRor:CODE:ALL?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:ERRor:CODE:ALL?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SYSTem:ERRor:CODE:ALL?
        ```
    """


class SystemErrorCode(SCPICmdRead):
    """The ``SYSTem:ERRor:CODE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem:ERRor:CODE?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:ERRor:CODE?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.all``: The ``SYSTem:ERRor:CODE:ALL`` command.
        - ``.next``: The ``SYSTem:ERRor:CODE:NEXT`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._all = SystemErrorCodeAll(device, f"{self._cmd_syntax}:ALL")
        self._next = SystemErrorCodeNext(device, f"{self._cmd_syntax}:NEXT")

    @property
    def all(self) -> SystemErrorCodeAll:
        """Return the ``SYSTem:ERRor:CODE:ALL`` command.

        Description:
            - This command returns the error and event queue for the codes of all the unread items
              and removes them from the queue.

        Usage:
            - Using the ``.query()`` method will send the ``SYSTem:ERRor:CODE:ALL?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem:ERRor:CODE:ALL?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SYSTem:ERRor:CODE:ALL?
            ```
        """
        return self._all

    @property
    def next(self) -> SystemErrorCodeNext:
        """Return the ``SYSTem:ERRor:CODE:NEXT`` command.

        Description:
            - This command returns the error and event queue for the next item and removes it from
              the queue.

        Usage:
            - Using the ``.query()`` method will send the ``SYSTem:ERRor:CODE:NEXT?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem:ERRor:CODE:NEXT?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SYSTem:ERRor:CODE:NEXT?
            ```
        """
        return self._next


class SystemErrorAll(SCPICmdRead):
    """The ``SYSTem:ERRor:ALL`` command.

    Description:
        - This command returns the error and event queue for all the unread items and removes them
          from the queue.

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem:ERRor:ALL?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:ERRor:ALL?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SYSTem:ERRor:ALL?
        ```
    """


class SystemErrorCmd(SCPICmdRead):
    """The ``SYSTem:ERRor`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem:ERRor?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:ERRor?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.all``: The ``SYSTem:ERRor:ALL`` command.
        - ``.code``: The ``SYSTem:ERRor:CODE`` command tree.
        - ``.count``: The ``SYSTem:ERRor:COUNt`` command.
        - ``.dialog``: The ``SYSTem:ERRor:DIALog`` command.
        - ``.next``: The ``SYSTem:ERRor:NEXT`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._all = SystemErrorAll(device, f"{self._cmd_syntax}:ALL")
        self._code = SystemErrorCode(device, f"{self._cmd_syntax}:CODE")
        self._count = SystemErrorCount(device, f"{self._cmd_syntax}:COUNt")
        self._dialog = SystemErrorDialog(device, f"{self._cmd_syntax}:DIALog")
        self._next = SystemErrorNext(device, f"{self._cmd_syntax}:NEXT")

    @property
    def all(self) -> SystemErrorAll:
        """Return the ``SYSTem:ERRor:ALL`` command.

        Description:
            - This command returns the error and event queue for all the unread items and removes
              them from the queue.

        Usage:
            - Using the ``.query()`` method will send the ``SYSTem:ERRor:ALL?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem:ERRor:ALL?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SYSTem:ERRor:ALL?
            ```
        """
        return self._all

    @property
    def code(self) -> SystemErrorCode:
        """Return the ``SYSTem:ERRor:CODE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SYSTem:ERRor:CODE?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem:ERRor:CODE?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.all``: The ``SYSTem:ERRor:CODE:ALL`` command.
            - ``.next``: The ``SYSTem:ERRor:CODE:NEXT`` command.
        """
        return self._code

    @property
    def count(self) -> SystemErrorCount:
        """Return the ``SYSTem:ERRor:COUNt`` command.

        Description:
            - This command returns the error and event queue for the number of unread items.

        Usage:
            - Using the ``.query()`` method will send the ``SYSTem:ERRor:COUNt?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem:ERRor:COUNt?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SYSTem:ERRor:COUNt?
            ```
        """
        return self._count

    @property
    def dialog(self) -> SystemErrorDialog:
        """Return the ``SYSTem:ERRor:DIALog`` command.

        Description:
            - This command enables or disables error dialogs from displaying on the UI when an error
              condition occurs on the AWG.

        Usage:
            - Using the ``.query()`` method will send the ``SYSTem:ERRor:DIALog?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem:ERRor:DIALog?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SYSTem:ERRor:DIALog value``
              command.

        SCPI Syntax:
            ```
            - SYSTem:ERRor:DIALog <show_dialog>
            - SYSTem:ERRor:DIALog?
            ```

        Info:
            - ``*RST`` sets this value to 1.
        """
        return self._dialog

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


class SystemDate(SCPICmdWrite):
    """The ``SYSTem:DATE`` command.

    Description:
        - This command sets or returns the system date. When the values are nonintegers, they are
          rounded off to nearest integral values.

    Usage:
        - Using the ``.write(value)`` method will send the ``SYSTem:DATE value`` command.

    SCPI Syntax:
        ```
        - SYSTem:DATE <year>,<month>,<day>
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
        - ``.time``: The ``SYSTem:TIME`` command.
        - ``.version``: The ``SYSTem:VERSion`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SYSTem") -> None:
        super().__init__(device, cmd_syntax)
        self._date = SystemDate(device, f"{self._cmd_syntax}:DATE")
        self._error = SystemError(device, f"{self._cmd_syntax}:ERRor")
        self._time = SystemTime(device, f"{self._cmd_syntax}:TIME")
        self._version = SystemVersion(device, f"{self._cmd_syntax}:VERSion")

    @property
    def date(self) -> SystemDate:
        """Return the ``SYSTem:DATE`` command.

        Description:
            - This command sets or returns the system date. When the values are nonintegers, they
              are rounded off to nearest integral values.

        Usage:
            - Using the ``.write(value)`` method will send the ``SYSTem:DATE value`` command.

        SCPI Syntax:
            ```
            - SYSTem:DATE <year>,<month>,<day>
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
            - ``.all``: The ``SYSTem:ERRor:ALL`` command.
            - ``.code``: The ``SYSTem:ERRor:CODE`` command tree.
            - ``.count``: The ``SYSTem:ERRor:COUNt`` command.
            - ``.dialog``: The ``SYSTem:ERRor:DIALog`` command.
            - ``.next``: The ``SYSTem:ERRor:NEXT`` command.
        """
        return self._error

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
