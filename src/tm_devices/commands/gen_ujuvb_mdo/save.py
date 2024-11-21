"""The save commands module.

These commands are used in the following models:
MDO3

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SAVe:ASSIgn:TYPe {IMAGe|WAVEform|SETUp|UNASsigned}
    - SAVe:ASSIgn:TYPe?
    - SAVe:EVENTtable:B<x> <file path>
    - SAVe:EVENTtable:BUS<x> <file path>
    - SAVe:IMAGe <file path>
    - SAVe:IMAGe:FILEFormat {PNG|BMP|TIFf}
    - SAVe:IMAGe:FILEFormat?
    - SAVe:IMAGe:INKSaver {OFF|ON|0|1}
    - SAVe:IMAGe:INKSaver?
    - SAVe:IMAGe:LAYout {LANdscape|PORTRait}
    - SAVe:IMAGe:LAYout?
    - SAVe:MASK <QString>
    - SAVe:SETUp {<file path>|<NR1>}
    - SAVe:WAVEform <Source>,<Destination>
    - SAVe:WAVEform:FILEFormat {INTERNal|SPREADSheet}
    - SAVe:WAVEform:FILEFormat:RF_BB_IQ {TIQ|MATLAB}
    - SAVe:WAVEform:FILEFormat:RF_BB_IQ?
    - SAVe:WAVEform:FILEFormat?
    - SAVe:WAVEform:GATIng {NONe|CURSors|SCREEN}
    - SAVe:WAVEform:GATIng?
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


class SaveWaveformFileformatRfBbIq(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:WAVEform:FILEFormat:RF_BB_IQ`` command.

    Description:
        - This command specifies the file format for saving the RF baseband I & Q data. The default
          format is TIQ. See the description of the ``SAVE:WAVEFORM`` command for detailed
          information about these formats.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:WAVEform:FILEFormat:RF_BB_IQ?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe:WAVEform:FILEFormat:RF_BB_IQ?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SAVe:WAVEform:FILEFormat:RF_BB_IQ value`` command.

    SCPI Syntax:
        ```
        - SAVe:WAVEform:FILEFormat:RF_BB_IQ {TIQ|MATLAB}
        - SAVe:WAVEform:FILEFormat:RF_BB_IQ?
        ```

    Info:
        - ``TIQ`` specifies to use the TIQ file format for saving the RF baseband I & Q data.
        - ``MATLAB`` specifies to use the MATLAB file format for saving the RF baseband I & Q data.
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

    Properties:
        - ``.rf_bb_iq``: The ``SAVe:WAVEform:FILEFormat:RF_BB_IQ`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._rf_bb_iq = SaveWaveformFileformatRfBbIq(device, f"{self._cmd_syntax}:RF_BB_IQ")

    @property
    def rf_bb_iq(self) -> SaveWaveformFileformatRfBbIq:
        """Return the ``SAVe:WAVEform:FILEFormat:RF_BB_IQ`` command.

        Description:
            - This command specifies the file format for saving the RF baseband I & Q data. The
              default format is TIQ. See the description of the ``SAVE:WAVEFORM`` command for
              detailed information about these formats.

        Usage:
            - Using the ``.query()`` method will send the ``SAVe:WAVEform:FILEFormat:RF_BB_IQ?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SAVe:WAVEform:FILEFormat:RF_BB_IQ?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SAVe:WAVEform:FILEFormat:RF_BB_IQ value`` command.

        SCPI Syntax:
            ```
            - SAVe:WAVEform:FILEFormat:RF_BB_IQ {TIQ|MATLAB}
            - SAVe:WAVEform:FILEFormat:RF_BB_IQ?
            ```

        Info:
            - ``TIQ`` specifies to use the TIQ file format for saving the RF baseband I & Q data.
            - ``MATLAB`` specifies to use the MATLAB file format for saving the RF baseband I & Q
              data.
        """
        return self._rf_bb_iq


class SaveWaveform(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:WAVEform`` command.

    Description:
        - This command saves the specified waveform to the specified destination reference memory,
          or saves the specified waveform(s) to the specified destination file.

    Usage:
        - Using the ``.write(value)`` method will send the ``SAVe:WAVEform value`` command.

    SCPI Syntax:
        ```
        - SAVe:WAVEform <Source>,<Destination>
        ```

    Info:
        - ``CH<x>`` - x has a minimum of 1 and a maximum of 4.
        - ``D<x>`` - x has a minimum of 0 and a maximum of 15.
        - ``EMEM`` (instruments with the arbitrary waveform feature) - EMEM is the arbitrary
          waveform edit memory.
        - ``ARB<x>`` is one of the internal arbitrary waveform storage locations.
        - ``RF_NORMal, RF_AVErage, RF_MAXHold, RF_MINHold`` - These sources can be saved to REF1-4,
          an ISF or CSV file.
        - ``RF_BB_IQ`` - specifies to save baseband I & Q data.
        - ``ALL`` - Specifies all displayed waveforms subject to the restrictions indicated in the
          note below for saving ALL waveforms.
        - ``REF<x>`` - For saving a single scope waveform to one of the 4 internal reference
          waveform memory storage locations (see descriptions for source waveforms above for which
          waveforms can be saved to REF1-4).
        - ``EMEM`` - For instruments with the arbitrary waveform feature, scope waveforms (CH1-4,
          MATH, REF1-4, D0-D15) can be saved to arbitrary waveform edit memory.
        - ``ARB<x>`` - For instruments with the arbitrary waveform feature, EMEM can be saved to one
          of the 4 internal arbitrary waveform memorylocations.
        - ``<file path>`` - Specifies the destination file path to save the specified waveform(s).

    Properties:
        - ``.fileformat``: The ``SAVe:WAVEform:FILEFormat`` command.
        - ``.gating``: The ``SAVe:WAVEform:GATIng`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fileformat = SaveWaveformFileformat(device, f"{self._cmd_syntax}:FILEFormat")
        self._gating = SaveWaveformGating(device, f"{self._cmd_syntax}:GATIng")

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

        Sub-properties:
            - ``.rf_bb_iq``: The ``SAVe:WAVEform:FILEFormat:RF_BB_IQ`` command.
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


class SaveMask(SCPICmdWrite):
    """The ``SAVe:MASK`` command.

    Description:
        - This command saves the current mask definition to the file specified with a quoted string,
          into the current working directory. You can recall the mask from the file by using the
          command ``RECALL:MASK A`` series of examples showing how to use mask commands for typical
          tasks is included in an appendix.

    Usage:
        - Using the ``.write(value)`` method will send the ``SAVe:MASK value`` command.

    SCPI Syntax:
        ```
        - SAVe:MASK <QString>
        ```

    Info:
        - ``QString`` is a quoted string that is the name of the mask definition being saved to the
          current working directory.
    """

    _WRAP_ARG_WITH_QUOTES = True


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


class SaveImageInksaver(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:IMAGe:INKSaver`` command.

    Description:
        - This command specifies the current ink saver setting for the ``SAVE:IMAGE`` command. If
          set to 'ON' or '1', images will be generated using the ink saver palette. If set to 'OFF'
          or '0', images will be generated using the standard palette.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:IMAGe:INKSaver?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe:IMAGe:INKSaver?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVe:IMAGe:INKSaver value`` command.

    SCPI Syntax:
        ```
        - SAVe:IMAGe:INKSaver {OFF|ON|0|1}
        - SAVe:IMAGe:INKSaver?
        ```

    Info:
        - ``OFF`` or 0 generates images from the Inksaver palette.
        - ``ON`` or 1 generates images using the Standard palette.
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
        - ``.inksaver``: The ``SAVe:IMAGe:INKSaver`` command.
        - ``.layout``: The ``SAVe:IMAGe:LAYout`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fileformat = SaveImageFileformat(device, f"{self._cmd_syntax}:FILEFormat")
        self._inksaver = SaveImageInksaver(device, f"{self._cmd_syntax}:INKSaver")
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
    def inksaver(self) -> SaveImageInksaver:
        """Return the ``SAVe:IMAGe:INKSaver`` command.

        Description:
            - This command specifies the current ink saver setting for the ``SAVE:IMAGE`` command.
              If set to 'ON' or '1', images will be generated using the ink saver palette. If set to
              'OFF' or '0', images will be generated using the standard palette.

        Usage:
            - Using the ``.query()`` method will send the ``SAVe:IMAGe:INKSaver?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVe:IMAGe:INKSaver?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVe:IMAGe:INKSaver value``
              command.

        SCPI Syntax:
            ```
            - SAVe:IMAGe:INKSaver {OFF|ON|0|1}
            - SAVe:IMAGe:INKSaver?
            ```

        Info:
            - ``OFF`` or 0 generates images from the Inksaver palette.
            - ``ON`` or 1 generates images using the Standard palette.
        """
        return self._inksaver

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
          (1-2).

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


class SaveEventtableBItem(ValidatedDynamicNumberCmd, SCPICmdWrite):
    """The ``SAVe:EVENTtable:B<x>`` command.

    Description:
        - Saves the data from bus<x> to a specified file and location; where x is the bus number
          (1-2).

    Usage:
        - Using the ``.write(value)`` method will send the ``SAVe:EVENTtable:B<x> value`` command.

    SCPI Syntax:
        ```
        - SAVe:EVENTtable:B<x> <file path>
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
        - ``.b``: The ``SAVe:EVENTtable:B<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bus: Dict[int, SaveEventtableBusItem] = DefaultDictPassKeyToFactory(
            lambda x: SaveEventtableBusItem(device, f"{self._cmd_syntax}:BUS{x}")
        )
        self._b: Dict[int, SaveEventtableBItem] = DefaultDictPassKeyToFactory(
            lambda x: SaveEventtableBItem(device, f"{self._cmd_syntax}:B{x}")
        )

    @property
    def bus(self) -> Dict[int, SaveEventtableBusItem]:
        """Return the ``SAVe:EVENTtable:BUS<x>`` command.

        Description:
            - Saves the data from bus<x> to a specified file and location; where x is the bus number
              (1-2).

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

    @property
    def b(self) -> Dict[int, SaveEventtableBItem]:
        """Return the ``SAVe:EVENTtable:B<x>`` command.

        Description:
            - Saves the data from bus<x> to a specified file and location; where x is the bus number
              (1-2).

        Usage:
            - Using the ``.write(value)`` method will send the ``SAVe:EVENTtable:B<x> value``
              command.

        SCPI Syntax:
            ```
            - SAVe:EVENTtable:B<x> <file path>
            ```

        Info:
            - ``<file path>`` is a quoted string that defines the file name and path location where
              the event table will be stored.
        """
        return self._b


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
        - SAVe:ASSIgn:TYPe {IMAGe|WAVEform|SETUp|UNASsigned}
        - SAVe:ASSIgn:TYPe?
        ```

    Info:
        - ``IMAGe`` assigns the Save button to save screen images.
        - ``WAVEform`` assigns the Save button to save waveforms.
        - ``SETUp`` assigns the Save button to save setups.
        - ``UNASsigned`` sets the Save button to unassigned.
    """


class SaveAssign(SCPICmdRead):
    """The ``SAVe:ASSIgn`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:ASSIgn?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe:ASSIgn?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.type``: The ``SAVe:ASSIgn:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._type = SaveAssignType(device, f"{self._cmd_syntax}:TYPe")

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
            - SAVe:ASSIgn:TYPe {IMAGe|WAVEform|SETUp|UNASsigned}
            - SAVe:ASSIgn:TYPe?
            ```

        Info:
            - ``IMAGe`` assigns the Save button to save screen images.
            - ``WAVEform`` assigns the Save button to save waveforms.
            - ``SETUp`` assigns the Save button to save setups.
            - ``UNASsigned`` sets the Save button to unassigned.
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
        - ``.mask``: The ``SAVe:MASK`` command.
        - ``.setup``: The ``SAVe:SETUp`` command.
        - ``.waveform``: The ``SAVe:WAVEform`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SAVe") -> None:
        super().__init__(device, cmd_syntax)
        self._assign = SaveAssign(device, f"{self._cmd_syntax}:ASSIgn")
        self._eventtable = SaveEventtable(device, f"{self._cmd_syntax}:EVENTtable")
        self._image = SaveImage(device, f"{self._cmd_syntax}:IMAGe")
        self._mask = SaveMask(device, f"{self._cmd_syntax}:MASK")
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
            - ``.b``: The ``SAVe:EVENTtable:B<x>`` command.
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
            - ``.inksaver``: The ``SAVe:IMAGe:INKSaver`` command.
            - ``.layout``: The ``SAVe:IMAGe:LAYout`` command.
        """
        return self._image

    @property
    def mask(self) -> SaveMask:
        """Return the ``SAVe:MASK`` command.

        Description:
            - This command saves the current mask definition to the file specified with a quoted
              string, into the current working directory. You can recall the mask from the file by
              using the command ``RECALL:MASK A`` series of examples showing how to use mask
              commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.write(value)`` method will send the ``SAVe:MASK value`` command.

        SCPI Syntax:
            ```
            - SAVe:MASK <QString>
            ```

        Info:
            - ``QString`` is a quoted string that is the name of the mask definition being saved to
              the current working directory.
        """
        return self._mask

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
            - This command saves the specified waveform to the specified destination reference
              memory, or saves the specified waveform(s) to the specified destination file.

        Usage:
            - Using the ``.write(value)`` method will send the ``SAVe:WAVEform value`` command.

        SCPI Syntax:
            ```
            - SAVe:WAVEform <Source>,<Destination>
            ```

        Info:
            - ``CH<x>`` - x has a minimum of 1 and a maximum of 4.
            - ``D<x>`` - x has a minimum of 0 and a maximum of 15.
            - ``EMEM`` (instruments with the arbitrary waveform feature) - EMEM is the arbitrary
              waveform edit memory.
            - ``ARB<x>`` is one of the internal arbitrary waveform storage locations.
            - ``RF_NORMal, RF_AVErage, RF_MAXHold, RF_MINHold`` - These sources can be saved to
              REF1-4, an ISF or CSV file.
            - ``RF_BB_IQ`` - specifies to save baseband I & Q data.
            - ``ALL`` - Specifies all displayed waveforms subject to the restrictions indicated in
              the note below for saving ALL waveforms.
            - ``REF<x>`` - For saving a single scope waveform to one of the 4 internal reference
              waveform memory storage locations (see descriptions for source waveforms above for
              which waveforms can be saved to REF1-4).
            - ``EMEM`` - For instruments with the arbitrary waveform feature, scope waveforms
              (CH1-4, MATH, REF1-4, D0-D15) can be saved to arbitrary waveform edit memory.
            - ``ARB<x>`` - For instruments with the arbitrary waveform feature, EMEM can be saved to
              one of the 4 internal arbitrary waveform memorylocations.
            - ``<file path>`` - Specifies the destination file path to save the specified
              waveform(s).

        Sub-properties:
            - ``.fileformat``: The ``SAVe:WAVEform:FILEFormat`` command.
            - ``.gating``: The ``SAVe:WAVEform:GATIng`` command.
        """
        return self._waveform
