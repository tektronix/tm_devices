# pylint: disable=line-too-long
"""The bus commands module.

These commands are used in the following models:
DPO5KB, MSO5KB, MSO70KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - BUS:B1<x>:DISplay:HIERarchical <QString>
    - BUS:B1<x>:DISplay:HIERarchical?
    - BUS:B1<x>:DISplay:LAYout <QString>
    - BUS:B1<x>:DISplay:LAYout?
    - BUS:B1<x>:USB:HYSTeresis <NR3>
    - BUS:B1<x>:USB:HYSTeresis?
    - BUS:B<x>:CAN:BITRate {RATE10K|RATE100K|RATE1M|RATE125K|RATE153K|RATE20K|RATE25K|RATE250K|RATE31K|RATE33K|RATE37K|RATE400K|RATE50K|RATE500K|RATE62K|RATE68K|RATE800K|RATE83K|RATE92K|CUSTom}
    - BUS:B<x>:CAN:BITRate:VALue <nr3>
    - BUS:B<x>:CAN:BITRate:VALue?
    - BUS:B<x>:CAN:BITRate?
    - BUS:B<x>:CAN:PRObe {DIFFerential|CANH|CANL|RX|TX}
    - BUS:B<x>:CAN:PRObe?
    - BUS:B<x>:CAN:SOUrce {CH<x>|D0|D1|D10|D11|D12|D13|D14|D15|D2|D3|D4|D5|D6|D7|D8|D9|MATH<x>}
    - BUS:B<x>:CAN:SOUrce?
    - BUS:B<x>:DISplay:DECOde:FILe {decodeFileName}
    - BUS:B<x>:DISplay:DECOde:FILe?
    - BUS:B<x>:DISplay:DECOde:STAte {OFF|ON|RELoad}
    - BUS:B<x>:DISplay:DECOde:STAte?
    - BUS:B<x>:DISplay:TYPe {BUS|WAVEFORMS|BOTh}
    - BUS:B<x>:DISplay:TYPe?
    - BUS:B<x>:ETHERnet:PRObe {DIFFerential|SINGleended}
    - BUS:B<x>:ETHERnet:PRObe?
    - BUS:B<x>:ETHERnet:SOUrce {CH<x>|MATH<x>}
    - BUS:B<x>:ETHERnet:SOUrce:DMINus {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
    - BUS:B<x>:ETHERnet:SOUrce:DMINus?
    - BUS:B<x>:ETHERnet:SOUrce:DPLUs {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
    - BUS:B<x>:ETHERnet:SOUrce:DPLUs?
    - BUS:B<x>:ETHERnet:SOUrce?
    - BUS:B<x>:ETHERnet:TYPe {ENET10BASET|ENET100BASETX}
    - BUS:B<x>:ETHERnet:TYPe?
    - BUS:B<x>:FLEXRAY:BITRate {RATE10M|RATE5M|RATE2M|CUSTom}
    - BUS:B<x>:FLEXRAY:BITRate:VALue <nr3>
    - BUS:B<x>:FLEXRAY:BITRate:VALue?
    - BUS:B<x>:FLEXRAY:BITRate?
    - BUS:B<x>:FLEXRAY:CHANnel {A|B}
    - BUS:B<x>:FLEXRAY:CHANnel?
    - BUS:B<x>:FLEXRAY:PROBe {BDIFFBP|BM|TXRX}
    - BUS:B<x>:FLEXRAY:PROBe?
    - BUS:B<x>:FLEXRAY:SIGnal {BDIFFBP|BM|TXRX}
    - BUS:B<x>:FLEXRAY:SIGnal?
    - BUS:B<x>:FLEXRAY:SOUrce {CH<x>|D0|D1|D10|D11|D12|D13|D14|D15|D2|D3|D4|D5|D6|D7|D8|D9|MATH<x>}
    - BUS:B<x>:FLEXRAY:SOUrce?
    - BUS:B<x>:I2C:CLOCk:SOUrce {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>|}
    - BUS:B<x>:I2C:CLOCk:SOUrce?
    - BUS:B<x>:I2C:DATa:SOUrce {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
    - BUS:B<x>:I2C:DATa:SOUrce?
    - BUS:B<x>:I2C:RWINADDR {No|Yes}
    - BUS:B<x>:I2C:RWINADDR?
    - BUS:B<x>:LABel <string>
    - BUS:B<x>:LABel?
    - BUS:B<x>:LIN:BITRate {RATE10K|RATE1K|RATE19K|RATE2K|RATE4K|RATE9K|CUSTom}
    - BUS:B<x>:LIN:BITRate:VALue <nr3>
    - BUS:B<x>:LIN:BITRate:VALue?
    - BUS:B<x>:LIN:BITRate?
    - BUS:B<x>:LIN:IDFORmat {NOPARity|PARity}
    - BUS:B<x>:LIN:IDFORmat?
    - BUS:B<x>:LIN:POLarity {INVerted|NORMal}
    - BUS:B<x>:LIN:POLarity?
    - BUS:B<x>:LIN:SOUrce {CH<x>|D0|D1|D10|D11|D12|D13|D14|D15|D2|D3|D4|D5|D6|D7|D8|D9|MATH<x>}
    - BUS:B<x>:LIN:SOUrce?
    - BUS:B<x>:LIN:STANDard {MIXed|V1X|V2X}
    - BUS:B<x>:LIN:STANDard?
    - BUS:B<x>:MIL1553B:POLarity {NORMal|INVerted}
    - BUS:B<x>:MIL1553B:POLarity?
    - BUS:B<x>:MIL1553B:RESPonsetime:MAXimum <NR3>
    - BUS:B<x>:MIL1553B:RESPonsetime:MAXimum?
    - BUS:B<x>:MIL1553B:RESPonsetime:MINimum <NR3>
    - BUS:B<x>:MIL1553B:RESPonsetime:MINimum?
    - BUS:B<x>:MIL1553B:SOUrce {CH<x>|MATH<x>}
    - BUS:B<x>:MIL1553B:SOUrce?
    - BUS:B<x>:MIPICSITWo:CLOCk:SOUrce {CH<x>|D<x>|MATH<x>}
    - BUS:B<x>:MIPICSITWo:CLOCk:SOUrce?
    - BUS:B<x>:MIPICSITWo:CLOCk:TYPe {ANALog|DIGItal}
    - BUS:B<x>:MIPICSITWo:CLOCk:TYPe?
    - BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DIFFerential {D<x>}
    - BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DIFFerential?
    - BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DMINUS {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
    - BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DMINUS?
    - BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DPLUS {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
    - BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DPLUS?
    - BUS:B<x>:MIPICSITWo:LANE<x>:TYPe {ANALog|DIGItal}
    - BUS:B<x>:MIPICSITWo:LANE<x>:TYPe?
    - BUS:B<x>:MIPIDSIOne:CLOCk:SOUrce {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
    - BUS:B<x>:MIPIDSIOne:CLOCk:SOUrce?
    - BUS:B<x>:MIPIDSIOne:CLOCk:TYPe {ANALog|DIGItal}
    - BUS:B<x>:MIPIDSIOne:CLOCk:TYPe?
    - BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DIFFerential {D<x>}
    - BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DIFFerential?
    - BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DMINUS {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
    - BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DMINUS?
    - BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DPLUS {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
    - BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DPLUS?
    - BUS:B<x>:MIPIDSIOne:LANE<x>:TYPe {ANALog|DIGItal}
    - BUS:B<x>:MIPIDSIOne:LANE<x>:TYPe?
    - BUS:B<x>:PARallel:CLOCk:EDGE {FALL|RISe|EITHer}
    - BUS:B<x>:PARallel:CLOCk:EDGE?
    - BUS:B<x>:PARallel:CLOCk:SOUrce {CH<x>|D0|D1|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
    - BUS:B<x>:PARallel:CLOCk:SOUrce?
    - BUS:B<x>:PARallel:ISCLOCKED {YES|NO}
    - BUS:B<x>:PARallel:ISCLOCKED?
    - BUS:B<x>:PARallel:SOURCES {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
    - BUS:B<x>:PARallel:SOURCES?
    - BUS:B<x>:PCIE:BITRate {RATE2500|RATE5000|RATE8000|RATE16000|AUTO|CUSTom}
    - BUS:B<x>:PCIE:BITRate:VALue <nr3>
    - BUS:B<x>:PCIE:BITRate:VALue?
    - BUS:B<x>:PCIE:BITRate?
    - BUS:B<x>:PCIE:HYSTeresis <nr3>
    - BUS:B<x>:PCIE:HYSTeresis?
    - BUS:B<x>:PCIE:LANE <nr3>
    - BUS:B<x>:PCIE:LANE?
    - BUS:B<x>:PCIE:SOUrce {CH<x>|D0|D1|D10|D11|D12|D13|D14|D15|D2|D3|D4|D5|D6|D7|D8|D9|MATH<x>}
    - BUS:B<x>:PCIE:SOUrce?
    - BUS:B<x>:POSition <NR3>
    - BUS:B<x>:POSition?
    - BUS:B<x>:RS232C:BITRate <NR3>
    - BUS:B<x>:RS232C:BITRate?
    - BUS:B<x>:RS232C:DATABits <NR3>
    - BUS:B<x>:RS232C:DATABits?
    - BUS:B<x>:RS232C:DELIMiter {NUL1|CR|LF|SPace|XFF}
    - BUS:B<x>:RS232C:DELIMiter?
    - BUS:B<x>:RS232C:DISplaymode {FRAme|PACKET}
    - BUS:B<x>:RS232C:DISplaymode?
    - BUS:B<x>:RS232C:PARity {NONe|EVEN|ODD}
    - BUS:B<x>:RS232C:PARity?
    - BUS:B<x>:RS232C:POLarity {NORMal|INVERTed}
    - BUS:B<x>:RS232C:POLarity?
    - BUS:B<x>:RS232C:SOUrce {CH<x>|D<x>|MATH<x>}
    - BUS:B<x>:RS232C:SOUrce?
    - BUS:B<x>:S64B66B:BITRate { CUSTom|RATE10000|RATE12000|RATE14000 }
    - BUS:B<x>:S64B66B:BITRate:VALue <NR3>
    - BUS:B<x>:S64B66B:BITRate:VALue?
    - BUS:B<x>:S64B66B:BITRate?
    - BUS:B<x>:S64B66B:DESCRAMble { ON|OFF }
    - BUS:B<x>:S64B66B:DESCRAMble?
    - BUS:B<x>:S64B66B:HYSTeresis <NR3>
    - BUS:B<x>:S64B66B:HYSTeresis?
    - BUS:B<x>:S64B66B:SOUrce { CH1|CH2|CH3|CH4|MATH1|MATH2|MATH3|MATH4 }
    - BUS:B<x>:S64B66B:SOUrce?
    - BUS:B<x>:S8B10B:BITRate {CUSTom|RATE1250|RATE1500|RATE2125|RATE2500|RATE3000|RATE3125|RATE4250|RATE5000|RATE6000|RATE6250}
    - BUS:B<x>:S8B10B:BITRate:VALue <NR3>
    - BUS:B<x>:S8B10B:BITRate:VALue?
    - BUS:B<x>:S8B10B:BITRate?
    - BUS:B<x>:S8B10B:HYSTeresis <NR3>
    - BUS:B<x>:S8B10B:HYSTeresis?
    - BUS:B<x>:S8B10B:SOUrce {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
    - BUS:B<x>:S8B10B:SOUrce?
    - BUS:B<x>:SPI:BITOrder {LSB|MSB}
    - BUS:B<x>:SPI:BITOrder?
    - BUS:B<x>:SPI:CLOCk:POLarity {FALL|RISE}
    - BUS:B<x>:SPI:CLOCk:POLarity?
    - BUS:B<x>:SPI:CLOCk:SOUrce {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
    - BUS:B<x>:SPI:CLOCk:SOUrce?
    - BUS:B<x>:SPI:DATa:DELay <NR1>
    - BUS:B<x>:SPI:DATa:DELay?
    - BUS:B<x>:SPI:DATa:POLarity {high|low}
    - BUS:B<x>:SPI:DATa:POLarity?
    - BUS:B<x>:SPI:DATa:SIZe <NR3>
    - BUS:B<x>:SPI:DATa:SIZe?
    - BUS:B<x>:SPI:DATa:SOUrce {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
    - BUS:B<x>:SPI:DATa:SOUrce?
    - BUS:B<x>:SPI:FRAMING {IDLE|SS}
    - BUS:B<x>:SPI:FRAMING?
    - BUS:B<x>:SPI:IDLETime <nr3>
    - BUS:B<x>:SPI:IDLETime?
    - BUS:B<x>:SPI:SELect:POLarity {LOW|HIGH}
    - BUS:B<x>:SPI:SELect:POLarity?
    - BUS:B<x>:SPI:SELect:SOUrce {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
    - BUS:B<x>:SPI:SELect:SOUrce?
    - BUS:B<x>:TYPe {CAN|CUSTom|FLEXRAY|LIN|I2C|MIPICSITWo|MIPIDSIOne|PARallel|PCIE|RS232c|S8B10B|SPI|USB|ETHernet}
    - BUS:B<x>:TYPe?
    - BUS:B<x>:USB:BITRate {FULL|HIGH|LOW}
    - BUS:B<x>:USB:BITRate?
    - BUS:B<x>:USB:PRObe {DIFFerential|SINGleended}
    - BUS:B<x>:USB:PRObe?
    - BUS:B<x>:USB:SOUrce {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
    - BUS:B<x>:USB:SOUrce:DMINus {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
    - BUS:B<x>:USB:SOUrce:DMINus?
    - BUS:B<x>:USB:SOUrce:DPLUs {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
    - BUS:B<x>:USB:SOUrce:DPLUs?
    - BUS:B<x>:USB:SOUrce?
    - BUS:CH<x>:LOWTHRESHold <NR3>
    - BUS:CH<x>:LOWTHRESHold?
    - BUS:CH<x>:THRESHold <NR3>
    - BUS:CH<x>:THRESHold?
    - BUS:MATH<x>:LOWTHRESHold <NR3>
    - BUS:MATH<x>:LOWTHRESHold?
    - BUS:MATH<x>:THRESHold <NR3>
    - BUS:MATH<x>:THRESHold?
    - BUS:REF<x>:THRESHold <NR3>
    - BUS:REF<x>:THRESHold?
    ```
"""  # noqa: E501

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    ValidatedChannel,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class BusRefItemThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:REF<x>:THRESHold`` command.

    Description:
        - If there is a high and low threshold for the reference waveform in the bus, this command
          sets or queries the high threshold value. Otherwise, this command sets or queries the
          threshold value.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:REF<x>:THRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:REF<x>:THRESHold?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:REF<x>:THRESHold value`` command.

    SCPI Syntax:
        ```
        - BUS:REF<x>:THRESHold <NR3>
        - BUS:REF<x>:THRESHold?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the high threshold value for the
          reference waveform. The default value is 0 V.
    """


class BusRefItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``BUS:REF<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:REF<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.threshold``: The ``BUS:REF<x>:THRESHold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._threshold = BusRefItemThreshold(device, f"{self._cmd_syntax}:THRESHold")

    @property
    def threshold(self) -> BusRefItemThreshold:
        """Return the ``BUS:REF<x>:THRESHold`` command.

        Description:
            - If there is a high and low threshold for the reference waveform in the bus, this
              command sets or queries the high threshold value. Otherwise, this command sets or
              queries the threshold value.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:REF<x>:THRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:REF<x>:THRESHold?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:REF<x>:THRESHold value``
              command.

        SCPI Syntax:
            ```
            - BUS:REF<x>:THRESHold <NR3>
            - BUS:REF<x>:THRESHold?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the high threshold value for the
              reference waveform. The default value is 0 V.
        """
        return self._threshold


class BusMathItemThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:MATH<x>:THRESHold`` command.

    Description:
        - If there is a high and low threshold for the mathematical waveform in the bus, this
          command sets or queries the high threshold value. Otherwise, this command sets or queries
          the threshold value.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:MATH<x>:THRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:MATH<x>:THRESHold?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:MATH<x>:THRESHold value`` command.

    SCPI Syntax:
        ```
        - BUS:MATH<x>:THRESHold <NR3>
        - BUS:MATH<x>:THRESHold?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the high threshold value for the
          mathematical waveform. The default value is 0 V.
    """


class BusMathItemLowthreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:MATH<x>:LOWTHRESHold`` command.

    Description:
        - This command sets or queries the low threshold value of the mathematical waveform for the
          bus (USB differential).

    Usage:
        - Using the ``.query()`` method will send the ``BUS:MATH<x>:LOWTHRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:MATH<x>:LOWTHRESHold?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:MATH<x>:LOWTHRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:MATH<x>:LOWTHRESHold <NR3>
        - BUS:MATH<x>:LOWTHRESHold?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the threshold in Volts. The default
          value is 0V.
    """


class BusMathItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``BUS:MATH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:MATH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:MATH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.lowthreshold``: The ``BUS:MATH<x>:LOWTHRESHold`` command.
        - ``.threshold``: The ``BUS:MATH<x>:THRESHold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._lowthreshold = BusMathItemLowthreshold(device, f"{self._cmd_syntax}:LOWTHRESHold")
        self._threshold = BusMathItemThreshold(device, f"{self._cmd_syntax}:THRESHold")

    @property
    def lowthreshold(self) -> BusMathItemLowthreshold:
        """Return the ``BUS:MATH<x>:LOWTHRESHold`` command.

        Description:
            - This command sets or queries the low threshold value of the mathematical waveform for
              the bus (USB differential).

        Usage:
            - Using the ``.query()`` method will send the ``BUS:MATH<x>:LOWTHRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:MATH<x>:LOWTHRESHold?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:MATH<x>:LOWTHRESHold value``
              command.

        SCPI Syntax:
            ```
            - BUS:MATH<x>:LOWTHRESHold <NR3>
            - BUS:MATH<x>:LOWTHRESHold?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the threshold in Volts. The
              default value is 0V.
        """
        return self._lowthreshold

    @property
    def threshold(self) -> BusMathItemThreshold:
        """Return the ``BUS:MATH<x>:THRESHold`` command.

        Description:
            - If there is a high and low threshold for the mathematical waveform in the bus, this
              command sets or queries the high threshold value. Otherwise, this command sets or
              queries the threshold value.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:MATH<x>:THRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:MATH<x>:THRESHold?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:MATH<x>:THRESHold value``
              command.

        SCPI Syntax:
            ```
            - BUS:MATH<x>:THRESHold <NR3>
            - BUS:MATH<x>:THRESHold?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the high threshold value for the
              mathematical waveform. The default value is 0 V.
        """
        return self._threshold


class BusChannelThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:CH<x>:THRESHold`` command.

    Description:
        - If there is a high and low threshold for the analog source in the bus, this command sets
          or queries the high threshold value. Otherwise, this command sets or queries the threshold
          value.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:CH<x>:THRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:CH<x>:THRESHold?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:CH<x>:THRESHold value`` command.

    SCPI Syntax:
        ```
        - BUS:CH<x>:THRESHold <NR3>
        - BUS:CH<x>:THRESHold?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the high threshold value for the
          specified analog source. The default value is 1.4 V.
    """


class BusChannelLowthreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:CH<x>:LOWTHRESHold`` command.

    Description:
        - This command sets or queries the low threshold value for the analog source in the bus (USB
          differential).

    Usage:
        - Using the ``.query()`` method will send the ``BUS:CH<x>:LOWTHRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:CH<x>:LOWTHRESHold?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:CH<x>:LOWTHRESHold value`` command.

    SCPI Syntax:
        ```
        - BUS:CH<x>:LOWTHRESHold <NR3>
        - BUS:CH<x>:LOWTHRESHold?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the threshold in millivolts. The
          default value is -200 mV.
    """


class BusChannel(ValidatedChannel, SCPICmdRead):
    """The ``BUS:CH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:CH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.lowthreshold``: The ``BUS:CH<x>:LOWTHRESHold`` command.
        - ``.threshold``: The ``BUS:CH<x>:THRESHold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._lowthreshold = BusChannelLowthreshold(device, f"{self._cmd_syntax}:LOWTHRESHold")
        self._threshold = BusChannelThreshold(device, f"{self._cmd_syntax}:THRESHold")

    @property
    def lowthreshold(self) -> BusChannelLowthreshold:
        """Return the ``BUS:CH<x>:LOWTHRESHold`` command.

        Description:
            - This command sets or queries the low threshold value for the analog source in the bus
              (USB differential).

        Usage:
            - Using the ``.query()`` method will send the ``BUS:CH<x>:LOWTHRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:CH<x>:LOWTHRESHold?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:CH<x>:LOWTHRESHold value``
              command.

        SCPI Syntax:
            ```
            - BUS:CH<x>:LOWTHRESHold <NR3>
            - BUS:CH<x>:LOWTHRESHold?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the threshold in millivolts. The
              default value is -200 mV.
        """
        return self._lowthreshold

    @property
    def threshold(self) -> BusChannelThreshold:
        """Return the ``BUS:CH<x>:THRESHold`` command.

        Description:
            - If there is a high and low threshold for the analog source in the bus, this command
              sets or queries the high threshold value. Otherwise, this command sets or queries the
              threshold value.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:CH<x>:THRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:CH<x>:THRESHold?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:CH<x>:THRESHold value``
              command.

        SCPI Syntax:
            ```
            - BUS:CH<x>:THRESHold <NR3>
            - BUS:CH<x>:THRESHold?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the high threshold value for the
              specified analog source. The default value is 1.4 V.
        """
        return self._threshold


class BusBItemUsbSourceDplus(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:USB:SOUrce:DPLUs`` command.

    Description:
        - This command sets or queries the USB Data Source for D+ input. If you are using
          single-ended probes, you need to set the sources for both the D+ and D- inputs.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:USB:SOUrce:DPLUs?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:SOUrce:DPLUs?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:SOUrce:DPLUs value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:USB:SOUrce:DPLUs {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
        - BUS:B<x>:USB:SOUrce:DPLUs?
        ```

    Info:
        - ``CH1-Ch4`` specifies an analog channel as the D+ source for the specified USB bus.
        - ``D<x>`` specifies a digital channel as the D+ source for the specified USB bus. x has a
          minimum of 0 and a maximum of 15.
        - ``MATH<x>`` specifies a math channel as the D+ source for the specified USB bus. x has a
          minimum of 1 and a maximum of 4.
    """  # noqa: E501


class BusBItemUsbSourceDminus(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:USB:SOUrce:DMINus`` command.

    Description:
        - This command sets or queries the USB Data Source for D- input for bus <x>, where x is the
          bus number. If you are using single-ended probes, you need to set the sources for both the
          D+ and D- inputs.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:USB:SOUrce:DMINus?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:SOUrce:DMINus?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:SOUrce:DMINus value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:USB:SOUrce:DMINus {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
        - BUS:B<x>:USB:SOUrce:DMINus?
        ```

    Info:
        - ``CH1-Ch4`` specifies an analog channel as the D- source for the specified USB bus.
        - ``D<x>`` specifies a digital channel as the D-source for the specified USB bus. x has a
          minimum of 0 and a maximum of 15.
        - ``MATH<x>`` specifies a math channel as the D- source for the specified USB bus. x has a
          minimum of 1 and a maximum of 4.
    """  # noqa: E501


class BusBItemUsbSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:USB:SOUrce`` command.

    Description:
        - This command sets or queries the USB Data Source for bus <x>, where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:USB:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:SOUrce?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:USB:SOUrce {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
        - BUS:B<x>:USB:SOUrce?
        ```

    Info:
        - ``CH1-Ch4`` specifies an analog channel as the data source for the specified USB bus.
        - ``D<x>`` specifies a digital channel as the data source for the specified USB bus. x has a
          minimum of 0 and a maximum of 15.
        - ``MATH<x>`` specifies a math channel as the data source for the specified USB bus. x has a
          minimum of 1 and a maximum of 4.

    Properties:
        - ``.dminus``: The ``BUS:B<x>:USB:SOUrce:DMINus`` command.
        - ``.dplus``: The ``BUS:B<x>:USB:SOUrce:DPLUs`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._dminus = BusBItemUsbSourceDminus(device, f"{self._cmd_syntax}:DMINus")
        self._dplus = BusBItemUsbSourceDplus(device, f"{self._cmd_syntax}:DPLUs")

    @property
    def dminus(self) -> BusBItemUsbSourceDminus:
        """Return the ``BUS:B<x>:USB:SOUrce:DMINus`` command.

        Description:
            - This command sets or queries the USB Data Source for D- input for bus <x>, where x is
              the bus number. If you are using single-ended probes, you need to set the sources for
              both the D+ and D- inputs.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:USB:SOUrce:DMINus?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:SOUrce:DMINus?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:SOUrce:DMINus value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:USB:SOUrce:DMINus {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
            - BUS:B<x>:USB:SOUrce:DMINus?
            ```

        Info:
            - ``CH1-Ch4`` specifies an analog channel as the D- source for the specified USB bus.
            - ``D<x>`` specifies a digital channel as the D-source for the specified USB bus. x has
              a minimum of 0 and a maximum of 15.
            - ``MATH<x>`` specifies a math channel as the D- source for the specified USB bus. x has
              a minimum of 1 and a maximum of 4.
        """  # noqa: E501
        return self._dminus

    @property
    def dplus(self) -> BusBItemUsbSourceDplus:
        """Return the ``BUS:B<x>:USB:SOUrce:DPLUs`` command.

        Description:
            - This command sets or queries the USB Data Source for D+ input. If you are using
              single-ended probes, you need to set the sources for both the D+ and D- inputs.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:USB:SOUrce:DPLUs?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:SOUrce:DPLUs?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:SOUrce:DPLUs value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:USB:SOUrce:DPLUs {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
            - BUS:B<x>:USB:SOUrce:DPLUs?
            ```

        Info:
            - ``CH1-Ch4`` specifies an analog channel as the D+ source for the specified USB bus.
            - ``D<x>`` specifies a digital channel as the D+ source for the specified USB bus. x has
              a minimum of 0 and a maximum of 15.
            - ``MATH<x>`` specifies a math channel as the D+ source for the specified USB bus. x has
              a minimum of 1 and a maximum of 4.
        """  # noqa: E501
        return self._dplus


class BusBItemUsbProbe(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:USB:PRObe`` command.

    Description:
        - This command specifies the type of probe connected to the USB bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:USB:PRObe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:PRObe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:PRObe value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:USB:PRObe {DIFFerential|SINGleended}
        - BUS:B<x>:USB:PRObe?
        ```

    Info:
        - ``DIFFerential`` indicates the bus probe is a differential probe.
        - ``SINGleended`` indicates the bus probe is not a differential probe.
    """


class BusBItemUsbBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:USB:BITRate`` command.

    Description:
        - This command sets or queries the USB data rate for bus <x>, where the bus number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:USB:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:BITRate value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:USB:BITRate {FULL|HIGH|LOW}
        - BUS:B<x>:USB:BITRate?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``FULL`` indicates the bit rate is 12 Mbps.
        - ``HIGH`` indicates the bit rate is 480 Mbps.
        - ``LOW`` indicates the bit rate is 1.5 Mbps.
    """


class BusBItemUsb(SCPICmdRead):
    """The ``BUS:B<x>:USB`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:USB?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:USB:BITRate`` command.
        - ``.probe``: The ``BUS:B<x>:USB:PRObe`` command.
        - ``.source``: The ``BUS:B<x>:USB:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemUsbBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._probe = BusBItemUsbProbe(device, f"{self._cmd_syntax}:PRObe")
        self._source = BusBItemUsbSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def bitrate(self) -> BusBItemUsbBitrate:
        """Return the ``BUS:B<x>:USB:BITRate`` command.

        Description:
            - This command sets or queries the USB data rate for bus <x>, where the bus number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:USB:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:BITRate?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:USB:BITRate {FULL|HIGH|LOW}
            - BUS:B<x>:USB:BITRate?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``FULL`` indicates the bit rate is 12 Mbps.
            - ``HIGH`` indicates the bit rate is 480 Mbps.
            - ``LOW`` indicates the bit rate is 1.5 Mbps.
        """
        return self._bitrate

    @property
    def probe(self) -> BusBItemUsbProbe:
        """Return the ``BUS:B<x>:USB:PRObe`` command.

        Description:
            - This command specifies the type of probe connected to the USB bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:USB:PRObe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:PRObe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:PRObe value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:USB:PRObe {DIFFerential|SINGleended}
            - BUS:B<x>:USB:PRObe?
            ```

        Info:
            - ``DIFFerential`` indicates the bus probe is a differential probe.
            - ``SINGleended`` indicates the bus probe is not a differential probe.
        """
        return self._probe

    @property
    def source(self) -> BusBItemUsbSource:
        """Return the ``BUS:B<x>:USB:SOUrce`` command.

        Description:
            - This command sets or queries the USB Data Source for bus <x>, where x is the bus
              number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:USB:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:USB:SOUrce {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
            - BUS:B<x>:USB:SOUrce?
            ```

        Info:
            - ``CH1-Ch4`` specifies an analog channel as the data source for the specified USB bus.
            - ``D<x>`` specifies a digital channel as the data source for the specified USB bus. x
              has a minimum of 0 and a maximum of 15.
            - ``MATH<x>`` specifies a math channel as the data source for the specified USB bus. x
              has a minimum of 1 and a maximum of 4.

        Sub-properties:
            - ``.dminus``: The ``BUS:B<x>:USB:SOUrce:DMINus`` command.
            - ``.dplus``: The ``BUS:B<x>:USB:SOUrce:DPLUs`` command.
        """  # noqa: E501
        return self._source


class BusBItemType(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:TYPe`` command.

    Description:
        - This command sets or queries the type for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:TYPe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:TYPe value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:TYPe {CAN|CUSTom|FLEXRAY|LIN|I2C|MIPICSITWo|MIPIDSIOne|PARallel|PCIE|RS232c|S8B10B|SPI|USB|ETHernet}
        - BUS:B<x>:TYPe?
        ```

    Info:
        - ``CAN`` specifies a CAN bus.
        - ``CUSTom`` specifies a custom bus.
        - ``FLEXRAY`` specifies a FLEXRAY bus.
        - ``LIN`` specifies a LIN bus.
        - ``I2C`` specifies the Inter-IC bus.
        - ``MIPICSITWo`` specifies the MIPI CSI2 bus.
        - ``MIPIDSIOne`` specifies the MIPI DSI1 bus.
        - ``PARallel`` specifies the Parallel bus.
        - ``PCIE`` specifies a PCIe bus.
        - ``RS232`` specifies the RS232 Serial bus.
        - ``S8B10B`` specifies the 8B10B bus.
        - ``SPI`` specifies the Serial Peripheral Interface bus.
        - ``USB`` specifies the Universal Serial Bus.
        - ``ETHernet`` specifies the Ethernet bus.
    """  # noqa: E501


class BusBItemSpiSelectSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:SELect:SOUrce`` command.

    Description:
        - This command sets or queries the SPI Slave Select (SS) source for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:SELect:SOUrce {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
        - BUS:B<x>:SPI:SELect:SOUrce?
        ```

    Info:
        - ``CH<x>`` designates an analog channel as the busses' SPI Slave Select source. x has a
          minimum of 1 and a maximum of 4.
        - ``D<x>`` designates a digital input signal as the Slave Select source. x has a minimum of
          0 and a maximum of 15.
        - ``MATH1-MAThH4`` designates a math waveform as the Slave Select source.
    """  # noqa: E501


class BusBItemSpiSelectPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:SELect:POLarity`` command.

    Description:
        - This command sets or queries the SPI Slave Select (SS) polarity for the specified bus. The
          bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SELect:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:SELect:POLarity {LOW|HIGH}
        - BUS:B<x>:SPI:SELect:POLarity?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``LOW`` sets an active low polarity.
        - ``HIGH`` sets an active high polarity.
    """


class BusBItemSpiSelect(SCPICmdRead):
    """The ``BUS:B<x>:SPI:SELect`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:SPI:SELect:POLarity`` command.
        - ``.source``: The ``BUS:B<x>:SPI:SELect:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemSpiSelectPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemSpiSelectSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def polarity(self) -> BusBItemSpiSelectPolarity:
        """Return the ``BUS:B<x>:SPI:SELect:POLarity`` command.

        Description:
            - This command sets or queries the SPI Slave Select (SS) polarity for the specified bus.
              The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPI:SELect:POLarity value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:SELect:POLarity {LOW|HIGH}
            - BUS:B<x>:SPI:SELect:POLarity?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``LOW`` sets an active low polarity.
            - ``HIGH`` sets an active high polarity.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemSpiSelectSource:
        """Return the ``BUS:B<x>:SPI:SELect:SOUrce`` command.

        Description:
            - This command sets or queries the SPI Slave Select (SS) source for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:SELect:SOUrce {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
            - BUS:B<x>:SPI:SELect:SOUrce?
            ```

        Info:
            - ``CH<x>`` designates an analog channel as the busses' SPI Slave Select source. x has a
              minimum of 1 and a maximum of 4.
            - ``D<x>`` designates a digital input signal as the Slave Select source. x has a minimum
              of 0 and a maximum of 15.
            - ``MATH1-MAThH4`` designates a math waveform as the Slave Select source.
        """  # noqa: E501
        return self._source


class BusBItemSpiIdletime(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:IDLETime`` command.

    Description:
        - This command sets or queries the SPI idle time. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:IDLETime?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:IDLETime?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:IDLETime value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:IDLETime <nr3>
        - BUS:B<x>:SPI:IDLETime?
        ```

    Info:
        - ``<nr3>`` specifies the SPI idle time.
    """


class BusBItemSpiFraming(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:FRAMING`` command.

    Description:
        - This command sets or queries the SPI framing setting for the specified bus. The bus number
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:FRAMING?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:FRAMING?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:FRAMING value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:FRAMING {IDLE|SS}
        - BUS:B<x>:SPI:FRAMING?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``IDLE`` specifies IDLE SPI framing.
        - ``SS`` specifies SS SPI framing.
    """


class BusBItemSpiDataSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa:SOUrce`` command.

    Description:
        - This command sets or queries the SPI data (DATA) source for the bus specified by x. The
          value of x can range from 1 through 16.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATa:SOUrce {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
        - BUS:B<x>:SPI:DATa:SOUrce?
        ```

    Info:
        - ``CH<x>`` designates an analog channel as the data source for the specified SPI bus. x has
          a minimum of 1 and a maximum of 4.
        - ``MATH<x>`` designates a math waveform as the data source. x has a minimum of 1 and a
          maximum of 4.
        - ``D<x>`` designates a digital input signal as the data source. x has a minimum of 0 and a
          maximum of 15.
    """  # noqa: E501


class BusBItemSpiDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa:SIZe`` command.

    Description:
        - This command sets or queries the number of bits per word for the specified SPI bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:SIZe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATa:SIZe <NR3>
        - BUS:B<x>:SPI:DATa:SIZe?
        ```

    Info:
        - ``<NR3>`` is the data size for the specified bus. The minimum value is 2 and maximum is
          64.
    """


class BusBItemSpiDataPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa:POLarity`` command.

    Description:
        - This command sets or queries the SPI data (DATA) polarity for the bus specified by x. The
          value of x can range from 1 through 16. The SPI decode operation treats high inputs as
          ones in normal polarity and zeros in inverted polarity.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATa:POLarity {high|low}
        - BUS:B<x>:SPI:DATa:POLarity?
        ```

    Info:
        - ``high`` sets the SPI data polarity to active high.
        - ``low`` sets the SPI data polarity to active low.
    """


class BusBItemSpiDataDelay(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa:DELay`` command.

    Description:
        - This command sets or queries the SPI data (DATA) delay for the bus specified by x. The
          value of x can range from 1 through 16. It controls the number of SPI data bits the
          decoding process will ignore at the start of the transfer frame.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:DELay?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:DELay?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:DELay value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATa:DELay <NR1>
        - BUS:B<x>:SPI:DATa:DELay?
        ```

    Info:
        - ``<NR1>`` specifies the SPI bus data delay in bits.
    """


class BusBItemSpiData(SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.delay``: The ``BUS:B<x>:SPI:DATa:DELay`` command.
        - ``.polarity``: The ``BUS:B<x>:SPI:DATa:POLarity`` command.
        - ``.size``: The ``BUS:B<x>:SPI:DATa:SIZe`` command.
        - ``.source``: The ``BUS:B<x>:SPI:DATa:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._delay = BusBItemSpiDataDelay(device, f"{self._cmd_syntax}:DELay")
        self._polarity = BusBItemSpiDataPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._size = BusBItemSpiDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._source = BusBItemSpiDataSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def delay(self) -> BusBItemSpiDataDelay:
        """Return the ``BUS:B<x>:SPI:DATa:DELay`` command.

        Description:
            - This command sets or queries the SPI data (DATA) delay for the bus specified by x. The
              value of x can range from 1 through 16. It controls the number of SPI data bits the
              decoding process will ignore at the start of the transfer frame.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:DELay?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:DELay?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:DELay value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATa:DELay <NR1>
            - BUS:B<x>:SPI:DATa:DELay?
            ```

        Info:
            - ``<NR1>`` specifies the SPI bus data delay in bits.
        """
        return self._delay

    @property
    def polarity(self) -> BusBItemSpiDataPolarity:
        """Return the ``BUS:B<x>:SPI:DATa:POLarity`` command.

        Description:
            - This command sets or queries the SPI data (DATA) polarity for the bus specified by x.
              The value of x can range from 1 through 16. The SPI decode operation treats high
              inputs as ones in normal polarity and zeros in inverted polarity.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:POLarity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATa:POLarity {high|low}
            - BUS:B<x>:SPI:DATa:POLarity?
            ```

        Info:
            - ``high`` sets the SPI data polarity to active high.
            - ``low`` sets the SPI data polarity to active low.
        """
        return self._polarity

    @property
    def size(self) -> BusBItemSpiDataSize:
        """Return the ``BUS:B<x>:SPI:DATa:SIZe`` command.

        Description:
            - This command sets or queries the number of bits per word for the specified SPI bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:SIZe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:SIZe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:SIZe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATa:SIZe <NR3>
            - BUS:B<x>:SPI:DATa:SIZe?
            ```

        Info:
            - ``<NR3>`` is the data size for the specified bus. The minimum value is 2 and maximum
              is 64.
        """
        return self._size

    @property
    def source(self) -> BusBItemSpiDataSource:
        """Return the ``BUS:B<x>:SPI:DATa:SOUrce`` command.

        Description:
            - This command sets or queries the SPI data (DATA) source for the bus specified by x.
              The value of x can range from 1 through 16.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATa:SOUrce {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
            - BUS:B<x>:SPI:DATa:SOUrce?
            ```

        Info:
            - ``CH<x>`` designates an analog channel as the data source for the specified SPI bus. x
              has a minimum of 1 and a maximum of 4.
            - ``MATH<x>`` designates a math waveform as the data source. x has a minimum of 1 and a
              maximum of 4.
            - ``D<x>`` designates a digital input signal as the data source. x has a minimum of 0
              and a maximum of 15.
        """  # noqa: E501
        return self._source


class BusBItemSpiClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:CLOCk:SOUrce`` command.

    Description:
        - This command sets or queries the SPI clock (SCK) source for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:CLOCk:SOUrce {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
        - BUS:B<x>:SPI:CLOCk:SOUrce?
        ```

    Info:
        - ``D<x>`` designates a digital input signal as the clock source. x has a minimum of 0 and a
          maximum of 15.
        - ``CH<x>`` designates an analog channel as the buss SPI clock source. x has a minimum of 1
          and a maximum of 4.
        - ``MATH<x>`` designates a math waveform as the clock source. x has a minimum of 1 and a
          maximum of 4.
    """  # noqa: E501


class BusBItemSpiClockPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:CLOCk:POLarity`` command.

    Description:
        - This command sets or queries the SPI clock (SCLK) source polarity for the specified bus.
          The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCk:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:CLOCk:POLarity {FALL|RISE}
        - BUS:B<x>:SPI:CLOCk:POLarity?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``FALL`` sets the clock to the falling edge of the signal.
        - ``RISE`` sets the clock to the rising edge of the signal.
    """


class BusBItemSpiClock(SCPICmdRead):
    """The ``BUS:B<x>:SPI:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCk?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:SPI:CLOCk:POLarity`` command.
        - ``.source``: The ``BUS:B<x>:SPI:CLOCk:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemSpiClockPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemSpiClockSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def polarity(self) -> BusBItemSpiClockPolarity:
        """Return the ``BUS:B<x>:SPI:CLOCk:POLarity`` command.

        Description:
            - This command sets or queries the SPI clock (SCLK) source polarity for the specified
              bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCk:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:POLarity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:CLOCk:POLarity {FALL|RISE}
            - BUS:B<x>:SPI:CLOCk:POLarity?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``FALL`` sets the clock to the falling edge of the signal.
            - ``RISE`` sets the clock to the rising edge of the signal.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemSpiClockSource:
        """Return the ``BUS:B<x>:SPI:CLOCk:SOUrce`` command.

        Description:
            - This command sets or queries the SPI clock (SCK) source for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCk:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:CLOCk:SOUrce {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
            - BUS:B<x>:SPI:CLOCk:SOUrce?
            ```

        Info:
            - ``D<x>`` designates a digital input signal as the clock source. x has a minimum of 0
              and a maximum of 15.
            - ``CH<x>`` designates an analog channel as the buss SPI clock source. x has a minimum
              of 1 and a maximum of 4.
            - ``MATH<x>`` designates a math waveform as the clock source. x has a minimum of 1 and a
              maximum of 4.
        """  # noqa: E501
        return self._source


class BusBItemSpiBitorder(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:BITOrder`` command.

    Description:
        - This command sets or queries the SPI bit order for the specified bus. The bus is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:BITOrder?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:BITOrder?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:BITOrder value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:BITOrder {LSB|MSB}
        - BUS:B<x>:SPI:BITOrder?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``LSB`` specifies that each bit becomes the recovered value's new LSB, after shifting
          previously recovered bits one place to the left. The decoding happens right to left.
        - ``MSB`` specifies that each successive bit from the bus's data line becomes the new MSB of
          the recovered value, shifting any previously recovered bits one place to the right. The
          decoding happens left to right.
    """


class BusBItemSpi(SCPICmdRead):
    """The ``BUS:B<x>:SPI`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.bitorder``: The ``BUS:B<x>:SPI:BITOrder`` command.
        - ``.clock``: The ``BUS:B<x>:SPI:CLOCk`` command tree.
        - ``.data``: The ``BUS:B<x>:SPI:DATa`` command tree.
        - ``.framing``: The ``BUS:B<x>:SPI:FRAMING`` command.
        - ``.idletime``: The ``BUS:B<x>:SPI:IDLETime`` command.
        - ``.select``: The ``BUS:B<x>:SPI:SELect`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitorder = BusBItemSpiBitorder(device, f"{self._cmd_syntax}:BITOrder")
        self._clock = BusBItemSpiClock(device, f"{self._cmd_syntax}:CLOCk")
        self._data = BusBItemSpiData(device, f"{self._cmd_syntax}:DATa")
        self._framing = BusBItemSpiFraming(device, f"{self._cmd_syntax}:FRAMING")
        self._idletime = BusBItemSpiIdletime(device, f"{self._cmd_syntax}:IDLETime")
        self._select = BusBItemSpiSelect(device, f"{self._cmd_syntax}:SELect")

    @property
    def bitorder(self) -> BusBItemSpiBitorder:
        """Return the ``BUS:B<x>:SPI:BITOrder`` command.

        Description:
            - This command sets or queries the SPI bit order for the specified bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:BITOrder?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:BITOrder?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:BITOrder value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:BITOrder {LSB|MSB}
            - BUS:B<x>:SPI:BITOrder?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``LSB`` specifies that each bit becomes the recovered value's new LSB, after shifting
              previously recovered bits one place to the left. The decoding happens right to left.
            - ``MSB`` specifies that each successive bit from the bus's data line becomes the new
              MSB of the recovered value, shifting any previously recovered bits one place to the
              right. The decoding happens left to right.
        """
        return self._bitorder

    @property
    def clock(self) -> BusBItemSpiClock:
        """Return the ``BUS:B<x>:SPI:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCk?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:SPI:CLOCk:POLarity`` command.
            - ``.source``: The ``BUS:B<x>:SPI:CLOCk:SOUrce`` command.
        """
        return self._clock

    @property
    def data(self) -> BusBItemSpiData:
        """Return the ``BUS:B<x>:SPI:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.delay``: The ``BUS:B<x>:SPI:DATa:DELay`` command.
            - ``.polarity``: The ``BUS:B<x>:SPI:DATa:POLarity`` command.
            - ``.size``: The ``BUS:B<x>:SPI:DATa:SIZe`` command.
            - ``.source``: The ``BUS:B<x>:SPI:DATa:SOUrce`` command.
        """
        return self._data

    @property
    def framing(self) -> BusBItemSpiFraming:
        """Return the ``BUS:B<x>:SPI:FRAMING`` command.

        Description:
            - This command sets or queries the SPI framing setting for the specified bus. The bus
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:FRAMING?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:FRAMING?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:FRAMING value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:FRAMING {IDLE|SS}
            - BUS:B<x>:SPI:FRAMING?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``IDLE`` specifies IDLE SPI framing.
            - ``SS`` specifies SS SPI framing.
        """
        return self._framing

    @property
    def idletime(self) -> BusBItemSpiIdletime:
        """Return the ``BUS:B<x>:SPI:IDLETime`` command.

        Description:
            - This command sets or queries the SPI idle time. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:IDLETime?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:IDLETime?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:IDLETime value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:IDLETime <nr3>
            - BUS:B<x>:SPI:IDLETime?
            ```

        Info:
            - ``<nr3>`` specifies the SPI idle time.
        """
        return self._idletime

    @property
    def select(self) -> BusBItemSpiSelect:
        """Return the ``BUS:B<x>:SPI:SELect`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:SPI:SELect:POLarity`` command.
            - ``.source``: The ``BUS:B<x>:SPI:SELect:SOUrce`` command.
        """
        return self._select


class BusBItemS8b10bSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:S8B10B:SOUrce`` command.

    Description:
        - Sets or queries the signal sources for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:S8B10B:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S8B10B:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:S8B10B:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:S8B10B:SOUrce {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
        - BUS:B<x>:S8B10B:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel to use as the bus signal source. x has a minimum of
          1 and a maximum of 4.
        - ``D<x>`` specifies a digital channel to use as the bus signal source. x has a minimum of 0
          and a maximum of 15.
        - ``MATH<x>`` specifies a math channel to use as the bus signal source. x has a minimum of 1
          and a maximum of 4.
    """  # noqa: E501


class BusBItemS8b10bHysteresis(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:S8B10B:HYSTeresis`` command.

    Description:
        - Sets or queries the hysteresis for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:S8B10B:HYSTeresis?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S8B10B:HYSTeresis?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:S8B10B:HYSTeresis value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:S8B10B:HYSTeresis <NR3>
        - BUS:B<x>:S8B10B:HYSTeresis?
        ```
    """


class BusBItemS8b10bBitrateValue(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:S8B10B:BITRate:VALue`` command.

    Description:
        - Sets the data rate for the specified bus to a rate that you specify in bits per second.
          The bitrate must be set to custom (see Related Commands, below).

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:S8B10B:BITRate:VALue?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S8B10B:BITRate:VALue?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:S8B10B:BITRate:VALue value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:S8B10B:BITRate:VALue <NR3>
        - BUS:B<x>:S8B10B:BITRate:VALue?
        ```

    Info:
        - ``<NR3>`` is the data rate in bits per second.
    """


class BusBItemS8b10bBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:S8B10B:BITRate`` command.

    Description:
        - Sets the bus data for the specified bus to a standard rate in bits per second, or enables
          you to specify a custom data rate using the value command. The query returns the bus data
          rate that is set for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:S8B10B:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S8B10B:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:S8B10B:BITRate value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:S8B10B:BITRate {CUSTom|RATE1250|RATE1500|RATE2125|RATE2500|RATE3000|RATE3125|RATE4250|RATE5000|RATE6000|RATE6250}
        - BUS:B<x>:S8B10B:BITRate?
        ```

    Info:
        - ``CUSTOM`` sets the bus data rate to Custom, allowing you to set the value (see Related
          Commands).
        - ``RATE1250`` sets the bus data rate to 1.25 Gb/s.
        - ``RATE1500`` sets the bus data rate to 1.5 Gb/s.
        - ``RATE2125`` sets the bus data rate to 2.125 Gb/s.
        - ``RATE2500`` sets the bus data rate to 2.5 Gb/s.
        - ``RATE3000`` sets the bus data rate to 3.0 Gb/s.
        - ``RATE3125`` sets the bus data rate to 3.125 Gb/s.
        - ``RATE4250`` sets the bus data rate to 4.25 Gb/s.
        - ``RATE5000`` sets the bus data rate to 5.0 Gb/s.
        - ``RATE6000`` sets the bus data rate to 6.0 Gb/s.
        - ``RATE6250`` sets the bus data rate to 6.25 Gb/s.

    Properties:
        - ``.value``: The ``BUS:B<x>:S8B10B:BITRate:VALue`` command.
    """  # noqa: E501

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = BusBItemS8b10bBitrateValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> BusBItemS8b10bBitrateValue:
        """Return the ``BUS:B<x>:S8B10B:BITRate:VALue`` command.

        Description:
            - Sets the data rate for the specified bus to a rate that you specify in bits per
              second. The bitrate must be set to custom (see Related Commands, below).

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:S8B10B:BITRate:VALue?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S8B10B:BITRate:VALue?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:S8B10B:BITRate:VALue value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:S8B10B:BITRate:VALue <NR3>
            - BUS:B<x>:S8B10B:BITRate:VALue?
            ```

        Info:
            - ``<NR3>`` is the data rate in bits per second.
        """
        return self._value


class BusBItemS8b10b(SCPICmdRead):
    """The ``BUS:B<x>:S8B10B`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:S8B10B?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S8B10B?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:S8B10B:BITRate`` command.
        - ``.hysteresis``: The ``BUS:B<x>:S8B10B:HYSTeresis`` command.
        - ``.source``: The ``BUS:B<x>:S8B10B:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemS8b10bBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._hysteresis = BusBItemS8b10bHysteresis(device, f"{self._cmd_syntax}:HYSTeresis")
        self._source = BusBItemS8b10bSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def bitrate(self) -> BusBItemS8b10bBitrate:
        """Return the ``BUS:B<x>:S8B10B:BITRate`` command.

        Description:
            - Sets the bus data for the specified bus to a standard rate in bits per second, or
              enables you to specify a custom data rate using the value command. The query returns
              the bus data rate that is set for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:S8B10B:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S8B10B:BITRate?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:S8B10B:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:S8B10B:BITRate {CUSTom|RATE1250|RATE1500|RATE2125|RATE2500|RATE3000|RATE3125|RATE4250|RATE5000|RATE6000|RATE6250}
            - BUS:B<x>:S8B10B:BITRate?
            ```

        Info:
            - ``CUSTOM`` sets the bus data rate to Custom, allowing you to set the value (see
              Related Commands).
            - ``RATE1250`` sets the bus data rate to 1.25 Gb/s.
            - ``RATE1500`` sets the bus data rate to 1.5 Gb/s.
            - ``RATE2125`` sets the bus data rate to 2.125 Gb/s.
            - ``RATE2500`` sets the bus data rate to 2.5 Gb/s.
            - ``RATE3000`` sets the bus data rate to 3.0 Gb/s.
            - ``RATE3125`` sets the bus data rate to 3.125 Gb/s.
            - ``RATE4250`` sets the bus data rate to 4.25 Gb/s.
            - ``RATE5000`` sets the bus data rate to 5.0 Gb/s.
            - ``RATE6000`` sets the bus data rate to 6.0 Gb/s.
            - ``RATE6250`` sets the bus data rate to 6.25 Gb/s.

        Sub-properties:
            - ``.value``: The ``BUS:B<x>:S8B10B:BITRate:VALue`` command.
        """  # noqa: E501
        return self._bitrate

    @property
    def hysteresis(self) -> BusBItemS8b10bHysteresis:
        """Return the ``BUS:B<x>:S8B10B:HYSTeresis`` command.

        Description:
            - Sets or queries the hysteresis for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:S8B10B:HYSTeresis?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S8B10B:HYSTeresis?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:S8B10B:HYSTeresis value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:S8B10B:HYSTeresis <NR3>
            - BUS:B<x>:S8B10B:HYSTeresis?
            ```
        """
        return self._hysteresis

    @property
    def source(self) -> BusBItemS8b10bSource:
        """Return the ``BUS:B<x>:S8B10B:SOUrce`` command.

        Description:
            - Sets or queries the signal sources for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:S8B10B:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S8B10B:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:S8B10B:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:S8B10B:SOUrce {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
            - BUS:B<x>:S8B10B:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel to use as the bus signal source. x has a minimum
              of 1 and a maximum of 4.
            - ``D<x>`` specifies a digital channel to use as the bus signal source. x has a minimum
              of 0 and a maximum of 15.
            - ``MATH<x>`` specifies a math channel to use as the bus signal source. x has a minimum
              of 1 and a maximum of 4.
        """  # noqa: E501
        return self._source


class BusBItemS64b66bSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:S64B66B:SOUrce`` command.

    Description:
        - Set or query the signal sources for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:S64B66B:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S64B66B:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:S64B66B:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:S64B66B:SOUrce { CH1|CH2|CH3|CH4|MATH1|MATH2|MATH3|MATH4 }
        - BUS:B<x>:S64B66B:SOUrce?
        ```

    Info:
        - ``CH<x>`` is the analog channel used as the signal source. x has a minimum of 1 and a
          maximum of 4.
        - ``MATH<x>`` is the math channel used as the signal source. x has a minimum of 1 and a
          maximum of 4.
    """


class BusBItemS64b66bHysteresis(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:S64B66B:HYSTeresis`` command.

    Description:
        - Set or query the hysteresis of the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:S64B66B:HYSTeresis?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S64B66B:HYSTeresis?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:S64B66B:HYSTeresis value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:S64B66B:HYSTeresis <NR3>
        - BUS:B<x>:S64B66B:HYSTeresis?
        ```

    Info:
        - ``<NR3>`` is the hysteresis value.
    """


class BusBItemS64b66bDescramble(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:S64B66B:DESCRAMble`` command.

    Description:
        - Set or query that the Descramble checkbox is checked (ON) or unchecked (OFF).

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:S64B66B:DESCRAMble?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S64B66B:DESCRAMble?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:S64B66B:DESCRAMble value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:S64B66B:DESCRAMble { ON|OFF }
        - BUS:B<x>:S64B66B:DESCRAMble?
        ```

    Info:
        - ``ON`` enables descrambling.
        - ``OFF`` disables descrambling.
    """


class BusBItemS64b66bBitrateValue(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:S64B66B:BITRate:VALue`` command.

    Description:
        - Set or query the data rate for the specified bus to a rate that you specify in bits per
          second. The bitrate must be set to custom (see Related Commands, below).

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:S64B66B:BITRate:VALue?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S64B66B:BITRate:VALue?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:S64B66B:BITRate:VALue value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:S64B66B:BITRate:VALue <NR3>
        - BUS:B<x>:S64B66B:BITRate:VALue?
        ```

    Info:
        - ``<NR3>`` is the data rate in bits per second.
    """


class BusBItemS64b66bBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:S64B66B:BITRate`` command.

    Description:
        - Set or query the data rate for the specified bus to a standard rate in bits per second, or
          enables you to specify a custom data rate using ``BUS:B<x>:S64B66B:BITRate:VALue``. The
          query returns the data rate that is set for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:S64B66B:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S64B66B:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:S64B66B:BITRate value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:S64B66B:BITRate { CUSTom|RATE10000|RATE12000|RATE14000 }
        - BUS:B<x>:S64B66B:BITRate?
        ```

    Info:
        - ``CUSTom`` sets the data rate to Custom, allowing you to set the value. (See Related
          Commands.).
        - ``RATE10000`` sets the data rate to 10 Gb/s.
        - ``RATE12000`` sets the data rate to 12 Gb/s.
        - ``RATE14000`` sets the data rate to 14 Gb/s.

    Properties:
        - ``.value``: The ``BUS:B<x>:S64B66B:BITRate:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = BusBItemS64b66bBitrateValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> BusBItemS64b66bBitrateValue:
        """Return the ``BUS:B<x>:S64B66B:BITRate:VALue`` command.

        Description:
            - Set or query the data rate for the specified bus to a rate that you specify in bits
              per second. The bitrate must be set to custom (see Related Commands, below).

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:S64B66B:BITRate:VALue?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S64B66B:BITRate:VALue?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:S64B66B:BITRate:VALue value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:S64B66B:BITRate:VALue <NR3>
            - BUS:B<x>:S64B66B:BITRate:VALue?
            ```

        Info:
            - ``<NR3>`` is the data rate in bits per second.
        """
        return self._value


class BusBItemS64b66b(SCPICmdRead):
    """The ``BUS:B<x>:S64B66B`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:S64B66B?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S64B66B?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:S64B66B:BITRate`` command.
        - ``.descramble``: The ``BUS:B<x>:S64B66B:DESCRAMble`` command.
        - ``.hysteresis``: The ``BUS:B<x>:S64B66B:HYSTeresis`` command.
        - ``.source``: The ``BUS:B<x>:S64B66B:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemS64b66bBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._descramble = BusBItemS64b66bDescramble(device, f"{self._cmd_syntax}:DESCRAMble")
        self._hysteresis = BusBItemS64b66bHysteresis(device, f"{self._cmd_syntax}:HYSTeresis")
        self._source = BusBItemS64b66bSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def bitrate(self) -> BusBItemS64b66bBitrate:
        """Return the ``BUS:B<x>:S64B66B:BITRate`` command.

        Description:
            - Set or query the data rate for the specified bus to a standard rate in bits per
              second, or enables you to specify a custom data rate using
              ``BUS:B<x>:S64B66B:BITRate:VALue``. The query returns the data rate that is set for
              the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:S64B66B:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S64B66B:BITRate?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:S64B66B:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:S64B66B:BITRate { CUSTom|RATE10000|RATE12000|RATE14000 }
            - BUS:B<x>:S64B66B:BITRate?
            ```

        Info:
            - ``CUSTom`` sets the data rate to Custom, allowing you to set the value. (See Related
              Commands.).
            - ``RATE10000`` sets the data rate to 10 Gb/s.
            - ``RATE12000`` sets the data rate to 12 Gb/s.
            - ``RATE14000`` sets the data rate to 14 Gb/s.

        Sub-properties:
            - ``.value``: The ``BUS:B<x>:S64B66B:BITRate:VALue`` command.
        """
        return self._bitrate

    @property
    def descramble(self) -> BusBItemS64b66bDescramble:
        """Return the ``BUS:B<x>:S64B66B:DESCRAMble`` command.

        Description:
            - Set or query that the Descramble checkbox is checked (ON) or unchecked (OFF).

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:S64B66B:DESCRAMble?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S64B66B:DESCRAMble?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:S64B66B:DESCRAMble value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:S64B66B:DESCRAMble { ON|OFF }
            - BUS:B<x>:S64B66B:DESCRAMble?
            ```

        Info:
            - ``ON`` enables descrambling.
            - ``OFF`` disables descrambling.
        """
        return self._descramble

    @property
    def hysteresis(self) -> BusBItemS64b66bHysteresis:
        """Return the ``BUS:B<x>:S64B66B:HYSTeresis`` command.

        Description:
            - Set or query the hysteresis of the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:S64B66B:HYSTeresis?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S64B66B:HYSTeresis?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:S64B66B:HYSTeresis value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:S64B66B:HYSTeresis <NR3>
            - BUS:B<x>:S64B66B:HYSTeresis?
            ```

        Info:
            - ``<NR3>`` is the hysteresis value.
        """
        return self._hysteresis

    @property
    def source(self) -> BusBItemS64b66bSource:
        """Return the ``BUS:B<x>:S64B66B:SOUrce`` command.

        Description:
            - Set or query the signal sources for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:S64B66B:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S64B66B:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:S64B66B:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:S64B66B:SOUrce { CH1|CH2|CH3|CH4|MATH1|MATH2|MATH3|MATH4 }
            - BUS:B<x>:S64B66B:SOUrce?
            ```

        Info:
            - ``CH<x>`` is the analog channel used as the signal source. x has a minimum of 1 and a
              maximum of 4.
            - ``MATH<x>`` is the math channel used as the signal source. x has a minimum of 1 and a
              maximum of 4.
        """
        return self._source


class BusBItemRs232cSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:SOUrce`` command.

    Description:
        - This command sets or queries the RS-232 polarity for bus <x>, where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:SOUrce {CH<x>|D<x>|MATH<x>}
        - BUS:B<x>:RS232C:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel to use as the RS232C source. x has a minimum of 1
          and a maximum of 4.
        - ``D<x>`` specifies a digital channel to use for the RS232C source. x has a minimum of 0
          and a maximum of 15.
        - ``MATH<x>`` specifies a math channel to use for the RS232C source. x has a minimum of 1
          and a maximum of 4.
    """


class BusBItemRs232cPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:POLarity`` command.

    Description:
        - This command specifies the polarity for the RS-232C bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:POLarity?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:POLarity {NORMal|INVERTed}
        - BUS:B<x>:RS232C:POLarity?
        ```

    Info:
        - ``NORMal`` sets the polarity to positive.
        - ``INVERTed`` sets the polarity to negative.
    """


class BusBItemRs232cParity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:PARity`` command.

    Description:
        - This command sets or queries the RS-232C parity for bus <x>, where the bus number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:PARity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:PARity?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:PARity value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:PARity {NONe|EVEN|ODD}
        - BUS:B<x>:RS232C:PARity?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``NONe`` specifies no parity.
        - ``EVEN`` specifies even parity.
        - ``ODD`` specifies odd parity.
    """


class BusBItemRs232cDisplaymode(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:DISplaymode`` command.

    Description:
        - This command specifies the display mode for the RS-232 bus (frame or packet).

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:DISplaymode?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:DISplaymode?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:DISplaymode value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:DISplaymode {FRAme|PACKET}
        - BUS:B<x>:RS232C:DISplaymode?
        ```

    Info:
        - ``FRAme`` displays each frame as a single entity.
        - ``PACKET`` displays a group of frames terminated with a single frame defined by the
          ``BUS:B<x>:RS232C:DELImiter`` command or the front panel.
    """


class BusBItemRs232cDelimiter(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:DELIMiter`` command.

    Description:
        - This command sets or queries the RS-232C delimiting value for a packet on bus <x>, where x
          is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:DELIMiter?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:DELIMiter?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:DELIMiter value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:DELIMiter {NUL1|CR|LF|SPace|XFF}
        - BUS:B<x>:RS232C:DELIMiter?
        ```

    Info:
        - ``NULl`` specifies NULl (0x00 ) delimiting value for a packet.
        - ``CR`` specifies CR (0x0D) delimiting value for a packet.
        - ``LF`` specifies LF (0x0A) delimiting value for a packet.
        - ``XFF`` specifies XFF (0xFF) delimiting value for a packet.
        - ``SPace`` specifies SPace delimiting value for a packet.
    """


class BusBItemRs232cDatabits(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:DATABits`` command.

    Description:
        - This command sets or queries the number of RS-232C data bits for bus<x>, where x is the
          bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:DATABits?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:DATABits?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:DATABits value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:DATABits <NR3>
        - BUS:B<x>:RS232C:DATABits?
        ```

    Info:
        - ``<NR3>`` specifies the number of bits in the RS-232C data frame.
    """


class BusBItemRs232cBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:BITRate`` command.

    Description:
        - This command sets or queries the RS232C bit rate for bus<x>, where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:BITRate value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:BITRate <NR3>
        - BUS:B<x>:RS232C:BITRate?
        ```

    Info:
        - ``<NR3>`` is the bit rate in bits-per-second. You can enter any positive integer, and the
          instrument will coerce the value to the closest supported bit rate.
    """


class BusBItemRs232c(SCPICmdRead):
    """The ``BUS:B<x>:RS232C`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:RS232C:BITRate`` command.
        - ``.databits``: The ``BUS:B<x>:RS232C:DATABits`` command.
        - ``.delimiter``: The ``BUS:B<x>:RS232C:DELIMiter`` command.
        - ``.displaymode``: The ``BUS:B<x>:RS232C:DISplaymode`` command.
        - ``.parity``: The ``BUS:B<x>:RS232C:PARity`` command.
        - ``.polarity``: The ``BUS:B<x>:RS232C:POLarity`` command.
        - ``.source``: The ``BUS:B<x>:RS232C:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemRs232cBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._databits = BusBItemRs232cDatabits(device, f"{self._cmd_syntax}:DATABits")
        self._delimiter = BusBItemRs232cDelimiter(device, f"{self._cmd_syntax}:DELIMiter")
        self._displaymode = BusBItemRs232cDisplaymode(device, f"{self._cmd_syntax}:DISplaymode")
        self._parity = BusBItemRs232cParity(device, f"{self._cmd_syntax}:PARity")
        self._polarity = BusBItemRs232cPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemRs232cSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def bitrate(self) -> BusBItemRs232cBitrate:
        """Return the ``BUS:B<x>:RS232C:BITRate`` command.

        Description:
            - This command sets or queries the RS232C bit rate for bus<x>, where x is the bus
              number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:BITRate?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:BITRate <NR3>
            - BUS:B<x>:RS232C:BITRate?
            ```

        Info:
            - ``<NR3>`` is the bit rate in bits-per-second. You can enter any positive integer, and
              the instrument will coerce the value to the closest supported bit rate.
        """
        return self._bitrate

    @property
    def databits(self) -> BusBItemRs232cDatabits:
        """Return the ``BUS:B<x>:RS232C:DATABits`` command.

        Description:
            - This command sets or queries the number of RS-232C data bits for bus<x>, where x is
              the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:DATABits?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:DATABits?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:DATABits value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:DATABits <NR3>
            - BUS:B<x>:RS232C:DATABits?
            ```

        Info:
            - ``<NR3>`` specifies the number of bits in the RS-232C data frame.
        """
        return self._databits

    @property
    def delimiter(self) -> BusBItemRs232cDelimiter:
        """Return the ``BUS:B<x>:RS232C:DELIMiter`` command.

        Description:
            - This command sets or queries the RS-232C delimiting value for a packet on bus <x>,
              where x is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:DELIMiter?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:DELIMiter?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:DELIMiter value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:DELIMiter {NUL1|CR|LF|SPace|XFF}
            - BUS:B<x>:RS232C:DELIMiter?
            ```

        Info:
            - ``NULl`` specifies NULl (0x00 ) delimiting value for a packet.
            - ``CR`` specifies CR (0x0D) delimiting value for a packet.
            - ``LF`` specifies LF (0x0A) delimiting value for a packet.
            - ``XFF`` specifies XFF (0xFF) delimiting value for a packet.
            - ``SPace`` specifies SPace delimiting value for a packet.
        """
        return self._delimiter

    @property
    def displaymode(self) -> BusBItemRs232cDisplaymode:
        """Return the ``BUS:B<x>:RS232C:DISplaymode`` command.

        Description:
            - This command specifies the display mode for the RS-232 bus (frame or packet).

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:DISplaymode?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:DISplaymode?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:DISplaymode value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:DISplaymode {FRAme|PACKET}
            - BUS:B<x>:RS232C:DISplaymode?
            ```

        Info:
            - ``FRAme`` displays each frame as a single entity.
            - ``PACKET`` displays a group of frames terminated with a single frame defined by the
              ``BUS:B<x>:RS232C:DELImiter`` command or the front panel.
        """
        return self._displaymode

    @property
    def parity(self) -> BusBItemRs232cParity:
        """Return the ``BUS:B<x>:RS232C:PARity`` command.

        Description:
            - This command sets or queries the RS-232C parity for bus <x>, where the bus number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:PARity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:PARity?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:PARity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:PARity {NONe|EVEN|ODD}
            - BUS:B<x>:RS232C:PARity?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``NONe`` specifies no parity.
            - ``EVEN`` specifies even parity.
            - ``ODD`` specifies odd parity.
        """
        return self._parity

    @property
    def polarity(self) -> BusBItemRs232cPolarity:
        """Return the ``BUS:B<x>:RS232C:POLarity`` command.

        Description:
            - This command specifies the polarity for the RS-232C bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:POLarity?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:POLarity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:POLarity {NORMal|INVERTed}
            - BUS:B<x>:RS232C:POLarity?
            ```

        Info:
            - ``NORMal`` sets the polarity to positive.
            - ``INVERTed`` sets the polarity to negative.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemRs232cSource:
        """Return the ``BUS:B<x>:RS232C:SOUrce`` command.

        Description:
            - This command sets or queries the RS-232 polarity for bus <x>, where x is the bus
              number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:SOUrce {CH<x>|D<x>|MATH<x>}
            - BUS:B<x>:RS232C:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel to use as the RS232C source. x has a minimum of
              1 and a maximum of 4.
            - ``D<x>`` specifies a digital channel to use for the RS232C source. x has a minimum of
              0 and a maximum of 15.
            - ``MATH<x>`` specifies a math channel to use for the RS232C source. x has a minimum of
              1 and a maximum of 4.
        """
        return self._source


class BusBItemPosition(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:POSition`` command.

    Description:
        - This command specifies the position of the bus waveform on the display.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:POSition?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:POSition value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:POSition <NR3>
        - BUS:B<x>:POSition?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the position of the bus <x> waveform
          on the display.
    """


class BusBItemPcieSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PCIE:SOUrce`` command.

    Description:
        - This command sets or queries the PCIE bus source. The bus is specified by x. The value of
          x can range from 1 to 16.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PCIE:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PCIE:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PCIE:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PCIE:SOUrce {CH<x>|D0|D1|D10|D11|D12|D13|D14|D15|D2|D3|D4|D5|D6|D7|D8|D9|MATH<x>}
        - BUS:B<x>:PCIE:SOUrce?
        ```
    """


class BusBItemPcieLane(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PCIE:LANE`` command.

    Description:
        - This command sets or queries the PCIE bus lane number. The bus is specified by x. The
          value of x can range from 1 to 16.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PCIE:LANE?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PCIE:LANE?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PCIE:LANE value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PCIE:LANE <nr3>
        - BUS:B<x>:PCIE:LANE?
        ```

    Info:
        - ``<nr3>`` specifies the bus lane.
    """


class BusBItemPcieHysteresis(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PCIE:HYSTeresis`` command.

    Description:
        - This command sets or queries the PCIE bus hysteresis. The bus is specified by x. The value
          of x can range from 1 to 16.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PCIE:HYSTeresis?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PCIE:HYSTeresis?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PCIE:HYSTeresis value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PCIE:HYSTeresis <nr3>
        - BUS:B<x>:PCIE:HYSTeresis?
        ```

    Info:
        - ``<nr3>`` specifies the hysteresis.
    """


class BusBItemPcieBitrateValue(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PCIE:BITRate:VALue`` command.

    Description:
        - This command sets or queries the PCIE bus bit rate value. The bus is specified by x. The
          value of x can range from 1 to 16.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PCIE:BITRate:VALue?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PCIE:BITRate:VALue?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PCIE:BITRate:VALue value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PCIE:BITRate:VALue <nr3>
        - BUS:B<x>:PCIE:BITRate:VALue?
        ```

    Info:
        - ``<nr3>`` specifies the bit rate value.
    """


class BusBItemPcieBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PCIE:BITRate`` command.

    Description:
        - This command sets or queries the PCIE bus bit rate. The bus is specified by x. The value
          of x can range from 1 to 16.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PCIE:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PCIE:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PCIE:BITRate value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PCIE:BITRate {RATE2500|RATE5000|RATE8000|RATE16000|AUTO|CUSTom}
        - BUS:B<x>:PCIE:BITRate?
        ```

    Properties:
        - ``.value``: The ``BUS:B<x>:PCIE:BITRate:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = BusBItemPcieBitrateValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> BusBItemPcieBitrateValue:
        """Return the ``BUS:B<x>:PCIE:BITRate:VALue`` command.

        Description:
            - This command sets or queries the PCIE bus bit rate value. The bus is specified by x.
              The value of x can range from 1 to 16.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PCIE:BITRate:VALue?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PCIE:BITRate:VALue?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:PCIE:BITRate:VALue value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PCIE:BITRate:VALue <nr3>
            - BUS:B<x>:PCIE:BITRate:VALue?
            ```

        Info:
            - ``<nr3>`` specifies the bit rate value.
        """
        return self._value


class BusBItemPcie(SCPICmdRead):
    """The ``BUS:B<x>:PCIE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PCIE?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PCIE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:PCIE:BITRate`` command.
        - ``.hysteresis``: The ``BUS:B<x>:PCIE:HYSTeresis`` command.
        - ``.lane``: The ``BUS:B<x>:PCIE:LANE`` command.
        - ``.source``: The ``BUS:B<x>:PCIE:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemPcieBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._hysteresis = BusBItemPcieHysteresis(device, f"{self._cmd_syntax}:HYSTeresis")
        self._lane = BusBItemPcieLane(device, f"{self._cmd_syntax}:LANE")
        self._source = BusBItemPcieSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def bitrate(self) -> BusBItemPcieBitrate:
        """Return the ``BUS:B<x>:PCIE:BITRate`` command.

        Description:
            - This command sets or queries the PCIE bus bit rate. The bus is specified by x. The
              value of x can range from 1 to 16.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PCIE:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PCIE:BITRate?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:PCIE:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PCIE:BITRate {RATE2500|RATE5000|RATE8000|RATE16000|AUTO|CUSTom}
            - BUS:B<x>:PCIE:BITRate?
            ```

        Sub-properties:
            - ``.value``: The ``BUS:B<x>:PCIE:BITRate:VALue`` command.
        """
        return self._bitrate

    @property
    def hysteresis(self) -> BusBItemPcieHysteresis:
        """Return the ``BUS:B<x>:PCIE:HYSTeresis`` command.

        Description:
            - This command sets or queries the PCIE bus hysteresis. The bus is specified by x. The
              value of x can range from 1 to 16.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PCIE:HYSTeresis?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PCIE:HYSTeresis?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:PCIE:HYSTeresis value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PCIE:HYSTeresis <nr3>
            - BUS:B<x>:PCIE:HYSTeresis?
            ```

        Info:
            - ``<nr3>`` specifies the hysteresis.
        """
        return self._hysteresis

    @property
    def lane(self) -> BusBItemPcieLane:
        """Return the ``BUS:B<x>:PCIE:LANE`` command.

        Description:
            - This command sets or queries the PCIE bus lane number. The bus is specified by x. The
              value of x can range from 1 to 16.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PCIE:LANE?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PCIE:LANE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:PCIE:LANE value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PCIE:LANE <nr3>
            - BUS:B<x>:PCIE:LANE?
            ```

        Info:
            - ``<nr3>`` specifies the bus lane.
        """
        return self._lane

    @property
    def source(self) -> BusBItemPcieSource:
        """Return the ``BUS:B<x>:PCIE:SOUrce`` command.

        Description:
            - This command sets or queries the PCIE bus source. The bus is specified by x. The value
              of x can range from 1 to 16.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PCIE:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PCIE:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:PCIE:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PCIE:SOUrce {CH<x>|D0|D1|D10|D11|D12|D13|D14|D15|D2|D3|D4|D5|D6|D7|D8|D9|MATH<x>}
            - BUS:B<x>:PCIE:SOUrce?
            ```
        """  # noqa: E501
        return self._source


class BusBItemParallelSources(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:SOURCES`` command.

    Description:
        - This command sets or queries the members of the Parallel mode of specified bus according
          to a supplied list of signals. The first item on the list becomes the MSB signal of the
          Bus. The second becomes the next-most-significant, and so on, with the last item becoming
          the LSB of the bus. If no signals are listed, the Bus is emptied of members. No signal can
          appear more than once in the list of bus members.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:SOURCES?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:SOURCES?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PARallel:SOURCES value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:SOURCES {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
        - BUS:B<x>:PARallel:SOURCES?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel to use as the Parallel source. x has a minimum of 1
          and a maximum of 4.
        - ``D<x>`` specifies a digital channel to use as the Parallel source. x has a minimum of 0
          and a maximum of 15.
        - ``MATH<x>`` specifies the math channel to use as the Parallel source. x has a minimum of 1
          and a maximum of 4.
    """  # noqa: E501


class BusBItemParallelIsclocked(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:ISCLOCKED`` command.

    Description:
        - This command sets or queries the Parallel bus behavior to either Clocked or not Clocked
          for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:ISCLOCKED?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:ISCLOCKED?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PARallel:ISCLOCKED value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:ISCLOCKED {YES|NO}
        - BUS:B<x>:PARallel:ISCLOCKED?
        ```

    Info:
        - ``YES`` specifies the Parallel mode of the specified bus to be clocked.
        - ``NO`` specifies the Parallel mode of the specified bus to be unclocked (asynchronous).
    """


class BusBItemParallelClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:CLOCk:SOUrce`` command.

    Description:
        - This command sets or queries the Parallel clock source for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk:SOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:CLOCk:SOUrce {CH<x>|D0|D1|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
        - BUS:B<x>:PARallel:CLOCk:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel to use as the Parallel clock source. x has a minimum
          of 1 and a maximum of 4.
        - ``D<x>`` specifies a digital channel to use as the Parallel clock source. x has a minimum
          of 0 and a maximum of 15.
        - ``MATH<x>`` specifies the math channel to use as the Parallel clock source. x has a
          minimum of 1 and a maximum of 4.
    """  # noqa: E501


class BusBItemParallelClockEdge(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:CLOCk:EDGE`` command.

    Description:
        - This command sets or queries which edge of a clocked parallel busses' signal establishes
          when new bus values are sampled.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCk:EDGE?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk:EDGE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk:EDGE value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:CLOCk:EDGE {FALL|RISe|EITHer}
        - BUS:B<x>:PARallel:CLOCk:EDGE?
        ```

    Info:
        - ``FALL`` decodes on the falling edge of the clocked parallel bus signal.
        - ``RISe`` decodes on the rising edge of the clocked parallel bus signal.
        - ``EITHer`` decodes on the rising or falling edge of the clocked parallel bus signal.
    """


class BusBItemParallelClock(SCPICmdRead):
    """The ``BUS:B<x>:PARallel:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.edge``: The ``BUS:B<x>:PARallel:CLOCk:EDGE`` command.
        - ``.source``: The ``BUS:B<x>:PARallel:CLOCk:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._edge = BusBItemParallelClockEdge(device, f"{self._cmd_syntax}:EDGE")
        self._source = BusBItemParallelClockSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def edge(self) -> BusBItemParallelClockEdge:
        """Return the ``BUS:B<x>:PARallel:CLOCk:EDGE`` command.

        Description:
            - This command sets or queries which edge of a clocked parallel busses' signal
              establishes when new bus values are sampled.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCk:EDGE?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk:EDGE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PARallel:CLOCk:EDGE value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:CLOCk:EDGE {FALL|RISe|EITHer}
            - BUS:B<x>:PARallel:CLOCk:EDGE?
            ```

        Info:
            - ``FALL`` decodes on the falling edge of the clocked parallel bus signal.
            - ``RISe`` decodes on the rising edge of the clocked parallel bus signal.
            - ``EITHer`` decodes on the rising or falling edge of the clocked parallel bus signal.
        """
        return self._edge

    @property
    def source(self) -> BusBItemParallelClockSource:
        """Return the ``BUS:B<x>:PARallel:CLOCk:SOUrce`` command.

        Description:
            - This command sets or queries the Parallel clock source for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCk:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PARallel:CLOCk:SOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:CLOCk:SOUrce {CH<x>|D0|D1|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
            - BUS:B<x>:PARallel:CLOCk:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel to use as the Parallel clock source. x has a
              minimum of 1 and a maximum of 4.
            - ``D<x>`` specifies a digital channel to use as the Parallel clock source. x has a
              minimum of 0 and a maximum of 15.
            - ``MATH<x>`` specifies the math channel to use as the Parallel clock source. x has a
              minimum of 1 and a maximum of 4.
        """  # noqa: E501
        return self._source


class BusBItemParallel(SCPICmdRead):
    """The ``BUS:B<x>:PARallel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.clock``: The ``BUS:B<x>:PARallel:CLOCk`` command tree.
        - ``.isclocked``: The ``BUS:B<x>:PARallel:ISCLOCKED`` command.
        - ``.sources``: The ``BUS:B<x>:PARallel:SOURCES`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._clock = BusBItemParallelClock(device, f"{self._cmd_syntax}:CLOCk")
        self._isclocked = BusBItemParallelIsclocked(device, f"{self._cmd_syntax}:ISCLOCKED")
        self._sources = BusBItemParallelSources(device, f"{self._cmd_syntax}:SOURCES")

    @property
    def clock(self) -> BusBItemParallelClock:
        """Return the ``BUS:B<x>:PARallel:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.edge``: The ``BUS:B<x>:PARallel:CLOCk:EDGE`` command.
            - ``.source``: The ``BUS:B<x>:PARallel:CLOCk:SOUrce`` command.
        """
        return self._clock

    @property
    def isclocked(self) -> BusBItemParallelIsclocked:
        """Return the ``BUS:B<x>:PARallel:ISCLOCKED`` command.

        Description:
            - This command sets or queries the Parallel bus behavior to either Clocked or not
              Clocked for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:ISCLOCKED?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:ISCLOCKED?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:PARallel:ISCLOCKED value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:ISCLOCKED {YES|NO}
            - BUS:B<x>:PARallel:ISCLOCKED?
            ```

        Info:
            - ``YES`` specifies the Parallel mode of the specified bus to be clocked.
            - ``NO`` specifies the Parallel mode of the specified bus to be unclocked
              (asynchronous).
        """
        return self._isclocked

    @property
    def sources(self) -> BusBItemParallelSources:
        """Return the ``BUS:B<x>:PARallel:SOURCES`` command.

        Description:
            - This command sets or queries the members of the Parallel mode of specified bus
              according to a supplied list of signals. The first item on the list becomes the MSB
              signal of the Bus. The second becomes the next-most-significant, and so on, with the
              last item becoming the LSB of the bus. If no signals are listed, the Bus is emptied of
              members. No signal can appear more than once in the list of bus members.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:SOURCES?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:SOURCES?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:PARallel:SOURCES value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:SOURCES {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
            - BUS:B<x>:PARallel:SOURCES?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel to use as the Parallel source. x has a minimum
              of 1 and a maximum of 4.
            - ``D<x>`` specifies a digital channel to use as the Parallel source. x has a minimum of
              0 and a maximum of 15.
            - ``MATH<x>`` specifies the math channel to use as the Parallel source. x has a minimum
              of 1 and a maximum of 4.
        """  # noqa: E501
        return self._sources


class BusBItemMipidsioneLaneItemType(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MIPIDSIOne:LANE<x>:TYPe`` command.

    Description:
        - This command sets or queries the lane source type for the specified MIPI DSI1 bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIPIDSIOne:LANE<x>:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIPIDSIOne:LANE<x>:TYPe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:MIPIDSIOne:LANE<x>:TYPe value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MIPIDSIOne:LANE<x>:TYPe {ANALog|DIGItal}
        - BUS:B<x>:MIPIDSIOne:LANE<x>:TYPe?
        ```

    Info:
        - ``ANALog`` sets the source type for the specified lane to support analog input.
        - ``DIGItal`` sets the source type for the specified lane to support digital input.
    """


class BusBItemMipidsioneLaneItemSourceDplus(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DPLUS`` command.

    Description:
        - This command sets or queries the D Plus source for the specified lane of the specified
          MIPI DSI1 bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DPLUS?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DPLUS?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DPLUS value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DPLUS {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
        - BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DPLUS?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel to use as the D Plus source for the specified lane.
          x has a minimum of 1 and a maximum of 4.
        - ``D<x>`` specifies a digital channel to use as the D Plus source for the specified lane. x
          has a minimum of 0 and a maximum of 15.
        - ``MATH<x>`` specifies a math channel to use as the D Plus source for the specified lane. x
          has a minimum of 1 and a maximum of 4.
    """  # noqa: E501


class BusBItemMipidsioneLaneItemSourceDminus(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DMINUS`` command.

    Description:
        - This command sets or queries the D Minus source for the specified lane of the specified
          MIPI DSI1 bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DMINUS?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DMINUS?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DMINUS value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DMINUS {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
        - BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DMINUS?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel to use as the D Minus source for the specified lane.
          x has a minimum of 1 and a maximum of 4.
        - ``D<x>`` specifies a digital channel to use as the D Minus source for the specified lane.
          x has a minimum of 0 and a maximum of 15.
        - ``MATH<x>`` specifies a math channel to use as the D Minus source for the specified lane.
          x has a minimum of 1 and a maximum of 4.
    """  # noqa: E501


class BusBItemMipidsioneLaneItemSourceDifferential(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DIFFerential`` command.

    Description:
        - This command sets or queries the differential source for the specified lane of the
          specified MIPI DSI1 bus.

    Usage:
        - Using the ``.query()`` method will send the
          ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DIFFerential?`` query.
        - Using the ``.verify(value)`` method will send the
          ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DIFFerential?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DIFFerential value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DIFFerential {D<x>}
        - BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DIFFerential?
        ```

    Info:
        - ``D<x>`` specifies a digital input signal to use as the differential source for the
          specified lane. x has a minimum of 0 and a maximum of 15.
    """


class BusBItemMipidsioneLaneItemSource(SCPICmdRead):
    """The ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.differential``: The ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DIFFerential`` command.
        - ``.dminus``: The ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DMINUS`` command.
        - ``.dplus``: The ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DPLUS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._differential = BusBItemMipidsioneLaneItemSourceDifferential(
            device, f"{self._cmd_syntax}:DIFFerential"
        )
        self._dminus = BusBItemMipidsioneLaneItemSourceDminus(device, f"{self._cmd_syntax}:DMINUS")
        self._dplus = BusBItemMipidsioneLaneItemSourceDplus(device, f"{self._cmd_syntax}:DPLUS")

    @property
    def differential(self) -> BusBItemMipidsioneLaneItemSourceDifferential:
        """Return the ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DIFFerential`` command.

        Description:
            - This command sets or queries the differential source for the specified lane of the
              specified MIPI DSI1 bus.

        Usage:
            - Using the ``.query()`` method will send the
              ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DIFFerential?`` query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DIFFerential?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DIFFerential value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DIFFerential {D<x>}
            - BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DIFFerential?
            ```

        Info:
            - ``D<x>`` specifies a digital input signal to use as the differential source for the
              specified lane. x has a minimum of 0 and a maximum of 15.
        """
        return self._differential

    @property
    def dminus(self) -> BusBItemMipidsioneLaneItemSourceDminus:
        """Return the ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DMINUS`` command.

        Description:
            - This command sets or queries the D Minus source for the specified lane of the
              specified MIPI DSI1 bus.

        Usage:
            - Using the ``.query()`` method will send the
              ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DMINUS?`` query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DMINUS?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DMINUS value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DMINUS {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
            - BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DMINUS?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel to use as the D Minus source for the specified
              lane. x has a minimum of 1 and a maximum of 4.
            - ``D<x>`` specifies a digital channel to use as the D Minus source for the specified
              lane. x has a minimum of 0 and a maximum of 15.
            - ``MATH<x>`` specifies a math channel to use as the D Minus source for the specified
              lane. x has a minimum of 1 and a maximum of 4.
        """  # noqa: E501
        return self._dminus

    @property
    def dplus(self) -> BusBItemMipidsioneLaneItemSourceDplus:
        """Return the ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DPLUS`` command.

        Description:
            - This command sets or queries the D Plus source for the specified lane of the specified
              MIPI DSI1 bus.

        Usage:
            - Using the ``.query()`` method will send the
              ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DPLUS?`` query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DPLUS?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DPLUS value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DPLUS {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
            - BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DPLUS?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel to use as the D Plus source for the specified
              lane. x has a minimum of 1 and a maximum of 4.
            - ``D<x>`` specifies a digital channel to use as the D Plus source for the specified
              lane. x has a minimum of 0 and a maximum of 15.
            - ``MATH<x>`` specifies a math channel to use as the D Plus source for the specified
              lane. x has a minimum of 1 and a maximum of 4.
        """  # noqa: E501
        return self._dplus


class BusBItemMipidsioneLaneItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``BUS:B<x>:MIPIDSIOne:LANE<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIPIDSIOne:LANE<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIPIDSIOne:LANE<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce`` command tree.
        - ``.type``: The ``BUS:B<x>:MIPIDSIOne:LANE<x>:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemMipidsioneLaneItemSource(device, f"{self._cmd_syntax}:SOUrce")
        self._type = BusBItemMipidsioneLaneItemType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def source(self) -> BusBItemMipidsioneLaneItemSource:
        """Return the ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.differential``: The ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DIFFerential`` command.
            - ``.dminus``: The ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DMINUS`` command.
            - ``.dplus``: The ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce:DPLUS`` command.
        """
        return self._source

    @property
    def type(self) -> BusBItemMipidsioneLaneItemType:
        """Return the ``BUS:B<x>:MIPIDSIOne:LANE<x>:TYPe`` command.

        Description:
            - This command sets or queries the lane source type for the specified MIPI DSI1 bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MIPIDSIOne:LANE<x>:TYPe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:MIPIDSIOne:LANE<x>:TYPe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MIPIDSIOne:LANE<x>:TYPe value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MIPIDSIOne:LANE<x>:TYPe {ANALog|DIGItal}
            - BUS:B<x>:MIPIDSIOne:LANE<x>:TYPe?
            ```

        Info:
            - ``ANALog`` sets the source type for the specified lane to support analog input.
            - ``DIGItal`` sets the source type for the specified lane to support digital input.
        """
        return self._type


class BusBItemMipidsioneClockType(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MIPIDSIOne:CLOCk:TYPe`` command.

    Description:
        - This command sets or queries the clock source type for the specified MIPI DSI1 bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIPIDSIOne:CLOCk:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIPIDSIOne:CLOCk:TYPe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:MIPIDSIOne:CLOCk:TYPe value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MIPIDSIOne:CLOCk:TYPe {ANALog|DIGItal}
        - BUS:B<x>:MIPIDSIOne:CLOCk:TYPe?
        ```

    Info:
        - ``ANALog`` sets the clock source type to support analog input.
        - ``DIGItal`` sets the clock source type to support digital input.
    """


class BusBItemMipidsioneClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MIPIDSIOne:CLOCk:SOUrce`` command.

    Description:
        - This command sets or queries the clock source for the specified MIPI DSI1 bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIPIDSIOne:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIPIDSIOne:CLOCk:SOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:MIPIDSIOne:CLOCk:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MIPIDSIOne:CLOCk:SOUrce {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
        - BUS:B<x>:MIPIDSIOne:CLOCk:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel to use as the clock source. x has a minimum of 1 and
          a maximum of 4.
        - ``MATH<x>`` specifies a math channel to use as the clock source. x has a minimum of 1 and
          a maximum of 4.
        - ``D<x>`` specifies a digital channel to use as the clock source. x has a minimum of 0 and
          a maximum of 15.
    """  # noqa: E501


class BusBItemMipidsioneClock(SCPICmdRead):
    """The ``BUS:B<x>:MIPIDSIOne:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIPIDSIOne:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIPIDSIOne:CLOCk?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``BUS:B<x>:MIPIDSIOne:CLOCk:SOUrce`` command.
        - ``.type``: The ``BUS:B<x>:MIPIDSIOne:CLOCk:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemMipidsioneClockSource(device, f"{self._cmd_syntax}:SOUrce")
        self._type = BusBItemMipidsioneClockType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def source(self) -> BusBItemMipidsioneClockSource:
        """Return the ``BUS:B<x>:MIPIDSIOne:CLOCk:SOUrce`` command.

        Description:
            - This command sets or queries the clock source for the specified MIPI DSI1 bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MIPIDSIOne:CLOCk:SOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:MIPIDSIOne:CLOCk:SOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MIPIDSIOne:CLOCk:SOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MIPIDSIOne:CLOCk:SOUrce {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
            - BUS:B<x>:MIPIDSIOne:CLOCk:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel to use as the clock source. x has a minimum of 1
              and a maximum of 4.
            - ``MATH<x>`` specifies a math channel to use as the clock source. x has a minimum of 1
              and a maximum of 4.
            - ``D<x>`` specifies a digital channel to use as the clock source. x has a minimum of 0
              and a maximum of 15.
        """  # noqa: E501
        return self._source

    @property
    def type(self) -> BusBItemMipidsioneClockType:
        """Return the ``BUS:B<x>:MIPIDSIOne:CLOCk:TYPe`` command.

        Description:
            - This command sets or queries the clock source type for the specified MIPI DSI1 bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MIPIDSIOne:CLOCk:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIPIDSIOne:CLOCk:TYPe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MIPIDSIOne:CLOCk:TYPe value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MIPIDSIOne:CLOCk:TYPe {ANALog|DIGItal}
            - BUS:B<x>:MIPIDSIOne:CLOCk:TYPe?
            ```

        Info:
            - ``ANALog`` sets the clock source type to support analog input.
            - ``DIGItal`` sets the clock source type to support digital input.
        """
        return self._type


class BusBItemMipidsione(SCPICmdRead):
    """The ``BUS:B<x>:MIPIDSIOne`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIPIDSIOne?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIPIDSIOne?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.clock``: The ``BUS:B<x>:MIPIDSIOne:CLOCk`` command tree.
        - ``.lane``: The ``BUS:B<x>:MIPIDSIOne:LANE<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._clock = BusBItemMipidsioneClock(device, f"{self._cmd_syntax}:CLOCk")
        self._lane: Dict[int, BusBItemMipidsioneLaneItem] = DefaultDictPassKeyToFactory(
            lambda x: BusBItemMipidsioneLaneItem(device, f"{self._cmd_syntax}:LANE{x}")
        )

    @property
    def clock(self) -> BusBItemMipidsioneClock:
        """Return the ``BUS:B<x>:MIPIDSIOne:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MIPIDSIOne:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIPIDSIOne:CLOCk?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:MIPIDSIOne:CLOCk:SOUrce`` command.
            - ``.type``: The ``BUS:B<x>:MIPIDSIOne:CLOCk:TYPe`` command.
        """
        return self._clock

    @property
    def lane(self) -> Dict[int, BusBItemMipidsioneLaneItem]:
        """Return the ``BUS:B<x>:MIPIDSIOne:LANE<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MIPIDSIOne:LANE<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIPIDSIOne:LANE<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:MIPIDSIOne:LANE<x>:SOUrce`` command tree.
            - ``.type``: The ``BUS:B<x>:MIPIDSIOne:LANE<x>:TYPe`` command.
        """
        return self._lane


class BusBItemMipicsitwoLaneItemType(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MIPICSITWo:LANE<x>:TYPe`` command.

    Description:
        - This command sets or queries the lane source type for the specified MIPI CSI2 bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIPICSITWo:LANE<x>:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIPICSITWo:LANE<x>:TYPe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:MIPICSITWo:LANE<x>:TYPe value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MIPICSITWo:LANE<x>:TYPe {ANALog|DIGItal}
        - BUS:B<x>:MIPICSITWo:LANE<x>:TYPe?
        ```

    Info:
        - ``ANALog`` sets the source type for the specified lane to support analog input.
        - ``DIGItal`` sets the source type for the specified lane to support digital input.
    """


class BusBItemMipicsitwoLaneItemSourceDplus(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DPLUS`` command.

    Description:
        - This command sets or queries the D Plus source for the specified lane of the specified
          MIPI CSI2 bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DPLUS?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DPLUS?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DPLUS value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DPLUS {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
        - BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DPLUS?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel to use as the D Plus source for the specified lane.
          x has a minimum of 1 and a maximum of 4.
        - ``D<x>`` specifies a digital channel to use as the D Plus source for the specified lane. x
          has a minimum of 0 and a maximum of 15.
        - ``MATH<x>`` specifies a math channel to use as the D Plus source for the specified lane. x
          has a minimum of 1 and a maximum of 4.
    """  # noqa: E501


class BusBItemMipicsitwoLaneItemSourceDminus(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DMINUS`` command.

    Description:
        - This command sets or queries the D Minus source for the specified lane of the specified
          MIPI CSI2 bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DMINUS?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DMINUS?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DMINUS value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DMINUS {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
        - BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DMINUS?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel to use as the D Minus source for the specified lane.
          x has a minimum of 1 and a maximum of 4.
        - ``D<x>`` specifies a digital channel to use as the D Minus source for the specified lane.
          x has a minimum of 0 and a maximum of 15.
        - ``MATH<x>`` specifies a math channel to use as the D Minus source for the specified lane.
          x has a minimum of 1 and a maximum of 4.
    """  # noqa: E501


class BusBItemMipicsitwoLaneItemSourceDifferential(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DIFFerential`` command.

    Description:
        - This command sets or queries the differential source for the specified lane of the
          specified MIPI CSI2 bus.

    Usage:
        - Using the ``.query()`` method will send the
          ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DIFFerential?`` query.
        - Using the ``.verify(value)`` method will send the
          ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DIFFerential?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DIFFerential value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DIFFerential {D<x>}
        - BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DIFFerential?
        ```

    Info:
        - ``D<x>`` specifies a digital input signal to use as the differential source. x has a
          minimum of 0 and a maximum of 15.
    """


class BusBItemMipicsitwoLaneItemSource(SCPICmdRead):
    """The ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.differential``: The ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DIFFerential`` command.
        - ``.dminus``: The ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DMINUS`` command.
        - ``.dplus``: The ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DPLUS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._differential = BusBItemMipicsitwoLaneItemSourceDifferential(
            device, f"{self._cmd_syntax}:DIFFerential"
        )
        self._dminus = BusBItemMipicsitwoLaneItemSourceDminus(device, f"{self._cmd_syntax}:DMINUS")
        self._dplus = BusBItemMipicsitwoLaneItemSourceDplus(device, f"{self._cmd_syntax}:DPLUS")

    @property
    def differential(self) -> BusBItemMipicsitwoLaneItemSourceDifferential:
        """Return the ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DIFFerential`` command.

        Description:
            - This command sets or queries the differential source for the specified lane of the
              specified MIPI CSI2 bus.

        Usage:
            - Using the ``.query()`` method will send the
              ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DIFFerential?`` query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DIFFerential?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DIFFerential value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DIFFerential {D<x>}
            - BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DIFFerential?
            ```

        Info:
            - ``D<x>`` specifies a digital input signal to use as the differential source. x has a
              minimum of 0 and a maximum of 15.
        """
        return self._differential

    @property
    def dminus(self) -> BusBItemMipicsitwoLaneItemSourceDminus:
        """Return the ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DMINUS`` command.

        Description:
            - This command sets or queries the D Minus source for the specified lane of the
              specified MIPI CSI2 bus.

        Usage:
            - Using the ``.query()`` method will send the
              ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DMINUS?`` query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DMINUS?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DMINUS value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DMINUS {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
            - BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DMINUS?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel to use as the D Minus source for the specified
              lane. x has a minimum of 1 and a maximum of 4.
            - ``D<x>`` specifies a digital channel to use as the D Minus source for the specified
              lane. x has a minimum of 0 and a maximum of 15.
            - ``MATH<x>`` specifies a math channel to use as the D Minus source for the specified
              lane. x has a minimum of 1 and a maximum of 4.
        """  # noqa: E501
        return self._dminus

    @property
    def dplus(self) -> BusBItemMipicsitwoLaneItemSourceDplus:
        """Return the ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DPLUS`` command.

        Description:
            - This command sets or queries the D Plus source for the specified lane of the specified
              MIPI CSI2 bus.

        Usage:
            - Using the ``.query()`` method will send the
              ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DPLUS?`` query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DPLUS?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DPLUS value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DPLUS {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
            - BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DPLUS?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel to use as the D Plus source for the specified
              lane. x has a minimum of 1 and a maximum of 4.
            - ``D<x>`` specifies a digital channel to use as the D Plus source for the specified
              lane. x has a minimum of 0 and a maximum of 15.
            - ``MATH<x>`` specifies a math channel to use as the D Plus source for the specified
              lane. x has a minimum of 1 and a maximum of 4.
        """  # noqa: E501
        return self._dplus


class BusBItemMipicsitwoLaneItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``BUS:B<x>:MIPICSITWo:LANE<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIPICSITWo:LANE<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIPICSITWo:LANE<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce`` command tree.
        - ``.type``: The ``BUS:B<x>:MIPICSITWo:LANE<x>:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemMipicsitwoLaneItemSource(device, f"{self._cmd_syntax}:SOUrce")
        self._type = BusBItemMipicsitwoLaneItemType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def source(self) -> BusBItemMipicsitwoLaneItemSource:
        """Return the ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.differential``: The ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DIFFerential`` command.
            - ``.dminus``: The ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DMINUS`` command.
            - ``.dplus``: The ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce:DPLUS`` command.
        """
        return self._source

    @property
    def type(self) -> BusBItemMipicsitwoLaneItemType:
        """Return the ``BUS:B<x>:MIPICSITWo:LANE<x>:TYPe`` command.

        Description:
            - This command sets or queries the lane source type for the specified MIPI CSI2 bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MIPICSITWo:LANE<x>:TYPe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:MIPICSITWo:LANE<x>:TYPe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MIPICSITWo:LANE<x>:TYPe value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MIPICSITWo:LANE<x>:TYPe {ANALog|DIGItal}
            - BUS:B<x>:MIPICSITWo:LANE<x>:TYPe?
            ```

        Info:
            - ``ANALog`` sets the source type for the specified lane to support analog input.
            - ``DIGItal`` sets the source type for the specified lane to support digital input.
        """
        return self._type


class BusBItemMipicsitwoClockType(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MIPICSITWo:CLOCk:TYPe`` command.

    Description:
        - This command sets or queries the MIPI CSI2 clock source type for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIPICSITWo:CLOCk:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIPICSITWo:CLOCk:TYPe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:MIPICSITWo:CLOCk:TYPe value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MIPICSITWo:CLOCk:TYPe {ANALog|DIGItal}
        - BUS:B<x>:MIPICSITWo:CLOCk:TYPe?
        ```

    Info:
        - ``ANALog`` sets the clock source type to support analog input for the specified bus.
        - ``DIGItal`` sets the clock source type to support digital input for the specified bus.
    """


class BusBItemMipicsitwoClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MIPICSITWo:CLOCk:SOUrce`` command.

    Description:
        - This command sets or queries the MIPI CSI2 clock source for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIPICSITWo:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIPICSITWo:CLOCk:SOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:MIPICSITWo:CLOCk:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MIPICSITWo:CLOCk:SOUrce {CH<x>|D<x>|MATH<x>}
        - BUS:B<x>:MIPICSITWo:CLOCk:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel to use as the MIPI CSI2 clock source. x has a
          minimum of 1 and a maximum of 4.
        - ``D<x>`` specifies a digital channel to use as the MIPI CSI2 clock source. x has a minimum
          of 0 and a maximum of 15.
        - ``MATH<x>`` specifies a math channel to use as the MIPI CSI2 clock source. x has a minimum
          of 1 and a maximum of 4.
    """


class BusBItemMipicsitwoClock(SCPICmdRead):
    """The ``BUS:B<x>:MIPICSITWo:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIPICSITWo:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIPICSITWo:CLOCk?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``BUS:B<x>:MIPICSITWo:CLOCk:SOUrce`` command.
        - ``.type``: The ``BUS:B<x>:MIPICSITWo:CLOCk:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemMipicsitwoClockSource(device, f"{self._cmd_syntax}:SOUrce")
        self._type = BusBItemMipicsitwoClockType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def source(self) -> BusBItemMipicsitwoClockSource:
        """Return the ``BUS:B<x>:MIPICSITWo:CLOCk:SOUrce`` command.

        Description:
            - This command sets or queries the MIPI CSI2 clock source for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MIPICSITWo:CLOCk:SOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:MIPICSITWo:CLOCk:SOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MIPICSITWo:CLOCk:SOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MIPICSITWo:CLOCk:SOUrce {CH<x>|D<x>|MATH<x>}
            - BUS:B<x>:MIPICSITWo:CLOCk:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel to use as the MIPI CSI2 clock source. x has a
              minimum of 1 and a maximum of 4.
            - ``D<x>`` specifies a digital channel to use as the MIPI CSI2 clock source. x has a
              minimum of 0 and a maximum of 15.
            - ``MATH<x>`` specifies a math channel to use as the MIPI CSI2 clock source. x has a
              minimum of 1 and a maximum of 4.
        """
        return self._source

    @property
    def type(self) -> BusBItemMipicsitwoClockType:
        """Return the ``BUS:B<x>:MIPICSITWo:CLOCk:TYPe`` command.

        Description:
            - This command sets or queries the MIPI CSI2 clock source type for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MIPICSITWo:CLOCk:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIPICSITWo:CLOCk:TYPe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MIPICSITWo:CLOCk:TYPe value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MIPICSITWo:CLOCk:TYPe {ANALog|DIGItal}
            - BUS:B<x>:MIPICSITWo:CLOCk:TYPe?
            ```

        Info:
            - ``ANALog`` sets the clock source type to support analog input for the specified bus.
            - ``DIGItal`` sets the clock source type to support digital input for the specified bus.
        """
        return self._type


class BusBItemMipicsitwo(SCPICmdRead):
    """The ``BUS:B<x>:MIPICSITWo`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIPICSITWo?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIPICSITWo?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.clock``: The ``BUS:B<x>:MIPICSITWo:CLOCk`` command tree.
        - ``.lane``: The ``BUS:B<x>:MIPICSITWo:LANE<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._clock = BusBItemMipicsitwoClock(device, f"{self._cmd_syntax}:CLOCk")
        self._lane: Dict[int, BusBItemMipicsitwoLaneItem] = DefaultDictPassKeyToFactory(
            lambda x: BusBItemMipicsitwoLaneItem(device, f"{self._cmd_syntax}:LANE{x}")
        )

    @property
    def clock(self) -> BusBItemMipicsitwoClock:
        """Return the ``BUS:B<x>:MIPICSITWo:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MIPICSITWo:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIPICSITWo:CLOCk?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:MIPICSITWo:CLOCk:SOUrce`` command.
            - ``.type``: The ``BUS:B<x>:MIPICSITWo:CLOCk:TYPe`` command.
        """
        return self._clock

    @property
    def lane(self) -> Dict[int, BusBItemMipicsitwoLaneItem]:
        """Return the ``BUS:B<x>:MIPICSITWo:LANE<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MIPICSITWo:LANE<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIPICSITWo:LANE<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:MIPICSITWo:LANE<x>:SOUrce`` command tree.
            - ``.type``: The ``BUS:B<x>:MIPICSITWo:LANE<x>:TYPe`` command.
        """
        return self._lane


class BusBItemMil1553bSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MIL1553B:SOUrce`` command.

    Description:
        - This command sets or queries sets the MIL-STD-1553 bus source. The supported source
          waveforms are channels 1-4 and math waveforms 1-4. The default is channel 1. B<x>
          specifies the bus number, which can range from 1 to 16.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIL1553B:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIL1553B:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:MIL1553B:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MIL1553B:SOUrce {CH<x>|MATH<x>}
        - BUS:B<x>:MIL1553B:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies to use one of the analog channels as the MIL-STD-1553 bus source for
          differential input. x has a minimum of 1 and a maximum of 4.
        - ``MATH<x>`` specifies to use the math waveform as the MIL-STD-1553 bus source for
          differential input x has a minimum of 1 and a maximum of 4.
    """


class BusBItemMil1553bResponsetimeMinimum(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MIL1553B:RESPonsetime:MINimum`` command.

    Description:
        - This command sets or queries the minimum response time to a valid command issued for the
          specified MIL-STD-1553 bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIL1553B:RESPonsetime:MINimum?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``BUS:B<x>:MIL1553B:RESPonsetime:MINimum?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:MIL1553B:RESPonsetime:MINimum value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MIL1553B:RESPonsetime:MINimum <NR3>
        - BUS:B<x>:MIL1553B:RESPonsetime:MINimum?
        ```

    Info:
        - ``B<x>`` is the Bus number.
        - ``<NR3>`` is a floating point number that specifies the minimum response time, in seconds.
    """


class BusBItemMil1553bResponsetimeMaximum(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MIL1553B:RESPonsetime:MAXimum`` command.

    Description:
        - This command sets or queries the maximum response time to a valid command issued for the
          specified MIL-STD-1553 bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIL1553B:RESPonsetime:MAXimum?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``BUS:B<x>:MIL1553B:RESPonsetime:MAXimum?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:MIL1553B:RESPonsetime:MAXimum value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MIL1553B:RESPonsetime:MAXimum <NR3>
        - BUS:B<x>:MIL1553B:RESPonsetime:MAXimum?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is a floating point number that specifies the maximum response time, in seconds.
    """


class BusBItemMil1553bResponsetime(SCPICmdRead):
    """The ``BUS:B<x>:MIL1553B:RESPonsetime`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIL1553B:RESPonsetime?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIL1553B:RESPonsetime?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.maximum``: The ``BUS:B<x>:MIL1553B:RESPonsetime:MAXimum`` command.
        - ``.minimum``: The ``BUS:B<x>:MIL1553B:RESPonsetime:MINimum`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._maximum = BusBItemMil1553bResponsetimeMaximum(device, f"{self._cmd_syntax}:MAXimum")
        self._minimum = BusBItemMil1553bResponsetimeMinimum(device, f"{self._cmd_syntax}:MINimum")

    @property
    def maximum(self) -> BusBItemMil1553bResponsetimeMaximum:
        """Return the ``BUS:B<x>:MIL1553B:RESPonsetime:MAXimum`` command.

        Description:
            - This command sets or queries the maximum response time to a valid command issued for
              the specified MIL-STD-1553 bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``BUS:B<x>:MIL1553B:RESPonsetime:MAXimum?`` query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:MIL1553B:RESPonsetime:MAXimum?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MIL1553B:RESPonsetime:MAXimum value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MIL1553B:RESPonsetime:MAXimum <NR3>
            - BUS:B<x>:MIL1553B:RESPonsetime:MAXimum?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is a floating point number that specifies the maximum response time, in
              seconds.
        """
        return self._maximum

    @property
    def minimum(self) -> BusBItemMil1553bResponsetimeMinimum:
        """Return the ``BUS:B<x>:MIL1553B:RESPonsetime:MINimum`` command.

        Description:
            - This command sets or queries the minimum response time to a valid command issued for
              the specified MIL-STD-1553 bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``BUS:B<x>:MIL1553B:RESPonsetime:MINimum?`` query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:MIL1553B:RESPonsetime:MINimum?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MIL1553B:RESPonsetime:MINimum value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MIL1553B:RESPonsetime:MINimum <NR3>
            - BUS:B<x>:MIL1553B:RESPonsetime:MINimum?
            ```

        Info:
            - ``B<x>`` is the Bus number.
            - ``<NR3>`` is a floating point number that specifies the minimum response time, in
              seconds.
        """
        return self._minimum


class BusBItemMil1553bPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MIL1553B:POLarity`` command.

    Description:
        - This command sets the MIL-STD-1553 bus polarity to normal or inverted. B<x> specifies the
          bus number, which can range from 1 to 16.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIL1553B:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIL1553B:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:MIL1553B:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MIL1553B:POLarity {NORMal|INVerted}
        - BUS:B<x>:MIL1553B:POLarity?
        ```

    Info:
        - ``NORMal`` - A high-low transition sets the MIL-STD-1553 bus polarity to positive.
        - ``INVerted`` - A high-low transition sets the MIL-STD-1553 bus polarity to negative.
    """


class BusBItemMil1553b(SCPICmdRead):
    """The ``BUS:B<x>:MIL1553B`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIL1553B?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIL1553B?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:MIL1553B:POLarity`` command.
        - ``.responsetime``: The ``BUS:B<x>:MIL1553B:RESPonsetime`` command tree.
        - ``.source``: The ``BUS:B<x>:MIL1553B:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemMil1553bPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._responsetime = BusBItemMil1553bResponsetime(
            device, f"{self._cmd_syntax}:RESPonsetime"
        )
        self._source = BusBItemMil1553bSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def polarity(self) -> BusBItemMil1553bPolarity:
        """Return the ``BUS:B<x>:MIL1553B:POLarity`` command.

        Description:
            - This command sets the MIL-STD-1553 bus polarity to normal or inverted. B<x> specifies
              the bus number, which can range from 1 to 16.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MIL1553B:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIL1553B:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:MIL1553B:POLarity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MIL1553B:POLarity {NORMal|INVerted}
            - BUS:B<x>:MIL1553B:POLarity?
            ```

        Info:
            - ``NORMal`` - A high-low transition sets the MIL-STD-1553 bus polarity to positive.
            - ``INVerted`` - A high-low transition sets the MIL-STD-1553 bus polarity to negative.
        """
        return self._polarity

    @property
    def responsetime(self) -> BusBItemMil1553bResponsetime:
        """Return the ``BUS:B<x>:MIL1553B:RESPonsetime`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MIL1553B:RESPonsetime?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIL1553B:RESPonsetime?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.maximum``: The ``BUS:B<x>:MIL1553B:RESPonsetime:MAXimum`` command.
            - ``.minimum``: The ``BUS:B<x>:MIL1553B:RESPonsetime:MINimum`` command.
        """
        return self._responsetime

    @property
    def source(self) -> BusBItemMil1553bSource:
        """Return the ``BUS:B<x>:MIL1553B:SOUrce`` command.

        Description:
            - This command sets or queries sets the MIL-STD-1553 bus source. The supported source
              waveforms are channels 1-4 and math waveforms 1-4. The default is channel 1. B<x>
              specifies the bus number, which can range from 1 to 16.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MIL1553B:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIL1553B:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:MIL1553B:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MIL1553B:SOUrce {CH<x>|MATH<x>}
            - BUS:B<x>:MIL1553B:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies to use one of the analog channels as the MIL-STD-1553 bus source
              for differential input. x has a minimum of 1 and a maximum of 4.
            - ``MATH<x>`` specifies to use the math waveform as the MIL-STD-1553 bus source for
              differential input x has a minimum of 1 and a maximum of 4.
        """
        return self._source


class BusBItemLinStandard(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LIN:STANDard`` command.

    Description:
        - This command sets or queries the LIN bus standard for the specified bus. The bus number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:STANDard?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:STANDard?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:STANDard value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:STANDard {MIXed|V1X|V2X}
        - BUS:B<x>:LIN:STANDard?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``MIXed`` specifies both versions 1.x and 2.x of the LIN standard.
        - ``V1X`` specifies version 1.x of the LIN standard.
        - ``V2X`` specifies version 2.x of the LIN standard.
    """


class BusBItemLinSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LIN:SOUrce`` command.

    Description:
        - This command sets or queries sets the LIN bus source. The bus is specified by x. The value
          of x can range from 1 to 16.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:SOUrce?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:SOUrce {CH<x>|D0|D1|D10|D11|D12|D13|D14|D15|D2|D3|D4|D5|D6|D7|D8|D9|MATH<x>}
        - BUS:B<x>:LIN:SOUrce?
        ```
    """


class BusBItemLinPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LIN:POLarity`` command.

    Description:
        - This command sets or queries the LIN bus polarity. The bus is specified by x. The value of
          x can range from 1 to 16.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:POLarity?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:POLarity value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:POLarity {INVerted|NORMal}
        - BUS:B<x>:LIN:POLarity?
        ```
    """


class BusBItemLinIdformat(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LIN:IDFORmat`` command.

    Description:
        - This command sets or queries LIN bus identifier format for the specified bus. The bus
          number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:IDFORmat?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:IDFORmat?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:IDFORmat value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:IDFORmat {NOPARity|PARity}
        - BUS:B<x>:LIN:IDFORmat?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``NOPARity`` specifies an id format that includes parity.
        - ``PARity`` specifies an id format that separates parity.
    """


class BusBItemLinBitrateValue(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LIN:BITRate:VALue`` command.

    Description:
        - This command sets or queries the LIN bus custom bitrate value. The bus is specified by x.
          The value of x can range from 1 to 16.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:BITRate:VALue?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:BITRate:VALue?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:BITRate:VALue value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:BITRate:VALue <nr3>
        - BUS:B<x>:LIN:BITRate:VALue?
        ```
    """


class BusBItemLinBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LIN:BITRate`` command.

    Description:
        - This command sets or queries the LIN bus bit rate. The bus number is specified by x. If
          you select Custom, use ``BUS:BX:LIN:BITRATE:CUSTOM`` to set the bit rate.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:BITRate value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:BITRate {RATE10K|RATE1K|RATE19K|RATE2K|RATE4K|RATE9K|CUSTom}
        - BUS:B<x>:LIN:BITRate?
        ```

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.value``: The ``BUS:B<x>:LIN:BITRate:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = BusBItemLinBitrateValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> BusBItemLinBitrateValue:
        """Return the ``BUS:B<x>:LIN:BITRate:VALue`` command.

        Description:
            - This command sets or queries the LIN bus custom bitrate value. The bus is specified by
              x. The value of x can range from 1 to 16.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:BITRate:VALue?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:BITRate:VALue?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:BITRate:VALue value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:BITRate:VALue <nr3>
            - BUS:B<x>:LIN:BITRate:VALue?
            ```
        """
        return self._value


class BusBItemLin(SCPICmdRead):
    """The ``BUS:B<x>:LIN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:LIN:BITRate`` command.
        - ``.idformat``: The ``BUS:B<x>:LIN:IDFORmat`` command.
        - ``.polarity``: The ``BUS:B<x>:LIN:POLarity`` command.
        - ``.source``: The ``BUS:B<x>:LIN:SOUrce`` command.
        - ``.standard``: The ``BUS:B<x>:LIN:STANDard`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemLinBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._idformat = BusBItemLinIdformat(device, f"{self._cmd_syntax}:IDFORmat")
        self._polarity = BusBItemLinPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemLinSource(device, f"{self._cmd_syntax}:SOUrce")
        self._standard = BusBItemLinStandard(device, f"{self._cmd_syntax}:STANDard")

    @property
    def bitrate(self) -> BusBItemLinBitrate:
        """Return the ``BUS:B<x>:LIN:BITRate`` command.

        Description:
            - This command sets or queries the LIN bus bit rate. The bus number is specified by x.
              If you select Custom, use ``BUS:BX:LIN:BITRATE:CUSTOM`` to set the bit rate.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:BITRate?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:BITRate {RATE10K|RATE1K|RATE19K|RATE2K|RATE4K|RATE9K|CUSTom}
            - BUS:B<x>:LIN:BITRate?
            ```

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.value``: The ``BUS:B<x>:LIN:BITRate:VALue`` command.
        """
        return self._bitrate

    @property
    def idformat(self) -> BusBItemLinIdformat:
        """Return the ``BUS:B<x>:LIN:IDFORmat`` command.

        Description:
            - This command sets or queries LIN bus identifier format for the specified bus. The bus
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:IDFORmat?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:IDFORmat?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:IDFORmat value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:IDFORmat {NOPARity|PARity}
            - BUS:B<x>:LIN:IDFORmat?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``NOPARity`` specifies an id format that includes parity.
            - ``PARity`` specifies an id format that separates parity.
        """
        return self._idformat

    @property
    def polarity(self) -> BusBItemLinPolarity:
        """Return the ``BUS:B<x>:LIN:POLarity`` command.

        Description:
            - This command sets or queries the LIN bus polarity. The bus is specified by x. The
              value of x can range from 1 to 16.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:POLarity?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:POLarity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:POLarity {INVerted|NORMal}
            - BUS:B<x>:LIN:POLarity?
            ```
        """
        return self._polarity

    @property
    def source(self) -> BusBItemLinSource:
        """Return the ``BUS:B<x>:LIN:SOUrce`` command.

        Description:
            - This command sets or queries sets the LIN bus source. The bus is specified by x. The
              value of x can range from 1 to 16.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:SOUrce {CH<x>|D0|D1|D10|D11|D12|D13|D14|D15|D2|D3|D4|D5|D6|D7|D8|D9|MATH<x>}
            - BUS:B<x>:LIN:SOUrce?
            ```
        """  # noqa: E501
        return self._source

    @property
    def standard(self) -> BusBItemLinStandard:
        """Return the ``BUS:B<x>:LIN:STANDard`` command.

        Description:
            - This command sets or queries the LIN bus standard for the specified bus. The bus
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:STANDard?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:STANDard?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:STANDard value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:STANDard {MIXed|V1X|V2X}
            - BUS:B<x>:LIN:STANDard?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``MIXed`` specifies both versions 1.x and 2.x of the LIN standard.
            - ``V1X`` specifies version 1.x of the LIN standard.
            - ``V2X`` specifies version 2.x of the LIN standard.
        """
        return self._standard


class BusBItemLabel(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LABel`` command.

    Description:
        - This command sets or queries the waveform label for the specified bus. The bus name string
          accepts only eight characters and truncates when more than eight characters.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LABel <string>
        - BUS:B<x>:LABel?
        ```

    Info:
        - ``<string>`` is an alphanumeric string of text enclosed in quotes. The text string is
          limited to 30 characters. It contains the text label information for bus.
    """


class BusBItemI2cRwinaddr(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I2C:RWINADDR`` command.

    Description:
        - This command sets or queries the manner in which seven-bit I2C slave addresses are
          represented in the 'busform' display of the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:RWINADDR?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:RWINADDR?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:RWINADDR value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I2C:RWINADDR {No|Yes}
        - BUS:B<x>:I2C:RWINADDR?
        ```

    Info:
        - ``No`` displays seven-bit slave addresses as integers in the range of 0 to 127, with the
          state of the R/W* bit from the LSB of the slave address byte. For example, the slave
          address byte of 0b10100101 is displayed as the value 0x52 R.
        - ``Yes`` displays the entire slave address byte as a number, with the R/W* signal as its
          LSB (bit 0) and the slave address in bits 7..0. For example, the slave address byte of
          0b10100101 is displayed as the value 0xA5 R.
    """


class BusBItemI2cDataSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I2C:DATa:SOUrce`` command.

    Description:
        - This command sets or queries the I2C data (SDA) source for the specified I2C bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:DATa:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:DATa:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:DATa:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I2C:DATa:SOUrce {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
        - BUS:B<x>:I2C:DATa:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel to use as the I2C SDATA source. x has a minimum of 1
          and a maximum of 4.
        - ``D<x>`` specifies a digital channel to use as the I2C SDATA source. x has a minimum of 0
          and a maximum of 15.
        - ``MATH<x>`` specifies a math channel to use as the I2C SDATA source. x has a minimum of 1
          and a maximum of 4.
    """  # noqa: E501


class BusBItemI2cData(SCPICmdRead):
    """The ``BUS:B<x>:I2C:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:DATa?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``BUS:B<x>:I2C:DATa:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemI2cDataSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def source(self) -> BusBItemI2cDataSource:
        """Return the ``BUS:B<x>:I2C:DATa:SOUrce`` command.

        Description:
            - This command sets or queries the I2C data (SDA) source for the specified I2C bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:DATa:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:DATa:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:DATa:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I2C:DATa:SOUrce {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
            - BUS:B<x>:I2C:DATa:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel to use as the I2C SDATA source. x has a minimum
              of 1 and a maximum of 4.
            - ``D<x>`` specifies a digital channel to use as the I2C SDATA source. x has a minimum
              of 0 and a maximum of 15.
            - ``MATH<x>`` specifies a math channel to use as the I2C SDATA source. x has a minimum
              of 1 and a maximum of 4.
        """  # noqa: E501
        return self._source


class BusBItemI2cClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I2C:CLOCk:SOUrce`` command.

    Description:
        - This command sets or queries the I2C clock (SCLK) source for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:CLOCk:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:CLOCk:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I2C:CLOCk:SOUrce {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>|}
        - BUS:B<x>:I2C:CLOCk:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel to use as the I2C SCLK source. x has a minimum of 1
          and a maximum of 4.
        - ``D<x>`` specifies a digital channel to use as the I2C SCLK source. x has a minimum of 0
          and a maximum of 15.
        - ``MATH<x>`` specifies a math channel to use as the I2C SCLK source. x has a minimum of 1
          and a maximum of 4.
    """  # noqa: E501


class BusBItemI2cClock(SCPICmdRead):
    """The ``BUS:B<x>:I2C:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:CLOCk?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``BUS:B<x>:I2C:CLOCk:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemI2cClockSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def source(self) -> BusBItemI2cClockSource:
        """Return the ``BUS:B<x>:I2C:CLOCk:SOUrce`` command.

        Description:
            - This command sets or queries the I2C clock (SCLK) source for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:CLOCk:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:CLOCk:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:CLOCk:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I2C:CLOCk:SOUrce {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>|}
            - BUS:B<x>:I2C:CLOCk:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel to use as the I2C SCLK source. x has a minimum
              of 1 and a maximum of 4.
            - ``D<x>`` specifies a digital channel to use as the I2C SCLK source. x has a minimum of
              0 and a maximum of 15.
            - ``MATH<x>`` specifies a math channel to use as the I2C SCLK source. x has a minimum of
              1 and a maximum of 4.
        """  # noqa: E501
        return self._source


class BusBItemI2c(SCPICmdRead):
    """The ``BUS:B<x>:I2C`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.clock``: The ``BUS:B<x>:I2C:CLOCk`` command tree.
        - ``.data``: The ``BUS:B<x>:I2C:DATa`` command tree.
        - ``.rwinaddr``: The ``BUS:B<x>:I2C:RWINADDR`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._clock = BusBItemI2cClock(device, f"{self._cmd_syntax}:CLOCk")
        self._data = BusBItemI2cData(device, f"{self._cmd_syntax}:DATa")
        self._rwinaddr = BusBItemI2cRwinaddr(device, f"{self._cmd_syntax}:RWINADDR")

    @property
    def clock(self) -> BusBItemI2cClock:
        """Return the ``BUS:B<x>:I2C:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:CLOCk?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:I2C:CLOCk:SOUrce`` command.
        """
        return self._clock

    @property
    def data(self) -> BusBItemI2cData:
        """Return the ``BUS:B<x>:I2C:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:DATa?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:I2C:DATa:SOUrce`` command.
        """
        return self._data

    @property
    def rwinaddr(self) -> BusBItemI2cRwinaddr:
        """Return the ``BUS:B<x>:I2C:RWINADDR`` command.

        Description:
            - This command sets or queries the manner in which seven-bit I2C slave addresses are
              represented in the 'busform' display of the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:RWINADDR?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:RWINADDR?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:RWINADDR value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I2C:RWINADDR {No|Yes}
            - BUS:B<x>:I2C:RWINADDR?
            ```

        Info:
            - ``No`` displays seven-bit slave addresses as integers in the range of 0 to 127, with
              the state of the R/W* bit from the LSB of the slave address byte. For example, the
              slave address byte of 0b10100101 is displayed as the value 0x52 R.
            - ``Yes`` displays the entire slave address byte as a number, with the R/W* signal as
              its LSB (bit 0) and the slave address in bits 7..0. For example, the slave address
              byte of 0b10100101 is displayed as the value 0xA5 R.
        """
        return self._rwinaddr


class BusBItemFlexraySource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:FLEXRAY:SOUrce`` command.

    Description:
        - This command sets or queries the FLEXRAY bus signal source. The bus is specified by x. The
          value of x can range from 1 to 16.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXRAY:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXRAY:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXRAY:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:FLEXRAY:SOUrce {CH<x>|D0|D1|D10|D11|D12|D13|D14|D15|D2|D3|D4|D5|D6|D7|D8|D9|MATH<x>}
        - BUS:B<x>:FLEXRAY:SOUrce?
        ```
    """  # noqa: E501


class BusBItemFlexraySignal(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:FLEXRAY:SIGnal`` command.

    Description:
        - This command sets or queries the FLEXRAY probe. The bus is specified by x. The value of x
          can range from 1 to 16.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXRAY:SIGnal?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXRAY:SIGnal?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXRAY:SIGnal value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:FLEXRAY:SIGnal {BDIFFBP|BM|TXRX}
        - BUS:B<x>:FLEXRAY:SIGnal?
        ```
    """


class BusBItemFlexrayProbe(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:FLEXRAY:PROBe`` command.

    Description:
        - This command sets or queries the FLEXRAY probe. The bus is specified by x. The value of x
          can range from 1 to 16.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXRAY:PROBe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXRAY:PROBe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXRAY:PROBe value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:FLEXRAY:PROBe {BDIFFBP|BM|TXRX}
        - BUS:B<x>:FLEXRAY:PROBe?
        ```
    """


class BusBItemFlexrayChannel(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:FLEXRAY:CHANnel`` command.

    Description:
        - This command sets or queries the FLEXRAY bus input channel. The bus is specified by x. The
          value of x can range from 1 to 16.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXRAY:CHANnel?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXRAY:CHANnel?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXRAY:CHANnel value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:FLEXRAY:CHANnel {A|B}
        - BUS:B<x>:FLEXRAY:CHANnel?
        ```

    Info:
        - ``A`` specifies the A channel.
        - ``B`` specifies the B channel.
    """


class BusBItemFlexrayBitrateValue(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:FLEXRAY:BITRate:VALue`` command.

    Description:
        - This command sets or queries FLEXRAY custom bit rate. The bus is specified by x. The value
          of x can range from 1 to 16.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXRAY:BITRate:VALue?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXRAY:BITRate:VALue?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXRAY:BITRate:VALue value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:FLEXRAY:BITRate:VALue <nr3>
        - BUS:B<x>:FLEXRAY:BITRate:VALue?
        ```
    """


class BusBItemFlexrayBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:FLEXRAY:BITRate`` command.

    Description:
        - This command sets or queries the FLEXRAY bus bit rate. The bus is specified by x. The
          value of x can range from 1 to 16.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXRAY:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXRAY:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXRAY:BITRate value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:FLEXRAY:BITRate {RATE10M|RATE5M|RATE2M|CUSTom}
        - BUS:B<x>:FLEXRAY:BITRate?
        ```

    Properties:
        - ``.value``: The ``BUS:B<x>:FLEXRAY:BITRate:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = BusBItemFlexrayBitrateValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> BusBItemFlexrayBitrateValue:
        """Return the ``BUS:B<x>:FLEXRAY:BITRate:VALue`` command.

        Description:
            - This command sets or queries FLEXRAY custom bit rate. The bus is specified by x. The
              value of x can range from 1 to 16.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXRAY:BITRate:VALue?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXRAY:BITRate:VALue?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:FLEXRAY:BITRate:VALue value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:FLEXRAY:BITRate:VALue <nr3>
            - BUS:B<x>:FLEXRAY:BITRate:VALue?
            ```
        """
        return self._value


class BusBItemFlexray(SCPICmdRead):
    """The ``BUS:B<x>:FLEXRAY`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXRAY?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXRAY?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:FLEXRAY:BITRate`` command.
        - ``.channel``: The ``BUS:B<x>:FLEXRAY:CHANnel`` command.
        - ``.source``: The ``BUS:B<x>:FLEXRAY:SOUrce`` command.
        - ``.probe``: The ``BUS:B<x>:FLEXRAY:PROBe`` command.
        - ``.signal``: The ``BUS:B<x>:FLEXRAY:SIGnal`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemFlexrayBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._channel = BusBItemFlexrayChannel(device, f"{self._cmd_syntax}:CHANnel")
        self._source = BusBItemFlexraySource(device, f"{self._cmd_syntax}:SOUrce")
        self._probe = BusBItemFlexrayProbe(device, f"{self._cmd_syntax}:PROBe")
        self._signal = BusBItemFlexraySignal(device, f"{self._cmd_syntax}:SIGnal")

    @property
    def bitrate(self) -> BusBItemFlexrayBitrate:
        """Return the ``BUS:B<x>:FLEXRAY:BITRate`` command.

        Description:
            - This command sets or queries the FLEXRAY bus bit rate. The bus is specified by x. The
              value of x can range from 1 to 16.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXRAY:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXRAY:BITRate?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXRAY:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:FLEXRAY:BITRate {RATE10M|RATE5M|RATE2M|CUSTom}
            - BUS:B<x>:FLEXRAY:BITRate?
            ```

        Sub-properties:
            - ``.value``: The ``BUS:B<x>:FLEXRAY:BITRate:VALue`` command.
        """
        return self._bitrate

    @property
    def channel(self) -> BusBItemFlexrayChannel:
        """Return the ``BUS:B<x>:FLEXRAY:CHANnel`` command.

        Description:
            - This command sets or queries the FLEXRAY bus input channel. The bus is specified by x.
              The value of x can range from 1 to 16.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXRAY:CHANnel?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXRAY:CHANnel?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXRAY:CHANnel value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:FLEXRAY:CHANnel {A|B}
            - BUS:B<x>:FLEXRAY:CHANnel?
            ```

        Info:
            - ``A`` specifies the A channel.
            - ``B`` specifies the B channel.
        """
        return self._channel

    @property
    def source(self) -> BusBItemFlexraySource:
        """Return the ``BUS:B<x>:FLEXRAY:SOUrce`` command.

        Description:
            - This command sets or queries the FLEXRAY bus signal source. The bus is specified by x.
              The value of x can range from 1 to 16.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXRAY:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXRAY:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXRAY:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:FLEXRAY:SOUrce {CH<x>|D0|D1|D10|D11|D12|D13|D14|D15|D2|D3|D4|D5|D6|D7|D8|D9|MATH<x>}
            - BUS:B<x>:FLEXRAY:SOUrce?
            ```
        """  # noqa: E501
        return self._source

    @property
    def probe(self) -> BusBItemFlexrayProbe:
        """Return the ``BUS:B<x>:FLEXRAY:PROBe`` command.

        Description:
            - This command sets or queries the FLEXRAY probe. The bus is specified by x. The value
              of x can range from 1 to 16.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXRAY:PROBe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXRAY:PROBe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXRAY:PROBe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:FLEXRAY:PROBe {BDIFFBP|BM|TXRX}
            - BUS:B<x>:FLEXRAY:PROBe?
            ```
        """
        return self._probe

    @property
    def signal(self) -> BusBItemFlexraySignal:
        """Return the ``BUS:B<x>:FLEXRAY:SIGnal`` command.

        Description:
            - This command sets or queries the FLEXRAY probe. The bus is specified by x. The value
              of x can range from 1 to 16.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXRAY:SIGnal?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXRAY:SIGnal?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXRAY:SIGnal value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:FLEXRAY:SIGnal {BDIFFBP|BM|TXRX}
            - BUS:B<x>:FLEXRAY:SIGnal?
            ```
        """
        return self._signal


class BusBItemEthernetType(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ETHERnet:TYPe`` command.

    Description:
        - This command specifies the Ethernet standard type: 10Base-T or 100Base-T. The default is
          ENET 100 BASETX.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:TYPe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERnet:TYPe value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERnet:TYPe {ENET10BASET|ENET100BASETX}
        - BUS:B<x>:ETHERnet:TYPe?
        ```

    Info:
        - ``ENET10BASET`` specifies the Ethernet type as 10Base-T standard. This standard supports
          data transfer rates up to 10 Mbps (also called Twisted Pair Ethernet).
        - ``ENET100BASETX`` specifies the Ethernet type as 100Base-T standard. This standard
          supports data transfer rates up to 100 Mbps (also called Fast Ethernet).
    """


class BusBItemEthernetSourceDplus(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ETHERnet:SOUrce:DPLUs`` command.

    Description:
        - This command specifies the Ethernet data source for the D+ input for differential probing.
          The default is channel 1. B<x> specifies the bus number, which can range from 1 to 16.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DPLUs?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DPLUs?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DPLUs value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERnet:SOUrce:DPLUs {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
        - BUS:B<x>:ETHERnet:SOUrce:DPLUs?
        ```

    Info:
        - ``CH<x>`` specifies to use one of the analog channels 1 - 4 as the Ethernet data source
          for the D+ input. x has a minimum of 1 and a maximum of 4.
        - ``D<x>`` specifies to use one of the digital channels D0 - D15 as the Ethernet data source
          for the D+ input. x has a minimum of 0 and a maximum of 15.
        - ``MATH<x>`` specifies to use one of the math waveforms as the Ethernet data source for the
          D+ input. x has a minimum of 1 and a maximum of 4.
    """  # noqa: E501


class BusBItemEthernetSourceDminus(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ETHERnet:SOUrce:DMINus`` command.

    Description:
        - This command specifies the Ethernet data source for D- input for differential probing. The
          default is Channel 2. B<x> specifies the bus number, which can range from 1 to 16.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DMINus?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DMINus?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DMINus value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERnet:SOUrce:DMINus {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
        - BUS:B<x>:ETHERnet:SOUrce:DMINus?
        ```

    Info:
        - ``CH<x>`` specifies to use one of the analog channels as the Ethernet data source for the
          D- input. x has a minimum of 1 and a maximum of 4.
        - ``D<x>`` specifies to use one of the digital channels D0 - D15 as the Ethernet data source
          for the D- input. x has a minimum of 0 and a maximum of 15.
        - ``MATH<x>`` specifies to use one of the math waveforms as the Ethernet data source for the
          D- input. x has a minimum of 1 and a maximum of 4.
    """  # noqa: E501


class BusBItemEthernetSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ETHERnet:SOUrce`` command.

    Description:
        - This command specifies the Ethernet data source for differential input. The supported
          source waveforms are channels 1-4 and math waveforms 1-4. The default is channel 1. B<x>
          specifies the bus number, which can range from 1 to 16.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERnet:SOUrce {CH<x>|MATH<x>}
        - BUS:B<x>:ETHERnet:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies to use one of the channels 1-4 as the Ethernet data source for
          differential input. x has a minimum of 1 and a maximum of 4.
        - ``MATH<x>`` specifies to use a math waveform as the source for Ethernet data differential
          input x has a minimum of 1 and a maximum of 4.

    Properties:
        - ``.dminus``: The ``BUS:B<x>:ETHERnet:SOUrce:DMINus`` command.
        - ``.dplus``: The ``BUS:B<x>:ETHERnet:SOUrce:DPLUs`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._dminus = BusBItemEthernetSourceDminus(device, f"{self._cmd_syntax}:DMINus")
        self._dplus = BusBItemEthernetSourceDplus(device, f"{self._cmd_syntax}:DPLUs")

    @property
    def dminus(self) -> BusBItemEthernetSourceDminus:
        """Return the ``BUS:B<x>:ETHERnet:SOUrce:DMINus`` command.

        Description:
            - This command specifies the Ethernet data source for D- input for differential probing.
              The default is Channel 2. B<x> specifies the bus number, which can range from 1 to 16.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DMINus?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DMINus?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ETHERnet:SOUrce:DMINus value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERnet:SOUrce:DMINus {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
            - BUS:B<x>:ETHERnet:SOUrce:DMINus?
            ```

        Info:
            - ``CH<x>`` specifies to use one of the analog channels as the Ethernet data source for
              the D- input. x has a minimum of 1 and a maximum of 4.
            - ``D<x>`` specifies to use one of the digital channels D0 - D15 as the Ethernet data
              source for the D- input. x has a minimum of 0 and a maximum of 15.
            - ``MATH<x>`` specifies to use one of the math waveforms as the Ethernet data source for
              the D- input. x has a minimum of 1 and a maximum of 4.
        """  # noqa: E501
        return self._dminus

    @property
    def dplus(self) -> BusBItemEthernetSourceDplus:
        """Return the ``BUS:B<x>:ETHERnet:SOUrce:DPLUs`` command.

        Description:
            - This command specifies the Ethernet data source for the D+ input for differential
              probing. The default is channel 1. B<x> specifies the bus number, which can range from
              1 to 16.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DPLUs?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DPLUs?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ETHERnet:SOUrce:DPLUs value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERnet:SOUrce:DPLUs {CH<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|MATH<x>}
            - BUS:B<x>:ETHERnet:SOUrce:DPLUs?
            ```

        Info:
            - ``CH<x>`` specifies to use one of the analog channels 1 - 4 as the Ethernet data
              source for the D+ input. x has a minimum of 1 and a maximum of 4.
            - ``D<x>`` specifies to use one of the digital channels D0 - D15 as the Ethernet data
              source for the D+ input. x has a minimum of 0 and a maximum of 15.
            - ``MATH<x>`` specifies to use one of the math waveforms as the Ethernet data source for
              the D+ input. x has a minimum of 1 and a maximum of 4.
        """  # noqa: E501
        return self._dplus


class BusBItemEthernetProbe(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ETHERnet:PRObe`` command.

    Description:
        - This command specifies the Ethernet probe type: differential or single-ended. The default
          is DIFFerential. B<x> is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:PRObe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:PRObe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERnet:PRObe value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERnet:PRObe {DIFFerential|SINGleended}
        - BUS:B<x>:ETHERnet:PRObe?
        ```

    Info:
        - ``DIFFerential``
        - ``SINGleended``
    """


class BusBItemEthernet(SCPICmdRead):
    """The ``BUS:B<x>:ETHERnet`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.probe``: The ``BUS:B<x>:ETHERnet:PRObe`` command.
        - ``.source``: The ``BUS:B<x>:ETHERnet:SOUrce`` command.
        - ``.type``: The ``BUS:B<x>:ETHERnet:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._probe = BusBItemEthernetProbe(device, f"{self._cmd_syntax}:PRObe")
        self._source = BusBItemEthernetSource(device, f"{self._cmd_syntax}:SOUrce")
        self._type = BusBItemEthernetType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def probe(self) -> BusBItemEthernetProbe:
        """Return the ``BUS:B<x>:ETHERnet:PRObe`` command.

        Description:
            - This command specifies the Ethernet probe type: differential or single-ended. The
              default is DIFFerential. B<x> is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:PRObe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:PRObe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERnet:PRObe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERnet:PRObe {DIFFerential|SINGleended}
            - BUS:B<x>:ETHERnet:PRObe?
            ```

        Info:
            - ``DIFFerential``
            - ``SINGleended``
        """
        return self._probe

    @property
    def source(self) -> BusBItemEthernetSource:
        """Return the ``BUS:B<x>:ETHERnet:SOUrce`` command.

        Description:
            - This command specifies the Ethernet data source for differential input. The supported
              source waveforms are channels 1-4 and math waveforms 1-4. The default is channel 1.
              B<x> specifies the bus number, which can range from 1 to 16.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERnet:SOUrce {CH<x>|MATH<x>}
            - BUS:B<x>:ETHERnet:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies to use one of the channels 1-4 as the Ethernet data source for
              differential input. x has a minimum of 1 and a maximum of 4.
            - ``MATH<x>`` specifies to use a math waveform as the source for Ethernet data
              differential input x has a minimum of 1 and a maximum of 4.

        Sub-properties:
            - ``.dminus``: The ``BUS:B<x>:ETHERnet:SOUrce:DMINus`` command.
            - ``.dplus``: The ``BUS:B<x>:ETHERnet:SOUrce:DPLUs`` command.
        """
        return self._source

    @property
    def type(self) -> BusBItemEthernetType:
        """Return the ``BUS:B<x>:ETHERnet:TYPe`` command.

        Description:
            - This command specifies the Ethernet standard type: 10Base-T or 100Base-T. The default
              is ENET 100 BASETX.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:TYPe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERnet:TYPe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERnet:TYPe {ENET10BASET|ENET100BASETX}
            - BUS:B<x>:ETHERnet:TYPe?
            ```

        Info:
            - ``ENET10BASET`` specifies the Ethernet type as 10Base-T standard. This standard
              supports data transfer rates up to 10 Mbps (also called Twisted Pair Ethernet).
            - ``ENET100BASETX`` specifies the Ethernet type as 100Base-T standard. This standard
              supports data transfer rates up to 100 Mbps (also called Fast Ethernet).
        """
        return self._type


class BusBItemDisplayType(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:DISplay:TYPe`` command.

    Description:
        - This command sets or queries the decoding display style for the specified bus. You can
          display in either logic waveform, busform, or both.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay:TYPe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:DISplay:TYPe value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:DISplay:TYPe {BUS|WAVEFORMS|BOTh}
        - BUS:B<x>:DISplay:TYPe?
        ```

    Info:
        - ``BUS`` , displays the decoding in busform only.
        - ``WAVEFORMS`` , displays the decoding in logic waveforms only.
        - ``BOTh`` , displays the decoding in both logic waveform and busform.
    """


class BusBItemDisplayDecodeState(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:DISplay:DECOde:STAte`` command.

    Description:
        - This command sets or queries whether the specified bus is enabled to display symbolic
          decode of its busform values.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay:DECOde:STAte?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay:DECOde:STAte?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:DISplay:DECOde:STAte value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:DISplay:DECOde:STAte {OFF|ON|RELoad}
        - BUS:B<x>:DISplay:DECOde:STAte?
        ```

    Info:
        - ``OFF`` = the specified bus does not display symbolic decode of its busform values.
        - ``ON`` = the specified bus displays symbolic decode of its busform values.
        - ``RELoad`` reparses to whatever symbolic decode file name it is currently assigned. For
          example, this can be useful if the contents of that file are changed after having assigned
          it to a Bus.
    """


class BusBItemDisplayDecodeFile(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:DISplay:DECOde:FILe`` command.

    Description:
        - This command sets or queries the name of a TSF-formatted text file used to construct a
          symbolic decode table from for the specified bus. The decode table associates symbolic
          names with the numeric values they represent. When a Bus is set to perform symbolic
          decode, numeric values in its 'busform' trace are replaced by the first matching symbol
          (if any) from the table. Each Bus can use its own specific lookup table. For example, an
          I2C-type Bus might use a table that associates the symbol 'ROM' with the number
          0b10100111, even though another the decode table for another bus associates the symbol
          'MAX' with that same number. The lookup table format is the same for all the bus types.
          The decode files for all the buses are available in the default location
          C:UsersPublicTektronixTekScopebusDecodeTables.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay:DECOde:FILe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay:DECOde:FILe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:DISplay:DECOde:FILe value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:DISplay:DECOde:FILe {decodeFileName}
        - BUS:B<x>:DISplay:DECOde:FILe?
        ```

    Info:
        - ``decodeFileName`` specifies the name of a TSF-formatted text file.
    """


class BusBItemDisplayDecode(SCPICmdRead):
    """The ``BUS:B<x>:DISplay:DECOde`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay:DECOde?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay:DECOde?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.file``: The ``BUS:B<x>:DISplay:DECOde:FILe`` command.
        - ``.state``: The ``BUS:B<x>:DISplay:DECOde:STAte`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._file = BusBItemDisplayDecodeFile(device, f"{self._cmd_syntax}:FILe")
        self._state = BusBItemDisplayDecodeState(device, f"{self._cmd_syntax}:STAte")

    @property
    def file(self) -> BusBItemDisplayDecodeFile:
        """Return the ``BUS:B<x>:DISplay:DECOde:FILe`` command.

        Description:
            - This command sets or queries the name of a TSF-formatted text file used to construct a
              symbolic decode table from for the specified bus. The decode table associates symbolic
              names with the numeric values they represent. When a Bus is set to perform symbolic
              decode, numeric values in its 'busform' trace are replaced by the first matching
              symbol (if any) from the table. Each Bus can use its own specific lookup table. For
              example, an I2C-type Bus might use a table that associates the symbol 'ROM' with the
              number 0b10100111, even though another the decode table for another bus associates the
              symbol 'MAX' with that same number. The lookup table format is the same for all the
              bus types. The decode files for all the buses are available in the default location
              C:UsersPublicTektronixTekScopebusDecodeTables.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay:DECOde:FILe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay:DECOde:FILe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:DISplay:DECOde:FILe value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:DISplay:DECOde:FILe {decodeFileName}
            - BUS:B<x>:DISplay:DECOde:FILe?
            ```

        Info:
            - ``decodeFileName`` specifies the name of a TSF-formatted text file.
        """
        return self._file

    @property
    def state(self) -> BusBItemDisplayDecodeState:
        """Return the ``BUS:B<x>:DISplay:DECOde:STAte`` command.

        Description:
            - This command sets or queries whether the specified bus is enabled to display symbolic
              decode of its busform values.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay:DECOde:STAte?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay:DECOde:STAte?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:DISplay:DECOde:STAte value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:DISplay:DECOde:STAte {OFF|ON|RELoad}
            - BUS:B<x>:DISplay:DECOde:STAte?
            ```

        Info:
            - ``OFF`` = the specified bus does not display symbolic decode of its busform values.
            - ``ON`` = the specified bus displays symbolic decode of its busform values.
            - ``RELoad`` reparses to whatever symbolic decode file name it is currently assigned.
              For example, this can be useful if the contents of that file are changed after having
              assigned it to a Bus.
        """
        return self._state


class BusBItemDisplay(SCPICmdRead):
    """The ``BUS:B<x>:DISplay`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.decode``: The ``BUS:B<x>:DISplay:DECOde`` command tree.
        - ``.type``: The ``BUS:B<x>:DISplay:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._decode = BusBItemDisplayDecode(device, f"{self._cmd_syntax}:DECOde")
        self._type = BusBItemDisplayType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def decode(self) -> BusBItemDisplayDecode:
        """Return the ``BUS:B<x>:DISplay:DECOde`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay:DECOde?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay:DECOde?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.file``: The ``BUS:B<x>:DISplay:DECOde:FILe`` command.
            - ``.state``: The ``BUS:B<x>:DISplay:DECOde:STAte`` command.
        """
        return self._decode

    @property
    def type(self) -> BusBItemDisplayType:
        """Return the ``BUS:B<x>:DISplay:TYPe`` command.

        Description:
            - This command sets or queries the decoding display style for the specified bus. You can
              display in either logic waveform, busform, or both.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay:TYPe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:DISplay:TYPe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:DISplay:TYPe {BUS|WAVEFORMS|BOTh}
            - BUS:B<x>:DISplay:TYPe?
            ```

        Info:
            - ``BUS`` , displays the decoding in busform only.
            - ``WAVEFORMS`` , displays the decoding in logic waveforms only.
            - ``BOTh`` , displays the decoding in both logic waveform and busform.
        """
        return self._type


class BusBItemCanSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:SOUrce`` command.

    Description:
        - This command sets or queries the CAN source channel. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:SOUrce?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:SOUrce {CH<x>|D0|D1|D10|D11|D12|D13|D14|D15|D2|D3|D4|D5|D6|D7|D8|D9|MATH<x>}
        - BUS:B<x>:CAN:SOUrce?
        ```
    """


class BusBItemCanProbe(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:PRObe`` command.

    Description:
        - This command sets or queries CAN probe type. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:PRObe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:PRObe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:PRObe value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:PRObe {DIFFerential|CANH|CANL|RX|TX}
        - BUS:B<x>:CAN:PRObe?
        ```
    """


class BusBItemCanBitrateValue(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:BITRate:VALue`` command.

    Description:
        - This command sets or queries CAN custom bitrate value. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:BITRate:VALue?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:BITRate:VALue?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:BITRate:VALue value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:BITRate:VALue <nr3>
        - BUS:B<x>:CAN:BITRate:VALue?
        ```

    Info:
        - ``<nr3>`` specifies the CAN custom bitrate value.
    """


class BusBItemCanBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:BITRate`` command.

    Description:
        - This command sets or queries the CAN bitrate. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:BITRate value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:BITRate {RATE10K|RATE100K|RATE1M|RATE125K|RATE153K|RATE20K|RATE25K|RATE250K|RATE31K|RATE33K|RATE37K|RATE400K|RATE50K|RATE500K|RATE62K|RATE68K|RATE800K|RATE83K|RATE92K|CUSTom}
        - BUS:B<x>:CAN:BITRate?
        ```

    Properties:
        - ``.value``: The ``BUS:B<x>:CAN:BITRate:VALue`` command.
    """  # noqa: E501

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = BusBItemCanBitrateValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> BusBItemCanBitrateValue:
        """Return the ``BUS:B<x>:CAN:BITRate:VALue`` command.

        Description:
            - This command sets or queries CAN custom bitrate value. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:BITRate:VALue?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:BITRate:VALue?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:BITRate:VALue value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:BITRate:VALue <nr3>
            - BUS:B<x>:CAN:BITRate:VALue?
            ```

        Info:
            - ``<nr3>`` specifies the CAN custom bitrate value.
        """
        return self._value


class BusBItemCan(SCPICmdRead):
    """The ``BUS:B<x>:CAN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:CAN:BITRate`` command.
        - ``.probe``: The ``BUS:B<x>:CAN:PRObe`` command.
        - ``.source``: The ``BUS:B<x>:CAN:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemCanBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._probe = BusBItemCanProbe(device, f"{self._cmd_syntax}:PRObe")
        self._source = BusBItemCanSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def bitrate(self) -> BusBItemCanBitrate:
        """Return the ``BUS:B<x>:CAN:BITRate`` command.

        Description:
            - This command sets or queries the CAN bitrate. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:BITRate?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:BITRate {RATE10K|RATE100K|RATE1M|RATE125K|RATE153K|RATE20K|RATE25K|RATE250K|RATE31K|RATE33K|RATE37K|RATE400K|RATE50K|RATE500K|RATE62K|RATE68K|RATE800K|RATE83K|RATE92K|CUSTom}
            - BUS:B<x>:CAN:BITRate?
            ```

        Sub-properties:
            - ``.value``: The ``BUS:B<x>:CAN:BITRate:VALue`` command.
        """  # noqa: E501
        return self._bitrate

    @property
    def probe(self) -> BusBItemCanProbe:
        """Return the ``BUS:B<x>:CAN:PRObe`` command.

        Description:
            - This command sets or queries CAN probe type. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:PRObe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:PRObe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:PRObe value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:PRObe {DIFFerential|CANH|CANL|RX|TX}
            - BUS:B<x>:CAN:PRObe?
            ```
        """
        return self._probe

    @property
    def source(self) -> BusBItemCanSource:
        """Return the ``BUS:B<x>:CAN:SOUrce`` command.

        Description:
            - This command sets or queries the CAN source channel. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:SOUrce {CH<x>|D0|D1|D10|D11|D12|D13|D14|D15|D2|D3|D4|D5|D6|D7|D8|D9|MATH<x>}
            - BUS:B<x>:CAN:SOUrce?
            ```
        """  # noqa: E501
        return self._source


#  pylint: disable=too-many-instance-attributes
class BusBItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``BUS:B<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.can``: The ``BUS:B<x>:CAN`` command tree.
        - ``.display``: The ``BUS:B<x>:DISplay`` command tree.
        - ``.ethernet``: The ``BUS:B<x>:ETHERnet`` command tree.
        - ``.flexray``: The ``BUS:B<x>:FLEXRAY`` command tree.
        - ``.i2c``: The ``BUS:B<x>:I2C`` command tree.
        - ``.label``: The ``BUS:B<x>:LABel`` command.
        - ``.lin``: The ``BUS:B<x>:LIN`` command tree.
        - ``.mil1553b``: The ``BUS:B<x>:MIL1553B`` command tree.
        - ``.mipicsitwo``: The ``BUS:B<x>:MIPICSITWo`` command tree.
        - ``.mipidsione``: The ``BUS:B<x>:MIPIDSIOne`` command tree.
        - ``.parallel``: The ``BUS:B<x>:PARallel`` command tree.
        - ``.pcie``: The ``BUS:B<x>:PCIE`` command tree.
        - ``.position``: The ``BUS:B<x>:POSition`` command.
        - ``.rs232c``: The ``BUS:B<x>:RS232C`` command tree.
        - ``.s64b66b``: The ``BUS:B<x>:S64B66B`` command tree.
        - ``.s8b10b``: The ``BUS:B<x>:S8B10B`` command tree.
        - ``.spi``: The ``BUS:B<x>:SPI`` command tree.
        - ``.type``: The ``BUS:B<x>:TYPe`` command.
        - ``.usb``: The ``BUS:B<x>:USB`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._can = BusBItemCan(device, f"{self._cmd_syntax}:CAN")
        self._display = BusBItemDisplay(device, f"{self._cmd_syntax}:DISplay")
        self._ethernet = BusBItemEthernet(device, f"{self._cmd_syntax}:ETHERnet")
        self._flexray = BusBItemFlexray(device, f"{self._cmd_syntax}:FLEXRAY")
        self._i2c = BusBItemI2c(device, f"{self._cmd_syntax}:I2C")
        self._label = BusBItemLabel(device, f"{self._cmd_syntax}:LABel")
        self._lin = BusBItemLin(device, f"{self._cmd_syntax}:LIN")
        self._mil1553b = BusBItemMil1553b(device, f"{self._cmd_syntax}:MIL1553B")
        self._mipicsitwo = BusBItemMipicsitwo(device, f"{self._cmd_syntax}:MIPICSITWo")
        self._mipidsione = BusBItemMipidsione(device, f"{self._cmd_syntax}:MIPIDSIOne")
        self._parallel = BusBItemParallel(device, f"{self._cmd_syntax}:PARallel")
        self._pcie = BusBItemPcie(device, f"{self._cmd_syntax}:PCIE")
        self._position = BusBItemPosition(device, f"{self._cmd_syntax}:POSition")
        self._rs232c = BusBItemRs232c(device, f"{self._cmd_syntax}:RS232C")
        self._s64b66b = BusBItemS64b66b(device, f"{self._cmd_syntax}:S64B66B")
        self._s8b10b = BusBItemS8b10b(device, f"{self._cmd_syntax}:S8B10B")
        self._spi = BusBItemSpi(device, f"{self._cmd_syntax}:SPI")
        self._type = BusBItemType(device, f"{self._cmd_syntax}:TYPe")
        self._usb = BusBItemUsb(device, f"{self._cmd_syntax}:USB")

    @property
    def can(self) -> BusBItemCan:
        """Return the ``BUS:B<x>:CAN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:CAN:BITRate`` command.
            - ``.probe``: The ``BUS:B<x>:CAN:PRObe`` command.
            - ``.source``: The ``BUS:B<x>:CAN:SOUrce`` command.
        """
        return self._can

    @property
    def display(self) -> BusBItemDisplay:
        """Return the ``BUS:B<x>:DISplay`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.decode``: The ``BUS:B<x>:DISplay:DECOde`` command tree.
            - ``.type``: The ``BUS:B<x>:DISplay:TYPe`` command.
        """
        return self._display

    @property
    def ethernet(self) -> BusBItemEthernet:
        """Return the ``BUS:B<x>:ETHERnet`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.probe``: The ``BUS:B<x>:ETHERnet:PRObe`` command.
            - ``.source``: The ``BUS:B<x>:ETHERnet:SOUrce`` command.
            - ``.type``: The ``BUS:B<x>:ETHERnet:TYPe`` command.
        """
        return self._ethernet

    @property
    def flexray(self) -> BusBItemFlexray:
        """Return the ``BUS:B<x>:FLEXRAY`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXRAY?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXRAY?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:FLEXRAY:BITRate`` command.
            - ``.channel``: The ``BUS:B<x>:FLEXRAY:CHANnel`` command.
            - ``.source``: The ``BUS:B<x>:FLEXRAY:SOUrce`` command.
            - ``.probe``: The ``BUS:B<x>:FLEXRAY:PROBe`` command.
            - ``.signal``: The ``BUS:B<x>:FLEXRAY:SIGnal`` command.
        """
        return self._flexray

    @property
    def i2c(self) -> BusBItemI2c:
        """Return the ``BUS:B<x>:I2C`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.clock``: The ``BUS:B<x>:I2C:CLOCk`` command tree.
            - ``.data``: The ``BUS:B<x>:I2C:DATa`` command tree.
            - ``.rwinaddr``: The ``BUS:B<x>:I2C:RWINADDR`` command.
        """
        return self._i2c

    @property
    def label(self) -> BusBItemLabel:
        """Return the ``BUS:B<x>:LABel`` command.

        Description:
            - This command sets or queries the waveform label for the specified bus. The bus name
              string accepts only eight characters and truncates when more than eight characters.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LABel <string>
            - BUS:B<x>:LABel?
            ```

        Info:
            - ``<string>`` is an alphanumeric string of text enclosed in quotes. The text string is
              limited to 30 characters. It contains the text label information for bus.
        """
        return self._label

    @property
    def lin(self) -> BusBItemLin:
        """Return the ``BUS:B<x>:LIN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:LIN:BITRate`` command.
            - ``.idformat``: The ``BUS:B<x>:LIN:IDFORmat`` command.
            - ``.polarity``: The ``BUS:B<x>:LIN:POLarity`` command.
            - ``.source``: The ``BUS:B<x>:LIN:SOUrce`` command.
            - ``.standard``: The ``BUS:B<x>:LIN:STANDard`` command.
        """
        return self._lin

    @property
    def mil1553b(self) -> BusBItemMil1553b:
        """Return the ``BUS:B<x>:MIL1553B`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MIL1553B?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIL1553B?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:MIL1553B:POLarity`` command.
            - ``.responsetime``: The ``BUS:B<x>:MIL1553B:RESPonsetime`` command tree.
            - ``.source``: The ``BUS:B<x>:MIL1553B:SOUrce`` command.
        """
        return self._mil1553b

    @property
    def mipicsitwo(self) -> BusBItemMipicsitwo:
        """Return the ``BUS:B<x>:MIPICSITWo`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MIPICSITWo?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIPICSITWo?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.clock``: The ``BUS:B<x>:MIPICSITWo:CLOCk`` command tree.
            - ``.lane``: The ``BUS:B<x>:MIPICSITWo:LANE<x>`` command tree.
        """
        return self._mipicsitwo

    @property
    def mipidsione(self) -> BusBItemMipidsione:
        """Return the ``BUS:B<x>:MIPIDSIOne`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MIPIDSIOne?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIPIDSIOne?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.clock``: The ``BUS:B<x>:MIPIDSIOne:CLOCk`` command tree.
            - ``.lane``: The ``BUS:B<x>:MIPIDSIOne:LANE<x>`` command tree.
        """
        return self._mipidsione

    @property
    def parallel(self) -> BusBItemParallel:
        """Return the ``BUS:B<x>:PARallel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.clock``: The ``BUS:B<x>:PARallel:CLOCk`` command tree.
            - ``.isclocked``: The ``BUS:B<x>:PARallel:ISCLOCKED`` command.
            - ``.sources``: The ``BUS:B<x>:PARallel:SOURCES`` command.
        """
        return self._parallel

    @property
    def pcie(self) -> BusBItemPcie:
        """Return the ``BUS:B<x>:PCIE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PCIE?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PCIE?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:PCIE:BITRate`` command.
            - ``.hysteresis``: The ``BUS:B<x>:PCIE:HYSTeresis`` command.
            - ``.lane``: The ``BUS:B<x>:PCIE:LANE`` command.
            - ``.source``: The ``BUS:B<x>:PCIE:SOUrce`` command.
        """
        return self._pcie

    @property
    def position(self) -> BusBItemPosition:
        """Return the ``BUS:B<x>:POSition`` command.

        Description:
            - This command specifies the position of the bus waveform on the display.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:POSition?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:POSition value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:POSition <NR3>
            - BUS:B<x>:POSition?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the position of the bus <x>
              waveform on the display.
        """
        return self._position

    @property
    def rs232c(self) -> BusBItemRs232c:
        """Return the ``BUS:B<x>:RS232C`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:RS232C:BITRate`` command.
            - ``.databits``: The ``BUS:B<x>:RS232C:DATABits`` command.
            - ``.delimiter``: The ``BUS:B<x>:RS232C:DELIMiter`` command.
            - ``.displaymode``: The ``BUS:B<x>:RS232C:DISplaymode`` command.
            - ``.parity``: The ``BUS:B<x>:RS232C:PARity`` command.
            - ``.polarity``: The ``BUS:B<x>:RS232C:POLarity`` command.
            - ``.source``: The ``BUS:B<x>:RS232C:SOUrce`` command.
        """
        return self._rs232c

    @property
    def s64b66b(self) -> BusBItemS64b66b:
        """Return the ``BUS:B<x>:S64B66B`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:S64B66B?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S64B66B?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:S64B66B:BITRate`` command.
            - ``.descramble``: The ``BUS:B<x>:S64B66B:DESCRAMble`` command.
            - ``.hysteresis``: The ``BUS:B<x>:S64B66B:HYSTeresis`` command.
            - ``.source``: The ``BUS:B<x>:S64B66B:SOUrce`` command.
        """
        return self._s64b66b

    @property
    def s8b10b(self) -> BusBItemS8b10b:
        """Return the ``BUS:B<x>:S8B10B`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:S8B10B?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S8B10B?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:S8B10B:BITRate`` command.
            - ``.hysteresis``: The ``BUS:B<x>:S8B10B:HYSTeresis`` command.
            - ``.source``: The ``BUS:B<x>:S8B10B:SOUrce`` command.
        """
        return self._s8b10b

    @property
    def spi(self) -> BusBItemSpi:
        """Return the ``BUS:B<x>:SPI`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.bitorder``: The ``BUS:B<x>:SPI:BITOrder`` command.
            - ``.clock``: The ``BUS:B<x>:SPI:CLOCk`` command tree.
            - ``.data``: The ``BUS:B<x>:SPI:DATa`` command tree.
            - ``.framing``: The ``BUS:B<x>:SPI:FRAMING`` command.
            - ``.idletime``: The ``BUS:B<x>:SPI:IDLETime`` command.
            - ``.select``: The ``BUS:B<x>:SPI:SELect`` command tree.
        """
        return self._spi

    @property
    def type(self) -> BusBItemType:
        """Return the ``BUS:B<x>:TYPe`` command.

        Description:
            - This command sets or queries the type for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:TYPe?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:TYPe value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:TYPe {CAN|CUSTom|FLEXRAY|LIN|I2C|MIPICSITWo|MIPIDSIOne|PARallel|PCIE|RS232c|S8B10B|SPI|USB|ETHernet}
            - BUS:B<x>:TYPe?
            ```

        Info:
            - ``CAN`` specifies a CAN bus.
            - ``CUSTom`` specifies a custom bus.
            - ``FLEXRAY`` specifies a FLEXRAY bus.
            - ``LIN`` specifies a LIN bus.
            - ``I2C`` specifies the Inter-IC bus.
            - ``MIPICSITWo`` specifies the MIPI CSI2 bus.
            - ``MIPIDSIOne`` specifies the MIPI DSI1 bus.
            - ``PARallel`` specifies the Parallel bus.
            - ``PCIE`` specifies a PCIe bus.
            - ``RS232`` specifies the RS232 Serial bus.
            - ``S8B10B`` specifies the 8B10B bus.
            - ``SPI`` specifies the Serial Peripheral Interface bus.
            - ``USB`` specifies the Universal Serial Bus.
            - ``ETHernet`` specifies the Ethernet bus.
        """  # noqa: E501
        return self._type

    @property
    def usb(self) -> BusBItemUsb:
        """Return the ``BUS:B<x>:USB`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:USB?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:USB:BITRate`` command.
            - ``.probe``: The ``BUS:B<x>:USB:PRObe`` command.
            - ``.source``: The ``BUS:B<x>:USB:SOUrce`` command.
        """
        return self._usb


class BusB1ItemUsbHysteresis(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B1<x>:USB:HYSTeresis`` command.

    Description:
        - This command sets or queries the hysteresis for USB Super Speed.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B1<x>:USB:HYSTeresis?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B1<x>:USB:HYSTeresis?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B1<x>:USB:HYSTeresis value``
          command.

    SCPI Syntax:
        ```
        - BUS:B1<x>:USB:HYSTeresis <NR3>
        - BUS:B1<x>:USB:HYSTeresis?
        ```

    Info:
        - ``<NR3>`` sets the hysteresis for USB Super Speed.
    """


class BusB1ItemUsb(SCPICmdRead):
    """The ``BUS:B1<x>:USB`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B1<x>:USB?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B1<x>:USB?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.hysteresis``: The ``BUS:B1<x>:USB:HYSTeresis`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hysteresis = BusB1ItemUsbHysteresis(device, f"{self._cmd_syntax}:HYSTeresis")

    @property
    def hysteresis(self) -> BusB1ItemUsbHysteresis:
        """Return the ``BUS:B1<x>:USB:HYSTeresis`` command.

        Description:
            - This command sets or queries the hysteresis for USB Super Speed.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B1<x>:USB:HYSTeresis?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B1<x>:USB:HYSTeresis?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B1<x>:USB:HYSTeresis value``
              command.

        SCPI Syntax:
            ```
            - BUS:B1<x>:USB:HYSTeresis <NR3>
            - BUS:B1<x>:USB:HYSTeresis?
            ```

        Info:
            - ``<NR3>`` sets the hysteresis for USB Super Speed.
        """
        return self._hysteresis


class BusB1ItemDisplayLayout(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B1<x>:DISplay:LAYout`` command.

    Description:
        - This command sets or queries the format a bus layer should use.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B1<x>:DISplay:LAYout?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B1<x>:DISplay:LAYout?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B1<x>:DISplay:LAYout value``
          command.

    SCPI Syntax:
        ```
        - BUS:B1<x>:DISplay:LAYout <QString>
        - BUS:B1<x>:DISplay:LAYout?
        ```

    Info:
        - ``<QString>`` consists of two items; the layer identifier and the format identifier.
    """

    _WRAP_ARG_WITH_QUOTES = True


class BusB1ItemDisplayHierarchical(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B1<x>:DISplay:HIERarchical`` command.

    Description:
        - This command sets or queries the display of a bus layer on or off.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B1<x>:DISplay:HIERarchical?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B1<x>:DISplay:HIERarchical?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B1<x>:DISplay:HIERarchical value``
          command.

    SCPI Syntax:
        ```
        - BUS:B1<x>:DISplay:HIERarchical <QString>
        - BUS:B1<x>:DISplay:HIERarchical?
        ```

    Info:
        - ``<QString>`` consists of two items; the layer identifier and the ON/OFF value.
    """

    _WRAP_ARG_WITH_QUOTES = True


class BusB1ItemDisplay(SCPICmdRead):
    """The ``BUS:B1<x>:DISplay`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B1<x>:DISplay?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B1<x>:DISplay?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.hierarchical``: The ``BUS:B1<x>:DISplay:HIERarchical`` command.
        - ``.layout``: The ``BUS:B1<x>:DISplay:LAYout`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hierarchical = BusB1ItemDisplayHierarchical(
            device, f"{self._cmd_syntax}:HIERarchical"
        )
        self._layout = BusB1ItemDisplayLayout(device, f"{self._cmd_syntax}:LAYout")

    @property
    def hierarchical(self) -> BusB1ItemDisplayHierarchical:
        """Return the ``BUS:B1<x>:DISplay:HIERarchical`` command.

        Description:
            - This command sets or queries the display of a bus layer on or off.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B1<x>:DISplay:HIERarchical?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B1<x>:DISplay:HIERarchical?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B1<x>:DISplay:HIERarchical value`` command.

        SCPI Syntax:
            ```
            - BUS:B1<x>:DISplay:HIERarchical <QString>
            - BUS:B1<x>:DISplay:HIERarchical?
            ```

        Info:
            - ``<QString>`` consists of two items; the layer identifier and the ON/OFF value.
        """
        return self._hierarchical

    @property
    def layout(self) -> BusB1ItemDisplayLayout:
        """Return the ``BUS:B1<x>:DISplay:LAYout`` command.

        Description:
            - This command sets or queries the format a bus layer should use.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B1<x>:DISplay:LAYout?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B1<x>:DISplay:LAYout?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B1<x>:DISplay:LAYout value``
              command.

        SCPI Syntax:
            ```
            - BUS:B1<x>:DISplay:LAYout <QString>
            - BUS:B1<x>:DISplay:LAYout?
            ```

        Info:
            - ``<QString>`` consists of two items; the layer identifier and the format identifier.
        """
        return self._layout


class BusB1Item(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``BUS:B1<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B1<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B1<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.display``: The ``BUS:B1<x>:DISplay`` command tree.
        - ``.usb``: The ``BUS:B1<x>:USB`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._display = BusB1ItemDisplay(device, f"{self._cmd_syntax}:DISplay")
        self._usb = BusB1ItemUsb(device, f"{self._cmd_syntax}:USB")

    @property
    def display(self) -> BusB1ItemDisplay:
        """Return the ``BUS:B1<x>:DISplay`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B1<x>:DISplay?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B1<x>:DISplay?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.hierarchical``: The ``BUS:B1<x>:DISplay:HIERarchical`` command.
            - ``.layout``: The ``BUS:B1<x>:DISplay:LAYout`` command.
        """
        return self._display

    @property
    def usb(self) -> BusB1ItemUsb:
        """Return the ``BUS:B1<x>:USB`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B1<x>:USB?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B1<x>:USB?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.hysteresis``: The ``BUS:B1<x>:USB:HYSTeresis`` command.
        """
        return self._usb


class Bus(SCPICmdRead):
    """The ``BUS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.b1``: The ``BUS:B1<x>`` command tree.
        - ``.b``: The ``BUS:B<x>`` command tree.
        - ``.ch``: The ``BUS:CH<x>`` command tree.
        - ``.math``: The ``BUS:MATH<x>`` command tree.
        - ``.ref``: The ``BUS:REF<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "BUS") -> None:
        super().__init__(device, cmd_syntax)
        self._b1: Dict[int, BusB1Item] = DefaultDictPassKeyToFactory(
            lambda x: BusB1Item(device, f"{self._cmd_syntax}:B1{x}")
        )
        self._b: Dict[int, BusBItem] = DefaultDictPassKeyToFactory(
            lambda x: BusBItem(device, f"{self._cmd_syntax}:B{x}")
        )
        self._ch: Dict[int, BusChannel] = DefaultDictPassKeyToFactory(
            lambda x: BusChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._math: Dict[int, BusMathItem] = DefaultDictPassKeyToFactory(
            lambda x: BusMathItem(device, f"{self._cmd_syntax}:MATH{x}")
        )
        self._ref: Dict[int, BusRefItem] = DefaultDictPassKeyToFactory(
            lambda x: BusRefItem(device, f"{self._cmd_syntax}:REF{x}")
        )

    @property
    def b1(self) -> Dict[int, BusB1Item]:
        """Return the ``BUS:B1<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B1<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B1<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.display``: The ``BUS:B1<x>:DISplay`` command tree.
            - ``.usb``: The ``BUS:B1<x>:USB`` command tree.
        """
        return self._b1

    @property
    def b(self) -> Dict[int, BusBItem]:
        """Return the ``BUS:B<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.can``: The ``BUS:B<x>:CAN`` command tree.
            - ``.display``: The ``BUS:B<x>:DISplay`` command tree.
            - ``.ethernet``: The ``BUS:B<x>:ETHERnet`` command tree.
            - ``.flexray``: The ``BUS:B<x>:FLEXRAY`` command tree.
            - ``.i2c``: The ``BUS:B<x>:I2C`` command tree.
            - ``.label``: The ``BUS:B<x>:LABel`` command.
            - ``.lin``: The ``BUS:B<x>:LIN`` command tree.
            - ``.mil1553b``: The ``BUS:B<x>:MIL1553B`` command tree.
            - ``.mipicsitwo``: The ``BUS:B<x>:MIPICSITWo`` command tree.
            - ``.mipidsione``: The ``BUS:B<x>:MIPIDSIOne`` command tree.
            - ``.parallel``: The ``BUS:B<x>:PARallel`` command tree.
            - ``.pcie``: The ``BUS:B<x>:PCIE`` command tree.
            - ``.position``: The ``BUS:B<x>:POSition`` command.
            - ``.rs232c``: The ``BUS:B<x>:RS232C`` command tree.
            - ``.s64b66b``: The ``BUS:B<x>:S64B66B`` command tree.
            - ``.s8b10b``: The ``BUS:B<x>:S8B10B`` command tree.
            - ``.spi``: The ``BUS:B<x>:SPI`` command tree.
            - ``.type``: The ``BUS:B<x>:TYPe`` command.
            - ``.usb``: The ``BUS:B<x>:USB`` command tree.
        """
        return self._b

    @property
    def ch(self) -> Dict[int, BusChannel]:
        """Return the ``BUS:CH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:CH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.lowthreshold``: The ``BUS:CH<x>:LOWTHRESHold`` command.
            - ``.threshold``: The ``BUS:CH<x>:THRESHold`` command.
        """
        return self._ch

    @property
    def math(self) -> Dict[int, BusMathItem]:
        """Return the ``BUS:MATH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:MATH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:MATH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.lowthreshold``: The ``BUS:MATH<x>:LOWTHRESHold`` command.
            - ``.threshold``: The ``BUS:MATH<x>:THRESHold`` command.
        """
        return self._math

    @property
    def ref(self) -> Dict[int, BusRefItem]:
        """Return the ``BUS:REF<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:REF<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.threshold``: The ``BUS:REF<x>:THRESHold`` command.
        """
        return self._ref
