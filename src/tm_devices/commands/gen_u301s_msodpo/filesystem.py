"""The filesystem commands module.

These commands are used in the following models:
DPO2K, DPO2KB, MSO2K, MSO2KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - FILESystem
    - FILESystem:COPy {<source file path>,<destination file path>}
    - FILESystem:CWD {<new working directory path>}
    - FILESystem:DELEte <file path>
    - FILESystem:DIR?
    - FILESystem:FORMat
    - FILESystem:FREESpace?
    - FILESystem:MKDir <directory path>
    - FILESystem:READFile <QString>
    - FILESystem:REName <old file path>,<new file path>
    - FILESystem:RMDir <directory path>
    - FILESystem:WRITEFile <file path>, <data>
    - FILESystem?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class FilesystemWritefile(SCPICmdWrite):
    """The ``FILESystem:WRITEFile`` command.

    Description:
        - Writes the specified block data to a file in the oscilloscope current working directory.
          If the specified file does not exist or is not readable, an appropriate error event is
          posted.

    Usage:
        - Using the ``.write(value)`` method will send the ``FILESystem:WRITEFile value`` command.

    SCPI Syntax:
        ```
        - FILESystem:WRITEFile <file path>, <data>
        ```

    Info:
        - ``<file path>`` is the quoted string that defines the file name and path. If the path is
          within the current working directory, specify the file name only.
        - ``<data>`` can be either DEFINITE LENGTH encoding or INDEFINITE LENGTH ARBITRARY BLOCK
          PROGRAM DATA encoding as described in IEEE488.2.
    """


class FilesystemRmdir(SCPICmdWrite):
    """The ``FILESystem:RMDir`` command.

    Description:
        - Deletes a named directory. This command deletes the specified directory and all of its
          contents. The directory must not be a read-only directory.

    Usage:
        - Using the ``.write(value)`` method will send the ``FILESystem:RMDir value`` command.

    SCPI Syntax:
        ```
        - FILESystem:RMDir <directory path>
        ```

    Info:
        - ``<directory path>`` is a quoted string that defines the directory name and path. If the
          file path is within the current working directory, you need only specify the file name.
    """


class FilesystemRename(SCPICmdWrite):
    """The ``FILESystem:REName`` command.

    Description:
        - Assigns a new name to an existing file.

    Usage:
        - Using the ``.write(value)`` method will send the ``FILESystem:REName value`` command.

    SCPI Syntax:
        ```
        - FILESystem:REName <old file path>,<new file path>
        ```

    Info:
        - ``<old file path>`` is a quoted string that defines the file name and path. If the file
          path is within the current working directory, you need only specify the file name.
        - ``<new file path>`` is a quoted string that defines the file name and path. If the file
          path is within the current working directory, you need only specify the file name.
    """


class FilesystemReadfile(SCPICmdWrite):
    """The ``FILESystem:READFile`` command.

    Description:
        - This command writes the contents of the specified file to the current interface. If the
          specified file does not exist or is not readable, an appropriate error event is posted.

    Usage:
        - Using the ``.write(value)`` method will send the ``FILESystem:READFile value`` command.

    SCPI Syntax:
        ```
        - FILESystem:READFile <QString>
        ```

    Info:
        - ``<QString>`` is a quoted string that defines the file name and path. If the file path is
          within the current working directory, you need only specify the file name.
    """

    _WRAP_ARG_WITH_QUOTES = True


class FilesystemMkdir(SCPICmdWrite):
    """The ``FILESystem:MKDir`` command.

    Description:
        - Creates a new folder.

    Usage:
        - Using the ``.write(value)`` method will send the ``FILESystem:MKDir value`` command.

    SCPI Syntax:
        ```
        - FILESystem:MKDir <directory path>
        ```

    Info:
        - ``<directory path>`` is a quoted string that specifies the directory to create.
    """


class FilesystemFreespace(SCPICmdRead):
    """The ``FILESystem:FREESpace`` command.

    Description:
        - Returns the number of bytes of free space on the current drive.

    Usage:
        - Using the ``.query()`` method will send the ``FILESystem:FREESpace?`` query.
        - Using the ``.verify(value)`` method will send the ``FILESystem:FREESpace?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - FILESystem:FREESpace?
        ```
    """


class FilesystemFormat(SCPICmdWriteNoArguments):
    """The ``FILESystem:FORMat`` command.

    Description:
        - Formats a mass storage device. This command should be used with extreme caution as it
          causes all data on the specified mass storage device to be lost. Drive letters (e.g., E:)
          are case sensitive and must be upper case. For all other FILESYSTEM commands, drives
          letters are not case sensitive. Example: ``FILES:FORMAT`` 'E:/' Formats the USB flash
          drive installed in the oscilloscope's front panel USB port.

    Usage:
        - Using the ``.write()`` method will send the ``FILESystem:FORMat`` command.

    SCPI Syntax:
        ```
        - FILESystem:FORMat
        ```
    """


class FilesystemDir(SCPICmdRead):
    """The ``FILESystem:DIR`` command.

    Description:
        - This query-only command returns a comma separated list of quoted strings. Each string
          contains the name of a file or directory in the folder referred to by the
          ``FILESYSTEM:CWD`` command.

    Usage:
        - Using the ``.query()`` method will send the ``FILESystem:DIR?`` query.
        - Using the ``.verify(value)`` method will send the ``FILESystem:DIR?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - FILESystem:DIR?
        ```
    """


class FilesystemDelete(SCPICmdWrite):
    r"""The ``FILESystem:DELEte`` command.

    Description:
        - This command deletes a named file. If you specify a directory name, it will delete the
          directory and all of its contents, the same as the RMDir command. You can also specify the
          filename as \*.* to delete all of the files in the current or specified directory.

    Usage:
        - Using the ``.write(value)`` method will send the ``FILESystem:DELEte value`` command.

    SCPI Syntax:
        ```
        - FILESystem:DELEte <file path>
        ```

    Info:
        - ``<file path>`` is a quoted string that defines the file name and path. If the file path
          is within the current working directory, you need only specify the file name.
        - ``*.*`` will delete all files and subdirectories within the current working directory.
    """


class FilesystemCwd(SCPICmdWrite):
    """The ``FILESystem:CWD`` command.

    Description:
        - This command specifies the current working directory (CWD) for FILESystem commands. The
          default working directory is 'E:/'. Anytime you use this command to change the directory,
          the directory that you specify is retained as the current working directory until you
          either change the directory or you delete the directory. If you delete the current working
          directory, the oscilloscope resets current working directory to the default directory the
          next time the oscilloscope is powered on or the next time you execute a file system
          command. This command supports the permutations of file and directory names supported by
          Microsoft Windows: Relative path names; for example, './Temp' Absolute path names; for
          example, 'E:/MyWaveform' Implied relative path names; for example 'newfile.txt' becomes
          'E:/TekScope/newfile.txt' if the current working directory is 'E:/TekScope'

    Usage:
        - Using the ``.write(value)`` method will send the ``FILESystem:CWD value`` command.

    SCPI Syntax:
        ```
        - FILESystem:CWD {<new working directory path>}
        ```

    Info:
        - ``<new working directory path>`` is a quoted string that defines the current working; a
          directory name can be up to 128 characters.
    """


class FilesystemCopy(SCPICmdWrite):
    """The ``FILESystem:COPy`` command.

    Description:
        - This command (no query form) copies a named file to a new file. The new file might be in a
          totally separate directory than the old file. You can only copy one file at a time using
          this command. Wild card characters are not allowed.

    Usage:
        - Using the ``.write(value)`` method will send the ``FILESystem:COPy value`` command.

    SCPI Syntax:
        ```
        - FILESystem:COPy {<source file path>,<destination file path>}
        ```

    Info:
        - ``<source file path>`` is a quoted string that defines the file name and path. If the file
          path is within the current working directory, you need only specify the file name.
        - ``<destination file path>`` is a quoted string that defines the file name and path. If the
          file path is within the current working directory, you need only specify the file name.
    """


#  pylint: disable=too-many-instance-attributes
class Filesystem(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``FILESystem`` command.

    Description:
        - Returns the directory listing of the current working directory and the number of bytes of
          free space available. This query is the same as the ``FILESYSTEM:DIR`` query and the
          ``FILESYSTEM:FREESPACE`` query.

    Usage:
        - Using the ``.query()`` method will send the ``FILESystem?`` query.
        - Using the ``.verify(value)`` method will send the ``FILESystem?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``FILESystem`` command.

    SCPI Syntax:
        ```
        - FILESystem
        - FILESystem?
        ```

    Properties:
        - ``.copy``: The ``FILESystem:COPy`` command.
        - ``.cwd``: The ``FILESystem:CWD`` command.
        - ``.delete``: The ``FILESystem:DELEte`` command.
        - ``.dir``: The ``FILESystem:DIR`` command.
        - ``.format``: The ``FILESystem:FORMat`` command.
        - ``.freespace``: The ``FILESystem:FREESpace`` command.
        - ``.mkdir``: The ``FILESystem:MKDir`` command.
        - ``.readfile``: The ``FILESystem:READFile`` command.
        - ``.rename``: The ``FILESystem:REName`` command.
        - ``.rmdir``: The ``FILESystem:RMDir`` command.
        - ``.writefile``: The ``FILESystem:WRITEFile`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "FILESystem"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._copy = FilesystemCopy(device, f"{self._cmd_syntax}:COPy")
        self._cwd = FilesystemCwd(device, f"{self._cmd_syntax}:CWD")
        self._delete = FilesystemDelete(device, f"{self._cmd_syntax}:DELEte")
        self._dir = FilesystemDir(device, f"{self._cmd_syntax}:DIR")
        self._format = FilesystemFormat(device, f"{self._cmd_syntax}:FORMat")
        self._freespace = FilesystemFreespace(device, f"{self._cmd_syntax}:FREESpace")
        self._mkdir = FilesystemMkdir(device, f"{self._cmd_syntax}:MKDir")
        self._readfile = FilesystemReadfile(device, f"{self._cmd_syntax}:READFile")
        self._rename = FilesystemRename(device, f"{self._cmd_syntax}:REName")
        self._rmdir = FilesystemRmdir(device, f"{self._cmd_syntax}:RMDir")
        self._writefile = FilesystemWritefile(device, f"{self._cmd_syntax}:WRITEFile")

    @property
    def copy(self) -> FilesystemCopy:
        """Return the ``FILESystem:COPy`` command.

        Description:
            - This command (no query form) copies a named file to a new file. The new file might be
              in a totally separate directory than the old file. You can only copy one file at a
              time using this command. Wild card characters are not allowed.

        Usage:
            - Using the ``.write(value)`` method will send the ``FILESystem:COPy value`` command.

        SCPI Syntax:
            ```
            - FILESystem:COPy {<source file path>,<destination file path>}
            ```

        Info:
            - ``<source file path>`` is a quoted string that defines the file name and path. If the
              file path is within the current working directory, you need only specify the file
              name.
            - ``<destination file path>`` is a quoted string that defines the file name and path. If
              the file path is within the current working directory, you need only specify the file
              name.
        """
        return self._copy

    @property
    def cwd(self) -> FilesystemCwd:
        """Return the ``FILESystem:CWD`` command.

        Description:
            - This command specifies the current working directory (CWD) for FILESystem commands.
              The default working directory is 'E:/'. Anytime you use this command to change the
              directory, the directory that you specify is retained as the current working directory
              until you either change the directory or you delete the directory. If you delete the
              current working directory, the oscilloscope resets current working directory to the
              default directory the next time the oscilloscope is powered on or the next time you
              execute a file system command. This command supports the permutations of file and
              directory names supported by Microsoft Windows: Relative path names; for example,
              './Temp' Absolute path names; for example, 'E:/MyWaveform' Implied relative path
              names; for example 'newfile.txt' becomes 'E:/TekScope/newfile.txt' if the current
              working directory is 'E:/TekScope'

        Usage:
            - Using the ``.write(value)`` method will send the ``FILESystem:CWD value`` command.

        SCPI Syntax:
            ```
            - FILESystem:CWD {<new working directory path>}
            ```

        Info:
            - ``<new working directory path>`` is a quoted string that defines the current working;
              a directory name can be up to 128 characters.
        """
        return self._cwd

    @property
    def delete(self) -> FilesystemDelete:
        r"""Return the ``FILESystem:DELEte`` command.

        Description:
            - This command deletes a named file. If you specify a directory name, it will delete the
              directory and all of its contents, the same as the RMDir command. You can also specify
              the filename as \*.* to delete all of the files in the current or specified directory.

        Usage:
            - Using the ``.write(value)`` method will send the ``FILESystem:DELEte value`` command.

        SCPI Syntax:
            ```
            - FILESystem:DELEte <file path>
            ```

        Info:
            - ``<file path>`` is a quoted string that defines the file name and path. If the file
              path is within the current working directory, you need only specify the file name.
            - ``*.*`` will delete all files and subdirectories within the current working directory.
        """
        return self._delete

    @property
    def dir(self) -> FilesystemDir:
        """Return the ``FILESystem:DIR`` command.

        Description:
            - This query-only command returns a comma separated list of quoted strings. Each string
              contains the name of a file or directory in the folder referred to by the
              ``FILESYSTEM:CWD`` command.

        Usage:
            - Using the ``.query()`` method will send the ``FILESystem:DIR?`` query.
            - Using the ``.verify(value)`` method will send the ``FILESystem:DIR?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - FILESystem:DIR?
            ```
        """
        return self._dir

    @property
    def format(self) -> FilesystemFormat:
        """Return the ``FILESystem:FORMat`` command.

        Description:
            - Formats a mass storage device. This command should be used with extreme caution as it
              causes all data on the specified mass storage device to be lost. Drive letters (e.g.,
              E:) are case sensitive and must be upper case. For all other FILESYSTEM commands,
              drives letters are not case sensitive. Example: ``FILES:FORMAT`` 'E:/' Formats the USB
              flash drive installed in the oscilloscope's front panel USB port.

        Usage:
            - Using the ``.write()`` method will send the ``FILESystem:FORMat`` command.

        SCPI Syntax:
            ```
            - FILESystem:FORMat
            ```
        """
        return self._format

    @property
    def freespace(self) -> FilesystemFreespace:
        """Return the ``FILESystem:FREESpace`` command.

        Description:
            - Returns the number of bytes of free space on the current drive.

        Usage:
            - Using the ``.query()`` method will send the ``FILESystem:FREESpace?`` query.
            - Using the ``.verify(value)`` method will send the ``FILESystem:FREESpace?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - FILESystem:FREESpace?
            ```
        """
        return self._freespace

    @property
    def mkdir(self) -> FilesystemMkdir:
        """Return the ``FILESystem:MKDir`` command.

        Description:
            - Creates a new folder.

        Usage:
            - Using the ``.write(value)`` method will send the ``FILESystem:MKDir value`` command.

        SCPI Syntax:
            ```
            - FILESystem:MKDir <directory path>
            ```

        Info:
            - ``<directory path>`` is a quoted string that specifies the directory to create.
        """
        return self._mkdir

    @property
    def readfile(self) -> FilesystemReadfile:
        """Return the ``FILESystem:READFile`` command.

        Description:
            - This command writes the contents of the specified file to the current interface. If
              the specified file does not exist or is not readable, an appropriate error event is
              posted.

        Usage:
            - Using the ``.write(value)`` method will send the ``FILESystem:READFile value``
              command.

        SCPI Syntax:
            ```
            - FILESystem:READFile <QString>
            ```

        Info:
            - ``<QString>`` is a quoted string that defines the file name and path. If the file path
              is within the current working directory, you need only specify the file name.
        """
        return self._readfile

    @property
    def rename(self) -> FilesystemRename:
        """Return the ``FILESystem:REName`` command.

        Description:
            - Assigns a new name to an existing file.

        Usage:
            - Using the ``.write(value)`` method will send the ``FILESystem:REName value`` command.

        SCPI Syntax:
            ```
            - FILESystem:REName <old file path>,<new file path>
            ```

        Info:
            - ``<old file path>`` is a quoted string that defines the file name and path. If the
              file path is within the current working directory, you need only specify the file
              name.
            - ``<new file path>`` is a quoted string that defines the file name and path. If the
              file path is within the current working directory, you need only specify the file
              name.
        """
        return self._rename

    @property
    def rmdir(self) -> FilesystemRmdir:
        """Return the ``FILESystem:RMDir`` command.

        Description:
            - Deletes a named directory. This command deletes the specified directory and all of its
              contents. The directory must not be a read-only directory.

        Usage:
            - Using the ``.write(value)`` method will send the ``FILESystem:RMDir value`` command.

        SCPI Syntax:
            ```
            - FILESystem:RMDir <directory path>
            ```

        Info:
            - ``<directory path>`` is a quoted string that defines the directory name and path. If
              the file path is within the current working directory, you need only specify the file
              name.
        """
        return self._rmdir

    @property
    def writefile(self) -> FilesystemWritefile:
        """Return the ``FILESystem:WRITEFile`` command.

        Description:
            - Writes the specified block data to a file in the oscilloscope current working
              directory. If the specified file does not exist or is not readable, an appropriate
              error event is posted.

        Usage:
            - Using the ``.write(value)`` method will send the ``FILESystem:WRITEFile value``
              command.

        SCPI Syntax:
            ```
            - FILESystem:WRITEFile <file path>, <data>
            ```

        Info:
            - ``<file path>`` is the quoted string that defines the file name and path. If the path
              is within the current working directory, specify the file name only.
            - ``<data>`` can be either DEFINITE LENGTH encoding or INDEFINITE LENGTH ARBITRARY BLOCK
              PROGRAM DATA encoding as described in IEEE488.2.
        """
        return self._writefile
