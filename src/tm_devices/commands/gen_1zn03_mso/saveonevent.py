"""The saveonevent commands module.

These commands are used in the following models:
MSO2

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SAVEONEVent:FILEDest <Qstring>
    - SAVEONEVent:FILEDest?
    - SAVEONEVent:FILEName <QString>
    - SAVEONEVent:FILEName?
    - SAVEONEVent:IMAGe:FILEFormat {PNG|BMP|JPG}
    - SAVEONEVent:IMAGe:FILEFormat?
    - SAVEONEVent:WAVEform:FILEFormat {INTERNal|SPREADSheet|MATlab}
    - SAVEONEVent:WAVEform:FILEFormat?
    - SAVEONEVent:WAVEform:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|ALL}
    - SAVEONEVent:WAVEform:SOUrce?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class SaveoneventWaveformSource(SCPICmdWrite, SCPICmdRead):
    """The ``SAVEONEVent:WAVEform:SOUrce`` command.

    Description:
        - This command sets or returns the sources for saving waveforms when an event occurs. This
          command replaces ``SAVEON:WAVEFORM:SOURCE`` (still valid command, but only an alias for
          this new command).

    Usage:
        - Using the ``.query()`` method will send the ``SAVEONEVent:WAVEform:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEONEVent:WAVEform:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVEONEVent:WAVEform:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - SAVEONEVent:WAVEform:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|ALL}
        - SAVEONEVent:WAVEform:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the source waveform for saving.
        - ``DCH<x>_D<x>`` specifies a digital channel to use as the save on source. The supported
          digital channel value is 1. The supported digital bit values are 0 to 15 or DALL (all
          digital channels).
        - ``Math<x>`` specifies a math waveform as the source waveform for saving.
        - ``REF<x>`` specifies a reference waveform as the source waveform for saving.
        - ``ALL`` specifies all analog, math, digital, and reference waveforms as the source
          waveforms for saving.
    """


class SaveoneventWaveformFileformat(SCPICmdWrite, SCPICmdRead):
    """The ``SAVEONEVent:WAVEform:FILEFormat`` command.

    Description:
        - This command sets or returns the file extension (csv, wfm, mat). This command replaces
          ``SAVEON:WAVEFORM:FILEFORMAT`` (still valid command, but only an alias for this new
          command).

    Usage:
        - Using the ``.query()`` method will send the ``SAVEONEVent:WAVEform:FILEFormat?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEONEVent:WAVEform:FILEFormat?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVEONEVent:WAVEform:FILEFormat value``
          command.

    SCPI Syntax:
        ```
        - SAVEONEVent:WAVEform:FILEFormat {INTERNal|SPREADSheet|MATlab}
        - SAVEONEVent:WAVEform:FILEFormat?
        ```

    Info:
        - ``INTERNal`` specifies saving the waveform in the instrument internal format.
        - ``SPREADSheet`` specifies saving the waveform in comma separated values format.
        - ``MATlab`` specifies saving the waveform in matlab compatible file format.
    """


class SaveoneventWaveform(SCPICmdRead):
    """The ``SAVEONEVent:WAVEform`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SAVEONEVent:WAVEform?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEONEVent:WAVEform?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.fileformat``: The ``SAVEONEVent:WAVEform:FILEFormat`` command.
        - ``.source``: The ``SAVEONEVent:WAVEform:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fileformat = SaveoneventWaveformFileformat(device, f"{self._cmd_syntax}:FILEFormat")
        self._source = SaveoneventWaveformSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def fileformat(self) -> SaveoneventWaveformFileformat:
        """Return the ``SAVEONEVent:WAVEform:FILEFormat`` command.

        Description:
            - This command sets or returns the file extension (csv, wfm, mat). This command replaces
              ``SAVEON:WAVEFORM:FILEFORMAT`` (still valid command, but only an alias for this new
              command).

        Usage:
            - Using the ``.query()`` method will send the ``SAVEONEVent:WAVEform:FILEFormat?``
              query.
            - Using the ``.verify(value)`` method will send the ``SAVEONEVent:WAVEform:FILEFormat?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SAVEONEVent:WAVEform:FILEFormat value`` command.

        SCPI Syntax:
            ```
            - SAVEONEVent:WAVEform:FILEFormat {INTERNal|SPREADSheet|MATlab}
            - SAVEONEVent:WAVEform:FILEFormat?
            ```

        Info:
            - ``INTERNal`` specifies saving the waveform in the instrument internal format.
            - ``SPREADSheet`` specifies saving the waveform in comma separated values format.
            - ``MATlab`` specifies saving the waveform in matlab compatible file format.
        """
        return self._fileformat

    @property
    def source(self) -> SaveoneventWaveformSource:
        """Return the ``SAVEONEVent:WAVEform:SOUrce`` command.

        Description:
            - This command sets or returns the sources for saving waveforms when an event occurs.
              This command replaces ``SAVEON:WAVEFORM:SOURCE`` (still valid command, but only an
              alias for this new command).

        Usage:
            - Using the ``.query()`` method will send the ``SAVEONEVent:WAVEform:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEONEVent:WAVEform:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVEONEVent:WAVEform:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - SAVEONEVent:WAVEform:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|ALL}
            - SAVEONEVent:WAVEform:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the source waveform for saving.
            - ``DCH<x>_D<x>`` specifies a digital channel to use as the save on source. The
              supported digital channel value is 1. The supported digital bit values are 0 to 15 or
              DALL (all digital channels).
            - ``Math<x>`` specifies a math waveform as the source waveform for saving.
            - ``REF<x>`` specifies a reference waveform as the source waveform for saving.
            - ``ALL`` specifies all analog, math, digital, and reference waveforms as the source
              waveforms for saving.
        """
        return self._source


class SaveoneventImageFileformat(SCPICmdWrite, SCPICmdRead):
    """The ``SAVEONEVent:IMAGe:FILEFormat`` command.

    Description:
        - This command sets or returns the image file extension (png, jpg, bmp). This command
          replaces ``SAVEON:IMAGE:FILEFORMAT`` (still valid command, but only an alias for this new
          command).

    Usage:
        - Using the ``.query()`` method will send the ``SAVEONEVent:IMAGe:FILEFormat?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEONEVent:IMAGe:FILEFormat?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVEONEVent:IMAGe:FILEFormat value``
          command.

    SCPI Syntax:
        ```
        - SAVEONEVent:IMAGe:FILEFormat {PNG|BMP|JPG}
        - SAVEONEVent:IMAGe:FILEFormat?
        ```

    Info:
        - ``PNG`` specifies using PNG format for saved image files.
        - ``BMP`` specifies using BMP format for saved image files.
        - ``JPG`` specifies using JPEG format for saved image files.
    """


class SaveoneventImage(SCPICmdRead):
    """The ``SAVEONEVent:IMAGe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SAVEONEVent:IMAGe?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEONEVent:IMAGe?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.fileformat``: The ``SAVEONEVent:IMAGe:FILEFormat`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fileformat = SaveoneventImageFileformat(device, f"{self._cmd_syntax}:FILEFormat")

    @property
    def fileformat(self) -> SaveoneventImageFileformat:
        """Return the ``SAVEONEVent:IMAGe:FILEFormat`` command.

        Description:
            - This command sets or returns the image file extension (png, jpg, bmp). This command
              replaces ``SAVEON:IMAGE:FILEFORMAT`` (still valid command, but only an alias for this
              new command).

        Usage:
            - Using the ``.query()`` method will send the ``SAVEONEVent:IMAGe:FILEFormat?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEONEVent:IMAGe:FILEFormat?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SAVEONEVent:IMAGe:FILEFormat value`` command.

        SCPI Syntax:
            ```
            - SAVEONEVent:IMAGe:FILEFormat {PNG|BMP|JPG}
            - SAVEONEVent:IMAGe:FILEFormat?
            ```

        Info:
            - ``PNG`` specifies using PNG format for saved image files.
            - ``BMP`` specifies using BMP format for saved image files.
            - ``JPG`` specifies using JPEG format for saved image files.
        """
        return self._fileformat


class SaveoneventFilename(SCPICmdWrite, SCPICmdRead):
    """The ``SAVEONEVent:FILEName`` command.

    Description:
        - This command sets or queries the file name without the extension. This command replaces
          ``SAVEON:FILE:NAME`` (still valid command, but only an alias for this new command).

    Usage:
        - Using the ``.query()`` method will send the ``SAVEONEVent:FILEName?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEONEVent:FILEName?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVEONEVent:FILEName value`` command.

    SCPI Syntax:
        ```
        - SAVEONEVent:FILEName <QString>
        - SAVEONEVent:FILEName?
        ```

    Info:
        - ``<QString>`` specifies the name of the file.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SaveoneventFiledest(SCPICmdWrite, SCPICmdRead):
    """The ``SAVEONEVent:FILEDest`` command.

    Description:
        - This command sets or queries the location where files are saved. This command replaces
          ``SAVEON:FILE:DEST`` (still valid command, but only an alias for this new command).

    Usage:
        - Using the ``.query()`` method will send the ``SAVEONEVent:FILEDest?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEONEVent:FILEDest?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SAVEONEVent:FILEDest value`` command.

    SCPI Syntax:
        ```
        - SAVEONEVent:FILEDest <Qstring>
        - SAVEONEVent:FILEDest?
        ```

    Info:
        - ``<QString>`` specifies the location to store files.
    """


class Saveonevent(SCPICmdRead):
    """The ``SAVEONEVent`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SAVEONEVent?`` query.
        - Using the ``.verify(value)`` method will send the ``SAVEONEVent?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.filedest``: The ``SAVEONEVent:FILEDest`` command.
        - ``.filename``: The ``SAVEONEVent:FILEName`` command.
        - ``.image``: The ``SAVEONEVent:IMAGe`` command tree.
        - ``.waveform``: The ``SAVEONEVent:WAVEform`` command tree.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "SAVEONEVent"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._filedest = SaveoneventFiledest(device, f"{self._cmd_syntax}:FILEDest")
        self._filename = SaveoneventFilename(device, f"{self._cmd_syntax}:FILEName")
        self._image = SaveoneventImage(device, f"{self._cmd_syntax}:IMAGe")
        self._waveform = SaveoneventWaveform(device, f"{self._cmd_syntax}:WAVEform")

    @property
    def filedest(self) -> SaveoneventFiledest:
        """Return the ``SAVEONEVent:FILEDest`` command.

        Description:
            - This command sets or queries the location where files are saved. This command replaces
              ``SAVEON:FILE:DEST`` (still valid command, but only an alias for this new command).

        Usage:
            - Using the ``.query()`` method will send the ``SAVEONEVent:FILEDest?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEONEVent:FILEDest?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVEONEVent:FILEDest value``
              command.

        SCPI Syntax:
            ```
            - SAVEONEVent:FILEDest <Qstring>
            - SAVEONEVent:FILEDest?
            ```

        Info:
            - ``<QString>`` specifies the location to store files.
        """
        return self._filedest

    @property
    def filename(self) -> SaveoneventFilename:
        """Return the ``SAVEONEVent:FILEName`` command.

        Description:
            - This command sets or queries the file name without the extension. This command
              replaces ``SAVEON:FILE:NAME`` (still valid command, but only an alias for this new
              command).

        Usage:
            - Using the ``.query()`` method will send the ``SAVEONEVent:FILEName?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEONEVent:FILEName?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SAVEONEVent:FILEName value``
              command.

        SCPI Syntax:
            ```
            - SAVEONEVent:FILEName <QString>
            - SAVEONEVent:FILEName?
            ```

        Info:
            - ``<QString>`` specifies the name of the file.
        """
        return self._filename

    @property
    def image(self) -> SaveoneventImage:
        """Return the ``SAVEONEVent:IMAGe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SAVEONEVent:IMAGe?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEONEVent:IMAGe?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.fileformat``: The ``SAVEONEVent:IMAGe:FILEFormat`` command.
        """
        return self._image

    @property
    def waveform(self) -> SaveoneventWaveform:
        """Return the ``SAVEONEVent:WAVEform`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SAVEONEVent:WAVEform?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEONEVent:WAVEform?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.fileformat``: The ``SAVEONEVent:WAVEform:FILEFormat`` command.
            - ``.source``: The ``SAVEONEVent:WAVEform:SOUrce`` command.
        """
        return self._waveform
