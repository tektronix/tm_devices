# pylint: disable=line-too-long
"""The search commands module.

These commands are used in the following models:
DPO2K, DPO2KB, MSO2K, MSO2KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SEARCH:SEARCH<x>:COPy {SEARCHtotrigger|TRIGgertosearch}
    - SEARCH:SEARCH<x>:STATE {ON|OFF|<NR1>}
    - SEARCH:SEARCH<x>:STATE?
    - SEARCH:SEARCH<x>:TOTAL?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe {STandard|EXTended}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue <bin>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:CONDition {SOF|FRAMEtype|IDentifier|DATA|IDANDDATA|EOF|ACKMISS|ERROR}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:CONDition?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:DIRection {READ|WRITE|NOCARE}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:DIRection?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier {LESSThan|MOREThan|UNEQual|LESSEQual|MOREEQual|EQual}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:SIZe <NR1>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:SIZe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:VALue <bin>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FRAMEtype {DATA|REMote|ERRor|OVERLoad}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FRAMEtype?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe {STandard|EXTended}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue <bin>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CONDition {SOF|FRAMETypeid|CYCLEcount|HEADer|DATA|IDANDDATA|EOF|ERROR}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CONDition?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet <NR1>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe <NR1>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE {STATic|DYNAMic|ANY}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE {CRCHeader|CRCTrailer|SYNCFrame|STARTupnosync|NULLFRStatic|NULLFRDynamic}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEType {NORMal|PAYLoad|NULL|SYNC|STARTup}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEType?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe {ADDR7|ADDR10}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe {GENeralcall|STARtbyte|HSmode|EEPROM|USER}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue <bin>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:CONDition {STARt|STOP|REPEATstart|ACKMISS|ADDRess|DATA|ADDRANDDATA}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:CONDition?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:DIRection {READ|WRITE|NOCARE}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:DIRection?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:SIZe <NR1>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:SIZe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:VALue <bin>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:CONDition {SYNCField|IDentifier|DATA|IDANDDATA|WAKEup|SLEEP|ERROR}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:CONDition?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:SIZe <NR1>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:SIZe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:ERRTYPE {SYNC|PARity|CHecksum}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:ERRTYPE?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:CONDition {RXSTArt|RXDATA|RXENDPacket|RXPARity|TXSTArt|TXDATA|TXENDPacket|TXPARity}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:CONDition?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:CONDition {SS|MISO|MOSI|MISOMOSI}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:CONDition?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue <bin>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue <bin>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue <bin>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue <bin>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:SIZe <NR1>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:SIZe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce {B<x>}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS?
    - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe {RISe|FALL}
    - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe?
    - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce {CH<x>|MATH}
    - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce?
    - SEARCH:SEARCH<x>:TRIGger:A:LEVel {<NR3>|TTL|ECL}
    - SEARCH:SEARCH<x>:TRIGger:A:LEVel:CH<x> {<NR3>|TTL|ECL}
    - SEARCH:SEARCH<x>:TRIGger:A:LEVel:CH<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LEVel:MATH {TTL|ECL}
    - SEARCH:SEARCH<x>:TRIGger:A:LEVel:MATH?
    - SEARCH:SEARCH<x>:TRIGger:A:LEVel:REF<x> {TTL|ECL}
    - SEARCH:SEARCH<x>:TRIGger:A:LEVel:REF<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LEVel?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion {AND|NANd}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CH<x> {HIGH|LOW|X}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CH<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:EDGE {FALL|RISe|EITher}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:EDGE?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:SOUrce {CH<x>|MATH|REF|D<x>|NONe}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:D<x> {HIGH|LOW|X}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:D<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:MATH {HIGH|LOW|X}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:MATH?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:REF<x> {HIGH|LOW|X}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:REF<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:CH<x> {HIGH|LOW|X}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:CH<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:D<x> {HIGH|LOW|X}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:D<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:MATH {HIGH|LOW|X}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:MATH?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:REF<x> {HIGH|LOW|X}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:REF<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn {TRUe|FALSe|LESSThan|MOREThan|Than|EQUal|UNEQual}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:MORELimit <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:MORELimit?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:CH<x> {<NR3>|TTL|ECL}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:CH<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:MATH {TTL|ECL|<NR3>}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:MATH?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:REF<x> {TTL|ECL|<NR3>}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:REF<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:CH<x> {TTL|ECL|<NR3>}
    - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:CH<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:MATH {TTL|ECL|<NR3>}
    - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:MATH?
    - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:REF<x> {TTL|ECL|<NR3>}
    - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:REF<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity {NEGative|POSitive}
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity?
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce {CH<x>|MATH|REF}
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce?
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn {LESSthan|MOREthan|EQual|UNEQual}
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn?
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WIDth <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WIDth?
    - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:DELTatime <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:DELTatime?
    - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:POLarity {EITher|NEGative|POSitive}
    - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:POLarity?
    - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:SOUrce {CH<x>|MATH}
    - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:SOUrce?
    - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:WHEn {SLOWer|FASTer|EQual|UNEQual}
    - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:WHEn?
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity {EITher|NEGative|POSitive}
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity?
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce {CH<x>|MATH|REF}
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce?
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn {LESSthan|MOREthan|EQual|UNEQual|OCCURS}
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn?
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:EDGE {FALL|RISe}
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:EDGE?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce {CH<x>|MATH|REF}
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:THReshold {<NR3>|TTL|ECL}
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:THReshold?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:SOUrce DPO Models:{CH<x>|MATH|REF|D<x>}
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:SOUrce?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:THReshold {<NR3>|TTL|ECL}
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:THReshold?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:HOLDTime <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:HOLDTime?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:SETTime <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:SETTime?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:CH<x> <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:CH<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH1 <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH1?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:REF<x> <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:REF<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:DELTatime <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:DELTatime?
    - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:POLarity {EITher|NEGative|POSitive}
    - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:POLarity?
    - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:SOUrce {CH<x>|MATH}
    - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:SOUrce?
    - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:WHEn {SLOWer|FASTer|EQual|UNEQual}
    - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:WHEn?
    - SEARCH:SEARCH<x>:TRIGger:A:TYPe {EDGe|SETHold|PULSEWidth|RUNt|TRAnsition|LOGIc|BUS (with the appropriate application module installed)}
    - SEARCH:SEARCH<x>:TRIGger:A:TYPe?
    - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:CH<x> {TTL|ECL}
    - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:CH<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:MATH {TTL|ECL}
    - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:MATH?
    - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:REF<x> {TTL|ECL}
    - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:REF<x>?
    - SEARCH?
    ```
"""  # noqa: E501

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    SCPICmdWriteNoArguments,
    ValidatedChannel,
    ValidatedDigitalBit,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class SearchSearchItemTriggerAUpperthresholdRefItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead
):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:REF<x>`` command.

    Description:
        - Sets or returns the reference waveform upper threshold to determine where to place a mark.
          This setting is applied to all reference waveform searches that uses an upper threshold.
          SEARCH<x> is the search number and REF<x> is the reference channel number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:REF<x>?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:REF<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:REF<x> {TTL|ECL}
        - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:REF<x>?
        ```

    Info:
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
        - ``ECL`` specifies a preset ECL high level of -1.3 V.
    """


class SearchSearchItemTriggerAUpperthresholdMath(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:MATH`` command.

    Description:
        - Sets or returns the math waveform upper threshold to determine where to place a mark. This
          setting is applied to all math waveform searches that uses an upper threshold. <x> is the
          search number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:MATH?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:MATH?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:MATH value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:MATH {TTL|ECL}
        - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:MATH?
        ```

    Info:
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
        - ``ECL`` specifies a preset ECL high level of -1.3 V.
    """


class SearchSearchItemTriggerAUpperthresholdChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:CH<x>`` command.

    Description:
        - Sets or returns the channel waveform upper threshold to determine where to place a mark.
          This setting is applied to all channel searches that uses an upper threshold. SEARCH<x> is
          the search number and CH<x> is the channel number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:CH<x>?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:CH<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:CH<x> {TTL|ECL}
        - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:CH<x>?
        ```

    Info:
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
        - ``ECL`` specifies a preset ECL high level of -1.3 V.
    """


class SearchSearchItemTriggerAUpperthreshold(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:CH<x>`` command.
        - ``.math``: The ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:MATH`` command.
        - ``.ref``: The ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:REF<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, SearchSearchItemTriggerAUpperthresholdChannel] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerAUpperthresholdChannel(
                    device, f"{self._cmd_syntax}:CH{x}"
                )
            )
        )
        self._math = SearchSearchItemTriggerAUpperthresholdMath(device, f"{self._cmd_syntax}:MATH")
        self._ref: Dict[int, SearchSearchItemTriggerAUpperthresholdRefItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerAUpperthresholdRefItem(
                    device, f"{self._cmd_syntax}:REF{x}"
                )
            )
        )

    @property
    def ch(self) -> Dict[int, SearchSearchItemTriggerAUpperthresholdChannel]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:CH<x>`` command.

        Description:
            - Sets or returns the channel waveform upper threshold to determine where to place a
              mark. This setting is applied to all channel searches that uses an upper threshold.
              SEARCH<x> is the search number and CH<x> is the channel number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:CH<x>?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:CH<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:CH<x> {TTL|ECL}
            - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:CH<x>?
            ```

        Info:
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
            - ``ECL`` specifies a preset ECL high level of -1.3 V.
        """
        return self._ch

    @property
    def math(self) -> SearchSearchItemTriggerAUpperthresholdMath:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:MATH`` command.

        Description:
            - Sets or returns the math waveform upper threshold to determine where to place a mark.
              This setting is applied to all math waveform searches that uses an upper threshold.
              <x> is the search number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:MATH?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:MATH?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:MATH value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:MATH {TTL|ECL}
            - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:MATH?
            ```

        Info:
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
            - ``ECL`` specifies a preset ECL high level of -1.3 V.
        """
        return self._math

    @property
    def ref(self) -> Dict[int, SearchSearchItemTriggerAUpperthresholdRefItem]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:REF<x>`` command.

        Description:
            - Sets or returns the reference waveform upper threshold to determine where to place a
              mark. This setting is applied to all reference waveform searches that uses an upper
              threshold. SEARCH<x> is the search number and REF<x> is the reference channel number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:REF<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:REF<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:REF<x> {TTL|ECL}
            - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:REF<x>?
            ```

        Info:
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
            - ``ECL`` specifies a preset ECL high level of -1.3 V.
        """
        return self._ref


class SearchSearchItemTriggerAType(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:TYPe`` command.

    Description:
        - Sets or returns the trigger type setting for a search to determine where to place a mark.
          <x> is the search number.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:TYPe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:TYPe value``
          command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:TYPe {EDGe|SETHold|PULSEWidth|RUNt|TRAnsition|LOGIc|BUS (with the appropriate application module installed)}
        - SEARCH:SEARCH<x>:TRIGger:A:TYPe?
        ```

    Info:
        - ``RUNt`` triggers when a pulse crosses the first preset voltage threshold but does not
          cross the second preset threshold before recrossing the first. The thresholds are set with
          the ``SEARCH:SEARCHX:TRIGGER:A:LOWERTHRESHOLD:CHX`` and
          ``SEARCH:SEARCHX:TRIGGER:A:UPPERTHRESHOLD:CHX`` commands.
        - ``PULSEWIdth`` triggers when a pulse is found that has the specified polarity and is
          either inside or outside the limits as specified by
          ``SEARCH:SEARCHX:TRIGGER:A:LOGIC:PATTERN:WHEN:LESSLIMIT`` and
          ``SEARCH:SEARCHX:TRIGGER:A:LOGIC:PATTERN:WHEN:MORELIMIT``. The polarity is selected using
          the ``SEARCH:SEARCHX:TRIGGER:A:RUNT:POLARITY`` command.
        - ``TRAnsition`` triggers when a pulse crosses both thresholds in the same direction as the
          specified polarity and the transition time between the two threshold crossings is greater
          or less than the specified time delta.
    """  # noqa: E501


class SearchSearchItemTriggerATransitionWhen(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:WHEn`` command.

    Description:
        - This command specifies the condition for a transition search. SEARCH<x> is the search
          number, which is always 1.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:WHEn?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:WHEn?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:WHEn value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:WHEn {SLOWer|FASTer|EQual|UNEQual}
        - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:WHEn?
        ```

    Info:
        - ``FASTer`` sets the search to occur when the transitioning signal is faster than the set
          volts/second rate.
        - ``SLOWer`` sets the search to occur when the transitioning signal is slower than the set
          volts/second rate.
        - ``EQual`` sets the search to occur when the transitioning signal is equal to the set
          volts/second rate within a ±5% tolerance.
        - ``UNEQual`` sets the search to occur when the transitioning signal is not equal to the set
          volts/second rate ±5%.
    """


class SearchSearchItemTriggerATransitionSource(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:SOUrce`` command.

    Description:
        - Sets or returns the source setting for an transition trigger search to determine where to
          place a mark. <x> is the search number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:SOUrce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:SOUrce value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:SOUrce {CH<x>|MATH}
        - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies one input channel as the edge source. x has a minimum of 1 and a
          maximum of 4.
        - ``MATH`` specifies the math waveform as the search source.
    """


class SearchSearchItemTriggerATransitionPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:POLarity`` command.

    Description:
        - This command specifies the polarity setting for an transition search to determine where to
          place a mark. SEARCH<x> is the search number, which is always 1.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:POLarity?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:POLarity value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:POLarity {EITher|NEGative|POSitive}
        - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:POLarity?
        ```

    Info:
        - ``POSitive`` specifies that a pulse edge must traverse from the lower (most negative) to
          higher (most positive) level for transition searching to occur.
        - ``NEGative`` specifies that a pulse edge must traverse from the upper (most positive) to
          lower (most negative) level for transition searching to occur.
        - ``EITher`` specifies either positive or negative polarity.
    """


class SearchSearchItemTriggerATransitionDeltatime(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:DELTatime`` command.

    Description:
        - This command specifies the transition delta time setting to be used as the value to
          compare against when a transition time is found. < SEARCH<x> is the search number, which
          is always 1.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:DELTatime?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:DELTatime?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:DELTatime value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:DELTatime <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:DELTatime?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the transition time, in seconds.
    """


class SearchSearchItemTriggerATransition(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.deltatime``: The ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:DELTatime`` command.
        - ``.polarity``: The ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:POLarity`` command.
        - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:SOUrce`` command.
        - ``.when``: The ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:WHEn`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._deltatime = SearchSearchItemTriggerATransitionDeltatime(
            device, f"{self._cmd_syntax}:DELTatime"
        )
        self._polarity = SearchSearchItemTriggerATransitionPolarity(
            device, f"{self._cmd_syntax}:POLarity"
        )
        self._source = SearchSearchItemTriggerATransitionSource(
            device, f"{self._cmd_syntax}:SOUrce"
        )
        self._when = SearchSearchItemTriggerATransitionWhen(device, f"{self._cmd_syntax}:WHEn")

    @property
    def deltatime(self) -> SearchSearchItemTriggerATransitionDeltatime:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:DELTatime`` command.

        Description:
            - This command specifies the transition delta time setting to be used as the value to
              compare against when a transition time is found. < SEARCH<x> is the search number,
              which is always 1.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:DELTatime?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:DELTatime?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:DELTatime value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:DELTatime <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:DELTatime?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the transition time, in seconds.
        """
        return self._deltatime

    @property
    def polarity(self) -> SearchSearchItemTriggerATransitionPolarity:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:POLarity`` command.

        Description:
            - This command specifies the polarity setting for an transition search to determine
              where to place a mark. SEARCH<x> is the search number, which is always 1.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:POLarity?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:POLarity value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:POLarity {EITher|NEGative|POSitive}
            - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:POLarity?
            ```

        Info:
            - ``POSitive`` specifies that a pulse edge must traverse from the lower (most negative)
              to higher (most positive) level for transition searching to occur.
            - ``NEGative`` specifies that a pulse edge must traverse from the upper (most positive)
              to lower (most negative) level for transition searching to occur.
            - ``EITher`` specifies either positive or negative polarity.
        """
        return self._polarity

    @property
    def source(self) -> SearchSearchItemTriggerATransitionSource:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:SOUrce`` command.

        Description:
            - Sets or returns the source setting for an transition trigger search to determine where
              to place a mark. <x> is the search number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:SOUrce?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:SOUrce value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:SOUrce {CH<x>|MATH}
            - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies one input channel as the edge source. x has a minimum of 1 and a
              maximum of 4.
            - ``MATH`` specifies the math waveform as the search source.
        """
        return self._source

    @property
    def when(self) -> SearchSearchItemTriggerATransitionWhen:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:WHEn`` command.

        Description:
            - This command specifies the condition for a transition search. SEARCH<x> is the search
              number, which is always 1.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:WHEn?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:WHEn?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:WHEn value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:WHEn {SLOWer|FASTer|EQual|UNEQual}
            - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:WHEn?
            ```

        Info:
            - ``FASTer`` sets the search to occur when the transitioning signal is faster than the
              set volts/second rate.
            - ``SLOWer`` sets the search to occur when the transitioning signal is slower than the
              set volts/second rate.
            - ``EQual`` sets the search to occur when the transitioning signal is equal to the set
              volts/second rate within a ±5% tolerance.
            - ``UNEQual`` sets the search to occur when the transitioning signal is not equal to the
              set volts/second rate ±5%.
        """
        return self._when


class SearchSearchItemTriggerASetholdThresholdRefItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead
):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:REF<x>`` command.

    Description:
        - This command specifies the search setup and hold threshold for the selected reference
          waveform. This helps to determine where to place search marks. Search<x> is the search
          number, which is always 1. REF<x> is the reference waveform number, which can be 1-4.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:REF<x>?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:REF<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:REF<x> <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:REF<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the lower threshold in volts.
    """


class SearchSearchItemTriggerASetholdThresholdMath1(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH1`` command.

    Description:
        - This command specifies the search setup and hold threshold for the math waveform. This
          helps to determine where to place search marks. Search<x> is the search number, which is
          always 1.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH1?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH1?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH1 value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH1 <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH1?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the lower threshold in volts.
    """


class SearchSearchItemTriggerASetholdThresholdMath(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH`` command.

    Description:
        - This command specifies the search setup and hold threshold for the math waveform. This
          helps to determine where to place search marks. Search<x> is the search number, which is
          always 1.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the lower threshold in volts.
    """


class SearchSearchItemTriggerASetholdThresholdChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:CH<x>`` command.

    Description:
        - Sets or returns the trigger search setup and hold lower threshold to determine where to
          place a mark. Search<x> is the search number, which is always 1. CH<x> is the channel
          number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:CH<x>?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:CH<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:CH<x> <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:CH<x>?
        ```

    Info:
        - ``<NR3>`` is the lower threshold in volts.
    """


class SearchSearchItemTriggerASetholdThreshold(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:CH<x>`` command.
        - ``.ref``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:REF<x>`` command.
        - ``.math``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH`` command.
        - ``.math1``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH1`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, SearchSearchItemTriggerASetholdThresholdChannel] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerASetholdThresholdChannel(
                    device, f"{self._cmd_syntax}:CH{x}"
                )
            )
        )
        self._ref: Dict[int, SearchSearchItemTriggerASetholdThresholdRefItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerASetholdThresholdRefItem(
                    device, f"{self._cmd_syntax}:REF{x}"
                )
            )
        )
        self._math = SearchSearchItemTriggerASetholdThresholdMath(
            device, f"{self._cmd_syntax}:MATH"
        )
        self._math1 = SearchSearchItemTriggerASetholdThresholdMath1(
            device, f"{self._cmd_syntax}:MATH1"
        )

    @property
    def ch(self) -> Dict[int, SearchSearchItemTriggerASetholdThresholdChannel]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:CH<x>`` command.

        Description:
            - Sets or returns the trigger search setup and hold lower threshold to determine where
              to place a mark. Search<x> is the search number, which is always 1. CH<x> is the
              channel number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:CH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:CH<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:CH<x> <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:CH<x>?
            ```

        Info:
            - ``<NR3>`` is the lower threshold in volts.
        """
        return self._ch

    @property
    def ref(self) -> Dict[int, SearchSearchItemTriggerASetholdThresholdRefItem]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:REF<x>`` command.

        Description:
            - This command specifies the search setup and hold threshold for the selected reference
              waveform. This helps to determine where to place search marks. Search<x> is the search
              number, which is always 1. REF<x> is the reference waveform number, which can be 1-4.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:REF<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:REF<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:REF<x> <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:REF<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the lower threshold in volts.
        """
        return self._ref

    @property
    def math(self) -> SearchSearchItemTriggerASetholdThresholdMath:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH`` command.

        Description:
            - This command specifies the search setup and hold threshold for the math waveform. This
              helps to determine where to place search marks. Search<x> is the search number, which
              is always 1.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the lower threshold in volts.
        """
        return self._math

    @property
    def math1(self) -> SearchSearchItemTriggerASetholdThresholdMath1:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH1`` command.

        Description:
            - This command specifies the search setup and hold threshold for the math waveform. This
              helps to determine where to place search marks. Search<x> is the search number, which
              is always 1.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH1?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH1?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH1 value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH1 <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH1?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the lower threshold in volts.
        """
        return self._math1


class SearchSearchItemTriggerASetholdSettime(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:SETTime`` command.

    Description:
        - This command sets or queries the setup time setting for a setup/hold trigger search to
          determine where to place a mark. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:SETTime?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:SETTime?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:SETTime value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:SETTime <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:SETTime?
        ```

    Info:
        - ``<NR3>`` specifies the setup time for setup and hold violation triggering.
    """


class SearchSearchItemTriggerASetholdHoldtime(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:HOLDTime`` command.

    Description:
        - This command sets or queries the hold time setting for a setup/hold trigger search to
          determine where to place a mark. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:HOLDTime?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:HOLDTime?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:HOLDTime value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:HOLDTime <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:HOLDTime?
        ```

    Info:
        - ``<NR3>`` specifies the hold time setting in seconds. Positive values for hold time occur
          after the clock edge. Negative values occur before the clock edge.
    """


class SearchSearchItemTriggerASetholdDataThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:THReshold`` command.

    Description:
        - Sets or returns the data threshold setting for an setup/hold trigger search to determine
          where to place a mark. <x> is the search number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:THReshold?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:THReshold value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:THReshold {<NR3>|TTL|ECL}
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:THReshold?
        ```

    Info:
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
        - ``ECL`` specifies a preset ECL high level of -1.3 V.
        - ``<NR3>`` is the clock level, in volts.
    """


class SearchSearchItemTriggerASetholdDataSource(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:SOUrce`` command.

    Description:
        - Sets or returns the data source setting for an setup/hold trigger search to determine
          where to place a mark. <x> is the search number. You cannot specify the same source for
          both clock and data.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:SOUrce?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:SOUrce value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:SOUrce DPO Models:{CH<x>|MATH|REF|D<x>}
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an input channel as the search source. x has a minimum of 1 and a
          maximum of 4.
        - ``MATH`` specifies the math waveform as the search source.
        - ``REF`` specifies the reference waveform as the search source.
        - ``D<x>`` specifies the digital waveform as the search source. x has a minimum of 0 and a
          maximum of 15.
    """


class SearchSearchItemTriggerASetholdData(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Info:
        - ``CH<x>`` specifies an input channel as the search source. x has a minimum of 1 and a
          maximum of 4.

    Properties:
        - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:SOUrce`` command.
        - ``.threshold``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = SearchSearchItemTriggerASetholdDataSource(
            device, f"{self._cmd_syntax}:SOUrce"
        )
        self._threshold = SearchSearchItemTriggerASetholdDataThreshold(
            device, f"{self._cmd_syntax}:THReshold"
        )

    @property
    def source(self) -> SearchSearchItemTriggerASetholdDataSource:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:SOUrce`` command.

        Description:
            - Sets or returns the data source setting for an setup/hold trigger search to determine
              where to place a mark. <x> is the search number. You cannot specify the same source
              for both clock and data.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:SOUrce?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:SOUrce value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:SOUrce DPO Models:{CH<x>|MATH|REF|D<x>}
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an input channel as the search source. x has a minimum of 1 and a
              maximum of 4.
            - ``MATH`` specifies the math waveform as the search source.
            - ``REF`` specifies the reference waveform as the search source.
            - ``D<x>`` specifies the digital waveform as the search source. x has a minimum of 0 and
              a maximum of 15.
        """
        return self._source

    @property
    def threshold(self) -> SearchSearchItemTriggerASetholdDataThreshold:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:THReshold`` command.

        Description:
            - Sets or returns the data threshold setting for an setup/hold trigger search to
              determine where to place a mark. <x> is the search number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:THReshold?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:THReshold value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:THReshold {<NR3>|TTL|ECL}
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:THReshold?
            ```

        Info:
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
            - ``ECL`` specifies a preset ECL high level of -1.3 V.
            - ``<NR3>`` is the clock level, in volts.
        """
        return self._threshold


class SearchSearchItemTriggerASetholdClockThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:THReshold`` command.

    Description:
        - This command specifies the clock threshold setting for an setup/hold search to determine
          where to place a mark. SEARCH<x> is the search number, which is always 1.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:THReshold?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:THReshold value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:THReshold {<NR3>|TTL|ECL}
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:THReshold?
        ```

    Info:
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
        - ``ECL`` specifies a preset ECL high level of -1.3V.
        - ``<NR3>`` is a floating point number that specifies the clock level, in volts.
    """


class SearchSearchItemTriggerASetholdClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce`` command.

    Description:
        - Sets or returns the clock source setting for an setup/hold trigger search to determine
          where to place a mark. <x> is the search number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce {CH<x>|MATH|REF}
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an input channel as the edge source. x has a minimum of 1 and a
          maximum of 4.
        - ``MATH`` specifies the math waveform as the search source.
        - ``REF`` specifies the reference waveform as the search source.
    """


class SearchSearchItemTriggerASetholdClockEdge(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:EDGE`` command.

    Description:
        - This command sets or queries the clock slope setting for a setup/hold trigger search to
          determine where to place a mark. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:EDGE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:EDGE?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:EDGE value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:EDGE {FALL|RISe}
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:EDGE?
        ```

    Info:
        - ``FALL`` specifies the polarity as the clock falling edge.
        - ``RISe`` specifies the polarity as the clock rising edge.
    """


class SearchSearchItemTriggerASetholdClock(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.edge``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:EDGE`` command.
        - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce`` command.
        - ``.threshold``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._edge = SearchSearchItemTriggerASetholdClockEdge(device, f"{self._cmd_syntax}:EDGE")
        self._source = SearchSearchItemTriggerASetholdClockSource(
            device, f"{self._cmd_syntax}:SOUrce"
        )
        self._threshold = SearchSearchItemTriggerASetholdClockThreshold(
            device, f"{self._cmd_syntax}:THReshold"
        )

    @property
    def edge(self) -> SearchSearchItemTriggerASetholdClockEdge:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:EDGE`` command.

        Description:
            - This command sets or queries the clock slope setting for a setup/hold trigger search
              to determine where to place a mark. The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:EDGE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:EDGE?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:EDGE value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:EDGE {FALL|RISe}
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:EDGE?
            ```

        Info:
            - ``FALL`` specifies the polarity as the clock falling edge.
            - ``RISe`` specifies the polarity as the clock rising edge.
        """
        return self._edge

    @property
    def source(self) -> SearchSearchItemTriggerASetholdClockSource:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce`` command.

        Description:
            - Sets or returns the clock source setting for an setup/hold trigger search to determine
              where to place a mark. <x> is the search number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce {CH<x>|MATH|REF}
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an input channel as the edge source. x has a minimum of 1 and a
              maximum of 4.
            - ``MATH`` specifies the math waveform as the search source.
            - ``REF`` specifies the reference waveform as the search source.
        """
        return self._source

    @property
    def threshold(self) -> SearchSearchItemTriggerASetholdClockThreshold:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:THReshold`` command.

        Description:
            - This command specifies the clock threshold setting for an setup/hold search to
              determine where to place a mark. SEARCH<x> is the search number, which is always 1.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:THReshold?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:THReshold value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:THReshold {<NR3>|TTL|ECL}
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:THReshold?
            ```

        Info:
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
            - ``ECL`` specifies a preset ECL high level of -1.3V.
            - ``<NR3>`` is a floating point number that specifies the clock level, in volts.
        """
        return self._threshold


class SearchSearchItemTriggerASethold(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.clock``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk`` command tree.
        - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa`` command tree.
        - ``.holdtime``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:HOLDTime`` command.
        - ``.settime``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:SETTime`` command.
        - ``.threshold``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._clock = SearchSearchItemTriggerASetholdClock(device, f"{self._cmd_syntax}:CLOCk")
        self._data = SearchSearchItemTriggerASetholdData(device, f"{self._cmd_syntax}:DATa")
        self._holdtime = SearchSearchItemTriggerASetholdHoldtime(
            device, f"{self._cmd_syntax}:HOLDTime"
        )
        self._settime = SearchSearchItemTriggerASetholdSettime(
            device, f"{self._cmd_syntax}:SETTime"
        )
        self._threshold = SearchSearchItemTriggerASetholdThreshold(
            device, f"{self._cmd_syntax}:THReshold"
        )

    @property
    def clock(self) -> SearchSearchItemTriggerASetholdClock:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.edge``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:EDGE`` command.
            - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce`` command.
            - ``.threshold``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:THReshold`` command.
        """
        return self._clock

    @property
    def data(self) -> SearchSearchItemTriggerASetholdData:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Info:
            - ``CH<x>`` specifies an input channel as the search source. x has a minimum of 1 and a
              maximum of 4.

        Sub-properties:
            - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:SOUrce`` command.
            - ``.threshold``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:THReshold`` command.
        """
        return self._data

    @property
    def holdtime(self) -> SearchSearchItemTriggerASetholdHoldtime:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:HOLDTime`` command.

        Description:
            - This command sets or queries the hold time setting for a setup/hold trigger search to
              determine where to place a mark. The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:HOLDTime?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:HOLDTime?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:HOLDTime value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:HOLDTime <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:HOLDTime?
            ```

        Info:
            - ``<NR3>`` specifies the hold time setting in seconds. Positive values for hold time
              occur after the clock edge. Negative values occur before the clock edge.
        """
        return self._holdtime

    @property
    def settime(self) -> SearchSearchItemTriggerASetholdSettime:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:SETTime`` command.

        Description:
            - This command sets or queries the setup time setting for a setup/hold trigger search to
              determine where to place a mark. The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:SETTime?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:SETTime?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:SETTime value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:SETTime <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:SETTime?
            ```

        Info:
            - ``<NR3>`` specifies the setup time for setup and hold violation triggering.
        """
        return self._settime

    @property
    def threshold(self) -> SearchSearchItemTriggerASetholdThreshold:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:CH<x>`` command.
            - ``.ref``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:REF<x>`` command.
            - ``.math``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH`` command.
            - ``.math1``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH1`` command.
        """
        return self._threshold


class SearchSearchItemTriggerARuntWidth(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth`` command.

    Description:
        - This command sets or queries the width setting for a runt trigger search to determine
          where to place a mark. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth?
        ```

    Info:
        - ``<NR3>`` specifies the minimum width in seconds.
    """


class SearchSearchItemTriggerARuntWhen(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn`` command.

    Description:
        - Sets or returns the condition setting for a runt trigger search to determine where to
          place a mark. <x> is the search number.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn {LESSthan|MOREthan|EQual|UNEQual|OCCURS}
        - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn?
        ```

    Info:
        - ``OCCURS`` argument specifies a trigger event if a runt of any detectable width occurs.
        - ``LESSthan`` argument sets the oscilloscope to trigger if the a runt pulse is detected
          with width less than the time set by the ``SEARCH:SEARCHX:TRIGGER:A:RUNT:WIDTH`` command.
        - ``MOREthan`` argument sets the oscilloscope to trigger if the a runt pulse is detected
          with width more than the time set by the ``SEARCH:SEARCHX:TRIGGER:A:RUNT:WIDTH`` command.
        - ``EQUal`` argument sets the oscilloscope to trigger when the pattern is true for a time
          period equal to the time period specified in ``SEARCH:SEARCHX:TRIGGER:A:RUNT:WIDTH``
          within a ±5% tolerance.
        - ``NOTEQual`` argument sets the oscilloscope to trigger when the pattern is true for a time
          period greater than or less than (but not equal) the time period specified in
          ``SEARCH:SEARCHX:TRIGGER:A:RUNT:WIDTH`` within a ±5% tolerance.
    """


class SearchSearchItemTriggerARuntSource(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce`` command.

    Description:
        - Sets or returns the source setting for a runt trigger search to determine where to place a
          mark. <x> is the search number.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce {CH<x>|MATH|REF}
        - SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an input channel as the edge source. x has a minimum of 1 and a
          maximum of 4.
        - ``MATH`` specifies the math waveform as the search source.
        - ``REF`` specifies the reference waveform as the search source.
    """


class SearchSearchItemTriggerARuntPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity`` command.

    Description:
        - This command specifies the polarity setting for a runt search to determine where to place
          a mark. SEARCH<x> is the search number, which is always 1.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity {EITher|NEGative|POSitive}
        - SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity?
        ```

    Info:
        - ``POSitive`` places a mark when the rising edge crosses the low threshold and the falling
          edge re-crosses the low threshold without either edge ever crossing the high threshold.
        - ``NEGative`` places a mark when the falling edge crosses the high threshold and the rising
          edge re-crosses the high threshold without either edge ever crossing the low threshold.
        - ``EITher`` places a mark on a runt of either polarity.
    """


class SearchSearchItemTriggerARunt(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.polarity``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity`` command.
        - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce`` command.
        - ``.when``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn`` command.
        - ``.width``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = SearchSearchItemTriggerARuntPolarity(
            device, f"{self._cmd_syntax}:POLarity"
        )
        self._source = SearchSearchItemTriggerARuntSource(device, f"{self._cmd_syntax}:SOUrce")
        self._when = SearchSearchItemTriggerARuntWhen(device, f"{self._cmd_syntax}:WHEn")
        self._width = SearchSearchItemTriggerARuntWidth(device, f"{self._cmd_syntax}:WIDth")

    @property
    def polarity(self) -> SearchSearchItemTriggerARuntPolarity:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity`` command.

        Description:
            - This command specifies the polarity setting for a runt search to determine where to
              place a mark. SEARCH<x> is the search number, which is always 1.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity {EITher|NEGative|POSitive}
            - SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity?
            ```

        Info:
            - ``POSitive`` places a mark when the rising edge crosses the low threshold and the
              falling edge re-crosses the low threshold without either edge ever crossing the high
              threshold.
            - ``NEGative`` places a mark when the falling edge crosses the high threshold and the
              rising edge re-crosses the high threshold without either edge ever crossing the low
              threshold.
            - ``EITher`` places a mark on a runt of either polarity.
        """
        return self._polarity

    @property
    def source(self) -> SearchSearchItemTriggerARuntSource:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce`` command.

        Description:
            - Sets or returns the source setting for a runt trigger search to determine where to
              place a mark. <x> is the search number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce {CH<x>|MATH|REF}
            - SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an input channel as the edge source. x has a minimum of 1 and a
              maximum of 4.
            - ``MATH`` specifies the math waveform as the search source.
            - ``REF`` specifies the reference waveform as the search source.
        """
        return self._source

    @property
    def when(self) -> SearchSearchItemTriggerARuntWhen:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn`` command.

        Description:
            - Sets or returns the condition setting for a runt trigger search to determine where to
              place a mark. <x> is the search number.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn {LESSthan|MOREthan|EQual|UNEQual|OCCURS}
            - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn?
            ```

        Info:
            - ``OCCURS`` argument specifies a trigger event if a runt of any detectable width
              occurs.
            - ``LESSthan`` argument sets the oscilloscope to trigger if the a runt pulse is detected
              with width less than the time set by the ``SEARCH:SEARCHX:TRIGGER:A:RUNT:WIDTH``
              command.
            - ``MOREthan`` argument sets the oscilloscope to trigger if the a runt pulse is detected
              with width more than the time set by the ``SEARCH:SEARCHX:TRIGGER:A:RUNT:WIDTH``
              command.
            - ``EQUal`` argument sets the oscilloscope to trigger when the pattern is true for a
              time period equal to the time period specified in
              ``SEARCH:SEARCHX:TRIGGER:A:RUNT:WIDTH`` within a ±5% tolerance.
            - ``NOTEQual`` argument sets the oscilloscope to trigger when the pattern is true for a
              time period greater than or less than (but not equal) the time period specified in
              ``SEARCH:SEARCHX:TRIGGER:A:RUNT:WIDTH`` within a ±5% tolerance.
        """
        return self._when

    @property
    def width(self) -> SearchSearchItemTriggerARuntWidth:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth`` command.

        Description:
            - This command sets or queries the width setting for a runt trigger search to determine
              where to place a mark. The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth?
            ```

        Info:
            - ``<NR3>`` specifies the minimum width in seconds.
        """
        return self._width


class SearchSearchItemTriggerARisefallWhen(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:WHEn`` command.

    Description:
        - This command specifies the condition for a transition search. SEARCH<x> is the search
          number, which is always 1.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:WHEn?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:WHEn?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:WHEn value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:WHEn {SLOWer|FASTer|EQual|UNEQual}
        - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:WHEn?
        ```

    Info:
        - ``FASTer`` sets the search to occur when the transitioning signal is faster than the set
          volts/second rate.
        - ``SLOWer`` sets the search to occur when the transitioning signal is slower than the set
          volts/second rate.
        - ``EQual`` sets the search to occur when the transitioning signal is equal to the set
          volts/second rate within a ±5% tolerance.
        - ``UNEQual`` sets the search to occur when the transitioning signal is not equal to the set
          volts/second rate ±5%.
    """


class SearchSearchItemTriggerARisefallSource(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:SOUrce`` command.

    Description:
        - Sets or returns the source setting for an transition trigger search to determine where to
          place a mark. <x> is the search number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:SOUrce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:SOUrce value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:SOUrce {CH<x>|MATH}
        - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies one input channel as the edge source. x has a minimum of 1 and a
          maximum of 4.
        - ``MATH`` specifies the math waveform as the search source.
    """


class SearchSearchItemTriggerARisefallPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:POLarity`` command.

    Description:
        - This command specifies the polarity setting for an transition search to determine where to
          place a mark. SEARCH<x> is the search number, which is always 1.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:POLarity?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:POLarity value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:POLarity {EITher|NEGative|POSitive}
        - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:POLarity?
        ```

    Info:
        - ``POSitive`` specifies that a pulse edge must traverse from the lower (most negative) to
          higher (most positive) level for transition searching to occur.
        - ``NEGative`` specifies that a pulse edge must traverse from the upper (most positive) to
          lower (most negative) level for transition searching to occur.
        - ``EITher`` specifies either positive or negative polarity.
    """


class SearchSearchItemTriggerARisefallDeltatime(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:DELTatime`` command.

    Description:
        - This command specifies the transition delta time setting to be used as the value to
          compare against when a transition time is found. < SEARCH<x> is the search number, which
          is always 1.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:DELTatime?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:DELTatime?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:DELTatime value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:DELTatime <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:DELTatime?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the transition time, in seconds.
    """


class SearchSearchItemTriggerARisefall(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall?``
          query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.deltatime``: The ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:DELTatime`` command.
        - ``.polarity``: The ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:POLarity`` command.
        - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:SOUrce`` command.
        - ``.when``: The ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:WHEn`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._deltatime = SearchSearchItemTriggerARisefallDeltatime(
            device, f"{self._cmd_syntax}:DELTatime"
        )
        self._polarity = SearchSearchItemTriggerARisefallPolarity(
            device, f"{self._cmd_syntax}:POLarity"
        )
        self._source = SearchSearchItemTriggerARisefallSource(device, f"{self._cmd_syntax}:SOUrce")
        self._when = SearchSearchItemTriggerARisefallWhen(device, f"{self._cmd_syntax}:WHEn")

    @property
    def deltatime(self) -> SearchSearchItemTriggerARisefallDeltatime:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:DELTatime`` command.

        Description:
            - This command specifies the transition delta time setting to be used as the value to
              compare against when a transition time is found. < SEARCH<x> is the search number,
              which is always 1.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:DELTatime?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:DELTatime?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:DELTatime value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:DELTatime <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:DELTatime?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the transition time, in seconds.
        """
        return self._deltatime

    @property
    def polarity(self) -> SearchSearchItemTriggerARisefallPolarity:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:POLarity`` command.

        Description:
            - This command specifies the polarity setting for an transition search to determine
              where to place a mark. SEARCH<x> is the search number, which is always 1.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:POLarity?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:POLarity value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:POLarity {EITher|NEGative|POSitive}
            - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:POLarity?
            ```

        Info:
            - ``POSitive`` specifies that a pulse edge must traverse from the lower (most negative)
              to higher (most positive) level for transition searching to occur.
            - ``NEGative`` specifies that a pulse edge must traverse from the upper (most positive)
              to lower (most negative) level for transition searching to occur.
            - ``EITher`` specifies either positive or negative polarity.
        """
        return self._polarity

    @property
    def source(self) -> SearchSearchItemTriggerARisefallSource:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:SOUrce`` command.

        Description:
            - Sets or returns the source setting for an transition trigger search to determine where
              to place a mark. <x> is the search number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:SOUrce?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:SOUrce value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:SOUrce {CH<x>|MATH}
            - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies one input channel as the edge source. x has a minimum of 1 and a
              maximum of 4.
            - ``MATH`` specifies the math waveform as the search source.
        """
        return self._source

    @property
    def when(self) -> SearchSearchItemTriggerARisefallWhen:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:WHEn`` command.

        Description:
            - This command specifies the condition for a transition search. SEARCH<x> is the search
              number, which is always 1.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:WHEn?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:WHEn?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:WHEn value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:WHEn {SLOWer|FASTer|EQual|UNEQual}
            - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:WHEn?
            ```

        Info:
            - ``FASTer`` sets the search to occur when the transitioning signal is faster than the
              set volts/second rate.
            - ``SLOWer`` sets the search to occur when the transitioning signal is slower than the
              set volts/second rate.
            - ``EQual`` sets the search to occur when the transitioning signal is equal to the set
              volts/second rate within a ±5% tolerance.
            - ``UNEQual`` sets the search to occur when the transitioning signal is not equal to the
              set volts/second rate ±5%.
        """
        return self._when


class SearchSearchItemTriggerAPulsewidthWidth(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WIDth`` command.

    Description:
        - This command specifies the width setting to use, in seconds, when searching the waveform
          record for pulses of a certain width (duration). SEARCH<x> is the search number, which is
          always 1.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WIDth?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WIDth?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WIDth value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WIDth <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WIDth?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the pulse width.
    """


class SearchSearchItemTriggerAPulsewidthWhen(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn`` command.

    Description:
        - Sets or returns the condition for generating a pulse width search to determine where to
          place a mark. <x> is the search number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn {LESSthan|MOREthan|EQual|UNEQual}
        - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn?
        ```

    Info:
        - ``LESSThan`` places a mark if the pulse width is less than the time set by the
          ``SEARCH:SEARCHX:TRIGGER:A:PULSEWIDTH:WIDTH`` command.
        - ``MOREthan`` places a mark if the pulse width is more than the time set by the
          ``SEARCH:SEARCHX:TRIGGER:A:PULSEWIDTH:WIDTH`` command.
        - ``EQUal`` places a mark if the pulse width is equal to the time set by the
          ``SEARCH:SEARCHX:TRIGGER:A:PULSEWIDTH:WIDTH`` command within a tolerance of ±5%.
        - ``UNEQual`` places a mark if the pulse width is unequal to the time the time set by the
          ``SEARCH:SEARCHX:TRIGGER:A:PULSEWIDTH:WIDTH`` command within a tolerance of ±5%.
    """


class SearchSearchItemTriggerAPulsewidthSource(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce`` command.

    Description:
        - Sets or returns the source waveform for a pulse trigger search to determine where to place
          a mark. <x> is the search number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce {CH<x>|MATH|REF}
        - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies one input channel as the edge source, where <x> = 1, 2, 3 or 4.
        - ``MATH`` specifies the math waveform as the search source.
        - ``REF`` specifies the reference waveform as the search source.
    """


class SearchSearchItemTriggerAPulsewidthPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity`` command.

    Description:
        - This command specifies the polarity for a pulse search to determine where to place a mark.
          SEARCH<x> is the search number, which is always 1.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity {NEGative|POSitive}
        - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity?
        ```

    Info:
        - ``POSITIVe`` places a mark only when the polarity of the pulse is positive.
        - ``NEGative`` places a mark only when the polarity of the pulse is negative.
    """


class SearchSearchItemTriggerAPulsewidth(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.polarity``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity`` command.
        - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce`` command.
        - ``.when``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn`` command.
        - ``.width``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WIDth`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = SearchSearchItemTriggerAPulsewidthPolarity(
            device, f"{self._cmd_syntax}:POLarity"
        )
        self._source = SearchSearchItemTriggerAPulsewidthSource(
            device, f"{self._cmd_syntax}:SOUrce"
        )
        self._when = SearchSearchItemTriggerAPulsewidthWhen(device, f"{self._cmd_syntax}:WHEn")
        self._width = SearchSearchItemTriggerAPulsewidthWidth(device, f"{self._cmd_syntax}:WIDth")

    @property
    def polarity(self) -> SearchSearchItemTriggerAPulsewidthPolarity:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity`` command.

        Description:
            - This command specifies the polarity for a pulse search to determine where to place a
              mark. SEARCH<x> is the search number, which is always 1.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity {NEGative|POSitive}
            - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity?
            ```

        Info:
            - ``POSITIVe`` places a mark only when the polarity of the pulse is positive.
            - ``NEGative`` places a mark only when the polarity of the pulse is negative.
        """
        return self._polarity

    @property
    def source(self) -> SearchSearchItemTriggerAPulsewidthSource:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce`` command.

        Description:
            - Sets or returns the source waveform for a pulse trigger search to determine where to
              place a mark. <x> is the search number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce {CH<x>|MATH|REF}
            - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies one input channel as the edge source, where <x> = 1, 2, 3 or 4.
            - ``MATH`` specifies the math waveform as the search source.
            - ``REF`` specifies the reference waveform as the search source.
        """
        return self._source

    @property
    def when(self) -> SearchSearchItemTriggerAPulsewidthWhen:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn`` command.

        Description:
            - Sets or returns the condition for generating a pulse width search to determine where
              to place a mark. <x> is the search number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn {LESSthan|MOREthan|EQual|UNEQual}
            - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn?
            ```

        Info:
            - ``LESSThan`` places a mark if the pulse width is less than the time set by the
              ``SEARCH:SEARCHX:TRIGGER:A:PULSEWIDTH:WIDTH`` command.
            - ``MOREthan`` places a mark if the pulse width is more than the time set by the
              ``SEARCH:SEARCHX:TRIGGER:A:PULSEWIDTH:WIDTH`` command.
            - ``EQUal`` places a mark if the pulse width is equal to the time set by the
              ``SEARCH:SEARCHX:TRIGGER:A:PULSEWIDTH:WIDTH`` command within a tolerance of ±5%.
            - ``UNEQual`` places a mark if the pulse width is unequal to the time the time set by
              the ``SEARCH:SEARCHX:TRIGGER:A:PULSEWIDTH:WIDTH`` command within a tolerance of ±5%.
        """
        return self._when

    @property
    def width(self) -> SearchSearchItemTriggerAPulsewidthWidth:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WIDth`` command.

        Description:
            - This command specifies the width setting to use, in seconds, when searching the
              waveform record for pulses of a certain width (duration). SEARCH<x> is the search
              number, which is always 1.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WIDth?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WIDth?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WIDth value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WIDth <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WIDth?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the pulse width.
        """
        return self._width


class SearchSearchItemTriggerALowerthresholdRefItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead
):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:REF<x>`` command.

    Description:
        - Sets or returns the reference waveform lower threshold to determine where to place a mark.
          This setting is applied to all reference searches that use a lower threshold. SEARCH<x> is
          the search number and REF<x> is the reference channel number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:REF<x>?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:REF<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:REF<x> {TTL|ECL|<NR3>}
        - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:REF<x>?
        ```

    Info:
        - ``TTL`` specifies a preset TTL level of 1.4 V.
        - ``ECL`` specifies a preset ECL level of -1.3 V.
        - ``<NR3>`` specifies the threshold voltage level.
    """


class SearchSearchItemTriggerALowerthresholdMath(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:MATH`` command.

    Description:
        - Sets or returns the math waveform lower threshold to determine where to place a mark. This
          setting is applied to all math searches that use a lower threshold.<x> is the search
          number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:MATH?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:MATH?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:MATH value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:MATH {TTL|ECL|<NR3>}
        - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:MATH?
        ```

    Info:
        - ``TTL`` specifies a preset TTL level of 1.4 V.
        - ``ECL`` specifies a preset ECL level of -1.3 V.
        - ``<NR3>`` specifies the threshold voltage level.
    """


class SearchSearchItemTriggerALowerthresholdChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:CH<x>`` command.

    Description:
        - Sets or returns the channel waveform lower threshold to determine where to place a mark.
          This setting is applied to all channel searches that use a lower threshold. SEARCH<x> is
          the search number and CH<x> is the channel number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:CH<x>?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:CH<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:CH<x> {TTL|ECL|<NR3>}
        - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:CH<x>?
        ```

    Info:
        - ``TTL`` specifies a preset TTL level of 1.4 V.
        - ``ECL`` specifies a preset ECLlevel of -1.3 V.
    """


class SearchSearchItemTriggerALowerthreshold(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:CH<x>`` command.
        - ``.math``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:MATH`` command.
        - ``.ref``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:REF<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, SearchSearchItemTriggerALowerthresholdChannel] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerALowerthresholdChannel(
                    device, f"{self._cmd_syntax}:CH{x}"
                )
            )
        )
        self._math = SearchSearchItemTriggerALowerthresholdMath(device, f"{self._cmd_syntax}:MATH")
        self._ref: Dict[int, SearchSearchItemTriggerALowerthresholdRefItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerALowerthresholdRefItem(
                    device, f"{self._cmd_syntax}:REF{x}"
                )
            )
        )

    @property
    def ch(self) -> Dict[int, SearchSearchItemTriggerALowerthresholdChannel]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:CH<x>`` command.

        Description:
            - Sets or returns the channel waveform lower threshold to determine where to place a
              mark. This setting is applied to all channel searches that use a lower threshold.
              SEARCH<x> is the search number and CH<x> is the channel number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:CH<x>?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:CH<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:CH<x> {TTL|ECL|<NR3>}
            - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:CH<x>?
            ```

        Info:
            - ``TTL`` specifies a preset TTL level of 1.4 V.
            - ``ECL`` specifies a preset ECLlevel of -1.3 V.
        """
        return self._ch

    @property
    def math(self) -> SearchSearchItemTriggerALowerthresholdMath:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:MATH`` command.

        Description:
            - Sets or returns the math waveform lower threshold to determine where to place a mark.
              This setting is applied to all math searches that use a lower threshold.<x> is the
              search number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:MATH?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:MATH?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:MATH value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:MATH {TTL|ECL|<NR3>}
            - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:MATH?
            ```

        Info:
            - ``TTL`` specifies a preset TTL level of 1.4 V.
            - ``ECL`` specifies a preset ECL level of -1.3 V.
            - ``<NR3>`` specifies the threshold voltage level.
        """
        return self._math

    @property
    def ref(self) -> Dict[int, SearchSearchItemTriggerALowerthresholdRefItem]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:REF<x>`` command.

        Description:
            - Sets or returns the reference waveform lower threshold to determine where to place a
              mark. This setting is applied to all reference searches that use a lower threshold.
              SEARCH<x> is the search number and REF<x> is the reference channel number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:REF<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:REF<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:REF<x> {TTL|ECL|<NR3>}
            - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:REF<x>?
            ```

        Info:
            - ``TTL`` specifies a preset TTL level of 1.4 V.
            - ``ECL`` specifies a preset ECL level of -1.3 V.
            - ``<NR3>`` specifies the threshold voltage level.
        """
        return self._ref


class SearchSearchItemTriggerALogicThresholdRefItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead
):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:REF<x>`` command.

    Description:
        - Sets or returns the reference waveform threshold level for a logic trigger search to
          determine where to place a mark. SEARCH<x> is the search number and REF<x> is the
          reference channel number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:REF<x>?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:REF<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:REF<x> {TTL|ECL|<NR3>}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:REF<x>?
        ```

    Info:
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
        - ``ECL`` specifies a preset ECL high level of -1.3 V.
        - ``<NR3>`` specifies the threshold voltage level.
    """


class SearchSearchItemTriggerALogicThresholdMath(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:MATH`` command.

    Description:
        - Sets or returns the math waveform threshold level for a logic trigger search to determine
          where to place a mark. <x> is the search number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:MATH?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:MATH?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:MATH value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:MATH {TTL|ECL|<NR3>}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:MATH?
        ```

    Info:
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
        - ``ECL`` specifies a preset ECL high level of -1.3 V.
        - ``<NR3>`` specifies the threshold voltage level.
    """


class SearchSearchItemTriggerALogicThresholdChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:CH<x>`` command.

    Description:
        - Sets or returns the channel threshold level for a logic trigger search to determine where
          to place a mark. SEARCH<x> is the search number and CH<x> is the channel number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:CH<x>?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:CH<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:CH<x> {<NR3>|TTL|ECL}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:CH<x>?
        ```

    Info:
        - ``<NR3>`` specifies the threshold voltage level.
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
        - ``ECL`` specifies a preset ECL high level of -1.3 V.
    """


class SearchSearchItemTriggerALogicThreshold(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:CH<x>`` command.
        - ``.math``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:MATH`` command.
        - ``.ref``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:REF<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, SearchSearchItemTriggerALogicThresholdChannel] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerALogicThresholdChannel(
                    device, f"{self._cmd_syntax}:CH{x}"
                )
            )
        )
        self._math = SearchSearchItemTriggerALogicThresholdMath(device, f"{self._cmd_syntax}:MATH")
        self._ref: Dict[int, SearchSearchItemTriggerALogicThresholdRefItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerALogicThresholdRefItem(
                    device, f"{self._cmd_syntax}:REF{x}"
                )
            )
        )

    @property
    def ch(self) -> Dict[int, SearchSearchItemTriggerALogicThresholdChannel]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:CH<x>`` command.

        Description:
            - Sets or returns the channel threshold level for a logic trigger search to determine
              where to place a mark. SEARCH<x> is the search number and CH<x> is the channel number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:CH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:CH<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:CH<x> {<NR3>|TTL|ECL}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:CH<x>?
            ```

        Info:
            - ``<NR3>`` specifies the threshold voltage level.
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
            - ``ECL`` specifies a preset ECL high level of -1.3 V.
        """
        return self._ch

    @property
    def math(self) -> SearchSearchItemTriggerALogicThresholdMath:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:MATH`` command.

        Description:
            - Sets or returns the math waveform threshold level for a logic trigger search to
              determine where to place a mark. <x> is the search number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:MATH?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:MATH?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:MATH value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:MATH {TTL|ECL|<NR3>}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:MATH?
            ```

        Info:
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
            - ``ECL`` specifies a preset ECL high level of -1.3 V.
            - ``<NR3>`` specifies the threshold voltage level.
        """
        return self._math

    @property
    def ref(self) -> Dict[int, SearchSearchItemTriggerALogicThresholdRefItem]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:REF<x>`` command.

        Description:
            - Sets or returns the reference waveform threshold level for a logic trigger search to
              determine where to place a mark. SEARCH<x> is the search number and REF<x> is the
              reference channel number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:REF<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:REF<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:REF<x> {TTL|ECL|<NR3>}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:REF<x>?
            ```

        Info:
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
            - ``ECL`` specifies a preset ECL high level of -1.3 V.
            - ``<NR3>`` specifies the threshold voltage level.
        """
        return self._ref


class SearchSearchItemTriggerALogicPatternWhenMorelimit(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:MORELimit`` command.

    Description:
        - This command specifies the minimum time that the selected pattern may be true and still
          generate an A logic pattern search to place a mark. SEARCH<x> is the search number, which
          is always 1.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:MORELimit?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:MORELimit?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:MORELimit value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:MORELimit <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:MORELimit?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the minimum amount of time to hold the
          pattern true.
    """


class SearchSearchItemTriggerALogicPatternWhenLesslimit(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit`` command.

    Description:
        - This command specifies the maximum time that the selected pattern may be true and still
          generate an A logic pattern search to place a mark. <x> is the search number, which is
          always 1

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the maximum amount of time to hold the
          pattern true.
    """


class SearchSearchItemTriggerALogicPatternWhen(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn`` command.

    Description:
        - Sets or returns the condition for generating a logic pattern trigger search to determine
          where to place a mark. <x> is the search number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn {TRUe|FALSe|LESSThan|MOREThan|Than|EQUal|UNEQual}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn?
        ```

    Info:
        - ``TRUe`` places a mark when the pattern becomes true.
        - ``FALSe`` places a mark when the pattern becomes false.
        - ``LESSThan`` places a mark if the specific pattern is true less than the time set by the
          ``SEARCH:SEARCHX:TRIGGER:A:LOGIC:PATTERN:WHEN:LESSLIMIT`` command.
        - ``MOREThan`` places a mark if the specific pattern is true more than the time set by the
          ``SEARCH:SEARCHX:TRIGGER:A:LOGIC:PATTERN:WHEN:LESSLIMIT`` command.
        - ``EQUal`` places a mark if the specific pattern is true longer than the time set by the
          ``SEARCH:SEARCHX:TRIGGER:A:LOGIC:PATTERN:WHEN:LESSLIMIT`` command, but less than the
          specified time set by the ``SEARCH:SEARCHX:TRIGGER:A:LOGIC:PATTERN:WHEN:MORELIMIT``
          command.
        - ``UNEQual`` places a mark if the specific pattern is true less than the time set by the
          ``SEARCH:SEARCHX:TRIGGER:A:LOGIC:PATTERN:WHEN:LESSLIMIT`` command, or longer than the
          specified time set by the ``SEARCH:SEARCHX:TRIGGER:A:LOGIC:PATTERN:WHEN:MORELIMIT``
          command.

    Properties:
        - ``.lesslimit``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit`` command.
        - ``.morelimit``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:MORELimit`` command.
    """  # noqa: E501

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._lesslimit = SearchSearchItemTriggerALogicPatternWhenLesslimit(
            device, f"{self._cmd_syntax}:LESSLimit"
        )
        self._morelimit = SearchSearchItemTriggerALogicPatternWhenMorelimit(
            device, f"{self._cmd_syntax}:MORELimit"
        )

    @property
    def lesslimit(self) -> SearchSearchItemTriggerALogicPatternWhenLesslimit:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit`` command.

        Description:
            - This command specifies the maximum time that the selected pattern may be true and
              still generate an A logic pattern search to place a mark. <x> is the search number,
              which is always 1

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the maximum amount of time to hold
              the pattern true.
        """
        return self._lesslimit

    @property
    def morelimit(self) -> SearchSearchItemTriggerALogicPatternWhenMorelimit:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:MORELimit`` command.

        Description:
            - This command specifies the minimum time that the selected pattern may be true and
              still generate an A logic pattern search to place a mark. SEARCH<x> is the search
              number, which is always 1.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:MORELimit?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:MORELimit?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:MORELimit value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:MORELimit <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:MORELimit?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the minimum amount of time to hold
              the pattern true.
        """
        return self._morelimit


class SearchSearchItemTriggerALogicPatternInputRefItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead
):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:REF<x>`` command.

    Description:
        - Sets or returns the Boolean logic criteria for a pattern trigger search to determine where
          to place a mark. SEARCH<x> is the search number and REF<x> is the reference channel
          number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:REF<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:REF<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:REF<x> {HIGH|LOW|X}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:REF<x>?
        ```

    Info:
        - ``HIGH`` specifies a high logic level.
        - ``LOW`` specifies a low logic level.
        - ``X`` specifies a 'don't care' condition.
    """


class SearchSearchItemTriggerALogicPatternInputMath(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:MATH`` command.

    Description:
        - Sets or returns the Boolean logic criteria for a logic pattern trigger search to determine
          where to place a mark. <x> is the search number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:MATH?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:MATH?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:MATH value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:MATH {HIGH|LOW|X}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:MATH?
        ```

    Info:
        - ``HIGH`` specifies a high logic level.
        - ``LOW`` specifies a low logic level.
        - ``X`` specifies a 'don't care' condition.
    """


class SearchSearchItemTriggerALogicPatternInputDigitalBit(
    ValidatedDigitalBit, SCPICmdWrite, SCPICmdRead
):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:D<x>`` command.

    Description:
        - Sets or returns the logic criteria for a logic pattern search to determine where to place
          a mark. SEARCH<x> is the search number and D<x> is the digital channel number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:D<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:D<x>?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:D<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:D<x> {HIGH|LOW|X}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:D<x>?
        ```

    Info:
        - ``HIGH`` specifies a high logic level.
        - ``LOW`` specifies a low logic level.
        - ``X`` specifies a 'don't care' condition.
    """


class SearchSearchItemTriggerALogicPatternInputChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:CH<x>`` command.

    Description:
        - This command specifies the logic condition to be used in a logic search when the input is
          an analog channel. SEARCH<x> is the search number, which is always 1, and CH<x> is the
          analog channel number, which can be 1- 4.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:CH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:CH<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:CH<x> {HIGH|LOW|X}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:CH<x>?
        ```

    Info:
        - ``HIGH`` specifies a high logic level.
        - ``LOW`` specifies a low logic level.
        - ``X`` specifies a 'don't care' condition.
    """


class SearchSearchItemTriggerALogicPatternInput(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:CH<x>`` command.
        - ``.d``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:D<x>`` command.
        - ``.math``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:MATH`` command.
        - ``.ref``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:REF<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, SearchSearchItemTriggerALogicPatternInputChannel] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerALogicPatternInputChannel(
                    device, f"{self._cmd_syntax}:CH{x}"
                )
            )
        )
        self._d: Dict[int, SearchSearchItemTriggerALogicPatternInputDigitalBit] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerALogicPatternInputDigitalBit(
                    device, f"{self._cmd_syntax}:D{x}"
                )
            )
        )
        self._math = SearchSearchItemTriggerALogicPatternInputMath(
            device, f"{self._cmd_syntax}:MATH"
        )
        self._ref: Dict[int, SearchSearchItemTriggerALogicPatternInputRefItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerALogicPatternInputRefItem(
                    device, f"{self._cmd_syntax}:REF{x}"
                )
            )
        )

    @property
    def ch(self) -> Dict[int, SearchSearchItemTriggerALogicPatternInputChannel]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:CH<x>`` command.

        Description:
            - This command specifies the logic condition to be used in a logic search when the input
              is an analog channel. SEARCH<x> is the search number, which is always 1, and CH<x> is
              the analog channel number, which can be 1- 4.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:CH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:CH<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:CH<x> {HIGH|LOW|X}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:CH<x>?
            ```

        Info:
            - ``HIGH`` specifies a high logic level.
            - ``LOW`` specifies a low logic level.
            - ``X`` specifies a 'don't care' condition.
        """
        return self._ch

    @property
    def d(self) -> Dict[int, SearchSearchItemTriggerALogicPatternInputDigitalBit]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:D<x>`` command.

        Description:
            - Sets or returns the logic criteria for a logic pattern search to determine where to
              place a mark. SEARCH<x> is the search number and D<x> is the digital channel number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:D<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:D<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:D<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:D<x> {HIGH|LOW|X}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:D<x>?
            ```

        Info:
            - ``HIGH`` specifies a high logic level.
            - ``LOW`` specifies a low logic level.
            - ``X`` specifies a 'don't care' condition.
        """
        return self._d

    @property
    def math(self) -> SearchSearchItemTriggerALogicPatternInputMath:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:MATH`` command.

        Description:
            - Sets or returns the Boolean logic criteria for a logic pattern trigger search to
              determine where to place a mark. <x> is the search number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:MATH?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:MATH?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:MATH value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:MATH {HIGH|LOW|X}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:MATH?
            ```

        Info:
            - ``HIGH`` specifies a high logic level.
            - ``LOW`` specifies a low logic level.
            - ``X`` specifies a 'don't care' condition.
        """
        return self._math

    @property
    def ref(self) -> Dict[int, SearchSearchItemTriggerALogicPatternInputRefItem]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:REF<x>`` command.

        Description:
            - Sets or returns the Boolean logic criteria for a pattern trigger search to determine
              where to place a mark. SEARCH<x> is the search number and REF<x> is the reference
              channel number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:REF<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:REF<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:REF<x> {HIGH|LOW|X}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:REF<x>?
            ```

        Info:
            - ``HIGH`` specifies a high logic level.
            - ``LOW`` specifies a low logic level.
            - ``X`` specifies a 'don't care' condition.
        """
        return self._ref


class SearchSearchItemTriggerALogicPattern(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.input``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut`` command tree.
        - ``.when``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._input = SearchSearchItemTriggerALogicPatternInput(device, f"{self._cmd_syntax}:INPut")
        self._when = SearchSearchItemTriggerALogicPatternWhen(device, f"{self._cmd_syntax}:WHEn")

    @property
    def input(self) -> SearchSearchItemTriggerALogicPatternInput:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:CH<x>`` command.
            - ``.d``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:D<x>`` command.
            - ``.math``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:MATH`` command.
            - ``.ref``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:REF<x>`` command.
        """
        return self._input

    @property
    def when(self) -> SearchSearchItemTriggerALogicPatternWhen:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn`` command.

        Description:
            - Sets or returns the condition for generating a logic pattern trigger search to
              determine where to place a mark. <x> is the search number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn {TRUe|FALSe|LESSThan|MOREThan|Than|EQUal|UNEQual}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn?
            ```

        Info:
            - ``TRUe`` places a mark when the pattern becomes true.
            - ``FALSe`` places a mark when the pattern becomes false.
            - ``LESSThan`` places a mark if the specific pattern is true less than the time set by
              the ``SEARCH:SEARCHX:TRIGGER:A:LOGIC:PATTERN:WHEN:LESSLIMIT`` command.
            - ``MOREThan`` places a mark if the specific pattern is true more than the time set by
              the ``SEARCH:SEARCHX:TRIGGER:A:LOGIC:PATTERN:WHEN:LESSLIMIT`` command.
            - ``EQUal`` places a mark if the specific pattern is true longer than the time set by
              the ``SEARCH:SEARCHX:TRIGGER:A:LOGIC:PATTERN:WHEN:LESSLIMIT`` command, but less than
              the specified time set by the
              ``SEARCH:SEARCHX:TRIGGER:A:LOGIC:PATTERN:WHEN:MORELIMIT`` command.
            - ``UNEQual`` places a mark if the specific pattern is true less than the time set by
              the ``SEARCH:SEARCHX:TRIGGER:A:LOGIC:PATTERN:WHEN:LESSLIMIT`` command, or longer than
              the specified time set by the
              ``SEARCH:SEARCHX:TRIGGER:A:LOGIC:PATTERN:WHEN:MORELIMIT`` command.

        Sub-properties:
            - ``.lesslimit``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit``
              command.
            - ``.morelimit``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:MORELimit``
              command.
        """  # noqa: E501
        return self._when


class SearchSearchItemTriggerALogicInputRefItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead
):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:REF<x>`` command.

    Description:
        - This command specifies the logic condition of the reference waveform to be used in a logic
          search. SEARCH<x> is the search number, which is always 1, and REF<x> is the reference
          channel number, which can be 1-4.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:REF<x>?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:REF<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:REF<x> {HIGH|LOW|X}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:REF<x>?
        ```

    Info:
        - ``HIGH`` specifies a high logic level.
        - ``LOW`` specifies a low logic level.
        - ``X`` specifies a 'don't care' condition.
    """


class SearchSearchItemTriggerALogicInputMath(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:MATH`` command.

    Description:
        - This command specifies the logic condition of the math input to be used in a logic search.
          <x> is the search number, which is always 1.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:MATH?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:MATH?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:MATH value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:MATH {HIGH|LOW|X}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:MATH?
        ```

    Info:
        - ``HIGH`` specifies a high logic level.
        - ``LOW`` specifies a low logic level.
        - ``X`` specifies a 'don't care' condition.
    """


class SearchSearchItemTriggerALogicInputDigitalBit(ValidatedDigitalBit, SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:D<x>`` command.

    Description:
        - This command specifies the logic condition to be used in a logic search when the input is
          a digital channel. SEARCH<x> is the search number, which is always 1, and D<x> is the
          digital channel number, which can be D0 - D16.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:D<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:D<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:D<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:D<x> {HIGH|LOW|X}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:D<x>?
        ```

    Info:
        - ``HIGH`` specifies a high logic level.
        - ``LOW`` specifies a low logic level.
        - ``X`` specifies a 'don't care' condition.
    """


class SearchSearchItemTriggerALogicInputClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:SOUrce`` command.

    Description:
        - Sets or returns the clock source definition for a logic trigger search. <x> is the search
          number. If a clock source is defined, then the logic search is determined by the state of
          the other inputs at the clock transition. If no clock source is defined, then the logic
          search is determined only by the state of the inputs.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:SOUrce value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:SOUrce {CH<x>|MATH|REF|D<x>|NONe}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies a channel input as the clock source, where <x> = 1, 2, 3, or 4.
        - ``MATH`` specifies the math waveform as the clock source.
        - ``REF`` specifies the reference waveform as the clock source.
        - ``D<x>`` specifies the digital waveform as the clock source, where <x>=0-15.
        - ``NONe`` specifies no clock source.
    """


class SearchSearchItemTriggerALogicInputClockEdge(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:EDGE`` command.

    Description:
        - Sets or returns whether the clock edge is a rising or falling for a logic search to
          determine where to place a mark. <x> is the search number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:EDGE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:EDGE?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:EDGE value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:EDGE {FALL|RISe|EITher}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:EDGE?
        ```

    Info:
        - ``RISe`` specifies a rising edge.
        - ``FALL`` specifies a falling edge.
        - ``EITher`` specifies either a falling or rising edge.
    """


class SearchSearchItemTriggerALogicInputClock(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.edge``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:EDGE`` command.
        - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._edge = SearchSearchItemTriggerALogicInputClockEdge(device, f"{self._cmd_syntax}:EDGE")
        self._source = SearchSearchItemTriggerALogicInputClockSource(
            device, f"{self._cmd_syntax}:SOUrce"
        )

    @property
    def edge(self) -> SearchSearchItemTriggerALogicInputClockEdge:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:EDGE`` command.

        Description:
            - Sets or returns whether the clock edge is a rising or falling for a logic search to
              determine where to place a mark. <x> is the search number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:EDGE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:EDGE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:EDGE value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:EDGE {FALL|RISe|EITher}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:EDGE?
            ```

        Info:
            - ``RISe`` specifies a rising edge.
            - ``FALL`` specifies a falling edge.
            - ``EITher`` specifies either a falling or rising edge.
        """
        return self._edge

    @property
    def source(self) -> SearchSearchItemTriggerALogicInputClockSource:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:SOUrce`` command.

        Description:
            - Sets or returns the clock source definition for a logic trigger search. <x> is the
              search number. If a clock source is defined, then the logic search is determined by
              the state of the other inputs at the clock transition. If no clock source is defined,
              then the logic search is determined only by the state of the inputs.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:SOUrce value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:SOUrce {CH<x>|MATH|REF|D<x>|NONe}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies a channel input as the clock source, where <x> = 1, 2, 3, or 4.
            - ``MATH`` specifies the math waveform as the clock source.
            - ``REF`` specifies the reference waveform as the clock source.
            - ``D<x>`` specifies the digital waveform as the clock source, where <x>=0-15.
            - ``NONe`` specifies no clock source.
        """
        return self._source


class SearchSearchItemTriggerALogicInputChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CH<x>`` command.

    Description:
        - This command specifies the logic condition to be used in a logic search when the input is
          an analog channel. SEARCH<x> is the search number, which is always 1, and CH<x> is the
          channel number, which can be 1-4.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CH<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CH<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CH<x> {HIGH|LOW|X}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CH<x>?
        ```

    Info:
        - ``HIGH`` specifies the logic high.
        - ``LOW`` specifies the logic low.
        - ``X`` specifies a 'don't care' state.
    """


class SearchSearchItemTriggerALogicInput(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CH<x>`` command.
        - ``.clock``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk`` command tree.
        - ``.d``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:D<x>`` command.
        - ``.math``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:MATH`` command.
        - ``.ref``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:REF<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, SearchSearchItemTriggerALogicInputChannel] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerALogicInputChannel(
                    device, f"{self._cmd_syntax}:CH{x}"
                )
            )
        )
        self._clock = SearchSearchItemTriggerALogicInputClock(device, f"{self._cmd_syntax}:CLOCk")
        self._d: Dict[int, SearchSearchItemTriggerALogicInputDigitalBit] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerALogicInputDigitalBit(
                    device, f"{self._cmd_syntax}:D{x}"
                )
            )
        )
        self._math = SearchSearchItemTriggerALogicInputMath(device, f"{self._cmd_syntax}:MATH")
        self._ref: Dict[int, SearchSearchItemTriggerALogicInputRefItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerALogicInputRefItem(
                    device, f"{self._cmd_syntax}:REF{x}"
                )
            )
        )

    @property
    def ch(self) -> Dict[int, SearchSearchItemTriggerALogicInputChannel]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CH<x>`` command.

        Description:
            - This command specifies the logic condition to be used in a logic search when the input
              is an analog channel. SEARCH<x> is the search number, which is always 1, and CH<x> is
              the channel number, which can be 1-4.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CH<x>?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CH<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CH<x> {HIGH|LOW|X}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CH<x>?
            ```

        Info:
            - ``HIGH`` specifies the logic high.
            - ``LOW`` specifies the logic low.
            - ``X`` specifies a 'don't care' state.
        """
        return self._ch

    @property
    def clock(self) -> SearchSearchItemTriggerALogicInputClock:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.edge``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:EDGE`` command.
            - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:SOUrce`` command.
        """
        return self._clock

    @property
    def d(self) -> Dict[int, SearchSearchItemTriggerALogicInputDigitalBit]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:D<x>`` command.

        Description:
            - This command specifies the logic condition to be used in a logic search when the input
              is a digital channel. SEARCH<x> is the search number, which is always 1, and D<x> is
              the digital channel number, which can be D0 - D16.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:D<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:D<x>?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:D<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:D<x> {HIGH|LOW|X}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:D<x>?
            ```

        Info:
            - ``HIGH`` specifies a high logic level.
            - ``LOW`` specifies a low logic level.
            - ``X`` specifies a 'don't care' condition.
        """
        return self._d

    @property
    def math(self) -> SearchSearchItemTriggerALogicInputMath:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:MATH`` command.

        Description:
            - This command specifies the logic condition of the math input to be used in a logic
              search. <x> is the search number, which is always 1.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:MATH?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:MATH?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:MATH value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:MATH {HIGH|LOW|X}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:MATH?
            ```

        Info:
            - ``HIGH`` specifies a high logic level.
            - ``LOW`` specifies a low logic level.
            - ``X`` specifies a 'don't care' condition.
        """
        return self._math

    @property
    def ref(self) -> Dict[int, SearchSearchItemTriggerALogicInputRefItem]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:REF<x>`` command.

        Description:
            - This command specifies the logic condition of the reference waveform to be used in a
              logic search. SEARCH<x> is the search number, which is always 1, and REF<x> is the
              reference channel number, which can be 1-4.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:REF<x>?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:REF<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:REF<x> {HIGH|LOW|X}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:REF<x>?
            ```

        Info:
            - ``HIGH`` specifies a high logic level.
            - ``LOW`` specifies a low logic level.
            - ``X`` specifies a 'don't care' condition.
        """
        return self._ref


class SearchSearchItemTriggerALogicFunction(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion`` command.

    Description:
        - Sets or returns the logic operator for a logic trigger search to determine where to place
          a mark. <x> is the search number.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion {AND|NANd}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion?
        ```

    Info:
        - ``AND`` places a mark if all conditions are true.
        - ``NANd`` places a mark if any of the conditions is false.
    """


class SearchSearchItemTriggerALogic(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.function``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion`` command.
        - ``.input``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut`` command tree.
        - ``.pattern``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern`` command tree.
        - ``.threshold``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._function = SearchSearchItemTriggerALogicFunction(
            device, f"{self._cmd_syntax}:FUNCtion"
        )
        self._input = SearchSearchItemTriggerALogicInput(device, f"{self._cmd_syntax}:INPut")
        self._pattern = SearchSearchItemTriggerALogicPattern(device, f"{self._cmd_syntax}:PATtern")
        self._threshold = SearchSearchItemTriggerALogicThreshold(
            device, f"{self._cmd_syntax}:THReshold"
        )

    @property
    def function(self) -> SearchSearchItemTriggerALogicFunction:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion`` command.

        Description:
            - Sets or returns the logic operator for a logic trigger search to determine where to
              place a mark. <x> is the search number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion {AND|NANd}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion?
            ```

        Info:
            - ``AND`` places a mark if all conditions are true.
            - ``NANd`` places a mark if any of the conditions is false.
        """
        return self._function

    @property
    def input(self) -> SearchSearchItemTriggerALogicInput:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CH<x>`` command.
            - ``.clock``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk`` command tree.
            - ``.d``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:D<x>`` command.
            - ``.math``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:MATH`` command.
            - ``.ref``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:REF<x>`` command.
        """
        return self._input

    @property
    def pattern(self) -> SearchSearchItemTriggerALogicPattern:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.input``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut`` command tree.
            - ``.when``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn`` command.
        """
        return self._pattern

    @property
    def threshold(self) -> SearchSearchItemTriggerALogicThreshold:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:CH<x>`` command.
            - ``.math``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:MATH`` command.
            - ``.ref``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:REF<x>`` command.
        """
        return self._threshold


class SearchSearchItemTriggerALevelRefItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:REF<x>`` command.

    Description:
        - Sets or returns the specified reference waveform level for an edge trigger search to
          determine where to place a mark. SEARCH<x> is the search number and REF<x> is the
          reference channel number.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:REF<x>?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:REF<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:REF<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LEVel:REF<x> {TTL|ECL}
        - SEARCH:SEARCH<x>:TRIGger:A:LEVel:REF<x>?
        ```

    Info:
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
        - ``ECL`` specifies a preset ECL high level of -1.3 V.
    """


class SearchSearchItemTriggerALevelMath(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:MATH`` command.

    Description:
        - [1] Sets or returns the math waveform level for an edge trigger search to determine where
          to place a mark. <x> is the search number. The value of MATH is 1 for all oscilloscopes.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:MATH?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:MATH?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:MATH value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LEVel:MATH {TTL|ECL}
        - SEARCH:SEARCH<x>:TRIGger:A:LEVel:MATH?
        ```

    Info:
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
        - ``ECL`` specifies a preset ECL high level of -1.3 V.
    """


class SearchSearchItemTriggerALevelChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:CH<x>`` command.

    Description:
        - Sets or returns the level for an edge trigger search to determine where to place a mark.
          SEARCH<x> is the search number and CH<x> is the channel number. Each channel can have an
          independent level.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:CH<x>?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:CH<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:CH<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LEVel:CH<x> {<NR3>|TTL|ECL}
        - SEARCH:SEARCH<x>:TRIGger:A:LEVel:CH<x>?
        ```

    Info:
        - ``<NR3>`` specifies the trigger level in volts.
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
        - ``ECL`` specifies a preset ECL high level of -1.3 V.
    """


class SearchSearchItemTriggerALevel(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel`` command.

    Description:
        - Sets or returns the level for an edge trigger search to determine where to place a mark.
          <x> is the search number.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:LEVel?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:LEVel?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LEVel value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LEVel {<NR3>|TTL|ECL}
        - SEARCH:SEARCH<x>:TRIGger:A:LEVel?
        ```

    Info:
        - ``<NR3>`` specifies the trigger level, in volts.
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
        - ``ECL`` specifies a preset ECL high level of -1.3 V.

    Properties:
        - ``.ch``: The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:CH<x>`` command.
        - ``.math``: The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:MATH`` command.
        - ``.ref``: The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:REF<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, SearchSearchItemTriggerALevelChannel] = DefaultDictPassKeyToFactory(
            lambda x: SearchSearchItemTriggerALevelChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._math = SearchSearchItemTriggerALevelMath(device, f"{self._cmd_syntax}:MATH")
        self._ref: Dict[int, SearchSearchItemTriggerALevelRefItem] = DefaultDictPassKeyToFactory(
            lambda x: SearchSearchItemTriggerALevelRefItem(device, f"{self._cmd_syntax}:REF{x}")
        )

    @property
    def ch(self) -> Dict[int, SearchSearchItemTriggerALevelChannel]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:CH<x>`` command.

        Description:
            - Sets or returns the level for an edge trigger search to determine where to place a
              mark. SEARCH<x> is the search number and CH<x> is the channel number. Each channel can
              have an independent level.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:CH<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:CH<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LEVel:CH<x> {<NR3>|TTL|ECL}
            - SEARCH:SEARCH<x>:TRIGger:A:LEVel:CH<x>?
            ```

        Info:
            - ``<NR3>`` specifies the trigger level in volts.
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
            - ``ECL`` specifies a preset ECL high level of -1.3 V.
        """
        return self._ch

    @property
    def math(self) -> SearchSearchItemTriggerALevelMath:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:MATH`` command.

        Description:
            - [1] Sets or returns the math waveform level for an edge trigger search to determine
              where to place a mark. <x> is the search number. The value of MATH is 1 for all
              oscilloscopes.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:MATH?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:MATH?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:MATH value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LEVel:MATH {TTL|ECL}
            - SEARCH:SEARCH<x>:TRIGger:A:LEVel:MATH?
            ```

        Info:
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
            - ``ECL`` specifies a preset ECL high level of -1.3 V.
        """
        return self._math

    @property
    def ref(self) -> Dict[int, SearchSearchItemTriggerALevelRefItem]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:REF<x>`` command.

        Description:
            - Sets or returns the specified reference waveform level for an edge trigger search to
              determine where to place a mark. SEARCH<x> is the search number and REF<x> is the
              reference channel number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:REF<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:REF<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LEVel:REF<x> {TTL|ECL}
            - SEARCH:SEARCH<x>:TRIGger:A:LEVel:REF<x>?
            ```

        Info:
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
            - ``ECL`` specifies a preset ECL high level of -1.3 V.
        """
        return self._ref


class SearchSearchItemTriggerAEdgeSource(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce`` command.

    Description:
        - Sets or returns the source waveform for an edge trigger search to determine where to place
          a mark. <x> is the search number.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce {CH<x>|MATH}
        - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies one input channel as the edge source, where <x> is the channel number.
        - ``MATH`` specifies the math waveform as the search source.
    """


class SearchSearchItemTriggerAEdgeSlope(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe`` command.

    Description:
        - Sets or returns the slope for an edge trigger search to determine where to place a mark.
          <x> is the search number.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe {RISe|FALL}
        - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe?
        ```

    Info:
        - ``RISe`` specifies a rising edge.
        - ``FALL`` specifies a falling edge.
    """


class SearchSearchItemTriggerAEdge(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:EDGE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:EDGE?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:EDGE?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.slope``: The ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe`` command.
        - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._slope = SearchSearchItemTriggerAEdgeSlope(device, f"{self._cmd_syntax}:SLOpe")
        self._source = SearchSearchItemTriggerAEdgeSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def slope(self) -> SearchSearchItemTriggerAEdgeSlope:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe`` command.

        Description:
            - Sets or returns the slope for an edge trigger search to determine where to place a
              mark. <x> is the search number.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe {RISe|FALL}
            - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe?
            ```

        Info:
            - ``RISe`` specifies a rising edge.
            - ``FALL`` specifies a falling edge.
        """
        return self._slope

    @property
    def source(self) -> SearchSearchItemTriggerAEdgeSource:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce`` command.

        Description:
            - Sets or returns the source waveform for an edge trigger search to determine where to
              place a mark. <x> is the search number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce {CH<x>|MATH}
            - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies one input channel as the edge source, where <x> is the channel
              number.
            - ``MATH`` specifies the math waveform as the search source.
        """
        return self._source


class SearchSearchItemTriggerABusSource(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce`` command.

    Description:
        - This command specifies the source of a bus search. <x> is the search number. SEARCH<x> is
          the search number, which is always 1.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce {B<x>}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce?
        ```

    Info:
        - ``B1`` specifies the Bus 1 source.
        - ``B2`` specifies the Bus 2 source.
        - ``B3`` specifies the Bus 3 source.
        - ``B4`` specifies the Bus 4 source.
    """


class SearchSearchItemTriggerABusBItemSpiDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:SIZe`` command.

    Description:
        - This command specifies the length of the data string to be used in an SPI search, if the
          search condition is MISO, MOSI, or MISOMOSI. SEARCH<x> is the search number, which is
          always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:SIZe?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:SIZe <NR1>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:SIZe?
        ```

    Info:
        - ``<NR1>`` is the data string length in bytes.
    """


class SearchSearchItemTriggerABusBItemSpiDataOutValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue`` command.

    Description:
        - This command specifies the data out value to be used in an SPI search if the search the
          condition is set to MOSI, or MISOMOSI. SEARCH<x> is the search number, which is always 1,
          and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue <bin>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue?
        ```

    Info:
        - ``<bin>`` is the data in binary format.
    """


class SearchSearchItemTriggerABusBItemSpiDataOut(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:OUT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:OUT?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:OUT?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = SearchSearchItemTriggerABusBItemSpiDataOutValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemSpiDataOutValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue`` command.

        Description:
            - This command specifies the data out value to be used in an SPI search if the search
              the condition is set to MOSI, or MISOMOSI. SEARCH<x> is the search number, which is
              always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue <bin>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue?
            ```

        Info:
            - ``<bin>`` is the data in binary format.
        """
        return self._value


class SearchSearchItemTriggerABusBItemSpiDataMosiValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue`` command.

    Description:
        - This command specifies the data out value to be used in an SPI search if the search the
          condition is set to MOSI, or MISOMOSI. SEARCH<x> is the search number, which is always 1,
          and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue <bin>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue?
        ```

    Info:
        - ``<bin>`` is the data in binary format.
    """


class SearchSearchItemTriggerABusBItemSpiDataMosi(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MOSI`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MOSI?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MOSI?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = SearchSearchItemTriggerABusBItemSpiDataMosiValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemSpiDataMosiValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue`` command.

        Description:
            - This command specifies the data out value to be used in an SPI search if the search
              the condition is set to MOSI, or MISOMOSI. SEARCH<x> is the search number, which is
              always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue <bin>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue?
            ```

        Info:
            - ``<bin>`` is the data in binary format.
        """
        return self._value


class SearchSearchItemTriggerABusBItemSpiDataMisoValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue`` command.

    Description:
        - This command specifies the data in value to be used in an SPI search, if the search
          condition is set to MISO or MISOMOSI. SEARCH<x> is the search number, which is always 1,
          and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue <bin>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue?
        ```

    Info:
        - ``<bin>`` is the data string in binary format.
    """


class SearchSearchItemTriggerABusBItemSpiDataMiso(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MISO`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MISO?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MISO?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = SearchSearchItemTriggerABusBItemSpiDataMisoValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemSpiDataMisoValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue`` command.

        Description:
            - This command specifies the data in value to be used in an SPI search, if the search
              condition is set to MISO or MISOMOSI. SEARCH<x> is the search number, which is always
              1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue <bin>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue?
            ```

        Info:
            - ``<bin>`` is the data string in binary format.
        """
        return self._value


class SearchSearchItemTriggerABusBItemSpiDataInValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue`` command.

    Description:
        - This command specifies the data in value to be used in an SPI search, if the search
          condition is set to MISO or MISOMOSI. SEARCH<x> is the search number, which is always 1,
          and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue <bin>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue?
        ```

    Info:
        - ``<bin>`` is the data string in binary format.
    """


class SearchSearchItemTriggerABusBItemSpiDataIn(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:IN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:IN?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:IN?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = SearchSearchItemTriggerABusBItemSpiDataInValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemSpiDataInValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue`` command.

        Description:
            - This command specifies the data in value to be used in an SPI search, if the search
              condition is set to MISO or MISOMOSI. SEARCH<x> is the search number, which is always
              1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue <bin>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue?
            ```

        Info:
            - ``<bin>`` is the data string in binary format.
        """
        return self._value


class SearchSearchItemTriggerABusBItemSpiData(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:SIZe`` command.
        - ``.miso``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MISO`` command tree.
        - ``.in``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:IN`` command tree.
        - ``.mosi``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MOSI`` command tree.
        - ``.out``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:OUT`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._size = SearchSearchItemTriggerABusBItemSpiDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._miso = SearchSearchItemTriggerABusBItemSpiDataMiso(device, f"{self._cmd_syntax}:MISO")
        self._in = SearchSearchItemTriggerABusBItemSpiDataIn(device, f"{self._cmd_syntax}:IN")
        self._mosi = SearchSearchItemTriggerABusBItemSpiDataMosi(device, f"{self._cmd_syntax}:MOSI")
        self._out = SearchSearchItemTriggerABusBItemSpiDataOut(device, f"{self._cmd_syntax}:OUT")

    @property
    def size(self) -> SearchSearchItemTriggerABusBItemSpiDataSize:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:SIZe`` command.

        Description:
            - This command specifies the length of the data string to be used in an SPI search, if
              the search condition is MISO, MOSI, or MISOMOSI. SEARCH<x> is the search number, which
              is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:SIZe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:SIZe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:SIZe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:SIZe <NR1>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:SIZe?
            ```

        Info:
            - ``<NR1>`` is the data string length in bytes.
        """
        return self._size

    @property
    def miso(self) -> SearchSearchItemTriggerABusBItemSpiDataMiso:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MISO`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MISO?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MISO?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue`` command.
        """
        return self._miso

    @property
    def in_(self) -> SearchSearchItemTriggerABusBItemSpiDataIn:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:IN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:IN?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:IN?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue`` command.
        """
        return self._in

    @property
    def mosi(self) -> SearchSearchItemTriggerABusBItemSpiDataMosi:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MOSI`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MOSI?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MOSI?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue`` command.
        """
        return self._mosi

    @property
    def out(self) -> SearchSearchItemTriggerABusBItemSpiDataOut:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:OUT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:OUT?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:OUT?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue`` command.
        """
        return self._out


class SearchSearchItemTriggerABusBItemSpiCondition(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:CONDition`` command.

    Description:
        - Sets or returns the search condition for a SPI trigger search. SEARCH<x> is the search
          number and B<x> is the bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:CONDition?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:CONDition value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:CONDition {SS|MISO|MOSI|MISOMOSI}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:CONDition?
        ```

    Info:
        - ``SS`` specifies a search based on the Slave Selection condition.
        - ``MISO`` specifies a search based on the Master-In Slave-Out condition.
        - ``MOSI`` specifies a search based on the Master-Out Slave-In condition.
        - ``MISOMOSI`` specifies a search based on the Master-In Slave-Out and Master-Out Slave-In
          conditions.
    """


class SearchSearchItemTriggerABusBItemSpi(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:CONDition`` command.
        - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = SearchSearchItemTriggerABusBItemSpiCondition(
            device, f"{self._cmd_syntax}:CONDition"
        )
        self._data = SearchSearchItemTriggerABusBItemSpiData(device, f"{self._cmd_syntax}:DATa")

    @property
    def condition(self) -> SearchSearchItemTriggerABusBItemSpiCondition:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:CONDition`` command.

        Description:
            - Sets or returns the search condition for a SPI trigger search. SEARCH<x> is the search
              number and B<x> is the bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:CONDition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:CONDition?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:CONDition value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:CONDition {SS|MISO|MOSI|MISOMOSI}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:CONDition?
            ```

        Info:
            - ``SS`` specifies a search based on the Slave Selection condition.
            - ``MISO`` specifies a search based on the Master-In Slave-Out condition.
            - ``MOSI`` specifies a search based on the Master-Out Slave-In condition.
            - ``MISOMOSI`` specifies a search based on the Master-In Slave-Out and Master-Out
              Slave-In conditions.
        """
        return self._condition

    @property
    def data(self) -> SearchSearchItemTriggerABusBItemSpiData:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:SIZe`` command.
            - ``.miso``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MISO`` command tree.
            - ``.in``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:IN`` command tree.
            - ``.mosi``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:MOSI`` command tree.
            - ``.out``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa:OUT`` command tree.
        """
        return self._data


class SearchSearchItemTriggerABusBItemRs232cTxDataValue(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue`` command.

    Description:
        - This command specifies the data value to be used for an RS-232 search, if the condition is
          set to RXDATA. SEARCH<x> is the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue?
        ```
    """


class SearchSearchItemTriggerABusBItemRs232cTxDataSize(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe`` command.

    Description:
        - This command specifies the length of the data string to be used for an RS-232 search if
          the search condition is set to TXDATA. SEARCH<x> is the search number, which is always 1,
          and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe?
        ```

    Info:
        - ``<NR1>`` is the length of the data string in Bytes.
    """


class SearchSearchItemTriggerABusBItemRs232cTxData(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    Properties:
        - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe`` command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._size = SearchSearchItemTriggerABusBItemRs232cTxDataSize(
            device, f"{self._cmd_syntax}:SIZe"
        )
        self._value = SearchSearchItemTriggerABusBItemRs232cTxDataValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def size(self) -> SearchSearchItemTriggerABusBItemRs232cTxDataSize:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe`` command.

        Description:
            - This command specifies the length of the data string to be used for an RS-232 search
              if the search condition is set to TXDATA. SEARCH<x> is the search number, which is
              always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe?
            ```

        Info:
            - ``<NR1>`` is the length of the data string in Bytes.
        """
        return self._size

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemRs232cTxDataValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue`` command.

        Description:
            - This command specifies the data value to be used for an RS-232 search, if the
              condition is set to RXDATA. SEARCH<x> is the search number, which is always 1, and
              B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue?
            ```
        """
        return self._value


class SearchSearchItemTriggerABusBItemRs232cTx(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._data = SearchSearchItemTriggerABusBItemRs232cTxData(
            device, f"{self._cmd_syntax}:DATa"
        )

    @property
    def data(self) -> SearchSearchItemTriggerABusBItemRs232cTxData:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe`` command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue`` command.
        """
        return self._data


class SearchSearchItemTriggerABusBItemRs232cRxDataValue(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue`` command.

    Description:
        - This command specifies the data value to be used in an RS-232 search, if the condition is
          set to RXDATA. SEARCH<x> is the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue?
        ```
    """


class SearchSearchItemTriggerABusBItemRs232cRxDataSize(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe`` command.

    Description:
        - This command specifies the length of the data string to be used in an RS-232 search, if
          the search condition is set to RXDATA. SEARCH<x> is the search number, which is always 1,
          and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe?
        ```

    Info:
        - ``<NR1>`` is the length of the data string in Bytes.
    """


class SearchSearchItemTriggerABusBItemRs232cRxData(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    Properties:
        - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe`` command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._size = SearchSearchItemTriggerABusBItemRs232cRxDataSize(
            device, f"{self._cmd_syntax}:SIZe"
        )
        self._value = SearchSearchItemTriggerABusBItemRs232cRxDataValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def size(self) -> SearchSearchItemTriggerABusBItemRs232cRxDataSize:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe`` command.

        Description:
            - This command specifies the length of the data string to be used in an RS-232 search,
              if the search condition is set to RXDATA. SEARCH<x> is the search number, which is
              always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe?
            ```

        Info:
            - ``<NR1>`` is the length of the data string in Bytes.
        """
        return self._size

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemRs232cRxDataValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue`` command.

        Description:
            - This command specifies the data value to be used in an RS-232 search, if the condition
              is set to RXDATA. SEARCH<x> is the search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue?
            ```
        """
        return self._value


class SearchSearchItemTriggerABusBItemRs232cRx(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._data = SearchSearchItemTriggerABusBItemRs232cRxData(
            device, f"{self._cmd_syntax}:DATa"
        )

    @property
    def data(self) -> SearchSearchItemTriggerABusBItemRs232cRxData:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe`` command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue`` command.
        """
        return self._data


class SearchSearchItemTriggerABusBItemRs232cCondition(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:CONDition`` command.

    Description:
        - Sets or returns the condition for a RS232 trigger search. SEARCH<x> is the search number
          and B<x> is the bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:CONDition?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:CONDition value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:CONDition {RXSTArt|RXDATA|RXENDPacket|RXPARity|TXSTArt|TXDATA|TXENDPacket|TXPARity}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:CONDition?
        ```

    Info:
        - ``RXSTArt`` specifies a search based on the RX Start Bit.
        - ``RXDATA`` specifies a search based on RX Data.
        - ``RXENDPacket`` specifies a search based on the RX End of Packet condition.
        - ``RXPARIty`` specifies a search based on the RX parity.
        - ``TXSTArt`` specifies a search base on the TX Start Bit.
        - ``TXDATA`` specifies a search based on TX Data.
        - ``TXENDPacket`` specifies a search based on the TX End of Packet condition.
        - ``TXPARIty`` specifies a search based on the TX parity.
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemRs232c(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:CONDition`` command.
        - ``.rx``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX`` command tree.
        - ``.tx``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = SearchSearchItemTriggerABusBItemRs232cCondition(
            device, f"{self._cmd_syntax}:CONDition"
        )
        self._rx = SearchSearchItemTriggerABusBItemRs232cRx(device, f"{self._cmd_syntax}:RX")
        self._tx = SearchSearchItemTriggerABusBItemRs232cTx(device, f"{self._cmd_syntax}:TX")

    @property
    def condition(self) -> SearchSearchItemTriggerABusBItemRs232cCondition:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:CONDition`` command.

        Description:
            - Sets or returns the condition for a RS232 trigger search. SEARCH<x> is the search
              number and B<x> is the bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:CONDition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:CONDition?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:CONDition value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:CONDition {RXSTArt|RXDATA|RXENDPacket|RXPARity|TXSTArt|TXDATA|TXENDPacket|TXPARity}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:CONDition?
            ```

        Info:
            - ``RXSTArt`` specifies a search based on the RX Start Bit.
            - ``RXDATA`` specifies a search based on RX Data.
            - ``RXENDPacket`` specifies a search based on the RX End of Packet condition.
            - ``RXPARIty`` specifies a search based on the RX parity.
            - ``TXSTArt`` specifies a search base on the TX Start Bit.
            - ``TXDATA`` specifies a search based on TX Data.
            - ``TXENDPacket`` specifies a search based on the TX End of Packet condition.
            - ``TXPARIty`` specifies a search based on the TX parity.
        """  # noqa: E501
        return self._condition

    @property
    def rx(self) -> SearchSearchItemTriggerABusBItemRs232cRx:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        Sub-properties:
            - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa`` command tree.
        """
        return self._rx

    @property
    def tx(self) -> SearchSearchItemTriggerABusBItemRs232cTx:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        Sub-properties:
            - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa`` command tree.
        """
        return self._tx


class SearchSearchItemTriggerABusBItemParallelValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel:VALue`` command.

    Description:
        - This command specifies the data value to be used in a Parallel search. SEARCH<x> is the
          search number and B<x> SEARCH<x> is the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel:VALue?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel:VALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel:VALue?
        ```

    Info:
        - ``<QString>`` is the binary data string.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemParallel(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = SearchSearchItemTriggerABusBItemParallelValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemParallelValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel:VALue`` command.

        Description:
            - This command specifies the data value to be used in a Parallel search. SEARCH<x> is
              the search number and B<x> SEARCH<x> is the search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel:VALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel:VALue?
            ```

        Info:
            - ``<QString>`` is the binary data string.
        """
        return self._value


class SearchSearchItemTriggerABusBItemLinIdentifierValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue`` command.

    Description:
        - This command specifies the binary address string used for LIN search if search condition
          is set to IDentifier or IDANDDATA (identifier and data). SEARCH<x> is the search number,
          which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue?
        ```

    Info:
        - ``<QString>`` is a quoted string specifying the binary address string to be used in a LIN
          search if the search condition is set to IDentifier or IDANDDATA (identifier and data).
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemLinIdentifier(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:IDentifier`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:IDentifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:IDentifier?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = SearchSearchItemTriggerABusBItemLinIdentifierValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemLinIdentifierValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue`` command.

        Description:
            - This command specifies the binary address string used for LIN search if search
              condition is set to IDentifier or IDANDDATA (identifier and data). SEARCH<x> is the
              search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue?
            ```

        Info:
            - ``<QString>`` is a quoted string specifying the binary address string to be used in a
              LIN search if the search condition is set to IDentifier or IDANDDATA (identifier and
              data).
        """
        return self._value


class SearchSearchItemTriggerABusBItemLinErrtype(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:ERRTYPE`` command.

    Description:
        - Sets or returns the error type used for a LIN Search.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:ERRTYPE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:ERRTYPE?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:ERRTYPE value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:ERRTYPE {SYNC|PARity|CHecksum}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:ERRTYPE?
        ```

    Info:
        - ``SYNC`` specifies a sync error type.
        - ``PARity`` specifies a parity error type.
        - ``CHecksum`` specifies a checksum error type.
    """


class SearchSearchItemTriggerABusBItemLinDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:VALue`` command.

    Description:
        - This command specifies the data value to be used in a LIN search if the search condition
          is set to IDentifier or IDANDDATA (identifier and data). SEARCH<x> is the search number,
          which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:VALue?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:VALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:VALue?
        ```

    Info:
        - ``<QString>`` is the binary data string for the search.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemLinDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:SIZe`` command.

    Description:
        - This command specifies the length of the data string, in bytes, to be used in a LIN
          search, if the search condition is set to IDentifier or IDANDDATA (identifier and data).
          SEARCH<x> is the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:SIZe?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:SIZe <NR1>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:SIZe?
        ```

    Info:
        - ``<NR1>`` is the length of the data in bytes.
    """


class SearchSearchItemTriggerABusBItemLinDataQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier`` command.

    Description:
        - Sets or returns the LIN data qualifier. This only applies if the trigger condition is
          IDANDDATA or DATA.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?
        ```

    Info:
        - ``LESSThan`` sets the LIN data qualifier to less than.
        - ``MOREThan`` sets the LIN data qualifier to greater than.
        - ``EQUal`` sets the LIN data qualifier to equal.
        - ``UNEQual`` sets the LIN data qualifier to not equal.
        - ``LESSEQual`` sets the LIN data qualifier to less than or equal.
        - ``MOREEQual`` sets the LIN data qualifier to more than or equal.
        - ``INrange`` sets the LIN data qualifier to in range.
        - ``OUTrange`` sets the LIN data qualifier to out of range.
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemLinDataHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue`` command.

    Description:
        - This command specifies the high data value to be used in a LIN search, if the search
          condition is set to IDentifier or IDANDDATA (identifier and data). SEARCH<x> is the search
          number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue?
        ```

    Info:
        - ``<QString>`` is a quoted string of 1s, 0s, or Xs representing the binary data string to
          be used in a LIN search if the search condition is IDentifier or IDANDDATA (identifier and
          data).
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemLinData(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue`` command.
        - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier`` command.
        - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:SIZe`` command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = SearchSearchItemTriggerABusBItemLinDataHivalue(
            device, f"{self._cmd_syntax}:HIVALue"
        )
        self._qualifier = SearchSearchItemTriggerABusBItemLinDataQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._size = SearchSearchItemTriggerABusBItemLinDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._value = SearchSearchItemTriggerABusBItemLinDataValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def hivalue(self) -> SearchSearchItemTriggerABusBItemLinDataHivalue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue`` command.

        Description:
            - This command specifies the high data value to be used in a LIN search, if the search
              condition is set to IDentifier or IDANDDATA (identifier and data). SEARCH<x> is the
              search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue?
            ```

        Info:
            - ``<QString>`` is a quoted string of 1s, 0s, or Xs representing the binary data string
              to be used in a LIN search if the search condition is IDentifier or IDANDDATA
              (identifier and data).
        """
        return self._hivalue

    @property
    def qualifier(self) -> SearchSearchItemTriggerABusBItemLinDataQualifier:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier`` command.

        Description:
            - Sets or returns the LIN data qualifier. This only applies if the trigger condition is
              IDANDDATA or DATA.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?
            ```

        Info:
            - ``LESSThan`` sets the LIN data qualifier to less than.
            - ``MOREThan`` sets the LIN data qualifier to greater than.
            - ``EQUal`` sets the LIN data qualifier to equal.
            - ``UNEQual`` sets the LIN data qualifier to not equal.
            - ``LESSEQual`` sets the LIN data qualifier to less than or equal.
            - ``MOREEQual`` sets the LIN data qualifier to more than or equal.
            - ``INrange`` sets the LIN data qualifier to in range.
            - ``OUTrange`` sets the LIN data qualifier to out of range.
        """  # noqa: E501
        return self._qualifier

    @property
    def size(self) -> SearchSearchItemTriggerABusBItemLinDataSize:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:SIZe`` command.

        Description:
            - This command specifies the length of the data string, in bytes, to be used in a LIN
              search, if the search condition is set to IDentifier or IDANDDATA (identifier and
              data). SEARCH<x> is the search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:SIZe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:SIZe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:SIZe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:SIZe <NR1>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:SIZe?
            ```

        Info:
            - ``<NR1>`` is the length of the data in bytes.
        """
        return self._size

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemLinDataValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:VALue`` command.

        Description:
            - This command specifies the data value to be used in a LIN search if the search
              condition is set to IDentifier or IDANDDATA (identifier and data). SEARCH<x> is the
              search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:VALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:VALue?
            ```

        Info:
            - ``<QString>`` is the binary data string for the search.
        """
        return self._value


class SearchSearchItemTriggerABusBItemLinCondition(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:CONDition`` command.

    Description:
        - This command specifies the search condition for a LIN search. SEARCH<x> is the search
          number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:CONDition?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:CONDition value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:CONDition {SYNCField|IDentifier|DATA|IDANDDATA|WAKEup|SLEEP|ERROR}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:CONDition?
        ```

    Info:
        - ``SYNCField`` specifies to search on the sync field.
        - ``IDentifier`` specifies to search on the identifier.
        - ``DATA`` specifies to search on the data.
        - ``IDANDDATA`` specifies to search on the identifier and the data.
        - ``WAKEup`` specifies to search on wake up.
        - ``SLEEP`` specifies to search on sleep.
        - ``ERROR`` specifies to search on errors.
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemLin(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:CONDition`` command.
        - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa`` command tree.
        - ``.errtype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:ERRTYPE`` command.
        - ``.identifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:IDentifier`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = SearchSearchItemTriggerABusBItemLinCondition(
            device, f"{self._cmd_syntax}:CONDition"
        )
        self._data = SearchSearchItemTriggerABusBItemLinData(device, f"{self._cmd_syntax}:DATa")
        self._errtype = SearchSearchItemTriggerABusBItemLinErrtype(
            device, f"{self._cmd_syntax}:ERRTYPE"
        )
        self._identifier = SearchSearchItemTriggerABusBItemLinIdentifier(
            device, f"{self._cmd_syntax}:IDentifier"
        )

    @property
    def condition(self) -> SearchSearchItemTriggerABusBItemLinCondition:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:CONDition`` command.

        Description:
            - This command specifies the search condition for a LIN search. SEARCH<x> is the search
              number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:CONDition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:CONDition?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:CONDition value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:CONDition {SYNCField|IDentifier|DATA|IDANDDATA|WAKEup|SLEEP|ERROR}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:CONDition?
            ```

        Info:
            - ``SYNCField`` specifies to search on the sync field.
            - ``IDentifier`` specifies to search on the identifier.
            - ``DATA`` specifies to search on the data.
            - ``IDANDDATA`` specifies to search on the identifier and the data.
            - ``WAKEup`` specifies to search on wake up.
            - ``SLEEP`` specifies to search on sleep.
            - ``ERROR`` specifies to search on errors.
        """  # noqa: E501
        return self._condition

    @property
    def data(self) -> SearchSearchItemTriggerABusBItemLinData:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue`` command.
            - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier``
              command.
            - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:SIZe`` command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:VALue`` command.
        """
        return self._data

    @property
    def errtype(self) -> SearchSearchItemTriggerABusBItemLinErrtype:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:ERRTYPE`` command.

        Description:
            - Sets or returns the error type used for a LIN Search.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:ERRTYPE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:ERRTYPE?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:ERRTYPE value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:ERRTYPE {SYNC|PARity|CHecksum}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:ERRTYPE?
            ```

        Info:
            - ``SYNC`` specifies a sync error type.
            - ``PARity`` specifies a parity error type.
            - ``CHecksum`` specifies a checksum error type.
        """
        return self._errtype

    @property
    def identifier(self) -> SearchSearchItemTriggerABusBItemLinIdentifier:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:IDentifier`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:IDentifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:IDentifier?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue`` command.
        """
        return self._identifier


class SearchSearchItemTriggerABusBItemI2cDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:VALue`` command.

    Description:
        - This command specifies the data value to be used in an I2C search, if the search condition
          is set to DATA or ADDRANDDATA (address and data). SEARCH<x> is the search number, which is
          always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:VALue?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:VALue <bin>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:VALue?
        ```

    Info:
        - ``<bin>`` is the data in binary format.
    """


class SearchSearchItemTriggerABusBItemI2cDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:SIZe`` command.

    Description:
        - This command specifies the length of the data string, in bytes, to be used for an I2C
          search, if the search condition is set to DATA or ADDRANDDATA (address and data).
          SEARCH<x> is the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:SIZe?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:SIZe <NR1>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:SIZe?
        ```

    Info:
        - ``<NR1>`` is the data string length in bytes.
    """


class SearchSearchItemTriggerABusBItemI2cDataDirection(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:DIRection`` command.

    Description:
        - This command specifies the data direction to use for an I2C search: either read, write, or
          either. SEARCH<x> is the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:DIRection?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:DIRection?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:DIRection value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:DIRection {READ|WRITE|NOCARE}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:DIRection?
        ```

    Info:
        - ``READ`` specifies a read condition.
        - ``WRITE`` specifies a write condition.
        - ``NOCARE`` specifies either a read or write condition.
    """


class SearchSearchItemTriggerABusBItemI2cData(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.direction``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:DIRection`` command.
        - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:SIZe`` command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._direction = SearchSearchItemTriggerABusBItemI2cDataDirection(
            device, f"{self._cmd_syntax}:DIRection"
        )
        self._size = SearchSearchItemTriggerABusBItemI2cDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._value = SearchSearchItemTriggerABusBItemI2cDataValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def direction(self) -> SearchSearchItemTriggerABusBItemI2cDataDirection:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:DIRection`` command.

        Description:
            - This command specifies the data direction to use for an I2C search: either read,
              write, or either. SEARCH<x> is the search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:DIRection?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:DIRection?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:DIRection value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:DIRection {READ|WRITE|NOCARE}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:DIRection?
            ```

        Info:
            - ``READ`` specifies a read condition.
            - ``WRITE`` specifies a write condition.
            - ``NOCARE`` specifies either a read or write condition.
        """
        return self._direction

    @property
    def size(self) -> SearchSearchItemTriggerABusBItemI2cDataSize:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:SIZe`` command.

        Description:
            - This command specifies the length of the data string, in bytes, to be used for an I2C
              search, if the search condition is set to DATA or ADDRANDDATA (address and data).
              SEARCH<x> is the search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:SIZe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:SIZe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:SIZe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:SIZe <NR1>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:SIZe?
            ```

        Info:
            - ``<NR1>`` is the data string length in bytes.
        """
        return self._size

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemI2cDataValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:VALue`` command.

        Description:
            - This command specifies the data value to be used in an I2C search, if the search
              condition is set to DATA or ADDRANDDATA (address and data). SEARCH<x> is the search
              number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:VALue <bin>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:VALue?
            ```

        Info:
            - ``<bin>`` is the data in binary format.
        """
        return self._value


class SearchSearchItemTriggerABusBItemI2cCondition(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:CONDition`` command.

    Description:
        - This command specifies the search condition to use for an I2C search. SEARCH<x> is the
          search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:CONDition?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:CONDition value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:CONDition {STARt|STOP|REPEATstart|ACKMISS|ADDRess|DATA|ADDRANDDATA}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:CONDition?
        ```

    Info:
        - ``STARt`` specifies a search based on a start condition.
        - ``STOP`` specifies a search based on a stop condition.
        - ``REPEATstart`` specifies a search based on a repeat of start condition.
        - ``ACKMISS`` specifies a search based on a missing acknowledgement condition.
        - ``ADDRess`` specifies a search based on an address.
        - ``DATA`` specifies a search based on a data condition.
        - ``ADDRANDDATA`` specifies a search based on an address and data condition.
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemI2cAddressValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue`` command.

    Description:
        - This command specifies the address value to be used in an I2C search if the search
          condition is ADDRess or ADDRANDDATA (address and data). SEARCH<x> is the search number,
          which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue <bin>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue?
        ```

    Info:
        - ``<bin>`` is the address in binary format.
    """


class SearchSearchItemTriggerABusBItemI2cAddressType(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe`` command.

    Description:
        - This command specifies the I2C address type to be used in an I2C search. SEARCH<x> is the
          search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe {GENeralcall|STARtbyte|HSmode|EEPROM|USER}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe?
        ```

    Info:
        - ``GENeralcall`` specifies the GENeralcall address type.
        - ``STARtbyte`` specifies the STARtbyte address type.
        - ``HSmode`` specifies the HSmode address type.
        - ``EEPROM`` specifies the EEPROM address type.
        - ``USER`` specifies a user address.
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemI2cAddressMode(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe`` command.

    Description:
        - This command specifies the I2C address mode to be used in an I2C search: either 7 or
          10-Bit. SEARCH<x> is the search number and B<x> SEARCH<x> is the search number, which is
          always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe {ADDR7|ADDR10}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe?
        ```

    Info:
        - ``ADDR7`` specifies 7-bit addresses.
        - ``ADDR10`` specifies 10-bit addresses.
    """


class SearchSearchItemTriggerABusBItemI2cAddress(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.mode``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe`` command.
        - ``.type``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe`` command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = SearchSearchItemTriggerABusBItemI2cAddressMode(
            device, f"{self._cmd_syntax}:MODe"
        )
        self._type = SearchSearchItemTriggerABusBItemI2cAddressType(
            device, f"{self._cmd_syntax}:TYPe"
        )
        self._value = SearchSearchItemTriggerABusBItemI2cAddressValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def mode(self) -> SearchSearchItemTriggerABusBItemI2cAddressMode:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe`` command.

        Description:
            - This command specifies the I2C address mode to be used in an I2C search: either 7 or
              10-Bit. SEARCH<x> is the search number and B<x> SEARCH<x> is the search number, which
              is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe {ADDR7|ADDR10}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe?
            ```

        Info:
            - ``ADDR7`` specifies 7-bit addresses.
            - ``ADDR10`` specifies 10-bit addresses.
        """
        return self._mode

    @property
    def type(self) -> SearchSearchItemTriggerABusBItemI2cAddressType:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe`` command.

        Description:
            - This command specifies the I2C address type to be used in an I2C search. SEARCH<x> is
              the search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe {GENeralcall|STARtbyte|HSmode|EEPROM|USER}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe?
            ```

        Info:
            - ``GENeralcall`` specifies the GENeralcall address type.
            - ``STARtbyte`` specifies the STARtbyte address type.
            - ``HSmode`` specifies the HSmode address type.
            - ``EEPROM`` specifies the EEPROM address type.
            - ``USER`` specifies a user address.
        """  # noqa: E501
        return self._type

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemI2cAddressValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue`` command.

        Description:
            - This command specifies the address value to be used in an I2C search if the search
              condition is ADDRess or ADDRANDDATA (address and data). SEARCH<x> is the search
              number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue <bin>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue?
            ```

        Info:
            - ``<bin>`` is the address in binary format.
        """
        return self._value


class SearchSearchItemTriggerABusBItemI2c(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.address``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess`` command tree.
        - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:CONDition`` command.
        - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._address = SearchSearchItemTriggerABusBItemI2cAddress(
            device, f"{self._cmd_syntax}:ADDRess"
        )
        self._condition = SearchSearchItemTriggerABusBItemI2cCondition(
            device, f"{self._cmd_syntax}:CONDition"
        )
        self._data = SearchSearchItemTriggerABusBItemI2cData(device, f"{self._cmd_syntax}:DATa")

    @property
    def address(self) -> SearchSearchItemTriggerABusBItemI2cAddress:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        Sub-properties:
            - ``.mode``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe`` command.
            - ``.type``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe`` command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue`` command.
        """
        return self._address

    @property
    def condition(self) -> SearchSearchItemTriggerABusBItemI2cCondition:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:CONDition`` command.

        Description:
            - This command specifies the search condition to use for an I2C search. SEARCH<x> is the
              search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:CONDition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:CONDition?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:CONDition value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:CONDition {STARt|STOP|REPEATstart|ACKMISS|ADDRess|DATA|ADDRANDDATA}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:CONDition?
            ```

        Info:
            - ``STARt`` specifies a search based on a start condition.
            - ``STOP`` specifies a search based on a stop condition.
            - ``REPEATstart`` specifies a search based on a repeat of start condition.
            - ``ACKMISS`` specifies a search based on a missing acknowledgement condition.
            - ``ADDRess`` specifies a search based on an address.
            - ``DATA`` specifies a search based on a data condition.
            - ``ADDRANDDATA`` specifies a search based on an address and data condition.
        """  # noqa: E501
        return self._condition

    @property
    def data(self) -> SearchSearchItemTriggerABusBItemI2cData:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.direction``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:DIRection``
              command.
            - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:SIZe`` command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa:VALue`` command.
        """
        return self._data


class SearchSearchItemTriggerABusBItemFlexrayHeaderPaylength(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength`` command.

    Description:
        - This command specifies to use the payload length portion of the binary header string when
          searching on the FlexRay bus header. This command specifies the payload length to be used
          in a FlexRay search. The search condition needs to be set to HEADer (using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search number,
          which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength?
        ```

    Info:
        - ``<QString>`` is a quoted string representing the payload length portion of the binary
          header string used for a FlexRay search.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemFlexrayHeaderIndbits(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits`` command.

    Description:
        - This command specifies to use the indicator bits portion of the binary header string when
          searching on the FlexRay bus header. The search condition needs to be set to HEADer (using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search number,
          which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemFlexrayHeaderFrameid(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID`` command.

    Description:
        - This command specifies to use the frame ID portion of the binary header string when
          searching on the FlexRay bus header. The search condition needs to be set to HEADer (using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search number,
          which is always 1, and B<x>.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID?
        ```

    Info:
        - ``<QString>`` is a quoted string representing the frame ID portion of the binary header
          string used for a FlexRay search.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemFlexrayHeaderCyclecount(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount`` command.

    Description:
        - This command specifies to use the cycle count portion of the binary header string when
          searching on the FlexRay bus header. The search condition needs to be set to HEADer (using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search number,
          which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount?
        ```

    Info:
        - ``<QString>`` is a quoted string representing the cycle count portion of the binary header
          string used for FlexRay search.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemFlexrayHeaderCrc(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC`` command.

    Description:
        - This command specifies the CRC portion of the binary header string to be used when
          searching on FlexRay bus data. The search condition needs to be set to HEADer (using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search number,
          which is always 1, B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC?
        ```

    Info:
        - ``<QString>`` is a quoted string representing the CRC portion of the binary header string
          used for FlexRay search.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemFlexrayHeader(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    Properties:
        - ``.crc``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC`` command.
        - ``.cyclecount``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount``
          command.
        - ``.frameid``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID`` command.
        - ``.indbits``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits`` command.
        - ``.paylength``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength``
          command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._crc = SearchSearchItemTriggerABusBItemFlexrayHeaderCrc(
            device, f"{self._cmd_syntax}:CRC"
        )
        self._cyclecount = SearchSearchItemTriggerABusBItemFlexrayHeaderCyclecount(
            device, f"{self._cmd_syntax}:CYCLEcount"
        )
        self._frameid = SearchSearchItemTriggerABusBItemFlexrayHeaderFrameid(
            device, f"{self._cmd_syntax}:FRAMEID"
        )
        self._indbits = SearchSearchItemTriggerABusBItemFlexrayHeaderIndbits(
            device, f"{self._cmd_syntax}:INDBits"
        )
        self._paylength = SearchSearchItemTriggerABusBItemFlexrayHeaderPaylength(
            device, f"{self._cmd_syntax}:PAYLength"
        )

    @property
    def crc(self) -> SearchSearchItemTriggerABusBItemFlexrayHeaderCrc:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC`` command.

        Description:
            - This command specifies the CRC portion of the binary header string to be used when
              searching on FlexRay bus data. The search condition needs to be set to HEADer (using
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search
              number, which is always 1, B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC?
            ```

        Info:
            - ``<QString>`` is a quoted string representing the CRC portion of the binary header
              string used for FlexRay search.
        """
        return self._crc

    @property
    def cyclecount(self) -> SearchSearchItemTriggerABusBItemFlexrayHeaderCyclecount:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount`` command.

        Description:
            - This command specifies to use the cycle count portion of the binary header string when
              searching on the FlexRay bus header. The search condition needs to be set to HEADer
              (using ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search
              number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount?
            ```

        Info:
            - ``<QString>`` is a quoted string representing the cycle count portion of the binary
              header string used for FlexRay search.
        """
        return self._cyclecount

    @property
    def frameid(self) -> SearchSearchItemTriggerABusBItemFlexrayHeaderFrameid:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID`` command.

        Description:
            - This command specifies to use the frame ID portion of the binary header string when
              searching on the FlexRay bus header. The search condition needs to be set to HEADer
              (using ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search
              number, which is always 1, and B<x>.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID?
            ```

        Info:
            - ``<QString>`` is a quoted string representing the frame ID portion of the binary
              header string used for a FlexRay search.
        """
        return self._frameid

    @property
    def indbits(self) -> SearchSearchItemTriggerABusBItemFlexrayHeaderIndbits:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits`` command.

        Description:
            - This command specifies to use the indicator bits portion of the binary header string
              when searching on the FlexRay bus header. The search condition needs to be set to
              HEADer (using ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the
              search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits?
            ```
        """
        return self._indbits

    @property
    def paylength(self) -> SearchSearchItemTriggerABusBItemFlexrayHeaderPaylength:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength`` command.

        Description:
            - This command specifies to use the payload length portion of the binary header string
              when searching on the FlexRay bus header. This command specifies the payload length to
              be used in a FlexRay search. The search condition needs to be set to HEADer (using
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search
              number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength?
            ```

        Info:
            - ``<QString>`` is a quoted string representing the payload length portion of the binary
              header string used for a FlexRay search.
        """
        return self._paylength


class SearchSearchItemTriggerABusBItemFlexrayFrametype(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEType`` command.

    Description:
        - This command specifies the frame type (normal, payload, null, sync or startup) to use when
          searching on FlexRay bus data. The search condition needs to be set to FRAMEType (using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search number,
          which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEType?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEType?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEType value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEType {NORMal|PAYLoad|NULL|SYNC|STARTup}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEType?
        ```

    Info:
        - ``NORMal`` sets the frame type to normal.
        - ``PAYLoad`` sets the frame type to payload.
        - ``NULL`` sets the frame type to NULL.
        - ``SYNC`` sets the frame type to sync.
        - ``STARTup`` sets the frame type to start up.
    """


class SearchSearchItemTriggerABusBItemFlexrayFrameidValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue`` command.

    Description:
        - This command specifies the low value to use when searching on the FlexRay bus frame ID
          field. (Use ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:FRAMEID:HIVALUE`` to set the high
          value.) The search condition needs to be set to IDentifier (using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search number,
          which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue?
        ```

    Info:
        - ``<QString>`` is a quoted string representing the binary data string used for FlexRay
          frame ID low value.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemFlexrayFrameidQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier`` command.

    Description:
        - Sets or returns the FLEXRAY frame ID qualifier.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier?
        ```

    Info:
        - ``LESSThan`` sets the frame id qualifier to LESSThan.
        - ``MOREThan`` sets the frame id qualifier to MOREThan.
        - ``QUal`` sets the frame id qualifier to QUal.
        - ``UNEQual`` sets the frame id qualifier to UNEQual.
        - ``LESSEQual`` sets the frame id qualifier to LESSEQual.
        - ``MOREEQual`` sets the frame id qualifier to MOREEQual.
        - ``INrange`` sets the frame id qualifier to INrange.
        - ``OUTrange`` sets the frame id qualifier to OUTrange.
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemFlexrayFrameidHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue`` command.

    Description:
        - This command specifies the high value to use when searching on the FlexRay bus frame ID
          field. (Use ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:FRAMEID:VALUE`` to set the low
          value.) The search condition needs to be set to IDentifier (using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search number,
          which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemFlexrayFrameid(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue`` command.
        - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier``
          command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = SearchSearchItemTriggerABusBItemFlexrayFrameidHivalue(
            device, f"{self._cmd_syntax}:HIVALue"
        )
        self._qualifier = SearchSearchItemTriggerABusBItemFlexrayFrameidQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._value = SearchSearchItemTriggerABusBItemFlexrayFrameidValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def hivalue(self) -> SearchSearchItemTriggerABusBItemFlexrayFrameidHivalue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue`` command.

        Description:
            - This command specifies the high value to use when searching on the FlexRay bus frame
              ID field. (Use ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:FRAMEID:VALUE`` to set the
              low value.) The search condition needs to be set to IDentifier (using
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search
              number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue?
            ```
        """
        return self._hivalue

    @property
    def qualifier(self) -> SearchSearchItemTriggerABusBItemFlexrayFrameidQualifier:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier`` command.

        Description:
            - Sets or returns the FLEXRAY frame ID qualifier.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier?
            ```

        Info:
            - ``LESSThan`` sets the frame id qualifier to LESSThan.
            - ``MOREThan`` sets the frame id qualifier to MOREThan.
            - ``QUal`` sets the frame id qualifier to QUal.
            - ``UNEQual`` sets the frame id qualifier to UNEQual.
            - ``LESSEQual`` sets the frame id qualifier to LESSEQual.
            - ``MOREEQual`` sets the frame id qualifier to MOREEQual.
            - ``INrange`` sets the frame id qualifier to INrange.
            - ``OUTrange`` sets the frame id qualifier to OUTrange.
        """  # noqa: E501
        return self._qualifier

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemFlexrayFrameidValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue`` command.

        Description:
            - This command specifies the low value to use when searching on the FlexRay bus frame ID
              field. (Use ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:FRAMEID:HIVALUE`` to set the
              high value.) The search condition needs to be set to IDentifier (using
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search
              number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue?
            ```

        Info:
            - ``<QString>`` is a quoted string representing the binary data string used for FlexRay
              frame ID low value.
        """
        return self._value


class SearchSearchItemTriggerABusBItemFlexrayErrtype(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE`` command.

    Description:
        - This command specifies the error type to use when searching on the FlexRay bus signal. The
          search condition needs to be set to ERROR (using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search number,
          which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE {CRCHeader|CRCTrailer|SYNCFrame|STARTupnosync|NULLFRStatic|NULLFRDynamic}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE?
        ```

    Info:
        - ``CRCHeader`` sets the error type to CRC header.
        - ``CRCTrailer`` sets the error type to CRC trailer.
        - ``SYNCFrame`` sets the error type to sync frame.
        - ``STARTupnosync`` sets the error type to start up with no sync.
        - ``NULLFRStatic`` sets the error type to null frame static.
        - ``NULLFRDynamic`` sets the error type to null frame dynamic.
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemFlexrayEoftype(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE`` command.

    Description:
        - This command specifies which end of file type to use (static, dynamic or any) when
          searching on the FlexRay bus EOF field. The search condition needs to be set to EOF (using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search number,
          which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE {STATic|DYNAMic|ANY}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE?
        ```

    Info:
        - ``STATic`` sets the FlexRay end of frame type to STATIC.
        - ``DYNAMic`` sets the FlexRay end of frame type to DYNAMIC.
        - ``ANY`` sets the FlexRay end of frame type to ANY type.
    """


class SearchSearchItemTriggerABusBItemFlexrayDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue`` command.

    Description:
        - This command specifies the low value to use when searching on the FlexRay bus data field.
          The search condition needs to be set to ID or IDANDDATA (using
          ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search number, which is always
          1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue?
        ```

    Info:
        - ``<QString>`` is a quoted string that is the low binary data string to be used for a
          FlexRay search if the search condition is set to IDANDDATA.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemFlexrayDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe`` command.

    Description:
        - This command specifies the length of the data string, in bytes, to use when searching on
          the FlexRay bus data field. The search condition needs to be set to ID or IDANDDATA (using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search number,
          which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe <NR1>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe?
        ```

    Info:
        - ``<NR1>`` is the length of the data string in bytes. Length range is 1 to 8.
    """


class SearchSearchItemTriggerABusBItemFlexrayDataQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier`` command.

    Description:
        - Sets or returns the FLEXRAY data qualifier.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier?
        ```

    Info:
        - ``LESSThan`` sets the FLEXRAY data qualifier to less than.
        - ``MOREThan`` sets the FLEXRAY data qualifier to greater than.
        - ``EQUal`` sets the FLEXRAY data qualifier to equal.
        - ``UNEQual`` sets the FLEXRAY data qualifier to not equal.
        - ``LESSEQual`` sets the FLEXRAY data qualifier to less than or equal.
        - ``MOREEQual`` sets the FLEXRAY data qualifier to greater than or equal.
        - ``INrange`` sets the FLEXRAY data qualifier to in range.
        - ``OUTrange`` sets the FLEXRAY data qualifier to out of range.
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemFlexrayDataOffset(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet`` command.

    Description:
        - This command specifies the offset of the data string in bytes to be used when searching on
          the FlexRay bus data field. The search condition needs to be set to ID or IDANDDATA (using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search number,
          which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet <NR1>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet?
        ```

    Info:
        - ``<NR1>`` is the data offset in bytes. A byte offset of -1 signifies don't care, and no
          byte offset is used. The instrument will search or match any byte value that fits.
    """


class SearchSearchItemTriggerABusBItemFlexrayDataHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue`` command.

    Description:
        - This command specifies the high value to use when searching on the FlexRay bus data field.
          The search condition needs to be set to ID or IDANDDATA (using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search number,
          which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue?
        ```

    Info:
        - ``<QString>`` is a quoted string that is the data field high binary value.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemFlexrayData(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue`` command.
        - ``.offset``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet`` command.
        - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier``
          command.
        - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe`` command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = SearchSearchItemTriggerABusBItemFlexrayDataHivalue(
            device, f"{self._cmd_syntax}:HIVALue"
        )
        self._offset = SearchSearchItemTriggerABusBItemFlexrayDataOffset(
            device, f"{self._cmd_syntax}:OFFSet"
        )
        self._qualifier = SearchSearchItemTriggerABusBItemFlexrayDataQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._size = SearchSearchItemTriggerABusBItemFlexrayDataSize(
            device, f"{self._cmd_syntax}:SIZe"
        )
        self._value = SearchSearchItemTriggerABusBItemFlexrayDataValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def hivalue(self) -> SearchSearchItemTriggerABusBItemFlexrayDataHivalue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue`` command.

        Description:
            - This command specifies the high value to use when searching on the FlexRay bus data
              field. The search condition needs to be set to ID or IDANDDATA (using
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search
              number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue?
            ```

        Info:
            - ``<QString>`` is a quoted string that is the data field high binary value.
        """
        return self._hivalue

    @property
    def offset(self) -> SearchSearchItemTriggerABusBItemFlexrayDataOffset:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet`` command.

        Description:
            - This command specifies the offset of the data string in bytes to be used when
              searching on the FlexRay bus data field. The search condition needs to be set to ID or
              IDANDDATA (using ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is
              the search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet <NR1>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet?
            ```

        Info:
            - ``<NR1>`` is the data offset in bytes. A byte offset of -1 signifies don't care, and
              no byte offset is used. The instrument will search or match any byte value that fits.
        """
        return self._offset

    @property
    def qualifier(self) -> SearchSearchItemTriggerABusBItemFlexrayDataQualifier:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier`` command.

        Description:
            - Sets or returns the FLEXRAY data qualifier.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier?
            ```

        Info:
            - ``LESSThan`` sets the FLEXRAY data qualifier to less than.
            - ``MOREThan`` sets the FLEXRAY data qualifier to greater than.
            - ``EQUal`` sets the FLEXRAY data qualifier to equal.
            - ``UNEQual`` sets the FLEXRAY data qualifier to not equal.
            - ``LESSEQual`` sets the FLEXRAY data qualifier to less than or equal.
            - ``MOREEQual`` sets the FLEXRAY data qualifier to greater than or equal.
            - ``INrange`` sets the FLEXRAY data qualifier to in range.
            - ``OUTrange`` sets the FLEXRAY data qualifier to out of range.
        """  # noqa: E501
        return self._qualifier

    @property
    def size(self) -> SearchSearchItemTriggerABusBItemFlexrayDataSize:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe`` command.

        Description:
            - This command specifies the length of the data string, in bytes, to use when searching
              on the FlexRay bus data field. The search condition needs to be set to ID or IDANDDATA
              (using ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search
              number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe <NR1>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe?
            ```

        Info:
            - ``<NR1>`` is the length of the data string in bytes. Length range is 1 to 8.
        """
        return self._size

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemFlexrayDataValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue`` command.

        Description:
            - This command specifies the low value to use when searching on the FlexRay bus data
              field. The search condition needs to be set to ID or IDANDDATA (using
              ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search number, which is
              always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue?
            ```

        Info:
            - ``<QString>`` is a quoted string that is the low binary data string to be used for a
              FlexRay search if the search condition is set to IDANDDATA.
        """
        return self._value


class SearchSearchItemTriggerABusBItemFlexrayCyclecountValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue`` command.

    Description:
        - This command specifies the low data value to be used when searching on the FlexRay bus
          cycle count field. The search condition must be set to CYCLEcount (using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search number,
          which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue?
        ```

    Info:
        - ``<QString>`` is a quoted string that is the cycle count binary value.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemFlexrayCyclecountQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier`` command.

    Description:
        - Sets or returns the FLEXRAY cycle count qualifier.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier?
        ```
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemFlexrayCyclecountHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue`` command.

    Description:
        - This command specifies the upper data value of the range to be used when searching on the
          FlexRay bus cycle count field. (Use
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CYCLECOUNT:VALUE`` to set the low value.) The
          search condition must be set to CYCLEcount (using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search number,
          which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue?
        ```

    Info:
        - ``<QString>`` is a quoted string that is the cycle count high value.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemFlexrayCyclecount(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue``
          command.
        - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier``
          command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = SearchSearchItemTriggerABusBItemFlexrayCyclecountHivalue(
            device, f"{self._cmd_syntax}:HIVALue"
        )
        self._qualifier = SearchSearchItemTriggerABusBItemFlexrayCyclecountQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._value = SearchSearchItemTriggerABusBItemFlexrayCyclecountValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def hivalue(self) -> SearchSearchItemTriggerABusBItemFlexrayCyclecountHivalue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue`` command.

        Description:
            - This command specifies the upper data value of the range to be used when searching on
              the FlexRay bus cycle count field. (Use
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CYCLECOUNT:VALUE`` to set the low value.)
              The search condition must be set to CYCLEcount (using
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search
              number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue?
            ```

        Info:
            - ``<QString>`` is a quoted string that is the cycle count high value.
        """
        return self._hivalue

    @property
    def qualifier(self) -> SearchSearchItemTriggerABusBItemFlexrayCyclecountQualifier:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier`` command.

        Description:
            - Sets or returns the FLEXRAY cycle count qualifier.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier?
            ```
        """  # noqa: E501
        return self._qualifier

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemFlexrayCyclecountValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue`` command.

        Description:
            - This command specifies the low data value to be used when searching on the FlexRay bus
              cycle count field. The search condition must be set to CYCLEcount (using
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search
              number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue?
            ```

        Info:
            - ``<QString>`` is a quoted string that is the cycle count binary value.
        """
        return self._value


class SearchSearchItemTriggerABusBItemFlexrayCondition(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CONDition`` command.

    Description:
        - This command specifies the condition to use when searching on FlexRay bus data (start of
          frame, frame type, ID, cycle count, header, data, ID and data, EOF, error). SEARCH<x> is
          the search number, which is always 1, and B<x> is the bus number B1-B2.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CONDition?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CONDition value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CONDition {SOF|FRAMETypeid|CYCLEcount|HEADer|DATA|IDANDDATA|EOF|ERROR}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CONDition?
        ```

    Info:
        - ``SOF`` sets the search condition to start of frame.
        - ``FRAMETypeid`` sets the search condition to a frame type id.
        - ``CYCLEcount`` sets the search condition to cycle count.
        - ``HEADer`` sets the search condition to header.
        - ``DATA`` sets the search condition to data.
        - ``IDANDDATA`` sets the search condition to ID and data.
        - ``EOF`` sets the search condition to EOF.
        - ``ERROR`` sets the search condition to an error.
    """  # noqa: E501


#  pylint: disable=too-many-instance-attributes
class SearchSearchItemTriggerABusBItemFlexray(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CONDition`` command.
        - ``.cyclecount``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount`` command
          tree.
        - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa`` command tree.
        - ``.eoftype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE`` command.
        - ``.errtype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE`` command.
        - ``.frameid``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID`` command tree.
        - ``.frametype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEType`` command.
        - ``.header``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = SearchSearchItemTriggerABusBItemFlexrayCondition(
            device, f"{self._cmd_syntax}:CONDition"
        )
        self._cyclecount = SearchSearchItemTriggerABusBItemFlexrayCyclecount(
            device, f"{self._cmd_syntax}:CYCLEcount"
        )
        self._data = SearchSearchItemTriggerABusBItemFlexrayData(device, f"{self._cmd_syntax}:DATa")
        self._eoftype = SearchSearchItemTriggerABusBItemFlexrayEoftype(
            device, f"{self._cmd_syntax}:EOFTYPE"
        )
        self._errtype = SearchSearchItemTriggerABusBItemFlexrayErrtype(
            device, f"{self._cmd_syntax}:ERRTYPE"
        )
        self._frameid = SearchSearchItemTriggerABusBItemFlexrayFrameid(
            device, f"{self._cmd_syntax}:FRAMEID"
        )
        self._frametype = SearchSearchItemTriggerABusBItemFlexrayFrametype(
            device, f"{self._cmd_syntax}:FRAMEType"
        )
        self._header = SearchSearchItemTriggerABusBItemFlexrayHeader(
            device, f"{self._cmd_syntax}:HEADER"
        )

    @property
    def condition(self) -> SearchSearchItemTriggerABusBItemFlexrayCondition:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CONDition`` command.

        Description:
            - This command specifies the condition to use when searching on FlexRay bus data (start
              of frame, frame type, ID, cycle count, header, data, ID and data, EOF, error).
              SEARCH<x> is the search number, which is always 1, and B<x> is the bus number B1-B2.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CONDition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CONDition?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CONDition value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CONDition {SOF|FRAMETypeid|CYCLEcount|HEADer|DATA|IDANDDATA|EOF|ERROR}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CONDition?
            ```

        Info:
            - ``SOF`` sets the search condition to start of frame.
            - ``FRAMETypeid`` sets the search condition to a frame type id.
            - ``CYCLEcount`` sets the search condition to cycle count.
            - ``HEADer`` sets the search condition to header.
            - ``DATA`` sets the search condition to data.
            - ``IDANDDATA`` sets the search condition to ID and data.
            - ``EOF`` sets the search condition to EOF.
            - ``ERROR`` sets the search condition to an error.
        """  # noqa: E501
        return self._condition

    @property
    def cyclecount(self) -> SearchSearchItemTriggerABusBItemFlexrayCyclecount:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue``
              command.
            - ``.qualifier``: The
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier`` command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue``
              command.
        """
        return self._cyclecount

    @property
    def data(self) -> SearchSearchItemTriggerABusBItemFlexrayData:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue``
              command.
            - ``.offset``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet`` command.
            - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier``
              command.
            - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe`` command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue`` command.
        """
        return self._data

    @property
    def eoftype(self) -> SearchSearchItemTriggerABusBItemFlexrayEoftype:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE`` command.

        Description:
            - This command specifies which end of file type to use (static, dynamic or any) when
              searching on the FlexRay bus EOF field. The search condition needs to be set to EOF
              (using ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search
              number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE {STATic|DYNAMic|ANY}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE?
            ```

        Info:
            - ``STATic`` sets the FlexRay end of frame type to STATIC.
            - ``DYNAMic`` sets the FlexRay end of frame type to DYNAMIC.
            - ``ANY`` sets the FlexRay end of frame type to ANY type.
        """
        return self._eoftype

    @property
    def errtype(self) -> SearchSearchItemTriggerABusBItemFlexrayErrtype:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE`` command.

        Description:
            - This command specifies the error type to use when searching on the FlexRay bus signal.
              The search condition needs to be set to ERROR (using
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search
              number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE {CRCHeader|CRCTrailer|SYNCFrame|STARTupnosync|NULLFRStatic|NULLFRDynamic}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE?
            ```

        Info:
            - ``CRCHeader`` sets the error type to CRC header.
            - ``CRCTrailer`` sets the error type to CRC trailer.
            - ``SYNCFrame`` sets the error type to sync frame.
            - ``STARTupnosync`` sets the error type to start up with no sync.
            - ``NULLFRStatic`` sets the error type to null frame static.
            - ``NULLFRDynamic`` sets the error type to null frame dynamic.
        """  # noqa: E501
        return self._errtype

    @property
    def frameid(self) -> SearchSearchItemTriggerABusBItemFlexrayFrameid:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue``
              command.
            - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier``
              command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue`` command.
        """
        return self._frameid

    @property
    def frametype(self) -> SearchSearchItemTriggerABusBItemFlexrayFrametype:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEType`` command.

        Description:
            - This command specifies the frame type (normal, payload, null, sync or startup) to use
              when searching on FlexRay bus data. The search condition needs to be set to FRAMEType
              (using ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search
              number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEType?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEType?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEType value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEType {NORMal|PAYLoad|NULL|SYNC|STARTup}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEType?
            ```

        Info:
            - ``NORMal`` sets the frame type to normal.
            - ``PAYLoad`` sets the frame type to payload.
            - ``NULL`` sets the frame type to NULL.
            - ``SYNC`` sets the frame type to sync.
            - ``STARTup`` sets the frame type to start up.
        """  # noqa: E501
        return self._frametype

    @property
    def header(self) -> SearchSearchItemTriggerABusBItemFlexrayHeader:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.crc``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC`` command.
            - ``.cyclecount``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount``
              command.
            - ``.frameid``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID``
              command.
            - ``.indbits``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits``
              command.
            - ``.paylength``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength``
              command.
        """
        return self._header


class SearchSearchItemTriggerABusBItemCanIdentifierValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue`` command.

    Description:
        - This command sets the binary address value to be used to search on CAN bus data. This only
          applies if the search condition has been set to IDANDDATA or DATA (using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:CONDITION``). SEARCH<x> is the search number, which
          is always 1, and B<x> is the bus number (1-2).

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue <bin>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue?
        ```

    Info:
        - ``<bin>`` is the address in binary format.
    """


class SearchSearchItemTriggerABusBItemCanIdentifierMode(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe`` command.

    Description:
        - Sets or returns the CAN addressing mode for a trigger search to a standard or extended
          format. SEARCH<x> is the search number and B<x> is the bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe {STandard|EXTended}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?
        ```

    Info:
        - ``STandard`` specifies an 11-bit identifier field.
        - ``EXTended`` specifies a 29-bit identifier field.
    """


class SearchSearchItemTriggerABusBItemCanIdentifier(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    Properties:
        - ``.mode``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe`` command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = SearchSearchItemTriggerABusBItemCanIdentifierMode(
            device, f"{self._cmd_syntax}:MODe"
        )
        self._value = SearchSearchItemTriggerABusBItemCanIdentifierValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def mode(self) -> SearchSearchItemTriggerABusBItemCanIdentifierMode:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe`` command.

        Description:
            - Sets or returns the CAN addressing mode for a trigger search to a standard or extended
              format. SEARCH<x> is the search number and B<x> is the bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe {STandard|EXTended}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?
            ```

        Info:
            - ``STandard`` specifies an 11-bit identifier field.
            - ``EXTended`` specifies a 29-bit identifier field.
        """
        return self._mode

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemCanIdentifierValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue`` command.

        Description:
            - This command sets the binary address value to be used to search on CAN bus data. This
              only applies if the search condition has been set to IDANDDATA or DATA (using
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:CONDITION``). SEARCH<x> is the search number,
              which is always 1, and B<x> is the bus number (1-2).

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue <bin>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue?
            ```

        Info:
            - ``<bin>`` is the address in binary format.
        """
        return self._value


class SearchSearchItemTriggerABusBItemCanFrametype(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FRAMEtype`` command.

    Description:
        - This command sets the frame type (data, remote, error or overload) to be used to search on
          CAN bus data. This only applies if the search condition has been set to FRAMEtype (using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:CONDITION``). SEARCH<x> is the search number, which
          is always 1, and B<x> is the bus number (1-2).

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FRAMEtype?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FRAMEtype?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FRAMEtype value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FRAMEtype {DATA|REMote|ERRor|OVERLoad}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FRAMEtype?
        ```

    Info:
        - ``DATA`` specifies a data frame.
        - ``REMote`` specifies a remote frame.
        - ``ERRor`` specifies an error frame.
        - ``OVERLoad`` specifies an overload frame.
    """


class SearchSearchItemTriggerABusBItemCanDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:VALue`` command.

    Description:
        - This command sets the binary data value to be used to search on CAN bus data. This only
          applies if the search condition has been set to IDANDDATA or DATA (using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:CONDITION``). SEARCH<x> is the search number, which
          is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:VALue?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:VALue <bin>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:VALue?
        ```

    Info:
        - ``<bin>`` is the data in binary format.
    """


class SearchSearchItemTriggerABusBItemCanDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:SIZe`` command.

    Description:
        - This command sets the length of the data string, in bytes, to be used to search on CAN bus
          data. This only applies if the search condition has been set to IDANDDATA or DATA (using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:CONDITION``). SEARCH<x> is the search number, which
          is always 1, and B<x> is the bus number (1-2).

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:SIZe?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:SIZe <NR1>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:SIZe?
        ```

    Info:
        - ``<NR1>`` is the data string length in bytes.
    """


class SearchSearchItemTriggerABusBItemCanDataQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier`` command.

    Description:
        - Sets or returns the CAN data qualifier for a search. SEARCH<x> is the search number and
          B<x> is the bus number. This only applies if the trigger condition is IDANDDATA or DATA.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier {LESSThan|MOREThan|UNEQual|LESSEQual|MOREEQual|EQual}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?
        ```

    Info:
        - ``LESSThan`` searches for bus data less than the value specified by
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:DATA:VALUE``.
        - ``MOREThan`` searches for bus data more than the value specified by
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:DATA:VALUE``.
        - ``UNEQual`` searches for bus data not equal to the value specified by
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:DATA:VALUE``.
        - ``LESSEQual`` searches for bus data less than or equal to the value specified by
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:DATA:VALUE``.
        - ``MOREEQual`` searches for bus data more than or equal to the value specified by
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:DATA:VALUE``.
        - ``EQual`` searches for bus data equal to the value specified by
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:DATA:VALUE``.
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemCanDataDirection(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:DIRection`` command.

    Description:
        - This command sets the data direction (read, write or nocare) to be used to search on CAN
          bus data. This only applies if the search condition has been set to IDentifier (using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:CONDITION``). SEARCH<x> is the search number, which
          is always 1, and B<x> is the bus number (1-2).

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:DIRection?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:DIRection?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:DIRection value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:DIRection {READ|WRITE|NOCARE}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:DIRection?
        ```

    Info:
        - ``READ`` specifies the read direction.
        - ``WRITE`` specifies the write direction.
        - ``NOCARE`` specifies either a read or write direction.
    """


class SearchSearchItemTriggerABusBItemCanData(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.direction``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:DIRection`` command.
        - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier`` command.
        - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:SIZe`` command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._direction = SearchSearchItemTriggerABusBItemCanDataDirection(
            device, f"{self._cmd_syntax}:DIRection"
        )
        self._qualifier = SearchSearchItemTriggerABusBItemCanDataQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._size = SearchSearchItemTriggerABusBItemCanDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._value = SearchSearchItemTriggerABusBItemCanDataValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def direction(self) -> SearchSearchItemTriggerABusBItemCanDataDirection:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:DIRection`` command.

        Description:
            - This command sets the data direction (read, write or nocare) to be used to search on
              CAN bus data. This only applies if the search condition has been set to IDentifier
              (using ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:CONDITION``). SEARCH<x> is the search
              number, which is always 1, and B<x> is the bus number (1-2).

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:DIRection?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:DIRection?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:DIRection value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:DIRection {READ|WRITE|NOCARE}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:DIRection?
            ```

        Info:
            - ``READ`` specifies the read direction.
            - ``WRITE`` specifies the write direction.
            - ``NOCARE`` specifies either a read or write direction.
        """
        return self._direction

    @property
    def qualifier(self) -> SearchSearchItemTriggerABusBItemCanDataQualifier:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier`` command.

        Description:
            - Sets or returns the CAN data qualifier for a search. SEARCH<x> is the search number
              and B<x> is the bus number. This only applies if the trigger condition is IDANDDATA or
              DATA.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier {LESSThan|MOREThan|UNEQual|LESSEQual|MOREEQual|EQual}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?
            ```

        Info:
            - ``LESSThan`` searches for bus data less than the value specified by
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:DATA:VALUE``.
            - ``MOREThan`` searches for bus data more than the value specified by
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:DATA:VALUE``.
            - ``UNEQual`` searches for bus data not equal to the value specified by
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:DATA:VALUE``.
            - ``LESSEQual`` searches for bus data less than or equal to the value specified by
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:DATA:VALUE``.
            - ``MOREEQual`` searches for bus data more than or equal to the value specified by
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:DATA:VALUE``.
            - ``EQual`` searches for bus data equal to the value specified by
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:DATA:VALUE``.
        """  # noqa: E501
        return self._qualifier

    @property
    def size(self) -> SearchSearchItemTriggerABusBItemCanDataSize:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:SIZe`` command.

        Description:
            - This command sets the length of the data string, in bytes, to be used to search on CAN
              bus data. This only applies if the search condition has been set to IDANDDATA or DATA
              (using ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:CONDITION``). SEARCH<x> is the search
              number, which is always 1, and B<x> is the bus number (1-2).

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:SIZe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:SIZe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:SIZe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:SIZe <NR1>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:SIZe?
            ```

        Info:
            - ``<NR1>`` is the data string length in bytes.
        """
        return self._size

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemCanDataValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:VALue`` command.

        Description:
            - This command sets the binary data value to be used to search on CAN bus data. This
              only applies if the search condition has been set to IDANDDATA or DATA (using
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:CONDITION``). SEARCH<x> is the search number,
              which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:VALue <bin>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:VALue?
            ```

        Info:
            - ``<bin>`` is the data in binary format.
        """
        return self._value


class SearchSearchItemTriggerABusBItemCanCondition(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:CONDition`` command.

    Description:
        - Sets or returns the search condition for a CAN trigger search. SEARCH<x> is the search
          number and B<x> is the bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:CONDition?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:CONDition value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:CONDition {SOF|FRAMEtype|IDentifier|DATA|IDANDDATA|EOF|ACKMISS|ERROR}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:CONDition?
        ```

    Info:
        - ``SOF`` specifies a search based on the start of frame.
        - ``FRAMEtype`` specifies a search based on the frame type.
        - ``IDentifier`` specifies a search based on the frame identifier.
        - ``DATA`` specifies a search based on the frame data.
        - ``IDANDDATA`` specifies a search based on the frame identifier and data.
        - ``EOF`` specifies a search base on the end of frame.
        - ``ACKMISS`` specifies a search based on the missing ACK field.
        - ``ERROR`` specifies a search based on a bit stuffing error.
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemCanAddressValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue`` command.

    Description:
        - This command sets the binary address value to be used to search on CAN bus data. This only
          applies if the search condition has been set to IDANDDATA or DATA (using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:CONDITION``). SEARCH<x> is the search number, which
          is always 1, and B<x> is the bus number (1-2).

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue <bin>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue?
        ```

    Info:
        - ``<bin>`` is the address in binary format.
    """


class SearchSearchItemTriggerABusBItemCanAddressMode(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe`` command.

    Description:
        - Sets or returns the CAN addressing mode for a trigger search to a standard or extended
          format. SEARCH<x> is the search number and B<x> is the bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe {STandard|EXTended}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe?
        ```

    Info:
        - ``STandard`` specifies an 11-bit identifier field.
        - ``EXTended`` specifies a 29-bit identifier field.
    """


class SearchSearchItemTriggerABusBItemCanAddress(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.mode``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe`` command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = SearchSearchItemTriggerABusBItemCanAddressMode(
            device, f"{self._cmd_syntax}:MODe"
        )
        self._value = SearchSearchItemTriggerABusBItemCanAddressValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def mode(self) -> SearchSearchItemTriggerABusBItemCanAddressMode:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe`` command.

        Description:
            - Sets or returns the CAN addressing mode for a trigger search to a standard or extended
              format. SEARCH<x> is the search number and B<x> is the bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe {STandard|EXTended}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe?
            ```

        Info:
            - ``STandard`` specifies an 11-bit identifier field.
            - ``EXTended`` specifies a 29-bit identifier field.
        """
        return self._mode

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemCanAddressValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue`` command.

        Description:
            - This command sets the binary address value to be used to search on CAN bus data. This
              only applies if the search condition has been set to IDANDDATA or DATA (using
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:CONDITION``). SEARCH<x> is the search number,
              which is always 1, and B<x> is the bus number (1-2).

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue <bin>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue?
            ```

        Info:
            - ``<bin>`` is the address in binary format.
        """
        return self._value


class SearchSearchItemTriggerABusBItemCan(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:CONDition`` command.
        - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa`` command tree.
        - ``.frametype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FRAMEtype`` command.
        - ``.identifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier`` command tree.
        - ``.address``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = SearchSearchItemTriggerABusBItemCanCondition(
            device, f"{self._cmd_syntax}:CONDition"
        )
        self._data = SearchSearchItemTriggerABusBItemCanData(device, f"{self._cmd_syntax}:DATa")
        self._frametype = SearchSearchItemTriggerABusBItemCanFrametype(
            device, f"{self._cmd_syntax}:FRAMEtype"
        )
        self._identifier = SearchSearchItemTriggerABusBItemCanIdentifier(
            device, f"{self._cmd_syntax}:IDentifier"
        )
        self._address = SearchSearchItemTriggerABusBItemCanAddress(
            device, f"{self._cmd_syntax}:ADDRess"
        )

    @property
    def condition(self) -> SearchSearchItemTriggerABusBItemCanCondition:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:CONDition`` command.

        Description:
            - Sets or returns the search condition for a CAN trigger search. SEARCH<x> is the search
              number and B<x> is the bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:CONDition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:CONDition?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:CONDition value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:CONDition {SOF|FRAMEtype|IDentifier|DATA|IDANDDATA|EOF|ACKMISS|ERROR}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:CONDition?
            ```

        Info:
            - ``SOF`` specifies a search based on the start of frame.
            - ``FRAMEtype`` specifies a search based on the frame type.
            - ``IDentifier`` specifies a search based on the frame identifier.
            - ``DATA`` specifies a search based on the frame data.
            - ``IDANDDATA`` specifies a search based on the frame identifier and data.
            - ``EOF`` specifies a search base on the end of frame.
            - ``ACKMISS`` specifies a search based on the missing ACK field.
            - ``ERROR`` specifies a search based on a bit stuffing error.
        """  # noqa: E501
        return self._condition

    @property
    def data(self) -> SearchSearchItemTriggerABusBItemCanData:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.direction``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:DIRection``
              command.
            - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier``
              command.
            - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:SIZe`` command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:VALue`` command.
        """
        return self._data

    @property
    def frametype(self) -> SearchSearchItemTriggerABusBItemCanFrametype:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FRAMEtype`` command.

        Description:
            - This command sets the frame type (data, remote, error or overload) to be used to
              search on CAN bus data. This only applies if the search condition has been set to
              FRAMEtype (using ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:CONDITION``). SEARCH<x> is the
              search number, which is always 1, and B<x> is the bus number (1-2).

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FRAMEtype?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FRAMEtype?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FRAMEtype value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FRAMEtype {DATA|REMote|ERRor|OVERLoad}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FRAMEtype?
            ```

        Info:
            - ``DATA`` specifies a data frame.
            - ``REMote`` specifies a remote frame.
            - ``ERRor`` specifies an error frame.
            - ``OVERLoad`` specifies an overload frame.
        """
        return self._frametype

    @property
    def identifier(self) -> SearchSearchItemTriggerABusBItemCanIdentifier:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.mode``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe`` command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue`` command.
        """
        return self._identifier

    @property
    def address(self) -> SearchSearchItemTriggerABusBItemCanAddress:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        Sub-properties:
            - ``.mode``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe`` command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue`` command.
        """
        return self._address


class SearchSearchItemTriggerABusBItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>?``
          query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.can``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN`` command tree.
        - ``.flexray``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray`` command tree.
        - ``.i2c``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C`` command tree.
        - ``.lin``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN`` command tree.
        - ``.parallel``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel`` command tree.
        - ``.rs232c``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C`` command tree.
        - ``.spi``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._can = SearchSearchItemTriggerABusBItemCan(device, f"{self._cmd_syntax}:CAN")
        self._flexray = SearchSearchItemTriggerABusBItemFlexray(
            device, f"{self._cmd_syntax}:FLEXray"
        )
        self._i2c = SearchSearchItemTriggerABusBItemI2c(device, f"{self._cmd_syntax}:I2C")
        self._lin = SearchSearchItemTriggerABusBItemLin(device, f"{self._cmd_syntax}:LIN")
        self._parallel = SearchSearchItemTriggerABusBItemParallel(
            device, f"{self._cmd_syntax}:PARallel"
        )
        self._rs232c = SearchSearchItemTriggerABusBItemRs232c(device, f"{self._cmd_syntax}:RS232C")
        self._spi = SearchSearchItemTriggerABusBItemSpi(device, f"{self._cmd_syntax}:SPI")

    @property
    def can(self) -> SearchSearchItemTriggerABusBItemCan:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:CONDition`` command.
            - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa`` command tree.
            - ``.frametype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FRAMEtype`` command.
            - ``.identifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier`` command
              tree.
            - ``.address``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess`` command tree.
        """
        return self._can

    @property
    def flexray(self) -> SearchSearchItemTriggerABusBItemFlexray:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CONDition`` command.
            - ``.cyclecount``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount``
              command tree.
            - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa`` command tree.
            - ``.eoftype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE`` command.
            - ``.errtype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE`` command.
            - ``.frameid``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID`` command
              tree.
            - ``.frametype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEType`` command.
            - ``.header``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:HEADER`` command tree.
        """
        return self._flexray

    @property
    def i2c(self) -> SearchSearchItemTriggerABusBItemI2c:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.address``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:ADDRess`` command tree.
            - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:CONDition`` command.
            - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C:DATa`` command tree.
        """
        return self._i2c

    @property
    def lin(self) -> SearchSearchItemTriggerABusBItemLin:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:CONDition`` command.
            - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa`` command tree.
            - ``.errtype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:ERRTYPE`` command.
            - ``.identifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:IDentifier`` command
              tree.
        """
        return self._lin

    @property
    def parallel(self) -> SearchSearchItemTriggerABusBItemParallel:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel:VALue`` command.
        """
        return self._parallel

    @property
    def rs232c(self) -> SearchSearchItemTriggerABusBItemRs232c:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:CONDition`` command.
            - ``.rx``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX`` command tree.
            - ``.tx``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX`` command tree.
        """
        return self._rs232c

    @property
    def spi(self) -> SearchSearchItemTriggerABusBItemSpi:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:CONDition`` command.
            - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:DATa`` command tree.
        """
        return self._spi


class SearchSearchItemTriggerABus(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS`` command.

    Description:
        - Queries the ``SEARCH:SEARCH<x>:TRIGger:A:BUS`` settings. <x> is the search number, which
          is always 1. There are two buses, B1-B2. To set the search type to bus, use
          ``SEARCH:SEARCHX:TRIGGER:A:TYPE BUS``.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS?
        ```

    Properties:
        - ``.b``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>`` command tree.
        - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._b: Dict[int, SearchSearchItemTriggerABusBItem] = DefaultDictPassKeyToFactory(
            lambda x: SearchSearchItemTriggerABusBItem(device, f"{self._cmd_syntax}:B{x}")
        )
        self._source = SearchSearchItemTriggerABusSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def b(self) -> Dict[int, SearchSearchItemTriggerABusBItem]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.can``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN`` command tree.
            - ``.flexray``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray`` command tree.
            - ``.i2c``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C`` command tree.
            - ``.lin``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN`` command tree.
            - ``.parallel``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel`` command tree.
            - ``.rs232c``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C`` command tree.
            - ``.spi``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI`` command tree.
        """
        return self._b

    @property
    def source(self) -> SearchSearchItemTriggerABusSource:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce`` command.

        Description:
            - This command specifies the source of a bus search. <x> is the search number. SEARCH<x>
              is the search number, which is always 1.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce {B<x>}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce?
            ```

        Info:
            - ``B1`` specifies the Bus 1 source.
            - ``B2`` specifies the Bus 2 source.
            - ``B3`` specifies the Bus 3 source.
            - ``B4`` specifies the Bus 4 source.
        """
        return self._source


#  pylint: disable=too-many-instance-attributes
class SearchSearchItemTriggerA(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bus``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS`` command.
        - ``.edge``: The ``SEARCH:SEARCH<x>:TRIGger:A:EDGE`` command tree.
        - ``.level``: The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel`` command.
        - ``.logic``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc`` command tree.
        - ``.lowerthreshold``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold`` command tree.
        - ``.pulsewidth``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth`` command tree.
        - ``.runt``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT`` command tree.
        - ``.sethold``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold`` command tree.
        - ``.type``: The ``SEARCH:SEARCH<x>:TRIGger:A:TYPe`` command.
        - ``.upperthreshold``: The ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold`` command tree.
        - ``.transition``: The ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition`` command tree.
        - ``.risefall``: The ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bus = SearchSearchItemTriggerABus(device, f"{self._cmd_syntax}:BUS")
        self._edge = SearchSearchItemTriggerAEdge(device, f"{self._cmd_syntax}:EDGE")
        self._level = SearchSearchItemTriggerALevel(device, f"{self._cmd_syntax}:LEVel")
        self._logic = SearchSearchItemTriggerALogic(device, f"{self._cmd_syntax}:LOGIc")
        self._lowerthreshold = SearchSearchItemTriggerALowerthreshold(
            device, f"{self._cmd_syntax}:LOWerthreshold"
        )
        self._pulsewidth = SearchSearchItemTriggerAPulsewidth(
            device, f"{self._cmd_syntax}:PULSEWidth"
        )
        self._runt = SearchSearchItemTriggerARunt(device, f"{self._cmd_syntax}:RUNT")
        self._sethold = SearchSearchItemTriggerASethold(device, f"{self._cmd_syntax}:SETHold")
        self._type = SearchSearchItemTriggerAType(device, f"{self._cmd_syntax}:TYPe")
        self._upperthreshold = SearchSearchItemTriggerAUpperthreshold(
            device, f"{self._cmd_syntax}:UPPerthreshold"
        )
        self._transition = SearchSearchItemTriggerATransition(
            device, f"{self._cmd_syntax}:TRANsition"
        )
        self._risefall = SearchSearchItemTriggerARisefall(device, f"{self._cmd_syntax}:RISEFall")

    @property
    def bus(self) -> SearchSearchItemTriggerABus:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS`` command.

        Description:
            - Queries the ``SEARCH:SEARCH<x>:TRIGger:A:BUS`` settings. <x> is the search number,
              which is always 1. There are two buses, B1-B2. To set the search type to bus, use
              ``SEARCH:SEARCHX:TRIGGER:A:TYPE BUS``.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS?`` query.
            - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS?
            ```

        Sub-properties:
            - ``.b``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>`` command tree.
            - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce`` command.
        """
        return self._bus

    @property
    def edge(self) -> SearchSearchItemTriggerAEdge:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:EDGE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:EDGE?``
              query.
            - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:EDGE?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.slope``: The ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe`` command.
            - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce`` command.
        """
        return self._edge

    @property
    def level(self) -> SearchSearchItemTriggerALevel:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LEVel`` command.

        Description:
            - Sets or returns the level for an edge trigger search to determine where to place a
              mark. <x> is the search number.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:LEVel?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LEVel?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LEVel value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LEVel {<NR3>|TTL|ECL}
            - SEARCH:SEARCH<x>:TRIGger:A:LEVel?
            ```

        Info:
            - ``<NR3>`` specifies the trigger level, in volts.
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
            - ``ECL`` specifies a preset ECL high level of -1.3 V.

        Sub-properties:
            - ``.ch``: The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:CH<x>`` command.
            - ``.math``: The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:MATH`` command.
            - ``.ref``: The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:REF<x>`` command.
        """
        return self._level

    @property
    def logic(self) -> SearchSearchItemTriggerALogic:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.function``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion`` command.
            - ``.input``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut`` command tree.
            - ``.pattern``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern`` command tree.
            - ``.threshold``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold`` command tree.
        """
        return self._logic

    @property
    def lowerthreshold(self) -> SearchSearchItemTriggerALowerthreshold:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:CH<x>`` command.
            - ``.math``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:MATH`` command.
            - ``.ref``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:REF<x>`` command.
        """
        return self._lowerthreshold

    @property
    def pulsewidth(self) -> SearchSearchItemTriggerAPulsewidth:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity`` command.
            - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce`` command.
            - ``.when``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn`` command.
            - ``.width``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WIDth`` command.
        """
        return self._pulsewidth

    @property
    def runt(self) -> SearchSearchItemTriggerARunt:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT?``
              query.
            - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity`` command.
            - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce`` command.
            - ``.when``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn`` command.
            - ``.width``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth`` command.
        """
        return self._runt

    @property
    def sethold(self) -> SearchSearchItemTriggerASethold:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.clock``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk`` command tree.
            - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa`` command tree.
            - ``.holdtime``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:HOLDTime`` command.
            - ``.settime``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:SETTime`` command.
            - ``.threshold``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold`` command tree.
        """
        return self._sethold

    @property
    def type(self) -> SearchSearchItemTriggerAType:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:TYPe`` command.

        Description:
            - Sets or returns the trigger type setting for a search to determine where to place a
              mark. <x> is the search number.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:TYPe?``
              query.
            - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:TYPe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TYPe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:TYPe {EDGe|SETHold|PULSEWidth|RUNt|TRAnsition|LOGIc|BUS (with the appropriate application module installed)}
            - SEARCH:SEARCH<x>:TRIGger:A:TYPe?
            ```

        Info:
            - ``RUNt`` triggers when a pulse crosses the first preset voltage threshold but does not
              cross the second preset threshold before recrossing the first. The thresholds are set
              with the ``SEARCH:SEARCHX:TRIGGER:A:LOWERTHRESHOLD:CHX`` and
              ``SEARCH:SEARCHX:TRIGGER:A:UPPERTHRESHOLD:CHX`` commands.
            - ``PULSEWIdth`` triggers when a pulse is found that has the specified polarity and is
              either inside or outside the limits as specified by
              ``SEARCH:SEARCHX:TRIGGER:A:LOGIC:PATTERN:WHEN:LESSLIMIT`` and
              ``SEARCH:SEARCHX:TRIGGER:A:LOGIC:PATTERN:WHEN:MORELIMIT``. The polarity is selected
              using the ``SEARCH:SEARCHX:TRIGGER:A:RUNT:POLARITY`` command.
            - ``TRAnsition`` triggers when a pulse crosses both thresholds in the same direction as
              the specified polarity and the transition time between the two threshold crossings is
              greater or less than the specified time delta.
        """  # noqa: E501
        return self._type

    @property
    def upperthreshold(self) -> SearchSearchItemTriggerAUpperthreshold:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:CH<x>`` command.
            - ``.math``: The ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:MATH`` command.
            - ``.ref``: The ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:REF<x>`` command.
        """
        return self._upperthreshold

    @property
    def transition(self) -> SearchSearchItemTriggerATransition:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.deltatime``: The ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:DELTatime`` command.
            - ``.polarity``: The ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:POLarity`` command.
            - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:SOUrce`` command.
            - ``.when``: The ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition:WHEn`` command.
        """
        return self._transition

    @property
    def risefall(self) -> SearchSearchItemTriggerARisefall:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.deltatime``: The ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:DELTatime`` command.
            - ``.polarity``: The ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:POLarity`` command.
            - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:SOUrce`` command.
            - ``.when``: The ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall:WHEn`` command.
        """
        return self._risefall


class SearchSearchItemTrigger(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.a``: The ``SEARCH:SEARCH<x>:TRIGger:A`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._a = SearchSearchItemTriggerA(device, f"{self._cmd_syntax}:A")

    @property
    def a(self) -> SearchSearchItemTriggerA:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A?`` query.
            - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bus``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS`` command.
            - ``.edge``: The ``SEARCH:SEARCH<x>:TRIGger:A:EDGE`` command tree.
            - ``.level``: The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel`` command.
            - ``.logic``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc`` command tree.
            - ``.lowerthreshold``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold`` command tree.
            - ``.pulsewidth``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth`` command tree.
            - ``.runt``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT`` command tree.
            - ``.sethold``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold`` command tree.
            - ``.type``: The ``SEARCH:SEARCH<x>:TRIGger:A:TYPe`` command.
            - ``.upperthreshold``: The ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold`` command tree.
            - ``.transition``: The ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition`` command tree.
            - ``.risefall``: The ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall`` command tree.
        """
        return self._a


class SearchSearchItemTotal(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TOTAL`` command.

    Description:
        - This query-only command returns the total number of found search marks for this search.
          The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TOTAL?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TOTAL?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TOTAL?
        ```
    """


class SearchSearchItemState(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:STATE`` command.

    Description:
        - Sets the search state to on or off. <x> is the search number, which is always 1. The query
          form returns the search state. A series of example command sequences showing different
          searches and triggers is included as an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:STATE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SEARCH:SEARCH<x>:STATE value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:STATE {ON|OFF|<NR1>}
        - SEARCH:SEARCH<x>:STATE?
        ```

    Info:
        - ``OFF`` or <NR1> = 0 sets the search state to off.
        - ``ON`` or <NR1> ≠ 0 sets the search state to on.
    """


class SearchSearchItemCopy(SCPICmdWrite):
    """The ``SEARCH:SEARCH<x>:COPy`` command.

    Description:
        - This command (no query form) copies the search criteria to or from the trigger. The search
          number is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``SEARCH:SEARCH<x>:COPy value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:COPy {SEARCHtotrigger|TRIGgertosearch}
        ```

    Info:
        - ``SEARCHtotrigger`` copies the search criteria to the trigger.
        - ``TRIGgertosearch`` copies the trigger criteria to the search.
    """


class SearchSearchItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.copy``: The ``SEARCH:SEARCH<x>:COPy`` command.
        - ``.state``: The ``SEARCH:SEARCH<x>:STATE`` command.
        - ``.total``: The ``SEARCH:SEARCH<x>:TOTAL`` command.
        - ``.trigger``: The ``SEARCH:SEARCH<x>:TRIGger`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._copy = SearchSearchItemCopy(device, f"{self._cmd_syntax}:COPy")
        self._state = SearchSearchItemState(device, f"{self._cmd_syntax}:STATE")
        self._total = SearchSearchItemTotal(device, f"{self._cmd_syntax}:TOTAL")
        self._trigger = SearchSearchItemTrigger(device, f"{self._cmd_syntax}:TRIGger")

    @property
    def copy(self) -> SearchSearchItemCopy:
        """Return the ``SEARCH:SEARCH<x>:COPy`` command.

        Description:
            - This command (no query form) copies the search criteria to or from the trigger. The
              search number is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``SEARCH:SEARCH<x>:COPy value``
              command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:COPy {SEARCHtotrigger|TRIGgertosearch}
            ```

        Info:
            - ``SEARCHtotrigger`` copies the search criteria to the trigger.
            - ``TRIGgertosearch`` copies the trigger criteria to the search.
        """
        return self._copy

    @property
    def state(self) -> SearchSearchItemState:
        """Return the ``SEARCH:SEARCH<x>:STATE`` command.

        Description:
            - Sets the search state to on or off. <x> is the search number, which is always 1. The
              query form returns the search state. A series of example command sequences showing
              different searches and triggers is included as an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:STATE?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SEARCH:SEARCH<x>:STATE value``
              command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:STATE {ON|OFF|<NR1>}
            - SEARCH:SEARCH<x>:STATE?
            ```

        Info:
            - ``OFF`` or <NR1> = 0 sets the search state to off.
            - ``ON`` or <NR1> ≠ 0 sets the search state to on.
        """
        return self._state

    @property
    def total(self) -> SearchSearchItemTotal:
        """Return the ``SEARCH:SEARCH<x>:TOTAL`` command.

        Description:
            - This query-only command returns the total number of found search marks for this
              search. The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TOTAL?`` query.
            - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TOTAL?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TOTAL?
            ```
        """
        return self._total

    @property
    def trigger(self) -> SearchSearchItemTrigger:
        """Return the ``SEARCH:SEARCH<x>:TRIGger`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger?`` query.
            - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.a``: The ``SEARCH:SEARCH<x>:TRIGger:A`` command tree.
        """
        return self._trigger


class Search(SCPICmdRead):
    """The ``SEARCH`` command.

    Description:
        - Returns all search-related settings.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SEARCH?
        ```

    Properties:
        - ``.search``: The ``SEARCH:SEARCH<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SEARCH") -> None:
        super().__init__(device, cmd_syntax)
        self._search: Dict[int, SearchSearchItem] = DefaultDictPassKeyToFactory(
            lambda x: SearchSearchItem(device, f"{self._cmd_syntax}:SEARCH{x}")
        )

    @property
    def search(self) -> Dict[int, SearchSearchItem]:
        """Return the ``SEARCH:SEARCH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.copy``: The ``SEARCH:SEARCH<x>:COPy`` command.
            - ``.state``: The ``SEARCH:SEARCH<x>:STATE`` command.
            - ``.total``: The ``SEARCH:SEARCH<x>:TOTAL`` command.
            - ``.trigger``: The ``SEARCH:SEARCH<x>:TRIGger`` command tree.
        """
        return self._search
