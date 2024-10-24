"""The filesystem commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - FILESystem:COPy {<source QString>,<destination QString>}
    - FILESystem:CWD {<new working directory path>}
    - FILESystem:DELEte <file path>
    - FILESystem:DIR?
    - FILESystem:FORMat
    - FILESystem:FREESpace?
    - FILESystem:LDIR?
    - FILESystem:MKDir <directory path>
    - FILESystem:MOUNT:AVAILable?
    - FILESystem:MOUNT:DRIve <Qstring>
    - FILESystem:MOUNT:LIST?
    - FILESystem:READFile <QString>
    - FILESystem:REName <old file path>,<new file path>
    - FILESystem:RMDir <directory path>
    - FILESystem:UNMOUNT:DRIve QString
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


class FilesystemUnmountDrive(SCPICmdWrite):
    """The ``FILESystem:UNMOUNT:DRIve`` command.

    Description:
        - This command attempts to un-mount the network drive specified by the quoted string
          argument.

    Usage:
        - Using the ``.write(value)`` method will send the ``FILESystem:UNMOUNT:DRIve value``
          command.

    SCPI Syntax:
        ```
        - FILESystem:UNMOUNT:DRIve QString
        ```
    """


class FilesystemUnmount(SCPICmdRead):
    """The ``FILESystem:UNMOUNT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``FILESystem:UNMOUNT?`` query.
        - Using the ``.verify(value)`` method will send the ``FILESystem:UNMOUNT?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.drive``: The ``FILESystem:UNMOUNT:DRIve`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._drive = FilesystemUnmountDrive(device, f"{self._cmd_syntax}:DRIve")

    @property
    def drive(self) -> FilesystemUnmountDrive:
        """Return the ``FILESystem:UNMOUNT:DRIve`` command.

        Description:
            - This command attempts to un-mount the network drive specified by the quoted string
              argument.

        Usage:
            - Using the ``.write(value)`` method will send the ``FILESystem:UNMOUNT:DRIve value``
              command.

        SCPI Syntax:
            ```
            - FILESystem:UNMOUNT:DRIve QString
            ```
        """
        return self._drive


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


class FilesystemMountList(SCPICmdRead):
    """The ``FILESystem:MOUNT:LIST`` command.

    Description:
        - This query returns a comma-separated list of the mounted network drives, including the
          drive letter, server identity (DNS name or IP address), mount path and type. If no network
          drives are mounted, an empty string is returned. Mount types are either NFS or CIFS (for
          Microsoft Windows networks).

    Usage:
        - Using the ``.query()`` method will send the ``FILESystem:MOUNT:LIST?`` query.
        - Using the ``.verify(value)`` method will send the ``FILESystem:MOUNT:LIST?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - FILESystem:MOUNT:LIST?
        ```
    """


class FilesystemMountDrive(SCPICmdWrite):
    """The ``FILESystem:MOUNT:DRIve`` command.

    Description:
        - This command attempts to mount the network drive specified by the quoted string argument.
          The query form takes a quoted string argument specifying the drive letter, and returns a
          Boolean to indicate whether the specified drive letter is mounted. 1 = mounted; 0 = not
          mounted. You can get the details of the mounted drives by querying
          ``FILESYSTEM:MOUNT:LIST``

    Usage:
        - Using the ``.write(value)`` method will send the ``FILESystem:MOUNT:DRIve value`` command.

    SCPI Syntax:
        ```
        - FILESystem:MOUNT:DRIve <Qstring>
        ```

    Info:
        - ``Drive Name:`` The drive name to use, which should be a case insensitive single letter
          followed by a colon. The drive name must be a letter between 'I' and 'Z', inclusive.
          Drives A: through D: are not used and drives E: through H: are reserved for the USB ports.
        - ``Server Identity:`` One of.
        - ``Path:`` The path to be mounted; e.g. /this/that/mydir.
        - ``Domain:`` The domain/workgroup of the target mount.
        - ``User Name:`` The user name.
        - ``User Password:`` The user password.
    """


class FilesystemMountAvailable(SCPICmdRead):
    """The ``FILESystem:MOUNT:AVAILable`` command.

    Description:
        - This query returns a comma-separated list of available drive letters that can be used for
          mounting network drives.

    Usage:
        - Using the ``.query()`` method will send the ``FILESystem:MOUNT:AVAILable?`` query.
        - Using the ``.verify(value)`` method will send the ``FILESystem:MOUNT:AVAILable?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - FILESystem:MOUNT:AVAILable?
        ```
    """


class FilesystemMount(SCPICmdRead):
    """The ``FILESystem:MOUNT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``FILESystem:MOUNT?`` query.
        - Using the ``.verify(value)`` method will send the ``FILESystem:MOUNT?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.available``: The ``FILESystem:MOUNT:AVAILable`` command.
        - ``.drive``: The ``FILESystem:MOUNT:DRIve`` command.
        - ``.list``: The ``FILESystem:MOUNT:LIST`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._available = FilesystemMountAvailable(device, f"{self._cmd_syntax}:AVAILable")
        self._drive = FilesystemMountDrive(device, f"{self._cmd_syntax}:DRIve")
        self._list = FilesystemMountList(device, f"{self._cmd_syntax}:LIST")

    @property
    def available(self) -> FilesystemMountAvailable:
        """Return the ``FILESystem:MOUNT:AVAILable`` command.

        Description:
            - This query returns a comma-separated list of available drive letters that can be used
              for mounting network drives.

        Usage:
            - Using the ``.query()`` method will send the ``FILESystem:MOUNT:AVAILable?`` query.
            - Using the ``.verify(value)`` method will send the ``FILESystem:MOUNT:AVAILable?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - FILESystem:MOUNT:AVAILable?
            ```
        """
        return self._available

    @property
    def drive(self) -> FilesystemMountDrive:
        """Return the ``FILESystem:MOUNT:DRIve`` command.

        Description:
            - This command attempts to mount the network drive specified by the quoted string
              argument. The query form takes a quoted string argument specifying the drive letter,
              and returns a Boolean to indicate whether the specified drive letter is mounted. 1 =
              mounted; 0 = not mounted. You can get the details of the mounted drives by querying
              ``FILESYSTEM:MOUNT:LIST``

        Usage:
            - Using the ``.write(value)`` method will send the ``FILESystem:MOUNT:DRIve value``
              command.

        SCPI Syntax:
            ```
            - FILESystem:MOUNT:DRIve <Qstring>
            ```

        Info:
            - ``Drive Name:`` The drive name to use, which should be a case insensitive single
              letter followed by a colon. The drive name must be a letter between 'I' and 'Z',
              inclusive. Drives A: through D: are not used and drives E: through H: are reserved for
              the USB ports.
            - ``Server Identity:`` One of.
            - ``Path:`` The path to be mounted; e.g. /this/that/mydir.
            - ``Domain:`` The domain/workgroup of the target mount.
            - ``User Name:`` The user name.
            - ``User Password:`` The user password.
        """
        return self._drive

    @property
    def list(self) -> FilesystemMountList:
        """Return the ``FILESystem:MOUNT:LIST`` command.

        Description:
            - This query returns a comma-separated list of the mounted network drives, including the
              drive letter, server identity (DNS name or IP address), mount path and type. If no
              network drives are mounted, an empty string is returned. Mount types are either NFS or
              CIFS (for Microsoft Windows networks).

        Usage:
            - Using the ``.query()`` method will send the ``FILESystem:MOUNT:LIST?`` query.
            - Using the ``.verify(value)`` method will send the ``FILESystem:MOUNT:LIST?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - FILESystem:MOUNT:LIST?
            ```
        """
        return self._list


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


class FilesystemLdir(SCPICmdRead):
    """The ``FILESystem:LDIR`` command.

    Description:
        - Returns a comma separated list of every file, file size, type, modification date and time,
          and directory in the folder referred to by the ``FILESYSTEM:CWD`` command. This is
          different than the ``:DIR`` query in that it provides a long output format with the file
          size, type, and modification date/time. Each entry is a semicolon separated list: < file
          name>;<type>;<size in bytes>;<date>;<time>

    Usage:
        - Using the ``.query()`` method will send the ``FILESystem:LDIR?`` query.
        - Using the ``.verify(value)`` method will send the ``FILESystem:LDIR?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - FILESystem:LDIR?
        ```
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
        - This command copies a named file to a new file. The new file may be in a totally separate
          directory than the old file. You can only copy one file at a time using this command. Wild
          card characters are not allowed.

    Usage:
        - Using the ``.write(value)`` method will send the ``FILESystem:COPy value`` command.

    SCPI Syntax:
        ```
        - FILESystem:COPy {<source QString>,<destination QString>}
        ```

    Info:
        - ``QString`` is a quoted string that defines the file name and path. If the file path is
          within the current working directory, you need only specify the file name.
    """


#  pylint: disable=too-many-instance-attributes
class Filesystem(SCPICmdRead):
    """The ``FILESystem`` command.

    Description:
        - This query-only command returns the directory listing of the current working directory.
          This query is the same as the ``FILESystem:DIR?`` query.

    Usage:
        - Using the ``.query()`` method will send the ``FILESystem?`` query.
        - Using the ``.verify(value)`` method will send the ``FILESystem?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - FILESystem?
        ```

    Properties:
        - ``.copy``: The ``FILESystem:COPy`` command.
        - ``.cwd``: The ``FILESystem:CWD`` command.
        - ``.delete``: The ``FILESystem:DELEte`` command.
        - ``.dir``: The ``FILESystem:DIR`` command.
        - ``.format``: The ``FILESystem:FORMat`` command.
        - ``.freespace``: The ``FILESystem:FREESpace`` command.
        - ``.ldir``: The ``FILESystem:LDIR`` command.
        - ``.mkdir``: The ``FILESystem:MKDir`` command.
        - ``.mount``: The ``FILESystem:MOUNT`` command tree.
        - ``.readfile``: The ``FILESystem:READFile`` command.
        - ``.rename``: The ``FILESystem:REName`` command.
        - ``.rmdir``: The ``FILESystem:RMDir`` command.
        - ``.unmount``: The ``FILESystem:UNMOUNT`` command tree.
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
        self._ldir = FilesystemLdir(device, f"{self._cmd_syntax}:LDIR")
        self._mkdir = FilesystemMkdir(device, f"{self._cmd_syntax}:MKDir")
        self._mount = FilesystemMount(device, f"{self._cmd_syntax}:MOUNT")
        self._readfile = FilesystemReadfile(device, f"{self._cmd_syntax}:READFile")
        self._rename = FilesystemRename(device, f"{self._cmd_syntax}:REName")
        self._rmdir = FilesystemRmdir(device, f"{self._cmd_syntax}:RMDir")
        self._unmount = FilesystemUnmount(device, f"{self._cmd_syntax}:UNMOUNT")
        self._writefile = FilesystemWritefile(device, f"{self._cmd_syntax}:WRITEFile")

    @property
    def copy(self) -> FilesystemCopy:
        """Return the ``FILESystem:COPy`` command.

        Description:
            - This command copies a named file to a new file. The new file may be in a totally
              separate directory than the old file. You can only copy one file at a time using this
              command. Wild card characters are not allowed.

        Usage:
            - Using the ``.write(value)`` method will send the ``FILESystem:COPy value`` command.

        SCPI Syntax:
            ```
            - FILESystem:COPy {<source QString>,<destination QString>}
            ```

        Info:
            - ``QString`` is a quoted string that defines the file name and path. If the file path
              is within the current working directory, you need only specify the file name.
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
    def ldir(self) -> FilesystemLdir:
        """Return the ``FILESystem:LDIR`` command.

        Description:
            - Returns a comma separated list of every file, file size, type, modification date and
              time, and directory in the folder referred to by the ``FILESYSTEM:CWD`` command. This
              is different than the ``:DIR`` query in that it provides a long output format with the
              file size, type, and modification date/time. Each entry is a semicolon separated list:
              < file name>;<type>;<size in bytes>;<date>;<time>

        Usage:
            - Using the ``.query()`` method will send the ``FILESystem:LDIR?`` query.
            - Using the ``.verify(value)`` method will send the ``FILESystem:LDIR?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - FILESystem:LDIR?
            ```
        """
        return self._ldir

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
    def mount(self) -> FilesystemMount:
        """Return the ``FILESystem:MOUNT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``FILESystem:MOUNT?`` query.
            - Using the ``.verify(value)`` method will send the ``FILESystem:MOUNT?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.available``: The ``FILESystem:MOUNT:AVAILable`` command.
            - ``.drive``: The ``FILESystem:MOUNT:DRIve`` command.
            - ``.list``: The ``FILESystem:MOUNT:LIST`` command.
        """
        return self._mount

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
    def unmount(self) -> FilesystemUnmount:
        """Return the ``FILESystem:UNMOUNT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``FILESystem:UNMOUNT?`` query.
            - Using the ``.verify(value)`` method will send the ``FILESystem:UNMOUNT?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.drive``: The ``FILESystem:UNMOUNT:DRIve`` command.
        """
        return self._unmount

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
