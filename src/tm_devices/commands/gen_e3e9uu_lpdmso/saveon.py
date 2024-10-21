"""The saveon commands module.

These commands are used in the following models:
LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SAVEON:FILE:DEST <QString>
    - SAVEON:FILE:DEST?
    - SAVEON:FILE:NAME <QString>
    - SAVEON:FILE:NAME?
    - SAVEON:IMAGe {ON|OFF|<NR1>}
    - SAVEON:IMAGe:FILEFormat {PNG|BMP|JPG}
    - SAVEON:IMAGe:FILEFormat?
    - SAVEON:IMAGe?
    - SAVEON:TRIGger {ON|OFF|<NR1>}
    - SAVEON:TRIGger?
    - SAVEON:WAVEform {ON|OFF|<NR1>}
    - SAVEON:WAVEform:FILEFormat {INTERNal|SPREADSheet}
    - SAVEON:WAVEform:FILEFormat?
    - SAVEON:WAVEform:SOURce {CH<x>|MATH<x>|REF<x>|ALL}
    - SAVEON:WAVEform:SOURce?
    - SAVEON:WAVEform?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class SaveonWaveformSource(SCPICmdWrite, SCPICmdRead):
    """The ``SAVEON:WAVEform:SOURce`` command.

    Description:
        - This command sets or queries the sources for saving waveforms when ``SAVEON:TRIGGER`` is
          ON.

    Usage:
        - Using the ``.query()`` method will send the ``SAVEON:WAVEform:SOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEON:WAVEform:SOURce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVEON:WAVEform:SOURce value`` command.

    SCPI Syntax:
        ```
        - SAVEON:WAVEform:SOURce {CH<x>|MATH<x>|REF<x>|ALL}
        - SAVEON:WAVEform:SOURce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the source waveform for saving.
        - ``MATH<x>`` specifies a math waveform as the source waveform for saving.
        - ``REF<x>`` specifies a reference waveform as the source waveform for saving.
        - ``ALL`` specifies all analog, math, and reference waveforms as the source waveforms for
          saving.
    """


class SaveonWaveformFileformat(SCPICmdWrite, SCPICmdRead):
    """The ``SAVEON:WAVEform:FILEFormat`` command.

    Description:
        - This command sets or queries the file format for saving waveforms when
          ``:SAVEON:WAVEform`` is set to 1.

    Usage:
        - Using the ``.query()`` method will send the ``SAVEON:WAVEform:FILEFormat?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEON:WAVEform:FILEFormat?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVEON:WAVEform:FILEFormat value``
          command.

    SCPI Syntax:
        ```
        - SAVEON:WAVEform:FILEFormat {INTERNal|SPREADSheet}
        - SAVEON:WAVEform:FILEFormat?
        ```

    Info:
        - ``INTERNal`` specifies saving the waveform in the instrument internal format.
        - ``SPREADSheet`` specifies saving the waveform in comma separated values format.
    """


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

    Properties:
        - ``.fileformat``: The ``SAVEON:WAVEform:FILEFormat`` command.
        - ``.source``: The ``SAVEON:WAVEform:SOURce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fileformat = SaveonWaveformFileformat(device, f"{self._cmd_syntax}:FILEFormat")
        self._source = SaveonWaveformSource(device, f"{self._cmd_syntax}:SOURce")

    @property
    def fileformat(self) -> SaveonWaveformFileformat:
        """Return the ``SAVEON:WAVEform:FILEFormat`` command.

        Description:
            - This command sets or queries the file format for saving waveforms when
              ``:SAVEON:WAVEform`` is set to 1.

        Usage:
            - Using the ``.query()`` method will send the ``SAVEON:WAVEform:FILEFormat?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEON:WAVEform:FILEFormat?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVEON:WAVEform:FILEFormat value``
              command.

        SCPI Syntax:
            ```
            - SAVEON:WAVEform:FILEFormat {INTERNal|SPREADSheet}
            - SAVEON:WAVEform:FILEFormat?
            ```

        Info:
            - ``INTERNal`` specifies saving the waveform in the instrument internal format.
            - ``SPREADSheet`` specifies saving the waveform in comma separated values format.
        """
        return self._fileformat

    @property
    def source(self) -> SaveonWaveformSource:
        """Return the ``SAVEON:WAVEform:SOURce`` command.

        Description:
            - This command sets or queries the sources for saving waveforms when ``SAVEON:TRIGGER``
              is ON.

        Usage:
            - Using the ``.query()`` method will send the ``SAVEON:WAVEform:SOURce?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEON:WAVEform:SOURce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVEON:WAVEform:SOURce value``
              command.

        SCPI Syntax:
            ```
            - SAVEON:WAVEform:SOURce {CH<x>|MATH<x>|REF<x>|ALL}
            - SAVEON:WAVEform:SOURce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the source waveform for saving.
            - ``MATH<x>`` specifies a math waveform as the source waveform for saving.
            - ``REF<x>`` specifies a reference waveform as the source waveform for saving.
            - ``ALL`` specifies all analog, math, and reference waveforms as the source waveforms
              for saving.
        """
        return self._source


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


class SaveonImageFileformat(SCPICmdWrite, SCPICmdRead):
    """The ``SAVEON:IMAGe:FILEFormat`` command.

    Description:
        - This command sets or queries the file format to be used for saved image files when
          ``:SAVEON:IMAGe`` is set to 1.

    Usage:
        - Using the ``.query()`` method will send the ``SAVEON:IMAGe:FILEFormat?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEON:IMAGe:FILEFormat?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVEON:IMAGe:FILEFormat value``
          command.

    SCPI Syntax:
        ```
        - SAVEON:IMAGe:FILEFormat {PNG|BMP|JPG}
        - SAVEON:IMAGe:FILEFormat?
        ```

    Info:
        - ``PNG`` specifies using PNG format for saved image files.
        - ``BMP`` specifies using BMP format for saved image files.
        - ``JPG`` specifies using JPEG format for saved image files.
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

    Properties:
        - ``.fileformat``: The ``SAVEON:IMAGe:FILEFormat`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fileformat = SaveonImageFileformat(device, f"{self._cmd_syntax}:FILEFormat")

    @property
    def fileformat(self) -> SaveonImageFileformat:
        """Return the ``SAVEON:IMAGe:FILEFormat`` command.

        Description:
            - This command sets or queries the file format to be used for saved image files when
              ``:SAVEON:IMAGe`` is set to 1.

        Usage:
            - Using the ``.query()`` method will send the ``SAVEON:IMAGe:FILEFormat?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEON:IMAGe:FILEFormat?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVEON:IMAGe:FILEFormat value``
              command.

        SCPI Syntax:
            ```
            - SAVEON:IMAGe:FILEFormat {PNG|BMP|JPG}
            - SAVEON:IMAGe:FILEFormat?
            ```

        Info:
            - ``PNG`` specifies using PNG format for saved image files.
            - ``BMP`` specifies using BMP format for saved image files.
            - ``JPG`` specifies using JPEG format for saved image files.
        """
        return self._fileformat


class SaveonFileName(SCPICmdWrite, SCPICmdRead):
    """The ``SAVEON:FILE:NAME`` command.

    Description:
        - Sets or queries the file name to use when ``SAVEON:TRIGer`` is ON.

    Usage:
        - Using the ``.query()`` method will send the ``SAVEON:FILE:NAME?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEON:FILE:NAME?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVEON:FILE:NAME value`` command.

    SCPI Syntax:
        ```
        - SAVEON:FILE:NAME <QString>
        - SAVEON:FILE:NAME?
        ```

    Info:
        - ``<QString>`` is the file name you want to use.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SaveonFileDest(SCPICmdWrite, SCPICmdRead):
    """The ``SAVEON:FILE:DEST`` command.

    Description:
        - This command sets or queries the location where files are saved when ``SAVEON:TRIGGER`` is
          ON and ``SAVEON:WAVEFORM`` is ON. You can save the files to a local drive or network path
          by entering the desired location in <QString>. You can also select to save the files to a
          USB drive.

    Usage:
        - Using the ``.query()`` method will send the ``SAVEON:FILE:DEST?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEON:FILE:DEST?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVEON:FILE:DEST value`` command.

    SCPI Syntax:
        ```
        - SAVEON:FILE:DEST <QString>
        - SAVEON:FILE:DEST?
        ```

    Info:
        - ``<QString>`` specifies the location to store files.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SaveonFile(SCPICmdRead):
    """The ``SAVEON:FILE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SAVEON:FILE?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEON:FILE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.dest``: The ``SAVEON:FILE:DEST`` command.
        - ``.name``: The ``SAVEON:FILE:NAME`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._dest = SaveonFileDest(device, f"{self._cmd_syntax}:DEST")
        self._name = SaveonFileName(device, f"{self._cmd_syntax}:NAME")

    @property
    def dest(self) -> SaveonFileDest:
        """Return the ``SAVEON:FILE:DEST`` command.

        Description:
            - This command sets or queries the location where files are saved when
              ``SAVEON:TRIGGER`` is ON and ``SAVEON:WAVEFORM`` is ON. You can save the files to a
              local drive or network path by entering the desired location in <QString>. You can
              also select to save the files to a USB drive.

        Usage:
            - Using the ``.query()`` method will send the ``SAVEON:FILE:DEST?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEON:FILE:DEST?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVEON:FILE:DEST value`` command.

        SCPI Syntax:
            ```
            - SAVEON:FILE:DEST <QString>
            - SAVEON:FILE:DEST?
            ```

        Info:
            - ``<QString>`` specifies the location to store files.
        """
        return self._dest

    @property
    def name(self) -> SaveonFileName:
        """Return the ``SAVEON:FILE:NAME`` command.

        Description:
            - Sets or queries the file name to use when ``SAVEON:TRIGer`` is ON.

        Usage:
            - Using the ``.query()`` method will send the ``SAVEON:FILE:NAME?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEON:FILE:NAME?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVEON:FILE:NAME value`` command.

        SCPI Syntax:
            ```
            - SAVEON:FILE:NAME <QString>
            - SAVEON:FILE:NAME?
            ```

        Info:
            - ``<QString>`` is the file name you want to use.
        """
        return self._name


class Saveon(SCPICmdRead):
    """The ``SAVEON`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SAVEON?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEON?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.file``: The ``SAVEON:FILE`` command tree.
        - ``.image``: The ``SAVEON:IMAGe`` command.
        - ``.trigger``: The ``SAVEON:TRIGger`` command.
        - ``.waveform``: The ``SAVEON:WAVEform`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SAVEON") -> None:
        super().__init__(device, cmd_syntax)
        self._file = SaveonFile(device, f"{self._cmd_syntax}:FILE")
        self._image = SaveonImage(device, f"{self._cmd_syntax}:IMAGe")
        self._trigger = SaveonTrigger(device, f"{self._cmd_syntax}:TRIGger")
        self._waveform = SaveonWaveform(device, f"{self._cmd_syntax}:WAVEform")

    @property
    def file(self) -> SaveonFile:
        """Return the ``SAVEON:FILE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SAVEON:FILE?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEON:FILE?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.dest``: The ``SAVEON:FILE:DEST`` command.
            - ``.name``: The ``SAVEON:FILE:NAME`` command.
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

        Sub-properties:
            - ``.fileformat``: The ``SAVEON:IMAGe:FILEFormat`` command.
        """
        return self._image

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

        Sub-properties:
            - ``.fileformat``: The ``SAVEON:WAVEform:FILEFormat`` command.
            - ``.source``: The ``SAVEON:WAVEform:SOURce`` command.
        """
        return self._waveform
