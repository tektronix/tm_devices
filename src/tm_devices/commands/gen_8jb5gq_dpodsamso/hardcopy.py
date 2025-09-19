"""The hardcopy commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - HARDCopy STARt
    - HARDCopy:FILEName <file path>
    - HARDCopy:FILEName?
    - HARDCopy:LAYout {PORTRait|LANdscape}
    - HARDCopy:LAYout?
    - HARDCopy:PALEtte {COLOr|BLACKANDWhite|INKSaver}
    - HARDCopy:PALEtte?
    - HARDCopy:PORT {FILE|PRINTER}
    - HARDCopy:PORT?
    - HARDCopy:READOuts {OFFGRAticule|ONGRAticule}
    - HARDCopy:READOuts?
    - HARDCopy:VIEW {FULLSCREEN|GRAticule|FULLNOmenu}
    - HARDCopy:VIEW?
    - HARDCopy?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class HardcopyView(SCPICmdWrite, SCPICmdRead):
    """The ``HARDCopy:VIEW`` command.

    Description:
        - This command sets or queries the area of the screen to be hard copied.

    Usage:
        - Using the ``.query()`` method will send the ``HARDCopy:VIEW?`` query.
        - Using the ``.verify(value)`` method will send the ``HARDCopy:VIEW?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HARDCopy:VIEW value`` command.

    SCPI Syntax:
        ```
        - HARDCopy:VIEW {FULLSCREEN|GRAticule|FULLNOmenu}
        - HARDCopy:VIEW?
        ```

    Info:
        - ``FULLSCREEN`` sets the area to be hard copied to both the graticule and menu areas of the
          screen.
        - ``GRAticule`` sets the area to be hard copied to only the graticule area of the screen.
        - ``FULLNOmenu`` sets the area to be hard copied to full screen but hides any menus or
          toolbars.
    """


class HardcopyReadouts(SCPICmdWrite, SCPICmdRead):
    """The ``HARDCopy:READOuts`` command.

    Description:
        - This command sets or queries the area on a hard copy where the readout appears. This
          command is equivalent to selecting Page Setup from the File menu and setting the Readouts
          Below Graticule in the control window.

    Usage:
        - Using the ``.query()`` method will send the ``HARDCopy:READOuts?`` query.
        - Using the ``.verify(value)`` method will send the ``HARDCopy:READOuts?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HARDCopy:READOuts value`` command.

    SCPI Syntax:
        ```
        - HARDCopy:READOuts {OFFGRAticule|ONGRAticule}
        - HARDCopy:READOuts?
        ```

    Info:
        - ``OFFGRATICULE`` places the readouts off the graticule area.
        - ``ONGRATICULE`` places the readouts on the graticule area on hardcopies.
    """


class HardcopyPort(SCPICmdWrite, SCPICmdRead):
    """The ``HARDCopy:PORT`` command.

    Description:
        - This command selects or returns whether the hard copy data will be sent to a file or
          printed on the next hard copy command (for example, the HARDCopy STARt command). This is
          equivalent to selecting Print in the File menu and then either choosing Print to file or
          specifying the default printer. If FILE is selected then the EXPORT setup commands are
          used to create the file. If PRINTER is selected, then the HARDCOPY commands are used to
          send the data to the printer.

    Usage:
        - Using the ``.query()`` method will send the ``HARDCopy:PORT?`` query.
        - Using the ``.verify(value)`` method will send the ``HARDCopy:PORT?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HARDCopy:PORT value`` command.

    SCPI Syntax:
        ```
        - HARDCopy:PORT {FILE|PRINTER}
        - HARDCopy:PORT?
        ```

    Info:
        - ``FILE`` argument specifies that the hard copy is stored in the file specified in the
          ``HARDCOPY:FILENAME`` command.
        - ``PRINTER`` argument specifies that the hard copy is sent to the printer specified in the
          Print dialog box.
    """


class HardcopyPalette(SCPICmdWrite, SCPICmdRead):
    """The ``HARDCopy:PALEtte`` command.

    Description:
        - This command sets or queries the hard copy color palette.

    Usage:
        - Using the ``.query()`` method will send the ``HARDCopy:PALEtte?`` query.
        - Using the ``.verify(value)`` method will send the ``HARDCopy:PALEtte?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HARDCopy:PALEtte value`` command.

    SCPI Syntax:
        ```
        - HARDCopy:PALEtte {COLOr|BLACKANDWhite|INKSaver}
        - HARDCopy:PALEtte?
        ```

    Info:
        - ``COLOr`` argument sets the hard copy output to color.
        - ``BLACKANDwhite`` argument sets the hard copy output to black and white.
        - ``INKSaver`` argument sets the hard copy output to save ink.
    """


class HardcopyLayout(SCPICmdWrite, SCPICmdRead):
    """The ``HARDCopy:LAYout`` command.

    Description:
        - This command specifies the page orientation for hard copy. If you set the layout to
          LANdscape, the printer will print hard copies in landscape mode where the long edge of the
          screen will print to the long edge of the sheet of paper. If you set the layout to
          PORTRait, the printer will print hard copies in portrait mode. This command is not
          applicable for PictBridge hardcopies.

    Usage:
        - Using the ``.query()`` method will send the ``HARDCopy:LAYout?`` query.
        - Using the ``.verify(value)`` method will send the ``HARDCopy:LAYout?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HARDCopy:LAYout value`` command.

    SCPI Syntax:
        ```
        - HARDCopy:LAYout {PORTRait|LANdscape}
        - HARDCopy:LAYout?
        ```

    Info:
        - ``PORTRait`` orients the screen image vertically on the printed page.
        - ``LANdscape`` orients the screen image horizontally on the printed page.
    """


class HardcopyFilename(SCPICmdWrite, SCPICmdRead):
    """The ``HARDCopy:FILEName`` command.

    Description:
        - This command sets or queries the file that will be sent hardcopy data on the next HARDCopy
          command (if the ``HARDCopy:PORT`` is set to FILE).

    Usage:
        - Using the ``.query()`` method will send the ``HARDCopy:FILEName?`` query.
        - Using the ``.verify(value)`` method will send the ``HARDCopy:FILEName?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HARDCopy:FILEName value`` command.

    SCPI Syntax:
        ```
        - HARDCopy:FILEName <file path>
        - HARDCopy:FILEName?
        ```

    Info:
        - ``<file path>`` specifies that the hard copy is sent to the named file. <file path> is a
          quoted string that defines the file name and path. Input the file path using the form
          ``<drive>:<dir>``/<filename>.<drive> and one or more <dir>s are optional. The file path
          cannot exceed 128 characters. If you do not specify the path with <drive>: and one or more
          <dir>s, the default location is 'C:UsersPublicTektronixTekScopeScreen Captures'. The
          filename extension is set by the ``EXPort:FORMat`` command.
    """


class Hardcopy(SCPICmdWrite, SCPICmdRead):
    """The ``HARDCopy`` command.

    Description:
        - This command sends a copy of the screen display to the port specified by
          ``HARDCopy:PORT``. This command is equivalent to pressing the PRINT button on the front
          panel. When printing to a file, the file format can be BMP, JPG, PNG, PCX or TIFF. The
          format of the saved screen capture is set by the ``EXPORT:FORMAT`` command. The file
          format setting is persistent, and will not be affected by a default setup or ``*RST``
          command sent to the instrument. The ``HARDCopy`` query returns the port and file path.

    Usage:
        - Using the ``.query()`` method will send the ``HARDCopy?`` query.
        - Using the ``.verify(value)`` method will send the ``HARDCopy?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HARDCopy value`` command.

    SCPI Syntax:
        ```
        - HARDCopy STARt
        - HARDCopy?
        ```

    Info:
        - ``STARt`` initiates a screen copy to a file or the default system printer, as specified by
          the ``:HARDCopy:PORT`` selection. The default system printer is set within the Windows
          operating system. If you need information about how to set the default system printer,
          refer to Microsoft Windows online help.

    Properties:
        - ``.filename``: The ``HARDCopy:FILEName`` command.
        - ``.layout``: The ``HARDCopy:LAYout`` command.
        - ``.palette``: The ``HARDCopy:PALEtte`` command.
        - ``.port``: The ``HARDCopy:PORT`` command.
        - ``.readouts``: The ``HARDCopy:READOuts`` command.
        - ``.view``: The ``HARDCopy:VIEW`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "HARDCopy") -> None:
        super().__init__(device, cmd_syntax)
        self._filename = HardcopyFilename(device, f"{self._cmd_syntax}:FILEName")
        self._layout = HardcopyLayout(device, f"{self._cmd_syntax}:LAYout")
        self._palette = HardcopyPalette(device, f"{self._cmd_syntax}:PALEtte")
        self._port = HardcopyPort(device, f"{self._cmd_syntax}:PORT")
        self._readouts = HardcopyReadouts(device, f"{self._cmd_syntax}:READOuts")
        self._view = HardcopyView(device, f"{self._cmd_syntax}:VIEW")

    @property
    def filename(self) -> HardcopyFilename:
        """Return the ``HARDCopy:FILEName`` command.

        Description:
            - This command sets or queries the file that will be sent hardcopy data on the next
              HARDCopy command (if the ``HARDCopy:PORT`` is set to FILE).

        Usage:
            - Using the ``.query()`` method will send the ``HARDCopy:FILEName?`` query.
            - Using the ``.verify(value)`` method will send the ``HARDCopy:FILEName?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HARDCopy:FILEName value`` command.

        SCPI Syntax:
            ```
            - HARDCopy:FILEName <file path>
            - HARDCopy:FILEName?
            ```

        Info:
            - ``<file path>`` specifies that the hard copy is sent to the named file. <file path> is
              a quoted string that defines the file name and path. Input the file path using the
              form ``<drive>:<dir>``/<filename>.<drive> and one or more <dir>s are optional. The
              file path cannot exceed 128 characters. If you do not specify the path with <drive>:
              and one or more <dir>s, the default location is 'C:UsersPublicTektronixTekScopeScreen
              Captures'. The filename extension is set by the ``EXPort:FORMat`` command.
        """
        return self._filename

    @property
    def layout(self) -> HardcopyLayout:
        """Return the ``HARDCopy:LAYout`` command.

        Description:
            - This command specifies the page orientation for hard copy. If you set the layout to
              LANdscape, the printer will print hard copies in landscape mode where the long edge of
              the screen will print to the long edge of the sheet of paper. If you set the layout to
              PORTRait, the printer will print hard copies in portrait mode. This command is not
              applicable for PictBridge hardcopies.

        Usage:
            - Using the ``.query()`` method will send the ``HARDCopy:LAYout?`` query.
            - Using the ``.verify(value)`` method will send the ``HARDCopy:LAYout?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HARDCopy:LAYout value`` command.

        SCPI Syntax:
            ```
            - HARDCopy:LAYout {PORTRait|LANdscape}
            - HARDCopy:LAYout?
            ```

        Info:
            - ``PORTRait`` orients the screen image vertically on the printed page.
            - ``LANdscape`` orients the screen image horizontally on the printed page.
        """
        return self._layout

    @property
    def palette(self) -> HardcopyPalette:
        """Return the ``HARDCopy:PALEtte`` command.

        Description:
            - This command sets or queries the hard copy color palette.

        Usage:
            - Using the ``.query()`` method will send the ``HARDCopy:PALEtte?`` query.
            - Using the ``.verify(value)`` method will send the ``HARDCopy:PALEtte?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HARDCopy:PALEtte value`` command.

        SCPI Syntax:
            ```
            - HARDCopy:PALEtte {COLOr|BLACKANDWhite|INKSaver}
            - HARDCopy:PALEtte?
            ```

        Info:
            - ``COLOr`` argument sets the hard copy output to color.
            - ``BLACKANDwhite`` argument sets the hard copy output to black and white.
            - ``INKSaver`` argument sets the hard copy output to save ink.
        """
        return self._palette

    @property
    def port(self) -> HardcopyPort:
        """Return the ``HARDCopy:PORT`` command.

        Description:
            - This command selects or returns whether the hard copy data will be sent to a file or
              printed on the next hard copy command (for example, the HARDCopy STARt command). This
              is equivalent to selecting Print in the File menu and then either choosing Print to
              file or specifying the default printer. If FILE is selected then the EXPORT setup
              commands are used to create the file. If PRINTER is selected, then the HARDCOPY
              commands are used to send the data to the printer.

        Usage:
            - Using the ``.query()`` method will send the ``HARDCopy:PORT?`` query.
            - Using the ``.verify(value)`` method will send the ``HARDCopy:PORT?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HARDCopy:PORT value`` command.

        SCPI Syntax:
            ```
            - HARDCopy:PORT {FILE|PRINTER}
            - HARDCopy:PORT?
            ```

        Info:
            - ``FILE`` argument specifies that the hard copy is stored in the file specified in the
              ``HARDCOPY:FILENAME`` command.
            - ``PRINTER`` argument specifies that the hard copy is sent to the printer specified in
              the Print dialog box.
        """
        return self._port

    @property
    def readouts(self) -> HardcopyReadouts:
        """Return the ``HARDCopy:READOuts`` command.

        Description:
            - This command sets or queries the area on a hard copy where the readout appears. This
              command is equivalent to selecting Page Setup from the File menu and setting the
              Readouts Below Graticule in the control window.

        Usage:
            - Using the ``.query()`` method will send the ``HARDCopy:READOuts?`` query.
            - Using the ``.verify(value)`` method will send the ``HARDCopy:READOuts?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HARDCopy:READOuts value`` command.

        SCPI Syntax:
            ```
            - HARDCopy:READOuts {OFFGRAticule|ONGRAticule}
            - HARDCopy:READOuts?
            ```

        Info:
            - ``OFFGRATICULE`` places the readouts off the graticule area.
            - ``ONGRATICULE`` places the readouts on the graticule area on hardcopies.
        """
        return self._readouts

    @property
    def view(self) -> HardcopyView:
        """Return the ``HARDCopy:VIEW`` command.

        Description:
            - This command sets or queries the area of the screen to be hard copied.

        Usage:
            - Using the ``.query()`` method will send the ``HARDCopy:VIEW?`` query.
            - Using the ``.verify(value)`` method will send the ``HARDCopy:VIEW?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HARDCopy:VIEW value`` command.

        SCPI Syntax:
            ```
            - HARDCopy:VIEW {FULLSCREEN|GRAticule|FULLNOmenu}
            - HARDCopy:VIEW?
            ```

        Info:
            - ``FULLSCREEN`` sets the area to be hard copied to both the graticule and menu areas of
              the screen.
            - ``GRAticule`` sets the area to be hard copied to only the graticule area of the
              screen.
            - ``FULLNOmenu`` sets the area to be hard copied to full screen but hides any menus or
              toolbars.
        """
        return self._view
