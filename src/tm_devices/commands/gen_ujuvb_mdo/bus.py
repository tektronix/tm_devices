# pylint: disable=line-too-long
"""The bus commands module.

These commands are used in the following models:
MDO3

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - BUS:B<x>:ARINC429A:BITRate {LOW|HI|<NR1>}
    - BUS:B<x>:ARINC429A:BITRate?
    - BUS:B<x>:ARINC429A:DATA:FORMAT {DATA|SDIDATA|SDIDATASSM}
    - BUS:B<x>:ARINC429A:DATA:FORMAT?
    - BUS:B<x>:ARINC429A:POLarity {NORMal|INVERTed}
    - BUS:B<x>:ARINC429A:POLarity?
    - BUS:B<x>:ARINC429A:SOUrce {CH<x>|MATH|REF<x>}
    - BUS:B<x>:ARINC429A:SOUrce?
    - BUS:B<x>:AUDio:BITDelay <NR1>
    - BUS:B<x>:AUDio:BITDelay?
    - BUS:B<x>:AUDio:BITOrder {MSB|LSB}
    - BUS:B<x>:AUDio:BITOrder?
    - BUS:B<x>:AUDio:CHANnel:SIZe <NR1>
    - BUS:B<x>:AUDio:CHANnel:SIZe?
    - BUS:B<x>:AUDio:CLOCk:POLarity {FALL|RISe}
    - BUS:B<x>:AUDio:CLOCk:POLarity?
    - BUS:B<x>:AUDio:CLOCk:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:AUDio:CLOCk:SOUrce?
    - BUS:B<x>:AUDio:DATa:POLarity {NORMal|INVERTed}
    - BUS:B<x>:AUDio:DATa:POLarity?
    - BUS:B<x>:AUDio:DATa:SIZe <NR1>
    - BUS:B<x>:AUDio:DATa:SIZe?
    - BUS:B<x>:AUDio:DATa:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:AUDio:DATa:SOUrce?
    - BUS:B<x>:AUDio:DISplay:FORMat {BINary|HEXadecimal|SIGNEDDECimal}
    - BUS:B<x>:AUDio:DISplay:FORMat?
    - BUS:B<x>:AUDio:FRAME:SIZe <NR1>
    - BUS:B<x>:AUDio:FRAME:SIZe?
    - BUS:B<x>:AUDio:FRAMESync:POLarity {FALL|RISe}
    - BUS:B<x>:AUDio:FRAMESync:POLarity?
    - BUS:B<x>:AUDio:FRAMESync:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:AUDio:FRAMESync:SOUrce?
    - BUS:B<x>:AUDio:TYPe {I2S|LJ|RJ|TDM}
    - BUS:B<x>:AUDio:TYPe?
    - BUS:B<x>:AUDio:WORDSel:POLarity {NORMal|INVERTed}
    - BUS:B<x>:AUDio:WORDSel:POLarity?
    - BUS:B<x>:AUDio:WORDSel:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:AUDio:WORDSel:SOUrce?
    - BUS:B<x>:CAN:BITRate <NR1>
    - BUS:B<x>:CAN:BITRate?
    - BUS:B<x>:CAN:FD:BITRate <NR1>
    - BUS:B<x>:CAN:FD:BITRate?
    - BUS:B<x>:CAN:FD:STANDard {ISO | NONISO} string
    - BUS:B<x>:CAN:FD:STANDard?
    - BUS:B<x>:CAN:PRObe {CANH|CANL|RX|TX|DIFFerential}
    - BUS:B<x>:CAN:PRObe?
    - BUS:B<x>:CAN:SAMPLEpoint <NR1>
    - BUS:B<x>:CAN:SAMPLEpoint?
    - BUS:B<x>:CAN:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:CAN:SOUrce?
    - BUS:B<x>:CAN:STANDard {CAN2X|CANFD} string
    - BUS:B<x>:CAN:STANDard?
    - BUS:B<x>:DISplay:FORMat {BINary|HEXadecimal|ASCII|MIXed|MIXED2|BLOCKHEX}
    - BUS:B<x>:DISplay:FORMat?
    - BUS:B<x>:DISplay:TYPe {BUS|BOTh}
    - BUS:B<x>:DISplay:TYPe?
    - BUS:B<x>:ETHERnet:PROTOcol {IPv4|OTHER}
    - BUS:B<x>:ETHERnet:PROTOcol?
    - BUS:B<x>:ETHERnet:PRObe {DIFFerential|SINGleended}
    - BUS:B<x>:ETHERnet:PRObe?
    - BUS:B<x>:ETHERnet:SOUrce:DIFFerential {CH<x>|MATH|REF<x>}
    - BUS:B<x>:ETHERnet:SOUrce:DIFFerential?
    - BUS:B<x>:ETHERnet:SOUrce:DMINus {CH<x>|D<x>}
    - BUS:B<x>:ETHERnet:SOUrce:DMINus?
    - BUS:B<x>:ETHERnet:SOUrce:DPLUs {CH<x>|D<x>}
    - BUS:B<x>:ETHERnet:SOUrce:DPLUs?
    - BUS:B<x>:ETHERnet:TYPe {ENET10BASET|ENET100BASETX}
    - BUS:B<x>:ETHERnet:TYPe?
    - BUS:B<x>:FLEXray:BITRate <NR1>
    - BUS:B<x>:FLEXray:BITRate?
    - BUS:B<x>:FLEXray:CHannel {A|B}
    - BUS:B<x>:FLEXray:CHannel?
    - BUS:B<x>:FLEXray:SIGnal {BDIFFBP|BM|TXRX}
    - BUS:B<x>:FLEXray:SIGnal?
    - BUS:B<x>:FLEXray:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:FLEXray:SOUrce?
    - BUS:B<x>:I2C:ADDRess:RWINClude {ON|OFF|<NR1>}
    - BUS:B<x>:I2C:ADDRess:RWINClude?
    - BUS:B<x>:I2C:CLOCk:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:I2C:CLOCk:SOUrce?
    - BUS:B<x>:I2C:DATa:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:I2C:DATa:SOUrce?
    - BUS:B<x>:I2C:SCLk:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:I2C:SCLk:SOUrce?
    - BUS:B<x>:I2C:SDAta:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:I2C:SDAta:SOUrce?
    - BUS:B<x>:LABel <Qstring>
    - BUS:B<x>:LABel?
    - BUS:B<x>:LIN:BITRate <NR1>
    - BUS:B<x>:LIN:BITRate?
    - BUS:B<x>:LIN:IDFORmat {NOPARity|PARity}
    - BUS:B<x>:LIN:IDFORmat?
    - BUS:B<x>:LIN:MAXBytedelim <NR1>
    - BUS:B<x>:LIN:MAXBytedelim?
    - BUS:B<x>:LIN:POLarity {NORMal|INVerted}
    - BUS:B<x>:LIN:POLarity?
    - BUS:B<x>:LIN:SAMPLEpoint <NR1>
    - BUS:B<x>:LIN:SAMPLEpoint?
    - BUS:B<x>:LIN:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:LIN:SOUrce?
    - BUS:B<x>:LIN:STANDard {V1X|V2X|MIXed}
    - BUS:B<x>:LIN:STANDard?
    - BUS:B<x>:MIL1553B:POLarity {NORMal|INVERTed}
    - BUS:B<x>:MIL1553B:POLarity?
    - BUS:B<x>:MIL1553B:RESPonsetime:MAXimum <NR3>
    - BUS:B<x>:MIL1553B:RESPonsetime:MAXimum?
    - BUS:B<x>:MIL1553B:RESPonsetime:MINimum <NR3>
    - BUS:B<x>:MIL1553B:RESPonsetime:MINimum?
    - BUS:B<x>:MIL1553B:SOUrce {CH<x>|MATH|REF<x>}
    - BUS:B<x>:MIL1553B:SOUrce?
    - BUS:B<x>:PARallel:BIT<x>:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:PARallel:BIT<x>:SOUrce?
    - BUS:B<x>:PARallel:CLOCk:EDGE {EITher|RISing|FALling}
    - BUS:B<x>:PARallel:CLOCk:EDGE?
    - BUS:B<x>:PARallel:CLOCk:ISCLOCKed {YES|NO}
    - BUS:B<x>:PARallel:CLOCk:ISCLOCKed?
    - BUS:B<x>:PARallel:CLOCk:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:PARallel:CLOCk:SOUrce?
    - BUS:B<x>:PARallel:WIDth <NR1>
    - BUS:B<x>:PARallel:WIDth?
    - BUS:B<x>:POSition <NR3>
    - BUS:B<x>:POSition?
    - BUS:B<x>:RS232C:BITRate <NR1>
    - BUS:B<x>:RS232C:BITRate?
    - BUS:B<x>:RS232C:DATABits {7|8|9}
    - BUS:B<x>:RS232C:DATABits?
    - BUS:B<x>:RS232C:DELIMiter {NULl|LF|CR|SPace|XFF}
    - BUS:B<x>:RS232C:DELIMiter?
    - BUS:B<x>:RS232C:DISplaymode {FRAme|PACKET}
    - BUS:B<x>:RS232C:DISplaymode?
    - BUS:B<x>:RS232C:PARity {NONe|EVEN|ODD}
    - BUS:B<x>:RS232C:PARity?
    - BUS:B<x>:RS232C:POLarity {NORMal|INVERTed}
    - BUS:B<x>:RS232C:POLarity?
    - BUS:B<x>:RS232C:RX:SOUrce {CH<x>|D<x>|Off}
    - BUS:B<x>:RS232C:RX:SOUrce?
    - BUS:B<x>:RS232C:TX:SOUrce {CH<x>|D<x>|Off}
    - BUS:B<x>:RS232C:TX:SOUrce?
    - BUS:B<x>:SENT:CHANWidth {TWELVEtwelve|FOURTEENten|SIXTEENeight}
    - BUS:B<x>:SENT:CHANWidth?
    - BUS:B<x>:SENT:NIBBLECount {THREE|FOUR|SIX}
    - BUS:B<x>:SENT:NIBBLECount?
    - BUS:B<x>:SENT:NUMCHANnel {ONE|TWO}
    - BUS:B<x>:SENT:NUMCHANnel?
    - BUS:B<x>:SENT:PAUSEPULSe {NO|YES}
    - BUS:B<x>:SENT:PAUSEPULSe?
    - BUS:B<x>:SENT:POLARITY {INVerted|NORmal}
    - BUS:B<x>:SENT:POLARITY?
    - BUS:B<x>:SENT:SLOW {NOne|ENHANCED4|ENHANCED8|SHOrt}
    - BUS:B<x>:SENT:SLOW?
    - BUS:B<x>:SENT:SOUrce {CH<x>|D<x>|MATH|REF<x>}
    - BUS:B<x>:SENT:SOUrce?
    - BUS:B<x>:SENT:TICKTIME <NR3>
    - BUS:B<x>:SENT:TICKTIME?
    - BUS:B<x>:SENT:TICKTOLerance <NR3>
    - BUS:B<x>:SENT:TICKTOLerance?
    - BUS:B<x>:SPI:BITOrder {LSB|MSB}
    - BUS:B<x>:SPI:BITOrder?
    - BUS:B<x>:SPI:CLOCk:POLarity {FALL|RISe}
    - BUS:B<x>:SPI:CLOCk:POLarity?
    - BUS:B<x>:SPI:CLOCk:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:SPI:CLOCk:SOUrce?
    - BUS:B<x>:SPI:DATa:IN:POLarity {LOW|HIGH}
    - BUS:B<x>:SPI:DATa:IN:POLarity?
    - BUS:B<x>:SPI:DATa:IN:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:SPI:DATa:IN:SOUrce?
    - BUS:B<x>:SPI:DATa:MISO:POLarity {LOW|HIGH}
    - BUS:B<x>:SPI:DATa:MISO:POLarity?
    - BUS:B<x>:SPI:DATa:MISO:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:SPI:DATa:MISO:SOUrce?
    - BUS:B<x>:SPI:DATa:MOSI:POLarity {LOW|HIGH}
    - BUS:B<x>:SPI:DATa:MOSI:POLarity?
    - BUS:B<x>:SPI:DATa:MOSI:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:SPI:DATa:MOSI:SOUrce?
    - BUS:B<x>:SPI:DATa:OUT:POLarity {LOW|HIGH}
    - BUS:B<x>:SPI:DATa:OUT:POLarity?
    - BUS:B<x>:SPI:DATa:OUT:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:SPI:DATa:OUT:SOUrce?
    - BUS:B<x>:SPI:DATa:SIZe <NR1>
    - BUS:B<x>:SPI:DATa:SIZe?
    - BUS:B<x>:SPI:FRAMING {SS|IDLEtime}
    - BUS:B<x>:SPI:FRAMING?
    - BUS:B<x>:SPI:IDLETime <NR3>
    - BUS:B<x>:SPI:IDLETime?
    - BUS:B<x>:SPI:SCLk:POLarity {FALL|RISe}
    - BUS:B<x>:SPI:SCLk:POLarity?
    - BUS:B<x>:SPI:SCLk:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:SPI:SCLk:SOUrce?
    - BUS:B<x>:SPI:SELect:POLarity {LOW|HIGH}
    - BUS:B<x>:SPI:SELect:POLarity?
    - BUS:B<x>:SPI:SELect:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:SPI:SELect:SOUrce?
    - BUS:B<x>:SPI:SS:POLarity {LOW|HIGH}
    - BUS:B<x>:SPI:SS:POLarity?
    - BUS:B<x>:SPI:SS:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:SPI:SS:SOUrce?
    - BUS:B<x>:STATE {ON|OFF|<NR1>}
    - BUS:B<x>:STATE?
    - BUS:B<x>:TYPe {I2C|SPI|CAN|RS232C|PARallel|USB|LIN|FLEXRay|AUDio|ETHERnet|MIL1553B|ARINC429A}
    - BUS:B<x>:TYPe?
    - BUS:B<x>:USB:BITRate {LOW|FULL|HIGH}
    - BUS:B<x>:USB:BITRate?
    - BUS:B<x>:USB:PRObe {DIFFerential|SINGleended}
    - BUS:B<x>:USB:PRObe?
    - BUS:B<x>:USB:SOUrce:DIFFerential {CH<x>|MATH|REF<x>}
    - BUS:B<x>:USB:SOUrce:DIFFerential?
    - BUS:B<x>:USB:SOUrce:DMINus {CH<x>|D<x>}
    - BUS:B<x>:USB:SOUrce:DMINus?
    - BUS:B<x>:USB:SOUrce:DPLUs {CH<x>|D<x>}
    - BUS:B<x>:USB:SOUrce:DPLUs?
    - BUS:LOWerthreshold:CH<x> {<NR3>|ECL|TTL}
    - BUS:LOWerthreshold:CH<x>?
    - BUS:LOWerthreshold:MATH {<NR3>|ECL|TTL}
    - BUS:LOWerthreshold:MATH1 {<NR3>|ECL|TTL}
    - BUS:LOWerthreshold:MATH1?
    - BUS:LOWerthreshold:MATH?
    - BUS:LOWerthreshold:REF<x> {<NR3>|ECL|TTL}
    - BUS:LOWerthreshold:REF<x>?
    - BUS:THReshold:CH<x> {ECL|TTL|<NR3>}
    - BUS:THReshold:CH<x>?
    - BUS:THReshold:D<x> {<NR3>|ECL|TTL}
    - BUS:THReshold:D<x>?
    - BUS:UPPerthreshold:CH<x> {<NR3>|ECL|TTL}
    - BUS:UPPerthreshold:CH<x>?
    - BUS:UPPerthreshold:MATH {<NR3>|ECL|TTL}
    - BUS:UPPerthreshold:MATH1 {<NR3>|ECL|TTL}
    - BUS:UPPerthreshold:MATH1?
    - BUS:UPPerthreshold:MATH?
    - BUS:UPPerthreshold:REF<x> {<NR3>|ECL|TTL}
    - BUS:UPPerthreshold:REF<x>?
    - BUS?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    ValidatedChannel,
    ValidatedDigitalBit,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class BusUpperthresholdRefItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``BUS:UPPerthreshold:REF<x>`` command.

    Description:
        - This command sets the upper threshold for each reference waveform. This applies to all
          search and trigger types that use that reference waveform.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:UPPerthreshold:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:UPPerthreshold:REF<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:UPPerthreshold:REF<x> value``
          command.

    SCPI Syntax:
        ```
        - BUS:UPPerthreshold:REF<x> {<NR3>|ECL|TTL}
        - BUS:UPPerthreshold:REF<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the upper threshold for the reference
          waveform, in volts.
        - ``ECL`` - ECL (-1.3 volts). Note that this setting is constrained, depending upon the
          vertical scale for the specified reference waveform.
        - ``TTL`` - TTL (1.4 volts). Note that this setting is constrained, depending upon the
          vertical scale for the specified reference waveform.
    """


class BusUpperthresholdMath1(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:UPPerthreshold:MATH1`` command.

    Description:
        - This command specifies the upper threshold of the math waveform. This will apply to all
          search and trigger types that use the math waveform.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:UPPerthreshold:MATH1?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:UPPerthreshold:MATH1?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:UPPerthreshold:MATH1 value``
          command.

    SCPI Syntax:
        ```
        - BUS:UPPerthreshold:MATH1 {<NR3>|ECL|TTL}
        - BUS:UPPerthreshold:MATH1?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the upper threshold of the math
          waveform, in volts.
        - ``ECL`` - ECL (-1.3 volts). Note that this setting is constrained, depending upon the
          vertical scale for the specified math waveform.
        - ``TTL`` - TTL (1.4 volts). Note that this setting is constrained, depending upon the
          vertical scale for the specified math waveform.
    """


class BusUpperthresholdMath(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:UPPerthreshold:MATH`` command.

    Description:
        - This command specifies the upper threshold of the math waveform. This will apply to all
          search and trigger types that use the math waveform.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:UPPerthreshold:MATH?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:UPPerthreshold:MATH?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:UPPerthreshold:MATH value``
          command.

    SCPI Syntax:
        ```
        - BUS:UPPerthreshold:MATH {<NR3>|ECL|TTL}
        - BUS:UPPerthreshold:MATH?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the upper threshold of the math
          waveform, in volts.
        - ``ECL`` - ECL (-1.3 volts). Note that this setting is constrained, depending upon the
          vertical scale for the specified math waveform.
        - ``TTL`` - TTL (1.4 volts). Note that this setting is constrained, depending upon the
          vertical scale for the specified math waveform.
    """


class BusUpperthresholdChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``BUS:UPPerthreshold:CH<x>`` command.

    Description:
        - Sets the upper threshold for each analog channel (1-4). This applies to all search and
          trigger types that use the channel.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:UPPerthreshold:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:UPPerthreshold:CH<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:UPPerthreshold:CH<x> value``
          command.

    SCPI Syntax:
        ```
        - BUS:UPPerthreshold:CH<x> {<NR3>|ECL|TTL}
        - BUS:UPPerthreshold:CH<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the threshold, in volts.
        - ``ECL`` specifies a preset ECL high level of -1.3V.
        - ``TTL`` specifies a preset TTL high level of 1.4V.
    """


class BusUpperthreshold(SCPICmdRead):
    """The ``BUS:UPPerthreshold`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:UPPerthreshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:UPPerthreshold?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``BUS:UPPerthreshold:CH<x>`` command.
        - ``.ref``: The ``BUS:UPPerthreshold:REF<x>`` command.
        - ``.math``: The ``BUS:UPPerthreshold:MATH`` command.
        - ``.math1``: The ``BUS:UPPerthreshold:MATH1`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, BusUpperthresholdChannel] = DefaultDictPassKeyToFactory(
            lambda x: BusUpperthresholdChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._ref: Dict[int, BusUpperthresholdRefItem] = DefaultDictPassKeyToFactory(
            lambda x: BusUpperthresholdRefItem(device, f"{self._cmd_syntax}:REF{x}")
        )
        self._math = BusUpperthresholdMath(device, f"{self._cmd_syntax}:MATH")
        self._math1 = BusUpperthresholdMath1(device, f"{self._cmd_syntax}:MATH1")

    @property
    def ch(self) -> Dict[int, BusUpperthresholdChannel]:
        """Return the ``BUS:UPPerthreshold:CH<x>`` command.

        Description:
            - Sets the upper threshold for each analog channel (1-4). This applies to all search and
              trigger types that use the channel.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:UPPerthreshold:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:UPPerthreshold:CH<x>?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:UPPerthreshold:CH<x> value``
              command.

        SCPI Syntax:
            ```
            - BUS:UPPerthreshold:CH<x> {<NR3>|ECL|TTL}
            - BUS:UPPerthreshold:CH<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the threshold, in volts.
            - ``ECL`` specifies a preset ECL high level of -1.3V.
            - ``TTL`` specifies a preset TTL high level of 1.4V.
        """
        return self._ch

    @property
    def ref(self) -> Dict[int, BusUpperthresholdRefItem]:
        """Return the ``BUS:UPPerthreshold:REF<x>`` command.

        Description:
            - This command sets the upper threshold for each reference waveform. This applies to all
              search and trigger types that use that reference waveform.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:UPPerthreshold:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:UPPerthreshold:REF<x>?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:UPPerthreshold:REF<x> value``
              command.

        SCPI Syntax:
            ```
            - BUS:UPPerthreshold:REF<x> {<NR3>|ECL|TTL}
            - BUS:UPPerthreshold:REF<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the upper threshold for the
              reference waveform, in volts.
            - ``ECL`` - ECL (-1.3 volts). Note that this setting is constrained, depending upon the
              vertical scale for the specified reference waveform.
            - ``TTL`` - TTL (1.4 volts). Note that this setting is constrained, depending upon the
              vertical scale for the specified reference waveform.
        """
        return self._ref

    @property
    def math(self) -> BusUpperthresholdMath:
        """Return the ``BUS:UPPerthreshold:MATH`` command.

        Description:
            - This command specifies the upper threshold of the math waveform. This will apply to
              all search and trigger types that use the math waveform.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:UPPerthreshold:MATH?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:UPPerthreshold:MATH?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:UPPerthreshold:MATH value``
              command.

        SCPI Syntax:
            ```
            - BUS:UPPerthreshold:MATH {<NR3>|ECL|TTL}
            - BUS:UPPerthreshold:MATH?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the upper threshold of the math
              waveform, in volts.
            - ``ECL`` - ECL (-1.3 volts). Note that this setting is constrained, depending upon the
              vertical scale for the specified math waveform.
            - ``TTL`` - TTL (1.4 volts). Note that this setting is constrained, depending upon the
              vertical scale for the specified math waveform.
        """
        return self._math

    @property
    def math1(self) -> BusUpperthresholdMath1:
        """Return the ``BUS:UPPerthreshold:MATH1`` command.

        Description:
            - This command specifies the upper threshold of the math waveform. This will apply to
              all search and trigger types that use the math waveform.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:UPPerthreshold:MATH1?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:UPPerthreshold:MATH1?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:UPPerthreshold:MATH1 value``
              command.

        SCPI Syntax:
            ```
            - BUS:UPPerthreshold:MATH1 {<NR3>|ECL|TTL}
            - BUS:UPPerthreshold:MATH1?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the upper threshold of the math
              waveform, in volts.
            - ``ECL`` - ECL (-1.3 volts). Note that this setting is constrained, depending upon the
              vertical scale for the specified math waveform.
            - ``TTL`` - TTL (1.4 volts). Note that this setting is constrained, depending upon the
              vertical scale for the specified math waveform.
        """
        return self._math1


class BusThresholdDigitalBit(ValidatedDigitalBit, SCPICmdWrite, SCPICmdRead):
    """The ``BUS:THReshold:D<x>`` command.

    Description:
        - This command specifies the threshold for digital channel <x>, where x is the digital
          channel number (0-15). This will apply to all Search and Trigger Types that use the
          channel.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:THReshold:D<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:THReshold:D<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:THReshold:D<x> value`` command.

    SCPI Syntax:
        ```
        - BUS:THReshold:D<x> {<NR3>|ECL|TTL}
        - BUS:THReshold:D<x>?
        ```

    Info:
        - ``ECL`` specifies a preset ECL high level of -1.3V.
        - ``TTL`` specifies a preset TTL high level of 1.4V.
        - ``<NR3>`` is a floating point number that specifies the threshold level, in volts.
    """


class BusThresholdChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``BUS:THReshold:CH<x>`` command.

    Description:
        - This command specifies the threshold for analog channel <x>, where x is the channel number
          (1-4). This setting applies to all trigger types that use the channel.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:THReshold:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:THReshold:CH<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:THReshold:CH<x> value`` command.

    SCPI Syntax:
        ```
        - BUS:THReshold:CH<x> {ECL|TTL|<NR3>}
        - BUS:THReshold:CH<x>?
        ```

    Info:
        - ``ECL`` specifies a preset ECL high level of -1.3V.
        - ``TTL`` specifies a TTL preset high level of 1.4V.
        - ``<NR3>`` is a floating point number that specifies the threshold level, in volts.
    """


class BusThreshold(SCPICmdRead):
    """The ``BUS:THReshold`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:THReshold?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``BUS:THReshold:CH<x>`` command.
        - ``.d``: The ``BUS:THReshold:D<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, BusThresholdChannel] = DefaultDictPassKeyToFactory(
            lambda x: BusThresholdChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._d: Dict[int, BusThresholdDigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: BusThresholdDigitalBit(device, f"{self._cmd_syntax}:D{x}")
        )

    @property
    def ch(self) -> Dict[int, BusThresholdChannel]:
        """Return the ``BUS:THReshold:CH<x>`` command.

        Description:
            - This command specifies the threshold for analog channel <x>, where x is the channel
              number (1-4). This setting applies to all trigger types that use the channel.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:THReshold:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:THReshold:CH<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:THReshold:CH<x> value``
              command.

        SCPI Syntax:
            ```
            - BUS:THReshold:CH<x> {ECL|TTL|<NR3>}
            - BUS:THReshold:CH<x>?
            ```

        Info:
            - ``ECL`` specifies a preset ECL high level of -1.3V.
            - ``TTL`` specifies a TTL preset high level of 1.4V.
            - ``<NR3>`` is a floating point number that specifies the threshold level, in volts.
        """
        return self._ch

    @property
    def d(self) -> Dict[int, BusThresholdDigitalBit]:
        """Return the ``BUS:THReshold:D<x>`` command.

        Description:
            - This command specifies the threshold for digital channel <x>, where x is the digital
              channel number (0-15). This will apply to all Search and Trigger Types that use the
              channel.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:THReshold:D<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:THReshold:D<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:THReshold:D<x> value`` command.

        SCPI Syntax:
            ```
            - BUS:THReshold:D<x> {<NR3>|ECL|TTL}
            - BUS:THReshold:D<x>?
            ```

        Info:
            - ``ECL`` specifies a preset ECL high level of -1.3V.
            - ``TTL`` specifies a preset TTL high level of 1.4V.
            - ``<NR3>`` is a floating point number that specifies the threshold level, in volts.
        """
        return self._d


class BusLowerthresholdRefItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``BUS:LOWerthreshold:REF<x>`` command.

    Description:
        - This command sets the lower threshold for each reference waveform. This applies to all
          search and trigger types that use that reference waveform.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:LOWerthreshold:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:LOWerthreshold:REF<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:LOWerthreshold:REF<x> value``
          command.

    SCPI Syntax:
        ```
        - BUS:LOWerthreshold:REF<x> {<NR3>|ECL|TTL}
        - BUS:LOWerthreshold:REF<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the lower threshold for the reference
          waveform, in volts.
        - ``ECL`` - ECL (-1.3 volts). Note that this setting is constrained, depending upon the
          vertical scale for the specified reference waveform.
        - ``TTL`` - TTL (1.4 volts). Note that this setting is constrained, depending upon the
          vertical scale for the specified reference waveform.
    """


class BusLowerthresholdMath1(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:LOWerthreshold:MATH1`` command.

    Description:
        - This command specifies the lower threshold for the math waveform. This will apply to all
          search and trigger types that use the math waveform.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:LOWerthreshold:MATH1?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:LOWerthreshold:MATH1?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:LOWerthreshold:MATH1 value``
          command.

    SCPI Syntax:
        ```
        - BUS:LOWerthreshold:MATH1 {<NR3>|ECL|TTL}
        - BUS:LOWerthreshold:MATH1?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the lower threshold for the reference
          waveform, in volts.
        - ``ECL`` - ECL (-1.3 volts). Note that this setting is constrained, depending upon the
          vertical scale of the specified math waveform.
        - ``TTL`` - TTL (1.4 volts). Note that this setting is constrained, depending upon the
          vertical scale of the specified math waveform.
    """


class BusLowerthresholdMath(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:LOWerthreshold:MATH`` command.

    Description:
        - This command specifies the lower threshold for the math waveform. This will apply to all
          search and trigger types that use the math waveform.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:LOWerthreshold:MATH?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:LOWerthreshold:MATH?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:LOWerthreshold:MATH value``
          command.

    SCPI Syntax:
        ```
        - BUS:LOWerthreshold:MATH {<NR3>|ECL|TTL}
        - BUS:LOWerthreshold:MATH?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the lower threshold for the reference
          waveform, in volts.
        - ``ECL`` - ECL (-1.3 volts). Note that this setting is constrained, depending upon the
          vertical scale of the specified math waveform.
        - ``TTL`` - TTL (1.4 volts). Note that this setting is constrained, depending upon the
          vertical scale of the specified math waveform.
    """


class BusLowerthresholdChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``BUS:LOWerthreshold:CH<x>`` command.

    Description:
        - This command sets the lower threshold for each channel. This applies to all search and
          trigger types that use the channel.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:LOWerthreshold:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:LOWerthreshold:CH<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:LOWerthreshold:CH<x> value``
          command.

    SCPI Syntax:
        ```
        - BUS:LOWerthreshold:CH<x> {<NR3>|ECL|TTL}
        - BUS:LOWerthreshold:CH<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the threshold, in volts.
        - ``ECL`` specifies a preset ECL high level of -1.3V.
        - ``TTL`` specifies a preset TTL high level of 1.4V.
    """


class BusLowerthreshold(SCPICmdRead):
    """The ``BUS:LOWerthreshold`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:LOWerthreshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:LOWerthreshold?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``BUS:LOWerthreshold:CH<x>`` command.
        - ``.ref``: The ``BUS:LOWerthreshold:REF<x>`` command.
        - ``.math``: The ``BUS:LOWerthreshold:MATH`` command.
        - ``.math1``: The ``BUS:LOWerthreshold:MATH1`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, BusLowerthresholdChannel] = DefaultDictPassKeyToFactory(
            lambda x: BusLowerthresholdChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._ref: Dict[int, BusLowerthresholdRefItem] = DefaultDictPassKeyToFactory(
            lambda x: BusLowerthresholdRefItem(device, f"{self._cmd_syntax}:REF{x}")
        )
        self._math = BusLowerthresholdMath(device, f"{self._cmd_syntax}:MATH")
        self._math1 = BusLowerthresholdMath1(device, f"{self._cmd_syntax}:MATH1")

    @property
    def ch(self) -> Dict[int, BusLowerthresholdChannel]:
        """Return the ``BUS:LOWerthreshold:CH<x>`` command.

        Description:
            - This command sets the lower threshold for each channel. This applies to all search and
              trigger types that use the channel.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:LOWerthreshold:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:LOWerthreshold:CH<x>?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:LOWerthreshold:CH<x> value``
              command.

        SCPI Syntax:
            ```
            - BUS:LOWerthreshold:CH<x> {<NR3>|ECL|TTL}
            - BUS:LOWerthreshold:CH<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the threshold, in volts.
            - ``ECL`` specifies a preset ECL high level of -1.3V.
            - ``TTL`` specifies a preset TTL high level of 1.4V.
        """
        return self._ch

    @property
    def ref(self) -> Dict[int, BusLowerthresholdRefItem]:
        """Return the ``BUS:LOWerthreshold:REF<x>`` command.

        Description:
            - This command sets the lower threshold for each reference waveform. This applies to all
              search and trigger types that use that reference waveform.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:LOWerthreshold:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:LOWerthreshold:REF<x>?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:LOWerthreshold:REF<x> value``
              command.

        SCPI Syntax:
            ```
            - BUS:LOWerthreshold:REF<x> {<NR3>|ECL|TTL}
            - BUS:LOWerthreshold:REF<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the lower threshold for the
              reference waveform, in volts.
            - ``ECL`` - ECL (-1.3 volts). Note that this setting is constrained, depending upon the
              vertical scale for the specified reference waveform.
            - ``TTL`` - TTL (1.4 volts). Note that this setting is constrained, depending upon the
              vertical scale for the specified reference waveform.
        """
        return self._ref

    @property
    def math(self) -> BusLowerthresholdMath:
        """Return the ``BUS:LOWerthreshold:MATH`` command.

        Description:
            - This command specifies the lower threshold for the math waveform. This will apply to
              all search and trigger types that use the math waveform.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:LOWerthreshold:MATH?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:LOWerthreshold:MATH?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:LOWerthreshold:MATH value``
              command.

        SCPI Syntax:
            ```
            - BUS:LOWerthreshold:MATH {<NR3>|ECL|TTL}
            - BUS:LOWerthreshold:MATH?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the lower threshold for the
              reference waveform, in volts.
            - ``ECL`` - ECL (-1.3 volts). Note that this setting is constrained, depending upon the
              vertical scale of the specified math waveform.
            - ``TTL`` - TTL (1.4 volts). Note that this setting is constrained, depending upon the
              vertical scale of the specified math waveform.
        """
        return self._math

    @property
    def math1(self) -> BusLowerthresholdMath1:
        """Return the ``BUS:LOWerthreshold:MATH1`` command.

        Description:
            - This command specifies the lower threshold for the math waveform. This will apply to
              all search and trigger types that use the math waveform.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:LOWerthreshold:MATH1?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:LOWerthreshold:MATH1?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:LOWerthreshold:MATH1 value``
              command.

        SCPI Syntax:
            ```
            - BUS:LOWerthreshold:MATH1 {<NR3>|ECL|TTL}
            - BUS:LOWerthreshold:MATH1?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the lower threshold for the
              reference waveform, in volts.
            - ``ECL`` - ECL (-1.3 volts). Note that this setting is constrained, depending upon the
              vertical scale of the specified math waveform.
            - ``TTL`` - TTL (1.4 volts). Note that this setting is constrained, depending upon the
              vertical scale of the specified math waveform.
        """
        return self._math1


class BusBItemUsbSourceDplus(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:USB:SOUrce:DPLUs`` command.

    Description:
        - This command specifies the source for the USB D+ input. If you are using single-ended
          probes, you need to set the sources for both the D+ and D- inputs.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:USB:SOUrce:DPLUs?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:SOUrce:DPLUs?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:SOUrce:DPLUs value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:USB:SOUrce:DPLUs {CH<x>|D<x>}
        - BUS:B<x>:USB:SOUrce:DPLUs?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the source waveform for D+ input.
        - ``D<x>`` specifies a digital channel as the source waveform for D+ input. (Requires option
          3-MSO.).
    """


class BusBItemUsbSourceDminus(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:USB:SOUrce:DMINus`` command.

    Description:
        - This command specifies the source for the USB bus D- input. If you are using single-ended
          probes, you need to set the sources for both the D+ and D- inputs.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:USB:SOUrce:DMINus?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:SOUrce:DMINus?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:SOUrce:DMINus value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:USB:SOUrce:DMINus {CH<x>|D<x>}
        - BUS:B<x>:USB:SOUrce:DMINus?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the source waveform for the D- input.
        - ``D<x>`` specifies a digital channel as the source waveform for the D- input. (Requires
          option 3-MSO.).
    """


class BusBItemUsbSourceDifferential(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:USB:SOUrce:DIFFerential`` command.

    Description:
        - This command specifies the source waveform for the USB bus when using a differential
          probe.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:USB:SOUrce:DIFFerential?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:SOUrce:DIFFerential?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:USB:SOUrce:DIFFerential value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:USB:SOUrce:DIFFerential {CH<x>|MATH|REF<x>}
        - BUS:B<x>:USB:SOUrce:DIFFerential?
        ```

    Info:
        - ``CH<x>`` specifies an analog waveform as the source. This channel should have an attached
          differential probe.
        - ``MATH`` specifies the math waveform as the source.
        - ``REF<x>`` specifies a reference waveform as the source.
    """


class BusBItemUsbSource(SCPICmdRead):
    """The ``BUS:B<x>:USB:SOUrce`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:USB:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:SOUrce?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.differential``: The ``BUS:B<x>:USB:SOUrce:DIFFerential`` command.
        - ``.dminus``: The ``BUS:B<x>:USB:SOUrce:DMINus`` command.
        - ``.dplus``: The ``BUS:B<x>:USB:SOUrce:DPLUs`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._differential = BusBItemUsbSourceDifferential(
            device, f"{self._cmd_syntax}:DIFFerential"
        )
        self._dminus = BusBItemUsbSourceDminus(device, f"{self._cmd_syntax}:DMINus")
        self._dplus = BusBItemUsbSourceDplus(device, f"{self._cmd_syntax}:DPLUs")

    @property
    def differential(self) -> BusBItemUsbSourceDifferential:
        """Return the ``BUS:B<x>:USB:SOUrce:DIFFerential`` command.

        Description:
            - This command specifies the source waveform for the USB bus when using a differential
              probe.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:USB:SOUrce:DIFFerential?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:USB:SOUrce:DIFFerential?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:USB:SOUrce:DIFFerential value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:USB:SOUrce:DIFFerential {CH<x>|MATH|REF<x>}
            - BUS:B<x>:USB:SOUrce:DIFFerential?
            ```

        Info:
            - ``CH<x>`` specifies an analog waveform as the source. This channel should have an
              attached differential probe.
            - ``MATH`` specifies the math waveform as the source.
            - ``REF<x>`` specifies a reference waveform as the source.
        """
        return self._differential

    @property
    def dminus(self) -> BusBItemUsbSourceDminus:
        """Return the ``BUS:B<x>:USB:SOUrce:DMINus`` command.

        Description:
            - This command specifies the source for the USB bus D- input. If you are using
              single-ended probes, you need to set the sources for both the D+ and D- inputs.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:USB:SOUrce:DMINus?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:SOUrce:DMINus?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:SOUrce:DMINus value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:USB:SOUrce:DMINus {CH<x>|D<x>}
            - BUS:B<x>:USB:SOUrce:DMINus?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the source waveform for the D- input.
            - ``D<x>`` specifies a digital channel as the source waveform for the D- input.
              (Requires option 3-MSO.).
        """
        return self._dminus

    @property
    def dplus(self) -> BusBItemUsbSourceDplus:
        """Return the ``BUS:B<x>:USB:SOUrce:DPLUs`` command.

        Description:
            - This command specifies the source for the USB D+ input. If you are using single-ended
              probes, you need to set the sources for both the D+ and D- inputs.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:USB:SOUrce:DPLUs?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:SOUrce:DPLUs?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:SOUrce:DPLUs value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:USB:SOUrce:DPLUs {CH<x>|D<x>}
            - BUS:B<x>:USB:SOUrce:DPLUs?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the source waveform for D+ input.
            - ``D<x>`` specifies a digital channel as the source waveform for D+ input. (Requires
              option 3-MSO.).
        """
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
        - This command specifies the bit rate for the USB bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:USB:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:BITRate value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:USB:BITRate {LOW|FULL|HIGH}
        - BUS:B<x>:USB:BITRate?
        ```

    Info:
        - ``LOW`` indicates the bit rate is 1.5 Mbps.
        - ``FULL`` indicates the bit rate is 12 Mbps.
        - ``HIGH`` indicates the bit rate is 480 Mbps.
    """


class BusBItemUsb(SCPICmdRead):
    """The ``BUS:B<x>:USB`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:USB?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:USB:BITRate`` command.
        - ``.probe``: The ``BUS:B<x>:USB:PRObe`` command.
        - ``.source``: The ``BUS:B<x>:USB:SOUrce`` command tree.
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
            - This command specifies the bit rate for the USB bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:USB:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:BITRate?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:USB:BITRate {LOW|FULL|HIGH}
            - BUS:B<x>:USB:BITRate?
            ```

        Info:
            - ``LOW`` indicates the bit rate is 1.5 Mbps.
            - ``FULL`` indicates the bit rate is 12 Mbps.
            - ``HIGH`` indicates the bit rate is 480 Mbps.
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
        """Return the ``BUS:B<x>:USB:SOUrce`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:USB:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.differential``: The ``BUS:B<x>:USB:SOUrce:DIFFerential`` command.
            - ``.dminus``: The ``BUS:B<x>:USB:SOUrce:DMINus`` command.
            - ``.dplus``: The ``BUS:B<x>:USB:SOUrce:DPLUs`` command.
        """
        return self._source


class BusBItemType(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:TYPe`` command.

    Description:
        - This command specifies (or queries) the bus type. The supported bus types are dependent on
          the oscilloscope model and the installed application models. With the exception of the
          parallel bus, all bus types require installation of an application option.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:TYPe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:TYPe value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:TYPe {I2C|SPI|CAN|RS232C|PARallel|USB|LIN|FLEXRay|AUDio|ETHERnet|MIL1553B|ARINC429A}
        - BUS:B<x>:TYPe?
        ```

    Info:
        - ``I2C`` specifies the Inter-IC bus.
        - ``SPI`` specifies the Serial Peripheral Interface bus (not available on two-channel
          models).
        - ``CAN`` specifies the Controller Area Network bus.
        - ``RS232C`` specifies the RS-232C bus.
        - ``PARallel`` specifies the Parallel bus.
        - ``USB`` specifies the USB bus.
        - ``LIN`` specifies the LIN bus.
        - ``FLEXRay`` specifies the FLexRay bus.
        - ``AUDio`` specifies the audio bus.
        - ``ETHERnet`` specifies the Ethernet bus.
        - ``MIL1553B`` specifies the MIL-STD-1553 bus.
        - ``ARINC429A`` specifies the Aeronautical Radio INC (specification 429) bus.
    """  # noqa: E501


class BusBItemState(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:STATE`` command.

    Description:
        - This command specifies the on/off state of the bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:STATE value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:STATE {ON|OFF|<NR1>}
        - BUS:B<x>:STATE?
        ```

    Info:
        - ``ON`` or <NR1> ≠ 0 turns on the bus.
        - ``OFF`` or <NR1> = 0 turns off the bus.
    """


class BusBItemSpiSsSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:SS:SOUrce`` command.

    Description:
        - This command specifies the source waveform for the SPI bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SS:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SS:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SS:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:SS:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:SPI:SS:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the source waveform.
        - ``D<x>`` specifies a digital channel as the source waveform. (Requires option 3-MSO.).
    """


class BusBItemSpiSsPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:SS:POLarity`` command.

    Description:
        - This command specifies the polarity for the SPI bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SS:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SS:POLarity?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SS:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:SS:POLarity {LOW|HIGH}
        - BUS:B<x>:SPI:SS:POLarity?
        ```

    Info:
        - ``LOW`` specifies an active low polarity.
        - ``HIGH`` specifies an active high polarity.
    """


class BusBItemSpiSs(SCPICmdRead):
    """The ``BUS:B<x>:SPI:SS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SS?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SS?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:SPI:SS:POLarity`` command.
        - ``.source``: The ``BUS:B<x>:SPI:SS:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemSpiSsPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemSpiSsSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def polarity(self) -> BusBItemSpiSsPolarity:
        """Return the ``BUS:B<x>:SPI:SS:POLarity`` command.

        Description:
            - This command specifies the polarity for the SPI bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SS:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SS:POLarity?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SS:POLarity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:SS:POLarity {LOW|HIGH}
            - BUS:B<x>:SPI:SS:POLarity?
            ```

        Info:
            - ``LOW`` specifies an active low polarity.
            - ``HIGH`` specifies an active high polarity.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemSpiSsSource:
        """Return the ``BUS:B<x>:SPI:SS:SOUrce`` command.

        Description:
            - This command specifies the source waveform for the SPI bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SS:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SS:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SS:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:SS:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:SPI:SS:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the source waveform.
            - ``D<x>`` specifies a digital channel as the source waveform. (Requires option 3-MSO.).
        """
        return self._source


class BusBItemSpiSelectSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:SELect:SOUrce`` command.

    Description:
        - This command specifies the source waveform for the SPI bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:SELect:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:SPI:SELect:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the source waveform.
        - ``D<x>`` specifies a digital channel as the source waveform. (Requires option 3-MSO.).
    """


class BusBItemSpiSelectPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:SELect:POLarity`` command.

    Description:
        - This command specifies the polarity for the SPI bus.

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
        - ``LOW`` specifies an active low polarity.
        - ``HIGH`` specifies an active high polarity.
    """


class BusBItemSpiSelect(SCPICmdRead):
    """The ``BUS:B<x>:SPI:SELect`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect?`` query and raise
          an AssertionError if the returned value does not match ``value``.

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
            - This command specifies the polarity for the SPI bus.

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
            - ``LOW`` specifies an active low polarity.
            - ``HIGH`` specifies an active high polarity.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemSpiSelectSource:
        """Return the ``BUS:B<x>:SPI:SELect:SOUrce`` command.

        Description:
            - This command specifies the source waveform for the SPI bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:SELect:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:SPI:SELect:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the source waveform.
            - ``D<x>`` specifies a digital channel as the source waveform. (Requires option 3-MSO.).
        """
        return self._source


class BusBItemSpiSclkSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:SCLk:SOUrce`` command.

    Description:
        - This command specifies the SCLK source waveform for the SPI bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SCLk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SCLk:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SCLk:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:SCLk:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:SPI:SCLk:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the SCLK source waveform.
        - ``D<x>`` specifies a digital channel as the SCLK source waveform. (Requires option
          3-MSO.).
    """


class BusBItemSpiSclkPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:SCLk:POLarity`` command.

    Description:
        - This command specifies the SCLK polarity for the SPI bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SCLk:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SCLk:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SCLk:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:SCLk:POLarity {FALL|RISe}
        - BUS:B<x>:SPI:SCLk:POLarity?
        ```

    Info:
        - ``FALL`` specifies the SCLK polarity as falling edge.
        - ``RISe`` specifies the SCLK polarity as rising edge.
    """


class BusBItemSpiSclk(SCPICmdRead):
    """The ``BUS:B<x>:SPI:SCLk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SCLk?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SCLk?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:SPI:SCLk:POLarity`` command.
        - ``.source``: The ``BUS:B<x>:SPI:SCLk:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemSpiSclkPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemSpiSclkSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def polarity(self) -> BusBItemSpiSclkPolarity:
        """Return the ``BUS:B<x>:SPI:SCLk:POLarity`` command.

        Description:
            - This command specifies the SCLK polarity for the SPI bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SCLk:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SCLk:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SCLk:POLarity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:SCLk:POLarity {FALL|RISe}
            - BUS:B<x>:SPI:SCLk:POLarity?
            ```

        Info:
            - ``FALL`` specifies the SCLK polarity as falling edge.
            - ``RISe`` specifies the SCLK polarity as rising edge.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemSpiSclkSource:
        """Return the ``BUS:B<x>:SPI:SCLk:SOUrce`` command.

        Description:
            - This command specifies the SCLK source waveform for the SPI bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SCLk:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SCLk:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SCLk:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:SCLk:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:SPI:SCLk:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the SCLK source waveform.
            - ``D<x>`` specifies a digital channel as the SCLK source waveform. (Requires option
              3-MSO.).
        """
        return self._source


class BusBItemSpiIdletime(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:IDLETime`` command.

    Description:
        - This command sets or queries the SPI idle time for the specified bus. The bus is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:IDLETime?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:IDLETime?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:IDLETime value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:IDLETime <NR3>
        - BUS:B<x>:SPI:IDLETime?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` specifies the SPI idle time.
    """


class BusBItemSpiFraming(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:FRAMING`` command.

    Description:
        - This command specifies the type of framing to use for the SPI bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:FRAMING?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:FRAMING?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:FRAMING value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:FRAMING {SS|IDLEtime}
        - BUS:B<x>:SPI:FRAMING?
        ```
    """


class BusBItemSpiDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa:SIZe`` command.

    Description:
        - This command sets or queries the number of bits per word for the specified SPI bus. The
          bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:SIZe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATa:SIZe <NR1>
        - BUS:B<x>:SPI:DATa:SIZe?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR1>`` is the data size for the specified bus. The minimum value is 2 and maximum is
          32.
    """


class BusBItemSpiDataOutSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa:OUT:SOUrce`` command.

    Description:
        - This command specifies the MOSI source for the SPI bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:OUT:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:OUT:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:OUT:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATa:OUT:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:SPI:DATa:OUT:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the MOSI source waveform.
        - ``D<x>`` specifies a digital channel as the SPI MOSI source waveform. (Requires option
          3-MSO.).
    """


class BusBItemSpiDataOutPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa:OUT:POLarity`` command.

    Description:
        - This command specifies the MOSI polarity for the SPI bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:OUT:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:OUT:POLarity?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:OUT:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATa:OUT:POLarity {LOW|HIGH}
        - BUS:B<x>:SPI:DATa:OUT:POLarity?
        ```

    Info:
        - ``LOW`` specifies the active low polarity.
        - ``HIGH`` specifies the active high polarity.
    """


class BusBItemSpiDataOut(SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa:OUT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:OUT?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:OUT?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:SPI:DATa:OUT:POLarity`` command.
        - ``.source``: The ``BUS:B<x>:SPI:DATa:OUT:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemSpiDataOutPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemSpiDataOutSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def polarity(self) -> BusBItemSpiDataOutPolarity:
        """Return the ``BUS:B<x>:SPI:DATa:OUT:POLarity`` command.

        Description:
            - This command specifies the MOSI polarity for the SPI bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:OUT:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:OUT:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPI:DATa:OUT:POLarity value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATa:OUT:POLarity {LOW|HIGH}
            - BUS:B<x>:SPI:DATa:OUT:POLarity?
            ```

        Info:
            - ``LOW`` specifies the active low polarity.
            - ``HIGH`` specifies the active high polarity.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemSpiDataOutSource:
        """Return the ``BUS:B<x>:SPI:DATa:OUT:SOUrce`` command.

        Description:
            - This command specifies the MOSI source for the SPI bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:OUT:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:OUT:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPI:DATa:OUT:SOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATa:OUT:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:SPI:DATa:OUT:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the MOSI source waveform.
            - ``D<x>`` specifies a digital channel as the SPI MOSI source waveform. (Requires option
              3-MSO.).
        """
        return self._source


class BusBItemSpiDataMosiSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa:MOSI:SOUrce`` command.

    Description:
        - This command specifies the MOSI source for the SPI bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:MOSI:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:MOSI:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:MOSI:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATa:MOSI:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:SPI:DATa:MOSI:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the MOSI source waveform.
        - ``D<x>`` specifies a digital channel as the SPI MOSI source waveform. (Requires option
          3-MSO.).
    """


class BusBItemSpiDataMosiPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa:MOSI:POLarity`` command.

    Description:
        - This command specifies the MOSI polarity for the SPI bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:MOSI:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:MOSI:POLarity?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:MOSI:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATa:MOSI:POLarity {LOW|HIGH}
        - BUS:B<x>:SPI:DATa:MOSI:POLarity?
        ```

    Info:
        - ``LOW`` specifies the active low polarity.
        - ``HIGH`` specifies the active high polarity.
    """


class BusBItemSpiDataMosi(SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa:MOSI`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:MOSI?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:MOSI?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:SPI:DATa:MOSI:POLarity`` command.
        - ``.source``: The ``BUS:B<x>:SPI:DATa:MOSI:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemSpiDataMosiPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemSpiDataMosiSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def polarity(self) -> BusBItemSpiDataMosiPolarity:
        """Return the ``BUS:B<x>:SPI:DATa:MOSI:POLarity`` command.

        Description:
            - This command specifies the MOSI polarity for the SPI bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:MOSI:POLarity?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:MOSI:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPI:DATa:MOSI:POLarity value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATa:MOSI:POLarity {LOW|HIGH}
            - BUS:B<x>:SPI:DATa:MOSI:POLarity?
            ```

        Info:
            - ``LOW`` specifies the active low polarity.
            - ``HIGH`` specifies the active high polarity.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemSpiDataMosiSource:
        """Return the ``BUS:B<x>:SPI:DATa:MOSI:SOUrce`` command.

        Description:
            - This command specifies the MOSI source for the SPI bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:MOSI:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:MOSI:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPI:DATa:MOSI:SOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATa:MOSI:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:SPI:DATa:MOSI:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the MOSI source waveform.
            - ``D<x>`` specifies a digital channel as the SPI MOSI source waveform. (Requires option
              3-MSO.).
        """
        return self._source


class BusBItemSpiDataMisoSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa:MISO:SOUrce`` command.

    Description:
        - This command specifies the MISO source waveform for the SPI bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:MISO:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:MISO:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:MISO:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATa:MISO:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:SPI:DATa:MISO:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the MISO source waveform.
        - ``D<x>`` specifies a digital channel as the MISO source waveform. (Requires 3-MSO
          option.).
    """


class BusBItemSpiDataMisoPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa:MISO:POLarity`` command.

    Description:
        - This command specifies the MISO polarity for the SPI bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:MISO:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:MISO:POLarity?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:MISO:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATa:MISO:POLarity {LOW|HIGH}
        - BUS:B<x>:SPI:DATa:MISO:POLarity?
        ```

    Info:
        - ``LOW`` specifies an active low polarity.
        - ``HIGH`` specifies an active high polarity.
    """


class BusBItemSpiDataMiso(SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa:MISO`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:MISO?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:MISO?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:SPI:DATa:MISO:POLarity`` command.
        - ``.source``: The ``BUS:B<x>:SPI:DATa:MISO:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemSpiDataMisoPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemSpiDataMisoSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def polarity(self) -> BusBItemSpiDataMisoPolarity:
        """Return the ``BUS:B<x>:SPI:DATa:MISO:POLarity`` command.

        Description:
            - This command specifies the MISO polarity for the SPI bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:MISO:POLarity?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:MISO:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPI:DATa:MISO:POLarity value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATa:MISO:POLarity {LOW|HIGH}
            - BUS:B<x>:SPI:DATa:MISO:POLarity?
            ```

        Info:
            - ``LOW`` specifies an active low polarity.
            - ``HIGH`` specifies an active high polarity.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemSpiDataMisoSource:
        """Return the ``BUS:B<x>:SPI:DATa:MISO:SOUrce`` command.

        Description:
            - This command specifies the MISO source waveform for the SPI bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:MISO:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:MISO:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPI:DATa:MISO:SOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATa:MISO:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:SPI:DATa:MISO:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the MISO source waveform.
            - ``D<x>`` specifies a digital channel as the MISO source waveform. (Requires 3-MSO
              option.).
        """
        return self._source


class BusBItemSpiDataInSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa:IN:SOUrce`` command.

    Description:
        - This command specifies the MISO source waveform for the SPI bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:IN:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:IN:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:IN:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATa:IN:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:SPI:DATa:IN:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the MISO source waveform.
        - ``D<x>`` specifies a digital channel as the MISO source waveform. (Requires 3-MSO
          option.).
    """


class BusBItemSpiDataInPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa:IN:POLarity`` command.

    Description:
        - This command specifies the MISO polarity for the SPI bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:IN:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:IN:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:IN:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATa:IN:POLarity {LOW|HIGH}
        - BUS:B<x>:SPI:DATa:IN:POLarity?
        ```

    Info:
        - ``LOW`` specifies an active low polarity.
        - ``HIGH`` specifies an active high polarity.
    """


class BusBItemSpiDataIn(SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa:IN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:IN?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:IN?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:SPI:DATa:IN:POLarity`` command.
        - ``.source``: The ``BUS:B<x>:SPI:DATa:IN:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemSpiDataInPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemSpiDataInSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def polarity(self) -> BusBItemSpiDataInPolarity:
        """Return the ``BUS:B<x>:SPI:DATa:IN:POLarity`` command.

        Description:
            - This command specifies the MISO polarity for the SPI bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:IN:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:IN:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPI:DATa:IN:POLarity value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATa:IN:POLarity {LOW|HIGH}
            - BUS:B<x>:SPI:DATa:IN:POLarity?
            ```

        Info:
            - ``LOW`` specifies an active low polarity.
            - ``HIGH`` specifies an active high polarity.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemSpiDataInSource:
        """Return the ``BUS:B<x>:SPI:DATa:IN:SOUrce`` command.

        Description:
            - This command specifies the MISO source waveform for the SPI bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:IN:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:IN:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:IN:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATa:IN:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:SPI:DATa:IN:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the MISO source waveform.
            - ``D<x>`` specifies a digital channel as the MISO source waveform. (Requires 3-MSO
              option.).
        """
        return self._source


class BusBItemSpiData(SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.size``: The ``BUS:B<x>:SPI:DATa:SIZe`` command.
        - ``.in``: The ``BUS:B<x>:SPI:DATa:IN`` command tree.
        - ``.miso``: The ``BUS:B<x>:SPI:DATa:MISO`` command tree.
        - ``.out``: The ``BUS:B<x>:SPI:DATa:OUT`` command tree.
        - ``.mosi``: The ``BUS:B<x>:SPI:DATa:MOSI`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._size = BusBItemSpiDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._in = BusBItemSpiDataIn(device, f"{self._cmd_syntax}:IN")
        self._miso = BusBItemSpiDataMiso(device, f"{self._cmd_syntax}:MISO")
        self._out = BusBItemSpiDataOut(device, f"{self._cmd_syntax}:OUT")
        self._mosi = BusBItemSpiDataMosi(device, f"{self._cmd_syntax}:MOSI")

    @property
    def size(self) -> BusBItemSpiDataSize:
        """Return the ``BUS:B<x>:SPI:DATa:SIZe`` command.

        Description:
            - This command sets or queries the number of bits per word for the specified SPI bus.
              The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:SIZe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:SIZe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:SIZe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATa:SIZe <NR1>
            - BUS:B<x>:SPI:DATa:SIZe?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR1>`` is the data size for the specified bus. The minimum value is 2 and maximum
              is 32.
        """
        return self._size

    @property
    def in_(self) -> BusBItemSpiDataIn:
        """Return the ``BUS:B<x>:SPI:DATa:IN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:IN?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:IN?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:SPI:DATa:IN:POLarity`` command.
            - ``.source``: The ``BUS:B<x>:SPI:DATa:IN:SOUrce`` command.
        """
        return self._in

    @property
    def miso(self) -> BusBItemSpiDataMiso:
        """Return the ``BUS:B<x>:SPI:DATa:MISO`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:MISO?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:MISO?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:SPI:DATa:MISO:POLarity`` command.
            - ``.source``: The ``BUS:B<x>:SPI:DATa:MISO:SOUrce`` command.
        """
        return self._miso

    @property
    def out(self) -> BusBItemSpiDataOut:
        """Return the ``BUS:B<x>:SPI:DATa:OUT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:OUT?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:OUT?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:SPI:DATa:OUT:POLarity`` command.
            - ``.source``: The ``BUS:B<x>:SPI:DATa:OUT:SOUrce`` command.
        """
        return self._out

    @property
    def mosi(self) -> BusBItemSpiDataMosi:
        """Return the ``BUS:B<x>:SPI:DATa:MOSI`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:MOSI?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:MOSI?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:SPI:DATa:MOSI:POLarity`` command.
            - ``.source``: The ``BUS:B<x>:SPI:DATa:MOSI:SOUrce`` command.
        """
        return self._mosi


class BusBItemSpiClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:CLOCk:SOUrce`` command.

    Description:
        - This command specifies the SCLK source waveform for the SPI bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:CLOCk:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:SPI:CLOCk:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the SCLK source waveform.
        - ``D<x>`` specifies a digital channel as the SCLK source waveform. (Requires option
          3-MSO.).
    """


class BusBItemSpiClockPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:CLOCk:POLarity`` command.

    Description:
        - This command specifies the SCLK polarity for the SPI bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCk:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:CLOCk:POLarity {FALL|RISe}
        - BUS:B<x>:SPI:CLOCk:POLarity?
        ```

    Info:
        - ``FALL`` specifies the SCLK polarity as falling edge.
        - ``RISe`` specifies the SCLK polarity as rising edge.
    """


class BusBItemSpiClock(SCPICmdRead):
    """The ``BUS:B<x>:SPI:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCk?`` query and raise
          an AssertionError if the returned value does not match ``value``.

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
            - This command specifies the SCLK polarity for the SPI bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCk:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:POLarity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:CLOCk:POLarity {FALL|RISe}
            - BUS:B<x>:SPI:CLOCk:POLarity?
            ```

        Info:
            - ``FALL`` specifies the SCLK polarity as falling edge.
            - ``RISe`` specifies the SCLK polarity as rising edge.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemSpiClockSource:
        """Return the ``BUS:B<x>:SPI:CLOCk:SOUrce`` command.

        Description:
            - This command specifies the SCLK source waveform for the SPI bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCk:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:CLOCk:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:SPI:CLOCk:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the SCLK source waveform.
            - ``D<x>`` specifies a digital channel as the SCLK source waveform. (Requires option
              3-MSO.).
        """
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


#  pylint: disable=too-many-instance-attributes
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
        - ``.data``: The ``BUS:B<x>:SPI:DATa`` command tree.
        - ``.framing``: The ``BUS:B<x>:SPI:FRAMING`` command.
        - ``.idletime``: The ``BUS:B<x>:SPI:IDLETime`` command.
        - ``.clock``: The ``BUS:B<x>:SPI:CLOCk`` command tree.
        - ``.sclk``: The ``BUS:B<x>:SPI:SCLk`` command tree.
        - ``.select``: The ``BUS:B<x>:SPI:SELect`` command tree.
        - ``.ss``: The ``BUS:B<x>:SPI:SS`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitorder = BusBItemSpiBitorder(device, f"{self._cmd_syntax}:BITOrder")
        self._data = BusBItemSpiData(device, f"{self._cmd_syntax}:DATa")
        self._framing = BusBItemSpiFraming(device, f"{self._cmd_syntax}:FRAMING")
        self._idletime = BusBItemSpiIdletime(device, f"{self._cmd_syntax}:IDLETime")
        self._clock = BusBItemSpiClock(device, f"{self._cmd_syntax}:CLOCk")
        self._sclk = BusBItemSpiSclk(device, f"{self._cmd_syntax}:SCLk")
        self._select = BusBItemSpiSelect(device, f"{self._cmd_syntax}:SELect")
        self._ss = BusBItemSpiSs(device, f"{self._cmd_syntax}:SS")

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
    def data(self) -> BusBItemSpiData:
        """Return the ``BUS:B<x>:SPI:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.size``: The ``BUS:B<x>:SPI:DATa:SIZe`` command.
            - ``.in``: The ``BUS:B<x>:SPI:DATa:IN`` command tree.
            - ``.miso``: The ``BUS:B<x>:SPI:DATa:MISO`` command tree.
            - ``.out``: The ``BUS:B<x>:SPI:DATa:OUT`` command tree.
            - ``.mosi``: The ``BUS:B<x>:SPI:DATa:MOSI`` command tree.
        """
        return self._data

    @property
    def framing(self) -> BusBItemSpiFraming:
        """Return the ``BUS:B<x>:SPI:FRAMING`` command.

        Description:
            - This command specifies the type of framing to use for the SPI bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:FRAMING?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:FRAMING?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:FRAMING value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:FRAMING {SS|IDLEtime}
            - BUS:B<x>:SPI:FRAMING?
            ```
        """
        return self._framing

    @property
    def idletime(self) -> BusBItemSpiIdletime:
        """Return the ``BUS:B<x>:SPI:IDLETime`` command.

        Description:
            - This command sets or queries the SPI idle time for the specified bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:IDLETime?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:IDLETime?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:IDLETime value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:IDLETime <NR3>
            - BUS:B<x>:SPI:IDLETime?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` specifies the SPI idle time.
        """
        return self._idletime

    @property
    def clock(self) -> BusBItemSpiClock:
        """Return the ``BUS:B<x>:SPI:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCk?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:SPI:CLOCk:POLarity`` command.
            - ``.source``: The ``BUS:B<x>:SPI:CLOCk:SOUrce`` command.
        """
        return self._clock

    @property
    def sclk(self) -> BusBItemSpiSclk:
        """Return the ``BUS:B<x>:SPI:SCLk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SCLk?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SCLk?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:SPI:SCLk:POLarity`` command.
            - ``.source``: The ``BUS:B<x>:SPI:SCLk:SOUrce`` command.
        """
        return self._sclk

    @property
    def select(self) -> BusBItemSpiSelect:
        """Return the ``BUS:B<x>:SPI:SELect`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:SPI:SELect:POLarity`` command.
            - ``.source``: The ``BUS:B<x>:SPI:SELect:SOUrce`` command.
        """
        return self._select

    @property
    def ss(self) -> BusBItemSpiSs:
        """Return the ``BUS:B<x>:SPI:SS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SS?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SS?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:SPI:SS:POLarity`` command.
            - ``.source``: The ``BUS:B<x>:SPI:SS:SOUrce`` command.
        """
        return self._ss


class BusBItemSentTicktolerance(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SENT:TICKTOLerance`` command.

    Description:
        - This command sets or queries the SENT bus Tick Tolerance percent parameter for the
          specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:TICKTOLerance?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:TICKTOLerance?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:TICKTOLerance value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SENT:TICKTOLerance <NR3>
        - BUS:B<x>:SENT:TICKTOLerance?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` is the tick tolerance percentage.
    """


class BusBItemSentTicktime(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SENT:TICKTIME`` command.

    Description:
        - This command sets or queries the SENT bus Clock Tick parameter for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:TICKTIME?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:TICKTIME?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:TICKTIME value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SENT:TICKTIME <NR3>
        - BUS:B<x>:SENT:TICKTIME?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` is the SENT clock tick time, in seconds.
    """


class BusBItemSentSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SENT:SOUrce`` command.

    Description:
        - This command sets or queries the SENT DATA source for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SENT:SOUrce {CH<x>|D<x>|MATH|REF<x>}
        - BUS:B<x>:SENT:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``CH<x>`` specifies an analog channel as the source waveform for the SENT bus.
        - ``D<x>`` specifies a digital channel as the source waveform for the specified SENT bus.
        - ``MATH`` specifies a math waveform as the source waveform for the SENT bus.
        - ``REF<x>`` specifies a reference waveform as the source waveform for the SENT bus.
    """


class BusBItemSentSlow(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SENT:SLOW`` command.

    Description:
        - This command sets or queries the SENT slow channel configuration for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:SLOW?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:SLOW?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:SLOW value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SENT:SLOW {NOne|ENHANCED4|ENHANCED8|SHOrt}
        - BUS:B<x>:SENT:SLOW?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``NOne`` specifies no slow channel configured.
        - ``ENHANCED4`` specifies Enhanced 4 slow channel configuration.
        - ``ENHANCED8`` specifies Enhanced 8 slow channel configuration.
        - ``SHOrt`` specifies short slow channel configuration.
    """


class BusBItemSentPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SENT:POLARITY`` command.

    Description:
        - This command sets or queries SENT Idle State signal polarity for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:POLARITY?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:POLARITY?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:POLARITY value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SENT:POLARITY {INVerted|NORmal}
        - BUS:B<x>:SENT:POLARITY?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``INVerted`` specifies inverted polarity.
        - ``NORmal`` specifies normal polarity.
    """


class BusBItemSentPausepulse(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SENT:PAUSEPULSe`` command.

    Description:
        - This command sets or queries SENT pause pulse for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:PAUSEPULSe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:PAUSEPULSe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:PAUSEPULSe value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SENT:PAUSEPULSe {NO|YES}
        - BUS:B<x>:SENT:PAUSEPULSe?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``NO`` specifies no pause pulse.
        - ``YES`` specifies a pause pulse is used.
    """


class BusBItemSentNumchannel(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SENT:NUMCHANnel`` command.

    Description:
        - This command sets or queries SENT fast data channels for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:NUMCHANnel?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:NUMCHANnel?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:NUMCHANnel value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SENT:NUMCHANnel {ONE|TWO}
        - BUS:B<x>:SENT:NUMCHANnel?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``ONE`` specifies a SENT bus with one fast channel.
        - ``TWO`` specifies a SENT bus with two fast channels.
    """


class BusBItemSentNibblecount(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SENT:NIBBLECount`` command.

    Description:
        - This command sets or queries SENT data nibbles for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:NIBBLECount?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:NIBBLECount?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:NIBBLECount value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SENT:NIBBLECount {THREE|FOUR|SIX}
        - BUS:B<x>:SENT:NIBBLECount?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``THREE`` specifies regular data with 3 nibbles.
        - ``FOUR`` specifies regular data with 4nibbles.
        - ``SIX`` specifies regular data with 6nibbles.
    """


class BusBItemSentChanwidth(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SENT:CHANWidth`` command.

    Description:
        - This command sets or queries SENT fast channel bit widths for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:CHANWidth?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:CHANWidth?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:CHANWidth value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SENT:CHANWidth {TWELVEtwelve|FOURTEENten|SIXTEENeight}
        - BUS:B<x>:SENT:CHANWidth?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``TWELVEtwelve`` sets both Fast Channel 1 and Fast Channel 2 to12 bits wide.
        - ``FOURTEENten`` sets Fast Channel 1 to 14 bits and Fast Channel 2 to 10 bits.
        - ``SIXTEENeight`` sets Fast Channel 1 to 16 bits and Fast Channel 2 to eight bits.
    """


#  pylint: disable=too-many-instance-attributes
class BusBItemSent(SCPICmdRead):
    """The ``BUS:B<x>:SENT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SENT?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.chanwidth``: The ``BUS:B<x>:SENT:CHANWidth`` command.
        - ``.nibblecount``: The ``BUS:B<x>:SENT:NIBBLECount`` command.
        - ``.numchannel``: The ``BUS:B<x>:SENT:NUMCHANnel`` command.
        - ``.pausepulse``: The ``BUS:B<x>:SENT:PAUSEPULSe`` command.
        - ``.polarity``: The ``BUS:B<x>:SENT:POLARITY`` command.
        - ``.slow``: The ``BUS:B<x>:SENT:SLOW`` command.
        - ``.source``: The ``BUS:B<x>:SENT:SOUrce`` command.
        - ``.ticktime``: The ``BUS:B<x>:SENT:TICKTIME`` command.
        - ``.ticktolerance``: The ``BUS:B<x>:SENT:TICKTOLerance`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._chanwidth = BusBItemSentChanwidth(device, f"{self._cmd_syntax}:CHANWidth")
        self._nibblecount = BusBItemSentNibblecount(device, f"{self._cmd_syntax}:NIBBLECount")
        self._numchannel = BusBItemSentNumchannel(device, f"{self._cmd_syntax}:NUMCHANnel")
        self._pausepulse = BusBItemSentPausepulse(device, f"{self._cmd_syntax}:PAUSEPULSe")
        self._polarity = BusBItemSentPolarity(device, f"{self._cmd_syntax}:POLARITY")
        self._slow = BusBItemSentSlow(device, f"{self._cmd_syntax}:SLOW")
        self._source = BusBItemSentSource(device, f"{self._cmd_syntax}:SOUrce")
        self._ticktime = BusBItemSentTicktime(device, f"{self._cmd_syntax}:TICKTIME")
        self._ticktolerance = BusBItemSentTicktolerance(device, f"{self._cmd_syntax}:TICKTOLerance")

    @property
    def chanwidth(self) -> BusBItemSentChanwidth:
        """Return the ``BUS:B<x>:SENT:CHANWidth`` command.

        Description:
            - This command sets or queries SENT fast channel bit widths for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:CHANWidth?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:CHANWidth?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:CHANWidth value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SENT:CHANWidth {TWELVEtwelve|FOURTEENten|SIXTEENeight}
            - BUS:B<x>:SENT:CHANWidth?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``TWELVEtwelve`` sets both Fast Channel 1 and Fast Channel 2 to12 bits wide.
            - ``FOURTEENten`` sets Fast Channel 1 to 14 bits and Fast Channel 2 to 10 bits.
            - ``SIXTEENeight`` sets Fast Channel 1 to 16 bits and Fast Channel 2 to eight bits.
        """
        return self._chanwidth

    @property
    def nibblecount(self) -> BusBItemSentNibblecount:
        """Return the ``BUS:B<x>:SENT:NIBBLECount`` command.

        Description:
            - This command sets or queries SENT data nibbles for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:NIBBLECount?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:NIBBLECount?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:NIBBLECount value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SENT:NIBBLECount {THREE|FOUR|SIX}
            - BUS:B<x>:SENT:NIBBLECount?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``THREE`` specifies regular data with 3 nibbles.
            - ``FOUR`` specifies regular data with 4nibbles.
            - ``SIX`` specifies regular data with 6nibbles.
        """
        return self._nibblecount

    @property
    def numchannel(self) -> BusBItemSentNumchannel:
        """Return the ``BUS:B<x>:SENT:NUMCHANnel`` command.

        Description:
            - This command sets or queries SENT fast data channels for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:NUMCHANnel?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:NUMCHANnel?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:NUMCHANnel value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SENT:NUMCHANnel {ONE|TWO}
            - BUS:B<x>:SENT:NUMCHANnel?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``ONE`` specifies a SENT bus with one fast channel.
            - ``TWO`` specifies a SENT bus with two fast channels.
        """
        return self._numchannel

    @property
    def pausepulse(self) -> BusBItemSentPausepulse:
        """Return the ``BUS:B<x>:SENT:PAUSEPULSe`` command.

        Description:
            - This command sets or queries SENT pause pulse for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:PAUSEPULSe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:PAUSEPULSe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:PAUSEPULSe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SENT:PAUSEPULSe {NO|YES}
            - BUS:B<x>:SENT:PAUSEPULSe?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``NO`` specifies no pause pulse.
            - ``YES`` specifies a pause pulse is used.
        """
        return self._pausepulse

    @property
    def polarity(self) -> BusBItemSentPolarity:
        """Return the ``BUS:B<x>:SENT:POLARITY`` command.

        Description:
            - This command sets or queries SENT Idle State signal polarity for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:POLARITY?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:POLARITY?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:POLARITY value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SENT:POLARITY {INVerted|NORmal}
            - BUS:B<x>:SENT:POLARITY?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``INVerted`` specifies inverted polarity.
            - ``NORmal`` specifies normal polarity.
        """
        return self._polarity

    @property
    def slow(self) -> BusBItemSentSlow:
        """Return the ``BUS:B<x>:SENT:SLOW`` command.

        Description:
            - This command sets or queries the SENT slow channel configuration for the specified
              bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:SLOW?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:SLOW?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:SLOW value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SENT:SLOW {NOne|ENHANCED4|ENHANCED8|SHOrt}
            - BUS:B<x>:SENT:SLOW?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``NOne`` specifies no slow channel configured.
            - ``ENHANCED4`` specifies Enhanced 4 slow channel configuration.
            - ``ENHANCED8`` specifies Enhanced 8 slow channel configuration.
            - ``SHOrt`` specifies short slow channel configuration.
        """
        return self._slow

    @property
    def source(self) -> BusBItemSentSource:
        """Return the ``BUS:B<x>:SENT:SOUrce`` command.

        Description:
            - This command sets or queries the SENT DATA source for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SENT:SOUrce {CH<x>|D<x>|MATH|REF<x>}
            - BUS:B<x>:SENT:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``CH<x>`` specifies an analog channel as the source waveform for the SENT bus.
            - ``D<x>`` specifies a digital channel as the source waveform for the specified SENT
              bus.
            - ``MATH`` specifies a math waveform as the source waveform for the SENT bus.
            - ``REF<x>`` specifies a reference waveform as the source waveform for the SENT bus.
        """
        return self._source

    @property
    def ticktime(self) -> BusBItemSentTicktime:
        """Return the ``BUS:B<x>:SENT:TICKTIME`` command.

        Description:
            - This command sets or queries the SENT bus Clock Tick parameter for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:TICKTIME?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:TICKTIME?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:TICKTIME value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SENT:TICKTIME <NR3>
            - BUS:B<x>:SENT:TICKTIME?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` is the SENT clock tick time, in seconds.
        """
        return self._ticktime

    @property
    def ticktolerance(self) -> BusBItemSentTicktolerance:
        """Return the ``BUS:B<x>:SENT:TICKTOLerance`` command.

        Description:
            - This command sets or queries the SENT bus Tick Tolerance percent parameter for the
              specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:TICKTOLerance?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:TICKTOLerance?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:TICKTOLerance value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SENT:TICKTOLerance <NR3>
            - BUS:B<x>:SENT:TICKTOLerance?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` is the tick tolerance percentage.
        """
        return self._ticktolerance


class BusBItemRs232cTxSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:TX:SOUrce`` command.

    Description:
        - This command specifies the TX source waveform for the RS-232 bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:TX:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:TX:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:TX:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:TX:SOUrce {CH<x>|D<x>|Off}
        - BUS:B<x>:RS232C:TX:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the TX source waveform.
        - ``D<x>`` specifies a digital channel as the TX source waveform. (Requires option 3-MSO.).
        - ``Off`` sets the specified bus input to off.
    """


class BusBItemRs232cTx(SCPICmdRead):
    """The ``BUS:B<x>:RS232C:TX`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:TX?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:TX?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``BUS:B<x>:RS232C:TX:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemRs232cTxSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def source(self) -> BusBItemRs232cTxSource:
        """Return the ``BUS:B<x>:RS232C:TX:SOUrce`` command.

        Description:
            - This command specifies the TX source waveform for the RS-232 bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:TX:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:TX:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:TX:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:TX:SOUrce {CH<x>|D<x>|Off}
            - BUS:B<x>:RS232C:TX:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the TX source waveform.
            - ``D<x>`` specifies a digital channel as the TX source waveform. (Requires option
              3-MSO.).
            - ``Off`` sets the specified bus input to off.
        """
        return self._source


class BusBItemRs232cRxSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:RX:SOUrce`` command.

    Description:
        - This command specifies the RX source waveform for the RS-232 bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:RX:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:RX:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:RX:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:RX:SOUrce {CH<x>|D<x>|Off}
        - BUS:B<x>:RS232C:RX:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the RX source waveform.
        - ``D<x>`` specifies a digital channel as the RX source waveform. (Requires option 3-MSO.).
        - ``Off`` sets the specified bus input to off.
    """


class BusBItemRs232cRx(SCPICmdRead):
    """The ``BUS:B<x>:RS232C:RX`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:RX?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:RX?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``BUS:B<x>:RS232C:RX:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemRs232cRxSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def source(self) -> BusBItemRs232cRxSource:
        """Return the ``BUS:B<x>:RS232C:RX:SOUrce`` command.

        Description:
            - This command specifies the RX source waveform for the RS-232 bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:RX:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:RX:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:RX:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:RX:SOUrce {CH<x>|D<x>|Off}
            - BUS:B<x>:RS232C:RX:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the RX source waveform.
            - ``D<x>`` specifies a digital channel as the RX source waveform. (Requires option
              3-MSO.).
            - ``Off`` sets the specified bus input to off.
        """
        return self._source


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
        - This command specifies the delimiting value for a packet on the RS-232 bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:DELIMiter?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:DELIMiter?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:DELIMiter value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:DELIMiter {NULl|LF|CR|SPace|XFF}
        - BUS:B<x>:RS232C:DELIMiter?
        ```

    Info:
        - ``NULl`` specifies 0x00.
        - ``LF`` specifies 0x0A.
        - ``CR`` specifies 0x0D.
        - ``XFF`` specifies 0xFF.
    """


class BusBItemRs232cDatabits(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:DATABits`` command.

    Description:
        - This command sets or queries the RS-232C data width for bus<x>, where the bus number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:DATABits?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:DATABits?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:DATABits value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:DATABits {7|8|9}
        - BUS:B<x>:RS232C:DATABits?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``7`` specifies the number of bits as 7 in the RS-232C data frame.
        - ``8`` specifies the number of bits as 8 in the RS-232C data frame.
        - ``9`` specifies the number of bits as 9 in the RS-232C data frame.
    """


class BusBItemRs232cBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:BITRate`` command.

    Description:
        - This command specifies the bit rate for the RS-232 bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:BITRate value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:BITRate <NR1>
        - BUS:B<x>:RS232C:BITRate?
        ```

    Info:
        - ``<NR1>`` is the bit rate in bits-per-second. You can enter any positive integer, and the
          instrument will coerce the value to the closest supported bit rate.
    """


#  pylint: disable=too-many-instance-attributes
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
        - ``.rx``: The ``BUS:B<x>:RS232C:RX`` command tree.
        - ``.tx``: The ``BUS:B<x>:RS232C:TX`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemRs232cBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._databits = BusBItemRs232cDatabits(device, f"{self._cmd_syntax}:DATABits")
        self._delimiter = BusBItemRs232cDelimiter(device, f"{self._cmd_syntax}:DELIMiter")
        self._displaymode = BusBItemRs232cDisplaymode(device, f"{self._cmd_syntax}:DISplaymode")
        self._parity = BusBItemRs232cParity(device, f"{self._cmd_syntax}:PARity")
        self._polarity = BusBItemRs232cPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._rx = BusBItemRs232cRx(device, f"{self._cmd_syntax}:RX")
        self._tx = BusBItemRs232cTx(device, f"{self._cmd_syntax}:TX")

    @property
    def bitrate(self) -> BusBItemRs232cBitrate:
        """Return the ``BUS:B<x>:RS232C:BITRate`` command.

        Description:
            - This command specifies the bit rate for the RS-232 bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:BITRate?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:BITRate <NR1>
            - BUS:B<x>:RS232C:BITRate?
            ```

        Info:
            - ``<NR1>`` is the bit rate in bits-per-second. You can enter any positive integer, and
              the instrument will coerce the value to the closest supported bit rate.
        """
        return self._bitrate

    @property
    def databits(self) -> BusBItemRs232cDatabits:
        """Return the ``BUS:B<x>:RS232C:DATABits`` command.

        Description:
            - This command sets or queries the RS-232C data width for bus<x>, where the bus number
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:DATABits?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:DATABits?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:DATABits value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:DATABits {7|8|9}
            - BUS:B<x>:RS232C:DATABits?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``7`` specifies the number of bits as 7 in the RS-232C data frame.
            - ``8`` specifies the number of bits as 8 in the RS-232C data frame.
            - ``9`` specifies the number of bits as 9 in the RS-232C data frame.
        """
        return self._databits

    @property
    def delimiter(self) -> BusBItemRs232cDelimiter:
        """Return the ``BUS:B<x>:RS232C:DELIMiter`` command.

        Description:
            - This command specifies the delimiting value for a packet on the RS-232 bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:DELIMiter?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:DELIMiter?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:DELIMiter value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:DELIMiter {NULl|LF|CR|SPace|XFF}
            - BUS:B<x>:RS232C:DELIMiter?
            ```

        Info:
            - ``NULl`` specifies 0x00.
            - ``LF`` specifies 0x0A.
            - ``CR`` specifies 0x0D.
            - ``XFF`` specifies 0xFF.
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
    def rx(self) -> BusBItemRs232cRx:
        """Return the ``BUS:B<x>:RS232C:RX`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:RX?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:RX?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:RS232C:RX:SOUrce`` command.
        """
        return self._rx

    @property
    def tx(self) -> BusBItemRs232cTx:
        """Return the ``BUS:B<x>:RS232C:TX`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:TX?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:TX?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:RS232C:TX:SOUrce`` command.
        """
        return self._tx


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


class BusBItemParallelWidth(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:WIDth`` command.

    Description:
        - This command specifies the number of bits to use for the width of the parallel bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:WIDth?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:WIDth?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PARallel:WIDth value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:WIDth <NR1>
        - BUS:B<x>:PARallel:WIDth?
        ```

    Info:
        - ``<NR1>`` is the number of bits.
    """


class BusBItemParallelClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:CLOCk:SOUrce`` command.

    Description:
        - Specifies the clock source waveform for the parallel bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk:SOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:CLOCk:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:PARallel:CLOCk:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel to use the clock source waveform.
        - ``D<x>`` specifies a digital channels the clock source waveform. (Requires option 3-MSO.).
    """


class BusBItemParallelClockIsclocked(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:CLOCk:ISCLOCKed`` command.

    Description:
        - Specifies the state of the clock function for the parallel bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCk:ISCLOCKed?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk:ISCLOCKed?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:PARallel:CLOCk:ISCLOCKed value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:CLOCk:ISCLOCKed {YES|NO}
        - BUS:B<x>:PARallel:CLOCk:ISCLOCKed?
        ```

    Info:
        - ``YES`` specifes that the parallel bus is clocked.
        - ``NO`` specifes that the parallel bus is not clocked.
    """


class BusBItemParallelClockEdge(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:CLOCk:EDGE`` command.

    Description:
        - Specifies the clock edge for the parallel bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCk:EDGE?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk:EDGE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk:EDGE value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:CLOCk:EDGE {EITher|RISing|FALling}
        - BUS:B<x>:PARallel:CLOCk:EDGE?
        ```

    Info:
        - ``EIther`` specifies either edge as the clock edge.
        - ``RISing`` specifies the rising edge as the clock edge.
        - ``FALling`` specifies the falling edge as the clock edge.
    """


class BusBItemParallelClock(SCPICmdRead):
    """The ``BUS:B<x>:PARallel:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.edge``: The ``BUS:B<x>:PARallel:CLOCk:EDGE`` command.
        - ``.isclocked``: The ``BUS:B<x>:PARallel:CLOCk:ISCLOCKed`` command.
        - ``.source``: The ``BUS:B<x>:PARallel:CLOCk:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._edge = BusBItemParallelClockEdge(device, f"{self._cmd_syntax}:EDGE")
        self._isclocked = BusBItemParallelClockIsclocked(device, f"{self._cmd_syntax}:ISCLOCKed")
        self._source = BusBItemParallelClockSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def edge(self) -> BusBItemParallelClockEdge:
        """Return the ``BUS:B<x>:PARallel:CLOCk:EDGE`` command.

        Description:
            - Specifies the clock edge for the parallel bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCk:EDGE?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk:EDGE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PARallel:CLOCk:EDGE value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:CLOCk:EDGE {EITher|RISing|FALling}
            - BUS:B<x>:PARallel:CLOCk:EDGE?
            ```

        Info:
            - ``EIther`` specifies either edge as the clock edge.
            - ``RISing`` specifies the rising edge as the clock edge.
            - ``FALling`` specifies the falling edge as the clock edge.
        """
        return self._edge

    @property
    def isclocked(self) -> BusBItemParallelClockIsclocked:
        """Return the ``BUS:B<x>:PARallel:CLOCk:ISCLOCKed`` command.

        Description:
            - Specifies the state of the clock function for the parallel bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCk:ISCLOCKed?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:PARallel:CLOCk:ISCLOCKed?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PARallel:CLOCk:ISCLOCKed value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:CLOCk:ISCLOCKed {YES|NO}
            - BUS:B<x>:PARallel:CLOCk:ISCLOCKed?
            ```

        Info:
            - ``YES`` specifes that the parallel bus is clocked.
            - ``NO`` specifes that the parallel bus is not clocked.
        """
        return self._isclocked

    @property
    def source(self) -> BusBItemParallelClockSource:
        """Return the ``BUS:B<x>:PARallel:CLOCk:SOUrce`` command.

        Description:
            - Specifies the clock source waveform for the parallel bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCk:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PARallel:CLOCk:SOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:CLOCk:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:PARallel:CLOCk:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel to use the clock source waveform.
            - ``D<x>`` specifies a digital channels the clock source waveform. (Requires option
              3-MSO.).
        """
        return self._source


class BusBItemParallelBitItemSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:BIT<x>:SOUrce`` command.

    Description:
        - Specifies the bit source waveform for the parallel bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:BIT<x>:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:BIT<x>:SOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PARallel:BIT<x>:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:BIT<x>:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:PARallel:BIT<x>:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the bit source waveform.
        - ``D<x>`` specifies a digital channel as the bit source waveform. (Requires option 3-MSO.).
    """


class BusBItemParallelBitItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:BIT<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:BIT<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:BIT<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``BUS:B<x>:PARallel:BIT<x>:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemParallelBitItemSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def source(self) -> BusBItemParallelBitItemSource:
        """Return the ``BUS:B<x>:PARallel:BIT<x>:SOUrce`` command.

        Description:
            - Specifies the bit source waveform for the parallel bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:BIT<x>:SOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:BIT<x>:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PARallel:BIT<x>:SOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:BIT<x>:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:PARallel:BIT<x>:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the bit source waveform.
            - ``D<x>`` specifies a digital channel as the bit source waveform. (Requires option
              3-MSO.).
        """
        return self._source


class BusBItemParallel(SCPICmdRead):
    """The ``BUS:B<x>:PARallel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bit``: The ``BUS:B<x>:PARallel:BIT<x>`` command tree.
        - ``.clock``: The ``BUS:B<x>:PARallel:CLOCk`` command tree.
        - ``.width``: The ``BUS:B<x>:PARallel:WIDth`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bit: Dict[int, BusBItemParallelBitItem] = DefaultDictPassKeyToFactory(
            lambda x: BusBItemParallelBitItem(device, f"{self._cmd_syntax}:BIT{x}")
        )
        self._clock = BusBItemParallelClock(device, f"{self._cmd_syntax}:CLOCk")
        self._width = BusBItemParallelWidth(device, f"{self._cmd_syntax}:WIDth")

    @property
    def bit(self) -> Dict[int, BusBItemParallelBitItem]:
        """Return the ``BUS:B<x>:PARallel:BIT<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:BIT<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:BIT<x>?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:PARallel:BIT<x>:SOUrce`` command.
        """
        return self._bit

    @property
    def clock(self) -> BusBItemParallelClock:
        """Return the ``BUS:B<x>:PARallel:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.edge``: The ``BUS:B<x>:PARallel:CLOCk:EDGE`` command.
            - ``.isclocked``: The ``BUS:B<x>:PARallel:CLOCk:ISCLOCKed`` command.
            - ``.source``: The ``BUS:B<x>:PARallel:CLOCk:SOUrce`` command.
        """
        return self._clock

    @property
    def width(self) -> BusBItemParallelWidth:
        """Return the ``BUS:B<x>:PARallel:WIDth`` command.

        Description:
            - This command specifies the number of bits to use for the width of the parallel bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:WIDth?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:WIDth?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:PARallel:WIDth value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:WIDth <NR1>
            - BUS:B<x>:PARallel:WIDth?
            ```

        Info:
            - ``<NR1>`` is the number of bits.
        """
        return self._width


class BusBItemMil1553bSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MIL1553B:SOUrce`` command.

    Description:
        - This command specifies the source for differential input for the MIL-STD-1553 bus. The
          supported source waveforms are channels 1-4, math waveform, and reference waveforms 1-4.
          The default is channel 1.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIL1553B:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIL1553B:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:MIL1553B:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MIL1553B:SOUrce {CH<x>|MATH|REF<x>}
        - BUS:B<x>:MIL1553B:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the source for differential input.
        - ``MATH`` specifies the math waveform as the MIL-STD-1553 bus source for differential
          input.
        - ``REF<x>`` specifies a reference waveform as the source for differential input.
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
        - This command sets or queries the source polarity for the specified MIL-STD-1553 bus. The
          bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIL1553B:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIL1553B:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:MIL1553B:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MIL1553B:POLarity {NORMal|INVERTed}
        - BUS:B<x>:MIL1553B:POLarity?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``NORMal`` specifies normal polarity.
        - ``INVERTed`` specifies inverted polarity.
    """


class BusBItemMil1553b(SCPICmdRead):
    """The ``BUS:B<x>:MIL1553B`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIL1553B?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIL1553B?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

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
            - This command sets or queries the source polarity for the specified MIL-STD-1553 bus.
              The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MIL1553B:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIL1553B:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:MIL1553B:POLarity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MIL1553B:POLarity {NORMal|INVERTed}
            - BUS:B<x>:MIL1553B:POLarity?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``NORMal`` specifies normal polarity.
            - ``INVERTed`` specifies inverted polarity.
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
            - This command specifies the source for differential input for the MIL-STD-1553 bus. The
              supported source waveforms are channels 1-4, math waveform, and reference waveforms
              1-4. The default is channel 1.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MIL1553B:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIL1553B:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:MIL1553B:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MIL1553B:SOUrce {CH<x>|MATH|REF<x>}
            - BUS:B<x>:MIL1553B:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the source for differential input.
            - ``MATH`` specifies the math waveform as the MIL-STD-1553 bus source for differential
              input.
            - ``REF<x>`` specifies a reference waveform as the source for differential input.
        """
        return self._source


class BusBItemLinStandard(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LIN:STANDard`` command.

    Description:
        - Specifies the LIN bus standard to use.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:STANDard?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:STANDard?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:STANDard value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:STANDard {V1X|V2X|MIXed}
        - BUS:B<x>:LIN:STANDard?
        ```

    Info:
        - ``V1X`` sets the LIN bus standard to V1X.
        - ``V2X`` sets the LIN bus standard to V2X.
        - ``MIXed`` sets the LIN bus standard to MIXED.
    """


class BusBItemLinSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LIN:SOUrce`` command.

    Description:
        - Specifies the source waveform for the LIN bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:SOUrce?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:LIN:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the source waveform.
        - ``D<x>`` specifies a digital channel as the source waveform. (Requires option 3-MSO.).
    """


class BusBItemLinSamplepoint(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LIN:SAMPLEpoint`` command.

    Description:
        - Specifies the LIN sample point, for the specified LIN bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:SAMPLEpoint?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:SAMPLEpoint?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:SAMPLEpoint value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:SAMPLEpoint <NR1>
        - BUS:B<x>:LIN:SAMPLEpoint?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` is a percentage that represents the point at which to sample during each bit
          period.
    """


class BusBItemLinPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LIN:POLarity`` command.

    Description:
        - Specifies the LIN bus polarity.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:POLarity?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:POLarity value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:POLarity {NORMal|INVerted}
        - BUS:B<x>:LIN:POLarity?
        ```

    Info:
        - ``NORMal`` specifies normal polarity.
        - ``INVerted`` specifies inverted polarity.
    """


class BusBItemLinMaxbytedelim(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LIN:MAXBytedelim`` command.

    Description:
        - Specifies the maximum byte delimiter for the LIN bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:MAXBytedelim?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:MAXBytedelim?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:MAXBytedelim value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:MAXBytedelim <NR1>
        - BUS:B<x>:LIN:MAXBytedelim?
        ```

    Info:
        - ``<NR1>`` is the maximum byte delimiter for the LIN bus.
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


class BusBItemLinBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LIN:BITRate`` command.

    Description:
        - Specifies the bit rate for the LIN bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:BITRate value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:BITRate <NR1>
        - BUS:B<x>:LIN:BITRate?
        ```

    Info:
        - ``<NR1>`` is the LIN bus bit rate. You can enter any positive integer, and the instrument
          will coerce the value to the closest supported bit rate.
    """


class BusBItemLin(SCPICmdRead):
    """The ``BUS:B<x>:LIN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:LIN:BITRate`` command.
        - ``.idformat``: The ``BUS:B<x>:LIN:IDFORmat`` command.
        - ``.maxbytedelim``: The ``BUS:B<x>:LIN:MAXBytedelim`` command.
        - ``.polarity``: The ``BUS:B<x>:LIN:POLarity`` command.
        - ``.samplepoint``: The ``BUS:B<x>:LIN:SAMPLEpoint`` command.
        - ``.source``: The ``BUS:B<x>:LIN:SOUrce`` command.
        - ``.standard``: The ``BUS:B<x>:LIN:STANDard`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemLinBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._idformat = BusBItemLinIdformat(device, f"{self._cmd_syntax}:IDFORmat")
        self._maxbytedelim = BusBItemLinMaxbytedelim(device, f"{self._cmd_syntax}:MAXBytedelim")
        self._polarity = BusBItemLinPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._samplepoint = BusBItemLinSamplepoint(device, f"{self._cmd_syntax}:SAMPLEpoint")
        self._source = BusBItemLinSource(device, f"{self._cmd_syntax}:SOUrce")
        self._standard = BusBItemLinStandard(device, f"{self._cmd_syntax}:STANDard")

    @property
    def bitrate(self) -> BusBItemLinBitrate:
        """Return the ``BUS:B<x>:LIN:BITRate`` command.

        Description:
            - Specifies the bit rate for the LIN bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:BITRate?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:BITRate <NR1>
            - BUS:B<x>:LIN:BITRate?
            ```

        Info:
            - ``<NR1>`` is the LIN bus bit rate. You can enter any positive integer, and the
              instrument will coerce the value to the closest supported bit rate.
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
    def maxbytedelim(self) -> BusBItemLinMaxbytedelim:
        """Return the ``BUS:B<x>:LIN:MAXBytedelim`` command.

        Description:
            - Specifies the maximum byte delimiter for the LIN bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:MAXBytedelim?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:MAXBytedelim?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:MAXBytedelim value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:MAXBytedelim <NR1>
            - BUS:B<x>:LIN:MAXBytedelim?
            ```

        Info:
            - ``<NR1>`` is the maximum byte delimiter for the LIN bus.
        """
        return self._maxbytedelim

    @property
    def polarity(self) -> BusBItemLinPolarity:
        """Return the ``BUS:B<x>:LIN:POLarity`` command.

        Description:
            - Specifies the LIN bus polarity.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:POLarity?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:POLarity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:POLarity {NORMal|INVerted}
            - BUS:B<x>:LIN:POLarity?
            ```

        Info:
            - ``NORMal`` specifies normal polarity.
            - ``INVerted`` specifies inverted polarity.
        """
        return self._polarity

    @property
    def samplepoint(self) -> BusBItemLinSamplepoint:
        """Return the ``BUS:B<x>:LIN:SAMPLEpoint`` command.

        Description:
            - Specifies the LIN sample point, for the specified LIN bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:SAMPLEpoint?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:SAMPLEpoint?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:SAMPLEpoint value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:SAMPLEpoint <NR1>
            - BUS:B<x>:LIN:SAMPLEpoint?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` is a percentage that represents the point at which to sample during each bit
              period.
        """
        return self._samplepoint

    @property
    def source(self) -> BusBItemLinSource:
        """Return the ``BUS:B<x>:LIN:SOUrce`` command.

        Description:
            - Specifies the source waveform for the LIN bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:LIN:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the source waveform.
            - ``D<x>`` specifies a digital channel as the source waveform. (Requires option 3-MSO.).
        """
        return self._source

    @property
    def standard(self) -> BusBItemLinStandard:
        """Return the ``BUS:B<x>:LIN:STANDard`` command.

        Description:
            - Specifies the LIN bus standard to use.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:STANDard?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:STANDard?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:STANDard value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:STANDard {V1X|V2X|MIXed}
            - BUS:B<x>:LIN:STANDard?
            ```

        Info:
            - ``V1X`` sets the LIN bus standard to V1X.
            - ``V2X`` sets the LIN bus standard to V2X.
            - ``MIXed`` sets the LIN bus standard to MIXED.
        """
        return self._standard


class BusBItemLabel(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LABel`` command.

    Description:
        - Specifies the waveform label for the bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LABel <Qstring>
        - BUS:B<x>:LABel?
        ```

    Info:
        - ``<Qstring>`` is an alphanumeric string of text, enclosed in quotes, that contains the
          text label information for bus <x>. The text string is limited to 30 characters.
    """


class BusBItemI2cSdataSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I2C:SDAta:SOUrce`` command.

    Description:
        - Specifies the SDATA source for the I2C bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:SDAta:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:SDAta:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:SDAta:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I2C:SDAta:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:I2C:SDAta:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the I2C SDATA source waveform.
        - ``D<x>`` specifies a digital channel as the I2C SDATA source waveform. (Requires option
          3-MSO.).
    """


class BusBItemI2cSdata(SCPICmdRead):
    """The ``BUS:B<x>:I2C:SDAta`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:SDAta?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:SDAta?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``BUS:B<x>:I2C:SDAta:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemI2cSdataSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def source(self) -> BusBItemI2cSdataSource:
        """Return the ``BUS:B<x>:I2C:SDAta:SOUrce`` command.

        Description:
            - Specifies the SDATA source for the I2C bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:SDAta:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:SDAta:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:SDAta:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I2C:SDAta:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:I2C:SDAta:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the I2C SDATA source waveform.
            - ``D<x>`` specifies a digital channel as the I2C SDATA source waveform. (Requires
              option 3-MSO.).
        """
        return self._source


class BusBItemI2cSclkSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I2C:SCLk:SOUrce`` command.

    Description:
        - This command specifies the SCLK source for the I2C bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:SCLk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:SCLk:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:SCLk:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I2C:SCLk:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:I2C:SCLk:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the SCLK source waveform.
        - ``D<x>`` specifies a digital channel as the SCLK source waveform. (Requires option
          3-MSO.).
    """


class BusBItemI2cSclk(SCPICmdRead):
    """The ``BUS:B<x>:I2C:SCLk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:SCLk?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:SCLk?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``BUS:B<x>:I2C:SCLk:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemI2cSclkSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def source(self) -> BusBItemI2cSclkSource:
        """Return the ``BUS:B<x>:I2C:SCLk:SOUrce`` command.

        Description:
            - This command specifies the SCLK source for the I2C bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:SCLk:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:SCLk:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:SCLk:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I2C:SCLk:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:I2C:SCLk:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the SCLK source waveform.
            - ``D<x>`` specifies a digital channel as the SCLK source waveform. (Requires option
              3-MSO.).
        """
        return self._source


class BusBItemI2cDataSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I2C:DATa:SOUrce`` command.

    Description:
        - Specifies the SDATA source for the I2C bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:DATa:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:DATa:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:DATa:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I2C:DATa:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:I2C:DATa:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the I2C SDATA source waveform.
        - ``D<x>`` specifies a digital channel as the I2C SDATA source waveform. (Requires option
          3-MSO.).
    """


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
            - Specifies the SDATA source for the I2C bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:DATa:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:DATa:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:DATa:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I2C:DATa:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:I2C:DATa:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the I2C SDATA source waveform.
            - ``D<x>`` specifies a digital channel as the I2C SDATA source waveform. (Requires
              option 3-MSO.).
        """
        return self._source


class BusBItemI2cClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I2C:CLOCk:SOUrce`` command.

    Description:
        - This command specifies the SCLK source for the I2C bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:CLOCk:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:CLOCk:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I2C:CLOCk:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:I2C:CLOCk:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the SCLK source waveform.
        - ``D<x>`` specifies a digital channel as the SCLK source waveform. (Requires option
          3-MSO.).
    """


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
            - This command specifies the SCLK source for the I2C bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:CLOCk:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:CLOCk:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:CLOCk:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I2C:CLOCk:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:I2C:CLOCk:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the SCLK source waveform.
            - ``D<x>`` specifies a digital channel as the SCLK source waveform. (Requires option
              3-MSO.).
        """
        return self._source


class BusBItemI2cAddressRwinclude(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I2C:ADDRess:RWINClude`` command.

    Description:
        - Sets and returns whether the read/write bit is included in the address.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:ADDRess:RWINClude?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:ADDRess:RWINClude?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:ADDRess:RWINClude value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I2C:ADDRess:RWINClude {ON|OFF|<NR1>}
        - BUS:B<x>:I2C:ADDRess:RWINClude?
        ```

    Info:
        - ``<NR1>`` = 0 does not include the read/write bit in the address; any other value includes
          the read/write bit in the address.
    """


class BusBItemI2cAddress(SCPICmdRead):
    """The ``BUS:B<x>:I2C:ADDRess`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:ADDRess?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:ADDRess?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.rwinclude``: The ``BUS:B<x>:I2C:ADDRess:RWINClude`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._rwinclude = BusBItemI2cAddressRwinclude(device, f"{self._cmd_syntax}:RWINClude")

    @property
    def rwinclude(self) -> BusBItemI2cAddressRwinclude:
        """Return the ``BUS:B<x>:I2C:ADDRess:RWINClude`` command.

        Description:
            - Sets and returns whether the read/write bit is included in the address.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:ADDRess:RWINClude?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:ADDRess:RWINClude?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:I2C:ADDRess:RWINClude value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I2C:ADDRess:RWINClude {ON|OFF|<NR1>}
            - BUS:B<x>:I2C:ADDRess:RWINClude?
            ```

        Info:
            - ``<NR1>`` = 0 does not include the read/write bit in the address; any other value
              includes the read/write bit in the address.
        """
        return self._rwinclude


class BusBItemI2c(SCPICmdRead):
    """The ``BUS:B<x>:I2C`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.address``: The ``BUS:B<x>:I2C:ADDRess`` command tree.
        - ``.clock``: The ``BUS:B<x>:I2C:CLOCk`` command tree.
        - ``.sclk``: The ``BUS:B<x>:I2C:SCLk`` command tree.
        - ``.data``: The ``BUS:B<x>:I2C:DATa`` command tree.
        - ``.sdata``: The ``BUS:B<x>:I2C:SDAta`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._address = BusBItemI2cAddress(device, f"{self._cmd_syntax}:ADDRess")
        self._clock = BusBItemI2cClock(device, f"{self._cmd_syntax}:CLOCk")
        self._sclk = BusBItemI2cSclk(device, f"{self._cmd_syntax}:SCLk")
        self._data = BusBItemI2cData(device, f"{self._cmd_syntax}:DATa")
        self._sdata = BusBItemI2cSdata(device, f"{self._cmd_syntax}:SDAta")

    @property
    def address(self) -> BusBItemI2cAddress:
        """Return the ``BUS:B<x>:I2C:ADDRess`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:ADDRess?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:ADDRess?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.rwinclude``: The ``BUS:B<x>:I2C:ADDRess:RWINClude`` command.
        """
        return self._address

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
    def sclk(self) -> BusBItemI2cSclk:
        """Return the ``BUS:B<x>:I2C:SCLk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:SCLk?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:SCLk?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:I2C:SCLk:SOUrce`` command.
        """
        return self._sclk

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
    def sdata(self) -> BusBItemI2cSdata:
        """Return the ``BUS:B<x>:I2C:SDAta`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:SDAta?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:SDAta?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:I2C:SDAta:SOUrce`` command.
        """
        return self._sdata


class BusBItemFlexraySource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:FLEXray:SOUrce`` command.

    Description:
        - Specifies the FlexRay bus source waveform.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXray:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:FLEXray:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:FLEXray:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the source waveform.
    """


class BusBItemFlexraySignal(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:FLEXray:SIGnal`` command.

    Description:
        - This command sets or queries the FlexRay signal type for the specified bus. The bus number
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:SIGnal?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:SIGnal?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXray:SIGnal value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:FLEXray:SIGnal {BDIFFBP|BM|TXRX}
        - BUS:B<x>:FLEXray:SIGnal?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``BDIFFBP`` sets the FlexRay signal type to BDIFFBP.
        - ``BM`` sets the FlexRay signal type to BM.
        - ``TXRX`` sets the FlexRay signal type to TXRX.
    """


class BusBItemFlexrayChannel(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:FLEXray:CHannel`` command.

    Description:
        - This command sets or queries the FlexRay channel type for the specified bus. The bus
          number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:CHannel?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:CHannel?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXray:CHannel value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:FLEXray:CHannel {A|B}
        - BUS:B<x>:FLEXray:CHannel?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``A`` specifies the A channel.
        - ``B`` specifies the B channel.
    """


class BusBItemFlexrayBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:FLEXray:BITRate`` command.

    Description:
        - Specifies the bit rate for the FlexRay bus signal. The maximum bitrate is 100 Mbps.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXray:BITRate value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:FLEXray:BITRate <NR1>
        - BUS:B<x>:FLEXray:BITRate?
        ```

    Info:
        - ``<NR1>`` specifies the FlexRay bus bit rate. You can enter any positive integer, and the
          instrument will coerce the value to the closest supported bit rate.
    """


class BusBItemFlexray(SCPICmdRead):
    """The ``BUS:B<x>:FLEXray`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:FLEXray:BITRate`` command.
        - ``.channel``: The ``BUS:B<x>:FLEXray:CHannel`` command.
        - ``.signal``: The ``BUS:B<x>:FLEXray:SIGnal`` command.
        - ``.source``: The ``BUS:B<x>:FLEXray:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemFlexrayBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._channel = BusBItemFlexrayChannel(device, f"{self._cmd_syntax}:CHannel")
        self._signal = BusBItemFlexraySignal(device, f"{self._cmd_syntax}:SIGnal")
        self._source = BusBItemFlexraySource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def bitrate(self) -> BusBItemFlexrayBitrate:
        """Return the ``BUS:B<x>:FLEXray:BITRate`` command.

        Description:
            - Specifies the bit rate for the FlexRay bus signal. The maximum bitrate is 100 Mbps.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:BITRate?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXray:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:FLEXray:BITRate <NR1>
            - BUS:B<x>:FLEXray:BITRate?
            ```

        Info:
            - ``<NR1>`` specifies the FlexRay bus bit rate. You can enter any positive integer, and
              the instrument will coerce the value to the closest supported bit rate.
        """
        return self._bitrate

    @property
    def channel(self) -> BusBItemFlexrayChannel:
        """Return the ``BUS:B<x>:FLEXray:CHannel`` command.

        Description:
            - This command sets or queries the FlexRay channel type for the specified bus. The bus
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:CHannel?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:CHannel?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXray:CHannel value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:FLEXray:CHannel {A|B}
            - BUS:B<x>:FLEXray:CHannel?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``A`` specifies the A channel.
            - ``B`` specifies the B channel.
        """
        return self._channel

    @property
    def signal(self) -> BusBItemFlexraySignal:
        """Return the ``BUS:B<x>:FLEXray:SIGnal`` command.

        Description:
            - This command sets or queries the FlexRay signal type for the specified bus. The bus
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:SIGnal?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:SIGnal?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXray:SIGnal value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:FLEXray:SIGnal {BDIFFBP|BM|TXRX}
            - BUS:B<x>:FLEXray:SIGnal?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``BDIFFBP`` sets the FlexRay signal type to BDIFFBP.
            - ``BM`` sets the FlexRay signal type to BM.
            - ``TXRX`` sets the FlexRay signal type to TXRX.
        """
        return self._signal

    @property
    def source(self) -> BusBItemFlexraySource:
        """Return the ``BUS:B<x>:FLEXray:SOUrce`` command.

        Description:
            - Specifies the FlexRay bus source waveform.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXray:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:FLEXray:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:FLEXray:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the source waveform.
        """
        return self._source


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
        - This command specifies the Ethernet data source for the D+ input for single-ended probing.
          The default is channel 1.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DPLUs?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DPLUs?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DPLUs value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERnet:SOUrce:DPLUs {CH<x>|D<x>}
        - BUS:B<x>:ETHERnet:SOUrce:DPLUs?
        ```

    Info:
        - ``CH<x>`` specifies to use one of the analog channels 1-4 as the Ethernet data source for
          the D+ input.
        - ``D<x>`` specifies to use one of the digital channels D0 - D15 as the Ethernet data source
          for the D+ input. Requires option 3-MSO.
    """


class BusBItemEthernetSourceDminus(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ETHERnet:SOUrce:DMINus`` command.

    Description:
        - This command specifies the Ethernet data source for D- input for single-ended probing. The
          default is Channel 2.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DMINus?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DMINus?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DMINus value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERnet:SOUrce:DMINus {CH<x>|D<x>}
        - BUS:B<x>:ETHERnet:SOUrce:DMINus?
        ```

    Info:
        - ``CH<x>`` specifies to use one of the analog channels as the Ethernet data source for the
          D- input.
        - ``D<x>`` specifies to use one of the digital channels D0 - D15 as the Ethernet data source
          for the D- input.
    """


class BusBItemEthernetSourceDifferential(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ETHERnet:SOUrce:DIFFerential`` command.

    Description:
        - This command specifies the Ethernet data source for differential input. The supported
          source waveforms are channels 1-4, math waveform, and reference waveforms 1-4. The default
          is channel 1.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DIFFerential?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``BUS:B<x>:ETHERnet:SOUrce:DIFFerential?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:ETHERnet:SOUrce:DIFFerential value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERnet:SOUrce:DIFFerential {CH<x>|MATH|REF<x>}
        - BUS:B<x>:ETHERnet:SOUrce:DIFFerential?
        ```

    Info:
        - ``CH<x>`` specifies to use one of the channels 1-4 as the Ethernet data source for
          differential input.
        - ``MATH`` specifies to use the math waveform as the source for Ethernet data differential
          input.
        - ``REF<x>`` specifies to use one of the reference waveforms 1-4 as the source for Ethernet
          data differential input.
    """


class BusBItemEthernetSource(SCPICmdRead):
    """The ``BUS:B<x>:ETHERnet:SOUrce`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.differential``: The ``BUS:B<x>:ETHERnet:SOUrce:DIFFerential`` command.
        - ``.dminus``: The ``BUS:B<x>:ETHERnet:SOUrce:DMINus`` command.
        - ``.dplus``: The ``BUS:B<x>:ETHERnet:SOUrce:DPLUs`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._differential = BusBItemEthernetSourceDifferential(
            device, f"{self._cmd_syntax}:DIFFerential"
        )
        self._dminus = BusBItemEthernetSourceDminus(device, f"{self._cmd_syntax}:DMINus")
        self._dplus = BusBItemEthernetSourceDplus(device, f"{self._cmd_syntax}:DPLUs")

    @property
    def differential(self) -> BusBItemEthernetSourceDifferential:
        """Return the ``BUS:B<x>:ETHERnet:SOUrce:DIFFerential`` command.

        Description:
            - This command specifies the Ethernet data source for differential input. The supported
              source waveforms are channels 1-4, math waveform, and reference waveforms 1-4. The
              default is channel 1.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DIFFerential?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:ETHERnet:SOUrce:DIFFerential?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ETHERnet:SOUrce:DIFFerential value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERnet:SOUrce:DIFFerential {CH<x>|MATH|REF<x>}
            - BUS:B<x>:ETHERnet:SOUrce:DIFFerential?
            ```

        Info:
            - ``CH<x>`` specifies to use one of the channels 1-4 as the Ethernet data source for
              differential input.
            - ``MATH`` specifies to use the math waveform as the source for Ethernet data
              differential input.
            - ``REF<x>`` specifies to use one of the reference waveforms 1-4 as the source for
              Ethernet data differential input.
        """
        return self._differential

    @property
    def dminus(self) -> BusBItemEthernetSourceDminus:
        """Return the ``BUS:B<x>:ETHERnet:SOUrce:DMINus`` command.

        Description:
            - This command specifies the Ethernet data source for D- input for single-ended probing.
              The default is Channel 2.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DMINus?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DMINus?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ETHERnet:SOUrce:DMINus value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERnet:SOUrce:DMINus {CH<x>|D<x>}
            - BUS:B<x>:ETHERnet:SOUrce:DMINus?
            ```

        Info:
            - ``CH<x>`` specifies to use one of the analog channels as the Ethernet data source for
              the D- input.
            - ``D<x>`` specifies to use one of the digital channels D0 - D15 as the Ethernet data
              source for the D- input.
        """
        return self._dminus

    @property
    def dplus(self) -> BusBItemEthernetSourceDplus:
        """Return the ``BUS:B<x>:ETHERnet:SOUrce:DPLUs`` command.

        Description:
            - This command specifies the Ethernet data source for the D+ input for single-ended
              probing. The default is channel 1.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DPLUs?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DPLUs?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ETHERnet:SOUrce:DPLUs value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERnet:SOUrce:DPLUs {CH<x>|D<x>}
            - BUS:B<x>:ETHERnet:SOUrce:DPLUs?
            ```

        Info:
            - ``CH<x>`` specifies to use one of the analog channels 1-4 as the Ethernet data source
              for the D+ input.
            - ``D<x>`` specifies to use one of the digital channels D0 - D15 as the Ethernet data
              source for the D+ input. Requires option 3-MSO.
        """
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


class BusBItemEthernetProtocol(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ETHERnet:PROTOcol`` command.

    Description:
        - Use this command to set the Ethernet protocol type to TCP/IPv4, or to OTHER. The default
          is IPV4.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:PROTOcol?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:PROTOcol?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERnet:PROTOcol value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERnet:PROTOcol {IPv4|OTHER}
        - BUS:B<x>:ETHERnet:PROTOcol?
        ```

    Info:
        - ``IPv4`` sets the Ethernet protocol type to Internet Protocol version 4.
        - ``OTHER`` sets the Ethernet protocol type to other than IPv4.
    """


class BusBItemEthernet(SCPICmdRead):
    """The ``BUS:B<x>:ETHERnet`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.protocol``: The ``BUS:B<x>:ETHERnet:PROTOcol`` command.
        - ``.probe``: The ``BUS:B<x>:ETHERnet:PRObe`` command.
        - ``.source``: The ``BUS:B<x>:ETHERnet:SOUrce`` command tree.
        - ``.type``: The ``BUS:B<x>:ETHERnet:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._protocol = BusBItemEthernetProtocol(device, f"{self._cmd_syntax}:PROTOcol")
        self._probe = BusBItemEthernetProbe(device, f"{self._cmd_syntax}:PRObe")
        self._source = BusBItemEthernetSource(device, f"{self._cmd_syntax}:SOUrce")
        self._type = BusBItemEthernetType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def protocol(self) -> BusBItemEthernetProtocol:
        """Return the ``BUS:B<x>:ETHERnet:PROTOcol`` command.

        Description:
            - Use this command to set the Ethernet protocol type to TCP/IPv4, or to OTHER. The
              default is IPV4.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:PROTOcol?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:PROTOcol?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERnet:PROTOcol value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERnet:PROTOcol {IPv4|OTHER}
            - BUS:B<x>:ETHERnet:PROTOcol?
            ```

        Info:
            - ``IPv4`` sets the Ethernet protocol type to Internet Protocol version 4.
            - ``OTHER`` sets the Ethernet protocol type to other than IPv4.
        """
        return self._protocol

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
        """Return the ``BUS:B<x>:ETHERnet:SOUrce`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.differential``: The ``BUS:B<x>:ETHERnet:SOUrce:DIFFerential`` command.
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
        - Specifies the display type for bus. You can set up the bus to display the protocol
          information, the logic waveforms that comprise the bus, or both.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay:TYPe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:DISplay:TYPe value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:DISplay:TYPe {BUS|BOTh}
        - BUS:B<x>:DISplay:TYPe?
        ```

    Info:
        - ``BUS`` displays the bus waveforms only.
        - ``BOTh`` displays both the bus and logic waveforms.
    """


class BusBItemDisplayFormat(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:DISplay:FORMat`` command.

    Description:
        - Specifies the display format for the numerical information in the bus waveform. The
          display formats supported depend on the ``BUS:BX:TYPE``. Supported display formats Bus
          type Display format Audio BINary | HEXadecimal | ASCII | SIGNEDDECimal CAN BINary |
          HEXadecimal | MIXed Ethernet BINary | HEXadecimal | ASCII | MIXed FlexRay BINary |
          HEXadecimal | MIXed I 2 C BINary | HEXadecimal LIN BINary | HEXadecimal | MiXed
          MIL-STD-1553 BINary | HEXadecimal | ASCII|MIXed|BLOCKHEX Parallel BINary | HEXadecimal
          RS232C BINary | HEXadecimal | ASCII SPI BINary | HEXadecimal USB BINary | HEXadecimal |
          MIXed | MIXED2 SIGNEDDECimal is set using the audio application
          ``BUS:BX:AUDIO:DISPLAY:FORMAT`` command.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay:FORMat?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay:FORMat?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:DISplay:FORMat value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:DISplay:FORMat {BINary|HEXadecimal|ASCII|MIXed|MIXED2|BLOCKHEX}
        - BUS:B<x>:DISplay:FORMat?
        ```

    Info:
        - ``BINary`` - All values are displayed in binary.
        - ``HEXadecimal`` - All values are displayed in hexadecimal.
        - ``ASCII`` - All values are displayed in an ASCII format, for RS-232 only.
        - ``MIXed`` - Values are displayed in a mixture of hexadecimal, binary, and decimal,
          depending on the field.
        - ``MIXED2`` - Values are displayed in a mixture of hexadecimal, binary, decimal and ASCII,
          depending on the field.
        - ``BLOCKHEX`` - Displays the 16-bits of each payload as a block of 4 hexadecimal digits.
    """


class BusBItemDisplay(SCPICmdRead):
    """The ``BUS:B<x>:DISplay`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.format``: The ``BUS:B<x>:DISplay:FORMat`` command.
        - ``.type``: The ``BUS:B<x>:DISplay:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._format = BusBItemDisplayFormat(device, f"{self._cmd_syntax}:FORMat")
        self._type = BusBItemDisplayType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def format(self) -> BusBItemDisplayFormat:
        """Return the ``BUS:B<x>:DISplay:FORMat`` command.

        Description:
            - Specifies the display format for the numerical information in the bus waveform. The
              display formats supported depend on the ``BUS:BX:TYPE``. Supported display formats Bus
              type Display format Audio BINary | HEXadecimal | ASCII | SIGNEDDECimal CAN BINary |
              HEXadecimal | MIXed Ethernet BINary | HEXadecimal | ASCII | MIXed FlexRay BINary |
              HEXadecimal | MIXed I 2 C BINary | HEXadecimal LIN BINary | HEXadecimal | MiXed
              MIL-STD-1553 BINary | HEXadecimal | ASCII|MIXed|BLOCKHEX Parallel BINary | HEXadecimal
              RS232C BINary | HEXadecimal | ASCII SPI BINary | HEXadecimal USB BINary | HEXadecimal
              | MIXed | MIXED2 SIGNEDDECimal is set using the audio application
              ``BUS:BX:AUDIO:DISPLAY:FORMAT`` command.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay:FORMat?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay:FORMat?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:DISplay:FORMat value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:DISplay:FORMat {BINary|HEXadecimal|ASCII|MIXed|MIXED2|BLOCKHEX}
            - BUS:B<x>:DISplay:FORMat?
            ```

        Info:
            - ``BINary`` - All values are displayed in binary.
            - ``HEXadecimal`` - All values are displayed in hexadecimal.
            - ``ASCII`` - All values are displayed in an ASCII format, for RS-232 only.
            - ``MIXed`` - Values are displayed in a mixture of hexadecimal, binary, and decimal,
              depending on the field.
            - ``MIXED2`` - Values are displayed in a mixture of hexadecimal, binary, decimal and
              ASCII, depending on the field.
            - ``BLOCKHEX`` - Displays the 16-bits of each payload as a block of 4 hexadecimal
              digits.
        """
        return self._format

    @property
    def type(self) -> BusBItemDisplayType:
        """Return the ``BUS:B<x>:DISplay:TYPe`` command.

        Description:
            - Specifies the display type for bus. You can set up the bus to display the protocol
              information, the logic waveforms that comprise the bus, or both.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay:TYPe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:DISplay:TYPe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:DISplay:TYPe {BUS|BOTh}
            - BUS:B<x>:DISplay:TYPe?
            ```

        Info:
            - ``BUS`` displays the bus waveforms only.
            - ``BOTh`` displays both the bus and logic waveforms.
        """
        return self._type


class BusBItemCanStandard(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:STANDard`` command.

    Description:
        - Specifies the CAN bus standard to use.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:STANDard?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:STANDard?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:STANDard value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:STANDard {CAN2X|CANFD} string
        - BUS:B<x>:CAN:STANDard?
        ```

    Info:
        - ``CAN2X`` sets the CAN bus standard to CAN 2.0.
        - ``CANFD`` sets the CAN bus standard to CAN FD.
    """


class BusBItemCanSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:SOUrce`` command.

    Description:
        - Specifies the CAN bus data source.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:SOUrce?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:CAN:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the data source waveform.
        - ``D<x>`` specifies a digital channel as the data source waveform. (Requires installation
          of option 3-MSO.).
    """


class BusBItemCanSamplepoint(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:SAMPLEpoint`` command.

    Description:
        - This command sets or queries the sample point for the specified CAN bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:SAMPLEpoint?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:SAMPLEpoint?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:SAMPLEpoint value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:SAMPLEpoint <NR1>
        - BUS:B<x>:CAN:SAMPLEpoint?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` is the sample point, in percent, for the specified CAN bus.
    """


class BusBItemCanProbe(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:PRObe`` command.

    Description:
        - Specifies the probing method for the CAN bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:PRObe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:PRObe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:PRObe value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:PRObe {CANH|CANL|RX|TX|DIFFerential}
        - BUS:B<x>:CAN:PRObe?
        ```

    Info:
        - ``CANH`` specifies the single-ended CANH signal, as specified by the CAN standard.
        - ``CANL`` specifies the single-ended CANL signal, as specified by the CAN standard.
        - ``RX`` specifies the receive signal on the bus side of the CAN transceiver.
        - ``TX`` specifies the transmit signal.
        - ``DIFFerential`` specifies the differential CAN signal.
    """


class BusBItemCanFdStandard(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:FD:STANDard`` command.

    Description:
        - Specifies the CAN FD standard to use.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:FD:STANDard?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:FD:STANDard?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:FD:STANDard value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:FD:STANDard {ISO | NONISO} string
        - BUS:B<x>:CAN:FD:STANDard?
        ```

    Info:
        - ``ISO`` sets the CAN FD standard to ISO CAN FD (11898-``1:2015``).
        - ``NONISO`` sets the CAN FD standard to non-ISO CAN FD (``Bosch:2012``).
    """


class BusBItemCanFdBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:FD:BITRate`` command.

    Description:
        - Specifies the FD bit rate for the CAN bus. This is the bitrate used for CAN FD frames
          transmitted with increased data phase rates. The maximum bitrate is 10 Mbps.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:FD:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:FD:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:FD:BITRate value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:FD:BITRate <NR1>
        - BUS:B<x>:CAN:FD:BITRate?
        ```

    Info:
        - ``<NR1>`` is the FD bit rate. The instrument supports bit rates at 100 bps intervals. You
          can enter any positive integer, and the instrument will coerce the value to the closest
          supported bit rate.
    """


class BusBItemCanFd(SCPICmdRead):
    """The ``BUS:B<x>:CAN:FD`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:FD?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:FD?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:CAN:FD:BITRate`` command.
        - ``.standard``: The ``BUS:B<x>:CAN:FD:STANDard`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemCanFdBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._standard = BusBItemCanFdStandard(device, f"{self._cmd_syntax}:STANDard")

    @property
    def bitrate(self) -> BusBItemCanFdBitrate:
        """Return the ``BUS:B<x>:CAN:FD:BITRate`` command.

        Description:
            - Specifies the FD bit rate for the CAN bus. This is the bitrate used for CAN FD frames
              transmitted with increased data phase rates. The maximum bitrate is 10 Mbps.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:FD:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:FD:BITRate?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:FD:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:FD:BITRate <NR1>
            - BUS:B<x>:CAN:FD:BITRate?
            ```

        Info:
            - ``<NR1>`` is the FD bit rate. The instrument supports bit rates at 100 bps intervals.
              You can enter any positive integer, and the instrument will coerce the value to the
              closest supported bit rate.
        """
        return self._bitrate

    @property
    def standard(self) -> BusBItemCanFdStandard:
        """Return the ``BUS:B<x>:CAN:FD:STANDard`` command.

        Description:
            - Specifies the CAN FD standard to use.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:FD:STANDard?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:FD:STANDard?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:FD:STANDard value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:FD:STANDard {ISO | NONISO} string
            - BUS:B<x>:CAN:FD:STANDard?
            ```

        Info:
            - ``ISO`` sets the CAN FD standard to ISO CAN FD (11898-``1:2015``).
            - ``NONISO`` sets the CAN FD standard to non-ISO CAN FD (``Bosch:2012``).
        """
        return self._standard


class BusBItemCanBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:BITRate`` command.

    Description:
        - Specifies the bit rate for the CAN bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:BITRate value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:BITRate <NR1>
        - BUS:B<x>:CAN:BITRate?
        ```

    Info:
        - ``<NR1>`` is the bit rate. The instrument supports bit rates at 10 bps intervals. You can
          enter any positive integer, and the instrument will coerce the value to the closest
          supported bit rate.
    """


class BusBItemCan(SCPICmdRead):
    """The ``BUS:B<x>:CAN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:CAN:BITRate`` command.
        - ``.fd``: The ``BUS:B<x>:CAN:FD`` command tree.
        - ``.probe``: The ``BUS:B<x>:CAN:PRObe`` command.
        - ``.samplepoint``: The ``BUS:B<x>:CAN:SAMPLEpoint`` command.
        - ``.source``: The ``BUS:B<x>:CAN:SOUrce`` command.
        - ``.standard``: The ``BUS:B<x>:CAN:STANDard`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemCanBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._fd = BusBItemCanFd(device, f"{self._cmd_syntax}:FD")
        self._probe = BusBItemCanProbe(device, f"{self._cmd_syntax}:PRObe")
        self._samplepoint = BusBItemCanSamplepoint(device, f"{self._cmd_syntax}:SAMPLEpoint")
        self._source = BusBItemCanSource(device, f"{self._cmd_syntax}:SOUrce")
        self._standard = BusBItemCanStandard(device, f"{self._cmd_syntax}:STANDard")

    @property
    def bitrate(self) -> BusBItemCanBitrate:
        """Return the ``BUS:B<x>:CAN:BITRate`` command.

        Description:
            - Specifies the bit rate for the CAN bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:BITRate?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:BITRate <NR1>
            - BUS:B<x>:CAN:BITRate?
            ```

        Info:
            - ``<NR1>`` is the bit rate. The instrument supports bit rates at 10 bps intervals. You
              can enter any positive integer, and the instrument will coerce the value to the
              closest supported bit rate.
        """
        return self._bitrate

    @property
    def fd(self) -> BusBItemCanFd:
        """Return the ``BUS:B<x>:CAN:FD`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:FD?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:FD?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:CAN:FD:BITRate`` command.
            - ``.standard``: The ``BUS:B<x>:CAN:FD:STANDard`` command.
        """
        return self._fd

    @property
    def probe(self) -> BusBItemCanProbe:
        """Return the ``BUS:B<x>:CAN:PRObe`` command.

        Description:
            - Specifies the probing method for the CAN bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:PRObe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:PRObe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:PRObe value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:PRObe {CANH|CANL|RX|TX|DIFFerential}
            - BUS:B<x>:CAN:PRObe?
            ```

        Info:
            - ``CANH`` specifies the single-ended CANH signal, as specified by the CAN standard.
            - ``CANL`` specifies the single-ended CANL signal, as specified by the CAN standard.
            - ``RX`` specifies the receive signal on the bus side of the CAN transceiver.
            - ``TX`` specifies the transmit signal.
            - ``DIFFerential`` specifies the differential CAN signal.
        """
        return self._probe

    @property
    def samplepoint(self) -> BusBItemCanSamplepoint:
        """Return the ``BUS:B<x>:CAN:SAMPLEpoint`` command.

        Description:
            - This command sets or queries the sample point for the specified CAN bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:SAMPLEpoint?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:SAMPLEpoint?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:SAMPLEpoint value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:SAMPLEpoint <NR1>
            - BUS:B<x>:CAN:SAMPLEpoint?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` is the sample point, in percent, for the specified CAN bus.
        """
        return self._samplepoint

    @property
    def source(self) -> BusBItemCanSource:
        """Return the ``BUS:B<x>:CAN:SOUrce`` command.

        Description:
            - Specifies the CAN bus data source.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:CAN:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the data source waveform.
            - ``D<x>`` specifies a digital channel as the data source waveform. (Requires
              installation of option 3-MSO.).
        """
        return self._source

    @property
    def standard(self) -> BusBItemCanStandard:
        """Return the ``BUS:B<x>:CAN:STANDard`` command.

        Description:
            - Specifies the CAN bus standard to use.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:STANDard?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:STANDard?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:STANDard value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:STANDard {CAN2X|CANFD} string
            - BUS:B<x>:CAN:STANDard?
            ```

        Info:
            - ``CAN2X`` sets the CAN bus standard to CAN 2.0.
            - ``CANFD`` sets the CAN bus standard to CAN FD.
        """
        return self._standard


class BusBItemAudioWordselSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUDio:WORDSel:SOUrce`` command.

    Description:
        - Specifies the word select source waveform for the AUDIO bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:WORDSel:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:WORDSel:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:WORDSel:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUDio:WORDSel:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:AUDio:WORDSel:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the word select source waveform .
        - ``D<x>`` specifies a digital channel as the word select source waveform. (Requires option
          3-MSO.).
    """


class BusBItemAudioWordselPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUDio:WORDSel:POLarity`` command.

    Description:
        - This command sets or queries the word select source polarity for the specified audio bus.
          The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:WORDSel:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:WORDSel:POLarity?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:WORDSel:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUDio:WORDSel:POLarity {NORMal|INVERTed}
        - BUS:B<x>:AUDio:WORDSel:POLarity?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``NORMal`` specifies positive polarity.
        - ``INVERTed`` specifies negative polarity.
    """


class BusBItemAudioWordsel(SCPICmdRead):
    """The ``BUS:B<x>:AUDio:WORDSel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:WORDSel?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:WORDSel?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:AUDio:WORDSel:POLarity`` command.
        - ``.source``: The ``BUS:B<x>:AUDio:WORDSel:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemAudioWordselPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemAudioWordselSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def polarity(self) -> BusBItemAudioWordselPolarity:
        """Return the ``BUS:B<x>:AUDio:WORDSel:POLarity`` command.

        Description:
            - This command sets or queries the word select source polarity for the specified audio
              bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:WORDSel:POLarity?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:WORDSel:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:AUDio:WORDSel:POLarity value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUDio:WORDSel:POLarity {NORMal|INVERTed}
            - BUS:B<x>:AUDio:WORDSel:POLarity?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``NORMal`` specifies positive polarity.
            - ``INVERTed`` specifies negative polarity.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemAudioWordselSource:
        """Return the ``BUS:B<x>:AUDio:WORDSel:SOUrce`` command.

        Description:
            - Specifies the word select source waveform for the AUDIO bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:WORDSel:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:WORDSel:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:AUDio:WORDSel:SOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUDio:WORDSel:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:AUDio:WORDSel:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the word select source waveform .
            - ``D<x>`` specifies a digital channel as the word select source waveform. (Requires
              option 3-MSO.).
        """
        return self._source


class BusBItemAudioType(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUDio:TYPe`` command.

    Description:
        - This command sets or queries the audio format (type) for the specified audio bus. The bus
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:TYPe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:TYPe value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUDio:TYPe {I2S|LJ|RJ|TDM}
        - BUS:B<x>:AUDio:TYPe?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``I2S`` specifies the I2S audio format.
        - ``LJ`` specifies the left-justified audio format.
        - ``RJ`` specifies the right-justified audio format.
        - ``TDM`` specifies the time-division multiplexing audio format.
    """


class BusBItemAudioFramesyncSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUDio:FRAMESync:SOUrce`` command.

    Description:
        - Specifies the frame sync source waveform for the AUDIO bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:FRAMESync:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:FRAMESync:SOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:FRAMESync:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUDio:FRAMESync:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:AUDio:FRAMESync:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the frame sync source waveform.
        - ``D<x>`` specifies a digital channel as the frame sync source waveform. (Requires option
          3-MSO.).
    """


class BusBItemAudioFramesyncPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUDio:FRAMESync:POLarity`` command.

    Description:
        - Specifies the frame sync polarity for the AUDIO bus - falling or rising edge.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:FRAMESync:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:FRAMESync:POLarity?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:AUDio:FRAMESync:POLarity value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUDio:FRAMESync:POLarity {FALL|RISe}
        - BUS:B<x>:AUDio:FRAMESync:POLarity?
        ```

    Info:
        - ``FALL`` specifies the falling edge as the frame sync polarity.
        - ``RISe`` specifies the rising edge as the frame sync polarity.
    """


class BusBItemAudioFramesync(SCPICmdRead):
    """The ``BUS:B<x>:AUDio:FRAMESync`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:FRAMESync?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:FRAMESync?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:AUDio:FRAMESync:POLarity`` command.
        - ``.source``: The ``BUS:B<x>:AUDio:FRAMESync:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemAudioFramesyncPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemAudioFramesyncSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def polarity(self) -> BusBItemAudioFramesyncPolarity:
        """Return the ``BUS:B<x>:AUDio:FRAMESync:POLarity`` command.

        Description:
            - Specifies the frame sync polarity for the AUDIO bus - falling or rising edge.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:FRAMESync:POLarity?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:AUDio:FRAMESync:POLarity?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:AUDio:FRAMESync:POLarity value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUDio:FRAMESync:POLarity {FALL|RISe}
            - BUS:B<x>:AUDio:FRAMESync:POLarity?
            ```

        Info:
            - ``FALL`` specifies the falling edge as the frame sync polarity.
            - ``RISe`` specifies the rising edge as the frame sync polarity.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemAudioFramesyncSource:
        """Return the ``BUS:B<x>:AUDio:FRAMESync:SOUrce`` command.

        Description:
            - Specifies the frame sync source waveform for the AUDIO bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:FRAMESync:SOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:FRAMESync:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:AUDio:FRAMESync:SOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUDio:FRAMESync:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:AUDio:FRAMESync:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the frame sync source waveform.
            - ``D<x>`` specifies a digital channel as the frame sync source waveform. (Requires
              option 3-MSO.).
        """
        return self._source


class BusBItemAudioFrameSize(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUDio:FRAME:SIZe`` command.

    Description:
        - This command sets or queries the number of audio channels in each frame for the specified
          AUDIO bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:FRAME:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:FRAME:SIZe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:FRAME:SIZe value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUDio:FRAME:SIZe <NR1>
        - BUS:B<x>:AUDio:FRAME:SIZe?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` specifies the number of channels in each frame.
    """


class BusBItemAudioFrame(SCPICmdRead):
    """The ``BUS:B<x>:AUDio:FRAME`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:FRAME?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:FRAME?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.size``: The ``BUS:B<x>:AUDio:FRAME:SIZe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._size = BusBItemAudioFrameSize(device, f"{self._cmd_syntax}:SIZe")

    @property
    def size(self) -> BusBItemAudioFrameSize:
        """Return the ``BUS:B<x>:AUDio:FRAME:SIZe`` command.

        Description:
            - This command sets or queries the number of audio channels in each frame for the
              specified AUDIO bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:FRAME:SIZe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:FRAME:SIZe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:FRAME:SIZe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUDio:FRAME:SIZe <NR1>
            - BUS:B<x>:AUDio:FRAME:SIZe?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` specifies the number of channels in each frame.
        """
        return self._size


class BusBItemAudioDisplayFormat(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUDio:DISplay:FORMat`` command.

    Description:
        - Specifies the display format for the AUDIO bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:DISplay:FORMat?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:DISplay:FORMat?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:DISplay:FORMat value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUDio:DISplay:FORMat {BINary|HEXadecimal|SIGNEDDECimal}
        - BUS:B<x>:AUDio:DISplay:FORMat?
        ```

    Info:
        - ``BINary`` specifies a binary data display.
        - ``HEXadecimal`` specifies a hexadecimal data display.
        - ``SIGNEDDECimal`` specifies a signed decimal data display.
    """


class BusBItemAudioDisplay(SCPICmdRead):
    """The ``BUS:B<x>:AUDio:DISplay`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:DISplay?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:DISplay?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.format``: The ``BUS:B<x>:AUDio:DISplay:FORMat`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._format = BusBItemAudioDisplayFormat(device, f"{self._cmd_syntax}:FORMat")

    @property
    def format(self) -> BusBItemAudioDisplayFormat:
        """Return the ``BUS:B<x>:AUDio:DISplay:FORMat`` command.

        Description:
            - Specifies the display format for the AUDIO bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:DISplay:FORMat?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:DISplay:FORMat?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:AUDio:DISplay:FORMat value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUDio:DISplay:FORMat {BINary|HEXadecimal|SIGNEDDECimal}
            - BUS:B<x>:AUDio:DISplay:FORMat?
            ```

        Info:
            - ``BINary`` specifies a binary data display.
            - ``HEXadecimal`` specifies a hexadecimal data display.
            - ``SIGNEDDECimal`` specifies a signed decimal data display.
        """
        return self._format


class BusBItemAudioDataSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUDio:DATa:SOUrce`` command.

    Description:
        - Specifies the data source waveform for the AUDIO bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:DATa:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:DATa:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:DATa:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUDio:DATa:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:AUDio:DATa:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the data source waveform for the audio bus.
        - ``D<x>`` specifies a digital channel as the data source waveform for the audio bus.
          (Requires option 3-MSO.).
    """


class BusBItemAudioDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUDio:DATa:SIZe`` command.

    Description:
        - This command sets or queries the number of bits per channel for the specified audio bus.
          This command only applies to the TDM Audio type. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:DATa:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:DATa:SIZe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:DATa:SIZe value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUDio:DATa:SIZe <NR1>
        - BUS:B<x>:AUDio:DATa:SIZe?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``NR1`` specifies the number of bits per word.
    """


class BusBItemAudioDataPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUDio:DATa:POLarity`` command.

    Description:
        - Specifies the data polarity for the AUDIO bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:DATa:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:DATa:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:DATa:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUDio:DATa:POLarity {NORMal|INVERTed}
        - BUS:B<x>:AUDio:DATa:POLarity?
        ```

    Info:
        - ``NORMal`` specifies positive data polarity for the audio bus.
        - ``INVERTed`` specifies negative data polarity for the audio bus.
    """


class BusBItemAudioData(SCPICmdRead):
    """The ``BUS:B<x>:AUDio:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:DATa?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:AUDio:DATa:POLarity`` command.
        - ``.size``: The ``BUS:B<x>:AUDio:DATa:SIZe`` command.
        - ``.source``: The ``BUS:B<x>:AUDio:DATa:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemAudioDataPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._size = BusBItemAudioDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._source = BusBItemAudioDataSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def polarity(self) -> BusBItemAudioDataPolarity:
        """Return the ``BUS:B<x>:AUDio:DATa:POLarity`` command.

        Description:
            - Specifies the data polarity for the AUDIO bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:DATa:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:DATa:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:AUDio:DATa:POLarity value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUDio:DATa:POLarity {NORMal|INVERTed}
            - BUS:B<x>:AUDio:DATa:POLarity?
            ```

        Info:
            - ``NORMal`` specifies positive data polarity for the audio bus.
            - ``INVERTed`` specifies negative data polarity for the audio bus.
        """
        return self._polarity

    @property
    def size(self) -> BusBItemAudioDataSize:
        """Return the ``BUS:B<x>:AUDio:DATa:SIZe`` command.

        Description:
            - This command sets or queries the number of bits per channel for the specified audio
              bus. This command only applies to the TDM Audio type. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:DATa:SIZe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:DATa:SIZe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:DATa:SIZe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUDio:DATa:SIZe <NR1>
            - BUS:B<x>:AUDio:DATa:SIZe?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``NR1`` specifies the number of bits per word.
        """
        return self._size

    @property
    def source(self) -> BusBItemAudioDataSource:
        """Return the ``BUS:B<x>:AUDio:DATa:SOUrce`` command.

        Description:
            - Specifies the data source waveform for the AUDIO bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:DATa:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:DATa:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:DATa:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUDio:DATa:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:AUDio:DATa:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the data source waveform for the audio bus.
            - ``D<x>`` specifies a digital channel as the data source waveform for the audio bus.
              (Requires option 3-MSO.).
        """
        return self._source


class BusBItemAudioClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUDio:CLOCk:SOUrce`` command.

    Description:
        - Specifies the clock source waveform for the AUDIO bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:CLOCk:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:CLOCk:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUDio:CLOCk:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:AUDio:CLOCk:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the clock source waveform for the audio bus.
        - ``D<x>`` specifies a digital channel as the clock source waveform for the audio bus.
          (Requires installation of option 3-MSO.).
    """


class BusBItemAudioClockPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUDio:CLOCk:POLarity`` command.

    Description:
        - Specifies the clock polarity for the AUDIO bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:CLOCk:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:CLOCk:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:CLOCk:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUDio:CLOCk:POLarity {FALL|RISe}
        - BUS:B<x>:AUDio:CLOCk:POLarity?
        ```

    Info:
        - ``FALL`` sets falling edge as the clock polarity.
        - ``RISe`` sets rising edge as the clock polarity.
    """


class BusBItemAudioClock(SCPICmdRead):
    """The ``BUS:B<x>:AUDio:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:CLOCk?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:AUDio:CLOCk:POLarity`` command.
        - ``.source``: The ``BUS:B<x>:AUDio:CLOCk:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemAudioClockPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemAudioClockSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def polarity(self) -> BusBItemAudioClockPolarity:
        """Return the ``BUS:B<x>:AUDio:CLOCk:POLarity`` command.

        Description:
            - Specifies the clock polarity for the AUDIO bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:CLOCk:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:CLOCk:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:AUDio:CLOCk:POLarity value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUDio:CLOCk:POLarity {FALL|RISe}
            - BUS:B<x>:AUDio:CLOCk:POLarity?
            ```

        Info:
            - ``FALL`` sets falling edge as the clock polarity.
            - ``RISe`` sets rising edge as the clock polarity.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemAudioClockSource:
        """Return the ``BUS:B<x>:AUDio:CLOCk:SOUrce`` command.

        Description:
            - Specifies the clock source waveform for the AUDIO bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:CLOCk:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:CLOCk:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:CLOCk:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUDio:CLOCk:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:AUDio:CLOCk:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the clock source waveform for the audio bus.
            - ``D<x>`` specifies a digital channel as the clock source waveform for the audio bus.
              (Requires installation of option 3-MSO.).
        """
        return self._source


class BusBItemAudioChannelSize(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUDio:CHANnel:SIZe`` command.

    Description:
        - Specifies the number of bits per channel for the AUDIO bus. (To specify the number of bits
          per word, use ``BUS:BX:AUDIO:DATA:SIZE``).

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:CHANnel:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:CHANnel:SIZe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:CHANnel:SIZe value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUDio:CHANnel:SIZe <NR1>
        - BUS:B<x>:AUDio:CHANnel:SIZe?
        ```

    Info:
        - ``<NR1>`` specifies the number of bits per channel.
    """


class BusBItemAudioChannel(SCPICmdRead):
    """The ``BUS:B<x>:AUDio:CHANnel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:CHANnel?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:CHANnel?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.size``: The ``BUS:B<x>:AUDio:CHANnel:SIZe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._size = BusBItemAudioChannelSize(device, f"{self._cmd_syntax}:SIZe")

    @property
    def size(self) -> BusBItemAudioChannelSize:
        """Return the ``BUS:B<x>:AUDio:CHANnel:SIZe`` command.

        Description:
            - Specifies the number of bits per channel for the AUDIO bus. (To specify the number of
              bits per word, use ``BUS:BX:AUDIO:DATA:SIZE``).

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:CHANnel:SIZe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:CHANnel:SIZe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:CHANnel:SIZe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUDio:CHANnel:SIZe <NR1>
            - BUS:B<x>:AUDio:CHANnel:SIZe?
            ```

        Info:
            - ``<NR1>`` specifies the number of bits per channel.
        """
        return self._size


class BusBItemAudioBitorder(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUDio:BITOrder`` command.

    Description:
        - Specifies the bit order for the specified AUDIO bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:BITOrder?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:BITOrder?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:BITOrder value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUDio:BITOrder {MSB|LSB}
        - BUS:B<x>:AUDio:BITOrder?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``MSB`` specifies that the most significant bit will be expected first in the order.
        - ``LSB`` specifies that the least significant bit will be expected first in the order.
    """


class BusBItemAudioBitdelay(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUDio:BITDelay`` command.

    Description:
        - This command sets or queries the number of delay bits for the specified AUDIO bus. The bus
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:BITDelay?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:BITDelay?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:BITDelay value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUDio:BITDelay <NR1>
        - BUS:B<x>:AUDio:BITDelay?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` specifies the number of delay bits.
    """


#  pylint: disable=too-many-instance-attributes
class BusBItemAudio(SCPICmdRead):
    """The ``BUS:B<x>:AUDio`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.bitdelay``: The ``BUS:B<x>:AUDio:BITDelay`` command.
        - ``.bitorder``: The ``BUS:B<x>:AUDio:BITOrder`` command.
        - ``.channel``: The ``BUS:B<x>:AUDio:CHANnel`` command tree.
        - ``.clock``: The ``BUS:B<x>:AUDio:CLOCk`` command tree.
        - ``.data``: The ``BUS:B<x>:AUDio:DATa`` command tree.
        - ``.display``: The ``BUS:B<x>:AUDio:DISplay`` command tree.
        - ``.frame``: The ``BUS:B<x>:AUDio:FRAME`` command tree.
        - ``.framesync``: The ``BUS:B<x>:AUDio:FRAMESync`` command tree.
        - ``.type``: The ``BUS:B<x>:AUDio:TYPe`` command.
        - ``.wordsel``: The ``BUS:B<x>:AUDio:WORDSel`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitdelay = BusBItemAudioBitdelay(device, f"{self._cmd_syntax}:BITDelay")
        self._bitorder = BusBItemAudioBitorder(device, f"{self._cmd_syntax}:BITOrder")
        self._channel = BusBItemAudioChannel(device, f"{self._cmd_syntax}:CHANnel")
        self._clock = BusBItemAudioClock(device, f"{self._cmd_syntax}:CLOCk")
        self._data = BusBItemAudioData(device, f"{self._cmd_syntax}:DATa")
        self._display = BusBItemAudioDisplay(device, f"{self._cmd_syntax}:DISplay")
        self._frame = BusBItemAudioFrame(device, f"{self._cmd_syntax}:FRAME")
        self._framesync = BusBItemAudioFramesync(device, f"{self._cmd_syntax}:FRAMESync")
        self._type = BusBItemAudioType(device, f"{self._cmd_syntax}:TYPe")
        self._wordsel = BusBItemAudioWordsel(device, f"{self._cmd_syntax}:WORDSel")

    @property
    def bitdelay(self) -> BusBItemAudioBitdelay:
        """Return the ``BUS:B<x>:AUDio:BITDelay`` command.

        Description:
            - This command sets or queries the number of delay bits for the specified AUDIO bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:BITDelay?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:BITDelay?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:BITDelay value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUDio:BITDelay <NR1>
            - BUS:B<x>:AUDio:BITDelay?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` specifies the number of delay bits.
        """
        return self._bitdelay

    @property
    def bitorder(self) -> BusBItemAudioBitorder:
        """Return the ``BUS:B<x>:AUDio:BITOrder`` command.

        Description:
            - Specifies the bit order for the specified AUDIO bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:BITOrder?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:BITOrder?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:BITOrder value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUDio:BITOrder {MSB|LSB}
            - BUS:B<x>:AUDio:BITOrder?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``MSB`` specifies that the most significant bit will be expected first in the order.
            - ``LSB`` specifies that the least significant bit will be expected first in the order.
        """
        return self._bitorder

    @property
    def channel(self) -> BusBItemAudioChannel:
        """Return the ``BUS:B<x>:AUDio:CHANnel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:CHANnel?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:CHANnel?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.size``: The ``BUS:B<x>:AUDio:CHANnel:SIZe`` command.
        """
        return self._channel

    @property
    def clock(self) -> BusBItemAudioClock:
        """Return the ``BUS:B<x>:AUDio:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:CLOCk?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:AUDio:CLOCk:POLarity`` command.
            - ``.source``: The ``BUS:B<x>:AUDio:CLOCk:SOUrce`` command.
        """
        return self._clock

    @property
    def data(self) -> BusBItemAudioData:
        """Return the ``BUS:B<x>:AUDio:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:DATa?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:AUDio:DATa:POLarity`` command.
            - ``.size``: The ``BUS:B<x>:AUDio:DATa:SIZe`` command.
            - ``.source``: The ``BUS:B<x>:AUDio:DATa:SOUrce`` command.
        """
        return self._data

    @property
    def display(self) -> BusBItemAudioDisplay:
        """Return the ``BUS:B<x>:AUDio:DISplay`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:DISplay?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:DISplay?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.format``: The ``BUS:B<x>:AUDio:DISplay:FORMat`` command.
        """
        return self._display

    @property
    def frame(self) -> BusBItemAudioFrame:
        """Return the ``BUS:B<x>:AUDio:FRAME`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:FRAME?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:FRAME?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.size``: The ``BUS:B<x>:AUDio:FRAME:SIZe`` command.
        """
        return self._frame

    @property
    def framesync(self) -> BusBItemAudioFramesync:
        """Return the ``BUS:B<x>:AUDio:FRAMESync`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:FRAMESync?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:FRAMESync?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:AUDio:FRAMESync:POLarity`` command.
            - ``.source``: The ``BUS:B<x>:AUDio:FRAMESync:SOUrce`` command.
        """
        return self._framesync

    @property
    def type(self) -> BusBItemAudioType:
        """Return the ``BUS:B<x>:AUDio:TYPe`` command.

        Description:
            - This command sets or queries the audio format (type) for the specified audio bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:TYPe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:TYPe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUDio:TYPe {I2S|LJ|RJ|TDM}
            - BUS:B<x>:AUDio:TYPe?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``I2S`` specifies the I2S audio format.
            - ``LJ`` specifies the left-justified audio format.
            - ``RJ`` specifies the right-justified audio format.
            - ``TDM`` specifies the time-division multiplexing audio format.
        """
        return self._type

    @property
    def wordsel(self) -> BusBItemAudioWordsel:
        """Return the ``BUS:B<x>:AUDio:WORDSel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:WORDSel?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:WORDSel?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:AUDio:WORDSel:POLarity`` command.
            - ``.source``: The ``BUS:B<x>:AUDio:WORDSel:SOUrce`` command.
        """
        return self._wordsel


class BusBItemArinc429aSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ARINC429A:SOUrce`` command.

    Description:
        - This command specifies the source for the differential input for the ARINC429 bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ARINC429A:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ARINC429A:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ARINC429A:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ARINC429A:SOUrce {CH<x>|MATH|REF<x>}
        - BUS:B<x>:ARINC429A:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the source for the differential input.
        - ``MATH`` specifies the math waveform as the source for differential input.
        - ``REF<x>`` specifies a reference waveform as the source for differential input.
    """


class BusBItemArinc429aPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ARINC429A:POLarity`` command.

    Description:
        - This command sets the polarity of the ARINC429 bus (normal or inverted).

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ARINC429A:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ARINC429A:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ARINC429A:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ARINC429A:POLarity {NORMal|INVERTed}
        - BUS:B<x>:ARINC429A:POLarity?
        ```

    Info:
        - ``NORMal`` - A positive differential pulse in the first half of a bit period that then
          returns to zero differential represents a 1 on the differential source.
        - ``INVERTed`` - A positive differential pulse in the first half of a bit period that then
          returns to zero differential represents a 0 on the differential source.
    """


class BusBItemArinc429aDataFormat(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ARINC429A:DATA:FORMAT`` command.

    Description:
        - Specifies the format of the DATA field in ARINC429 packets on a bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ARINC429A:DATA:FORMAT?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ARINC429A:DATA:FORMAT?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ARINC429A:DATA:FORMAT value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ARINC429A:DATA:FORMAT {DATA|SDIDATA|SDIDATASSM}
        - BUS:B<x>:ARINC429A:DATA:FORMAT?
        ```

    Info:
        - ``DATA`` sets the ARINC429 DATA field width to 19 bits wide (covering bits 11 through 29
          of the 32 bit packet).
        - ``SDIDATA`` sets the ARINC429 DATA field width to 21 bits wide (covering bits 9 through 29
          of the 32 bit packet).
        - ``SDIDATASSM`` sets the ARINC429 DATA field width to 23 bits wide (covering bits 9 through
          31 of the 32 bit packet).
    """


class BusBItemArinc429aData(SCPICmdRead):
    """The ``BUS:B<x>:ARINC429A:DATA`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ARINC429A:DATA?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ARINC429A:DATA?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.format``: The ``BUS:B<x>:ARINC429A:DATA:FORMAT`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._format = BusBItemArinc429aDataFormat(device, f"{self._cmd_syntax}:FORMAT")

    @property
    def format(self) -> BusBItemArinc429aDataFormat:
        """Return the ``BUS:B<x>:ARINC429A:DATA:FORMAT`` command.

        Description:
            - Specifies the format of the DATA field in ARINC429 packets on a bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ARINC429A:DATA:FORMAT?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ARINC429A:DATA:FORMAT?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ARINC429A:DATA:FORMAT value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ARINC429A:DATA:FORMAT {DATA|SDIDATA|SDIDATASSM}
            - BUS:B<x>:ARINC429A:DATA:FORMAT?
            ```

        Info:
            - ``DATA`` sets the ARINC429 DATA field width to 19 bits wide (covering bits 11 through
              29 of the 32 bit packet).
            - ``SDIDATA`` sets the ARINC429 DATA field width to 21 bits wide (covering bits 9
              through 29 of the 32 bit packet).
            - ``SDIDATASSM`` sets the ARINC429 DATA field width to 23 bits wide (covering bits 9
              through 31 of the 32 bit packet).
        """
        return self._format


class BusBItemArinc429aBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ARINC429A:BITRate`` command.

    Description:
        - This command specifies the bit rate for the ARINC429 bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ARINC429A:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ARINC429A:BITRate?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ARINC429A:BITRate value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ARINC429A:BITRate {LOW|HI|<NR1>}
        - BUS:B<x>:ARINC429A:BITRate?
        ```

    Info:
        - ``LOW`` sets the ARINC429 bit rate to handle low speed signals (12000 bits-per-second to
          14500 bits-per-second).
        - ``HI`` sets the ARINC429 bit rate to handle high speed signals (100,000 bits-per-second).
        - ``<NR1>`` is a bit rate in bits-per-second. You can enter any positive integer, and the
          instrument will coerce the value to the closest supported bit rate.
    """


class BusBItemArinc429a(SCPICmdRead):
    """The ``BUS:B<x>:ARINC429A`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ARINC429A?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ARINC429A?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:ARINC429A:BITRate`` command.
        - ``.data``: The ``BUS:B<x>:ARINC429A:DATA`` command tree.
        - ``.polarity``: The ``BUS:B<x>:ARINC429A:POLarity`` command.
        - ``.source``: The ``BUS:B<x>:ARINC429A:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemArinc429aBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._data = BusBItemArinc429aData(device, f"{self._cmd_syntax}:DATA")
        self._polarity = BusBItemArinc429aPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemArinc429aSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def bitrate(self) -> BusBItemArinc429aBitrate:
        """Return the ``BUS:B<x>:ARINC429A:BITRate`` command.

        Description:
            - This command specifies the bit rate for the ARINC429 bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ARINC429A:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ARINC429A:BITRate?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:ARINC429A:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ARINC429A:BITRate {LOW|HI|<NR1>}
            - BUS:B<x>:ARINC429A:BITRate?
            ```

        Info:
            - ``LOW`` sets the ARINC429 bit rate to handle low speed signals (12000 bits-per-second
              to 14500 bits-per-second).
            - ``HI`` sets the ARINC429 bit rate to handle high speed signals (100,000
              bits-per-second).
            - ``<NR1>`` is a bit rate in bits-per-second. You can enter any positive integer, and
              the instrument will coerce the value to the closest supported bit rate.
        """
        return self._bitrate

    @property
    def data(self) -> BusBItemArinc429aData:
        """Return the ``BUS:B<x>:ARINC429A:DATA`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ARINC429A:DATA?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ARINC429A:DATA?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.format``: The ``BUS:B<x>:ARINC429A:DATA:FORMAT`` command.
        """
        return self._data

    @property
    def polarity(self) -> BusBItemArinc429aPolarity:
        """Return the ``BUS:B<x>:ARINC429A:POLarity`` command.

        Description:
            - This command sets the polarity of the ARINC429 bus (normal or inverted).

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ARINC429A:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ARINC429A:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:ARINC429A:POLarity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ARINC429A:POLarity {NORMal|INVERTed}
            - BUS:B<x>:ARINC429A:POLarity?
            ```

        Info:
            - ``NORMal`` - A positive differential pulse in the first half of a bit period that then
              returns to zero differential represents a 1 on the differential source.
            - ``INVERTed`` - A positive differential pulse in the first half of a bit period that
              then returns to zero differential represents a 0 on the differential source.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemArinc429aSource:
        """Return the ``BUS:B<x>:ARINC429A:SOUrce`` command.

        Description:
            - This command specifies the source for the differential input for the ARINC429 bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ARINC429A:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ARINC429A:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:ARINC429A:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ARINC429A:SOUrce {CH<x>|MATH|REF<x>}
            - BUS:B<x>:ARINC429A:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the source for the differential input.
            - ``MATH`` specifies the math waveform as the source for differential input.
            - ``REF<x>`` specifies a reference waveform as the source for differential input.
        """
        return self._source


#  pylint: disable=too-many-instance-attributes
class BusBItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``BUS:B<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.arinc429a``: The ``BUS:B<x>:ARINC429A`` command tree.
        - ``.audio``: The ``BUS:B<x>:AUDio`` command tree.
        - ``.can``: The ``BUS:B<x>:CAN`` command tree.
        - ``.display``: The ``BUS:B<x>:DISplay`` command tree.
        - ``.ethernet``: The ``BUS:B<x>:ETHERnet`` command tree.
        - ``.flexray``: The ``BUS:B<x>:FLEXray`` command tree.
        - ``.i2c``: The ``BUS:B<x>:I2C`` command tree.
        - ``.label``: The ``BUS:B<x>:LABel`` command.
        - ``.lin``: The ``BUS:B<x>:LIN`` command tree.
        - ``.mil1553b``: The ``BUS:B<x>:MIL1553B`` command tree.
        - ``.parallel``: The ``BUS:B<x>:PARallel`` command tree.
        - ``.position``: The ``BUS:B<x>:POSition`` command.
        - ``.rs232c``: The ``BUS:B<x>:RS232C`` command tree.
        - ``.sent``: The ``BUS:B<x>:SENT`` command tree.
        - ``.spi``: The ``BUS:B<x>:SPI`` command tree.
        - ``.state``: The ``BUS:B<x>:STATE`` command.
        - ``.type``: The ``BUS:B<x>:TYPe`` command.
        - ``.usb``: The ``BUS:B<x>:USB`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._arinc429a = BusBItemArinc429a(device, f"{self._cmd_syntax}:ARINC429A")
        self._audio = BusBItemAudio(device, f"{self._cmd_syntax}:AUDio")
        self._can = BusBItemCan(device, f"{self._cmd_syntax}:CAN")
        self._display = BusBItemDisplay(device, f"{self._cmd_syntax}:DISplay")
        self._ethernet = BusBItemEthernet(device, f"{self._cmd_syntax}:ETHERnet")
        self._flexray = BusBItemFlexray(device, f"{self._cmd_syntax}:FLEXray")
        self._i2c = BusBItemI2c(device, f"{self._cmd_syntax}:I2C")
        self._label = BusBItemLabel(device, f"{self._cmd_syntax}:LABel")
        self._lin = BusBItemLin(device, f"{self._cmd_syntax}:LIN")
        self._mil1553b = BusBItemMil1553b(device, f"{self._cmd_syntax}:MIL1553B")
        self._parallel = BusBItemParallel(device, f"{self._cmd_syntax}:PARallel")
        self._position = BusBItemPosition(device, f"{self._cmd_syntax}:POSition")
        self._rs232c = BusBItemRs232c(device, f"{self._cmd_syntax}:RS232C")
        self._sent = BusBItemSent(device, f"{self._cmd_syntax}:SENT")
        self._spi = BusBItemSpi(device, f"{self._cmd_syntax}:SPI")
        self._state = BusBItemState(device, f"{self._cmd_syntax}:STATE")
        self._type = BusBItemType(device, f"{self._cmd_syntax}:TYPe")
        self._usb = BusBItemUsb(device, f"{self._cmd_syntax}:USB")

    @property
    def arinc429a(self) -> BusBItemArinc429a:
        """Return the ``BUS:B<x>:ARINC429A`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ARINC429A?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ARINC429A?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:ARINC429A:BITRate`` command.
            - ``.data``: The ``BUS:B<x>:ARINC429A:DATA`` command tree.
            - ``.polarity``: The ``BUS:B<x>:ARINC429A:POLarity`` command.
            - ``.source``: The ``BUS:B<x>:ARINC429A:SOUrce`` command.
        """
        return self._arinc429a

    @property
    def audio(self) -> BusBItemAudio:
        """Return the ``BUS:B<x>:AUDio`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.bitdelay``: The ``BUS:B<x>:AUDio:BITDelay`` command.
            - ``.bitorder``: The ``BUS:B<x>:AUDio:BITOrder`` command.
            - ``.channel``: The ``BUS:B<x>:AUDio:CHANnel`` command tree.
            - ``.clock``: The ``BUS:B<x>:AUDio:CLOCk`` command tree.
            - ``.data``: The ``BUS:B<x>:AUDio:DATa`` command tree.
            - ``.display``: The ``BUS:B<x>:AUDio:DISplay`` command tree.
            - ``.frame``: The ``BUS:B<x>:AUDio:FRAME`` command tree.
            - ``.framesync``: The ``BUS:B<x>:AUDio:FRAMESync`` command tree.
            - ``.type``: The ``BUS:B<x>:AUDio:TYPe`` command.
            - ``.wordsel``: The ``BUS:B<x>:AUDio:WORDSel`` command tree.
        """
        return self._audio

    @property
    def can(self) -> BusBItemCan:
        """Return the ``BUS:B<x>:CAN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:CAN:BITRate`` command.
            - ``.fd``: The ``BUS:B<x>:CAN:FD`` command tree.
            - ``.probe``: The ``BUS:B<x>:CAN:PRObe`` command.
            - ``.samplepoint``: The ``BUS:B<x>:CAN:SAMPLEpoint`` command.
            - ``.source``: The ``BUS:B<x>:CAN:SOUrce`` command.
            - ``.standard``: The ``BUS:B<x>:CAN:STANDard`` command.
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
            - ``.format``: The ``BUS:B<x>:DISplay:FORMat`` command.
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
            - ``.protocol``: The ``BUS:B<x>:ETHERnet:PROTOcol`` command.
            - ``.probe``: The ``BUS:B<x>:ETHERnet:PRObe`` command.
            - ``.source``: The ``BUS:B<x>:ETHERnet:SOUrce`` command tree.
            - ``.type``: The ``BUS:B<x>:ETHERnet:TYPe`` command.
        """
        return self._ethernet

    @property
    def flexray(self) -> BusBItemFlexray:
        """Return the ``BUS:B<x>:FLEXray`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:FLEXray:BITRate`` command.
            - ``.channel``: The ``BUS:B<x>:FLEXray:CHannel`` command.
            - ``.signal``: The ``BUS:B<x>:FLEXray:SIGnal`` command.
            - ``.source``: The ``BUS:B<x>:FLEXray:SOUrce`` command.
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
            - ``.address``: The ``BUS:B<x>:I2C:ADDRess`` command tree.
            - ``.clock``: The ``BUS:B<x>:I2C:CLOCk`` command tree.
            - ``.sclk``: The ``BUS:B<x>:I2C:SCLk`` command tree.
            - ``.data``: The ``BUS:B<x>:I2C:DATa`` command tree.
            - ``.sdata``: The ``BUS:B<x>:I2C:SDAta`` command tree.
        """
        return self._i2c

    @property
    def label(self) -> BusBItemLabel:
        """Return the ``BUS:B<x>:LABel`` command.

        Description:
            - Specifies the waveform label for the bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LABel <Qstring>
            - BUS:B<x>:LABel?
            ```

        Info:
            - ``<Qstring>`` is an alphanumeric string of text, enclosed in quotes, that contains the
              text label information for bus <x>. The text string is limited to 30 characters.
        """
        return self._label

    @property
    def lin(self) -> BusBItemLin:
        """Return the ``BUS:B<x>:LIN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:LIN:BITRate`` command.
            - ``.idformat``: The ``BUS:B<x>:LIN:IDFORmat`` command.
            - ``.maxbytedelim``: The ``BUS:B<x>:LIN:MAXBytedelim`` command.
            - ``.polarity``: The ``BUS:B<x>:LIN:POLarity`` command.
            - ``.samplepoint``: The ``BUS:B<x>:LIN:SAMPLEpoint`` command.
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

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:MIL1553B:POLarity`` command.
            - ``.responsetime``: The ``BUS:B<x>:MIL1553B:RESPonsetime`` command tree.
            - ``.source``: The ``BUS:B<x>:MIL1553B:SOUrce`` command.
        """
        return self._mil1553b

    @property
    def parallel(self) -> BusBItemParallel:
        """Return the ``BUS:B<x>:PARallel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bit``: The ``BUS:B<x>:PARallel:BIT<x>`` command tree.
            - ``.clock``: The ``BUS:B<x>:PARallel:CLOCk`` command tree.
            - ``.width``: The ``BUS:B<x>:PARallel:WIDth`` command.
        """
        return self._parallel

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
            - ``.rx``: The ``BUS:B<x>:RS232C:RX`` command tree.
            - ``.tx``: The ``BUS:B<x>:RS232C:TX`` command tree.
        """
        return self._rs232c

    @property
    def sent(self) -> BusBItemSent:
        """Return the ``BUS:B<x>:SENT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SENT?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.chanwidth``: The ``BUS:B<x>:SENT:CHANWidth`` command.
            - ``.nibblecount``: The ``BUS:B<x>:SENT:NIBBLECount`` command.
            - ``.numchannel``: The ``BUS:B<x>:SENT:NUMCHANnel`` command.
            - ``.pausepulse``: The ``BUS:B<x>:SENT:PAUSEPULSe`` command.
            - ``.polarity``: The ``BUS:B<x>:SENT:POLARITY`` command.
            - ``.slow``: The ``BUS:B<x>:SENT:SLOW`` command.
            - ``.source``: The ``BUS:B<x>:SENT:SOUrce`` command.
            - ``.ticktime``: The ``BUS:B<x>:SENT:TICKTIME`` command.
            - ``.ticktolerance``: The ``BUS:B<x>:SENT:TICKTOLerance`` command.
        """
        return self._sent

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
            - ``.data``: The ``BUS:B<x>:SPI:DATa`` command tree.
            - ``.framing``: The ``BUS:B<x>:SPI:FRAMING`` command.
            - ``.idletime``: The ``BUS:B<x>:SPI:IDLETime`` command.
            - ``.clock``: The ``BUS:B<x>:SPI:CLOCk`` command tree.
            - ``.sclk``: The ``BUS:B<x>:SPI:SCLk`` command tree.
            - ``.select``: The ``BUS:B<x>:SPI:SELect`` command tree.
            - ``.ss``: The ``BUS:B<x>:SPI:SS`` command tree.
        """
        return self._spi

    @property
    def state(self) -> BusBItemState:
        """Return the ``BUS:B<x>:STATE`` command.

        Description:
            - This command specifies the on/off state of the bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:STATE?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:STATE value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:STATE {ON|OFF|<NR1>}
            - BUS:B<x>:STATE?
            ```

        Info:
            - ``ON`` or <NR1> ≠ 0 turns on the bus.
            - ``OFF`` or <NR1> = 0 turns off the bus.
        """
        return self._state

    @property
    def type(self) -> BusBItemType:
        """Return the ``BUS:B<x>:TYPe`` command.

        Description:
            - This command specifies (or queries) the bus type. The supported bus types are
              dependent on the oscilloscope model and the installed application models. With the
              exception of the parallel bus, all bus types require installation of an application
              option.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:TYPe?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:TYPe value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:TYPe {I2C|SPI|CAN|RS232C|PARallel|USB|LIN|FLEXRay|AUDio|ETHERnet|MIL1553B|ARINC429A}
            - BUS:B<x>:TYPe?
            ```

        Info:
            - ``I2C`` specifies the Inter-IC bus.
            - ``SPI`` specifies the Serial Peripheral Interface bus (not available on two-channel
              models).
            - ``CAN`` specifies the Controller Area Network bus.
            - ``RS232C`` specifies the RS-232C bus.
            - ``PARallel`` specifies the Parallel bus.
            - ``USB`` specifies the USB bus.
            - ``LIN`` specifies the LIN bus.
            - ``FLEXRay`` specifies the FLexRay bus.
            - ``AUDio`` specifies the audio bus.
            - ``ETHERnet`` specifies the Ethernet bus.
            - ``MIL1553B`` specifies the MIL-STD-1553 bus.
            - ``ARINC429A`` specifies the Aeronautical Radio INC (specification 429) bus.
        """  # noqa: E501
        return self._type

    @property
    def usb(self) -> BusBItemUsb:
        """Return the ``BUS:B<x>:USB`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:USB?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:USB:BITRate`` command.
            - ``.probe``: The ``BUS:B<x>:USB:PRObe`` command.
            - ``.source``: The ``BUS:B<x>:USB:SOUrce`` command tree.
        """
        return self._usb


class Bus(SCPICmdRead):
    """The ``BUS`` command.

    Description:
        - Returns the parameters for each serial (if installed) and parallel bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - BUS?
        ```

    Properties:
        - ``.b``: The ``BUS:B<x>`` command tree.
        - ``.lowerthreshold``: The ``BUS:LOWerthreshold`` command tree.
        - ``.threshold``: The ``BUS:THReshold`` command tree.
        - ``.upperthreshold``: The ``BUS:UPPerthreshold`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "BUS") -> None:
        super().__init__(device, cmd_syntax)
        self._b: Dict[int, BusBItem] = DefaultDictPassKeyToFactory(
            lambda x: BusBItem(device, f"{self._cmd_syntax}:B{x}")
        )
        self._lowerthreshold = BusLowerthreshold(device, f"{self._cmd_syntax}:LOWerthreshold")
        self._threshold = BusThreshold(device, f"{self._cmd_syntax}:THReshold")
        self._upperthreshold = BusUpperthreshold(device, f"{self._cmd_syntax}:UPPerthreshold")

    @property
    def b(self) -> Dict[int, BusBItem]:
        """Return the ``BUS:B<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.arinc429a``: The ``BUS:B<x>:ARINC429A`` command tree.
            - ``.audio``: The ``BUS:B<x>:AUDio`` command tree.
            - ``.can``: The ``BUS:B<x>:CAN`` command tree.
            - ``.display``: The ``BUS:B<x>:DISplay`` command tree.
            - ``.ethernet``: The ``BUS:B<x>:ETHERnet`` command tree.
            - ``.flexray``: The ``BUS:B<x>:FLEXray`` command tree.
            - ``.i2c``: The ``BUS:B<x>:I2C`` command tree.
            - ``.label``: The ``BUS:B<x>:LABel`` command.
            - ``.lin``: The ``BUS:B<x>:LIN`` command tree.
            - ``.mil1553b``: The ``BUS:B<x>:MIL1553B`` command tree.
            - ``.parallel``: The ``BUS:B<x>:PARallel`` command tree.
            - ``.position``: The ``BUS:B<x>:POSition`` command.
            - ``.rs232c``: The ``BUS:B<x>:RS232C`` command tree.
            - ``.sent``: The ``BUS:B<x>:SENT`` command tree.
            - ``.spi``: The ``BUS:B<x>:SPI`` command tree.
            - ``.state``: The ``BUS:B<x>:STATE`` command.
            - ``.type``: The ``BUS:B<x>:TYPe`` command.
            - ``.usb``: The ``BUS:B<x>:USB`` command tree.
        """
        return self._b

    @property
    def lowerthreshold(self) -> BusLowerthreshold:
        """Return the ``BUS:LOWerthreshold`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:LOWerthreshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:LOWerthreshold?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``BUS:LOWerthreshold:CH<x>`` command.
            - ``.ref``: The ``BUS:LOWerthreshold:REF<x>`` command.
            - ``.math``: The ``BUS:LOWerthreshold:MATH`` command.
            - ``.math1``: The ``BUS:LOWerthreshold:MATH1`` command.
        """
        return self._lowerthreshold

    @property
    def threshold(self) -> BusThreshold:
        """Return the ``BUS:THReshold`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:THReshold?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``BUS:THReshold:CH<x>`` command.
            - ``.d``: The ``BUS:THReshold:D<x>`` command.
        """
        return self._threshold

    @property
    def upperthreshold(self) -> BusUpperthreshold:
        """Return the ``BUS:UPPerthreshold`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:UPPerthreshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:UPPerthreshold?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``BUS:UPPerthreshold:CH<x>`` command.
            - ``.ref``: The ``BUS:UPPerthreshold:REF<x>`` command.
            - ``.math``: The ``BUS:UPPerthreshold:MATH`` command.
            - ``.math1``: The ``BUS:UPPerthreshold:MATH1`` command.
        """
        return self._upperthreshold
