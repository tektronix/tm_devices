"""The mmemory commands module.

These commands are used in the following models:
AWG70KA, AWG70KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - MMEMory:CATalog? [<msus>]
    - MMEMory:CDIRectory [<directory_name>]
    - MMEMory:CDIRectory?
    - MMEMory:DATA <file_path>[,<start_index>],<block_data>
    - MMEMory:DATA:SIZE? <file_path>
    - MMEMory:DATA? <file_path>[,<start_index>[,<size>]]
    - MMEMory:DELete <file_name>[,<msus>]
    - MMEMory:IMPort <wfm_name>,<filepath>,<type>
    - MMEMory:IMPort:PARameter:NORMalize <Type>
    - MMEMory:IMPort:PARameter:NORMalize?
    - MMEMory:MDIRectory <directory_name>
    - MMEMory:MSIS [<msus>]
    - MMEMory:MSIS?
    - MMEMory:OPEN <filepath>
    - MMEMory:OPEN:PARameter:NORMalize <Type>
    - MMEMory:OPEN:PARameter:NORMalize?
    - MMEMory:OPEN:PARameter:SIQ {0|1|OFF|ON}
    - MMEMory:OPEN:PARameter:SIQ?
    - MMEMory:OPEN:SASSet:SEQuence <filepath>[,<desired_sequence>]
    - MMEMory:OPEN:SASSet:SEQuence:MROPened?
    - MMEMory:OPEN:SASSet:WAVeform <filepath>[,<desired_waveform>]
    - MMEMory:OPEN:SETup <filepath>
    - MMEMory:OPEN:TXT <filepath>,<bitdepth>
    - MMEMory:SAVE:SEQuence <sequence>,<filepath>
    - MMEMory:SAVE:SETup <filepath>[,<with_assets>]
    - MMEMory:SAVE:WAVeform:MAT <wfm_name>,<filepath>
    - MMEMory:SAVE:WAVeform:TIQ <wfm_name>,<filepath>
    - MMEMory:SAVE:WAVeform:TXT <wfm_name>,<filepath>,<bitdepth>[,<IQ Component>]
    - MMEMory:SAVE:WAVeform:WFM <wfm_name>,<filepath>[,<IQ_Component>]
    - MMEMory:SAVE:WAVeform:WFMX <wfm_name>,<filepath>
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdReadWithArguments, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class MmemorySaveWaveformWfmx(SCPICmdWrite):
    """The ``MMEMory:SAVE:WAVeform:WFMX`` command.

    Description:
        - This command exports a waveform given a unique waveform name to an eligible storage
          location from the AWG's waveforms as the .WFMX file type.

    Usage:
        - Using the ``.write(value)`` method will send the ``MMEMory:SAVE:WAVeform:WFMX value``
          command.

    SCPI Syntax:
        ```
        - MMEMory:SAVE:WAVeform:WFMX <wfm_name>,<filepath>
        ```
    """


class MmemorySaveWaveformWfm(SCPICmdWrite):
    """The ``MMEMory:SAVE:WAVeform:WFM`` command.

    Description:
        - This command exports a waveform given a unique waveform name to an eligible storage
          location from the AWG's waveforms as the .WFM file type. The .WFM file type is compatible
          with the AWG 400/500/600/700/5000/7000 instruments.

    Usage:
        - Using the ``.write(value)`` method will send the ``MMEMory:SAVE:WAVeform:WFM value``
          command.

    SCPI Syntax:
        ```
        - MMEMory:SAVE:WAVeform:WFM <wfm_name>,<filepath>[,<IQ_Component>]
        ```
    """


class MmemorySaveWaveformTxt(SCPICmdWrite):
    """The ``MMEMory:SAVE:WAVeform:TXT`` command.

    Description:
        - This command exports a waveform given a unique waveform name to an eligible storage
          location from the AWG's waveforms as a text file as the .TXT file type.

    Usage:
        - Using the ``.write(value)`` method will send the ``MMEMory:SAVE:WAVeform:TXT value``
          command.

    SCPI Syntax:
        ```
        - MMEMory:SAVE:WAVeform:TXT <wfm_name>,<filepath>,<bitdepth>[,<IQ Component>]
        ```
    """


class MmemorySaveWaveformTiq(SCPICmdWrite):
    """The ``MMEMory:SAVE:WAVeform:TIQ`` command.

    Description:
        - This command exports an IQ waveform given a unique waveform name to an eligible storage
          location from the arbitrary waveform generator's assets as the .TIQ file type.

    Usage:
        - Using the ``.write(value)`` method will send the ``MMEMory:SAVE:WAVeform:TIQ value``
          command.

    SCPI Syntax:
        ```
        - MMEMory:SAVE:WAVeform:TIQ <wfm_name>,<filepath>
        ```
    """


class MmemorySaveWaveformMat(SCPICmdWrite):
    """The ``MMEMory:SAVE:WAVeform:MAT`` command.

    Description:
        - This command exports a waveform given a unique waveform name to an eligible storage
          location from the AWG's waveforms with the AWG Specific MATLAB file format (MAT 5).

    Usage:
        - Using the ``.write(value)`` method will send the ``MMEMory:SAVE:WAVeform:MAT value``
          command.

    SCPI Syntax:
        ```
        - MMEMory:SAVE:WAVeform:MAT <wfm_name>,<filepath>
        ```
    """


class MmemorySaveWaveform(SCPICmdRead):
    """The ``MMEMory:SAVE:WAVeform`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:SAVE:WAVeform?`` query.
        - Using the ``.verify(value)`` method will send the ``MMEMory:SAVE:WAVeform?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.mat``: The ``MMEMory:SAVE:WAVeform:MAT`` command.
        - ``.tiq``: The ``MMEMory:SAVE:WAVeform:TIQ`` command.
        - ``.txt``: The ``MMEMory:SAVE:WAVeform:TXT`` command.
        - ``.wfm``: The ``MMEMory:SAVE:WAVeform:WFM`` command.
        - ``.wfmx``: The ``MMEMory:SAVE:WAVeform:WFMX`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mat = MmemorySaveWaveformMat(device, f"{self._cmd_syntax}:MAT")
        self._tiq = MmemorySaveWaveformTiq(device, f"{self._cmd_syntax}:TIQ")
        self._txt = MmemorySaveWaveformTxt(device, f"{self._cmd_syntax}:TXT")
        self._wfm = MmemorySaveWaveformWfm(device, f"{self._cmd_syntax}:WFM")
        self._wfmx = MmemorySaveWaveformWfmx(device, f"{self._cmd_syntax}:WFMX")

    @property
    def mat(self) -> MmemorySaveWaveformMat:
        """Return the ``MMEMory:SAVE:WAVeform:MAT`` command.

        Description:
            - This command exports a waveform given a unique waveform name to an eligible storage
              location from the AWG's waveforms with the AWG Specific MATLAB file format (MAT 5).

        Usage:
            - Using the ``.write(value)`` method will send the ``MMEMory:SAVE:WAVeform:MAT value``
              command.

        SCPI Syntax:
            ```
            - MMEMory:SAVE:WAVeform:MAT <wfm_name>,<filepath>
            ```
        """
        return self._mat

    @property
    def tiq(self) -> MmemorySaveWaveformTiq:
        """Return the ``MMEMory:SAVE:WAVeform:TIQ`` command.

        Description:
            - This command exports an IQ waveform given a unique waveform name to an eligible
              storage location from the arbitrary waveform generator's assets as the .TIQ file type.

        Usage:
            - Using the ``.write(value)`` method will send the ``MMEMory:SAVE:WAVeform:TIQ value``
              command.

        SCPI Syntax:
            ```
            - MMEMory:SAVE:WAVeform:TIQ <wfm_name>,<filepath>
            ```
        """
        return self._tiq

    @property
    def txt(self) -> MmemorySaveWaveformTxt:
        """Return the ``MMEMory:SAVE:WAVeform:TXT`` command.

        Description:
            - This command exports a waveform given a unique waveform name to an eligible storage
              location from the AWG's waveforms as a text file as the .TXT file type.

        Usage:
            - Using the ``.write(value)`` method will send the ``MMEMory:SAVE:WAVeform:TXT value``
              command.

        SCPI Syntax:
            ```
            - MMEMory:SAVE:WAVeform:TXT <wfm_name>,<filepath>,<bitdepth>[,<IQ Component>]
            ```
        """
        return self._txt

    @property
    def wfm(self) -> MmemorySaveWaveformWfm:
        """Return the ``MMEMory:SAVE:WAVeform:WFM`` command.

        Description:
            - This command exports a waveform given a unique waveform name to an eligible storage
              location from the AWG's waveforms as the .WFM file type. The .WFM file type is
              compatible with the AWG 400/500/600/700/5000/7000 instruments.

        Usage:
            - Using the ``.write(value)`` method will send the ``MMEMory:SAVE:WAVeform:WFM value``
              command.

        SCPI Syntax:
            ```
            - MMEMory:SAVE:WAVeform:WFM <wfm_name>,<filepath>[,<IQ_Component>]
            ```
        """
        return self._wfm

    @property
    def wfmx(self) -> MmemorySaveWaveformWfmx:
        """Return the ``MMEMory:SAVE:WAVeform:WFMX`` command.

        Description:
            - This command exports a waveform given a unique waveform name to an eligible storage
              location from the AWG's waveforms as the .WFMX file type.

        Usage:
            - Using the ``.write(value)`` method will send the ``MMEMory:SAVE:WAVeform:WFMX value``
              command.

        SCPI Syntax:
            ```
            - MMEMory:SAVE:WAVeform:WFMX <wfm_name>,<filepath>
            ```
        """
        return self._wfmx


class MmemorySaveSetup(SCPICmdWrite):
    """The ``MMEMory:SAVE:SETup`` command.

    Description:
        - This command saves the AWG's setup and optionally includes the assets (waveforms and
          sequences). This command supports the native setup file format (.AWGX).

    Usage:
        - Using the ``.write(value)`` method will send the ``MMEMory:SAVE:SETup value`` command.

    SCPI Syntax:
        ```
        - MMEMory:SAVE:SETup <filepath>[,<with_assets>]
        ```
    """


class MmemorySaveSequence(SCPICmdWrite):
    """The ``MMEMory:SAVE:SEQuence`` command.

    Description:
        - This command exports a sequence given a unique name to an eligible storage location as the
          .SEQX file type.

    Usage:
        - Using the ``.write(value)`` method will send the ``MMEMory:SAVE:SEQuence value`` command.

    SCPI Syntax:
        ```
        - MMEMory:SAVE:SEQuence <sequence>,<filepath>
        ```
    """


class MmemorySave(SCPICmdRead):
    """The ``MMEMory:SAVE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:SAVE?`` query.
        - Using the ``.verify(value)`` method will send the ``MMEMory:SAVE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.sequence``: The ``MMEMory:SAVE:SEQuence`` command.
        - ``.setup``: The ``MMEMory:SAVE:SETup`` command.
        - ``.waveform``: The ``MMEMory:SAVE:WAVeform`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._sequence = MmemorySaveSequence(device, f"{self._cmd_syntax}:SEQuence")
        self._setup = MmemorySaveSetup(device, f"{self._cmd_syntax}:SETup")
        self._waveform = MmemorySaveWaveform(device, f"{self._cmd_syntax}:WAVeform")

    @property
    def sequence(self) -> MmemorySaveSequence:
        """Return the ``MMEMory:SAVE:SEQuence`` command.

        Description:
            - This command exports a sequence given a unique name to an eligible storage location as
              the .SEQX file type.

        Usage:
            - Using the ``.write(value)`` method will send the ``MMEMory:SAVE:SEQuence value``
              command.

        SCPI Syntax:
            ```
            - MMEMory:SAVE:SEQuence <sequence>,<filepath>
            ```
        """
        return self._sequence

    @property
    def setup(self) -> MmemorySaveSetup:
        """Return the ``MMEMory:SAVE:SETup`` command.

        Description:
            - This command saves the AWG's setup and optionally includes the assets (waveforms and
              sequences). This command supports the native setup file format (.AWGX).

        Usage:
            - Using the ``.write(value)`` method will send the ``MMEMory:SAVE:SETup value`` command.

        SCPI Syntax:
            ```
            - MMEMory:SAVE:SETup <filepath>[,<with_assets>]
            ```
        """
        return self._setup

    @property
    def waveform(self) -> MmemorySaveWaveform:
        """Return the ``MMEMory:SAVE:WAVeform`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MMEMory:SAVE:WAVeform?`` query.
            - Using the ``.verify(value)`` method will send the ``MMEMory:SAVE:WAVeform?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.mat``: The ``MMEMory:SAVE:WAVeform:MAT`` command.
            - ``.tiq``: The ``MMEMory:SAVE:WAVeform:TIQ`` command.
            - ``.txt``: The ``MMEMory:SAVE:WAVeform:TXT`` command.
            - ``.wfm``: The ``MMEMory:SAVE:WAVeform:WFM`` command.
            - ``.wfmx``: The ``MMEMory:SAVE:WAVeform:WFMX`` command.
        """
        return self._waveform


class MmemoryOpenTxt(SCPICmdWrite):
    """The ``MMEMory:OPEN:TXT`` command.

    Description:
        - This command loads a waveform from a .TXT file into the AWG's waveform list.

    Usage:
        - Using the ``.write(value)`` method will send the ``MMEMory:OPEN:TXT value`` command.

    SCPI Syntax:
        ```
        - MMEMory:OPEN:TXT <filepath>,<bitdepth>
        ```
    """


class MmemoryOpenSetup(SCPICmdWrite):
    """The ``MMEMory:OPEN:SETup`` command.

    Description:
        - This command restores a setup file designated by the <filepath>. The supported file format
          is the native setup format (.AWGX).

    Usage:
        - Using the ``.write(value)`` method will send the ``MMEMory:OPEN:SETup value`` command.

    SCPI Syntax:
        ```
        - MMEMory:OPEN:SETup <filepath>
        ```
    """


class MmemoryOpenSassetWaveform(SCPICmdWrite):
    """The ``MMEMory:OPEN:SASSet:WAVeform`` command.

    Description:
        - This command loads a single waveform if ``<desired_waveform>`` is designated. Otherwise
          the command imports all waveforms within the designated file in <filepath>. File formats
          supported: .AWG - AWG5000, AWG7000 Series waveforms.AWGX - AWG70000 Series waveforms.MAT -
          MATLAB files.SEQX - AWG70000 Series sequences

    Usage:
        - Using the ``.write(value)`` method will send the ``MMEMory:OPEN:SASSet:WAVeform value``
          command.

    SCPI Syntax:
        ```
        - MMEMory:OPEN:SASSet:WAVeform <filepath>[,<desired_waveform>]
        ```
    """


class MmemoryOpenSassetSequenceMropened(SCPICmdRead):
    """The ``MMEMory:OPEN:SASSet:SEQuence:MROPened`` command.

    Description:
        - This command returns which sequence was most recently added or replaced from the most
          recently opened or imported sequence file.

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:OPEN:SASSet:SEQuence:MROPened?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MMEMory:OPEN:SASSet:SEQuence:MROPened?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MMEMory:OPEN:SASSet:SEQuence:MROPened?
        ```
    """


class MmemoryOpenSassetSequence(SCPICmdWrite, SCPICmdRead):
    """The ``MMEMory:OPEN:SASSet:SEQuence`` command.

    Description:
        - This command loads all sequences, or a single sequence if ``<desired_sequence>`` is
          designated, into the Sequences list and all associated (used) sequences and waveforms
          within the designated file in <filepath>. File formats supported: .AWG - AWG7000 Series
          setup.AWGX - AWG70000 Series setup.SEQ - AWG400, AWG500, AWG600 Series sequence.SEQX -
          AWG70000 Series sequence

    Usage:
        - Using the ``.write(value)`` method will send the ``MMEMory:OPEN:SASSet:SEQuence value``
          command.

    SCPI Syntax:
        ```
        - MMEMory:OPEN:SASSet:SEQuence <filepath>[,<desired_sequence>]
        ```

    Properties:
        - ``.mropened``: The ``MMEMory:OPEN:SASSet:SEQuence:MROPened`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mropened = MmemoryOpenSassetSequenceMropened(device, f"{self._cmd_syntax}:MROPened")

    @property
    def mropened(self) -> MmemoryOpenSassetSequenceMropened:
        """Return the ``MMEMory:OPEN:SASSet:SEQuence:MROPened`` command.

        Description:
            - This command returns which sequence was most recently added or replaced from the most
              recently opened or imported sequence file.

        Usage:
            - Using the ``.query()`` method will send the ``MMEMory:OPEN:SASSet:SEQuence:MROPened?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MMEMory:OPEN:SASSet:SEQuence:MROPened?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MMEMory:OPEN:SASSet:SEQuence:MROPened?
            ```
        """
        return self._mropened


class MmemoryOpenSasset(SCPICmdRead):
    """The ``MMEMory:OPEN:SASSet`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:OPEN:SASSet?`` query.
        - Using the ``.verify(value)`` method will send the ``MMEMory:OPEN:SASSet?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.sequence``: The ``MMEMory:OPEN:SASSet:SEQuence`` command.
        - ``.waveform``: The ``MMEMory:OPEN:SASSet:WAVeform`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._sequence = MmemoryOpenSassetSequence(device, f"{self._cmd_syntax}:SEQuence")
        self._waveform = MmemoryOpenSassetWaveform(device, f"{self._cmd_syntax}:WAVeform")

    @property
    def sequence(self) -> MmemoryOpenSassetSequence:
        """Return the ``MMEMory:OPEN:SASSet:SEQuence`` command.

        Description:
            - This command loads all sequences, or a single sequence if ``<desired_sequence>`` is
              designated, into the Sequences list and all associated (used) sequences and waveforms
              within the designated file in <filepath>. File formats supported: .AWG - AWG7000
              Series setup.AWGX - AWG70000 Series setup.SEQ - AWG400, AWG500, AWG600 Series
              sequence.SEQX - AWG70000 Series sequence

        Usage:
            - Using the ``.write(value)`` method will send the
              ``MMEMory:OPEN:SASSet:SEQuence value`` command.

        SCPI Syntax:
            ```
            - MMEMory:OPEN:SASSet:SEQuence <filepath>[,<desired_sequence>]
            ```

        Sub-properties:
            - ``.mropened``: The ``MMEMory:OPEN:SASSet:SEQuence:MROPened`` command.
        """
        return self._sequence

    @property
    def waveform(self) -> MmemoryOpenSassetWaveform:
        """Return the ``MMEMory:OPEN:SASSet:WAVeform`` command.

        Description:
            - This command loads a single waveform if ``<desired_waveform>`` is designated.
              Otherwise the command imports all waveforms within the designated file in <filepath>.
              File formats supported: .AWG - AWG5000, AWG7000 Series waveforms.AWGX - AWG70000
              Series waveforms.MAT - MATLAB files.SEQX - AWG70000 Series sequences

        Usage:
            - Using the ``.write(value)`` method will send the
              ``MMEMory:OPEN:SASSet:WAVeform value`` command.

        SCPI Syntax:
            ```
            - MMEMory:OPEN:SASSet:WAVeform <filepath>[,<desired_waveform>]
            ```
        """
        return self._waveform


class MmemoryOpenParameterSiq(SCPICmdWrite, SCPICmdRead):
    """The ``MMEMory:OPEN:PARameter:SIQ`` command.

    Description:
        - This command sets or returns if the IQ waveform (from supported formats) is separated into
          two separate _I and _Q waveforms while importing. File formats supported: .TMP - Midas
          BLUE waveform.PRM - Midas BLUE waveform.IQT - Tektronix RSA IQ Pair.TIQ - IQ Pair.MAT -
          .Matlab files from Tektronix RSA instruments

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:OPEN:PARameter:SIQ?`` query.
        - Using the ``.verify(value)`` method will send the ``MMEMory:OPEN:PARameter:SIQ?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MMEMory:OPEN:PARameter:SIQ value``
          command.

    SCPI Syntax:
        ```
        - MMEMory:OPEN:PARameter:SIQ {0|1|OFF|ON}
        - MMEMory:OPEN:PARameter:SIQ?
        ```
    """


class MmemoryOpenParameterNormalize(SCPICmdWrite, SCPICmdRead):
    """The ``MMEMory:OPEN:PARameter:NORMalize`` command.

    Description:
        - This command sets or queries if the imported data is normalized during select file format
          import operations. The imported waveform data (for select file formats) is normalized
          based on the option set in this command. File formats supported: .WFM -
          AWG400/AWG500/AWG600/AWG700 Series waveform.AWG - AWG5000, AWG7000 Series waveform.TXT -
          Analog text files from AWG.RFD - RFXpress AWG Series waveforms.MAT - Matlab files

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:OPEN:PARameter:NORMalize?`` query.
        - Using the ``.verify(value)`` method will send the ``MMEMory:OPEN:PARameter:NORMalize?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MMEMory:OPEN:PARameter:NORMalize value`` command.

    SCPI Syntax:
        ```
        - MMEMory:OPEN:PARameter:NORMalize <Type>
        - MMEMory:OPEN:PARameter:NORMalize?
        ```

    Info:
        - ``NONE`` will not normalize the imported data. The data may contain points outside of the
          AWG's amplitude range.FSCale normalizes the imported data to the full amplitude
          range.ZREFerence normalizes the imported data while preserving the offset.
        - ``*RST`` sets the arguments to NONE.
    """


class MmemoryOpenParameter(SCPICmdRead):
    """The ``MMEMory:OPEN:PARameter`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:OPEN:PARameter?`` query.
        - Using the ``.verify(value)`` method will send the ``MMEMory:OPEN:PARameter?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.normalize``: The ``MMEMory:OPEN:PARameter:NORMalize`` command.
        - ``.siq``: The ``MMEMory:OPEN:PARameter:SIQ`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._normalize = MmemoryOpenParameterNormalize(device, f"{self._cmd_syntax}:NORMalize")
        self._siq = MmemoryOpenParameterSiq(device, f"{self._cmd_syntax}:SIQ")

    @property
    def normalize(self) -> MmemoryOpenParameterNormalize:
        """Return the ``MMEMory:OPEN:PARameter:NORMalize`` command.

        Description:
            - This command sets or queries if the imported data is normalized during select file
              format import operations. The imported waveform data (for select file formats) is
              normalized based on the option set in this command. File formats supported: .WFM -
              AWG400/AWG500/AWG600/AWG700 Series waveform.AWG - AWG5000, AWG7000 Series waveform.TXT
              - Analog text files from AWG.RFD - RFXpress AWG Series waveforms.MAT - Matlab files

        Usage:
            - Using the ``.query()`` method will send the ``MMEMory:OPEN:PARameter:NORMalize?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MMEMory:OPEN:PARameter:NORMalize?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MMEMory:OPEN:PARameter:NORMalize value`` command.

        SCPI Syntax:
            ```
            - MMEMory:OPEN:PARameter:NORMalize <Type>
            - MMEMory:OPEN:PARameter:NORMalize?
            ```

        Info:
            - ``NONE`` will not normalize the imported data. The data may contain points outside of
              the AWG's amplitude range.FSCale normalizes the imported data to the full amplitude
              range.ZREFerence normalizes the imported data while preserving the offset.
            - ``*RST`` sets the arguments to NONE.
        """
        return self._normalize

    @property
    def siq(self) -> MmemoryOpenParameterSiq:
        """Return the ``MMEMory:OPEN:PARameter:SIQ`` command.

        Description:
            - This command sets or returns if the IQ waveform (from supported formats) is separated
              into two separate _I and _Q waveforms while importing. File formats supported: .TMP -
              Midas BLUE waveform.PRM - Midas BLUE waveform.IQT - Tektronix RSA IQ Pair.TIQ - IQ
              Pair.MAT - .Matlab files from Tektronix RSA instruments

        Usage:
            - Using the ``.query()`` method will send the ``MMEMory:OPEN:PARameter:SIQ?`` query.
            - Using the ``.verify(value)`` method will send the ``MMEMory:OPEN:PARameter:SIQ?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MMEMory:OPEN:PARameter:SIQ value``
              command.

        SCPI Syntax:
            ```
            - MMEMory:OPEN:PARameter:SIQ {0|1|OFF|ON}
            - MMEMory:OPEN:PARameter:SIQ?
            ```
        """
        return self._siq


class MmemoryOpen(SCPICmdWrite, SCPICmdRead):
    """The ``MMEMory:OPEN`` command.

    Description:
        - This command loads a file into the AWG waveform list. File formats supported: .WFMX -
          AWG70000 Series waveform file format.ISF - TDS3000 and DPO4000 waveform file format.TDS -
          TDS5000/TDS6000/TDS7000, DPO7000/DPO70000/DSA70000 Series waveform file format.WFM -
          AWG400/AWG500/AWG600/AWG700/AWG5000/AWG7000 Series waveform file format.PAT -
          AWG400/AWG500/AWG600/AWG700 Series pattern file.TFW - AFG3000 Series waveform file
          format.IQT - RSA3000 Series waveform file format.TIQ - RFXpress waveform file format.TIQ -
          RSA6000 Series waveform file format.WFM - MDO waveform file format.SEQX - AWG70000 Series
          sequence file format.SEQ - AWG400/AWG500/AWG600 sequence format.TMP - Midas BLUE file
          format.PRM - Midas BLUE file format

    Usage:
        - Using the ``.write(value)`` method will send the ``MMEMory:OPEN value`` command.

    SCPI Syntax:
        ```
        - MMEMory:OPEN <filepath>
        ```

    Properties:
        - ``.sasset``: The ``MMEMory:OPEN:SASSet`` command tree.
        - ``.setup``: The ``MMEMory:OPEN:SETup`` command.
        - ``.txt``: The ``MMEMory:OPEN:TXT`` command.
        - ``.parameter``: The ``MMEMory:OPEN:PARameter`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._sasset = MmemoryOpenSasset(device, f"{self._cmd_syntax}:SASSet")
        self._setup = MmemoryOpenSetup(device, f"{self._cmd_syntax}:SETup")
        self._txt = MmemoryOpenTxt(device, f"{self._cmd_syntax}:TXT")
        self._parameter = MmemoryOpenParameter(device, f"{self._cmd_syntax}:PARameter")

    @property
    def sasset(self) -> MmemoryOpenSasset:
        """Return the ``MMEMory:OPEN:SASSet`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MMEMory:OPEN:SASSet?`` query.
            - Using the ``.verify(value)`` method will send the ``MMEMory:OPEN:SASSet?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.sequence``: The ``MMEMory:OPEN:SASSet:SEQuence`` command.
            - ``.waveform``: The ``MMEMory:OPEN:SASSet:WAVeform`` command.
        """
        return self._sasset

    @property
    def setup(self) -> MmemoryOpenSetup:
        """Return the ``MMEMory:OPEN:SETup`` command.

        Description:
            - This command restores a setup file designated by the <filepath>. The supported file
              format is the native setup format (.AWGX).

        Usage:
            - Using the ``.write(value)`` method will send the ``MMEMory:OPEN:SETup value`` command.

        SCPI Syntax:
            ```
            - MMEMory:OPEN:SETup <filepath>
            ```
        """
        return self._setup

    @property
    def txt(self) -> MmemoryOpenTxt:
        """Return the ``MMEMory:OPEN:TXT`` command.

        Description:
            - This command loads a waveform from a .TXT file into the AWG's waveform list.

        Usage:
            - Using the ``.write(value)`` method will send the ``MMEMory:OPEN:TXT value`` command.

        SCPI Syntax:
            ```
            - MMEMory:OPEN:TXT <filepath>,<bitdepth>
            ```
        """
        return self._txt

    @property
    def parameter(self) -> MmemoryOpenParameter:
        """Return the ``MMEMory:OPEN:PARameter`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MMEMory:OPEN:PARameter?`` query.
            - Using the ``.verify(value)`` method will send the ``MMEMory:OPEN:PARameter?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.normalize``: The ``MMEMory:OPEN:PARameter:NORMalize`` command.
            - ``.siq``: The ``MMEMory:OPEN:PARameter:SIQ`` command.
        """
        return self._parameter


class MmemoryMsis(SCPICmdWrite, SCPICmdRead):
    """The ``MMEMory:MSIS`` command.

    Description:
        - This command selects or returns a mass storage device used by all MMEMory commands. <msus>
          specifies a drive using a drive letter. The drive letter can represent hard disk drives,
          network drives, external DVD/CD-RW drives, or USB memory.

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:MSIS?`` query.
        - Using the ``.verify(value)`` method will send the ``MMEMory:MSIS?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MMEMory:MSIS value`` command.

    SCPI Syntax:
        ```
        - MMEMory:MSIS [<msus>]
        - MMEMory:MSIS?
        ```
    """


class MmemoryMdirectory(SCPICmdWrite):
    """The ``MMEMory:MDIRectory`` command.

    Description:
        - This command creates a directory in the mass storage system. If the specified directory is
          locked in the mass storage system, this command causes an error.

    Usage:
        - Using the ``.write(value)`` method will send the ``MMEMory:MDIRectory value`` command.

    SCPI Syntax:
        ```
        - MMEMory:MDIRectory <directory_name>
        ```
    """


class MmemoryImportParameterNormalize(SCPICmdWrite, SCPICmdRead):
    """The ``MMEMory:IMPort:PARameter:NORMalize`` command.

    Description:
        - This command sets or queries if the imported data is normalized during select file format
          import operations. The imported waveform data (for select file formats) is normalized
          based on the option set in this command. File Formats supported: .WFM -
          AWG400/AWG500/AWG600/AWG700 Series waveform.AWG - AWG5000,AWG7000 Series waveforms.TXT -
          Analog text files from AWG.RFD - RFXpress AWG Series waveforms

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:IMPort:PARameter:NORMalize?`` query.
        - Using the ``.verify(value)`` method will send the ``MMEMory:IMPort:PARameter:NORMalize?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MMEMory:IMPort:PARameter:NORMalize value`` command.

    SCPI Syntax:
        ```
        - MMEMory:IMPort:PARameter:NORMalize <Type>
        - MMEMory:IMPort:PARameter:NORMalize?
        ```

    Info:
        - ``NONE`` will not normalize the imported data. The data may contain points outside of the
          AWG's amplitude range.FSCale normalizes the imported data to the full amplitude
          range.ZREFerence normalizes the imported data while preserving the offset.
    """


class MmemoryImportParameter(SCPICmdRead):
    """The ``MMEMory:IMPort:PARameter`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:IMPort:PARameter?`` query.
        - Using the ``.verify(value)`` method will send the ``MMEMory:IMPort:PARameter?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.normalize``: The ``MMEMory:IMPort:PARameter:NORMalize`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._normalize = MmemoryImportParameterNormalize(device, f"{self._cmd_syntax}:NORMalize")

    @property
    def normalize(self) -> MmemoryImportParameterNormalize:
        """Return the ``MMEMory:IMPort:PARameter:NORMalize`` command.

        Description:
            - This command sets or queries if the imported data is normalized during select file
              format import operations. The imported waveform data (for select file formats) is
              normalized based on the option set in this command. File Formats supported: .WFM -
              AWG400/AWG500/AWG600/AWG700 Series waveform.AWG - AWG5000,AWG7000 Series waveforms.TXT
              - Analog text files from AWG.RFD - RFXpress AWG Series waveforms

        Usage:
            - Using the ``.query()`` method will send the ``MMEMory:IMPort:PARameter:NORMalize?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MMEMory:IMPort:PARameter:NORMalize?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MMEMory:IMPort:PARameter:NORMalize value`` command.

        SCPI Syntax:
            ```
            - MMEMory:IMPort:PARameter:NORMalize <Type>
            - MMEMory:IMPort:PARameter:NORMalize?
            ```

        Info:
            - ``NONE`` will not normalize the imported data. The data may contain points outside of
              the AWG's amplitude range.FSCale normalizes the imported data to the full amplitude
              range.ZREFerence normalizes the imported data while preserving the offset.
        """
        return self._normalize


class MmemoryImport(SCPICmdWrite, SCPICmdRead):
    """The ``MMEMory:IMPort`` command.

    Description:
        - This command imports a file into the AWG's waveform list. File formats supported: ISF -
          TDS3000 and DPO4000 waveform formatTDS - TDS5000/TDS6000/TDS7000,
          DPO7000/DPO70000/DSA70000 Series waveformTXT - Text file with analog dataTXT8 - Text file
          with 8 bit DAC resolutionTXT9 - Text file with 9 bit DAC resolutionTXT10 - Text file with
          10 bit DAC resolutionTXT14 - Text file with 14 bit DAC resolutionWFM -
          AWG400/AWG500/AWG600/AWG700 Series waveformPAT - AWG400/AWG500/AWG600/AWG700 Series
          pattern fileTFW - AFG3000 Series waveform file formatIQT - RSA3000 Series waveform file
          formatTIQ - RSA6000 Series waveform file format

    Usage:
        - Using the ``.write(value)`` method will send the ``MMEMory:IMPort value`` command.

    SCPI Syntax:
        ```
        - MMEMory:IMPort <wfm_name>,<filepath>,<type>
        ```

    Properties:
        - ``.parameter``: The ``MMEMory:IMPort:PARameter`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._parameter = MmemoryImportParameter(device, f"{self._cmd_syntax}:PARameter")

    @property
    def parameter(self) -> MmemoryImportParameter:
        """Return the ``MMEMory:IMPort:PARameter`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MMEMory:IMPort:PARameter?`` query.
            - Using the ``.verify(value)`` method will send the ``MMEMory:IMPort:PARameter?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.normalize``: The ``MMEMory:IMPort:PARameter:NORMalize`` command.
        """
        return self._parameter


class MmemoryDelete(SCPICmdWrite):
    """The ``MMEMory:DELete`` command.

    Description:
        - This command deletes a file or directory from the AWG's hard disk. When used on a
          directory, this command succeeds only if the directory is empty.

    Usage:
        - Using the ``.write(value)`` method will send the ``MMEMory:DELete value`` command.

    SCPI Syntax:
        ```
        - MMEMory:DELete <file_name>[,<msus>]
        ```
    """


class MmemoryDataSize(SCPICmdReadWithArguments):
    """The ``MMEMory:DATA:SIZE`` command.

    Description:
        - This command returns the size in bytes of a selected file.

    Usage:
        - Using the ``.query(argument)`` method will send the ``MMEMory:DATA:SIZE? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``MMEMory:DATA:SIZE? argument`` query and raise an AssertionError if the returned value
          does not match ``value``.

    SCPI Syntax:
        ```
        - MMEMory:DATA:SIZE? <file_path>
        ```
    """


class MmemoryData(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``MMEMory:DATA`` command.

    Description:
        - This command sets or returns block data to/from a file in the current mass storage device.

    Usage:
        - Using the ``.query(argument)`` method will send the ``MMEMory:DATA? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the ``MMEMory:DATA? argument``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MMEMory:DATA value`` command.

    SCPI Syntax:
        ```
        - MMEMory:DATA <file_path>[,<start_index>],<block_data>
        - MMEMory:DATA? <file_path>[,<start_index>[,<size>]]
        ```

    Properties:
        - ``.size``: The ``MMEMory:DATA:SIZE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._size = MmemoryDataSize(device, f"{self._cmd_syntax}:SIZE")

    @property
    def size(self) -> MmemoryDataSize:
        """Return the ``MMEMory:DATA:SIZE`` command.

        Description:
            - This command returns the size in bytes of a selected file.

        Usage:
            - Using the ``.query(argument)`` method will send the ``MMEMory:DATA:SIZE? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``MMEMory:DATA:SIZE? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.

        SCPI Syntax:
            ```
            - MMEMory:DATA:SIZE? <file_path>
            ```
        """
        return self._size


class MmemoryCdirectory(SCPICmdWrite, SCPICmdRead):
    """The ``MMEMory:CDIRectory`` command.

    Description:
        - This command changes the current working directory in the mass storage system.

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:CDIRectory?`` query.
        - Using the ``.verify(value)`` method will send the ``MMEMory:CDIRectory?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MMEMory:CDIRectory value`` command.

    SCPI Syntax:
        ```
        - MMEMory:CDIRectory [<directory_name>]
        - MMEMory:CDIRectory?
        ```
    """


class MmemoryCatalog(SCPICmdReadWithArguments):
    """The ``MMEMory:CATalog`` command.

    Description:
        - This command returns the current contents and state of the mass storage media.

    Usage:
        - Using the ``.query(argument)`` method will send the ``MMEMory:CATalog? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the ``MMEMory:CATalog? argument``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MMEMory:CATalog? [<msus>]
        ```
    """


#  pylint: disable=too-many-instance-attributes
class Mmemory(SCPICmdRead):
    """The ``MMEMory`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory?`` query.
        - Using the ``.verify(value)`` method will send the ``MMEMory?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.catalog``: The ``MMEMory:CATalog`` command.
        - ``.cdirectory``: The ``MMEMory:CDIRectory`` command.
        - ``.data``: The ``MMEMory:DATA`` command.
        - ``.delete``: The ``MMEMory:DELete`` command.
        - ``.import``: The ``MMEMory:IMPort`` command.
        - ``.mdirectory``: The ``MMEMory:MDIRectory`` command.
        - ``.msis``: The ``MMEMory:MSIS`` command.
        - ``.open``: The ``MMEMory:OPEN`` command.
        - ``.save``: The ``MMEMory:SAVE`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "MMEMory") -> None:
        super().__init__(device, cmd_syntax)
        self._catalog = MmemoryCatalog(device, f"{self._cmd_syntax}:CATalog")
        self._cdirectory = MmemoryCdirectory(device, f"{self._cmd_syntax}:CDIRectory")
        self._data = MmemoryData(device, f"{self._cmd_syntax}:DATA")
        self._delete = MmemoryDelete(device, f"{self._cmd_syntax}:DELete")
        self._import = MmemoryImport(device, f"{self._cmd_syntax}:IMPort")
        self._mdirectory = MmemoryMdirectory(device, f"{self._cmd_syntax}:MDIRectory")
        self._msis = MmemoryMsis(device, f"{self._cmd_syntax}:MSIS")
        self._open = MmemoryOpen(device, f"{self._cmd_syntax}:OPEN")
        self._save = MmemorySave(device, f"{self._cmd_syntax}:SAVE")

    @property
    def catalog(self) -> MmemoryCatalog:
        """Return the ``MMEMory:CATalog`` command.

        Description:
            - This command returns the current contents and state of the mass storage media.

        Usage:
            - Using the ``.query(argument)`` method will send the ``MMEMory:CATalog? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``MMEMory:CATalog? argument`` query and raise an AssertionError if the returned value
              does not match ``value``.

        SCPI Syntax:
            ```
            - MMEMory:CATalog? [<msus>]
            ```
        """
        return self._catalog

    @property
    def cdirectory(self) -> MmemoryCdirectory:
        """Return the ``MMEMory:CDIRectory`` command.

        Description:
            - This command changes the current working directory in the mass storage system.

        Usage:
            - Using the ``.query()`` method will send the ``MMEMory:CDIRectory?`` query.
            - Using the ``.verify(value)`` method will send the ``MMEMory:CDIRectory?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MMEMory:CDIRectory value`` command.

        SCPI Syntax:
            ```
            - MMEMory:CDIRectory [<directory_name>]
            - MMEMory:CDIRectory?
            ```
        """
        return self._cdirectory

    @property
    def data(self) -> MmemoryData:
        """Return the ``MMEMory:DATA`` command.

        Description:
            - This command sets or returns block data to/from a file in the current mass storage
              device.

        Usage:
            - Using the ``.query(argument)`` method will send the ``MMEMory:DATA? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the ``MMEMory:DATA? argument``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MMEMory:DATA value`` command.

        SCPI Syntax:
            ```
            - MMEMory:DATA <file_path>[,<start_index>],<block_data>
            - MMEMory:DATA? <file_path>[,<start_index>[,<size>]]
            ```

        Sub-properties:
            - ``.size``: The ``MMEMory:DATA:SIZE`` command.
        """
        return self._data

    @property
    def delete(self) -> MmemoryDelete:
        """Return the ``MMEMory:DELete`` command.

        Description:
            - This command deletes a file or directory from the AWG's hard disk. When used on a
              directory, this command succeeds only if the directory is empty.

        Usage:
            - Using the ``.write(value)`` method will send the ``MMEMory:DELete value`` command.

        SCPI Syntax:
            ```
            - MMEMory:DELete <file_name>[,<msus>]
            ```
        """
        return self._delete

    @property
    def import_(self) -> MmemoryImport:
        """Return the ``MMEMory:IMPort`` command.

        Description:
            - This command imports a file into the AWG's waveform list. File formats supported: ISF
              - TDS3000 and DPO4000 waveform formatTDS - TDS5000/TDS6000/TDS7000,
              DPO7000/DPO70000/DSA70000 Series waveformTXT - Text file with analog dataTXT8 - Text
              file with 8 bit DAC resolutionTXT9 - Text file with 9 bit DAC resolutionTXT10 - Text
              file with 10 bit DAC resolutionTXT14 - Text file with 14 bit DAC resolutionWFM -
              AWG400/AWG500/AWG600/AWG700 Series waveformPAT - AWG400/AWG500/AWG600/AWG700 Series
              pattern fileTFW - AFG3000 Series waveform file formatIQT - RSA3000 Series waveform
              file formatTIQ - RSA6000 Series waveform file format

        Usage:
            - Using the ``.write(value)`` method will send the ``MMEMory:IMPort value`` command.

        SCPI Syntax:
            ```
            - MMEMory:IMPort <wfm_name>,<filepath>,<type>
            ```

        Sub-properties:
            - ``.parameter``: The ``MMEMory:IMPort:PARameter`` command tree.
        """
        return self._import

    @property
    def mdirectory(self) -> MmemoryMdirectory:
        """Return the ``MMEMory:MDIRectory`` command.

        Description:
            - This command creates a directory in the mass storage system. If the specified
              directory is locked in the mass storage system, this command causes an error.

        Usage:
            - Using the ``.write(value)`` method will send the ``MMEMory:MDIRectory value`` command.

        SCPI Syntax:
            ```
            - MMEMory:MDIRectory <directory_name>
            ```
        """
        return self._mdirectory

    @property
    def msis(self) -> MmemoryMsis:
        """Return the ``MMEMory:MSIS`` command.

        Description:
            - This command selects or returns a mass storage device used by all MMEMory commands.
              <msus> specifies a drive using a drive letter. The drive letter can represent hard
              disk drives, network drives, external DVD/CD-RW drives, or USB memory.

        Usage:
            - Using the ``.query()`` method will send the ``MMEMory:MSIS?`` query.
            - Using the ``.verify(value)`` method will send the ``MMEMory:MSIS?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MMEMory:MSIS value`` command.

        SCPI Syntax:
            ```
            - MMEMory:MSIS [<msus>]
            - MMEMory:MSIS?
            ```
        """
        return self._msis

    @property
    def open(self) -> MmemoryOpen:
        """Return the ``MMEMory:OPEN`` command.

        Description:
            - This command loads a file into the AWG waveform list. File formats supported: .WFMX -
              AWG70000 Series waveform file format.ISF - TDS3000 and DPO4000 waveform file
              format.TDS - TDS5000/TDS6000/TDS7000, DPO7000/DPO70000/DSA70000 Series waveform file
              format.WFM - AWG400/AWG500/AWG600/AWG700/AWG5000/AWG7000 Series waveform file
              format.PAT - AWG400/AWG500/AWG600/AWG700 Series pattern file.TFW - AFG3000 Series
              waveform file format.IQT - RSA3000 Series waveform file format.TIQ - RFXpress waveform
              file format.TIQ - RSA6000 Series waveform file format.WFM - MDO waveform file
              format.SEQX - AWG70000 Series sequence file format.SEQ - AWG400/AWG500/AWG600 sequence
              format.TMP - Midas BLUE file format.PRM - Midas BLUE file format

        Usage:
            - Using the ``.write(value)`` method will send the ``MMEMory:OPEN value`` command.

        SCPI Syntax:
            ```
            - MMEMory:OPEN <filepath>
            ```

        Sub-properties:
            - ``.sasset``: The ``MMEMory:OPEN:SASSet`` command tree.
            - ``.setup``: The ``MMEMory:OPEN:SETup`` command.
            - ``.txt``: The ``MMEMory:OPEN:TXT`` command.
            - ``.parameter``: The ``MMEMory:OPEN:PARameter`` command tree.
        """
        return self._open

    @property
    def save(self) -> MmemorySave:
        """Return the ``MMEMory:SAVE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MMEMory:SAVE?`` query.
            - Using the ``.verify(value)`` method will send the ``MMEMory:SAVE?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.sequence``: The ``MMEMory:SAVE:SEQuence`` command.
            - ``.setup``: The ``MMEMory:SAVE:SETup`` command.
            - ``.waveform``: The ``MMEMory:SAVE:WAVeform`` command tree.
        """
        return self._save
