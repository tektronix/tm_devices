"""The save commands module.

These commands are used in the following models:
DPO2K, DPO2KB, MSO2K, MSO2KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SAVe:ASSIgn:FOLder?
    - SAVe:ASSIgn:TYPe {IMAGe|WAVEform|SETUp}
    - SAVe:ASSIgn:TYPe?
    - SAVe:EVENTtable:BUS<x> <file path>
    - SAVe:IMAGe <file path>
    - SAVe:IMAGe:FILEFormat {PNG|BMP|TIFf}
    - SAVe:IMAGe:FILEFormat?
    - SAVe:IMAGe:LAYout {LANdscape|PORTRait}
    - SAVe:IMAGe:LAYout?
    - SAVe:SETUp {<file path>|<NR1>}
    - SAVe:WAVEform [<wfm>,{REF<x>}] | [<wfm>, <QString>] | [ALL, <QString>]
    - SAVe:WAVEform:FILEFormat {INTERNal|SPREADSheet}
    - SAVe:WAVEform:FILEFormat?
    - SAVe:WAVEform:GATIng {NONe|CURSors|SCREEN}
    - SAVe:WAVEform:GATIng?
    - SAVe:WAVEform:SPREADSheet:RESOlution {FULL|REDUced}
    - SAVe:WAVEform:SPREADSheet:RESOlution?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class SaveWaveformSpreadsheetResolution(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:WAVEform:SPREADSheet:RESOlution`` command.

    Description:
        - Specifies whether to save the full (LRL) or reduced (thumb) resolution waveform to a CSV
          file.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:WAVEform:SPREADSheet:RESOlution?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SAVe:WAVEform:SPREADSheet:RESOlution?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SAVe:WAVEform:SPREADSheet:RESOlution value`` command.

    SCPI Syntax:
        ```
        - SAVe:WAVEform:SPREADSheet:RESOlution {FULL|REDUced}
        - SAVe:WAVEform:SPREADSheet:RESOlution?
        ```

    Info:
        - ``FULL`` specifies that full resolution waveform is saved to a CSV file.
        - ``REDUced`` specifies that reduced resolution waveform is saved to a CSV file.
    """


class SaveWaveformSpreadsheet(SCPICmdRead):
    """The ``SAVe:WAVEform:SPREADSheet`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:WAVEform:SPREADSheet?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe:WAVEform:SPREADSheet?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.resolution``: The ``SAVe:WAVEform:SPREADSheet:RESOlution`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._resolution = SaveWaveformSpreadsheetResolution(
            device, f"{self._cmd_syntax}:RESOlution"
        )

    @property
    def resolution(self) -> SaveWaveformSpreadsheetResolution:
        """Return the ``SAVe:WAVEform:SPREADSheet:RESOlution`` command.

        Description:
            - Specifies whether to save the full (LRL) or reduced (thumb) resolution waveform to a
              CSV file.

        Usage:
            - Using the ``.query()`` method will send the ``SAVe:WAVEform:SPREADSheet:RESOlution?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SAVe:WAVEform:SPREADSheet:RESOlution?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SAVe:WAVEform:SPREADSheet:RESOlution value`` command.

        SCPI Syntax:
            ```
            - SAVe:WAVEform:SPREADSheet:RESOlution {FULL|REDUced}
            - SAVe:WAVEform:SPREADSheet:RESOlution?
            ```

        Info:
            - ``FULL`` specifies that full resolution waveform is saved to a CSV file.
            - ``REDUced`` specifies that reduced resolution waveform is saved to a CSV file.
        """
        return self._resolution


class SaveWaveformGating(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:WAVEform:GATIng`` command.

    Description:
        - Specifies whether save waveform operations should save the entire waveform (NONe) or a
          specified portion of the waveform.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:WAVEform:GATIng?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe:WAVEform:GATIng?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVe:WAVEform:GATIng value`` command.

    SCPI Syntax:
        ```
        - SAVe:WAVEform:GATIng {NONe|CURSors|SCREEN}
        - SAVe:WAVEform:GATIng?
        ```

    Info:
        - ``CURSors`` turns on cursors and the gates are the waveform record points at the cursor
          positions.
        - ``NONe`` saves the entire waveform.
        - ``SCREEN`` , if zoom is on, the gates are the start and end waveform record points of the
          zoom (upper) graticule, otherwise the gates are the start and end waveform record points
          of the main graticule.
    """


class SaveWaveformFileformat(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:WAVEform:FILEFormat`` command.

    Description:
        - This command specifies the file format to be used when saving waveforms - either an
          internal format, .ISF, or an external comma-delimited spreadsheet format, .CSV, that
          includes waveform header and timing information.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:WAVEform:FILEFormat?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe:WAVEform:FILEFormat?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVe:WAVEform:FILEFormat value``
          command.

    SCPI Syntax:
        ```
        - SAVe:WAVEform:FILEFormat {INTERNal|SPREADSheet}
        - SAVe:WAVEform:FILEFormat?
        ```

    Info:
        - ``INTERNal`` specifies to save waveforms using an internal format. The file name should be
          specified with .ISF filename extension. These files can be recalled as reference
          waveforms.
        - ``SPREADSheet`` specifies that waveform data is saved in a format that contains comma
          delimited values. These waveform data files should be named using the .CSV filename
          extension. Saving waveforms in .CSV format enables spreadsheet programs to import the
          data.
    """


class SaveWaveform(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:WAVEform`` command.

    Description:
        - This command saves a specified waveform or all displayed waveforms (excluding serial bus
          waveforms).

    Usage:
        - Using the ``.write(value)`` method will send the ``SAVe:WAVEform value`` command.

    SCPI Syntax:
        ```
        - SAVe:WAVEform [<wfm>,{REF<x>}] | [<wfm>, <QString>] | [ALL, <QString>]
        ```

    Info:
        - ``<wfm>, <REF<x>>`` saves the specified waveform to the specified reference memory
          location.
        - ``<wfm>, <QString>`` saves the specified waveform to the file specified in the quoted
          string argument.
        - ``ALL, <QString>`` saves all displayed waveforms, excluding serial bus waveforms, to a
          single CSV file specified by the quoted string argument when the
          ``SAVE:WAVEFORM:FILEFORMAT`` is set to SPREADSHEET, or saves all displayed waveforms,
          excluding serial bus waveforms to individual ISF (internal save format) files with a file
          name prefix specified by the argument with an underscore (_) and the waveform ID (such as
          CH1, REF1, MATH) appended to the file name(s).

    Properties:
        - ``.fileformat``: The ``SAVe:WAVEform:FILEFormat`` command.
        - ``.gating``: The ``SAVe:WAVEform:GATIng`` command.
        - ``.spreadsheet``: The ``SAVe:WAVEform:SPREADSheet`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fileformat = SaveWaveformFileformat(device, f"{self._cmd_syntax}:FILEFormat")
        self._gating = SaveWaveformGating(device, f"{self._cmd_syntax}:GATIng")
        self._spreadsheet = SaveWaveformSpreadsheet(device, f"{self._cmd_syntax}:SPREADSheet")

    @property
    def fileformat(self) -> SaveWaveformFileformat:
        """Return the ``SAVe:WAVEform:FILEFormat`` command.

        Description:
            - This command specifies the file format to be used when saving waveforms - either an
              internal format, .ISF, or an external comma-delimited spreadsheet format, .CSV, that
              includes waveform header and timing information.

        Usage:
            - Using the ``.query()`` method will send the ``SAVe:WAVEform:FILEFormat?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVe:WAVEform:FILEFormat?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVe:WAVEform:FILEFormat value``
              command.

        SCPI Syntax:
            ```
            - SAVe:WAVEform:FILEFormat {INTERNal|SPREADSheet}
            - SAVe:WAVEform:FILEFormat?
            ```

        Info:
            - ``INTERNal`` specifies to save waveforms using an internal format. The file name
              should be specified with .ISF filename extension. These files can be recalled as
              reference waveforms.
            - ``SPREADSheet`` specifies that waveform data is saved in a format that contains comma
              delimited values. These waveform data files should be named using the .CSV filename
              extension. Saving waveforms in .CSV format enables spreadsheet programs to import the
              data.
        """
        return self._fileformat

    @property
    def gating(self) -> SaveWaveformGating:
        """Return the ``SAVe:WAVEform:GATIng`` command.

        Description:
            - Specifies whether save waveform operations should save the entire waveform (NONe) or a
              specified portion of the waveform.

        Usage:
            - Using the ``.query()`` method will send the ``SAVe:WAVEform:GATIng?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVe:WAVEform:GATIng?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVe:WAVEform:GATIng value``
              command.

        SCPI Syntax:
            ```
            - SAVe:WAVEform:GATIng {NONe|CURSors|SCREEN}
            - SAVe:WAVEform:GATIng?
            ```

        Info:
            - ``CURSors`` turns on cursors and the gates are the waveform record points at the
              cursor positions.
            - ``NONe`` saves the entire waveform.
            - ``SCREEN`` , if zoom is on, the gates are the start and end waveform record points of
              the zoom (upper) graticule, otherwise the gates are the start and end waveform record
              points of the main graticule.
        """
        return self._gating

    @property
    def spreadsheet(self) -> SaveWaveformSpreadsheet:
        """Return the ``SAVe:WAVEform:SPREADSheet`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SAVe:WAVEform:SPREADSheet?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVe:WAVEform:SPREADSheet?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.resolution``: The ``SAVe:WAVEform:SPREADSheet:RESOlution`` command.
        """
        return self._spreadsheet


class SaveSetup(SCPICmdWrite):
    """The ``SAVe:SETUp`` command.

    Description:
        - Stores the state of the oscilloscope to a specified memory location. You can later use the
          ``*RCL`` command to restore the oscilloscope to this saved state.

    Usage:
        - Using the ``.write(value)`` method will send the ``SAVe:SETUp value`` command.

    SCPI Syntax:
        ```
        - SAVe:SETUp {<file path>|<NR1>}
        ```

    Info:
        - ``<file path>`` is the target location for storing the setup file. <file path> is a quoted
          string that defines the file name and path. Input the file path using the form
          ``<drive>:<dir>``/<filename>. <extension> and one or <dir>s are optional. If you do not
          specify them, the oscilloscope will store the file in the current working directory.
          <filename> stands for a filename. (Use of wildcard characters in filenames is not
          supported.) Filename extensions are not required but are highly recommended. For setups,
          use the extension '.SET'.
        - ``<NR1>`` specifies a location for saving the current front-panel setup. The front-panel
          setup value ranges from 1 to 10. Using an out-of-range value causes an execution error.
          Any settings that have been stored previously at this location will be overwritten.
    """


class SaveImageLayout(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:IMAGe:LAYout`` command.

    Description:
        - This command specifies the layout to use for saved screen images.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:IMAGe:LAYout?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe:IMAGe:LAYout?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVe:IMAGe:LAYout value`` command.

    SCPI Syntax:
        ```
        - SAVe:IMAGe:LAYout {LANdscape|PORTRait}
        - SAVe:IMAGe:LAYout?
        ```

    Info:
        - ``LANdscape`` specifies that screen images are saved in landscape format.
        - ``PORTRait`` specifies that screen images are saved in portrait format.
    """


class SaveImageFileformat(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:IMAGe:FILEFormat`` command.

    Description:
        - This command specifies the file format to use for saving screen images.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:IMAGe:FILEFormat?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe:IMAGe:FILEFormat?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVe:IMAGe:FILEFormat value`` command.

    SCPI Syntax:
        ```
        - SAVe:IMAGe:FILEFormat {PNG|BMP|TIFf}
        - SAVe:IMAGe:FILEFormat?
        ```

    Info:
        - ``PNG`` saves the file in Portable Network Graphics format.
        - ``BMP`` saves the file in Microsoft Windows bitmap format.
        - ``TIFf`` saves the file in Tagged Image File Format.
    """


class SaveImage(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:IMAGe`` command.

    Description:
        - Saves a capture of the screen image to the specified file. Supported image formats are
          PNG, Windows Bitmap, and TIFF. The file format is specified by the
          ``SAVE:IMAGE:FILEFORMAT`` command. The ``SAVE:IMAGE:INKSAVER`` command determines whether
          the data is saved in InkSaver mode.

    Usage:
        - Using the ``.write(value)`` method will send the ``SAVe:IMAGe value`` command.

    SCPI Syntax:
        ```
        - SAVe:IMAGe <file path>
        ```

    Info:
        - ``<file path>`` is a filename, including path, where the image will be saved. If you do
          not specify a directory, the oscilloscope will store the file in the current working
          directory. File name extensions are not required but are highly recommended.

    Properties:
        - ``.fileformat``: The ``SAVe:IMAGe:FILEFormat`` command.
        - ``.layout``: The ``SAVe:IMAGe:LAYout`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fileformat = SaveImageFileformat(device, f"{self._cmd_syntax}:FILEFormat")
        self._layout = SaveImageLayout(device, f"{self._cmd_syntax}:LAYout")

    @property
    def fileformat(self) -> SaveImageFileformat:
        """Return the ``SAVe:IMAGe:FILEFormat`` command.

        Description:
            - This command specifies the file format to use for saving screen images.

        Usage:
            - Using the ``.query()`` method will send the ``SAVe:IMAGe:FILEFormat?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVe:IMAGe:FILEFormat?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVe:IMAGe:FILEFormat value``
              command.

        SCPI Syntax:
            ```
            - SAVe:IMAGe:FILEFormat {PNG|BMP|TIFf}
            - SAVe:IMAGe:FILEFormat?
            ```

        Info:
            - ``PNG`` saves the file in Portable Network Graphics format.
            - ``BMP`` saves the file in Microsoft Windows bitmap format.
            - ``TIFf`` saves the file in Tagged Image File Format.
        """
        return self._fileformat

    @property
    def layout(self) -> SaveImageLayout:
        """Return the ``SAVe:IMAGe:LAYout`` command.

        Description:
            - This command specifies the layout to use for saved screen images.

        Usage:
            - Using the ``.query()`` method will send the ``SAVe:IMAGe:LAYout?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVe:IMAGe:LAYout?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVe:IMAGe:LAYout value`` command.

        SCPI Syntax:
            ```
            - SAVe:IMAGe:LAYout {LANdscape|PORTRait}
            - SAVe:IMAGe:LAYout?
            ```

        Info:
            - ``LANdscape`` specifies that screen images are saved in landscape format.
            - ``PORTRait`` specifies that screen images are saved in portrait format.
        """
        return self._layout


class SaveEventtableBusItem(ValidatedDynamicNumberCmd, SCPICmdWrite):
    """The ``SAVe:EVENTtable:BUS<x>`` command.

    Description:
        - Saves the data from bus<x> to a specified file and location; where x is the bus number

    Usage:
        - Using the ``.write(value)`` method will send the ``SAVe:EVENTtable:BUS<x> value`` command.

    SCPI Syntax:
        ```
        - SAVe:EVENTtable:BUS<x> <file path>
        ```

    Info:
        - ``<file path>`` is a quoted string that defines the file name and path location where the
          event table will be stored.
    """


class SaveEventtable(SCPICmdRead):
    """The ``SAVe:EVENTtable`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:EVENTtable?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe:EVENTtable?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bus``: The ``SAVe:EVENTtable:BUS<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bus: Dict[int, SaveEventtableBusItem] = DefaultDictPassKeyToFactory(
            lambda x: SaveEventtableBusItem(device, f"{self._cmd_syntax}:BUS{x}")
        )

    @property
    def bus(self) -> Dict[int, SaveEventtableBusItem]:
        """Return the ``SAVe:EVENTtable:BUS<x>`` command.

        Description:
            - Saves the data from bus<x> to a specified file and location; where x is the bus number

        Usage:
            - Using the ``.write(value)`` method will send the ``SAVe:EVENTtable:BUS<x> value``
              command.

        SCPI Syntax:
            ```
            - SAVe:EVENTtable:BUS<x> <file path>
            ```

        Info:
            - ``<file path>`` is a quoted string that defines the file name and path location where
              the event table will be stored.
        """
        return self._bus


class SaveAssignType(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:ASSIgn:TYPe`` command.

    Description:
        - This command specifies the assignment of the data to be saved when the front-panel Save
          button is pressed.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:ASSIgn:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe:ASSIgn:TYPe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVe:ASSIgn:TYPe value`` command.

    SCPI Syntax:
        ```
        - SAVe:ASSIgn:TYPe {IMAGe|WAVEform|SETUp}
        - SAVe:ASSIgn:TYPe?
        ```

    Info:
        - ``IMAGe`` assigns the Save button to save screen images.
        - ``WAVEform`` assigns the Save button to save waveforms.
        - ``SETUp`` assigns the Save button to save setups.
    """


class SaveAssignFolder(SCPICmdRead):
    """The ``SAVe:ASSIgn:FOLder`` command.

    Description:
        - Returns the file name that the next front-panel Save button operation will save the
          requested save type data to.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:ASSIgn:FOLder?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe:ASSIgn:FOLder?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SAVe:ASSIgn:FOLder?
        ```
    """


class SaveAssign(SCPICmdRead):
    """The ``SAVe:ASSIgn`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:ASSIgn?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe:ASSIgn?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.folder``: The ``SAVe:ASSIgn:FOLder`` command.
        - ``.type``: The ``SAVe:ASSIgn:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._folder = SaveAssignFolder(device, f"{self._cmd_syntax}:FOLder")
        self._type = SaveAssignType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def folder(self) -> SaveAssignFolder:
        """Return the ``SAVe:ASSIgn:FOLder`` command.

        Description:
            - Returns the file name that the next front-panel Save button operation will save the
              requested save type data to.

        Usage:
            - Using the ``.query()`` method will send the ``SAVe:ASSIgn:FOLder?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVe:ASSIgn:FOLder?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SAVe:ASSIgn:FOLder?
            ```
        """
        return self._folder

    @property
    def type(self) -> SaveAssignType:
        """Return the ``SAVe:ASSIgn:TYPe`` command.

        Description:
            - This command specifies the assignment of the data to be saved when the front-panel
              Save button is pressed.

        Usage:
            - Using the ``.query()`` method will send the ``SAVe:ASSIgn:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVe:ASSIgn:TYPe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVe:ASSIgn:TYPe value`` command.

        SCPI Syntax:
            ```
            - SAVe:ASSIgn:TYPe {IMAGe|WAVEform|SETUp}
            - SAVe:ASSIgn:TYPe?
            ```

        Info:
            - ``IMAGe`` assigns the Save button to save screen images.
            - ``WAVEform`` assigns the Save button to save waveforms.
            - ``SETUp`` assigns the Save button to save setups.
        """
        return self._type


class Save(SCPICmdRead):
    """The ``SAVe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.assign``: The ``SAVe:ASSIgn`` command tree.
        - ``.eventtable``: The ``SAVe:EVENTtable`` command tree.
        - ``.image``: The ``SAVe:IMAGe`` command.
        - ``.setup``: The ``SAVe:SETUp`` command.
        - ``.waveform``: The ``SAVe:WAVEform`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SAVe") -> None:
        super().__init__(device, cmd_syntax)
        self._assign = SaveAssign(device, f"{self._cmd_syntax}:ASSIgn")
        self._eventtable = SaveEventtable(device, f"{self._cmd_syntax}:EVENTtable")
        self._image = SaveImage(device, f"{self._cmd_syntax}:IMAGe")
        self._setup = SaveSetup(device, f"{self._cmd_syntax}:SETUp")
        self._waveform = SaveWaveform(device, f"{self._cmd_syntax}:WAVEform")

    @property
    def assign(self) -> SaveAssign:
        """Return the ``SAVe:ASSIgn`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SAVe:ASSIgn?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVe:ASSIgn?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.folder``: The ``SAVe:ASSIgn:FOLder`` command.
            - ``.type``: The ``SAVe:ASSIgn:TYPe`` command.
        """
        return self._assign

    @property
    def eventtable(self) -> SaveEventtable:
        """Return the ``SAVe:EVENTtable`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SAVe:EVENTtable?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVe:EVENTtable?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bus``: The ``SAVe:EVENTtable:BUS<x>`` command.
        """
        return self._eventtable

    @property
    def image(self) -> SaveImage:
        """Return the ``SAVe:IMAGe`` command.

        Description:
            - Saves a capture of the screen image to the specified file. Supported image formats are
              PNG, Windows Bitmap, and TIFF. The file format is specified by the
              ``SAVE:IMAGE:FILEFORMAT`` command. The ``SAVE:IMAGE:INKSAVER`` command determines
              whether the data is saved in InkSaver mode.

        Usage:
            - Using the ``.write(value)`` method will send the ``SAVe:IMAGe value`` command.

        SCPI Syntax:
            ```
            - SAVe:IMAGe <file path>
            ```

        Info:
            - ``<file path>`` is a filename, including path, where the image will be saved. If you
              do not specify a directory, the oscilloscope will store the file in the current
              working directory. File name extensions are not required but are highly recommended.

        Sub-properties:
            - ``.fileformat``: The ``SAVe:IMAGe:FILEFormat`` command.
            - ``.layout``: The ``SAVe:IMAGe:LAYout`` command.
        """
        return self._image

    @property
    def setup(self) -> SaveSetup:
        """Return the ``SAVe:SETUp`` command.

        Description:
            - Stores the state of the oscilloscope to a specified memory location. You can later use
              the ``*RCL`` command to restore the oscilloscope to this saved state.

        Usage:
            - Using the ``.write(value)`` method will send the ``SAVe:SETUp value`` command.

        SCPI Syntax:
            ```
            - SAVe:SETUp {<file path>|<NR1>}
            ```

        Info:
            - ``<file path>`` is the target location for storing the setup file. <file path> is a
              quoted string that defines the file name and path. Input the file path using the form
              ``<drive>:<dir>``/<filename>. <extension> and one or <dir>s are optional. If you do
              not specify them, the oscilloscope will store the file in the current working
              directory. <filename> stands for a filename. (Use of wildcard characters in filenames
              is not supported.) Filename extensions are not required but are highly recommended.
              For setups, use the extension '.SET'.
            - ``<NR1>`` specifies a location for saving the current front-panel setup. The
              front-panel setup value ranges from 1 to 10. Using an out-of-range value causes an
              execution error. Any settings that have been stored previously at this location will
              be overwritten.
        """
        return self._setup

    @property
    def waveform(self) -> SaveWaveform:
        """Return the ``SAVe:WAVEform`` command.

        Description:
            - This command saves a specified waveform or all displayed waveforms (excluding serial
              bus waveforms).

        Usage:
            - Using the ``.write(value)`` method will send the ``SAVe:WAVEform value`` command.

        SCPI Syntax:
            ```
            - SAVe:WAVEform [<wfm>,{REF<x>}] | [<wfm>, <QString>] | [ALL, <QString>]
            ```

        Info:
            - ``<wfm>, <REF<x>>`` saves the specified waveform to the specified reference memory
              location.
            - ``<wfm>, <QString>`` saves the specified waveform to the file specified in the quoted
              string argument.
            - ``ALL, <QString>`` saves all displayed waveforms, excluding serial bus waveforms, to a
              single CSV file specified by the quoted string argument when the
              ``SAVE:WAVEFORM:FILEFORMAT`` is set to SPREADSHEET, or saves all displayed waveforms,
              excluding serial bus waveforms to individual ISF (internal save format) files with a
              file name prefix specified by the argument with an underscore (_) and the waveform ID
              (such as CH1, REF1, MATH) appended to the file name(s).

        Sub-properties:
            - ``.fileformat``: The ``SAVe:WAVEform:FILEFormat`` command.
            - ``.gating``: The ``SAVe:WAVEform:GATIng`` command.
            - ``.spreadsheet``: The ``SAVe:WAVEform:SPREADSheet`` command tree.
        """
        return self._waveform
