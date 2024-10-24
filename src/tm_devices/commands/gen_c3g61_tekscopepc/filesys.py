"""The filesys commands module.

These commands are used in the following models:
TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - FILESYS:COLLECTLOGFILES <QString>
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class FilesysCollectlogfiles(SCPICmdWrite):
    """The ``FILESYS:COLLECTLOGFILES`` command.

    Description:
        - This command copies the internal log files to the local, USB, TekDrive or network drive
          specified by the quoted string argument.

    Usage:
        - Using the ``.write(value)`` method will send the ``FILESYS:COLLECTLOGFILES value``
          command.

    SCPI Syntax:
        ```
        - FILESYS:COLLECTLOGFILES <QString>
        ```

    Info:
        - ``<QString>`` is a quoted string that specifies the file path to save the .zip file to.
    """

    _WRAP_ARG_WITH_QUOTES = True


class Filesys(SCPICmdRead):
    """The ``FILESYS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``FILESYS?`` query.
        - Using the ``.verify(value)`` method will send the ``FILESYS?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.collectlogfiles``: The ``FILESYS:COLLECTLOGFILES`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "FILESYS") -> None:
        super().__init__(device, cmd_syntax)
        self._collectlogfiles = FilesysCollectlogfiles(
            device, f"{self._cmd_syntax}:COLLECTLOGFILES"
        )

    @property
    def collectlogfiles(self) -> FilesysCollectlogfiles:
        """Return the ``FILESYS:COLLECTLOGFILES`` command.

        Description:
            - This command copies the internal log files to the local, USB, TekDrive or network
              drive specified by the quoted string argument.

        Usage:
            - Using the ``.write(value)`` method will send the ``FILESYS:COLLECTLOGFILES value``
              command.

        SCPI Syntax:
            ```
            - FILESYS:COLLECTLOGFILES <QString>
            ```

        Info:
            - ``<QString>`` is a quoted string that specifies the file path to save the .zip file
              to.
        """
        return self._collectlogfiles
