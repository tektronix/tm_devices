# pylint: disable=line-too-long
"""The math commands module.

These commands are used in the following models:
TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - MATH:ADDNew <QString>
    - MATH:DELete <QString>
    - MATH:LIST?
    - MATH:MATH<x>:ARINC429A:SUPPortedfields {DATa}
    - MATH:MATH<x>:ARINC429A:SUPPortedfields?
    - MATH:MATH<x>:AUDIO:SUPPortedfields {LCHannel|RCHannel|TDMChannel}
    - MATH:MATH<x>:AUDIO:SUPPortedfields?
    - MATH:MATH<x>:AUTOETHERnet:SUPPortedfields {DATa|IPData|TDATa}
    - MATH:MATH<x>:AUTOETHERnet:SUPPortedfields?
    - MATH:MATH<x>:AVG:MODE {ON|OFF|<NR1>}
    - MATH:MATH<x>:AVG:WEIGht <NR1>
    - MATH:MATH<x>:CAN:SUPPortedfields {DATa}
    - MATH:MATH<x>:CAN:SUPPortedfields?
    - MATH:MATH<x>:CXPI:SUPPortedfields {DATa}
    - MATH:MATH<x>:CXPI:SUPPortedfields?
    - MATH:MATH<x>:DEFine <QString>
    - MATH:MATH<x>:DEFine?
    - MATH:MATH<x>:ESPI:SUPPortedfields {DATa|CDATa|RDATa}
    - MATH:MATH<x>:ESPI:SUPPortedfields?
    - MATH:MATH<x>:ETHERCAT:SUPPortedfields {DATa|SDATa|NWVariabledata}
    - MATH:MATH<x>:ETHERCAT:SUPPortedfields?
    - MATH:MATH<x>:ETHERnet:SUPPortedfields {DATa|IPData|TDATa}
    - MATH:MATH<x>:ETHERnet:SUPPortedfields?
    - MATH:MATH<x>:EUSB:SUPPortedfields {DATa|DDATa}
    - MATH:MATH<x>:EUSB:SUPPortedfields?
    - MATH:MATH<x>:FILTer:CFReq <NR3>
    - MATH:MATH<x>:FILTer:CFReq?
    - MATH:MATH<x>:FILTer:DELay <NR3>
    - MATH:MATH<x>:FILTer:DELay?
    - MATH:MATH<x>:FILTer:DESIgn {EXECUTE|ABORT|APPLY}
    - MATH:MATH<x>:FILTer:HCFReq <NR3>
    - MATH:MATH<x>:FILTer:HCFReq?
    - MATH:MATH<x>:FILTer:INFo?
    - MATH:MATH<x>:FILTer:LCFReq <NR3>
    - MATH:MATH<x>:FILTer:LCFReq?
    - MATH:MATH<x>:FILTer:LOAD <QString>
    - MATH:MATH<x>:FILTer:LOAD:RESPonse {1|0}
    - MATH:MATH<x>:FILTer:LOAD:RESPonse?
    - MATH:MATH<x>:FILTer:ORDer <NR1>
    - MATH:MATH<x>:FILTer:ORDer?
    - MATH:MATH<x>:FILTer:PRIPple <NR3>
    - MATH:MATH<x>:FILTer:PRIPple?
    - MATH:MATH<x>:FILTer:RESPonse {BUTTerworth|CHEBYONe|CHEBYTWo|ELLiptical|GAUSsian|BESSelCUSTom}
    - MATH:MATH<x>:FILTer:ROFactor <NR3>
    - MATH:MATH<x>:FILTer:ROFactor?
    - MATH:MATH<x>:FILTer:SATTenuation <NR3>
    - MATH:MATH<x>:FILTer:SATTenuation?
    - MATH:MATH<x>:FILTer:SAVe <QString>
    - MATH:MATH<x>:FILTer:SAVe:RESPonse {1|0}
    - MATH:MATH<x>:FILTer:SAVe:RESPonse?
    - MATH:MATH<x>:FILTer:SDEViation <NR3>
    - MATH:MATH<x>:FILTer:SDEViation?
    - MATH:MATH<x>:FILTer:SDURation <NR3>
    - MATH:MATH<x>:FILTer:SDURation?
    - MATH:MATH<x>:FILTer:SOURce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - MATH:MATH<x>:FILTer:SOURce?
    - MATH:MATH<x>:FILTer:SYMBols <NR1>
    - MATH:MATH<x>:FILTer:SYMBols?
    - MATH:MATH<x>:FILTer:TWIDth <NR3>
    - MATH:MATH<x>:FILTer:TWIDth?
    - MATH:MATH<x>:FILTer:TYPe {LPASs|HPASs|BPASs|BSTop|APASs|HILBert|DIFFerentiator|RC|RRC}
    - MATH:MATH<x>:FILTer:TYPe?
    - MATH:MATH<x>:FLEXray:SUPPortedfields {DATa}
    - MATH:MATH<x>:FLEXray:SUPPortedfields?
    - MATH:MATH<x>:FUNCtion {ADD|SUBtract|MULTiply|DIVide}
    - MATH:MATH<x>:GATing {NONE|SCREEN|CURSor}
    - MATH:MATH<x>:GATing?
    - MATH:MATH<x>:I2C:SUPPortedfields {DATa}
    - MATH:MATH<x>:I2C:SUPPortedfields?
    - MATH:MATH<x>:I3C:SUPPortedfields {DATa}
    - MATH:MATH<x>:I3C:SUPPortedfields?
    - MATH:MATH<x>:INTERpolation {ON|OFF}
    - MATH:MATH<x>:LABel:COLor <QString>
    - MATH:MATH<x>:LABel:FONT:BOLD {ON|OFF|<NR1>}
    - MATH:MATH<x>:LABel:FONT:ITALic {ON|OFF|<NR1>}
    - MATH:MATH<x>:LABel:FONT:SIZE <NR1>
    - MATH:MATH<x>:LABel:FONT:TYPE <QString>
    - MATH:MATH<x>:LABel:FONT:UNDERline {ON|OFF|<NR1>}
    - MATH:MATH<x>:LABel:NAMe <QString>
    - MATH:MATH<x>:LABel:NAMe?
    - MATH:MATH<x>:LABel:XPOS <NR1>
    - MATH:MATH<x>:LABel:XPOS?
    - MATH:MATH<x>:LABel:YPOS <NR1>
    - MATH:MATH<x>:LABel:YPOS?
    - MATH:MATH<x>:LIN:SUPPortedfields {DATa}
    - MATH:MATH<x>:LIN:SUPPortedfields?
    - MATH:MATH<x>:MDIO:SUPPortedfields {DATa}
    - MATH:MATH<x>:MDIO:SUPPortedfields?
    - MATH:MATH<x>:MIL1553B:SUPPortedfields {DATa|PAYLoad}
    - MATH:MATH<x>:MIL1553B:SUPPortedfields?
    - MATH:MATH<x>:ONEWIRe:SUPPortedfields {DATa}
    - MATH:MATH<x>:ONEWIRe:SUPPortedfields?
    - MATH:MATH<x>:PARallel:SUPPortedfields {DATa}
    - MATH:MATH<x>:PARallel:SUPPortedfields?
    - MATH:MATH<x>:PSIFIVe:SUPPortedfields {DATa|DRA|DRB|SDATa}
    - MATH:MATH<x>:PSIFIVe:SUPPortedfields?
    - MATH:MATH<x>:RS232C:SUPPortedfields {DATa|TXData|RXData}
    - MATH:MATH<x>:RS232C:SUPPortedfields?
    - MATH:MATH<x>:SDLC:SUPPortedfields {DATa}
    - MATH:MATH<x>:SDLC:SUPPortedfields?
    - MATH:MATH<x>:SENT:SUPPortedfields {FCData|FCDFirst|FCDTwo|SDATa}
    - MATH:MATH<x>:SENT:SUPPortedfields?
    - MATH:MATH<x>:SIGNeddata {ON|OFF}
    - MATH:MATH<x>:SIGNeddata?
    - MATH:MATH<x>:SMBUS:SUPPortedfields {DATa}
    - MATH:MATH<x>:SMBUS:SUPPortedfields?
    - MATH:MATH<x>:SOUrce1 {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - MATH:MATH<x>:SPACEWIRe:SUPPortedfields {DATa}
    - MATH:MATH<x>:SPACEWIRe:SUPPortedfields?
    - MATH:MATH<x>:SPECTral:HORZ {LOG|LINEAr}
    - MATH:MATH<x>:SPECTral:HORZ?
    - MATH:MATH<x>:SPECTral:MAG {LINEAr|DBM}
    - MATH:MATH<x>:SPECTral:MAG?
    - MATH:MATH<x>:SPECTral:PHASE {DEGrees|RADians|GROUPDelay}
    - MATH:MATH<x>:SPECTral:PHASE?
    - MATH:MATH<x>:SPECTral:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - MATH:MATH<x>:SPECTral:SOUrce?
    - MATH:MATH<x>:SPECTral:SUPPress {OFF|ON|0|1}
    - MATH:MATH<x>:SPECTral:SUPPress:VALue <NR3>
    - MATH:MATH<x>:SPECTral:SUPPress:VALue?
    - MATH:MATH<x>:SPECTral:SUPPress?
    - MATH:MATH<x>:SPECTral:TYPE {MAGNitude|PHASe|REAL|IMAGinary}
    - MATH:MATH<x>:SPECTral:TYPE?
    - MATH:MATH<x>:SPECTral:UNWRap {OFF|ON|0|1}
    - MATH:MATH<x>:SPECTral:UNWRap:DEGrees <NR3>
    - MATH:MATH<x>:SPECTral:UNWRap:DEGrees?
    - MATH:MATH<x>:SPECTral:UNWRap?
    - MATH:MATH<x>:SPECTral:WINdow {RECTANGular|HAMMing|HANNing|BLACKMANHarris|KAISERBessel|GAUSSian|FLATTOP2|TEKEXPonential}
    - MATH:MATH<x>:SPECTral:WINdow?
    - MATH:MATH<x>:SPI:SUPPortedfields {DATa|MOSIdata|MISOdata}
    - MATH:MATH<x>:SPI:SUPPortedfields?
    - MATH:MATH<x>:SPMI:SUPPortedfields {DATa|CDATa|RDATa}
    - MATH:MATH<x>:SPMI:SUPPortedfields?
    - MATH:MATH<x>:SVID:SUPPortedfields {MPAYload|SPAYload}
    - MATH:MATH<x>:SVID:SUPPortedfields?
    - MATH:MATH<x>:TYPe {BASic|FILTER|FFT|ADVanced}
    - MATH:MATH<x>:USB:SUPPortedfields {DATa}
    - MATH:MATH<x>:USB:SUPPortedfields?
    - MATH:MATH<x>:VUNIT <QString>
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


class MathMathItemVunit(SCPICmdWrite):
    """The ``MATH:MATH<x>:VUNIT`` command.

    Description:
        - This command specifies or returns the math custom vertical units. The math waveform is
          specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:VUNIT value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:VUNIT <QString>
        ```

    Info:
        - ``<QString>`` is the custom vertical units.
    """

    _WRAP_ARG_WITH_QUOTES = True


class MathMathItemUsbSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:USB:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for USB bus.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:USB:SUPPortedfields?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:USB:SUPPortedfields?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:USB:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:USB:SUPPortedfields {DATa}
        - MATH:MATH<x>:USB:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
    """


class MathMathItemUsb(SCPICmdRead):
    """The ``MATH:MATH<x>:USB`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:USB?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:USB?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:USB:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemUsbSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemUsbSupportedfields:
        """Return the ``MATH:MATH<x>:USB:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for USB
              bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:USB:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:USB:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:USB:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:USB:SUPPortedfields {DATa}
            - MATH:MATH<x>:USB:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
        """
        return self._supportedfields


class MathMathItemType(SCPICmdWrite):
    """The ``MATH:MATH<x>:TYPe`` command.

    Description:
        - This command sets or queries the math type. The math waveform is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:TYPe value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:TYPe {BASic|FILTER|FFT|ADVanced}
        ```

    Info:
        - ``BASic`` set the type to basic math.
        - ``FILTER`` sets the math type to filter. Requires UDFLT licenses on 5, 6 series MSO
          instruments and Tekscope (Offline).
        - ``FFT`` sets the type to FFT math, which can use any live analog or reference waveform in
          the time domain. NOTE. You can also use FFT as part of a math expression by declaring the
          type.
        - ``ADVanced`` sets the type to advanced math.
    """


class MathMathItemSvidSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:SVID:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for SVID bus.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SVID:SUPPortedfields?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SVID:SUPPortedfields?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:SVID:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:SVID:SUPPortedfields {MPAYload|SPAYload}
        - MATH:MATH<x>:SVID:SUPPortedfields?
        ```

    Info:
        - ``MPAYload`` sets the field type to MPAYload.
        - ``SPAYload`` sets the field type to SPAYload.
    """


class MathMathItemSvid(SCPICmdRead):
    """The ``MATH:MATH<x>:SVID`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SVID?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SVID?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:SVID:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemSvidSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemSvidSupportedfields:
        """Return the ``MATH:MATH<x>:SVID:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for SVID
              bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SVID:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:SVID:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:SVID:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:SVID:SUPPortedfields {MPAYload|SPAYload}
            - MATH:MATH<x>:SVID:SUPPortedfields?
            ```

        Info:
            - ``MPAYload`` sets the field type to MPAYload.
            - ``SPAYload`` sets the field type to SPAYload.
        """
        return self._supportedfields


class MathMathItemSpmiSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:SPMI:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for SPMI bus.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPMI:SUPPortedfields?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPMI:SUPPortedfields?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:SPMI:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:SPMI:SUPPortedfields {DATa|CDATa|RDATa}
        - MATH:MATH<x>:SPMI:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
        - ``CDATa`` sets the field type to CDATa.
        - ``RDATa`` sets the field type to RDATa.
    """


class MathMathItemSpmi(SCPICmdRead):
    """The ``MATH:MATH<x>:SPMI`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPMI?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPMI?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:SPMI:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemSpmiSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemSpmiSupportedfields:
        """Return the ``MATH:MATH<x>:SPMI:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for SPMI
              bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPMI:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:SPMI:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:SPMI:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:SPMI:SUPPortedfields {DATa|CDATa|RDATa}
            - MATH:MATH<x>:SPMI:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
            - ``CDATa`` sets the field type to CDATa.
            - ``RDATa`` sets the field type to RDATa.
        """
        return self._supportedfields


class MathMathItemSpiSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:SPI:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for SPI bus.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPI:SUPPortedfields?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPI:SUPPortedfields?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:SPI:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:SPI:SUPPortedfields {DATa|MOSIdata|MISOdata}
        - MATH:MATH<x>:SPI:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
        - ``MOSIdata`` sets the field type to MOSIdata. MOSIdata field is available to select when
          SPI Bus configuration for Data Inputs is set to Two.
        - ``MISOdata`` sets the field type to MISOdata. MISOdata field is available to select when
          SPI Bus configuration for Data Inputs is set to Two.
    """


class MathMathItemSpi(SCPICmdRead):
    """The ``MATH:MATH<x>:SPI`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPI?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPI?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:SPI:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemSpiSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemSpiSupportedfields:
        """Return the ``MATH:MATH<x>:SPI:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for SPI
              bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPI:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:SPI:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:SPI:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:SPI:SUPPortedfields {DATa|MOSIdata|MISOdata}
            - MATH:MATH<x>:SPI:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
            - ``MOSIdata`` sets the field type to MOSIdata. MOSIdata field is available to select
              when SPI Bus configuration for Data Inputs is set to Two.
            - ``MISOdata`` sets the field type to MISOdata. MISOdata field is available to select
              when SPI Bus configuration for Data Inputs is set to Two.
        """
        return self._supportedfields


class MathMathItemSpectralWindow(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:SPECTral:WINdow`` command.

    Description:
        - This command sets or queries the window function used to apply the specified FFT window to
          the input data for the specified math waveform. The Math waveform is specified by x. A
          spectral window determines what the filter shape of the spectral analyzer will be in the
          frequency domain. It can be described by a mathematical function that is multiplied
          point-by-point times the input data to the spectral analyzer. Following is a list of
          arguments that specify the window function used to multiply the input data. The windows
          are listed in the order of their ability to resolve frequencies (resolution bandwidth).

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPECTral:WINdow?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPECTral:WINdow?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:SPECTral:WINdow value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:SPECTral:WINdow {RECTANGular|HAMMing|HANNing|BLACKMANHarris|KAISERBessel|GAUSSian|FLATTOP2|TEKEXPonential}
        - MATH:MATH<x>:SPECTral:WINdow?
        ```

    Info:
        - ``RECTANGular`` window function is equivalent to multiplying all gate data by one.
        - ``HAMMing`` window function is based on a cosine series.
        - ``HANNing`` window function is based on a cosine series.
        - ``BLACKMANHarris`` window function is based on a cosine series.
        - ``KAISERBessel`` window function is based on a cosine series.
        - ``GAUSSian`` window function has the best localization characteristics in the joint
          time/frequency plane.
        - ``FLATTOP2`` window function is a cosine series window with a flattened frequency response
          lobe.
        - ``TEKEXPonential`` window has an exponential nonsymmetrical shape in the time domain and a
          triangular shape in the frequency domain.
    """  # noqa: E501


class MathMathItemSpectralUnwrapDegrees(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:SPECTral:UNWRap:DEGrees`` command.

    Description:
        - This command sets or queries how many degrees adjacent phase values can jump before being
          unwrapped. This requires the Spectral type to be Phase and the UNWRAP to be enabled for
          this PI command to have any affect. The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPECTral:UNWRap:DEGrees?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MATH:MATH<x>:SPECTral:UNWRap:DEGrees?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:SPECTral:UNWRap:DEGrees value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:SPECTral:UNWRap:DEGrees <NR3>
        - MATH:MATH<x>:SPECTral:UNWRap:DEGrees?
        ```

    Info:
        - ``<NR3>`` is the value of unwrap phase in degrees.
    """


class MathMathItemSpectralUnwrap(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:SPECTral:UNWRap`` command.

    Description:
        - This command sets or queries whether phase unwrap of the spectral analyzer output data is
          enabled. The Math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPECTral:UNWRap?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPECTral:UNWRap?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:SPECTral:UNWRap value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:SPECTral:UNWRap {OFF|ON|0|1}
        - MATH:MATH<x>:SPECTral:UNWRap?
        ```

    Info:
        - ``0`` disables phase unwrap for the specified math waveform.
        - ``1`` enables phase unwrap for the specified math waveform.
        - ``ON`` enables phase unwrap for the specified math waveform.
        - ``OFF`` disables phase unwrap for the specified math waveform.

    Properties:
        - ``.degrees``: The ``MATH:MATH<x>:SPECTral:UNWRap:DEGrees`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._degrees = MathMathItemSpectralUnwrapDegrees(device, f"{self._cmd_syntax}:DEGrees")

    @property
    def degrees(self) -> MathMathItemSpectralUnwrapDegrees:
        """Return the ``MATH:MATH<x>:SPECTral:UNWRap:DEGrees`` command.

        Description:
            - This command sets or queries how many degrees adjacent phase values can jump before
              being unwrapped. This requires the Spectral type to be Phase and the UNWRAP to be
              enabled for this PI command to have any affect. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPECTral:UNWRap:DEGrees?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:SPECTral:UNWRap:DEGrees?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:SPECTral:UNWRap:DEGrees value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:SPECTral:UNWRap:DEGrees <NR3>
            - MATH:MATH<x>:SPECTral:UNWRap:DEGrees?
            ```

        Info:
            - ``<NR3>`` is the value of unwrap phase in degrees.
        """
        return self._degrees


class MathMathItemSpectralType(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:SPECTral:TYPE`` command.

    Description:
        - This command sets or queries the FFT type selected for spectral analysis. The math
          waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPECTral:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPECTral:TYPE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:SPECTral:TYPE value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:SPECTral:TYPE {MAGNitude|PHASe|REAL|IMAGinary}
        - MATH:MATH<x>:SPECTral:TYPE?
        ```

    Info:
        - ``MAGNitude`` specifies the magnitude spectral function.
        - ``PHASe`` specifies the phase spectral function.
        - ``REAL`` specifies the real spectral function.
        - ``IMAGinary`` specifies the imaginary spectral function.
    """


class MathMathItemSpectralSuppressValue(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:SPECTral:SUPPress:VALue`` command.

    Description:
        - This command sets or queries in volts the value of suppression threshold of the specified
          math waveform. This requires the Spectral type to be Phase and the Suppression to be
          enabled for this PI command to have any affect. The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPECTral:SUPPress:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MATH:MATH<x>:SPECTral:SUPPress:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:SPECTral:SUPPress:VALue value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:SPECTral:SUPPress:VALue <NR3>
        - MATH:MATH<x>:SPECTral:SUPPress:VALue?
        ```

    Info:
        - ``<NR3>`` is the value of suppression threshold of the specified math waveform in volts.
    """


class MathMathItemSpectralSuppress(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:SPECTral:SUPPress`` command.

    Description:
        - This command sets or queries whether suppression threshold for the specified math waveform
          is enabled. This is only applied when Spectral Plot type is Phase. The math waveform is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPECTral:SUPPress?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPECTral:SUPPress?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:SPECTral:SUPPress value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:SPECTral:SUPPress {OFF|ON|0|1}
        - MATH:MATH<x>:SPECTral:SUPPress?
        ```

    Info:
        - ``0`` disables suppression threshold for the specified math waveform.
        - ``1`` enables suppression threshold for the specified math waveform.
        - ``ON`` enables suppression threshold for the specified math waveform.
        - ``OFF`` disables suppression threshold for the specified math waveform.

    Properties:
        - ``.value``: The ``MATH:MATH<x>:SPECTral:SUPPress:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = MathMathItemSpectralSuppressValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> MathMathItemSpectralSuppressValue:
        """Return the ``MATH:MATH<x>:SPECTral:SUPPress:VALue`` command.

        Description:
            - This command sets or queries in volts the value of suppression threshold of the
              specified math waveform. This requires the Spectral type to be Phase and the
              Suppression to be enabled for this PI command to have any affect. The math waveform is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPECTral:SUPPress:VALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:SPECTral:SUPPress:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:SPECTral:SUPPress:VALue value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:SPECTral:SUPPress:VALue <NR3>
            - MATH:MATH<x>:SPECTral:SUPPress:VALue?
            ```

        Info:
            - ``<NR3>`` is the value of suppression threshold of the specified math waveform in
              volts.
        """
        return self._value


class MathMathItemSpectralSource(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:SPECTral:SOUrce`` command.

    Description:
        - This command sets or queries the specified spectral math source. This only works with a
          math of type FFT. The math waveform is specified by x. ``MATH:MATH<x>:SPECTRAL:SOURCE`` is
          for use when the ``MATH:MATH<x>:TYPE`` is FFT.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPECTral:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPECTral:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:SPECTral:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:SPECTral:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - MATH:MATH<x>:SPECTral:SOUrce?
        ```

    Info:
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``Math<x>`` specifies a math waveform as the source.
        - ``REF<x>`` specifies a reference waveform as the source.
    """


class MathMathItemSpectralPhase(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:SPECTral:PHASE`` command.

    Description:
        - This command sets or queries the units of a SpectralPhase function in the specified math
          definition string. The Math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPECTral:PHASE?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPECTral:PHASE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:SPECTral:PHASE value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:SPECTral:PHASE {DEGrees|RADians|GROUPDelay}
        - MATH:MATH<x>:SPECTral:PHASE?
        ```

    Info:
        - ``DEGREES`` sets the SpectralPhase units to degrees.
        - ``RADIANS`` sets the SpectralPhase units to radians.
        - ``GROUPDELAY`` sets the SpectralPhase units to groupdelay, which computes the derivative
          of unwrapped phase spectrum. Units are expressed in seconds.
    """


class MathMathItemSpectralMag(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:SPECTral:MAG`` command.

    Description:
        - This command sets or queries the units of the SpectralMag function in the specified math
          definition string. The Math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPECTral:MAG?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPECTral:MAG?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:SPECTral:MAG value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:SPECTral:MAG {LINEAr|DBM}
        - MATH:MATH<x>:SPECTral:MAG?
        ```

    Info:
        - ``LINEAR`` sets the SpectralMag units to linear.
        - ``DBM`` sets the SpectralMag units to decibels. It also sets the Ref Level Offset to a
          value that is the equivalent of 1 mW into 50 Ω.
    """


class MathMathItemSpectralHorz(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:SPECTral:HORZ`` command.

    Description:
        - This command sets or queries the horizontal display scale of the spectral math waveform.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPECTral:HORZ?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPECTral:HORZ?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:SPECTral:HORZ value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:SPECTral:HORZ {LOG|LINEAr}
        - MATH:MATH<x>:SPECTral:HORZ?
        ```

    Info:
        - ``LINEAr`` sets the SpectralMag units to linear.
        - ``LOG`` sets the SpectralMag units to log.
    """


#  pylint: disable=too-many-instance-attributes
class MathMathItemSpectral(SCPICmdRead):
    """The ``MATH:MATH<x>:SPECTral`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPECTral?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPECTral?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.horz``: The ``MATH:MATH<x>:SPECTral:HORZ`` command.
        - ``.mag``: The ``MATH:MATH<x>:SPECTral:MAG`` command.
        - ``.phase``: The ``MATH:MATH<x>:SPECTral:PHASE`` command.
        - ``.source``: The ``MATH:MATH<x>:SPECTral:SOUrce`` command.
        - ``.suppress``: The ``MATH:MATH<x>:SPECTral:SUPPress`` command.
        - ``.type``: The ``MATH:MATH<x>:SPECTral:TYPE`` command.
        - ``.unwrap``: The ``MATH:MATH<x>:SPECTral:UNWRap`` command.
        - ``.window``: The ``MATH:MATH<x>:SPECTral:WINdow`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._horz = MathMathItemSpectralHorz(device, f"{self._cmd_syntax}:HORZ")
        self._mag = MathMathItemSpectralMag(device, f"{self._cmd_syntax}:MAG")
        self._phase = MathMathItemSpectralPhase(device, f"{self._cmd_syntax}:PHASE")
        self._source = MathMathItemSpectralSource(device, f"{self._cmd_syntax}:SOUrce")
        self._suppress = MathMathItemSpectralSuppress(device, f"{self._cmd_syntax}:SUPPress")
        self._type = MathMathItemSpectralType(device, f"{self._cmd_syntax}:TYPE")
        self._unwrap = MathMathItemSpectralUnwrap(device, f"{self._cmd_syntax}:UNWRap")
        self._window = MathMathItemSpectralWindow(device, f"{self._cmd_syntax}:WINdow")

    @property
    def horz(self) -> MathMathItemSpectralHorz:
        """Return the ``MATH:MATH<x>:SPECTral:HORZ`` command.

        Description:
            - This command sets or queries the horizontal display scale of the spectral math
              waveform. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPECTral:HORZ?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPECTral:HORZ?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:SPECTral:HORZ value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:SPECTral:HORZ {LOG|LINEAr}
            - MATH:MATH<x>:SPECTral:HORZ?
            ```

        Info:
            - ``LINEAr`` sets the SpectralMag units to linear.
            - ``LOG`` sets the SpectralMag units to log.
        """
        return self._horz

    @property
    def mag(self) -> MathMathItemSpectralMag:
        """Return the ``MATH:MATH<x>:SPECTral:MAG`` command.

        Description:
            - This command sets or queries the units of the SpectralMag function in the specified
              math definition string. The Math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPECTral:MAG?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPECTral:MAG?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:SPECTral:MAG value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:SPECTral:MAG {LINEAr|DBM}
            - MATH:MATH<x>:SPECTral:MAG?
            ```

        Info:
            - ``LINEAR`` sets the SpectralMag units to linear.
            - ``DBM`` sets the SpectralMag units to decibels. It also sets the Ref Level Offset to a
              value that is the equivalent of 1 mW into 50 Ω.
        """
        return self._mag

    @property
    def phase(self) -> MathMathItemSpectralPhase:
        """Return the ``MATH:MATH<x>:SPECTral:PHASE`` command.

        Description:
            - This command sets or queries the units of a SpectralPhase function in the specified
              math definition string. The Math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPECTral:PHASE?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPECTral:PHASE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:SPECTral:PHASE value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:SPECTral:PHASE {DEGrees|RADians|GROUPDelay}
            - MATH:MATH<x>:SPECTral:PHASE?
            ```

        Info:
            - ``DEGREES`` sets the SpectralPhase units to degrees.
            - ``RADIANS`` sets the SpectralPhase units to radians.
            - ``GROUPDELAY`` sets the SpectralPhase units to groupdelay, which computes the
              derivative of unwrapped phase spectrum. Units are expressed in seconds.
        """
        return self._phase

    @property
    def source(self) -> MathMathItemSpectralSource:
        """Return the ``MATH:MATH<x>:SPECTral:SOUrce`` command.

        Description:
            - This command sets or queries the specified spectral math source. This only works with
              a math of type FFT. The math waveform is specified by x.
              ``MATH:MATH<x>:SPECTRAL:SOURCE`` is for use when the ``MATH:MATH<x>:TYPE`` is FFT.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPECTral:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPECTral:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:SPECTral:SOUrce value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:SPECTral:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - MATH:MATH<x>:SPECTral:SOUrce?
            ```

        Info:
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``Math<x>`` specifies a math waveform as the source.
            - ``REF<x>`` specifies a reference waveform as the source.
        """
        return self._source

    @property
    def suppress(self) -> MathMathItemSpectralSuppress:
        """Return the ``MATH:MATH<x>:SPECTral:SUPPress`` command.

        Description:
            - This command sets or queries whether suppression threshold for the specified math
              waveform is enabled. This is only applied when Spectral Plot type is Phase. The math
              waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPECTral:SUPPress?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPECTral:SUPPress?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:SPECTral:SUPPress value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:SPECTral:SUPPress {OFF|ON|0|1}
            - MATH:MATH<x>:SPECTral:SUPPress?
            ```

        Info:
            - ``0`` disables suppression threshold for the specified math waveform.
            - ``1`` enables suppression threshold for the specified math waveform.
            - ``ON`` enables suppression threshold for the specified math waveform.
            - ``OFF`` disables suppression threshold for the specified math waveform.

        Sub-properties:
            - ``.value``: The ``MATH:MATH<x>:SPECTral:SUPPress:VALue`` command.
        """
        return self._suppress

    @property
    def type(self) -> MathMathItemSpectralType:
        """Return the ``MATH:MATH<x>:SPECTral:TYPE`` command.

        Description:
            - This command sets or queries the FFT type selected for spectral analysis. The math
              waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPECTral:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPECTral:TYPE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:SPECTral:TYPE value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:SPECTral:TYPE {MAGNitude|PHASe|REAL|IMAGinary}
            - MATH:MATH<x>:SPECTral:TYPE?
            ```

        Info:
            - ``MAGNitude`` specifies the magnitude spectral function.
            - ``PHASe`` specifies the phase spectral function.
            - ``REAL`` specifies the real spectral function.
            - ``IMAGinary`` specifies the imaginary spectral function.
        """
        return self._type

    @property
    def unwrap(self) -> MathMathItemSpectralUnwrap:
        """Return the ``MATH:MATH<x>:SPECTral:UNWRap`` command.

        Description:
            - This command sets or queries whether phase unwrap of the spectral analyzer output data
              is enabled. The Math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPECTral:UNWRap?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPECTral:UNWRap?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:SPECTral:UNWRap value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:SPECTral:UNWRap {OFF|ON|0|1}
            - MATH:MATH<x>:SPECTral:UNWRap?
            ```

        Info:
            - ``0`` disables phase unwrap for the specified math waveform.
            - ``1`` enables phase unwrap for the specified math waveform.
            - ``ON`` enables phase unwrap for the specified math waveform.
            - ``OFF`` disables phase unwrap for the specified math waveform.

        Sub-properties:
            - ``.degrees``: The ``MATH:MATH<x>:SPECTral:UNWRap:DEGrees`` command.
        """
        return self._unwrap

    @property
    def window(self) -> MathMathItemSpectralWindow:
        """Return the ``MATH:MATH<x>:SPECTral:WINdow`` command.

        Description:
            - This command sets or queries the window function used to apply the specified FFT
              window to the input data for the specified math waveform. The Math waveform is
              specified by x. A spectral window determines what the filter shape of the spectral
              analyzer will be in the frequency domain. It can be described by a mathematical
              function that is multiplied point-by-point times the input data to the spectral
              analyzer. Following is a list of arguments that specify the window function used to
              multiply the input data. The windows are listed in the order of their ability to
              resolve frequencies (resolution bandwidth).

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPECTral:WINdow?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPECTral:WINdow?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:SPECTral:WINdow value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:SPECTral:WINdow {RECTANGular|HAMMing|HANNing|BLACKMANHarris|KAISERBessel|GAUSSian|FLATTOP2|TEKEXPonential}
            - MATH:MATH<x>:SPECTral:WINdow?
            ```

        Info:
            - ``RECTANGular`` window function is equivalent to multiplying all gate data by one.
            - ``HAMMing`` window function is based on a cosine series.
            - ``HANNing`` window function is based on a cosine series.
            - ``BLACKMANHarris`` window function is based on a cosine series.
            - ``KAISERBessel`` window function is based on a cosine series.
            - ``GAUSSian`` window function has the best localization characteristics in the joint
              time/frequency plane.
            - ``FLATTOP2`` window function is a cosine series window with a flattened frequency
              response lobe.
            - ``TEKEXPonential`` window has an exponential nonsymmetrical shape in the time domain
              and a triangular shape in the frequency domain.
        """  # noqa: E501
        return self._window


class MathMathItemSpacewireSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:SPACEWIRe:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for SPACEWIRe
          bus. The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPACEWIRe:SUPPortedfields?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MATH:MATH<x>:SPACEWIRe:SUPPortedfields?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:SPACEWIRe:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:SPACEWIRe:SUPPortedfields {DATa}
        - MATH:MATH<x>:SPACEWIRe:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
    """


class MathMathItemSpacewire(SCPICmdRead):
    """The ``MATH:MATH<x>:SPACEWIRe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPACEWIRe?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPACEWIRe?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:SPACEWIRe:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemSpacewireSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemSpacewireSupportedfields:
        """Return the ``MATH:MATH<x>:SPACEWIRe:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for
              SPACEWIRe bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MATH:MATH<x>:SPACEWIRe:SUPPortedfields?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:SPACEWIRe:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:SPACEWIRe:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:SPACEWIRe:SUPPortedfields {DATa}
            - MATH:MATH<x>:SPACEWIRe:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
        """
        return self._supportedfields


class MathMathItemSource1(SCPICmdWrite):
    """The ``MATH:MATH<x>:SOUrce1`` command.

    Description:
        - This command sets or queries the specified math source. The source in the command can be
          either 1 or 2. This command sets the Basic Math components in the user interface, with two
          sources and a function. You would also need to set the math type to Basic to see the
          change in the user interface but this will not effect the programmable interface. The math
          waveform and source are specified by x. SOURCE1 and SOURCE2 are for use when the
          ``MATH:MATH<x>:TYPE`` is BASIC.

    Usage:
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:SOUrce1 value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:SOUrce1 {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        ```

    Info:
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``Math<x>`` specifies a math waveform as the source.
        - ``REF<x>`` specifies a reference waveform as the source.
    """


class MathMathItemSmbusSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:SMBUS:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for SMBUS bus.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SMBUS:SUPPortedfields?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SMBUS:SUPPortedfields?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:SMBUS:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:SMBUS:SUPPortedfields {DATa}
        - MATH:MATH<x>:SMBUS:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
    """


class MathMathItemSmbus(SCPICmdRead):
    """The ``MATH:MATH<x>:SMBUS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SMBUS?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SMBUS?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:SMBUS:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemSmbusSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemSmbusSupportedfields:
        """Return the ``MATH:MATH<x>:SMBUS:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for SMBUS
              bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SMBUS:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:SMBUS:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:SMBUS:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:SMBUS:SUPPortedfields {DATa}
            - MATH:MATH<x>:SMBUS:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
        """
        return self._supportedfields


class MathMathItemSigneddata(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:SIGNeddata`` command.

    Description:
        - This command sets or queries value to denote that bus field is decoded as signed/unsigned
          data for math on bus source. The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SIGNeddata?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SIGNeddata?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:SIGNeddata value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:SIGNeddata {ON|OFF}
        - MATH:MATH<x>:SIGNeddata?
        ```

    Info:
        - ``ON`` indicates that the bus field is decoded as signed data for drawing the math
          waveform.
        - ``OFF`` indicates that the bus field is decoded as unsigned data for drawing the math
          waveform.
    """


class MathMathItemSentSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:SENT:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for SENT bus.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SENT:SUPPortedfields?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SENT:SUPPortedfields?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:SENT:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:SENT:SUPPortedfields {FCData|FCDFirst|FCDTwo|SDATa}
        - MATH:MATH<x>:SENT:SUPPortedfields?
        ```

    Info:
        - ``FCData`` sets the field type to FCData. FCData field is available to select when SENT
          Bus configuration for Fast Data Channels is set to 2.
        - ``FCDFirst`` sets the field type to FCDFirst.
        - ``FCDTwo`` sets the field type to FCDTwo.
        - ``SDATa`` sets the field type to SDATa. SDATa is available when SENT Bus configuration for
          Slow Channel is not None.
    """


class MathMathItemSent(SCPICmdRead):
    """The ``MATH:MATH<x>:SENT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SENT?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SENT?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:SENT:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemSentSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemSentSupportedfields:
        """Return the ``MATH:MATH<x>:SENT:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for SENT
              bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SENT:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:SENT:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:SENT:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:SENT:SUPPortedfields {FCData|FCDFirst|FCDTwo|SDATa}
            - MATH:MATH<x>:SENT:SUPPortedfields?
            ```

        Info:
            - ``FCData`` sets the field type to FCData. FCData field is available to select when
              SENT Bus configuration for Fast Data Channels is set to 2.
            - ``FCDFirst`` sets the field type to FCDFirst.
            - ``FCDTwo`` sets the field type to FCDTwo.
            - ``SDATa`` sets the field type to SDATa. SDATa is available when SENT Bus configuration
              for Slow Channel is not None.
        """
        return self._supportedfields


class MathMathItemSdlcSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:SDLC:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for SDLC bus.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SDLC:SUPPortedfields?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SDLC:SUPPortedfields?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:SDLC:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:SDLC:SUPPortedfields {DATa}
        - MATH:MATH<x>:SDLC:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
    """


class MathMathItemSdlc(SCPICmdRead):
    """The ``MATH:MATH<x>:SDLC`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SDLC?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SDLC?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:SDLC:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemSdlcSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemSdlcSupportedfields:
        """Return the ``MATH:MATH<x>:SDLC:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for SDLC
              bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SDLC:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:SDLC:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:SDLC:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:SDLC:SUPPortedfields {DATa}
            - MATH:MATH<x>:SDLC:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
        """
        return self._supportedfields


class MathMathItemRs232cSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:RS232C:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for RS232C
          bus. The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:RS232C:SUPPortedfields?``
          query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:RS232C:SUPPortedfields?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:RS232C:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:RS232C:SUPPortedfields {DATa|TXData|RXData}
        - MATH:MATH<x>:RS232C:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
        - ``TXData`` sets the field type to TXData. TXData field can be set when RS232 Bus
          configuration for Data Inputs is set to Two.
        - ``RXData`` sets the field type to RXData. RXData field can be set when RS232 Bus
          configuration for Data Inputs is set to Two.
    """


class MathMathItemRs232c(SCPICmdRead):
    """The ``MATH:MATH<x>:RS232C`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:RS232C?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:RS232C?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:RS232C:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemRs232cSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemRs232cSupportedfields:
        """Return the ``MATH:MATH<x>:RS232C:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for RS232C
              bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:RS232C:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:RS232C:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:RS232C:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:RS232C:SUPPortedfields {DATa|TXData|RXData}
            - MATH:MATH<x>:RS232C:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
            - ``TXData`` sets the field type to TXData. TXData field can be set when RS232 Bus
              configuration for Data Inputs is set to Two.
            - ``RXData`` sets the field type to RXData. RXData field can be set when RS232 Bus
              configuration for Data Inputs is set to Two.
        """
        return self._supportedfields


class MathMathItemPsifiveSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:PSIFIVe:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for PSIFIVe
          bus. The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:PSIFIVe:SUPPortedfields?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MATH:MATH<x>:PSIFIVe:SUPPortedfields?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:PSIFIVe:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:PSIFIVe:SUPPortedfields {DATa|DRA|DRB|SDATa}
        - MATH:MATH<x>:PSIFIVe:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
        - ``DRA`` sets the field type to DRA.
        - ``DRB`` sets the field type to DRB.
        - ``SDATa`` sets the field type to SDATa.
    """


class MathMathItemPsifive(SCPICmdRead):
    """The ``MATH:MATH<x>:PSIFIVe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:PSIFIVe?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:PSIFIVe?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:PSIFIVe:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemPsifiveSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemPsifiveSupportedfields:
        """Return the ``MATH:MATH<x>:PSIFIVe:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for
              PSIFIVe bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:PSIFIVe:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:PSIFIVe:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:PSIFIVe:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:PSIFIVe:SUPPortedfields {DATa|DRA|DRB|SDATa}
            - MATH:MATH<x>:PSIFIVe:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
            - ``DRA`` sets the field type to DRA.
            - ``DRB`` sets the field type to DRB.
            - ``SDATa`` sets the field type to SDATa.
        """
        return self._supportedfields


class MathMathItemParallelSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:PARallel:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for PARallel
          bus. The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:PARallel:SUPPortedfields?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MATH:MATH<x>:PARallel:SUPPortedfields?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:PARallel:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:PARallel:SUPPortedfields {DATa}
        - MATH:MATH<x>:PARallel:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
    """


class MathMathItemParallel(SCPICmdRead):
    """The ``MATH:MATH<x>:PARallel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:PARallel?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:PARallel?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:PARallel:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemParallelSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemParallelSupportedfields:
        """Return the ``MATH:MATH<x>:PARallel:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for
              PARallel bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:PARallel:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:PARallel:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:PARallel:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:PARallel:SUPPortedfields {DATa}
            - MATH:MATH<x>:PARallel:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
        """
        return self._supportedfields


class MathMathItemOnewireSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:ONEWIRe:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for ONEWIRe
          bus. The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:ONEWIRe:SUPPortedfields?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MATH:MATH<x>:ONEWIRe:SUPPortedfields?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:ONEWIRe:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:ONEWIRe:SUPPortedfields {DATa}
        - MATH:MATH<x>:ONEWIRe:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
    """


class MathMathItemOnewire(SCPICmdRead):
    """The ``MATH:MATH<x>:ONEWIRe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:ONEWIRe?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:ONEWIRe?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:ONEWIRe:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemOnewireSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemOnewireSupportedfields:
        """Return the ``MATH:MATH<x>:ONEWIRe:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for
              ONEWIRe bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:ONEWIRe:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:ONEWIRe:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:ONEWIRe:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:ONEWIRe:SUPPortedfields {DATa}
            - MATH:MATH<x>:ONEWIRe:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
        """
        return self._supportedfields


class MathMathItemMil1553bSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:MIL1553B:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for MIL1553B
          bus. The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:MIL1553B:SUPPortedfields?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MATH:MATH<x>:MIL1553B:SUPPortedfields?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:MIL1553B:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:MIL1553B:SUPPortedfields {DATa|PAYLoad}
        - MATH:MATH<x>:MIL1553B:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
        - ``PAYLoad`` sets the field type to PAYLoad.
    """


class MathMathItemMil1553b(SCPICmdRead):
    """The ``MATH:MATH<x>:MIL1553B`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:MIL1553B?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:MIL1553B?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:MIL1553B:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemMil1553bSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemMil1553bSupportedfields:
        """Return the ``MATH:MATH<x>:MIL1553B:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for
              MIL1553B bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:MIL1553B:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:MIL1553B:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:MIL1553B:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:MIL1553B:SUPPortedfields {DATa|PAYLoad}
            - MATH:MATH<x>:MIL1553B:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
            - ``PAYLoad`` sets the field type to PAYLoad.
        """
        return self._supportedfields


class MathMathItemMdioSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:MDIO:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for MDIO bus.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:MDIO:SUPPortedfields?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:MDIO:SUPPortedfields?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:MDIO:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:MDIO:SUPPortedfields {DATa}
        - MATH:MATH<x>:MDIO:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
    """


class MathMathItemMdio(SCPICmdRead):
    """The ``MATH:MATH<x>:MDIO`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:MDIO?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:MDIO?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:MDIO:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemMdioSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemMdioSupportedfields:
        """Return the ``MATH:MATH<x>:MDIO:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for MDIO
              bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:MDIO:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:MDIO:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:MDIO:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:MDIO:SUPPortedfields {DATa}
            - MATH:MATH<x>:MDIO:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
        """
        return self._supportedfields


class MathMathItemLinSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:LIN:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for LIN bus.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:LIN:SUPPortedfields?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LIN:SUPPortedfields?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:LIN:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:LIN:SUPPortedfields {DATa}
        - MATH:MATH<x>:LIN:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
    """


class MathMathItemLin(SCPICmdRead):
    """The ``MATH:MATH<x>:LIN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:LIN?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LIN?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:LIN:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemLinSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemLinSupportedfields:
        """Return the ``MATH:MATH<x>:LIN:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for LIN
              bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:LIN:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:LIN:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:LIN:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:LIN:SUPPortedfields {DATa}
            - MATH:MATH<x>:LIN:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
        """
        return self._supportedfields


class MathMathItemLabelYpos(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:LABel:YPOS`` command.

    Description:
        - This command sets or queries the y-position of the specified math label. The Math waveform
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:YPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:YPOS?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:LABel:YPOS value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:LABel:YPOS <NR1>
        - MATH:MATH<x>:LABel:YPOS?
        ```

    Info:
        - ``<NR1>`` is the location (in pixels) where the label for the selected math waveform is
          displayed, relative to the baseline of the waveform.
    """


class MathMathItemLabelXpos(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:LABel:XPOS`` command.

    Description:
        - This command sets or queries the X position of the specified math label. Maths are
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:XPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:XPOS?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:LABel:XPOS value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:LABel:XPOS <NR1>
        - MATH:MATH<x>:LABel:XPOS?
        ```

    Info:
        - ``<NR1>`` is the location (in pixels) where the label for the selected math waveform is
          displayed, relative to the left edge of the display.
    """


class MathMathItemLabelName(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:LABel:NAMe`` command.

    Description:
        - This command sets or queries the label string, which is used for annotating the math
          waveform on the screen. The math waveform to which the label is attached is specified by
          x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:NAMe?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:NAMe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:LABel:NAMe value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:LABel:NAMe <QString>
        - MATH:MATH<x>:LABel:NAMe?
        ```

    Info:
        - ``<QString>`` specifies the label to annotate the math waveform.
    """

    _WRAP_ARG_WITH_QUOTES = True


class MathMathItemLabelFontUnderline(SCPICmdWrite):
    """The ``MATH:MATH<x>:LABel:FONT:UNDERline`` command.

    Description:
        - This command sets or queries the underline state of the specified math label. The math
          waveform is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:LABel:FONT:UNDERline value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:LABel:FONT:UNDERline {ON|OFF|<NR1>}
        ```

    Info:
        - ``<NR1>`` = 0 turns off underline, and any other integer turns on underline.
        - ``OFF`` turns off underline.
        - ``ON`` turns on underline.
    """


class MathMathItemLabelFontType(SCPICmdWrite):
    """The ``MATH:MATH<x>:LABel:FONT:TYPE`` command.

    Description:
        - This command sets or queries font type of the specified math label, such as Arial or Times
          New Roman. The math waveform is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:LABel:FONT:TYPE value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:LABel:FONT:TYPE <QString>
        ```

    Info:
        - ``<QString>`` is the name of the font type.
    """

    _WRAP_ARG_WITH_QUOTES = True


class MathMathItemLabelFontSize(SCPICmdWrite):
    """The ``MATH:MATH<x>:LABel:FONT:SIZE`` command.

    Description:
        - This command sets or queries font size of the specified math label. The math waveform is
          specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:LABel:FONT:SIZE value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:LABel:FONT:SIZE <NR1>
        ```

    Info:
        - ``<NR1>`` sets the label size in points.
    """


class MathMathItemLabelFontItalic(SCPICmdWrite):
    """The ``MATH:MATH<x>:LABel:FONT:ITALic`` command.

    Description:
        - This command sets or queries italic state of the specified math label. The math waveform
          is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:LABel:FONT:ITALic value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:LABel:FONT:ITALic {ON|OFF|<NR1>}
        ```

    Info:
        - ``<NR1>`` = 0 turns off italic, and any other integer turns on italic.
        - ``OFF`` turns off italic.
        - ``ON`` turns on italic.
    """


class MathMathItemLabelFontBold(SCPICmdWrite):
    """The ``MATH:MATH<x>:LABel:FONT:BOLD`` command.

    Description:
        - This command sets or queries the bold state of the specified math label. The math waveform
          is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:LABel:FONT:BOLD value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:LABel:FONT:BOLD {ON|OFF|<NR1>}
        ```

    Info:
        - ``<NR1>`` = 0 turns off bold, and any other integer turns on bold.
        - ``OFF`` turns off bold.
        - ``ON`` turns on bold.
    """


class MathMathItemLabelFont(SCPICmdRead):
    """The ``MATH:MATH<x>:LABel:FONT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:FONT?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:FONT?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bold``: The ``MATH:MATH<x>:LABel:FONT:BOLD`` command.
        - ``.italic``: The ``MATH:MATH<x>:LABel:FONT:ITALic`` command.
        - ``.size``: The ``MATH:MATH<x>:LABel:FONT:SIZE`` command.
        - ``.type``: The ``MATH:MATH<x>:LABel:FONT:TYPE`` command.
        - ``.underline``: The ``MATH:MATH<x>:LABel:FONT:UNDERline`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bold = MathMathItemLabelFontBold(device, f"{self._cmd_syntax}:BOLD")
        self._italic = MathMathItemLabelFontItalic(device, f"{self._cmd_syntax}:ITALic")
        self._size = MathMathItemLabelFontSize(device, f"{self._cmd_syntax}:SIZE")
        self._type = MathMathItemLabelFontType(device, f"{self._cmd_syntax}:TYPE")
        self._underline = MathMathItemLabelFontUnderline(device, f"{self._cmd_syntax}:UNDERline")

    @property
    def bold(self) -> MathMathItemLabelFontBold:
        """Return the ``MATH:MATH<x>:LABel:FONT:BOLD`` command.

        Description:
            - This command sets or queries the bold state of the specified math label. The math
              waveform is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:LABel:FONT:BOLD value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:LABel:FONT:BOLD {ON|OFF|<NR1>}
            ```

        Info:
            - ``<NR1>`` = 0 turns off bold, and any other integer turns on bold.
            - ``OFF`` turns off bold.
            - ``ON`` turns on bold.
        """
        return self._bold

    @property
    def italic(self) -> MathMathItemLabelFontItalic:
        """Return the ``MATH:MATH<x>:LABel:FONT:ITALic`` command.

        Description:
            - This command sets or queries italic state of the specified math label. The math
              waveform is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:LABel:FONT:ITALic value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:LABel:FONT:ITALic {ON|OFF|<NR1>}
            ```

        Info:
            - ``<NR1>`` = 0 turns off italic, and any other integer turns on italic.
            - ``OFF`` turns off italic.
            - ``ON`` turns on italic.
        """
        return self._italic

    @property
    def size(self) -> MathMathItemLabelFontSize:
        """Return the ``MATH:MATH<x>:LABel:FONT:SIZE`` command.

        Description:
            - This command sets or queries font size of the specified math label. The math waveform
              is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:LABel:FONT:SIZE value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:LABel:FONT:SIZE <NR1>
            ```

        Info:
            - ``<NR1>`` sets the label size in points.
        """
        return self._size

    @property
    def type(self) -> MathMathItemLabelFontType:
        """Return the ``MATH:MATH<x>:LABel:FONT:TYPE`` command.

        Description:
            - This command sets or queries font type of the specified math label, such as Arial or
              Times New Roman. The math waveform is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:LABel:FONT:TYPE value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:LABel:FONT:TYPE <QString>
            ```

        Info:
            - ``<QString>`` is the name of the font type.
        """
        return self._type

    @property
    def underline(self) -> MathMathItemLabelFontUnderline:
        """Return the ``MATH:MATH<x>:LABel:FONT:UNDERline`` command.

        Description:
            - This command sets or queries the underline state of the specified math label. The math
              waveform is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:LABel:FONT:UNDERline value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:LABel:FONT:UNDERline {ON|OFF|<NR1>}
            ```

        Info:
            - ``<NR1>`` = 0 turns off underline, and any other integer turns on underline.
            - ``OFF`` turns off underline.
            - ``ON`` turns on underline.
        """
        return self._underline


class MathMathItemLabelColor(SCPICmdWrite):
    """The ``MATH:MATH<x>:LABel:COLor`` command.

    Description:
        - This command sets or queries color of the specified math's label. The math waveform is
          specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:LABel:COLor value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:LABel:COLor <QString>
        ```

    Info:
        - ``<QString`` > is the color of the label. To return the color to the default color, send
          an empty string as in this example: ``:MATH:MATH1:LABEL:COLOR`` ''.
    """

    _WRAP_ARG_WITH_QUOTES = True


class MathMathItemLabel(SCPICmdRead):
    """The ``MATH:MATH<x>:LABel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.color``: The ``MATH:MATH<x>:LABel:COLor`` command.
        - ``.font``: The ``MATH:MATH<x>:LABel:FONT`` command tree.
        - ``.name``: The ``MATH:MATH<x>:LABel:NAMe`` command.
        - ``.xpos``: The ``MATH:MATH<x>:LABel:XPOS`` command.
        - ``.ypos``: The ``MATH:MATH<x>:LABel:YPOS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._color = MathMathItemLabelColor(device, f"{self._cmd_syntax}:COLor")
        self._font = MathMathItemLabelFont(device, f"{self._cmd_syntax}:FONT")
        self._name = MathMathItemLabelName(device, f"{self._cmd_syntax}:NAMe")
        self._xpos = MathMathItemLabelXpos(device, f"{self._cmd_syntax}:XPOS")
        self._ypos = MathMathItemLabelYpos(device, f"{self._cmd_syntax}:YPOS")

    @property
    def color(self) -> MathMathItemLabelColor:
        """Return the ``MATH:MATH<x>:LABel:COLor`` command.

        Description:
            - This command sets or queries color of the specified math's label. The math waveform is
              specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:LABel:COLor value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:LABel:COLor <QString>
            ```

        Info:
            - ``<QString`` > is the color of the label. To return the color to the default color,
              send an empty string as in this example: ``:MATH:MATH1:LABEL:COLOR`` ''.
        """
        return self._color

    @property
    def font(self) -> MathMathItemLabelFont:
        """Return the ``MATH:MATH<x>:LABel:FONT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:FONT?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:FONT?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bold``: The ``MATH:MATH<x>:LABel:FONT:BOLD`` command.
            - ``.italic``: The ``MATH:MATH<x>:LABel:FONT:ITALic`` command.
            - ``.size``: The ``MATH:MATH<x>:LABel:FONT:SIZE`` command.
            - ``.type``: The ``MATH:MATH<x>:LABel:FONT:TYPE`` command.
            - ``.underline``: The ``MATH:MATH<x>:LABel:FONT:UNDERline`` command.
        """
        return self._font

    @property
    def name(self) -> MathMathItemLabelName:
        """Return the ``MATH:MATH<x>:LABel:NAMe`` command.

        Description:
            - This command sets or queries the label string, which is used for annotating the math
              waveform on the screen. The math waveform to which the label is attached is specified
              by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:NAMe?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:NAMe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:LABel:NAMe value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:LABel:NAMe <QString>
            - MATH:MATH<x>:LABel:NAMe?
            ```

        Info:
            - ``<QString>`` specifies the label to annotate the math waveform.
        """
        return self._name

    @property
    def xpos(self) -> MathMathItemLabelXpos:
        """Return the ``MATH:MATH<x>:LABel:XPOS`` command.

        Description:
            - This command sets or queries the X position of the specified math label. Maths are
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:XPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:XPOS?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:LABel:XPOS value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:LABel:XPOS <NR1>
            - MATH:MATH<x>:LABel:XPOS?
            ```

        Info:
            - ``<NR1>`` is the location (in pixels) where the label for the selected math waveform
              is displayed, relative to the left edge of the display.
        """
        return self._xpos

    @property
    def ypos(self) -> MathMathItemLabelYpos:
        """Return the ``MATH:MATH<x>:LABel:YPOS`` command.

        Description:
            - This command sets or queries the y-position of the specified math label. The Math
              waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:YPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:YPOS?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:LABel:YPOS value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:LABel:YPOS <NR1>
            - MATH:MATH<x>:LABel:YPOS?
            ```

        Info:
            - ``<NR1>`` is the location (in pixels) where the label for the selected math waveform
              is displayed, relative to the baseline of the waveform.
        """
        return self._ypos


class MathMathItemInterpolation(SCPICmdWrite):
    """The ``MATH:MATH<x>:INTERpolation`` command.

    Description:
        - This command sets or queries whether sinc interpolation is enabled for math on bus source.
          The math waveform is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:INTERpolation value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:INTERpolation {ON|OFF}
        ```

    Info:
        - ``ON`` indicates that the sinc interpolation is used for math waveform.
        - ``OFF`` indicates no interpolation is used for math waveform. Waveform will appear
          'stair-steppy' in this case.
    """


class MathMathItemI3cSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:I3C:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for I3Cbus.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:I3C:SUPPortedfields?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:I3C:SUPPortedfields?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:I3C:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:I3C:SUPPortedfields {DATa}
        - MATH:MATH<x>:I3C:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
    """


class MathMathItemI3c(SCPICmdRead):
    """The ``MATH:MATH<x>:I3C`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:I3C?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:I3C?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:I3C:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemI3cSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemI3cSupportedfields:
        """Return the ``MATH:MATH<x>:I3C:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for
              I3Cbus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:I3C:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:I3C:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:I3C:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:I3C:SUPPortedfields {DATa}
            - MATH:MATH<x>:I3C:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
        """
        return self._supportedfields


class MathMathItemI2cSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:I2C:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for I2C bus.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:I2C:SUPPortedfields?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:I2C:SUPPortedfields?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:I2C:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:I2C:SUPPortedfields {DATa}
        - MATH:MATH<x>:I2C:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
    """


class MathMathItemI2c(SCPICmdRead):
    """The ``MATH:MATH<x>:I2C`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:I2C?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:I2C?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:I2C:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemI2cSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemI2cSupportedfields:
        """Return the ``MATH:MATH<x>:I2C:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for I2C
              bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:I2C:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:I2C:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:I2C:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:I2C:SUPPortedfields {DATa}
            - MATH:MATH<x>:I2C:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
        """
        return self._supportedfields


class MathMathItemGating(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:GATing`` command.

    Description:
        - This command specifies or returns the gating setting. It only applies to Math FFT plots.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:GATing?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:GATing?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:GATing value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:GATing {NONE|SCREEN|CURSor}
        - MATH:MATH<x>:GATing?
        ```

    Info:
        - ``NONE`` turns off math gating.
        - ``SCREEN`` turns on gating, using the left and right edges of the screen.
        - ``CURSor`` limits math to the portion of the waveform between the vertical bar cursors,
          even if they are off screen.
    """


class MathMathItemFunction(SCPICmdWrite):
    """The ``MATH:MATH<x>:FUNCtion`` command.

    Description:
        - This command sets or queries the basic math arithmetic function. The math waveform is
          specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FUNCtion value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:FUNCtion {ADD|SUBtract|MULTiply|DIVide}
        ```

    Info:
        - ``ADD`` sets the basic math function to add.
        - ``SUBtract`` sets the basic math function to subtract.
        - ``MULTiply`` sets the basic math function to multiply.
        - ``DIVide`` sets the basic math function to divide.
    """


class MathMathItemFlexraySupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:FLEXray:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for FLEXray
          bus. The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:FLEXray:SUPPortedfields?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MATH:MATH<x>:FLEXray:SUPPortedfields?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:FLEXray:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:FLEXray:SUPPortedfields {DATa}
        - MATH:MATH<x>:FLEXray:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
    """


class MathMathItemFlexray(SCPICmdRead):
    """The ``MATH:MATH<x>:FLEXray`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:FLEXray?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FLEXray?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:FLEXray:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemFlexraySupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemFlexraySupportedfields:
        """Return the ``MATH:MATH<x>:FLEXray:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for
              FLEXray bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:FLEXray:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:FLEXray:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:FLEXray:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:FLEXray:SUPPortedfields {DATa}
            - MATH:MATH<x>:FLEXray:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
        """
        return self._supportedfields


class MathMathItemFilterType(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:FILTer:TYPe`` command.

    Description:
        - This command specifies or queries the filter type. The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:TYPe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:TYPe value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:FILTer:TYPe {LPASs|HPASs|BPASs|BSTop|APASs|HILBert|DIFFerentiator|RC|RRC}
        - MATH:MATH<x>:FILTer:TYPe?
        ```

    Info:
        - ``LPASs`` specifies the filter type as LPASs.
        - ``HPASs`` specifies the filter type as HPASs.
        - ``BPASs`` specifies the filter type as BPASs.
        - ``BSTop`` specifies the filter type as BSTop.
        - ``APASs`` specifies the filter type as APASs.
        - ``HILBert`` specifies the filter type as HILBert.
        - ``DIFFerentiator`` specifies the filter type as DIFFerentiator.
        - ``RC`` specifies the filter type as RC.
        - ``RRC`` specifies the filter type as RRC.
    """


class MathMathItemFilterTwidth(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:FILTer:TWIDth`` command.

    Description:
        - This command sets or queries the filter Transition Width for Custom filter response. The
          math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:TWIDth?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:TWIDth?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:TWIDth value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:FILTer:TWIDth <NR3>
        - MATH:MATH<x>:FILTer:TWIDth?
        ```

    Info:
        - ``<NR3>`` specifies the Transition Width for Custom filter response.
    """


class MathMathItemFilterSymbols(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:FILTer:SYMBols`` command.

    Description:
        - This command sets or queries the symbol for raised cosine or root raised cosine filter.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:SYMBols?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:SYMBols?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:SYMBols value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:FILTer:SYMBols <NR1>
        - MATH:MATH<x>:FILTer:SYMBols?
        ```

    Info:
        - ``<NR1>`` specifies the number of symbols for Raised-Cosine (RC) filter type.
    """


class MathMathItemFilterSource(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:FILTer:SOURce`` command.

    Description:
        - This command sets or queries the math waveform filter source. The math waveform and source
          are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:SOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:SOURce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:SOURce value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:FILTer:SOURce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - MATH:MATH<x>:FILTer:SOURce?
        ```

    Info:
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``Math<x>`` specifies a math waveform as the source.
        - ``REF<x>`` specifies a reference waveform as the source.
    """


class MathMathItemFilterSduration(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:FILTer:SDURation`` command.

    Description:
        - This command sets or queries the symbol duration for raised cosine or root raised cosine
          filter. The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:SDURation?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:SDURation?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:SDURation value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:FILTer:SDURation <NR3>
        - MATH:MATH<x>:FILTer:SDURation?
        ```

    Info:
        - ``<NR3>`` specifies the number of symbol duration for Root-Raised-Cosine (RRC) filter
          type.
    """


class MathMathItemFilterSdeviation(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:FILTer:SDEViation`` command.

    Description:
        - This command sets or queries the standard deviation in Gaussian filter. The math waveform
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:SDEViation?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:SDEViation?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:SDEViation value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:FILTer:SDEViation <NR3>
        - MATH:MATH<x>:FILTer:SDEViation?
        ```

    Info:
        - ``<NR3>`` sets the standard deviation in gaussian filter.
    """


class MathMathItemFilterSaveResponse(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:FILTer:SAVe:RESPonse`` command.

    Description:
        - This command set the filter response images to be saved while saving the filter file. The
          math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:SAVe:RESPonse?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:SAVe:RESPonse?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:FILTer:SAVe:RESPonse value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:FILTer:SAVe:RESPonse {1|0}
        - MATH:MATH<x>:FILTer:SAVe:RESPonse?
        ```

    Info:
        - ``1`` enables the save of the filter response image.
        - ``0`` disables the save of the filter response image. This is the default value.
    """


class MathMathItemFilterSave(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:FILTer:SAVe`` command.

    Description:
        - This command saves the filter file. The math waveform is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:SAVe value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:FILTer:SAVe <QString>
        ```

    Info:
        - ``<QString>`` saves the created filter in .flt format to the specified save location.

    Properties:
        - ``.response``: The ``MATH:MATH<x>:FILTer:SAVe:RESPonse`` command.
    """

    _WRAP_ARG_WITH_QUOTES = True

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._response = MathMathItemFilterSaveResponse(device, f"{self._cmd_syntax}:RESPonse")

    @property
    def response(self) -> MathMathItemFilterSaveResponse:
        """Return the ``MATH:MATH<x>:FILTer:SAVe:RESPonse`` command.

        Description:
            - This command set the filter response images to be saved while saving the filter file.
              The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:SAVe:RESPonse?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:FILTer:SAVe:RESPonse?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:FILTer:SAVe:RESPonse value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:FILTer:SAVe:RESPonse {1|0}
            - MATH:MATH<x>:FILTer:SAVe:RESPonse?
            ```

        Info:
            - ``1`` enables the save of the filter response image.
            - ``0`` disables the save of the filter response image. This is the default value.
        """
        return self._response


class MathMathItemFilterSattenuation(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:FILTer:SATTenuation`` command.

    Description:
        - This command sets or queries the stop band attenuation in the filter response. The math
          waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:SATTenuation?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:SATTenuation?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:FILTer:SATTenuation value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:FILTer:SATTenuation <NR3>
        - MATH:MATH<x>:FILTer:SATTenuation?
        ```

    Info:
        - ``<NR3>`` sets the stop band attenuation in the filter response.
    """


class MathMathItemFilterRofactor(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:FILTer:ROFactor`` command.

    Description:
        - This command sets or queries roll off factor for raised cosine or root raised cosine
          filter. The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:ROFactor?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:ROFactor?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:ROFactor value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:FILTer:ROFactor <NR3>
        - MATH:MATH<x>:FILTer:ROFactor?
        ```

    Info:
        - ``<NR1>`` specifies the Roll-off Factor value for Rasied-Cosine(RC) filter type.
    """


class MathMathItemFilterResponse(SCPICmdWrite):
    """The ``MATH:MATH<x>:FILTer:RESPonse`` command.

    Description:
        - This command will load the filter responses and automatically apply filter option. The
          math waveform is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:RESPonse value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:FILTer:RESPonse {BUTTerworth|CHEBYONe|CHEBYTWo|ELLiptical|GAUSsian|BESSelCUSTom}
        ```

    Info:
        - ``BUTTerworth`` specifies the filter response as BUTTerworth.
        - ``CHEBYONe`` specifies the filter response as CHEBYONe.
        - ``CHEBYTWo`` specifies the filter response as CHEBYTWo.
        - ``ELLiptical`` specifies the filter response as ELLiptical.
        - ``GAUSsian`` specifies the filter response as GAUSsian.
        - ``BESSelCUSTom`` specifies the filter response as BESSelCUSTom.
    """  # noqa: E501


class MathMathItemFilterPripple(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:FILTer:PRIPple`` command.

    Description:
        - This command sets or queries the pass band ripple in the filter response. The math
          waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:PRIPple?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:PRIPple?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:PRIPple value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:FILTer:PRIPple <NR3>
        - MATH:MATH<x>:FILTer:PRIPple?
        ```

    Info:
        - ``<NR3>`` sets the pass band ripple in the filter response.
    """


class MathMathItemFilterOrder(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:FILTer:ORDer`` command.

    Description:
        - This command sets or queries the filter order. The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:ORDer?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:ORDer?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:ORDer value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:FILTer:ORDer <NR1>
        - MATH:MATH<x>:FILTer:ORDer?
        ```

    Info:
        - ``<NR1>`` sets the filter order.
    """


class MathMathItemFilterLoadResponse(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:FILTer:LOAD:RESPonse`` command.

    Description:
        - This command will load the filter responses and automatically apply filter option. The
          math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:LOAD:RESPonse?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:LOAD:RESPonse?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:FILTer:LOAD:RESPonse value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:FILTer:LOAD:RESPonse {1|0}
        - MATH:MATH<x>:FILTer:LOAD:RESPonse?
        ```

    Info:
        - ``1`` enables recall of filter response image.
        - ``0`` disables recall of filter response image.
    """


class MathMathItemFilterLoad(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:FILTer:LOAD`` command.

    Description:
        - This command loads the filter file. The math waveform is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:LOAD value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:FILTer:LOAD <QString>
        ```

    Info:
        - ``<QString>`` sets the path to the filter file to load. Linux default location is C:.
          Windows default location is C:UsersPublicTektronixTekScopeFilters.

    Properties:
        - ``.response``: The ``MATH:MATH<x>:FILTer:LOAD:RESPonse`` command.
    """

    _WRAP_ARG_WITH_QUOTES = True

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._response = MathMathItemFilterLoadResponse(device, f"{self._cmd_syntax}:RESPonse")

    @property
    def response(self) -> MathMathItemFilterLoadResponse:
        """Return the ``MATH:MATH<x>:FILTer:LOAD:RESPonse`` command.

        Description:
            - This command will load the filter responses and automatically apply filter option. The
              math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:LOAD:RESPonse?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:FILTer:LOAD:RESPonse?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:FILTer:LOAD:RESPonse value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:FILTer:LOAD:RESPonse {1|0}
            - MATH:MATH<x>:FILTer:LOAD:RESPonse?
            ```

        Info:
            - ``1`` enables recall of filter response image.
            - ``0`` disables recall of filter response image.
        """
        return self._response


class MathMathItemFilterLcfreq(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:FILTer:LCFReq`` command.

    Description:
        - This command sets or queries the low cutoff frequency for bandpass or band stop filter.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:LCFReq?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:LCFReq?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:LCFReq value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:FILTer:LCFReq <NR3>
        - MATH:MATH<x>:FILTer:LCFReq?
        ```

    Info:
        - ``<NR3>`` sets the low cutoff frequency for bandpass or band stop filter.
    """


class MathMathItemFilterInfo(SCPICmdRead):
    """The ``MATH:MATH<x>:FILTer:INFo`` command.

    Description:
        - This command returns filter information output when the user creates a filter. The math
          waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:INFo?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:INFo?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:FILTer:INFo?
        ```
    """


class MathMathItemFilterHcfreq(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:FILTer:HCFReq`` command.

    Description:
        - This command sets or queries the high cutoff frequency for bandpass or band stop filter.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:HCFReq?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:HCFReq?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:HCFReq value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:FILTer:HCFReq <NR3>
        - MATH:MATH<x>:FILTer:HCFReq?
        ```

    Info:
        - ``<NR3>`` sets the high cutoff frequency for bandpass or band stop filter.
    """


class MathMathItemFilterDesign(SCPICmdWrite):
    """The ``MATH:MATH<x>:FILTer:DESIgn`` command.

    Description:
        - This command performs filter specific Apply, Abort, and Generate operations. The math
          waveform is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:DESIgn value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:FILTer:DESIgn {EXECUTE|ABORT|APPLY}
        ```

    Info:
        - ``EXECUTE`` executes filter file creation.
        - ``APPLY`` applies the filter definition on the Math waveform.
        - ``ABORT`` aborts the filter execution.
    """


class MathMathItemFilterDelay(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:FILTer:DELay`` command.

    Description:
        - This command sets or queries the delay for all pass filter. The math waveform is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:DELay?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:DELay?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:DELay value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:FILTer:DELay <NR3>
        - MATH:MATH<x>:FILTer:DELay?
        ```

    Info:
        - ``<NR3>`` sets the delay for all pass filter.
    """


class MathMathItemFilterCfreq(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:FILTer:CFReq`` command.

    Description:
        - This command sets or queries the filter cutoff frequency. The math waveform is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:CFReq?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:CFReq?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:CFReq value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:FILTer:CFReq <NR3>
        - MATH:MATH<x>:FILTer:CFReq?
        ```

    Info:
        - ``<NR3>`` sets the filter cutoff frequency.
    """


#  pylint: disable=too-many-instance-attributes
class MathMathItemFilter(SCPICmdRead):
    """The ``MATH:MATH<x>:FILTer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.cfreq``: The ``MATH:MATH<x>:FILTer:CFReq`` command.
        - ``.delay``: The ``MATH:MATH<x>:FILTer:DELay`` command.
        - ``.design``: The ``MATH:MATH<x>:FILTer:DESIgn`` command.
        - ``.hcfreq``: The ``MATH:MATH<x>:FILTer:HCFReq`` command.
        - ``.info``: The ``MATH:MATH<x>:FILTer:INFo`` command.
        - ``.lcfreq``: The ``MATH:MATH<x>:FILTer:LCFReq`` command.
        - ``.load``: The ``MATH:MATH<x>:FILTer:LOAD`` command.
        - ``.order``: The ``MATH:MATH<x>:FILTer:ORDer`` command.
        - ``.pripple``: The ``MATH:MATH<x>:FILTer:PRIPple`` command.
        - ``.response``: The ``MATH:MATH<x>:FILTer:RESPonse`` command.
        - ``.rofactor``: The ``MATH:MATH<x>:FILTer:ROFactor`` command.
        - ``.sattenuation``: The ``MATH:MATH<x>:FILTer:SATTenuation`` command.
        - ``.save``: The ``MATH:MATH<x>:FILTer:SAVe`` command.
        - ``.sdeviation``: The ``MATH:MATH<x>:FILTer:SDEViation`` command.
        - ``.sduration``: The ``MATH:MATH<x>:FILTer:SDURation`` command.
        - ``.source``: The ``MATH:MATH<x>:FILTer:SOURce`` command.
        - ``.symbols``: The ``MATH:MATH<x>:FILTer:SYMBols`` command.
        - ``.twidth``: The ``MATH:MATH<x>:FILTer:TWIDth`` command.
        - ``.type``: The ``MATH:MATH<x>:FILTer:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._cfreq = MathMathItemFilterCfreq(device, f"{self._cmd_syntax}:CFReq")
        self._delay = MathMathItemFilterDelay(device, f"{self._cmd_syntax}:DELay")
        self._design = MathMathItemFilterDesign(device, f"{self._cmd_syntax}:DESIgn")
        self._hcfreq = MathMathItemFilterHcfreq(device, f"{self._cmd_syntax}:HCFReq")
        self._info = MathMathItemFilterInfo(device, f"{self._cmd_syntax}:INFo")
        self._lcfreq = MathMathItemFilterLcfreq(device, f"{self._cmd_syntax}:LCFReq")
        self._load = MathMathItemFilterLoad(device, f"{self._cmd_syntax}:LOAD")
        self._order = MathMathItemFilterOrder(device, f"{self._cmd_syntax}:ORDer")
        self._pripple = MathMathItemFilterPripple(device, f"{self._cmd_syntax}:PRIPple")
        self._response = MathMathItemFilterResponse(device, f"{self._cmd_syntax}:RESPonse")
        self._rofactor = MathMathItemFilterRofactor(device, f"{self._cmd_syntax}:ROFactor")
        self._sattenuation = MathMathItemFilterSattenuation(
            device, f"{self._cmd_syntax}:SATTenuation"
        )
        self._save = MathMathItemFilterSave(device, f"{self._cmd_syntax}:SAVe")
        self._sdeviation = MathMathItemFilterSdeviation(device, f"{self._cmd_syntax}:SDEViation")
        self._sduration = MathMathItemFilterSduration(device, f"{self._cmd_syntax}:SDURation")
        self._source = MathMathItemFilterSource(device, f"{self._cmd_syntax}:SOURce")
        self._symbols = MathMathItemFilterSymbols(device, f"{self._cmd_syntax}:SYMBols")
        self._twidth = MathMathItemFilterTwidth(device, f"{self._cmd_syntax}:TWIDth")
        self._type = MathMathItemFilterType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def cfreq(self) -> MathMathItemFilterCfreq:
        """Return the ``MATH:MATH<x>:FILTer:CFReq`` command.

        Description:
            - This command sets or queries the filter cutoff frequency. The math waveform is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:CFReq?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:CFReq?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:CFReq value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:FILTer:CFReq <NR3>
            - MATH:MATH<x>:FILTer:CFReq?
            ```

        Info:
            - ``<NR3>`` sets the filter cutoff frequency.
        """
        return self._cfreq

    @property
    def delay(self) -> MathMathItemFilterDelay:
        """Return the ``MATH:MATH<x>:FILTer:DELay`` command.

        Description:
            - This command sets or queries the delay for all pass filter. The math waveform is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:DELay?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:DELay?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:DELay value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:FILTer:DELay <NR3>
            - MATH:MATH<x>:FILTer:DELay?
            ```

        Info:
            - ``<NR3>`` sets the delay for all pass filter.
        """
        return self._delay

    @property
    def design(self) -> MathMathItemFilterDesign:
        """Return the ``MATH:MATH<x>:FILTer:DESIgn`` command.

        Description:
            - This command performs filter specific Apply, Abort, and Generate operations. The math
              waveform is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:DESIgn value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:FILTer:DESIgn {EXECUTE|ABORT|APPLY}
            ```

        Info:
            - ``EXECUTE`` executes filter file creation.
            - ``APPLY`` applies the filter definition on the Math waveform.
            - ``ABORT`` aborts the filter execution.
        """
        return self._design

    @property
    def hcfreq(self) -> MathMathItemFilterHcfreq:
        """Return the ``MATH:MATH<x>:FILTer:HCFReq`` command.

        Description:
            - This command sets or queries the high cutoff frequency for bandpass or band stop
              filter. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:HCFReq?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:HCFReq?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:HCFReq value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:FILTer:HCFReq <NR3>
            - MATH:MATH<x>:FILTer:HCFReq?
            ```

        Info:
            - ``<NR3>`` sets the high cutoff frequency for bandpass or band stop filter.
        """
        return self._hcfreq

    @property
    def info(self) -> MathMathItemFilterInfo:
        """Return the ``MATH:MATH<x>:FILTer:INFo`` command.

        Description:
            - This command returns filter information output when the user creates a filter. The
              math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:INFo?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:INFo?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:FILTer:INFo?
            ```
        """
        return self._info

    @property
    def lcfreq(self) -> MathMathItemFilterLcfreq:
        """Return the ``MATH:MATH<x>:FILTer:LCFReq`` command.

        Description:
            - This command sets or queries the low cutoff frequency for bandpass or band stop
              filter. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:LCFReq?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:LCFReq?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:LCFReq value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:FILTer:LCFReq <NR3>
            - MATH:MATH<x>:FILTer:LCFReq?
            ```

        Info:
            - ``<NR3>`` sets the low cutoff frequency for bandpass or band stop filter.
        """
        return self._lcfreq

    @property
    def load(self) -> MathMathItemFilterLoad:
        """Return the ``MATH:MATH<x>:FILTer:LOAD`` command.

        Description:
            - This command loads the filter file. The math waveform is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:LOAD value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:FILTer:LOAD <QString>
            ```

        Info:
            - ``<QString>`` sets the path to the filter file to load. Linux default location is C:.
              Windows default location is C:UsersPublicTektronixTekScopeFilters.

        Sub-properties:
            - ``.response``: The ``MATH:MATH<x>:FILTer:LOAD:RESPonse`` command.
        """
        return self._load

    @property
    def order(self) -> MathMathItemFilterOrder:
        """Return the ``MATH:MATH<x>:FILTer:ORDer`` command.

        Description:
            - This command sets or queries the filter order. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:ORDer?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:ORDer?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:ORDer value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:FILTer:ORDer <NR1>
            - MATH:MATH<x>:FILTer:ORDer?
            ```

        Info:
            - ``<NR1>`` sets the filter order.
        """
        return self._order

    @property
    def pripple(self) -> MathMathItemFilterPripple:
        """Return the ``MATH:MATH<x>:FILTer:PRIPple`` command.

        Description:
            - This command sets or queries the pass band ripple in the filter response. The math
              waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:PRIPple?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:PRIPple?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:PRIPple value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:FILTer:PRIPple <NR3>
            - MATH:MATH<x>:FILTer:PRIPple?
            ```

        Info:
            - ``<NR3>`` sets the pass band ripple in the filter response.
        """
        return self._pripple

    @property
    def response(self) -> MathMathItemFilterResponse:
        """Return the ``MATH:MATH<x>:FILTer:RESPonse`` command.

        Description:
            - This command will load the filter responses and automatically apply filter option. The
              math waveform is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:FILTer:RESPonse value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:FILTer:RESPonse {BUTTerworth|CHEBYONe|CHEBYTWo|ELLiptical|GAUSsian|BESSelCUSTom}
            ```

        Info:
            - ``BUTTerworth`` specifies the filter response as BUTTerworth.
            - ``CHEBYONe`` specifies the filter response as CHEBYONe.
            - ``CHEBYTWo`` specifies the filter response as CHEBYTWo.
            - ``ELLiptical`` specifies the filter response as ELLiptical.
            - ``GAUSsian`` specifies the filter response as GAUSsian.
            - ``BESSelCUSTom`` specifies the filter response as BESSelCUSTom.
        """  # noqa: E501
        return self._response

    @property
    def rofactor(self) -> MathMathItemFilterRofactor:
        """Return the ``MATH:MATH<x>:FILTer:ROFactor`` command.

        Description:
            - This command sets or queries roll off factor for raised cosine or root raised cosine
              filter. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:ROFactor?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:ROFactor?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:FILTer:ROFactor value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:FILTer:ROFactor <NR3>
            - MATH:MATH<x>:FILTer:ROFactor?
            ```

        Info:
            - ``<NR1>`` specifies the Roll-off Factor value for Rasied-Cosine(RC) filter type.
        """
        return self._rofactor

    @property
    def sattenuation(self) -> MathMathItemFilterSattenuation:
        """Return the ``MATH:MATH<x>:FILTer:SATTenuation`` command.

        Description:
            - This command sets or queries the stop band attenuation in the filter response. The
              math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:SATTenuation?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:FILTer:SATTenuation?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:FILTer:SATTenuation value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:FILTer:SATTenuation <NR3>
            - MATH:MATH<x>:FILTer:SATTenuation?
            ```

        Info:
            - ``<NR3>`` sets the stop band attenuation in the filter response.
        """
        return self._sattenuation

    @property
    def save(self) -> MathMathItemFilterSave:
        """Return the ``MATH:MATH<x>:FILTer:SAVe`` command.

        Description:
            - This command saves the filter file. The math waveform is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:SAVe value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:FILTer:SAVe <QString>
            ```

        Info:
            - ``<QString>`` saves the created filter in .flt format to the specified save location.

        Sub-properties:
            - ``.response``: The ``MATH:MATH<x>:FILTer:SAVe:RESPonse`` command.
        """
        return self._save

    @property
    def sdeviation(self) -> MathMathItemFilterSdeviation:
        """Return the ``MATH:MATH<x>:FILTer:SDEViation`` command.

        Description:
            - This command sets or queries the standard deviation in Gaussian filter. The math
              waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:SDEViation?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:SDEViation?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:FILTer:SDEViation value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:FILTer:SDEViation <NR3>
            - MATH:MATH<x>:FILTer:SDEViation?
            ```

        Info:
            - ``<NR3>`` sets the standard deviation in gaussian filter.
        """
        return self._sdeviation

    @property
    def sduration(self) -> MathMathItemFilterSduration:
        """Return the ``MATH:MATH<x>:FILTer:SDURation`` command.

        Description:
            - This command sets or queries the symbol duration for raised cosine or root raised
              cosine filter. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:SDURation?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:SDURation?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:FILTer:SDURation value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:FILTer:SDURation <NR3>
            - MATH:MATH<x>:FILTer:SDURation?
            ```

        Info:
            - ``<NR3>`` specifies the number of symbol duration for Root-Raised-Cosine (RRC) filter
              type.
        """
        return self._sduration

    @property
    def source(self) -> MathMathItemFilterSource:
        """Return the ``MATH:MATH<x>:FILTer:SOURce`` command.

        Description:
            - This command sets or queries the math waveform filter source. The math waveform and
              source are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:SOURce?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:SOURce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:SOURce value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:FILTer:SOURce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - MATH:MATH<x>:FILTer:SOURce?
            ```

        Info:
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``Math<x>`` specifies a math waveform as the source.
            - ``REF<x>`` specifies a reference waveform as the source.
        """
        return self._source

    @property
    def symbols(self) -> MathMathItemFilterSymbols:
        """Return the ``MATH:MATH<x>:FILTer:SYMBols`` command.

        Description:
            - This command sets or queries the symbol for raised cosine or root raised cosine
              filter. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:SYMBols?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:SYMBols?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:SYMBols value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:FILTer:SYMBols <NR1>
            - MATH:MATH<x>:FILTer:SYMBols?
            ```

        Info:
            - ``<NR1>`` specifies the number of symbols for Raised-Cosine (RC) filter type.
        """
        return self._symbols

    @property
    def twidth(self) -> MathMathItemFilterTwidth:
        """Return the ``MATH:MATH<x>:FILTer:TWIDth`` command.

        Description:
            - This command sets or queries the filter Transition Width for Custom filter response.
              The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:TWIDth?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:TWIDth?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:TWIDth value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:FILTer:TWIDth <NR3>
            - MATH:MATH<x>:FILTer:TWIDth?
            ```

        Info:
            - ``<NR3>`` specifies the Transition Width for Custom filter response.
        """
        return self._twidth

    @property
    def type(self) -> MathMathItemFilterType:
        """Return the ``MATH:MATH<x>:FILTer:TYPe`` command.

        Description:
            - This command specifies or queries the filter type. The math waveform is specified by
              x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer:TYPe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FILTer:TYPe value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:FILTer:TYPe {LPASs|HPASs|BPASs|BSTop|APASs|HILBert|DIFFerentiator|RC|RRC}
            - MATH:MATH<x>:FILTer:TYPe?
            ```

        Info:
            - ``LPASs`` specifies the filter type as LPASs.
            - ``HPASs`` specifies the filter type as HPASs.
            - ``BPASs`` specifies the filter type as BPASs.
            - ``BSTop`` specifies the filter type as BSTop.
            - ``APASs`` specifies the filter type as APASs.
            - ``HILBert`` specifies the filter type as HILBert.
            - ``DIFFerentiator`` specifies the filter type as DIFFerentiator.
            - ``RC`` specifies the filter type as RC.
            - ``RRC`` specifies the filter type as RRC.
        """
        return self._type


class MathMathItemEusbSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:EUSB:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for EUSB bus.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:EUSB:SUPPortedfields?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:EUSB:SUPPortedfields?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:EUSB:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:EUSB:SUPPortedfields {DATa|DDATa}
        - MATH:MATH<x>:EUSB:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa. DATa field can be set when eUSB Bus configuration
          for Speed is set to High and Signal type is Diff.
        - ``DDATa`` sets the field type to DDATa.
    """


class MathMathItemEusb(SCPICmdRead):
    """The ``MATH:MATH<x>:EUSB`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:EUSB?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:EUSB?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:EUSB:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemEusbSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemEusbSupportedfields:
        """Return the ``MATH:MATH<x>:EUSB:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for EUSB
              bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:EUSB:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:EUSB:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:EUSB:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:EUSB:SUPPortedfields {DATa|DDATa}
            - MATH:MATH<x>:EUSB:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa. DATa field can be set when eUSB Bus
              configuration for Speed is set to High and Signal type is Diff.
            - ``DDATa`` sets the field type to DDATa.
        """
        return self._supportedfields


class MathMathItemEthernetSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:ETHERnet:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for ETHERnet
          bus. The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:ETHERnet:SUPPortedfields?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MATH:MATH<x>:ETHERnet:SUPPortedfields?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:ETHERnet:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:ETHERnet:SUPPortedfields {DATa|IPData|TDATa}
        - MATH:MATH<x>:ETHERnet:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
        - ``IPData`` sets the field type to IPData.
        - ``TDATa`` sets the field type to TDATa.
    """


class MathMathItemEthernet(SCPICmdRead):
    """The ``MATH:MATH<x>:ETHERnet`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:ETHERnet?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:ETHERnet?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:ETHERnet:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemEthernetSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemEthernetSupportedfields:
        """Return the ``MATH:MATH<x>:ETHERnet:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for
              ETHERnet bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:ETHERnet:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:ETHERnet:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:ETHERnet:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:ETHERnet:SUPPortedfields {DATa|IPData|TDATa}
            - MATH:MATH<x>:ETHERnet:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
            - ``IPData`` sets the field type to IPData.
            - ``TDATa`` sets the field type to TDATa.
        """
        return self._supportedfields


class MathMathItemEthercatSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:ETHERCAT:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for ETHERCAT
          bus. The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:ETHERCAT:SUPPortedfields?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MATH:MATH<x>:ETHERCAT:SUPPortedfields?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:ETHERCAT:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:ETHERCAT:SUPPortedfields {DATa|SDATa|NWVariabledata}
        - MATH:MATH<x>:ETHERCAT:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
        - ``SDATa`` sets the field type to SDATa.
        - ``NWVariabledata`` sets the field type to NWVariabledata.
    """


class MathMathItemEthercat(SCPICmdRead):
    """The ``MATH:MATH<x>:ETHERCAT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:ETHERCAT?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:ETHERCAT?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:ETHERCAT:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemEthercatSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemEthercatSupportedfields:
        """Return the ``MATH:MATH<x>:ETHERCAT:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for
              ETHERCAT bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:ETHERCAT:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:ETHERCAT:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:ETHERCAT:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:ETHERCAT:SUPPortedfields {DATa|SDATa|NWVariabledata}
            - MATH:MATH<x>:ETHERCAT:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
            - ``SDATa`` sets the field type to SDATa.
            - ``NWVariabledata`` sets the field type to NWVariabledata.
        """
        return self._supportedfields


class MathMathItemEspiSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:ESPI:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for ESPI bus.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:ESPI:SUPPortedfields?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:ESPI:SUPPortedfields?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:ESPI:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:ESPI:SUPPortedfields {DATa|CDATa|RDATa}
        - MATH:MATH<x>:ESPI:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
        - ``CDATa`` sets the field type to CDATa.
        - ``RDATa`` sets the field type to RDATa.
    """


class MathMathItemEspi(SCPICmdRead):
    """The ``MATH:MATH<x>:ESPI`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:ESPI?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:ESPI?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:ESPI:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemEspiSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemEspiSupportedfields:
        """Return the ``MATH:MATH<x>:ESPI:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for ESPI
              bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:ESPI:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:ESPI:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:ESPI:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:ESPI:SUPPortedfields {DATa|CDATa|RDATa}
            - MATH:MATH<x>:ESPI:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
            - ``CDATa`` sets the field type to CDATa.
            - ``RDATa`` sets the field type to RDATa.
        """
        return self._supportedfields


class MathMathItemDefine(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:DEFine`` command.

    Description:
        - This command allows you to define new waveforms using mathematical expressions. The query
          form of this command returns the math definition for the specified math waveform. The math
          waveform is specified by x. You can specify a math expression from waveforms, measurements
          and scalar sources, functions, operands, and numerical constants. Math expressions can be
          simple, such as Ch1, which specifies that a waveform should show the signal source of
          Channel 1 with no mathematical computation. Math expressions can also be complex,
          consisting of 100 plus characters and comprising many sources (including other math
          waveforms), functions, and operands. As an example, you can enter the expression
          Log(Ch1+Ch2), which specifies that the signals from channels 1 and 2 are to be
          algebraically added, and the base 10 log of the sum is to be shown as the final math
          waveform.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:DEFine?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:DEFine?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:DEFine value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:DEFine <QString>
        - MATH:MATH<x>:DEFine?
        ```

    Info:
        - ``<QString>`` quoted string argument is the mathematical expression that defines the
          waveform. ``MATH:MATH<x>:DEFINE?`` is for use when the ``MATH:MATH<x>:TYPE`` is ADVANCED.
    """

    _WRAP_ARG_WITH_QUOTES = True


class MathMathItemCxpiSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:CXPI:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for CXPI bus.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:CXPI:SUPPortedfields?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:CXPI:SUPPortedfields?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:CXPI:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:CXPI:SUPPortedfields {DATa}
        - MATH:MATH<x>:CXPI:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
    """


class MathMathItemCxpi(SCPICmdRead):
    """The ``MATH:MATH<x>:CXPI`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:CXPI?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:CXPI?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:CXPI:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemCxpiSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemCxpiSupportedfields:
        """Return the ``MATH:MATH<x>:CXPI:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for CXPI
              bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:CXPI:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:CXPI:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:CXPI:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:CXPI:SUPPortedfields {DATa}
            - MATH:MATH<x>:CXPI:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
        """
        return self._supportedfields


class MathMathItemCanSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:CAN:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for CAN bus.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:CAN:SUPPortedfields?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:CAN:SUPPortedfields?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:CAN:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:CAN:SUPPortedfields {DATa}
        - MATH:MATH<x>:CAN:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
    """


class MathMathItemCan(SCPICmdRead):
    """The ``MATH:MATH<x>:CAN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:CAN?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:CAN?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:CAN:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemCanSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemCanSupportedfields:
        """Return the ``MATH:MATH<x>:CAN:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for CAN
              bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:CAN:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:CAN:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:CAN:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:CAN:SUPPortedfields {DATa}
            - MATH:MATH<x>:CAN:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
        """
        return self._supportedfields


class MathMathItemAvgWeight(SCPICmdWrite):
    """The ``MATH:MATH<x>:AVG:WEIGht`` command.

    Description:
        - This command sets or queries the number of acquisitions at which the averaging algorithm
          will begin exponential averaging. The math waveform is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:AVG:WEIGht value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:AVG:WEIGht <NR1>
        ```

    Info:
        - ``<NR1>`` is the number of acquisitions at which the averaging algorithm will begin
          exponential averaging.
    """


class MathMathItemAvgMode(SCPICmdWrite):
    """The ``MATH:MATH<x>:AVG:MODE`` command.

    Description:
        - This command sets or queries the math average mode flag. If the flag is set to 1, math
          averaging is turned on. The math waveform is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:AVG:MODE value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:AVG:MODE {ON|OFF|<NR1>}
        ```

    Info:
        - ``<NR1>`` = 0 turns off average mode, and any other integer turns on average mode.
        - ``OFF`` turns off average mode.
        - ``ON`` turns on average mode.
    """


class MathMathItemAvg(SCPICmdRead):
    """The ``MATH:MATH<x>:AVG`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:AVG?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:AVG?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.mode``: The ``MATH:MATH<x>:AVG:MODE`` command.
        - ``.weight``: The ``MATH:MATH<x>:AVG:WEIGht`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = MathMathItemAvgMode(device, f"{self._cmd_syntax}:MODE")
        self._weight = MathMathItemAvgWeight(device, f"{self._cmd_syntax}:WEIGht")

    @property
    def mode(self) -> MathMathItemAvgMode:
        """Return the ``MATH:MATH<x>:AVG:MODE`` command.

        Description:
            - This command sets or queries the math average mode flag. If the flag is set to 1, math
              averaging is turned on. The math waveform is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:AVG:MODE value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:AVG:MODE {ON|OFF|<NR1>}
            ```

        Info:
            - ``<NR1>`` = 0 turns off average mode, and any other integer turns on average mode.
            - ``OFF`` turns off average mode.
            - ``ON`` turns on average mode.
        """
        return self._mode

    @property
    def weight(self) -> MathMathItemAvgWeight:
        """Return the ``MATH:MATH<x>:AVG:WEIGht`` command.

        Description:
            - This command sets or queries the number of acquisitions at which the averaging
              algorithm will begin exponential averaging. The math waveform is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:AVG:WEIGht value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:AVG:WEIGht <NR1>
            ```

        Info:
            - ``<NR1>`` is the number of acquisitions at which the averaging algorithm will begin
              exponential averaging.
        """
        return self._weight


class MathMathItemAutoethernetSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:AUTOETHERnet:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for
          AUTOETHERnet bus. The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:AUTOETHERnet:SUPPortedfields?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MATH:MATH<x>:AUTOETHERnet:SUPPortedfields?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:AUTOETHERnet:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:AUTOETHERnet:SUPPortedfields {DATa|IPData|TDATa}
        - MATH:MATH<x>:AUTOETHERnet:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
        - ``IPData`` sets the field type to IPData.
        - ``TDATa`` sets the field type to TDATa.
    """


class MathMathItemAutoethernet(SCPICmdRead):
    """The ``MATH:MATH<x>:AUTOETHERnet`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:AUTOETHERnet?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:AUTOETHERnet?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:AUTOETHERnet:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemAutoethernetSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemAutoethernetSupportedfields:
        """Return the ``MATH:MATH<x>:AUTOETHERnet:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for
              AUTOETHERnet bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MATH:MATH<x>:AUTOETHERnet:SUPPortedfields?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:AUTOETHERnet:SUPPortedfields?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:AUTOETHERnet:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:AUTOETHERnet:SUPPortedfields {DATa|IPData|TDATa}
            - MATH:MATH<x>:AUTOETHERnet:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
            - ``IPData`` sets the field type to IPData.
            - ``TDATa`` sets the field type to TDATa.
        """
        return self._supportedfields


class MathMathItemAudioSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:AUDIO:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for Audio bus.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:AUDIO:SUPPortedfields?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:AUDIO:SUPPortedfields?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:AUDIO:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:AUDIO:SUPPortedfields {LCHannel|RCHannel|TDMChannel}
        - MATH:MATH<x>:AUDIO:SUPPortedfields?
        ```

    Info:
        - ``LCHannel`` sets the field type to LCHannel.
        - ``RCHannel`` sets the field type to RCHannel.
        - ``TDMChannel`` sets the field type to TDMChannel.
    """


class MathMathItemAudio(SCPICmdRead):
    """The ``MATH:MATH<x>:AUDIO`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:AUDIO?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:AUDIO?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:AUDIO:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemAudioSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemAudioSupportedfields:
        """Return the ``MATH:MATH<x>:AUDIO:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for Audio
              bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:AUDIO:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:AUDIO:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:AUDIO:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:AUDIO:SUPPortedfields {LCHannel|RCHannel|TDMChannel}
            - MATH:MATH<x>:AUDIO:SUPPortedfields?
            ```

        Info:
            - ``LCHannel`` sets the field type to LCHannel.
            - ``RCHannel`` sets the field type to RCHannel.
            - ``TDMChannel`` sets the field type to TDMChannel.
        """
        return self._supportedfields


class MathMathItemArinc429aSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:ARINC429A:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for ARINC429A
          bus. The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:ARINC429A:SUPPortedfields?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MATH:MATH<x>:ARINC429A:SUPPortedfields?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:ARINC429A:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:ARINC429A:SUPPortedfields {DATa}
        - MATH:MATH<x>:ARINC429A:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
    """


class MathMathItemArinc429a(SCPICmdRead):
    """The ``MATH:MATH<x>:ARINC429A`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:ARINC429A?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:ARINC429A?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:ARINC429A:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemArinc429aSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemArinc429aSupportedfields:
        """Return the ``MATH:MATH<x>:ARINC429A:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for
              ARINC429A bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MATH:MATH<x>:ARINC429A:SUPPortedfields?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:ARINC429A:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:ARINC429A:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:ARINC429A:SUPPortedfields {DATa}
            - MATH:MATH<x>:ARINC429A:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
        """
        return self._supportedfields


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class MathMathItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``MATH:MATH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.arinc429a``: The ``MATH:MATH<x>:ARINC429A`` command tree.
        - ``.audio``: The ``MATH:MATH<x>:AUDIO`` command tree.
        - ``.autoethernet``: The ``MATH:MATH<x>:AUTOETHERnet`` command tree.
        - ``.avg``: The ``MATH:MATH<x>:AVG`` command tree.
        - ``.can``: The ``MATH:MATH<x>:CAN`` command tree.
        - ``.cxpi``: The ``MATH:MATH<x>:CXPI`` command tree.
        - ``.define``: The ``MATH:MATH<x>:DEFine`` command.
        - ``.espi``: The ``MATH:MATH<x>:ESPI`` command tree.
        - ``.ethercat``: The ``MATH:MATH<x>:ETHERCAT`` command tree.
        - ``.ethernet``: The ``MATH:MATH<x>:ETHERnet`` command tree.
        - ``.eusb``: The ``MATH:MATH<x>:EUSB`` command tree.
        - ``.filter``: The ``MATH:MATH<x>:FILTer`` command tree.
        - ``.flexray``: The ``MATH:MATH<x>:FLEXray`` command tree.
        - ``.function``: The ``MATH:MATH<x>:FUNCtion`` command.
        - ``.gating``: The ``MATH:MATH<x>:GATing`` command.
        - ``.i2c``: The ``MATH:MATH<x>:I2C`` command tree.
        - ``.i3c``: The ``MATH:MATH<x>:I3C`` command tree.
        - ``.interpolation``: The ``MATH:MATH<x>:INTERpolation`` command.
        - ``.label``: The ``MATH:MATH<x>:LABel`` command tree.
        - ``.lin``: The ``MATH:MATH<x>:LIN`` command tree.
        - ``.mdio``: The ``MATH:MATH<x>:MDIO`` command tree.
        - ``.mil1553b``: The ``MATH:MATH<x>:MIL1553B`` command tree.
        - ``.onewire``: The ``MATH:MATH<x>:ONEWIRe`` command tree.
        - ``.parallel``: The ``MATH:MATH<x>:PARallel`` command tree.
        - ``.psifive``: The ``MATH:MATH<x>:PSIFIVe`` command tree.
        - ``.rs232c``: The ``MATH:MATH<x>:RS232C`` command tree.
        - ``.sdlc``: The ``MATH:MATH<x>:SDLC`` command tree.
        - ``.sent``: The ``MATH:MATH<x>:SENT`` command tree.
        - ``.signeddata``: The ``MATH:MATH<x>:SIGNeddata`` command.
        - ``.smbus``: The ``MATH:MATH<x>:SMBUS`` command tree.
        - ``.source1``: The ``MATH:MATH<x>:SOUrce1`` command.
        - ``.spacewire``: The ``MATH:MATH<x>:SPACEWIRe`` command tree.
        - ``.spectral``: The ``MATH:MATH<x>:SPECTral`` command tree.
        - ``.spi``: The ``MATH:MATH<x>:SPI`` command tree.
        - ``.spmi``: The ``MATH:MATH<x>:SPMI`` command tree.
        - ``.svid``: The ``MATH:MATH<x>:SVID`` command tree.
        - ``.type``: The ``MATH:MATH<x>:TYPe`` command.
        - ``.usb``: The ``MATH:MATH<x>:USB`` command tree.
        - ``.vunit``: The ``MATH:MATH<x>:VUNIT`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._arinc429a = MathMathItemArinc429a(device, f"{self._cmd_syntax}:ARINC429A")
        self._audio = MathMathItemAudio(device, f"{self._cmd_syntax}:AUDIO")
        self._autoethernet = MathMathItemAutoethernet(device, f"{self._cmd_syntax}:AUTOETHERnet")
        self._avg = MathMathItemAvg(device, f"{self._cmd_syntax}:AVG")
        self._can = MathMathItemCan(device, f"{self._cmd_syntax}:CAN")
        self._cxpi = MathMathItemCxpi(device, f"{self._cmd_syntax}:CXPI")
        self._define = MathMathItemDefine(device, f"{self._cmd_syntax}:DEFine")
        self._espi = MathMathItemEspi(device, f"{self._cmd_syntax}:ESPI")
        self._ethercat = MathMathItemEthercat(device, f"{self._cmd_syntax}:ETHERCAT")
        self._ethernet = MathMathItemEthernet(device, f"{self._cmd_syntax}:ETHERnet")
        self._eusb = MathMathItemEusb(device, f"{self._cmd_syntax}:EUSB")
        self._filter = MathMathItemFilter(device, f"{self._cmd_syntax}:FILTer")
        self._flexray = MathMathItemFlexray(device, f"{self._cmd_syntax}:FLEXray")
        self._function = MathMathItemFunction(device, f"{self._cmd_syntax}:FUNCtion")
        self._gating = MathMathItemGating(device, f"{self._cmd_syntax}:GATing")
        self._i2c = MathMathItemI2c(device, f"{self._cmd_syntax}:I2C")
        self._i3c = MathMathItemI3c(device, f"{self._cmd_syntax}:I3C")
        self._interpolation = MathMathItemInterpolation(device, f"{self._cmd_syntax}:INTERpolation")
        self._label = MathMathItemLabel(device, f"{self._cmd_syntax}:LABel")
        self._lin = MathMathItemLin(device, f"{self._cmd_syntax}:LIN")
        self._mdio = MathMathItemMdio(device, f"{self._cmd_syntax}:MDIO")
        self._mil1553b = MathMathItemMil1553b(device, f"{self._cmd_syntax}:MIL1553B")
        self._onewire = MathMathItemOnewire(device, f"{self._cmd_syntax}:ONEWIRe")
        self._parallel = MathMathItemParallel(device, f"{self._cmd_syntax}:PARallel")
        self._psifive = MathMathItemPsifive(device, f"{self._cmd_syntax}:PSIFIVe")
        self._rs232c = MathMathItemRs232c(device, f"{self._cmd_syntax}:RS232C")
        self._sdlc = MathMathItemSdlc(device, f"{self._cmd_syntax}:SDLC")
        self._sent = MathMathItemSent(device, f"{self._cmd_syntax}:SENT")
        self._signeddata = MathMathItemSigneddata(device, f"{self._cmd_syntax}:SIGNeddata")
        self._smbus = MathMathItemSmbus(device, f"{self._cmd_syntax}:SMBUS")
        self._source1 = MathMathItemSource1(device, f"{self._cmd_syntax}:SOUrce1")
        self._spacewire = MathMathItemSpacewire(device, f"{self._cmd_syntax}:SPACEWIRe")
        self._spectral = MathMathItemSpectral(device, f"{self._cmd_syntax}:SPECTral")
        self._spi = MathMathItemSpi(device, f"{self._cmd_syntax}:SPI")
        self._spmi = MathMathItemSpmi(device, f"{self._cmd_syntax}:SPMI")
        self._svid = MathMathItemSvid(device, f"{self._cmd_syntax}:SVID")
        self._type = MathMathItemType(device, f"{self._cmd_syntax}:TYPe")
        self._usb = MathMathItemUsb(device, f"{self._cmd_syntax}:USB")
        self._vunit = MathMathItemVunit(device, f"{self._cmd_syntax}:VUNIT")

    @property
    def arinc429a(self) -> MathMathItemArinc429a:
        """Return the ``MATH:MATH<x>:ARINC429A`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:ARINC429A?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:ARINC429A?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:ARINC429A:SUPPortedfields`` command.
        """
        return self._arinc429a

    @property
    def audio(self) -> MathMathItemAudio:
        """Return the ``MATH:MATH<x>:AUDIO`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:AUDIO?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:AUDIO?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:AUDIO:SUPPortedfields`` command.
        """
        return self._audio

    @property
    def autoethernet(self) -> MathMathItemAutoethernet:
        """Return the ``MATH:MATH<x>:AUTOETHERnet`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:AUTOETHERnet?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:AUTOETHERnet?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:AUTOETHERnet:SUPPortedfields`` command.
        """
        return self._autoethernet

    @property
    def avg(self) -> MathMathItemAvg:
        """Return the ``MATH:MATH<x>:AVG`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:AVG?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:AVG?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.mode``: The ``MATH:MATH<x>:AVG:MODE`` command.
            - ``.weight``: The ``MATH:MATH<x>:AVG:WEIGht`` command.
        """
        return self._avg

    @property
    def can(self) -> MathMathItemCan:
        """Return the ``MATH:MATH<x>:CAN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:CAN?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:CAN?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:CAN:SUPPortedfields`` command.
        """
        return self._can

    @property
    def cxpi(self) -> MathMathItemCxpi:
        """Return the ``MATH:MATH<x>:CXPI`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:CXPI?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:CXPI?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:CXPI:SUPPortedfields`` command.
        """
        return self._cxpi

    @property
    def define(self) -> MathMathItemDefine:
        """Return the ``MATH:MATH<x>:DEFine`` command.

        Description:
            - This command allows you to define new waveforms using mathematical expressions. The
              query form of this command returns the math definition for the specified math
              waveform. The math waveform is specified by x. You can specify a math expression from
              waveforms, measurements and scalar sources, functions, operands, and numerical
              constants. Math expressions can be simple, such as Ch1, which specifies that a
              waveform should show the signal source of Channel 1 with no mathematical computation.
              Math expressions can also be complex, consisting of 100 plus characters and comprising
              many sources (including other math waveforms), functions, and operands. As an example,
              you can enter the expression Log(Ch1+Ch2), which specifies that the signals from
              channels 1 and 2 are to be algebraically added, and the base 10 log of the sum is to
              be shown as the final math waveform.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:DEFine?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:DEFine?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:DEFine value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:DEFine <QString>
            - MATH:MATH<x>:DEFine?
            ```

        Info:
            - ``<QString>`` quoted string argument is the mathematical expression that defines the
              waveform. ``MATH:MATH<x>:DEFINE?`` is for use when the ``MATH:MATH<x>:TYPE`` is
              ADVANCED.
        """
        return self._define

    @property
    def espi(self) -> MathMathItemEspi:
        """Return the ``MATH:MATH<x>:ESPI`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:ESPI?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:ESPI?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:ESPI:SUPPortedfields`` command.
        """
        return self._espi

    @property
    def ethercat(self) -> MathMathItemEthercat:
        """Return the ``MATH:MATH<x>:ETHERCAT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:ETHERCAT?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:ETHERCAT?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:ETHERCAT:SUPPortedfields`` command.
        """
        return self._ethercat

    @property
    def ethernet(self) -> MathMathItemEthernet:
        """Return the ``MATH:MATH<x>:ETHERnet`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:ETHERnet?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:ETHERnet?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:ETHERnet:SUPPortedfields`` command.
        """
        return self._ethernet

    @property
    def eusb(self) -> MathMathItemEusb:
        """Return the ``MATH:MATH<x>:EUSB`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:EUSB?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:EUSB?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:EUSB:SUPPortedfields`` command.
        """
        return self._eusb

    @property
    def filter(self) -> MathMathItemFilter:
        """Return the ``MATH:MATH<x>:FILTer`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:FILTer?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FILTer?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.cfreq``: The ``MATH:MATH<x>:FILTer:CFReq`` command.
            - ``.delay``: The ``MATH:MATH<x>:FILTer:DELay`` command.
            - ``.design``: The ``MATH:MATH<x>:FILTer:DESIgn`` command.
            - ``.hcfreq``: The ``MATH:MATH<x>:FILTer:HCFReq`` command.
            - ``.info``: The ``MATH:MATH<x>:FILTer:INFo`` command.
            - ``.lcfreq``: The ``MATH:MATH<x>:FILTer:LCFReq`` command.
            - ``.load``: The ``MATH:MATH<x>:FILTer:LOAD`` command.
            - ``.order``: The ``MATH:MATH<x>:FILTer:ORDer`` command.
            - ``.pripple``: The ``MATH:MATH<x>:FILTer:PRIPple`` command.
            - ``.response``: The ``MATH:MATH<x>:FILTer:RESPonse`` command.
            - ``.rofactor``: The ``MATH:MATH<x>:FILTer:ROFactor`` command.
            - ``.sattenuation``: The ``MATH:MATH<x>:FILTer:SATTenuation`` command.
            - ``.save``: The ``MATH:MATH<x>:FILTer:SAVe`` command.
            - ``.sdeviation``: The ``MATH:MATH<x>:FILTer:SDEViation`` command.
            - ``.sduration``: The ``MATH:MATH<x>:FILTer:SDURation`` command.
            - ``.source``: The ``MATH:MATH<x>:FILTer:SOURce`` command.
            - ``.symbols``: The ``MATH:MATH<x>:FILTer:SYMBols`` command.
            - ``.twidth``: The ``MATH:MATH<x>:FILTer:TWIDth`` command.
            - ``.type``: The ``MATH:MATH<x>:FILTer:TYPe`` command.
        """
        return self._filter

    @property
    def flexray(self) -> MathMathItemFlexray:
        """Return the ``MATH:MATH<x>:FLEXray`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:FLEXray?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FLEXray?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:FLEXray:SUPPortedfields`` command.
        """
        return self._flexray

    @property
    def function(self) -> MathMathItemFunction:
        """Return the ``MATH:MATH<x>:FUNCtion`` command.

        Description:
            - This command sets or queries the basic math arithmetic function. The math waveform is
              specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FUNCtion value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:FUNCtion {ADD|SUBtract|MULTiply|DIVide}
            ```

        Info:
            - ``ADD`` sets the basic math function to add.
            - ``SUBtract`` sets the basic math function to subtract.
            - ``MULTiply`` sets the basic math function to multiply.
            - ``DIVide`` sets the basic math function to divide.
        """
        return self._function

    @property
    def gating(self) -> MathMathItemGating:
        """Return the ``MATH:MATH<x>:GATing`` command.

        Description:
            - This command specifies or returns the gating setting. It only applies to Math FFT
              plots. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:GATing?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:GATing?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:GATing value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:GATing {NONE|SCREEN|CURSor}
            - MATH:MATH<x>:GATing?
            ```

        Info:
            - ``NONE`` turns off math gating.
            - ``SCREEN`` turns on gating, using the left and right edges of the screen.
            - ``CURSor`` limits math to the portion of the waveform between the vertical bar
              cursors, even if they are off screen.
        """
        return self._gating

    @property
    def i2c(self) -> MathMathItemI2c:
        """Return the ``MATH:MATH<x>:I2C`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:I2C?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:I2C?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:I2C:SUPPortedfields`` command.
        """
        return self._i2c

    @property
    def i3c(self) -> MathMathItemI3c:
        """Return the ``MATH:MATH<x>:I3C`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:I3C?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:I3C?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:I3C:SUPPortedfields`` command.
        """
        return self._i3c

    @property
    def interpolation(self) -> MathMathItemInterpolation:
        """Return the ``MATH:MATH<x>:INTERpolation`` command.

        Description:
            - This command sets or queries whether sinc interpolation is enabled for math on bus
              source. The math waveform is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:INTERpolation value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:INTERpolation {ON|OFF}
            ```

        Info:
            - ``ON`` indicates that the sinc interpolation is used for math waveform.
            - ``OFF`` indicates no interpolation is used for math waveform. Waveform will appear
              'stair-steppy' in this case.
        """
        return self._interpolation

    @property
    def label(self) -> MathMathItemLabel:
        """Return the ``MATH:MATH<x>:LABel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.color``: The ``MATH:MATH<x>:LABel:COLor`` command.
            - ``.font``: The ``MATH:MATH<x>:LABel:FONT`` command tree.
            - ``.name``: The ``MATH:MATH<x>:LABel:NAMe`` command.
            - ``.xpos``: The ``MATH:MATH<x>:LABel:XPOS`` command.
            - ``.ypos``: The ``MATH:MATH<x>:LABel:YPOS`` command.
        """
        return self._label

    @property
    def lin(self) -> MathMathItemLin:
        """Return the ``MATH:MATH<x>:LIN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:LIN?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LIN?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:LIN:SUPPortedfields`` command.
        """
        return self._lin

    @property
    def mdio(self) -> MathMathItemMdio:
        """Return the ``MATH:MATH<x>:MDIO`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:MDIO?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:MDIO?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:MDIO:SUPPortedfields`` command.
        """
        return self._mdio

    @property
    def mil1553b(self) -> MathMathItemMil1553b:
        """Return the ``MATH:MATH<x>:MIL1553B`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:MIL1553B?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:MIL1553B?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:MIL1553B:SUPPortedfields`` command.
        """
        return self._mil1553b

    @property
    def onewire(self) -> MathMathItemOnewire:
        """Return the ``MATH:MATH<x>:ONEWIRe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:ONEWIRe?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:ONEWIRe?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:ONEWIRe:SUPPortedfields`` command.
        """
        return self._onewire

    @property
    def parallel(self) -> MathMathItemParallel:
        """Return the ``MATH:MATH<x>:PARallel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:PARallel?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:PARallel?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:PARallel:SUPPortedfields`` command.
        """
        return self._parallel

    @property
    def psifive(self) -> MathMathItemPsifive:
        """Return the ``MATH:MATH<x>:PSIFIVe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:PSIFIVe?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:PSIFIVe?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:PSIFIVe:SUPPortedfields`` command.
        """
        return self._psifive

    @property
    def rs232c(self) -> MathMathItemRs232c:
        """Return the ``MATH:MATH<x>:RS232C`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:RS232C?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:RS232C?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:RS232C:SUPPortedfields`` command.
        """
        return self._rs232c

    @property
    def sdlc(self) -> MathMathItemSdlc:
        """Return the ``MATH:MATH<x>:SDLC`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SDLC?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SDLC?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:SDLC:SUPPortedfields`` command.
        """
        return self._sdlc

    @property
    def sent(self) -> MathMathItemSent:
        """Return the ``MATH:MATH<x>:SENT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SENT?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SENT?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:SENT:SUPPortedfields`` command.
        """
        return self._sent

    @property
    def signeddata(self) -> MathMathItemSigneddata:
        """Return the ``MATH:MATH<x>:SIGNeddata`` command.

        Description:
            - This command sets or queries value to denote that bus field is decoded as
              signed/unsigned data for math on bus source. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SIGNeddata?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SIGNeddata?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:SIGNeddata value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:SIGNeddata {ON|OFF}
            - MATH:MATH<x>:SIGNeddata?
            ```

        Info:
            - ``ON`` indicates that the bus field is decoded as signed data for drawing the math
              waveform.
            - ``OFF`` indicates that the bus field is decoded as unsigned data for drawing the math
              waveform.
        """
        return self._signeddata

    @property
    def smbus(self) -> MathMathItemSmbus:
        """Return the ``MATH:MATH<x>:SMBUS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SMBUS?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SMBUS?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:SMBUS:SUPPortedfields`` command.
        """
        return self._smbus

    @property
    def source1(self) -> MathMathItemSource1:
        """Return the ``MATH:MATH<x>:SOUrce1`` command.

        Description:
            - This command sets or queries the specified math source. The source in the command can
              be either 1 or 2. This command sets the Basic Math components in the user interface,
              with two sources and a function. You would also need to set the math type to Basic to
              see the change in the user interface but this will not effect the programmable
              interface. The math waveform and source are specified by x. SOURCE1 and SOURCE2 are
              for use when the ``MATH:MATH<x>:TYPE`` is BASIC.

        Usage:
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:SOUrce1 value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:SOUrce1 {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            ```

        Info:
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``Math<x>`` specifies a math waveform as the source.
            - ``REF<x>`` specifies a reference waveform as the source.
        """
        return self._source1

    @property
    def spacewire(self) -> MathMathItemSpacewire:
        """Return the ``MATH:MATH<x>:SPACEWIRe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPACEWIRe?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPACEWIRe?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:SPACEWIRe:SUPPortedfields`` command.
        """
        return self._spacewire

    @property
    def spectral(self) -> MathMathItemSpectral:
        """Return the ``MATH:MATH<x>:SPECTral`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPECTral?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPECTral?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.horz``: The ``MATH:MATH<x>:SPECTral:HORZ`` command.
            - ``.mag``: The ``MATH:MATH<x>:SPECTral:MAG`` command.
            - ``.phase``: The ``MATH:MATH<x>:SPECTral:PHASE`` command.
            - ``.source``: The ``MATH:MATH<x>:SPECTral:SOUrce`` command.
            - ``.suppress``: The ``MATH:MATH<x>:SPECTral:SUPPress`` command.
            - ``.type``: The ``MATH:MATH<x>:SPECTral:TYPE`` command.
            - ``.unwrap``: The ``MATH:MATH<x>:SPECTral:UNWRap`` command.
            - ``.window``: The ``MATH:MATH<x>:SPECTral:WINdow`` command.
        """
        return self._spectral

    @property
    def spi(self) -> MathMathItemSpi:
        """Return the ``MATH:MATH<x>:SPI`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPI?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPI?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:SPI:SUPPortedfields`` command.
        """
        return self._spi

    @property
    def spmi(self) -> MathMathItemSpmi:
        """Return the ``MATH:MATH<x>:SPMI`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPMI?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPMI?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:SPMI:SUPPortedfields`` command.
        """
        return self._spmi

    @property
    def svid(self) -> MathMathItemSvid:
        """Return the ``MATH:MATH<x>:SVID`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SVID?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SVID?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:SVID:SUPPortedfields`` command.
        """
        return self._svid

    @property
    def type(self) -> MathMathItemType:
        """Return the ``MATH:MATH<x>:TYPe`` command.

        Description:
            - This command sets or queries the math type. The math waveform is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:TYPe value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:TYPe {BASic|FILTER|FFT|ADVanced}
            ```

        Info:
            - ``BASic`` set the type to basic math.
            - ``FILTER`` sets the math type to filter. Requires UDFLT licenses on 5, 6 series MSO
              instruments and Tekscope (Offline).
            - ``FFT`` sets the type to FFT math, which can use any live analog or reference waveform
              in the time domain. NOTE. You can also use FFT as part of a math expression by
              declaring the type.
            - ``ADVanced`` sets the type to advanced math.
        """
        return self._type

    @property
    def usb(self) -> MathMathItemUsb:
        """Return the ``MATH:MATH<x>:USB`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:USB?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:USB?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:USB:SUPPortedfields`` command.
        """
        return self._usb

    @property
    def vunit(self) -> MathMathItemVunit:
        """Return the ``MATH:MATH<x>:VUNIT`` command.

        Description:
            - This command specifies or returns the math custom vertical units. The math waveform is
              specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:VUNIT value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:VUNIT <QString>
            ```

        Info:
            - ``<QString>`` is the custom vertical units.
        """
        return self._vunit


class MathList(SCPICmdRead):
    """The ``MATH:LIST`` command.

    Description:
        - This query returns a comma separated list of all currently defined math waveforms.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:LIST?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:LIST?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MATH:LIST?
        ```
    """


class MathDelete(SCPICmdWrite):
    """The ``MATH:DELete`` command.

    Description:
        - This command deletes the specified math.

    Usage:
        - Using the ``.write(value)`` method will send the ``MATH:DELete value`` command.

    SCPI Syntax:
        ```
        - MATH:DELete <QString>
        ```

    Info:
        - ``<QString>`` is a quoted string specifying the math waveform to delete. The quoted string
          is of the form 'MATH<NR1>', where <NR1> is ≥1.
    """

    _WRAP_ARG_WITH_QUOTES = True


class MathAddnew(SCPICmdWrite):
    """The ``MATH:ADDNew`` command.

    Description:
        - This command adds the specified math.

    Usage:
        - Using the ``.write(value)`` method will send the ``MATH:ADDNew value`` command.

    SCPI Syntax:
        ```
        - MATH:ADDNew <QString>
        ```

    Info:
        - ``<QString>`` is the quoted string specifying the math waveform to add. The argument is of
          the form 'MATH<NR1>', where <NR1> is ≥1.
    """

    _WRAP_ARG_WITH_QUOTES = True


class Math(SCPICmdRead):
    """The ``MATH`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.addnew``: The ``MATH:ADDNew`` command.
        - ``.delete``: The ``MATH:DELete`` command.
        - ``.list``: The ``MATH:LIST`` command.
        - ``.math``: The ``MATH:MATH<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "MATH") -> None:
        super().__init__(device, cmd_syntax)
        self._addnew = MathAddnew(device, f"{self._cmd_syntax}:ADDNew")
        self._delete = MathDelete(device, f"{self._cmd_syntax}:DELete")
        self._list = MathList(device, f"{self._cmd_syntax}:LIST")
        self._math: Dict[int, MathMathItem] = DefaultDictPassKeyToFactory(
            lambda x: MathMathItem(device, f"{self._cmd_syntax}:MATH{x}")
        )

    @property
    def addnew(self) -> MathAddnew:
        """Return the ``MATH:ADDNew`` command.

        Description:
            - This command adds the specified math.

        Usage:
            - Using the ``.write(value)`` method will send the ``MATH:ADDNew value`` command.

        SCPI Syntax:
            ```
            - MATH:ADDNew <QString>
            ```

        Info:
            - ``<QString>`` is the quoted string specifying the math waveform to add. The argument
              is of the form 'MATH<NR1>', where <NR1> is ≥1.
        """
        return self._addnew

    @property
    def delete(self) -> MathDelete:
        """Return the ``MATH:DELete`` command.

        Description:
            - This command deletes the specified math.

        Usage:
            - Using the ``.write(value)`` method will send the ``MATH:DELete value`` command.

        SCPI Syntax:
            ```
            - MATH:DELete <QString>
            ```

        Info:
            - ``<QString>`` is a quoted string specifying the math waveform to delete. The quoted
              string is of the form 'MATH<NR1>', where <NR1> is ≥1.
        """
        return self._delete

    @property
    def list(self) -> MathList:
        """Return the ``MATH:LIST`` command.

        Description:
            - This query returns a comma separated list of all currently defined math waveforms.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:LIST?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:LIST?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MATH:LIST?
            ```
        """
        return self._list

    @property
    def math(self) -> Dict[int, MathMathItem]:
        """Return the ``MATH:MATH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.arinc429a``: The ``MATH:MATH<x>:ARINC429A`` command tree.
            - ``.audio``: The ``MATH:MATH<x>:AUDIO`` command tree.
            - ``.autoethernet``: The ``MATH:MATH<x>:AUTOETHERnet`` command tree.
            - ``.avg``: The ``MATH:MATH<x>:AVG`` command tree.
            - ``.can``: The ``MATH:MATH<x>:CAN`` command tree.
            - ``.cxpi``: The ``MATH:MATH<x>:CXPI`` command tree.
            - ``.define``: The ``MATH:MATH<x>:DEFine`` command.
            - ``.espi``: The ``MATH:MATH<x>:ESPI`` command tree.
            - ``.ethercat``: The ``MATH:MATH<x>:ETHERCAT`` command tree.
            - ``.ethernet``: The ``MATH:MATH<x>:ETHERnet`` command tree.
            - ``.eusb``: The ``MATH:MATH<x>:EUSB`` command tree.
            - ``.filter``: The ``MATH:MATH<x>:FILTer`` command tree.
            - ``.flexray``: The ``MATH:MATH<x>:FLEXray`` command tree.
            - ``.function``: The ``MATH:MATH<x>:FUNCtion`` command.
            - ``.gating``: The ``MATH:MATH<x>:GATing`` command.
            - ``.i2c``: The ``MATH:MATH<x>:I2C`` command tree.
            - ``.i3c``: The ``MATH:MATH<x>:I3C`` command tree.
            - ``.interpolation``: The ``MATH:MATH<x>:INTERpolation`` command.
            - ``.label``: The ``MATH:MATH<x>:LABel`` command tree.
            - ``.lin``: The ``MATH:MATH<x>:LIN`` command tree.
            - ``.mdio``: The ``MATH:MATH<x>:MDIO`` command tree.
            - ``.mil1553b``: The ``MATH:MATH<x>:MIL1553B`` command tree.
            - ``.onewire``: The ``MATH:MATH<x>:ONEWIRe`` command tree.
            - ``.parallel``: The ``MATH:MATH<x>:PARallel`` command tree.
            - ``.psifive``: The ``MATH:MATH<x>:PSIFIVe`` command tree.
            - ``.rs232c``: The ``MATH:MATH<x>:RS232C`` command tree.
            - ``.sdlc``: The ``MATH:MATH<x>:SDLC`` command tree.
            - ``.sent``: The ``MATH:MATH<x>:SENT`` command tree.
            - ``.signeddata``: The ``MATH:MATH<x>:SIGNeddata`` command.
            - ``.smbus``: The ``MATH:MATH<x>:SMBUS`` command tree.
            - ``.source1``: The ``MATH:MATH<x>:SOUrce1`` command.
            - ``.spacewire``: The ``MATH:MATH<x>:SPACEWIRe`` command tree.
            - ``.spectral``: The ``MATH:MATH<x>:SPECTral`` command tree.
            - ``.spi``: The ``MATH:MATH<x>:SPI`` command tree.
            - ``.spmi``: The ``MATH:MATH<x>:SPMI`` command tree.
            - ``.svid``: The ``MATH:MATH<x>:SVID`` command tree.
            - ``.type``: The ``MATH:MATH<x>:TYPe`` command.
            - ``.usb``: The ``MATH:MATH<x>:USB`` command tree.
            - ``.vunit``: The ``MATH:MATH<x>:VUNIT`` command.
        """
        return self._math
