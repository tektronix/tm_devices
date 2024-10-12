# pylint: disable=line-too-long
"""The save commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SAVe:EVENTtable:BUS<x> <string>
    - SAVe:MARKS <string>
    - SAVe:MASK <QString>
    - SAVe:SETUp {<file path>|<NR1>}
    - SAVe:WAVEform [<wfm>,REF<x>]| [<wfm>,<QString>] | [ALL,[QString]]| [DIGITALALL,<QString>]
    - SAVe:WAVEform:DATa:STARt {<NR1>}
    - SAVe:WAVEform:DATa:STOP {<NR1>}
    - SAVe:WAVEform:FILEFormat {INTERNal|MATHCad|MATLab|SPREADSHEETCsv|SPREADSHEETTxt|TIMEStamp|AUTO}
    - SAVe:WAVEform:FILEFormat?
    - SAVe:WAVEform:FORCESAMEFilesize {ON|OFF|<NR1>}
    - SAVe:WAVEform:FORCESAMEFilesize?
    ```
"""  # noqa: E501

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class SaveWaveformForcesamefilesize(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:WAVEform:FORCESAMEFilesize`` command.

    Description:
        - This command sets or queries the save waveform force same file size.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:WAVEform:FORCESAMEFilesize?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe:WAVEform:FORCESAMEFilesize?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVe:WAVEform:FORCESAMEFilesize value``
          command.

    SCPI Syntax:
        ```
        - SAVe:WAVEform:FORCESAMEFilesize {ON|OFF|<NR1>}
        - SAVe:WAVEform:FORCESAMEFilesize?
        ```

    Info:
        - ``<NR1>`` = 0 disables the function; any other value enables it.
        - ``OFF`` disables the function.
        - ``ON`` enables the function.
    """


class SaveWaveformFileformat(SCPICmdWrite, SCPICmdRead):
    r"""The ``SAVe:WAVEform:FILEFormat`` command.

    Description:
        - This command specifies or returns the file format for saved waveforms. Waveform header and
          timing information is included in the resulting file of non-internal formats. The
          instrument saves DPO waveforms as a 1000 x 502 matrix, with the first row corresponding to
          the most recently acquired data. The values specified by ``SAVE:WAVEFORM:DATA:START`` and
          ``SAVE:WAVEFORM:DATA:STOP`` determine the range of waveform data to output. In the event
          that ``SAVe:WAVEform:DATa:STOP`` value is greater than the current record length, the
          current record length determines the last output value. This command is equivalent to
          selecting Save As from the File menu, clicking the Waveform button, and selecting the
          desired waveform file format.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:WAVEform:FILEFormat?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe:WAVEform:FILEFormat?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVe:WAVEform:FILEFormat value``
          command.

    SCPI Syntax:
        ```
        - SAVe:WAVEform:FILEFormat {INTERNal|MATHCad|MATLab|SPREADSHEETCsv|SPREADSHEETTxt|TIMEStamp|AUTO}
        - SAVe:WAVEform:FILEFormat?
        ```

    Info:
        - ``INTERNal`` specifies that waveforms are saved in an internal format, using a .wfm file
          name extension. These files can be recalled as reference waveforms. When this argument is
          specified, the settings specified via the ``SAVe:WAVEform:DATa:STARt`` and
          ``SAVe:WAVEform:DATa:STOP`` commands have no meaning as the entire waveform is saved.
        - ``MATHCad`` specifies that waveforms are saved in MathCad format, using a .dat file name
          extension. When saving in this format, waveform values are delimited with new lines.
          MathCad format enables easy import of waveform data into MathCad or MATLAB. For FastAcq
          waveforms, data is imported as a matrix. For these formats, waveform header and timing
          information is saved in a separate header file. MathCad format header files use a _hdr.dat
          extension.
        - ``MATLab`` specifies that waveforms are saved in Matlab format, using a .dat file name
          extension. When saving in this format, waveform values are delimited with new lines.
          MATLAB format enables easy import of waveform data into MathCad or MATLAB. For FastAcq
          waveforms, data is imported as a matrix. For these formats, waveform header and timing
          information is saved in a separate header file. MATLAB format header files use a _hdr.dat
          extension.
        - ``SPREADSHEETCsv`` specifies that waveform data is saved in a format that contains comma
          delimited values. These waveform data files are named using the .csv file name extension.
          Saving waveforms in CSV format enables spreadsheet programs to import the data.
        - ``SPREADSHEETTxt`` specifies that waveform data is saved in a format that contains tab
          delimited values. These waveform data files are named using the .txt file name extension.
          Saving waveforms in this format enables spreadsheet programs to import the data.
        - ``TIMEStamp`` specifies that timestamp data is saved in a format that contains comma
          delimited values. These data files are named using the .txt file name extension. Saving
          waveforms in this format enables spreadsheet programs to import the data.
        - ``AUTO`` specifies that the file format should be taken from the file name extension.
          Supported extensions include \\*.wfm, \\*.csv, \\*.txt, \\*.h5). If an extension is read
          that is not supported, no file will be written out. If no extension is given in the
          filename, \\*.csv will be written out. Auto format always uses the entire waveform record
          and does not utilize ``SAVe:WAVEform:DATa:STARt`` or STOP or any other limitations on
          output data.
    """  # noqa: E501


class SaveWaveformDataStop(SCPICmdWrite):
    """The ``SAVe:WAVEform:DATa:STOP`` command.

    Description:
        - Sets or queries the save waveform ending waveform data sample.

    Usage:
        - Using the ``.write(value)`` method will send the ``SAVe:WAVEform:DATa:STOP value``
          command.

    SCPI Syntax:
        ```
        - SAVe:WAVEform:DATa:STOP {<NR1>}
        ```

    Info:
        - ``<NR1>`` specifies the ending waveform sample used by the ``SAVe:WAVEform`` command. This
          works for Spreadsheet CSV, Spreadsheet TXT, Mathcad, and Matlab file formats.
    """


class SaveWaveformDataStart(SCPICmdWrite):
    """The ``SAVe:WAVEform:DATa:STARt`` command.

    Description:
        - Sets or queries the save waveform starting waveform data sample.

    Usage:
        - Using the ``.write(value)`` method will send the ``SAVe:WAVEform:DATa:STARt value``
          command.

    SCPI Syntax:
        ```
        - SAVe:WAVEform:DATa:STARt {<NR1>}
        ```

    Info:
        - ``<NR1>`` specifies the starting waveform sample used by the ``SAVe:WAVEform`` command.
          This works for Spreadsheet CSV, Spreadsheet TXT, Mathcad, and Matlab file formats.
    """


class SaveWaveformData(SCPICmdRead):
    """The ``SAVe:WAVEform:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:WAVEform:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe:WAVEform:DATa?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.start``: The ``SAVe:WAVEform:DATa:STARt`` command.
        - ``.stop``: The ``SAVe:WAVEform:DATa:STOP`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._start = SaveWaveformDataStart(device, f"{self._cmd_syntax}:STARt")
        self._stop = SaveWaveformDataStop(device, f"{self._cmd_syntax}:STOP")

    @property
    def start(self) -> SaveWaveformDataStart:
        """Return the ``SAVe:WAVEform:DATa:STARt`` command.

        Description:
            - Sets or queries the save waveform starting waveform data sample.

        Usage:
            - Using the ``.write(value)`` method will send the ``SAVe:WAVEform:DATa:STARt value``
              command.

        SCPI Syntax:
            ```
            - SAVe:WAVEform:DATa:STARt {<NR1>}
            ```

        Info:
            - ``<NR1>`` specifies the starting waveform sample used by the ``SAVe:WAVEform``
              command. This works for Spreadsheet CSV, Spreadsheet TXT, Mathcad, and Matlab file
              formats.
        """
        return self._start

    @property
    def stop(self) -> SaveWaveformDataStop:
        """Return the ``SAVe:WAVEform:DATa:STOP`` command.

        Description:
            - Sets or queries the save waveform ending waveform data sample.

        Usage:
            - Using the ``.write(value)`` method will send the ``SAVe:WAVEform:DATa:STOP value``
              command.

        SCPI Syntax:
            ```
            - SAVe:WAVEform:DATa:STOP {<NR1>}
            ```

        Info:
            - ``<NR1>`` specifies the ending waveform sample used by the ``SAVe:WAVEform`` command.
              This works for Spreadsheet CSV, Spreadsheet TXT, Mathcad, and Matlab file formats.
        """
        return self._stop


class SaveWaveform(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:WAVEform`` command.

    Description:
        - This command (no query form) saves a waveform to one of four reference memory locations or
          a file.

    Usage:
        - Using the ``.write(value)`` method will send the ``SAVe:WAVEform value`` command.

    SCPI Syntax:
        ```
        - SAVe:WAVEform [<wfm>,REF<x>]| [<wfm>,<QString>] | [ALL,[QString]]| [DIGITALALL,<QString>]
        ```

    Info:
        - ``<wfm>,REF<x>`` saves the specified waveform to the specified reference memory location.
        - ``<wfm>,<QString>`` saves the specified waveform to the file specified.
        - ``ALL,[QString>]`` saves all displayed waveforms, excluding digital waveforms, to
          individual files based on the ``SAVE:WAVEFORM:FILEFORMAT`` setting.
        - ``DIGITALALL,<QString>`` saves all digital waveforms to a single file specified by the
          quoted string argument and based on the ``SAVE:WAVEFORM:FILEFORMAT`` setting.

    Properties:
        - ``.data``: The ``SAVe:WAVEform:DATa`` command tree.
        - ``.fileformat``: The ``SAVe:WAVEform:FILEFormat`` command.
        - ``.forcesamefilesize``: The ``SAVe:WAVEform:FORCESAMEFilesize`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._data = SaveWaveformData(device, f"{self._cmd_syntax}:DATa")
        self._fileformat = SaveWaveformFileformat(device, f"{self._cmd_syntax}:FILEFormat")
        self._forcesamefilesize = SaveWaveformForcesamefilesize(
            device, f"{self._cmd_syntax}:FORCESAMEFilesize"
        )

    @property
    def data(self) -> SaveWaveformData:
        """Return the ``SAVe:WAVEform:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SAVe:WAVEform:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVe:WAVEform:DATa?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.start``: The ``SAVe:WAVEform:DATa:STARt`` command.
            - ``.stop``: The ``SAVe:WAVEform:DATa:STOP`` command.
        """
        return self._data

    @property
    def fileformat(self) -> SaveWaveformFileformat:
        r"""Return the ``SAVe:WAVEform:FILEFormat`` command.

        Description:
            - This command specifies or returns the file format for saved waveforms. Waveform header
              and timing information is included in the resulting file of non-internal formats. The
              instrument saves DPO waveforms as a 1000 x 502 matrix, with the first row
              corresponding to the most recently acquired data. The values specified by
              ``SAVE:WAVEFORM:DATA:START`` and ``SAVE:WAVEFORM:DATA:STOP`` determine the range of
              waveform data to output. In the event that ``SAVe:WAVEform:DATa:STOP`` value is
              greater than the current record length, the current record length determines the last
              output value. This command is equivalent to selecting Save As from the File menu,
              clicking the Waveform button, and selecting the desired waveform file format.

        Usage:
            - Using the ``.query()`` method will send the ``SAVe:WAVEform:FILEFormat?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVe:WAVEform:FILEFormat?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVe:WAVEform:FILEFormat value``
              command.

        SCPI Syntax:
            ```
            - SAVe:WAVEform:FILEFormat {INTERNal|MATHCad|MATLab|SPREADSHEETCsv|SPREADSHEETTxt|TIMEStamp|AUTO}
            - SAVe:WAVEform:FILEFormat?
            ```

        Info:
            - ``INTERNal`` specifies that waveforms are saved in an internal format, using a .wfm
              file name extension. These files can be recalled as reference waveforms. When this
              argument is specified, the settings specified via the ``SAVe:WAVEform:DATa:STARt`` and
              ``SAVe:WAVEform:DATa:STOP`` commands have no meaning as the entire waveform is saved.
            - ``MATHCad`` specifies that waveforms are saved in MathCad format, using a .dat file
              name extension. When saving in this format, waveform values are delimited with new
              lines. MathCad format enables easy import of waveform data into MathCad or MATLAB. For
              FastAcq waveforms, data is imported as a matrix. For these formats, waveform header
              and timing information is saved in a separate header file. MathCad format header files
              use a _hdr.dat extension.
            - ``MATLab`` specifies that waveforms are saved in Matlab format, using a .dat file name
              extension. When saving in this format, waveform values are delimited with new lines.
              MATLAB format enables easy import of waveform data into MathCad or MATLAB. For FastAcq
              waveforms, data is imported as a matrix. For these formats, waveform header and timing
              information is saved in a separate header file. MATLAB format header files use a
              _hdr.dat extension.
            - ``SPREADSHEETCsv`` specifies that waveform data is saved in a format that contains
              comma delimited values. These waveform data files are named using the .csv file name
              extension. Saving waveforms in CSV format enables spreadsheet programs to import the
              data.
            - ``SPREADSHEETTxt`` specifies that waveform data is saved in a format that contains tab
              delimited values. These waveform data files are named using the .txt file name
              extension. Saving waveforms in this format enables spreadsheet programs to import the
              data.
            - ``TIMEStamp`` specifies that timestamp data is saved in a format that contains comma
              delimited values. These data files are named using the .txt file name extension.
              Saving waveforms in this format enables spreadsheet programs to import the data.
            - ``AUTO`` specifies that the file format should be taken from the file name extension.
              Supported extensions include \\*.wfm, \\*.csv, \\*.txt, \\*.h5). If an extension is
              read that is not supported, no file will be written out. If no extension is given in
              the filename, \\*.csv will be written out. Auto format always uses the entire waveform
              record and does not utilize ``SAVe:WAVEform:DATa:STARt`` or STOP or any other
              limitations on output data.
        """  # noqa: E501
        return self._fileformat

    @property
    def forcesamefilesize(self) -> SaveWaveformForcesamefilesize:
        """Return the ``SAVe:WAVEform:FORCESAMEFilesize`` command.

        Description:
            - This command sets or queries the save waveform force same file size.

        Usage:
            - Using the ``.query()`` method will send the ``SAVe:WAVEform:FORCESAMEFilesize?``
              query.
            - Using the ``.verify(value)`` method will send the ``SAVe:WAVEform:FORCESAMEFilesize?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SAVe:WAVEform:FORCESAMEFilesize value`` command.

        SCPI Syntax:
            ```
            - SAVe:WAVEform:FORCESAMEFilesize {ON|OFF|<NR1>}
            - SAVe:WAVEform:FORCESAMEFilesize?
            ```

        Info:
            - ``<NR1>`` = 0 disables the function; any other value enables it.
            - ``OFF`` disables the function.
            - ``ON`` enables the function.
        """
        return self._forcesamefilesize


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


class SaveMarks(SCPICmdWrite):
    """The ``SAVe:MARKS`` command.

    Description:
        - This command saves the user search marks in CSV format, to the file that you specify by
          <string>.

    Usage:
        - Using the ``.write(value)`` method will send the ``SAVe:MARKS value`` command.

    SCPI Syntax:
        ```
        - SAVe:MARKS <string>
        ```
    """


class SaveEventtableBusItem(ValidatedDynamicNumberCmd, SCPICmdWrite):
    """The ``SAVe:EVENTtable:BUS<x>`` command.

    Description:
        - Saves the event table contents of the specified bus in CSV format, to the file that you
          specify by <string>.

    Usage:
        - Using the ``.write(value)`` method will send the ``SAVe:EVENTtable:BUS<x> value`` command.

    SCPI Syntax:
        ```
        - SAVe:EVENTtable:BUS<x> <string>
        ```
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
            - Saves the event table contents of the specified bus in CSV format, to the file that
              you specify by <string>.

        Usage:
            - Using the ``.write(value)`` method will send the ``SAVe:EVENTtable:BUS<x> value``
              command.

        SCPI Syntax:
            ```
            - SAVe:EVENTtable:BUS<x> <string>
            ```
        """
        return self._bus


class Save(SCPICmdRead):
    """The ``SAVe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.eventtable``: The ``SAVe:EVENTtable`` command tree.
        - ``.marks``: The ``SAVe:MARKS`` command.
        - ``.mask``: The ``SAVe:MASK`` command.
        - ``.setup``: The ``SAVe:SETUp`` command.
        - ``.waveform``: The ``SAVe:WAVEform`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SAVe") -> None:
        super().__init__(device, cmd_syntax)
        self._eventtable = SaveEventtable(device, f"{self._cmd_syntax}:EVENTtable")
        self._marks = SaveMarks(device, f"{self._cmd_syntax}:MARKS")
        self._mask = SaveMask(device, f"{self._cmd_syntax}:MASK")
        self._setup = SaveSetup(device, f"{self._cmd_syntax}:SETUp")
        self._waveform = SaveWaveform(device, f"{self._cmd_syntax}:WAVEform")

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
    def marks(self) -> SaveMarks:
        """Return the ``SAVe:MARKS`` command.

        Description:
            - This command saves the user search marks in CSV format, to the file that you specify
              by <string>.

        Usage:
            - Using the ``.write(value)`` method will send the ``SAVe:MARKS value`` command.

        SCPI Syntax:
            ```
            - SAVe:MARKS <string>
            ```
        """
        return self._marks

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
            - This command (no query form) saves a waveform to one of four reference memory
              locations or a file.

        Usage:
            - Using the ``.write(value)`` method will send the ``SAVe:WAVEform value`` command.

        SCPI Syntax:
            ```
            - SAVe:WAVEform [<wfm>,REF<x>]| [<wfm>,<QString>] | [ALL,[QString]]| [DIGITALALL,<QString>]
            ```

        Info:
            - ``<wfm>,REF<x>`` saves the specified waveform to the specified reference memory
              location.
            - ``<wfm>,<QString>`` saves the specified waveform to the file specified.
            - ``ALL,[QString>]`` saves all displayed waveforms, excluding digital waveforms, to
              individual files based on the ``SAVE:WAVEFORM:FILEFORMAT`` setting.
            - ``DIGITALALL,<QString>`` saves all digital waveforms to a single file specified by the
              quoted string argument and based on the ``SAVE:WAVEFORM:FILEFORMAT`` setting.

        Sub-properties:
            - ``.data``: The ``SAVe:WAVEform:DATa`` command tree.
            - ``.fileformat``: The ``SAVe:WAVEform:FILEFormat`` command.
            - ``.forcesamefilesize``: The ``SAVe:WAVEform:FORCESAMEFilesize`` command.
        """  # noqa: E501
        return self._waveform
