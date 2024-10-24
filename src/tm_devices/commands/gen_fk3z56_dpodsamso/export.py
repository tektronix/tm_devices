"""The export commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - EXPort STARt
    - EXPort:FILEName <file path>
    - EXPort:FILEName?
    - EXPort:FORMat {BMP|JPEG|PCX|PNG|TIFF}
    - EXPort:FORMat?
    - EXPort:PALEtte {COLOr|INKSaver|BLACKANDWhite}
    - EXPort:PALEtte?
    - EXPort:READOuts {OFFGRAticule|ONGRAticule}
    - EXPort:READOuts?
    - EXPort:VIEW {FULLSCREEN|GRAticule|FULLNOmenu}
    - EXPort:VIEW?
    - EXPort?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class ExportView(SCPICmdWrite, SCPICmdRead):
    """The ``EXPort:VIEW`` command.

    Description:
        - This command sets or queries the area of the screen to be exported.

    Usage:
        - Using the ``.query()`` method will send the ``EXPort:VIEW?`` query.
        - Using the ``.verify(value)`` method will send the ``EXPort:VIEW?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EXPort:VIEW value`` command.

    SCPI Syntax:
        ```
        - EXPort:VIEW {FULLSCREEN|GRAticule|FULLNOmenu}
        - EXPort:VIEW?
        ```

    Info:
        - ``FULLSCREEN`` displays both the graticule and menu areas of the screen.
        - ``GRAticule`` displays only the graticule area of the screen.
        - ``FULLNOmenu`` displays the full screen but hides any menus or toolbars.
    """


class ExportReadouts(SCPICmdWrite, SCPICmdRead):
    """The ``EXPort:READOuts`` command.

    Description:
        - This command sets or queries the area on the screen where the readout appear for export.

    Usage:
        - Using the ``.query()`` method will send the ``EXPort:READOuts?`` query.
        - Using the ``.verify(value)`` method will send the ``EXPort:READOuts?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EXPort:READOuts value`` command.

    SCPI Syntax:
        ```
        - EXPort:READOuts {OFFGRAticule|ONGRAticule}
        - EXPort:READOuts?
        ```

    Info:
        - ``OFFGRATICULE`` places the readouts off the graticule area.
        - ``ONGRATICULE`` places the readouts on the graticule area for export.
    """


class ExportPalette(SCPICmdWrite, SCPICmdRead):
    """The ``EXPort:PALEtte`` command.

    Description:
        - This command sets or queries the export color palette.

    Usage:
        - Using the ``.query()`` method will send the ``EXPort:PALEtte?`` query.
        - Using the ``.verify(value)`` method will send the ``EXPort:PALEtte?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EXPort:PALEtte value`` command.

    SCPI Syntax:
        ```
        - EXPort:PALEtte {COLOr|INKSaver|BLACKANDWhite}
        - EXPort:PALEtte?
        ```

    Info:
        - ``COLOr`` Hard copy output is color.
        - ``INKSaver`` Hard copy output saves ink.
        - ``BLACKANDwhite`` Hard copy output is black and white.
    """


class ExportFormat(SCPICmdWrite, SCPICmdRead):
    """The ``EXPort:FORMat`` command.

    Description:
        - This command sets or queries the image format for exporting waveforms to a file.

    Usage:
        - Using the ``.query()`` method will send the ``EXPort:FORMat?`` query.
        - Using the ``.verify(value)`` method will send the ``EXPort:FORMat?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EXPort:FORMat value`` command.

    SCPI Syntax:
        ```
        - EXPort:FORMat {BMP|JPEG|PCX|PNG|TIFF}
        - EXPort:FORMat?
        ```

    Info:
        - ``BMP`` specifies BMP image format.
        - ``JPEG`` specifies JPEG image format.
        - ``PCX`` specifies PCX image format.
        - ``PNG`` specifies PNG image format.
        - ``TIFF`` specifies TIFF image format.
    """


class ExportFilename(SCPICmdWrite, SCPICmdRead):
    """The ``EXPort:FILEName`` command.

    Description:
        - This command sets or queries the file/path that will be sent export data on the next
          EXPORT command.

    Usage:
        - Using the ``.query()`` method will send the ``EXPort:FILEName?`` query.
        - Using the ``.verify(value)`` method will send the ``EXPort:FILEName?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EXPort:FILEName value`` command.

    SCPI Syntax:
        ```
        - EXPort:FILEName <file path>
        - EXPort:FILEName?
        ```

    Info:
        - ``<file path>`` specifies that the hard copy is sent to the named file. <file path> is a
          quoted string that defines the file name and path. Input the file path using the form
          ``<drive>:<dir>``/<filename>.<drive> and one or more <dir>s are optional. The file path
          cannot exceed 128 characters. If you do not specify the path with <drive>: and one or more
          <dir>s, the default location is 'C:UsersPublicTektronixTekScopeScreen Captures'. While
          filename extensions are not required, they are highly recommended.
    """


class Export(SCPICmdWrite, SCPICmdRead):
    """The ``EXPort`` command.

    Description:
        - This command sends a copy of the waveform to the file path specified by
          ``EXPORT:FILENAME``. The ``EXPort`` query returns image format and file information.

    Usage:
        - Using the ``.query()`` method will send the ``EXPort?`` query.
        - Using the ``.verify(value)`` method will send the ``EXPort?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EXPort value`` command.

    SCPI Syntax:
        ```
        - EXPort STARt
        - EXPort?
        ```

    Info:
        - ``STARt`` initiates the export.

    Properties:
        - ``.filename``: The ``EXPort:FILEName`` command.
        - ``.format``: The ``EXPort:FORMat`` command.
        - ``.palette``: The ``EXPort:PALEtte`` command.
        - ``.readouts``: The ``EXPort:READOuts`` command.
        - ``.view``: The ``EXPort:VIEW`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "EXPort") -> None:
        super().__init__(device, cmd_syntax)
        self._filename = ExportFilename(device, f"{self._cmd_syntax}:FILEName")
        self._format = ExportFormat(device, f"{self._cmd_syntax}:FORMat")
        self._palette = ExportPalette(device, f"{self._cmd_syntax}:PALEtte")
        self._readouts = ExportReadouts(device, f"{self._cmd_syntax}:READOuts")
        self._view = ExportView(device, f"{self._cmd_syntax}:VIEW")

    @property
    def filename(self) -> ExportFilename:
        """Return the ``EXPort:FILEName`` command.

        Description:
            - This command sets or queries the file/path that will be sent export data on the next
              EXPORT command.

        Usage:
            - Using the ``.query()`` method will send the ``EXPort:FILEName?`` query.
            - Using the ``.verify(value)`` method will send the ``EXPort:FILEName?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EXPort:FILEName value`` command.

        SCPI Syntax:
            ```
            - EXPort:FILEName <file path>
            - EXPort:FILEName?
            ```

        Info:
            - ``<file path>`` specifies that the hard copy is sent to the named file. <file path> is
              a quoted string that defines the file name and path. Input the file path using the
              form ``<drive>:<dir>``/<filename>.<drive> and one or more <dir>s are optional. The
              file path cannot exceed 128 characters. If you do not specify the path with <drive>:
              and one or more <dir>s, the default location is 'C:UsersPublicTektronixTekScopeScreen
              Captures'. While filename extensions are not required, they are highly recommended.
        """
        return self._filename

    @property
    def format(self) -> ExportFormat:
        """Return the ``EXPort:FORMat`` command.

        Description:
            - This command sets or queries the image format for exporting waveforms to a file.

        Usage:
            - Using the ``.query()`` method will send the ``EXPort:FORMat?`` query.
            - Using the ``.verify(value)`` method will send the ``EXPort:FORMat?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EXPort:FORMat value`` command.

        SCPI Syntax:
            ```
            - EXPort:FORMat {BMP|JPEG|PCX|PNG|TIFF}
            - EXPort:FORMat?
            ```

        Info:
            - ``BMP`` specifies BMP image format.
            - ``JPEG`` specifies JPEG image format.
            - ``PCX`` specifies PCX image format.
            - ``PNG`` specifies PNG image format.
            - ``TIFF`` specifies TIFF image format.
        """
        return self._format

    @property
    def palette(self) -> ExportPalette:
        """Return the ``EXPort:PALEtte`` command.

        Description:
            - This command sets or queries the export color palette.

        Usage:
            - Using the ``.query()`` method will send the ``EXPort:PALEtte?`` query.
            - Using the ``.verify(value)`` method will send the ``EXPort:PALEtte?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EXPort:PALEtte value`` command.

        SCPI Syntax:
            ```
            - EXPort:PALEtte {COLOr|INKSaver|BLACKANDWhite}
            - EXPort:PALEtte?
            ```

        Info:
            - ``COLOr`` Hard copy output is color.
            - ``INKSaver`` Hard copy output saves ink.
            - ``BLACKANDwhite`` Hard copy output is black and white.
        """
        return self._palette

    @property
    def readouts(self) -> ExportReadouts:
        """Return the ``EXPort:READOuts`` command.

        Description:
            - This command sets or queries the area on the screen where the readout appear for
              export.

        Usage:
            - Using the ``.query()`` method will send the ``EXPort:READOuts?`` query.
            - Using the ``.verify(value)`` method will send the ``EXPort:READOuts?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EXPort:READOuts value`` command.

        SCPI Syntax:
            ```
            - EXPort:READOuts {OFFGRAticule|ONGRAticule}
            - EXPort:READOuts?
            ```

        Info:
            - ``OFFGRATICULE`` places the readouts off the graticule area.
            - ``ONGRATICULE`` places the readouts on the graticule area for export.
        """
        return self._readouts

    @property
    def view(self) -> ExportView:
        """Return the ``EXPort:VIEW`` command.

        Description:
            - This command sets or queries the area of the screen to be exported.

        Usage:
            - Using the ``.query()`` method will send the ``EXPort:VIEW?`` query.
            - Using the ``.verify(value)`` method will send the ``EXPort:VIEW?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EXPort:VIEW value`` command.

        SCPI Syntax:
            ```
            - EXPort:VIEW {FULLSCREEN|GRAticule|FULLNOmenu}
            - EXPort:VIEW?
            ```

        Info:
            - ``FULLSCREEN`` displays both the graticule and menu areas of the screen.
            - ``GRAticule`` displays only the graticule area of the screen.
            - ``FULLNOmenu`` displays the full screen but hides any menus or toolbars.
        """
        return self._view
