# pylint: disable=line-too-long
"""The display commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - DISplay:CLOCk {ON|OFF|<NR1>}
    - DISplay:CLOCk?
    - DISplay:COLOr:MATHCOLOr {DEFAULT|INHERIT}
    - DISplay:COLOr:MATHCOLOr?
    - DISplay:COLOr:PALEtte:IMAGEView {NORMal|MONOGREEN|MONOGRAY|TEMPErature|SPECTral|USEr}
    - DISplay:COLOr:PALEtte:IMAGEView?
    - DISplay:COLOr:PALEtte:RECORDView {NORMal|MONOGREEN|MONOGRAY|TEMPErature|SPECTral|USEr}
    - DISplay:COLOr:PALEtte:RECORDView?
    - DISplay:COLOr:PALEtte:USEr RESET
    - DISplay:COLOr:PALEtte:USEr:CARet <NR1>,<NR1>,<NR1>
    - DISplay:COLOr:PALEtte:USEr:CARet?
    - DISplay:COLOr:PALEtte:USEr:CH<x> <NR1>,<NR1>,<NR1>
    - DISplay:COLOr:PALEtte:USEr:CH<x>?
    - DISplay:COLOr:PALEtte:USEr:GRAticule <NR1>,<NR1>,<NR1>
    - DISplay:COLOr:PALEtte:USEr:GRAticule?
    - DISplay:COLOr:PALEtte:USEr:HIStogram <NR1>,<NR1>,<NR1>
    - DISplay:COLOr:PALEtte:USEr:HIStogram?
    - DISplay:COLOr:PALEtte:USEr:MASK <NR1>,<NR1>,<NR1>
    - DISplay:COLOr:PALEtte:USEr:MASK?
    - DISplay:COLOr:PALEtte:USEr:MASKHighlight <NR1>,<NR1>,<NR1>
    - DISplay:COLOr:PALEtte:USEr:MASKHighlight?
    - DISplay:COLOr:PALEtte:USEr:MATH<x> <NR1>,<NR1>,<NR1>
    - DISplay:COLOr:PALEtte:USEr:MATH<x>?
    - DISplay:COLOr:PALEtte:USEr:REF<x> <NR1>,<NR1>,<NR1>
    - DISplay:COLOr:PALEtte:USEr:REF<x>?
    - DISplay:COLOr:PALEtte:USEr:WAVEform {HLS|SPECTral|TEMPErature}
    - DISplay:COLOr:PALEtte:USEr:WAVEform?
    - DISplay:COLOr:PALEtte:USEr?
    - DISplay:COLOr:REFCOLOr {DEFAULT|INHERIT}
    - DISplay:COLOr:REFCOLOr?
    - DISplay:COLOr?
    - DISplay:DATa? (BMP| JPEG| PNG | TIFF)[,(FULLSCREEN | GRAticule | FULLNOmenu)[,(COLOr | INKSaver | BLACKANDWhite )]]
    - DISplay:DESKew {<NR1>|OFF|ON|AUTO}
    - DISplay:DESKew?
    - DISplay:DIGital:HEIght {SMAll|LARge|MEDium|XSMAll}
    - DISplay:DIGital:HEIght?
    - DISplay:DPOJETPlot? (PLOT1 | PLOT2 | PLOT3 | PLOT4 | SUMMARY)[,(JPEG | JPG | TIF | TIFF | BMP | EMF | PNG)]
    - DISplay:FILTer {LINEAr|SINX}
    - DISplay:FILTer?
    - DISplay:FORMat {YT|XY|XYZ}
    - DISplay:FORMat?
    - DISplay:GRAticule {CROSSHair|FRAme|FULl|GRId|IRE|NTSC|MV|PAL}
    - DISplay:GRAticule?
    - DISplay:INTENSITy:AUTOBright {ON|OFF|<NR1>}
    - DISplay:INTENSITy:AUTOBright?
    - DISplay:INTENSITy:BACKLight {LOW|MEDium|HIGH}
    - DISplay:INTENSITy:BACKLight?
    - DISplay:INTENSITy:CUSTOMPct <NRF>
    - DISplay:INTENSITy:CUSTOMPct?
    - DISplay:INTENSITy:SCREENSAVER {ON|OFF|<NR1>}
    - DISplay:INTENSITy:SCREENSAVER?
    - DISplay:INTENSITy:SCREENSAVERDELAY {<NR1>}
    - DISplay:INTENSITy:SCREENSAVERDELAY?
    - DISplay:INTENSITy:WAVEform:IMAGEView <NR2>
    - DISplay:INTENSITy:WAVEform:IMAGEView?
    - DISplay:INTENSITy:WAVEform:RECORDView <NR2>
    - DISplay:INTENSITy:WAVEform:RECORDView?
    - DISplay:INTENSITy?
    - DISplay:PERSistence {OFF|INFPersist|VARpersist}
    - DISplay:PERSistence:RESET
    - DISplay:PERSistence?
    - DISplay:SCREENTExt:LABel<x>:FONTCOlor <QString>
    - DISplay:SCREENTExt:LABel<x>:FONTCOlor?
    - DISplay:SCREENTExt:LABel<x>:FONTEFfect {NONe|CAPS|SHADow|EMBOss|ENGRave}
    - DISplay:SCREENTExt:LABel<x>:FONTEFfect?
    - DISplay:SCREENTExt:LABel<x>:FONTNAme <QString>
    - DISplay:SCREENTExt:LABel<x>:FONTNAme?
    - DISplay:SCREENTExt:LABel<x>:FONTSIze <NR1>
    - DISplay:SCREENTExt:LABel<x>:FONTSIze?
    - DISplay:SCREENTExt:LABel<x>:FONTSTyle <QString>
    - DISplay:SCREENTExt:LABel<x>:FONTSTyle?
    - DISplay:SCREENTExt:LABel<x>:NAMe <QString>
    - DISplay:SCREENTExt:LABel<x>:NAMe?
    - DISplay:SCREENTExt:LABel<x>:STATE {ON|OFF|<NR1>}
    - DISplay:SCREENTExt:LABel<x>:STATE?
    - DISplay:SCREENTExt:LABel<x>:XPOS <NR1>
    - DISplay:SCREENTExt:LABel<x>:YPOS <NR1>
    - DISplay:SCREENTExt:LABel<x>?
    - DISplay:SCREENTExt:STATE {ON|OFF|<NR1>}
    - DISplay:SCREENTExt?
    - DISplay:SHOWREmote {ON|OFF|<NR1>}
    - DISplay:SHOWREmote?
    - DISplay:STYle {DOTs|INTENSIFied|VECtors}
    - DISplay:STYle?
    - DISplay:TRIGBar {OFF|SHORt|LONG}
    - DISplay:TRIGBar?
    - DISplay:TRIGT {ON|OFF|<NR1>}
    - DISplay:TRIGT?
    - DISplay:VARpersist <NR3>
    - DISplay:VARpersist?
    - DISplay:WAVEform {ON|OFF|<NR1>}
    - DISplay:WAVEform?
    - DISplay?
    ```
"""  # noqa: E501

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdReadWithArguments,
    SCPICmdWrite,
    SCPICmdWriteNoArguments,
    ValidatedChannel,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class DisplayWaveform(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEform`` command.

    Description:
        - This command globally enables or disables the waveform display. When disabled, the
          waveform is still acquired and held in memory, but it is not drawn to the screen.
          Disabling the waveform display may improve processing speed.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEform?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEform?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:WAVEform value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEform {ON|OFF|<NR1>}
        - DISplay:WAVEform?
        ```

    Info:
        - ``<NR1>`` enables or disables the waveform display. 0 disables the waveform display; any
          other value enables the waveform display.
        - ``ON`` enables the waveform display.
        - ``OFF`` disables the waveform display.
    """


class DisplayVarpersist(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:VARpersist`` command.

    Description:
        - This command sets or queries display persistence decay time, which is the approximate
          decay time for a freshly struck persistence sample.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:VARpersist?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:VARpersist?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:VARpersist value`` command.

    SCPI Syntax:
        ```
        - DISplay:VARpersist <NR3>
        - DISplay:VARpersist?
        ```

    Info:
        - ``<NR3>`` indicates the persistence decay time and ranges from 0.5 to 100.
    """


class DisplayTrigt(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:TRIGT`` command.

    Description:
        - This command controls or queries the display of the trigger T. The trigger T shows where
          the trigger occurred on the waveform.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:TRIGT?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:TRIGT?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:TRIGT value`` command.

    SCPI Syntax:
        ```
        - DISplay:TRIGT {ON|OFF|<NR1>}
        - DISplay:TRIGT?
        ```

    Info:
        - ``<NR1>`` = 0 disables the trigger T; any other value displays the trigger T.
        - ``OFF`` removes the trigger indicator T from the display.
        - ``ON`` displays a T at the trigger point.
    """


class DisplayTrigbar(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:TRIGBar`` command.

    Description:
        - This command controls or queries the display of the trigger-level indicator bars.
          Indicator bars show where the trigger voltage level is set. The instrument will only
          display the bar if the associated trigger source is also displayed. If both a main and a
          delayed trigger are displayed, then two bars will appear. One will accompany each source.
          If a logic trigger is selected, then multiple bars might appear. One will show the upper
          threshold and one will show the lower threshold. This command is equivalent to selecting
          Display Setup from the Display menu and then choosing the Objects tab.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:TRIGBar?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:TRIGBar?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:TRIGBar value`` command.

    SCPI Syntax:
        ```
        - DISplay:TRIGBar {OFF|SHORt|LONG}
        - DISplay:TRIGBar?
        ```

    Info:
        - ``OFF`` removes the trigger indicator bar from the display.
        - ``SHORt`` displays, as the indicator, a short arrow at the right side of the graticule for
          each displayed trigger signal.
        - ``LONG`` displays, as the indicator, a horizontal line across the width of the graticule
          for each displayed trigger signal.
    """


class DisplayStyle(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:STYle`` command.

    Description:
        - This command sets or queries how the data is displayed for normal and FastAcq modes. This
          command is equivalent to selecting Display Style from the Display menu and choosing a
          style.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:STYle?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:STYle?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:STYle value`` command.

    SCPI Syntax:
        ```
        - DISplay:STYle {DOTs|INTENSIFied|VECtors}
        - DISplay:STYle?
        ```

    Info:
        - ``DOTs`` displays individual data points. New points immediately replace old ones.
        - ``INTENSIFied`` causes the display to show interpolated samples with dark spaces (Only the
          'real' samples are displayed).
        - ``VECtors`` connects adjacent data points. New points immediately replace old ones.
    """


class DisplayShowremote(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:SHOWREmote`` command.

    Description:
        - This command sets or queries the state of the remote display feature and is equivalent to
          selecting Display Remote from the Display menu. The query form of this command returns ON
          (1) or OFF (0). This feature allows you to view waveforms and other graticule data on a
          remote display using remote control software like VNC (Virtual Network Computing) or
          Symantec pcAnywhere.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:SHOWREmote?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:SHOWREmote?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:SHOWREmote value`` command.

    SCPI Syntax:
        ```
        - DISplay:SHOWREmote {ON|OFF|<NR1>}
        - DISplay:SHOWREmote?
        ```

    Info:
        - ``<NR1>`` = 0 disables remote display of waveform and other graticule data; any other
          value enables remote display of waveform and other graticule data.
        - ``ON`` enables the remote display of waveform and other graticule data.
        - ``OFF`` disables the remote display of waveform and other graticule data.
    """


class DisplayScreentextState(SCPICmdWrite):
    """The ``DISplay:SCREENTExt:STATE`` command.

    Description:
        - This command controls the display of screen text.

    Usage:
        - Using the ``.write(value)`` method will send the ``DISplay:SCREENTExt:STATE value``
          command.

    SCPI Syntax:
        ```
        - DISplay:SCREENTExt:STATE {ON|OFF|<NR1>}
        ```

    Info:
        - ``<NR1>`` = 0 disables screen text; any other value enables screen text.
        - ``ON`` turns on the display of screen text.
        - ``OFF`` turns off the display of screen text.
    """


class DisplayScreentextLabelItemYpos(SCPICmdWrite):
    """The ``DISplay:SCREENTExt:LABel<x>:YPOS`` command.

    Description:
        - This command sets the vertical position of a given label. The label is specified by x. The
          value of x can range from 1 through 8.

    Usage:
        - Using the ``.write(value)`` method will send the
          ``DISplay:SCREENTExt:LABel<x>:YPOS value`` command.

    SCPI Syntax:
        ```
        - DISplay:SCREENTExt:LABel<x>:YPOS <NR1>
        ```

    Info:
        - ``<NR1>`` sets the vertical position of the screen text label. The value can range from 0
          to 385.
    """


class DisplayScreentextLabelItemXpos(SCPICmdWrite):
    """The ``DISplay:SCREENTExt:LABel<x>:XPOS`` command.

    Description:
        - This command sets the horizontal position of a given screen text label. The label is
          specified by x. The value of x can range from 1 through 8.

    Usage:
        - Using the ``.write(value)`` method will send the
          ``DISplay:SCREENTExt:LABel<x>:XPOS value`` command.

    SCPI Syntax:
        ```
        - DISplay:SCREENTExt:LABel<x>:XPOS <NR1>
        ```

    Info:
        - ``<NR1>`` sets the horizontal position of the screen text label. The value can range from
          0 to 500.
    """


class DisplayScreentextLabelItemState(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:SCREENTExt:LABel<x>:STATE`` command.

    Description:
        - This command sets the state to be displayed for a given label. <x> is the label number, 1
          through 8.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:SCREENTExt:LABel<x>:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:SCREENTExt:LABel<x>:STATE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:SCREENTExt:LABel<x>:STATE value`` command.

    SCPI Syntax:
        ```
        - DISplay:SCREENTExt:LABel<x>:STATE {ON|OFF|<NR1>}
        - DISplay:SCREENTExt:LABel<x>:STATE?
        ```

    Info:
        - ``OFF`` = the screen text does not display.
        - ``ON`` = the screen text displays.
    """


class DisplayScreentextLabelItemName(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:SCREENTExt:LABel<x>:NAMe`` command.

    Description:
        - This command sets the text to be displayed for a given label. The label is specified by
          <x>. The value of <x> can range from 1 through 8.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:SCREENTExt:LABel<x>:NAMe?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:SCREENTExt:LABel<x>:NAMe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:SCREENTExt:LABel<x>:NAMe value`` command.

    SCPI Syntax:
        ```
        - DISplay:SCREENTExt:LABel<x>:NAMe <QString>
        - DISplay:SCREENTExt:LABel<x>:NAMe?
        ```

    Info:
        - ``<QString>`` argument is the text to be displayed for a given label.
    """

    _WRAP_ARG_WITH_QUOTES = True


class DisplayScreentextLabelItemFontstyle(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:SCREENTExt:LABel<x>:FONTSTyle`` command.

    Description:
        - This command sets or queries the screen text label font style. <x> is the label number, 1
          through 8.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:SCREENTExt:LABel<x>:FONTSTyle?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:SCREENTExt:LABel<x>:FONTSTyle?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:SCREENTExt:LABel<x>:FONTSTyle value`` command.

    SCPI Syntax:
        ```
        - DISplay:SCREENTExt:LABel<x>:FONTSTyle <QString>
        - DISplay:SCREENTExt:LABel<x>:FONTSTyle?
        ```

    Info:
        - ``<QString>`` argument is the font style to be displayed for a given label.
    """

    _WRAP_ARG_WITH_QUOTES = True


class DisplayScreentextLabelItemFontsize(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:SCREENTExt:LABel<x>:FONTSIze`` command.

    Description:
        - This command sets or queries the screen text label font size. <x> is the label number
          which ranges from 1 through 8.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:SCREENTExt:LABel<x>:FONTSIze?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:SCREENTExt:LABel<x>:FONTSIze?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:SCREENTExt:LABel<x>:FONTSIze value`` command.

    SCPI Syntax:
        ```
        - DISplay:SCREENTExt:LABel<x>:FONTSIze <NR1>
        - DISplay:SCREENTExt:LABel<x>:FONTSIze?
        ```

    Info:
        - ``<NR1>`` is the font size to be displayed for a given label.
    """


class DisplayScreentextLabelItemFontname(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:SCREENTExt:LABel<x>:FONTNAme`` command.

    Description:
        - This command sets or queries the screen text label font name. <x> is the label number
          which ranges from 1 through 8.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:SCREENTExt:LABel<x>:FONTNAme?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:SCREENTExt:LABel<x>:FONTNAme?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:SCREENTExt:LABel<x>:FONTNAme value`` command.

    SCPI Syntax:
        ```
        - DISplay:SCREENTExt:LABel<x>:FONTNAme <QString>
        - DISplay:SCREENTExt:LABel<x>:FONTNAme?
        ```

    Info:
        - ``<QString>`` argument is the font name to be displayed for a given label.
    """

    _WRAP_ARG_WITH_QUOTES = True


class DisplayScreentextLabelItemFonteffect(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:SCREENTExt:LABel<x>:FONTEFfect`` command.

    Description:
        - This command sets or queries the screen text label font effect. <x> is the label number, 1
          through 8.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:SCREENTExt:LABel<x>:FONTEFfect?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:SCREENTExt:LABel<x>:FONTEFfect?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:SCREENTExt:LABel<x>:FONTEFfect value`` command.

    SCPI Syntax:
        ```
        - DISplay:SCREENTExt:LABel<x>:FONTEFfect {NONe|CAPS|SHADow|EMBOss|ENGRave}
        - DISplay:SCREENTExt:LABel<x>:FONTEFfect?
        ```

    Info:
        - ``NONe`` sets the screen text label font effect to none.
        - ``CAPS`` sets the screen text label font effect to capital.
        - ``SHADow`` sets the screen text label font effect to shadow.
        - ``EMBOss`` sets the screen text label font effect to emboss.
        - ``ENGRAve`` sets the screen text label font effect to engrave.
    """


class DisplayScreentextLabelItemFontcolor(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:SCREENTExt:LABel<x>:FONTCOlor`` command.

    Description:
        - This command sets or queries the screen text label font color. <x> is the label number, 1
          through 8.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:SCREENTExt:LABel<x>:FONTCOlor?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:SCREENTExt:LABel<x>:FONTCOlor?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:SCREENTExt:LABel<x>:FONTCOlor value`` command.

    SCPI Syntax:
        ```
        - DISplay:SCREENTExt:LABel<x>:FONTCOlor <QString>
        - DISplay:SCREENTExt:LABel<x>:FONTCOlor?
        ```

    Info:
        - ``<QString>`` argument is the font color to be displayed for a given label.
    """

    _WRAP_ARG_WITH_QUOTES = True


#  pylint: disable=too-many-instance-attributes
class DisplayScreentextLabelItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``DISplay:SCREENTExt:LABel<x>`` command.

    Description:
        - This query-only command returns the screen text setting for a given label. Specifically,
          it provides the name, horizontal position (XPOS), and vertical position (YPOS).

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:SCREENTExt:LABel<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:SCREENTExt:LABel<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:SCREENTExt:LABel<x>?
        ```

    Properties:
        - ``.fontcolor``: The ``DISplay:SCREENTExt:LABel<x>:FONTCOlor`` command.
        - ``.fonteffect``: The ``DISplay:SCREENTExt:LABel<x>:FONTEFfect`` command.
        - ``.fontname``: The ``DISplay:SCREENTExt:LABel<x>:FONTNAme`` command.
        - ``.fontsize``: The ``DISplay:SCREENTExt:LABel<x>:FONTSIze`` command.
        - ``.fontstyle``: The ``DISplay:SCREENTExt:LABel<x>:FONTSTyle`` command.
        - ``.name``: The ``DISplay:SCREENTExt:LABel<x>:NAMe`` command.
        - ``.state``: The ``DISplay:SCREENTExt:LABel<x>:STATE`` command.
        - ``.xpos``: The ``DISplay:SCREENTExt:LABel<x>:XPOS`` command.
        - ``.ypos``: The ``DISplay:SCREENTExt:LABel<x>:YPOS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fontcolor = DisplayScreentextLabelItemFontcolor(
            device, f"{self._cmd_syntax}:FONTCOlor"
        )
        self._fonteffect = DisplayScreentextLabelItemFonteffect(
            device, f"{self._cmd_syntax}:FONTEFfect"
        )
        self._fontname = DisplayScreentextLabelItemFontname(device, f"{self._cmd_syntax}:FONTNAme")
        self._fontsize = DisplayScreentextLabelItemFontsize(device, f"{self._cmd_syntax}:FONTSIze")
        self._fontstyle = DisplayScreentextLabelItemFontstyle(
            device, f"{self._cmd_syntax}:FONTSTyle"
        )
        self._name = DisplayScreentextLabelItemName(device, f"{self._cmd_syntax}:NAMe")
        self._state = DisplayScreentextLabelItemState(device, f"{self._cmd_syntax}:STATE")
        self._xpos = DisplayScreentextLabelItemXpos(device, f"{self._cmd_syntax}:XPOS")
        self._ypos = DisplayScreentextLabelItemYpos(device, f"{self._cmd_syntax}:YPOS")

    @property
    def fontcolor(self) -> DisplayScreentextLabelItemFontcolor:
        """Return the ``DISplay:SCREENTExt:LABel<x>:FONTCOlor`` command.

        Description:
            - This command sets or queries the screen text label font color. <x> is the label
              number, 1 through 8.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:SCREENTExt:LABel<x>:FONTCOlor?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:SCREENTExt:LABel<x>:FONTCOlor?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:SCREENTExt:LABel<x>:FONTCOlor value`` command.

        SCPI Syntax:
            ```
            - DISplay:SCREENTExt:LABel<x>:FONTCOlor <QString>
            - DISplay:SCREENTExt:LABel<x>:FONTCOlor?
            ```

        Info:
            - ``<QString>`` argument is the font color to be displayed for a given label.
        """
        return self._fontcolor

    @property
    def fonteffect(self) -> DisplayScreentextLabelItemFonteffect:
        """Return the ``DISplay:SCREENTExt:LABel<x>:FONTEFfect`` command.

        Description:
            - This command sets or queries the screen text label font effect. <x> is the label
              number, 1 through 8.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:SCREENTExt:LABel<x>:FONTEFfect?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:SCREENTExt:LABel<x>:FONTEFfect?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:SCREENTExt:LABel<x>:FONTEFfect value`` command.

        SCPI Syntax:
            ```
            - DISplay:SCREENTExt:LABel<x>:FONTEFfect {NONe|CAPS|SHADow|EMBOss|ENGRave}
            - DISplay:SCREENTExt:LABel<x>:FONTEFfect?
            ```

        Info:
            - ``NONe`` sets the screen text label font effect to none.
            - ``CAPS`` sets the screen text label font effect to capital.
            - ``SHADow`` sets the screen text label font effect to shadow.
            - ``EMBOss`` sets the screen text label font effect to emboss.
            - ``ENGRAve`` sets the screen text label font effect to engrave.
        """
        return self._fonteffect

    @property
    def fontname(self) -> DisplayScreentextLabelItemFontname:
        """Return the ``DISplay:SCREENTExt:LABel<x>:FONTNAme`` command.

        Description:
            - This command sets or queries the screen text label font name. <x> is the label number
              which ranges from 1 through 8.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:SCREENTExt:LABel<x>:FONTNAme?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:SCREENTExt:LABel<x>:FONTNAme?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:SCREENTExt:LABel<x>:FONTNAme value`` command.

        SCPI Syntax:
            ```
            - DISplay:SCREENTExt:LABel<x>:FONTNAme <QString>
            - DISplay:SCREENTExt:LABel<x>:FONTNAme?
            ```

        Info:
            - ``<QString>`` argument is the font name to be displayed for a given label.
        """
        return self._fontname

    @property
    def fontsize(self) -> DisplayScreentextLabelItemFontsize:
        """Return the ``DISplay:SCREENTExt:LABel<x>:FONTSIze`` command.

        Description:
            - This command sets or queries the screen text label font size. <x> is the label number
              which ranges from 1 through 8.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:SCREENTExt:LABel<x>:FONTSIze?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:SCREENTExt:LABel<x>:FONTSIze?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:SCREENTExt:LABel<x>:FONTSIze value`` command.

        SCPI Syntax:
            ```
            - DISplay:SCREENTExt:LABel<x>:FONTSIze <NR1>
            - DISplay:SCREENTExt:LABel<x>:FONTSIze?
            ```

        Info:
            - ``<NR1>`` is the font size to be displayed for a given label.
        """
        return self._fontsize

    @property
    def fontstyle(self) -> DisplayScreentextLabelItemFontstyle:
        """Return the ``DISplay:SCREENTExt:LABel<x>:FONTSTyle`` command.

        Description:
            - This command sets or queries the screen text label font style. <x> is the label
              number, 1 through 8.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:SCREENTExt:LABel<x>:FONTSTyle?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:SCREENTExt:LABel<x>:FONTSTyle?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:SCREENTExt:LABel<x>:FONTSTyle value`` command.

        SCPI Syntax:
            ```
            - DISplay:SCREENTExt:LABel<x>:FONTSTyle <QString>
            - DISplay:SCREENTExt:LABel<x>:FONTSTyle?
            ```

        Info:
            - ``<QString>`` argument is the font style to be displayed for a given label.
        """
        return self._fontstyle

    @property
    def name(self) -> DisplayScreentextLabelItemName:
        """Return the ``DISplay:SCREENTExt:LABel<x>:NAMe`` command.

        Description:
            - This command sets the text to be displayed for a given label. The label is specified
              by <x>. The value of <x> can range from 1 through 8.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:SCREENTExt:LABel<x>:NAMe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:SCREENTExt:LABel<x>:NAMe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:SCREENTExt:LABel<x>:NAMe value`` command.

        SCPI Syntax:
            ```
            - DISplay:SCREENTExt:LABel<x>:NAMe <QString>
            - DISplay:SCREENTExt:LABel<x>:NAMe?
            ```

        Info:
            - ``<QString>`` argument is the text to be displayed for a given label.
        """
        return self._name

    @property
    def state(self) -> DisplayScreentextLabelItemState:
        """Return the ``DISplay:SCREENTExt:LABel<x>:STATE`` command.

        Description:
            - This command sets the state to be displayed for a given label. <x> is the label
              number, 1 through 8.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:SCREENTExt:LABel<x>:STATE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:SCREENTExt:LABel<x>:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:SCREENTExt:LABel<x>:STATE value`` command.

        SCPI Syntax:
            ```
            - DISplay:SCREENTExt:LABel<x>:STATE {ON|OFF|<NR1>}
            - DISplay:SCREENTExt:LABel<x>:STATE?
            ```

        Info:
            - ``OFF`` = the screen text does not display.
            - ``ON`` = the screen text displays.
        """
        return self._state

    @property
    def xpos(self) -> DisplayScreentextLabelItemXpos:
        """Return the ``DISplay:SCREENTExt:LABel<x>:XPOS`` command.

        Description:
            - This command sets the horizontal position of a given screen text label. The label is
              specified by x. The value of x can range from 1 through 8.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``DISplay:SCREENTExt:LABel<x>:XPOS value`` command.

        SCPI Syntax:
            ```
            - DISplay:SCREENTExt:LABel<x>:XPOS <NR1>
            ```

        Info:
            - ``<NR1>`` sets the horizontal position of the screen text label. The value can range
              from 0 to 500.
        """
        return self._xpos

    @property
    def ypos(self) -> DisplayScreentextLabelItemYpos:
        """Return the ``DISplay:SCREENTExt:LABel<x>:YPOS`` command.

        Description:
            - This command sets the vertical position of a given label. The label is specified by x.
              The value of x can range from 1 through 8.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``DISplay:SCREENTExt:LABel<x>:YPOS value`` command.

        SCPI Syntax:
            ```
            - DISplay:SCREENTExt:LABel<x>:YPOS <NR1>
            ```

        Info:
            - ``<NR1>`` sets the vertical position of the screen text label. The value can range
              from 0 to 385.
        """
        return self._ypos


class DisplayScreentext(SCPICmdRead):
    """The ``DISplay:SCREENTExt`` command.

    Description:
        - This query-only command returns all screen text settings.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:SCREENTExt?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:SCREENTExt?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:SCREENTExt?
        ```

    Properties:
        - ``.label``: The ``DISplay:SCREENTExt:LABel<x>`` command.
        - ``.state``: The ``DISplay:SCREENTExt:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._label: Dict[int, DisplayScreentextLabelItem] = DefaultDictPassKeyToFactory(
            lambda x: DisplayScreentextLabelItem(device, f"{self._cmd_syntax}:LABel{x}")
        )
        self._state = DisplayScreentextState(device, f"{self._cmd_syntax}:STATE")

    @property
    def label(self) -> Dict[int, DisplayScreentextLabelItem]:
        """Return the ``DISplay:SCREENTExt:LABel<x>`` command.

        Description:
            - This query-only command returns the screen text setting for a given label.
              Specifically, it provides the name, horizontal position (XPOS), and vertical position
              (YPOS).

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:SCREENTExt:LABel<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:SCREENTExt:LABel<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:SCREENTExt:LABel<x>?
            ```

        Sub-properties:
            - ``.fontcolor``: The ``DISplay:SCREENTExt:LABel<x>:FONTCOlor`` command.
            - ``.fonteffect``: The ``DISplay:SCREENTExt:LABel<x>:FONTEFfect`` command.
            - ``.fontname``: The ``DISplay:SCREENTExt:LABel<x>:FONTNAme`` command.
            - ``.fontsize``: The ``DISplay:SCREENTExt:LABel<x>:FONTSIze`` command.
            - ``.fontstyle``: The ``DISplay:SCREENTExt:LABel<x>:FONTSTyle`` command.
            - ``.name``: The ``DISplay:SCREENTExt:LABel<x>:NAMe`` command.
            - ``.state``: The ``DISplay:SCREENTExt:LABel<x>:STATE`` command.
            - ``.xpos``: The ``DISplay:SCREENTExt:LABel<x>:XPOS`` command.
            - ``.ypos``: The ``DISplay:SCREENTExt:LABel<x>:YPOS`` command.
        """
        return self._label

    @property
    def state(self) -> DisplayScreentextState:
        """Return the ``DISplay:SCREENTExt:STATE`` command.

        Description:
            - This command controls the display of screen text.

        Usage:
            - Using the ``.write(value)`` method will send the ``DISplay:SCREENTExt:STATE value``
              command.

        SCPI Syntax:
            ```
            - DISplay:SCREENTExt:STATE {ON|OFF|<NR1>}
            ```

        Info:
            - ``<NR1>`` = 0 disables screen text; any other value enables screen text.
            - ``ON`` turns on the display of screen text.
            - ``OFF`` turns off the display of screen text.
        """
        return self._state


class DisplayPersistenceReset(SCPICmdWriteNoArguments):
    """The ``DISplay:PERSistence:RESET`` command.

    Description:
        - This command controls the clearing of persistence data that has been built up over time.
          Persistence is valid for wave views only.

    Usage:
        - Using the ``.write()`` method will send the ``DISplay:PERSistence:RESET`` command.

    SCPI Syntax:
        ```
        - DISplay:PERSistence:RESET
        ```
    """


class DisplayPersistence(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:PERSistence`` command.

    Description:
        - This command sets or queries the persistence aspect of the display. This affects the
          display only and is equivalent to selecting Display Persistence from the Display menu.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PERSistence?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PERSistence?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:PERSistence value`` command.

    SCPI Syntax:
        ```
        - DISplay:PERSistence {OFF|INFPersist|VARpersist}
        - DISplay:PERSistence?
        ```

    Info:
        - ``OFF`` disables the persistence aspect of the display.
        - ``INFPersist`` sets a display mode where any pixels, once touched by samples, remain set
          until cleared by a mode change.
        - ``VARPersist`` sets a display mode where set pixels are gradually dimmed.

    Properties:
        - ``.reset``: The ``DISplay:PERSistence:RESET`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._reset = DisplayPersistenceReset(device, f"{self._cmd_syntax}:RESET")

    @property
    def reset(self) -> DisplayPersistenceReset:
        """Return the ``DISplay:PERSistence:RESET`` command.

        Description:
            - This command controls the clearing of persistence data that has been built up over
              time. Persistence is valid for wave views only.

        Usage:
            - Using the ``.write()`` method will send the ``DISplay:PERSistence:RESET`` command.

        SCPI Syntax:
            ```
            - DISplay:PERSistence:RESET
            ```
        """
        return self._reset


class DisplayIntensityWaveformRecordview(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:INTENSITy:WAVEform:RECORDView`` command.

    Description:
        - This command sets or queries the saturation level for record view waveforms.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:INTENSITy:WAVEform:RECORDView?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:INTENSITy:WAVEform:RECORDView?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:INTENSITy:WAVEform:RECORDView value`` command.

    SCPI Syntax:
        ```
        - DISplay:INTENSITy:WAVEform:RECORDView <NR2>
        - DISplay:INTENSITy:WAVEform:RECORDView?
        ```

    Info:
        - ``<NR2>`` is the waveform saturation and ranges from 10 to 100 percent.
    """


class DisplayIntensityWaveformImageview(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:INTENSITy:WAVEform:IMAGEView`` command.

    Description:
        - This command sets or queries the saturation level for image view waveforms.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:INTENSITy:WAVEform:IMAGEView?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:INTENSITy:WAVEform:IMAGEView?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:INTENSITy:WAVEform:IMAGEView value`` command.

    SCPI Syntax:
        ```
        - DISplay:INTENSITy:WAVEform:IMAGEView <NR2>
        - DISplay:INTENSITy:WAVEform:IMAGEView?
        ```

    Info:
        - ``<NR2>`` is the waveform saturation and ranges from 10 to 100 percent.
    """


class DisplayIntensityWaveform(SCPICmdRead):
    """The ``DISplay:INTENSITy:WAVEform`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:INTENSITy:WAVEform?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy:WAVEform?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.imageview``: The ``DISplay:INTENSITy:WAVEform:IMAGEView`` command.
        - ``.recordview``: The ``DISplay:INTENSITy:WAVEform:RECORDView`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._imageview = DisplayIntensityWaveformImageview(device, f"{self._cmd_syntax}:IMAGEView")
        self._recordview = DisplayIntensityWaveformRecordview(
            device, f"{self._cmd_syntax}:RECORDView"
        )

    @property
    def imageview(self) -> DisplayIntensityWaveformImageview:
        """Return the ``DISplay:INTENSITy:WAVEform:IMAGEView`` command.

        Description:
            - This command sets or queries the saturation level for image view waveforms.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:INTENSITy:WAVEform:IMAGEView?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:INTENSITy:WAVEform:IMAGEView?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:INTENSITy:WAVEform:IMAGEView value`` command.

        SCPI Syntax:
            ```
            - DISplay:INTENSITy:WAVEform:IMAGEView <NR2>
            - DISplay:INTENSITy:WAVEform:IMAGEView?
            ```

        Info:
            - ``<NR2>`` is the waveform saturation and ranges from 10 to 100 percent.
        """
        return self._imageview

    @property
    def recordview(self) -> DisplayIntensityWaveformRecordview:
        """Return the ``DISplay:INTENSITy:WAVEform:RECORDView`` command.

        Description:
            - This command sets or queries the saturation level for record view waveforms.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:INTENSITy:WAVEform:RECORDView?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:INTENSITy:WAVEform:RECORDView?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:INTENSITy:WAVEform:RECORDView value`` command.

        SCPI Syntax:
            ```
            - DISplay:INTENSITy:WAVEform:RECORDView <NR2>
            - DISplay:INTENSITy:WAVEform:RECORDView?
            ```

        Info:
            - ``<NR2>`` is the waveform saturation and ranges from 10 to 100 percent.
        """
        return self._recordview


class DisplayIntensityScreensaverdelay(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:INTENSITy:SCREENSAVERDELAY`` command.

    Description:
        - This command sets or queries the timeout of the screen saver features of the display
          system. When enabled (after the specified screen saver delay seconds of control activity
          and when the screen saver feature is enabled) the instrument activates the screen saver
          feature. Normal instrument displays are restored and the delay timer is reset upon any
          control activity. The instrument continues to acquire and process data normally while in
          screen saver mode; only the display is disabled. This command is equivalent to selecting
          Objects from the Display menu and entering a time in the Delay field of the LCD Backlight
          Timeout control.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:INTENSITy:SCREENSAVERDELAY?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy:SCREENSAVERDELAY?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:INTENSITy:SCREENSAVERDELAY value`` command.

    SCPI Syntax:
        ```
        - DISplay:INTENSITy:SCREENSAVERDELAY {<NR1>}
        - DISplay:INTENSITy:SCREENSAVERDELAY?
        ```

    Info:
        - ``<NR1>`` sets the screen saver timeout, which ranges from 30 through 28800 seconds.
    """


class DisplayIntensityScreensaver(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:INTENSITy:SCREENSAVER`` command.

    Description:
        - This command sets and queries the screen saver features of the MS Windows operating
          system. When enabled, a delay timer (set in seconds by the
          ``DISPLAY:INTENSITY:SCREENSAVERDELAY`` command) begins counting down. When this screen
          saver delay times out, the screen low-power mode engages. This causes the LCD backlight to
          switch off and clears both waveform and text displays. Any control (front panel, mouse or
          keyboard) or touch screen activity resets the delay timer and restores normal instrument
          display. This command is equivalent to selecting LCD Save Enabled from the Display menu.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:INTENSITy:SCREENSAVER?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy:SCREENSAVER?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:INTENSITy:SCREENSAVER value``
          command.

    SCPI Syntax:
        ```
        - DISplay:INTENSITy:SCREENSAVER {ON|OFF|<NR1>}
        - DISplay:INTENSITy:SCREENSAVER?
        ```

    Info:
        - ``OFF`` disables the screen saver feature.
        - ``ON`` enables the screen saver feature after the specified screen saver delay seconds of
          control activity have passed.
        - ``<NR1>`` = 0 disables the screen saver feature; <NR1> = 1 enables the screen saver
          protection features.
    """


class DisplayIntensityCustompct(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:INTENSITy:CUSTOMPct`` command.

    Description:
        - This command sets or queries the waveform intensity which allows you to adjust the
          brightness and contrast of the waveforms. Higher intensity values are used so that the
          less frequent waveform parts such as glitches standout more. Waveform intensity applies to
          all waveforms (channels, maths, and references). There are two waveform intensity settings
          one for FastAcq and one for RecordVu (that is the FastAcq is off). The waveform intensity
          control allows the intensity to be changed from 10 to 100. The default value is 75. At
          intensity value 100, all waveform points are displayed at full intensity.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:INTENSITy:CUSTOMPct?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy:CUSTOMPct?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:INTENSITy:CUSTOMPct value``
          command.

    SCPI Syntax:
        ```
        - DISplay:INTENSITy:CUSTOMPct <NRF>
        - DISplay:INTENSITy:CUSTOMPct?
        ```

    Info:
        - ``<NRF>`` is the custom percent intensity which ranges from 5 to 100.
    """


class DisplayIntensityBacklight(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:INTENSITy:BACKLight`` command.

    Description:
        - This command sets or queries the display backlight intensity setting.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:INTENSITy:BACKLight?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy:BACKLight?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:INTENSITy:BACKLight value``
          command.

    SCPI Syntax:
        ```
        - DISplay:INTENSITy:BACKLight {LOW|MEDium|HIGH}
        - DISplay:INTENSITy:BACKLight?
        ```

    Info:
        - ``LOW`` selects a low brightness level.
        - ``MEDium`` selects a moderate brightness level.
        - ``HIGH`` selects a full brightness level.
    """


class DisplayIntensityAutobright(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:INTENSITy:AUTOBright`` command.

    Description:
        - This command enables automatic, ongoing adjustment of the intensity to display images. The
          query form returns a 1 (ON) or a 0 (OFF). This command is equivalent to selecting Display
          Setup from the Display menu and choosing the Appearance tab.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:INTENSITy:AUTOBright?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy:AUTOBright?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:INTENSITy:AUTOBright value``
          command.

    SCPI Syntax:
        ```
        - DISplay:INTENSITy:AUTOBright {ON|OFF|<NR1>}
        - DISplay:INTENSITy:AUTOBright?
        ```

    Info:
        - ``OFF`` argument allows the system to use the manually set waveform intensity value
          against an absolute scale. The display simulates the appearance of signals on an analog
          instrument. Waveforms that trigger more frequently appear brighter than waveforms that
          trigger less frequently.
        - ``ON`` argument allows the system to adjust the settings automatically to provide a
          visible waveform.
        - ``<NR1>`` = 0 allows the system to use the manually-set waveform intensity value against
          an absolute scale; any other value allows the system to adjust settings.
    """


class DisplayIntensity(SCPICmdRead):
    """The ``DISplay:INTENSITy`` command.

    Description:
        - This query-only command returns the waveform saturation level and screen saver settings.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:INTENSITy?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:INTENSITy?
        ```

    Properties:
        - ``.autobright``: The ``DISplay:INTENSITy:AUTOBright`` command.
        - ``.backlight``: The ``DISplay:INTENSITy:BACKLight`` command.
        - ``.custompct``: The ``DISplay:INTENSITy:CUSTOMPct`` command.
        - ``.screensaver``: The ``DISplay:INTENSITy:SCREENSAVER`` command.
        - ``.screensaverdelay``: The ``DISplay:INTENSITy:SCREENSAVERDELAY`` command.
        - ``.waveform``: The ``DISplay:INTENSITy:WAVEform`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autobright = DisplayIntensityAutobright(device, f"{self._cmd_syntax}:AUTOBright")
        self._backlight = DisplayIntensityBacklight(device, f"{self._cmd_syntax}:BACKLight")
        self._custompct = DisplayIntensityCustompct(device, f"{self._cmd_syntax}:CUSTOMPct")
        self._screensaver = DisplayIntensityScreensaver(device, f"{self._cmd_syntax}:SCREENSAVER")
        self._screensaverdelay = DisplayIntensityScreensaverdelay(
            device, f"{self._cmd_syntax}:SCREENSAVERDELAY"
        )
        self._waveform = DisplayIntensityWaveform(device, f"{self._cmd_syntax}:WAVEform")

    @property
    def autobright(self) -> DisplayIntensityAutobright:
        """Return the ``DISplay:INTENSITy:AUTOBright`` command.

        Description:
            - This command enables automatic, ongoing adjustment of the intensity to display images.
              The query form returns a 1 (ON) or a 0 (OFF). This command is equivalent to selecting
              Display Setup from the Display menu and choosing the Appearance tab.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:INTENSITy:AUTOBright?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy:AUTOBright?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:INTENSITy:AUTOBright value`` command.

        SCPI Syntax:
            ```
            - DISplay:INTENSITy:AUTOBright {ON|OFF|<NR1>}
            - DISplay:INTENSITy:AUTOBright?
            ```

        Info:
            - ``OFF`` argument allows the system to use the manually set waveform intensity value
              against an absolute scale. The display simulates the appearance of signals on an
              analog instrument. Waveforms that trigger more frequently appear brighter than
              waveforms that trigger less frequently.
            - ``ON`` argument allows the system to adjust the settings automatically to provide a
              visible waveform.
            - ``<NR1>`` = 0 allows the system to use the manually-set waveform intensity value
              against an absolute scale; any other value allows the system to adjust settings.
        """
        return self._autobright

    @property
    def backlight(self) -> DisplayIntensityBacklight:
        """Return the ``DISplay:INTENSITy:BACKLight`` command.

        Description:
            - This command sets or queries the display backlight intensity setting.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:INTENSITy:BACKLight?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy:BACKLight?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:INTENSITy:BACKLight value``
              command.

        SCPI Syntax:
            ```
            - DISplay:INTENSITy:BACKLight {LOW|MEDium|HIGH}
            - DISplay:INTENSITy:BACKLight?
            ```

        Info:
            - ``LOW`` selects a low brightness level.
            - ``MEDium`` selects a moderate brightness level.
            - ``HIGH`` selects a full brightness level.
        """
        return self._backlight

    @property
    def custompct(self) -> DisplayIntensityCustompct:
        """Return the ``DISplay:INTENSITy:CUSTOMPct`` command.

        Description:
            - This command sets or queries the waveform intensity which allows you to adjust the
              brightness and contrast of the waveforms. Higher intensity values are used so that the
              less frequent waveform parts such as glitches standout more. Waveform intensity
              applies to all waveforms (channels, maths, and references). There are two waveform
              intensity settings one for FastAcq and one for RecordVu (that is the FastAcq is off).
              The waveform intensity control allows the intensity to be changed from 10 to 100. The
              default value is 75. At intensity value 100, all waveform points are displayed at full
              intensity.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:INTENSITy:CUSTOMPct?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy:CUSTOMPct?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:INTENSITy:CUSTOMPct value``
              command.

        SCPI Syntax:
            ```
            - DISplay:INTENSITy:CUSTOMPct <NRF>
            - DISplay:INTENSITy:CUSTOMPct?
            ```

        Info:
            - ``<NRF>`` is the custom percent intensity which ranges from 5 to 100.
        """
        return self._custompct

    @property
    def screensaver(self) -> DisplayIntensityScreensaver:
        """Return the ``DISplay:INTENSITy:SCREENSAVER`` command.

        Description:
            - This command sets and queries the screen saver features of the MS Windows operating
              system. When enabled, a delay timer (set in seconds by the
              ``DISPLAY:INTENSITY:SCREENSAVERDELAY`` command) begins counting down. When this screen
              saver delay times out, the screen low-power mode engages. This causes the LCD
              backlight to switch off and clears both waveform and text displays. Any control (front
              panel, mouse or keyboard) or touch screen activity resets the delay timer and restores
              normal instrument display. This command is equivalent to selecting LCD Save Enabled
              from the Display menu.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:INTENSITy:SCREENSAVER?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy:SCREENSAVER?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:INTENSITy:SCREENSAVER value`` command.

        SCPI Syntax:
            ```
            - DISplay:INTENSITy:SCREENSAVER {ON|OFF|<NR1>}
            - DISplay:INTENSITy:SCREENSAVER?
            ```

        Info:
            - ``OFF`` disables the screen saver feature.
            - ``ON`` enables the screen saver feature after the specified screen saver delay seconds
              of control activity have passed.
            - ``<NR1>`` = 0 disables the screen saver feature; <NR1> = 1 enables the screen saver
              protection features.
        """
        return self._screensaver

    @property
    def screensaverdelay(self) -> DisplayIntensityScreensaverdelay:
        """Return the ``DISplay:INTENSITy:SCREENSAVERDELAY`` command.

        Description:
            - This command sets or queries the timeout of the screen saver features of the display
              system. When enabled (after the specified screen saver delay seconds of control
              activity and when the screen saver feature is enabled) the instrument activates the
              screen saver feature. Normal instrument displays are restored and the delay timer is
              reset upon any control activity. The instrument continues to acquire and process data
              normally while in screen saver mode; only the display is disabled. This command is
              equivalent to selecting Objects from the Display menu and entering a time in the Delay
              field of the LCD Backlight Timeout control.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:INTENSITy:SCREENSAVERDELAY?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:INTENSITy:SCREENSAVERDELAY?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:INTENSITy:SCREENSAVERDELAY value`` command.

        SCPI Syntax:
            ```
            - DISplay:INTENSITy:SCREENSAVERDELAY {<NR1>}
            - DISplay:INTENSITy:SCREENSAVERDELAY?
            ```

        Info:
            - ``<NR1>`` sets the screen saver timeout, which ranges from 30 through 28800 seconds.
        """
        return self._screensaverdelay

    @property
    def waveform(self) -> DisplayIntensityWaveform:
        """Return the ``DISplay:INTENSITy:WAVEform`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:INTENSITy:WAVEform?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy:WAVEform?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.imageview``: The ``DISplay:INTENSITy:WAVEform:IMAGEView`` command.
            - ``.recordview``: The ``DISplay:INTENSITy:WAVEform:RECORDView`` command.
        """
        return self._waveform


class DisplayGraticule(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:GRAticule`` command.

    Description:
        - This command selects or queries the type of graticule that is displayed. This command is
          equivalent to selecting Graticule Style from the Display menu.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:GRAticule?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:GRAticule?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:GRAticule value`` command.

    SCPI Syntax:
        ```
        - DISplay:GRAticule {CROSSHair|FRAme|FULl|GRId|IRE|NTSC|MV|PAL}
        - DISplay:GRAticule?
        ```

    Info:
        - ``CROSSHair`` specifies a frame and cross hairs.
        - ``FRAme`` specifies a frame only.
        - ``FULl`` specifies a frame, a grid and cross hairs.
        - ``GRId`` specifies a frame and grid only.
        - ``IRE`` specifies an IRE video graticule, and sets the vertical scale to 143 mV per
          division.
        - ``NTSC`` specifies an NTSC video graticule (same as the IRE graticule), and sets the
          vertical scale to 133 mV per division.
        - ``MV`` specifies an mV video graticule and sets the vertical scale to 133 mV per division.
          This graticule is used to measure PAL standard video signals.
        - ``PAL`` specifies a PAL video graticule (same as the mV graticule) and sets the vertical
          scale to 133 mV per division. This graticule is used to measure PAL standard video
          signals.
    """


class DisplayFormat(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:FORMat`` command.

    Description:
        - This command sets or queries the display format. This command is equivalent to selecting
          Format from the Display menu.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:FORMat?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:FORMat?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:FORMat value`` command.

    SCPI Syntax:
        ```
        - DISplay:FORMat {YT|XY|XYZ}
        - DISplay:FORMat?
        ```

    Info:
        - ``YT`` sets the display to a voltage versus time format and is the default mode.
        - ``XY`` argument displays one waveform against another. The source pairs that make up an XY
          trace are predefined and are listed in the following table. Selecting one source causes
          its corresponding source to be implicitly selected, producing a single trace from the two
          input waveforms.
        - ``XYZ`` argument is available only for four-channel instruments. The argument combines
          channel 1 and channel 2 for X and Y coordinates and uses channel 3 to provide the
          intensity value for the sample. XYZ groups channels 1, 2 and 3 to form a single trace.
          Other channel, math, and reference waveforms are turned off.
    """


class DisplayFilter(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:FILTer`` command.

    Description:
        - This command sets or queries the type of interpolation to use for the display. Filtering
          only applies to normal-mode acquisition. The ``DISplay:FILTer`` command also provides
          selection for acquisition interpolation type. This command is equivalent to selecting
          Waveform Interpolation from the Display menu.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:FILTer?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:FILTer?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:FILTer value`` command.

    SCPI Syntax:
        ```
        - DISplay:FILTer {LINEAr|SINX}
        - DISplay:FILTer?
        ```

    Info:
        - ``LINEAr`` specifies linear interpolation, where acquired points are connected with
          straight lines.
        - ``SINX`` specifies sin(x)/x interpolation, where acquired points are fit to a curve.
    """


class DisplayDpojetplot(SCPICmdReadWithArguments):
    """The ``DISplay:DPOJETPlot`` command.

    Description:
        - This command queries which DPOJET plot is selected and the screen capture file format.

    Usage:
        - Using the ``.query(argument)`` method will send the ``DISplay:DPOJETPlot? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``DISplay:DPOJETPlot? argument`` query and raise an AssertionError if the returned value
          does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:DPOJETPlot? (PLOT1 | PLOT2 | PLOT3 | PLOT4 | SUMMARY)[,(JPEG | JPG | TIF | TIFF | BMP | EMF | PNG)]
        ```
    """  # noqa: E501


class DisplayDigitalHeight(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:DIGital:HEIght`` command.

    Description:
        - This command sets or queries the height of the digital input waveform and the label
          associated with the channel.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:DIGital:HEIght?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:DIGital:HEIght?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:DIGital:HEIght value`` command.

    SCPI Syntax:
        ```
        - DISplay:DIGital:HEIght {SMAll|LARge|MEDium|XSMAll}
        - DISplay:DIGital:HEIght?
        ```

    Info:
        - ``SMAll`` specifies the height of the digital input waveform and the label associated with
          the channel to small.
        - ``LARge`` specifies the height of the digital input waveform and the label associated with
          the channel to large.
        - ``MEDium`` specifies the height of the digital input waveform and the label associated
          with the channel to medium.
        - ``XSMAll`` specifies the height of the digital input waveform and the label associated
          with the channel to extra small.
    """


class DisplayDigital(SCPICmdRead):
    """The ``DISplay:DIGital`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:DIGital?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:DIGital?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.height``: The ``DISplay:DIGital:HEIght`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._height = DisplayDigitalHeight(device, f"{self._cmd_syntax}:HEIght")

    @property
    def height(self) -> DisplayDigitalHeight:
        """Return the ``DISplay:DIGital:HEIght`` command.

        Description:
            - This command sets or queries the height of the digital input waveform and the label
              associated with the channel.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:DIGital:HEIght?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:DIGital:HEIght?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:DIGital:HEIght value``
              command.

        SCPI Syntax:
            ```
            - DISplay:DIGital:HEIght {SMAll|LARge|MEDium|XSMAll}
            - DISplay:DIGital:HEIght?
            ```

        Info:
            - ``SMAll`` specifies the height of the digital input waveform and the label associated
              with the channel to small.
            - ``LARge`` specifies the height of the digital input waveform and the label associated
              with the channel to large.
            - ``MEDium`` specifies the height of the digital input waveform and the label associated
              with the channel to medium.
            - ``XSMAll`` specifies the height of the digital input waveform and the label associated
              with the channel to extra small.
        """
        return self._height


class DisplayDeskew(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:DESKew`` command.

    Description:
        - This command controls or queries the state of the Display Only button.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:DESKew?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:DESKew?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:DESKew value`` command.

    SCPI Syntax:
        ```
        - DISplay:DESKew {<NR1>|OFF|ON|AUTO}
        - DISplay:DESKew?
        ```

    Info:
        - ``OFF`` sets deskew for the acquisition waveform.
        - ``ON`` sets deskew to deskew the display only.
        - ``<NR1>`` = 0 will deskew the acquisition waveform; any other value will deskew the
          display only.
        - ``AUTO`` automatically selects the deskew setting.
    """


class DisplayData(SCPICmdReadWithArguments):
    """The ``DISplay:DATa`` command.

    Description:
        - The query returns the screen shot from the oscilloscope in block data format, as defined
          in the IEEE 488.2 standard. The first argument is the file format and is required. The
          second option is the screen view. The third option is the palate. If no options are
          specified, the default selections are FULLSCREEN and COLOr. If you want to specify the
          second option, the first option must be specified. For example, if you want the screen
          capture to be INKSaver, you must specify a screen view. BMP,GRA,INKS.

    Usage:
        - Using the ``.query(argument)`` method will send the ``DISplay:DATa? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the ``DISplay:DATa? argument``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:DATa? (BMP| JPEG| PNG | TIFF)[,(FULLSCREEN | GRAticule | FULLNOmenu)[,(COLOr | INKSaver | BLACKANDWhite )]]
        ```
    """  # noqa: E501


class DisplayColorRefcolor(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:COLOr:REFCOLOr`` command.

    Description:
        - This command sets or queries the color to be used for reference traces, either in the
          standard palette's nominal REF color or according to the color of the source waveform.
          This command is equivalent to selecting Display Setup from the Display menu and then
          choosing the Colors tab.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:COLOr:REFCOLOr?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:COLOr:REFCOLOr?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:COLOr:REFCOLOr value`` command.

    SCPI Syntax:
        ```
        - DISplay:COLOr:REFCOLOr {DEFAULT|INHERIT}
        - DISplay:COLOr:REFCOLOr?
        ```

    Info:
        - ``DEFAULT`` assigns color reference traces to the nominal palette reference color, which
          is off-white.
        - ``INHERIT`` assigns color reference traces to the source waveform color.
    """


class DisplayColorPaletteUserWaveform(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:COLOr:PALEtte:USEr:WAVEform`` command.

    Description:
        - This command sets or queries the user palette waveform colors. It assigns the
          hue-lightness-saturation (HLS) triplet to be used for the specified waveform for the user
          palette.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:COLOr:PALEtte:USEr:WAVEform?``
          query.
        - Using the ``.verify(value)`` method will send the ``DISplay:COLOr:PALEtte:USEr:WAVEform?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:COLOr:PALEtte:USEr:WAVEform value`` command.

    SCPI Syntax:
        ```
        - DISplay:COLOr:PALEtte:USEr:WAVEform {HLS|SPECTral|TEMPErature}
        - DISplay:COLOr:PALEtte:USEr:WAVEform?
        ```

    Info:
        - ``HLS`` sets the color of user waveforms to the hue, lightness, and saturation specified
          by the ``DISPLAY:COLOR:PALETTE:USER:WAVEFORM`` commands.
        - ``SPECTral`` sets the color of user waveforms to spectral.
        - ``TEMPErature`` sets the color of user waveforms to temperature.
    """


class DisplayColorPaletteUserRefItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:COLOr:PALEtte:USEr:REF<x>`` command.

    Description:
        - This command sets or queries the user palette reference colors assigned to the reference
          waveforms. It assigns the hue-lightness-saturation (HLS) triplet to be used for the
          specified reference waveform color for the user palette. The reference waveform is
          specified by x. The value of x can range from 1 through 4.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:COLOr:PALEtte:USEr:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:COLOr:PALEtte:USEr:REF<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:COLOr:PALEtte:USEr:REF<x> value`` command.

    SCPI Syntax:
        ```
        - DISplay:COLOr:PALEtte:USEr:REF<x> <NR1>,<NR1>,<NR1>
        - DISplay:COLOr:PALEtte:USEr:REF<x>?
        ```

    Info:
        - ``<NR1>`` Hue. Range of 0 to 360.
        - ``<NR1>`` Lightness. Range of 0 to 100.
        - ``<NR1>`` Saturation. Range of 0 to 100.
    """


class DisplayColorPaletteUserMathItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:COLOr:PALEtte:USEr:MATH<x>`` command.

    Description:
        - This command sets or queries the user palette math colors. It assigns the
          hue-lightness-saturation (HLS) triplet to be used for the specified math waveform for the
          user palette. The math waveform is specified by x. The value of x can range from 1 through
          4.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:COLOr:PALEtte:USEr:MATH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:COLOr:PALEtte:USEr:MATH<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:COLOr:PALEtte:USEr:MATH<x> value`` command.

    SCPI Syntax:
        ```
        - DISplay:COLOr:PALEtte:USEr:MATH<x> <NR1>,<NR1>,<NR1>
        - DISplay:COLOr:PALEtte:USEr:MATH<x>?
        ```

    Info:
        - ``<NR1>`` Hue. Range of 0 to 360.
        - ``<NR1>`` Lightness. Range of 0 to 100.
        - ``<NR1>`` Saturation. Range of 0 to 100.
    """


class DisplayColorPaletteUserMaskhighlight(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:COLOr:PALEtte:USEr:MASKHighlight`` command.

    Description:
        - This command sets or queries the user palette mask hits color. It assigns the
          hue-lightness-saturation (HLS) triplet to be used for the mask highlight (mask hits) color
          for the user palette.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:COLOr:PALEtte:USEr:MASKHighlight?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:COLOr:PALEtte:USEr:MASKHighlight?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:COLOr:PALEtte:USEr:MASKHighlight value`` command.

    SCPI Syntax:
        ```
        - DISplay:COLOr:PALEtte:USEr:MASKHighlight <NR1>,<NR1>,<NR1>
        - DISplay:COLOr:PALEtte:USEr:MASKHighlight?
        ```

    Info:
        - ``<NR1>`` Hue. Range of 0 to 360.
        - ``<NR1>`` Lightness. Range of 0 to 100.
        - ``<NR1>`` Saturation. Range of 0 to 100.
    """


class DisplayColorPaletteUserMask(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:COLOr:PALEtte:USEr:MASK`` command.

    Description:
        - This command sets or queries the user palette mask color. It assigns the
          hue-lightness-saturation (HLS) color for the mask color for the user palette.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:COLOr:PALEtte:USEr:MASK?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:COLOr:PALEtte:USEr:MASK?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:COLOr:PALEtte:USEr:MASK value``
          command.

    SCPI Syntax:
        ```
        - DISplay:COLOr:PALEtte:USEr:MASK <NR1>,<NR1>,<NR1>
        - DISplay:COLOr:PALEtte:USEr:MASK?
        ```

    Info:
        - ``<NR1>`` Hue. Range of 0 to 360.
        - ``<NR1>`` Lightness. Range of 0 to 100.
        - ``<NR1>`` Saturation. Range of 0 to 100.
    """


class DisplayColorPaletteUserHistogram(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:COLOr:PALEtte:USEr:HIStogram`` command.

    Description:
        - This command sets or queries the user palette histogram color. It assigns the
          hue-saturation-lightness (HLS) triplet to be used for the histogram color for the user
          palette.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:COLOr:PALEtte:USEr:HIStogram?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:COLOr:PALEtte:USEr:HIStogram?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:COLOr:PALEtte:USEr:HIStogram value`` command.

    SCPI Syntax:
        ```
        - DISplay:COLOr:PALEtte:USEr:HIStogram <NR1>,<NR1>,<NR1>
        - DISplay:COLOr:PALEtte:USEr:HIStogram?
        ```

    Info:
        - ``<NR1>`` Hue. Range of 0 to 360.
        - ``<NR1>`` Lightness. Range of 0 to 100.
        - ``<NR1>`` Saturation. Range of 0 to 100.
    """


class DisplayColorPaletteUserGraticule(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:COLOr:PALEtte:USEr:GRAticule`` command.

    Description:
        - This command sets or queries the user palette graticule color. It assigns the
          hue-lightness-saturation triplet to be used for the graticule color for the user palette.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:COLOr:PALEtte:USEr:GRAticule?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:COLOr:PALEtte:USEr:GRAticule?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:COLOr:PALEtte:USEr:GRAticule value`` command.

    SCPI Syntax:
        ```
        - DISplay:COLOr:PALEtte:USEr:GRAticule <NR1>,<NR1>,<NR1>
        - DISplay:COLOr:PALEtte:USEr:GRAticule?
        ```

    Info:
        - ``<NR1>`` Hue. Range of 0 to 360.
        - ``<NR1>`` Lightness. Range of 0 to 100.
        - ``<NR1>`` Saturation. Range of 0 to 100.
    """


class DisplayColorPaletteUserChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:COLOr:PALEtte:USEr:CH<x>`` command.

    Description:
        - This command sets or queries the hue-lightness-saturation (HLS) triplet to be used for the
          specified channel color for the user palette. The channel is specified by x. The value of
          x can range from 1 through 4.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:COLOr:PALEtte:USEr:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:COLOr:PALEtte:USEr:CH<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:COLOr:PALEtte:USEr:CH<x> value`` command.

    SCPI Syntax:
        ```
        - DISplay:COLOr:PALEtte:USEr:CH<x> <NR1>,<NR1>,<NR1>
        - DISplay:COLOr:PALEtte:USEr:CH<x>?
        ```

    Info:
        - ``<NR1>`` Hue. Range of 0 to 360.
        - ``<NR1>`` Lightness. Range of 0 to 100.
        - ``<NR1>`` Saturation. Range of 0 to 100.
    """


class DisplayColorPaletteUserCaret(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:COLOr:PALEtte:USEr:CARet`` command.

    Description:
        - This command sets or queries the caret color for the user palette. It assigns the HUE,
          light, Saturation (HLS) triplet used for the caret color. The caret is the solid, inverted
          delta positioned on the top graticule line, which indicates the trigger position within
          the waveform record.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:COLOr:PALEtte:USEr:CARet?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:COLOr:PALEtte:USEr:CARet?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:COLOr:PALEtte:USEr:CARet value`` command.

    SCPI Syntax:
        ```
        - DISplay:COLOr:PALEtte:USEr:CARet <NR1>,<NR1>,<NR1>
        - DISplay:COLOr:PALEtte:USEr:CARet?
        ```

    Info:
        - ``<NR1>`` Hue. Range of 0 to 360.
        - ``<NR1>`` Lightness. Range of 0 to 100.
        - ``<NR1>`` Saturation. Range of 0 to 100.
    """


#  pylint: disable=too-many-instance-attributes
class DisplayColorPaletteUser(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:COLOr:PALEtte:USEr`` command.

    Description:
        - This command queries the color palette for group settings. It outputs settings from the
          DISPlay CARET, CH<x>, GRATICULE, HISTOGRAM, MASK, MASKHIGHLIGHT, MATH<x>, and REF<x>
          commands.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:COLOr:PALEtte:USEr?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:COLOr:PALEtte:USEr?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:COLOr:PALEtte:USEr value``
          command.

    SCPI Syntax:
        ```
        - DISplay:COLOr:PALEtte:USEr RESET
        - DISplay:COLOr:PALEtte:USEr?
        ```

    Info:
        - ``RESET`` sets all user palettes to their default values.

    Properties:
        - ``.caret``: The ``DISplay:COLOr:PALEtte:USEr:CARet`` command.
        - ``.ch``: The ``DISplay:COLOr:PALEtte:USEr:CH<x>`` command.
        - ``.graticule``: The ``DISplay:COLOr:PALEtte:USEr:GRAticule`` command.
        - ``.histogram``: The ``DISplay:COLOr:PALEtte:USEr:HIStogram`` command.
        - ``.mask``: The ``DISplay:COLOr:PALEtte:USEr:MASK`` command.
        - ``.maskhighlight``: The ``DISplay:COLOr:PALEtte:USEr:MASKHighlight`` command.
        - ``.math``: The ``DISplay:COLOr:PALEtte:USEr:MATH<x>`` command.
        - ``.ref``: The ``DISplay:COLOr:PALEtte:USEr:REF<x>`` command.
        - ``.waveform``: The ``DISplay:COLOr:PALEtte:USEr:WAVEform`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._caret = DisplayColorPaletteUserCaret(device, f"{self._cmd_syntax}:CARet")
        self._ch: Dict[int, DisplayColorPaletteUserChannel] = DefaultDictPassKeyToFactory(
            lambda x: DisplayColorPaletteUserChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._graticule = DisplayColorPaletteUserGraticule(device, f"{self._cmd_syntax}:GRAticule")
        self._histogram = DisplayColorPaletteUserHistogram(device, f"{self._cmd_syntax}:HIStogram")
        self._mask = DisplayColorPaletteUserMask(device, f"{self._cmd_syntax}:MASK")
        self._maskhighlight = DisplayColorPaletteUserMaskhighlight(
            device, f"{self._cmd_syntax}:MASKHighlight"
        )
        self._math: Dict[int, DisplayColorPaletteUserMathItem] = DefaultDictPassKeyToFactory(
            lambda x: DisplayColorPaletteUserMathItem(device, f"{self._cmd_syntax}:MATH{x}")
        )
        self._ref: Dict[int, DisplayColorPaletteUserRefItem] = DefaultDictPassKeyToFactory(
            lambda x: DisplayColorPaletteUserRefItem(device, f"{self._cmd_syntax}:REF{x}")
        )
        self._waveform = DisplayColorPaletteUserWaveform(device, f"{self._cmd_syntax}:WAVEform")

    @property
    def caret(self) -> DisplayColorPaletteUserCaret:
        """Return the ``DISplay:COLOr:PALEtte:USEr:CARet`` command.

        Description:
            - This command sets or queries the caret color for the user palette. It assigns the HUE,
              light, Saturation (HLS) triplet used for the caret color. The caret is the solid,
              inverted delta positioned on the top graticule line, which indicates the trigger
              position within the waveform record.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:COLOr:PALEtte:USEr:CARet?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:COLOr:PALEtte:USEr:CARet?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:COLOr:PALEtte:USEr:CARet value`` command.

        SCPI Syntax:
            ```
            - DISplay:COLOr:PALEtte:USEr:CARet <NR1>,<NR1>,<NR1>
            - DISplay:COLOr:PALEtte:USEr:CARet?
            ```

        Info:
            - ``<NR1>`` Hue. Range of 0 to 360.
            - ``<NR1>`` Lightness. Range of 0 to 100.
            - ``<NR1>`` Saturation. Range of 0 to 100.
        """
        return self._caret

    @property
    def ch(self) -> Dict[int, DisplayColorPaletteUserChannel]:
        """Return the ``DISplay:COLOr:PALEtte:USEr:CH<x>`` command.

        Description:
            - This command sets or queries the hue-lightness-saturation (HLS) triplet to be used for
              the specified channel color for the user palette. The channel is specified by x. The
              value of x can range from 1 through 4.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:COLOr:PALEtte:USEr:CH<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:COLOr:PALEtte:USEr:CH<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:COLOr:PALEtte:USEr:CH<x> value`` command.

        SCPI Syntax:
            ```
            - DISplay:COLOr:PALEtte:USEr:CH<x> <NR1>,<NR1>,<NR1>
            - DISplay:COLOr:PALEtte:USEr:CH<x>?
            ```

        Info:
            - ``<NR1>`` Hue. Range of 0 to 360.
            - ``<NR1>`` Lightness. Range of 0 to 100.
            - ``<NR1>`` Saturation. Range of 0 to 100.
        """
        return self._ch

    @property
    def graticule(self) -> DisplayColorPaletteUserGraticule:
        """Return the ``DISplay:COLOr:PALEtte:USEr:GRAticule`` command.

        Description:
            - This command sets or queries the user palette graticule color. It assigns the
              hue-lightness-saturation triplet to be used for the graticule color for the user
              palette.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:COLOr:PALEtte:USEr:GRAticule?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:COLOr:PALEtte:USEr:GRAticule?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:COLOr:PALEtte:USEr:GRAticule value`` command.

        SCPI Syntax:
            ```
            - DISplay:COLOr:PALEtte:USEr:GRAticule <NR1>,<NR1>,<NR1>
            - DISplay:COLOr:PALEtte:USEr:GRAticule?
            ```

        Info:
            - ``<NR1>`` Hue. Range of 0 to 360.
            - ``<NR1>`` Lightness. Range of 0 to 100.
            - ``<NR1>`` Saturation. Range of 0 to 100.
        """
        return self._graticule

    @property
    def histogram(self) -> DisplayColorPaletteUserHistogram:
        """Return the ``DISplay:COLOr:PALEtte:USEr:HIStogram`` command.

        Description:
            - This command sets or queries the user palette histogram color. It assigns the
              hue-saturation-lightness (HLS) triplet to be used for the histogram color for the user
              palette.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:COLOr:PALEtte:USEr:HIStogram?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:COLOr:PALEtte:USEr:HIStogram?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:COLOr:PALEtte:USEr:HIStogram value`` command.

        SCPI Syntax:
            ```
            - DISplay:COLOr:PALEtte:USEr:HIStogram <NR1>,<NR1>,<NR1>
            - DISplay:COLOr:PALEtte:USEr:HIStogram?
            ```

        Info:
            - ``<NR1>`` Hue. Range of 0 to 360.
            - ``<NR1>`` Lightness. Range of 0 to 100.
            - ``<NR1>`` Saturation. Range of 0 to 100.
        """
        return self._histogram

    @property
    def mask(self) -> DisplayColorPaletteUserMask:
        """Return the ``DISplay:COLOr:PALEtte:USEr:MASK`` command.

        Description:
            - This command sets or queries the user palette mask color. It assigns the
              hue-lightness-saturation (HLS) color for the mask color for the user palette.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:COLOr:PALEtte:USEr:MASK?``
              query.
            - Using the ``.verify(value)`` method will send the ``DISplay:COLOr:PALEtte:USEr:MASK?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:COLOr:PALEtte:USEr:MASK value`` command.

        SCPI Syntax:
            ```
            - DISplay:COLOr:PALEtte:USEr:MASK <NR1>,<NR1>,<NR1>
            - DISplay:COLOr:PALEtte:USEr:MASK?
            ```

        Info:
            - ``<NR1>`` Hue. Range of 0 to 360.
            - ``<NR1>`` Lightness. Range of 0 to 100.
            - ``<NR1>`` Saturation. Range of 0 to 100.
        """
        return self._mask

    @property
    def maskhighlight(self) -> DisplayColorPaletteUserMaskhighlight:
        """Return the ``DISplay:COLOr:PALEtte:USEr:MASKHighlight`` command.

        Description:
            - This command sets or queries the user palette mask hits color. It assigns the
              hue-lightness-saturation (HLS) triplet to be used for the mask highlight (mask hits)
              color for the user palette.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:COLOr:PALEtte:USEr:MASKHighlight?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:COLOr:PALEtte:USEr:MASKHighlight?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:COLOr:PALEtte:USEr:MASKHighlight value`` command.

        SCPI Syntax:
            ```
            - DISplay:COLOr:PALEtte:USEr:MASKHighlight <NR1>,<NR1>,<NR1>
            - DISplay:COLOr:PALEtte:USEr:MASKHighlight?
            ```

        Info:
            - ``<NR1>`` Hue. Range of 0 to 360.
            - ``<NR1>`` Lightness. Range of 0 to 100.
            - ``<NR1>`` Saturation. Range of 0 to 100.
        """
        return self._maskhighlight

    @property
    def math(self) -> Dict[int, DisplayColorPaletteUserMathItem]:
        """Return the ``DISplay:COLOr:PALEtte:USEr:MATH<x>`` command.

        Description:
            - This command sets or queries the user palette math colors. It assigns the
              hue-lightness-saturation (HLS) triplet to be used for the specified math waveform for
              the user palette. The math waveform is specified by x. The value of x can range from 1
              through 4.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:COLOr:PALEtte:USEr:MATH<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:COLOr:PALEtte:USEr:MATH<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:COLOr:PALEtte:USEr:MATH<x> value`` command.

        SCPI Syntax:
            ```
            - DISplay:COLOr:PALEtte:USEr:MATH<x> <NR1>,<NR1>,<NR1>
            - DISplay:COLOr:PALEtte:USEr:MATH<x>?
            ```

        Info:
            - ``<NR1>`` Hue. Range of 0 to 360.
            - ``<NR1>`` Lightness. Range of 0 to 100.
            - ``<NR1>`` Saturation. Range of 0 to 100.
        """
        return self._math

    @property
    def ref(self) -> Dict[int, DisplayColorPaletteUserRefItem]:
        """Return the ``DISplay:COLOr:PALEtte:USEr:REF<x>`` command.

        Description:
            - This command sets or queries the user palette reference colors assigned to the
              reference waveforms. It assigns the hue-lightness-saturation (HLS) triplet to be used
              for the specified reference waveform color for the user palette. The reference
              waveform is specified by x. The value of x can range from 1 through 4.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:COLOr:PALEtte:USEr:REF<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:COLOr:PALEtte:USEr:REF<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:COLOr:PALEtte:USEr:REF<x> value`` command.

        SCPI Syntax:
            ```
            - DISplay:COLOr:PALEtte:USEr:REF<x> <NR1>,<NR1>,<NR1>
            - DISplay:COLOr:PALEtte:USEr:REF<x>?
            ```

        Info:
            - ``<NR1>`` Hue. Range of 0 to 360.
            - ``<NR1>`` Lightness. Range of 0 to 100.
            - ``<NR1>`` Saturation. Range of 0 to 100.
        """
        return self._ref

    @property
    def waveform(self) -> DisplayColorPaletteUserWaveform:
        """Return the ``DISplay:COLOr:PALEtte:USEr:WAVEform`` command.

        Description:
            - This command sets or queries the user palette waveform colors. It assigns the
              hue-lightness-saturation (HLS) triplet to be used for the specified waveform for the
              user palette.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:COLOr:PALEtte:USEr:WAVEform?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:COLOr:PALEtte:USEr:WAVEform?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:COLOr:PALEtte:USEr:WAVEform value`` command.

        SCPI Syntax:
            ```
            - DISplay:COLOr:PALEtte:USEr:WAVEform {HLS|SPECTral|TEMPErature}
            - DISplay:COLOr:PALEtte:USEr:WAVEform?
            ```

        Info:
            - ``HLS`` sets the color of user waveforms to the hue, lightness, and saturation
              specified by the ``DISPLAY:COLOR:PALETTE:USER:WAVEFORM`` commands.
            - ``SPECTral`` sets the color of user waveforms to spectral.
            - ``TEMPErature`` sets the color of user waveforms to temperature.
        """
        return self._waveform


class DisplayColorPaletteRecordview(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:COLOr:PALEtte:RECORDView`` command.

    Description:
        - This command sets or queries the color palette for all record view (non image view)
          waveforms.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:COLOr:PALEtte:RECORDView?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:COLOr:PALEtte:RECORDView?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:COLOr:PALEtte:RECORDView value`` command.

    SCPI Syntax:
        ```
        - DISplay:COLOr:PALEtte:RECORDView {NORMal|MONOGREEN|MONOGRAY|TEMPErature|SPECTral|USEr}
        - DISplay:COLOr:PALEtte:RECORDView?
        ```

    Info:
        - ``NORMal`` colors traces according to their channel. This is the default color palette.
        - ``MONOGREEN`` colors traces green, emulating a traditional instrument color palette.
        - ``MONOGRAY`` colors traces gray, emulating a monochrome instrument.
        - ``TEMPErature`` colors all traces using a multicolored palette, where 'intensity' is
          represented by hue; blue for least frequently hit, red for most frequently hit. All traces
          share this palette.
        - ``SPECTral`` colors all traces using a multicolored palette, where 'intensity' is
          represented by hue; red for least frequently hit, blue for most frequently hit. All traces
          share this palette.
        - ``USEr`` colors all traces using a user-defined palette. All traces share this palette.
    """


class DisplayColorPaletteImageview(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:COLOr:PALEtte:IMAGEView`` command.

    Description:
        - This command sets or queries the color palette for all image view (DPO and WfmDB) traces.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:COLOr:PALEtte:IMAGEView?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:COLOr:PALEtte:IMAGEView?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:COLOr:PALEtte:IMAGEView value``
          command.

    SCPI Syntax:
        ```
        - DISplay:COLOr:PALEtte:IMAGEView {NORMal|MONOGREEN|MONOGRAY|TEMPErature|SPECTral|USEr}
        - DISplay:COLOr:PALEtte:IMAGEView?
        ```

    Info:
        - ``NORMal`` colors traces according to their channel. This is the default color palette.
        - ``MONOGREEN`` colors traces green, emulating a traditional instrument color palette.
        - ``MONOGRAY`` colors traces gray, emulating a monochrome instrument.
        - ``TEMPErature``
        - ``SPECTral``
        - ``USEr``
    """


class DisplayColorPalette(SCPICmdRead):
    """The ``DISplay:COLOr:PALEtte`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:COLOr:PALEtte?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:COLOr:PALEtte?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.imageview``: The ``DISplay:COLOr:PALEtte:IMAGEView`` command.
        - ``.recordview``: The ``DISplay:COLOr:PALEtte:RECORDView`` command.
        - ``.user``: The ``DISplay:COLOr:PALEtte:USEr`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._imageview = DisplayColorPaletteImageview(device, f"{self._cmd_syntax}:IMAGEView")
        self._recordview = DisplayColorPaletteRecordview(device, f"{self._cmd_syntax}:RECORDView")
        self._user = DisplayColorPaletteUser(device, f"{self._cmd_syntax}:USEr")

    @property
    def imageview(self) -> DisplayColorPaletteImageview:
        """Return the ``DISplay:COLOr:PALEtte:IMAGEView`` command.

        Description:
            - This command sets or queries the color palette for all image view (DPO and WfmDB)
              traces.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:COLOr:PALEtte:IMAGEView?``
              query.
            - Using the ``.verify(value)`` method will send the ``DISplay:COLOr:PALEtte:IMAGEView?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:COLOr:PALEtte:IMAGEView value`` command.

        SCPI Syntax:
            ```
            - DISplay:COLOr:PALEtte:IMAGEView {NORMal|MONOGREEN|MONOGRAY|TEMPErature|SPECTral|USEr}
            - DISplay:COLOr:PALEtte:IMAGEView?
            ```

        Info:
            - ``NORMal`` colors traces according to their channel. This is the default color
              palette.
            - ``MONOGREEN`` colors traces green, emulating a traditional instrument color palette.
            - ``MONOGRAY`` colors traces gray, emulating a monochrome instrument.
            - ``TEMPErature``
            - ``SPECTral``
            - ``USEr``
        """
        return self._imageview

    @property
    def recordview(self) -> DisplayColorPaletteRecordview:
        """Return the ``DISplay:COLOr:PALEtte:RECORDView`` command.

        Description:
            - This command sets or queries the color palette for all record view (non image view)
              waveforms.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:COLOr:PALEtte:RECORDView?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:COLOr:PALEtte:RECORDView?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:COLOr:PALEtte:RECORDView value`` command.

        SCPI Syntax:
            ```
            - DISplay:COLOr:PALEtte:RECORDView {NORMal|MONOGREEN|MONOGRAY|TEMPErature|SPECTral|USEr}
            - DISplay:COLOr:PALEtte:RECORDView?
            ```

        Info:
            - ``NORMal`` colors traces according to their channel. This is the default color
              palette.
            - ``MONOGREEN`` colors traces green, emulating a traditional instrument color palette.
            - ``MONOGRAY`` colors traces gray, emulating a monochrome instrument.
            - ``TEMPErature`` colors all traces using a multicolored palette, where 'intensity' is
              represented by hue; blue for least frequently hit, red for most frequently hit. All
              traces share this palette.
            - ``SPECTral`` colors all traces using a multicolored palette, where 'intensity' is
              represented by hue; red for least frequently hit, blue for most frequently hit. All
              traces share this palette.
            - ``USEr`` colors all traces using a user-defined palette. All traces share this
              palette.
        """
        return self._recordview

    @property
    def user(self) -> DisplayColorPaletteUser:
        """Return the ``DISplay:COLOr:PALEtte:USEr`` command.

        Description:
            - This command queries the color palette for group settings. It outputs settings from
              the DISPlay CARET, CH<x>, GRATICULE, HISTOGRAM, MASK, MASKHIGHLIGHT, MATH<x>, and
              REF<x> commands.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:COLOr:PALEtte:USEr?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:COLOr:PALEtte:USEr?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:COLOr:PALEtte:USEr value``
              command.

        SCPI Syntax:
            ```
            - DISplay:COLOr:PALEtte:USEr RESET
            - DISplay:COLOr:PALEtte:USEr?
            ```

        Info:
            - ``RESET`` sets all user palettes to their default values.

        Sub-properties:
            - ``.caret``: The ``DISplay:COLOr:PALEtte:USEr:CARet`` command.
            - ``.ch``: The ``DISplay:COLOr:PALEtte:USEr:CH<x>`` command.
            - ``.graticule``: The ``DISplay:COLOr:PALEtte:USEr:GRAticule`` command.
            - ``.histogram``: The ``DISplay:COLOr:PALEtte:USEr:HIStogram`` command.
            - ``.mask``: The ``DISplay:COLOr:PALEtte:USEr:MASK`` command.
            - ``.maskhighlight``: The ``DISplay:COLOr:PALEtte:USEr:MASKHighlight`` command.
            - ``.math``: The ``DISplay:COLOr:PALEtte:USEr:MATH<x>`` command.
            - ``.ref``: The ``DISplay:COLOr:PALEtte:USEr:REF<x>`` command.
            - ``.waveform``: The ``DISplay:COLOr:PALEtte:USEr:WAVEform`` command.
        """
        return self._user


class DisplayColorMathcolor(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:COLOr:MATHCOLOr`` command.

    Description:
        - This command sets or queries the color to be used for math traces, either in the standard
          palette's nominal Math color, or according to the color of the source waveform. This
          command is equivalent to selecting Display Setup from the Display menu and then choosing
          the Colors tab.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:COLOr:MATHCOLOr?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:COLOr:MATHCOLOr?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:COLOr:MATHCOLOr value``
          command.

    SCPI Syntax:
        ```
        - DISplay:COLOr:MATHCOLOr {DEFAULT|INHERIT}
        - DISplay:COLOr:MATHCOLOr?
        ```

    Info:
        - ``DEFAULT`` sets color math traces in nominal palette math color, which is red.
        - ``INHERIT`` sets color math traces in the source waveform color. Math waveforms are drawn
          in the same color as their primary source waveform.
    """


class DisplayColor(SCPICmdRead):
    """The ``DISplay:COLOr`` command.

    Description:
        - This query-only command returns the settings from the PALETTE, MATHCOLOR and REFCOLOR
          commands. This is equivalent to selecting Colors from the Display menu.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:COLOr?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:COLOr?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:COLOr?
        ```

    Properties:
        - ``.mathcolor``: The ``DISplay:COLOr:MATHCOLOr`` command.
        - ``.palette``: The ``DISplay:COLOr:PALEtte`` command tree.
        - ``.refcolor``: The ``DISplay:COLOr:REFCOLOr`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mathcolor = DisplayColorMathcolor(device, f"{self._cmd_syntax}:MATHCOLOr")
        self._palette = DisplayColorPalette(device, f"{self._cmd_syntax}:PALEtte")
        self._refcolor = DisplayColorRefcolor(device, f"{self._cmd_syntax}:REFCOLOr")

    @property
    def mathcolor(self) -> DisplayColorMathcolor:
        """Return the ``DISplay:COLOr:MATHCOLOr`` command.

        Description:
            - This command sets or queries the color to be used for math traces, either in the
              standard palette's nominal Math color, or according to the color of the source
              waveform. This command is equivalent to selecting Display Setup from the Display menu
              and then choosing the Colors tab.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:COLOr:MATHCOLOr?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:COLOr:MATHCOLOr?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:COLOr:MATHCOLOr value``
              command.

        SCPI Syntax:
            ```
            - DISplay:COLOr:MATHCOLOr {DEFAULT|INHERIT}
            - DISplay:COLOr:MATHCOLOr?
            ```

        Info:
            - ``DEFAULT`` sets color math traces in nominal palette math color, which is red.
            - ``INHERIT`` sets color math traces in the source waveform color. Math waveforms are
              drawn in the same color as their primary source waveform.
        """
        return self._mathcolor

    @property
    def palette(self) -> DisplayColorPalette:
        """Return the ``DISplay:COLOr:PALEtte`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:COLOr:PALEtte?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:COLOr:PALEtte?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.imageview``: The ``DISplay:COLOr:PALEtte:IMAGEView`` command.
            - ``.recordview``: The ``DISplay:COLOr:PALEtte:RECORDView`` command.
            - ``.user``: The ``DISplay:COLOr:PALEtte:USEr`` command.
        """
        return self._palette

    @property
    def refcolor(self) -> DisplayColorRefcolor:
        """Return the ``DISplay:COLOr:REFCOLOr`` command.

        Description:
            - This command sets or queries the color to be used for reference traces, either in the
              standard palette's nominal REF color or according to the color of the source waveform.
              This command is equivalent to selecting Display Setup from the Display menu and then
              choosing the Colors tab.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:COLOr:REFCOLOr?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:COLOr:REFCOLOr?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:COLOr:REFCOLOr value``
              command.

        SCPI Syntax:
            ```
            - DISplay:COLOr:REFCOLOr {DEFAULT|INHERIT}
            - DISplay:COLOr:REFCOLOr?
            ```

        Info:
            - ``DEFAULT`` assigns color reference traces to the nominal palette reference color,
              which is off-white.
            - ``INHERIT`` assigns color reference traces to the source waveform color.
        """
        return self._refcolor


class DisplayClock(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:CLOCk`` command.

    Description:
        - This command specifies whether the oscilloscope displays the date and time. The query form
          of this command returns an ON (1) or an OFF (0).

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:CLOCk?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:CLOCk value`` command.

    SCPI Syntax:
        ```
        - DISplay:CLOCk {ON|OFF|<NR1>}
        - DISplay:CLOCk?
        ```

    Info:
        - ``ON`` enables the display of date and time.
        - ``OFF`` disables the display of date and time.
        - ``<NR1>`` = 0 disables the display of date and time; any other value enables the display
          of date and time.
    """


#  pylint: disable=too-many-instance-attributes
class Display(SCPICmdRead):
    """The ``DISplay`` command.

    Description:
        - This query-only command returns the current Display settings.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay?
        ```

    Properties:
        - ``.clock``: The ``DISplay:CLOCk`` command.
        - ``.color``: The ``DISplay:COLOr`` command.
        - ``.data``: The ``DISplay:DATa`` command.
        - ``.deskew``: The ``DISplay:DESKew`` command.
        - ``.digital``: The ``DISplay:DIGital`` command tree.
        - ``.dpojetplot``: The ``DISplay:DPOJETPlot`` command.
        - ``.filter``: The ``DISplay:FILTer`` command.
        - ``.format``: The ``DISplay:FORMat`` command.
        - ``.graticule``: The ``DISplay:GRAticule`` command.
        - ``.intensity``: The ``DISplay:INTENSITy`` command.
        - ``.persistence``: The ``DISplay:PERSistence`` command.
        - ``.screentext``: The ``DISplay:SCREENTExt`` command.
        - ``.showremote``: The ``DISplay:SHOWREmote`` command.
        - ``.style``: The ``DISplay:STYle`` command.
        - ``.trigbar``: The ``DISplay:TRIGBar`` command.
        - ``.trigt``: The ``DISplay:TRIGT`` command.
        - ``.varpersist``: The ``DISplay:VARpersist`` command.
        - ``.waveform``: The ``DISplay:WAVEform`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "DISplay") -> None:
        super().__init__(device, cmd_syntax)
        self._clock = DisplayClock(device, f"{self._cmd_syntax}:CLOCk")
        self._color = DisplayColor(device, f"{self._cmd_syntax}:COLOr")
        self._data = DisplayData(device, f"{self._cmd_syntax}:DATa")
        self._deskew = DisplayDeskew(device, f"{self._cmd_syntax}:DESKew")
        self._digital = DisplayDigital(device, f"{self._cmd_syntax}:DIGital")
        self._dpojetplot = DisplayDpojetplot(device, f"{self._cmd_syntax}:DPOJETPlot")
        self._filter = DisplayFilter(device, f"{self._cmd_syntax}:FILTer")
        self._format = DisplayFormat(device, f"{self._cmd_syntax}:FORMat")
        self._graticule = DisplayGraticule(device, f"{self._cmd_syntax}:GRAticule")
        self._intensity = DisplayIntensity(device, f"{self._cmd_syntax}:INTENSITy")
        self._persistence = DisplayPersistence(device, f"{self._cmd_syntax}:PERSistence")
        self._screentext = DisplayScreentext(device, f"{self._cmd_syntax}:SCREENTExt")
        self._showremote = DisplayShowremote(device, f"{self._cmd_syntax}:SHOWREmote")
        self._style = DisplayStyle(device, f"{self._cmd_syntax}:STYle")
        self._trigbar = DisplayTrigbar(device, f"{self._cmd_syntax}:TRIGBar")
        self._trigt = DisplayTrigt(device, f"{self._cmd_syntax}:TRIGT")
        self._varpersist = DisplayVarpersist(device, f"{self._cmd_syntax}:VARpersist")
        self._waveform = DisplayWaveform(device, f"{self._cmd_syntax}:WAVEform")

    @property
    def clock(self) -> DisplayClock:
        """Return the ``DISplay:CLOCk`` command.

        Description:
            - This command specifies whether the oscilloscope displays the date and time. The query
              form of this command returns an ON (1) or an OFF (0).

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:CLOCk?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:CLOCk value`` command.

        SCPI Syntax:
            ```
            - DISplay:CLOCk {ON|OFF|<NR1>}
            - DISplay:CLOCk?
            ```

        Info:
            - ``ON`` enables the display of date and time.
            - ``OFF`` disables the display of date and time.
            - ``<NR1>`` = 0 disables the display of date and time; any other value enables the
              display of date and time.
        """
        return self._clock

    @property
    def color(self) -> DisplayColor:
        """Return the ``DISplay:COLOr`` command.

        Description:
            - This query-only command returns the settings from the PALETTE, MATHCOLOR and REFCOLOR
              commands. This is equivalent to selecting Colors from the Display menu.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:COLOr?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:COLOr?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:COLOr?
            ```

        Sub-properties:
            - ``.mathcolor``: The ``DISplay:COLOr:MATHCOLOr`` command.
            - ``.palette``: The ``DISplay:COLOr:PALEtte`` command tree.
            - ``.refcolor``: The ``DISplay:COLOr:REFCOLOr`` command.
        """
        return self._color

    @property
    def data(self) -> DisplayData:
        """Return the ``DISplay:DATa`` command.

        Description:
            - The query returns the screen shot from the oscilloscope in block data format, as
              defined in the IEEE 488.2 standard. The first argument is the file format and is
              required. The second option is the screen view. The third option is the palate. If no
              options are specified, the default selections are FULLSCREEN and COLOr. If you want to
              specify the second option, the first option must be specified. For example, if you
              want the screen capture to be INKSaver, you must specify a screen view. BMP,GRA,INKS.

        Usage:
            - Using the ``.query(argument)`` method will send the ``DISplay:DATa? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the ``DISplay:DATa? argument``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:DATa? (BMP| JPEG| PNG | TIFF)[,(FULLSCREEN | GRAticule | FULLNOmenu)[,(COLOr | INKSaver | BLACKANDWhite )]]
            ```
        """  # noqa: E501
        return self._data

    @property
    def deskew(self) -> DisplayDeskew:
        """Return the ``DISplay:DESKew`` command.

        Description:
            - This command controls or queries the state of the Display Only button.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:DESKew?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:DESKew?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:DESKew value`` command.

        SCPI Syntax:
            ```
            - DISplay:DESKew {<NR1>|OFF|ON|AUTO}
            - DISplay:DESKew?
            ```

        Info:
            - ``OFF`` sets deskew for the acquisition waveform.
            - ``ON`` sets deskew to deskew the display only.
            - ``<NR1>`` = 0 will deskew the acquisition waveform; any other value will deskew the
              display only.
            - ``AUTO`` automatically selects the deskew setting.
        """
        return self._deskew

    @property
    def digital(self) -> DisplayDigital:
        """Return the ``DISplay:DIGital`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:DIGital?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:DIGital?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.height``: The ``DISplay:DIGital:HEIght`` command.
        """
        return self._digital

    @property
    def dpojetplot(self) -> DisplayDpojetplot:
        """Return the ``DISplay:DPOJETPlot`` command.

        Description:
            - This command queries which DPOJET plot is selected and the screen capture file format.

        Usage:
            - Using the ``.query(argument)`` method will send the ``DISplay:DPOJETPlot? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``DISplay:DPOJETPlot? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:DPOJETPlot? (PLOT1 | PLOT2 | PLOT3 | PLOT4 | SUMMARY)[,(JPEG | JPG | TIF | TIFF | BMP | EMF | PNG)]
            ```
        """  # noqa: E501
        return self._dpojetplot

    @property
    def filter(self) -> DisplayFilter:
        """Return the ``DISplay:FILTer`` command.

        Description:
            - This command sets or queries the type of interpolation to use for the display.
              Filtering only applies to normal-mode acquisition. The ``DISplay:FILTer`` command also
              provides selection for acquisition interpolation type. This command is equivalent to
              selecting Waveform Interpolation from the Display menu.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:FILTer?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:FILTer?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:FILTer value`` command.

        SCPI Syntax:
            ```
            - DISplay:FILTer {LINEAr|SINX}
            - DISplay:FILTer?
            ```

        Info:
            - ``LINEAr`` specifies linear interpolation, where acquired points are connected with
              straight lines.
            - ``SINX`` specifies sin(x)/x interpolation, where acquired points are fit to a curve.
        """
        return self._filter

    @property
    def format(self) -> DisplayFormat:
        """Return the ``DISplay:FORMat`` command.

        Description:
            - This command sets or queries the display format. This command is equivalent to
              selecting Format from the Display menu.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:FORMat?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:FORMat?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:FORMat value`` command.

        SCPI Syntax:
            ```
            - DISplay:FORMat {YT|XY|XYZ}
            - DISplay:FORMat?
            ```

        Info:
            - ``YT`` sets the display to a voltage versus time format and is the default mode.
            - ``XY`` argument displays one waveform against another. The source pairs that make up
              an XY trace are predefined and are listed in the following table. Selecting one source
              causes its corresponding source to be implicitly selected, producing a single trace
              from the two input waveforms.
            - ``XYZ`` argument is available only for four-channel instruments. The argument combines
              channel 1 and channel 2 for X and Y coordinates and uses channel 3 to provide the
              intensity value for the sample. XYZ groups channels 1, 2 and 3 to form a single trace.
              Other channel, math, and reference waveforms are turned off.
        """
        return self._format

    @property
    def graticule(self) -> DisplayGraticule:
        """Return the ``DISplay:GRAticule`` command.

        Description:
            - This command selects or queries the type of graticule that is displayed. This command
              is equivalent to selecting Graticule Style from the Display menu.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:GRAticule?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:GRAticule?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:GRAticule value`` command.

        SCPI Syntax:
            ```
            - DISplay:GRAticule {CROSSHair|FRAme|FULl|GRId|IRE|NTSC|MV|PAL}
            - DISplay:GRAticule?
            ```

        Info:
            - ``CROSSHair`` specifies a frame and cross hairs.
            - ``FRAme`` specifies a frame only.
            - ``FULl`` specifies a frame, a grid and cross hairs.
            - ``GRId`` specifies a frame and grid only.
            - ``IRE`` specifies an IRE video graticule, and sets the vertical scale to 143 mV per
              division.
            - ``NTSC`` specifies an NTSC video graticule (same as the IRE graticule), and sets the
              vertical scale to 133 mV per division.
            - ``MV`` specifies an mV video graticule and sets the vertical scale to 133 mV per
              division. This graticule is used to measure PAL standard video signals.
            - ``PAL`` specifies a PAL video graticule (same as the mV graticule) and sets the
              vertical scale to 133 mV per division. This graticule is used to measure PAL standard
              video signals.
        """
        return self._graticule

    @property
    def intensity(self) -> DisplayIntensity:
        """Return the ``DISplay:INTENSITy`` command.

        Description:
            - This query-only command returns the waveform saturation level and screen saver
              settings.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:INTENSITy?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:INTENSITy?
            ```

        Sub-properties:
            - ``.autobright``: The ``DISplay:INTENSITy:AUTOBright`` command.
            - ``.backlight``: The ``DISplay:INTENSITy:BACKLight`` command.
            - ``.custompct``: The ``DISplay:INTENSITy:CUSTOMPct`` command.
            - ``.screensaver``: The ``DISplay:INTENSITy:SCREENSAVER`` command.
            - ``.screensaverdelay``: The ``DISplay:INTENSITy:SCREENSAVERDELAY`` command.
            - ``.waveform``: The ``DISplay:INTENSITy:WAVEform`` command tree.
        """
        return self._intensity

    @property
    def persistence(self) -> DisplayPersistence:
        """Return the ``DISplay:PERSistence`` command.

        Description:
            - This command sets or queries the persistence aspect of the display. This affects the
              display only and is equivalent to selecting Display Persistence from the Display menu.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PERSistence?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:PERSistence?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:PERSistence value``
              command.

        SCPI Syntax:
            ```
            - DISplay:PERSistence {OFF|INFPersist|VARpersist}
            - DISplay:PERSistence?
            ```

        Info:
            - ``OFF`` disables the persistence aspect of the display.
            - ``INFPersist`` sets a display mode where any pixels, once touched by samples, remain
              set until cleared by a mode change.
            - ``VARPersist`` sets a display mode where set pixels are gradually dimmed.

        Sub-properties:
            - ``.reset``: The ``DISplay:PERSistence:RESET`` command.
        """
        return self._persistence

    @property
    def screentext(self) -> DisplayScreentext:
        """Return the ``DISplay:SCREENTExt`` command.

        Description:
            - This query-only command returns all screen text settings.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:SCREENTExt?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:SCREENTExt?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:SCREENTExt?
            ```

        Sub-properties:
            - ``.label``: The ``DISplay:SCREENTExt:LABel<x>`` command.
            - ``.state``: The ``DISplay:SCREENTExt:STATE`` command.
        """
        return self._screentext

    @property
    def showremote(self) -> DisplayShowremote:
        """Return the ``DISplay:SHOWREmote`` command.

        Description:
            - This command sets or queries the state of the remote display feature and is equivalent
              to selecting Display Remote from the Display menu. The query form of this command
              returns ON (1) or OFF (0). This feature allows you to view waveforms and other
              graticule data on a remote display using remote control software like VNC (Virtual
              Network Computing) or Symantec pcAnywhere.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:SHOWREmote?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:SHOWREmote?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:SHOWREmote value`` command.

        SCPI Syntax:
            ```
            - DISplay:SHOWREmote {ON|OFF|<NR1>}
            - DISplay:SHOWREmote?
            ```

        Info:
            - ``<NR1>`` = 0 disables remote display of waveform and other graticule data; any other
              value enables remote display of waveform and other graticule data.
            - ``ON`` enables the remote display of waveform and other graticule data.
            - ``OFF`` disables the remote display of waveform and other graticule data.
        """
        return self._showremote

    @property
    def style(self) -> DisplayStyle:
        """Return the ``DISplay:STYle`` command.

        Description:
            - This command sets or queries how the data is displayed for normal and FastAcq modes.
              This command is equivalent to selecting Display Style from the Display menu and
              choosing a style.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:STYle?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:STYle?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:STYle value`` command.

        SCPI Syntax:
            ```
            - DISplay:STYle {DOTs|INTENSIFied|VECtors}
            - DISplay:STYle?
            ```

        Info:
            - ``DOTs`` displays individual data points. New points immediately replace old ones.
            - ``INTENSIFied`` causes the display to show interpolated samples with dark spaces (Only
              the 'real' samples are displayed).
            - ``VECtors`` connects adjacent data points. New points immediately replace old ones.
        """
        return self._style

    @property
    def trigbar(self) -> DisplayTrigbar:
        """Return the ``DISplay:TRIGBar`` command.

        Description:
            - This command controls or queries the display of the trigger-level indicator bars.
              Indicator bars show where the trigger voltage level is set. The instrument will only
              display the bar if the associated trigger source is also displayed. If both a main and
              a delayed trigger are displayed, then two bars will appear. One will accompany each
              source. If a logic trigger is selected, then multiple bars might appear. One will show
              the upper threshold and one will show the lower threshold. This command is equivalent
              to selecting Display Setup from the Display menu and then choosing the Objects tab.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:TRIGBar?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:TRIGBar?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:TRIGBar value`` command.

        SCPI Syntax:
            ```
            - DISplay:TRIGBar {OFF|SHORt|LONG}
            - DISplay:TRIGBar?
            ```

        Info:
            - ``OFF`` removes the trigger indicator bar from the display.
            - ``SHORt`` displays, as the indicator, a short arrow at the right side of the graticule
              for each displayed trigger signal.
            - ``LONG`` displays, as the indicator, a horizontal line across the width of the
              graticule for each displayed trigger signal.
        """
        return self._trigbar

    @property
    def trigt(self) -> DisplayTrigt:
        """Return the ``DISplay:TRIGT`` command.

        Description:
            - This command controls or queries the display of the trigger T. The trigger T shows
              where the trigger occurred on the waveform.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:TRIGT?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:TRIGT?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:TRIGT value`` command.

        SCPI Syntax:
            ```
            - DISplay:TRIGT {ON|OFF|<NR1>}
            - DISplay:TRIGT?
            ```

        Info:
            - ``<NR1>`` = 0 disables the trigger T; any other value displays the trigger T.
            - ``OFF`` removes the trigger indicator T from the display.
            - ``ON`` displays a T at the trigger point.
        """
        return self._trigt

    @property
    def varpersist(self) -> DisplayVarpersist:
        """Return the ``DISplay:VARpersist`` command.

        Description:
            - This command sets or queries display persistence decay time, which is the approximate
              decay time for a freshly struck persistence sample.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:VARpersist?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:VARpersist?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:VARpersist value`` command.

        SCPI Syntax:
            ```
            - DISplay:VARpersist <NR3>
            - DISplay:VARpersist?
            ```

        Info:
            - ``<NR3>`` indicates the persistence decay time and ranges from 0.5 to 100.
        """
        return self._varpersist

    @property
    def waveform(self) -> DisplayWaveform:
        """Return the ``DISplay:WAVEform`` command.

        Description:
            - This command globally enables or disables the waveform display. When disabled, the
              waveform is still acquired and held in memory, but it is not drawn to the screen.
              Disabling the waveform display may improve processing speed.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEform?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEform?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:WAVEform value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEform {ON|OFF|<NR1>}
            - DISplay:WAVEform?
            ```

        Info:
            - ``<NR1>`` enables or disables the waveform display. 0 disables the waveform display;
              any other value enables the waveform display.
            - ``ON`` enables the waveform display.
            - ``OFF`` disables the waveform display.
        """
        return self._waveform
