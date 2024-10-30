"""The mmemory commands module.

These commands are used in the following models:
AFG3K, AFG3KB, AFG3KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - MMEMory:CATalog?
    - MMEMory:CDIRectory [<directory_name>]
    - MMEMory:CDIRectory?
    - MMEMory:DELete <file_name>
    - MMEMory:LOAD:STATe {0|1|2|3|4},<file_name>
    - MMEMory:LOAD:TRACe EMEMory|EMEMory[1]|EMEMory2,<file_name>
    - MMEMory:LOCK:STATe <file_name>,{ON|OFF|<NR1>}<file_name>?
    - MMEMory:LOCK:STATe?
    - MMEMory:MDIRectory <directory_name>
    - MMEMory:STORe:STATe {0|1|2|3|4},<file_name>
    - MMEMory:STORe:TRACe EMEMory[1]|EMEMory2,<file_name>
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class MmemoryStoreTrace(SCPICmdWrite):
    """The ``MMEMory:STORe:TRACe`` command.

    Description:
        - This command copies a waveform data file in the Edit Memory to a file in the mass storage
          system. If the file in the mass storage is locked, this command causes an error. You
          cannot create a new file if the directory is locked.

    Usage:
        - Using the ``.write(value)`` method will send the ``MMEMory:STORe:TRACe value`` command.

    SCPI Syntax:
        ```
        - MMEMory:STORe:TRACe EMEMory[1]|EMEMory2,<file_name>
        ```
    """


class MmemoryStoreState(SCPICmdWrite):
    """The ``MMEMory:STORe:STATe`` command.

    Description:
        - This command copies a setup file in the setup memory to a specified file in the mass
          storage system. If the specified file in the mass storage system is locked, this command
          causes an error. You cannot create a new file if the directory is locked. If the setup
          memory is deleted, this command causes an error. The ``<file_name>`` argument is a quoted
          string that defines the file name and path.

    Usage:
        - Using the ``.write(value)`` method will send the ``MMEMory:STORe:STATe value`` command.

    SCPI Syntax:
        ```
        - MMEMory:STORe:STATe {0|1|2|3|4},<file_name>
        ```
    """


class MmemoryStore(SCPICmdRead):
    """The ``MMEMory:STORe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:STORe?`` query.
        - Using the ``.verify(value)`` method will send the ``MMEMory:STORe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``MMEMory:STORe:STATe`` command.
        - ``.trace``: The ``MMEMory:STORe:TRACe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = MmemoryStoreState(device, f"{self._cmd_syntax}:STATe")
        self._trace = MmemoryStoreTrace(device, f"{self._cmd_syntax}:TRACe")

    @property
    def state(self) -> MmemoryStoreState:
        """Return the ``MMEMory:STORe:STATe`` command.

        Description:
            - This command copies a setup file in the setup memory to a specified file in the mass
              storage system. If the specified file in the mass storage system is locked, this
              command causes an error. You cannot create a new file if the directory is locked. If
              the setup memory is deleted, this command causes an error. The ``<file_name>``
              argument is a quoted string that defines the file name and path.

        Usage:
            - Using the ``.write(value)`` method will send the ``MMEMory:STORe:STATe value``
              command.

        SCPI Syntax:
            ```
            - MMEMory:STORe:STATe {0|1|2|3|4},<file_name>
            ```
        """
        return self._state

    @property
    def trace(self) -> MmemoryStoreTrace:
        """Return the ``MMEMory:STORe:TRACe`` command.

        Description:
            - This command copies a waveform data file in the Edit Memory to a file in the mass
              storage system. If the file in the mass storage is locked, this command causes an
              error. You cannot create a new file if the directory is locked.

        Usage:
            - Using the ``.write(value)`` method will send the ``MMEMory:STORe:TRACe value``
              command.

        SCPI Syntax:
            ```
            - MMEMory:STORe:TRACe EMEMory[1]|EMEMory2,<file_name>
            ```
        """
        return self._trace


class MmemoryMdirectory(SCPICmdWrite):
    """The ``MMEMory:MDIRectory`` command.

    Description:
        - This command creates a directory in the mass storage system. If the specified directory is
          locked in the mass storage system, this command causes an error.

    Usage:
        - Using the ``.write(value)`` method will send the ``MMEMory:MDIRectory value`` command.

    SCPI Syntax:
        ```
        - MMEMory:MDIRectory <directory_name>
        ```
    """


class MmemoryLockState(SCPICmdWrite, SCPICmdRead):
    """The ``MMEMory:LOCK:STATe`` command.

    Description:
        - This command sets or queries whether to lock a file or directory in the mass storage
          system. If you lock a file or directory, you cannot overwrite or delete it.

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:LOCK:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``MMEMory:LOCK:STATe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MMEMory:LOCK:STATe value`` command.

    SCPI Syntax:
        ```
        - MMEMory:LOCK:STATe <file_name>,{ON|OFF|<NR1>}<file_name>?
        - MMEMory:LOCK:STATe?
        ```
    """


class MmemoryLock(SCPICmdRead):
    """The ``MMEMory:LOCK`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:LOCK?`` query.
        - Using the ``.verify(value)`` method will send the ``MMEMory:LOCK?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``MMEMory:LOCK:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = MmemoryLockState(device, f"{self._cmd_syntax}:STATe")

    @property
    def state(self) -> MmemoryLockState:
        """Return the ``MMEMory:LOCK:STATe`` command.

        Description:
            - This command sets or queries whether to lock a file or directory in the mass storage
              system. If you lock a file or directory, you cannot overwrite or delete it.

        Usage:
            - Using the ``.query()`` method will send the ``MMEMory:LOCK:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``MMEMory:LOCK:STATe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MMEMory:LOCK:STATe value`` command.

        SCPI Syntax:
            ```
            - MMEMory:LOCK:STATe <file_name>,{ON|OFF|<NR1>}<file_name>?
            - MMEMory:LOCK:STATe?
            ```
        """
        return self._state


class MmemoryLoadTrace(SCPICmdWrite):
    """The ``MMEMory:LOAD:TRACe`` command.

    Description:
        - This command copies a waveform data file in the mass storage system to Edit Memory. If the
          file format is different, this command causes an error.

    Usage:
        - Using the ``.write(value)`` method will send the ``MMEMory:LOAD:TRACe value`` command.

    SCPI Syntax:
        ```
        - MMEMory:LOAD:TRACe EMEMory|EMEMory[1]|EMEMory2,<file_name>
        ```
    """


class MmemoryLoadState(SCPICmdWrite):
    """The ``MMEMory:LOAD:STATe`` command.

    Description:
        - This command copies a setup file in the mass storage system to an internal setup memory.
          If a specified internal setup memory is locked, this command causes an error. When you
          power off the instrument, the setups are automatically overwritten in the setup memory 0
          (last setup memory).

    Usage:
        - Using the ``.write(value)`` method will send the ``MMEMory:LOAD:STATe value`` command.

    SCPI Syntax:
        ```
        - MMEMory:LOAD:STATe {0|1|2|3|4},<file_name>
        ```
    """


class MmemoryLoad(SCPICmdRead):
    """The ``MMEMory:LOAD`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:LOAD?`` query.
        - Using the ``.verify(value)`` method will send the ``MMEMory:LOAD?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``MMEMory:LOAD:STATe`` command.
        - ``.trace``: The ``MMEMory:LOAD:TRACe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = MmemoryLoadState(device, f"{self._cmd_syntax}:STATe")
        self._trace = MmemoryLoadTrace(device, f"{self._cmd_syntax}:TRACe")

    @property
    def state(self) -> MmemoryLoadState:
        """Return the ``MMEMory:LOAD:STATe`` command.

        Description:
            - This command copies a setup file in the mass storage system to an internal setup
              memory. If a specified internal setup memory is locked, this command causes an error.
              When you power off the instrument, the setups are automatically overwritten in the
              setup memory 0 (last setup memory).

        Usage:
            - Using the ``.write(value)`` method will send the ``MMEMory:LOAD:STATe value`` command.

        SCPI Syntax:
            ```
            - MMEMory:LOAD:STATe {0|1|2|3|4},<file_name>
            ```
        """
        return self._state

    @property
    def trace(self) -> MmemoryLoadTrace:
        """Return the ``MMEMory:LOAD:TRACe`` command.

        Description:
            - This command copies a waveform data file in the mass storage system to Edit Memory. If
              the file format is different, this command causes an error.

        Usage:
            - Using the ``.write(value)`` method will send the ``MMEMory:LOAD:TRACe value`` command.

        SCPI Syntax:
            ```
            - MMEMory:LOAD:TRACe EMEMory|EMEMory[1]|EMEMory2,<file_name>
            ```
        """
        return self._trace


class MmemoryDelete(SCPICmdWrite):
    """The ``MMEMory:DELete`` command.

    Description:
        - This command deletes a file or directory from the mass storage system. If a specified file
          in the mass storage is not allowed to overwrite or delete, this command causes an error.
          You can delete a directory if it is empty.

    Usage:
        - Using the ``.write(value)`` method will send the ``MMEMory:DELete value`` command.

    SCPI Syntax:
        ```
        - MMEMory:DELete <file_name>
        ```
    """


class MmemoryCdirectory(SCPICmdWrite, SCPICmdRead):
    """The ``MMEMory:CDIRectory`` command.

    Description:
        - This command changes the current working directory in the mass storage system.

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:CDIRectory?`` query.
        - Using the ``.verify(value)`` method will send the ``MMEMory:CDIRectory?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MMEMory:CDIRectory value`` command.

    SCPI Syntax:
        ```
        - MMEMory:CDIRectory [<directory_name>]
        - MMEMory:CDIRectory?
        ```
    """


class MmemoryCatalog(SCPICmdRead):
    """The ``MMEMory:CATalog`` command.

    Description:
        - This query-only command returns the current state of the mass storage system (USB memory).

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:CATalog?`` query.
        - Using the ``.verify(value)`` method will send the ``MMEMory:CATalog?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MMEMory:CATalog?
        ```
    """


class Mmemory(SCPICmdRead):
    """The ``MMEMory`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory?`` query.
        - Using the ``.verify(value)`` method will send the ``MMEMory?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.catalog``: The ``MMEMory:CATalog`` command.
        - ``.cdirectory``: The ``MMEMory:CDIRectory`` command.
        - ``.delete``: The ``MMEMory:DELete`` command.
        - ``.load``: The ``MMEMory:LOAD`` command tree.
        - ``.lock``: The ``MMEMory:LOCK`` command tree.
        - ``.mdirectory``: The ``MMEMory:MDIRectory`` command.
        - ``.store``: The ``MMEMory:STORe`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "MMEMory") -> None:
        super().__init__(device, cmd_syntax)
        self._catalog = MmemoryCatalog(device, f"{self._cmd_syntax}:CATalog")
        self._cdirectory = MmemoryCdirectory(device, f"{self._cmd_syntax}:CDIRectory")
        self._delete = MmemoryDelete(device, f"{self._cmd_syntax}:DELete")
        self._load = MmemoryLoad(device, f"{self._cmd_syntax}:LOAD")
        self._lock = MmemoryLock(device, f"{self._cmd_syntax}:LOCK")
        self._mdirectory = MmemoryMdirectory(device, f"{self._cmd_syntax}:MDIRectory")
        self._store = MmemoryStore(device, f"{self._cmd_syntax}:STORe")

    @property
    def catalog(self) -> MmemoryCatalog:
        """Return the ``MMEMory:CATalog`` command.

        Description:
            - This query-only command returns the current state of the mass storage system (USB
              memory).

        Usage:
            - Using the ``.query()`` method will send the ``MMEMory:CATalog?`` query.
            - Using the ``.verify(value)`` method will send the ``MMEMory:CATalog?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MMEMory:CATalog?
            ```
        """
        return self._catalog

    @property
    def cdirectory(self) -> MmemoryCdirectory:
        """Return the ``MMEMory:CDIRectory`` command.

        Description:
            - This command changes the current working directory in the mass storage system.

        Usage:
            - Using the ``.query()`` method will send the ``MMEMory:CDIRectory?`` query.
            - Using the ``.verify(value)`` method will send the ``MMEMory:CDIRectory?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MMEMory:CDIRectory value`` command.

        SCPI Syntax:
            ```
            - MMEMory:CDIRectory [<directory_name>]
            - MMEMory:CDIRectory?
            ```
        """
        return self._cdirectory

    @property
    def delete(self) -> MmemoryDelete:
        """Return the ``MMEMory:DELete`` command.

        Description:
            - This command deletes a file or directory from the mass storage system. If a specified
              file in the mass storage is not allowed to overwrite or delete, this command causes an
              error. You can delete a directory if it is empty.

        Usage:
            - Using the ``.write(value)`` method will send the ``MMEMory:DELete value`` command.

        SCPI Syntax:
            ```
            - MMEMory:DELete <file_name>
            ```
        """
        return self._delete

    @property
    def load(self) -> MmemoryLoad:
        """Return the ``MMEMory:LOAD`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MMEMory:LOAD?`` query.
            - Using the ``.verify(value)`` method will send the ``MMEMory:LOAD?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``MMEMory:LOAD:STATe`` command.
            - ``.trace``: The ``MMEMory:LOAD:TRACe`` command.
        """
        return self._load

    @property
    def lock(self) -> MmemoryLock:
        """Return the ``MMEMory:LOCK`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MMEMory:LOCK?`` query.
            - Using the ``.verify(value)`` method will send the ``MMEMory:LOCK?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``MMEMory:LOCK:STATe`` command.
        """
        return self._lock

    @property
    def mdirectory(self) -> MmemoryMdirectory:
        """Return the ``MMEMory:MDIRectory`` command.

        Description:
            - This command creates a directory in the mass storage system. If the specified
              directory is locked in the mass storage system, this command causes an error.

        Usage:
            - Using the ``.write(value)`` method will send the ``MMEMory:MDIRectory value`` command.

        SCPI Syntax:
            ```
            - MMEMory:MDIRectory <directory_name>
            ```
        """
        return self._mdirectory

    @property
    def store(self) -> MmemoryStore:
        """Return the ``MMEMory:STORe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MMEMory:STORe?`` query.
            - Using the ``.verify(value)`` method will send the ``MMEMory:STORe?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``MMEMory:STORe:STATe`` command.
            - ``.trace``: The ``MMEMory:STORe:TRACe`` command.
        """
        return self._store
