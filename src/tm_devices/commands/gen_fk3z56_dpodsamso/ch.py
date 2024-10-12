# pylint: disable=line-too-long
"""The ch commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CH<x>:ATIACTive?
    - CH<x>:AVAILable?
    - CH<x>:BANdwidth {<NR3>|FIVe|FULl|TWEnty|ONEfifty|TWOfifty}
    - CH<x>:BANdwidth:ENHanced {AUTO|OFF}
    - CH<x>:BANdwidth:ENHanced:ALLMatched?
    - CH<x>:BANdwidth:ENHanced:APPLYtoall {ON|OFF|1|0}
    - CH<x>:BANdwidth:ENHanced:APPLYtoall?
    - CH<x>:BANdwidth:ENHanced:FORCe {OFF|ON}
    - CH<x>:BANdwidth:ENHanced:FORCe?
    - CH<x>:BANdwidth:ENHanced:STATE?
    - CH<x>:BANdwidth:ENHanced?
    - CH<x>:BANdwidth?
    - CH<x>:COUPling {AC|DC|DCREJect|GND}
    - CH<x>:COUPling?
    - CH<x>:DESKew <NR3>
    - CH<x>:DESKew?
    - CH<x>:FASTAcqcapable?
    - CH<x>:FASTFRamecapable?
    - CH<x>:ICAPture:SOUrce {D<x>|CQ0}
    - CH<x>:ICAPture:SOUrce?
    - CH<x>:ICAPture:STATE {ON|OFF|<NR1>}
    - CH<x>:ICAPture:STATE?
    - CH<x>:INVert {ON|OFF|<NR1>}
    - CH<x>:INVert?
    - CH<x>:LABel:NAMe <QString>
    - CH<x>:LABel:NAMe?
    - CH<x>:LABel:XPOS <NR1>
    - CH<x>:LABel:XPOS?
    - CH<x>:LABel:YPOS <NR1>
    - CH<x>:LABel:YPOS?
    - CH<x>:OFFSet <NR3>
    - CH<x>:OFFSet?
    - CH<x>:OPTI:POWER?
    - CH<x>:OPTIcal:RCVR {OFF|FLAT|FLAT33|ENET257R4|ENET266PAM4| OTU2795|FC28050|USER} [,<NR1>]
    - CH<x>:OPTIcal:RCVR:USERVALue?
    - CH<x>:OPTIcal:WLENgth <NR1> [, USER|, FACTory]
    - CH<x>:OPTIcal:WLENgth:LIST?
    - CH<x>:OPTIcal:WLENgth?
    - CH<x>:POSition <NR3>
    - CH<x>:POSition?
    - CH<x>:PROBECOntrol {AUTO|MANual}
    - CH<x>:PROBECOntrol?
    - CH<x>:PROBECal?
    - CH<x>:PROBEFunc:EXTAtten <NR3>
    - CH<x>:PROBEFunc:EXTAtten?
    - CH<x>:PROBEFunc:EXTDBatten <NR3>
    - CH<x>:PROBEFunc:EXTDBatten?
    - CH<x>:PROBEFunc:EXTUnits <QString>
    - CH<x>:PROBEFunc:EXTUnits?
    - CH<x>:PRObe:AUTOZero EXECute
    - CH<x>:PRObe:DC:CALibration:LAST:HARDware?
    - CH<x>:PRObe:DC:CALibration:LAST:TIME?
    - CH<x>:PRObe:DEGAUSS EXECute
    - CH<x>:PRObe:DEGAUSS:STATE?
    - CH<x>:PRObe:FORCEDRange <dynamicRangeNR3>
    - CH<x>:PRObe:FORCEDRange?
    - CH<x>:PRObe:GAIN?
    - CH<x>:PRObe:ID:SERnumber?
    - CH<x>:PRObe:ID:TYPe?
    - CH<x>:PRObe:ID?
    - CH<x>:PRObe:INPUTMode {DEFault|DIFFerential|COMmonmode|A|B}
    - CH<x>:PRObe:INPUTMode:AOFFSet <NR3>
    - CH<x>:PRObe:INPUTMode:AOFFSet?
    - CH<x>:PRObe:INPUTMode:BOFFSet <NR3>
    - CH<x>:PRObe:INPUTMode:BOFFSet?
    - CH<x>:PRObe:INPUTMode:CMOFFSet <NR3>
    - CH<x>:PRObe:INPUTMode:CMOFFSet?
    - CH<x>:PRObe:INPUTMode:DMOFFSet <NR3>
    - CH<x>:PRObe:INPUTMode:DMOFFSet?
    - CH<x>:PRObe:INPUTMode?
    - CH<x>:PRObe:RANge <rangeName>{ATTEN1X|ATTEN1_25X|ATTEN1_5X|ATTEN1_75X|ATTEN2X| ATTEN2_5X|ATTEN3X|ATTEN3_5X|ATTEN4X|ATTEN4_5X| ATTEN5X|ATTEN5_5X|ATTEN6X|ATTEN6_5X|ATTEN7X| ATTEN7_5X|ATTEN8X|ATTEN8_5X|ATTEN9X|ATTEN9_5X| ATTEN10X|ATTEN12_5X|ATTEN15X|ATTEN17_5X|ATTEN20X| ATTEN25X|ATTEN30X|ATTEN35X|ATTEN40X|ATTEN45X| ATTEN50X|ATTEN55X|ATTEN60X|ATTEN65X|ATTEN70X| ATTEN75X|ATTEN80X|ATTEN85X|ATTEN90X|ATTEN95X| ATTEN100X|ATTEN125X|ATTEN150X|ATTEN175X|ATTEN200X| ATTEN250X|ATTEN300X|ATTEN350X|ATTEN400X|ATTEN450X| ATTEN500X|ATTEN550X|ATTEN600X|ATTEN650X|ATTEN700X| ATTEN750X|ATTEN800X|ATTEN850X|ATTEN900X|ATTEN950X| ATTEN1000X}
    - CH<x>:PRObe:RANge?
    - CH<x>:PRObe:RESistance?
    - CH<x>:PRObe:SET <QString>
    - CH<x>:PRObe:SET?
    - CH<x>:PRObe:SIGnal {PASS|BYPass}
    - CH<x>:PRObe:SIGnal?
    - CH<x>:PRObe:TIPtype {HBWStraightflex|OTHer}
    - CH<x>:PRObe:TIPtype?
    - CH<x>:PRObe:UNIts?
    - CH<x>:PRObe?
    - CH<x>:SCAle <NR3>
    - CH<x>:SCAle?
    - CH<x>:TERmination <NR3>
    - CH<x>:TERmination?
    - CH<x>:THRESHold <NR3>
    - CH<x>:THRESHold?
    - CH<x>:VTERm:BIAS <NR3>
    - CH<x>:VTERm:BIAS?
    - CH<x>:VTERm:DUAL:A <NR3>
    - CH<x>:VTERm:DUAL:A?
    - CH<x>:VTERm:DUAL:B <NR3>
    - CH<x>:VTERm:DUAL:B?
    - CH<x>?
    ```
"""  # noqa: E501

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, ValidatedChannel

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class ChannelVtermDualB(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:VTERm:DUAL:B`` command.

    Description:
        - This command sets or queries the termination voltage for probes with dual inputs that
          support settable termination voltage.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:VTERm:DUAL:B?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:VTERm:DUAL:B?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:VTERm:DUAL:B value`` command.

    SCPI Syntax:
        ```
        - CH<x>:VTERm:DUAL:B <NR3>
        - CH<x>:VTERm:DUAL:B?
        ```

    Info:
        - ``<NR3>`` specifies the termination voltage.
    """


class ChannelVtermDualA(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:VTERm:DUAL:A`` command.

    Description:
        - This command sets or queries the termination voltage for probes with dual inputs that
          support settable termination voltage.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:VTERm:DUAL:A?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:VTERm:DUAL:A?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:VTERm:DUAL:A value`` command.

    SCPI Syntax:
        ```
        - CH<x>:VTERm:DUAL:A <NR3>
        - CH<x>:VTERm:DUAL:A?
        ```

    Info:
        - ``<NR3>`` specifies the termination voltage.
    """


class ChannelVtermDual(SCPICmdRead):
    """The ``CH<x>:VTERm:DUAL`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:VTERm:DUAL?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:VTERm:DUAL?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.a``: The ``CH<x>:VTERm:DUAL:A`` command.
        - ``.b``: The ``CH<x>:VTERm:DUAL:B`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._a = ChannelVtermDualA(device, f"{self._cmd_syntax}:A")
        self._b = ChannelVtermDualB(device, f"{self._cmd_syntax}:B")

    @property
    def a(self) -> ChannelVtermDualA:
        """Return the ``CH<x>:VTERm:DUAL:A`` command.

        Description:
            - This command sets or queries the termination voltage for probes with dual inputs that
              support settable termination voltage.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:VTERm:DUAL:A?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:VTERm:DUAL:A?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:VTERm:DUAL:A value`` command.

        SCPI Syntax:
            ```
            - CH<x>:VTERm:DUAL:A <NR3>
            - CH<x>:VTERm:DUAL:A?
            ```

        Info:
            - ``<NR3>`` specifies the termination voltage.
        """
        return self._a

    @property
    def b(self) -> ChannelVtermDualB:
        """Return the ``CH<x>:VTERm:DUAL:B`` command.

        Description:
            - This command sets or queries the termination voltage for probes with dual inputs that
              support settable termination voltage.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:VTERm:DUAL:B?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:VTERm:DUAL:B?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:VTERm:DUAL:B value`` command.

        SCPI Syntax:
            ```
            - CH<x>:VTERm:DUAL:B <NR3>
            - CH<x>:VTERm:DUAL:B?
            ```

        Info:
            - ``<NR3>`` specifies the termination voltage.
        """
        return self._b


class ChannelVtermBias(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:VTERm:BIAS`` command.

    Description:
        - Sets or queries the termination bias voltage for the specified channel (if control is
          available).

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:VTERm:BIAS?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:VTERm:BIAS?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:VTERm:BIAS value`` command.

    SCPI Syntax:
        ```
        - CH<x>:VTERm:BIAS <NR3>
        - CH<x>:VTERm:BIAS?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` is the termination voltage.
    """


class ChannelVterm(SCPICmdRead):
    """The ``CH<x>:VTERm`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:VTERm?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:VTERm?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` is the channel number.

    Properties:
        - ``.bias``: The ``CH<x>:VTERm:BIAS`` command.
        - ``.dual``: The ``CH<x>:VTERm:DUAL`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bias = ChannelVtermBias(device, f"{self._cmd_syntax}:BIAS")
        self._dual = ChannelVtermDual(device, f"{self._cmd_syntax}:DUAL")

    @property
    def bias(self) -> ChannelVtermBias:
        """Return the ``CH<x>:VTERm:BIAS`` command.

        Description:
            - Sets or queries the termination bias voltage for the specified channel (if control is
              available).

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:VTERm:BIAS?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:VTERm:BIAS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:VTERm:BIAS value`` command.

        SCPI Syntax:
            ```
            - CH<x>:VTERm:BIAS <NR3>
            - CH<x>:VTERm:BIAS?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` is the termination voltage.
        """
        return self._bias

    @property
    def dual(self) -> ChannelVtermDual:
        """Return the ``CH<x>:VTERm:DUAL`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:VTERm:DUAL?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:VTERm:DUAL?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.a``: The ``CH<x>:VTERm:DUAL:A`` command.
            - ``.b``: The ``CH<x>:VTERm:DUAL:B`` command.
        """
        return self._dual


class ChannelThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:THRESHold`` command.

    Description:
        - This command sets or queries the comparable threshold for converting the analog signal to
          digital form for the channel specified by x. The value of x can range from 1 through 4.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:THRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:THRESHold?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:THRESHold value`` command.

    SCPI Syntax:
        ```
        - CH<x>:THRESHold <NR3>
        - CH<x>:THRESHold?
        ```

    Info:
        - ``<NR3>`` specifies the analog threshold in volts.
    """


class ChannelTermination(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:TERmination`` command.

    Description:
        - This command sets or queries the vertical termination for the specified analog channel.
          The channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:TERmination?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:TERmination?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:TERmination value`` command.

    SCPI Syntax:
        ```
        - CH<x>:TERmination <NR3>
        - CH<x>:TERmination?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` specifies the channel input resistance, which can be specified as 50 Ω or
          1,000,000 Ω.
    """


class ChannelScale(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:SCAle`` command.

    Description:
        - This command sets or returns the vertical scale for the specified analog channel. The
          channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:SCAle?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:SCAle value`` command.

    SCPI Syntax:
        ```
        - CH<x>:SCAle <NR3>
        - CH<x>:SCAle?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` is the vertical scale for the specified analog channel.
    """


class ChannelProbeUnits(SCPICmdRead):
    """The ``CH<x>:PRObe:UNIts`` command.

    Description:
        - This query-only command returns a string describing the units of measure for the probe
          attached to the specified channel. The channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:UNIts?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:UNIts?
        ```
    """


class ChannelProbeTiptype(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:TIPtype`` command.

    Description:
        - This command sets or queries the type of probe tip being used on the specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:TIPtype?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:TIPtype?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:TIPtype value`` command.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:TIPtype {HBWStraightflex|OTHer}
        - CH<x>:PRObe:TIPtype?
        ```

    Info:
        - ``HBWStraightflex`` lets the instrument know you are using a high bandwidth straight-flex
          probe tip.
        - ``OTHer`` lets the instrument know you are not using a high bandwidth straight-flex probe
          tip.
    """


class ChannelProbeSignal(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:SIGnal`` command.

    Description:
        - This command sets or queries aspects of probe accessory user interfaces. The available
          arguments for this command will vary depending on the accessory you attach to the
          instrument.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:SIGnal?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:SIGnal?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:SIGnal value`` command.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:SIGnal {PASS|BYPass}
        - CH<x>:PRObe:SIGnal?
        ```

    Info:
        - ``PASS`` opens a relay passing your signal to the instrument.
        - ``BYPass`` closes a relay preventing your signal from reaching the instrument. During
          probe degauss, the signal should be bypassed.
    """


class ChannelProbeSet(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:SET`` command.

    Description:
        - This command sets or queries aspects of probe accessory user interfaces, for example probe
          attenuation factors or probe audible over range. The available arguments for this command
          will vary depending on the accessory you attach to the instrument. The channel is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:SET?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:SET?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:SET value`` command.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:SET <QString>
        - CH<x>:PRObe:SET?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<QString>`` is a quoted string representing a settable aspect of the attached accessory.
    """

    _WRAP_ARG_WITH_QUOTES = True


class ChannelProbeResistance(SCPICmdRead):
    """The ``CH<x>:PRObe:RESistance`` command.

    Description:
        - This query-only command returns the resistance of the probe that is attached to the
          specified channel. The channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:RESistance?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:RESistance?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:RESistance?
        ```
    """


class ChannelProbeRange(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:RANge`` command.

    Description:
        - This command controls or queries the attenuation range of the probe on the designated
          channel. A partial list of probes supported by this command is: P7260, P7313, P7313SMA,
          P7340A, P7360, P7360A, P7380, P7380A, P7380SMA, and P7520. response will not appear in
          ``CHX:PROBE`` or LRN query responses for channels that do not have probes that implement
          the appropriate features. This command can be sent to any channel whose 'range-selection'
          policy is Manual without regard to the kind of probe installed in that channel (an error
          results if the policy is Auto). This permits accepting previous SET or LRN query responses
          even if the attached probe is different from the one when the query was sent. The ? query
          can be sent explicitly to any channel even though these commands do not appear in a SET
          response, but the oscilloscope will reply with the string 'N/A' if the probe does not
          implement those control mechanisms.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:RANge?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:RANge?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:RANge value`` command.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:RANge <rangeName>{ATTEN1X|ATTEN1_25X|ATTEN1_5X|ATTEN1_75X|ATTEN2X| ATTEN2_5X|ATTEN3X|ATTEN3_5X|ATTEN4X|ATTEN4_5X| ATTEN5X|ATTEN5_5X|ATTEN6X|ATTEN6_5X|ATTEN7X| ATTEN7_5X|ATTEN8X|ATTEN8_5X|ATTEN9X|ATTEN9_5X| ATTEN10X|ATTEN12_5X|ATTEN15X|ATTEN17_5X|ATTEN20X| ATTEN25X|ATTEN30X|ATTEN35X|ATTEN40X|ATTEN45X| ATTEN50X|ATTEN55X|ATTEN60X|ATTEN65X|ATTEN70X| ATTEN75X|ATTEN80X|ATTEN85X|ATTEN90X|ATTEN95X| ATTEN100X|ATTEN125X|ATTEN150X|ATTEN175X|ATTEN200X| ATTEN250X|ATTEN300X|ATTEN350X|ATTEN400X|ATTEN450X| ATTEN500X|ATTEN550X|ATTEN600X|ATTEN650X|ATTEN700X| ATTEN750X|ATTEN800X|ATTEN850X|ATTEN900X|ATTEN950X| ATTEN1000X}
        - CH<x>:PRObe:RANge?
        ```
    """  # noqa: E501


class ChannelProbeInputmodeDmoffset(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:INPUTMode:DMOFFSet`` command.

    Description:
        - This command sets or queries the requested common mode differential mode offset control of
          the probe that is attached to the specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:INPUTMode:DMOFFSet?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:INPUTMode:DMOFFSet?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:INPUTMode:DMOFFSet value``
          command.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:INPUTMode:DMOFFSet <NR3>
        - CH<x>:PRObe:INPUTMode:DMOFFSet?
        ```

    Info:
        - ``<NR3>`` specifies the differential mode offset control.
    """


class ChannelProbeInputmodeCmoffset(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:INPUTMode:CMOFFSet`` command.

    Description:
        - This command sets or queries the requested common mode offset control of the probe that is
          attached to the specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:INPUTMode:CMOFFSet?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:INPUTMode:CMOFFSet?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:INPUTMode:CMOFFSet value``
          command.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:INPUTMode:CMOFFSet <NR3>
        - CH<x>:PRObe:INPUTMode:CMOFFSet?
        ```

    Info:
        - ``<NR3>`` specifies the common mode offset control.
    """


class ChannelProbeInputmodeBoffset(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:INPUTMode:BOFFSet`` command.

    Description:
        - Sets or queries the B mode offset control of the probe that is attached to the specified
          channel.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:INPUTMode:BOFFSet?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:INPUTMode:BOFFSet?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:INPUTMode:BOFFSet value``
          command.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:INPUTMode:BOFFSet <NR3>
        - CH<x>:PRObe:INPUTMode:BOFFSet?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` sets the B mode offset value, in vertical units (V or A).
    """


class ChannelProbeInputmodeAoffset(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:INPUTMode:AOFFSet`` command.

    Description:
        - Sets or queries the A mode offset control of the probe that is attached to the specified
          channel.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:INPUTMode:AOFFSet?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:INPUTMode:AOFFSet?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:INPUTMode:AOFFSet value``
          command.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:INPUTMode:AOFFSet <NR3>
        - CH<x>:PRObe:INPUTMode:AOFFSet?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` sets the A mode offset value, in vertical units (V or A).
    """


class ChannelProbeInputmode(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:INPUTMode`` command.

    Description:
        - This command sets or queries the input mode of the probe that is attached to the specified
          channel.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:INPUTMode?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:INPUTMode?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:INPUTMode value`` command.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:INPUTMode {DEFault|DIFFerential|COMmonmode|A|B}
        - CH<x>:PRObe:INPUTMode?
        ```

    Info:
        - ``DEFault`` sets to the default.
        - ``DIFFerential`` sets the probe to route differential signals to the host.
        - ``COMmonmode`` sets the probe to route common-mode signals to the host.
        - ``A`` sets the probe to route single-ended A signals to the host.
        - ``B`` sets the probe to route single-ended B signals to the host.

    Properties:
        - ``.aoffset``: The ``CH<x>:PRObe:INPUTMode:AOFFSet`` command.
        - ``.boffset``: The ``CH<x>:PRObe:INPUTMode:BOFFSet`` command.
        - ``.cmoffset``: The ``CH<x>:PRObe:INPUTMode:CMOFFSet`` command.
        - ``.dmoffset``: The ``CH<x>:PRObe:INPUTMode:DMOFFSet`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._aoffset = ChannelProbeInputmodeAoffset(device, f"{self._cmd_syntax}:AOFFSet")
        self._boffset = ChannelProbeInputmodeBoffset(device, f"{self._cmd_syntax}:BOFFSet")
        self._cmoffset = ChannelProbeInputmodeCmoffset(device, f"{self._cmd_syntax}:CMOFFSet")
        self._dmoffset = ChannelProbeInputmodeDmoffset(device, f"{self._cmd_syntax}:DMOFFSet")

    @property
    def aoffset(self) -> ChannelProbeInputmodeAoffset:
        """Return the ``CH<x>:PRObe:INPUTMode:AOFFSet`` command.

        Description:
            - Sets or queries the A mode offset control of the probe that is attached to the
              specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:INPUTMode:AOFFSet?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:INPUTMode:AOFFSet?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CH<x>:PRObe:INPUTMode:AOFFSet value`` command.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:INPUTMode:AOFFSet <NR3>
            - CH<x>:PRObe:INPUTMode:AOFFSet?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` sets the A mode offset value, in vertical units (V or A).
        """
        return self._aoffset

    @property
    def boffset(self) -> ChannelProbeInputmodeBoffset:
        """Return the ``CH<x>:PRObe:INPUTMode:BOFFSet`` command.

        Description:
            - Sets or queries the B mode offset control of the probe that is attached to the
              specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:INPUTMode:BOFFSet?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:INPUTMode:BOFFSet?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CH<x>:PRObe:INPUTMode:BOFFSet value`` command.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:INPUTMode:BOFFSet <NR3>
            - CH<x>:PRObe:INPUTMode:BOFFSet?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` sets the B mode offset value, in vertical units (V or A).
        """
        return self._boffset

    @property
    def cmoffset(self) -> ChannelProbeInputmodeCmoffset:
        """Return the ``CH<x>:PRObe:INPUTMode:CMOFFSet`` command.

        Description:
            - This command sets or queries the requested common mode offset control of the probe
              that is attached to the specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:INPUTMode:CMOFFSet?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:INPUTMode:CMOFFSet?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CH<x>:PRObe:INPUTMode:CMOFFSet value`` command.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:INPUTMode:CMOFFSet <NR3>
            - CH<x>:PRObe:INPUTMode:CMOFFSet?
            ```

        Info:
            - ``<NR3>`` specifies the common mode offset control.
        """
        return self._cmoffset

    @property
    def dmoffset(self) -> ChannelProbeInputmodeDmoffset:
        """Return the ``CH<x>:PRObe:INPUTMode:DMOFFSet`` command.

        Description:
            - This command sets or queries the requested common mode differential mode offset
              control of the probe that is attached to the specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:INPUTMode:DMOFFSet?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:INPUTMode:DMOFFSet?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CH<x>:PRObe:INPUTMode:DMOFFSet value`` command.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:INPUTMode:DMOFFSet <NR3>
            - CH<x>:PRObe:INPUTMode:DMOFFSet?
            ```

        Info:
            - ``<NR3>`` specifies the differential mode offset control.
        """
        return self._dmoffset


class ChannelProbeIdType(SCPICmdRead):
    """The ``CH<x>:PRObe:ID:TYPe`` command.

    Description:
        - This query-only command returns the type of probe that is attached to the specified
          channel. The channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:ID:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:ID:TYPe?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:ID:TYPe?
        ```
    """


class ChannelProbeIdSernumber(SCPICmdRead):
    """The ``CH<x>:PRObe:ID:SERnumber`` command.

    Description:
        - This query-only command returns the serial number of the probe that is attached to the
          specified channel. The channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:ID:SERnumber?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:ID:SERnumber?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:ID:SERnumber?
        ```
    """


class ChannelProbeId(SCPICmdRead):
    """The ``CH<x>:PRObe:ID`` command.

    Description:
        - This query-only command returns the type and serial number of the probe that is attached
          to the specified channel. The channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:ID?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:ID?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:ID?
        ```

    Properties:
        - ``.sernumber``: The ``CH<x>:PRObe:ID:SERnumber`` command.
        - ``.type``: The ``CH<x>:PRObe:ID:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._sernumber = ChannelProbeIdSernumber(device, f"{self._cmd_syntax}:SERnumber")
        self._type = ChannelProbeIdType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def sernumber(self) -> ChannelProbeIdSernumber:
        """Return the ``CH<x>:PRObe:ID:SERnumber`` command.

        Description:
            - This query-only command returns the serial number of the probe that is attached to the
              specified channel. The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:ID:SERnumber?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:ID:SERnumber?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:ID:SERnumber?
            ```
        """
        return self._sernumber

    @property
    def type(self) -> ChannelProbeIdType:
        """Return the ``CH<x>:PRObe:ID:TYPe`` command.

        Description:
            - This query-only command returns the type of probe that is attached to the specified
              channel. The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:ID:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:ID:TYPe?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:ID:TYPe?
            ```
        """
        return self._type


class ChannelProbeGain(SCPICmdRead):
    """The ``CH<x>:PRObe:GAIN`` command.

    Description:
        - This query-only command returns the gain factor of the probe that is attached to the
          specified channel. The channel is specified by x. The gain of a probe is the output
          divided by the input transfer ratio. For example, a common 10x probe has a gain of 0.1.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:GAIN?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:GAIN?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:GAIN?
        ```
    """


class ChannelProbeForcedrange(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:FORCEDRange`` command.

    Description:
        - This command sets the attached probe to the specified range, or it queries the range of
          the probe attached to the specified channel. The channel is specified by x. The value of x
          can range from 1 through 4. A partial list of probes supported by this command includes
          the following probes: TCP0001, TCP0030, TCP0150, TDP0500, TDP1000, and TDP1500. response
          will not appear in ``CHX:PROBE`` or LRN query responses for channels that do not have
          probes that implement the appropriate features. This command can be sent to any channel
          whose 'range-selection' policy is Manual without regard to the kind of probe installed in
          that channel (an error results if the policy is Auto). This permits accepting previous SET
          or LRN query responses even if the attached probe is different from the one when the query
          was sent. The ? query can be sent explicitly to any channel even though these commands do
          not appear in a 'SET' response, but the oscilloscope will reply with the string 'N/A' if
          the probe does not implement those control mechanisms.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:FORCEDRange?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:FORCEDRange?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:FORCEDRange value``
          command.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:FORCEDRange <dynamicRangeNR3>
        - CH<x>:PRObe:FORCEDRange?
        ```

    Info:
        - ``<dynamicRangeNR3>`` specifies the probe range.
    """


class ChannelProbeDegaussState(SCPICmdRead):
    """The ``CH<x>:PRObe:DEGAUSS:STATE`` command.

    Description:
        - This command queries whether the probe attached to the specified channel requires a
          degauss operation. The channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:DEGAUSS:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:DEGAUSS:STATE?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:DEGAUSS:STATE?
        ```
    """


class ChannelProbeDegauss(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:DEGAUSS`` command.

    Description:
        - This command starts a degauss cycle of the TekVPI probe attached to the specified channel.
          The channel is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:DEGAUSS value`` command.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:DEGAUSS EXECute
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``EXECute`` starts the degauss cycle.

    Properties:
        - ``.state``: The ``CH<x>:PRObe:DEGAUSS:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ChannelProbeDegaussState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ChannelProbeDegaussState:
        """Return the ``CH<x>:PRObe:DEGAUSS:STATE`` command.

        Description:
            - This command queries whether the probe attached to the specified channel requires a
              degauss operation. The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:DEGAUSS:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:DEGAUSS:STATE?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:DEGAUSS:STATE?
            ```
        """
        return self._state


class ChannelProbeDcCalibrationLastTime(SCPICmdRead):
    """The ``CH<x>:PRObe:DC:CALibration:LAST:TIME`` command.

    Description:
        - Returns the date and time of the last calibration on the specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:DC:CALibration:LAST:TIME?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``CH<x>:PRObe:DC:CALibration:LAST:TIME?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:DC:CALibration:LAST:TIME?
        ```
    """


class ChannelProbeDcCalibrationLastHardware(SCPICmdRead):
    """The ``CH<x>:PRObe:DC:CALibration:LAST:HARDware`` command.

    Description:
        - Returns the probe and tip type and associated serial numbers with the last calibration on
          the specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:DC:CALibration:LAST:HARDware?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``CH<x>:PRObe:DC:CALibration:LAST:HARDware?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:DC:CALibration:LAST:HARDware?
        ```
    """


class ChannelProbeDcCalibrationLast(SCPICmdRead):
    """The ``CH<x>:PRObe:DC:CALibration:LAST`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:DC:CALibration:LAST?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:DC:CALibration:LAST?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.hardware``: The ``CH<x>:PRObe:DC:CALibration:LAST:HARDware`` command.
        - ``.time``: The ``CH<x>:PRObe:DC:CALibration:LAST:TIME`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hardware = ChannelProbeDcCalibrationLastHardware(
            device, f"{self._cmd_syntax}:HARDware"
        )
        self._time = ChannelProbeDcCalibrationLastTime(device, f"{self._cmd_syntax}:TIME")

    @property
    def hardware(self) -> ChannelProbeDcCalibrationLastHardware:
        """Return the ``CH<x>:PRObe:DC:CALibration:LAST:HARDware`` command.

        Description:
            - Returns the probe and tip type and associated serial numbers with the last calibration
              on the specified channel.

        Usage:
            - Using the ``.query()`` method will send the
              ``CH<x>:PRObe:DC:CALibration:LAST:HARDware?`` query.
            - Using the ``.verify(value)`` method will send the
              ``CH<x>:PRObe:DC:CALibration:LAST:HARDware?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:DC:CALibration:LAST:HARDware?
            ```
        """
        return self._hardware

    @property
    def time(self) -> ChannelProbeDcCalibrationLastTime:
        """Return the ``CH<x>:PRObe:DC:CALibration:LAST:TIME`` command.

        Description:
            - Returns the date and time of the last calibration on the specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:DC:CALibration:LAST:TIME?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CH<x>:PRObe:DC:CALibration:LAST:TIME?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:DC:CALibration:LAST:TIME?
            ```
        """
        return self._time


class ChannelProbeDcCalibration(SCPICmdRead):
    """The ``CH<x>:PRObe:DC:CALibration`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:DC:CALibration?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:DC:CALibration?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.last``: The ``CH<x>:PRObe:DC:CALibration:LAST`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._last = ChannelProbeDcCalibrationLast(device, f"{self._cmd_syntax}:LAST")

    @property
    def last(self) -> ChannelProbeDcCalibrationLast:
        """Return the ``CH<x>:PRObe:DC:CALibration:LAST`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:DC:CALibration:LAST?``
              query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:DC:CALibration:LAST?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.hardware``: The ``CH<x>:PRObe:DC:CALibration:LAST:HARDware`` command.
            - ``.time``: The ``CH<x>:PRObe:DC:CALibration:LAST:TIME`` command.
        """
        return self._last


class ChannelProbeDc(SCPICmdRead):
    """The ``CH<x>:PRObe:DC`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:DC?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:DC?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.calibration``: The ``CH<x>:PRObe:DC:CALibration`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._calibration = ChannelProbeDcCalibration(device, f"{self._cmd_syntax}:CALibration")

    @property
    def calibration(self) -> ChannelProbeDcCalibration:
        """Return the ``CH<x>:PRObe:DC:CALibration`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:DC:CALibration?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:DC:CALibration?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.last``: The ``CH<x>:PRObe:DC:CALibration:LAST`` command tree.
        """
        return self._calibration


class ChannelProbeAutozero(SCPICmdWrite):
    """The ``CH<x>:PRObe:AUTOZero`` command.

    Description:
        - This command executes the attached probe's Auto Zero function, for probes that support
          this feature. See your probe documentation for more details. The channel is specified by
          x.

    Usage:
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:AUTOZero value`` command.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:AUTOZero EXECute
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``EXECute`` sets the probe attached to the specified channel to autozero.
    """


#  pylint: disable=too-many-instance-attributes
class ChannelProbe(SCPICmdRead):
    """The ``CH<x>:PRObe`` command.

    Description:
        - This query-only command returns all information concerning the probe that is attached to
          the specified channel. The channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:PRObe?
        ```

    Properties:
        - ``.autozero``: The ``CH<x>:PRObe:AUTOZero`` command.
        - ``.dc``: The ``CH<x>:PRObe:DC`` command tree.
        - ``.degauss``: The ``CH<x>:PRObe:DEGAUSS`` command.
        - ``.forcedrange``: The ``CH<x>:PRObe:FORCEDRange`` command.
        - ``.gain``: The ``CH<x>:PRObe:GAIN`` command.
        - ``.id``: The ``CH<x>:PRObe:ID`` command.
        - ``.inputmode``: The ``CH<x>:PRObe:INPUTMode`` command.
        - ``.range``: The ``CH<x>:PRObe:RANge`` command.
        - ``.resistance``: The ``CH<x>:PRObe:RESistance`` command.
        - ``.set``: The ``CH<x>:PRObe:SET`` command.
        - ``.signal``: The ``CH<x>:PRObe:SIGnal`` command.
        - ``.tiptype``: The ``CH<x>:PRObe:TIPtype`` command.
        - ``.units``: The ``CH<x>:PRObe:UNIts`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autozero = ChannelProbeAutozero(device, f"{self._cmd_syntax}:AUTOZero")
        self._dc = ChannelProbeDc(device, f"{self._cmd_syntax}:DC")
        self._degauss = ChannelProbeDegauss(device, f"{self._cmd_syntax}:DEGAUSS")
        self._forcedrange = ChannelProbeForcedrange(device, f"{self._cmd_syntax}:FORCEDRange")
        self._gain = ChannelProbeGain(device, f"{self._cmd_syntax}:GAIN")
        self._id = ChannelProbeId(device, f"{self._cmd_syntax}:ID")
        self._inputmode = ChannelProbeInputmode(device, f"{self._cmd_syntax}:INPUTMode")
        self._range = ChannelProbeRange(device, f"{self._cmd_syntax}:RANge")
        self._resistance = ChannelProbeResistance(device, f"{self._cmd_syntax}:RESistance")
        self._set = ChannelProbeSet(device, f"{self._cmd_syntax}:SET")
        self._signal = ChannelProbeSignal(device, f"{self._cmd_syntax}:SIGnal")
        self._tiptype = ChannelProbeTiptype(device, f"{self._cmd_syntax}:TIPtype")
        self._units = ChannelProbeUnits(device, f"{self._cmd_syntax}:UNIts")

    @property
    def autozero(self) -> ChannelProbeAutozero:
        """Return the ``CH<x>:PRObe:AUTOZero`` command.

        Description:
            - This command executes the attached probe's Auto Zero function, for probes that support
              this feature. See your probe documentation for more details. The channel is specified
              by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:AUTOZero value``
              command.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:AUTOZero EXECute
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``EXECute`` sets the probe attached to the specified channel to autozero.
        """
        return self._autozero

    @property
    def dc(self) -> ChannelProbeDc:
        """Return the ``CH<x>:PRObe:DC`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:DC?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:DC?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.calibration``: The ``CH<x>:PRObe:DC:CALibration`` command tree.
        """
        return self._dc

    @property
    def degauss(self) -> ChannelProbeDegauss:
        """Return the ``CH<x>:PRObe:DEGAUSS`` command.

        Description:
            - This command starts a degauss cycle of the TekVPI probe attached to the specified
              channel. The channel is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:DEGAUSS value``
              command.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:DEGAUSS EXECute
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``EXECute`` starts the degauss cycle.

        Sub-properties:
            - ``.state``: The ``CH<x>:PRObe:DEGAUSS:STATE`` command.
        """
        return self._degauss

    @property
    def forcedrange(self) -> ChannelProbeForcedrange:
        """Return the ``CH<x>:PRObe:FORCEDRange`` command.

        Description:
            - This command sets the attached probe to the specified range, or it queries the range
              of the probe attached to the specified channel. The channel is specified by x. The
              value of x can range from 1 through 4. A partial list of probes supported by this
              command includes the following probes: TCP0001, TCP0030, TCP0150, TDP0500, TDP1000,
              and TDP1500. response will not appear in ``CHX:PROBE`` or LRN query responses for
              channels that do not have probes that implement the appropriate features. This command
              can be sent to any channel whose 'range-selection' policy is Manual without regard to
              the kind of probe installed in that channel (an error results if the policy is Auto).
              This permits accepting previous SET or LRN query responses even if the attached probe
              is different from the one when the query was sent. The ? query can be sent explicitly
              to any channel even though these commands do not appear in a 'SET' response, but the
              oscilloscope will reply with the string 'N/A' if the probe does not implement those
              control mechanisms.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:FORCEDRange?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:FORCEDRange?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:FORCEDRange value``
              command.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:FORCEDRange <dynamicRangeNR3>
            - CH<x>:PRObe:FORCEDRange?
            ```

        Info:
            - ``<dynamicRangeNR3>`` specifies the probe range.
        """
        return self._forcedrange

    @property
    def gain(self) -> ChannelProbeGain:
        """Return the ``CH<x>:PRObe:GAIN`` command.

        Description:
            - This query-only command returns the gain factor of the probe that is attached to the
              specified channel. The channel is specified by x. The gain of a probe is the output
              divided by the input transfer ratio. For example, a common 10x probe has a gain of
              0.1.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:GAIN?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:GAIN?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:GAIN?
            ```
        """
        return self._gain

    @property
    def id(self) -> ChannelProbeId:
        """Return the ``CH<x>:PRObe:ID`` command.

        Description:
            - This query-only command returns the type and serial number of the probe that is
              attached to the specified channel. The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:ID?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:ID?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:ID?
            ```

        Sub-properties:
            - ``.sernumber``: The ``CH<x>:PRObe:ID:SERnumber`` command.
            - ``.type``: The ``CH<x>:PRObe:ID:TYPe`` command.
        """
        return self._id

    @property
    def inputmode(self) -> ChannelProbeInputmode:
        """Return the ``CH<x>:PRObe:INPUTMode`` command.

        Description:
            - This command sets or queries the input mode of the probe that is attached to the
              specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:INPUTMode?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:INPUTMode?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:INPUTMode value``
              command.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:INPUTMode {DEFault|DIFFerential|COMmonmode|A|B}
            - CH<x>:PRObe:INPUTMode?
            ```

        Info:
            - ``DEFault`` sets to the default.
            - ``DIFFerential`` sets the probe to route differential signals to the host.
            - ``COMmonmode`` sets the probe to route common-mode signals to the host.
            - ``A`` sets the probe to route single-ended A signals to the host.
            - ``B`` sets the probe to route single-ended B signals to the host.

        Sub-properties:
            - ``.aoffset``: The ``CH<x>:PRObe:INPUTMode:AOFFSet`` command.
            - ``.boffset``: The ``CH<x>:PRObe:INPUTMode:BOFFSet`` command.
            - ``.cmoffset``: The ``CH<x>:PRObe:INPUTMode:CMOFFSet`` command.
            - ``.dmoffset``: The ``CH<x>:PRObe:INPUTMode:DMOFFSet`` command.
        """
        return self._inputmode

    @property
    def range(self) -> ChannelProbeRange:
        """Return the ``CH<x>:PRObe:RANge`` command.

        Description:
            - This command controls or queries the attenuation range of the probe on the designated
              channel. A partial list of probes supported by this command is: P7260, P7313,
              P7313SMA, P7340A, P7360, P7360A, P7380, P7380A, P7380SMA, and P7520. response will not
              appear in ``CHX:PROBE`` or LRN query responses for channels that do not have probes
              that implement the appropriate features. This command can be sent to any channel whose
              'range-selection' policy is Manual without regard to the kind of probe installed in
              that channel (an error results if the policy is Auto). This permits accepting previous
              SET or LRN query responses even if the attached probe is different from the one when
              the query was sent. The ? query can be sent explicitly to any channel even though
              these commands do not appear in a SET response, but the oscilloscope will reply with
              the string 'N/A' if the probe does not implement those control mechanisms.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:RANge?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:RANge?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:RANge value`` command.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:RANge <rangeName>{ATTEN1X|ATTEN1_25X|ATTEN1_5X|ATTEN1_75X|ATTEN2X| ATTEN2_5X|ATTEN3X|ATTEN3_5X|ATTEN4X|ATTEN4_5X| ATTEN5X|ATTEN5_5X|ATTEN6X|ATTEN6_5X|ATTEN7X| ATTEN7_5X|ATTEN8X|ATTEN8_5X|ATTEN9X|ATTEN9_5X| ATTEN10X|ATTEN12_5X|ATTEN15X|ATTEN17_5X|ATTEN20X| ATTEN25X|ATTEN30X|ATTEN35X|ATTEN40X|ATTEN45X| ATTEN50X|ATTEN55X|ATTEN60X|ATTEN65X|ATTEN70X| ATTEN75X|ATTEN80X|ATTEN85X|ATTEN90X|ATTEN95X| ATTEN100X|ATTEN125X|ATTEN150X|ATTEN175X|ATTEN200X| ATTEN250X|ATTEN300X|ATTEN350X|ATTEN400X|ATTEN450X| ATTEN500X|ATTEN550X|ATTEN600X|ATTEN650X|ATTEN700X| ATTEN750X|ATTEN800X|ATTEN850X|ATTEN900X|ATTEN950X| ATTEN1000X}
            - CH<x>:PRObe:RANge?
            ```
        """  # noqa: E501
        return self._range

    @property
    def resistance(self) -> ChannelProbeResistance:
        """Return the ``CH<x>:PRObe:RESistance`` command.

        Description:
            - This query-only command returns the resistance of the probe that is attached to the
              specified channel. The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:RESistance?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:RESistance?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:RESistance?
            ```
        """
        return self._resistance

    @property
    def set_(self) -> ChannelProbeSet:
        """Return the ``CH<x>:PRObe:SET`` command.

        Description:
            - This command sets or queries aspects of probe accessory user interfaces, for example
              probe attenuation factors or probe audible over range. The available arguments for
              this command will vary depending on the accessory you attach to the instrument. The
              channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:SET?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:SET?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:SET value`` command.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:SET <QString>
            - CH<x>:PRObe:SET?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<QString>`` is a quoted string representing a settable aspect of the attached
              accessory.
        """
        return self._set

    @property
    def signal(self) -> ChannelProbeSignal:
        """Return the ``CH<x>:PRObe:SIGnal`` command.

        Description:
            - This command sets or queries aspects of probe accessory user interfaces. The available
              arguments for this command will vary depending on the accessory you attach to the
              instrument.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:SIGnal?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:SIGnal?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:SIGnal value`` command.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:SIGnal {PASS|BYPass}
            - CH<x>:PRObe:SIGnal?
            ```

        Info:
            - ``PASS`` opens a relay passing your signal to the instrument.
            - ``BYPass`` closes a relay preventing your signal from reaching the instrument. During
              probe degauss, the signal should be bypassed.
        """
        return self._signal

    @property
    def tiptype(self) -> ChannelProbeTiptype:
        """Return the ``CH<x>:PRObe:TIPtype`` command.

        Description:
            - This command sets or queries the type of probe tip being used on the specified
              channel.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:TIPtype?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:TIPtype?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:TIPtype value``
              command.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:TIPtype {HBWStraightflex|OTHer}
            - CH<x>:PRObe:TIPtype?
            ```

        Info:
            - ``HBWStraightflex`` lets the instrument know you are using a high bandwidth
              straight-flex probe tip.
            - ``OTHer`` lets the instrument know you are not using a high bandwidth straight-flex
              probe tip.
        """
        return self._tiptype

    @property
    def units(self) -> ChannelProbeUnits:
        """Return the ``CH<x>:PRObe:UNIts`` command.

        Description:
            - This query-only command returns a string describing the units of measure for the probe
              attached to the specified channel. The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:UNIts?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:UNIts?
            ```
        """
        return self._units


class ChannelProbefuncExtunits(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PROBEFunc:EXTUnits`` command.

    Description:
        - This command sets the unit of measurement for the external attenuator of the specified
          channel. The channel is specified by x. The alternate units are used if they are enabled.
          Use the ``CHX:PROBEFUNC:EXTUNITS:STATE`` command to enable or disable the alternate units.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PROBEFunc:EXTUnits?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PROBEFunc:EXTUnits?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PROBEFunc:EXTUnits value``
          command.

    SCPI Syntax:
        ```
        - CH<x>:PROBEFunc:EXTUnits <QString>
        - CH<x>:PROBEFunc:EXTUnits?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<QString>`` indicates the attenuation unit of measurement for the specified channel.
    """

    _WRAP_ARG_WITH_QUOTES = True


class ChannelProbefuncExtdbatten(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PROBEFunc:EXTDBatten`` command.

    Description:
        - This command sets or queries the input-output ratio (expressed in decibel units) of
          external attenuation or gain between the signal and the instrument input channels. The
          channel is specified by x. The query form of this command returns the user-specified
          attenuation in decibels.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PROBEFunc:EXTDBatten?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PROBEFunc:EXTDBatten?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PROBEFunc:EXTDBatten value``
          command.

    SCPI Syntax:
        ```
        - CH<x>:PROBEFunc:EXTDBatten <NR3>
        - CH<x>:PROBEFunc:EXTDBatten?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` is the attenuation value, which is specified in the range from -200.00 dB to
          200.00 dB.
    """


class ChannelProbefuncExtatten(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PROBEFunc:EXTAtten`` command.

    Description:
        - This command is used to specify the attenuation value as a multiplier to the given scale
          factor on the specified channel. The channel is specified by x. The query form of this
          command returns the user-specified attenuation.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PROBEFunc:EXTAtten?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PROBEFunc:EXTAtten?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PROBEFunc:EXTAtten value``
          command.

    SCPI Syntax:
        ```
        - CH<x>:PROBEFunc:EXTAtten <NR3>
        - CH<x>:PROBEFunc:EXTAtten?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` is the attenuation value, which is specified as a multiplier in the range from
          1.00E-10 to 1.00E+10.
    """


class ChannelProbefunc(SCPICmdRead):
    """The ``CH<x>:PROBEFunc`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PROBEFunc?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PROBEFunc?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` is the channel number.

    Properties:
        - ``.extatten``: The ``CH<x>:PROBEFunc:EXTAtten`` command.
        - ``.extdbatten``: The ``CH<x>:PROBEFunc:EXTDBatten`` command.
        - ``.extunits``: The ``CH<x>:PROBEFunc:EXTUnits`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._extatten = ChannelProbefuncExtatten(device, f"{self._cmd_syntax}:EXTAtten")
        self._extdbatten = ChannelProbefuncExtdbatten(device, f"{self._cmd_syntax}:EXTDBatten")
        self._extunits = ChannelProbefuncExtunits(device, f"{self._cmd_syntax}:EXTUnits")

    @property
    def extatten(self) -> ChannelProbefuncExtatten:
        """Return the ``CH<x>:PROBEFunc:EXTAtten`` command.

        Description:
            - This command is used to specify the attenuation value as a multiplier to the given
              scale factor on the specified channel. The channel is specified by x. The query form
              of this command returns the user-specified attenuation.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PROBEFunc:EXTAtten?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PROBEFunc:EXTAtten?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:PROBEFunc:EXTAtten value``
              command.

        SCPI Syntax:
            ```
            - CH<x>:PROBEFunc:EXTAtten <NR3>
            - CH<x>:PROBEFunc:EXTAtten?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` is the attenuation value, which is specified as a multiplier in the range
              from 1.00E-10 to 1.00E+10.
        """
        return self._extatten

    @property
    def extdbatten(self) -> ChannelProbefuncExtdbatten:
        """Return the ``CH<x>:PROBEFunc:EXTDBatten`` command.

        Description:
            - This command sets or queries the input-output ratio (expressed in decibel units) of
              external attenuation or gain between the signal and the instrument input channels. The
              channel is specified by x. The query form of this command returns the user-specified
              attenuation in decibels.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PROBEFunc:EXTDBatten?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PROBEFunc:EXTDBatten?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:PROBEFunc:EXTDBatten value``
              command.

        SCPI Syntax:
            ```
            - CH<x>:PROBEFunc:EXTDBatten <NR3>
            - CH<x>:PROBEFunc:EXTDBatten?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` is the attenuation value, which is specified in the range from -200.00 dB to
              200.00 dB.
        """
        return self._extdbatten

    @property
    def extunits(self) -> ChannelProbefuncExtunits:
        """Return the ``CH<x>:PROBEFunc:EXTUnits`` command.

        Description:
            - This command sets the unit of measurement for the external attenuator of the specified
              channel. The channel is specified by x. The alternate units are used if they are
              enabled. Use the ``CHX:PROBEFUNC:EXTUNITS:STATE`` command to enable or disable the
              alternate units.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PROBEFunc:EXTUnits?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PROBEFunc:EXTUnits?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:PROBEFunc:EXTUnits value``
              command.

        SCPI Syntax:
            ```
            - CH<x>:PROBEFunc:EXTUnits <QString>
            - CH<x>:PROBEFunc:EXTUnits?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<QString>`` indicates the attenuation unit of measurement for the specified channel.
        """
        return self._extunits


class ChannelProbecal(SCPICmdRead):
    """The ``CH<x>:PROBECal`` command.

    Description:
        - This query-only command returns the probe calibration state for the specified channel. The
          channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PROBECal?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PROBECal?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:PROBECal?
        ```
    """


class ChannelProbecontrol(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PROBECOntrol`` command.

    Description:
        - This command sets or queries multirange probe range-control policy preference of the probe
          that is attached to CH<x>. The channel number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PROBECOntrol?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PROBECOntrol?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PROBECOntrol value`` command.

    SCPI Syntax:
        ```
        - CH<x>:PROBECOntrol {AUTO|MANual}
        - CH<x>:PROBECOntrol?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``AUTO`` sets the values. The probe range is automatically calculated.
        - ``MANual`` allows you to select various valid values for the probe connected to a
          particular channel.
    """


class ChannelPosition(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:POSition`` command.

    Description:
        - This command specifies the vertical position of channel <x>, where x is the channel number
          (1-4). The position value is applied to the signal before it is digitized. Increasing the
          position value of a waveform causes the waveform to move up. Decreasing the position value
          causes the waveform to move down. The position value determines the vertical graticule
          coordinate at which input signal values, minus the present offset setting for that
          channel, are displayed. For example, if the position for Channel 3 is set to 2.0 and the
          offset is set to 3.0, then input signals equal to 3.0 units are displayed 2.0 divisions
          above the center of the screen (at 1 V/div).

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:POSition?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:POSition value`` command.

    SCPI Syntax:
        ```
        - CH<x>:POSition <NR3>
        - CH<x>:POSition?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the position value for channel <x>, in
          divisions, from the center graticule. The range is 8 to -8 divisions.
    """


class ChannelOpticalWlengthList(SCPICmdRead):
    """The ``CH<x>:OPTIcal:WLENgth:LIST`` command.

    Description:
        - Query returns the comma-separated list of wavelengths with calibrated responses from the
          Probe. The units for the returned values are in nanometers.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:OPTIcal:WLENgth:LIST?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:OPTIcal:WLENgth:LIST?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:OPTIcal:WLENgth:LIST?
        ```
    """


class ChannelOpticalWlength(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:OPTIcal:WLENgth`` command.

    Description:
        - Get or set the optical wavelength (in nanometers) that is used by the Probe and
          oscilloscope to compensate for the applied optical signal. Use the optional second
          argument to specify whether the to recall the factory calibration values or the
          user-programmed calibration values.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:OPTIcal:WLENgth?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:OPTIcal:WLENgth?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:OPTIcal:WLENgth value`` command.

    SCPI Syntax:
        ```
        - CH<x>:OPTIcal:WLENgth <NR1> [, USER|, FACTory]
        - CH<x>:OPTIcal:WLENgth?
        ```

    Info:
        - ``<NR1>`` is the optical wavelength (in nanometers).
        - ``USER`` specifies user-programmed calibration values that can be loaded onto the probe
          through a separate utility.
        - ``FACTory`` specifies using factory calibration values. The second argument defaults to
          FACTory if none is specified.

    Properties:
        - ``.list``: The ``CH<x>:OPTIcal:WLENgth:LIST`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._list = ChannelOpticalWlengthList(device, f"{self._cmd_syntax}:LIST")

    @property
    def list(self) -> ChannelOpticalWlengthList:
        """Return the ``CH<x>:OPTIcal:WLENgth:LIST`` command.

        Description:
            - Query returns the comma-separated list of wavelengths with calibrated responses from
              the Probe. The units for the returned values are in nanometers.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:OPTIcal:WLENgth:LIST?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:OPTIcal:WLENgth:LIST?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:OPTIcal:WLENgth:LIST?
            ```
        """
        return self._list


class ChannelOpticalRcvrUservalue(SCPICmdRead):
    """The ``CH<x>:OPTIcal:RCVR:USERVALue`` command.

    Description:
        - This command queries the Baud rate for the user-specified Optical Reference Receiver (ORR)
          filter.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:OPTIcal:RCVR:USERVALue?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:OPTIcal:RCVR:USERVALue?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:OPTIcal:RCVR:USERVALue?
        ```
    """


class ChannelOpticalRcvr(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:OPTIcal:RCVR`` command.

    Description:
        - This command sets or queries the Optical Reference Receiver (ORR) DSP filter used to
          compensate for the applied optical signal. Using the USER value requires the optional,
          numeric second argument. The units for <NR1> are in Baud. 28.6 GigaBaud example:
          ``:CH1:OPTI:RCVR USER``, 28.6E9.

    Usage:
        - Using the ``.write(value)`` method will send the ``CH<x>:OPTIcal:RCVR value`` command.

    SCPI Syntax:
        ```
        - CH<x>:OPTIcal:RCVR {OFF|FLAT|FLAT33|ENET257R4|ENET266PAM4| OTU2795|FC28050|USER} [,<NR1>]
        ```

    Properties:
        - ``.uservalue``: The ``CH<x>:OPTIcal:RCVR:USERVALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._uservalue = ChannelOpticalRcvrUservalue(device, f"{self._cmd_syntax}:USERVALue")

    @property
    def uservalue(self) -> ChannelOpticalRcvrUservalue:
        """Return the ``CH<x>:OPTIcal:RCVR:USERVALue`` command.

        Description:
            - This command queries the Baud rate for the user-specified Optical Reference Receiver
              (ORR) filter.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:OPTIcal:RCVR:USERVALue?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:OPTIcal:RCVR:USERVALue?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:OPTIcal:RCVR:USERVALue?
            ```
        """
        return self._uservalue


class ChannelOptical(SCPICmdRead):
    """The ``CH<x>:OPTIcal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:OPTIcal?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:OPTIcal?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.rcvr``: The ``CH<x>:OPTIcal:RCVR`` command.
        - ``.wlength``: The ``CH<x>:OPTIcal:WLENgth`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._rcvr = ChannelOpticalRcvr(device, f"{self._cmd_syntax}:RCVR")
        self._wlength = ChannelOpticalWlength(device, f"{self._cmd_syntax}:WLENgth")

    @property
    def rcvr(self) -> ChannelOpticalRcvr:
        """Return the ``CH<x>:OPTIcal:RCVR`` command.

        Description:
            - This command sets or queries the Optical Reference Receiver (ORR) DSP filter used to
              compensate for the applied optical signal. Using the USER value requires the optional,
              numeric second argument. The units for <NR1> are in Baud. 28.6 GigaBaud example:
              ``:CH1:OPTI:RCVR USER``, 28.6E9.

        Usage:
            - Using the ``.write(value)`` method will send the ``CH<x>:OPTIcal:RCVR value`` command.

        SCPI Syntax:
            ```
            - CH<x>:OPTIcal:RCVR {OFF|FLAT|FLAT33|ENET257R4|ENET266PAM4| OTU2795|FC28050|USER} [,<NR1>]
            ```

        Sub-properties:
            - ``.uservalue``: The ``CH<x>:OPTIcal:RCVR:USERVALue`` command.
        """  # noqa: E501
        return self._rcvr

    @property
    def wlength(self) -> ChannelOpticalWlength:
        """Return the ``CH<x>:OPTIcal:WLENgth`` command.

        Description:
            - Get or set the optical wavelength (in nanometers) that is used by the Probe and
              oscilloscope to compensate for the applied optical signal. Use the optional second
              argument to specify whether the to recall the factory calibration values or the
              user-programmed calibration values.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:OPTIcal:WLENgth?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:OPTIcal:WLENgth?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:OPTIcal:WLENgth value``
              command.

        SCPI Syntax:
            ```
            - CH<x>:OPTIcal:WLENgth <NR1> [, USER|, FACTory]
            - CH<x>:OPTIcal:WLENgth?
            ```

        Info:
            - ``<NR1>`` is the optical wavelength (in nanometers).
            - ``USER`` specifies user-programmed calibration values that can be loaded onto the
              probe through a separate utility.
            - ``FACTory`` specifies using factory calibration values. The second argument defaults
              to FACTory if none is specified.

        Sub-properties:
            - ``.list``: The ``CH<x>:OPTIcal:WLENgth:LIST`` command.
        """
        return self._wlength


class ChannelOptiPower(SCPICmdRead):
    """The ``CH<x>:OPTI:POWER`` command.

    Description:
        - This command queries the power meter reading of the DPO7OE1 attached to the specified
          channel.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:OPTI:POWER?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:OPTI:POWER?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:OPTI:POWER?
        ```
    """


class ChannelOpti(SCPICmdRead):
    """The ``CH<x>:OPTI`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:OPTI?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:OPTI?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.power``: The ``CH<x>:OPTI:POWER`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._power = ChannelOptiPower(device, f"{self._cmd_syntax}:POWER")

    @property
    def power(self) -> ChannelOptiPower:
        """Return the ``CH<x>:OPTI:POWER`` command.

        Description:
            - This command queries the power meter reading of the DPO7OE1 attached to the specified
              channel.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:OPTI:POWER?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:OPTI:POWER?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:OPTI:POWER?
            ```
        """
        return self._power


class ChannelOffset(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:OFFSet`` command.

    Description:
        - This command sets or queries the vertical offset for the specified analog channel.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:OFFSet?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:OFFSet?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:OFFSet value`` command.

    SCPI Syntax:
        ```
        - CH<x>:OFFSet <NR3>
        - CH<x>:OFFSet?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` is the offset value for the specified channel.
    """


class ChannelLabelYpos(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:LABel:YPOS`` command.

    Description:
        - This command sets or queries the Y screen offset at which the label (attached to the
          displayed waveform of the specified channel) is displayed, relative to the waveform
          handle. The channel is specified by x. The value of x can range from 1 through 4. This
          command is equivalent to selecting Label from the Vertical menu and either viewing or
          setting Y Pos.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:LABel:YPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:LABel:YPOS?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:LABel:YPOS value`` command.

    SCPI Syntax:
        ```
        - CH<x>:LABel:YPOS <NR1>
        - CH<x>:LABel:YPOS?
        ```

    Info:
        - ``<NR1>`` is the location (in divisions) where the waveform label for the selected channel
          is displayed, relative to the waveform handle. Arguments should be integers ranging from
          10 to -10.
    """


class ChannelLabelXpos(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:LABel:XPOS`` command.

    Description:
        - This command sets or queries the X screen offset at which the label (attached to the
          displayed waveform of the specified channel) is displayed, relative to the left edge of
          the screen. The channel is specified by x. The value of x can range from 1 through 4. This
          command is equivalent to selecting Label from the Vertical menu and either viewing or
          setting X Pos.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:LABel:XPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:LABel:XPOS?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:LABel:XPOS value`` command.

    SCPI Syntax:
        ```
        - CH<x>:LABel:XPOS <NR1>
        - CH<x>:LABel:XPOS?
        ```

    Info:
        - ``<NR1>`` is the location (control in divisions) where the waveform label for the selected
          channel is displayed, relative to the left edge of the screen. Arguments should be
          integers ranging from 0 through 10.
    """


class ChannelLabelName(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:LABel:NAMe`` command.

    Description:
        - This command sets or queries the label attached to the displayed waveform for the
          specified channel. The channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:LABel:NAMe?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:LABel:NAMe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:LABel:NAMe value`` command.

    SCPI Syntax:
        ```
        - CH<x>:LABel:NAMe <QString>
        - CH<x>:LABel:NAMe?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<QString>`` is an alphanumeric character string, ranging from 1 through 32 characters in
          length.
    """

    _WRAP_ARG_WITH_QUOTES = True


class ChannelLabel(SCPICmdRead):
    """The ``CH<x>:LABel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:LABel?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` is the channel number.

    Properties:
        - ``.name``: The ``CH<x>:LABel:NAMe`` command.
        - ``.xpos``: The ``CH<x>:LABel:XPOS`` command.
        - ``.ypos``: The ``CH<x>:LABel:YPOS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._name = ChannelLabelName(device, f"{self._cmd_syntax}:NAMe")
        self._xpos = ChannelLabelXpos(device, f"{self._cmd_syntax}:XPOS")
        self._ypos = ChannelLabelYpos(device, f"{self._cmd_syntax}:YPOS")

    @property
    def name(self) -> ChannelLabelName:
        """Return the ``CH<x>:LABel:NAMe`` command.

        Description:
            - This command sets or queries the label attached to the displayed waveform for the
              specified channel. The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:LABel:NAMe?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:LABel:NAMe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:LABel:NAMe value`` command.

        SCPI Syntax:
            ```
            - CH<x>:LABel:NAMe <QString>
            - CH<x>:LABel:NAMe?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<QString>`` is an alphanumeric character string, ranging from 1 through 32
              characters in length.
        """
        return self._name

    @property
    def xpos(self) -> ChannelLabelXpos:
        """Return the ``CH<x>:LABel:XPOS`` command.

        Description:
            - This command sets or queries the X screen offset at which the label (attached to the
              displayed waveform of the specified channel) is displayed, relative to the left edge
              of the screen. The channel is specified by x. The value of x can range from 1 through
              4. This command is equivalent to selecting Label from the Vertical menu and either
              viewing or setting X Pos.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:LABel:XPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:LABel:XPOS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:LABel:XPOS value`` command.

        SCPI Syntax:
            ```
            - CH<x>:LABel:XPOS <NR1>
            - CH<x>:LABel:XPOS?
            ```

        Info:
            - ``<NR1>`` is the location (control in divisions) where the waveform label for the
              selected channel is displayed, relative to the left edge of the screen. Arguments
              should be integers ranging from 0 through 10.
        """
        return self._xpos

    @property
    def ypos(self) -> ChannelLabelYpos:
        """Return the ``CH<x>:LABel:YPOS`` command.

        Description:
            - This command sets or queries the Y screen offset at which the label (attached to the
              displayed waveform of the specified channel) is displayed, relative to the waveform
              handle. The channel is specified by x. The value of x can range from 1 through 4. This
              command is equivalent to selecting Label from the Vertical menu and either viewing or
              setting Y Pos.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:LABel:YPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:LABel:YPOS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:LABel:YPOS value`` command.

        SCPI Syntax:
            ```
            - CH<x>:LABel:YPOS <NR1>
            - CH<x>:LABel:YPOS?
            ```

        Info:
            - ``<NR1>`` is the location (in divisions) where the waveform label for the selected
              channel is displayed, relative to the waveform handle. Arguments should be integers
              ranging from 10 to -10.
        """
        return self._ypos


class ChannelInvert(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:INVert`` command.

    Description:
        - This command sets or queries invert state of the specified channel. The channel is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:INVert?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:INVert?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:INVert value`` command.

    SCPI Syntax:
        ```
        - CH<x>:INVert {ON|OFF|<NR1>}
        - CH<x>:INVert?
        ```

    Info:
        - ``OFF`` turns off the channel invert.
        - ``ON`` turns on the channel invert.
        - ``<NR1>`` 0 turns off the channel invert; any other value turns on the channel invert.
    """


class ChannelIcaptureState(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:ICAPture:STATE`` command.

    Description:
        - This command sets or queries the state of the iCapture feature for the channel specified
          by x. The value of x can range from 1 through 4.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:ICAPture:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:ICAPture:STATE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:ICAPture:STATE value`` command.

    SCPI Syntax:
        ```
        - CH<x>:ICAPture:STATE {ON|OFF|<NR1>}
        - CH<x>:ICAPture:STATE?
        ```

    Info:
        - ``<NR1>`` = 0 turns off the iCapture feature; any other value turns on the iCapture
          feature.
        - ``OFF`` turns off the iCapture feature.
        - ``ON`` turns on the iCapture feature.
    """


class ChannelIcaptureSource(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:ICAPture:SOUrce`` command.

    Description:
        - This command sets or queries the digital source to acquire iCapture signals.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:ICAPture:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:ICAPture:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:ICAPture:SOUrce value`` command.

    SCPI Syntax:
        ```
        - CH<x>:ICAPture:SOUrce {D<x>|CQ0}
        - CH<x>:ICAPture:SOUrce?
        ```

    Info:
        - ``D<x>`` or CQ0 specifies the digital channel. x has a minimum of 0 and a maximum of 15.
    """


class ChannelIcapture(SCPICmdRead):
    """The ``CH<x>:ICAPture`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:ICAPture?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:ICAPture?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``CH<x>:ICAPture:SOUrce`` command.
        - ``.state``: The ``CH<x>:ICAPture:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = ChannelIcaptureSource(device, f"{self._cmd_syntax}:SOUrce")
        self._state = ChannelIcaptureState(device, f"{self._cmd_syntax}:STATE")

    @property
    def source(self) -> ChannelIcaptureSource:
        """Return the ``CH<x>:ICAPture:SOUrce`` command.

        Description:
            - This command sets or queries the digital source to acquire iCapture signals.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:ICAPture:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:ICAPture:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:ICAPture:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - CH<x>:ICAPture:SOUrce {D<x>|CQ0}
            - CH<x>:ICAPture:SOUrce?
            ```

        Info:
            - ``D<x>`` or CQ0 specifies the digital channel. x has a minimum of 0 and a maximum of
              15.
        """
        return self._source

    @property
    def state(self) -> ChannelIcaptureState:
        """Return the ``CH<x>:ICAPture:STATE`` command.

        Description:
            - This command sets or queries the state of the iCapture feature for the channel
              specified by x. The value of x can range from 1 through 4.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:ICAPture:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:ICAPture:STATE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:ICAPture:STATE value``
              command.

        SCPI Syntax:
            ```
            - CH<x>:ICAPture:STATE {ON|OFF|<NR1>}
            - CH<x>:ICAPture:STATE?
            ```

        Info:
            - ``<NR1>`` = 0 turns off the iCapture feature; any other value turns on the iCapture
              feature.
            - ``OFF`` turns off the iCapture feature.
            - ``ON`` turns on the iCapture feature.
        """
        return self._state


class ChannelFastframecapable(SCPICmdRead):
    """The ``CH<x>:FASTFRamecapable`` command.

    Description:
        - This query-only command returns whether the specified channel is capable of FastFrame
          acquisitions.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:FASTFRamecapable?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:FASTFRamecapable?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:FASTFRamecapable?
        ```
    """


class ChannelFastacqcapable(SCPICmdRead):
    """The ``CH<x>:FASTAcqcapable`` command.

    Description:
        - This query-only command returns whether the specified channel is capable of FastAcq.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:FASTAcqcapable?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:FASTAcqcapable?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:FASTAcqcapable?
        ```
    """


class ChannelDeskew(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:DESKew`` command.

    Description:
        - This command sets or queries the horizontal deskew time for the specified channel. The
          channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:DESKew?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:DESKew?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:DESKew value`` command.

    SCPI Syntax:
        ```
        - CH<x>:DESKew <NR3>
        - CH<x>:DESKew?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` is the deskew time for this channel, ranging from -125 ns to +125 ns with a
          resolution of 40 ps. Out-of-range values are clipped.
    """


class ChannelCoupling(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:COUPling`` command.

    Description:
        - This command sets or queries the input attenuator coupling setting for the specified
          channel. The channel is specified by x. The value of x can range from 1 through 4. This
          command is equivalent to selecting Coupling from the Vertical menu.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:COUPling?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:COUPling?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:COUPling value`` command.

    SCPI Syntax:
        ```
        - CH<x>:COUPling {AC|DC|DCREJect|GND}
        - CH<x>:COUPling?
        ```

    Info:
        - ``AC`` sets the specified channel to AC coupling.
        - ``DC`` sets the specified channel to DC coupling.
        - ``DCREJect`` sets DC Reject coupling when probes are attached that have that feature.
        - ``GND`` sets the specified channel to ground. Only a flat, ground-level waveform will be
          displayed.
    """


class ChannelBandwidthEnhancedState(SCPICmdRead):
    """The ``CH<x>:BANdwidth:ENHanced:STATE`` command.

    Description:
        - This query-only command returns the state of the bandwidth enhancement filter (DSP).

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:BANdwidth:ENHanced:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:BANdwidth:ENHanced:STATE?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:BANdwidth:ENHanced:STATE?
        ```
    """


class ChannelBandwidthEnhancedForce(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:BANdwidth:ENHanced:FORCe`` command.

    Description:
        - This command sets or queries the Force constant sample rate of the Digital Filters (DSP).
          The bandwidth Enhanced Filter provides you the ability to 'Force' constant sample rate,
          keeping the system in the sample rate base. This is also known as Bandwidth Enhanced AUTO.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:BANdwidth:ENHanced:FORCe?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:BANdwidth:ENHanced:FORCe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:BANdwidth:ENHanced:FORCe value``
          command.

    SCPI Syntax:
        ```
        - CH<x>:BANdwidth:ENHanced:FORCe {OFF|ON}
        - CH<x>:BANdwidth:ENHanced:FORCe?
        ```

    Info:
        - ``OFF`` is the default setting; DSP filtering occurs when sample rate is supported.
        - ``ON`` forces the conditions appropriate for Digital Filtering (DSP) to occur. With this
          option system changes are made to achieve sample rate that Bandwidth Enhanced Digital
          Filters (DSP) operate in, a Horizontal Mode of Constant Sample Rate, appropriate DSP BW,
          and Bandwidth Enhanced Auto on the specified channel would all be selected. Incompatible
          features would be turned off for example, FastAcq would be inhibited.
    """


class ChannelBandwidthEnhancedApplytoall(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:BANdwidth:ENHanced:APPLYtoall`` command.

    Description:
        - This command sets or queries specified channel's bandwidth and bandwidth enhanced
          selection, 'DSP' or 'Analog Only' to set the other channels the same. Bandwidth achieved
          on each channel can further be limited while conditions, such as a lower bandwidth probe,
          that limited the bandwidth exist. A query will almost certainly return 0, as once the
          request is processed, ApplyToAll will return to its default state of OFF allowing the
          channels to continue operating independently.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:BANdwidth:ENHanced:APPLYtoall?``
          query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:BANdwidth:ENHanced:APPLYtoall?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``CH<x>:BANdwidth:ENHanced:APPLYtoall value`` command.

    SCPI Syntax:
        ```
        - CH<x>:BANdwidth:ENHanced:APPLYtoall {ON|OFF|1|0}
        - CH<x>:BANdwidth:ENHanced:APPLYtoall?
        ```

    Info:
        - ``ON`` sets other channels to bandwidth and bandwidth enhancement filters or analog only
          of the specified channel.
        - ``OFF`` is the default setting, each channel operates independently regarding bandwidth
          and bandwidth enhanced (DSP).
        - ``1`` sets other channels to bandwidth and bandwidth enhancement filters or analog only of
          the specified channel.
        - ``0`` is the default and each channel operates independently regarding bandwidth and
          bandwidth enhanced (DSP).
    """


class ChannelBandwidthEnhancedAllmatched(SCPICmdRead):
    """The ``CH<x>:BANdwidth:ENHanced:ALLMatched`` command.

    Description:
        - This query-only command returns the state of channel matching for enhanced bandwidth.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:BANdwidth:ENHanced:ALLMatched?``
          query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:BANdwidth:ENHanced:ALLMatched?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:BANdwidth:ENHanced:ALLMatched?
        ```
    """


class ChannelBandwidthEnhanced(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:BANdwidth:ENHanced`` command.

    Description:
        - This command sets or queries the 'Bandwidth Enhancement (DSP) Enabled' or 'Analog Only'
          option.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:BANdwidth:ENHanced?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:BANdwidth:ENHanced?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:BANdwidth:ENHanced value``
          command.

    SCPI Syntax:
        ```
        - CH<x>:BANdwidth:ENHanced {AUTO|OFF}
        - CH<x>:BANdwidth:ENHanced?
        ```

    Info:
        - ``AUTO`` allows 'Bandwidth Enhanced (DSP) Enabled', filtering as possible.
        - ``OFF`` allows 'Analog Only', preventing DSP filtering.

    Properties:
        - ``.allmatched``: The ``CH<x>:BANdwidth:ENHanced:ALLMatched`` command.
        - ``.applytoall``: The ``CH<x>:BANdwidth:ENHanced:APPLYtoall`` command.
        - ``.force``: The ``CH<x>:BANdwidth:ENHanced:FORCe`` command.
        - ``.state``: The ``CH<x>:BANdwidth:ENHanced:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._allmatched = ChannelBandwidthEnhancedAllmatched(
            device, f"{self._cmd_syntax}:ALLMatched"
        )
        self._applytoall = ChannelBandwidthEnhancedApplytoall(
            device, f"{self._cmd_syntax}:APPLYtoall"
        )
        self._force = ChannelBandwidthEnhancedForce(device, f"{self._cmd_syntax}:FORCe")
        self._state = ChannelBandwidthEnhancedState(device, f"{self._cmd_syntax}:STATE")

    @property
    def allmatched(self) -> ChannelBandwidthEnhancedAllmatched:
        """Return the ``CH<x>:BANdwidth:ENHanced:ALLMatched`` command.

        Description:
            - This query-only command returns the state of channel matching for enhanced bandwidth.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:BANdwidth:ENHanced:ALLMatched?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CH<x>:BANdwidth:ENHanced:ALLMatched?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:BANdwidth:ENHanced:ALLMatched?
            ```
        """
        return self._allmatched

    @property
    def applytoall(self) -> ChannelBandwidthEnhancedApplytoall:
        """Return the ``CH<x>:BANdwidth:ENHanced:APPLYtoall`` command.

        Description:
            - This command sets or queries specified channel's bandwidth and bandwidth enhanced
              selection, 'DSP' or 'Analog Only' to set the other channels the same. Bandwidth
              achieved on each channel can further be limited while conditions, such as a lower
              bandwidth probe, that limited the bandwidth exist. A query will almost certainly
              return 0, as once the request is processed, ApplyToAll will return to its default
              state of OFF allowing the channels to continue operating independently.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:BANdwidth:ENHanced:APPLYtoall?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CH<x>:BANdwidth:ENHanced:APPLYtoall?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CH<x>:BANdwidth:ENHanced:APPLYtoall value`` command.

        SCPI Syntax:
            ```
            - CH<x>:BANdwidth:ENHanced:APPLYtoall {ON|OFF|1|0}
            - CH<x>:BANdwidth:ENHanced:APPLYtoall?
            ```

        Info:
            - ``ON`` sets other channels to bandwidth and bandwidth enhancement filters or analog
              only of the specified channel.
            - ``OFF`` is the default setting, each channel operates independently regarding
              bandwidth and bandwidth enhanced (DSP).
            - ``1`` sets other channels to bandwidth and bandwidth enhancement filters or analog
              only of the specified channel.
            - ``0`` is the default and each channel operates independently regarding bandwidth and
              bandwidth enhanced (DSP).
        """
        return self._applytoall

    @property
    def force(self) -> ChannelBandwidthEnhancedForce:
        """Return the ``CH<x>:BANdwidth:ENHanced:FORCe`` command.

        Description:
            - This command sets or queries the Force constant sample rate of the Digital Filters
              (DSP). The bandwidth Enhanced Filter provides you the ability to 'Force' constant
              sample rate, keeping the system in the sample rate base. This is also known as
              Bandwidth Enhanced AUTO.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:BANdwidth:ENHanced:FORCe?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:BANdwidth:ENHanced:FORCe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CH<x>:BANdwidth:ENHanced:FORCe value`` command.

        SCPI Syntax:
            ```
            - CH<x>:BANdwidth:ENHanced:FORCe {OFF|ON}
            - CH<x>:BANdwidth:ENHanced:FORCe?
            ```

        Info:
            - ``OFF`` is the default setting; DSP filtering occurs when sample rate is supported.
            - ``ON`` forces the conditions appropriate for Digital Filtering (DSP) to occur. With
              this option system changes are made to achieve sample rate that Bandwidth Enhanced
              Digital Filters (DSP) operate in, a Horizontal Mode of Constant Sample Rate,
              appropriate DSP BW, and Bandwidth Enhanced Auto on the specified channel would all be
              selected. Incompatible features would be turned off for example, FastAcq would be
              inhibited.
        """
        return self._force

    @property
    def state(self) -> ChannelBandwidthEnhancedState:
        """Return the ``CH<x>:BANdwidth:ENHanced:STATE`` command.

        Description:
            - This query-only command returns the state of the bandwidth enhancement filter (DSP).

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:BANdwidth:ENHanced:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:BANdwidth:ENHanced:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:BANdwidth:ENHanced:STATE?
            ```
        """
        return self._state


class ChannelBandwidth(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:BANdwidth`` command.

    Description:
        - This command sets or queries the selectable low-pass bandwidth limit filter of the
          specified channel. The channel is specified by x. The value of x can range from 1 through
          4. This is equivalent to selecting Bandwidth from the Vertical menu. The query form of
          this command always returns the approximate realized bandwidth of the channel. Available
          arguments depend upon the instrument and the attached accessories.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:BANdwidth?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:BANdwidth?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:BANdwidth value`` command.

    SCPI Syntax:
        ```
        - CH<x>:BANdwidth {<NR3>|FIVe|FULl|TWEnty|ONEfifty|TWOfifty}
        - CH<x>:BANdwidth?
        ```

    Info:
        - ``<NR3>`` argument is a double-precision ASCII string. The instrument rounds this value to
          an available bandwidth using geometric rounding and then uses this value set the upper
          bandwidth.
        - ``FIVe`` sets the upper bandwidth limit to 500 MHz.
        - ``FULl`` disables any optional bandwidth limiting. The specified channel operates at its
          maximum bandwidth.
        - ``TWEnty`` sets the upper bandwidth limit to 20 MHz.
        - ``ONEfifty`` sets the upper bandwidth limit to 150 MHz.
        - ``TWOfifty`` sets the upper bandwidth limit to 250 MHz.

    Properties:
        - ``.enhanced``: The ``CH<x>:BANdwidth:ENHanced`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._enhanced = ChannelBandwidthEnhanced(device, f"{self._cmd_syntax}:ENHanced")

    @property
    def enhanced(self) -> ChannelBandwidthEnhanced:
        """Return the ``CH<x>:BANdwidth:ENHanced`` command.

        Description:
            - This command sets or queries the 'Bandwidth Enhancement (DSP) Enabled' or 'Analog
              Only' option.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:BANdwidth:ENHanced?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:BANdwidth:ENHanced?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:BANdwidth:ENHanced value``
              command.

        SCPI Syntax:
            ```
            - CH<x>:BANdwidth:ENHanced {AUTO|OFF}
            - CH<x>:BANdwidth:ENHanced?
            ```

        Info:
            - ``AUTO`` allows 'Bandwidth Enhanced (DSP) Enabled', filtering as possible.
            - ``OFF`` allows 'Analog Only', preventing DSP filtering.

        Sub-properties:
            - ``.allmatched``: The ``CH<x>:BANdwidth:ENHanced:ALLMatched`` command.
            - ``.applytoall``: The ``CH<x>:BANdwidth:ENHanced:APPLYtoall`` command.
            - ``.force``: The ``CH<x>:BANdwidth:ENHanced:FORCe`` command.
            - ``.state``: The ``CH<x>:BANdwidth:ENHanced:STATE`` command.
        """
        return self._enhanced


class ChannelAvailable(SCPICmdRead):
    """The ``CH<x>:AVAILable`` command.

    Description:
        - This query-only command returns whether the specified channel is available.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:AVAILable?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:AVAILable?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:AVAILable?
        ```
    """


class ChannelAtiactive(SCPICmdRead):
    """The ``CH<x>:ATIACTive`` command.

    Description:
        - This query-only command returns whether the specified channel is an ATI channel.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:ATIACTive?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:ATIACTive?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:ATIACTive?
        ```
    """


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class Channel(ValidatedChannel, SCPICmdRead):
    """The ``CH<x>`` command.

    Description:
        - This query-only command returns the vertical parameters for the specified channel. The
          channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>?
        ```

    Properties:
        - ``.atiactive``: The ``CH<x>:ATIACTive`` command.
        - ``.available``: The ``CH<x>:AVAILable`` command.
        - ``.bandwidth``: The ``CH<x>:BANdwidth`` command.
        - ``.coupling``: The ``CH<x>:COUPling`` command.
        - ``.deskew``: The ``CH<x>:DESKew`` command.
        - ``.fastacqcapable``: The ``CH<x>:FASTAcqcapable`` command.
        - ``.fastframecapable``: The ``CH<x>:FASTFRamecapable`` command.
        - ``.icapture``: The ``CH<x>:ICAPture`` command tree.
        - ``.invert``: The ``CH<x>:INVert`` command.
        - ``.label``: The ``CH<x>:LABel`` command tree.
        - ``.offset``: The ``CH<x>:OFFSet`` command.
        - ``.opti``: The ``CH<x>:OPTI`` command tree.
        - ``.optical``: The ``CH<x>:OPTIcal`` command tree.
        - ``.position``: The ``CH<x>:POSition`` command.
        - ``.probecontrol``: The ``CH<x>:PROBECOntrol`` command.
        - ``.probecal``: The ``CH<x>:PROBECal`` command.
        - ``.probefunc``: The ``CH<x>:PROBEFunc`` command tree.
        - ``.probe``: The ``CH<x>:PRObe`` command.
        - ``.scale``: The ``CH<x>:SCAle`` command.
        - ``.termination``: The ``CH<x>:TERmination`` command.
        - ``.threshold``: The ``CH<x>:THRESHold`` command.
        - ``.vterm``: The ``CH<x>:VTERm`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "CH<x>") -> None:
        super().__init__(device, cmd_syntax)
        self._atiactive = ChannelAtiactive(device, f"{self._cmd_syntax}:ATIACTive")
        self._available = ChannelAvailable(device, f"{self._cmd_syntax}:AVAILable")
        self._bandwidth = ChannelBandwidth(device, f"{self._cmd_syntax}:BANdwidth")
        self._coupling = ChannelCoupling(device, f"{self._cmd_syntax}:COUPling")
        self._deskew = ChannelDeskew(device, f"{self._cmd_syntax}:DESKew")
        self._fastacqcapable = ChannelFastacqcapable(device, f"{self._cmd_syntax}:FASTAcqcapable")
        self._fastframecapable = ChannelFastframecapable(
            device, f"{self._cmd_syntax}:FASTFRamecapable"
        )
        self._icapture = ChannelIcapture(device, f"{self._cmd_syntax}:ICAPture")
        self._invert = ChannelInvert(device, f"{self._cmd_syntax}:INVert")
        self._label = ChannelLabel(device, f"{self._cmd_syntax}:LABel")
        self._offset = ChannelOffset(device, f"{self._cmd_syntax}:OFFSet")
        self._opti = ChannelOpti(device, f"{self._cmd_syntax}:OPTI")
        self._optical = ChannelOptical(device, f"{self._cmd_syntax}:OPTIcal")
        self._position = ChannelPosition(device, f"{self._cmd_syntax}:POSition")
        self._probecontrol = ChannelProbecontrol(device, f"{self._cmd_syntax}:PROBECOntrol")
        self._probecal = ChannelProbecal(device, f"{self._cmd_syntax}:PROBECal")
        self._probefunc = ChannelProbefunc(device, f"{self._cmd_syntax}:PROBEFunc")
        self._probe = ChannelProbe(device, f"{self._cmd_syntax}:PRObe")
        self._scale = ChannelScale(device, f"{self._cmd_syntax}:SCAle")
        self._termination = ChannelTermination(device, f"{self._cmd_syntax}:TERmination")
        self._threshold = ChannelThreshold(device, f"{self._cmd_syntax}:THRESHold")
        self._vterm = ChannelVterm(device, f"{self._cmd_syntax}:VTERm")

    @property
    def atiactive(self) -> ChannelAtiactive:
        """Return the ``CH<x>:ATIACTive`` command.

        Description:
            - This query-only command returns whether the specified channel is an ATI channel.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:ATIACTive?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:ATIACTive?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:ATIACTive?
            ```
        """
        return self._atiactive

    @property
    def available(self) -> ChannelAvailable:
        """Return the ``CH<x>:AVAILable`` command.

        Description:
            - This query-only command returns whether the specified channel is available.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:AVAILable?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:AVAILable?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:AVAILable?
            ```
        """
        return self._available

    @property
    def bandwidth(self) -> ChannelBandwidth:
        """Return the ``CH<x>:BANdwidth`` command.

        Description:
            - This command sets or queries the selectable low-pass bandwidth limit filter of the
              specified channel. The channel is specified by x. The value of x can range from 1
              through 4. This is equivalent to selecting Bandwidth from the Vertical menu. The query
              form of this command always returns the approximate realized bandwidth of the channel.
              Available arguments depend upon the instrument and the attached accessories.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:BANdwidth?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:BANdwidth?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:BANdwidth value`` command.

        SCPI Syntax:
            ```
            - CH<x>:BANdwidth {<NR3>|FIVe|FULl|TWEnty|ONEfifty|TWOfifty}
            - CH<x>:BANdwidth?
            ```

        Info:
            - ``<NR3>`` argument is a double-precision ASCII string. The instrument rounds this
              value to an available bandwidth using geometric rounding and then uses this value set
              the upper bandwidth.
            - ``FIVe`` sets the upper bandwidth limit to 500 MHz.
            - ``FULl`` disables any optional bandwidth limiting. The specified channel operates at
              its maximum bandwidth.
            - ``TWEnty`` sets the upper bandwidth limit to 20 MHz.
            - ``ONEfifty`` sets the upper bandwidth limit to 150 MHz.
            - ``TWOfifty`` sets the upper bandwidth limit to 250 MHz.

        Sub-properties:
            - ``.enhanced``: The ``CH<x>:BANdwidth:ENHanced`` command.
        """
        return self._bandwidth

    @property
    def coupling(self) -> ChannelCoupling:
        """Return the ``CH<x>:COUPling`` command.

        Description:
            - This command sets or queries the input attenuator coupling setting for the specified
              channel. The channel is specified by x. The value of x can range from 1 through 4.
              This command is equivalent to selecting Coupling from the Vertical menu.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:COUPling?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:COUPling?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:COUPling value`` command.

        SCPI Syntax:
            ```
            - CH<x>:COUPling {AC|DC|DCREJect|GND}
            - CH<x>:COUPling?
            ```

        Info:
            - ``AC`` sets the specified channel to AC coupling.
            - ``DC`` sets the specified channel to DC coupling.
            - ``DCREJect`` sets DC Reject coupling when probes are attached that have that feature.
            - ``GND`` sets the specified channel to ground. Only a flat, ground-level waveform will
              be displayed.
        """
        return self._coupling

    @property
    def deskew(self) -> ChannelDeskew:
        """Return the ``CH<x>:DESKew`` command.

        Description:
            - This command sets or queries the horizontal deskew time for the specified channel. The
              channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:DESKew?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:DESKew?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:DESKew value`` command.

        SCPI Syntax:
            ```
            - CH<x>:DESKew <NR3>
            - CH<x>:DESKew?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` is the deskew time for this channel, ranging from -125 ns to +125 ns with a
              resolution of 40 ps. Out-of-range values are clipped.
        """
        return self._deskew

    @property
    def fastacqcapable(self) -> ChannelFastacqcapable:
        """Return the ``CH<x>:FASTAcqcapable`` command.

        Description:
            - This query-only command returns whether the specified channel is capable of FastAcq.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:FASTAcqcapable?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:FASTAcqcapable?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:FASTAcqcapable?
            ```
        """
        return self._fastacqcapable

    @property
    def fastframecapable(self) -> ChannelFastframecapable:
        """Return the ``CH<x>:FASTFRamecapable`` command.

        Description:
            - This query-only command returns whether the specified channel is capable of FastFrame
              acquisitions.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:FASTFRamecapable?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:FASTFRamecapable?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:FASTFRamecapable?
            ```
        """
        return self._fastframecapable

    @property
    def icapture(self) -> ChannelIcapture:
        """Return the ``CH<x>:ICAPture`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:ICAPture?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:ICAPture?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``CH<x>:ICAPture:SOUrce`` command.
            - ``.state``: The ``CH<x>:ICAPture:STATE`` command.
        """
        return self._icapture

    @property
    def invert(self) -> ChannelInvert:
        """Return the ``CH<x>:INVert`` command.

        Description:
            - This command sets or queries invert state of the specified channel. The channel is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:INVert?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:INVert?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:INVert value`` command.

        SCPI Syntax:
            ```
            - CH<x>:INVert {ON|OFF|<NR1>}
            - CH<x>:INVert?
            ```

        Info:
            - ``OFF`` turns off the channel invert.
            - ``ON`` turns on the channel invert.
            - ``<NR1>`` 0 turns off the channel invert; any other value turns on the channel invert.
        """
        return self._invert

    @property
    def label(self) -> ChannelLabel:
        """Return the ``CH<x>:LABel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:LABel?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` is the channel number.

        Sub-properties:
            - ``.name``: The ``CH<x>:LABel:NAMe`` command.
            - ``.xpos``: The ``CH<x>:LABel:XPOS`` command.
            - ``.ypos``: The ``CH<x>:LABel:YPOS`` command.
        """
        return self._label

    @property
    def offset(self) -> ChannelOffset:
        """Return the ``CH<x>:OFFSet`` command.

        Description:
            - This command sets or queries the vertical offset for the specified analog channel.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:OFFSet?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:OFFSet?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:OFFSet value`` command.

        SCPI Syntax:
            ```
            - CH<x>:OFFSet <NR3>
            - CH<x>:OFFSet?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` is the offset value for the specified channel.
        """
        return self._offset

    @property
    def opti(self) -> ChannelOpti:
        """Return the ``CH<x>:OPTI`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:OPTI?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:OPTI?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.power``: The ``CH<x>:OPTI:POWER`` command.
        """
        return self._opti

    @property
    def optical(self) -> ChannelOptical:
        """Return the ``CH<x>:OPTIcal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:OPTIcal?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:OPTIcal?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.rcvr``: The ``CH<x>:OPTIcal:RCVR`` command.
            - ``.wlength``: The ``CH<x>:OPTIcal:WLENgth`` command.
        """
        return self._optical

    @property
    def position(self) -> ChannelPosition:
        """Return the ``CH<x>:POSition`` command.

        Description:
            - This command specifies the vertical position of channel <x>, where x is the channel
              number (1-4). The position value is applied to the signal before it is digitized.
              Increasing the position value of a waveform causes the waveform to move up. Decreasing
              the position value causes the waveform to move down. The position value determines the
              vertical graticule coordinate at which input signal values, minus the present offset
              setting for that channel, are displayed. For example, if the position for Channel 3 is
              set to 2.0 and the offset is set to 3.0, then input signals equal to 3.0 units are
              displayed 2.0 divisions above the center of the screen (at 1 V/div).

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:POSition?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:POSition value`` command.

        SCPI Syntax:
            ```
            - CH<x>:POSition <NR3>
            - CH<x>:POSition?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the position value for channel
              <x>, in divisions, from the center graticule. The range is 8 to -8 divisions.
        """
        return self._position

    @property
    def probecontrol(self) -> ChannelProbecontrol:
        """Return the ``CH<x>:PROBECOntrol`` command.

        Description:
            - This command sets or queries multirange probe range-control policy preference of the
              probe that is attached to CH<x>. The channel number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PROBECOntrol?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PROBECOntrol?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:PROBECOntrol value`` command.

        SCPI Syntax:
            ```
            - CH<x>:PROBECOntrol {AUTO|MANual}
            - CH<x>:PROBECOntrol?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``AUTO`` sets the values. The probe range is automatically calculated.
            - ``MANual`` allows you to select various valid values for the probe connected to a
              particular channel.
        """
        return self._probecontrol

    @property
    def probecal(self) -> ChannelProbecal:
        """Return the ``CH<x>:PROBECal`` command.

        Description:
            - This query-only command returns the probe calibration state for the specified channel.
              The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PROBECal?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PROBECal?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:PROBECal?
            ```
        """
        return self._probecal

    @property
    def probefunc(self) -> ChannelProbefunc:
        """Return the ``CH<x>:PROBEFunc`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PROBEFunc?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PROBEFunc?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` is the channel number.

        Sub-properties:
            - ``.extatten``: The ``CH<x>:PROBEFunc:EXTAtten`` command.
            - ``.extdbatten``: The ``CH<x>:PROBEFunc:EXTDBatten`` command.
            - ``.extunits``: The ``CH<x>:PROBEFunc:EXTUnits`` command.
        """
        return self._probefunc

    @property
    def probe(self) -> ChannelProbe:
        """Return the ``CH<x>:PRObe`` command.

        Description:
            - This query-only command returns all information concerning the probe that is attached
              to the specified channel. The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:PRObe?
            ```

        Sub-properties:
            - ``.autozero``: The ``CH<x>:PRObe:AUTOZero`` command.
            - ``.dc``: The ``CH<x>:PRObe:DC`` command tree.
            - ``.degauss``: The ``CH<x>:PRObe:DEGAUSS`` command.
            - ``.forcedrange``: The ``CH<x>:PRObe:FORCEDRange`` command.
            - ``.gain``: The ``CH<x>:PRObe:GAIN`` command.
            - ``.id``: The ``CH<x>:PRObe:ID`` command.
            - ``.inputmode``: The ``CH<x>:PRObe:INPUTMode`` command.
            - ``.range``: The ``CH<x>:PRObe:RANge`` command.
            - ``.resistance``: The ``CH<x>:PRObe:RESistance`` command.
            - ``.set``: The ``CH<x>:PRObe:SET`` command.
            - ``.signal``: The ``CH<x>:PRObe:SIGnal`` command.
            - ``.tiptype``: The ``CH<x>:PRObe:TIPtype`` command.
            - ``.units``: The ``CH<x>:PRObe:UNIts`` command.
        """
        return self._probe

    @property
    def scale(self) -> ChannelScale:
        """Return the ``CH<x>:SCAle`` command.

        Description:
            - This command sets or returns the vertical scale for the specified analog channel. The
              channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:SCAle?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:SCAle value`` command.

        SCPI Syntax:
            ```
            - CH<x>:SCAle <NR3>
            - CH<x>:SCAle?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` is the vertical scale for the specified analog channel.
        """
        return self._scale

    @property
    def termination(self) -> ChannelTermination:
        """Return the ``CH<x>:TERmination`` command.

        Description:
            - This command sets or queries the vertical termination for the specified analog
              channel. The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:TERmination?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:TERmination?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:TERmination value`` command.

        SCPI Syntax:
            ```
            - CH<x>:TERmination <NR3>
            - CH<x>:TERmination?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` specifies the channel input resistance, which can be specified as 50 Ω or
              1,000,000 Ω.
        """
        return self._termination

    @property
    def threshold(self) -> ChannelThreshold:
        """Return the ``CH<x>:THRESHold`` command.

        Description:
            - This command sets or queries the comparable threshold for converting the analog signal
              to digital form for the channel specified by x. The value of x can range from 1
              through 4.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:THRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:THRESHold?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:THRESHold value`` command.

        SCPI Syntax:
            ```
            - CH<x>:THRESHold <NR3>
            - CH<x>:THRESHold?
            ```

        Info:
            - ``<NR3>`` specifies the analog threshold in volts.
        """
        return self._threshold

    @property
    def vterm(self) -> ChannelVterm:
        """Return the ``CH<x>:VTERm`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:VTERm?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:VTERm?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` is the channel number.

        Sub-properties:
            - ``.bias``: The ``CH<x>:VTERm:BIAS`` command.
            - ``.dual``: The ``CH<x>:VTERm:DUAL`` command tree.
        """
        return self._vterm
