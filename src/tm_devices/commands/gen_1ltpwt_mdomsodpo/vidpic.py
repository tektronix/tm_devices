"""The vidpic commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - VIDPic:AUTOContrast {0|1|OFF|ON}
    - VIDPic:AUTOContrast:UPDATERate <NR1>
    - VIDPic:AUTOContrast:UPDATERate?
    - VIDPic:AUTOContrast?
    - VIDPic:BRIGHTNess <NR1>
    - VIDPic:BRIGHTNess?
    - VIDPic:CONTRast <NR1>
    - VIDPic:CONTRast?
    - VIDPic:DISplay {0|1|OFF|ON}
    - VIDPic:DISplay?
    - VIDPic:FRAMETYPe {ODD|EVEN|INTERLAced}
    - VIDPic:FRAMETYPe?
    - VIDPic:LOCation:HEIght <NR1>
    - VIDPic:LOCation:HEIght?
    - VIDPic:LOCation:OFFSet <NR3>
    - VIDPic:LOCation:OFFSet?
    - VIDPic:LOCation:STARt:LINE <NR1>
    - VIDPic:LOCation:STARt:LINE?
    - VIDPic:LOCation:STARt:PIXel <NR1>
    - VIDPic:LOCation:STARt:PIXel?
    - VIDPic:LOCation:WIDth <NR1>
    - VIDPic:LOCation:WIDth?
    - VIDPic:LOCation:X <NR1>
    - VIDPic:LOCation:X?
    - VIDPic:LOCation:Y <NR1>
    - VIDPic:LOCation:Y?
    - VIDPic:SOUrce {CH<x>}
    - VIDPic:SOUrce?
    - VIDPic:STANdard {NTSC|PAL}
    - VIDPic:STANdard?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class VidpicStandard(SCPICmdWrite, SCPICmdRead):
    """The ``VIDPic:STANdard`` command.

    Description:
        - Sets (or queries) which video picture standard to use (either NTSC or PAL).

    Usage:
        - Using the ``.query()`` method will send the ``VIDPic:STANdard?`` query.
        - Using the ``.verify(value)`` method will send the ``VIDPic:STANdard?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VIDPic:STANdard value`` command.

    SCPI Syntax:
        ```
        - VIDPic:STANdard {NTSC|PAL}
        - VIDPic:STANdard?
        ```

    Info:
        - ``NTSC`` sets the video picture standard to NTSC (National Television Systems Committee).
        - ``PAL`` sets the video picture standard to PAL (Phase Alternation Line).
    """


class VidpicSource(SCPICmdWrite, SCPICmdRead):
    """The ``VIDPic:SOUrce`` command.

    Description:
        - Sets (or queries) the channel to use for the video picture source waveform.

    Usage:
        - Using the ``.query()`` method will send the ``VIDPic:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``VIDPic:SOUrce?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VIDPic:SOUrce value`` command.

    SCPI Syntax:
        ```
        - VIDPic:SOUrce {CH<x>}
        - VIDPic:SOUrce?
        ```

    Info:
        - ``CH<x>`` specify which channel to use for the video picture source waveform.
    """


class VidpicLocationY(SCPICmdWrite, SCPICmdRead):
    """The ``VIDPic:LOCation:Y`` command.

    Description:
        - Sets (or queries) the video picture Y origin location, in rows.

    Usage:
        - Using the ``.query()`` method will send the ``VIDPic:LOCation:Y?`` query.
        - Using the ``.verify(value)`` method will send the ``VIDPic:LOCation:Y?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VIDPic:LOCation:Y value`` command.

    SCPI Syntax:
        ```
        - VIDPic:LOCation:Y <NR1>
        - VIDPic:LOCation:Y?
        ```
    """


class VidpicLocationX(SCPICmdWrite, SCPICmdRead):
    """The ``VIDPic:LOCation:X`` command.

    Description:
        - Sets (or queries) the video picture X origin location, in columns.

    Usage:
        - Using the ``.query()`` method will send the ``VIDPic:LOCation:X?`` query.
        - Using the ``.verify(value)`` method will send the ``VIDPic:LOCation:X?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VIDPic:LOCation:X value`` command.

    SCPI Syntax:
        ```
        - VIDPic:LOCation:X <NR1>
        - VIDPic:LOCation:X?
        ```
    """


class VidpicLocationWidth(SCPICmdWrite, SCPICmdRead):
    """The ``VIDPic:LOCation:WIDth`` command.

    Description:
        - Sets (or queries) the video picture width, in columns.

    Usage:
        - Using the ``.query()`` method will send the ``VIDPic:LOCation:WIDth?`` query.
        - Using the ``.verify(value)`` method will send the ``VIDPic:LOCation:WIDth?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VIDPic:LOCation:WIDth value`` command.

    SCPI Syntax:
        ```
        - VIDPic:LOCation:WIDth <NR1>
        - VIDPic:LOCation:WIDth?
        ```
    """


class VidpicLocationStartPixel(SCPICmdWrite, SCPICmdRead):
    """The ``VIDPic:LOCation:STARt:PIXel`` command.

    Description:
        - Sets (or queries) the video picture starting pixel in each line The range for this value
          varies with the instrument screen geometry. Each video line is an analog signal of
          nominally 63.5us duration (10.9us blanking + 52.6us active video) that can be sampled from
          1MS/s to 100MS/s, giving from 52.6 to 5260 video samples or 'pixels' per output line. The
          start pixel is the starting sample in each line; it is limited to a single line at the
          current sample rate, i.e. ranges between -10.9 to 52.6 and -1090 to +5260.

    Usage:
        - Using the ``.query()`` method will send the ``VIDPic:LOCation:STARt:PIXel?`` query.
        - Using the ``.verify(value)`` method will send the ``VIDPic:LOCation:STARt:PIXel?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VIDPic:LOCation:STARt:PIXel value``
          command.

    SCPI Syntax:
        ```
        - VIDPic:LOCation:STARt:PIXel <NR1>
        - VIDPic:LOCation:STARt:PIXel?
        ```
    """


class VidpicLocationStartLine(SCPICmdWrite, SCPICmdRead):
    """The ``VIDPic:LOCation:STARt:LINE`` command.

    Description:
        - Sets (or queries) the video picture starting line number.

    Usage:
        - Using the ``.query()`` method will send the ``VIDPic:LOCation:STARt:LINE?`` query.
        - Using the ``.verify(value)`` method will send the ``VIDPic:LOCation:STARt:LINE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VIDPic:LOCation:STARt:LINE value``
          command.

    SCPI Syntax:
        ```
        - VIDPic:LOCation:STARt:LINE <NR1>
        - VIDPic:LOCation:STARt:LINE?
        ```
    """


class VidpicLocationStart(SCPICmdRead):
    """The ``VIDPic:LOCation:STARt`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``VIDPic:LOCation:STARt?`` query.
        - Using the ``.verify(value)`` method will send the ``VIDPic:LOCation:STARt?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.line``: The ``VIDPic:LOCation:STARt:LINE`` command.
        - ``.pixel``: The ``VIDPic:LOCation:STARt:PIXel`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._line = VidpicLocationStartLine(device, f"{self._cmd_syntax}:LINE")
        self._pixel = VidpicLocationStartPixel(device, f"{self._cmd_syntax}:PIXel")

    @property
    def line(self) -> VidpicLocationStartLine:
        """Return the ``VIDPic:LOCation:STARt:LINE`` command.

        Description:
            - Sets (or queries) the video picture starting line number.

        Usage:
            - Using the ``.query()`` method will send the ``VIDPic:LOCation:STARt:LINE?`` query.
            - Using the ``.verify(value)`` method will send the ``VIDPic:LOCation:STARt:LINE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VIDPic:LOCation:STARt:LINE value``
              command.

        SCPI Syntax:
            ```
            - VIDPic:LOCation:STARt:LINE <NR1>
            - VIDPic:LOCation:STARt:LINE?
            ```
        """
        return self._line

    @property
    def pixel(self) -> VidpicLocationStartPixel:
        """Return the ``VIDPic:LOCation:STARt:PIXel`` command.

        Description:
            - Sets (or queries) the video picture starting pixel in each line The range for this
              value varies with the instrument screen geometry. Each video line is an analog signal
              of nominally 63.5us duration (10.9us blanking + 52.6us active video) that can be
              sampled from 1MS/s to 100MS/s, giving from 52.6 to 5260 video samples or 'pixels' per
              output line. The start pixel is the starting sample in each line; it is limited to a
              single line at the current sample rate, i.e. ranges between -10.9 to 52.6 and -1090 to
              +5260.

        Usage:
            - Using the ``.query()`` method will send the ``VIDPic:LOCation:STARt:PIXel?`` query.
            - Using the ``.verify(value)`` method will send the ``VIDPic:LOCation:STARt:PIXel?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VIDPic:LOCation:STARt:PIXel value``
              command.

        SCPI Syntax:
            ```
            - VIDPic:LOCation:STARt:PIXel <NR1>
            - VIDPic:LOCation:STARt:PIXel?
            ```
        """
        return self._pixel


class VidpicLocationOffset(SCPICmdWrite, SCPICmdRead):
    """The ``VIDPic:LOCation:OFFSet`` command.

    Description:
        - Sets (or queries) the video picture line-to-line offset. This is the amount of additional
          delay time to add between lines of the video picture.

    Usage:
        - Using the ``.query()`` method will send the ``VIDPic:LOCation:OFFSet?`` query.
        - Using the ``.verify(value)`` method will send the ``VIDPic:LOCation:OFFSet?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VIDPic:LOCation:OFFSet value`` command.

    SCPI Syntax:
        ```
        - VIDPic:LOCation:OFFSet <NR3>
        - VIDPic:LOCation:OFFSet?
        ```
    """


class VidpicLocationHeight(SCPICmdWrite, SCPICmdRead):
    """The ``VIDPic:LOCation:HEIght`` command.

    Description:
        - Sets (or queries) the video picture height, in rows.

    Usage:
        - Using the ``.query()`` method will send the ``VIDPic:LOCation:HEIght?`` query.
        - Using the ``.verify(value)`` method will send the ``VIDPic:LOCation:HEIght?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VIDPic:LOCation:HEIght value`` command.

    SCPI Syntax:
        ```
        - VIDPic:LOCation:HEIght <NR1>
        - VIDPic:LOCation:HEIght?
        ```
    """


class VidpicLocation(SCPICmdRead):
    """The ``VIDPic:LOCation`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``VIDPic:LOCation?`` query.
        - Using the ``.verify(value)`` method will send the ``VIDPic:LOCation?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.height``: The ``VIDPic:LOCation:HEIght`` command.
        - ``.offset``: The ``VIDPic:LOCation:OFFSet`` command.
        - ``.start``: The ``VIDPic:LOCation:STARt`` command tree.
        - ``.width``: The ``VIDPic:LOCation:WIDth`` command.
        - ``.x``: The ``VIDPic:LOCation:X`` command.
        - ``.y``: The ``VIDPic:LOCation:Y`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._height = VidpicLocationHeight(device, f"{self._cmd_syntax}:HEIght")
        self._offset = VidpicLocationOffset(device, f"{self._cmd_syntax}:OFFSet")
        self._start = VidpicLocationStart(device, f"{self._cmd_syntax}:STARt")
        self._width = VidpicLocationWidth(device, f"{self._cmd_syntax}:WIDth")
        self._x = VidpicLocationX(device, f"{self._cmd_syntax}:X")
        self._y = VidpicLocationY(device, f"{self._cmd_syntax}:Y")

    @property
    def height(self) -> VidpicLocationHeight:
        """Return the ``VIDPic:LOCation:HEIght`` command.

        Description:
            - Sets (or queries) the video picture height, in rows.

        Usage:
            - Using the ``.query()`` method will send the ``VIDPic:LOCation:HEIght?`` query.
            - Using the ``.verify(value)`` method will send the ``VIDPic:LOCation:HEIght?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VIDPic:LOCation:HEIght value``
              command.

        SCPI Syntax:
            ```
            - VIDPic:LOCation:HEIght <NR1>
            - VIDPic:LOCation:HEIght?
            ```
        """
        return self._height

    @property
    def offset(self) -> VidpicLocationOffset:
        """Return the ``VIDPic:LOCation:OFFSet`` command.

        Description:
            - Sets (or queries) the video picture line-to-line offset. This is the amount of
              additional delay time to add between lines of the video picture.

        Usage:
            - Using the ``.query()`` method will send the ``VIDPic:LOCation:OFFSet?`` query.
            - Using the ``.verify(value)`` method will send the ``VIDPic:LOCation:OFFSet?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VIDPic:LOCation:OFFSet value``
              command.

        SCPI Syntax:
            ```
            - VIDPic:LOCation:OFFSet <NR3>
            - VIDPic:LOCation:OFFSet?
            ```
        """
        return self._offset

    @property
    def start(self) -> VidpicLocationStart:
        """Return the ``VIDPic:LOCation:STARt`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``VIDPic:LOCation:STARt?`` query.
            - Using the ``.verify(value)`` method will send the ``VIDPic:LOCation:STARt?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.line``: The ``VIDPic:LOCation:STARt:LINE`` command.
            - ``.pixel``: The ``VIDPic:LOCation:STARt:PIXel`` command.
        """
        return self._start

    @property
    def width(self) -> VidpicLocationWidth:
        """Return the ``VIDPic:LOCation:WIDth`` command.

        Description:
            - Sets (or queries) the video picture width, in columns.

        Usage:
            - Using the ``.query()`` method will send the ``VIDPic:LOCation:WIDth?`` query.
            - Using the ``.verify(value)`` method will send the ``VIDPic:LOCation:WIDth?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VIDPic:LOCation:WIDth value``
              command.

        SCPI Syntax:
            ```
            - VIDPic:LOCation:WIDth <NR1>
            - VIDPic:LOCation:WIDth?
            ```
        """
        return self._width

    @property
    def x(self) -> VidpicLocationX:
        """Return the ``VIDPic:LOCation:X`` command.

        Description:
            - Sets (or queries) the video picture X origin location, in columns.

        Usage:
            - Using the ``.query()`` method will send the ``VIDPic:LOCation:X?`` query.
            - Using the ``.verify(value)`` method will send the ``VIDPic:LOCation:X?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VIDPic:LOCation:X value`` command.

        SCPI Syntax:
            ```
            - VIDPic:LOCation:X <NR1>
            - VIDPic:LOCation:X?
            ```
        """
        return self._x

    @property
    def y(self) -> VidpicLocationY:
        """Return the ``VIDPic:LOCation:Y`` command.

        Description:
            - Sets (or queries) the video picture Y origin location, in rows.

        Usage:
            - Using the ``.query()`` method will send the ``VIDPic:LOCation:Y?`` query.
            - Using the ``.verify(value)`` method will send the ``VIDPic:LOCation:Y?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VIDPic:LOCation:Y value`` command.

        SCPI Syntax:
            ```
            - VIDPic:LOCation:Y <NR1>
            - VIDPic:LOCation:Y?
            ```
        """
        return self._y


class VidpicFrametype(SCPICmdWrite, SCPICmdRead):
    """The ``VIDPic:FRAMETYPe`` command.

    Description:
        - Sets (or queries) the video picture frame type (ODD, EVEN or INTERLAced). Interlaced
          frames combine successive odd and even frames by displaying alternating lines from each.
          The resulting image has twice as many rows, which changes its aspect ratio.

    Usage:
        - Using the ``.query()`` method will send the ``VIDPic:FRAMETYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``VIDPic:FRAMETYPe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VIDPic:FRAMETYPe value`` command.

    SCPI Syntax:
        ```
        - VIDPic:FRAMETYPe {ODD|EVEN|INTERLAced}
        - VIDPic:FRAMETYPe?
        ```

    Info:
        - ``ODD`` sets the frame type to Odd.
        - ``EVEN`` sets the frame type to Even.
        - ``INTERLAced`` sets the frame type to Interlaced.
    """


class VidpicDisplay(SCPICmdWrite, SCPICmdRead):
    """The ``VIDPic:DISplay`` command.

    Description:
        - Sets (or queries) the video picture display state.

    Usage:
        - Using the ``.query()`` method will send the ``VIDPic:DISplay?`` query.
        - Using the ``.verify(value)`` method will send the ``VIDPic:DISplay?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VIDPic:DISplay value`` command.

    SCPI Syntax:
        ```
        - VIDPic:DISplay {0|1|OFF|ON}
        - VIDPic:DISplay?
        ```

    Info:
        - ``1`` or ON turns on the video picture display feature.
        - ``0`` or OFF turns it off.
    """


class VidpicContrast(SCPICmdWrite, SCPICmdRead):
    """The ``VIDPic:CONTRast`` command.

    Description:
        - Sets (or queries) the video picture contrast level as an integer percentage.

    Usage:
        - Using the ``.query()`` method will send the ``VIDPic:CONTRast?`` query.
        - Using the ``.verify(value)`` method will send the ``VIDPic:CONTRast?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VIDPic:CONTRast value`` command.

    SCPI Syntax:
        ```
        - VIDPic:CONTRast <NR1>
        - VIDPic:CONTRast?
        ```
    """


class VidpicBrightness(SCPICmdWrite, SCPICmdRead):
    """The ``VIDPic:BRIGHTNess`` command.

    Description:
        - Sets (or queries) the video picture brightness level as an integer percentage.

    Usage:
        - Using the ``.query()`` method will send the ``VIDPic:BRIGHTNess?`` query.
        - Using the ``.verify(value)`` method will send the ``VIDPic:BRIGHTNess?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VIDPic:BRIGHTNess value`` command.

    SCPI Syntax:
        ```
        - VIDPic:BRIGHTNess <NR1>
        - VIDPic:BRIGHTNess?
        ```
    """


class VidpicAutocontrastUpdaterate(SCPICmdWrite, SCPICmdRead):
    """The ``VIDPic:AUTOContrast:UPDATERate`` command.

    Description:
        - Sets (or queries) the number of frames between automatic contrast updates.

    Usage:
        - Using the ``.query()`` method will send the ``VIDPic:AUTOContrast:UPDATERate?`` query.
        - Using the ``.verify(value)`` method will send the ``VIDPic:AUTOContrast:UPDATERate?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VIDPic:AUTOContrast:UPDATERate value``
          command.

    SCPI Syntax:
        ```
        - VIDPic:AUTOContrast:UPDATERate <NR1>
        - VIDPic:AUTOContrast:UPDATERate?
        ```
    """


class VidpicAutocontrast(SCPICmdWrite, SCPICmdRead):
    """The ``VIDPic:AUTOContrast`` command.

    Description:
        - Sets (or queries) the video picture automatic contrast state. Automatic contrast uses
          histogram equalization to optimize the use of brightness levels; each brightness level
          occupies approximately the same area in the image.

    Usage:
        - Using the ``.query()`` method will send the ``VIDPic:AUTOContrast?`` query.
        - Using the ``.verify(value)`` method will send the ``VIDPic:AUTOContrast?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VIDPic:AUTOContrast value`` command.

    SCPI Syntax:
        ```
        - VIDPic:AUTOContrast {0|1|OFF|ON}
        - VIDPic:AUTOContrast?
        ```

    Info:
        - ``1`` or ON turns on the auto contrast state for the video picture feature.
        - ``0`` or OFF turns it off.

    Properties:
        - ``.updaterate``: The ``VIDPic:AUTOContrast:UPDATERate`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._updaterate = VidpicAutocontrastUpdaterate(device, f"{self._cmd_syntax}:UPDATERate")

    @property
    def updaterate(self) -> VidpicAutocontrastUpdaterate:
        """Return the ``VIDPic:AUTOContrast:UPDATERate`` command.

        Description:
            - Sets (or queries) the number of frames between automatic contrast updates.

        Usage:
            - Using the ``.query()`` method will send the ``VIDPic:AUTOContrast:UPDATERate?`` query.
            - Using the ``.verify(value)`` method will send the ``VIDPic:AUTOContrast:UPDATERate?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``VIDPic:AUTOContrast:UPDATERate value`` command.

        SCPI Syntax:
            ```
            - VIDPic:AUTOContrast:UPDATERate <NR1>
            - VIDPic:AUTOContrast:UPDATERate?
            ```
        """
        return self._updaterate


#  pylint: disable=too-many-instance-attributes
class Vidpic(SCPICmdRead):
    """The ``VIDPic`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``VIDPic?`` query.
        - Using the ``.verify(value)`` method will send the ``VIDPic?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.autocontrast``: The ``VIDPic:AUTOContrast`` command.
        - ``.brightness``: The ``VIDPic:BRIGHTNess`` command.
        - ``.contrast``: The ``VIDPic:CONTRast`` command.
        - ``.display``: The ``VIDPic:DISplay`` command.
        - ``.frametype``: The ``VIDPic:FRAMETYPe`` command.
        - ``.location``: The ``VIDPic:LOCation`` command tree.
        - ``.source``: The ``VIDPic:SOUrce`` command.
        - ``.standard``: The ``VIDPic:STANdard`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "VIDPic") -> None:
        super().__init__(device, cmd_syntax)
        self._autocontrast = VidpicAutocontrast(device, f"{self._cmd_syntax}:AUTOContrast")
        self._brightness = VidpicBrightness(device, f"{self._cmd_syntax}:BRIGHTNess")
        self._contrast = VidpicContrast(device, f"{self._cmd_syntax}:CONTRast")
        self._display = VidpicDisplay(device, f"{self._cmd_syntax}:DISplay")
        self._frametype = VidpicFrametype(device, f"{self._cmd_syntax}:FRAMETYPe")
        self._location = VidpicLocation(device, f"{self._cmd_syntax}:LOCation")
        self._source = VidpicSource(device, f"{self._cmd_syntax}:SOUrce")
        self._standard = VidpicStandard(device, f"{self._cmd_syntax}:STANdard")

    @property
    def autocontrast(self) -> VidpicAutocontrast:
        """Return the ``VIDPic:AUTOContrast`` command.

        Description:
            - Sets (or queries) the video picture automatic contrast state. Automatic contrast uses
              histogram equalization to optimize the use of brightness levels; each brightness level
              occupies approximately the same area in the image.

        Usage:
            - Using the ``.query()`` method will send the ``VIDPic:AUTOContrast?`` query.
            - Using the ``.verify(value)`` method will send the ``VIDPic:AUTOContrast?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VIDPic:AUTOContrast value``
              command.

        SCPI Syntax:
            ```
            - VIDPic:AUTOContrast {0|1|OFF|ON}
            - VIDPic:AUTOContrast?
            ```

        Info:
            - ``1`` or ON turns on the auto contrast state for the video picture feature.
            - ``0`` or OFF turns it off.

        Sub-properties:
            - ``.updaterate``: The ``VIDPic:AUTOContrast:UPDATERate`` command.
        """
        return self._autocontrast

    @property
    def brightness(self) -> VidpicBrightness:
        """Return the ``VIDPic:BRIGHTNess`` command.

        Description:
            - Sets (or queries) the video picture brightness level as an integer percentage.

        Usage:
            - Using the ``.query()`` method will send the ``VIDPic:BRIGHTNess?`` query.
            - Using the ``.verify(value)`` method will send the ``VIDPic:BRIGHTNess?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VIDPic:BRIGHTNess value`` command.

        SCPI Syntax:
            ```
            - VIDPic:BRIGHTNess <NR1>
            - VIDPic:BRIGHTNess?
            ```
        """
        return self._brightness

    @property
    def contrast(self) -> VidpicContrast:
        """Return the ``VIDPic:CONTRast`` command.

        Description:
            - Sets (or queries) the video picture contrast level as an integer percentage.

        Usage:
            - Using the ``.query()`` method will send the ``VIDPic:CONTRast?`` query.
            - Using the ``.verify(value)`` method will send the ``VIDPic:CONTRast?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VIDPic:CONTRast value`` command.

        SCPI Syntax:
            ```
            - VIDPic:CONTRast <NR1>
            - VIDPic:CONTRast?
            ```
        """
        return self._contrast

    @property
    def display(self) -> VidpicDisplay:
        """Return the ``VIDPic:DISplay`` command.

        Description:
            - Sets (or queries) the video picture display state.

        Usage:
            - Using the ``.query()`` method will send the ``VIDPic:DISplay?`` query.
            - Using the ``.verify(value)`` method will send the ``VIDPic:DISplay?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VIDPic:DISplay value`` command.

        SCPI Syntax:
            ```
            - VIDPic:DISplay {0|1|OFF|ON}
            - VIDPic:DISplay?
            ```

        Info:
            - ``1`` or ON turns on the video picture display feature.
            - ``0`` or OFF turns it off.
        """
        return self._display

    @property
    def frametype(self) -> VidpicFrametype:
        """Return the ``VIDPic:FRAMETYPe`` command.

        Description:
            - Sets (or queries) the video picture frame type (ODD, EVEN or INTERLAced). Interlaced
              frames combine successive odd and even frames by displaying alternating lines from
              each. The resulting image has twice as many rows, which changes its aspect ratio.

        Usage:
            - Using the ``.query()`` method will send the ``VIDPic:FRAMETYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``VIDPic:FRAMETYPe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VIDPic:FRAMETYPe value`` command.

        SCPI Syntax:
            ```
            - VIDPic:FRAMETYPe {ODD|EVEN|INTERLAced}
            - VIDPic:FRAMETYPe?
            ```

        Info:
            - ``ODD`` sets the frame type to Odd.
            - ``EVEN`` sets the frame type to Even.
            - ``INTERLAced`` sets the frame type to Interlaced.
        """
        return self._frametype

    @property
    def location(self) -> VidpicLocation:
        """Return the ``VIDPic:LOCation`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``VIDPic:LOCation?`` query.
            - Using the ``.verify(value)`` method will send the ``VIDPic:LOCation?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.height``: The ``VIDPic:LOCation:HEIght`` command.
            - ``.offset``: The ``VIDPic:LOCation:OFFSet`` command.
            - ``.start``: The ``VIDPic:LOCation:STARt`` command tree.
            - ``.width``: The ``VIDPic:LOCation:WIDth`` command.
            - ``.x``: The ``VIDPic:LOCation:X`` command.
            - ``.y``: The ``VIDPic:LOCation:Y`` command.
        """
        return self._location

    @property
    def source(self) -> VidpicSource:
        """Return the ``VIDPic:SOUrce`` command.

        Description:
            - Sets (or queries) the channel to use for the video picture source waveform.

        Usage:
            - Using the ``.query()`` method will send the ``VIDPic:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``VIDPic:SOUrce?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VIDPic:SOUrce value`` command.

        SCPI Syntax:
            ```
            - VIDPic:SOUrce {CH<x>}
            - VIDPic:SOUrce?
            ```

        Info:
            - ``CH<x>`` specify which channel to use for the video picture source waveform.
        """
        return self._source

    @property
    def standard(self) -> VidpicStandard:
        """Return the ``VIDPic:STANdard`` command.

        Description:
            - Sets (or queries) which video picture standard to use (either NTSC or PAL).

        Usage:
            - Using the ``.query()`` method will send the ``VIDPic:STANdard?`` query.
            - Using the ``.verify(value)`` method will send the ``VIDPic:STANdard?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VIDPic:STANdard value`` command.

        SCPI Syntax:
            ```
            - VIDPic:STANdard {NTSC|PAL}
            - VIDPic:STANdard?
            ```

        Info:
            - ``NTSC`` sets the video picture standard to NTSC (National Television Systems
              Committee).
            - ``PAL`` sets the video picture standard to PAL (Phase Alternation Line).
        """
        return self._standard
