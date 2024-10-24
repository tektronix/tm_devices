"""The saveon commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SAVEON {RESET}
    - SAVEON:COUNt?
    - SAVEON:FILE:AUTOInc {ON|OFF|<NR1>}
    - SAVEON:FILE:AUTOInc?
    - SAVEON:FILE:COUNt <NR3>
    - SAVEON:FILE:COUNt?
    - SAVEON:FILE:DEST <string>
    - SAVEON:FILE:DEST?
    - SAVEON:FILE:NAME <string>
    - SAVEON:FILE:NAME?
    - SAVEON:FILE:TYPE {AUTO|CUSTOM}
    - SAVEON:FILE:TYPE?
    - SAVEON:IMAGe {ON|OFF|<NR1>}
    - SAVEON:IMAGe?
    - SAVEON:LIMit {ON|OFF|<NR1>}
    - SAVEON:LIMit?
    - SAVEON:MASK {ON|OFF|<NR1>}
    - SAVEON:MASK?
    - SAVEON:MEASUrement {ON|OFF|<NR1>}
    - SAVEON:MEASUrement?
    - SAVEON:NUMEvents <NR3>
    - SAVEON:NUMEvents?
    - SAVEON:SETUP {ON|OFF|<NR1>}
    - SAVEON:SETUP?
    - SAVEON:TRIGger {ON|OFF|<NR1>}
    - SAVEON:TRIGger?
    - SAVEON:WAVEform {ON|OFF|<NR1>}
    - SAVEON:WAVEform?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class SaveonWaveform(SCPICmdWrite, SCPICmdRead):
    """The ``SAVEON:WAVEform`` command.

    Description:
        - Sets or queries whether to save a waveform when a trigger occurs when ``SAVEON:TRIGGER``
          is ON. The waveform will be saved to the file you selected with ``SAVEON:FILE:NAME``, in
          the location that you selected using ``SAVEON:FILE:DEST``. You can set options for file
          storage (such as file name, file destination, and autoincrement), using the
          ``SAVEON:FILE`` commands.

    Usage:
        - Using the ``.query()`` method will send the ``SAVEON:WAVEform?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEON:WAVEform?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVEON:WAVEform value`` command.

    SCPI Syntax:
        ```
        - SAVEON:WAVEform {ON|OFF|<NR1>}
        - SAVEON:WAVEform?
        ```

    Info:
        - ``<NR1>`` = 0 disables Save On Waveform; any other value turns this feature on.
        - ``OFF`` disables Save On Waveform.
        - ``ON`` enables Save On Waveform.
    """


class SaveonTrigger(SCPICmdWrite, SCPICmdRead):
    """The ``SAVEON:TRIGger`` command.

    Description:
        - Sets or queries whether to save a file when a trigger occurs. You can define the trigger
          using Trigger commands or the instrument user interface. This command is longer necessary.
          Please see Act On Event commands for future development. The trigger will cause the
          instrument to save an image or a waveform to a file, depending on what you specified. For
          example, if you have set ``SAVEON:IMAGE`` to On, and a trigger event occurs, the
          instrument will save a screen capture. You can set options for file storage (such as file
          name, file destination, and auto increment), using the ``SAVEON:FILE`` commands. Use the
          instrument interface to select whether to save one or more analog channels, digital
          channels, or math waveforms Analog and math waveforms are saved using one file per
          waveform. Digital waveforms are all saved to a single file.

    Usage:
        - Using the ``.query()`` method will send the ``SAVEON:TRIGger?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEON:TRIGger?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVEON:TRIGger value`` command.

    SCPI Syntax:
        ```
        - SAVEON:TRIGger {ON|OFF|<NR1>}
        - SAVEON:TRIGger?
        ```

    Info:
        - ``<NR1>`` = 0 disables Save On Trigger; any other value turns this feature on.
        - ``OFF`` disables Save On Trigger.
        - ``ON`` enables Save On Trigger.
    """


class SaveonSetup(SCPICmdWrite, SCPICmdRead):
    """The ``SAVEON:SETUP`` command.

    Description:
        - Saves the instrument setup when there is an event. Queries the status of this feature (on
          or off).

    Usage:
        - Using the ``.query()`` method will send the ``SAVEON:SETUP?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEON:SETUP?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVEON:SETUP value`` command.

    SCPI Syntax:
        ```
        - SAVEON:SETUP {ON|OFF|<NR1>}
        - SAVEON:SETUP?
        ```

    Info:
        - ``<NR1>`` = 0 disables the feature; any other value turns this feature on.
        - ``ON`` enables the feature.
        - ``OFF`` disables the feature.
    """


class SaveonNumevents(SCPICmdWrite, SCPICmdRead):
    """The ``SAVEON:NUMEvents`` command.

    Description:
        - Sets or queries the maximum number of events that will be saved. You can use this feature
          to avoid running out of disk space, especially if you save large files.

    Usage:
        - Using the ``.query()`` method will send the ``SAVEON:NUMEvents?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEON:NUMEvents?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVEON:NUMEvents value`` command.

    SCPI Syntax:
        ```
        - SAVEON:NUMEvents <NR3>
        - SAVEON:NUMEvents?
        ```

    Info:
        - ``<NR3>`` specifies the number of events that will be saved before a reset is required.
    """


class SaveonMeasurement(SCPICmdWrite, SCPICmdRead):
    """The ``SAVEON:MEASUrement`` command.

    Description:
        - Sets or queries whether to save a measurement when any of the following triggers occurs:
          Limit test failure - if set to On. (``SAVEON:LIMIT``) Mask failure - if set to On.
          (``SAVEON:MASK``) Trigger - if set to On. (``SAVEON:TRIGGER``) The image will be saved to
          the file you selected with ``SAVEON:FILE:NAME``, in the location that you selected using
          ``SAVEON:FILE:DEST``. You can set options for file storage (such as file name, file
          destination, and autoincrement), using the SaveOn File commands.

    Usage:
        - Using the ``.query()`` method will send the ``SAVEON:MEASUrement?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEON:MEASUrement?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVEON:MEASUrement value`` command.

    SCPI Syntax:
        ```
        - SAVEON:MEASUrement {ON|OFF|<NR1>}
        - SAVEON:MEASUrement?
        ```

    Info:
        - ``<NR1>`` = 0 disables Save On Measurement; any other value turns this feature on.
        - ``OFF`` disables Save On Measurement.
        - ``ON`` enables Save On Measurement.
    """


class SaveonMask(SCPICmdWrite, SCPICmdRead):
    """The ``SAVEON:MASK`` command.

    Description:
        - Sets or queries whether to save a file when there is a mask failure. When ``SAVEON:MASK``
          is enabled, a mask failure will trigger the instrument to save an image, a measurement,
          and/or a waveform to a file, depending on what you specify using the Related Commands
          listed below. When there is a mask failure, if you have enabled ``SAVEON:IMAGe``, the
          instrument will save a screen capture to the file you selected using ``SAVEON:FILE:NAME``
          and ``SAVEON:FILE:DEST``. You can set options for file storage (such as file name, file
          destination, and autoincrement), using the SaveOn File commands. Use the oscilloscope
          interface to select whether to save one or more analog channels, digital channels, or math
          waveforms Analog and math waveforms are saved using one file per waveform. Digital
          waveforms are all saved to a single file.

    Usage:
        - Using the ``.query()`` method will send the ``SAVEON:MASK?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEON:MASK?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVEON:MASK value`` command.

    SCPI Syntax:
        ```
        - SAVEON:MASK {ON|OFF|<NR1>}
        - SAVEON:MASK?
        ```

    Info:
        - ``<NR1>`` = 0 disables Save On Mask; any other value turns this feature on.
        - ``OFF`` disables Save On Mask.
        - ``ON`` enables Save On Mask.
    """


class SaveonLimit(SCPICmdWrite, SCPICmdRead):
    """The ``SAVEON:LIMit`` command.

    Description:
        - Sets or queries whether to save a file when there is a limit test failure. When this is
          set to On, a limit test failure will trigger the instrument to save an image, a
          measurement, and/or a waveform to a file, depending on what you specify using the Related
          Commands listed below. For example, if you set ``SAVEON:IMAGe`` to On, the instrument will
          save a screen capture to the file you selected with ``SAVEON:FILE:NAME``, in the location
          that you selected using ``SAVEON:FILE:DEST``. You can set options for file storage (such
          as file name, file destination, and autoincrement), using the SaveOn File commands. Analog
          and math waveforms are saved using one file per waveform. Digital waveforms are all saved
          to a single file.

    Usage:
        - Using the ``.query()`` method will send the ``SAVEON:LIMit?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEON:LIMit?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVEON:LIMit value`` command.

    SCPI Syntax:
        ```
        - SAVEON:LIMit {ON|OFF|<NR1>}
        - SAVEON:LIMit?
        ```

    Info:
        - ``<NR1>`` = 0 disables Save On Limit; any other value turns this feature on.
        - ``OFF`` disables Save On Limit.
        - ``ON`` enables Save On Limit.
    """


class SaveonImage(SCPICmdWrite, SCPICmdRead):
    """The ``SAVEON:IMAGe`` command.

    Description:
        - This command sets or queries whether to save a screen capture when a trigger occurs and
          ``SAVEON:TRIGer`` is ON and ``SAVEON:IMAGE`` is ON.

    Usage:
        - Using the ``.query()`` method will send the ``SAVEON:IMAGe?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEON:IMAGe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVEON:IMAGe value`` command.

    SCPI Syntax:
        ```
        - SAVEON:IMAGe {ON|OFF|<NR1>}
        - SAVEON:IMAGe?
        ```

    Info:
        - ``<NR1>`` = 0 disables Save On Image; any other value turns this feature on.
        - ``OFF`` disables Save On Image.
        - ``ON`` enables Save On Image.
    """


class SaveonFileType(SCPICmdWrite, SCPICmdRead):
    """The ``SAVEON:FILE:TYPE`` command.

    Description:
        - Sets or queries whether to use the data and time as the file name (auto) or to use a
          custom file name.

    Usage:
        - Using the ``.query()`` method will send the ``SAVEON:FILE:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEON:FILE:TYPE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVEON:FILE:TYPE value`` command.

    SCPI Syntax:
        ```
        - SAVEON:FILE:TYPE {AUTO|CUSTOM}
        - SAVEON:FILE:TYPE?
        ```

    Info:
        - ``AUTO`` uses the date and time as the file name for the saved events. An example auto
          file name is: ``20110711_182946``.
        - ``CUSTOM`` uses the file name that you specified using the ``SAVEON:FILE:NAME`` command.
    """


class SaveonFileName(SCPICmdWrite, SCPICmdRead):
    """The ``SAVEON:FILE:NAME`` command.

    Description:
        - Sets or queries the file name to use when the file type is set to Custom. Selecting a file
          name You can select your own file name by entering the desired name in the <string>.
          Follow standard Microsoft Windows naming conventions. The limit is 127 characters, with no
          spaces allowed in the name. File storage location The file is saved in the location
          specified by the ``SAVEON:FILE:DEST`` command. Default names The default file name is
          SaveOnEvent. This name will be appended under certain circumstances. If you have
          previously selected (through the oscilloscope interface) to save channel 1 and channel 2
          waveforms, for example, two files are saved, and the default file names will reflect the
          channel. If you have selected to save bus B1, the default file name will reflect that. The
          file name also indicates whether it is an image, measurement, or waveform. Autoincrement
          If ``SAVEON:FILE:AUTOInc`` is enabled, a number will be added to the file name and will be
          incremented for each new file. For example, if three events trigger the oscilloscope to
          save a measurement, three files will be created, which might be named 'SaveOnEvent1Meas,'
          'SaveOnEvent2Meas,' and 'SaveOnEvent3Meas.' Extensions Although these files have
          extensions (CSV for measurements and WFM for waveforms, for example), you do not need to
          enter the extension. It will be added automatically, depending on what you are saving. The
          query ``SAVEON:FILE:NAME?`` will return the file name without the extension.

    Usage:
        - Using the ``.query()`` method will send the ``SAVEON:FILE:NAME?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEON:FILE:NAME?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVEON:FILE:NAME value`` command.

    SCPI Syntax:
        ```
        - SAVEON:FILE:NAME <string>
        - SAVEON:FILE:NAME?
        ```

    Info:
        - ``<string>`` is the file name you want to use.
    """


class SaveonFileDest(SCPICmdWrite, SCPICmdRead):
    """The ``SAVEON:FILE:DEST`` command.

    Description:
        - Sets or queries the location where files are saved. The default destination is
          C:usersusernameTektronixTekScopeSaveOnTrigger. You can save the files to a local drive or
          network path by entering the desired location in <string>. You can also select to save the
          files to a USB drive, using the browse button in the oscilloscope interface.

    Usage:
        - Using the ``.query()`` method will send the ``SAVEON:FILE:DEST?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEON:FILE:DEST?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVEON:FILE:DEST value`` command.

    SCPI Syntax:
        ```
        - SAVEON:FILE:DEST <string>
        - SAVEON:FILE:DEST?
        ```
    """


class SaveonFileCount(SCPICmdWrite, SCPICmdRead):
    """The ``SAVEON:FILE:COUNt`` command.

    Description:
        - <primary></primary> Sets or queries the starting number that will be appended to the
          custom file name when ``SAVEON:FILE:AUTOINC`` is enabled and an image, measurement, or
          waveform is saved. The total of files saved cannot exceed 32767. If this file count is
          reached, files will not be saved until you change the file count to a lower number.

    Usage:
        - Using the ``.query()`` method will send the ``SAVEON:FILE:COUNt?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEON:FILE:COUNt?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVEON:FILE:COUNt value`` command.

    SCPI Syntax:
        ```
        - SAVEON:FILE:COUNt <NR3>
        - SAVEON:FILE:COUNt?
        ```

    Info:
        - ``<NR3>`` specifies the starting number for automatically incrementing the file name.
    """


class SaveonFileAutoinc(SCPICmdWrite, SCPICmdRead):
    """The ``SAVEON:FILE:AUTOInc`` command.

    Description:
        - Sets or queries the state of the auto increment file name feature (on or off). If AUTOInc
          is on, each time that an image, measurement, or waveform is saved to a file, the number
          that is appended to the file name will be augmented automatically, depending on the
          settings that you have made in the Related Commands, below. If AUTOInc is off, the
          previous file will be overwritten.

    Usage:
        - Using the ``.query()`` method will send the ``SAVEON:FILE:AUTOInc?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEON:FILE:AUTOInc?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVEON:FILE:AUTOInc value`` command.

    SCPI Syntax:
        ```
        - SAVEON:FILE:AUTOInc {ON|OFF|<NR1>}
        - SAVEON:FILE:AUTOInc?
        ```

    Info:
        - ``<NR1>`` = 1 enables the Auto increment function; any other value disables the function.
        - ``ON`` indicates that each time that an image, measurement, or waveform is saved, the
          number that is appended to the file name will be augmented automatically.
        - ``OFF`` indicates that when an image, measurement, or waveform file is saved, the name
          will not be augmented and the previously saved file will be overwritten.
    """


class SaveonFile(SCPICmdRead):
    """The ``SAVEON:FILE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SAVEON:FILE?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEON:FILE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.autoinc``: The ``SAVEON:FILE:AUTOInc`` command.
        - ``.count``: The ``SAVEON:FILE:COUNt`` command.
        - ``.dest``: The ``SAVEON:FILE:DEST`` command.
        - ``.name``: The ``SAVEON:FILE:NAME`` command.
        - ``.type``: The ``SAVEON:FILE:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autoinc = SaveonFileAutoinc(device, f"{self._cmd_syntax}:AUTOInc")
        self._count = SaveonFileCount(device, f"{self._cmd_syntax}:COUNt")
        self._dest = SaveonFileDest(device, f"{self._cmd_syntax}:DEST")
        self._name = SaveonFileName(device, f"{self._cmd_syntax}:NAME")
        self._type = SaveonFileType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def autoinc(self) -> SaveonFileAutoinc:
        """Return the ``SAVEON:FILE:AUTOInc`` command.

        Description:
            - Sets or queries the state of the auto increment file name feature (on or off). If
              AUTOInc is on, each time that an image, measurement, or waveform is saved to a file,
              the number that is appended to the file name will be augmented automatically,
              depending on the settings that you have made in the Related Commands, below. If
              AUTOInc is off, the previous file will be overwritten.

        Usage:
            - Using the ``.query()`` method will send the ``SAVEON:FILE:AUTOInc?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEON:FILE:AUTOInc?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVEON:FILE:AUTOInc value``
              command.

        SCPI Syntax:
            ```
            - SAVEON:FILE:AUTOInc {ON|OFF|<NR1>}
            - SAVEON:FILE:AUTOInc?
            ```

        Info:
            - ``<NR1>`` = 1 enables the Auto increment function; any other value disables the
              function.
            - ``ON`` indicates that each time that an image, measurement, or waveform is saved, the
              number that is appended to the file name will be augmented automatically.
            - ``OFF`` indicates that when an image, measurement, or waveform file is saved, the name
              will not be augmented and the previously saved file will be overwritten.
        """
        return self._autoinc

    @property
    def count(self) -> SaveonFileCount:
        """Return the ``SAVEON:FILE:COUNt`` command.

        Description:
            - <primary></primary> Sets or queries the starting number that will be appended to the
              custom file name when ``SAVEON:FILE:AUTOINC`` is enabled and an image, measurement, or
              waveform is saved. The total of files saved cannot exceed 32767. If this file count is
              reached, files will not be saved until you change the file count to a lower number.

        Usage:
            - Using the ``.query()`` method will send the ``SAVEON:FILE:COUNt?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEON:FILE:COUNt?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVEON:FILE:COUNt value`` command.

        SCPI Syntax:
            ```
            - SAVEON:FILE:COUNt <NR3>
            - SAVEON:FILE:COUNt?
            ```

        Info:
            - ``<NR3>`` specifies the starting number for automatically incrementing the file name.
        """
        return self._count

    @property
    def dest(self) -> SaveonFileDest:
        """Return the ``SAVEON:FILE:DEST`` command.

        Description:
            - Sets or queries the location where files are saved. The default destination is
              C:usersusernameTektronixTekScopeSaveOnTrigger. You can save the files to a local drive
              or network path by entering the desired location in <string>. You can also select to
              save the files to a USB drive, using the browse button in the oscilloscope interface.

        Usage:
            - Using the ``.query()`` method will send the ``SAVEON:FILE:DEST?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEON:FILE:DEST?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVEON:FILE:DEST value`` command.

        SCPI Syntax:
            ```
            - SAVEON:FILE:DEST <string>
            - SAVEON:FILE:DEST?
            ```
        """
        return self._dest

    @property
    def name(self) -> SaveonFileName:
        """Return the ``SAVEON:FILE:NAME`` command.

        Description:
            - Sets or queries the file name to use when the file type is set to Custom. Selecting a
              file name You can select your own file name by entering the desired name in the
              <string>. Follow standard Microsoft Windows naming conventions. The limit is 127
              characters, with no spaces allowed in the name. File storage location The file is
              saved in the location specified by the ``SAVEON:FILE:DEST`` command. Default names The
              default file name is SaveOnEvent. This name will be appended under certain
              circumstances. If you have previously selected (through the oscilloscope interface) to
              save channel 1 and channel 2 waveforms, for example, two files are saved, and the
              default file names will reflect the channel. If you have selected to save bus B1, the
              default file name will reflect that. The file name also indicates whether it is an
              image, measurement, or waveform. Autoincrement If ``SAVEON:FILE:AUTOInc`` is enabled,
              a number will be added to the file name and will be incremented for each new file. For
              example, if three events trigger the oscilloscope to save a measurement, three files
              will be created, which might be named 'SaveOnEvent1Meas,' 'SaveOnEvent2Meas,' and
              'SaveOnEvent3Meas.' Extensions Although these files have extensions (CSV for
              measurements and WFM for waveforms, for example), you do not need to enter the
              extension. It will be added automatically, depending on what you are saving. The query
              ``SAVEON:FILE:NAME?`` will return the file name without the extension.

        Usage:
            - Using the ``.query()`` method will send the ``SAVEON:FILE:NAME?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEON:FILE:NAME?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVEON:FILE:NAME value`` command.

        SCPI Syntax:
            ```
            - SAVEON:FILE:NAME <string>
            - SAVEON:FILE:NAME?
            ```

        Info:
            - ``<string>`` is the file name you want to use.
        """
        return self._name

    @property
    def type(self) -> SaveonFileType:
        """Return the ``SAVEON:FILE:TYPE`` command.

        Description:
            - Sets or queries whether to use the data and time as the file name (auto) or to use a
              custom file name.

        Usage:
            - Using the ``.query()`` method will send the ``SAVEON:FILE:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEON:FILE:TYPE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVEON:FILE:TYPE value`` command.

        SCPI Syntax:
            ```
            - SAVEON:FILE:TYPE {AUTO|CUSTOM}
            - SAVEON:FILE:TYPE?
            ```

        Info:
            - ``AUTO`` uses the date and time as the file name for the saved events. An example auto
              file name is: ``20110711_182946``.
            - ``CUSTOM`` uses the file name that you specified using the ``SAVEON:FILE:NAME``
              command.
        """
        return self._type


class SaveonCount(SCPICmdRead):
    """The ``SAVEON:COUNt`` command.

    Description:
        - Returns the number of events (files) that have been saved since the last reset.

    Usage:
        - Using the ``.query()`` method will send the ``SAVEON:COUNt?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEON:COUNt?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SAVEON:COUNt?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class Saveon(SCPICmdWrite, SCPICmdRead):
    """The ``SAVEON`` command.

    Description:
        - Sets the auto-increment file count to 0. Once the number of saved files has reached the
          limit that you set (using the ``SAVEON:NUMevents`` command), no files will be saved until
          you reset the count.

    Usage:
        - Using the ``.write(value)`` method will send the ``SAVEON value`` command.

    SCPI Syntax:
        ```
        - SAVEON {RESET}
        ```

    Info:
        - ``RESET`` sets the file count to 0.

    Properties:
        - ``.count``: The ``SAVEON:COUNt`` command.
        - ``.file``: The ``SAVEON:FILE`` command tree.
        - ``.image``: The ``SAVEON:IMAGe`` command.
        - ``.limit``: The ``SAVEON:LIMit`` command.
        - ``.mask``: The ``SAVEON:MASK`` command.
        - ``.measurement``: The ``SAVEON:MEASUrement`` command.
        - ``.numevents``: The ``SAVEON:NUMEvents`` command.
        - ``.setup``: The ``SAVEON:SETUP`` command.
        - ``.trigger``: The ``SAVEON:TRIGger`` command.
        - ``.waveform``: The ``SAVEON:WAVEform`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SAVEON") -> None:
        super().__init__(device, cmd_syntax)
        self._count = SaveonCount(device, f"{self._cmd_syntax}:COUNt")
        self._file = SaveonFile(device, f"{self._cmd_syntax}:FILE")
        self._image = SaveonImage(device, f"{self._cmd_syntax}:IMAGe")
        self._limit = SaveonLimit(device, f"{self._cmd_syntax}:LIMit")
        self._mask = SaveonMask(device, f"{self._cmd_syntax}:MASK")
        self._measurement = SaveonMeasurement(device, f"{self._cmd_syntax}:MEASUrement")
        self._numevents = SaveonNumevents(device, f"{self._cmd_syntax}:NUMEvents")
        self._setup = SaveonSetup(device, f"{self._cmd_syntax}:SETUP")
        self._trigger = SaveonTrigger(device, f"{self._cmd_syntax}:TRIGger")
        self._waveform = SaveonWaveform(device, f"{self._cmd_syntax}:WAVEform")

    @property
    def count(self) -> SaveonCount:
        """Return the ``SAVEON:COUNt`` command.

        Description:
            - Returns the number of events (files) that have been saved since the last reset.

        Usage:
            - Using the ``.query()`` method will send the ``SAVEON:COUNt?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEON:COUNt?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SAVEON:COUNt?
            ```
        """
        return self._count

    @property
    def file(self) -> SaveonFile:
        """Return the ``SAVEON:FILE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SAVEON:FILE?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEON:FILE?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.autoinc``: The ``SAVEON:FILE:AUTOInc`` command.
            - ``.count``: The ``SAVEON:FILE:COUNt`` command.
            - ``.dest``: The ``SAVEON:FILE:DEST`` command.
            - ``.name``: The ``SAVEON:FILE:NAME`` command.
            - ``.type``: The ``SAVEON:FILE:TYPE`` command.
        """
        return self._file

    @property
    def image(self) -> SaveonImage:
        """Return the ``SAVEON:IMAGe`` command.

        Description:
            - This command sets or queries whether to save a screen capture when a trigger occurs
              and ``SAVEON:TRIGer`` is ON and ``SAVEON:IMAGE`` is ON.

        Usage:
            - Using the ``.query()`` method will send the ``SAVEON:IMAGe?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEON:IMAGe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVEON:IMAGe value`` command.

        SCPI Syntax:
            ```
            - SAVEON:IMAGe {ON|OFF|<NR1>}
            - SAVEON:IMAGe?
            ```

        Info:
            - ``<NR1>`` = 0 disables Save On Image; any other value turns this feature on.
            - ``OFF`` disables Save On Image.
            - ``ON`` enables Save On Image.
        """
        return self._image

    @property
    def limit(self) -> SaveonLimit:
        """Return the ``SAVEON:LIMit`` command.

        Description:
            - Sets or queries whether to save a file when there is a limit test failure. When this
              is set to On, a limit test failure will trigger the instrument to save an image, a
              measurement, and/or a waveform to a file, depending on what you specify using the
              Related Commands listed below. For example, if you set ``SAVEON:IMAGe`` to On, the
              instrument will save a screen capture to the file you selected with
              ``SAVEON:FILE:NAME``, in the location that you selected using ``SAVEON:FILE:DEST``.
              You can set options for file storage (such as file name, file destination, and
              autoincrement), using the SaveOn File commands. Analog and math waveforms are saved
              using one file per waveform. Digital waveforms are all saved to a single file.

        Usage:
            - Using the ``.query()`` method will send the ``SAVEON:LIMit?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEON:LIMit?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVEON:LIMit value`` command.

        SCPI Syntax:
            ```
            - SAVEON:LIMit {ON|OFF|<NR1>}
            - SAVEON:LIMit?
            ```

        Info:
            - ``<NR1>`` = 0 disables Save On Limit; any other value turns this feature on.
            - ``OFF`` disables Save On Limit.
            - ``ON`` enables Save On Limit.
        """
        return self._limit

    @property
    def mask(self) -> SaveonMask:
        """Return the ``SAVEON:MASK`` command.

        Description:
            - Sets or queries whether to save a file when there is a mask failure. When
              ``SAVEON:MASK`` is enabled, a mask failure will trigger the instrument to save an
              image, a measurement, and/or a waveform to a file, depending on what you specify using
              the Related Commands listed below. When there is a mask failure, if you have enabled
              ``SAVEON:IMAGe``, the instrument will save a screen capture to the file you selected
              using ``SAVEON:FILE:NAME`` and ``SAVEON:FILE:DEST``. You can set options for file
              storage (such as file name, file destination, and autoincrement), using the SaveOn
              File commands. Use the oscilloscope interface to select whether to save one or more
              analog channels, digital channels, or math waveforms Analog and math waveforms are
              saved using one file per waveform. Digital waveforms are all saved to a single file.

        Usage:
            - Using the ``.query()`` method will send the ``SAVEON:MASK?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEON:MASK?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVEON:MASK value`` command.

        SCPI Syntax:
            ```
            - SAVEON:MASK {ON|OFF|<NR1>}
            - SAVEON:MASK?
            ```

        Info:
            - ``<NR1>`` = 0 disables Save On Mask; any other value turns this feature on.
            - ``OFF`` disables Save On Mask.
            - ``ON`` enables Save On Mask.
        """
        return self._mask

    @property
    def measurement(self) -> SaveonMeasurement:
        """Return the ``SAVEON:MEASUrement`` command.

        Description:
            - Sets or queries whether to save a measurement when any of the following triggers
              occurs: Limit test failure - if set to On. (``SAVEON:LIMIT``) Mask failure - if set to
              On. (``SAVEON:MASK``) Trigger - if set to On. (``SAVEON:TRIGGER``) The image will be
              saved to the file you selected with ``SAVEON:FILE:NAME``, in the location that you
              selected using ``SAVEON:FILE:DEST``. You can set options for file storage (such as
              file name, file destination, and autoincrement), using the SaveOn File commands.

        Usage:
            - Using the ``.query()`` method will send the ``SAVEON:MEASUrement?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEON:MEASUrement?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVEON:MEASUrement value`` command.

        SCPI Syntax:
            ```
            - SAVEON:MEASUrement {ON|OFF|<NR1>}
            - SAVEON:MEASUrement?
            ```

        Info:
            - ``<NR1>`` = 0 disables Save On Measurement; any other value turns this feature on.
            - ``OFF`` disables Save On Measurement.
            - ``ON`` enables Save On Measurement.
        """
        return self._measurement

    @property
    def numevents(self) -> SaveonNumevents:
        """Return the ``SAVEON:NUMEvents`` command.

        Description:
            - Sets or queries the maximum number of events that will be saved. You can use this
              feature to avoid running out of disk space, especially if you save large files.

        Usage:
            - Using the ``.query()`` method will send the ``SAVEON:NUMEvents?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEON:NUMEvents?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVEON:NUMEvents value`` command.

        SCPI Syntax:
            ```
            - SAVEON:NUMEvents <NR3>
            - SAVEON:NUMEvents?
            ```

        Info:
            - ``<NR3>`` specifies the number of events that will be saved before a reset is
              required.
        """
        return self._numevents

    @property
    def setup(self) -> SaveonSetup:
        """Return the ``SAVEON:SETUP`` command.

        Description:
            - Saves the instrument setup when there is an event. Queries the status of this feature
              (on or off).

        Usage:
            - Using the ``.query()`` method will send the ``SAVEON:SETUP?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEON:SETUP?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVEON:SETUP value`` command.

        SCPI Syntax:
            ```
            - SAVEON:SETUP {ON|OFF|<NR1>}
            - SAVEON:SETUP?
            ```

        Info:
            - ``<NR1>`` = 0 disables the feature; any other value turns this feature on.
            - ``ON`` enables the feature.
            - ``OFF`` disables the feature.
        """
        return self._setup

    @property
    def trigger(self) -> SaveonTrigger:
        """Return the ``SAVEON:TRIGger`` command.

        Description:
            - Sets or queries whether to save a file when a trigger occurs. You can define the
              trigger using Trigger commands or the instrument user interface. This command is
              longer necessary. Please see Act On Event commands for future development. The trigger
              will cause the instrument to save an image or a waveform to a file, depending on what
              you specified. For example, if you have set ``SAVEON:IMAGE`` to On, and a trigger
              event occurs, the instrument will save a screen capture. You can set options for file
              storage (such as file name, file destination, and auto increment), using the
              ``SAVEON:FILE`` commands. Use the instrument interface to select whether to save one
              or more analog channels, digital channels, or math waveforms Analog and math waveforms
              are saved using one file per waveform. Digital waveforms are all saved to a single
              file.

        Usage:
            - Using the ``.query()`` method will send the ``SAVEON:TRIGger?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEON:TRIGger?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVEON:TRIGger value`` command.

        SCPI Syntax:
            ```
            - SAVEON:TRIGger {ON|OFF|<NR1>}
            - SAVEON:TRIGger?
            ```

        Info:
            - ``<NR1>`` = 0 disables Save On Trigger; any other value turns this feature on.
            - ``OFF`` disables Save On Trigger.
            - ``ON`` enables Save On Trigger.
        """
        return self._trigger

    @property
    def waveform(self) -> SaveonWaveform:
        """Return the ``SAVEON:WAVEform`` command.

        Description:
            - Sets or queries whether to save a waveform when a trigger occurs when
              ``SAVEON:TRIGGER`` is ON. The waveform will be saved to the file you selected with
              ``SAVEON:FILE:NAME``, in the location that you selected using ``SAVEON:FILE:DEST``.
              You can set options for file storage (such as file name, file destination, and
              autoincrement), using the ``SAVEON:FILE`` commands.

        Usage:
            - Using the ``.query()`` method will send the ``SAVEON:WAVEform?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEON:WAVEform?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVEON:WAVEform value`` command.

        SCPI Syntax:
            ```
            - SAVEON:WAVEform {ON|OFF|<NR1>}
            - SAVEON:WAVEform?
            ```

        Info:
            - ``<NR1>`` = 0 disables Save On Waveform; any other value turns this feature on.
            - ``OFF`` disables Save On Waveform.
            - ``ON`` enables Save On Waveform.
        """
        return self._waveform
