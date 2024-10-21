"""The filesystem commands module.

These commands are used in the following models:
LPD6, MSO2, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - FILESystem:COPy {<source_file_path>,<destination_file_path>}
    - FILESystem:CWD {<new_working_directory_path>}
    - FILESystem:CWD?
    - FILESystem:DELEte <file_path>
    - FILESystem:DIR?
    - FILESystem:HOMEDir?
    - FILESystem:LDIR?
    - FILESystem:MKDir <directory_path>
    - FILESystem:MOUNT:DRIVE <QString>
    - FILESystem:MOUNT:DRIVE? <QString>
    - FILESystem:MOUNT:TEKDrive <QString>
    - FILESystem:MOUNT:TEKDrive? <QString>
    - FILESystem:READFile <QString>
    - FILESystem:REName <old_file_path>,<new_file_path>
    - FILESystem:RMDir <directory_path>
    - FILESystem:TEKDrive:CODE:EXPirytime?
    - FILESystem:TEKDrive:CODE:STATus?
    - FILESystem:TEKDrive:CODE?
    - FILESystem:UNMOUNT:DRIve <QString>
    - FILESystem:UNMOUNT:TEKDrive <QString>
    - FILESystem:WRITEFile <file_path>,<data>
    - FILESystem?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdReadWithArguments, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class FilesystemWritefile(SCPICmdWrite):
    """The ``FILESystem:WRITEFile`` command.

    Description:
        - This command (no query form) writes the specified block data to the specified file on the
          instruments file system. If the destination file cannot be written, an error event is
          posted.

    Usage:
        - Using the ``.write(value)`` method will send the ``FILESystem:WRITEFile value`` command.

    SCPI Syntax:
        ```
        - FILESystem:WRITEFile <file_path>,<data>
        ```

    Info:
        - ``<file_path>`` is a quoted string that defines the file name and path. If the file path
          is within the current working directory, you need only specify the file name.
        - ``<data>`` is the specified block data to be written.
    """


class FilesystemUnmountTekdrive(SCPICmdWrite):
    """The ``FILESystem:UNMOUNT:TEKDrive`` command.

    Description:
        - This command unmounts the TekDrive specified by the quoted string argument and the drive
          name is case insensitive.

    Usage:
        - Using the ``.write(value)`` method will send the ``FILESystem:UNMOUNT:TEKDrive value``
          command.

    SCPI Syntax:
        ```
        - FILESystem:UNMOUNT:TEKDrive <QString>
        ```

    Info:
        - ``<QString>`` specifies the TekDrive to unmount.
    """

    _WRAP_ARG_WITH_QUOTES = True


class FilesystemUnmountDrive(SCPICmdWrite):
    """The ``FILESystem:UNMOUNT:DRIve`` command.

    Description:
        - This command unmounts the USB drive specified by the quoted string argument.

    Usage:
        - Using the ``.write(value)`` method will send the ``FILESystem:UNMOUNT:DRIve value``
          command.

    SCPI Syntax:
        ```
        - FILESystem:UNMOUNT:DRIve <QString>
        ```

    Info:
        - ``<QString>`` is a quoted string that specifies which USB drive to unmount. String is a
          case insensitive single letter followed by a colon.
    """

    _WRAP_ARG_WITH_QUOTES = True


class FilesystemUnmount(SCPICmdRead):
    """The ``FILESystem:UNMOUNT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``FILESystem:UNMOUNT?`` query.
        - Using the ``.verify(value)`` method will send the ``FILESystem:UNMOUNT?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.drive``: The ``FILESystem:UNMOUNT:DRIve`` command.
        - ``.tekdrive``: The ``FILESystem:UNMOUNT:TEKDrive`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._drive = FilesystemUnmountDrive(device, f"{self._cmd_syntax}:DRIve")
        self._tekdrive = FilesystemUnmountTekdrive(device, f"{self._cmd_syntax}:TEKDrive")

    @property
    def drive(self) -> FilesystemUnmountDrive:
        """Return the ``FILESystem:UNMOUNT:DRIve`` command.

        Description:
            - This command unmounts the USB drive specified by the quoted string argument.

        Usage:
            - Using the ``.write(value)`` method will send the ``FILESystem:UNMOUNT:DRIve value``
              command.

        SCPI Syntax:
            ```
            - FILESystem:UNMOUNT:DRIve <QString>
            ```

        Info:
            - ``<QString>`` is a quoted string that specifies which USB drive to unmount. String is
              a case insensitive single letter followed by a colon.
        """
        return self._drive

    @property
    def tekdrive(self) -> FilesystemUnmountTekdrive:
        """Return the ``FILESystem:UNMOUNT:TEKDrive`` command.

        Description:
            - This command unmounts the TekDrive specified by the quoted string argument and the
              drive name is case insensitive.

        Usage:
            - Using the ``.write(value)`` method will send the ``FILESystem:UNMOUNT:TEKDrive value``
              command.

        SCPI Syntax:
            ```
            - FILESystem:UNMOUNT:TEKDrive <QString>
            ```

        Info:
            - ``<QString>`` specifies the TekDrive to unmount.
        """
        return self._tekdrive


class FilesystemTekdriveCodeStatus(SCPICmdRead):
    """The ``FILESystem:TEKDrive:CODE:STATus`` command.

    Description:
        - This command returns status of short code.

    Usage:
        - Using the ``.query()`` method will send the ``FILESystem:TEKDrive:CODE:STATus?`` query.
        - Using the ``.verify(value)`` method will send the ``FILESystem:TEKDrive:CODE:STATus?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - FILESystem:TEKDrive:CODE:STATus?
        ```
    """


class FilesystemTekdriveCodeExpirytime(SCPICmdRead):
    """The ``FILESystem:TEKDrive:CODE:EXPirytime`` command.

    Description:
        - This command returns expiry time of short code. It is the absolute time that the expiry
          command returns. For example, if ``2:11`` pm is the time the user initiated the TekDrive
          mounting, then the expiry query returns + 5 minutes (``2:16`` pm).

    Usage:
        - Using the ``.query()`` method will send the ``FILESystem:TEKDrive:CODE:EXPirytime?``
          query.
        - Using the ``.verify(value)`` method will send the ``FILESystem:TEKDrive:CODE:EXPirytime?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - FILESystem:TEKDrive:CODE:EXPirytime?
        ```
    """


class FilesystemTekdriveCode(SCPICmdRead):
    """The ``FILESystem:TEKDrive:CODE`` command.

    Description:
        - This command returns short code in string format. This code must be entered (or pasted) at
          http://drive.tekcloud.com/activate. After the code is entered click the Activate button to
          complete the mounting of the TekDrive.

    Usage:
        - Using the ``.query()`` method will send the ``FILESystem:TEKDrive:CODE?`` query.
        - Using the ``.verify(value)`` method will send the ``FILESystem:TEKDrive:CODE?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - FILESystem:TEKDrive:CODE?
        ```

    Properties:
        - ``.expirytime``: The ``FILESystem:TEKDrive:CODE:EXPirytime`` command.
        - ``.status``: The ``FILESystem:TEKDrive:CODE:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._expirytime = FilesystemTekdriveCodeExpirytime(
            device, f"{self._cmd_syntax}:EXPirytime"
        )
        self._status = FilesystemTekdriveCodeStatus(device, f"{self._cmd_syntax}:STATus")

    @property
    def expirytime(self) -> FilesystemTekdriveCodeExpirytime:
        """Return the ``FILESystem:TEKDrive:CODE:EXPirytime`` command.

        Description:
            - This command returns expiry time of short code. It is the absolute time that the
              expiry command returns. For example, if ``2:11`` pm is the time the user initiated the
              TekDrive mounting, then the expiry query returns + 5 minutes (``2:16`` pm).

        Usage:
            - Using the ``.query()`` method will send the ``FILESystem:TEKDrive:CODE:EXPirytime?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``FILESystem:TEKDrive:CODE:EXPirytime?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - FILESystem:TEKDrive:CODE:EXPirytime?
            ```
        """
        return self._expirytime

    @property
    def status(self) -> FilesystemTekdriveCodeStatus:
        """Return the ``FILESystem:TEKDrive:CODE:STATus`` command.

        Description:
            - This command returns status of short code.

        Usage:
            - Using the ``.query()`` method will send the ``FILESystem:TEKDrive:CODE:STATus?``
              query.
            - Using the ``.verify(value)`` method will send the ``FILESystem:TEKDrive:CODE:STATus?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - FILESystem:TEKDrive:CODE:STATus?
            ```
        """
        return self._status


class FilesystemTekdrive(SCPICmdRead):
    """The ``FILESystem:TEKDrive`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``FILESystem:TEKDrive?`` query.
        - Using the ``.verify(value)`` method will send the ``FILESystem:TEKDrive?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.code``: The ``FILESystem:TEKDrive:CODE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._code = FilesystemTekdriveCode(device, f"{self._cmd_syntax}:CODE")

    @property
    def code(self) -> FilesystemTekdriveCode:
        """Return the ``FILESystem:TEKDrive:CODE`` command.

        Description:
            - This command returns short code in string format. This code must be entered (or
              pasted) at http://drive.tekcloud.com/activate. After the code is entered click the
              Activate button to complete the mounting of the TekDrive.

        Usage:
            - Using the ``.query()`` method will send the ``FILESystem:TEKDrive:CODE?`` query.
            - Using the ``.verify(value)`` method will send the ``FILESystem:TEKDrive:CODE?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - FILESystem:TEKDrive:CODE?
            ```

        Sub-properties:
            - ``.expirytime``: The ``FILESystem:TEKDrive:CODE:EXPirytime`` command.
            - ``.status``: The ``FILESystem:TEKDrive:CODE:STATus`` command.
        """
        return self._code


class FilesystemRmdir(SCPICmdWrite):
    """The ``FILESystem:RMDir`` command.

    Description:
        - This command (no query form) deletes a named directory. The directory must be empty.

    Usage:
        - Using the ``.write(value)`` method will send the ``FILESystem:RMDir value`` command.

    SCPI Syntax:
        ```
        - FILESystem:RMDir <directory_path>
        ```

    Info:
        - ``<directory_path>`` is a quoted string that defines the folder name and path. If the
          folder path is within the current working directory, you need only specify the folder
          name.
    """


class FilesystemRename(SCPICmdWrite):
    """The ``FILESystem:REName`` command.

    Description:
        - This command (no query form) assigns a new name to an existing file or folder.

    Usage:
        - Using the ``.write(value)`` method will send the ``FILESystem:REName value`` command.

    SCPI Syntax:
        ```
        - FILESystem:REName <old_file_path>,<new_file_path>
        ```

    Info:
        - ``<old_file_path>`` is a quoted string that defines the file or folder name and path. If
          the path is within the current working directory, you need only specify the file or folder
          name.
        - ``<new_file_path>`` is a quoted string that defines the file or folder name and path. If
          the path is within the current working directory, you need only specify the file or folder
          name.
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


class FilesystemMountTekdrive(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``FILESystem:MOUNT:TEKDrive`` command.

    Description:
        - This command mounts the TekDrive specified by the quoted string arguments. The argument
          must contain the drive name, AutoDisconnectMode, RestrictToCurrentIP, and
          AutoDisconnectTime. The drive name is the TekDrive name to be mounted. It is case
          insensitive. There are three options available for AutoDisconnectMode: Select Power Cycle
          to unmount the TekDrive after power cycling the oscilloscope. There is no time restriction
          when this option is selected Select Never to mount the TekDrive connection permanently.
          Select Custom to disconnect the TekDrive after a chosen duration. The default selection is
          Power Cycle. RestrictToCurrentIP restricts the connection to current network IP only. This
          may be used for additional network security. AutoDisconnectTime is the required time for
          the Auto Disconnect. The TekDrive gets disconnected automatically from the instrument
          after the specified time. The duration is in hours. The minimum is 0.25 hours and the
          maximum is 744 hours. The query form of this command returns whether or not the specified
          TekDrive is mounted.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``FILESystem:MOUNT:TEKDrive? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``FILESystem:MOUNT:TEKDrive? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``FILESystem:MOUNT:TEKDrive value``
          command.

    SCPI Syntax:
        ```
        - FILESystem:MOUNT:TEKDrive <QString>
        - FILESystem:MOUNT:TEKDrive? <QString>
        ```

    Info:
        - ``<QString>`` provides the information needed to mount the TekDrive and must have the
          drive name, AutoDisconnectMode, RestrictToCurrentIP, and AutoDisconnectTime.
    """

    _WRAP_ARG_WITH_QUOTES = True


class FilesystemMountDrive(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``FILESystem:MOUNT:DRIVE`` command.

    Description:
        - The command form mounts a network drive specified by the quoted string argument. The
          quoted string argument is a semicolon separated list of the following fields: Drive name -
          The drive name to be mounted. It is a case insensitive single letter followed by a colon.
          The drive name must be a letter between 'L:' and 'Z:', inclusive. Server identity - The
          server identity is the DNS name of the server or the IP address of the server. Path - The
          path to be mounted (e.g. /level1/level2/mydirectory). User name - The user name for the
          drive. User password - The password for the drive. Domain name - The domain/workgroup of
          the target mount. Verbose - The verbose option to capture mount failure messages. Domain
          name, user name, user password, and verbose are optional and are only used for mounts
          requiring SMB/CIFS interworking (MS Windows and MacOS). The query form returns a 0 or 1 to
          indicate that the drive name (quoted string) is currently mounted or not. A return of 1
          indicates the drive is mounted. A return of 0 indicated the drive is not mounted.

    Usage:
        - Using the ``.query(argument)`` method will send the ``FILESystem:MOUNT:DRIVE? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``FILESystem:MOUNT:DRIVE? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``FILESystem:MOUNT:DRIVE value`` command.

    SCPI Syntax:
        ```
        - FILESystem:MOUNT:DRIVE <QString>
        - FILESystem:MOUNT:DRIVE? <QString>
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class FilesystemMount(SCPICmdRead):
    """The ``FILESystem:MOUNT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``FILESystem:MOUNT?`` query.
        - Using the ``.verify(value)`` method will send the ``FILESystem:MOUNT?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.drive``: The ``FILESystem:MOUNT:DRIVE`` command.
        - ``.tekdrive``: The ``FILESystem:MOUNT:TEKDrive`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._drive = FilesystemMountDrive(device, f"{self._cmd_syntax}:DRIVE")
        self._tekdrive = FilesystemMountTekdrive(device, f"{self._cmd_syntax}:TEKDrive")

    @property
    def drive(self) -> FilesystemMountDrive:
        """Return the ``FILESystem:MOUNT:DRIVE`` command.

        Description:
            - The command form mounts a network drive specified by the quoted string argument. The
              quoted string argument is a semicolon separated list of the following fields: Drive
              name - The drive name to be mounted. It is a case insensitive single letter followed
              by a colon. The drive name must be a letter between 'L:' and 'Z:', inclusive. Server
              identity - The server identity is the DNS name of the server or the IP address of the
              server. Path - The path to be mounted (e.g. /level1/level2/mydirectory). User name -
              The user name for the drive. User password - The password for the drive. Domain name -
              The domain/workgroup of the target mount. Verbose - The verbose option to capture
              mount failure messages. Domain name, user name, user password, and verbose are
              optional and are only used for mounts requiring SMB/CIFS interworking (MS Windows and
              MacOS). The query form returns a 0 or 1 to indicate that the drive name (quoted
              string) is currently mounted or not. A return of 1 indicates the drive is mounted. A
              return of 0 indicated the drive is not mounted.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``FILESystem:MOUNT:DRIVE? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``FILESystem:MOUNT:DRIVE? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``FILESystem:MOUNT:DRIVE value``
              command.

        SCPI Syntax:
            ```
            - FILESystem:MOUNT:DRIVE <QString>
            - FILESystem:MOUNT:DRIVE? <QString>
            ```
        """
        return self._drive

    @property
    def tekdrive(self) -> FilesystemMountTekdrive:
        """Return the ``FILESystem:MOUNT:TEKDrive`` command.

        Description:
            - This command mounts the TekDrive specified by the quoted string arguments. The
              argument must contain the drive name, AutoDisconnectMode, RestrictToCurrentIP, and
              AutoDisconnectTime. The drive name is the TekDrive name to be mounted. It is case
              insensitive. There are three options available for AutoDisconnectMode: Select Power
              Cycle to unmount the TekDrive after power cycling the oscilloscope. There is no time
              restriction when this option is selected Select Never to mount the TekDrive connection
              permanently. Select Custom to disconnect the TekDrive after a chosen duration. The
              default selection is Power Cycle. RestrictToCurrentIP restricts the connection to
              current network IP only. This may be used for additional network security.
              AutoDisconnectTime is the required time for the Auto Disconnect. The TekDrive gets
              disconnected automatically from the instrument after the specified time. The duration
              is in hours. The minimum is 0.25 hours and the maximum is 744 hours. The query form of
              this command returns whether or not the specified TekDrive is mounted.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``FILESystem:MOUNT:TEKDrive? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``FILESystem:MOUNT:TEKDrive? argument`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``FILESystem:MOUNT:TEKDrive value``
              command.

        SCPI Syntax:
            ```
            - FILESystem:MOUNT:TEKDrive <QString>
            - FILESystem:MOUNT:TEKDrive? <QString>
            ```

        Info:
            - ``<QString>`` provides the information needed to mount the TekDrive and must have the
              drive name, AutoDisconnectMode, RestrictToCurrentIP, and AutoDisconnectTime.
        """
        return self._tekdrive


class FilesystemMkdir(SCPICmdWrite):
    """The ``FILESystem:MKDir`` command.

    Description:
        - This command (no query form) creates a new directory.

    Usage:
        - Using the ``.write(value)`` method will send the ``FILESystem:MKDir value`` command.

    SCPI Syntax:
        ```
        - FILESystem:MKDir <directory_path>
        ```

    Info:
        - ``<directory_path>`` is a quoted string that specifies the directory to create.
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


class FilesystemHomedir(SCPICmdRead):
    """The ``FILESystem:HOMEDir`` command.

    Description:
        - This query returns the current user's home directory.

    Usage:
        - Using the ``.query()`` method will send the ``FILESystem:HOMEDir?`` query.
        - Using the ``.verify(value)`` method will send the ``FILESystem:HOMEDir?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - FILESystem:HOMEDir?
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
    """The ``FILESystem:DELEte`` command.

    Description:
        - This command (no query form) deletes a named file or directory from a mass storage device.
          Once removed, the data in that file or directory can no longer be accessed. If the
          specified file is a directory, it must be empty before it can be deleted.

    Usage:
        - Using the ``.write(value)`` method will send the ``FILESystem:DELEte value`` command.

    SCPI Syntax:
        ```
        - FILESystem:DELEte <file_path>
        ```

    Info:
        - ``<file_path>`` is a quoted string that defines the file name and path. If the file path
          is within the current working directory, you need only specify the file name.
    """


class FilesystemCwd(SCPICmdWrite, SCPICmdRead):
    """The ``FILESystem:CWD`` command.

    Description:
        - This command sets or queries the current working directory. CWD is short for Current
          Working Directory. It changes the directory (folder) that the other FILESystem commands
          operate on.

    Usage:
        - Using the ``.query()`` method will send the ``FILESystem:CWD?`` query.
        - Using the ``.verify(value)`` method will send the ``FILESystem:CWD?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``FILESystem:CWD value`` command.

    SCPI Syntax:
        ```
        - FILESystem:CWD {<new_working_directory_path>}
        - FILESystem:CWD?
        ```

    Info:
        - ``<new_working_directory_path>`` is a quoted string that defines the current working; a
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
        - FILESystem:COPy {<source_file_path>,<destination_file_path>}
        ```

    Info:
        - ``<source_file_path>`` is a quoted string that defines the file name and path or
          directory. If the file path is within the current working directory, you need only specify
          the file name.
        - ``<destination_file_path>`` is a quoted string that defines the file name and path. If the
          file path is within the current working directory, you need only specify the file name.
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
        - ``.homedir``: The ``FILESystem:HOMEDir`` command.
        - ``.ldir``: The ``FILESystem:LDIR`` command.
        - ``.mkdir``: The ``FILESystem:MKDir`` command.
        - ``.mount``: The ``FILESystem:MOUNT`` command tree.
        - ``.readfile``: The ``FILESystem:READFile`` command.
        - ``.rename``: The ``FILESystem:REName`` command.
        - ``.rmdir``: The ``FILESystem:RMDir`` command.
        - ``.tekdrive``: The ``FILESystem:TEKDrive`` command tree.
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
        self._homedir = FilesystemHomedir(device, f"{self._cmd_syntax}:HOMEDir")
        self._ldir = FilesystemLdir(device, f"{self._cmd_syntax}:LDIR")
        self._mkdir = FilesystemMkdir(device, f"{self._cmd_syntax}:MKDir")
        self._mount = FilesystemMount(device, f"{self._cmd_syntax}:MOUNT")
        self._readfile = FilesystemReadfile(device, f"{self._cmd_syntax}:READFile")
        self._rename = FilesystemRename(device, f"{self._cmd_syntax}:REName")
        self._rmdir = FilesystemRmdir(device, f"{self._cmd_syntax}:RMDir")
        self._tekdrive = FilesystemTekdrive(device, f"{self._cmd_syntax}:TEKDrive")
        self._unmount = FilesystemUnmount(device, f"{self._cmd_syntax}:UNMOUNT")
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
            - FILESystem:COPy {<source_file_path>,<destination_file_path>}
            ```

        Info:
            - ``<source_file_path>`` is a quoted string that defines the file name and path or
              directory. If the file path is within the current working directory, you need only
              specify the file name.
            - ``<destination_file_path>`` is a quoted string that defines the file name and path. If
              the file path is within the current working directory, you need only specify the file
              name.
        """
        return self._copy

    @property
    def cwd(self) -> FilesystemCwd:
        """Return the ``FILESystem:CWD`` command.

        Description:
            - This command sets or queries the current working directory. CWD is short for Current
              Working Directory. It changes the directory (folder) that the other FILESystem
              commands operate on.

        Usage:
            - Using the ``.query()`` method will send the ``FILESystem:CWD?`` query.
            - Using the ``.verify(value)`` method will send the ``FILESystem:CWD?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``FILESystem:CWD value`` command.

        SCPI Syntax:
            ```
            - FILESystem:CWD {<new_working_directory_path>}
            - FILESystem:CWD?
            ```

        Info:
            - ``<new_working_directory_path>`` is a quoted string that defines the current working;
              a directory name can be up to 128 characters.
        """
        return self._cwd

    @property
    def delete(self) -> FilesystemDelete:
        """Return the ``FILESystem:DELEte`` command.

        Description:
            - This command (no query form) deletes a named file or directory from a mass storage
              device. Once removed, the data in that file or directory can no longer be accessed. If
              the specified file is a directory, it must be empty before it can be deleted.

        Usage:
            - Using the ``.write(value)`` method will send the ``FILESystem:DELEte value`` command.

        SCPI Syntax:
            ```
            - FILESystem:DELEte <file_path>
            ```

        Info:
            - ``<file_path>`` is a quoted string that defines the file name and path. If the file
              path is within the current working directory, you need only specify the file name.
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
    def homedir(self) -> FilesystemHomedir:
        """Return the ``FILESystem:HOMEDir`` command.

        Description:
            - This query returns the current user's home directory.

        Usage:
            - Using the ``.query()`` method will send the ``FILESystem:HOMEDir?`` query.
            - Using the ``.verify(value)`` method will send the ``FILESystem:HOMEDir?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - FILESystem:HOMEDir?
            ```
        """
        return self._homedir

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
            - This command (no query form) creates a new directory.

        Usage:
            - Using the ``.write(value)`` method will send the ``FILESystem:MKDir value`` command.

        SCPI Syntax:
            ```
            - FILESystem:MKDir <directory_path>
            ```

        Info:
            - ``<directory_path>`` is a quoted string that specifies the directory to create.
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
            - ``.drive``: The ``FILESystem:MOUNT:DRIVE`` command.
            - ``.tekdrive``: The ``FILESystem:MOUNT:TEKDrive`` command.
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
            - This command (no query form) assigns a new name to an existing file or folder.

        Usage:
            - Using the ``.write(value)`` method will send the ``FILESystem:REName value`` command.

        SCPI Syntax:
            ```
            - FILESystem:REName <old_file_path>,<new_file_path>
            ```

        Info:
            - ``<old_file_path>`` is a quoted string that defines the file or folder name and path.
              If the path is within the current working directory, you need only specify the file or
              folder name.
            - ``<new_file_path>`` is a quoted string that defines the file or folder name and path.
              If the path is within the current working directory, you need only specify the file or
              folder name.
        """
        return self._rename

    @property
    def rmdir(self) -> FilesystemRmdir:
        """Return the ``FILESystem:RMDir`` command.

        Description:
            - This command (no query form) deletes a named directory. The directory must be empty.

        Usage:
            - Using the ``.write(value)`` method will send the ``FILESystem:RMDir value`` command.

        SCPI Syntax:
            ```
            - FILESystem:RMDir <directory_path>
            ```

        Info:
            - ``<directory_path>`` is a quoted string that defines the folder name and path. If the
              folder path is within the current working directory, you need only specify the folder
              name.
        """
        return self._rmdir

    @property
    def tekdrive(self) -> FilesystemTekdrive:
        """Return the ``FILESystem:TEKDrive`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``FILESystem:TEKDrive?`` query.
            - Using the ``.verify(value)`` method will send the ``FILESystem:TEKDrive?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.code``: The ``FILESystem:TEKDrive:CODE`` command.
        """
        return self._tekdrive

    @property
    def unmount(self) -> FilesystemUnmount:
        """Return the ``FILESystem:UNMOUNT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``FILESystem:UNMOUNT?`` query.
            - Using the ``.verify(value)`` method will send the ``FILESystem:UNMOUNT?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.drive``: The ``FILESystem:UNMOUNT:DRIve`` command.
            - ``.tekdrive``: The ``FILESystem:UNMOUNT:TEKDrive`` command.
        """
        return self._unmount

    @property
    def writefile(self) -> FilesystemWritefile:
        """Return the ``FILESystem:WRITEFile`` command.

        Description:
            - This command (no query form) writes the specified block data to the specified file on
              the instruments file system. If the destination file cannot be written, an error event
              is posted.

        Usage:
            - Using the ``.write(value)`` method will send the ``FILESystem:WRITEFile value``
              command.

        SCPI Syntax:
            ```
            - FILESystem:WRITEFile <file_path>,<data>
            ```

        Info:
            - ``<file_path>`` is a quoted string that defines the file name and path. If the file
              path is within the current working directory, you need only specify the file name.
            - ``<data>`` is the specified block data to be written.
        """
        return self._writefile
