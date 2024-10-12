# pylint: disable=line-too-long
"""The mask commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - MASK:AUTOAdjust {ON|OFF|<NR1>}
    - MASK:AUTOAdjust:HDELTA {<NR3>}
    - MASK:AUTOAdjust:HDELTA?
    - MASK:AUTOAdjust:VDELTA {<NR3>}
    - MASK:AUTOAdjust:VDELTA?
    - MASK:AUTOAdjust?
    - MASK:AUTOSet:AUTOAdjust {ON|OFF|<NR1>}
    - MASK:AUTOSet:AUTOAdjust?
    - MASK:AUTOSet:HPOS {ON|OFF|<NR1>}
    - MASK:AUTOSet:HPOS?
    - MASK:AUTOSet:HSCAle {ON|OFF|<NR1>}
    - MASK:AUTOSet:HSCAle?
    - MASK:AUTOSet:MODe {MANual|AUTO}
    - MASK:AUTOSet:MODe?
    - MASK:AUTOSet:OFFSETAdj {ON|OFF|<NR1>}
    - MASK:AUTOSet:OFFSETAdj?
    - MASK:AUTOSet:STANdard {ATATXG<x>|ATARXG<x>|CLOCKCoax|CLOCKSymmetrical|D<x>|DS0Contra|DS0Double|DS0Single|DS0Timing|DS1|DS1A|DS1C|DS2RATESymmetrical|DS2RATECoax|DS2|DS3|DS4NA|DS4NA_Max|E1Symmetrical|E1Coax|E2|E3|E4_0|E4_1|ENET100FX|ENET100STP|ENET100UTP|ENET1250|ENET1000BCX_NTP2|ENET1000BCX_ATP2|ENET1000BCX_ATP3|ENETXAUI_Near|ENETXAUI_Far|FC133|FC266|FC531|FC1063|FC1063Draft|FC2125|FC133E|FC266E|FC531E|FC1063E|FC1063E_NBT|FC1063E_NDT|FC1063E_NGT|FC1063E_ABT|FC1063E_ADT|FC1063E_AGT|FC1063E_ABR|FC1063E_ADR|FC1063E_AGR|FC2125E_NBT|FC2125E_NDT|FC2125E_NGT|FC2125E_ABT|FC2125E_ADT|FC2125E_AGT|FC2125E_ABR|FC2125E_ADR|FC2125E_AGR|FC4250E_ABR|FC4250E_ABT|FC4250E_ADR|FC4250E_ADT|FC4250E_AGR|FC4250E_AGT|FC4250E_NBT|FC4250E_NDT|FC4250E_NGT|FST1|FST2|FST3|FST4|FST5|FST6|FW1394BS400BT1|FW1394BS400BT2|FW1394BS800BT1|FW1394BS800BT2|FW1394BS1600BT1|FW1394BS1600BT2|FW1394BS400B|FW1394BS800B|FW1394BS1600B|G703DS1|G703DS3|HST<x>|INF2_5G|INF2_5GE|NONe|OC1|OC3|OC12|OC48|OC48_FEC|RATE32Mbit|RATE97Mbit|RIO_DRV500M|RIO_DRV750M|RIO_DRV1G|RIO_DRV1_5G|RIO_DRV2G|RIO_EDRV500M|RIO_EDRV750M|RIO_EDRV1G|RIO_EDRV1_5G|RIO_EDRV2G|RIO_RCV500M|RIO_RCV750M|RIO_RCV1G|RIO_RCV1_5G|RIO_RCV2G|RIO_SERIAL_1G|RIO_SERIAL_2G|RIO_SERIAL_3G|SFI5_XMITADATA2|SFI5_XMITCDATA2|SFI5_XMITACLK2|SFI5_XMITCCLK2|SFI5_RCVBDATA2|SFI5_RCVDDATA2|SFI5_RCVBCLK2|SFI5_RCVDCLK2|SFI5_XMITADATA3|SFI5_XMITCDATA3|SFI5_XMITACLK3|SFI5_XMITCCLK3|SFI5_RCVBDATA3|SFI5_RCVDDATA3|SFI5_RCVBCLK3|SFI5_RCVDCLK3|PCIEXPRESS_Xmit|PCIEXPRESS_Rcv|SAS1_5_IR|SAS1_5_CR|SAS1_5_XR|SAS1_5_IR_AASJ|SAS1_5_CR_AASJ|SAS1_5_XR_AASJ|SAS1_5_SATA|SAS3_0_IR|SAS3_0_CR|SAS3_0_XR|SAS3_0_IR_AASJ|SAS3_0_CR_AASJ|SAS3_0_XR_AASJ|SAS3_0_SATA|STM0_1|STM0_0|STM0_HDBX|STM1E_0|STM1E_1|STS1Pulse|STS1Eye|STS3|STS3_Max|TFI5_2|TFI5_3|USERMask|VIDEO270|VIDEO292M|VIDEO360|VSROC192}
    - MASK:AUTOSet:STANdard?
    - MASK:AUTOSet:TRIGger {ON|OFF|<NR1>}
    - MASK:AUTOSet:TRIGger?
    - MASK:AUTOSet:USER:ONE <NR3>
    - MASK:AUTOSet:USER:ONE?
    - MASK:AUTOSet:USER:TYPe {ABSolute|NORMALIZed}
    - MASK:AUTOSet:USER:TYPe?
    - MASK:AUTOSet:USER:ZERo <NR3>
    - MASK:AUTOSet:USER:ZERo?
    - MASK:AUTOSet:VPOS {ON|OFF|<NR1>}
    - MASK:AUTOSet:VPOS?
    - MASK:AUTOSet:VSCAle {ON|OFF|<NR1>}
    - MASK:AUTOSet:VSCAle?
    - MASK:COPy:USER
    - MASK:COUNt RESET
    - MASK:COUNt:FAILURES?
    - MASK:COUNt:HITS?
    - MASK:COUNt:SEG<m>:HITS?
    - MASK:COUNt:STATE {ON|OFF|<NR1>}
    - MASK:COUNt:STATE?
    - MASK:COUNt:TESTS?
    - MASK:COUNt:TOTal?
    - MASK:COUNt:VIOLATIONS?
    - MASK:COUNt:WAVEFORMS?
    - MASK:DISplay {ON|OFF|<NR1>}
    - MASK:DISplay?
    - MASK:FILTer {ON|OFF|<NR1>}
    - MASK:FILTer:ORR:VERT_INDEX? CH<x>
    - MASK:FILTer?
    - MASK:HIGHLIGHTHits {ON|OFF|<NR1>}
    - MASK:HIGHLIGHTHits?
    - MASK:INVert {ON|OFF|<NR1>}
    - MASK:LOCk {ON|OFF|<NR1>}
    - MASK:LOCk?
    - MASK:MARgin:PERCent <NR3>
    - MASK:MARgin:PERCent?
    - MASK:MARgin:STATE {ON|OFF|<NR1>}
    - MASK:MARgin:STATE?
    - MASK:MASKPRE:AMPlitude <NR3>
    - MASK:MASKPRE:AMPlitude?
    - MASK:MASKPRE:HSCAle <NR3>
    - MASK:MASKPRE:HSCAle?
    - MASK:MASKPRE:HTRIGPOS <NR3>
    - MASK:MASKPRE:HTRIGPOS?
    - MASK:MASKPRE:PATTERNBITS <NR1>
    - MASK:MASKPRE:PATTERNBITS?
    - MASK:MASKPRE:PRESAMPBITS <NR1>
    - MASK:MASKPRE:PRESAMPBITS?
    - MASK:MASKPRE:RECOrdlength <NR1>
    - MASK:MASKPRE:RECOrdlength?
    - MASK:MASKPRE:SERIALTRIG {AMI|HDB3|B3ZS|B6ZS|B8ZS|CMI|NRZ|MLT3|EDGE}
    - MASK:MASKPRE:SERIALTRIG?
    - MASK:MASKPRE:TRIGTOSAMP <NR3>
    - MASK:MASKPRE:TRIGTOSAMP?
    - MASK:MASKPRE:VOFFSet <NR3>
    - MASK:MASKPRE:VOFFSet?
    - MASK:MASKPRE:VPOS <NR3>
    - MASK:MASKPRE:VPOS?
    - MASK:MASKPRE:VSCAle <NR3>
    - MASK:MASKPRE:VSCAle?
    - MASK:MASKPRE:WIDth <NR3>
    - MASK:MASKPRE:WIDth?
    - MASK:POLarity {BOTh|NEGAtive|POSITIVe}
    - MASK:POLarity?
    - MASK:SEG<m> DELEte
    - MASK:SEG<m>:NR_Pt?
    - MASK:SEG<m>:POINTS <NR3>,<NR3>[,<NR3>,<NR3>]
    - MASK:SEG<m>:POINTS?
    - MASK:SOUrce {CH<x>|MATH<x>|REF<x>}
    - MASK:SOUrce?
    - MASK:STANdard {ATARXG<x>|ATATXG1|ATATXG2|ATATXG3|CLOCKCoax|CLOCKSymmetrical|D<x>|DS0Contra|DS0Double|DS0Single|DS0Timing|DS1|DS1A|DS1C|DS2|DS2RATECoax|DS2RATESymmetrical|DS3|DS4NA|DS4NA_Max|E1Coax|E1Symmetrical|E2|E3|E4_1|E4_0|ENET1000BCX_ATP2|ENET1000BCX_ATP3|ENET1000BCX_NTP2|ENET100FX|ENET100STP|ENET100UTP|ENET1250|ENETXAUI_Far|ENETXAUI_Near|FC1063|FC1063Draft|FC1063E|FC1063E_ABR|FC1063E_ABT|FC1063E_ADR|FC1063E_ADT|FC1063E_AGR|FC1063E_AGT|FC1063E_NBT|FC1063E_NDT|FC1063E_NGT|FC133|FC133E|FC2125|FC2125E_ABR|FC2125E_ABT|FC2125E_ADR|FC2125E_ADT|FC2125E_AGR|FC2125E_AGT|FC2125E_NBT|FC2125E_NDT|FC2125E_NGT|FC266|FC266E|FC4250E_ABR|FC4250E_ABT|FC4250E_ADR|FC4250E_ADT|FC4250E_AGR|FC4250E_AGT|FC4250E_NBT|FC4250E_NDT|FC4250E_NGT|FC531|FC531E|FST1|FST2|FST3|FST4|FST5|FST6|FW1394BS1600B|FW1394BS1600BT1|FW1394BS1600BT2|FW1394BS400B|FW1394BS400BT1|FW1394BS400BT2|FW1394BS800B|FW1394BS800BT1|FW1394BS800BT2|G703DS1|G703DS3|HST<x>|INF2_5G|INF2_5GE|NONe|OC1|OC12|OC3|OC48|OC48_FEC|PCIEXPRESS_Rcv|PCIEXPRESS_Xmit|RATE32Mbit|RATE97Mbit|RIO_DRV1G|RIO_DRV1_5G|RIO_DRV2G|RIO_DRV500M|RIO_DRV500M|RIO_DRV750M|RIO_EDRV1G|RIO_EDRV1_5G|RIO_EDRV2G|RIO_EDRV500M|RIO_EDRV500M|RIO_EDRV750M|RIO_RCV1G|RIO_RCV1_5G|RIO_RCV2G|RIO_RCV500M|RIO_RCV500M|RIO_RCV750M|RIO_SERIAL_1G|RIO_SERIAL_2G|RIO_SERIAL_3G|SFI5_RCVBCLK2|SFI5_RCVBCLK3|SFI5_RCVBDATA2|SFI5_RCVBDATA3|SFI5_RCVDCLK2|SFI5_RCVDCLK3|SFI5_RCVDDATA2|SFI5_RCVDDATA3|SFI5_XMITACLK2|SFI5_XMITACLK3|SFI5_XMITADATA2|SFI5_XMITADATA3|SFI5_XMITCCLK2|SFI5_XMITCCLK3|SFI5_XMITCDATA2|SFI5_XMITCDATA3|STM0_0|STM0_1|STM0_HDBX|STM1E_1|STM1E_0|STS1Eye|STS1Pulse|STS3|STS3_Max|TFI5_2|TFI5_3|USERMask|VIDEO270|VIDEO292M|VIDEO360|VSROC192|SAS1_5_IR|SAS1_5_CR|SAS1_5_XR|SAS1_5_IR_AASJ|SAS1_5_CR_AASJ|SAS1_5_XR_AASJ|SAS1_5_SATA|SAS3_0_IR|SAS3_0_CR|SAS3_0_XR|SAS3_0_IR_AASJ|SAS3_0_CR_AASJ|SAS3_0_XR_AASJ|SAS3_0_SATA}
    - MASK:STANdard?
    - MASK:STOPOnviolation {ON|OFF|<NR1>}
    - MASK:STOPOnviolation?
    - MASK:TESt:AUX:COMPLetion {ON|OFF|<NR1>}
    - MASK:TESt:AUX:COMPLetion?
    - MASK:TESt:AUX:FAILure {ON|OFF|<NR1>}
    - MASK:TESt:AUX:FAILure?
    - MASK:TESt:BEEP:COMPLetion {ON|OFF|<NR1>}
    - MASK:TESt:BEEP:COMPLetion?
    - MASK:TESt:BEEP:FAILure {ON|OFF|<NR1>}
    - MASK:TESt:BEEP:FAILure?
    - MASK:TESt:DELay <NR3>
    - MASK:TESt:DELay?
    - MASK:TESt:HARDCopy {ON|OFF|<NR1>}
    - MASK:TESt:HARDCopy?
    - MASK:TESt:LOG:FAILure {ON|OFF|<NR1>}
    - MASK:TESt:LOG:FAILure?
    - MASK:TESt:REPeat {ON|OFF|<NR1>}
    - MASK:TESt:REPeat?
    - MASK:TESt:SAMple {<NR1>}
    - MASK:TESt:SAMple:THReshold {<NR1>}
    - MASK:TESt:SAMple:THReshold?
    - MASK:TESt:SAMple?
    - MASK:TESt:SAVEWFM {ON|OFF|<NR1>}
    - MASK:TESt:SAVEWFM:FILEName <QString>
    - MASK:TESt:SAVEWFM:FILEName?
    - MASK:TESt:SAVEWFM?
    - MASK:TESt:SRQ:COMPLetion {ON|OFF|<NR1>}
    - MASK:TESt:SRQ:COMPLetion?
    - MASK:TESt:SRQ:FAILure {ON|OFF|<NR1>}
    - MASK:TESt:SRQ:FAILure?
    - MASK:TESt:STATE {ON|OFF|<NR1>}
    - MASK:TESt:STATE?
    - MASK:TESt:STATUS?
    - MASK:TESt:STOP:FAILure {ON|OFF|<NR1>}
    - MASK:TESt:STOP:FAILure?
    - MASK:TESt:THReshold <NR1>
    - MASK:TESt:THReshold?
    - MASK:TESt:WAVEform <NR1>
    - MASK:TESt:WAVEform?
    - MASK:USER:AMPlitude <NR3>
    - MASK:USER:AMPlitude?
    - MASK:USER:BITRate <NR1>
    - MASK:USER:BITRate?
    - MASK:USER:HSCAle <NR3>
    - MASK:USER:HSCAle?
    - MASK:USER:HTRIGPOS <NR3>
    - MASK:USER:HTRIGPOS?
    - MASK:USER:LABel <QString>
    - MASK:USER:LABel?
    - MASK:USER:PATTERNBITS <NR1>
    - MASK:USER:PATTERNBITS?
    - MASK:USER:PRESAMPBITS <NR1>
    - MASK:USER:PRESAMPBITS?
    - MASK:USER:RECOrdlength <NR1>
    - MASK:USER:RECOrdlength?
    - MASK:USER:SEG<m> DELEte
    - MASK:USER:SEG<m>:NR_Pt?
    - MASK:USER:SEG<m>:POINTS <NR3>, <NR3> [, <NR3>, <NR3>]
    - MASK:USER:SEG<m>:POINTS?
    - MASK:USER:TRIGTOSAMP <NR3>
    - MASK:USER:TRIGTOSAMP?
    - MASK:USER:VOFFSet <NR3>
    - MASK:USER:VOFFSet?
    - MASK:USER:VPOS <NR3>
    - MASK:USER:VPOS?
    - MASK:USER:VSCAle <NR3>
    - MASK:USER:VSCAle?
    - MASK:USER:WIDth <NR3>
    - MASK:USER:WIDth?
    - MASK?
    ```
"""  # noqa: E501

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdReadWithArguments,
    SCPICmdWrite,
    SCPICmdWriteNoArguments,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class MaskUserWidth(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:WIDth`` command.

    Description:
        - This command specifies the nominal bit width value, in seconds, to be used for a
          user-defined custom mask. This is the time of one bit of data where bit width = 1 / (data
          rate of the signal). A series of examples showing how to use mask commands for typical
          tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:WIDth?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:WIDth?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:USER:WIDth value`` command.

    SCPI Syntax:
        ```
        - MASK:USER:WIDth <NR3>
        - MASK:USER:WIDth?
        ```

    Info:
        - ``<NR3>`` is a floating point number that indicates the nominal bit width value in
          seconds.
    """


class MaskUserVscale(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:VSCAle`` command.

    Description:
        - This command specifies the nominal value, in volts per division, to be used to vertically
          scale the input channels for a user-defined custom mask. A series of examples showing how
          to use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:VSCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:VSCAle?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:USER:VSCAle value`` command.

    SCPI Syntax:
        ```
        - MASK:USER:VSCAle <NR3>
        - MASK:USER:VSCAle?
        ```

    Info:
        - ``<NR3>`` is a floating point number that sets the nominal vertical scale value for the
          input channels for a user-defined custom mask.
    """


class MaskUserVpos(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:VPOS`` command.

    Description:
        - This command specifies the nominal value, in divisions, to be used to vertically position
          the input channels for a user-defined custom mask. A series of examples showing how to use
          mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:VPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:VPOS?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:USER:VPOS value`` command.

    SCPI Syntax:
        ```
        - MASK:USER:VPOS <NR3>
        - MASK:USER:VPOS?
        ```

    Info:
        - ``<NR3>`` is a floating point number that sets the nominal vertical position value in
          divisions.
    """


class MaskUserVoffset(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:VOFFSet`` command.

    Description:
        - This command specifies the nominal value, in volts, to be used to vertically offset the
          input channels for a user-defined custom mask. A series of examples showing how to use
          mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:VOFFSet?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:VOFFSet?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:USER:VOFFSet value`` command.

    SCPI Syntax:
        ```
        - MASK:USER:VOFFSet <NR3>
        - MASK:USER:VOFFSet?
        ```

    Info:
        - ``<NR3>`` is a floating point number that sets the nominal vertical offset value, in
          volts.
    """


class MaskUserTrigtosamp(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:TRIGTOSAMP`` command.

    Description:
        - This command specifies the nominal time, in seconds, from the (leading edge) trigger
          position to the pulse bit sampling position, to be used for testing with a user-defined
          custom mask. A series of examples showing how to use mask commands for typical tasks is
          included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:TRIGTOSAMP?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:TRIGTOSAMP?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:USER:TRIGTOSAMP value`` command.

    SCPI Syntax:
        ```
        - MASK:USER:TRIGTOSAMP <NR3>
        - MASK:USER:TRIGTOSAMP?
        ```

    Info:
        - ``<NR3>`` is a floating point number that sets the time to the pulse bit sampling
          position.
    """


class MaskUserSegItemPoints(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:SEG<m>:POINTS`` command.

    Description:
        - This command sets or returns the X-Y user coordinates of all points in the specified user
          mask segment. The set form defines new points in the user mask, replacing any existing
          points in the specified user mask segment. It sets or returns the vertices for a
          particular segment in the selected mask. m is an integer that specifies the user mask
          segment number.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:SEG<m>:POINTS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:SEG<m>:POINTS?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:USER:SEG<m>:POINTS value``
          command.

    SCPI Syntax:
        ```
        - MASK:USER:SEG<m>:POINTS <NR3>, <NR3> [, <NR3>, <NR3>]
        - MASK:USER:SEG<m>:POINTS?
        ```

    Info:
        - ``<NR3>`` refers to the coordinates of one of the vertices in the user mask. Each pair of
          numbers represents the horizontal and vertical coordinates of a mask segment vertex. The
          pairs must be listed in a counterclockwise order. If the vertical or horizontal scale or
          position is changed after this command and then the query form of this command is issued,
          the value returned from the instrument will not be the same. If just one pair is input, it
          is ignored and the user mask segment is marked as undefined. The default is not points in
          the user mask segment.
    """


class MaskUserSegItemNrPt(SCPICmdRead):
    """The ``MASK:USER:SEG<m>:NR_Pt`` command.

    Description:
        - This query-only command returns the number of points that make up the specified user mask
          segment. Each mask point consists of a pair of X-Y coordinates. m is an integer that
          specifies a user mask segment number.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:SEG<m>:NR_Pt?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:SEG<m>:NR_Pt?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MASK:USER:SEG<m>:NR_Pt?
        ```
    """


class MaskUserSegItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:SEG<m>`` command.

    Description:
        - This command deletes the specified mask segment from the user mask, whether or not the
          user mask is the current mask. m is an integer that specifies the user mask segment number
          to delete from the user mask.

    Usage:
        - Using the ``.write(value)`` method will send the ``MASK:USER:SEG<m> value`` command.

    SCPI Syntax:
        ```
        - MASK:USER:SEG<m> DELEte
        ```

    Info:
        - ``DELEte`` removes the specified segment from the mask.

    Properties:
        - ``.nr_pt``: The ``MASK:USER:SEG<m>:NR_Pt`` command.
        - ``.points``: The ``MASK:USER:SEG<m>:POINTS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._nr_pt = MaskUserSegItemNrPt(device, f"{self._cmd_syntax}:NR_Pt")
        self._points = MaskUserSegItemPoints(device, f"{self._cmd_syntax}:POINTS")

    @property
    def nr_pt(self) -> MaskUserSegItemNrPt:
        """Return the ``MASK:USER:SEG<m>:NR_Pt`` command.

        Description:
            - This query-only command returns the number of points that make up the specified user
              mask segment. Each mask point consists of a pair of X-Y coordinates. m is an integer
              that specifies a user mask segment number.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:SEG<m>:NR_Pt?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:SEG<m>:NR_Pt?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MASK:USER:SEG<m>:NR_Pt?
            ```
        """
        return self._nr_pt

    @property
    def points(self) -> MaskUserSegItemPoints:
        """Return the ``MASK:USER:SEG<m>:POINTS`` command.

        Description:
            - This command sets or returns the X-Y user coordinates of all points in the specified
              user mask segment. The set form defines new points in the user mask, replacing any
              existing points in the specified user mask segment. It sets or returns the vertices
              for a particular segment in the selected mask. m is an integer that specifies the user
              mask segment number.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:SEG<m>:POINTS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:SEG<m>:POINTS?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:USER:SEG<m>:POINTS value``
              command.

        SCPI Syntax:
            ```
            - MASK:USER:SEG<m>:POINTS <NR3>, <NR3> [, <NR3>, <NR3>]
            - MASK:USER:SEG<m>:POINTS?
            ```

        Info:
            - ``<NR3>`` refers to the coordinates of one of the vertices in the user mask. Each pair
              of numbers represents the horizontal and vertical coordinates of a mask segment
              vertex. The pairs must be listed in a counterclockwise order. If the vertical or
              horizontal scale or position is changed after this command and then the query form of
              this command is issued, the value returned from the instrument will not be the same.
              If just one pair is input, it is ignored and the user mask segment is marked as
              undefined. The default is not points in the user mask segment.
        """
        return self._points


class MaskUserRecordlength(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:RECOrdlength`` command.

    Description:
        - This command specifies the nominal record length to be used for pulse mask testing with a
          user-defined custom mask. A series of examples showing how to use mask commands for
          typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:RECOrdlength?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:RECOrdlength?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:USER:RECOrdlength value`` command.

    SCPI Syntax:
        ```
        - MASK:USER:RECOrdlength <NR1>
        - MASK:USER:RECOrdlength?
        ```

    Info:
        - ``<NR1>`` is an integer that sets the record length value to be used for pulse mask
          testing of a user-defined custom mask.
    """


class MaskUserPresampbits(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:PRESAMPBITS`` command.

    Description:
        - This command sets or returns the number of bits before the (isolated one) pulse leading
          edge in the serial trigger pass/fail testing. For example, DS1 has four leading zeros. The
          query form of this command returns the presample bit value of the displayed mask. The set
          form of this command only affects the user mask, regardless of the current (displayed)
          mask.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:PRESAMPBITS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:PRESAMPBITS?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:USER:PRESAMPBITS value`` command.

    SCPI Syntax:
        ```
        - MASK:USER:PRESAMPBITS <NR1>
        - MASK:USER:PRESAMPBITS?
        ```

    Info:
        - ``<NR1>`` is an integer that sets the number of bits before the trigger pulse.
    """


class MaskUserPatternbits(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:PATTERNBITS`` command.

    Description:
        - This command sets or returns the number of bits used for serial trigger for the User mask
          standard. For example, DS1 requires six bits, four leading zeros, a one, and a trailing
          zero. The query form of this command returns the serial bit value of the displayed mask.
          The set form of this command affects only the User mask, regardless of the current
          (displayed) mask.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:PATTERNBITS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:PATTERNBITS?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:USER:PATTERNBITS value`` command.

    SCPI Syntax:
        ```
        - MASK:USER:PATTERNBITS <NR1>
        - MASK:USER:PATTERNBITS?
        ```

    Info:
        - ``<NR1>`` is an integer that sets the number of bits.
    """


class MaskUserLabel(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:LABel`` command.

    Description:
        - This command specifies a user-defined label for a custom mask.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:LABel?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:USER:LABel value`` command.

    SCPI Syntax:
        ```
        - MASK:USER:LABel <QString>
        - MASK:USER:LABel?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class MaskUserHtrigpos(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:HTRIGPOS`` command.

    Description:
        - This command specifies the nominal trigger position (pulse leading edge), to be used to
          draw a user-defined custom mask, as a fraction of the display width. A series of examples
          showing how to use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:HTRIGPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:HTRIGPOS?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:USER:HTRIGPOS value`` command.

    SCPI Syntax:
        ```
        - MASK:USER:HTRIGPOS <NR3>
        - MASK:USER:HTRIGPOS?
        ```

    Info:
        - ``<NR3>`` is a floating point number in the range of 0.0 to 1.0 that sets the trigger
          points as a fraction of the display width, referenced from the left edge of the graticule.
    """


class MaskUserHscale(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:HSCAle`` command.

    Description:
        - This command specifies the nominal timing resolution, in time/division, to be used to draw
          a user-defined custom mask pulse shape. A series of examples showing how to use mask
          commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:HSCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:HSCAle?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:USER:HSCAle value`` command.

    SCPI Syntax:
        ```
        - MASK:USER:HSCAle <NR3>
        - MASK:USER:HSCAle?
        ```

    Info:
        - ``<NR3>`` is a floating point value that specifies the timing resolution used to a draw a
          user-defined custom mask pulse shape.
    """


class MaskUserBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:BITRate`` command.

    Description:
        - This command sets or returns the bit rate for the user mask.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:BITRate?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:USER:BITRate value`` command.

    SCPI Syntax:
        ```
        - MASK:USER:BITRate <NR1>
        - MASK:USER:BITRate?
        ```

    Info:
        - ``<NR1>`` is a number that sets the bit rate of the user mask in bits per second.
    """


class MaskUserAmplitude(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:AMPlitude`` command.

    Description:
        - This command sets or returns the current mask's nominal pulse amplitude in volts. The
          query form of this command returns the nominal pulse amplitude of the displayed mask. The
          set form of this command affects only the user mask, regardless of the current (displayed)
          mask.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:AMPlitude?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:AMPlitude?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:USER:AMPlitude value`` command.

    SCPI Syntax:
        ```
        - MASK:USER:AMPlitude <NR3>
        - MASK:USER:AMPlitude?
        ```

    Info:
        - ``<NR3>`` is a floating number that sets the nominal pulse amplitude in volts.
    """


#  pylint: disable=too-many-instance-attributes
class MaskUser(SCPICmdRead):
    """The ``MASK:USER`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.amplitude``: The ``MASK:USER:AMPlitude`` command.
        - ``.bitrate``: The ``MASK:USER:BITRate`` command.
        - ``.hscale``: The ``MASK:USER:HSCAle`` command.
        - ``.htrigpos``: The ``MASK:USER:HTRIGPOS`` command.
        - ``.label``: The ``MASK:USER:LABel`` command.
        - ``.patternbits``: The ``MASK:USER:PATTERNBITS`` command.
        - ``.presampbits``: The ``MASK:USER:PRESAMPBITS`` command.
        - ``.recordlength``: The ``MASK:USER:RECOrdlength`` command.
        - ``.seg``: The ``MASK:USER:SEG<m>`` command.
        - ``.trigtosamp``: The ``MASK:USER:TRIGTOSAMP`` command.
        - ``.voffset``: The ``MASK:USER:VOFFSet`` command.
        - ``.vpos``: The ``MASK:USER:VPOS`` command.
        - ``.vscale``: The ``MASK:USER:VSCAle`` command.
        - ``.width``: The ``MASK:USER:WIDth`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._amplitude = MaskUserAmplitude(device, f"{self._cmd_syntax}:AMPlitude")
        self._bitrate = MaskUserBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._hscale = MaskUserHscale(device, f"{self._cmd_syntax}:HSCAle")
        self._htrigpos = MaskUserHtrigpos(device, f"{self._cmd_syntax}:HTRIGPOS")
        self._label = MaskUserLabel(device, f"{self._cmd_syntax}:LABel")
        self._patternbits = MaskUserPatternbits(device, f"{self._cmd_syntax}:PATTERNBITS")
        self._presampbits = MaskUserPresampbits(device, f"{self._cmd_syntax}:PRESAMPBITS")
        self._recordlength = MaskUserRecordlength(device, f"{self._cmd_syntax}:RECOrdlength")
        self._seg: Dict[int, MaskUserSegItem] = DefaultDictPassKeyToFactory(
            lambda x: MaskUserSegItem(device, f"{self._cmd_syntax}:SEG{x}")
        )
        self._trigtosamp = MaskUserTrigtosamp(device, f"{self._cmd_syntax}:TRIGTOSAMP")
        self._voffset = MaskUserVoffset(device, f"{self._cmd_syntax}:VOFFSet")
        self._vpos = MaskUserVpos(device, f"{self._cmd_syntax}:VPOS")
        self._vscale = MaskUserVscale(device, f"{self._cmd_syntax}:VSCAle")
        self._width = MaskUserWidth(device, f"{self._cmd_syntax}:WIDth")

    @property
    def amplitude(self) -> MaskUserAmplitude:
        """Return the ``MASK:USER:AMPlitude`` command.

        Description:
            - This command sets or returns the current mask's nominal pulse amplitude in volts. The
              query form of this command returns the nominal pulse amplitude of the displayed mask.
              The set form of this command affects only the user mask, regardless of the current
              (displayed) mask.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:AMPlitude?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:AMPlitude?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:USER:AMPlitude value``
              command.

        SCPI Syntax:
            ```
            - MASK:USER:AMPlitude <NR3>
            - MASK:USER:AMPlitude?
            ```

        Info:
            - ``<NR3>`` is a floating number that sets the nominal pulse amplitude in volts.
        """
        return self._amplitude

    @property
    def bitrate(self) -> MaskUserBitrate:
        """Return the ``MASK:USER:BITRate`` command.

        Description:
            - This command sets or returns the bit rate for the user mask.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:BITRate?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:USER:BITRate value`` command.

        SCPI Syntax:
            ```
            - MASK:USER:BITRate <NR1>
            - MASK:USER:BITRate?
            ```

        Info:
            - ``<NR1>`` is a number that sets the bit rate of the user mask in bits per second.
        """
        return self._bitrate

    @property
    def hscale(self) -> MaskUserHscale:
        """Return the ``MASK:USER:HSCAle`` command.

        Description:
            - This command specifies the nominal timing resolution, in time/division, to be used to
              draw a user-defined custom mask pulse shape. A series of examples showing how to use
              mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:HSCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:HSCAle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:USER:HSCAle value`` command.

        SCPI Syntax:
            ```
            - MASK:USER:HSCAle <NR3>
            - MASK:USER:HSCAle?
            ```

        Info:
            - ``<NR3>`` is a floating point value that specifies the timing resolution used to a
              draw a user-defined custom mask pulse shape.
        """
        return self._hscale

    @property
    def htrigpos(self) -> MaskUserHtrigpos:
        """Return the ``MASK:USER:HTRIGPOS`` command.

        Description:
            - This command specifies the nominal trigger position (pulse leading edge), to be used
              to draw a user-defined custom mask, as a fraction of the display width. A series of
              examples showing how to use mask commands for typical tasks is included in an
              appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:HTRIGPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:HTRIGPOS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:USER:HTRIGPOS value`` command.

        SCPI Syntax:
            ```
            - MASK:USER:HTRIGPOS <NR3>
            - MASK:USER:HTRIGPOS?
            ```

        Info:
            - ``<NR3>`` is a floating point number in the range of 0.0 to 1.0 that sets the trigger
              points as a fraction of the display width, referenced from the left edge of the
              graticule.
        """
        return self._htrigpos

    @property
    def label(self) -> MaskUserLabel:
        """Return the ``MASK:USER:LABel`` command.

        Description:
            - This command specifies a user-defined label for a custom mask.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:LABel?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:USER:LABel value`` command.

        SCPI Syntax:
            ```
            - MASK:USER:LABel <QString>
            - MASK:USER:LABel?
            ```
        """
        return self._label

    @property
    def patternbits(self) -> MaskUserPatternbits:
        """Return the ``MASK:USER:PATTERNBITS`` command.

        Description:
            - This command sets or returns the number of bits used for serial trigger for the User
              mask standard. For example, DS1 requires six bits, four leading zeros, a one, and a
              trailing zero. The query form of this command returns the serial bit value of the
              displayed mask. The set form of this command affects only the User mask, regardless of
              the current (displayed) mask.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:PATTERNBITS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:PATTERNBITS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:USER:PATTERNBITS value``
              command.

        SCPI Syntax:
            ```
            - MASK:USER:PATTERNBITS <NR1>
            - MASK:USER:PATTERNBITS?
            ```

        Info:
            - ``<NR1>`` is an integer that sets the number of bits.
        """
        return self._patternbits

    @property
    def presampbits(self) -> MaskUserPresampbits:
        """Return the ``MASK:USER:PRESAMPBITS`` command.

        Description:
            - This command sets or returns the number of bits before the (isolated one) pulse
              leading edge in the serial trigger pass/fail testing. For example, DS1 has four
              leading zeros. The query form of this command returns the presample bit value of the
              displayed mask. The set form of this command only affects the user mask, regardless of
              the current (displayed) mask.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:PRESAMPBITS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:PRESAMPBITS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:USER:PRESAMPBITS value``
              command.

        SCPI Syntax:
            ```
            - MASK:USER:PRESAMPBITS <NR1>
            - MASK:USER:PRESAMPBITS?
            ```

        Info:
            - ``<NR1>`` is an integer that sets the number of bits before the trigger pulse.
        """
        return self._presampbits

    @property
    def recordlength(self) -> MaskUserRecordlength:
        """Return the ``MASK:USER:RECOrdlength`` command.

        Description:
            - This command specifies the nominal record length to be used for pulse mask testing
              with a user-defined custom mask. A series of examples showing how to use mask commands
              for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:RECOrdlength?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:RECOrdlength?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:USER:RECOrdlength value``
              command.

        SCPI Syntax:
            ```
            - MASK:USER:RECOrdlength <NR1>
            - MASK:USER:RECOrdlength?
            ```

        Info:
            - ``<NR1>`` is an integer that sets the record length value to be used for pulse mask
              testing of a user-defined custom mask.
        """
        return self._recordlength

    @property
    def seg(self) -> Dict[int, MaskUserSegItem]:
        """Return the ``MASK:USER:SEG<m>`` command.

        Description:
            - This command deletes the specified mask segment from the user mask, whether or not the
              user mask is the current mask. m is an integer that specifies the user mask segment
              number to delete from the user mask.

        Usage:
            - Using the ``.write(value)`` method will send the ``MASK:USER:SEG<m> value`` command.

        SCPI Syntax:
            ```
            - MASK:USER:SEG<m> DELEte
            ```

        Info:
            - ``DELEte`` removes the specified segment from the mask.

        Sub-properties:
            - ``.nr_pt``: The ``MASK:USER:SEG<m>:NR_Pt`` command.
            - ``.points``: The ``MASK:USER:SEG<m>:POINTS`` command.
        """
        return self._seg

    @property
    def trigtosamp(self) -> MaskUserTrigtosamp:
        """Return the ``MASK:USER:TRIGTOSAMP`` command.

        Description:
            - This command specifies the nominal time, in seconds, from the (leading edge) trigger
              position to the pulse bit sampling position, to be used for testing with a
              user-defined custom mask. A series of examples showing how to use mask commands for
              typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:TRIGTOSAMP?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:TRIGTOSAMP?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:USER:TRIGTOSAMP value``
              command.

        SCPI Syntax:
            ```
            - MASK:USER:TRIGTOSAMP <NR3>
            - MASK:USER:TRIGTOSAMP?
            ```

        Info:
            - ``<NR3>`` is a floating point number that sets the time to the pulse bit sampling
              position.
        """
        return self._trigtosamp

    @property
    def voffset(self) -> MaskUserVoffset:
        """Return the ``MASK:USER:VOFFSet`` command.

        Description:
            - This command specifies the nominal value, in volts, to be used to vertically offset
              the input channels for a user-defined custom mask. A series of examples showing how to
              use mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:VOFFSet?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:VOFFSet?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:USER:VOFFSet value`` command.

        SCPI Syntax:
            ```
            - MASK:USER:VOFFSet <NR3>
            - MASK:USER:VOFFSet?
            ```

        Info:
            - ``<NR3>`` is a floating point number that sets the nominal vertical offset value, in
              volts.
        """
        return self._voffset

    @property
    def vpos(self) -> MaskUserVpos:
        """Return the ``MASK:USER:VPOS`` command.

        Description:
            - This command specifies the nominal value, in divisions, to be used to vertically
              position the input channels for a user-defined custom mask. A series of examples
              showing how to use mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:VPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:VPOS?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:USER:VPOS value`` command.

        SCPI Syntax:
            ```
            - MASK:USER:VPOS <NR3>
            - MASK:USER:VPOS?
            ```

        Info:
            - ``<NR3>`` is a floating point number that sets the nominal vertical position value in
              divisions.
        """
        return self._vpos

    @property
    def vscale(self) -> MaskUserVscale:
        """Return the ``MASK:USER:VSCAle`` command.

        Description:
            - This command specifies the nominal value, in volts per division, to be used to
              vertically scale the input channels for a user-defined custom mask. A series of
              examples showing how to use mask commands for typical tasks is included in an
              appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:VSCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:VSCAle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:USER:VSCAle value`` command.

        SCPI Syntax:
            ```
            - MASK:USER:VSCAle <NR3>
            - MASK:USER:VSCAle?
            ```

        Info:
            - ``<NR3>`` is a floating point number that sets the nominal vertical scale value for
              the input channels for a user-defined custom mask.
        """
        return self._vscale

    @property
    def width(self) -> MaskUserWidth:
        """Return the ``MASK:USER:WIDth`` command.

        Description:
            - This command specifies the nominal bit width value, in seconds, to be used for a
              user-defined custom mask. This is the time of one bit of data where bit width = 1 /
              (data rate of the signal). A series of examples showing how to use mask commands for
              typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:WIDth?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:WIDth?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:USER:WIDth value`` command.

        SCPI Syntax:
            ```
            - MASK:USER:WIDth <NR3>
            - MASK:USER:WIDth?
            ```

        Info:
            - ``<NR3>`` is a floating point number that indicates the nominal bit width value in
              seconds.
        """
        return self._width


class MaskTestWaveform(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:WAVEform`` command.

    Description:
        - This command specifies the number of waveforms the instrument should test during a
          pass/fail mask test. A series of examples showing how to use mask commands for typical
          tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:WAVEform?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:WAVEform?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:WAVEform value`` command.

    SCPI Syntax:
        ```
        - MASK:TESt:WAVEform <NR1>
        - MASK:TESt:WAVEform?
        ```

    Info:
        - ``<NR1>`` is an integer that specifies the number of waveforms to test. The maximum
          waveform count that can be specified is 1E09.
    """


class MaskTestThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:THReshold`` command.

    Description:
        - This command specifies the number of failed tested waveforms needed in a pass/fail mask
          test to cause the test status to change to 'Failing'. A series of examples showing how to
          use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:THReshold?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:THReshold value`` command.

    SCPI Syntax:
        ```
        - MASK:TESt:THReshold <NR1>
        - MASK:TESt:THReshold?
        ```

    Info:
        - ``<NR1>`` is an integer that specifies the number of tested waveform violations occurring
          in each mask test that will change the test status to 'Failing'. The maximum number of
          failed tested waveforms that can be specified is 1E09. The default is 1.
    """


class MaskTestStopFailure(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:STOP:FAILure`` command.

    Description:
        - This command sets or returns the stop status on pass/fail test failure mode. When enabled,
          this command causes the instrument to stop acquiring data when the pass/fail status
          changes to 'Failing'. Repeat-on-completion mode has no effect.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:STOP:FAILure?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:STOP:FAILure?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:STOP:FAILure value`` command.

    SCPI Syntax:
        ```
        - MASK:TESt:STOP:FAILure {ON|OFF|<NR1>}
        - MASK:TESt:STOP:FAILure?
        ```

    Info:
        - ``<NR1>`` = 0 turns off the pass/fail stop on failure, and any other integer turns on the
          pass/fail SRQ on failure.
        - ``OFF`` turns off the pass/fail stop on failure. This is the default.
        - ``ON`` turns on the pass/fail stop on failure.
    """


class MaskTestStop(SCPICmdRead):
    """The ``MASK:TESt:STOP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:STOP?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:STOP?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.failure``: The ``MASK:TESt:STOP:FAILure`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._failure = MaskTestStopFailure(device, f"{self._cmd_syntax}:FAILure")

    @property
    def failure(self) -> MaskTestStopFailure:
        """Return the ``MASK:TESt:STOP:FAILure`` command.

        Description:
            - This command sets or returns the stop status on pass/fail test failure mode. When
              enabled, this command causes the instrument to stop acquiring data when the pass/fail
              status changes to 'Failing'. Repeat-on-completion mode has no effect.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:STOP:FAILure?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:STOP:FAILure?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:STOP:FAILure value``
              command.

        SCPI Syntax:
            ```
            - MASK:TESt:STOP:FAILure {ON|OFF|<NR1>}
            - MASK:TESt:STOP:FAILure?
            ```

        Info:
            - ``<NR1>`` = 0 turns off the pass/fail stop on failure, and any other integer turns on
              the pass/fail SRQ on failure.
            - ``OFF`` turns off the pass/fail stop on failure. This is the default.
            - ``ON`` turns on the pass/fail stop on failure.
        """
        return self._failure


class MaskTestStatus(SCPICmdRead):
    """The ``MASK:TESt:STATUS`` command.

    Description:
        - This query-only command returns the pass/fail test status. This command returns one of:
          OFF, DELAY, PASSING, FAILING, PASSED, FAILED, and VIOLATION. In other words, it indicates
          the result of the pass/fail test. When the violation count exceeds the violation
          threshold, the status changes from Passing to Failed.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:STATUS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:STATUS?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MASK:TESt:STATUS?
        ```
    """


class MaskTestState(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:STATE`` command.

    Description:
        - This command turns the pass/fail mask test on or off. Most of the other ``MASK:TEST``
          commands need to be executed before this command. A series of examples showing how to use
          mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:STATE value`` command.

    SCPI Syntax:
        ```
        - MASK:TESt:STATE {ON|OFF|<NR1>}
        - MASK:TESt:STATE?
        ```

    Info:
        - ``ON`` turns the mask test on.
        - ``OFF`` turns the mask test off.
        - ``<NR1>`` is an integer. 0 turns the mask test off; any other integer turns it on.
    """


class MaskTestSrqFailure(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:SRQ:FAILure`` command.

    Description:
        - This command causes the instrument to send an SRQ command when a pass/fail mask test
          fails. A series of examples showing how to use mask commands for typical tasks is included
          in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:SRQ:FAILure?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:SRQ:FAILure?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:SRQ:FAILure value`` command.

    SCPI Syntax:
        ```
        - MASK:TESt:SRQ:FAILure {ON|OFF|<NR1>}
        - MASK:TESt:SRQ:FAILure?
        ```

    Info:
        - ``ON`` turns on this feature, so that when a mask test fails, the instrument will send an
          SRQ command (if registers are set to send SRQ when OPC is asserted.
        - ``OFF`` turns off this feature.
        - ``<NR1>`` is an integer. 0 turns off this feature; any other integer turns it on.
    """


class MaskTestSrqCompletion(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:SRQ:COMPLetion`` command.

    Description:
        - This command causes the instrument to send an SRQ command when a pass/fail mask test
          completes. Use the command ``MASK:TEST:COMPLETION:CRITERION`` to specify criterion. The
          ``MASK:ACTONEVENT:ENABLE`` command should be set to ON for this event to happen. After the
          event occurs ``MASK:ACTONEVENT:ENABLE`` command will be set to OFF automatically. A series
          of examples showing how to use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:SRQ:COMPLetion?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:SRQ:COMPLetion?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:SRQ:COMPLetion value``
          command.

    SCPI Syntax:
        ```
        - MASK:TESt:SRQ:COMPLetion {ON|OFF|<NR1>}
        - MASK:TESt:SRQ:COMPLetion?
        ```

    Info:
        - ``ON`` turns on this feature, so that upon the completion of a mask test, the instrument
          will send an SRQ command (if registers are set to send SRQ when OPC is asserted).
        - ``OFF`` turns off this feature.
        - ``<NR1>`` is an integer. 0 turns off this feature; any other integer turns it on.
    """


class MaskTestSrq(SCPICmdRead):
    """The ``MASK:TESt:SRQ`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:SRQ?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:SRQ?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.completion``: The ``MASK:TESt:SRQ:COMPLetion`` command.
        - ``.failure``: The ``MASK:TESt:SRQ:FAILure`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._completion = MaskTestSrqCompletion(device, f"{self._cmd_syntax}:COMPLetion")
        self._failure = MaskTestSrqFailure(device, f"{self._cmd_syntax}:FAILure")

    @property
    def completion(self) -> MaskTestSrqCompletion:
        """Return the ``MASK:TESt:SRQ:COMPLetion`` command.

        Description:
            - This command causes the instrument to send an SRQ command when a pass/fail mask test
              completes. Use the command ``MASK:TEST:COMPLETION:CRITERION`` to specify criterion.
              The ``MASK:ACTONEVENT:ENABLE`` command should be set to ON for this event to happen.
              After the event occurs ``MASK:ACTONEVENT:ENABLE`` command will be set to OFF
              automatically. A series of examples showing how to use mask commands for typical tasks
              is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:SRQ:COMPLetion?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:SRQ:COMPLetion?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:SRQ:COMPLetion value``
              command.

        SCPI Syntax:
            ```
            - MASK:TESt:SRQ:COMPLetion {ON|OFF|<NR1>}
            - MASK:TESt:SRQ:COMPLetion?
            ```

        Info:
            - ``ON`` turns on this feature, so that upon the completion of a mask test, the
              instrument will send an SRQ command (if registers are set to send SRQ when OPC is
              asserted).
            - ``OFF`` turns off this feature.
            - ``<NR1>`` is an integer. 0 turns off this feature; any other integer turns it on.
        """
        return self._completion

    @property
    def failure(self) -> MaskTestSrqFailure:
        """Return the ``MASK:TESt:SRQ:FAILure`` command.

        Description:
            - This command causes the instrument to send an SRQ command when a pass/fail mask test
              fails. A series of examples showing how to use mask commands for typical tasks is
              included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:SRQ:FAILure?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:SRQ:FAILure?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:SRQ:FAILure value``
              command.

        SCPI Syntax:
            ```
            - MASK:TESt:SRQ:FAILure {ON|OFF|<NR1>}
            - MASK:TESt:SRQ:FAILure?
            ```

        Info:
            - ``ON`` turns on this feature, so that when a mask test fails, the instrument will send
              an SRQ command (if registers are set to send SRQ when OPC is asserted.
            - ``OFF`` turns off this feature.
            - ``<NR1>`` is an integer. 0 turns off this feature; any other integer turns it on.
        """
        return self._failure


class MaskTestSavewfmFilename(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:SAVEWFM:FILEName`` command.

    Description:
        - This command sets or returns the name of the directory and file to use with the
          ``MASK:TEST:SAVEWFM`` command. It defines the directory the files will be put in (name
          comes from date and time).

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:SAVEWFM:FILEName?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:SAVEWFM:FILEName?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:SAVEWFM:FILEName value``
          command.

    SCPI Syntax:
        ```
        - MASK:TESt:SAVEWFM:FILEName <QString>
        - MASK:TESt:SAVEWFM:FILEName?
        ```

    Info:
        - ``<QString>`` is a string representing the name of the file to save waveform data to.
    """

    _WRAP_ARG_WITH_QUOTES = True


class MaskTestSavewfm(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:SAVEWFM`` command.

    Description:
        - This command copies the waveform data from all active channels to a file on a flash memory
          device such as a USB stick or a network drive. See the command ``FILESYSTEM:MKDIR`` and
          other File System commands for more information on saving to a file. The
          ``MASK:ACTONEVENT:ENABLE`` command should be set to ON for this event to happen. After the
          event occurs ``MASK:ACTONEVENT:ENABLE`` command will be set to OFF automatically. A series
          of examples showing how to use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:SAVEWFM?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:SAVEWFM?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:SAVEWFM value`` command.

    SCPI Syntax:
        ```
        - MASK:TESt:SAVEWFM {ON|OFF|<NR1>}
        - MASK:TESt:SAVEWFM?
        ```

    Info:
        - ``ON`` turns on this feature, so that waveform data from all active channels is copied to
          files upon test failure.
        - ``OFF`` turns off this feature.
        - ``<NR1>`` is an integer. 0 turns off this feature; any other value turns it on.

    Properties:
        - ``.filename``: The ``MASK:TESt:SAVEWFM:FILEName`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._filename = MaskTestSavewfmFilename(device, f"{self._cmd_syntax}:FILEName")

    @property
    def filename(self) -> MaskTestSavewfmFilename:
        """Return the ``MASK:TESt:SAVEWFM:FILEName`` command.

        Description:
            - This command sets or returns the name of the directory and file to use with the
              ``MASK:TEST:SAVEWFM`` command. It defines the directory the files will be put in (name
              comes from date and time).

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:SAVEWFM:FILEName?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:SAVEWFM:FILEName?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:SAVEWFM:FILEName value``
              command.

        SCPI Syntax:
            ```
            - MASK:TESt:SAVEWFM:FILEName <QString>
            - MASK:TESt:SAVEWFM:FILEName?
            ```

        Info:
            - ``<QString>`` is a string representing the name of the file to save waveform data to.
        """
        return self._filename


class MaskTestSampleThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:SAMple:THReshold`` command.

    Description:
        - This command sets or returns the minimum number of hits in mask regions needed to cause
          the pass/fail status to change from PASSING to FAILING. This affects the mask test when
          the instrument is acquiring in waveform database (WfmDB) mode.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:SAMple:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:SAMple:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:SAMple:THReshold value``
          command.

    SCPI Syntax:
        ```
        - MASK:TESt:SAMple:THReshold {<NR1>}
        - MASK:TESt:SAMple:THReshold?
        ```

    Info:
        - ``<NR1>`` is the number of hits that can happen when the test fails.
    """


class MaskTestSample(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:SAMple`` command.

    Description:
        - This command sets or returns the minimum number of waveform database (WfmDB) points the
          instrument can acquire before it stops a single sequence acquisition or stops running a
          mask test. Hint: a bigger sample size can allow a greater throughput (more waveforms to
          get acquired at a time). However, a very large sample size can slow down the display
          update. So to speed up the display rate, consider reducing the sample size. This command
          works the same as the ``ACQUIRE:NUMSAMPLES`` command.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:SAMple?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:SAMple?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:SAMple value`` command.

    SCPI Syntax:
        ```
        - MASK:TESt:SAMple {<NR1>}
        - MASK:TESt:SAMple?
        ```

    Info:
        - ``<NR1>`` the number of points to sample.

    Properties:
        - ``.threshold``: The ``MASK:TESt:SAMple:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._threshold = MaskTestSampleThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def threshold(self) -> MaskTestSampleThreshold:
        """Return the ``MASK:TESt:SAMple:THReshold`` command.

        Description:
            - This command sets or returns the minimum number of hits in mask regions needed to
              cause the pass/fail status to change from PASSING to FAILING. This affects the mask
              test when the instrument is acquiring in waveform database (WfmDB) mode.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:SAMple:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:SAMple:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:SAMple:THReshold value``
              command.

        SCPI Syntax:
            ```
            - MASK:TESt:SAMple:THReshold {<NR1>}
            - MASK:TESt:SAMple:THReshold?
            ```

        Info:
            - ``<NR1>`` is the number of hits that can happen when the test fails.
        """
        return self._threshold


class MaskTestRepeat(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:REPeat`` command.

    Description:
        - This command causes the mask test cycle to continuously repeat upon the completion of the
          previous test cycle. A series of examples showing how to use mask commands for typical
          tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:REPeat?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:REPeat?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:REPeat value`` command.

    SCPI Syntax:
        ```
        - MASK:TESt:REPeat {ON|OFF|<NR1>}
        - MASK:TESt:REPeat?
        ```

    Info:
        - ``ON`` turns on this feature, so that the mask test cycle repeats continuously upon the
          completion of the previous test cycle.
        - ``OFF`` turns off this feature.
        - ``<NR1>`` is an integer. 0 turns off this feature; any other integer turns it on.
    """


class MaskTestLogFailure(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:LOG:FAILure`` command.

    Description:
        - This command sets or returns the log status on pass/fail test failure mode. When enabled,
          this command causes the instrument to log the current date and time to a file when the
          pass/fail status changes to 'Failing'. The file name is determined from the current date
          and time. The user cannot change this name.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:LOG:FAILure?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:LOG:FAILure?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:LOG:FAILure value`` command.

    SCPI Syntax:
        ```
        - MASK:TESt:LOG:FAILure {ON|OFF|<NR1>}
        - MASK:TESt:LOG:FAILure?
        ```

    Info:
        - ``<NR1>`` = 0 turns off the pass/fail log on failure, and any other integer turns on the
          pass/fail log on failure.
        - ``OFF`` turns off the pass/fail log on failure. This is the default.
        - ``ON`` turns on the pass/fail log on failure.
    """


class MaskTestLog(SCPICmdRead):
    """The ``MASK:TESt:LOG`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:LOG?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:LOG?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.failure``: The ``MASK:TESt:LOG:FAILure`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._failure = MaskTestLogFailure(device, f"{self._cmd_syntax}:FAILure")

    @property
    def failure(self) -> MaskTestLogFailure:
        """Return the ``MASK:TESt:LOG:FAILure`` command.

        Description:
            - This command sets or returns the log status on pass/fail test failure mode. When
              enabled, this command causes the instrument to log the current date and time to a file
              when the pass/fail status changes to 'Failing'. The file name is determined from the
              current date and time. The user cannot change this name.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:LOG:FAILure?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:LOG:FAILure?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:LOG:FAILure value``
              command.

        SCPI Syntax:
            ```
            - MASK:TESt:LOG:FAILure {ON|OFF|<NR1>}
            - MASK:TESt:LOG:FAILure?
            ```

        Info:
            - ``<NR1>`` = 0 turns off the pass/fail log on failure, and any other integer turns on
              the pass/fail log on failure.
            - ``OFF`` turns off the pass/fail log on failure. This is the default.
            - ``ON`` turns on the pass/fail log on failure.
        """
        return self._failure


class MaskTestHardcopy(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:HARDCopy`` command.

    Description:
        - This command will cause the instrument to generate a screen shot to the default printer as
          soon as a pass/fail mask test fails, using the current instrument hard copy settings. See
          ``HARDCOPY:ACTIVEPRINTER`` and other Hardcopy commands for more information on accessing
          printer settings. A series of examples showing how to use mask commands for typical tasks
          is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:HARDCopy?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:HARDCopy?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:HARDCopy value`` command.

    SCPI Syntax:
        ```
        - MASK:TESt:HARDCopy {ON|OFF|<NR1>}
        - MASK:TESt:HARDCopy?
        ```

    Info:
        - ``ON`` turns on this feature, so that the instrument will generate a screen hard copy to
          the default printer upon failure.
        - ``OFF`` turns off this feature.
        - ``<NR1>`` = 0 turns off this feature; any other value turns it on.
    """


class MaskTestDelay(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:DELay`` command.

    Description:
        - This command specifies the amount of time, in seconds, the instrument should wait after
          the start of pass/fail mask testing before it evaluates the waveforms. This command is
          useful if the test system requires some 'settling' time. A series of examples showing how
          to use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:DELay?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:DELay?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:DELay value`` command.

    SCPI Syntax:
        ```
        - MASK:TESt:DELay <NR3>
        - MASK:TESt:DELay?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the amount of time in seconds, to
          delay the start of the mask pass/fail test.
    """


class MaskTestBeepFailure(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:BEEP:FAILure`` command.

    Description:
        - This command sets or returns the beep status on pass/fail test failure mode. When enabled,
          this command causes the instrument to emit a tone when the pass/fail status changes to
          'Failing'.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:BEEP:FAILure?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:BEEP:FAILure?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:BEEP:FAILure value`` command.

    SCPI Syntax:
        ```
        - MASK:TESt:BEEP:FAILure {ON|OFF|<NR1>}
        - MASK:TESt:BEEP:FAILure?
        ```

    Info:
        - ``<NR1>`` = 0 turns off the pass/fail beep on failure, and any other integer turns on the
          pass/fail beep on failure.
        - ``OFF`` turns off the pass/fail beep on failure. This is the default.
        - ``ON`` turns on the pass/fail beep on failure.
    """


class MaskTestBeepCompletion(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:BEEP:COMPLetion`` command.

    Description:
        - This command sets or returns the beep on pass/fail test completion mode. When enabled,
          this command causes the instrument to emit a tone when the mask pass/fail test completes.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:BEEP:COMPLetion?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:BEEP:COMPLetion?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:BEEP:COMPLetion value``
          command.

    SCPI Syntax:
        ```
        - MASK:TESt:BEEP:COMPLetion {ON|OFF|<NR1>}
        - MASK:TESt:BEEP:COMPLetion?
        ```

    Info:
        - ``<NR1>`` = 0 turns off the pass/fail beep on completion, any other integer turns on the
          pass/fail beep on completion.
        - ``OFF`` turns off the pass/fail beep on completion.
        - ``ON`` turns on the pass/fail beep on completion.
    """


class MaskTestBeep(SCPICmdRead):
    """The ``MASK:TESt:BEEP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:BEEP?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:BEEP?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.completion``: The ``MASK:TESt:BEEP:COMPLetion`` command.
        - ``.failure``: The ``MASK:TESt:BEEP:FAILure`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._completion = MaskTestBeepCompletion(device, f"{self._cmd_syntax}:COMPLetion")
        self._failure = MaskTestBeepFailure(device, f"{self._cmd_syntax}:FAILure")

    @property
    def completion(self) -> MaskTestBeepCompletion:
        """Return the ``MASK:TESt:BEEP:COMPLetion`` command.

        Description:
            - This command sets or returns the beep on pass/fail test completion mode. When enabled,
              this command causes the instrument to emit a tone when the mask pass/fail test
              completes.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:BEEP:COMPLetion?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:BEEP:COMPLetion?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:BEEP:COMPLetion value``
              command.

        SCPI Syntax:
            ```
            - MASK:TESt:BEEP:COMPLetion {ON|OFF|<NR1>}
            - MASK:TESt:BEEP:COMPLetion?
            ```

        Info:
            - ``<NR1>`` = 0 turns off the pass/fail beep on completion, any other integer turns on
              the pass/fail beep on completion.
            - ``OFF`` turns off the pass/fail beep on completion.
            - ``ON`` turns on the pass/fail beep on completion.
        """
        return self._completion

    @property
    def failure(self) -> MaskTestBeepFailure:
        """Return the ``MASK:TESt:BEEP:FAILure`` command.

        Description:
            - This command sets or returns the beep status on pass/fail test failure mode. When
              enabled, this command causes the instrument to emit a tone when the pass/fail status
              changes to 'Failing'.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:BEEP:FAILure?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:BEEP:FAILure?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:BEEP:FAILure value``
              command.

        SCPI Syntax:
            ```
            - MASK:TESt:BEEP:FAILure {ON|OFF|<NR1>}
            - MASK:TESt:BEEP:FAILure?
            ```

        Info:
            - ``<NR1>`` = 0 turns off the pass/fail beep on failure, and any other integer turns on
              the pass/fail beep on failure.
            - ``OFF`` turns off the pass/fail beep on failure. This is the default.
            - ``ON`` turns on the pass/fail beep on failure.
        """
        return self._failure


class MaskTestAuxFailure(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:AUX:FAILure`` command.

    Description:
        - This command sets or returns the ``test:aux`` status on pass/fail test failure mode. When
          enabled, this command causes the instrument to provide a TTL signal at the AuxOut port
          when the pass/fail status changes to 'Failing'.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:AUX:FAILure?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:AUX:FAILure?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:AUX:FAILure value`` command.

    SCPI Syntax:
        ```
        - MASK:TESt:AUX:FAILure {ON|OFF|<NR1>}
        - MASK:TESt:AUX:FAILure?
        ```

    Info:
        - ``<NR1>`` = 0 disables the ``mask:test:aux:failure`` function; any other value enables it.
        - ``OFF`` turns off the pass/fail ``mask:test:aux`` on failure. This is the default.
        - ``ON`` turns on the pass/fail ``mask:test:aux`` on failure.
    """


class MaskTestAuxCompletion(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:AUX:COMPLetion`` command.

    Description:
        - This command sets or returns the ``test:aux`` on pass/fail test completion mode. When
          enabled, this command causes the instrument to provide a TTL signal at the ``Aux:Out``
          port when the mask pass/fail status changes to 'Failing'.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:AUX:COMPLetion?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:AUX:COMPLetion?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:AUX:COMPLetion value``
          command.

    SCPI Syntax:
        ```
        - MASK:TESt:AUX:COMPLetion {ON|OFF|<NR1>}
        - MASK:TESt:AUX:COMPLetion?
        ```

    Info:
        - ``<NR1>`` = 0 disables the ``mask:test:aux:completion`` function; any other value enables
          it.
        - ``OFF`` turns off the pass/fail ``mask:test:aux`` on completion.
        - ``ON`` turns on the pass/fail ``mask:test:aux`` on completion.
    """


class MaskTestAux(SCPICmdRead):
    """The ``MASK:TESt:AUX`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:AUX?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:AUX?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.completion``: The ``MASK:TESt:AUX:COMPLetion`` command.
        - ``.failure``: The ``MASK:TESt:AUX:FAILure`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._completion = MaskTestAuxCompletion(device, f"{self._cmd_syntax}:COMPLetion")
        self._failure = MaskTestAuxFailure(device, f"{self._cmd_syntax}:FAILure")

    @property
    def completion(self) -> MaskTestAuxCompletion:
        """Return the ``MASK:TESt:AUX:COMPLetion`` command.

        Description:
            - This command sets or returns the ``test:aux`` on pass/fail test completion mode. When
              enabled, this command causes the instrument to provide a TTL signal at the ``Aux:Out``
              port when the mask pass/fail status changes to 'Failing'.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:AUX:COMPLetion?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:AUX:COMPLetion?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:AUX:COMPLetion value``
              command.

        SCPI Syntax:
            ```
            - MASK:TESt:AUX:COMPLetion {ON|OFF|<NR1>}
            - MASK:TESt:AUX:COMPLetion?
            ```

        Info:
            - ``<NR1>`` = 0 disables the ``mask:test:aux:completion`` function; any other value
              enables it.
            - ``OFF`` turns off the pass/fail ``mask:test:aux`` on completion.
            - ``ON`` turns on the pass/fail ``mask:test:aux`` on completion.
        """
        return self._completion

    @property
    def failure(self) -> MaskTestAuxFailure:
        """Return the ``MASK:TESt:AUX:FAILure`` command.

        Description:
            - This command sets or returns the ``test:aux`` status on pass/fail test failure mode.
              When enabled, this command causes the instrument to provide a TTL signal at the AuxOut
              port when the pass/fail status changes to 'Failing'.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:AUX:FAILure?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:AUX:FAILure?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:AUX:FAILure value``
              command.

        SCPI Syntax:
            ```
            - MASK:TESt:AUX:FAILure {ON|OFF|<NR1>}
            - MASK:TESt:AUX:FAILure?
            ```

        Info:
            - ``<NR1>`` = 0 disables the ``mask:test:aux:failure`` function; any other value enables
              it.
            - ``OFF`` turns off the pass/fail ``mask:test:aux`` on failure. This is the default.
            - ``ON`` turns on the pass/fail ``mask:test:aux`` on failure.
        """
        return self._failure


#  pylint: disable=too-many-instance-attributes
class MaskTest(SCPICmdRead):
    """The ``MASK:TESt`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.aux``: The ``MASK:TESt:AUX`` command tree.
        - ``.beep``: The ``MASK:TESt:BEEP`` command tree.
        - ``.delay``: The ``MASK:TESt:DELay`` command.
        - ``.hardcopy``: The ``MASK:TESt:HARDCopy`` command.
        - ``.log``: The ``MASK:TESt:LOG`` command tree.
        - ``.repeat``: The ``MASK:TESt:REPeat`` command.
        - ``.sample``: The ``MASK:TESt:SAMple`` command.
        - ``.savewfm``: The ``MASK:TESt:SAVEWFM`` command.
        - ``.srq``: The ``MASK:TESt:SRQ`` command tree.
        - ``.state``: The ``MASK:TESt:STATE`` command.
        - ``.status``: The ``MASK:TESt:STATUS`` command.
        - ``.stop``: The ``MASK:TESt:STOP`` command tree.
        - ``.threshold``: The ``MASK:TESt:THReshold`` command.
        - ``.waveform``: The ``MASK:TESt:WAVEform`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._aux = MaskTestAux(device, f"{self._cmd_syntax}:AUX")
        self._beep = MaskTestBeep(device, f"{self._cmd_syntax}:BEEP")
        self._delay = MaskTestDelay(device, f"{self._cmd_syntax}:DELay")
        self._hardcopy = MaskTestHardcopy(device, f"{self._cmd_syntax}:HARDCopy")
        self._log = MaskTestLog(device, f"{self._cmd_syntax}:LOG")
        self._repeat = MaskTestRepeat(device, f"{self._cmd_syntax}:REPeat")
        self._sample = MaskTestSample(device, f"{self._cmd_syntax}:SAMple")
        self._savewfm = MaskTestSavewfm(device, f"{self._cmd_syntax}:SAVEWFM")
        self._srq = MaskTestSrq(device, f"{self._cmd_syntax}:SRQ")
        self._state = MaskTestState(device, f"{self._cmd_syntax}:STATE")
        self._status = MaskTestStatus(device, f"{self._cmd_syntax}:STATUS")
        self._stop = MaskTestStop(device, f"{self._cmd_syntax}:STOP")
        self._threshold = MaskTestThreshold(device, f"{self._cmd_syntax}:THReshold")
        self._waveform = MaskTestWaveform(device, f"{self._cmd_syntax}:WAVEform")

    @property
    def aux(self) -> MaskTestAux:
        """Return the ``MASK:TESt:AUX`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:AUX?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:AUX?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.completion``: The ``MASK:TESt:AUX:COMPLetion`` command.
            - ``.failure``: The ``MASK:TESt:AUX:FAILure`` command.
        """
        return self._aux

    @property
    def beep(self) -> MaskTestBeep:
        """Return the ``MASK:TESt:BEEP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:BEEP?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:BEEP?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.completion``: The ``MASK:TESt:BEEP:COMPLetion`` command.
            - ``.failure``: The ``MASK:TESt:BEEP:FAILure`` command.
        """
        return self._beep

    @property
    def delay(self) -> MaskTestDelay:
        """Return the ``MASK:TESt:DELay`` command.

        Description:
            - This command specifies the amount of time, in seconds, the instrument should wait
              after the start of pass/fail mask testing before it evaluates the waveforms. This
              command is useful if the test system requires some 'settling' time. A series of
              examples showing how to use mask commands for typical tasks is included in an
              appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:DELay?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:DELay?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:DELay value`` command.

        SCPI Syntax:
            ```
            - MASK:TESt:DELay <NR3>
            - MASK:TESt:DELay?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the amount of time in seconds, to
              delay the start of the mask pass/fail test.
        """
        return self._delay

    @property
    def hardcopy(self) -> MaskTestHardcopy:
        """Return the ``MASK:TESt:HARDCopy`` command.

        Description:
            - This command will cause the instrument to generate a screen shot to the default
              printer as soon as a pass/fail mask test fails, using the current instrument hard copy
              settings. See ``HARDCOPY:ACTIVEPRINTER`` and other Hardcopy commands for more
              information on accessing printer settings. A series of examples showing how to use
              mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:HARDCopy?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:HARDCopy?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:HARDCopy value`` command.

        SCPI Syntax:
            ```
            - MASK:TESt:HARDCopy {ON|OFF|<NR1>}
            - MASK:TESt:HARDCopy?
            ```

        Info:
            - ``ON`` turns on this feature, so that the instrument will generate a screen hard copy
              to the default printer upon failure.
            - ``OFF`` turns off this feature.
            - ``<NR1>`` = 0 turns off this feature; any other value turns it on.
        """
        return self._hardcopy

    @property
    def log(self) -> MaskTestLog:
        """Return the ``MASK:TESt:LOG`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:LOG?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:LOG?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.failure``: The ``MASK:TESt:LOG:FAILure`` command.
        """
        return self._log

    @property
    def repeat(self) -> MaskTestRepeat:
        """Return the ``MASK:TESt:REPeat`` command.

        Description:
            - This command causes the mask test cycle to continuously repeat upon the completion of
              the previous test cycle. A series of examples showing how to use mask commands for
              typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:REPeat?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:REPeat?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:REPeat value`` command.

        SCPI Syntax:
            ```
            - MASK:TESt:REPeat {ON|OFF|<NR1>}
            - MASK:TESt:REPeat?
            ```

        Info:
            - ``ON`` turns on this feature, so that the mask test cycle repeats continuously upon
              the completion of the previous test cycle.
            - ``OFF`` turns off this feature.
            - ``<NR1>`` is an integer. 0 turns off this feature; any other integer turns it on.
        """
        return self._repeat

    @property
    def sample(self) -> MaskTestSample:
        """Return the ``MASK:TESt:SAMple`` command.

        Description:
            - This command sets or returns the minimum number of waveform database (WfmDB) points
              the instrument can acquire before it stops a single sequence acquisition or stops
              running a mask test. Hint: a bigger sample size can allow a greater throughput (more
              waveforms to get acquired at a time). However, a very large sample size can slow down
              the display update. So to speed up the display rate, consider reducing the sample
              size. This command works the same as the ``ACQUIRE:NUMSAMPLES`` command.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:SAMple?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:SAMple?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:SAMple value`` command.

        SCPI Syntax:
            ```
            - MASK:TESt:SAMple {<NR1>}
            - MASK:TESt:SAMple?
            ```

        Info:
            - ``<NR1>`` the number of points to sample.

        Sub-properties:
            - ``.threshold``: The ``MASK:TESt:SAMple:THReshold`` command.
        """
        return self._sample

    @property
    def savewfm(self) -> MaskTestSavewfm:
        """Return the ``MASK:TESt:SAVEWFM`` command.

        Description:
            - This command copies the waveform data from all active channels to a file on a flash
              memory device such as a USB stick or a network drive. See the command
              ``FILESYSTEM:MKDIR`` and other File System commands for more information on saving to
              a file. The ``MASK:ACTONEVENT:ENABLE`` command should be set to ON for this event to
              happen. After the event occurs ``MASK:ACTONEVENT:ENABLE`` command will be set to OFF
              automatically. A series of examples showing how to use mask commands for typical tasks
              is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:SAVEWFM?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:SAVEWFM?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:SAVEWFM value`` command.

        SCPI Syntax:
            ```
            - MASK:TESt:SAVEWFM {ON|OFF|<NR1>}
            - MASK:TESt:SAVEWFM?
            ```

        Info:
            - ``ON`` turns on this feature, so that waveform data from all active channels is copied
              to files upon test failure.
            - ``OFF`` turns off this feature.
            - ``<NR1>`` is an integer. 0 turns off this feature; any other value turns it on.

        Sub-properties:
            - ``.filename``: The ``MASK:TESt:SAVEWFM:FILEName`` command.
        """
        return self._savewfm

    @property
    def srq(self) -> MaskTestSrq:
        """Return the ``MASK:TESt:SRQ`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:SRQ?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:SRQ?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.completion``: The ``MASK:TESt:SRQ:COMPLetion`` command.
            - ``.failure``: The ``MASK:TESt:SRQ:FAILure`` command.
        """
        return self._srq

    @property
    def state(self) -> MaskTestState:
        """Return the ``MASK:TESt:STATE`` command.

        Description:
            - This command turns the pass/fail mask test on or off. Most of the other ``MASK:TEST``
              commands need to be executed before this command. A series of examples showing how to
              use mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:STATE?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:STATE value`` command.

        SCPI Syntax:
            ```
            - MASK:TESt:STATE {ON|OFF|<NR1>}
            - MASK:TESt:STATE?
            ```

        Info:
            - ``ON`` turns the mask test on.
            - ``OFF`` turns the mask test off.
            - ``<NR1>`` is an integer. 0 turns the mask test off; any other integer turns it on.
        """
        return self._state

    @property
    def status(self) -> MaskTestStatus:
        """Return the ``MASK:TESt:STATUS`` command.

        Description:
            - This query-only command returns the pass/fail test status. This command returns one
              of: OFF, DELAY, PASSING, FAILING, PASSED, FAILED, and VIOLATION. In other words, it
              indicates the result of the pass/fail test. When the violation count exceeds the
              violation threshold, the status changes from Passing to Failed.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:STATUS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:STATUS?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MASK:TESt:STATUS?
            ```
        """
        return self._status

    @property
    def stop(self) -> MaskTestStop:
        """Return the ``MASK:TESt:STOP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:STOP?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:STOP?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.failure``: The ``MASK:TESt:STOP:FAILure`` command.
        """
        return self._stop

    @property
    def threshold(self) -> MaskTestThreshold:
        """Return the ``MASK:TESt:THReshold`` command.

        Description:
            - This command specifies the number of failed tested waveforms needed in a pass/fail
              mask test to cause the test status to change to 'Failing'. A series of examples
              showing how to use mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:THReshold?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:THReshold value``
              command.

        SCPI Syntax:
            ```
            - MASK:TESt:THReshold <NR1>
            - MASK:TESt:THReshold?
            ```

        Info:
            - ``<NR1>`` is an integer that specifies the number of tested waveform violations
              occurring in each mask test that will change the test status to 'Failing'. The maximum
              number of failed tested waveforms that can be specified is 1E09. The default is 1.
        """
        return self._threshold

    @property
    def waveform(self) -> MaskTestWaveform:
        """Return the ``MASK:TESt:WAVEform`` command.

        Description:
            - This command specifies the number of waveforms the instrument should test during a
              pass/fail mask test. A series of examples showing how to use mask commands for typical
              tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:WAVEform?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:WAVEform?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:WAVEform value`` command.

        SCPI Syntax:
            ```
            - MASK:TESt:WAVEform <NR1>
            - MASK:TESt:WAVEform?
            ```

        Info:
            - ``<NR1>`` is an integer that specifies the number of waveforms to test. The maximum
              waveform count that can be specified is 1E09.
        """
        return self._waveform


class MaskStoponviolation(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:STOPOnviolation`` command.

    Description:
        - This command stops the waveform acquisitions upon the first occurrence of a waveform
          violation. The ``MASK:ACTONEVENT:ENABLE`` command should be set to ON for this event to
          happen. After the event occurs ``MASK:ACTONEVENT:ENABLE`` command will be set to OFF
          automatically. You can also specify an action to be performed when acquisitions are
          stopped by using the commands such as ``MASK:TEST:SAVEWFM``, ``MASK:TEST:SAVEIMAGE``,
          ``MASK:TEST:AUXOUT:FAILURE``, ``MASK:TEST:HARDCOPY``, or ``MASK:TEST:SRQ:FAILURE``. A
          series of examples showing how to use mask commands for typical tasks is included in an
          appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:STOPOnviolation?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:STOPOnviolation?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:STOPOnviolation value`` command.

    SCPI Syntax:
        ```
        - MASK:STOPOnviolation {ON|OFF|<NR1>}
        - MASK:STOPOnviolation?
        ```

    Info:
        - ``ON`` stops waveform acquisition on the first occurrence of a mask violation.
        - ``OFF`` turns this feature off.
        - ``<NR1>=0`` turns this feature off ; any other value turns it on.
    """


class MaskStandard(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:STANdard`` command.

    Description:
        - This command deletes the existing mask (if any) and sets the selected standard mask. If
          ``MASK:COUNT:STATE`` is ON, mask counting starts immediately. The query form of this
          command returns the current mask standard. The following warning event is posted if the
          mask exceeds the instrument bandwidth: 2318,'Consider system bandwidth when testing at
          this bit rate.'

    Usage:
        - Using the ``.query()`` method will send the ``MASK:STANdard?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:STANdard?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:STANdard value`` command.

    SCPI Syntax:
        ```
        - MASK:STANdard {ATARXG<x>|ATATXG1|ATATXG2|ATATXG3|CLOCKCoax|CLOCKSymmetrical|D<x>|DS0Contra|DS0Double|DS0Single|DS0Timing|DS1|DS1A|DS1C|DS2|DS2RATECoax|DS2RATESymmetrical|DS3|DS4NA|DS4NA_Max|E1Coax|E1Symmetrical|E2|E3|E4_1|E4_0|ENET1000BCX_ATP2|ENET1000BCX_ATP3|ENET1000BCX_NTP2|ENET100FX|ENET100STP|ENET100UTP|ENET1250|ENETXAUI_Far|ENETXAUI_Near|FC1063|FC1063Draft|FC1063E|FC1063E_ABR|FC1063E_ABT|FC1063E_ADR|FC1063E_ADT|FC1063E_AGR|FC1063E_AGT|FC1063E_NBT|FC1063E_NDT|FC1063E_NGT|FC133|FC133E|FC2125|FC2125E_ABR|FC2125E_ABT|FC2125E_ADR|FC2125E_ADT|FC2125E_AGR|FC2125E_AGT|FC2125E_NBT|FC2125E_NDT|FC2125E_NGT|FC266|FC266E|FC4250E_ABR|FC4250E_ABT|FC4250E_ADR|FC4250E_ADT|FC4250E_AGR|FC4250E_AGT|FC4250E_NBT|FC4250E_NDT|FC4250E_NGT|FC531|FC531E|FST1|FST2|FST3|FST4|FST5|FST6|FW1394BS1600B|FW1394BS1600BT1|FW1394BS1600BT2|FW1394BS400B|FW1394BS400BT1|FW1394BS400BT2|FW1394BS800B|FW1394BS800BT1|FW1394BS800BT2|G703DS1|G703DS3|HST<x>|INF2_5G|INF2_5GE|NONe|OC1|OC12|OC3|OC48|OC48_FEC|PCIEXPRESS_Rcv|PCIEXPRESS_Xmit|RATE32Mbit|RATE97Mbit|RIO_DRV1G|RIO_DRV1_5G|RIO_DRV2G|RIO_DRV500M|RIO_DRV500M|RIO_DRV750M|RIO_EDRV1G|RIO_EDRV1_5G|RIO_EDRV2G|RIO_EDRV500M|RIO_EDRV500M|RIO_EDRV750M|RIO_RCV1G|RIO_RCV1_5G|RIO_RCV2G|RIO_RCV500M|RIO_RCV500M|RIO_RCV750M|RIO_SERIAL_1G|RIO_SERIAL_2G|RIO_SERIAL_3G|SFI5_RCVBCLK2|SFI5_RCVBCLK3|SFI5_RCVBDATA2|SFI5_RCVBDATA3|SFI5_RCVDCLK2|SFI5_RCVDCLK3|SFI5_RCVDDATA2|SFI5_RCVDDATA3|SFI5_XMITACLK2|SFI5_XMITACLK3|SFI5_XMITADATA2|SFI5_XMITADATA3|SFI5_XMITCCLK2|SFI5_XMITCCLK3|SFI5_XMITCDATA2|SFI5_XMITCDATA3|STM0_0|STM0_1|STM0_HDBX|STM1E_1|STM1E_0|STS1Eye|STS1Pulse|STS3|STS3_Max|TFI5_2|TFI5_3|USERMask|VIDEO270|VIDEO292M|VIDEO360|VSROC192|SAS1_5_IR|SAS1_5_CR|SAS1_5_XR|SAS1_5_IR_AASJ|SAS1_5_CR_AASJ|SAS1_5_XR_AASJ|SAS1_5_SATA|SAS3_0_IR|SAS3_0_CR|SAS3_0_XR|SAS3_0_IR_AASJ|SAS3_0_CR_AASJ|SAS3_0_XR_AASJ|SAS3_0_SATA}
        - MASK:STANdard?
        ```

    Info:
        - ``ATARXG1`` (Serial ATA, G1 Rx 1.5 Gb/s).
        - ``ATARXG2`` (Serial ATA, G2, Rx, 3.0 Gb/s).
        - ``ATARXG3`` (Serial ATA, G3, Rx).
        - ``ATATXG1`` (Serial ATA, G1 Tx, 1.5 Gb/s).
        - ``ATATXG2`` (Serial ATA, G2 Tx, 3.0 Gb/s).
        - ``H ATATXG3`` (Serial ATA, G3 Tx).
        - ``CLOCKCoax``
        - ``CLOCKSymmetrical``
        - ``D1``
        - ``D2``
        - ``DS0Contra`` (ITU-T, G703 (10/98), 64 kb/s).
        - ``DS0Double`` (ITU-T, G703 (10/98), 64 kb/s).
        - ``DS0Single`` (ITU-T, G703 (10/98), 64 kb/s).
        - ``DS0Timing`` (ITU-T, G703 (10/98), 64 kb/s).
        - ``DS1`` (ANSI T1.102-1993 (R1999), DS1, 1.544 Mb/s).
        - ``DS1A`` (ANSI T1.102-1993 (R1999), DS1A, 2.048 Mb/s).
        - ``DS1C`` (ANSI T1.102-1993 (R1999), DS1C, 3.152 Mb/s).
        - ``DS2`` (ANSI T1.102-1993 (R1999), DS2, 6.312 Mb/s).
        - ``DS2RATECoax`` (ITU-T, G703 (10/98), D2 Rate Coax, 6.312 Mb/s).
        - ``DS2RATESymmetrical`` (ITU-T, G703 (10/98), D2 Rate Sym, 6.312 Mb/s).
        - ``DS3`` (ANSI T1.102-1993 (R1999), DS3, 44.736 Mb/s).
        - ``DS4NA`` (ANSI T1.102-1993 (R1999), DS4NA, 139.26 Mb/s).
        - ``DS4NA_Max`` (ANSI T1.102-1993 (R1999), DSNA Max Output, 139.26 Mb.
        - ``E1Coax`` (ITU-T, G703 (10/98), E1 Coax Pair, 2.048 Mb/s).
        - ``E1Symmetrical`` (ITU-T, G703 (10/98), E1 Sym Pair, 2.048 Mb/s).
        - ``E2`` (ITU-T, G703 (10/98), E2, 8.448 Mb/s).
        - ``E3`` (ITU-T, G703 (10/98), E3, 34.368 Mb/s).
        - ``E4_0`` (ITU-T, G703 (10/98), E4 Binary 0).
        - ``E4_1`` (ITU-T, G703 (10/98), E4 Binary 1).
        - ``ENET100FX``
        - ``ENET100STP`` (IEEE Std 802.3 and ANSI X3.263-1995, 100 Base-Tx, STP, 125 Mb/s ).
        - ``ENET100UTP`` (IEEE Std 802.3 and ANSI X3.263-1995, 100 Base-Tx, UTP, 125 Mb/s).
        - ``ENET1000BCX_ATP2`` (1000B-CX Abs, TP2, 1.25 Gb/s).
        - ``ENET1000BCX_ATP3`` (1000B-CX Abs, TP3, 1.25 Gb/s).
        - ``ENET1000BCX_NTP2`` (1000B-CX Norm, TP2, 1.25 Gb/s).
        - ``ENET1250`` (IEEE Std 802.3 and ANSI X3.263-1995, GB Ethernet, 1.25 Gb/s).
        - ``ENETXAUI_FAR`` (10 Gigabit Attachment Unit Interface (XAUI), Far, 3.125 Gb/s).
        - ``ENETXAUI_Near`` (10 Gigabit Attachment Unit Interface (XAUI), Near, 3,125 Gb/s).
        - ``FC133`` (ANSI X3.230-1999 NCITS 1235D/Rev 11, Optical, 132.8 Mb/s).
        - ``FC133E`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Electrical 132.8 Mb/s).
        - ``FC266`` (ANSI X3.230-1999 NCITS 1235D/Rev 11, Optical, 265.6 Mb/s).
        - ``FC266E`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Electrical, 132.8 Mb/s).
        - ``FC531`` (ANSI X3.230-1999 NCITS 1235D/Rev 11, Optical, 531.2 Mb/s).
        - ``FC531E`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Electrical, 531.2 Mb/s).
        - ``FC1063`` (ANSI X3.230-1999 NCITS 1235D/Rev 11, Optical, 1.065 Gb/s).
        - ``FC1063E`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Electrical, 1.0625 Gb/s).
        - ``FC1063E_ABT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Beta, Transm).
        - ``FC1063E_ADT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Beta, Transm).
        - ``FC1063E_AGT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Gamma, Transm).
        - ``FC1063E_NBT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Norm, Beta, Transm).
        - ``FC1063E_NDT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Norm, Delta, Transm).
        - ``FC1063E_NGT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Norm, Gamma, Transm).
        - ``FC1063E_ABR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Beta, Recv).
        - ``FC1063E_ADR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Delta, Recv).
        - ``FC1063E_AGR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Gamma, Recv).
        - ``FC1063Draft`` (ANSI X3.230-1999 NCITS 1235D/Rev 11, Optical, Draft Rev 11).
        - ``FC2125`` (ANSI X3.230-1999 NCITS 1235D/Rev 11, Optical, 2.125).
        - ``FC2125E_ABT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Beta, Transm).
        - ``FC2125E_ADT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Delta, Transm).
        - ``FC2125E_AGT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Gamma, Transm).
        - ``FC2125E_NBT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Norm, Beta, Transm).
        - ``FC2125E_NDT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Norm, Delta, Transm).
        - ``FC2125E_NGT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Norm, Gamma, Transm).
        - ``FC2125E_ABR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Beta, Recv).
        - ``FC2125E_ADR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Delta, Recv).
        - ``FC2125E_AGR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Gamma, Recv).
        - ``FC4250E_ABT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 4.0, Abs, Beta, Transm).
        - ``FC4250E_ADT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 4.0, Abs, Delta, Transm).
        - ``FC4250E_AGT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 4.0, Abs, Gamma, Transm).
        - ``FC4250E_NBT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 4.0, Norm, Beta, Transm).
        - ``FC4250E_NDT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 4.0, Norm, Delta, Transm).
        - ``FC4250E_NGT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 4.0, Norm, Gamma, Transm).
        - ``FC4250E_ABR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 4.0, Abs, Beta, Recv).
        - ``FC4250E_ADR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 4.0, Abs, Delta, Recv).
        - ``FC4250E_AGR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 4.0, Abs, Gamma, Recv).
        - ``FST1`` (USB, ``FS:T1``, 12 Mb/s).
        - ``FST2`` (USB, ``FS:T2``, 12 Mb/s).
        - ``FST3`` (USB, ``FS:T3``, 12 Mb/s).
        - ``FST4`` (USB, ``FS:T4``: 12 Mb/s).
        - ``FST5`` (USB, ``FS:T5``, 12 Mb/s).
        - ``FST6`` (USB, ``FS:T6``, 12 Mb/s).
        - ``FW1394BS400B`` (IEEE 1394b, S400 Optical, 491.5 Mb/s).
        - ``FW1394BS400BT1`` (IEEE 1394b, S400b T1, 491.5 Mb/s).
        - ``FW1394BS400BT2`` (IEEE 1394b, S400b T2, 491.5 Mb/s).
        - ``FW1394BS800B`` (IEEE 1394b, S800 Optical, 988.0 Mb/s).
        - ``FW1394BS800BT1`` (IEEE 1394b, S800b T1, 983.0 Mb/s).
        - ``FW1394BS800BT2`` (IEEE 1394b, S800b T2, 983.0 Mb/s).
        - ``FW1394BS1600B`` (IEEE 1394b, S1600 Optical, 1.966 Gb/s).
        - ``FW1394BS1600BT1`` (IEEE 1394b, S1600b T1, 1.966 Gb/s).
        - ``FW1394BS1600BT2`` (IEEE 1394b, S1600b T2, 1.966 Gb/s).
        - ``G703D1`` (ITU-T, G703 (10/98), DS1 Rate, 1.544 Mb/s).
        - ``G703DS3`` (ITU-T, G703 (10/98).
        - ``HST1`` (USB, ``HS:T1``, 480 Mb/s) G703DS3 (ITU-T, G703 (10/98).
        - ``HST2`` (USB, ``HS:T2``, 480 Mb/s) G703DS3 (ITU-T, G703 (10/98).
        - ``HST3`` (USB, ``HS:T3``, 480 Mb/s).
        - ``HST4`` (USB, ``HS:T4``, 480 Mb/s).
        - ``HST5`` (USB, ``HS:T5``, 480 Mb/s).
        - ``HST6`` (USB, ``HS:T6``, 480 Mb/s).
        - ``INF2_5G`` (InfiniBand, IBTA Spec 1.0a, 2.5 Optical, 2.5 Gb/s).
        - ``INF2_5GE`` (InfiniBand, IBTA Spec 1.0a, 2.5 Electrical, 2.5 Gb/s).
        - ``NONe``
        - ``OC1`` (GR 253-CORE Issue 3 9/21/2000 OC1/STM0, 51.84 Mb/s).
        - ``OC3`` (GR 253-CORE Issue 3 9/21/2000 OC1/STM1, 155.52, Mb/s).
        - ``OC12`` (GR 253-CORE Issue 3 9/21/2000 OC1/STM4, 622.08 Mb/s).
        - ``OC48`` (GR 253-CORE Issue 3 9/21/2000 OC1/STM16, 2.4883 Gb/s.
        - ``OC48_FEC`` (Forward Error Correction - CSA8000 mask, 2.666 Gb/s).
        - ``PCIEXPRESS_Xmit`` (PCI Express Transmitter, 2.5 Gb/s).
        - ``PCIEXPRESS_Rcv`` (PCI Express Receiver, 2.5 Gb/s).
        - ``RATE32Mbit`` (ITU-T, G703 (10/98), 32.064 Mb/s).
        - ``RATE97Mbit`` (ITU-T, G703 (10/98), 97 Mbit, 97.728 Mb/s).
        - ``RIO_DRV1G`` (Rapid IO Driver, 1 Gb/s).
        - ``RIO_DRV1_5G`` (Rapid IO Driver, 5 Gb/s).
        - ``RIO_DRV2G`` (Rapid IO Driver, 2 Gb/s).
        - ``RIO_DRV500M`` (Rapid IO Driver, 500 Mb/s).
        - ``RIO_DRV750M`` (Rapid IO Driver, 750 Mb/s).
        - ``RIO_EDRV1G`` (Rapid IO Extended Driver, 1 Gb/s).
        - ``RIO_EDRV1_5G`` (Rapid IO Extended Driver, 1.5 Gb/s).
        - ``RIO_EDRV2G`` (Rapid IO Extended Driver, 2 Gb/s).
        - ``RIO_EDRV500M`` (Rapid IO Extended Driver, 500 Mb/s).
        - ``RIO_EDRV750M`` (Rapid IO Extended Driver, 750 Mb/s).
        - ``RIO_RCV500M`` (Rapid IO Receiver, 500 Mb/s).
        - ``RIO_RCV750M`` (Rapid IO Receiver, 750 Mb/s).
        - ``RIO_RCV1G`` (Rapid IO Receiver, 1 Gb/s).
        - ``RIO_RCV1_5G`` (Rapid IO Receiver, 1.5 Gb/s).
        - ``RIO_RCV2G`` (Rapid IO Receiver, 2 Gb/s).
        - ``RIO_SERIAL_1G`` (Rapid IO Serial, 1.25 Gb/s).
        - ``RIO_SERIAL_2G`` (Rapid IO Serial, 2.5 Gb/s).
        - ``RIO_SERIAL_3G`` (Rapid IO Serial, 3.25 Gb/s).
        - ``SFI5_XMITADATA2`` (SFI15 Transmit: Test Point A Data Signal 2, 2.488 Gb/s).
        - ``SFI5_XMITCDATA2`` (SFI15 Transmit: Test Point C Data Signal 2, 2.488 Gb/s).
        - ``SFI5_XMITACLK2`` (SFI15 Transmit: Test Point A Clock Signal 2, 2.488 Gb/s).
        - ``SFI5_XMITCCLK2`` (SFI15 Transmit: Test Point C Clock Signal 2, 2.488 Gb/s).
        - ``SFI5_RCVBDATA2`` (SFI15 Receive: Test Point B Data Signal 2, 2.488 Gb/s).
        - ``SFI5_RCVDDATA2`` (SFI15 Receive: Test Point D Data Signal 2, 2.488 Gb/s).
        - ``SFI5_RCVBCLK2`` (SFI15 Receive: Test Point B Clock Signal 2, 2.488 Gb/s).
        - ``SFI5_RCVDCLK2`` (SFI15 Receive: Test Point D Clock Signal 2, 2.488 Gb/s).
        - ``SFI5_XMITADATA3`` (SFI15 Transmit: Test Point A Data Signal 3, 3.125 Gb/s).
        - ``SFI5_XMITCDATA3`` (SFI15 Transmit: Test Point C Data Signal 3, 3.125 Gb/s).
        - ``SFI5_XMITACLK3`` (SFI15 Transmit: Test Point A Clock Signal 3, 3.125 Gb/s).
        - ``SFI5_XMITCCLK3`` (SFI15 Transmit: Test Point C Clock Signal 3, 3.125 Gb/s).
        - ``SFI5_RCVBDATA3`` (SFI15 Receive: Test Point B Data Signal 3, 3.125 Gb/s).
        - ``SFI5_RCVDDATA3`` (SFI15 Receive: Test Point D Data Signal 3, 3.125 Gb/s).
        - ``SFI5_RCVBCLK3`` (SFI15 Receive: Test Point B Clock Signal 3, 3.125 Gb/s).
        - ``SFI5_RCVDCLK3`` (SFI15 Receive: Test Point D Clock Signal 3, 3.125 Gb/s.
        - ``STM0_0`` (ITU-T, G703 (10/98), STM1E Binary 0).
        - ``STM0_1`` (ITU-T, G703 (10/98), STM1E Binary 1).
        - ``STM0_HDBX``
        - ``STS1Eye`` (ANSI T1.102-1993 (R1999), STS-1 Eye, 51.84 Mb/s).
        - ``STS1Pulse`` (ANSI T1.102-1993 (R1999), STS-1 Pulse, 51.84 Mb/s).
        - ``STS3`` (ANSI T1.102-1993 (R1999), STS-3, 155.52 Mb/s).
        - ``STS3_Max`` (ANSI T1.102-1993 (R1999), STS-3 Max Output, 155.52 Mb/s).
        - ``TFI15_2`` (TFI-5, 2.488 Gb/s).
        - ``TFI5_3`` (TFI-5, 3.1104 Gb/s).
        - ``USERMask``
        - ``VIDEO270``
        - ``VIDEO292M``
        - ``VIDEO360``
        - ``VSROC192`` (VSR OC192/STM64, 1.24416 Gb/s).
    """  # noqa: E501


class MaskSource(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:SOUrce`` command.

    Description:
        - This command sets or reports which source will be compared against the mask(s) when
          counting is turned on; it controls which trace to use in mask counting. It also affects
          mask autoset and how triggering is set up when you select the mask.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:SOUrce?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:SOUrce value`` command.

    SCPI Syntax:
        ```
        - MASK:SOUrce {CH<x>|MATH<x>|REF<x>}
        - MASK:SOUrce?
        ```

    Info:
        - ``CH<1-4>`` selects a channel waveform to be compared against the specified mask. The
          range for is 1 through 4.
        - ``MATH<1-4>`` selects a math waveform to be compared against the specified mask. The range
          for is 1 through 4.
        - ``REF<1-4>`` selects a reference waveform to be compared against the specified mask. The
          range is 1 through 4.
    """


class MaskSegItemPoints(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:SEG<m>:POINTS`` command.

    Description:
        - This command sets or returns the X-Y user coordinates of all points in the current mask
          segment. The set form defines new points in the current mask, replacing any existing
          points in the current mask segment; it sets or returns the vertices for a particular
          segment in the current mask. m is an integer that specifies the current mask segment
          number.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:SEG<m>:POINTS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:SEG<m>:POINTS?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:SEG<m>:POINTS value`` command.

    SCPI Syntax:
        ```
        - MASK:SEG<m>:POINTS <NR3>,<NR3>[,<NR3>,<NR3>]
        - MASK:SEG<m>:POINTS?
        ```

    Info:
        - ``<NR3>`` refers to the coordinates of one of the vertices in the Current mask. Each pair
          of numbers represents the horizontal and vertical coordinates of a mask segment vertex.
          The pairs must be listed in a counterclockwise order. If the vertical or horizontal scale
          or position is changed after this command and then the query form of this command is
          issued, the value returned from the instrument will not be the same. If just one pair is
          input, it is ignored and the current mask segment is marked as undefined. The default is
          no points in the current mask segment.
    """


class MaskSegItemNrPt(SCPICmdRead):
    """The ``MASK:SEG<m>:NR_Pt`` command.

    Description:
        - This query-only command returns the number of points that make up the specified mask
          segment of the current mask. Each mask point consists of an X-Y pair of coordinates. m is
          an integer number that specifies a mask segment number of the current mask.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:SEG<m>:NR_Pt?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:SEG<m>:NR_Pt?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MASK:SEG<m>:NR_Pt?
        ```
    """


class MaskSegItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``MASK:SEG<m>`` command.

    Description:
        - This command deletes the specified mask segment from the current mask. m is an integer
          that specifies the mask segment number to delete from the current mask.

    Usage:
        - Using the ``.write(value)`` method will send the ``MASK:SEG<m> value`` command.

    SCPI Syntax:
        ```
        - MASK:SEG<m> DELEte
        ```

    Info:
        - ``DELETE`` removes the specified mask segment from the mask.

    Properties:
        - ``.nr_pt``: The ``MASK:SEG<m>:NR_Pt`` command.
        - ``.points``: The ``MASK:SEG<m>:POINTS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._nr_pt = MaskSegItemNrPt(device, f"{self._cmd_syntax}:NR_Pt")
        self._points = MaskSegItemPoints(device, f"{self._cmd_syntax}:POINTS")

    @property
    def nr_pt(self) -> MaskSegItemNrPt:
        """Return the ``MASK:SEG<m>:NR_Pt`` command.

        Description:
            - This query-only command returns the number of points that make up the specified mask
              segment of the current mask. Each mask point consists of an X-Y pair of coordinates. m
              is an integer number that specifies a mask segment number of the current mask.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:SEG<m>:NR_Pt?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:SEG<m>:NR_Pt?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MASK:SEG<m>:NR_Pt?
            ```
        """
        return self._nr_pt

    @property
    def points(self) -> MaskSegItemPoints:
        """Return the ``MASK:SEG<m>:POINTS`` command.

        Description:
            - This command sets or returns the X-Y user coordinates of all points in the current
              mask segment. The set form defines new points in the current mask, replacing any
              existing points in the current mask segment; it sets or returns the vertices for a
              particular segment in the current mask. m is an integer that specifies the current
              mask segment number.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:SEG<m>:POINTS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:SEG<m>:POINTS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:SEG<m>:POINTS value`` command.

        SCPI Syntax:
            ```
            - MASK:SEG<m>:POINTS <NR3>,<NR3>[,<NR3>,<NR3>]
            - MASK:SEG<m>:POINTS?
            ```

        Info:
            - ``<NR3>`` refers to the coordinates of one of the vertices in the Current mask. Each
              pair of numbers represents the horizontal and vertical coordinates of a mask segment
              vertex. The pairs must be listed in a counterclockwise order. If the vertical or
              horizontal scale or position is changed after this command and then the query form of
              this command is issued, the value returned from the instrument will not be the same.
              If just one pair is input, it is ignored and the current mask segment is marked as
              undefined. The default is no points in the current mask segment.
        """
        return self._points


class MaskPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:POLarity`` command.

    Description:
        - This command sets or returns the input waveform polarity for the pass/fail test. It
          controls whether to test positive pulse, negative pulse, or both during pass/fail testing.
          This command only applies when ``MASK:TEST:STATE`` is on.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:POLarity?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:POLarity value`` command.

    SCPI Syntax:
        ```
        - MASK:POLarity {BOTh|NEGAtive|POSITIVe}
        - MASK:POLarity?
        ```

    Info:
        - ``BOTh`` enables testing for both positive and negative pulses. The instrument tests
          positive pulses on the ``mask:source`` waveform until ½ of the waveform is tested. Then
          the instrument inverts the mask and performs the remaining tests.
        - ``NEGAtive`` enables testing on negative pulses.
        - ``POSITIVe`` enables testing on positive pulses. This is the default.
    """


class MaskMaskpreWidth(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:MASKPRE:WIDth`` command.

    Description:
        - This command sets or returns the nominal bit width in seconds. The query form of this
          command returns the bit width value of the displayed mask. The set form of this command
          affects only the current (displayed) mask.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASKPRE:WIDth?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASKPRE:WIDth?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:MASKPRE:WIDth value`` command.

    SCPI Syntax:
        ```
        - MASK:MASKPRE:WIDth <NR3>
        - MASK:MASKPRE:WIDth?
        ```

    Info:
        - ``<NR3>`` is a floating point number that sets the nominal bit width in seconds. This
          number is the time of one bit of data where bit width = 1 / ( data rate of the signal ).
    """


class MaskMaskpreVscale(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:MASKPRE:VSCAle`` command.

    Description:
        - This command sets or returns the nominal vertical scale in volts per division, used to
          vertically scale the input channels. The query form of this command returns the vertical
          scale value of the displayed mask. The set form of this command affects only the current
          (displayed) mask.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASKPRE:VSCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASKPRE:VSCAle?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:MASKPRE:VSCAle value`` command.

    SCPI Syntax:
        ```
        - MASK:MASKPRE:VSCAle <NR3>
        - MASK:MASKPRE:VSCAle?
        ```

    Info:
        - ``<NR3>`` is a floating point number that sets the nominal bit width in seconds.
    """


class MaskMaskpreVpos(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:MASKPRE:VPOS`` command.

    Description:
        - This command sets or returns the nominal vertical position, control in divisions, used to
          vertically position the input channels. The query form of this command returns the
          vertical position value of the displayed mask. The set form of this command affects only
          the current (displayed) mask.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASKPRE:VPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASKPRE:VPOS?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:MASKPRE:VPOS value`` command.

    SCPI Syntax:
        ```
        - MASK:MASKPRE:VPOS <NR3>
        - MASK:MASKPRE:VPOS?
        ```

    Info:
        - ``<NR3>`` is a floating point number that sets the nominal vertical position control in
          divisions.
    """


class MaskMaskpreVoffset(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:MASKPRE:VOFFSet`` command.

    Description:
        - This command sets or returns the nominal vertical offset in volts, used to vertically
          offset the input channels. The query form of this command returns the offset value of the
          displayed mask. The set form of this command affects only the current (displayed) mask.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASKPRE:VOFFSet?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASKPRE:VOFFSet?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:MASKPRE:VOFFSet value`` command.

    SCPI Syntax:
        ```
        - MASK:MASKPRE:VOFFSet <NR3>
        - MASK:MASKPRE:VOFFSet?
        ```

    Info:
        - ``<NR3>`` is a floating point number that sets the nominal vertical offset in volts.
    """


class MaskMaskpreTrigtosamp(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:MASKPRE:TRIGTOSAMP`` command.

    Description:
        - This command sets or returns the time in seconds, from the (leading edge) trigger position
          to the pulse bit sampling position. The query form of this command returns the time value
          of the displayed mask. The set form of this command only affects the current (displayed)
          mask.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASKPRE:TRIGTOSAMP?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASKPRE:TRIGTOSAMP?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:MASKPRE:TRIGTOSAMP value``
          command.

    SCPI Syntax:
        ```
        - MASK:MASKPRE:TRIGTOSAMP <NR3>
        - MASK:MASKPRE:TRIGTOSAMP?
        ```

    Info:
        - ``<NR3>`` is the floating point number that sets the time to the pulse bit sampling
          position.
    """


class MaskMaskpreSerialtrig(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:MASKPRE:SERIALTRIG`` command.

    Description:
        - This command sets or returns the type of triggering used in pass/fail testing of the
          current mask.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASKPRE:SERIALTRIG?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASKPRE:SERIALTRIG?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:MASKPRE:SERIALTRIG value``
          command.

    SCPI Syntax:
        ```
        - MASK:MASKPRE:SERIALTRIG {AMI|HDB3|B3ZS|B6ZS|B8ZS|CMI|NRZ|MLT3|EDGE}
        - MASK:MASKPRE:SERIALTRIG?
        ```

    Info:
        - ``AMI`` is Alternate Mark Inversion.
        - ``HDB3`` is High-Density Bipolar Three-Bit substitution.
        - ``B3ZS`` is Bipolar 3 Zero Substitution.
        - ``B6ZS`` is Bipolar 6 Zero Substitution.
        - ``B8ZS`` is Bipolar 8 Zero Substitution.
        - ``CMI`` is Coded Mark Inversion.
        - ``NRZ`` is Non-Return to Zero.
        - ``MLT3`` is Multi-Level Transition.
    """


class MaskMaskpreRecordlength(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:MASKPRE:RECOrdlength`` command.

    Description:
        - This command sets or returns the nominal record length for pulse mask testing. The query
          form of this command returns the record length value of the displayed mask. The set form
          of this command affects only the current (displayed) mask.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASKPRE:RECOrdlength?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASKPRE:RECOrdlength?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:MASKPRE:RECOrdlength value``
          command.

    SCPI Syntax:
        ```
        - MASK:MASKPRE:RECOrdlength <NR1>
        - MASK:MASKPRE:RECOrdlength?
        ```

    Info:
        - ``<NR1>`` is an integer number that sets the record length.
    """


class MaskMaskprePresampbits(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:MASKPRE:PRESAMPBITS`` command.

    Description:
        - This command sets or returns the number of bits before the (isolated one) pulse leading
          edge in the serial trigger pass/fail testing. For example, DS1 has four leading zeros. The
          query form of this command returns the presample bit value of the displayed mask. The set
          form of this command only affects the current (displayed) mask.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASKPRE:PRESAMPBITS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASKPRE:PRESAMPBITS?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:MASKPRE:PRESAMPBITS value``
          command.

    SCPI Syntax:
        ```
        - MASK:MASKPRE:PRESAMPBITS <NR1>
        - MASK:MASKPRE:PRESAMPBITS?
        ```

    Info:
        - ``<NR1>`` is an integer that sets the number of bits before the trigger pulse.
    """


class MaskMaskprePatternbits(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:MASKPRE:PATTERNBITS`` command.

    Description:
        - This command sets or returns the number of bits used for serial trigger for the User mask
          standard. For example, DS1 requires six bits: four leading zeros, a one, and a trailing
          zero. The query form of this command returns the serial bit value of the displayed mask.
          The set form of this command affects only the current (displayed) mask.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASKPRE:PATTERNBITS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASKPRE:PATTERNBITS?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:MASKPRE:PATTERNBITS value``
          command.

    SCPI Syntax:
        ```
        - MASK:MASKPRE:PATTERNBITS <NR1>
        - MASK:MASKPRE:PATTERNBITS?
        ```

    Info:
        - ``<NR1>`` is an integer that sets the number of bits.
    """


class MaskMaskpreHtrigpos(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:MASKPRE:HTRIGPOS`` command.

    Description:
        - This command sets or returns the nominal trigger position (pulse leading edge) used to
          draw the mask as a fraction of the display width. The query form of this command returns
          the nominal trigger position of the displayed mask. The set form of this command affects
          only the current (displayed) mask.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASKPRE:HTRIGPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASKPRE:HTRIGPOS?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:MASKPRE:HTRIGPOS value`` command.

    SCPI Syntax:
        ```
        - MASK:MASKPRE:HTRIGPOS <NR3>
        - MASK:MASKPRE:HTRIGPOS?
        ```

    Info:
        - ``<NR3>`` is a floating point number in the range of 0.0 to 1.0 that sets the trigger
          points as a fraction of the display width, referenced from the left edge of the graticule.
          The number 0.0 represents the left edge.
    """


class MaskMaskpreHscale(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:MASKPRE:HSCAle`` command.

    Description:
        - This command sets or returns the nominal timing resolution used to draw the mask in
          time/division. The query form of this command returns the nominal timing resolution of the
          displayed mask. The set form of this command affects only the current (displayed) mask.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASKPRE:HSCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASKPRE:HSCAle?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:MASKPRE:HSCAle value`` command.

    SCPI Syntax:
        ```
        - MASK:MASKPRE:HSCAle <NR3>
        - MASK:MASKPRE:HSCAle?
        ```

    Info:
        - ``<NR3>`` is a floating point number that sets the mask drawing timing resolution.
    """


class MaskMaskpreAmplitude(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:MASKPRE:AMPlitude`` command.

    Description:
        - This command sets or returns the current mask's nominal pulse amplitude in volts. The
          query form of this command returns the nominal pulse amplitude of the displayed mask. The
          set form of this command affects only the current (displayed) mask.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASKPRE:AMPlitude?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASKPRE:AMPlitude?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:MASKPRE:AMPlitude value`` command.

    SCPI Syntax:
        ```
        - MASK:MASKPRE:AMPlitude <NR3>
        - MASK:MASKPRE:AMPlitude?
        ```

    Info:
        - ``<NR3>`` is a floating number that sets the nominal pulse amplitude in volts.
    """


#  pylint: disable=too-many-instance-attributes
class MaskMaskpre(SCPICmdRead):
    """The ``MASK:MASKPRE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASKPRE?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASKPRE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.amplitude``: The ``MASK:MASKPRE:AMPlitude`` command.
        - ``.hscale``: The ``MASK:MASKPRE:HSCAle`` command.
        - ``.htrigpos``: The ``MASK:MASKPRE:HTRIGPOS`` command.
        - ``.patternbits``: The ``MASK:MASKPRE:PATTERNBITS`` command.
        - ``.presampbits``: The ``MASK:MASKPRE:PRESAMPBITS`` command.
        - ``.recordlength``: The ``MASK:MASKPRE:RECOrdlength`` command.
        - ``.serialtrig``: The ``MASK:MASKPRE:SERIALTRIG`` command.
        - ``.trigtosamp``: The ``MASK:MASKPRE:TRIGTOSAMP`` command.
        - ``.voffset``: The ``MASK:MASKPRE:VOFFSet`` command.
        - ``.vpos``: The ``MASK:MASKPRE:VPOS`` command.
        - ``.vscale``: The ``MASK:MASKPRE:VSCAle`` command.
        - ``.width``: The ``MASK:MASKPRE:WIDth`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._amplitude = MaskMaskpreAmplitude(device, f"{self._cmd_syntax}:AMPlitude")
        self._hscale = MaskMaskpreHscale(device, f"{self._cmd_syntax}:HSCAle")
        self._htrigpos = MaskMaskpreHtrigpos(device, f"{self._cmd_syntax}:HTRIGPOS")
        self._patternbits = MaskMaskprePatternbits(device, f"{self._cmd_syntax}:PATTERNBITS")
        self._presampbits = MaskMaskprePresampbits(device, f"{self._cmd_syntax}:PRESAMPBITS")
        self._recordlength = MaskMaskpreRecordlength(device, f"{self._cmd_syntax}:RECOrdlength")
        self._serialtrig = MaskMaskpreSerialtrig(device, f"{self._cmd_syntax}:SERIALTRIG")
        self._trigtosamp = MaskMaskpreTrigtosamp(device, f"{self._cmd_syntax}:TRIGTOSAMP")
        self._voffset = MaskMaskpreVoffset(device, f"{self._cmd_syntax}:VOFFSet")
        self._vpos = MaskMaskpreVpos(device, f"{self._cmd_syntax}:VPOS")
        self._vscale = MaskMaskpreVscale(device, f"{self._cmd_syntax}:VSCAle")
        self._width = MaskMaskpreWidth(device, f"{self._cmd_syntax}:WIDth")

    @property
    def amplitude(self) -> MaskMaskpreAmplitude:
        """Return the ``MASK:MASKPRE:AMPlitude`` command.

        Description:
            - This command sets or returns the current mask's nominal pulse amplitude in volts. The
              query form of this command returns the nominal pulse amplitude of the displayed mask.
              The set form of this command affects only the current (displayed) mask.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASKPRE:AMPlitude?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASKPRE:AMPlitude?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:MASKPRE:AMPlitude value``
              command.

        SCPI Syntax:
            ```
            - MASK:MASKPRE:AMPlitude <NR3>
            - MASK:MASKPRE:AMPlitude?
            ```

        Info:
            - ``<NR3>`` is a floating number that sets the nominal pulse amplitude in volts.
        """
        return self._amplitude

    @property
    def hscale(self) -> MaskMaskpreHscale:
        """Return the ``MASK:MASKPRE:HSCAle`` command.

        Description:
            - This command sets or returns the nominal timing resolution used to draw the mask in
              time/division. The query form of this command returns the nominal timing resolution of
              the displayed mask. The set form of this command affects only the current (displayed)
              mask.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASKPRE:HSCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASKPRE:HSCAle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:MASKPRE:HSCAle value``
              command.

        SCPI Syntax:
            ```
            - MASK:MASKPRE:HSCAle <NR3>
            - MASK:MASKPRE:HSCAle?
            ```

        Info:
            - ``<NR3>`` is a floating point number that sets the mask drawing timing resolution.
        """
        return self._hscale

    @property
    def htrigpos(self) -> MaskMaskpreHtrigpos:
        """Return the ``MASK:MASKPRE:HTRIGPOS`` command.

        Description:
            - This command sets or returns the nominal trigger position (pulse leading edge) used to
              draw the mask as a fraction of the display width. The query form of this command
              returns the nominal trigger position of the displayed mask. The set form of this
              command affects only the current (displayed) mask.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASKPRE:HTRIGPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASKPRE:HTRIGPOS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:MASKPRE:HTRIGPOS value``
              command.

        SCPI Syntax:
            ```
            - MASK:MASKPRE:HTRIGPOS <NR3>
            - MASK:MASKPRE:HTRIGPOS?
            ```

        Info:
            - ``<NR3>`` is a floating point number in the range of 0.0 to 1.0 that sets the trigger
              points as a fraction of the display width, referenced from the left edge of the
              graticule. The number 0.0 represents the left edge.
        """
        return self._htrigpos

    @property
    def patternbits(self) -> MaskMaskprePatternbits:
        """Return the ``MASK:MASKPRE:PATTERNBITS`` command.

        Description:
            - This command sets or returns the number of bits used for serial trigger for the User
              mask standard. For example, DS1 requires six bits: four leading zeros, a one, and a
              trailing zero. The query form of this command returns the serial bit value of the
              displayed mask. The set form of this command affects only the current (displayed)
              mask.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASKPRE:PATTERNBITS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASKPRE:PATTERNBITS?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:MASKPRE:PATTERNBITS value``
              command.

        SCPI Syntax:
            ```
            - MASK:MASKPRE:PATTERNBITS <NR1>
            - MASK:MASKPRE:PATTERNBITS?
            ```

        Info:
            - ``<NR1>`` is an integer that sets the number of bits.
        """
        return self._patternbits

    @property
    def presampbits(self) -> MaskMaskprePresampbits:
        """Return the ``MASK:MASKPRE:PRESAMPBITS`` command.

        Description:
            - This command sets or returns the number of bits before the (isolated one) pulse
              leading edge in the serial trigger pass/fail testing. For example, DS1 has four
              leading zeros. The query form of this command returns the presample bit value of the
              displayed mask. The set form of this command only affects the current (displayed)
              mask.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASKPRE:PRESAMPBITS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASKPRE:PRESAMPBITS?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:MASKPRE:PRESAMPBITS value``
              command.

        SCPI Syntax:
            ```
            - MASK:MASKPRE:PRESAMPBITS <NR1>
            - MASK:MASKPRE:PRESAMPBITS?
            ```

        Info:
            - ``<NR1>`` is an integer that sets the number of bits before the trigger pulse.
        """
        return self._presampbits

    @property
    def recordlength(self) -> MaskMaskpreRecordlength:
        """Return the ``MASK:MASKPRE:RECOrdlength`` command.

        Description:
            - This command sets or returns the nominal record length for pulse mask testing. The
              query form of this command returns the record length value of the displayed mask. The
              set form of this command affects only the current (displayed) mask.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASKPRE:RECOrdlength?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASKPRE:RECOrdlength?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:MASKPRE:RECOrdlength value``
              command.

        SCPI Syntax:
            ```
            - MASK:MASKPRE:RECOrdlength <NR1>
            - MASK:MASKPRE:RECOrdlength?
            ```

        Info:
            - ``<NR1>`` is an integer number that sets the record length.
        """
        return self._recordlength

    @property
    def serialtrig(self) -> MaskMaskpreSerialtrig:
        """Return the ``MASK:MASKPRE:SERIALTRIG`` command.

        Description:
            - This command sets or returns the type of triggering used in pass/fail testing of the
              current mask.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASKPRE:SERIALTRIG?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASKPRE:SERIALTRIG?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:MASKPRE:SERIALTRIG value``
              command.

        SCPI Syntax:
            ```
            - MASK:MASKPRE:SERIALTRIG {AMI|HDB3|B3ZS|B6ZS|B8ZS|CMI|NRZ|MLT3|EDGE}
            - MASK:MASKPRE:SERIALTRIG?
            ```

        Info:
            - ``AMI`` is Alternate Mark Inversion.
            - ``HDB3`` is High-Density Bipolar Three-Bit substitution.
            - ``B3ZS`` is Bipolar 3 Zero Substitution.
            - ``B6ZS`` is Bipolar 6 Zero Substitution.
            - ``B8ZS`` is Bipolar 8 Zero Substitution.
            - ``CMI`` is Coded Mark Inversion.
            - ``NRZ`` is Non-Return to Zero.
            - ``MLT3`` is Multi-Level Transition.
        """
        return self._serialtrig

    @property
    def trigtosamp(self) -> MaskMaskpreTrigtosamp:
        """Return the ``MASK:MASKPRE:TRIGTOSAMP`` command.

        Description:
            - This command sets or returns the time in seconds, from the (leading edge) trigger
              position to the pulse bit sampling position. The query form of this command returns
              the time value of the displayed mask. The set form of this command only affects the
              current (displayed) mask.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASKPRE:TRIGTOSAMP?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASKPRE:TRIGTOSAMP?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:MASKPRE:TRIGTOSAMP value``
              command.

        SCPI Syntax:
            ```
            - MASK:MASKPRE:TRIGTOSAMP <NR3>
            - MASK:MASKPRE:TRIGTOSAMP?
            ```

        Info:
            - ``<NR3>`` is the floating point number that sets the time to the pulse bit sampling
              position.
        """
        return self._trigtosamp

    @property
    def voffset(self) -> MaskMaskpreVoffset:
        """Return the ``MASK:MASKPRE:VOFFSet`` command.

        Description:
            - This command sets or returns the nominal vertical offset in volts, used to vertically
              offset the input channels. The query form of this command returns the offset value of
              the displayed mask. The set form of this command affects only the current (displayed)
              mask.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASKPRE:VOFFSet?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASKPRE:VOFFSet?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:MASKPRE:VOFFSet value``
              command.

        SCPI Syntax:
            ```
            - MASK:MASKPRE:VOFFSet <NR3>
            - MASK:MASKPRE:VOFFSet?
            ```

        Info:
            - ``<NR3>`` is a floating point number that sets the nominal vertical offset in volts.
        """
        return self._voffset

    @property
    def vpos(self) -> MaskMaskpreVpos:
        """Return the ``MASK:MASKPRE:VPOS`` command.

        Description:
            - This command sets or returns the nominal vertical position, control in divisions, used
              to vertically position the input channels. The query form of this command returns the
              vertical position value of the displayed mask. The set form of this command affects
              only the current (displayed) mask.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASKPRE:VPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASKPRE:VPOS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:MASKPRE:VPOS value`` command.

        SCPI Syntax:
            ```
            - MASK:MASKPRE:VPOS <NR3>
            - MASK:MASKPRE:VPOS?
            ```

        Info:
            - ``<NR3>`` is a floating point number that sets the nominal vertical position control
              in divisions.
        """
        return self._vpos

    @property
    def vscale(self) -> MaskMaskpreVscale:
        """Return the ``MASK:MASKPRE:VSCAle`` command.

        Description:
            - This command sets or returns the nominal vertical scale in volts per division, used to
              vertically scale the input channels. The query form of this command returns the
              vertical scale value of the displayed mask. The set form of this command affects only
              the current (displayed) mask.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASKPRE:VSCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASKPRE:VSCAle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:MASKPRE:VSCAle value``
              command.

        SCPI Syntax:
            ```
            - MASK:MASKPRE:VSCAle <NR3>
            - MASK:MASKPRE:VSCAle?
            ```

        Info:
            - ``<NR3>`` is a floating point number that sets the nominal bit width in seconds.
        """
        return self._vscale

    @property
    def width(self) -> MaskMaskpreWidth:
        """Return the ``MASK:MASKPRE:WIDth`` command.

        Description:
            - This command sets or returns the nominal bit width in seconds. The query form of this
              command returns the bit width value of the displayed mask. The set form of this
              command affects only the current (displayed) mask.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASKPRE:WIDth?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASKPRE:WIDth?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:MASKPRE:WIDth value`` command.

        SCPI Syntax:
            ```
            - MASK:MASKPRE:WIDth <NR3>
            - MASK:MASKPRE:WIDth?
            ```

        Info:
            - ``<NR3>`` is a floating point number that sets the nominal bit width in seconds. This
              number is the time of one bit of data where bit width = 1 / ( data rate of the signal
              ).
        """
        return self._width


class MaskMarginState(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:MARgin:STATE`` command.

    Description:
        - This command sets or returns the state of the mask margins.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MARgin:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MARgin:STATE?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:MARgin:STATE value`` command.

    SCPI Syntax:
        ```
        - MASK:MARgin:STATE {ON|OFF|<NR1>}
        - MASK:MARgin:STATE?
        ```

    Info:
        - ``<NR1>`` = 0 turns off mask margins; any other integer turns on the selected mask
          margins.
        - ``OFF`` turns off mask margins. The currently displayed margined mask is erased and the
          original mask is displayed.
        - ``ON`` turns on mask margins.
    """


class MaskMarginPercent(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:MARgin:PERCent`` command.

    Description:
        - Sets or returns the tolerance for the mask test. A positive value expands the mask and a
          negative margin shrinks the mask by the specified percentage. A series of examples showing
          how to use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MARgin:PERCent?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MARgin:PERCent?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:MARgin:PERCent value`` command.

    SCPI Syntax:
        ```
        - MASK:MARgin:PERCent <NR3>
        - MASK:MARgin:PERCent?
        ```

    Info:
        - ``<NR3>`` is a floating point value that ranges from -50.0 to +50.0. The default is 5.
    """


class MaskMargin(SCPICmdRead):
    """The ``MASK:MARgin`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MARgin?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MARgin?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.percent``: The ``MASK:MARgin:PERCent`` command.
        - ``.state``: The ``MASK:MARgin:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._percent = MaskMarginPercent(device, f"{self._cmd_syntax}:PERCent")
        self._state = MaskMarginState(device, f"{self._cmd_syntax}:STATE")

    @property
    def percent(self) -> MaskMarginPercent:
        """Return the ``MASK:MARgin:PERCent`` command.

        Description:
            - Sets or returns the tolerance for the mask test. A positive value expands the mask and
              a negative margin shrinks the mask by the specified percentage. A series of examples
              showing how to use mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MARgin:PERCent?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MARgin:PERCent?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:MARgin:PERCent value``
              command.

        SCPI Syntax:
            ```
            - MASK:MARgin:PERCent <NR3>
            - MASK:MARgin:PERCent?
            ```

        Info:
            - ``<NR3>`` is a floating point value that ranges from -50.0 to +50.0. The default is 5.
        """
        return self._percent

    @property
    def state(self) -> MaskMarginState:
        """Return the ``MASK:MARgin:STATE`` command.

        Description:
            - This command sets or returns the state of the mask margins.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MARgin:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MARgin:STATE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:MARgin:STATE value`` command.

        SCPI Syntax:
            ```
            - MASK:MARgin:STATE {ON|OFF|<NR1>}
            - MASK:MARgin:STATE?
            ```

        Info:
            - ``<NR1>`` = 0 turns off mask margins; any other integer turns on the selected mask
              margins.
            - ``OFF`` turns off mask margins. The currently displayed margined mask is erased and
              the original mask is displayed.
            - ``ON`` turns on mask margins.
        """
        return self._state


class MaskLock(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:LOCk`` command.

    Description:
        - This command locks the mask to the source waveform so that any changes made to the
          horizontal and/or vertical scale settings of the waveform will redraw the mask segments in
          proportion. This feature is useful for expanding the horizontal and/or vertical settings
          in order to zoom in on waveforms and masks, and visually examine violation areas in more
          detail. A series of examples showing how to use mask commands for typical tasks is
          included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:LOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:LOCk?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:LOCk value`` command.

    SCPI Syntax:
        ```
        - MASK:LOCk {ON|OFF|<NR1>}
        - MASK:LOCk?
        ```

    Info:
        - ``ON`` turns on this feature, so that the mask is locked to the waveform.
        - ``OFF`` turns off this feature.
        - ``<NR1> = 0`` turns off this feature. Any other value turns it on.
    """


class MaskInvert(SCPICmdWrite):
    """The ``MASK:INVert`` command.

    Description:
        - This command controls whether the mask is drawn inverted. It has no effect if this mask
          cannot be inverted. The default is Off (Positive).

    Usage:
        - Using the ``.write(value)`` method will send the ``MASK:INVert value`` command.

    SCPI Syntax:
        ```
        - MASK:INVert {ON|OFF|<NR1>}
        ```

    Info:
        - ``<NR1>`` = 0 disables the ``mask:invert`` function; any other value enables it.
        - ``OFF`` Positive.
        - ``ON`` Negative.
    """


class MaskHighlighthits(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:HIGHLIGHTHits`` command.

    Description:
        - This command sets or returns whether hits in a mask are highlighted in different colors
          than other waveform data. The default is On.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:HIGHLIGHTHits?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:HIGHLIGHTHits?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:HIGHLIGHTHits value`` command.

    SCPI Syntax:
        ```
        - MASK:HIGHLIGHTHits {ON|OFF|<NR1>}
        - MASK:HIGHLIGHTHits?
        ```

    Info:
        - ``<NR1>`` = 0 disables the ``mask:highlighthits`` function; any other value enables it.
        - ``OFF`` disables the ``mask:highlighthits`` function.
        - ``ON`` enables the ``mask:highlighthits`` function.
    """


class MaskFilterOrrVertIndex(SCPICmdReadWithArguments):
    """The ``MASK:FILTer:ORR:VERT_INDEX`` command.

    Description:
        - This query-only command returns the optional channel specified vertical index used in the
          calibration filter. If no argument is supplied, CH1 vertical index is returned.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``MASK:FILTer:ORR:VERT_INDEX? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``MASK:FILTer:ORR:VERT_INDEX? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.

    SCPI Syntax:
        ```
        - MASK:FILTer:ORR:VERT_INDEX? CH<x>
        ```
    """


class MaskFilterOrr(SCPICmdRead):
    """The ``MASK:FILTer:ORR`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:FILTer:ORR?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:FILTer:ORR?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.vert_index``: The ``MASK:FILTer:ORR:VERT_INDEX`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._vert_index = MaskFilterOrrVertIndex(device, f"{self._cmd_syntax}:VERT_INDEX")

    @property
    def vert_index(self) -> MaskFilterOrrVertIndex:
        """Return the ``MASK:FILTer:ORR:VERT_INDEX`` command.

        Description:
            - This query-only command returns the optional channel specified vertical index used in
              the calibration filter. If no argument is supplied, CH1 vertical index is returned.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``MASK:FILTer:ORR:VERT_INDEX? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``MASK:FILTer:ORR:VERT_INDEX? argument`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MASK:FILTer:ORR:VERT_INDEX? CH<x>
            ```
        """
        return self._vert_index


class MaskFilter(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:FILTer`` command.

    Description:
        - This command sets or returns whether the selected digital filter will be run on the
          waveform data. The filter simulates optical hardware. That is, it simulates different
          hardware for each of several different optical standards. The digital filter runs on OC1,
          OC3, OC12, OC48, FC133, FC266, FC531, FC1063, FC2125Draft, Gigabit Ethernet, Infiniband
          2.5 Gb, 1394 b, 393 Mb, 786.43 Mb, 1.572 Gb

    Usage:
        - Using the ``.query()`` method will send the ``MASK:FILTer?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:FILTer?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:FILTer value`` command.

    SCPI Syntax:
        ```
        - MASK:FILTer {ON|OFF|<NR1>}
        - MASK:FILTer?
        ```

    Info:
        - ``<NR1>`` = 0 disables the digital filter; any other value enables it.
        - ``OFF`` disables the digital filter.
        - ``ON`` enables the digital filter.

    Properties:
        - ``.orr``: The ``MASK:FILTer:ORR`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._orr = MaskFilterOrr(device, f"{self._cmd_syntax}:ORR")

    @property
    def orr(self) -> MaskFilterOrr:
        """Return the ``MASK:FILTer:ORR`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:FILTer:ORR?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:FILTer:ORR?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.vert_index``: The ``MASK:FILTer:ORR:VERT_INDEX`` command.
        """
        return self._orr


class MaskDisplay(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:DISplay`` command.

    Description:
        - This command sets or queries whether defined masks are displayed on the screen. This is
          useful for temporarily turning off user-defined masks without deleting them. It is also
          useful for removing a standard mask from the screen, but leaving it as the selected
          standard. Mask counting, mask testing, and mask autoset are unavailable if the mask
          display is Off. The default is On.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:DISplay?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:DISplay?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:DISplay value`` command.

    SCPI Syntax:
        ```
        - MASK:DISplay {ON|OFF|<NR1>}
        - MASK:DISplay?
        ```

    Info:
        - ``<NR1>`` = 0 removes the masks from the display; any other value shows the masks on the
          display.
        - ``ON`` shows the masks on the display. This is the default value.
        - ``OFF`` removes the masks from the display.
    """


class MaskCountWaveforms(SCPICmdRead):
    """The ``MASK:COUNt:WAVEFORMS`` command.

    Description:
        - This query returns the number of waveforms that have been acquired and processed during
          pass/fail mask testing. A series of examples showing how to use mask commands for typical
          tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:COUNt:WAVEFORMS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:COUNt:WAVEFORMS?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MASK:COUNt:WAVEFORMS?
        ```
    """


class MaskCountViolations(SCPICmdRead):
    """The ``MASK:COUNt:VIOLATIONS`` command.

    Description:
        - This query returns the number of test violations that have occurred in the current mask
          pass/fail test. A test violation occurs when any part of a waveform falls within any mask
          segment. The default is 0. A series of examples showing how to use mask commands for
          typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:COUNt:VIOLATIONS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:COUNt:VIOLATIONS?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MASK:COUNt:VIOLATIONS?
        ```
    """


class MaskCountTotal(SCPICmdRead):
    """The ``MASK:COUNt:TOTal`` command.

    Description:
        - This query-only command returns the sum of all hits in all mask segments. This command is
          the same as ``MASK:COUNT:HITS?`` and is kept for compatibility with other Tektronix
          instruments.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:COUNt:TOTal?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:COUNt:TOTal?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MASK:COUNt:TOTal?
        ```
    """


class MaskCountTests(SCPICmdRead):
    """The ``MASK:COUNt:TESTS`` command.

    Description:
        - This query returns the number of pass/fail mask tests that have occurred. A series of
          examples showing how to use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:COUNt:TESTS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:COUNt:TESTS?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MASK:COUNt:TESTS?
        ```
    """


class MaskCountState(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:COUNt:STATE`` command.

    Description:
        - This command sets or queries the mask hits count state; it controls whether mask counting
          is being done. ``MASK:DISPLAY`` must be ON to enable ``MASK:COUNt:STATE`` to count mask
          violations.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:COUNt:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:COUNt:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:COUNt:STATE value`` command.

    SCPI Syntax:
        ```
        - MASK:COUNt:STATE {ON|OFF|<NR1>}
        - MASK:COUNt:STATE?
        ```

    Info:
        - ``<NR1>`` = 0 turns off mask hit counting, and other values turn on mask hit counting.
        - ``ON`` turns on mask counting.
        - ``OFF`` turns off mask counting. This is the default state.
    """


class MaskCountSegItemHits(SCPICmdRead):
    """The ``MASK:COUNt:SEG<m>:HITS`` command.

    Description:
        - This query-only command returns the number of hits in mask segment <m>. Hit counting must
          be turned on. m is the mask segment number.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:COUNt:SEG<m>:HITS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:COUNt:SEG<m>:HITS?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MASK:COUNt:SEG<m>:HITS?
        ```
    """


class MaskCountSegItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``MASK:COUNt:SEG<m>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:COUNt:SEG<m>?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:COUNt:SEG<m>?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.hits``: The ``MASK:COUNt:SEG<m>:HITS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hits = MaskCountSegItemHits(device, f"{self._cmd_syntax}:HITS")

    @property
    def hits(self) -> MaskCountSegItemHits:
        """Return the ``MASK:COUNt:SEG<m>:HITS`` command.

        Description:
            - This query-only command returns the number of hits in mask segment <m>. Hit counting
              must be turned on. m is the mask segment number.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:COUNt:SEG<m>:HITS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:COUNt:SEG<m>:HITS?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MASK:COUNt:SEG<m>:HITS?
            ```
        """
        return self._hits


class MaskCountHits(SCPICmdRead):
    """The ``MASK:COUNt:HITS`` command.

    Description:
        - This query returns the sum of all hits in all mask segments. A series of examples showing
          how to use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:COUNt:HITS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:COUNt:HITS?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MASK:COUNt:HITS?
        ```
    """


class MaskCountFailures(SCPICmdRead):
    """The ``MASK:COUNt:FAILURES`` command.

    Description:
        - This query returns the number of pass/fail mask tests that have failed. A series of
          examples showing how to use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:COUNt:FAILURES?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:COUNt:FAILURES?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MASK:COUNt:FAILURES?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class MaskCount(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:COUNt`` command.

    Description:
        - This command resets to zero the number of hits and failures for all mask segments. A
          series of examples showing how to use mask commands for typical tasks is included in an
          appendix.

    Usage:
        - Using the ``.write(value)`` method will send the ``MASK:COUNt value`` command.

    SCPI Syntax:
        ```
        - MASK:COUNt RESET
        ```

    Properties:
        - ``.failures``: The ``MASK:COUNt:FAILURES`` command.
        - ``.hits``: The ``MASK:COUNt:HITS`` command.
        - ``.seg``: The ``MASK:COUNt:SEG<m>`` command tree.
        - ``.state``: The ``MASK:COUNt:STATE`` command.
        - ``.tests``: The ``MASK:COUNt:TESTS`` command.
        - ``.total``: The ``MASK:COUNt:TOTal`` command.
        - ``.violations``: The ``MASK:COUNt:VIOLATIONS`` command.
        - ``.waveforms``: The ``MASK:COUNt:WAVEFORMS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._failures = MaskCountFailures(device, f"{self._cmd_syntax}:FAILURES")
        self._hits = MaskCountHits(device, f"{self._cmd_syntax}:HITS")
        self._seg: Dict[int, MaskCountSegItem] = DefaultDictPassKeyToFactory(
            lambda x: MaskCountSegItem(device, f"{self._cmd_syntax}:SEG{x}")
        )
        self._state = MaskCountState(device, f"{self._cmd_syntax}:STATE")
        self._tests = MaskCountTests(device, f"{self._cmd_syntax}:TESTS")
        self._total = MaskCountTotal(device, f"{self._cmd_syntax}:TOTal")
        self._violations = MaskCountViolations(device, f"{self._cmd_syntax}:VIOLATIONS")
        self._waveforms = MaskCountWaveforms(device, f"{self._cmd_syntax}:WAVEFORMS")

    @property
    def failures(self) -> MaskCountFailures:
        """Return the ``MASK:COUNt:FAILURES`` command.

        Description:
            - This query returns the number of pass/fail mask tests that have failed. A series of
              examples showing how to use mask commands for typical tasks is included in an
              appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:COUNt:FAILURES?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:COUNt:FAILURES?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MASK:COUNt:FAILURES?
            ```
        """
        return self._failures

    @property
    def hits(self) -> MaskCountHits:
        """Return the ``MASK:COUNt:HITS`` command.

        Description:
            - This query returns the sum of all hits in all mask segments. A series of examples
              showing how to use mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:COUNt:HITS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:COUNt:HITS?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MASK:COUNt:HITS?
            ```
        """
        return self._hits

    @property
    def seg(self) -> Dict[int, MaskCountSegItem]:
        """Return the ``MASK:COUNt:SEG<m>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:COUNt:SEG<m>?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:COUNt:SEG<m>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.hits``: The ``MASK:COUNt:SEG<m>:HITS`` command.
        """
        return self._seg

    @property
    def state(self) -> MaskCountState:
        """Return the ``MASK:COUNt:STATE`` command.

        Description:
            - This command sets or queries the mask hits count state; it controls whether mask
              counting is being done. ``MASK:DISPLAY`` must be ON to enable ``MASK:COUNt:STATE`` to
              count mask violations.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:COUNt:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:COUNt:STATE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:COUNt:STATE value`` command.

        SCPI Syntax:
            ```
            - MASK:COUNt:STATE {ON|OFF|<NR1>}
            - MASK:COUNt:STATE?
            ```

        Info:
            - ``<NR1>`` = 0 turns off mask hit counting, and other values turn on mask hit counting.
            - ``ON`` turns on mask counting.
            - ``OFF`` turns off mask counting. This is the default state.
        """
        return self._state

    @property
    def tests(self) -> MaskCountTests:
        """Return the ``MASK:COUNt:TESTS`` command.

        Description:
            - This query returns the number of pass/fail mask tests that have occurred. A series of
              examples showing how to use mask commands for typical tasks is included in an
              appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:COUNt:TESTS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:COUNt:TESTS?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MASK:COUNt:TESTS?
            ```
        """
        return self._tests

    @property
    def total(self) -> MaskCountTotal:
        """Return the ``MASK:COUNt:TOTal`` command.

        Description:
            - This query-only command returns the sum of all hits in all mask segments. This command
              is the same as ``MASK:COUNT:HITS?`` and is kept for compatibility with other Tektronix
              instruments.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:COUNt:TOTal?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:COUNt:TOTal?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MASK:COUNt:TOTal?
            ```
        """
        return self._total

    @property
    def violations(self) -> MaskCountViolations:
        """Return the ``MASK:COUNt:VIOLATIONS`` command.

        Description:
            - This query returns the number of test violations that have occurred in the current
              mask pass/fail test. A test violation occurs when any part of a waveform falls within
              any mask segment. The default is 0. A series of examples showing how to use mask
              commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:COUNt:VIOLATIONS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:COUNt:VIOLATIONS?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MASK:COUNt:VIOLATIONS?
            ```
        """
        return self._violations

    @property
    def waveforms(self) -> MaskCountWaveforms:
        """Return the ``MASK:COUNt:WAVEFORMS`` command.

        Description:
            - This query returns the number of waveforms that have been acquired and processed
              during pass/fail mask testing. A series of examples showing how to use mask commands
              for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:COUNt:WAVEFORMS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:COUNt:WAVEFORMS?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MASK:COUNt:WAVEFORMS?
            ```
        """
        return self._waveforms


class MaskCopyUser(SCPICmdWriteNoArguments):
    """The ``MASK:COPy:USER`` command.

    Description:
        - This creates a user-defined custom mask by making a copy of the source mask that was
          specified prior with the command . The source mask could be a standard, limit or another
          custom mask. A series of examples showing how to use mask commands for typical tasks is
          included in an appendix.

    Usage:
        - Using the ``.write()`` method will send the ``MASK:COPy:USER`` command.

    SCPI Syntax:
        ```
        - MASK:COPy:USER
        ```
    """


class MaskCopy(SCPICmdRead):
    """The ``MASK:COPy`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:COPy?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:COPy?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.user``: The ``MASK:COPy:USER`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._user = MaskCopyUser(device, f"{self._cmd_syntax}:USER")

    @property
    def user(self) -> MaskCopyUser:
        """Return the ``MASK:COPy:USER`` command.

        Description:
            - This creates a user-defined custom mask by making a copy of the source mask that was
              specified prior with the command . The source mask could be a standard, limit or
              another custom mask. A series of examples showing how to use mask commands for typical
              tasks is included in an appendix.

        Usage:
            - Using the ``.write()`` method will send the ``MASK:COPy:USER`` command.

        SCPI Syntax:
            ```
            - MASK:COPy:USER
            ```
        """
        return self._user


class MaskAutosetVscale(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:AUTOSet:VSCAle`` command.

    Description:
        - This command controls whether the mask autoset algorithm will affect the vertical scale
          while attempting to autoset. This command, like all the mask autoset commands, affects
          only an autoset on a standard mask, not the general instrument autoset function.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:AUTOSet:VSCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet:VSCAle?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:AUTOSet:VSCAle value`` command.

    SCPI Syntax:
        ```
        - MASK:AUTOSet:VSCAle {ON|OFF|<NR1>}
        - MASK:AUTOSet:VSCAle?
        ```

    Info:
        - ``<NR1>`` = 0 disables the ``autoset:vscale`` function; any other value enables it.
        - ``ON`` enables the ``autoset:vscale`` function.
        - ``OFF`` disables the ``autoset:vscale`` function.
    """


class MaskAutosetVpos(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:AUTOSet:VPOS`` command.

    Description:
        - This command controls whether the mask autoset algorithm will affect the vertical position
          (or offset) of the signal while attempting to autoset. The default is ON. This command,
          like all the mask autoset commands, affects only an autoset on a standard mask, not the
          general instrument autoset function.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:AUTOSet:VPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet:VPOS?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:AUTOSet:VPOS value`` command.

    SCPI Syntax:
        ```
        - MASK:AUTOSet:VPOS {ON|OFF|<NR1>}
        - MASK:AUTOSet:VPOS?
        ```

    Info:
        - ``<NR1>`` = 0 disables the ``autoset:vpos`` function; any other value enables it.
        - ``ON`` enables the ``autoset:vpos`` function.
        - ``OFF`` disables the ``autoset:vpos`` function.
    """


class MaskAutosetUserZero(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:AUTOSet:USER:ZERo`` command.

    Description:
        - This command sets or queries the level 0 used by autoset for user masks.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:AUTOSet:USER:ZERo?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet:USER:ZERo?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:AUTOSet:USER:ZERo value`` command.

    SCPI Syntax:
        ```
        - MASK:AUTOSet:USER:ZERo <NR3>
        - MASK:AUTOSet:USER:ZERo?
        ```

    Info:
        - ``<NR3>`` sets the zero level that autoset uses for user masks.
    """


class MaskAutosetUserType(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:AUTOSet:USER:TYPe`` command.

    Description:
        - This command sets or queries how autoset scales a mask.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:AUTOSet:USER:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet:USER:TYPe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:AUTOSet:USER:TYPe value`` command.

    SCPI Syntax:
        ```
        - MASK:AUTOSet:USER:TYPe {ABSolute|NORMALIZed}
        - MASK:AUTOSet:USER:TYPe?
        ```

    Info:
        - ``ABSOLUTE`` tells autoset to use the values supplied by ``MASK:AUTOSET:USER:ONE`` and
          ``MASK:AUTOSET:USER:ZERO`` for the one and zero of the mask.
        - ``NORMALIZED`` tells autoset to determine the mask one and zero by looking at the mask.
    """


class MaskAutosetUserOne(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:AUTOSet:USER:ONE`` command.

    Description:
        - This command sets or queries the level 1 value used by autoset for user masks.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:AUTOSet:USER:ONE?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet:USER:ONE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:AUTOSet:USER:ONE value`` command.

    SCPI Syntax:
        ```
        - MASK:AUTOSet:USER:ONE <NR3>
        - MASK:AUTOSet:USER:ONE?
        ```

    Info:
        - ``<NR3>`` sets the level 1 value used by autoset for user masks.
    """


class MaskAutosetUser(SCPICmdRead):
    """The ``MASK:AUTOSet:USER`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:AUTOSet:USER?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet:USER?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.one``: The ``MASK:AUTOSet:USER:ONE`` command.
        - ``.type``: The ``MASK:AUTOSet:USER:TYPe`` command.
        - ``.zero``: The ``MASK:AUTOSet:USER:ZERo`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._one = MaskAutosetUserOne(device, f"{self._cmd_syntax}:ONE")
        self._type = MaskAutosetUserType(device, f"{self._cmd_syntax}:TYPe")
        self._zero = MaskAutosetUserZero(device, f"{self._cmd_syntax}:ZERo")

    @property
    def one(self) -> MaskAutosetUserOne:
        """Return the ``MASK:AUTOSet:USER:ONE`` command.

        Description:
            - This command sets or queries the level 1 value used by autoset for user masks.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:AUTOSet:USER:ONE?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet:USER:ONE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:AUTOSet:USER:ONE value``
              command.

        SCPI Syntax:
            ```
            - MASK:AUTOSet:USER:ONE <NR3>
            - MASK:AUTOSet:USER:ONE?
            ```

        Info:
            - ``<NR3>`` sets the level 1 value used by autoset for user masks.
        """
        return self._one

    @property
    def type(self) -> MaskAutosetUserType:
        """Return the ``MASK:AUTOSet:USER:TYPe`` command.

        Description:
            - This command sets or queries how autoset scales a mask.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:AUTOSet:USER:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet:USER:TYPe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:AUTOSet:USER:TYPe value``
              command.

        SCPI Syntax:
            ```
            - MASK:AUTOSet:USER:TYPe {ABSolute|NORMALIZed}
            - MASK:AUTOSet:USER:TYPe?
            ```

        Info:
            - ``ABSOLUTE`` tells autoset to use the values supplied by ``MASK:AUTOSET:USER:ONE`` and
              ``MASK:AUTOSET:USER:ZERO`` for the one and zero of the mask.
            - ``NORMALIZED`` tells autoset to determine the mask one and zero by looking at the
              mask.
        """
        return self._type

    @property
    def zero(self) -> MaskAutosetUserZero:
        """Return the ``MASK:AUTOSet:USER:ZERo`` command.

        Description:
            - This command sets or queries the level 0 used by autoset for user masks.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:AUTOSet:USER:ZERo?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet:USER:ZERo?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:AUTOSet:USER:ZERo value``
              command.

        SCPI Syntax:
            ```
            - MASK:AUTOSet:USER:ZERo <NR3>
            - MASK:AUTOSet:USER:ZERo?
            ```

        Info:
            - ``<NR3>`` sets the zero level that autoset uses for user masks.
        """
        return self._zero


class MaskAutosetTrigger(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:AUTOSet:TRIGger`` command.

    Description:
        - This command specifies whether a mask AUTOSET affects the trigger level. Other trigger
          settings such as type of trigger are not changed by autoset. The default is ON. This
          command, like all the mask autoset commands, affects only an autoset on a standard mask,
          not the general instrument autoset function.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:AUTOSet:TRIGger?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet:TRIGger?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:AUTOSet:TRIGger value`` command.

    SCPI Syntax:
        ```
        - MASK:AUTOSet:TRIGger {ON|OFF|<NR1>}
        - MASK:AUTOSet:TRIGger?
        ```

    Info:
        - ``<NR1>`` = 0 disables the ``autoset:trigger`` function; any other value enables it.
        - ``ON`` enables the ``autoset:trigger`` function.
        - ``OFF`` disables the ``autoset:trigger`` function.
    """


class MaskAutosetStandard(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:AUTOSet:STANdard`` command.

    Description:
        - This command selects the standard mask in a mask autoset. This command, like all the
          ``MASK:AUTOSET`` commands, affects only an autoset on a standard mask, not the general
          instrument autoset function.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:AUTOSet:STANdard?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet:STANdard?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:AUTOSet:STANdard value`` command.

    SCPI Syntax:
        ```
        - MASK:AUTOSet:STANdard {ATATXG<x>|ATARXG<x>|CLOCKCoax|CLOCKSymmetrical|D<x>|DS0Contra|DS0Double|DS0Single|DS0Timing|DS1|DS1A|DS1C|DS2RATESymmetrical|DS2RATECoax|DS2|DS3|DS4NA|DS4NA_Max|E1Symmetrical|E1Coax|E2|E3|E4_0|E4_1|ENET100FX|ENET100STP|ENET100UTP|ENET1250|ENET1000BCX_NTP2|ENET1000BCX_ATP2|ENET1000BCX_ATP3|ENETXAUI_Near|ENETXAUI_Far|FC133|FC266|FC531|FC1063|FC1063Draft|FC2125|FC133E|FC266E|FC531E|FC1063E|FC1063E_NBT|FC1063E_NDT|FC1063E_NGT|FC1063E_ABT|FC1063E_ADT|FC1063E_AGT|FC1063E_ABR|FC1063E_ADR|FC1063E_AGR|FC2125E_NBT|FC2125E_NDT|FC2125E_NGT|FC2125E_ABT|FC2125E_ADT|FC2125E_AGT|FC2125E_ABR|FC2125E_ADR|FC2125E_AGR|FC4250E_ABR|FC4250E_ABT|FC4250E_ADR|FC4250E_ADT|FC4250E_AGR|FC4250E_AGT|FC4250E_NBT|FC4250E_NDT|FC4250E_NGT|FST1|FST2|FST3|FST4|FST5|FST6|FW1394BS400BT1|FW1394BS400BT2|FW1394BS800BT1|FW1394BS800BT2|FW1394BS1600BT1|FW1394BS1600BT2|FW1394BS400B|FW1394BS800B|FW1394BS1600B|G703DS1|G703DS3|HST<x>|INF2_5G|INF2_5GE|NONe|OC1|OC3|OC12|OC48|OC48_FEC|RATE32Mbit|RATE97Mbit|RIO_DRV500M|RIO_DRV750M|RIO_DRV1G|RIO_DRV1_5G|RIO_DRV2G|RIO_EDRV500M|RIO_EDRV750M|RIO_EDRV1G|RIO_EDRV1_5G|RIO_EDRV2G|RIO_RCV500M|RIO_RCV750M|RIO_RCV1G|RIO_RCV1_5G|RIO_RCV2G|RIO_SERIAL_1G|RIO_SERIAL_2G|RIO_SERIAL_3G|SFI5_XMITADATA2|SFI5_XMITCDATA2|SFI5_XMITACLK2|SFI5_XMITCCLK2|SFI5_RCVBDATA2|SFI5_RCVDDATA2|SFI5_RCVBCLK2|SFI5_RCVDCLK2|SFI5_XMITADATA3|SFI5_XMITCDATA3|SFI5_XMITACLK3|SFI5_XMITCCLK3|SFI5_RCVBDATA3|SFI5_RCVDDATA3|SFI5_RCVBCLK3|SFI5_RCVDCLK3|PCIEXPRESS_Xmit|PCIEXPRESS_Rcv|SAS1_5_IR|SAS1_5_CR|SAS1_5_XR|SAS1_5_IR_AASJ|SAS1_5_CR_AASJ|SAS1_5_XR_AASJ|SAS1_5_SATA|SAS3_0_IR|SAS3_0_CR|SAS3_0_XR|SAS3_0_IR_AASJ|SAS3_0_CR_AASJ|SAS3_0_XR_AASJ|SAS3_0_SATA|STM0_1|STM0_0|STM0_HDBX|STM1E_0|STM1E_1|STS1Pulse|STS1Eye|STS3|STS3_Max|TFI5_2|TFI5_3|USERMask|VIDEO270|VIDEO292M|VIDEO360|VSROC192}
        - MASK:AUTOSet:STANdard?
        ```

    Info:
        - ``ATATXG1`` (Serial ATA, G1 Tx, 1.5 Gb/s).
        - ``ATATXG2`` (Serial ATA, G2 Tx, 3.0 Gb/s).
        - ``ATATXG3`` (Serial ATA, G3 Tx).
        - ``ATARXG1`` (Serial ATA, G1 Rx 1.5 Gb/s).
        - ``ATARXG2`` (Serial ATA, G2, Rx, 3.0 Gb/s).
        - ``ATARXG3`` (Serial ATA, G3, Rx).
        - ``G703D1`` (ITU-T, G703 (10/98), DS1 Rate, 1.544 Mb/s).
        - ``DS1`` (ANSI T1.102-1993 (R1999), DS1, 1.544 Mb/s).
        - ``DS1A`` (ANSI T1.102-1993 (R1999), DS1A, 2.048 Mb/s).
        - ``DS1C`` (ANSI T1.102-1993 (R1999), DS1C, 3.152 Mb/s).
        - ``DS2`` (ANSI T1.102-1993 (R1999), DS2, 6.312 Mb/s).
        - ``DS3`` (ANSI T1.102-1993 (R1999), DS3, 44.736 Mb/s).
        - ``DS4NA`` (ANSI T1.102-1993 (R1999), DS4NA, 139.26 Mb/s).
        - ``DS4NA_Max`` (ANSI T1.102-1993 (R1999), DSNA Max Output, 139.26 Mb/s).
        - ``DS2RATECoax`` (ITU-T, G703 (10/98), D2 Rate Coax, 6.312 Mb/s).
        - ``DS2RATESymmetrical`` (ITU-T, G703 (10/98), D2 Rate Sym, 6.312 Mb/s).
        - ``E1Coax`` (ITU-T, G703 (10/98), E1 Coax Pair, 2.048 Mb/s).
        - ``E1Symmetrical`` (ITU-T, G703 (10/98), E1 Sym Pair, 2.048 Mb/s).
        - ``E2`` (ITU-T, G703 (10/98), 8.448 Mb/s).
        - ``RATE32Mbit`` (ITU-T, G703 (10/98), 32.064 Mb/s).
        - ``E3`` (ITU-T, G703 (10/98), E3, 34.368 Mb/s).
        - ``E4_0`` (ITU-T, G703 (10/98), E4 Binary 0).
        - ``E4_1`` (ITU-T, G703 (10/98), E4 Binary 1).
        - ``ENET100STP`` (IEEE Std 802.3 and ANSI X3.263-1995, 100 Base-Tx, STP, 125 Mb/s ).
        - ``ENET100UTP`` (IEEE Std 802.3 and ANSI X3.263-1995, 100 Base-Tx, UTP, 125 Mb/s).
        - ``ENET1250`` (IEEE Std 802.3 and ANSI X3.263-1995, GB Ethernet, 1.25 Gb/s).
        - ``FC133`` (ANSI X3.230-1999 NCITS 1235D/Rev 11, Optical, 132.8 Mb/s).
        - ``FC266`` (ANSI X3.230-1999 NCITS 1235D/Rev 11, Optical, 265.6 Mb/s).
        - ``FC531`` (ANSI X3.230-1999 NCITS 1235D/Rev 11, Optical, 531.2 Mb/s).
        - ``FC1063`` (ANSI X3.230-1999 NCITS 1235D/Rev 11, Optical, 1.065 Gb/s).
        - ``FC1063Draft`` (ANSI X3.230-1999 NCITS 1235D/Rev 11, Optical, Draft Rev 11).
        - ``FC2125`` (ANSI X3.230-1999 NCITS 1235D/Rev 11, Optical, 2.125).
        - ``FC133E`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Electrical 132.8 Mb/s).
        - ``FC266E`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Electrical, 132.8 Mb/s).
        - ``FC531E`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Electrical, 531.2 Mb/s).
        - ``FC1063E`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Electrical, 1.0625 Gb/s).
        - ``FC1063E_NBT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Norm, Beta, Transm).
        - ``FC1063E_NDT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Norm, Delta, Transm).
        - ``FC1063E_NGT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Norm, Gamma, Transm).
        - ``FC1063E_ABT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Beta, Transm).
        - ``FC1063E_ADT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Beta, Transm).
        - ``FC1063E_AGT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Gamma, Transm).
        - ``FC1063E_ABR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Beta, Recv).
        - ``FC1063E_ADR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Delta, Recv).
        - ``FC1063E_AGR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Gamma, Recv).
        - ``FC2125E_NBT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Norm, Beta, Transm).
        - ``FC2125E_NDT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Norm, Delta, Transm).
        - ``FC2125E_NGT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Norm, Gamma, Transm).
        - ``FC2125E_ABT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Beta, Transm).
        - ``FC2125E_ADT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Delta, Transm).
        - ``FC2125E_AGT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Gamma, Transm).
        - ``FC2125E_ABR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Beta, Recv).
        - ``FC2125E_ADR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Delta, Recv).
        - ``FC2125E_AGR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Gamma, Recv).
        - ``ENET1000BCX_NTP2`` (1000B-CX Norm, TP2, 1.25 Gb/s).
        - ``ENET1000BCX_ATP2`` (1000B-CX Abs, TP2, 1.25 Gb/s).
        - ``ENET1000BCX_ATP3`` (1000B-CX Abs, TP3, 1.25 Gb/s).
        - ``ENETXAUI_Near`` (10 Gigabit Attachment Unit Interface (XAUI), Near, 3,125 Gb/s).
        - ``ENETXAUI_Far`` (10 Gigabit Attachment Unit Interface (XAUI), Far, 3.125 Gb/s).
        - ``FST1`` (USB, ``FS:T1``, 12 Mb/s).
        - ``FST2`` (USB, ``FS:T2``, 12 Mb/s).
        - ``FST3`` (USB, ``FS:T3``, 12 Mb/s).
        - ``FST4`` (USB, ``FS:T4``: 12 Mb/s).
        - ``FST5`` (USB, ``FS:T5``, 12 Mb/s).
        - ``FST6`` (USB, ``FS:T6``, 12 Mb/s).
        - ``FW1394BS400BT1`` (IEEE 1394b, S400b T1, 491.5 Mb/s).
        - ``FW1394BS400BT2`` (IEEE 1394b, S400b T2, 491.5 Mb/s).
        - ``FW1394BS800BT1`` (IEEE 1394b, S800b T1, 983.0 Mb/s).
        - ``FW1394BS800BT2`` (IEEE 1394b, S800b T2, 983.0 Mb/s).
        - ``FW1394BS1600BT1`` (IEEE 1394b, S1600b T1, 1.966 Gb/s).
        - ``FW1394BS1600BT2`` (IEEE 1394b, S1600b T2, 1.966 Gb/s).
        - ``FW1394BS400B`` (IEEE 1394b, S400 Optical, 491.5 Mb/s).
        - ``FW1394BS800B`` (IEEE 1394b, S800 Optical, 988.0 Mb/s).
        - ``FW1394BS1600B`` (IEEE 1394b, S1600 Optical, 1.966 Gb/s).
        - ``G703DS3`` (ITU-T, G703 (10/98)).
        - ``HST1`` (USB, ``HS:T1``, 480 Mb/s).
        - ``HST2`` (USB, ``HS:T2``, 480 Mb/s).
        - ``HST3`` (USB, ``HS:T3``, 480 Mb/s).
        - ``HST4`` (USB, ``HS:T4``, 480 Mb/s).
        - ``HST5`` (USB, ``HS:T5``, 480 Mb/s).
        - ``HST6`` (USB, ``HS:T6``, 480 Mb/s).
        - ``INF2_5G`` (InfiniBand, IBTA Spec 1.0a, 2.5 Optical, 2.5 Gb/s).
        - ``INF2_5GE`` (InfiniBand, IBTA Spec 1.0a, 2.5 Electrical, 2.5 Gb/s).
        - ``OC1`` (GR 253-CORE Issue 3 9/21/2000 OC1/STM0, 51.84 Mb/s).
        - ``OC3`` (GR 253-CORE Issue 3 9/21/2000 OC1/STM1, 155.52, Mb/s).
        - ``OC12`` (GR 253-CORE Issue 3 9/21/2000 OC1/STM4, 622.08 Mb/s).
        - ``OC48`` (GR 253-CORE Issue 3 9/21/2000 OC1/STM16, 2.4883 Gb/s.
        - ``OC48_FEC`` (Forward Error Correction - CSA8000 mask, 2.666 Gb/s).
        - ``PCIEXPRESS_Xmit`` (PCI Express Transmitter, 2.5 Gb/s).
        - ``PCIEXPRESS_Rcv`` (PCI Express Receiver, 2.5 Gb/s).
        - ``RATE97Mbit`` (ITU-T, G703 (10/98), 97 Mbit, 97.728 Mb/s).
        - ``RIO_DRV500M`` (Rapid IO Driver, 500 Mb/s).
        - ``RIO_DRV750M`` (Rapid IO Driver, 750 Mb/s).
        - ``RIO_DRV1G`` (Rapid IO Driver, 1 Gb/s).
        - ``RIO_DRV1_5G`` (Rapid IO Driver, 5 Gb/s).
        - ``RIO_DRV2G`` (Rapid IO Driver, 2 Gb/s).
        - ``RIO_EDRV500M`` (Rapid IO Extended Driver, 500 Mb/s).
        - ``RIO_EDRV750M`` (Rapid IO Extended Driver, 750 Mb/s).
        - ``RIO_EDRV1G`` (Rapid IO Extended Driver, 1 Gb/s).
        - ``RIO_EDRV1_5G`` (Rapid IO Extended Driver, 1.5 Gb/s).
        - ``RIO_EDRV2G`` (Rapid IO Extended Driver, 2 Gb/s).
        - ``RIO_RCV500M`` (Rapid IO Receiver, 500 Mb/s).
        - ``RIO_RCV750M`` (Rapid IO Receiver, 750 Mb/s).
        - ``RIO_RCV1G`` (Rapid IO Receiver, 1 Gb/s).
        - ``RIO_RCV1_5G`` (Rapid IO Receiver, 1.5 Gb/s).
        - ``RIO_RCV2G`` (Rapid IO Receiver, 2 Gb/s).
        - ``RIO_SERIAL_1G`` (Rapid IO Serial, 1.25 Gb/s).
        - ``RIO_SERIAL_2G`` (Rapid IO Serial, 2.5 Gb/s).
        - ``RIO_SERIAL_3G`` (Rapid IO Serial, 3.25 Gb/s).
        - ``SFI5_XMITADATA2`` (SFI15 Transmit: Test Point A Data Signal 2, 2.488 Gb/s).
        - ``SFI5_XMITCDATA2`` (SFI15 Transmit: Test Point C Data Signal 2, 2.488 Gb/s).
        - ``SFI5_XMITACLK2`` (SFI15 Transmit: Test Point A Clock Signal 2, 2.488 Gb/s).
        - ``SFI5_XMITCCLK2`` (SFI15 Transmit: Test Point C Clock Signal 2, 2.488 Gb/s).
        - ``SFI5_RCVBDATA2`` (SFI15 Receive: Test Point B Data Signal 2, 2.488 Gb/s).
        - ``SFI5_RCVDDATA2`` (SFI15 Receive: Test Point D Data Signal 2, 2.488 Gb/s).
        - ``SFI5_RCVBCLK2`` (SFI15 Receive: Test Point B Clock Signal 2, 2.488 Gb/s).
        - ``SFI5_RCVDCLK2`` (SFI15 Receive: Test Point D Clock Signal 2, 2.488 Gb/s).
        - ``SFI5_XMITADATA3`` (SFI15 Transmit: Test Point A Data Signal 3, 3.125 Gb/s).
        - ``SFI5_XMITCDATA3`` (SFI15 Transmit: Test Point C Data Signal 3, 3.125 Gb/s).
        - ``SFI5_XMITACLK3`` (SFI15 Transmit: Test Point A Clock Signal 3, 3.125 Gb/s).
        - ``SFI5_XMITCCLK3`` (SFI15 Transmit: Test Point C Clock Signal 3, 3.125 Gb/s).
        - ``SFI5_RCVBDATA3`` (SFI15 Receive: Test Point B Data Signal 3, 3.125 Gb/s).
        - ``SFI5_RCVDDATA3`` (SFI15 Receive: Test Point D Data Signal 3, 3.125 Gb/s).
        - ``SFI5_RCVBCLK3`` (SFI15 Receive: Test Point B Clock Signal 3, 3.125 Gb/s).
        - ``SFI5_RCVDCLK3`` (SFI15 Receive: Test Point D Clock Signal 3, 3.125 Gb/s.
        - ``STM1E_0`` (ITU-T, G703 (10/98), STM1E Binary 0).
        - ``STM1E_1`` (ITU-T, G703 (10/98), STM1E Binary 1).
        - ``STS1Pulse`` (ANSI T1.102-1993 (R1999), STS-1 Pulse, 51.84 Mb/s).
        - ``STS1Eye`` (ANSI T1.102-1993 (R1999), STS-1 Eye, 51.84 Mb/s).
        - ``STS3`` (ANSI T1.102-1993 (R1999), STS-3, 155.52 Mb/s).
        - ``STS3_Max`` (ANSI T1.102-1993 (R1999), STS-3 Max Output, 155.52 Mb/s).
        - ``TFI15_2`` (TFI-5, 2.488 Gb/s).
        - ``TFI5_3`` (TFI-5, 3.1104 Gb/s).
        - ``USERMask``
        - ``VIDEO292M`` (SMPTE, 1.485 Gb/s).
        - ``VSROC192`` (VSR OC192/STM64, 1.24416 Gb/s).
    """  # noqa: E501


class MaskAutosetOffsetadj(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:AUTOSet:OFFSETAdj`` command.

    Description:
        - This command sets mask autoset not to enforce the rule that, for pulse standards, require
          0 V to be in a certain place in the mask. Instead, mask autoset will attempt to measure
          the DC offse t in the signal and use oscilloscope offset or position controls to
          compensate for the DC offset in the signal. This command, like all the ``MASK:AUTOSET``
          commands, affects only an autoset on a standard mask, not the general instrument autoset
          function.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:AUTOSet:OFFSETAdj?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet:OFFSETAdj?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:AUTOSet:OFFSETAdj value`` command.

    SCPI Syntax:
        ```
        - MASK:AUTOSet:OFFSETAdj {ON|OFF|<NR1>}
        - MASK:AUTOSet:OFFSETAdj?
        ```

    Info:
        - ``<NR1>`` = 0 disables the ``autoset:offsetadj`` function; any other value enables it.
        - ``ON`` enables the ``autoset:offsetadj`` function.
        - ``OFF`` disables the ``autoset:offsetadj`` function.
    """


class MaskAutosetMode(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:AUTOSet:MODe`` command.

    Description:
        - This command controls whether a mask autoset will be automatically done after a standard
          mask is selected. The autoset will never happen if the standard mask is selected from
          GPIB, since a 'SET?' sent back to the oscilloscope should not perform a mask autoset. The
          default value is: manual. This command, like all the ``MASK:AUTOSET`` commands, affects
          only an autoset on a standard mask, not the general instrument autoset function.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:AUTOSet:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet:MODe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:AUTOSet:MODe value`` command.

    SCPI Syntax:
        ```
        - MASK:AUTOSet:MODe {MANual|AUTO}
        - MASK:AUTOSet:MODe?
        ```

    Info:
        - ``MANual`` mask autoset is set manually.
        - ``AUTO`` mask autoset is set automatically.
    """


class MaskAutosetHscale(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:AUTOSet:HSCAle`` command.

    Description:
        - This command controls whether the autoset algorithm will attempt to change the horizontal
          scale while attempting a mask autoset. This command, like all the ``MASK:AUTOSET``
          commands, affects only an autoset on a standard mask, not the general instrument autoset
          function.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:AUTOSet:HSCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet:HSCAle?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:AUTOSet:HSCAle value`` command.

    SCPI Syntax:
        ```
        - MASK:AUTOSet:HSCAle {ON|OFF|<NR1>}
        - MASK:AUTOSet:HSCAle?
        ```

    Info:
        - ``<NR1>`` = 0 disables the ``autoset:hscale`` function; any other value enables it.
        - ``ON`` enables the ``autoset:hscale`` function.
        - ``OFF`` disables the ``autoset:hscale`` function.
    """


class MaskAutosetHpos(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:AUTOSet:HPOS`` command.

    Description:
        - This command controls whether the autoset algorithm will attempt to change the horizontal
          position of the signal while attempting to do a mask autoset. The default is ON. This
          command, like all the ``MASK:AUTOSET`` commands, affects only an autoset on a standard
          mask, not the general instrument autoset function.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:AUTOSet:HPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet:HPOS?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:AUTOSet:HPOS value`` command.

    SCPI Syntax:
        ```
        - MASK:AUTOSet:HPOS {ON|OFF|<NR1>}
        - MASK:AUTOSet:HPOS?
        ```

    Info:
        - ``<NR1>`` = 0 disables the ``autoset:hpos`` function; any other value disables enables it.
        - ``ON`` enables the ``autoset:hpos`` function.
        - ``OFF`` disables the ``autoset:hpos`` function.
    """


class MaskAutosetAutoadjust(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:AUTOSet:AUTOAdjust`` command.

    Description:
        - This command sets or returns whether the instrument settings are automatically matched to
          signal characteristics and specific mask requirements. It controls what happens at the end
          of a mask autoset. If ON, the horz/vert auto adjustment is run ONCE to potentially improve
          the result of mask autoset. This command, like all the ``MASK:AUTOSET`` commands, affects
          only an autoset on a standard mask, not the general instrument autoset function.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:AUTOSet:AUTOAdjust?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet:AUTOAdjust?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:AUTOSet:AUTOAdjust value``
          command.

    SCPI Syntax:
        ```
        - MASK:AUTOSet:AUTOAdjust {ON|OFF|<NR1>}
        - MASK:AUTOSet:AUTOAdjust?
        ```

    Info:
        - ``<NR1>`` = 0 disables the ``autoset:autoadjust`` function; any other value enables it.
        - ``ON`` enables the ``autoset:autoadjust`` function.
        - ``OFF`` disables the ``autoset:autoadjust`` function.
    """


#  pylint: disable=too-many-instance-attributes
class MaskAutoset(SCPICmdRead):
    """The ``MASK:AUTOSet`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:AUTOSet?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.autoadjust``: The ``MASK:AUTOSet:AUTOAdjust`` command.
        - ``.hpos``: The ``MASK:AUTOSet:HPOS`` command.
        - ``.hscale``: The ``MASK:AUTOSet:HSCAle`` command.
        - ``.mode``: The ``MASK:AUTOSet:MODe`` command.
        - ``.offsetadj``: The ``MASK:AUTOSet:OFFSETAdj`` command.
        - ``.standard``: The ``MASK:AUTOSet:STANdard`` command.
        - ``.trigger``: The ``MASK:AUTOSet:TRIGger`` command.
        - ``.user``: The ``MASK:AUTOSet:USER`` command tree.
        - ``.vpos``: The ``MASK:AUTOSet:VPOS`` command.
        - ``.vscale``: The ``MASK:AUTOSet:VSCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autoadjust = MaskAutosetAutoadjust(device, f"{self._cmd_syntax}:AUTOAdjust")
        self._hpos = MaskAutosetHpos(device, f"{self._cmd_syntax}:HPOS")
        self._hscale = MaskAutosetHscale(device, f"{self._cmd_syntax}:HSCAle")
        self._mode = MaskAutosetMode(device, f"{self._cmd_syntax}:MODe")
        self._offsetadj = MaskAutosetOffsetadj(device, f"{self._cmd_syntax}:OFFSETAdj")
        self._standard = MaskAutosetStandard(device, f"{self._cmd_syntax}:STANdard")
        self._trigger = MaskAutosetTrigger(device, f"{self._cmd_syntax}:TRIGger")
        self._user = MaskAutosetUser(device, f"{self._cmd_syntax}:USER")
        self._vpos = MaskAutosetVpos(device, f"{self._cmd_syntax}:VPOS")
        self._vscale = MaskAutosetVscale(device, f"{self._cmd_syntax}:VSCAle")

    @property
    def autoadjust(self) -> MaskAutosetAutoadjust:
        """Return the ``MASK:AUTOSet:AUTOAdjust`` command.

        Description:
            - This command sets or returns whether the instrument settings are automatically matched
              to signal characteristics and specific mask requirements. It controls what happens at
              the end of a mask autoset. If ON, the horz/vert auto adjustment is run ONCE to
              potentially improve the result of mask autoset. This command, like all the
              ``MASK:AUTOSET`` commands, affects only an autoset on a standard mask, not the general
              instrument autoset function.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:AUTOSet:AUTOAdjust?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet:AUTOAdjust?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:AUTOSet:AUTOAdjust value``
              command.

        SCPI Syntax:
            ```
            - MASK:AUTOSet:AUTOAdjust {ON|OFF|<NR1>}
            - MASK:AUTOSet:AUTOAdjust?
            ```

        Info:
            - ``<NR1>`` = 0 disables the ``autoset:autoadjust`` function; any other value enables
              it.
            - ``ON`` enables the ``autoset:autoadjust`` function.
            - ``OFF`` disables the ``autoset:autoadjust`` function.
        """
        return self._autoadjust

    @property
    def hpos(self) -> MaskAutosetHpos:
        """Return the ``MASK:AUTOSet:HPOS`` command.

        Description:
            - This command controls whether the autoset algorithm will attempt to change the
              horizontal position of the signal while attempting to do a mask autoset. The default
              is ON. This command, like all the ``MASK:AUTOSET`` commands, affects only an autoset
              on a standard mask, not the general instrument autoset function.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:AUTOSet:HPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet:HPOS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:AUTOSet:HPOS value`` command.

        SCPI Syntax:
            ```
            - MASK:AUTOSet:HPOS {ON|OFF|<NR1>}
            - MASK:AUTOSet:HPOS?
            ```

        Info:
            - ``<NR1>`` = 0 disables the ``autoset:hpos`` function; any other value disables enables
              it.
            - ``ON`` enables the ``autoset:hpos`` function.
            - ``OFF`` disables the ``autoset:hpos`` function.
        """
        return self._hpos

    @property
    def hscale(self) -> MaskAutosetHscale:
        """Return the ``MASK:AUTOSet:HSCAle`` command.

        Description:
            - This command controls whether the autoset algorithm will attempt to change the
              horizontal scale while attempting a mask autoset. This command, like all the
              ``MASK:AUTOSET`` commands, affects only an autoset on a standard mask, not the general
              instrument autoset function.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:AUTOSet:HSCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet:HSCAle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:AUTOSet:HSCAle value``
              command.

        SCPI Syntax:
            ```
            - MASK:AUTOSet:HSCAle {ON|OFF|<NR1>}
            - MASK:AUTOSet:HSCAle?
            ```

        Info:
            - ``<NR1>`` = 0 disables the ``autoset:hscale`` function; any other value enables it.
            - ``ON`` enables the ``autoset:hscale`` function.
            - ``OFF`` disables the ``autoset:hscale`` function.
        """
        return self._hscale

    @property
    def mode(self) -> MaskAutosetMode:
        """Return the ``MASK:AUTOSet:MODe`` command.

        Description:
            - This command controls whether a mask autoset will be automatically done after a
              standard mask is selected. The autoset will never happen if the standard mask is
              selected from GPIB, since a 'SET?' sent back to the oscilloscope should not perform a
              mask autoset. The default value is: manual. This command, like all the
              ``MASK:AUTOSET`` commands, affects only an autoset on a standard mask, not the general
              instrument autoset function.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:AUTOSet:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet:MODe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:AUTOSet:MODe value`` command.

        SCPI Syntax:
            ```
            - MASK:AUTOSet:MODe {MANual|AUTO}
            - MASK:AUTOSet:MODe?
            ```

        Info:
            - ``MANual`` mask autoset is set manually.
            - ``AUTO`` mask autoset is set automatically.
        """
        return self._mode

    @property
    def offsetadj(self) -> MaskAutosetOffsetadj:
        """Return the ``MASK:AUTOSet:OFFSETAdj`` command.

        Description:
            - This command sets mask autoset not to enforce the rule that, for pulse standards,
              require 0 V to be in a certain place in the mask. Instead, mask autoset will attempt
              to measure the DC offse t in the signal and use oscilloscope offset or position
              controls to compensate for the DC offset in the signal. This command, like all the
              ``MASK:AUTOSET`` commands, affects only an autoset on a standard mask, not the general
              instrument autoset function.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:AUTOSet:OFFSETAdj?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet:OFFSETAdj?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:AUTOSet:OFFSETAdj value``
              command.

        SCPI Syntax:
            ```
            - MASK:AUTOSet:OFFSETAdj {ON|OFF|<NR1>}
            - MASK:AUTOSet:OFFSETAdj?
            ```

        Info:
            - ``<NR1>`` = 0 disables the ``autoset:offsetadj`` function; any other value enables it.
            - ``ON`` enables the ``autoset:offsetadj`` function.
            - ``OFF`` disables the ``autoset:offsetadj`` function.
        """
        return self._offsetadj

    @property
    def standard(self) -> MaskAutosetStandard:
        """Return the ``MASK:AUTOSet:STANdard`` command.

        Description:
            - This command selects the standard mask in a mask autoset. This command, like all the
              ``MASK:AUTOSET`` commands, affects only an autoset on a standard mask, not the general
              instrument autoset function.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:AUTOSet:STANdard?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet:STANdard?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:AUTOSet:STANdard value``
              command.

        SCPI Syntax:
            ```
            - MASK:AUTOSet:STANdard {ATATXG<x>|ATARXG<x>|CLOCKCoax|CLOCKSymmetrical|D<x>|DS0Contra|DS0Double|DS0Single|DS0Timing|DS1|DS1A|DS1C|DS2RATESymmetrical|DS2RATECoax|DS2|DS3|DS4NA|DS4NA_Max|E1Symmetrical|E1Coax|E2|E3|E4_0|E4_1|ENET100FX|ENET100STP|ENET100UTP|ENET1250|ENET1000BCX_NTP2|ENET1000BCX_ATP2|ENET1000BCX_ATP3|ENETXAUI_Near|ENETXAUI_Far|FC133|FC266|FC531|FC1063|FC1063Draft|FC2125|FC133E|FC266E|FC531E|FC1063E|FC1063E_NBT|FC1063E_NDT|FC1063E_NGT|FC1063E_ABT|FC1063E_ADT|FC1063E_AGT|FC1063E_ABR|FC1063E_ADR|FC1063E_AGR|FC2125E_NBT|FC2125E_NDT|FC2125E_NGT|FC2125E_ABT|FC2125E_ADT|FC2125E_AGT|FC2125E_ABR|FC2125E_ADR|FC2125E_AGR|FC4250E_ABR|FC4250E_ABT|FC4250E_ADR|FC4250E_ADT|FC4250E_AGR|FC4250E_AGT|FC4250E_NBT|FC4250E_NDT|FC4250E_NGT|FST1|FST2|FST3|FST4|FST5|FST6|FW1394BS400BT1|FW1394BS400BT2|FW1394BS800BT1|FW1394BS800BT2|FW1394BS1600BT1|FW1394BS1600BT2|FW1394BS400B|FW1394BS800B|FW1394BS1600B|G703DS1|G703DS3|HST<x>|INF2_5G|INF2_5GE|NONe|OC1|OC3|OC12|OC48|OC48_FEC|RATE32Mbit|RATE97Mbit|RIO_DRV500M|RIO_DRV750M|RIO_DRV1G|RIO_DRV1_5G|RIO_DRV2G|RIO_EDRV500M|RIO_EDRV750M|RIO_EDRV1G|RIO_EDRV1_5G|RIO_EDRV2G|RIO_RCV500M|RIO_RCV750M|RIO_RCV1G|RIO_RCV1_5G|RIO_RCV2G|RIO_SERIAL_1G|RIO_SERIAL_2G|RIO_SERIAL_3G|SFI5_XMITADATA2|SFI5_XMITCDATA2|SFI5_XMITACLK2|SFI5_XMITCCLK2|SFI5_RCVBDATA2|SFI5_RCVDDATA2|SFI5_RCVBCLK2|SFI5_RCVDCLK2|SFI5_XMITADATA3|SFI5_XMITCDATA3|SFI5_XMITACLK3|SFI5_XMITCCLK3|SFI5_RCVBDATA3|SFI5_RCVDDATA3|SFI5_RCVBCLK3|SFI5_RCVDCLK3|PCIEXPRESS_Xmit|PCIEXPRESS_Rcv|SAS1_5_IR|SAS1_5_CR|SAS1_5_XR|SAS1_5_IR_AASJ|SAS1_5_CR_AASJ|SAS1_5_XR_AASJ|SAS1_5_SATA|SAS3_0_IR|SAS3_0_CR|SAS3_0_XR|SAS3_0_IR_AASJ|SAS3_0_CR_AASJ|SAS3_0_XR_AASJ|SAS3_0_SATA|STM0_1|STM0_0|STM0_HDBX|STM1E_0|STM1E_1|STS1Pulse|STS1Eye|STS3|STS3_Max|TFI5_2|TFI5_3|USERMask|VIDEO270|VIDEO292M|VIDEO360|VSROC192}
            - MASK:AUTOSet:STANdard?
            ```

        Info:
            - ``ATATXG1`` (Serial ATA, G1 Tx, 1.5 Gb/s).
            - ``ATATXG2`` (Serial ATA, G2 Tx, 3.0 Gb/s).
            - ``ATATXG3`` (Serial ATA, G3 Tx).
            - ``ATARXG1`` (Serial ATA, G1 Rx 1.5 Gb/s).
            - ``ATARXG2`` (Serial ATA, G2, Rx, 3.0 Gb/s).
            - ``ATARXG3`` (Serial ATA, G3, Rx).
            - ``G703D1`` (ITU-T, G703 (10/98), DS1 Rate, 1.544 Mb/s).
            - ``DS1`` (ANSI T1.102-1993 (R1999), DS1, 1.544 Mb/s).
            - ``DS1A`` (ANSI T1.102-1993 (R1999), DS1A, 2.048 Mb/s).
            - ``DS1C`` (ANSI T1.102-1993 (R1999), DS1C, 3.152 Mb/s).
            - ``DS2`` (ANSI T1.102-1993 (R1999), DS2, 6.312 Mb/s).
            - ``DS3`` (ANSI T1.102-1993 (R1999), DS3, 44.736 Mb/s).
            - ``DS4NA`` (ANSI T1.102-1993 (R1999), DS4NA, 139.26 Mb/s).
            - ``DS4NA_Max`` (ANSI T1.102-1993 (R1999), DSNA Max Output, 139.26 Mb/s).
            - ``DS2RATECoax`` (ITU-T, G703 (10/98), D2 Rate Coax, 6.312 Mb/s).
            - ``DS2RATESymmetrical`` (ITU-T, G703 (10/98), D2 Rate Sym, 6.312 Mb/s).
            - ``E1Coax`` (ITU-T, G703 (10/98), E1 Coax Pair, 2.048 Mb/s).
            - ``E1Symmetrical`` (ITU-T, G703 (10/98), E1 Sym Pair, 2.048 Mb/s).
            - ``E2`` (ITU-T, G703 (10/98), 8.448 Mb/s).
            - ``RATE32Mbit`` (ITU-T, G703 (10/98), 32.064 Mb/s).
            - ``E3`` (ITU-T, G703 (10/98), E3, 34.368 Mb/s).
            - ``E4_0`` (ITU-T, G703 (10/98), E4 Binary 0).
            - ``E4_1`` (ITU-T, G703 (10/98), E4 Binary 1).
            - ``ENET100STP`` (IEEE Std 802.3 and ANSI X3.263-1995, 100 Base-Tx, STP, 125 Mb/s ).
            - ``ENET100UTP`` (IEEE Std 802.3 and ANSI X3.263-1995, 100 Base-Tx, UTP, 125 Mb/s).
            - ``ENET1250`` (IEEE Std 802.3 and ANSI X3.263-1995, GB Ethernet, 1.25 Gb/s).
            - ``FC133`` (ANSI X3.230-1999 NCITS 1235D/Rev 11, Optical, 132.8 Mb/s).
            - ``FC266`` (ANSI X3.230-1999 NCITS 1235D/Rev 11, Optical, 265.6 Mb/s).
            - ``FC531`` (ANSI X3.230-1999 NCITS 1235D/Rev 11, Optical, 531.2 Mb/s).
            - ``FC1063`` (ANSI X3.230-1999 NCITS 1235D/Rev 11, Optical, 1.065 Gb/s).
            - ``FC1063Draft`` (ANSI X3.230-1999 NCITS 1235D/Rev 11, Optical, Draft Rev 11).
            - ``FC2125`` (ANSI X3.230-1999 NCITS 1235D/Rev 11, Optical, 2.125).
            - ``FC133E`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Electrical 132.8 Mb/s).
            - ``FC266E`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Electrical, 132.8 Mb/s).
            - ``FC531E`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Electrical, 531.2 Mb/s).
            - ``FC1063E`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Electrical, 1.0625 Gb/s).
            - ``FC1063E_NBT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Norm, Beta, Transm).
            - ``FC1063E_NDT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Norm, Delta, Transm).
            - ``FC1063E_NGT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Norm, Gamma, Transm).
            - ``FC1063E_ABT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Beta, Transm).
            - ``FC1063E_ADT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Beta, Transm).
            - ``FC1063E_AGT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Gamma, Transm).
            - ``FC1063E_ABR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Beta, Recv).
            - ``FC1063E_ADR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Delta, Recv).
            - ``FC1063E_AGR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Gamma, Recv).
            - ``FC2125E_NBT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Norm, Beta, Transm).
            - ``FC2125E_NDT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Norm, Delta, Transm).
            - ``FC2125E_NGT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Norm, Gamma, Transm).
            - ``FC2125E_ABT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Beta, Transm).
            - ``FC2125E_ADT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Delta, Transm).
            - ``FC2125E_AGT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Gamma, Transm).
            - ``FC2125E_ABR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Beta, Recv).
            - ``FC2125E_ADR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Delta, Recv).
            - ``FC2125E_AGR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Gamma, Recv).
            - ``ENET1000BCX_NTP2`` (1000B-CX Norm, TP2, 1.25 Gb/s).
            - ``ENET1000BCX_ATP2`` (1000B-CX Abs, TP2, 1.25 Gb/s).
            - ``ENET1000BCX_ATP3`` (1000B-CX Abs, TP3, 1.25 Gb/s).
            - ``ENETXAUI_Near`` (10 Gigabit Attachment Unit Interface (XAUI), Near, 3,125 Gb/s).
            - ``ENETXAUI_Far`` (10 Gigabit Attachment Unit Interface (XAUI), Far, 3.125 Gb/s).
            - ``FST1`` (USB, ``FS:T1``, 12 Mb/s).
            - ``FST2`` (USB, ``FS:T2``, 12 Mb/s).
            - ``FST3`` (USB, ``FS:T3``, 12 Mb/s).
            - ``FST4`` (USB, ``FS:T4``: 12 Mb/s).
            - ``FST5`` (USB, ``FS:T5``, 12 Mb/s).
            - ``FST6`` (USB, ``FS:T6``, 12 Mb/s).
            - ``FW1394BS400BT1`` (IEEE 1394b, S400b T1, 491.5 Mb/s).
            - ``FW1394BS400BT2`` (IEEE 1394b, S400b T2, 491.5 Mb/s).
            - ``FW1394BS800BT1`` (IEEE 1394b, S800b T1, 983.0 Mb/s).
            - ``FW1394BS800BT2`` (IEEE 1394b, S800b T2, 983.0 Mb/s).
            - ``FW1394BS1600BT1`` (IEEE 1394b, S1600b T1, 1.966 Gb/s).
            - ``FW1394BS1600BT2`` (IEEE 1394b, S1600b T2, 1.966 Gb/s).
            - ``FW1394BS400B`` (IEEE 1394b, S400 Optical, 491.5 Mb/s).
            - ``FW1394BS800B`` (IEEE 1394b, S800 Optical, 988.0 Mb/s).
            - ``FW1394BS1600B`` (IEEE 1394b, S1600 Optical, 1.966 Gb/s).
            - ``G703DS3`` (ITU-T, G703 (10/98)).
            - ``HST1`` (USB, ``HS:T1``, 480 Mb/s).
            - ``HST2`` (USB, ``HS:T2``, 480 Mb/s).
            - ``HST3`` (USB, ``HS:T3``, 480 Mb/s).
            - ``HST4`` (USB, ``HS:T4``, 480 Mb/s).
            - ``HST5`` (USB, ``HS:T5``, 480 Mb/s).
            - ``HST6`` (USB, ``HS:T6``, 480 Mb/s).
            - ``INF2_5G`` (InfiniBand, IBTA Spec 1.0a, 2.5 Optical, 2.5 Gb/s).
            - ``INF2_5GE`` (InfiniBand, IBTA Spec 1.0a, 2.5 Electrical, 2.5 Gb/s).
            - ``OC1`` (GR 253-CORE Issue 3 9/21/2000 OC1/STM0, 51.84 Mb/s).
            - ``OC3`` (GR 253-CORE Issue 3 9/21/2000 OC1/STM1, 155.52, Mb/s).
            - ``OC12`` (GR 253-CORE Issue 3 9/21/2000 OC1/STM4, 622.08 Mb/s).
            - ``OC48`` (GR 253-CORE Issue 3 9/21/2000 OC1/STM16, 2.4883 Gb/s.
            - ``OC48_FEC`` (Forward Error Correction - CSA8000 mask, 2.666 Gb/s).
            - ``PCIEXPRESS_Xmit`` (PCI Express Transmitter, 2.5 Gb/s).
            - ``PCIEXPRESS_Rcv`` (PCI Express Receiver, 2.5 Gb/s).
            - ``RATE97Mbit`` (ITU-T, G703 (10/98), 97 Mbit, 97.728 Mb/s).
            - ``RIO_DRV500M`` (Rapid IO Driver, 500 Mb/s).
            - ``RIO_DRV750M`` (Rapid IO Driver, 750 Mb/s).
            - ``RIO_DRV1G`` (Rapid IO Driver, 1 Gb/s).
            - ``RIO_DRV1_5G`` (Rapid IO Driver, 5 Gb/s).
            - ``RIO_DRV2G`` (Rapid IO Driver, 2 Gb/s).
            - ``RIO_EDRV500M`` (Rapid IO Extended Driver, 500 Mb/s).
            - ``RIO_EDRV750M`` (Rapid IO Extended Driver, 750 Mb/s).
            - ``RIO_EDRV1G`` (Rapid IO Extended Driver, 1 Gb/s).
            - ``RIO_EDRV1_5G`` (Rapid IO Extended Driver, 1.5 Gb/s).
            - ``RIO_EDRV2G`` (Rapid IO Extended Driver, 2 Gb/s).
            - ``RIO_RCV500M`` (Rapid IO Receiver, 500 Mb/s).
            - ``RIO_RCV750M`` (Rapid IO Receiver, 750 Mb/s).
            - ``RIO_RCV1G`` (Rapid IO Receiver, 1 Gb/s).
            - ``RIO_RCV1_5G`` (Rapid IO Receiver, 1.5 Gb/s).
            - ``RIO_RCV2G`` (Rapid IO Receiver, 2 Gb/s).
            - ``RIO_SERIAL_1G`` (Rapid IO Serial, 1.25 Gb/s).
            - ``RIO_SERIAL_2G`` (Rapid IO Serial, 2.5 Gb/s).
            - ``RIO_SERIAL_3G`` (Rapid IO Serial, 3.25 Gb/s).
            - ``SFI5_XMITADATA2`` (SFI15 Transmit: Test Point A Data Signal 2, 2.488 Gb/s).
            - ``SFI5_XMITCDATA2`` (SFI15 Transmit: Test Point C Data Signal 2, 2.488 Gb/s).
            - ``SFI5_XMITACLK2`` (SFI15 Transmit: Test Point A Clock Signal 2, 2.488 Gb/s).
            - ``SFI5_XMITCCLK2`` (SFI15 Transmit: Test Point C Clock Signal 2, 2.488 Gb/s).
            - ``SFI5_RCVBDATA2`` (SFI15 Receive: Test Point B Data Signal 2, 2.488 Gb/s).
            - ``SFI5_RCVDDATA2`` (SFI15 Receive: Test Point D Data Signal 2, 2.488 Gb/s).
            - ``SFI5_RCVBCLK2`` (SFI15 Receive: Test Point B Clock Signal 2, 2.488 Gb/s).
            - ``SFI5_RCVDCLK2`` (SFI15 Receive: Test Point D Clock Signal 2, 2.488 Gb/s).
            - ``SFI5_XMITADATA3`` (SFI15 Transmit: Test Point A Data Signal 3, 3.125 Gb/s).
            - ``SFI5_XMITCDATA3`` (SFI15 Transmit: Test Point C Data Signal 3, 3.125 Gb/s).
            - ``SFI5_XMITACLK3`` (SFI15 Transmit: Test Point A Clock Signal 3, 3.125 Gb/s).
            - ``SFI5_XMITCCLK3`` (SFI15 Transmit: Test Point C Clock Signal 3, 3.125 Gb/s).
            - ``SFI5_RCVBDATA3`` (SFI15 Receive: Test Point B Data Signal 3, 3.125 Gb/s).
            - ``SFI5_RCVDDATA3`` (SFI15 Receive: Test Point D Data Signal 3, 3.125 Gb/s).
            - ``SFI5_RCVBCLK3`` (SFI15 Receive: Test Point B Clock Signal 3, 3.125 Gb/s).
            - ``SFI5_RCVDCLK3`` (SFI15 Receive: Test Point D Clock Signal 3, 3.125 Gb/s.
            - ``STM1E_0`` (ITU-T, G703 (10/98), STM1E Binary 0).
            - ``STM1E_1`` (ITU-T, G703 (10/98), STM1E Binary 1).
            - ``STS1Pulse`` (ANSI T1.102-1993 (R1999), STS-1 Pulse, 51.84 Mb/s).
            - ``STS1Eye`` (ANSI T1.102-1993 (R1999), STS-1 Eye, 51.84 Mb/s).
            - ``STS3`` (ANSI T1.102-1993 (R1999), STS-3, 155.52 Mb/s).
            - ``STS3_Max`` (ANSI T1.102-1993 (R1999), STS-3 Max Output, 155.52 Mb/s).
            - ``TFI15_2`` (TFI-5, 2.488 Gb/s).
            - ``TFI5_3`` (TFI-5, 3.1104 Gb/s).
            - ``USERMask``
            - ``VIDEO292M`` (SMPTE, 1.485 Gb/s).
            - ``VSROC192`` (VSR OC192/STM64, 1.24416 Gb/s).
        """  # noqa: E501
        return self._standard

    @property
    def trigger(self) -> MaskAutosetTrigger:
        """Return the ``MASK:AUTOSet:TRIGger`` command.

        Description:
            - This command specifies whether a mask AUTOSET affects the trigger level. Other trigger
              settings such as type of trigger are not changed by autoset. The default is ON. This
              command, like all the mask autoset commands, affects only an autoset on a standard
              mask, not the general instrument autoset function.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:AUTOSet:TRIGger?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet:TRIGger?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:AUTOSet:TRIGger value``
              command.

        SCPI Syntax:
            ```
            - MASK:AUTOSet:TRIGger {ON|OFF|<NR1>}
            - MASK:AUTOSet:TRIGger?
            ```

        Info:
            - ``<NR1>`` = 0 disables the ``autoset:trigger`` function; any other value enables it.
            - ``ON`` enables the ``autoset:trigger`` function.
            - ``OFF`` disables the ``autoset:trigger`` function.
        """
        return self._trigger

    @property
    def user(self) -> MaskAutosetUser:
        """Return the ``MASK:AUTOSet:USER`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:AUTOSet:USER?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet:USER?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.one``: The ``MASK:AUTOSet:USER:ONE`` command.
            - ``.type``: The ``MASK:AUTOSet:USER:TYPe`` command.
            - ``.zero``: The ``MASK:AUTOSet:USER:ZERo`` command.
        """
        return self._user

    @property
    def vpos(self) -> MaskAutosetVpos:
        """Return the ``MASK:AUTOSet:VPOS`` command.

        Description:
            - This command controls whether the mask autoset algorithm will affect the vertical
              position (or offset) of the signal while attempting to autoset. The default is ON.
              This command, like all the mask autoset commands, affects only an autoset on a
              standard mask, not the general instrument autoset function.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:AUTOSet:VPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet:VPOS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:AUTOSet:VPOS value`` command.

        SCPI Syntax:
            ```
            - MASK:AUTOSet:VPOS {ON|OFF|<NR1>}
            - MASK:AUTOSet:VPOS?
            ```

        Info:
            - ``<NR1>`` = 0 disables the ``autoset:vpos`` function; any other value enables it.
            - ``ON`` enables the ``autoset:vpos`` function.
            - ``OFF`` disables the ``autoset:vpos`` function.
        """
        return self._vpos

    @property
    def vscale(self) -> MaskAutosetVscale:
        """Return the ``MASK:AUTOSet:VSCAle`` command.

        Description:
            - This command controls whether the mask autoset algorithm will affect the vertical
              scale while attempting to autoset. This command, like all the mask autoset commands,
              affects only an autoset on a standard mask, not the general instrument autoset
              function.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:AUTOSet:VSCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet:VSCAle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:AUTOSet:VSCAle value``
              command.

        SCPI Syntax:
            ```
            - MASK:AUTOSet:VSCAle {ON|OFF|<NR1>}
            - MASK:AUTOSet:VSCAle?
            ```

        Info:
            - ``<NR1>`` = 0 disables the ``autoset:vscale`` function; any other value enables it.
            - ``ON`` enables the ``autoset:vscale`` function.
            - ``OFF`` disables the ``autoset:vscale`` function.
        """
        return self._vscale


class MaskAutoadjustVdelta(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:AUTOAdjust:VDELTA`` command.

    Description:
        - This command sets or returns how far autofit searches vertically. Autofit moves the
          waveform vertically and/or horizontally to reduce the number of hits within a given mask.
          If infinite or variable persistence is enabled, these movements will clear any persistent
          data. If Autofit makes frequent adjustments, there might be very little or even no
          persistent data displayed.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:AUTOAdjust:VDELTA?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:AUTOAdjust:VDELTA?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:AUTOAdjust:VDELTA value`` command.

    SCPI Syntax:
        ```
        - MASK:AUTOAdjust:VDELTA {<NR3>}
        - MASK:AUTOAdjust:VDELTA?
        ```

    Info:
        - ``<NR3>`` is a floating point number that represents a percent of a division.
    """


class MaskAutoadjustHdelta(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:AUTOAdjust:HDELTA`` command.

    Description:
        - This command sets or returns how far autofit searches horizontally. Autofit moves the
          waveform vertically and/or horizontally to reduce the number of hits within a given mask.
          If infinite or variable persistence is enabled, these movements will clear any persistent
          data. If Autofit makes frequent adjustments, there might be very little or even no
          persistent data displayed.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:AUTOAdjust:HDELTA?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:AUTOAdjust:HDELTA?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:AUTOAdjust:HDELTA value`` command.

    SCPI Syntax:
        ```
        - MASK:AUTOAdjust:HDELTA {<NR3>}
        - MASK:AUTOAdjust:HDELTA?
        ```

    Info:
        - ``<NR3>`` is a floating point number that represents a percent of a division.
    """


class MaskAutoadjust(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:AUTOAdjust`` command.

    Description:
        - This command optimizes or queries the signal position within the mask to minimize hits. It
          sets a mode so that the ``MASK:SOURCE`` waveform is compared against the mask and is
          shifted up, down, left, or right to minimize the hits.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:AUTOAdjust?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:AUTOAdjust?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:AUTOAdjust value`` command.

    SCPI Syntax:
        ```
        - MASK:AUTOAdjust {ON|OFF|<NR1>}
        - MASK:AUTOAdjust?
        ```

    Info:
        - ``<NR1>`` = 0 disables the autoadjust function; any other value enables it.
        - ``ON`` enables the autoadjust function.
        - ``OFF`` disables the autoadjust function.

    Properties:
        - ``.hdelta``: The ``MASK:AUTOAdjust:HDELTA`` command.
        - ``.vdelta``: The ``MASK:AUTOAdjust:VDELTA`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hdelta = MaskAutoadjustHdelta(device, f"{self._cmd_syntax}:HDELTA")
        self._vdelta = MaskAutoadjustVdelta(device, f"{self._cmd_syntax}:VDELTA")

    @property
    def hdelta(self) -> MaskAutoadjustHdelta:
        """Return the ``MASK:AUTOAdjust:HDELTA`` command.

        Description:
            - This command sets or returns how far autofit searches horizontally. Autofit moves the
              waveform vertically and/or horizontally to reduce the number of hits within a given
              mask. If infinite or variable persistence is enabled, these movements will clear any
              persistent data. If Autofit makes frequent adjustments, there might be very little or
              even no persistent data displayed.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:AUTOAdjust:HDELTA?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:AUTOAdjust:HDELTA?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:AUTOAdjust:HDELTA value``
              command.

        SCPI Syntax:
            ```
            - MASK:AUTOAdjust:HDELTA {<NR3>}
            - MASK:AUTOAdjust:HDELTA?
            ```

        Info:
            - ``<NR3>`` is a floating point number that represents a percent of a division.
        """
        return self._hdelta

    @property
    def vdelta(self) -> MaskAutoadjustVdelta:
        """Return the ``MASK:AUTOAdjust:VDELTA`` command.

        Description:
            - This command sets or returns how far autofit searches vertically. Autofit moves the
              waveform vertically and/or horizontally to reduce the number of hits within a given
              mask. If infinite or variable persistence is enabled, these movements will clear any
              persistent data. If Autofit makes frequent adjustments, there might be very little or
              even no persistent data displayed.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:AUTOAdjust:VDELTA?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:AUTOAdjust:VDELTA?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:AUTOAdjust:VDELTA value``
              command.

        SCPI Syntax:
            ```
            - MASK:AUTOAdjust:VDELTA {<NR3>}
            - MASK:AUTOAdjust:VDELTA?
            ```

        Info:
            - ``<NR3>`` is a floating point number that represents a percent of a division.
        """
        return self._vdelta


#  pylint: disable=too-many-instance-attributes
class Mask(SCPICmdRead):
    """The ``MASK`` command.

    Description:
        - This query-only command returns the states of all settable mask parameters.

    Usage:
        - Using the ``.query()`` method will send the ``MASK?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MASK?
        ```

    Properties:
        - ``.autoadjust``: The ``MASK:AUTOAdjust`` command.
        - ``.autoset``: The ``MASK:AUTOSet`` command tree.
        - ``.copy``: The ``MASK:COPy`` command tree.
        - ``.count``: The ``MASK:COUNt`` command.
        - ``.display``: The ``MASK:DISplay`` command.
        - ``.filter``: The ``MASK:FILTer`` command.
        - ``.highlighthits``: The ``MASK:HIGHLIGHTHits`` command.
        - ``.invert``: The ``MASK:INVert`` command.
        - ``.lock``: The ``MASK:LOCk`` command.
        - ``.margin``: The ``MASK:MARgin`` command tree.
        - ``.maskpre``: The ``MASK:MASKPRE`` command tree.
        - ``.polarity``: The ``MASK:POLarity`` command.
        - ``.seg``: The ``MASK:SEG<m>`` command.
        - ``.source``: The ``MASK:SOUrce`` command.
        - ``.standard``: The ``MASK:STANdard`` command.
        - ``.stoponviolation``: The ``MASK:STOPOnviolation`` command.
        - ``.test``: The ``MASK:TESt`` command tree.
        - ``.user``: The ``MASK:USER`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "MASK") -> None:
        super().__init__(device, cmd_syntax)
        self._autoadjust = MaskAutoadjust(device, f"{self._cmd_syntax}:AUTOAdjust")
        self._autoset = MaskAutoset(device, f"{self._cmd_syntax}:AUTOSet")
        self._copy = MaskCopy(device, f"{self._cmd_syntax}:COPy")
        self._count = MaskCount(device, f"{self._cmd_syntax}:COUNt")
        self._display = MaskDisplay(device, f"{self._cmd_syntax}:DISplay")
        self._filter = MaskFilter(device, f"{self._cmd_syntax}:FILTer")
        self._highlighthits = MaskHighlighthits(device, f"{self._cmd_syntax}:HIGHLIGHTHits")
        self._invert = MaskInvert(device, f"{self._cmd_syntax}:INVert")
        self._lock = MaskLock(device, f"{self._cmd_syntax}:LOCk")
        self._margin = MaskMargin(device, f"{self._cmd_syntax}:MARgin")
        self._maskpre = MaskMaskpre(device, f"{self._cmd_syntax}:MASKPRE")
        self._polarity = MaskPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._seg: Dict[int, MaskSegItem] = DefaultDictPassKeyToFactory(
            lambda x: MaskSegItem(device, f"{self._cmd_syntax}:SEG{x}")
        )
        self._source = MaskSource(device, f"{self._cmd_syntax}:SOUrce")
        self._standard = MaskStandard(device, f"{self._cmd_syntax}:STANdard")
        self._stoponviolation = MaskStoponviolation(device, f"{self._cmd_syntax}:STOPOnviolation")
        self._test = MaskTest(device, f"{self._cmd_syntax}:TESt")
        self._user = MaskUser(device, f"{self._cmd_syntax}:USER")

    @property
    def autoadjust(self) -> MaskAutoadjust:
        """Return the ``MASK:AUTOAdjust`` command.

        Description:
            - This command optimizes or queries the signal position within the mask to minimize
              hits. It sets a mode so that the ``MASK:SOURCE`` waveform is compared against the mask
              and is shifted up, down, left, or right to minimize the hits.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:AUTOAdjust?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:AUTOAdjust?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:AUTOAdjust value`` command.

        SCPI Syntax:
            ```
            - MASK:AUTOAdjust {ON|OFF|<NR1>}
            - MASK:AUTOAdjust?
            ```

        Info:
            - ``<NR1>`` = 0 disables the autoadjust function; any other value enables it.
            - ``ON`` enables the autoadjust function.
            - ``OFF`` disables the autoadjust function.

        Sub-properties:
            - ``.hdelta``: The ``MASK:AUTOAdjust:HDELTA`` command.
            - ``.vdelta``: The ``MASK:AUTOAdjust:VDELTA`` command.
        """
        return self._autoadjust

    @property
    def autoset(self) -> MaskAutoset:
        """Return the ``MASK:AUTOSet`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:AUTOSet?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:AUTOSet?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.autoadjust``: The ``MASK:AUTOSet:AUTOAdjust`` command.
            - ``.hpos``: The ``MASK:AUTOSet:HPOS`` command.
            - ``.hscale``: The ``MASK:AUTOSet:HSCAle`` command.
            - ``.mode``: The ``MASK:AUTOSet:MODe`` command.
            - ``.offsetadj``: The ``MASK:AUTOSet:OFFSETAdj`` command.
            - ``.standard``: The ``MASK:AUTOSet:STANdard`` command.
            - ``.trigger``: The ``MASK:AUTOSet:TRIGger`` command.
            - ``.user``: The ``MASK:AUTOSet:USER`` command tree.
            - ``.vpos``: The ``MASK:AUTOSet:VPOS`` command.
            - ``.vscale``: The ``MASK:AUTOSet:VSCAle`` command.
        """
        return self._autoset

    @property
    def copy(self) -> MaskCopy:
        """Return the ``MASK:COPy`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:COPy?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:COPy?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.user``: The ``MASK:COPy:USER`` command.
        """
        return self._copy

    @property
    def count(self) -> MaskCount:
        """Return the ``MASK:COUNt`` command.

        Description:
            - This command resets to zero the number of hits and failures for all mask segments. A
              series of examples showing how to use mask commands for typical tasks is included in
              an appendix.

        Usage:
            - Using the ``.write(value)`` method will send the ``MASK:COUNt value`` command.

        SCPI Syntax:
            ```
            - MASK:COUNt RESET
            ```

        Sub-properties:
            - ``.failures``: The ``MASK:COUNt:FAILURES`` command.
            - ``.hits``: The ``MASK:COUNt:HITS`` command.
            - ``.seg``: The ``MASK:COUNt:SEG<m>`` command tree.
            - ``.state``: The ``MASK:COUNt:STATE`` command.
            - ``.tests``: The ``MASK:COUNt:TESTS`` command.
            - ``.total``: The ``MASK:COUNt:TOTal`` command.
            - ``.violations``: The ``MASK:COUNt:VIOLATIONS`` command.
            - ``.waveforms``: The ``MASK:COUNt:WAVEFORMS`` command.
        """
        return self._count

    @property
    def display(self) -> MaskDisplay:
        """Return the ``MASK:DISplay`` command.

        Description:
            - This command sets or queries whether defined masks are displayed on the screen. This
              is useful for temporarily turning off user-defined masks without deleting them. It is
              also useful for removing a standard mask from the screen, but leaving it as the
              selected standard. Mask counting, mask testing, and mask autoset are unavailable if
              the mask display is Off. The default is On.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:DISplay?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:DISplay?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:DISplay value`` command.

        SCPI Syntax:
            ```
            - MASK:DISplay {ON|OFF|<NR1>}
            - MASK:DISplay?
            ```

        Info:
            - ``<NR1>`` = 0 removes the masks from the display; any other value shows the masks on
              the display.
            - ``ON`` shows the masks on the display. This is the default value.
            - ``OFF`` removes the masks from the display.
        """
        return self._display

    @property
    def filter(self) -> MaskFilter:
        """Return the ``MASK:FILTer`` command.

        Description:
            - This command sets or returns whether the selected digital filter will be run on the
              waveform data. The filter simulates optical hardware. That is, it simulates different
              hardware for each of several different optical standards. The digital filter runs on
              OC1, OC3, OC12, OC48, FC133, FC266, FC531, FC1063, FC2125Draft, Gigabit Ethernet,
              Infiniband 2.5 Gb, 1394 b, 393 Mb, 786.43 Mb, 1.572 Gb

        Usage:
            - Using the ``.query()`` method will send the ``MASK:FILTer?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:FILTer?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:FILTer value`` command.

        SCPI Syntax:
            ```
            - MASK:FILTer {ON|OFF|<NR1>}
            - MASK:FILTer?
            ```

        Info:
            - ``<NR1>`` = 0 disables the digital filter; any other value enables it.
            - ``OFF`` disables the digital filter.
            - ``ON`` enables the digital filter.

        Sub-properties:
            - ``.orr``: The ``MASK:FILTer:ORR`` command tree.
        """
        return self._filter

    @property
    def highlighthits(self) -> MaskHighlighthits:
        """Return the ``MASK:HIGHLIGHTHits`` command.

        Description:
            - This command sets or returns whether hits in a mask are highlighted in different
              colors than other waveform data. The default is On.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:HIGHLIGHTHits?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:HIGHLIGHTHits?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:HIGHLIGHTHits value`` command.

        SCPI Syntax:
            ```
            - MASK:HIGHLIGHTHits {ON|OFF|<NR1>}
            - MASK:HIGHLIGHTHits?
            ```

        Info:
            - ``<NR1>`` = 0 disables the ``mask:highlighthits`` function; any other value enables
              it.
            - ``OFF`` disables the ``mask:highlighthits`` function.
            - ``ON`` enables the ``mask:highlighthits`` function.
        """
        return self._highlighthits

    @property
    def invert(self) -> MaskInvert:
        """Return the ``MASK:INVert`` command.

        Description:
            - This command controls whether the mask is drawn inverted. It has no effect if this
              mask cannot be inverted. The default is Off (Positive).

        Usage:
            - Using the ``.write(value)`` method will send the ``MASK:INVert value`` command.

        SCPI Syntax:
            ```
            - MASK:INVert {ON|OFF|<NR1>}
            ```

        Info:
            - ``<NR1>`` = 0 disables the ``mask:invert`` function; any other value enables it.
            - ``OFF`` Positive.
            - ``ON`` Negative.
        """
        return self._invert

    @property
    def lock(self) -> MaskLock:
        """Return the ``MASK:LOCk`` command.

        Description:
            - This command locks the mask to the source waveform so that any changes made to the
              horizontal and/or vertical scale settings of the waveform will redraw the mask
              segments in proportion. This feature is useful for expanding the horizontal and/or
              vertical settings in order to zoom in on waveforms and masks, and visually examine
              violation areas in more detail. A series of examples showing how to use mask commands
              for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:LOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:LOCk?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:LOCk value`` command.

        SCPI Syntax:
            ```
            - MASK:LOCk {ON|OFF|<NR1>}
            - MASK:LOCk?
            ```

        Info:
            - ``ON`` turns on this feature, so that the mask is locked to the waveform.
            - ``OFF`` turns off this feature.
            - ``<NR1> = 0`` turns off this feature. Any other value turns it on.
        """
        return self._lock

    @property
    def margin(self) -> MaskMargin:
        """Return the ``MASK:MARgin`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MARgin?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MARgin?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.percent``: The ``MASK:MARgin:PERCent`` command.
            - ``.state``: The ``MASK:MARgin:STATE`` command.
        """
        return self._margin

    @property
    def maskpre(self) -> MaskMaskpre:
        """Return the ``MASK:MASKPRE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASKPRE?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASKPRE?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.amplitude``: The ``MASK:MASKPRE:AMPlitude`` command.
            - ``.hscale``: The ``MASK:MASKPRE:HSCAle`` command.
            - ``.htrigpos``: The ``MASK:MASKPRE:HTRIGPOS`` command.
            - ``.patternbits``: The ``MASK:MASKPRE:PATTERNBITS`` command.
            - ``.presampbits``: The ``MASK:MASKPRE:PRESAMPBITS`` command.
            - ``.recordlength``: The ``MASK:MASKPRE:RECOrdlength`` command.
            - ``.serialtrig``: The ``MASK:MASKPRE:SERIALTRIG`` command.
            - ``.trigtosamp``: The ``MASK:MASKPRE:TRIGTOSAMP`` command.
            - ``.voffset``: The ``MASK:MASKPRE:VOFFSet`` command.
            - ``.vpos``: The ``MASK:MASKPRE:VPOS`` command.
            - ``.vscale``: The ``MASK:MASKPRE:VSCAle`` command.
            - ``.width``: The ``MASK:MASKPRE:WIDth`` command.
        """
        return self._maskpre

    @property
    def polarity(self) -> MaskPolarity:
        """Return the ``MASK:POLarity`` command.

        Description:
            - This command sets or returns the input waveform polarity for the pass/fail test. It
              controls whether to test positive pulse, negative pulse, or both during pass/fail
              testing. This command only applies when ``MASK:TEST:STATE`` is on.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:POLarity?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:POLarity value`` command.

        SCPI Syntax:
            ```
            - MASK:POLarity {BOTh|NEGAtive|POSITIVe}
            - MASK:POLarity?
            ```

        Info:
            - ``BOTh`` enables testing for both positive and negative pulses. The instrument tests
              positive pulses on the ``mask:source`` waveform until ½ of the waveform is tested.
              Then the instrument inverts the mask and performs the remaining tests.
            - ``NEGAtive`` enables testing on negative pulses.
            - ``POSITIVe`` enables testing on positive pulses. This is the default.
        """
        return self._polarity

    @property
    def seg(self) -> Dict[int, MaskSegItem]:
        """Return the ``MASK:SEG<m>`` command.

        Description:
            - This command deletes the specified mask segment from the current mask. m is an integer
              that specifies the mask segment number to delete from the current mask.

        Usage:
            - Using the ``.write(value)`` method will send the ``MASK:SEG<m> value`` command.

        SCPI Syntax:
            ```
            - MASK:SEG<m> DELEte
            ```

        Info:
            - ``DELETE`` removes the specified mask segment from the mask.

        Sub-properties:
            - ``.nr_pt``: The ``MASK:SEG<m>:NR_Pt`` command.
            - ``.points``: The ``MASK:SEG<m>:POINTS`` command.
        """
        return self._seg

    @property
    def source(self) -> MaskSource:
        """Return the ``MASK:SOUrce`` command.

        Description:
            - This command sets or reports which source will be compared against the mask(s) when
              counting is turned on; it controls which trace to use in mask counting. It also
              affects mask autoset and how triggering is set up when you select the mask.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:SOUrce?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:SOUrce value`` command.

        SCPI Syntax:
            ```
            - MASK:SOUrce {CH<x>|MATH<x>|REF<x>}
            - MASK:SOUrce?
            ```

        Info:
            - ``CH<1-4>`` selects a channel waveform to be compared against the specified mask. The
              range for is 1 through 4.
            - ``MATH<1-4>`` selects a math waveform to be compared against the specified mask. The
              range for is 1 through 4.
            - ``REF<1-4>`` selects a reference waveform to be compared against the specified mask.
              The range is 1 through 4.
        """
        return self._source

    @property
    def standard(self) -> MaskStandard:
        """Return the ``MASK:STANdard`` command.

        Description:
            - This command deletes the existing mask (if any) and sets the selected standard mask.
              If ``MASK:COUNT:STATE`` is ON, mask counting starts immediately. The query form of
              this command returns the current mask standard. The following warning event is posted
              if the mask exceeds the instrument bandwidth: 2318,'Consider system bandwidth when
              testing at this bit rate.'

        Usage:
            - Using the ``.query()`` method will send the ``MASK:STANdard?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:STANdard?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:STANdard value`` command.

        SCPI Syntax:
            ```
            - MASK:STANdard {ATARXG<x>|ATATXG1|ATATXG2|ATATXG3|CLOCKCoax|CLOCKSymmetrical|D<x>|DS0Contra|DS0Double|DS0Single|DS0Timing|DS1|DS1A|DS1C|DS2|DS2RATECoax|DS2RATESymmetrical|DS3|DS4NA|DS4NA_Max|E1Coax|E1Symmetrical|E2|E3|E4_1|E4_0|ENET1000BCX_ATP2|ENET1000BCX_ATP3|ENET1000BCX_NTP2|ENET100FX|ENET100STP|ENET100UTP|ENET1250|ENETXAUI_Far|ENETXAUI_Near|FC1063|FC1063Draft|FC1063E|FC1063E_ABR|FC1063E_ABT|FC1063E_ADR|FC1063E_ADT|FC1063E_AGR|FC1063E_AGT|FC1063E_NBT|FC1063E_NDT|FC1063E_NGT|FC133|FC133E|FC2125|FC2125E_ABR|FC2125E_ABT|FC2125E_ADR|FC2125E_ADT|FC2125E_AGR|FC2125E_AGT|FC2125E_NBT|FC2125E_NDT|FC2125E_NGT|FC266|FC266E|FC4250E_ABR|FC4250E_ABT|FC4250E_ADR|FC4250E_ADT|FC4250E_AGR|FC4250E_AGT|FC4250E_NBT|FC4250E_NDT|FC4250E_NGT|FC531|FC531E|FST1|FST2|FST3|FST4|FST5|FST6|FW1394BS1600B|FW1394BS1600BT1|FW1394BS1600BT2|FW1394BS400B|FW1394BS400BT1|FW1394BS400BT2|FW1394BS800B|FW1394BS800BT1|FW1394BS800BT2|G703DS1|G703DS3|HST<x>|INF2_5G|INF2_5GE|NONe|OC1|OC12|OC3|OC48|OC48_FEC|PCIEXPRESS_Rcv|PCIEXPRESS_Xmit|RATE32Mbit|RATE97Mbit|RIO_DRV1G|RIO_DRV1_5G|RIO_DRV2G|RIO_DRV500M|RIO_DRV500M|RIO_DRV750M|RIO_EDRV1G|RIO_EDRV1_5G|RIO_EDRV2G|RIO_EDRV500M|RIO_EDRV500M|RIO_EDRV750M|RIO_RCV1G|RIO_RCV1_5G|RIO_RCV2G|RIO_RCV500M|RIO_RCV500M|RIO_RCV750M|RIO_SERIAL_1G|RIO_SERIAL_2G|RIO_SERIAL_3G|SFI5_RCVBCLK2|SFI5_RCVBCLK3|SFI5_RCVBDATA2|SFI5_RCVBDATA3|SFI5_RCVDCLK2|SFI5_RCVDCLK3|SFI5_RCVDDATA2|SFI5_RCVDDATA3|SFI5_XMITACLK2|SFI5_XMITACLK3|SFI5_XMITADATA2|SFI5_XMITADATA3|SFI5_XMITCCLK2|SFI5_XMITCCLK3|SFI5_XMITCDATA2|SFI5_XMITCDATA3|STM0_0|STM0_1|STM0_HDBX|STM1E_1|STM1E_0|STS1Eye|STS1Pulse|STS3|STS3_Max|TFI5_2|TFI5_3|USERMask|VIDEO270|VIDEO292M|VIDEO360|VSROC192|SAS1_5_IR|SAS1_5_CR|SAS1_5_XR|SAS1_5_IR_AASJ|SAS1_5_CR_AASJ|SAS1_5_XR_AASJ|SAS1_5_SATA|SAS3_0_IR|SAS3_0_CR|SAS3_0_XR|SAS3_0_IR_AASJ|SAS3_0_CR_AASJ|SAS3_0_XR_AASJ|SAS3_0_SATA}
            - MASK:STANdard?
            ```

        Info:
            - ``ATARXG1`` (Serial ATA, G1 Rx 1.5 Gb/s).
            - ``ATARXG2`` (Serial ATA, G2, Rx, 3.0 Gb/s).
            - ``ATARXG3`` (Serial ATA, G3, Rx).
            - ``ATATXG1`` (Serial ATA, G1 Tx, 1.5 Gb/s).
            - ``ATATXG2`` (Serial ATA, G2 Tx, 3.0 Gb/s).
            - ``H ATATXG3`` (Serial ATA, G3 Tx).
            - ``CLOCKCoax``
            - ``CLOCKSymmetrical``
            - ``D1``
            - ``D2``
            - ``DS0Contra`` (ITU-T, G703 (10/98), 64 kb/s).
            - ``DS0Double`` (ITU-T, G703 (10/98), 64 kb/s).
            - ``DS0Single`` (ITU-T, G703 (10/98), 64 kb/s).
            - ``DS0Timing`` (ITU-T, G703 (10/98), 64 kb/s).
            - ``DS1`` (ANSI T1.102-1993 (R1999), DS1, 1.544 Mb/s).
            - ``DS1A`` (ANSI T1.102-1993 (R1999), DS1A, 2.048 Mb/s).
            - ``DS1C`` (ANSI T1.102-1993 (R1999), DS1C, 3.152 Mb/s).
            - ``DS2`` (ANSI T1.102-1993 (R1999), DS2, 6.312 Mb/s).
            - ``DS2RATECoax`` (ITU-T, G703 (10/98), D2 Rate Coax, 6.312 Mb/s).
            - ``DS2RATESymmetrical`` (ITU-T, G703 (10/98), D2 Rate Sym, 6.312 Mb/s).
            - ``DS3`` (ANSI T1.102-1993 (R1999), DS3, 44.736 Mb/s).
            - ``DS4NA`` (ANSI T1.102-1993 (R1999), DS4NA, 139.26 Mb/s).
            - ``DS4NA_Max`` (ANSI T1.102-1993 (R1999), DSNA Max Output, 139.26 Mb.
            - ``E1Coax`` (ITU-T, G703 (10/98), E1 Coax Pair, 2.048 Mb/s).
            - ``E1Symmetrical`` (ITU-T, G703 (10/98), E1 Sym Pair, 2.048 Mb/s).
            - ``E2`` (ITU-T, G703 (10/98), E2, 8.448 Mb/s).
            - ``E3`` (ITU-T, G703 (10/98), E3, 34.368 Mb/s).
            - ``E4_0`` (ITU-T, G703 (10/98), E4 Binary 0).
            - ``E4_1`` (ITU-T, G703 (10/98), E4 Binary 1).
            - ``ENET100FX``
            - ``ENET100STP`` (IEEE Std 802.3 and ANSI X3.263-1995, 100 Base-Tx, STP, 125 Mb/s ).
            - ``ENET100UTP`` (IEEE Std 802.3 and ANSI X3.263-1995, 100 Base-Tx, UTP, 125 Mb/s).
            - ``ENET1000BCX_ATP2`` (1000B-CX Abs, TP2, 1.25 Gb/s).
            - ``ENET1000BCX_ATP3`` (1000B-CX Abs, TP3, 1.25 Gb/s).
            - ``ENET1000BCX_NTP2`` (1000B-CX Norm, TP2, 1.25 Gb/s).
            - ``ENET1250`` (IEEE Std 802.3 and ANSI X3.263-1995, GB Ethernet, 1.25 Gb/s).
            - ``ENETXAUI_FAR`` (10 Gigabit Attachment Unit Interface (XAUI), Far, 3.125 Gb/s).
            - ``ENETXAUI_Near`` (10 Gigabit Attachment Unit Interface (XAUI), Near, 3,125 Gb/s).
            - ``FC133`` (ANSI X3.230-1999 NCITS 1235D/Rev 11, Optical, 132.8 Mb/s).
            - ``FC133E`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Electrical 132.8 Mb/s).
            - ``FC266`` (ANSI X3.230-1999 NCITS 1235D/Rev 11, Optical, 265.6 Mb/s).
            - ``FC266E`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Electrical, 132.8 Mb/s).
            - ``FC531`` (ANSI X3.230-1999 NCITS 1235D/Rev 11, Optical, 531.2 Mb/s).
            - ``FC531E`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Electrical, 531.2 Mb/s).
            - ``FC1063`` (ANSI X3.230-1999 NCITS 1235D/Rev 11, Optical, 1.065 Gb/s).
            - ``FC1063E`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Electrical, 1.0625 Gb/s).
            - ``FC1063E_ABT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Beta, Transm).
            - ``FC1063E_ADT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Beta, Transm).
            - ``FC1063E_AGT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Gamma, Transm).
            - ``FC1063E_NBT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Norm, Beta, Transm).
            - ``FC1063E_NDT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Norm, Delta, Transm).
            - ``FC1063E_NGT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Norm, Gamma, Transm).
            - ``FC1063E_ABR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Beta, Recv).
            - ``FC1063E_ADR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Delta, Recv).
            - ``FC1063E_AGR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Gamma, Recv).
            - ``FC1063Draft`` (ANSI X3.230-1999 NCITS 1235D/Rev 11, Optical, Draft Rev 11).
            - ``FC2125`` (ANSI X3.230-1999 NCITS 1235D/Rev 11, Optical, 2.125).
            - ``FC2125E_ABT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Beta, Transm).
            - ``FC2125E_ADT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Delta, Transm).
            - ``FC2125E_AGT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Gamma, Transm).
            - ``FC2125E_NBT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Norm, Beta, Transm).
            - ``FC2125E_NDT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Norm, Delta, Transm).
            - ``FC2125E_NGT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Norm, Gamma, Transm).
            - ``FC2125E_ABR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Beta, Recv).
            - ``FC2125E_ADR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Delta, Recv).
            - ``FC2125E_AGR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 11, Abs, Gamma, Recv).
            - ``FC4250E_ABT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 4.0, Abs, Beta, Transm).
            - ``FC4250E_ADT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 4.0, Abs, Delta, Transm).
            - ``FC4250E_AGT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 4.0, Abs, Gamma, Transm).
            - ``FC4250E_NBT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 4.0, Norm, Beta, Transm).
            - ``FC4250E_NDT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 4.0, Norm, Delta, Transm).
            - ``FC4250E_NGT`` (ANS1 X3.230-1999 NCITS 1235D/Rev 4.0, Norm, Gamma, Transm).
            - ``FC4250E_ABR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 4.0, Abs, Beta, Recv).
            - ``FC4250E_ADR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 4.0, Abs, Delta, Recv).
            - ``FC4250E_AGR`` (ANS1 X3.230-1999 NCITS 1235D/Rev 4.0, Abs, Gamma, Recv).
            - ``FST1`` (USB, ``FS:T1``, 12 Mb/s).
            - ``FST2`` (USB, ``FS:T2``, 12 Mb/s).
            - ``FST3`` (USB, ``FS:T3``, 12 Mb/s).
            - ``FST4`` (USB, ``FS:T4``: 12 Mb/s).
            - ``FST5`` (USB, ``FS:T5``, 12 Mb/s).
            - ``FST6`` (USB, ``FS:T6``, 12 Mb/s).
            - ``FW1394BS400B`` (IEEE 1394b, S400 Optical, 491.5 Mb/s).
            - ``FW1394BS400BT1`` (IEEE 1394b, S400b T1, 491.5 Mb/s).
            - ``FW1394BS400BT2`` (IEEE 1394b, S400b T2, 491.5 Mb/s).
            - ``FW1394BS800B`` (IEEE 1394b, S800 Optical, 988.0 Mb/s).
            - ``FW1394BS800BT1`` (IEEE 1394b, S800b T1, 983.0 Mb/s).
            - ``FW1394BS800BT2`` (IEEE 1394b, S800b T2, 983.0 Mb/s).
            - ``FW1394BS1600B`` (IEEE 1394b, S1600 Optical, 1.966 Gb/s).
            - ``FW1394BS1600BT1`` (IEEE 1394b, S1600b T1, 1.966 Gb/s).
            - ``FW1394BS1600BT2`` (IEEE 1394b, S1600b T2, 1.966 Gb/s).
            - ``G703D1`` (ITU-T, G703 (10/98), DS1 Rate, 1.544 Mb/s).
            - ``G703DS3`` (ITU-T, G703 (10/98).
            - ``HST1`` (USB, ``HS:T1``, 480 Mb/s) G703DS3 (ITU-T, G703 (10/98).
            - ``HST2`` (USB, ``HS:T2``, 480 Mb/s) G703DS3 (ITU-T, G703 (10/98).
            - ``HST3`` (USB, ``HS:T3``, 480 Mb/s).
            - ``HST4`` (USB, ``HS:T4``, 480 Mb/s).
            - ``HST5`` (USB, ``HS:T5``, 480 Mb/s).
            - ``HST6`` (USB, ``HS:T6``, 480 Mb/s).
            - ``INF2_5G`` (InfiniBand, IBTA Spec 1.0a, 2.5 Optical, 2.5 Gb/s).
            - ``INF2_5GE`` (InfiniBand, IBTA Spec 1.0a, 2.5 Electrical, 2.5 Gb/s).
            - ``NONe``
            - ``OC1`` (GR 253-CORE Issue 3 9/21/2000 OC1/STM0, 51.84 Mb/s).
            - ``OC3`` (GR 253-CORE Issue 3 9/21/2000 OC1/STM1, 155.52, Mb/s).
            - ``OC12`` (GR 253-CORE Issue 3 9/21/2000 OC1/STM4, 622.08 Mb/s).
            - ``OC48`` (GR 253-CORE Issue 3 9/21/2000 OC1/STM16, 2.4883 Gb/s.
            - ``OC48_FEC`` (Forward Error Correction - CSA8000 mask, 2.666 Gb/s).
            - ``PCIEXPRESS_Xmit`` (PCI Express Transmitter, 2.5 Gb/s).
            - ``PCIEXPRESS_Rcv`` (PCI Express Receiver, 2.5 Gb/s).
            - ``RATE32Mbit`` (ITU-T, G703 (10/98), 32.064 Mb/s).
            - ``RATE97Mbit`` (ITU-T, G703 (10/98), 97 Mbit, 97.728 Mb/s).
            - ``RIO_DRV1G`` (Rapid IO Driver, 1 Gb/s).
            - ``RIO_DRV1_5G`` (Rapid IO Driver, 5 Gb/s).
            - ``RIO_DRV2G`` (Rapid IO Driver, 2 Gb/s).
            - ``RIO_DRV500M`` (Rapid IO Driver, 500 Mb/s).
            - ``RIO_DRV750M`` (Rapid IO Driver, 750 Mb/s).
            - ``RIO_EDRV1G`` (Rapid IO Extended Driver, 1 Gb/s).
            - ``RIO_EDRV1_5G`` (Rapid IO Extended Driver, 1.5 Gb/s).
            - ``RIO_EDRV2G`` (Rapid IO Extended Driver, 2 Gb/s).
            - ``RIO_EDRV500M`` (Rapid IO Extended Driver, 500 Mb/s).
            - ``RIO_EDRV750M`` (Rapid IO Extended Driver, 750 Mb/s).
            - ``RIO_RCV500M`` (Rapid IO Receiver, 500 Mb/s).
            - ``RIO_RCV750M`` (Rapid IO Receiver, 750 Mb/s).
            - ``RIO_RCV1G`` (Rapid IO Receiver, 1 Gb/s).
            - ``RIO_RCV1_5G`` (Rapid IO Receiver, 1.5 Gb/s).
            - ``RIO_RCV2G`` (Rapid IO Receiver, 2 Gb/s).
            - ``RIO_SERIAL_1G`` (Rapid IO Serial, 1.25 Gb/s).
            - ``RIO_SERIAL_2G`` (Rapid IO Serial, 2.5 Gb/s).
            - ``RIO_SERIAL_3G`` (Rapid IO Serial, 3.25 Gb/s).
            - ``SFI5_XMITADATA2`` (SFI15 Transmit: Test Point A Data Signal 2, 2.488 Gb/s).
            - ``SFI5_XMITCDATA2`` (SFI15 Transmit: Test Point C Data Signal 2, 2.488 Gb/s).
            - ``SFI5_XMITACLK2`` (SFI15 Transmit: Test Point A Clock Signal 2, 2.488 Gb/s).
            - ``SFI5_XMITCCLK2`` (SFI15 Transmit: Test Point C Clock Signal 2, 2.488 Gb/s).
            - ``SFI5_RCVBDATA2`` (SFI15 Receive: Test Point B Data Signal 2, 2.488 Gb/s).
            - ``SFI5_RCVDDATA2`` (SFI15 Receive: Test Point D Data Signal 2, 2.488 Gb/s).
            - ``SFI5_RCVBCLK2`` (SFI15 Receive: Test Point B Clock Signal 2, 2.488 Gb/s).
            - ``SFI5_RCVDCLK2`` (SFI15 Receive: Test Point D Clock Signal 2, 2.488 Gb/s).
            - ``SFI5_XMITADATA3`` (SFI15 Transmit: Test Point A Data Signal 3, 3.125 Gb/s).
            - ``SFI5_XMITCDATA3`` (SFI15 Transmit: Test Point C Data Signal 3, 3.125 Gb/s).
            - ``SFI5_XMITACLK3`` (SFI15 Transmit: Test Point A Clock Signal 3, 3.125 Gb/s).
            - ``SFI5_XMITCCLK3`` (SFI15 Transmit: Test Point C Clock Signal 3, 3.125 Gb/s).
            - ``SFI5_RCVBDATA3`` (SFI15 Receive: Test Point B Data Signal 3, 3.125 Gb/s).
            - ``SFI5_RCVDDATA3`` (SFI15 Receive: Test Point D Data Signal 3, 3.125 Gb/s).
            - ``SFI5_RCVBCLK3`` (SFI15 Receive: Test Point B Clock Signal 3, 3.125 Gb/s).
            - ``SFI5_RCVDCLK3`` (SFI15 Receive: Test Point D Clock Signal 3, 3.125 Gb/s.
            - ``STM0_0`` (ITU-T, G703 (10/98), STM1E Binary 0).
            - ``STM0_1`` (ITU-T, G703 (10/98), STM1E Binary 1).
            - ``STM0_HDBX``
            - ``STS1Eye`` (ANSI T1.102-1993 (R1999), STS-1 Eye, 51.84 Mb/s).
            - ``STS1Pulse`` (ANSI T1.102-1993 (R1999), STS-1 Pulse, 51.84 Mb/s).
            - ``STS3`` (ANSI T1.102-1993 (R1999), STS-3, 155.52 Mb/s).
            - ``STS3_Max`` (ANSI T1.102-1993 (R1999), STS-3 Max Output, 155.52 Mb/s).
            - ``TFI15_2`` (TFI-5, 2.488 Gb/s).
            - ``TFI5_3`` (TFI-5, 3.1104 Gb/s).
            - ``USERMask``
            - ``VIDEO270``
            - ``VIDEO292M``
            - ``VIDEO360``
            - ``VSROC192`` (VSR OC192/STM64, 1.24416 Gb/s).
        """  # noqa: E501
        return self._standard

    @property
    def stoponviolation(self) -> MaskStoponviolation:
        """Return the ``MASK:STOPOnviolation`` command.

        Description:
            - This command stops the waveform acquisitions upon the first occurrence of a waveform
              violation. The ``MASK:ACTONEVENT:ENABLE`` command should be set to ON for this event
              to happen. After the event occurs ``MASK:ACTONEVENT:ENABLE`` command will be set to
              OFF automatically. You can also specify an action to be performed when acquisitions
              are stopped by using the commands such as ``MASK:TEST:SAVEWFM``,
              ``MASK:TEST:SAVEIMAGE``, ``MASK:TEST:AUXOUT:FAILURE``, ``MASK:TEST:HARDCOPY``, or
              ``MASK:TEST:SRQ:FAILURE``. A series of examples showing how to use mask commands for
              typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:STOPOnviolation?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:STOPOnviolation?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:STOPOnviolation value``
              command.

        SCPI Syntax:
            ```
            - MASK:STOPOnviolation {ON|OFF|<NR1>}
            - MASK:STOPOnviolation?
            ```

        Info:
            - ``ON`` stops waveform acquisition on the first occurrence of a mask violation.
            - ``OFF`` turns this feature off.
            - ``<NR1>=0`` turns this feature off ; any other value turns it on.
        """
        return self._stoponviolation

    @property
    def test(self) -> MaskTest:
        """Return the ``MASK:TESt`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.aux``: The ``MASK:TESt:AUX`` command tree.
            - ``.beep``: The ``MASK:TESt:BEEP`` command tree.
            - ``.delay``: The ``MASK:TESt:DELay`` command.
            - ``.hardcopy``: The ``MASK:TESt:HARDCopy`` command.
            - ``.log``: The ``MASK:TESt:LOG`` command tree.
            - ``.repeat``: The ``MASK:TESt:REPeat`` command.
            - ``.sample``: The ``MASK:TESt:SAMple`` command.
            - ``.savewfm``: The ``MASK:TESt:SAVEWFM`` command.
            - ``.srq``: The ``MASK:TESt:SRQ`` command tree.
            - ``.state``: The ``MASK:TESt:STATE`` command.
            - ``.status``: The ``MASK:TESt:STATUS`` command.
            - ``.stop``: The ``MASK:TESt:STOP`` command tree.
            - ``.threshold``: The ``MASK:TESt:THReshold`` command.
            - ``.waveform``: The ``MASK:TESt:WAVEform`` command.
        """
        return self._test

    @property
    def user(self) -> MaskUser:
        """Return the ``MASK:USER`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.amplitude``: The ``MASK:USER:AMPlitude`` command.
            - ``.bitrate``: The ``MASK:USER:BITRate`` command.
            - ``.hscale``: The ``MASK:USER:HSCAle`` command.
            - ``.htrigpos``: The ``MASK:USER:HTRIGPOS`` command.
            - ``.label``: The ``MASK:USER:LABel`` command.
            - ``.patternbits``: The ``MASK:USER:PATTERNBITS`` command.
            - ``.presampbits``: The ``MASK:USER:PRESAMPBITS`` command.
            - ``.recordlength``: The ``MASK:USER:RECOrdlength`` command.
            - ``.seg``: The ``MASK:USER:SEG<m>`` command.
            - ``.trigtosamp``: The ``MASK:USER:TRIGTOSAMP`` command.
            - ``.voffset``: The ``MASK:USER:VOFFSet`` command.
            - ``.vpos``: The ``MASK:USER:VPOS`` command.
            - ``.vscale``: The ``MASK:USER:VSCAle`` command.
            - ``.width``: The ``MASK:USER:WIDth`` command.
        """
        return self._user
