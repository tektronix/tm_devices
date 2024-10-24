# pylint: disable=line-too-long
"""The save commands module.

These commands are used in the following models:
TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SAVe:EVENTtable:BUS <QString>
    - SAVe:EVENTtable:CUSTom <QString>
    - SAVe:EVENTtable:CUSTom:COMMents <Qstring>
    - SAVe:EVENTtable:CUSTom:COMMents?
    - SAVe:EVENTtable:CUSTom:DATAFormat [SCIentific|ENGineering]
    - SAVe:EVENTtable:CUSTom:DATAFormat?
    - SAVe:EVENTtable:CUSTom:INCLUDEREFs {1|0}
    - SAVe:EVENTtable:CUSTom:INCLUDEREFs?
    - SAVe:EVENTtable:MEASUrement <QString>
    - SAVe:EVENTtable:PEAKS <QString>
    - SAVe:EVENTtable:SEARCHTable <QString>
    - SAVe:IMAGe <QString>
    - SAVe:IMAGe:COMPosition {NORMal|INVErted}
    - SAVe:IMAGe:COMPosition?
    - SAVe:IMAGe:VIEWTYpe {FULLScreen}
    - SAVe:IMAGe:VIEWTYpe?
    - SAVe:PLOTData <Qstring>
    - SAVe:REPOrt <QString>
    - SAVe:REPOrt:COMMents <QString>
    - SAVe:REPOrt:COMMents?
    - SAVe:SESsion <QString>
    - SAVe:SETUp <QString>
    - SAVe:SETUp:INCLUDEREFs {OFF|ON|0|1}
    - SAVe:SETUp:INCLUDEREFs?
    - SAVe:WAVEform {CH<x>[_DALL|_SV_NORMal|_SV_AVErage|_SV_MAXHold| _SV_MINHold|_MAG_VS_TIME|_FREQ_VS_TIME| _PHASE_VS_TIME]|MATH<x>|REF<x>|ALL| },<QString>
    - SAVe:WAVEform:GATing {NONe|CURSors|SCREEN|RESAMPLE|SELected}
    - SAVe:WAVEform:GATing:RESAMPLErate <NR1>
    - SAVe:WAVEform:GATing:RESAMPLErate?
    - SAVe:WAVEform:GATing?
    - SAVe:WAVEform:SOURCELIst?
    ```
"""  # noqa: E501

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class SaveWaveformSourcelist(SCPICmdRead):
    """The ``SAVe:WAVEform:SOURCELIst`` command.

    Description:
        - This query returns a list of the available waveforms that can be specified as the source
          for the ``SAVe:WAVEform`` command. Source waveforms must have their display mode set to On
          to appear in this list and to be saved.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:WAVEform:SOURCELIst?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe:WAVEform:SOURCELIst?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SAVe:WAVEform:SOURCELIst?
        ```
    """


class SaveWaveformGatingResamplerate(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:WAVEform:GATing:RESAMPLErate`` command.

    Description:
        - This command saves the waveform data at a sample interval. The resulting saved waveform is
          a resampled version of the original waveform with fewer data points.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:WAVEform:GATing:RESAMPLErate?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe:WAVEform:GATing:RESAMPLErate?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SAVe:WAVEform:GATing:RESAMPLErate value`` command.

    SCPI Syntax:
        ```
        - SAVe:WAVEform:GATing:RESAMPLErate <NR1>
        - SAVe:WAVEform:GATing:RESAMPLErate?
        ```

    Info:
        - ``<NR1>`` specifies the resample interval.
    """


class SaveWaveformGating(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:WAVEform:GATing`` command.

    Description:
        - This command specifies the method to save a specified part of the waveform data or the
          entire waveform.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:WAVEform:GATing?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe:WAVEform:GATing?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVe:WAVEform:GATing value`` command.

    SCPI Syntax:
        ```
        - SAVe:WAVEform:GATing {NONe|CURSors|SCREEN|RESAMPLE|SELected}
        - SAVe:WAVEform:GATing?
        ```

    Info:
        - ``NONe`` saves the full waveform data.
        - ``CURSors`` saves the waveform data located between the vertical cursors.
        - ``SCREEN`` saves the waveform data that is on the screen. Nothing outside the waveform
          will be saved.
        - ``RESAMPLE`` saves the waveform data at a sample interval set by the user. The resulting
          saved waveform is a resampled version of the original waveform with fewer data points.
        - ``SELected`` saves the data from the currently selected history or FastFrame acquisition.

    Properties:
        - ``.resamplerate``: The ``SAVe:WAVEform:GATing:RESAMPLErate`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._resamplerate = SaveWaveformGatingResamplerate(
            device, f"{self._cmd_syntax}:RESAMPLErate"
        )

    @property
    def resamplerate(self) -> SaveWaveformGatingResamplerate:
        """Return the ``SAVe:WAVEform:GATing:RESAMPLErate`` command.

        Description:
            - This command saves the waveform data at a sample interval. The resulting saved
              waveform is a resampled version of the original waveform with fewer data points.

        Usage:
            - Using the ``.query()`` method will send the ``SAVe:WAVEform:GATing:RESAMPLErate?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SAVe:WAVEform:GATing:RESAMPLErate?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SAVe:WAVEform:GATing:RESAMPLErate value`` command.

        SCPI Syntax:
            ```
            - SAVe:WAVEform:GATing:RESAMPLErate <NR1>
            - SAVe:WAVEform:GATing:RESAMPLErate?
            ```

        Info:
            - ``<NR1>`` specifies the resample interval.
        """
        return self._resamplerate


class SaveWaveform(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:WAVEform`` command.

    Description:
        - This command saves the specified waveform(s) to the specified destination file.

    Usage:
        - Using the ``.write(value)`` method will send the ``SAVe:WAVEform value`` command.

    SCPI Syntax:
        ```
        - SAVe:WAVEform {CH<x>[_DALL|_SV_NORMal|_SV_AVErage|_SV_MAXHold| _SV_MINHold|_MAG_VS_TIME|_FREQ_VS_TIME| _PHASE_VS_TIME]|MATH<x>|REF<x>|ALL| },<QString>
        ```

    Info:
        - ``<x>`` is the number of the analog channel, math, or reference waveform source used to
          save the waveform data.
        - ``_DALL`` saves the digital channel waveform data of the specified channel.
        - ``_SV_NORMal`` saves the Normal Spectrum view waveform of the specified channel.
        - ``_SV_AVErage`` saves the Average Spectrum view waveform of the specified channel.
        - ``_SV_MAXHold`` saves the Maximum Hold Spectrum view waveform of the specified channel.
        - ``_SV_MINHold`` saves the Minimum Hold Spectrum view waveform of the specified channel.
        - ``_MAG_VS_TIME`` saves the Magnitude vs.
        - ``_FREQ_VS_TIME`` saves the Freuency vs.
        - ``_PHASE_VS_TIME`` saves the Phase vs.
        - ``_SV_BASEBAND_IQ`` saves the baseband I & Q data of the specified channel.
        - ``ALL`` saves all displayed analog, math, and reference waveforms to individual files.
        - ``<Qstring>`` is a quoted string that defines the path and file name to use to save the
          specified file, in the format '[<path>]<filename.
        - ``<path>`` uses the form '<drive>/<dir>.
        - ``<filename>`` sets the file name to use to create the file.
        - ``<.ext>`` sets the file format to which to save the data.

    Properties:
        - ``.gating``: The ``SAVe:WAVEform:GATing`` command.
        - ``.sourcelist``: The ``SAVe:WAVEform:SOURCELIst`` command.
    """  # noqa: E501

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._gating = SaveWaveformGating(device, f"{self._cmd_syntax}:GATing")
        self._sourcelist = SaveWaveformSourcelist(device, f"{self._cmd_syntax}:SOURCELIst")

    @property
    def gating(self) -> SaveWaveformGating:
        """Return the ``SAVe:WAVEform:GATing`` command.

        Description:
            - This command specifies the method to save a specified part of the waveform data or the
              entire waveform.

        Usage:
            - Using the ``.query()`` method will send the ``SAVe:WAVEform:GATing?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVe:WAVEform:GATing?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVe:WAVEform:GATing value``
              command.

        SCPI Syntax:
            ```
            - SAVe:WAVEform:GATing {NONe|CURSors|SCREEN|RESAMPLE|SELected}
            - SAVe:WAVEform:GATing?
            ```

        Info:
            - ``NONe`` saves the full waveform data.
            - ``CURSors`` saves the waveform data located between the vertical cursors.
            - ``SCREEN`` saves the waveform data that is on the screen. Nothing outside the waveform
              will be saved.
            - ``RESAMPLE`` saves the waveform data at a sample interval set by the user. The
              resulting saved waveform is a resampled version of the original waveform with fewer
              data points.
            - ``SELected`` saves the data from the currently selected history or FastFrame
              acquisition.

        Sub-properties:
            - ``.resamplerate``: The ``SAVe:WAVEform:GATing:RESAMPLErate`` command.
        """
        return self._gating

    @property
    def sourcelist(self) -> SaveWaveformSourcelist:
        """Return the ``SAVe:WAVEform:SOURCELIst`` command.

        Description:
            - This query returns a list of the available waveforms that can be specified as the
              source for the ``SAVe:WAVEform`` command. Source waveforms must have their display
              mode set to On to appear in this list and to be saved.

        Usage:
            - Using the ``.query()`` method will send the ``SAVe:WAVEform:SOURCELIst?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVe:WAVEform:SOURCELIst?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SAVe:WAVEform:SOURCELIst?
            ```
        """
        return self._sourcelist


class SaveSetupIncluderefs(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:SETUp:INCLUDEREFs`` command.

    Description:
        - This command sets or queries whether displayed reference waveforms are to be included in
          saved setups.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:SETUp:INCLUDEREFs?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe:SETUp:INCLUDEREFs?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVe:SETUp:INCLUDEREFs value`` command.

    SCPI Syntax:
        ```
        - SAVe:SETUp:INCLUDEREFs {OFF|ON|0|1}
        - SAVe:SETUp:INCLUDEREFs?
        ```

    Info:
        - ``OFF`` specifies not including displayed reference waveforms in saved setups.
        - ``ON`` specifies including displayed reference waveforms in saved setups.
        - ``0`` specifies not including displayed reference waveforms in saved setups.
        - ``1`` specifies including displayed reference waveforms in saved setups.
    """


class SaveSetup(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:SETUp`` command.

    Description:
        - Saves the current instrument state to the specified file.

    Usage:
        - Using the ``.write(value)`` method will send the ``SAVe:SETUp value`` command.

    SCPI Syntax:
        ```
        - SAVe:SETUp <QString>
        ```

    Info:
        - ``<QString>`` is a quoted string that is the complete path specification. If a file name
          or path is specified, the file is expected to be located in a directory relative to the
          current working directory (specified by ``FILESYSTEM:CWD``) unless a complete path is
          specified.

    Properties:
        - ``.includerefs``: The ``SAVe:SETUp:INCLUDEREFs`` command.
    """

    _WRAP_ARG_WITH_QUOTES = True

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._includerefs = SaveSetupIncluderefs(device, f"{self._cmd_syntax}:INCLUDEREFs")

    @property
    def includerefs(self) -> SaveSetupIncluderefs:
        """Return the ``SAVe:SETUp:INCLUDEREFs`` command.

        Description:
            - This command sets or queries whether displayed reference waveforms are to be included
              in saved setups.

        Usage:
            - Using the ``.query()`` method will send the ``SAVe:SETUp:INCLUDEREFs?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVe:SETUp:INCLUDEREFs?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVe:SETUp:INCLUDEREFs value``
              command.

        SCPI Syntax:
            ```
            - SAVe:SETUp:INCLUDEREFs {OFF|ON|0|1}
            - SAVe:SETUp:INCLUDEREFs?
            ```

        Info:
            - ``OFF`` specifies not including displayed reference waveforms in saved setups.
            - ``ON`` specifies including displayed reference waveforms in saved setups.
            - ``0`` specifies not including displayed reference waveforms in saved setups.
            - ``1`` specifies including displayed reference waveforms in saved setups.
        """
        return self._includerefs


class SaveSession(SCPICmdWrite):
    """The ``SAVe:SESsion`` command.

    Description:
        - Saves the state of the instrument, including reference waveforms, to a saved session file.

    Usage:
        - Using the ``.write(value)`` method will send the ``SAVe:SESsion value`` command.

    SCPI Syntax:
        ```
        - SAVe:SESsion <QString>
        ```

    Info:
        - ``<QString>`` is the file path that specifies the location to save the specified
          instrument session file. If a file name or path is specified, the file is expected to be
          located in a directory relative to the current working directory (specified by.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SaveReportComments(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:REPOrt:COMMents`` command.

    Description:
        - This command sets or queries the comments to be included in saved report files.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:REPOrt:COMMents?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe:REPOrt:COMMents?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVe:REPOrt:COMMents value`` command.

    SCPI Syntax:
        ```
        - SAVe:REPOrt:COMMents <QString>
        - SAVe:REPOrt:COMMents?
        ```

    Info:
        - ``<QString>`` is the comments to be included in saved report files.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SaveReport(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:REPOrt`` command.

    Description:
        - This command saves a report to the specified file. Supported report formats are PDF and
          MHT (web page archive file).

    Usage:
        - Using the ``.write(value)`` method will send the ``SAVe:REPOrt value`` command.

    SCPI Syntax:
        ```
        - SAVe:REPOrt <QString>
        ```

    Info:
        - ``<QString>`` is the complete path specification. When specifying the file name with this
          command, use the correct file extension (.pdf for PDF format, or .mht for MHT format).

    Properties:
        - ``.comments``: The ``SAVe:REPOrt:COMMents`` command.
    """

    _WRAP_ARG_WITH_QUOTES = True

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._comments = SaveReportComments(device, f"{self._cmd_syntax}:COMMents")

    @property
    def comments(self) -> SaveReportComments:
        """Return the ``SAVe:REPOrt:COMMents`` command.

        Description:
            - This command sets or queries the comments to be included in saved report files.

        Usage:
            - Using the ``.query()`` method will send the ``SAVe:REPOrt:COMMents?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVe:REPOrt:COMMents?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVe:REPOrt:COMMents value``
              command.

        SCPI Syntax:
            ```
            - SAVe:REPOrt:COMMents <QString>
            - SAVe:REPOrt:COMMents?
            ```

        Info:
            - ``<QString>`` is the comments to be included in saved report files.
        """
        return self._comments


class SavePlotdata(SCPICmdWrite):
    """The ``SAVe:PLOTData`` command.

    Description:
        - Saves the plot data of the currently selected plot to a specified file. Supported file
          format is CSV. When specifying the file name with this command, use the correct file
          extension (.CSV). If a file name or path is specified, the file is expected to be located
          in a directory relative to the current working directory (specified by ``FILESYSTEM:CWD``)
          unless a complete path is specified. If the file argument begins with a drive designator
          (such as C:), then the file name is interpreted as a full path. If the file argument
          begins with '.' or '', or has a file path separator appearing anywhere other than the
          first character position, then the file name is treated as a path that is relative to the
          current working directory. To export an eye diagram plot data to a .csv file, the
          prerequisite command is ``MEASUrement:ADDMEAS TIE``

    Usage:
        - Using the ``.write(value)`` method will send the ``SAVe:PLOTData value`` command.

    SCPI Syntax:
        ```
        - SAVe:PLOTData <Qstring>
        ```

    Info:
        - ``<Qstring>`` sets the file name and location used to store the plot data.
    """


class SaveImageViewtype(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:IMAGe:VIEWTYpe`` command.

    Description:
        - Sets or queries the view type for saved images. Currently only FULLScreen is supported.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:IMAGe:VIEWTYpe?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe:IMAGe:VIEWTYpe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVe:IMAGe:VIEWTYpe value`` command.

    SCPI Syntax:
        ```
        - SAVe:IMAGe:VIEWTYpe {FULLScreen}
        - SAVe:IMAGe:VIEWTYpe?
        ```

    Info:
        - ``FULLScreen`` sets the screen capture mode to capture the full screen.
    """


class SaveImageComposition(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:IMAGe:COMPosition`` command.

    Description:
        - Sets or queries the color mode for saved images (normal or inverted).

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:IMAGe:COMPosition?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe:IMAGe:COMPosition?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVe:IMAGe:COMPosition value`` command.

    SCPI Syntax:
        ```
        - SAVe:IMAGe:COMPosition {NORMal|INVErted}
        - SAVe:IMAGe:COMPosition?
        ```

    Info:
        - ``NORMal`` Sets the saved screen capture to Normal colors.
        - ``INVErted`` sets the saved screen capture to Inverted colors.
    """


class SaveImage(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:IMAGe`` command.

    Description:
        - Saves a capture of the screen contents to the specified image file. Supported image
          formats are PNG, Windows Bitmap, and JPEG.

    Usage:
        - Using the ``.write(value)`` method will send the ``SAVe:IMAGe value`` command.

    SCPI Syntax:
        ```
        - SAVe:IMAGe <QString>
        ```

    Info:
        - ``<QString>`` is the file name and location used to store the image file.

    Properties:
        - ``.composition``: The ``SAVe:IMAGe:COMPosition`` command.
        - ``.viewtype``: The ``SAVe:IMAGe:VIEWTYpe`` command.
    """

    _WRAP_ARG_WITH_QUOTES = True

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._composition = SaveImageComposition(device, f"{self._cmd_syntax}:COMPosition")
        self._viewtype = SaveImageViewtype(device, f"{self._cmd_syntax}:VIEWTYpe")

    @property
    def composition(self) -> SaveImageComposition:
        """Return the ``SAVe:IMAGe:COMPosition`` command.

        Description:
            - Sets or queries the color mode for saved images (normal or inverted).

        Usage:
            - Using the ``.query()`` method will send the ``SAVe:IMAGe:COMPosition?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVe:IMAGe:COMPosition?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVe:IMAGe:COMPosition value``
              command.

        SCPI Syntax:
            ```
            - SAVe:IMAGe:COMPosition {NORMal|INVErted}
            - SAVe:IMAGe:COMPosition?
            ```

        Info:
            - ``NORMal`` Sets the saved screen capture to Normal colors.
            - ``INVErted`` sets the saved screen capture to Inverted colors.
        """
        return self._composition

    @property
    def viewtype(self) -> SaveImageViewtype:
        """Return the ``SAVe:IMAGe:VIEWTYpe`` command.

        Description:
            - Sets or queries the view type for saved images. Currently only FULLScreen is
              supported.

        Usage:
            - Using the ``.query()`` method will send the ``SAVe:IMAGe:VIEWTYpe?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVe:IMAGe:VIEWTYpe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVe:IMAGe:VIEWTYpe value``
              command.

        SCPI Syntax:
            ```
            - SAVe:IMAGe:VIEWTYpe {FULLScreen}
            - SAVe:IMAGe:VIEWTYpe?
            ```

        Info:
            - ``FULLScreen`` sets the screen capture mode to capture the full screen.
        """
        return self._viewtype


class SaveEventtableSearchtable(SCPICmdWrite):
    """The ``SAVe:EVENTtable:SEARCHTable`` command.

    Description:
        - This command saves a search results table to the specified file.

    Usage:
        - Using the ``.write(value)`` method will send the ``SAVe:EVENTtable:SEARCHTable value``
          command.

    SCPI Syntax:
        ```
        - SAVe:EVENTtable:SEARCHTable <QString>
        ```

    Info:
        - ``<QString>`` is the specified file. If a file name or path is specified, the file is
          expected to be located in a directory relative to the current working directory (specified
          by ``FILESYSTEM:CWD``) unless a complete path is specified.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SaveEventtablePeaks(SCPICmdWrite):
    """The ``SAVe:EVENTtable:PEAKS`` command.

    Description:
        - This command saves peak markers results table to the specified file.

    Usage:
        - Using the ``.write(value)`` method will send the ``SAVe:EVENTtable:PEAKS value`` command.

    SCPI Syntax:
        ```
        - SAVe:EVENTtable:PEAKS <QString>
        ```

    Info:
        - ``<QString>`` is the specified file. If a file name or path is specified, the file is
          expected to be located in a directory relative to the current working directory (specified
          by ``FILESYSTEM:CWD``) unless a complete path is specified.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SaveEventtableMeasurement(SCPICmdWrite):
    """The ``SAVe:EVENTtable:MEASUrement`` command.

    Description:
        - This command saves data (measurement) results to the specified file.

    Usage:
        - Using the ``.write(value)`` method will send the ``SAVe:EVENTtable:MEASUrement value``
          command.

    SCPI Syntax:
        ```
        - SAVe:EVENTtable:MEASUrement <QString>
        ```

    Info:
        - ``<QString>`` is the specified file. If a file name or path is specified, the file is
          expected to be located in a directory relative to the current working directory (specified
          by ``FILESYSTEM:CWD``) unless a complete path is specified.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SaveEventtableCustomIncluderefs(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:EVENTtable:CUSTom:INCLUDEREFs`` command.

    Description:
        - This command sets or queries whether to include displayed reference waveforms with saved
          results table files.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:EVENTtable:CUSTom:INCLUDEREFs?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe:EVENTtable:CUSTom:INCLUDEREFs?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SAVe:EVENTtable:CUSTom:INCLUDEREFs value`` command.

    SCPI Syntax:
        ```
        - SAVe:EVENTtable:CUSTom:INCLUDEREFs {1|0}
        - SAVe:EVENTtable:CUSTom:INCLUDEREFs?
        ```

    Info:
        - ``1`` sets the instrument to save all displayed reference waveforms as part of a saved
          results table file.
        - ``0`` sets the instrument to not save all displayed reference waveforms as part of a saved
          results table file.
    """


class SaveEventtableCustomDataformat(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:EVENTtable:CUSTom:DATAFormat`` command.

    Description:
        - This command sets or queries the data format to use for saving results table data.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:EVENTtable:CUSTom:DATAFormat?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe:EVENTtable:CUSTom:DATAFormat?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SAVe:EVENTtable:CUSTom:DATAFormat value`` command.

    SCPI Syntax:
        ```
        - SAVe:EVENTtable:CUSTom:DATAFormat [SCIentific|ENGineering]
        - SAVe:EVENTtable:CUSTom:DATAFormat?
        ```

    Info:
        - ``SCIentific`` sets the instrument to save results tables data in scientific notation (for
          example, 5.0100E-12).
        - ``ENGineering`` sets the instrument to save results tables data in engineering notation
          (for example, 5.0100ps).
    """


class SaveEventtableCustomComments(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:EVENTtable:CUSTom:COMMents`` command.

    Description:
        - This command sets or queries comments to be included in saved results table files.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:EVENTtable:CUSTom:COMMents?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe:EVENTtable:CUSTom:COMMents?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVe:EVENTtable:CUSTom:COMMents value``
          command.

    SCPI Syntax:
        ```
        - SAVe:EVENTtable:CUSTom:COMMents <Qstring>
        - SAVe:EVENTtable:CUSTom:COMMents?
        ```

    Info:
        - ``<Qstring>`` sets the instrument to save the quoted string as a comment in the saved
          results table file.
    """


class SaveEventtableCustom(SCPICmdWrite, SCPICmdRead):
    """The ``SAVe:EVENTtable:CUSTom`` command.

    Description:
        - This command saves the results table to the specified file path and name.

    Usage:
        - Using the ``.write(value)`` method will send the ``SAVe:EVENTtable:CUSTom value`` command.

    SCPI Syntax:
        ```
        - SAVe:EVENTtable:CUSTom <QString>
        ```

    Info:
        - ``<QString>`` is the specified file. If a file name or path is specified, the file is
          expected to be located in a directory relative to the current working directory (specified
          by ``FILESYSTEM:CWD``) unless a complete path is specified.

    Properties:
        - ``.comments``: The ``SAVe:EVENTtable:CUSTom:COMMents`` command.
        - ``.dataformat``: The ``SAVe:EVENTtable:CUSTom:DATAFormat`` command.
        - ``.includerefs``: The ``SAVe:EVENTtable:CUSTom:INCLUDEREFs`` command.
    """

    _WRAP_ARG_WITH_QUOTES = True

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._comments = SaveEventtableCustomComments(device, f"{self._cmd_syntax}:COMMents")
        self._dataformat = SaveEventtableCustomDataformat(device, f"{self._cmd_syntax}:DATAFormat")
        self._includerefs = SaveEventtableCustomIncluderefs(
            device, f"{self._cmd_syntax}:INCLUDEREFs"
        )

    @property
    def comments(self) -> SaveEventtableCustomComments:
        """Return the ``SAVe:EVENTtable:CUSTom:COMMents`` command.

        Description:
            - This command sets or queries comments to be included in saved results table files.

        Usage:
            - Using the ``.query()`` method will send the ``SAVe:EVENTtable:CUSTom:COMMents?``
              query.
            - Using the ``.verify(value)`` method will send the ``SAVe:EVENTtable:CUSTom:COMMents?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SAVe:EVENTtable:CUSTom:COMMents value`` command.

        SCPI Syntax:
            ```
            - SAVe:EVENTtable:CUSTom:COMMents <Qstring>
            - SAVe:EVENTtable:CUSTom:COMMents?
            ```

        Info:
            - ``<Qstring>`` sets the instrument to save the quoted string as a comment in the saved
              results table file.
        """
        return self._comments

    @property
    def dataformat(self) -> SaveEventtableCustomDataformat:
        """Return the ``SAVe:EVENTtable:CUSTom:DATAFormat`` command.

        Description:
            - This command sets or queries the data format to use for saving results table data.

        Usage:
            - Using the ``.query()`` method will send the ``SAVe:EVENTtable:CUSTom:DATAFormat?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SAVe:EVENTtable:CUSTom:DATAFormat?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SAVe:EVENTtable:CUSTom:DATAFormat value`` command.

        SCPI Syntax:
            ```
            - SAVe:EVENTtable:CUSTom:DATAFormat [SCIentific|ENGineering]
            - SAVe:EVENTtable:CUSTom:DATAFormat?
            ```

        Info:
            - ``SCIentific`` sets the instrument to save results tables data in scientific notation
              (for example, 5.0100E-12).
            - ``ENGineering`` sets the instrument to save results tables data in engineering
              notation (for example, 5.0100ps).
        """
        return self._dataformat

    @property
    def includerefs(self) -> SaveEventtableCustomIncluderefs:
        """Return the ``SAVe:EVENTtable:CUSTom:INCLUDEREFs`` command.

        Description:
            - This command sets or queries whether to include displayed reference waveforms with
              saved results table files.

        Usage:
            - Using the ``.query()`` method will send the ``SAVe:EVENTtable:CUSTom:INCLUDEREFs?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SAVe:EVENTtable:CUSTom:INCLUDEREFs?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SAVe:EVENTtable:CUSTom:INCLUDEREFs value`` command.

        SCPI Syntax:
            ```
            - SAVe:EVENTtable:CUSTom:INCLUDEREFs {1|0}
            - SAVe:EVENTtable:CUSTom:INCLUDEREFs?
            ```

        Info:
            - ``1`` sets the instrument to save all displayed reference waveforms as part of a saved
              results table file.
            - ``0`` sets the instrument to not save all displayed reference waveforms as part of a
              saved results table file.
        """
        return self._includerefs


class SaveEventtableBus(SCPICmdWrite):
    """The ``SAVe:EVENTtable:BUS`` command.

    Description:
        - This command saves bus results table to the specified file.

    Usage:
        - Using the ``.write(value)`` method will send the ``SAVe:EVENTtable:BUS value`` command.

    SCPI Syntax:
        ```
        - SAVe:EVENTtable:BUS <QString>
        ```

    Info:
        - ``<QString>`` is the specified file. If a file name or path is specified, the file is
          expected to be located in a directory relative to the current working directory (specified
          by ``FILESYSTEM:CWD``) unless a complete path is specified.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SaveEventtable(SCPICmdRead):
    """The ``SAVe:EVENTtable`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe:EVENTtable?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe:EVENTtable?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bus``: The ``SAVe:EVENTtable:BUS`` command.
        - ``.custom``: The ``SAVe:EVENTtable:CUSTom`` command.
        - ``.measurement``: The ``SAVe:EVENTtable:MEASUrement`` command.
        - ``.peaks``: The ``SAVe:EVENTtable:PEAKS`` command.
        - ``.searchtable``: The ``SAVe:EVENTtable:SEARCHTable`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bus = SaveEventtableBus(device, f"{self._cmd_syntax}:BUS")
        self._custom = SaveEventtableCustom(device, f"{self._cmd_syntax}:CUSTom")
        self._measurement = SaveEventtableMeasurement(device, f"{self._cmd_syntax}:MEASUrement")
        self._peaks = SaveEventtablePeaks(device, f"{self._cmd_syntax}:PEAKS")
        self._searchtable = SaveEventtableSearchtable(device, f"{self._cmd_syntax}:SEARCHTable")

    @property
    def bus(self) -> SaveEventtableBus:
        """Return the ``SAVe:EVENTtable:BUS`` command.

        Description:
            - This command saves bus results table to the specified file.

        Usage:
            - Using the ``.write(value)`` method will send the ``SAVe:EVENTtable:BUS value``
              command.

        SCPI Syntax:
            ```
            - SAVe:EVENTtable:BUS <QString>
            ```

        Info:
            - ``<QString>`` is the specified file. If a file name or path is specified, the file is
              expected to be located in a directory relative to the current working directory
              (specified by ``FILESYSTEM:CWD``) unless a complete path is specified.
        """
        return self._bus

    @property
    def custom(self) -> SaveEventtableCustom:
        """Return the ``SAVe:EVENTtable:CUSTom`` command.

        Description:
            - This command saves the results table to the specified file path and name.

        Usage:
            - Using the ``.write(value)`` method will send the ``SAVe:EVENTtable:CUSTom value``
              command.

        SCPI Syntax:
            ```
            - SAVe:EVENTtable:CUSTom <QString>
            ```

        Info:
            - ``<QString>`` is the specified file. If a file name or path is specified, the file is
              expected to be located in a directory relative to the current working directory
              (specified by ``FILESYSTEM:CWD``) unless a complete path is specified.

        Sub-properties:
            - ``.comments``: The ``SAVe:EVENTtable:CUSTom:COMMents`` command.
            - ``.dataformat``: The ``SAVe:EVENTtable:CUSTom:DATAFormat`` command.
            - ``.includerefs``: The ``SAVe:EVENTtable:CUSTom:INCLUDEREFs`` command.
        """
        return self._custom

    @property
    def measurement(self) -> SaveEventtableMeasurement:
        """Return the ``SAVe:EVENTtable:MEASUrement`` command.

        Description:
            - This command saves data (measurement) results to the specified file.

        Usage:
            - Using the ``.write(value)`` method will send the ``SAVe:EVENTtable:MEASUrement value``
              command.

        SCPI Syntax:
            ```
            - SAVe:EVENTtable:MEASUrement <QString>
            ```

        Info:
            - ``<QString>`` is the specified file. If a file name or path is specified, the file is
              expected to be located in a directory relative to the current working directory
              (specified by ``FILESYSTEM:CWD``) unless a complete path is specified.
        """
        return self._measurement

    @property
    def peaks(self) -> SaveEventtablePeaks:
        """Return the ``SAVe:EVENTtable:PEAKS`` command.

        Description:
            - This command saves peak markers results table to the specified file.

        Usage:
            - Using the ``.write(value)`` method will send the ``SAVe:EVENTtable:PEAKS value``
              command.

        SCPI Syntax:
            ```
            - SAVe:EVENTtable:PEAKS <QString>
            ```

        Info:
            - ``<QString>`` is the specified file. If a file name or path is specified, the file is
              expected to be located in a directory relative to the current working directory
              (specified by ``FILESYSTEM:CWD``) unless a complete path is specified.
        """
        return self._peaks

    @property
    def searchtable(self) -> SaveEventtableSearchtable:
        """Return the ``SAVe:EVENTtable:SEARCHTable`` command.

        Description:
            - This command saves a search results table to the specified file.

        Usage:
            - Using the ``.write(value)`` method will send the ``SAVe:EVENTtable:SEARCHTable value``
              command.

        SCPI Syntax:
            ```
            - SAVe:EVENTtable:SEARCHTable <QString>
            ```

        Info:
            - ``<QString>`` is the specified file. If a file name or path is specified, the file is
              expected to be located in a directory relative to the current working directory
              (specified by ``FILESYSTEM:CWD``) unless a complete path is specified.
        """
        return self._searchtable


class Save(SCPICmdRead):
    """The ``SAVe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SAVe?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.eventtable``: The ``SAVe:EVENTtable`` command tree.
        - ``.image``: The ``SAVe:IMAGe`` command.
        - ``.plotdata``: The ``SAVe:PLOTData`` command.
        - ``.report``: The ``SAVe:REPOrt`` command.
        - ``.session``: The ``SAVe:SESsion`` command.
        - ``.setup``: The ``SAVe:SETUp`` command.
        - ``.waveform``: The ``SAVe:WAVEform`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SAVe") -> None:
        super().__init__(device, cmd_syntax)
        self._eventtable = SaveEventtable(device, f"{self._cmd_syntax}:EVENTtable")
        self._image = SaveImage(device, f"{self._cmd_syntax}:IMAGe")
        self._plotdata = SavePlotdata(device, f"{self._cmd_syntax}:PLOTData")
        self._report = SaveReport(device, f"{self._cmd_syntax}:REPOrt")
        self._session = SaveSession(device, f"{self._cmd_syntax}:SESsion")
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
            - ``.bus``: The ``SAVe:EVENTtable:BUS`` command.
            - ``.custom``: The ``SAVe:EVENTtable:CUSTom`` command.
            - ``.measurement``: The ``SAVe:EVENTtable:MEASUrement`` command.
            - ``.peaks``: The ``SAVe:EVENTtable:PEAKS`` command.
            - ``.searchtable``: The ``SAVe:EVENTtable:SEARCHTable`` command.
        """
        return self._eventtable

    @property
    def image(self) -> SaveImage:
        """Return the ``SAVe:IMAGe`` command.

        Description:
            - Saves a capture of the screen contents to the specified image file. Supported image
              formats are PNG, Windows Bitmap, and JPEG.

        Usage:
            - Using the ``.write(value)`` method will send the ``SAVe:IMAGe value`` command.

        SCPI Syntax:
            ```
            - SAVe:IMAGe <QString>
            ```

        Info:
            - ``<QString>`` is the file name and location used to store the image file.

        Sub-properties:
            - ``.composition``: The ``SAVe:IMAGe:COMPosition`` command.
            - ``.viewtype``: The ``SAVe:IMAGe:VIEWTYpe`` command.
        """
        return self._image

    @property
    def plotdata(self) -> SavePlotdata:
        """Return the ``SAVe:PLOTData`` command.

        Description:
            - Saves the plot data of the currently selected plot to a specified file. Supported file
              format is CSV. When specifying the file name with this command, use the correct file
              extension (.CSV). If a file name or path is specified, the file is expected to be
              located in a directory relative to the current working directory (specified by
              ``FILESYSTEM:CWD``) unless a complete path is specified. If the file argument begins
              with a drive designator (such as C:), then the file name is interpreted as a full
              path. If the file argument begins with '.' or '', or has a file path separator
              appearing anywhere other than the first character position, then the file name is
              treated as a path that is relative to the current working directory. To export an eye
              diagram plot data to a .csv file, the prerequisite command is
              ``MEASUrement:ADDMEAS TIE``

        Usage:
            - Using the ``.write(value)`` method will send the ``SAVe:PLOTData value`` command.

        SCPI Syntax:
            ```
            - SAVe:PLOTData <Qstring>
            ```

        Info:
            - ``<Qstring>`` sets the file name and location used to store the plot data.
        """
        return self._plotdata

    @property
    def report(self) -> SaveReport:
        """Return the ``SAVe:REPOrt`` command.

        Description:
            - This command saves a report to the specified file. Supported report formats are PDF
              and MHT (web page archive file).

        Usage:
            - Using the ``.write(value)`` method will send the ``SAVe:REPOrt value`` command.

        SCPI Syntax:
            ```
            - SAVe:REPOrt <QString>
            ```

        Info:
            - ``<QString>`` is the complete path specification. When specifying the file name with
              this command, use the correct file extension (.pdf for PDF format, or .mht for MHT
              format).

        Sub-properties:
            - ``.comments``: The ``SAVe:REPOrt:COMMents`` command.
        """
        return self._report

    @property
    def session(self) -> SaveSession:
        """Return the ``SAVe:SESsion`` command.

        Description:
            - Saves the state of the instrument, including reference waveforms, to a saved session
              file.

        Usage:
            - Using the ``.write(value)`` method will send the ``SAVe:SESsion value`` command.

        SCPI Syntax:
            ```
            - SAVe:SESsion <QString>
            ```

        Info:
            - ``<QString>`` is the file path that specifies the location to save the specified
              instrument session file. If a file name or path is specified, the file is expected to
              be located in a directory relative to the current working directory (specified by.
        """
        return self._session

    @property
    def setup(self) -> SaveSetup:
        """Return the ``SAVe:SETUp`` command.

        Description:
            - Saves the current instrument state to the specified file.

        Usage:
            - Using the ``.write(value)`` method will send the ``SAVe:SETUp value`` command.

        SCPI Syntax:
            ```
            - SAVe:SETUp <QString>
            ```

        Info:
            - ``<QString>`` is a quoted string that is the complete path specification. If a file
              name or path is specified, the file is expected to be located in a directory relative
              to the current working directory (specified by ``FILESYSTEM:CWD``) unless a complete
              path is specified.

        Sub-properties:
            - ``.includerefs``: The ``SAVe:SETUp:INCLUDEREFs`` command.
        """
        return self._setup

    @property
    def waveform(self) -> SaveWaveform:
        """Return the ``SAVe:WAVEform`` command.

        Description:
            - This command saves the specified waveform(s) to the specified destination file.

        Usage:
            - Using the ``.write(value)`` method will send the ``SAVe:WAVEform value`` command.

        SCPI Syntax:
            ```
            - SAVe:WAVEform {CH<x>[_DALL|_SV_NORMal|_SV_AVErage|_SV_MAXHold| _SV_MINHold|_MAG_VS_TIME|_FREQ_VS_TIME| _PHASE_VS_TIME]|MATH<x>|REF<x>|ALL| },<QString>
            ```

        Info:
            - ``<x>`` is the number of the analog channel, math, or reference waveform source used
              to save the waveform data.
            - ``_DALL`` saves the digital channel waveform data of the specified channel.
            - ``_SV_NORMal`` saves the Normal Spectrum view waveform of the specified channel.
            - ``_SV_AVErage`` saves the Average Spectrum view waveform of the specified channel.
            - ``_SV_MAXHold`` saves the Maximum Hold Spectrum view waveform of the specified
              channel.
            - ``_SV_MINHold`` saves the Minimum Hold Spectrum view waveform of the specified
              channel.
            - ``_MAG_VS_TIME`` saves the Magnitude vs.
            - ``_FREQ_VS_TIME`` saves the Freuency vs.
            - ``_PHASE_VS_TIME`` saves the Phase vs.
            - ``_SV_BASEBAND_IQ`` saves the baseband I & Q data of the specified channel.
            - ``ALL`` saves all displayed analog, math, and reference waveforms to individual files.
            - ``<Qstring>`` is a quoted string that defines the path and file name to use to save
              the specified file, in the format '[<path>]<filename.
            - ``<path>`` uses the form '<drive>/<dir>.
            - ``<filename>`` sets the file name to use to create the file.
            - ``<.ext>`` sets the file format to which to save the data.

        Sub-properties:
            - ``.gating``: The ``SAVe:WAVEform:GATing`` command.
            - ``.sourcelist``: The ``SAVe:WAVEform:SOURCELIst`` command.
        """  # noqa: E501
        return self._waveform
