# pylint: disable=line-too-long
"""The trigger commands module.

These commands are used in the following models:
DPO2K, DPO2KB, MSO2K, MSO2KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - TRIGger FORCe
    - TRIGger:A SETLevel
    - TRIGger:A:BUS {I2C|SPI|CAN|RS232}
    - TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe {STandard|EXTended}
    - TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe?
    - TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue <QString>
    - TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue?
    - TRIGger:A:BUS:B<x>:CAN:CONDition {SOF|FRAMEtype|IDentifier|DATA|IDANDDATA|EOF|ACKMISS}
    - TRIGger:A:BUS:B<x>:CAN:CONDition?
    - TRIGger:A:BUS:B<x>:CAN:DATa:DIRection {READ|WRITE|NOCARE}
    - TRIGger:A:BUS:B<x>:CAN:DATa:DIRection?
    - TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual}
    - TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?
    - TRIGger:A:BUS:B<x>:CAN:DATa:SIZe <NR1>
    - TRIGger:A:BUS:B<x>:CAN:DATa:SIZe?
    - TRIGger:A:BUS:B<x>:CAN:DATa:VALue <QString>
    - TRIGger:A:BUS:B<x>:CAN:DATa:VALue?
    - TRIGger:A:BUS:B<x>:CAN:FRAMEtype {DATA|REMote|ERRor|OVERLoad}
    - TRIGger:A:BUS:B<x>:CAN:FRAMEtype?
    - TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe {STandard|EXTended}
    - TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?
    - TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue <QString>
    - TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue?
    - TRIGger:A:BUS:B<x>:FLEXray:CONDition {SOF|FRAMEType|IDentifier|CYCLEcount|HEADer|DATA|IDANDDATA|EOF|ERROR}
    - TRIGger:A:BUS:B<x>:FLEXray:CONDition?
    - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue <QString>
    - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue?
    - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
    - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier?
    - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue <QString>
    - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue?
    - TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue <QString>
    - TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue?
    - TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet <NR1>
    - TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet?
    - TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
    - TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier?
    - TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe <NR1>
    - TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe?
    - TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue <QString>
    - TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue?
    - TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE {STATic|DYNAMic|ANY}
    - TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE?
    - TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE {CRCHeader|CRCTrailer|SYNCFrame|STARTupnosync|NULLFRStatic|NULLFRDynamic}
    - TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE?
    - TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue <QString>
    - TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue?
    - TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
    - TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier?
    - TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue <QString>
    - TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue?
    - TRIGger:A:BUS:B<x>:FLEXray:FRAMEType {NORMal|PAYLoad|NULL|SYNC|STARTup}
    - TRIGger:A:BUS:B<x>:FLEXray:FRAMEType?
    - TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC <QString>
    - TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC?
    - TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount <QString>
    - TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount?
    - TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID <QString>
    - TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID?
    - TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits <QString>
    - TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits?
    - TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength <QString>
    - TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength?
    - TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe {ADDR7|ADDR10}
    - TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe?
    - TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe {GENeralcall|STARtbyte|HSmode|EEPROM|USER}
    - TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe?
    - TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue <QString>
    - TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue?
    - TRIGger:A:BUS:B<x>:I2C:CONDition {STARt|STOP|REPEATstart|ACKMISS|ADDRess|DATA|ADDRANDDATA}
    - TRIGger:A:BUS:B<x>:I2C:CONDition?
    - TRIGger:A:BUS:B<x>:I2C:DATa:DIRection {READ|WRITE|NOCARE}
    - TRIGger:A:BUS:B<x>:I2C:DATa:DIRection?
    - TRIGger:A:BUS:B<x>:I2C:DATa:SIZe <NR1>
    - TRIGger:A:BUS:B<x>:I2C:DATa:SIZe?
    - TRIGger:A:BUS:B<x>:I2C:DATa:VALue <QString>
    - TRIGger:A:BUS:B<x>:I2C:DATa:VALue?
    - TRIGger:A:BUS:B<x>:LIN:CONDition {SYNCField|IDentifier|DATA|IDANDDATA|WAKEup|SLEEP|ERROR}
    - TRIGger:A:BUS:B<x>:LIN:CONDition?
    - TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue <QString>
    - TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue?
    - TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
    - TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?
    - TRIGger:A:BUS:B<x>:LIN:DATa:SIZe <NR1>
    - TRIGger:A:BUS:B<x>:LIN:DATa:SIZe?
    - TRIGger:A:BUS:B<x>:LIN:DATa:VALue <QString>
    - TRIGger:A:BUS:B<x>:LIN:DATa:VALue?
    - TRIGger:A:BUS:B<x>:LIN:ERRTYPE {SYNC|PARity|CHecksum}
    - TRIGger:A:BUS:B<x>:LIN:ERRTYPE?
    - TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue <QString>
    - TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue?
    - TRIGger:A:BUS:B<x>:PARallel:VALue <QString>
    - TRIGger:A:BUS:B<x>:PARallel:VALue?
    - TRIGger:A:BUS:B<x>:RS232C:CONDition {RXSTArt|RXDATA|RXENDPacket|RXPARity|TXSTArt|TXDATA|TXENDPacket|TXPARity|}
    - TRIGger:A:BUS:B<x>:RS232C:CONDition?
    - TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe <NR1>
    - TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe?
    - TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue
    - TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue?
    - TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe <NR1>
    - TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe?
    - TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue
    - TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue?
    - TRIGger:A:BUS:B<x>:SPI:CONDition {SS|STARTofframe|MISO|MOSI|MISOMOSI}
    - TRIGger:A:BUS:B<x>:SPI:CONDition?
    - TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue <QString>
    - TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue?
    - TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue <QString>
    - TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue?
    - TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue <QString>
    - TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue?
    - TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue <QString>
    - TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue?
    - TRIGger:A:BUS:B<x>:SPI:DATa:SIZe <NR1>
    - TRIGger:A:BUS:B<x>:SPI:DATa:SIZe?
    - TRIGger:A:BUS:SOUrce {B<x>}
    - TRIGger:A:BUS:SOUrce?
    - TRIGger:A:BUS?
    - TRIGger:A:EDGE:COUPling {DC|HFRej|LFRej|NOISErej}
    - TRIGger:A:EDGE:COUPling?
    - TRIGger:A:EDGE:SLOpe {RISe|FALL}
    - TRIGger:A:EDGE:SLOpe?
    - TRIGger:A:EDGE:SOUrce {CH<x>|D<x>|EXT|LINE|AUX}
    - TRIGger:A:EDGE:SOUrce?
    - TRIGger:A:EDGE?
    - TRIGger:A:HOLDoff:TIMe <NR3>
    - TRIGger:A:HOLDoff:TIMe?
    - TRIGger:A:HOLDoff?
    - TRIGger:A:LEVel {ECL|TTL|<NR3>}
    - TRIGger:A:LEVel:AUXin {<NR3>|ECL|TTL}
    - TRIGger:A:LEVel:AUXin?
    - TRIGger:A:LEVel:CH<x> {<NR3>|TTL|ECL}
    - TRIGger:A:LEVel:CH<x>?
    - TRIGger:A:LEVel:D<x> {<NR3>|ECL|TTL}
    - TRIGger:A:LEVel:D<x>?
    - TRIGger:A:LEVel?
    - TRIGger:A:LOGIc:CLAss {LOGIC|SETHold}
    - TRIGger:A:LOGIc:CLAss?
    - TRIGger:A:LOGIc:FUNCtion {AND|NANd}
    - TRIGger:A:LOGIc:FUNCtion?
    - TRIGger:A:LOGIc:INPut:CH<x> {HIGH|LOW|X}
    - TRIGger:A:LOGIc:INPut:CH<x>?
    - TRIGger:A:LOGIc:INPut:CLOCk:EDGE {FALL|RISe|EITher}
    - TRIGger:A:LOGIc:INPut:CLOCk:EDGE?
    - TRIGger:A:LOGIc:INPut:CLOCk:SOUrce {CH<x>|D<x>|NONE}
    - TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?
    - TRIGger:A:LOGIc:INPut:D<x> {HIGH|LOW|X}
    - TRIGger:A:LOGIc:INPut:D<x>?
    - TRIGger:A:LOGIc:INPut?
    - TRIGger:A:LOGIc:PATtern:DELTatime <NR3>
    - TRIGger:A:LOGIc:PATtern:DELTatime?
    - TRIGger:A:LOGIc:PATtern:INPut:D<x> {HIGH|LOW|X}
    - TRIGger:A:LOGIc:PATtern:INPut:D<x>?
    - TRIGger:A:LOGIc:PATtern:WHEn {TRUe|FALSe|LESSThan|MOREThan|EQUal|UNEQual}
    - TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit <NR3>
    - TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit?
    - TRIGger:A:LOGIc:PATtern:WHEn:MORELimit <NR3>
    - TRIGger:A:LOGIc:PATtern:WHEn:MORELimit?
    - TRIGger:A:LOGIc:PATtern:WHEn?
    - TRIGger:A:LOGIc:PATtern?
    - TRIGger:A:LOGIc:THReshold:CH<x> {<NR3>|ECL|TTL}
    - TRIGger:A:LOGIc:THReshold:CH<x>?
    - TRIGger:A:LOGIc:THReshold:D<x> {<NR3>|ECL|TTL}
    - TRIGger:A:LOGIc:THReshold:D<x>?
    - TRIGger:A:LOGIc?
    - TRIGger:A:LOWerthreshold:AUX {<NR3>|ECL|TTL}
    - TRIGger:A:LOWerthreshold:AUX?
    - TRIGger:A:LOWerthreshold:CH<x> {ECL|TTL|<NR3>}
    - TRIGger:A:LOWerthreshold:CH<x>?
    - TRIGger:A:LOWerthreshold:EXT {<NR3>|ECL|TTL}
    - TRIGger:A:LOWerthreshold:EXT?
    - TRIGger:A:MODe {AUTO|NORMal}
    - TRIGger:A:MODe?
    - TRIGger:A:PULSEWidth:POLarity {NEGative|POSitive}
    - TRIGger:A:PULSEWidth:POLarity?
    - TRIGger:A:PULSEWidth:SOUrce {CH<x>|D<x>|LINE|EXT}
    - TRIGger:A:PULSEWidth:SOUrce?
    - TRIGger:A:PULSEWidth:WHEn {LESSthan|MOREthan|EQual|UNEQual}
    - TRIGger:A:PULSEWidth:WHEn?
    - TRIGger:A:PULSEWidth:Width <NR3>
    - TRIGger:A:PULSEWidth:Width?
    - TRIGger:A:PULSEWidth?
    - TRIGger:A:PULse:CLAss {RUNt|WIDth|TRANsition}
    - TRIGger:A:PULse:CLAss?
    - TRIGger:A:PULse?
    - TRIGger:A:RISEFall:DELTatime <NR3>
    - TRIGger:A:RISEFall:DELTatime?
    - TRIGger:A:RISEFall:POLarity {EITher|NEGative|POSitive}
    - TRIGger:A:RISEFall:POLarity?
    - TRIGger:A:RISEFall:SOUrce {CH<x>|D<x>}
    - TRIGger:A:RISEFall:SOUrce?
    - TRIGger:A:RISEFall:WHEn {SLOWer|FASTer|EQual|UNEQual}
    - TRIGger:A:RISEFall:WHEn?
    - TRIGger:A:RISEFall?
    - TRIGger:A:RUNT:POLarity {EITher|NEGative|POSitive}
    - TRIGger:A:RUNT:POLarity?
    - TRIGger:A:RUNT:SOUrce {CH<x>}
    - TRIGger:A:RUNT:SOUrce?
    - TRIGger:A:RUNT:WHEn {LESSthan|MOREthan|EQual|UNEQual|OCCURS}
    - TRIGger:A:RUNT:WHEn?
    - TRIGger:A:RUNT:WIDth <NR3>
    - TRIGger:A:RUNT:WIDth?
    - TRIGger:A:RUNT?
    - TRIGger:A:SETHold:CLOCk:EDGE {FALL|RISe}
    - TRIGger:A:SETHold:CLOCk:EDGE?
    - TRIGger:A:SETHold:CLOCk:SOUrce {CH<x>|D<x>}
    - TRIGger:A:SETHold:CLOCk:SOUrce?
    - TRIGger:A:SETHold:CLOCk:THReshold {<NR3>|TTL|ECL}
    - TRIGger:A:SETHold:CLOCk:THReshold?
    - TRIGger:A:SETHold:CLOCk?
    - TRIGger:A:SETHold:DATa:SOUrce DPO Models:{CH<x>|D<x>}
    - TRIGger:A:SETHold:DATa:SOUrce?
    - TRIGger:A:SETHold:DATa:THReshold {<NR3>|TTL|ECL}
    - TRIGger:A:SETHold:DATa:THReshold?
    - TRIGger:A:SETHold:DATa?
    - TRIGger:A:SETHold:HOLDTime <NR3>
    - TRIGger:A:SETHold:HOLDTime?
    - TRIGger:A:SETHold:SETTime <NR3>
    - TRIGger:A:SETHold:SETTime?
    - TRIGger:A:SETHold:THReshold:CH<x> {<NR3>|ECL|TTL}
    - TRIGger:A:SETHold:THReshold:CH<x>?
    - TRIGger:A:SETHold:THReshold:D<x> {<NR3>|ECL|TTL}
    - TRIGger:A:SETHold:THReshold:D<x>?
    - TRIGger:A:SETHold?
    - TRIGger:A:TRANsition:DELTatime <NR3>
    - TRIGger:A:TRANsition:DELTatime?
    - TRIGger:A:TRANsition:POLarity {EITher|NEGative|POSitive}
    - TRIGger:A:TRANsition:POLarity?
    - TRIGger:A:TRANsition:SOUrce {CH<x>|D<x>}
    - TRIGger:A:TRANsition:SOUrce?
    - TRIGger:A:TRANsition:WHEn {SLOWer|FASTer|EQual|UNEQual}
    - TRIGger:A:TRANsition:WHEn?
    - TRIGger:A:TRANsition?
    - TRIGger:A:TYPe {EDGe|LOGic|PULSe|BUS|VIDeo}
    - TRIGger:A:TYPe?
    - TRIGger:A:UPPerthreshold:CH<x> {<NR3>|ECL|TTL}
    - TRIGger:A:UPPerthreshold:CH<x>?
    - TRIGger:A:VIDeo:CUSTom:FORMat {INTERLAced|PROGressive}
    - TRIGger:A:VIDeo:CUSTom:FORMat?
    - TRIGger:A:VIDeo:CUSTom:LINEPeriod <NR3>
    - TRIGger:A:VIDeo:CUSTom:LINEPeriod?
    - TRIGger:A:VIDeo:CUSTom:SCAN {RATE15K|RATE20K|RATE25K|RATE35K|RATE50K}
    - TRIGger:A:VIDeo:CUSTom:SCAN?
    - TRIGger:A:VIDeo:CUSTom:SYNCInterval <NR3>
    - TRIGger:A:VIDeo:CUSTom:SYNCInterval?
    - TRIGger:A:VIDeo:CUSTom:TYPE {INTERLAced|PROGressive}
    - TRIGger:A:VIDeo:CUSTom:TYPE?
    - TRIGger:A:VIDeo:CUSTom?
    - TRIGger:A:VIDeo:FIELD {ODD|EVEN|ALLFields|ALLLines|NUMERic}
    - TRIGger:A:VIDeo:FIELD?
    - TRIGger:A:VIDeo:HDtv:FORMat {HD1080P24|HD720P60|HD480P60|HD1080I50|HD1080P25|HD1080I60|HD1080PSF24}
    - TRIGger:A:VIDeo:HDtv:FORMat?
    - TRIGger:A:VIDeo:HOLDoff:FIELD <NR3>
    - TRIGger:A:VIDeo:HOLDoff:FIELD?
    - TRIGger:A:VIDeo:LINE <NR1>
    - TRIGger:A:VIDeo:LINE?
    - TRIGger:A:VIDeo:POLarity {NEGative|POSitive|NORMal|INVERTed}
    - TRIGger:A:VIDeo:POLarity?
    - TRIGger:A:VIDeo:SOUrce {CH<x>}
    - TRIGger:A:VIDeo:SOUrce?
    - TRIGger:A:VIDeo:STANdard {NTSc|PAL|SECAM}
    - TRIGger:A:VIDeo:STANdard?
    - TRIGger:A:VIDeo:SYNC {ODD|EVEN|ALLFields|ALLLines|NUMERic}
    - TRIGger:A:VIDeo:SYNC?
    - TRIGger:A:VIDeo?
    - TRIGger:A?
    - TRIGger:B:LEVel:D<x> {ECL|TTL|<NR3>}
    - TRIGger:B:LEVel:D<x>?
    - TRIGger:B:LOWerthreshold:D<x> {<NR3>|ECL|TTL}
    - TRIGger:B:LOWerthreshold:D<x>?
    - TRIGger:EXTernal:PRObe <NR3>
    - TRIGger:EXTernal:PRObe?
    - TRIGger:EXTernal:YUNIts?
    - TRIGger:EXTernal?
    - TRIGger:FREQuency?
    - TRIGger:STATE?
    - TRIGger?
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


class TriggerState(SCPICmdRead):
    """The ``TRIGger:STATE`` command.

    Description:
        - This query-only command returns the current state of the triggering system.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TRIGger:STATE?
        ```
    """


class TriggerFrequency(SCPICmdRead):
    """The ``TRIGger:FREQuency`` command.

    Description:
        - Returns the trigger frequency in hertz if available. If the trigger frequency is not
          currently available, the IEEE Not A Number (NaN = 99.10E+36) value is returned. The
          maximum precision of the returned frequency is 12 digits. Use the
          ``DISPLAY:TRIGFREQUENCY`` command to enable/disable the calculation of the trigger
          frequency.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:FREQuency?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TRIGger:FREQuency?
        ```
    """


class TriggerExternalYunits(SCPICmdRead):
    """The ``TRIGger:EXTernal:YUNIts`` command.

    Description:
        - Returns the vertical (Y) units of the probe attached to the Aux In connector.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:EXTernal:YUNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:EXTernal:YUNIts?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TRIGger:EXTernal:YUNIts?
        ```
    """


class TriggerExternalProbe(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:EXTernal:PRObe`` command.

    Description:
        - This command specifies the attenuation factor value of the probe attached to the Aux Input
          connector.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:EXTernal:PRObe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:EXTernal:PRObe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:EXTernal:PRObe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:EXTernal:PRObe <NR3>
        - TRIGger:EXTernal:PRObe?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the attenuation factor of the probe.
    """


class TriggerExternal(SCPICmdRead):
    """The ``TRIGger:EXTernal`` command.

    Description:
        - Returns all external trigger-related parameters for the probe attached to the Aux Input
          connector.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:EXTernal?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:EXTernal?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TRIGger:EXTernal?
        ```

    Properties:
        - ``.probe``: The ``TRIGger:EXTernal:PRObe`` command.
        - ``.yunits``: The ``TRIGger:EXTernal:YUNIts`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._probe = TriggerExternalProbe(device, f"{self._cmd_syntax}:PRObe")
        self._yunits = TriggerExternalYunits(device, f"{self._cmd_syntax}:YUNIts")

    @property
    def probe(self) -> TriggerExternalProbe:
        """Return the ``TRIGger:EXTernal:PRObe`` command.

        Description:
            - This command specifies the attenuation factor value of the probe attached to the Aux
              Input connector.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:EXTernal:PRObe?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:EXTernal:PRObe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:EXTernal:PRObe value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:EXTernal:PRObe <NR3>
            - TRIGger:EXTernal:PRObe?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the attenuation factor of the
              probe.
        """
        return self._probe

    @property
    def yunits(self) -> TriggerExternalYunits:
        """Return the ``TRIGger:EXTernal:YUNIts`` command.

        Description:
            - Returns the vertical (Y) units of the probe attached to the Aux In connector.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:EXTernal:YUNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:EXTernal:YUNIts?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TRIGger:EXTernal:YUNIts?
            ```
        """
        return self._yunits


class TriggerBLowerthresholdDigitalBit(ValidatedDigitalBit, SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:B:LOWerthreshold:D<x>`` command.

    Description:
        - Sets or queries the lower threshold for the digital channel selected. Each channel can
          have an independent level. Used in runt and transition triggers as the lower threshold.
          Used for all other trigger types as the single level/threshold.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B:LOWerthreshold:D<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B:LOWerthreshold:D<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:B:LOWerthreshold:D<x> value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:B:LOWerthreshold:D<x> {<NR3>|ECL|TTL}
        - TRIGger:B:LOWerthreshold:D<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the threshold in volts.
        - ``ECL`` specifies a preset ECL high level of -1.3V.
        - ``TTL`` specifies a preset TTL high level of 1.4V.
    """


class TriggerBLowerthreshold(SCPICmdRead):
    """The ``TRIGger:B:LOWerthreshold`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B:LOWerthreshold?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B:LOWerthreshold?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.d``: The ``TRIGger:B:LOWerthreshold:D<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._d: Dict[int, TriggerBLowerthresholdDigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: TriggerBLowerthresholdDigitalBit(device, f"{self._cmd_syntax}:D{x}")
        )

    @property
    def d(self) -> Dict[int, TriggerBLowerthresholdDigitalBit]:
        """Return the ``TRIGger:B:LOWerthreshold:D<x>`` command.

        Description:
            - Sets or queries the lower threshold for the digital channel selected. Each channel can
              have an independent level. Used in runt and transition triggers as the lower
              threshold. Used for all other trigger types as the single level/threshold.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B:LOWerthreshold:D<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B:LOWerthreshold:D<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:B:LOWerthreshold:D<x> value`` command.

        SCPI Syntax:
            ```
            - TRIGger:B:LOWerthreshold:D<x> {<NR3>|ECL|TTL}
            - TRIGger:B:LOWerthreshold:D<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the threshold in volts.
            - ``ECL`` specifies a preset ECL high level of -1.3V.
            - ``TTL`` specifies a preset TTL high level of 1.4V.
        """
        return self._d


class TriggerBLevelDigitalBit(ValidatedDigitalBit, SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:B:LEVel:D<x>`` command.

    Description:
        - This command specifies the B trigger level for digital channel <x>, where x is the channel
          number. Each channel can have an independent level.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B:LEVel:D<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B:LEVel:D<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:B:LEVel:D<x> value`` command.

    SCPI Syntax:
        ```
        - TRIGger:B:LEVel:D<x> {ECL|TTL|<NR3>}
        - TRIGger:B:LEVel:D<x>?
        ```

    Info:
        - ``ECL`` specifies a preset ECL high level of -1.3V.
        - ``TTL`` specifies a preset TTL high level of 1.4V.
        - ``<NR3>`` is a floating point number that specifies the trigger level in user units
          (usually volts).
    """


class TriggerBLevel(SCPICmdRead):
    """The ``TRIGger:B:LEVel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B:LEVel?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B:LEVel?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.d``: The ``TRIGger:B:LEVel:D<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._d: Dict[int, TriggerBLevelDigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: TriggerBLevelDigitalBit(device, f"{self._cmd_syntax}:D{x}")
        )

    @property
    def d(self) -> Dict[int, TriggerBLevelDigitalBit]:
        """Return the ``TRIGger:B:LEVel:D<x>`` command.

        Description:
            - This command specifies the B trigger level for digital channel <x>, where x is the
              channel number. Each channel can have an independent level.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B:LEVel:D<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B:LEVel:D<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:B:LEVel:D<x> value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:B:LEVel:D<x> {ECL|TTL|<NR3>}
            - TRIGger:B:LEVel:D<x>?
            ```

        Info:
            - ``ECL`` specifies a preset ECL high level of -1.3V.
            - ``TTL`` specifies a preset TTL high level of 1.4V.
            - ``<NR3>`` is a floating point number that specifies the trigger level in user units
              (usually volts).
        """
        return self._d


class TriggerB(SCPICmdRead):
    """The ``TRIGger:B`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.level``: The ``TRIGger:B:LEVel`` command tree.
        - ``.lowerthreshold``: The ``TRIGger:B:LOWerthreshold`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._level = TriggerBLevel(device, f"{self._cmd_syntax}:LEVel")
        self._lowerthreshold = TriggerBLowerthreshold(device, f"{self._cmd_syntax}:LOWerthreshold")

    @property
    def level(self) -> TriggerBLevel:
        """Return the ``TRIGger:B:LEVel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B:LEVel?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B:LEVel?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.d``: The ``TRIGger:B:LEVel:D<x>`` command.
        """
        return self._level

    @property
    def lowerthreshold(self) -> TriggerBLowerthreshold:
        """Return the ``TRIGger:B:LOWerthreshold`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B:LOWerthreshold?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B:LOWerthreshold?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.d``: The ``TRIGger:B:LOWerthreshold:D<x>`` command.
        """
        return self._lowerthreshold


class TriggerAVideoSync(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:VIDeo:SYNC`` command.

    Description:
        - This command sets the video field to use for triggering on video signals (odd fields, even
          fields, all fields, all lines, numeric).

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:SYNC?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:SYNC?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:VIDeo:SYNC value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:VIDeo:SYNC {ODD|EVEN|ALLFields|ALLLines|NUMERic}
        - TRIGger:A:VIDeo:SYNC?
        ```

    Info:
        - ``ODD`` argument sets the oscilloscope to trigger on interlaced video odd fields.
        - ``EVEN`` argument sets the oscilloscope to trigger on interlaced video even fields.
        - ``ALLFields`` argument sets the oscilloscope to trigger on all fields.
        - ``ALLLines`` argument sets the oscilloscope to trigger on all video lines.
        - ``NUMERic`` argument sets the oscilloscope to trigger on the video signal line specified
          by the ``TRIGGER:A:VIDEO:LINE`` command.
    """


class TriggerAVideoStandard(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:VIDeo:STANdard`` command.

    Description:
        - Sets or returns the standard for the video trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:STANdard?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:STANdard?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:VIDeo:STANdard value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:VIDeo:STANdard {NTSc|PAL|SECAM}
        - TRIGger:A:VIDeo:STANdard?
        ```

    Info:
        - ``NTSc`` sets the oscilloscope to trigger on video signals that meet the NTSC
          525/60/``2:1`` standard (a line rate of 525 lines per frame and a field rate of 60 Hz).
        - ``PAL`` sets the oscilloscope to trigger on video signals that meet the NTSC
          625/50/``2:1`` standard (a line rate of 625 lines per frame and a field rate of 50 Hz).
        - ``SECAM`` sets the oscilloscope to trigger on video signals that meet the SECAM standard.
    """


class TriggerAVideoSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:VIDeo:SOUrce`` command.

    Description:
        - This command sets the source channel to use for triggering on video signals (CH1-4).

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:VIDeo:SOUrce value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:VIDeo:SOUrce {CH<x>}
        - TRIGger:A:VIDeo:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies the input channel to use as the A video trigger. x has a minimum of 1
          and a maximum of 4.
    """


class TriggerAVideoPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:VIDeo:POLarity`` command.

    Description:
        - Sets or returns the polarity of the A video trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:POLarity?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:VIDeo:POLarity value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:VIDeo:POLarity {NEGative|POSitive|NORMal|INVERTed}
        - TRIGger:A:VIDeo:POLarity?
        ```

    Info:
        - ``POSitive`` argument sets the oscilloscope to trigger on a positive video sync pulse.
        - ``NEGative`` argument sets the oscilloscope to trigger on a negative video sync pulse.
    """


class TriggerAVideoLine(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:VIDeo:LINE`` command.

    Description:
        - This command lets you set the specific video line number to be used for triggering on a
          video signal. You must also use the command to specify NUMERic as the video field to use.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:LINE?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:LINE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:VIDeo:LINE value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:VIDeo:LINE <NR1>
        - TRIGger:A:VIDeo:LINE?
        ```

    Info:
        - ``<NR1>`` argument is an integer that sets the video line number on which the oscilloscope
          triggers. The following table lists the valid choices, depending on the active video
          standard.
    """


class TriggerAVideoHoldoffField(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:VIDeo:HOLDoff:FIELD`` command.

    Description:
        - This command sets the video trigger holdoff, in terms of video fields, to use for
          triggering on video signals.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:HOLDoff:FIELD?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:HOLDoff:FIELD?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:VIDeo:HOLDoff:FIELD value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:VIDeo:HOLDoff:FIELD <NR3>
        - TRIGger:A:VIDeo:HOLDoff:FIELD?
        ```

    Info:
        - ``<NR3>`` argument is a real number from 0.0 to 8.5 in increments of 0.5. The argument
          sets the number of fields that the oscilloscope waits before rearming the video trigger.
    """


class TriggerAVideoHoldoff(SCPICmdRead):
    """The ``TRIGger:A:VIDeo:HOLDoff`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:HOLDoff?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:HOLDoff?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.field``: The ``TRIGger:A:VIDeo:HOLDoff:FIELD`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._field = TriggerAVideoHoldoffField(device, f"{self._cmd_syntax}:FIELD")

    @property
    def field(self) -> TriggerAVideoHoldoffField:
        """Return the ``TRIGger:A:VIDeo:HOLDoff:FIELD`` command.

        Description:
            - This command sets the video trigger holdoff, in terms of video fields, to use for
              triggering on video signals.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:HOLDoff:FIELD?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:HOLDoff:FIELD?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:VIDeo:HOLDoff:FIELD value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:VIDeo:HOLDoff:FIELD <NR3>
            - TRIGger:A:VIDeo:HOLDoff:FIELD?
            ```

        Info:
            - ``<NR3>`` argument is a real number from 0.0 to 8.5 in increments of 0.5. The argument
              sets the number of fields that the oscilloscope waits before rearming the video
              trigger.
        """
        return self._field


class TriggerAVideoHdtvFormat(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:VIDeo:HDtv:FORMat`` command.

    Description:
        - Sets or returns the HDTV video signal format on which to trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:HDtv:FORMat?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:HDtv:FORMat?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:VIDeo:HDtv:FORMat value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:VIDeo:HDtv:FORMat {HD1080P24|HD720P60|HD480P60|HD1080I50|HD1080P25|HD1080I60|HD1080PSF24}
        - TRIGger:A:VIDeo:HDtv:FORMat?
        ```
    """  # noqa: E501


class TriggerAVideoHdtv(SCPICmdRead):
    """The ``TRIGger:A:VIDeo:HDtv`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:HDtv?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:HDtv?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.format``: The ``TRIGger:A:VIDeo:HDtv:FORMat`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._format = TriggerAVideoHdtvFormat(device, f"{self._cmd_syntax}:FORMat")

    @property
    def format(self) -> TriggerAVideoHdtvFormat:
        """Return the ``TRIGger:A:VIDeo:HDtv:FORMat`` command.

        Description:
            - Sets or returns the HDTV video signal format on which to trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:HDtv:FORMat?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:HDtv:FORMat?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:VIDeo:HDtv:FORMat value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:VIDeo:HDtv:FORMat {HD1080P24|HD720P60|HD480P60|HD1080I50|HD1080P25|HD1080I60|HD1080PSF24}
            - TRIGger:A:VIDeo:HDtv:FORMat?
            ```
        """  # noqa: E501
        return self._format


class TriggerAVideoField(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:VIDeo:FIELD`` command.

    Description:
        - This command sets the video field to use for triggering on video signals (odd fields, even
          fields, all fields, all lines, numeric).

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:FIELD?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:FIELD?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:VIDeo:FIELD value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:VIDeo:FIELD {ODD|EVEN|ALLFields|ALLLines|NUMERic}
        - TRIGger:A:VIDeo:FIELD?
        ```

    Info:
        - ``ODD`` argument sets the oscilloscope to trigger on interlaced video odd fields.
        - ``EVEN`` argument sets the oscilloscope to trigger on interlaced video even fields.
        - ``ALLFields`` argument sets the oscilloscope to trigger on all fields.
        - ``ALLLines`` argument sets the oscilloscope to trigger on all video lines.
        - ``NUMERic`` argument sets the oscilloscope to trigger on the video signal line specified
          by the ``TRIGGER:A:VIDEO:LINE`` command.
    """


class TriggerAVideoCustomType(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:VIDeo:CUSTom:TYPE`` command.

    Description:
        - Sets or returns the video trigger format. Use this command only when the video format is
          set to custom.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:CUSTom:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:CUSTom:TYPE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:VIDeo:CUSTom:TYPE value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:VIDeo:CUSTom:TYPE {INTERLAced|PROGressive}
        - TRIGger:A:VIDeo:CUSTom:TYPE?
        ```

    Info:
        - ``INTERLAced`` argument sets the format for interlaced video lines.
        - ``PROGressive`` argument sets the format for progressive video lines.
    """


class TriggerAVideoCustomSyncinterval(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:VIDeo:CUSTom:SYNCInterval`` command.

    Description:
        - This command sets the sync interval for the standard under test to use for triggering on
          video signals. This is only required for BiLevel Custom. To use this command, you must
          also set the video standard to BILevelcustom (using ``TRIGGER:A:VIDEO:STANDARD``).

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:CUSTom:SYNCInterval?``
          query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:CUSTom:SYNCInterval?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:VIDeo:CUSTom:SYNCInterval value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:VIDeo:CUSTom:SYNCInterval <NR3>
        - TRIGger:A:VIDeo:CUSTom:SYNCInterval?
        ```

    Info:
        - ``<NR3>`` is the sync interval.
    """


class TriggerAVideoCustomScan(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:VIDeo:CUSTom:SCAN`` command.

    Description:
        - Sets or returns the horizontal line scan rate of the A video trigger. Use this command
          only when the video format is set to custom.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:CUSTom:SCAN?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:CUSTom:SCAN?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:VIDeo:CUSTom:SCAN value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:VIDeo:CUSTom:SCAN {RATE15K|RATE20K|RATE25K|RATE35K|RATE50K}
        - TRIGger:A:VIDeo:CUSTom:SCAN?
        ```

    Info:
        - ``RATE15`` sets the range of the video line scan rate to 15 kHz through 20 kHz. This is
          the standard broadcast rate.
        - ``RATE20`` sets the range of the video line scan rate to 20 kHz through 25 kHz.
        - ``RATE25`` sets the range of the video line scan rate to 25 kHz through 35 kHz.
        - ``RATE35`` sets the range of the video line scan rate to 35 kHz through 50 kHz.
        - ``RATE50`` sets the range of the video line scan rate to 50 kHz through 65 kHz.
    """


class TriggerAVideoCustomLineperiod(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:VIDeo:CUSTom:LINEPeriod`` command.

    Description:
        - This command sets the line period for the standard under test. To use this command, you
          must also set the video standard to BILevelcustom or TRILevelcustom (using
          ``TRIGGER:A:VIDEO:STANDARD``).

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:CUSTom:LINEPeriod?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:CUSTom:LINEPeriod?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:VIDeo:CUSTom:LINEPeriod value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:VIDeo:CUSTom:LINEPeriod <NR3>
        - TRIGger:A:VIDeo:CUSTom:LINEPeriod?
        ```

    Info:
        - ``<NR3>`` is the custom video line period.
    """


class TriggerAVideoCustomFormat(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:VIDeo:CUSTom:FORMat`` command.

    Description:
        - Sets or returns the video trigger format. Use this command only when the video format is
          set to custom.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:CUSTom:FORMat?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:CUSTom:FORMat?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:VIDeo:CUSTom:FORMat value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:VIDeo:CUSTom:FORMat {INTERLAced|PROGressive}
        - TRIGger:A:VIDeo:CUSTom:FORMat?
        ```

    Info:
        - ``INTERLAced`` argument sets the format for interlaced video lines.
        - ``PROGressive`` argument sets the format for progressive video lines.
    """


class TriggerAVideoCustom(SCPICmdRead):
    """The ``TRIGger:A:VIDeo:CUSTom`` command.

    Description:
        - This query-only command returns the A trigger custom video parameters.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:CUSTom?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:CUSTom?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TRIGger:A:VIDeo:CUSTom?
        ```

    Properties:
        - ``.lineperiod``: The ``TRIGger:A:VIDeo:CUSTom:LINEPeriod`` command.
        - ``.scan``: The ``TRIGger:A:VIDeo:CUSTom:SCAN`` command.
        - ``.syncinterval``: The ``TRIGger:A:VIDeo:CUSTom:SYNCInterval`` command.
        - ``.format``: The ``TRIGger:A:VIDeo:CUSTom:FORMat`` command.
        - ``.type``: The ``TRIGger:A:VIDeo:CUSTom:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._lineperiod = TriggerAVideoCustomLineperiod(device, f"{self._cmd_syntax}:LINEPeriod")
        self._scan = TriggerAVideoCustomScan(device, f"{self._cmd_syntax}:SCAN")
        self._syncinterval = TriggerAVideoCustomSyncinterval(
            device, f"{self._cmd_syntax}:SYNCInterval"
        )
        self._format = TriggerAVideoCustomFormat(device, f"{self._cmd_syntax}:FORMat")
        self._type = TriggerAVideoCustomType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def lineperiod(self) -> TriggerAVideoCustomLineperiod:
        """Return the ``TRIGger:A:VIDeo:CUSTom:LINEPeriod`` command.

        Description:
            - This command sets the line period for the standard under test. To use this command,
              you must also set the video standard to BILevelcustom or TRILevelcustom (using
              ``TRIGGER:A:VIDEO:STANDARD``).

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:CUSTom:LINEPeriod?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:VIDeo:CUSTom:LINEPeriod?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:VIDeo:CUSTom:LINEPeriod value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:VIDeo:CUSTom:LINEPeriod <NR3>
            - TRIGger:A:VIDeo:CUSTom:LINEPeriod?
            ```

        Info:
            - ``<NR3>`` is the custom video line period.
        """
        return self._lineperiod

    @property
    def scan(self) -> TriggerAVideoCustomScan:
        """Return the ``TRIGger:A:VIDeo:CUSTom:SCAN`` command.

        Description:
            - Sets or returns the horizontal line scan rate of the A video trigger. Use this command
              only when the video format is set to custom.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:CUSTom:SCAN?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:CUSTom:SCAN?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:VIDeo:CUSTom:SCAN value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:VIDeo:CUSTom:SCAN {RATE15K|RATE20K|RATE25K|RATE35K|RATE50K}
            - TRIGger:A:VIDeo:CUSTom:SCAN?
            ```

        Info:
            - ``RATE15`` sets the range of the video line scan rate to 15 kHz through 20 kHz. This
              is the standard broadcast rate.
            - ``RATE20`` sets the range of the video line scan rate to 20 kHz through 25 kHz.
            - ``RATE25`` sets the range of the video line scan rate to 25 kHz through 35 kHz.
            - ``RATE35`` sets the range of the video line scan rate to 35 kHz through 50 kHz.
            - ``RATE50`` sets the range of the video line scan rate to 50 kHz through 65 kHz.
        """
        return self._scan

    @property
    def syncinterval(self) -> TriggerAVideoCustomSyncinterval:
        """Return the ``TRIGger:A:VIDeo:CUSTom:SYNCInterval`` command.

        Description:
            - This command sets the sync interval for the standard under test to use for triggering
              on video signals. This is only required for BiLevel Custom. To use this command, you
              must also set the video standard to BILevelcustom (using
              ``TRIGGER:A:VIDEO:STANDARD``).

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:CUSTom:SYNCInterval?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:VIDeo:CUSTom:SYNCInterval?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:VIDeo:CUSTom:SYNCInterval value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:VIDeo:CUSTom:SYNCInterval <NR3>
            - TRIGger:A:VIDeo:CUSTom:SYNCInterval?
            ```

        Info:
            - ``<NR3>`` is the sync interval.
        """
        return self._syncinterval

    @property
    def format(self) -> TriggerAVideoCustomFormat:
        """Return the ``TRIGger:A:VIDeo:CUSTom:FORMat`` command.

        Description:
            - Sets or returns the video trigger format. Use this command only when the video format
              is set to custom.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:CUSTom:FORMat?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:CUSTom:FORMat?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:VIDeo:CUSTom:FORMat value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:VIDeo:CUSTom:FORMat {INTERLAced|PROGressive}
            - TRIGger:A:VIDeo:CUSTom:FORMat?
            ```

        Info:
            - ``INTERLAced`` argument sets the format for interlaced video lines.
            - ``PROGressive`` argument sets the format for progressive video lines.
        """
        return self._format

    @property
    def type(self) -> TriggerAVideoCustomType:
        """Return the ``TRIGger:A:VIDeo:CUSTom:TYPE`` command.

        Description:
            - Sets or returns the video trigger format. Use this command only when the video format
              is set to custom.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:CUSTom:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:CUSTom:TYPE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:VIDeo:CUSTom:TYPE value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:VIDeo:CUSTom:TYPE {INTERLAced|PROGressive}
            - TRIGger:A:VIDeo:CUSTom:TYPE?
            ```

        Info:
            - ``INTERLAced`` argument sets the format for interlaced video lines.
            - ``PROGressive`` argument sets the format for progressive video lines.
        """
        return self._type


#  pylint: disable=too-many-instance-attributes
class TriggerAVideo(SCPICmdRead):
    """The ``TRIGger:A:VIDeo`` command.

    Description:
        - Returns the A trigger video parameters.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TRIGger:A:VIDeo?
        ```

    Properties:
        - ``.custom``: The ``TRIGger:A:VIDeo:CUSTom`` command.
        - ``.hdtv``: The ``TRIGger:A:VIDeo:HDtv`` command tree.
        - ``.holdoff``: The ``TRIGger:A:VIDeo:HOLDoff`` command tree.
        - ``.line``: The ``TRIGger:A:VIDeo:LINE`` command.
        - ``.polarity``: The ``TRIGger:A:VIDeo:POLarity`` command.
        - ``.source``: The ``TRIGger:A:VIDeo:SOUrce`` command.
        - ``.standard``: The ``TRIGger:A:VIDeo:STANdard`` command.
        - ``.sync``: The ``TRIGger:A:VIDeo:SYNC`` command.
        - ``.field``: The ``TRIGger:A:VIDeo:FIELD`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._custom = TriggerAVideoCustom(device, f"{self._cmd_syntax}:CUSTom")
        self._hdtv = TriggerAVideoHdtv(device, f"{self._cmd_syntax}:HDtv")
        self._holdoff = TriggerAVideoHoldoff(device, f"{self._cmd_syntax}:HOLDoff")
        self._line = TriggerAVideoLine(device, f"{self._cmd_syntax}:LINE")
        self._polarity = TriggerAVideoPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = TriggerAVideoSource(device, f"{self._cmd_syntax}:SOUrce")
        self._standard = TriggerAVideoStandard(device, f"{self._cmd_syntax}:STANdard")
        self._sync = TriggerAVideoSync(device, f"{self._cmd_syntax}:SYNC")
        self._field = TriggerAVideoField(device, f"{self._cmd_syntax}:FIELD")

    @property
    def custom(self) -> TriggerAVideoCustom:
        """Return the ``TRIGger:A:VIDeo:CUSTom`` command.

        Description:
            - This query-only command returns the A trigger custom video parameters.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:CUSTom?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:CUSTom?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TRIGger:A:VIDeo:CUSTom?
            ```

        Sub-properties:
            - ``.lineperiod``: The ``TRIGger:A:VIDeo:CUSTom:LINEPeriod`` command.
            - ``.scan``: The ``TRIGger:A:VIDeo:CUSTom:SCAN`` command.
            - ``.syncinterval``: The ``TRIGger:A:VIDeo:CUSTom:SYNCInterval`` command.
            - ``.format``: The ``TRIGger:A:VIDeo:CUSTom:FORMat`` command.
            - ``.type``: The ``TRIGger:A:VIDeo:CUSTom:TYPE`` command.
        """
        return self._custom

    @property
    def hdtv(self) -> TriggerAVideoHdtv:
        """Return the ``TRIGger:A:VIDeo:HDtv`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:HDtv?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:HDtv?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.format``: The ``TRIGger:A:VIDeo:HDtv:FORMat`` command.
        """
        return self._hdtv

    @property
    def holdoff(self) -> TriggerAVideoHoldoff:
        """Return the ``TRIGger:A:VIDeo:HOLDoff`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:HOLDoff?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:HOLDoff?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.field``: The ``TRIGger:A:VIDeo:HOLDoff:FIELD`` command.
        """
        return self._holdoff

    @property
    def line(self) -> TriggerAVideoLine:
        """Return the ``TRIGger:A:VIDeo:LINE`` command.

        Description:
            - This command lets you set the specific video line number to be used for triggering on
              a video signal. You must also use the command to specify NUMERic as the video field to
              use.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:LINE?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:LINE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:VIDeo:LINE value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:VIDeo:LINE <NR1>
            - TRIGger:A:VIDeo:LINE?
            ```

        Info:
            - ``<NR1>`` argument is an integer that sets the video line number on which the
              oscilloscope triggers. The following table lists the valid choices, depending on the
              active video standard.
        """
        return self._line

    @property
    def polarity(self) -> TriggerAVideoPolarity:
        """Return the ``TRIGger:A:VIDeo:POLarity`` command.

        Description:
            - Sets or returns the polarity of the A video trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:POLarity?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:VIDeo:POLarity value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:VIDeo:POLarity {NEGative|POSitive|NORMal|INVERTed}
            - TRIGger:A:VIDeo:POLarity?
            ```

        Info:
            - ``POSitive`` argument sets the oscilloscope to trigger on a positive video sync pulse.
            - ``NEGative`` argument sets the oscilloscope to trigger on a negative video sync pulse.
        """
        return self._polarity

    @property
    def source(self) -> TriggerAVideoSource:
        """Return the ``TRIGger:A:VIDeo:SOUrce`` command.

        Description:
            - This command sets the source channel to use for triggering on video signals (CH1-4).

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:VIDeo:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:VIDeo:SOUrce {CH<x>}
            - TRIGger:A:VIDeo:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies the input channel to use as the A video trigger. x has a minimum
              of 1 and a maximum of 4.
        """
        return self._source

    @property
    def standard(self) -> TriggerAVideoStandard:
        """Return the ``TRIGger:A:VIDeo:STANdard`` command.

        Description:
            - Sets or returns the standard for the video trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:STANdard?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:STANdard?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:VIDeo:STANdard value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:VIDeo:STANdard {NTSc|PAL|SECAM}
            - TRIGger:A:VIDeo:STANdard?
            ```

        Info:
            - ``NTSc`` sets the oscilloscope to trigger on video signals that meet the NTSC
              525/60/``2:1`` standard (a line rate of 525 lines per frame and a field rate of 60
              Hz).
            - ``PAL`` sets the oscilloscope to trigger on video signals that meet the NTSC
              625/50/``2:1`` standard (a line rate of 625 lines per frame and a field rate of 50
              Hz).
            - ``SECAM`` sets the oscilloscope to trigger on video signals that meet the SECAM
              standard.
        """
        return self._standard

    @property
    def sync(self) -> TriggerAVideoSync:
        """Return the ``TRIGger:A:VIDeo:SYNC`` command.

        Description:
            - This command sets the video field to use for triggering on video signals (odd fields,
              even fields, all fields, all lines, numeric).

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:SYNC?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:SYNC?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:VIDeo:SYNC value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:VIDeo:SYNC {ODD|EVEN|ALLFields|ALLLines|NUMERic}
            - TRIGger:A:VIDeo:SYNC?
            ```

        Info:
            - ``ODD`` argument sets the oscilloscope to trigger on interlaced video odd fields.
            - ``EVEN`` argument sets the oscilloscope to trigger on interlaced video even fields.
            - ``ALLFields`` argument sets the oscilloscope to trigger on all fields.
            - ``ALLLines`` argument sets the oscilloscope to trigger on all video lines.
            - ``NUMERic`` argument sets the oscilloscope to trigger on the video signal line
              specified by the ``TRIGGER:A:VIDEO:LINE`` command.
        """
        return self._sync

    @property
    def field(self) -> TriggerAVideoField:
        """Return the ``TRIGger:A:VIDeo:FIELD`` command.

        Description:
            - This command sets the video field to use for triggering on video signals (odd fields,
              even fields, all fields, all lines, numeric).

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:FIELD?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:FIELD?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:VIDeo:FIELD value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:VIDeo:FIELD {ODD|EVEN|ALLFields|ALLLines|NUMERic}
            - TRIGger:A:VIDeo:FIELD?
            ```

        Info:
            - ``ODD`` argument sets the oscilloscope to trigger on interlaced video odd fields.
            - ``EVEN`` argument sets the oscilloscope to trigger on interlaced video even fields.
            - ``ALLFields`` argument sets the oscilloscope to trigger on all fields.
            - ``ALLLines`` argument sets the oscilloscope to trigger on all video lines.
            - ``NUMERic`` argument sets the oscilloscope to trigger on the video signal line
              specified by the ``TRIGGER:A:VIDEO:LINE`` command.
        """
        return self._field


class TriggerAUpperthresholdChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:UPPerthreshold:CH<x>`` command.

    Description:
        - This command sets the upper threshold for channel <x>, where x is the analog channel
          number 1-4. Each channel can have an independent level. Used only for runt and transition
          trigger types.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:UPPerthreshold:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:UPPerthreshold:CH<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:UPPerthreshold:CH<x> value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:UPPerthreshold:CH<x> {<NR3>|ECL|TTL}
        - TRIGger:A:UPPerthreshold:CH<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the threshold level, in volts.
        - ``ECL`` specifies a preset ECL high level of -1.3V.
        - ``TTL`` specifies a preset TTL high level of 1.4V.
    """


class TriggerAUpperthreshold(SCPICmdRead):
    """The ``TRIGger:A:UPPerthreshold`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:UPPerthreshold?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:UPPerthreshold?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``TRIGger:A:UPPerthreshold:CH<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, TriggerAUpperthresholdChannel] = DefaultDictPassKeyToFactory(
            lambda x: TriggerAUpperthresholdChannel(device, f"{self._cmd_syntax}:CH{x}")
        )

    @property
    def ch(self) -> Dict[int, TriggerAUpperthresholdChannel]:
        """Return the ``TRIGger:A:UPPerthreshold:CH<x>`` command.

        Description:
            - This command sets the upper threshold for channel <x>, where x is the analog channel
              number 1-4. Each channel can have an independent level. Used only for runt and
              transition trigger types.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:UPPerthreshold:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:UPPerthreshold:CH<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:UPPerthreshold:CH<x> value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:UPPerthreshold:CH<x> {<NR3>|ECL|TTL}
            - TRIGger:A:UPPerthreshold:CH<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the threshold level, in volts.
            - ``ECL`` specifies a preset ECL high level of -1.3V.
            - ``TTL`` specifies a preset TTL high level of 1.4V.
        """
        return self._ch


class TriggerAType(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:TYPe`` command.

    Description:
        - Sets or returns the type of A trigger. The five types of triggers are of Edge, Logic,
          Pulse, Serial, and Video. Logic and Pulse triggers contain classes. Logic triggers consist
          of State, Pattern, and SetHold classes; Pulse triggers consist of Runt, Width, and
          Transition logic classes. Once you have set the trigger type, you may also need to
          identify the associated trigger class. For details on selecting Logic and Pulse trigger
          classes, see ``TRIGGER:A:LOGIC:CLASS`` and ``TRIGGER:A:PULSE:CLASS`` respectively.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:TYPe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:TYPe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:TYPe {EDGe|LOGic|PULSe|BUS|VIDeo}
        - TRIGger:A:TYPe?
        ```

    Info:
        - ``EDGe`` is a normal trigger. A trigger event occurs when a signal passes through a
          specified voltage level in a specified direction and is controlled by the
          ``TRIGGER:A:EDGE`` commands.
        - ``LOGic`` specifies that a trigger occurs when specified conditions are met and is
          controlled by the ``TRIGGER:A:LOGIC`` commands.
        - ``PULSe`` specifies that a trigger occurs when a specified pulse is found and is
          controlled by the ``TRIGGER:A:PULSE`` commands.
        - ``BUS`` specifies that a trigger occurs when a communications signal is found. Supports
          CAN, I2C, SPI, and RS232 communications signals.
        - ``VIDeo`` specifies that the trigger occurs when a video signal is found.
    """


class TriggerATransitionWhen(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:TRANsition:WHEn`` command.

    Description:
        - This command specifies whether to check for a transitioning signal that is faster or
          slower than the specified delta time.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:TRANsition:WHEn?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:TRANsition:WHEn?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:TRANsition:WHEn value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:TRANsition:WHEn {SLOWer|FASTer|EQual|UNEQual}
        - TRIGger:A:TRANsition:WHEn?
        ```

    Info:
        - ``FASTer`` sets the trigger to occur when the signal transition time is faster than the
          time set by ``TRIGger:A:TRANsition:DELTatime``.
        - ``SLOWer`` sets the trigger to occur when the signal transition time is slower than the
          time set by.``TRIGger:A:TRANsition:DELTatime``.
        - ``EQual`` sets the trigger to occur when the signal transition time is equal to the time
          set by ``TRIGger:A:TRANsition:DELTatime``.
        - ``UNEQual`` sets the trigger to occur when the signal transition time is not equal to the
          time set by ``TRIGger:A:TRANsition:DELTatime``.
    """


class TriggerATransitionSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:TRANsition:SOUrce`` command.

    Description:
        - Sets or returns the source for transition trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:TRANsition:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:TRANsition:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:TRANsition:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:TRANsition:SOUrce {CH<x>|D<x>}
        - TRIGger:A:TRANsition:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies one of the input channels. x has a minimum of 1 and a maximum of 4.
        - ``D<x>`` specifies one of the input digital channels. x has a minimum of 0 and a maximum
          of 15.
    """


class TriggerATransitionPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:TRANsition:POLarity`` command.

    Description:
        - This command specifies the polarity for the transition trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:TRANsition:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:TRANsition:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:TRANsition:POLarity value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:TRANsition:POLarity {EITher|NEGative|POSitive}
        - TRIGger:A:TRANsition:POLarity?
        ```

    Info:
        - ``POSitive`` indicates that a pulse edge must traverse from the lower (most negative) to
          higher (most positive) level for transition triggering to occur.
        - ``NEGative`` indicates that a pulse edge must traverse from the upper (most positive) to
          lower (most negative) level for transition triggering to occur.
        - ``EITher`` indicates either positive or negative polarity.
    """


class TriggerATransitionDeltatime(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:TRANsition:DELTatime`` command.

    Description:
        - This command specifies the delta time used in calculating the transition value for the
          transition trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:TRANsition:DELTatime?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:TRANsition:DELTatime?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:TRANsition:DELTatime value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:TRANsition:DELTatime <NR3>
        - TRIGger:A:TRANsition:DELTatime?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the delta time, in seconds.
    """


class TriggerATransition(SCPICmdRead):
    """The ``TRIGger:A:TRANsition`` command.

    Description:
        - Returns transition time trigger parameters.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:TRANsition?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:TRANsition?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TRIGger:A:TRANsition?
        ```

    Properties:
        - ``.deltatime``: The ``TRIGger:A:TRANsition:DELTatime`` command.
        - ``.polarity``: The ``TRIGger:A:TRANsition:POLarity`` command.
        - ``.source``: The ``TRIGger:A:TRANsition:SOUrce`` command.
        - ``.when``: The ``TRIGger:A:TRANsition:WHEn`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._deltatime = TriggerATransitionDeltatime(device, f"{self._cmd_syntax}:DELTatime")
        self._polarity = TriggerATransitionPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = TriggerATransitionSource(device, f"{self._cmd_syntax}:SOUrce")
        self._when = TriggerATransitionWhen(device, f"{self._cmd_syntax}:WHEn")

    @property
    def deltatime(self) -> TriggerATransitionDeltatime:
        """Return the ``TRIGger:A:TRANsition:DELTatime`` command.

        Description:
            - This command specifies the delta time used in calculating the transition value for the
              transition trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:TRANsition:DELTatime?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:TRANsition:DELTatime?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:TRANsition:DELTatime value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:TRANsition:DELTatime <NR3>
            - TRIGger:A:TRANsition:DELTatime?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the delta time, in seconds.
        """
        return self._deltatime

    @property
    def polarity(self) -> TriggerATransitionPolarity:
        """Return the ``TRIGger:A:TRANsition:POLarity`` command.

        Description:
            - This command specifies the polarity for the transition trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:TRANsition:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:TRANsition:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:TRANsition:POLarity value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:TRANsition:POLarity {EITher|NEGative|POSitive}
            - TRIGger:A:TRANsition:POLarity?
            ```

        Info:
            - ``POSitive`` indicates that a pulse edge must traverse from the lower (most negative)
              to higher (most positive) level for transition triggering to occur.
            - ``NEGative`` indicates that a pulse edge must traverse from the upper (most positive)
              to lower (most negative) level for transition triggering to occur.
            - ``EITher`` indicates either positive or negative polarity.
        """
        return self._polarity

    @property
    def source(self) -> TriggerATransitionSource:
        """Return the ``TRIGger:A:TRANsition:SOUrce`` command.

        Description:
            - Sets or returns the source for transition trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:TRANsition:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:TRANsition:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:TRANsition:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:TRANsition:SOUrce {CH<x>|D<x>}
            - TRIGger:A:TRANsition:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies one of the input channels. x has a minimum of 1 and a maximum of
              4.
            - ``D<x>`` specifies one of the input digital channels. x has a minimum of 0 and a
              maximum of 15.
        """
        return self._source

    @property
    def when(self) -> TriggerATransitionWhen:
        """Return the ``TRIGger:A:TRANsition:WHEn`` command.

        Description:
            - This command specifies whether to check for a transitioning signal that is faster or
              slower than the specified delta time.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:TRANsition:WHEn?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:TRANsition:WHEn?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:TRANsition:WHEn value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:TRANsition:WHEn {SLOWer|FASTer|EQual|UNEQual}
            - TRIGger:A:TRANsition:WHEn?
            ```

        Info:
            - ``FASTer`` sets the trigger to occur when the signal transition time is faster than
              the time set by ``TRIGger:A:TRANsition:DELTatime``.
            - ``SLOWer`` sets the trigger to occur when the signal transition time is slower than
              the time set by.``TRIGger:A:TRANsition:DELTatime``.
            - ``EQual`` sets the trigger to occur when the signal transition time is equal to the
              time set by ``TRIGger:A:TRANsition:DELTatime``.
            - ``UNEQual`` sets the trigger to occur when the signal transition time is not equal to
              the time set by ``TRIGger:A:TRANsition:DELTatime``.
        """
        return self._when


class TriggerASetholdThresholdDigitalBit(ValidatedDigitalBit, SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:SETHold:THReshold:D<x>`` command.

    Description:
        - This command sets the threshold for the specified digital channel. <x> can be D0 - D15.
          All trigger types using the digital channel are affected.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:THReshold:D<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:THReshold:D<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:SETHold:THReshold:D<x> value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:SETHold:THReshold:D<x> {<NR3>|ECL|TTL}
        - TRIGger:A:SETHold:THReshold:D<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the threshold voltage, in volts.
        - ``ECL`` specifies a preset ECL high level of -1.3V.
        - ``TTL`` specifies a preset TTL high level of 1.4V.
    """


class TriggerASetholdThresholdChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:SETHold:THReshold:CH<x>`` command.

    Description:
        - This command specifies the threshold for the analog channel <x>. x can be 1-4. All trigger
          types using the channel are affected.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:THReshold:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:THReshold:CH<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:SETHold:THReshold:CH<x> value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:SETHold:THReshold:CH<x> {<NR3>|ECL|TTL}
        - TRIGger:A:SETHold:THReshold:CH<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the threshold voltage, in volts.
        - ``ECL`` specifies a preset ECL high level of -1.3V.
        - ``TTL`` specifies a preset TTL high level of 1.4V.
    """


class TriggerASetholdThreshold(SCPICmdRead):
    """The ``TRIGger:A:SETHold:THReshold`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``TRIGger:A:SETHold:THReshold:CH<x>`` command.
        - ``.d``: The ``TRIGger:A:SETHold:THReshold:D<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, TriggerASetholdThresholdChannel] = DefaultDictPassKeyToFactory(
            lambda x: TriggerASetholdThresholdChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._d: Dict[int, TriggerASetholdThresholdDigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: TriggerASetholdThresholdDigitalBit(device, f"{self._cmd_syntax}:D{x}")
        )

    @property
    def ch(self) -> Dict[int, TriggerASetholdThresholdChannel]:
        """Return the ``TRIGger:A:SETHold:THReshold:CH<x>`` command.

        Description:
            - This command specifies the threshold for the analog channel <x>. x can be 1-4. All
              trigger types using the channel are affected.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:THReshold:CH<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:SETHold:THReshold:CH<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:SETHold:THReshold:CH<x> value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:SETHold:THReshold:CH<x> {<NR3>|ECL|TTL}
            - TRIGger:A:SETHold:THReshold:CH<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the threshold voltage, in volts.
            - ``ECL`` specifies a preset ECL high level of -1.3V.
            - ``TTL`` specifies a preset TTL high level of 1.4V.
        """
        return self._ch

    @property
    def d(self) -> Dict[int, TriggerASetholdThresholdDigitalBit]:
        """Return the ``TRIGger:A:SETHold:THReshold:D<x>`` command.

        Description:
            - This command sets the threshold for the specified digital channel. <x> can be D0 -
              D15. All trigger types using the digital channel are affected.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:THReshold:D<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:SETHold:THReshold:D<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:SETHold:THReshold:D<x> value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:SETHold:THReshold:D<x> {<NR3>|ECL|TTL}
            - TRIGger:A:SETHold:THReshold:D<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the threshold voltage, in volts.
            - ``ECL`` specifies a preset ECL high level of -1.3V.
            - ``TTL`` specifies a preset TTL high level of 1.4V.
        """
        return self._d


class TriggerASetholdSettime(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:SETHold:SETTime`` command.

    Description:
        - This command specifies the setup time for setup and hold violation triggering. This
          command is equivalent to selecting Setup/Hold Setup from the Trig menu and then setting
          the desired Setup Time.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:SETTime?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:SETTime?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:SETHold:SETTime value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:SETHold:SETTime <NR3>
        - TRIGger:A:SETHold:SETTime?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the setup time for setup and hold
          violation triggering.
    """


class TriggerASetholdHoldtime(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:SETHold:HOLDTime`` command.

    Description:
        - This command specifies the hold time for setup and hold violation triggering. This command
          is equivalent to selecting Setup/Hold Setup from the Trig menu and then setting the
          desired Hold Time.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:HOLDTime?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:HOLDTime?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:SETHold:HOLDTime value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:SETHold:HOLDTime <NR3>
        - TRIGger:A:SETHold:HOLDTime?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the hold time setting, in seconds.
          Positive values for hold time occur after the clock edge. Negative values occur before the
          clock edge.
    """


class TriggerASetholdDataThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:SETHold:DATa:THReshold`` command.

    Description:
        - Sets or returns the data voltage threshold for setup and hold trigger. The digital
          channels do not have independent trigger levels. Channels D0-D7 share one common trigger
          level and D8-D15 share another common trigger level. For example changing the trigger
          level for D3 changes the levels for D0-D7.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:DATa:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:DATa:THReshold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:SETHold:DATa:THReshold value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:SETHold:DATa:THReshold {<NR3>|TTL|ECL}
        - TRIGger:A:SETHold:DATa:THReshold?
        ```

    Info:
        - ``TTL`` specifies the preset TTL high level of 1.4 V.
        - ``ECL`` specifies the preset ECL high level of -1.3 V.
        - ``<NR3>`` is the setup and hold data level, in V.
    """


class TriggerASetholdDataSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:SETHold:DATa:SOUrce`` command.

    Description:
        - Sets or returns the data source for the setup and hold trigger. You cannot specify the
          same source for both clock and data. For DPO models, you can specify only a single data
          source. Data sources for DPO models may be one of CH1-CH4 or D0-D15.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:DATa:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:DATa:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:SETHold:DATa:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:SETHold:DATa:SOUrce DPO Models:{CH<x>|D<x>}
        - TRIGger:A:SETHold:DATa:SOUrce?
        ```

    Info:
        - ``<wfm>`` specifies the source channel number and is one of CH1-CH4, and D0-D15. You can
          specify only one waveform on a DPO.
    """


class TriggerASetholdData(SCPICmdRead):
    """The ``TRIGger:A:SETHold:DATa`` command.

    Description:
        - Returns the voltage threshold and data source for the setup and hold trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:DATa?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TRIGger:A:SETHold:DATa?
        ```

    Properties:
        - ``.source``: The ``TRIGger:A:SETHold:DATa:SOUrce`` command.
        - ``.threshold``: The ``TRIGger:A:SETHold:DATa:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = TriggerASetholdDataSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = TriggerASetholdDataThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def source(self) -> TriggerASetholdDataSource:
        """Return the ``TRIGger:A:SETHold:DATa:SOUrce`` command.

        Description:
            - Sets or returns the data source for the setup and hold trigger. You cannot specify the
              same source for both clock and data. For DPO models, you can specify only a single
              data source. Data sources for DPO models may be one of CH1-CH4 or D0-D15.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:DATa:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:DATa:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:SETHold:DATa:SOUrce value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:SETHold:DATa:SOUrce DPO Models:{CH<x>|D<x>}
            - TRIGger:A:SETHold:DATa:SOUrce?
            ```

        Info:
            - ``<wfm>`` specifies the source channel number and is one of CH1-CH4, and D0-D15. You
              can specify only one waveform on a DPO.
        """
        return self._source

    @property
    def threshold(self) -> TriggerASetholdDataThreshold:
        """Return the ``TRIGger:A:SETHold:DATa:THReshold`` command.

        Description:
            - Sets or returns the data voltage threshold for setup and hold trigger. The digital
              channels do not have independent trigger levels. Channels D0-D7 share one common
              trigger level and D8-D15 share another common trigger level. For example changing the
              trigger level for D3 changes the levels for D0-D7.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:DATa:THReshold?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:SETHold:DATa:THReshold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:SETHold:DATa:THReshold value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:SETHold:DATa:THReshold {<NR3>|TTL|ECL}
            - TRIGger:A:SETHold:DATa:THReshold?
            ```

        Info:
            - ``TTL`` specifies the preset TTL high level of 1.4 V.
            - ``ECL`` specifies the preset ECL high level of -1.3 V.
            - ``<NR3>`` is the setup and hold data level, in V.
        """
        return self._threshold


class TriggerASetholdClockThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:SETHold:CLOCk:THReshold`` command.

    Description:
        - Sets or returns the clock voltage threshold for the setup and hold trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:CLOCk:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:CLOCk:THReshold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:SETHold:CLOCk:THReshold value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:SETHold:CLOCk:THReshold {<NR3>|TTL|ECL}
        - TRIGger:A:SETHold:CLOCk:THReshold?
        ```

    Info:
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
        - ``ECL`` specifies a preset ECL high level of -1.3 V.
        - ``<NR3>`` is the clock level, in volts.
    """


class TriggerASetholdClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:SETHold:CLOCk:SOUrce`` command.

    Description:
        - Sets or returns the clock source for the setup and hold triggering.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:CLOCk:SOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:SETHold:CLOCk:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:SETHold:CLOCk:SOUrce {CH<x>|D<x>}
        - TRIGger:A:SETHold:CLOCk:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies the input channel number. x has a minimum of 1 and a maximum of 4.
        - ``D<x>`` specifies the input digital channel number. x has a minimum of 0 and a maximum of
          15.
    """


class TriggerASetholdClockEdge(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:SETHold:CLOCk:EDGE`` command.

    Description:
        - This command specifies the clock edge polarity for setup and hold triggering.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:CLOCk:EDGE?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:CLOCk:EDGE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:SETHold:CLOCk:EDGE value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:SETHold:CLOCk:EDGE {FALL|RISe}
        - TRIGger:A:SETHold:CLOCk:EDGE?
        ```

    Info:
        - ``FALL`` specifies polarity as the clock falling edge.
        - ``RISe`` specifies polarity as the clock rising edge.
    """


class TriggerASetholdClock(SCPICmdRead):
    """The ``TRIGger:A:SETHold:CLOCk`` command.

    Description:
        - Returns the clock edge polarity, voltage threshold, and source input for setup and hold
          triggering.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:CLOCk?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TRIGger:A:SETHold:CLOCk?
        ```

    Properties:
        - ``.edge``: The ``TRIGger:A:SETHold:CLOCk:EDGE`` command.
        - ``.source``: The ``TRIGger:A:SETHold:CLOCk:SOUrce`` command.
        - ``.threshold``: The ``TRIGger:A:SETHold:CLOCk:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._edge = TriggerASetholdClockEdge(device, f"{self._cmd_syntax}:EDGE")
        self._source = TriggerASetholdClockSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = TriggerASetholdClockThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def edge(self) -> TriggerASetholdClockEdge:
        """Return the ``TRIGger:A:SETHold:CLOCk:EDGE`` command.

        Description:
            - This command specifies the clock edge polarity for setup and hold triggering.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:CLOCk:EDGE?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:CLOCk:EDGE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:SETHold:CLOCk:EDGE value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:SETHold:CLOCk:EDGE {FALL|RISe}
            - TRIGger:A:SETHold:CLOCk:EDGE?
            ```

        Info:
            - ``FALL`` specifies polarity as the clock falling edge.
            - ``RISe`` specifies polarity as the clock rising edge.
        """
        return self._edge

    @property
    def source(self) -> TriggerASetholdClockSource:
        """Return the ``TRIGger:A:SETHold:CLOCk:SOUrce`` command.

        Description:
            - Sets or returns the clock source for the setup and hold triggering.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:CLOCk:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:CLOCk:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:SETHold:CLOCk:SOUrce value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:SETHold:CLOCk:SOUrce {CH<x>|D<x>}
            - TRIGger:A:SETHold:CLOCk:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies the input channel number. x has a minimum of 1 and a maximum of 4.
            - ``D<x>`` specifies the input digital channel number. x has a minimum of 0 and a
              maximum of 15.
        """
        return self._source

    @property
    def threshold(self) -> TriggerASetholdClockThreshold:
        """Return the ``TRIGger:A:SETHold:CLOCk:THReshold`` command.

        Description:
            - Sets or returns the clock voltage threshold for the setup and hold trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:CLOCk:THReshold?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:SETHold:CLOCk:THReshold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:SETHold:CLOCk:THReshold value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:SETHold:CLOCk:THReshold {<NR3>|TTL|ECL}
            - TRIGger:A:SETHold:CLOCk:THReshold?
            ```

        Info:
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
            - ``ECL`` specifies a preset ECL high level of -1.3 V.
            - ``<NR3>`` is the clock level, in volts.
        """
        return self._threshold


class TriggerASethold(SCPICmdRead):
    """The ``TRIGger:A:SETHold`` command.

    Description:
        - Returns the clock edge polarity, voltage threshold and source input; data voltage
          threshold and source; and both setup and hold times for setup and hold violation
          triggering.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:SETHold?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TRIGger:A:SETHold?
        ```

    Properties:
        - ``.clock``: The ``TRIGger:A:SETHold:CLOCk`` command.
        - ``.data``: The ``TRIGger:A:SETHold:DATa`` command.
        - ``.holdtime``: The ``TRIGger:A:SETHold:HOLDTime`` command.
        - ``.settime``: The ``TRIGger:A:SETHold:SETTime`` command.
        - ``.threshold``: The ``TRIGger:A:SETHold:THReshold`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._clock = TriggerASetholdClock(device, f"{self._cmd_syntax}:CLOCk")
        self._data = TriggerASetholdData(device, f"{self._cmd_syntax}:DATa")
        self._holdtime = TriggerASetholdHoldtime(device, f"{self._cmd_syntax}:HOLDTime")
        self._settime = TriggerASetholdSettime(device, f"{self._cmd_syntax}:SETTime")
        self._threshold = TriggerASetholdThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def clock(self) -> TriggerASetholdClock:
        """Return the ``TRIGger:A:SETHold:CLOCk`` command.

        Description:
            - Returns the clock edge polarity, voltage threshold, and source input for setup and
              hold triggering.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:CLOCk?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TRIGger:A:SETHold:CLOCk?
            ```

        Sub-properties:
            - ``.edge``: The ``TRIGger:A:SETHold:CLOCk:EDGE`` command.
            - ``.source``: The ``TRIGger:A:SETHold:CLOCk:SOUrce`` command.
            - ``.threshold``: The ``TRIGger:A:SETHold:CLOCk:THReshold`` command.
        """
        return self._clock

    @property
    def data(self) -> TriggerASetholdData:
        """Return the ``TRIGger:A:SETHold:DATa`` command.

        Description:
            - Returns the voltage threshold and data source for the setup and hold trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:DATa?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TRIGger:A:SETHold:DATa?
            ```

        Sub-properties:
            - ``.source``: The ``TRIGger:A:SETHold:DATa:SOUrce`` command.
            - ``.threshold``: The ``TRIGger:A:SETHold:DATa:THReshold`` command.
        """
        return self._data

    @property
    def holdtime(self) -> TriggerASetholdHoldtime:
        """Return the ``TRIGger:A:SETHold:HOLDTime`` command.

        Description:
            - This command specifies the hold time for setup and hold violation triggering. This
              command is equivalent to selecting Setup/Hold Setup from the Trig menu and then
              setting the desired Hold Time.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:HOLDTime?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:HOLDTime?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:SETHold:HOLDTime value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:SETHold:HOLDTime <NR3>
            - TRIGger:A:SETHold:HOLDTime?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the hold time setting, in seconds.
              Positive values for hold time occur after the clock edge. Negative values occur before
              the clock edge.
        """
        return self._holdtime

    @property
    def settime(self) -> TriggerASetholdSettime:
        """Return the ``TRIGger:A:SETHold:SETTime`` command.

        Description:
            - This command specifies the setup time for setup and hold violation triggering. This
              command is equivalent to selecting Setup/Hold Setup from the Trig menu and then
              setting the desired Setup Time.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:SETTime?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:SETTime?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:SETHold:SETTime value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:SETHold:SETTime <NR3>
            - TRIGger:A:SETHold:SETTime?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the setup time for setup and hold
              violation triggering.
        """
        return self._settime

    @property
    def threshold(self) -> TriggerASetholdThreshold:
        """Return the ``TRIGger:A:SETHold:THReshold`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``TRIGger:A:SETHold:THReshold:CH<x>`` command.
            - ``.d``: The ``TRIGger:A:SETHold:THReshold:D<x>`` command.
        """
        return self._threshold


class TriggerARuntWidth(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:RUNT:WIDth`` command.

    Description:
        - This command specifies the width, in seconds, for a runt trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:RUNT:WIDth?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:RUNT:WIDth?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:RUNT:WIDth value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:RUNT:WIDth <NR3>
        - TRIGger:A:RUNT:WIDth?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the minimum width, in seconds.
    """


class TriggerARuntWhen(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:RUNT:WHEn`` command.

    Description:
        - This command specifies the type of pulse width the trigger checks for when it detects a
          runt.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:RUNT:WHEn?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:RUNT:WHEn?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:RUNT:WHEn value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:RUNT:WHEn {LESSthan|MOREthan|EQual|UNEQual|OCCURS}
        - TRIGger:A:RUNT:WHEn?
        ```

    Info:
        - ``OCCURS`` sets the instrument to trigger if a runt signal of any detectable width occurs.
        - ``LESSthan`` sets the instrument to trigger if the a runt pulse is detected with width
          less than the time set by the ``TRIGGER:A:RUNT:WIDTH`` command.
        - ``MOREthan`` sets the instrument to trigger if the a runt pulse is detected with width
          greater than the time set by the ``TRIGGER:A:RUNT:WIDTH`` command.
        - ``EQual`` sets the instrument to trigger if a runt pulse is detected with width equal to
          the time period specified in ``TRIGGER:A:RUNT:WIDTH`` within a ±5% tolerance.
        - ``UNEQual`` sets the instrument to trigger if a runt pulse is detected with width greater
          than or less than (but not equal to) the time period specified in ``TRIGGER:A:RUNT:WIDTH``
          within a ±5% tolerance.
    """


class TriggerARuntSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:RUNT:SOUrce`` command.

    Description:
        - This command specifies the source waveform for the runt trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:RUNT:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:RUNT:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:RUNT:SOUrce value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:RUNT:SOUrce {CH<x>}
        - TRIGger:A:RUNT:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies the analog channel number to use as the source waveform for the runt
          trigger. To specify the threshold levels when using CH<x> as the source, use
          ``TRIGGER:A:LOWERTHRESHOLD:CHX`` and ``TRIGGER:A:UPPERTHRESHOLD:CHX``.
    """


class TriggerARuntPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:RUNT:POLarity`` command.

    Description:
        - This command specifies the polarity for the runt trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:RUNT:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:RUNT:POLarity?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:RUNT:POLarity value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:RUNT:POLarity {EITher|NEGative|POSitive}
        - TRIGger:A:RUNT:POLarity?
        ```

    Info:
        - ``POSitive`` indicates that the rising edge crosses the low threshold and the falling edge
          recrosses the low threshold without either edge ever crossing the high threshold.
        - ``NEGative`` indicates that the falling edge crosses the high threshold and the rising
          edge recrosses the high threshold without either edge ever crossing the low threshold.
        - ``EITher`` triggers on a runt of either polarity.
    """


class TriggerARunt(SCPICmdRead):
    """The ``TRIGger:A:RUNT`` command.

    Description:
        - Returns the current A runt trigger parameters.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:RUNT?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:RUNT?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TRIGger:A:RUNT?
        ```

    Properties:
        - ``.polarity``: The ``TRIGger:A:RUNT:POLarity`` command.
        - ``.source``: The ``TRIGger:A:RUNT:SOUrce`` command.
        - ``.when``: The ``TRIGger:A:RUNT:WHEn`` command.
        - ``.width``: The ``TRIGger:A:RUNT:WIDth`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = TriggerARuntPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = TriggerARuntSource(device, f"{self._cmd_syntax}:SOUrce")
        self._when = TriggerARuntWhen(device, f"{self._cmd_syntax}:WHEn")
        self._width = TriggerARuntWidth(device, f"{self._cmd_syntax}:WIDth")

    @property
    def polarity(self) -> TriggerARuntPolarity:
        """Return the ``TRIGger:A:RUNT:POLarity`` command.

        Description:
            - This command specifies the polarity for the runt trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:RUNT:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:RUNT:POLarity?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:RUNT:POLarity value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:RUNT:POLarity {EITher|NEGative|POSitive}
            - TRIGger:A:RUNT:POLarity?
            ```

        Info:
            - ``POSitive`` indicates that the rising edge crosses the low threshold and the falling
              edge recrosses the low threshold without either edge ever crossing the high threshold.
            - ``NEGative`` indicates that the falling edge crosses the high threshold and the rising
              edge recrosses the high threshold without either edge ever crossing the low threshold.
            - ``EITher`` triggers on a runt of either polarity.
        """
        return self._polarity

    @property
    def source(self) -> TriggerARuntSource:
        """Return the ``TRIGger:A:RUNT:SOUrce`` command.

        Description:
            - This command specifies the source waveform for the runt trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:RUNT:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:RUNT:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:RUNT:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:RUNT:SOUrce {CH<x>}
            - TRIGger:A:RUNT:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies the analog channel number to use as the source waveform for the
              runt trigger. To specify the threshold levels when using CH<x> as the source, use
              ``TRIGGER:A:LOWERTHRESHOLD:CHX`` and ``TRIGGER:A:UPPERTHRESHOLD:CHX``.
        """
        return self._source

    @property
    def when(self) -> TriggerARuntWhen:
        """Return the ``TRIGger:A:RUNT:WHEn`` command.

        Description:
            - This command specifies the type of pulse width the trigger checks for when it detects
              a runt.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:RUNT:WHEn?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:RUNT:WHEn?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:RUNT:WHEn value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:RUNT:WHEn {LESSthan|MOREthan|EQual|UNEQual|OCCURS}
            - TRIGger:A:RUNT:WHEn?
            ```

        Info:
            - ``OCCURS`` sets the instrument to trigger if a runt signal of any detectable width
              occurs.
            - ``LESSthan`` sets the instrument to trigger if the a runt pulse is detected with width
              less than the time set by the ``TRIGGER:A:RUNT:WIDTH`` command.
            - ``MOREthan`` sets the instrument to trigger if the a runt pulse is detected with width
              greater than the time set by the ``TRIGGER:A:RUNT:WIDTH`` command.
            - ``EQual`` sets the instrument to trigger if a runt pulse is detected with width equal
              to the time period specified in ``TRIGGER:A:RUNT:WIDTH`` within a ±5% tolerance.
            - ``UNEQual`` sets the instrument to trigger if a runt pulse is detected with width
              greater than or less than (but not equal to) the time period specified in
              ``TRIGGER:A:RUNT:WIDTH`` within a ±5% tolerance.
        """
        return self._when

    @property
    def width(self) -> TriggerARuntWidth:
        """Return the ``TRIGger:A:RUNT:WIDth`` command.

        Description:
            - This command specifies the width, in seconds, for a runt trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:RUNT:WIDth?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:RUNT:WIDth?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:RUNT:WIDth value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:RUNT:WIDth <NR3>
            - TRIGger:A:RUNT:WIDth?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the minimum width, in seconds.
        """
        return self._width


class TriggerARisefallWhen(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:RISEFall:WHEn`` command.

    Description:
        - This command specifies whether to check for a transitioning signal that is faster or
          slower than the specified delta time.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:RISEFall:WHEn?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:RISEFall:WHEn?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:RISEFall:WHEn value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:RISEFall:WHEn {SLOWer|FASTer|EQual|UNEQual}
        - TRIGger:A:RISEFall:WHEn?
        ```

    Info:
        - ``FASTer`` sets the trigger to occur when the signal transition time is faster than the
          time set by ``TRIGger:A:TRANsition:DELTatime``.
        - ``SLOWer`` sets the trigger to occur when the signal transition time is slower than the
          time set by.``TRIGger:A:TRANsition:DELTatime``.
        - ``EQual`` sets the trigger to occur when the signal transition time is equal to the time
          set by ``TRIGger:A:TRANsition:DELTatime``.
        - ``UNEQual`` sets the trigger to occur when the signal transition time is not equal to the
          time set by ``TRIGger:A:TRANsition:DELTatime``.
    """


class TriggerARisefallSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:RISEFall:SOUrce`` command.

    Description:
        - Sets or returns the source for transition trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:RISEFall:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:RISEFall:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:RISEFall:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:RISEFall:SOUrce {CH<x>|D<x>}
        - TRIGger:A:RISEFall:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies one of the input channels. x has a minimum of 1 and a maximum of 4.
        - ``D<x>`` specifies one of the input digital channels. x has a minimum of 0 and a maximum
          of 15.
    """


class TriggerARisefallPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:RISEFall:POLarity`` command.

    Description:
        - This command specifies the polarity for the transition trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:RISEFall:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:RISEFall:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:RISEFall:POLarity value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:RISEFall:POLarity {EITher|NEGative|POSitive}
        - TRIGger:A:RISEFall:POLarity?
        ```

    Info:
        - ``POSitive`` indicates that a pulse edge must traverse from the lower (most negative) to
          higher (most positive) level for transition triggering to occur.
        - ``NEGative`` indicates that a pulse edge must traverse from the upper (most positive) to
          lower (most negative) level for transition triggering to occur.
        - ``EITher`` indicates either positive or negative polarity.
    """


class TriggerARisefallDeltatime(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:RISEFall:DELTatime`` command.

    Description:
        - This command specifies the delta time used in calculating the transition value for the
          transition trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:RISEFall:DELTatime?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:RISEFall:DELTatime?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:RISEFall:DELTatime value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:RISEFall:DELTatime <NR3>
        - TRIGger:A:RISEFall:DELTatime?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the delta time, in seconds.
    """


class TriggerARisefall(SCPICmdRead):
    """The ``TRIGger:A:RISEFall`` command.

    Description:
        - Returns transition time trigger parameters.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:RISEFall?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:RISEFall?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TRIGger:A:RISEFall?
        ```

    Properties:
        - ``.deltatime``: The ``TRIGger:A:RISEFall:DELTatime`` command.
        - ``.polarity``: The ``TRIGger:A:RISEFall:POLarity`` command.
        - ``.source``: The ``TRIGger:A:RISEFall:SOUrce`` command.
        - ``.when``: The ``TRIGger:A:RISEFall:WHEn`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._deltatime = TriggerARisefallDeltatime(device, f"{self._cmd_syntax}:DELTatime")
        self._polarity = TriggerARisefallPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = TriggerARisefallSource(device, f"{self._cmd_syntax}:SOUrce")
        self._when = TriggerARisefallWhen(device, f"{self._cmd_syntax}:WHEn")

    @property
    def deltatime(self) -> TriggerARisefallDeltatime:
        """Return the ``TRIGger:A:RISEFall:DELTatime`` command.

        Description:
            - This command specifies the delta time used in calculating the transition value for the
              transition trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:RISEFall:DELTatime?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:RISEFall:DELTatime?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:RISEFall:DELTatime value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:RISEFall:DELTatime <NR3>
            - TRIGger:A:RISEFall:DELTatime?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the delta time, in seconds.
        """
        return self._deltatime

    @property
    def polarity(self) -> TriggerARisefallPolarity:
        """Return the ``TRIGger:A:RISEFall:POLarity`` command.

        Description:
            - This command specifies the polarity for the transition trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:RISEFall:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:RISEFall:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:RISEFall:POLarity value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:RISEFall:POLarity {EITher|NEGative|POSitive}
            - TRIGger:A:RISEFall:POLarity?
            ```

        Info:
            - ``POSitive`` indicates that a pulse edge must traverse from the lower (most negative)
              to higher (most positive) level for transition triggering to occur.
            - ``NEGative`` indicates that a pulse edge must traverse from the upper (most positive)
              to lower (most negative) level for transition triggering to occur.
            - ``EITher`` indicates either positive or negative polarity.
        """
        return self._polarity

    @property
    def source(self) -> TriggerARisefallSource:
        """Return the ``TRIGger:A:RISEFall:SOUrce`` command.

        Description:
            - Sets or returns the source for transition trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:RISEFall:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:RISEFall:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:RISEFall:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:RISEFall:SOUrce {CH<x>|D<x>}
            - TRIGger:A:RISEFall:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies one of the input channels. x has a minimum of 1 and a maximum of
              4.
            - ``D<x>`` specifies one of the input digital channels. x has a minimum of 0 and a
              maximum of 15.
        """
        return self._source

    @property
    def when(self) -> TriggerARisefallWhen:
        """Return the ``TRIGger:A:RISEFall:WHEn`` command.

        Description:
            - This command specifies whether to check for a transitioning signal that is faster or
              slower than the specified delta time.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:RISEFall:WHEn?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:RISEFall:WHEn?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:RISEFall:WHEn value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:RISEFall:WHEn {SLOWer|FASTer|EQual|UNEQual}
            - TRIGger:A:RISEFall:WHEn?
            ```

        Info:
            - ``FASTer`` sets the trigger to occur when the signal transition time is faster than
              the time set by ``TRIGger:A:TRANsition:DELTatime``.
            - ``SLOWer`` sets the trigger to occur when the signal transition time is slower than
              the time set by.``TRIGger:A:TRANsition:DELTatime``.
            - ``EQual`` sets the trigger to occur when the signal transition time is equal to the
              time set by ``TRIGger:A:TRANsition:DELTatime``.
            - ``UNEQual`` sets the trigger to occur when the signal transition time is not equal to
              the time set by ``TRIGger:A:TRANsition:DELTatime``.
        """
        return self._when


class TriggerAPulseClass(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:PULse:CLAss`` command.

    Description:
        - Sets or returns the type of pulse on which to trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:PULse:CLAss?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULse:CLAss?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:PULse:CLAss value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:PULse:CLAss {RUNt|WIDth|TRANsition}
        - TRIGger:A:PULse:CLAss?
        ```

    Info:
        - ``RUNt`` triggers when a pulse crosses the first preset voltage threshold but does not
          cross the second preset threshold before recrossing the first.
        - ``WIDth`` triggers when a pulse is found that has the specified polarity and is either
          inside or outside the specified time limits.
        - ``TRAnsition`` triggers when a pulse crosses both thresholds in the same direction as the
          specified polarity and the transition time between the two threshold crossings is greater
          or less than the specified time delta.
    """


class TriggerAPulse(SCPICmdRead):
    """The ``TRIGger:A:PULse`` command.

    Description:
        - Returns the A pulse trigger parameters.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:PULse?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULse?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TRIGger:A:PULse?
        ```

    Properties:
        - ``.class``: The ``TRIGger:A:PULse:CLAss`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._class = TriggerAPulseClass(device, f"{self._cmd_syntax}:CLAss")

    @property
    def class_(self) -> TriggerAPulseClass:
        """Return the ``TRIGger:A:PULse:CLAss`` command.

        Description:
            - Sets or returns the type of pulse on which to trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:PULse:CLAss?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULse:CLAss?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:PULse:CLAss value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:PULse:CLAss {RUNt|WIDth|TRANsition}
            - TRIGger:A:PULse:CLAss?
            ```

        Info:
            - ``RUNt`` triggers when a pulse crosses the first preset voltage threshold but does not
              cross the second preset threshold before recrossing the first.
            - ``WIDth`` triggers when a pulse is found that has the specified polarity and is either
              inside or outside the specified time limits.
            - ``TRAnsition`` triggers when a pulse crosses both thresholds in the same direction as
              the specified polarity and the transition time between the two threshold crossings is
              greater or less than the specified time delta.
        """
        return self._class


class TriggerAPulsewidthWidth(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:PULSEWidth:Width`` command.

    Description:
        - Sets or returns the width setting for the pulse width trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:Width?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:Width?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:PULSEWidth:Width value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:PULSEWidth:Width <NR3>
        - TRIGger:A:PULSEWidth:Width?
        ```

    Info:
        - ``<NR3>`` specifies the pulse width in seconds.
    """


class TriggerAPulsewidthWhen(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:PULSEWidth:WHEn`` command.

    Description:
        - Sets or returns whether to trigger on a pulse that meets, falls outside, or within the
          specified range of limits.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:WHEn?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:WHEn?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:PULSEWidth:WHEn value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:PULSEWidth:WHEn {LESSthan|MOREthan|EQual|UNEQual}
        - TRIGger:A:PULSEWidth:WHEn?
        ```

    Info:
        - ``LESSthan`` argument sets the oscilloscope to trigger if a pulse is detected with width
          less than the time set by the ``TRIGGER:A:PULSEWIDTH:WIDTH`` command.
        - ``MOREthan`` argument sets the oscilloscope to trigger if a pulse is detected with width
          more than the time set by the ``TRIGGER:A:PULSEWIDTH:WIDTH`` command.
        - ``EQUal`` argument sets the oscilloscope to trigger if a pulse is detected with width
          equal to the time period specified in ``TRIGGER:A:PULSEWIDTH:WIDTH`` within a ±5%
          tolerance.
        - ``UNEQual`` argument sets the oscilloscope to trigger if a pulse is detected with width
          greater than or less than (but not equal) the time period specified in
          ``TRIGGER:A:PULSEWIDTH:WIDTH`` within a ±5% tolerance.
    """


class TriggerAPulsewidthSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:PULSEWidth:SOUrce`` command.

    Description:
        - Sets or returns the source for the pulse-width trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:PULSEWidth:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:PULSEWidth:SOUrce {CH<x>|D<x>|LINE|EXT}
        - TRIGger:A:PULSEWidth:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog input channel as the A edge trigger source. x has a minimum
          of 1 and a maximum of 4.
        - ``D<x>`` specifies an digital input channel as the A edge trigger source. x has a minimum
          of 0 and a maximum of 15.
        - ``EXT`` specifies an external trigger using the Aux In connector located on the front
          panel of the oscilloscope.
        - ``LINE`` specifies AC line voltage.
    """


class TriggerAPulsewidthPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:PULSEWidth:POLarity`` command.

    Description:
        - This command specifies the polarity for a pulse width trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:PULSEWidth:POLarity value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:PULSEWidth:POLarity {NEGative|POSitive}
        - TRIGger:A:PULSEWidth:POLarity?
        ```

    Info:
        - ``NEGative`` specifies a negative pulse.
        - ``POSitive`` specifies a positive pulse.
    """


class TriggerAPulsewidth(SCPICmdRead):
    """The ``TRIGger:A:PULSEWidth`` command.

    Description:
        - Returns the width parameters for the pulse width trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TRIGger:A:PULSEWidth?
        ```

    Properties:
        - ``.polarity``: The ``TRIGger:A:PULSEWidth:POLarity`` command.
        - ``.source``: The ``TRIGger:A:PULSEWidth:SOUrce`` command.
        - ``.when``: The ``TRIGger:A:PULSEWidth:WHEn`` command.
        - ``.width``: The ``TRIGger:A:PULSEWidth:Width`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = TriggerAPulsewidthPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = TriggerAPulsewidthSource(device, f"{self._cmd_syntax}:SOUrce")
        self._when = TriggerAPulsewidthWhen(device, f"{self._cmd_syntax}:WHEn")
        self._width = TriggerAPulsewidthWidth(device, f"{self._cmd_syntax}:Width")

    @property
    def polarity(self) -> TriggerAPulsewidthPolarity:
        """Return the ``TRIGger:A:PULSEWidth:POLarity`` command.

        Description:
            - This command specifies the polarity for a pulse width trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:PULSEWidth:POLarity value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:PULSEWidth:POLarity {NEGative|POSitive}
            - TRIGger:A:PULSEWidth:POLarity?
            ```

        Info:
            - ``NEGative`` specifies a negative pulse.
            - ``POSitive`` specifies a positive pulse.
        """
        return self._polarity

    @property
    def source(self) -> TriggerAPulsewidthSource:
        """Return the ``TRIGger:A:PULSEWidth:SOUrce`` command.

        Description:
            - Sets or returns the source for the pulse-width trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:PULSEWidth:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:PULSEWidth:SOUrce {CH<x>|D<x>|LINE|EXT}
            - TRIGger:A:PULSEWidth:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog input channel as the A edge trigger source. x has a
              minimum of 1 and a maximum of 4.
            - ``D<x>`` specifies an digital input channel as the A edge trigger source. x has a
              minimum of 0 and a maximum of 15.
            - ``EXT`` specifies an external trigger using the Aux In connector located on the front
              panel of the oscilloscope.
            - ``LINE`` specifies AC line voltage.
        """
        return self._source

    @property
    def when(self) -> TriggerAPulsewidthWhen:
        """Return the ``TRIGger:A:PULSEWidth:WHEn`` command.

        Description:
            - Sets or returns whether to trigger on a pulse that meets, falls outside, or within the
              specified range of limits.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:WHEn?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:WHEn?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:PULSEWidth:WHEn value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:PULSEWidth:WHEn {LESSthan|MOREthan|EQual|UNEQual}
            - TRIGger:A:PULSEWidth:WHEn?
            ```

        Info:
            - ``LESSthan`` argument sets the oscilloscope to trigger if a pulse is detected with
              width less than the time set by the ``TRIGGER:A:PULSEWIDTH:WIDTH`` command.
            - ``MOREthan`` argument sets the oscilloscope to trigger if a pulse is detected with
              width more than the time set by the ``TRIGGER:A:PULSEWIDTH:WIDTH`` command.
            - ``EQUal`` argument sets the oscilloscope to trigger if a pulse is detected with width
              equal to the time period specified in ``TRIGGER:A:PULSEWIDTH:WIDTH`` within a ±5%
              tolerance.
            - ``UNEQual`` argument sets the oscilloscope to trigger if a pulse is detected with
              width greater than or less than (but not equal) the time period specified in
              ``TRIGGER:A:PULSEWIDTH:WIDTH`` within a ±5% tolerance.
        """
        return self._when

    @property
    def width(self) -> TriggerAPulsewidthWidth:
        """Return the ``TRIGger:A:PULSEWidth:Width`` command.

        Description:
            - Sets or returns the width setting for the pulse width trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:Width?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:Width?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:PULSEWidth:Width value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:PULSEWidth:Width <NR3>
            - TRIGger:A:PULSEWidth:Width?
            ```

        Info:
            - ``<NR3>`` specifies the pulse width in seconds.
        """
        return self._width


class TriggerAMode(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:MODe`` command.

    Description:
        - This command sets or queries the A trigger mode. This command is equivalent to pushing the
          Mode button on the front panel.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:MODe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:MODe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:MODe {AUTO|NORMal}
        - TRIGger:A:MODe?
        ```

    Info:
        - ``AUTO`` generates a trigger if one is not detected within a specified time period.
        - ``NORMal`` waits for a valid trigger event.
    """


class TriggerALowerthresholdExt(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOWerthreshold:EXT`` command.

    Description:
        - Sets or returns the lower threshold for the Auxiliary Input. It is similar to
          ``TRIGGER:A:LEVEL:AUXIN``.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOWerthreshold:EXT?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOWerthreshold:EXT?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LOWerthreshold:EXT value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOWerthreshold:EXT {<NR3>|ECL|TTL}
        - TRIGger:A:LOWerthreshold:EXT?
        ```

    Info:
        - ``ECL`` specifies a preset ECL high level of -1.3 V.
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
        - ``<NR3>`` specifies the threshold level in volts.
    """


class TriggerALowerthresholdChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOWerthreshold:CH<x>`` command.

    Description:
        - This command specifies the lower threshold for the channel selected. Each channel can have
          an independent level. Used in runt and transition triggers as the lower threshold. Used
          for all other trigger types as the single level/threshold.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOWerthreshold:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOWerthreshold:CH<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LOWerthreshold:CH<x> value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOWerthreshold:CH<x> {ECL|TTL|<NR3>}
        - TRIGger:A:LOWerthreshold:CH<x>?
        ```

    Info:
        - ``ECL`` specifies a preset ECL high level of -1.3V.
        - ``TTL`` specifies a preset TTL high level of 1.4V.
        - ``<NR3>`` is a floating point number that specifies the clock level, in volts.
    """


class TriggerALowerthresholdAux(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOWerthreshold:AUX`` command.

    Description:
        - Sets or returns the lower threshold for the Auxiliary Input. It is similar to
          ``TRIGGER:A:LEVEL:AUXIN``.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOWerthreshold:AUX?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOWerthreshold:AUX?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LOWerthreshold:AUX value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOWerthreshold:AUX {<NR3>|ECL|TTL}
        - TRIGger:A:LOWerthreshold:AUX?
        ```

    Info:
        - ``ECL`` specifies a preset ECL high level of -1.3 V.
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
        - ``<NR3>`` specifies the threshold level in volts.
    """


class TriggerALowerthreshold(SCPICmdRead):
    """The ``TRIGger:A:LOWerthreshold`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOWerthreshold?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOWerthreshold?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``TRIGger:A:LOWerthreshold:CH<x>`` command.
        - ``.ext``: The ``TRIGger:A:LOWerthreshold:EXT`` command.
        - ``.aux``: The ``TRIGger:A:LOWerthreshold:AUX`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, TriggerALowerthresholdChannel] = DefaultDictPassKeyToFactory(
            lambda x: TriggerALowerthresholdChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._ext = TriggerALowerthresholdExt(device, f"{self._cmd_syntax}:EXT")
        self._aux = TriggerALowerthresholdAux(device, f"{self._cmd_syntax}:AUX")

    @property
    def ch(self) -> Dict[int, TriggerALowerthresholdChannel]:
        """Return the ``TRIGger:A:LOWerthreshold:CH<x>`` command.

        Description:
            - This command specifies the lower threshold for the channel selected. Each channel can
              have an independent level. Used in runt and transition triggers as the lower
              threshold. Used for all other trigger types as the single level/threshold.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOWerthreshold:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOWerthreshold:CH<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:LOWerthreshold:CH<x> value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOWerthreshold:CH<x> {ECL|TTL|<NR3>}
            - TRIGger:A:LOWerthreshold:CH<x>?
            ```

        Info:
            - ``ECL`` specifies a preset ECL high level of -1.3V.
            - ``TTL`` specifies a preset TTL high level of 1.4V.
            - ``<NR3>`` is a floating point number that specifies the clock level, in volts.
        """
        return self._ch

    @property
    def ext(self) -> TriggerALowerthresholdExt:
        """Return the ``TRIGger:A:LOWerthreshold:EXT`` command.

        Description:
            - Sets or returns the lower threshold for the Auxiliary Input. It is similar to
              ``TRIGGER:A:LEVEL:AUXIN``.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOWerthreshold:EXT?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOWerthreshold:EXT?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:LOWerthreshold:EXT value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOWerthreshold:EXT {<NR3>|ECL|TTL}
            - TRIGger:A:LOWerthreshold:EXT?
            ```

        Info:
            - ``ECL`` specifies a preset ECL high level of -1.3 V.
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
            - ``<NR3>`` specifies the threshold level in volts.
        """
        return self._ext

    @property
    def aux(self) -> TriggerALowerthresholdAux:
        """Return the ``TRIGger:A:LOWerthreshold:AUX`` command.

        Description:
            - Sets or returns the lower threshold for the Auxiliary Input. It is similar to
              ``TRIGGER:A:LEVEL:AUXIN``.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOWerthreshold:AUX?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOWerthreshold:AUX?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:LOWerthreshold:AUX value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOWerthreshold:AUX {<NR3>|ECL|TTL}
            - TRIGger:A:LOWerthreshold:AUX?
            ```

        Info:
            - ``ECL`` specifies a preset ECL high level of -1.3 V.
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
            - ``<NR3>`` specifies the threshold level in volts.
        """
        return self._aux


class TriggerALogicThresholdDigitalBit(ValidatedDigitalBit, SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOGIc:THReshold:D<x>`` command.

    Description:
        - This command specifies the trigger A logic threshold level for the specified digital
          channel <x>. This commands affects all trigger types using the digital channel.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:THReshold:D<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:THReshold:D<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGIc:THReshold:D<x> value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc:THReshold:D<x> {<NR3>|ECL|TTL}
        - TRIGger:A:LOGIc:THReshold:D<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the threshold level in volts.
        - ``ECL`` specifies a preset ECL high level of -1.3V.
        - ``TTL`` specifies a preset TTL high level of 1.4V.
    """


class TriggerALogicThresholdChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOGIc:THReshold:CH<x>`` command.

    Description:
        - This command sets or queries the logic trigger threshold voltage for both analog and
          digital channels (for MSO models), specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:THReshold:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:THReshold:CH<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGIc:THReshold:CH<x> value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc:THReshold:CH<x> {<NR3>|ECL|TTL}
        - TRIGger:A:LOGIc:THReshold:CH<x>?
        ```

    Info:
        - ``<NR3>`` specifies the threshold voltage, in volts.
        - ``ECL`` specifies a preset ECL high level of -1.3 V.
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
    """


class TriggerALogicThreshold(SCPICmdRead):
    """The ``TRIGger:A:LOGIc:THReshold`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:THReshold?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.d``: The ``TRIGger:A:LOGIc:THReshold:D<x>`` command.
        - ``.ch``: The ``TRIGger:A:LOGIc:THReshold:CH<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, TriggerALogicThresholdChannel] = DefaultDictPassKeyToFactory(
            lambda x: TriggerALogicThresholdChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._d: Dict[int, TriggerALogicThresholdDigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: TriggerALogicThresholdDigitalBit(device, f"{self._cmd_syntax}:D{x}")
        )

    @property
    def ch(self) -> Dict[int, TriggerALogicThresholdChannel]:
        """Return the ``TRIGger:A:LOGIc:THReshold:CH<x>`` command.

        Description:
            - This command sets or queries the logic trigger threshold voltage for both analog and
              digital channels (for MSO models), specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:THReshold:CH<x>?``
              query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:THReshold:CH<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:LOGIc:THReshold:CH<x> value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGIc:THReshold:CH<x> {<NR3>|ECL|TTL}
            - TRIGger:A:LOGIc:THReshold:CH<x>?
            ```

        Info:
            - ``<NR3>`` specifies the threshold voltage, in volts.
            - ``ECL`` specifies a preset ECL high level of -1.3 V.
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
        """
        return self._ch

    @property
    def d(self) -> Dict[int, TriggerALogicThresholdDigitalBit]:
        """Return the ``TRIGger:A:LOGIc:THReshold:D<x>`` command.

        Description:
            - This command specifies the trigger A logic threshold level for the specified digital
              channel <x>. This commands affects all trigger types using the digital channel.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:THReshold:D<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:THReshold:D<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:LOGIc:THReshold:D<x> value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGIc:THReshold:D<x> {<NR3>|ECL|TTL}
            - TRIGger:A:LOGIc:THReshold:D<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the threshold level in volts.
            - ``ECL`` specifies a preset ECL high level of -1.3V.
            - ``TTL`` specifies a preset TTL high level of 1.4V.
        """
        return self._d


class TriggerALogicPatternWhenMorelimit(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOGIc:PATtern:WHEn:MORELimit`` command.

    Description:
        - Sets or returns the minimum time that the selected pattern may be true and still generate
          an A logic pattern trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:PATtern:WHEn:MORELimit?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:LOGIc:PATtern:WHEn:MORELimit?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:LOGIc:PATtern:WHEn:MORELimit value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc:PATtern:WHEn:MORELimit <NR3>
        - TRIGger:A:LOGIc:PATtern:WHEn:MORELimit?
        ```

    Info:
        - ``<NR3>`` specifies the minimum amount of time to hold the pattern true.
    """


class TriggerALogicPatternWhenLesslimit(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit`` command.

    Description:
        - Sets or returns the maximum time that the selected pattern may be true and still generate
          an A logic pattern trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit <NR3>
        - TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit?
        ```

    Info:
        - ``<NR3>`` specifies the maximum amount of time to hold the pattern true.
    """


class TriggerALogicPatternWhen(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOGIc:PATtern:WHEn`` command.

    Description:
        - Sets or returns the pattern logic condition on which to trigger the oscilloscope.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:PATtern:WHEn?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:PATtern:WHEn?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGIc:PATtern:WHEn value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc:PATtern:WHEn {TRUe|FALSe|LESSThan|MOREThan|EQUal|UNEQual}
        - TRIGger:A:LOGIc:PATtern:WHEn?
        ```

    Info:
        - ``TRUE`` triggers the oscilloscope when the pattern becomes true.
        - ``FALSE`` triggers the oscilloscope when the pattern becomes false.
        - ``LESSTHAN`` triggers the oscilloscope when the input pattern is true for a time period
          less than the time period specified in ``TRIGGER:A:LOGIC:PATTERN:DELTATIME``.
        - ``MORETHAN`` triggers the oscilloscope when the input pattern is true for a time period
          more (greater) than the time period specified in ``TRIGGER:A:LOGIC:PATTERN:DELTATIME``.
        - ``EQUAL`` triggers the oscilloscope when the input pattern is true for a time period equal
          to the time period specified in ``TRIGGER:A:LOGIC:PATTERN:DELTATIME``, within a ±5%
          tolerance.
        - ``UNEQUAL`` triggers the oscilloscope when the input pattern is true for a time period
          greater than or less than (not equal to) the time period specified in
          ``TRIGGER:A:LOGIC:PATTERN:DELTATIME``, within a ±5% tolerance.

    Properties:
        - ``.lesslimit``: The ``TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit`` command.
        - ``.morelimit``: The ``TRIGger:A:LOGIc:PATtern:WHEn:MORELimit`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._lesslimit = TriggerALogicPatternWhenLesslimit(device, f"{self._cmd_syntax}:LESSLimit")
        self._morelimit = TriggerALogicPatternWhenMorelimit(device, f"{self._cmd_syntax}:MORELimit")

    @property
    def lesslimit(self) -> TriggerALogicPatternWhenLesslimit:
        """Return the ``TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit`` command.

        Description:
            - Sets or returns the maximum time that the selected pattern may be true and still
              generate an A logic pattern trigger.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit <NR3>
            - TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit?
            ```

        Info:
            - ``<NR3>`` specifies the maximum amount of time to hold the pattern true.
        """
        return self._lesslimit

    @property
    def morelimit(self) -> TriggerALogicPatternWhenMorelimit:
        """Return the ``TRIGger:A:LOGIc:PATtern:WHEn:MORELimit`` command.

        Description:
            - Sets or returns the minimum time that the selected pattern may be true and still
              generate an A logic pattern trigger.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:LOGIc:PATtern:WHEn:MORELimit?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:LOGIc:PATtern:WHEn:MORELimit?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:LOGIc:PATtern:WHEn:MORELimit value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGIc:PATtern:WHEn:MORELimit <NR3>
            - TRIGger:A:LOGIc:PATtern:WHEn:MORELimit?
            ```

        Info:
            - ``<NR3>`` specifies the minimum amount of time to hold the pattern true.
        """
        return self._morelimit


class TriggerALogicPatternInputDigitalBit(ValidatedDigitalBit, SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOGIc:PATtern:INPut:D<x>`` command.

    Description:
        - Sets or returns the A logic trigger input for the specified digital channel <x>, where x
          is the channel number. This command species the logic value used when the pattern trigger
          detects the threshold level.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:PATtern:INPut:D<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:PATtern:INPut:D<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:LOGIc:PATtern:INPut:D<x> value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc:PATtern:INPut:D<x> {HIGH|LOW|X}
        - TRIGger:A:LOGIc:PATtern:INPut:D<x>?
        ```

    Info:
        - ``HIGH`` specifies a logic high.
        - ``LOW`` specifies a logic low.
        - ``X`` specifies a 'do not care' state.
    """


class TriggerALogicPatternInput(SCPICmdRead):
    """The ``TRIGger:A:LOGIc:PATtern:INPut`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:PATtern:INPut?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:PATtern:INPut?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.d``: The ``TRIGger:A:LOGIc:PATtern:INPut:D<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._d: Dict[int, TriggerALogicPatternInputDigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: TriggerALogicPatternInputDigitalBit(device, f"{self._cmd_syntax}:D{x}")
        )

    @property
    def d(self) -> Dict[int, TriggerALogicPatternInputDigitalBit]:
        """Return the ``TRIGger:A:LOGIc:PATtern:INPut:D<x>`` command.

        Description:
            - Sets or returns the A logic trigger input for the specified digital channel <x>, where
              x is the channel number. This command species the logic value used when the pattern
              trigger detects the threshold level.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:PATtern:INPut:D<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:LOGIc:PATtern:INPut:D<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:LOGIc:PATtern:INPut:D<x> value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGIc:PATtern:INPut:D<x> {HIGH|LOW|X}
            - TRIGger:A:LOGIc:PATtern:INPut:D<x>?
            ```

        Info:
            - ``HIGH`` specifies a logic high.
            - ``LOW`` specifies a logic low.
            - ``X`` specifies a 'do not care' state.
        """
        return self._d


class TriggerALogicPatternDeltatime(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOGIc:PATtern:DELTatime`` command.

    Description:
        - This command specifies the pattern trigger delta time value. The time value is used as
          part of the pattern trigger condition to determine if the duration of a logic pattern
          meets the specified time constraints.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:PATtern:DELTatime?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:PATtern:DELTatime?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:LOGIc:PATtern:DELTatime value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc:PATtern:DELTatime <NR3>
        - TRIGger:A:LOGIc:PATtern:DELTatime?
        ```

    Info:
        - ``<NR3>`` is a floating point value with exponent that sets the pattern trigger time
          value. This argument has a range of 39.6E-9 (39.6 ns) to 10.0E0 (10 s), in increments of
          13.2 ns. Values that are not an increment of 13.2 ns are rounded to the nearest correct
          value.
    """


class TriggerALogicPattern(SCPICmdRead):
    """The ``TRIGger:A:LOGIc:PATtern`` command.

    Description:
        - Returns the conditions used for generating an A logic pattern trigger, with respect to the
          defined input pattern, and identifies the time that the selected pattern may be true and
          still generate the trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:PATtern?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:PATtern?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc:PATtern?
        ```

    Properties:
        - ``.deltatime``: The ``TRIGger:A:LOGIc:PATtern:DELTatime`` command.
        - ``.input``: The ``TRIGger:A:LOGIc:PATtern:INPut`` command tree.
        - ``.when``: The ``TRIGger:A:LOGIc:PATtern:WHEn`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._deltatime = TriggerALogicPatternDeltatime(device, f"{self._cmd_syntax}:DELTatime")
        self._input = TriggerALogicPatternInput(device, f"{self._cmd_syntax}:INPut")
        self._when = TriggerALogicPatternWhen(device, f"{self._cmd_syntax}:WHEn")

    @property
    def deltatime(self) -> TriggerALogicPatternDeltatime:
        """Return the ``TRIGger:A:LOGIc:PATtern:DELTatime`` command.

        Description:
            - This command specifies the pattern trigger delta time value. The time value is used as
              part of the pattern trigger condition to determine if the duration of a logic pattern
              meets the specified time constraints.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:PATtern:DELTatime?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:LOGIc:PATtern:DELTatime?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:LOGIc:PATtern:DELTatime value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGIc:PATtern:DELTatime <NR3>
            - TRIGger:A:LOGIc:PATtern:DELTatime?
            ```

        Info:
            - ``<NR3>`` is a floating point value with exponent that sets the pattern trigger time
              value. This argument has a range of 39.6E-9 (39.6 ns) to 10.0E0 (10 s), in increments
              of 13.2 ns. Values that are not an increment of 13.2 ns are rounded to the nearest
              correct value.
        """
        return self._deltatime

    @property
    def input(self) -> TriggerALogicPatternInput:
        """Return the ``TRIGger:A:LOGIc:PATtern:INPut`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:PATtern:INPut?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:PATtern:INPut?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.d``: The ``TRIGger:A:LOGIc:PATtern:INPut:D<x>`` command.
        """
        return self._input

    @property
    def when(self) -> TriggerALogicPatternWhen:
        """Return the ``TRIGger:A:LOGIc:PATtern:WHEn`` command.

        Description:
            - Sets or returns the pattern logic condition on which to trigger the oscilloscope.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:PATtern:WHEn?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:PATtern:WHEn?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:LOGIc:PATtern:WHEn value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGIc:PATtern:WHEn {TRUe|FALSe|LESSThan|MOREThan|EQUal|UNEQual}
            - TRIGger:A:LOGIc:PATtern:WHEn?
            ```

        Info:
            - ``TRUE`` triggers the oscilloscope when the pattern becomes true.
            - ``FALSE`` triggers the oscilloscope when the pattern becomes false.
            - ``LESSTHAN`` triggers the oscilloscope when the input pattern is true for a time
              period less than the time period specified in ``TRIGGER:A:LOGIC:PATTERN:DELTATIME``.
            - ``MORETHAN`` triggers the oscilloscope when the input pattern is true for a time
              period more (greater) than the time period specified in
              ``TRIGGER:A:LOGIC:PATTERN:DELTATIME``.
            - ``EQUAL`` triggers the oscilloscope when the input pattern is true for a time period
              equal to the time period specified in ``TRIGGER:A:LOGIC:PATTERN:DELTATIME``, within a
              ±5% tolerance.
            - ``UNEQUAL`` triggers the oscilloscope when the input pattern is true for a time period
              greater than or less than (not equal to) the time period specified in
              ``TRIGGER:A:LOGIC:PATTERN:DELTATIME``, within a ±5% tolerance.

        Sub-properties:
            - ``.lesslimit``: The ``TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit`` command.
            - ``.morelimit``: The ``TRIGger:A:LOGIc:PATtern:WHEn:MORELimit`` command.
        """
        return self._when


class TriggerALogicInputDigitalBit(ValidatedDigitalBit, SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOGIc:INPut:D<x>`` command.

    Description:
        - This command specifies the logic pattern for a trigger on digital channel <x>, where x is
          the channel number.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:INPut:D<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:INPut:D<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGIc:INPut:D<x> value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc:INPut:D<x> {HIGH|LOW|X}
        - TRIGger:A:LOGIc:INPut:D<x>?
        ```

    Info:
        - ``High`` specifies the logic high state.
        - ``Low`` specifies the logic low state.
        - ``X`` specifies a 'don't care' state.
    """


class TriggerALogicInputClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOGIc:INPut:CLOCk:SOUrce`` command.

    Description:
        - Sets or returns the channel to use as the clock source. The clock can be selected as NONE.
          A selection of None implies pattern trigger. Any other selection implies state trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:LOGIc:INPut:CLOCk:SOUrce value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc:INPut:CLOCk:SOUrce {CH<x>|D<x>|NONE}
        - TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies the analog input channel source. x has a minimum of 1 and a maximum of
          4.
        - ``D<x>`` specifies the digital input channel source. x has a minimum of 0 and a maximum of
          15.
        - ``NONE`` specifies a Pattern trigger.
    """


class TriggerALogicInputClockEdge(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOGIc:INPut:CLOCk:EDGE`` command.

    Description:
        - Sets the polarity of the clock channel.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:INPut:CLOCk:EDGE?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:INPut:CLOCk:EDGE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:LOGIc:INPut:CLOCk:EDGE value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc:INPut:CLOCk:EDGE {FALL|RISe|EITher}
        - TRIGger:A:LOGIc:INPut:CLOCk:EDGE?
        ```

    Info:
        - ``RISe`` specifies to trigger on the rising or positive edge of a signal.
        - ``FALL`` specifies to trigger on the falling or negative edge of a signal.
        - ``EITher`` specifies to trigger either on the falling or rising edge of a signal.
    """


class TriggerALogicInputClock(SCPICmdRead):
    """The ``TRIGger:A:LOGIc:INPut:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:INPut:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:INPut:CLOCk?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.edge``: The ``TRIGger:A:LOGIc:INPut:CLOCk:EDGE`` command.
        - ``.source``: The ``TRIGger:A:LOGIc:INPut:CLOCk:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._edge = TriggerALogicInputClockEdge(device, f"{self._cmd_syntax}:EDGE")
        self._source = TriggerALogicInputClockSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def edge(self) -> TriggerALogicInputClockEdge:
        """Return the ``TRIGger:A:LOGIc:INPut:CLOCk:EDGE`` command.

        Description:
            - Sets the polarity of the clock channel.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:INPut:CLOCk:EDGE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:LOGIc:INPut:CLOCk:EDGE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:LOGIc:INPut:CLOCk:EDGE value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGIc:INPut:CLOCk:EDGE {FALL|RISe|EITher}
            - TRIGger:A:LOGIc:INPut:CLOCk:EDGE?
            ```

        Info:
            - ``RISe`` specifies to trigger on the rising or positive edge of a signal.
            - ``FALL`` specifies to trigger on the falling or negative edge of a signal.
            - ``EITher`` specifies to trigger either on the falling or rising edge of a signal.
        """
        return self._edge

    @property
    def source(self) -> TriggerALogicInputClockSource:
        """Return the ``TRIGger:A:LOGIc:INPut:CLOCk:SOUrce`` command.

        Description:
            - Sets or returns the channel to use as the clock source. The clock can be selected as
              NONE. A selection of None implies pattern trigger. Any other selection implies state
              trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:LOGIc:INPut:CLOCk:SOUrce value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGIc:INPut:CLOCk:SOUrce {CH<x>|D<x>|NONE}
            - TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies the analog input channel source. x has a minimum of 1 and a
              maximum of 4.
            - ``D<x>`` specifies the digital input channel source. x has a minimum of 0 and a
              maximum of 15.
            - ``NONE`` specifies a Pattern trigger.
        """
        return self._source


class TriggerALogicInputChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOGIc:INPut:CH<x>`` command.

    Description:
        - This command specifies the logical input condition for the channel specified by <x>.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:INPut:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:INPut:CH<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGIc:INPut:CH<x> value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc:INPut:CH<x> {HIGH|LOW|X}
        - TRIGger:A:LOGIc:INPut:CH<x>?
        ```

    Info:
        - ``HIGH`` specifies the logic high.
        - ``LOW`` specifies the logic low.
        - ``X`` specifies a 'don't care' state.
    """


class TriggerALogicInput(SCPICmdRead):
    """The ``TRIGger:A:LOGIc:INPut`` command.

    Description:
        - Returns the logic input values for all channels. If a clock channel is defined, it returns
          the clock source and edge.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:INPut?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:INPut?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc:INPut?
        ```

    Properties:
        - ``.ch``: The ``TRIGger:A:LOGIc:INPut:CH<x>`` command.
        - ``.clock``: The ``TRIGger:A:LOGIc:INPut:CLOCk`` command tree.
        - ``.d``: The ``TRIGger:A:LOGIc:INPut:D<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, TriggerALogicInputChannel] = DefaultDictPassKeyToFactory(
            lambda x: TriggerALogicInputChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._clock = TriggerALogicInputClock(device, f"{self._cmd_syntax}:CLOCk")
        self._d: Dict[int, TriggerALogicInputDigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: TriggerALogicInputDigitalBit(device, f"{self._cmd_syntax}:D{x}")
        )

    @property
    def ch(self) -> Dict[int, TriggerALogicInputChannel]:
        """Return the ``TRIGger:A:LOGIc:INPut:CH<x>`` command.

        Description:
            - This command specifies the logical input condition for the channel specified by <x>.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:INPut:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:INPut:CH<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGIc:INPut:CH<x> value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGIc:INPut:CH<x> {HIGH|LOW|X}
            - TRIGger:A:LOGIc:INPut:CH<x>?
            ```

        Info:
            - ``HIGH`` specifies the logic high.
            - ``LOW`` specifies the logic low.
            - ``X`` specifies a 'don't care' state.
        """
        return self._ch

    @property
    def clock(self) -> TriggerALogicInputClock:
        """Return the ``TRIGger:A:LOGIc:INPut:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:INPut:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:INPut:CLOCk?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.edge``: The ``TRIGger:A:LOGIc:INPut:CLOCk:EDGE`` command.
            - ``.source``: The ``TRIGger:A:LOGIc:INPut:CLOCk:SOUrce`` command.
        """
        return self._clock

    @property
    def d(self) -> Dict[int, TriggerALogicInputDigitalBit]:
        """Return the ``TRIGger:A:LOGIc:INPut:D<x>`` command.

        Description:
            - This command specifies the logic pattern for a trigger on digital channel <x>, where x
              is the channel number.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:INPut:D<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:INPut:D<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGIc:INPut:D<x> value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGIc:INPut:D<x> {HIGH|LOW|X}
            - TRIGger:A:LOGIc:INPut:D<x>?
            ```

        Info:
            - ``High`` specifies the logic high state.
            - ``Low`` specifies the logic low state.
            - ``X`` specifies a 'don't care' state.
        """
        return self._d


class TriggerALogicFunction(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOGIc:FUNCtion`` command.

    Description:
        - Sets or returns the logical combination of the input channels for the A pattern and A
          state logic triggers.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:FUNCtion?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:FUNCtion?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGIc:FUNCtion value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc:FUNCtion {AND|NANd}
        - TRIGger:A:LOGIc:FUNCtion?
        ```

    Info:
        - ``AND`` specifies to trigger if all conditions are true.
        - ``NANd`` specifies to trigger if any of the conditions is false.
    """


class TriggerALogicClass(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOGIc:CLAss`` command.

    Description:
        - This command specifies what kind of logic trigger to use (either logic or setup/hold). You
          also need to set the trigger type to LOGIC using the command ``TRIGGER:A:TYPE``. The LOGIC
          argument sets the oscilloscope to trigger on logical combinations of the channels (set
          using the ``TRIGger:A:LOGIc:INPut`` commands as well as ``TRIGGER:A:LOGIC:FUNCTION``). You
          can use up to 20 channels for a logic trigger (4 analog and 16 digital). You can perform
          logic triggering using a clock; when ``TRIGGER:A:LOGIC:INPUT:CLOCK:SOURCE`` is set to one
          of the channels, the oscilloscope triggers when the specified logical combination of the
          remaining channels is true during a transition on the clock channel. You can also perform
          logic triggering without using a clock (by setting ``TRIGGER:A:LOGIC:INPUT:CLOCK:SOURCE``
          to NONE ), so that the oscilloscope triggers when the specified logical combination of
          data channels is met. Without a clock, you can also use the command
          ``TRIGGER:A:LOGIC:PATTERN:DELTATIME``. The SETHold argument sets the oscilloscope to
          trigger on setup and hold violations between a data source and a clock source. The
          clocking and data levels are used to determine if a clock or data transition has occurred.
          You can use up to 20 channels as Setup and Hold trigger data sources (4 analog and 16
          digital) using ``TRIGGER:A:SETHOLD:DATA:SOURCE``. You can use one channel input as the
          clock signal (``TRIGGER:A:SETHOLD:CLOCK:SOURCE``). The data sources cannot include the
          waveform specified for the clock source.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:CLAss?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:CLAss?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGIc:CLAss value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc:CLAss {LOGIC|SETHold}
        - TRIGger:A:LOGIc:CLAss?
        ```

    Info:
        - ``LOGIC`` - Use with the commands ``TRIGGER:A:LOGIC:FUNCTION``,
          ``TRIGGER:A:LOGIC:INPUT:CHX``, ``TRIGGER:A:LOGIC:INPUT:CLOCK:EDGE``,
          ``TRIGGER:A:LOGIC:INPUT:CLOCK:SOURCE``, ``TRIGGER:A:LOGIC:INPUT:DX``, and
          ``TRIGGER:A:LOGIC:INPUT:RF``. If you would like to use the logic trigger without a clock,
          you can also use the command ``TRIGGER:A:LOGIC:PATTERN:DELTATIME``.
        - ``SETHold`` - Use with the commands ``TRIGGER:A:SETHOLD:CLOCK:EDGE``,
          ``TRIGGER:A:SETHOLD:CLOCK:SOURCE``, ``TRIGGER:A:SETHOLD:CLOCK:THRESHOLD``,
          ``TRIGGER:A:SETHOLD:DATA:SOURCE``.
    """


class TriggerALogic(SCPICmdRead):
    """The ``TRIGger:A:LOGIc`` command.

    Description:
        - Returns all of the A logic trigger parameters.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc?
        ```

    Properties:
        - ``.class``: The ``TRIGger:A:LOGIc:CLAss`` command.
        - ``.function``: The ``TRIGger:A:LOGIc:FUNCtion`` command.
        - ``.input``: The ``TRIGger:A:LOGIc:INPut`` command.
        - ``.pattern``: The ``TRIGger:A:LOGIc:PATtern`` command.
        - ``.threshold``: The ``TRIGger:A:LOGIc:THReshold`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._class = TriggerALogicClass(device, f"{self._cmd_syntax}:CLAss")
        self._function = TriggerALogicFunction(device, f"{self._cmd_syntax}:FUNCtion")
        self._input = TriggerALogicInput(device, f"{self._cmd_syntax}:INPut")
        self._pattern = TriggerALogicPattern(device, f"{self._cmd_syntax}:PATtern")
        self._threshold = TriggerALogicThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def class_(self) -> TriggerALogicClass:
        """Return the ``TRIGger:A:LOGIc:CLAss`` command.

        Description:
            - This command specifies what kind of logic trigger to use (either logic or setup/hold).
              You also need to set the trigger type to LOGIC using the command ``TRIGGER:A:TYPE``.
              The LOGIC argument sets the oscilloscope to trigger on logical combinations of the
              channels (set using the ``TRIGger:A:LOGIc:INPut`` commands as well as
              ``TRIGGER:A:LOGIC:FUNCTION``). You can use up to 20 channels for a logic trigger (4
              analog and 16 digital). You can perform logic triggering using a clock; when
              ``TRIGGER:A:LOGIC:INPUT:CLOCK:SOURCE`` is set to one of the channels, the oscilloscope
              triggers when the specified logical combination of the remaining channels is true
              during a transition on the clock channel. You can also perform logic triggering
              without using a clock (by setting ``TRIGGER:A:LOGIC:INPUT:CLOCK:SOURCE`` to NONE ), so
              that the oscilloscope triggers when the specified logical combination of data channels
              is met. Without a clock, you can also use the command
              ``TRIGGER:A:LOGIC:PATTERN:DELTATIME``. The SETHold argument sets the oscilloscope to
              trigger on setup and hold violations between a data source and a clock source. The
              clocking and data levels are used to determine if a clock or data transition has
              occurred. You can use up to 20 channels as Setup and Hold trigger data sources (4
              analog and 16 digital) using ``TRIGGER:A:SETHOLD:DATA:SOURCE``. You can use one
              channel input as the clock signal (``TRIGGER:A:SETHOLD:CLOCK:SOURCE``). The data
              sources cannot include the waveform specified for the clock source.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:CLAss?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:CLAss?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGIc:CLAss value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGIc:CLAss {LOGIC|SETHold}
            - TRIGger:A:LOGIc:CLAss?
            ```

        Info:
            - ``LOGIC`` - Use with the commands ``TRIGGER:A:LOGIC:FUNCTION``,
              ``TRIGGER:A:LOGIC:INPUT:CHX``, ``TRIGGER:A:LOGIC:INPUT:CLOCK:EDGE``,
              ``TRIGGER:A:LOGIC:INPUT:CLOCK:SOURCE``, ``TRIGGER:A:LOGIC:INPUT:DX``, and
              ``TRIGGER:A:LOGIC:INPUT:RF``. If you would like to use the logic trigger without a
              clock, you can also use the command ``TRIGGER:A:LOGIC:PATTERN:DELTATIME``.
            - ``SETHold`` - Use with the commands ``TRIGGER:A:SETHOLD:CLOCK:EDGE``,
              ``TRIGGER:A:SETHOLD:CLOCK:SOURCE``, ``TRIGGER:A:SETHOLD:CLOCK:THRESHOLD``,
              ``TRIGGER:A:SETHOLD:DATA:SOURCE``.
        """
        return self._class

    @property
    def function(self) -> TriggerALogicFunction:
        """Return the ``TRIGger:A:LOGIc:FUNCtion`` command.

        Description:
            - Sets or returns the logical combination of the input channels for the A pattern and A
              state logic triggers.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:FUNCtion?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:FUNCtion?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGIc:FUNCtion value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGIc:FUNCtion {AND|NANd}
            - TRIGger:A:LOGIc:FUNCtion?
            ```

        Info:
            - ``AND`` specifies to trigger if all conditions are true.
            - ``NANd`` specifies to trigger if any of the conditions is false.
        """
        return self._function

    @property
    def input(self) -> TriggerALogicInput:
        """Return the ``TRIGger:A:LOGIc:INPut`` command.

        Description:
            - Returns the logic input values for all channels. If a clock channel is defined, it
              returns the clock source and edge.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:INPut?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:INPut?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGIc:INPut?
            ```

        Sub-properties:
            - ``.ch``: The ``TRIGger:A:LOGIc:INPut:CH<x>`` command.
            - ``.clock``: The ``TRIGger:A:LOGIc:INPut:CLOCk`` command tree.
            - ``.d``: The ``TRIGger:A:LOGIc:INPut:D<x>`` command.
        """
        return self._input

    @property
    def pattern(self) -> TriggerALogicPattern:
        """Return the ``TRIGger:A:LOGIc:PATtern`` command.

        Description:
            - Returns the conditions used for generating an A logic pattern trigger, with respect to
              the defined input pattern, and identifies the time that the selected pattern may be
              true and still generate the trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:PATtern?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:PATtern?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGIc:PATtern?
            ```

        Sub-properties:
            - ``.deltatime``: The ``TRIGger:A:LOGIc:PATtern:DELTatime`` command.
            - ``.input``: The ``TRIGger:A:LOGIc:PATtern:INPut`` command tree.
            - ``.when``: The ``TRIGger:A:LOGIc:PATtern:WHEn`` command.
        """
        return self._pattern

    @property
    def threshold(self) -> TriggerALogicThreshold:
        """Return the ``TRIGger:A:LOGIc:THReshold`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:THReshold?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.d``: The ``TRIGger:A:LOGIc:THReshold:D<x>`` command.
            - ``.ch``: The ``TRIGger:A:LOGIc:THReshold:CH<x>`` command.
        """
        return self._threshold


class TriggerALevelDigitalBit(ValidatedDigitalBit, SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LEVel:D<x>`` command.

    Description:
        - This command sets the threshold voltage level to use for an Edge or Pulse Width trigger
          when triggering on a digital channel waveform. <x> can be 1 - 16. Each channel can have an
          independent trigger level.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LEVel:D<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LEVel:D<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LEVel:D<x> value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:LEVel:D<x> {<NR3>|ECL|TTL}
        - TRIGger:A:LEVel:D<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that sets the trigger threshold level, in Volts, for
          the specified digital channel.
        - ``ECL`` sets the threshold level to a preset ECL high level of -1.3V.
        - ``TTL`` sets the threshold level to a preset TTL high level of 1.4V.
    """


class TriggerALevelChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LEVel:CH<x>`` command.

    Description:
        - Sets or returns the trigger level for the specified channel. Each channel can have an
          independent level.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LEVel:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LEVel:CH<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LEVel:CH<x> value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:LEVel:CH<x> {<NR3>|TTL|ECL}
        - TRIGger:A:LEVel:CH<x>?
        ```

    Info:
        - ``<NR3>`` specifies the trigger level in user units (usually volts).
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
        - ``ECL`` specifies a preset ECL high level of -1.3 V.
    """


class TriggerALevelAuxin(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LEVel:AUXin`` command.

    Description:
        - This command sets the threshold voltage level to use for an Edge, Pulse Width, Runt or
          Rise/Fall (aka Transition, aka Slew Rate) trigger when triggering on the Aux Input
          connector signal.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LEVel:AUXin?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LEVel:AUXin?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LEVel:AUXin value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:LEVel:AUXin {<NR3>|ECL|TTL}
        - TRIGger:A:LEVel:AUXin?
        ```

    Info:
        - ``<NR3>`` is a floating point number that sets the trigger threshold level, in Volts, for
          the Aux Input connector.
        - ``ECL`` sets the threshold level to a preset ECL high level of -1.3V.
        - ``TTL`` sets the threshold level to a preset TTL high level of 1.4V.
    """


class TriggerALevel(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LEVel`` command.

    Description:
        - Sets or returns the trigger level for the A trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LEVel?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LEVel?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LEVel value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:LEVel {ECL|TTL|<NR3>}
        - TRIGger:A:LEVel?
        ```

    Info:
        - ``ECL`` specifies a preset ECL high level of -1.3V.
        - ``TTL`` specifies a preset TTL high level of 1.4V.
        - ``<NR3>`` specifies the trigger level in user units (usually volts).

    Properties:
        - ``.auxin``: The ``TRIGger:A:LEVel:AUXin`` command.
        - ``.ch``: The ``TRIGger:A:LEVel:CH<x>`` command.
        - ``.d``: The ``TRIGger:A:LEVel:D<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._auxin = TriggerALevelAuxin(device, f"{self._cmd_syntax}:AUXin")
        self._ch: Dict[int, TriggerALevelChannel] = DefaultDictPassKeyToFactory(
            lambda x: TriggerALevelChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._d: Dict[int, TriggerALevelDigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: TriggerALevelDigitalBit(device, f"{self._cmd_syntax}:D{x}")
        )

    @property
    def auxin(self) -> TriggerALevelAuxin:
        """Return the ``TRIGger:A:LEVel:AUXin`` command.

        Description:
            - This command sets the threshold voltage level to use for an Edge, Pulse Width, Runt or
              Rise/Fall (aka Transition, aka Slew Rate) trigger when triggering on the Aux Input
              connector signal.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LEVel:AUXin?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LEVel:AUXin?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:LEVel:AUXin value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:LEVel:AUXin {<NR3>|ECL|TTL}
            - TRIGger:A:LEVel:AUXin?
            ```

        Info:
            - ``<NR3>`` is a floating point number that sets the trigger threshold level, in Volts,
              for the Aux Input connector.
            - ``ECL`` sets the threshold level to a preset ECL high level of -1.3V.
            - ``TTL`` sets the threshold level to a preset TTL high level of 1.4V.
        """
        return self._auxin

    @property
    def ch(self) -> Dict[int, TriggerALevelChannel]:
        """Return the ``TRIGger:A:LEVel:CH<x>`` command.

        Description:
            - Sets or returns the trigger level for the specified channel. Each channel can have an
              independent level.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LEVel:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LEVel:CH<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:LEVel:CH<x> value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:LEVel:CH<x> {<NR3>|TTL|ECL}
            - TRIGger:A:LEVel:CH<x>?
            ```

        Info:
            - ``<NR3>`` specifies the trigger level in user units (usually volts).
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
            - ``ECL`` specifies a preset ECL high level of -1.3 V.
        """
        return self._ch

    @property
    def d(self) -> Dict[int, TriggerALevelDigitalBit]:
        """Return the ``TRIGger:A:LEVel:D<x>`` command.

        Description:
            - This command sets the threshold voltage level to use for an Edge or Pulse Width
              trigger when triggering on a digital channel waveform. <x> can be 1 - 16. Each channel
              can have an independent trigger level.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LEVel:D<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LEVel:D<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:LEVel:D<x> value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:LEVel:D<x> {<NR3>|ECL|TTL}
            - TRIGger:A:LEVel:D<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that sets the trigger threshold level, in Volts,
              for the specified digital channel.
            - ``ECL`` sets the threshold level to a preset ECL high level of -1.3V.
            - ``TTL`` sets the threshold level to a preset TTL high level of 1.4V.
        """
        return self._d


class TriggerAHoldoffTime(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:HOLDoff:TIMe`` command.

    Description:
        - This command sets or queries the A trigger holdoff time. This command is equivalent to
          selecting Mode & Holdoff from the Trig menu, selecting Time, and then setting the desired
          Holdoff Time.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:HOLDoff:TIMe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:HOLDoff:TIMe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:HOLDoff:TIMe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:HOLDoff:TIMe <NR3>
        - TRIGger:A:HOLDoff:TIMe?
        ```

    Info:
        - ``<NR3>`` specifies the holdoff time in seconds. The range is from 0 seconds through 10
          seconds.
    """


class TriggerAHoldoff(SCPICmdRead):
    """The ``TRIGger:A:HOLDoff`` command.

    Description:
        - Returns the A trigger holdoff parameters. These parameters specify the time period during
          which the trigger circuitry is not looking to generate a trigger event.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:HOLDoff?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:HOLDoff?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TRIGger:A:HOLDoff?
        ```

    Properties:
        - ``.time``: The ``TRIGger:A:HOLDoff:TIMe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._time = TriggerAHoldoffTime(device, f"{self._cmd_syntax}:TIMe")

    @property
    def time(self) -> TriggerAHoldoffTime:
        """Return the ``TRIGger:A:HOLDoff:TIMe`` command.

        Description:
            - This command sets or queries the A trigger holdoff time. This command is equivalent to
              selecting Mode & Holdoff from the Trig menu, selecting Time, and then setting the
              desired Holdoff Time.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:HOLDoff:TIMe?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:HOLDoff:TIMe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:HOLDoff:TIMe value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:HOLDoff:TIMe <NR3>
            - TRIGger:A:HOLDoff:TIMe?
            ```

        Info:
            - ``<NR3>`` specifies the holdoff time in seconds. The range is from 0 seconds through
              10 seconds.
        """
        return self._time


class TriggerAEdgeSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:EDGE:SOUrce`` command.

    Description:
        - Sets or returns the source for the A edge trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:EDGE:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:EDGE:SOUrce value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:EDGE:SOUrce {CH<x>|D<x>|EXT|LINE|AUX}
        - TRIGger:A:EDGE:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog input channel as the A edge trigger source. x has a minimum
          of 1 and a maximum of 4.
        - ``D<x>`` specifies a digital input channel as the A edge trigger source. x has a minimum
          of 0 and a maximum of 15.
        - ``EXT`` specifies an external trigger using the Aux In connector located on the front
          panel of the oscilloscope.
        - ``LINE`` specifies the AC line as the trigger source.
        - ``AUX`` specifies the Auxiliary Input as the trigger source (if available on your
          oscilloscope).
    """


class TriggerAEdgeSlope(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:EDGE:SLOpe`` command.

    Description:
        - Sets or returns the slope for the A edge trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:EDGE:SLOpe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE:SLOpe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:EDGE:SLOpe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:EDGE:SLOpe {RISe|FALL}
        - TRIGger:A:EDGE:SLOpe?
        ```

    Info:
        - ``RISe`` specifies to trigger on the rising or positive edge of a signal.
        - ``FALL`` specifies to trigger on the falling or negative edge of a signal.
    """


class TriggerAEdgeCoupling(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:EDGE:COUPling`` command.

    Description:
        - This command sets or queries the type of coupling for the edge trigger. This command is
          equivalent to selecting Edge from the Trigger Type drop-down in the Trigger setup context
          menu, and choosing from the Coupling drop-down list.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:EDGE:COUPling?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE:COUPling?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:EDGE:COUPling value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:EDGE:COUPling {DC|HFRej|LFRej|NOISErej}
        - TRIGger:A:EDGE:COUPling?
        ```

    Info:
        - ``DC`` selects DC trigger coupling, which passes all input signals to the trigger
          circuitry.
        - ``HFRej`` coupling attenuates signals above 50 kHz before passing the signals to the
          trigger circuitry.
        - ``LFRej`` coupling attenuates signals below 80 kHz before passing the signals to the
          trigger circuitry.
        - ``NOISErej`` coupling provides stable triggering by increasing the trigger hysteresis.
          Increased hysteresis reduces the trigger sensitivity to noise but can require greater
          trigger signal amplitude.
    """


class TriggerAEdge(SCPICmdRead):
    """The ``TRIGger:A:EDGE`` command.

    Description:
        - Returns the trigger source, coupling, and slope for the A edge trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:EDGE?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TRIGger:A:EDGE?
        ```

    Properties:
        - ``.coupling``: The ``TRIGger:A:EDGE:COUPling`` command.
        - ``.slope``: The ``TRIGger:A:EDGE:SLOpe`` command.
        - ``.source``: The ``TRIGger:A:EDGE:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._coupling = TriggerAEdgeCoupling(device, f"{self._cmd_syntax}:COUPling")
        self._slope = TriggerAEdgeSlope(device, f"{self._cmd_syntax}:SLOpe")
        self._source = TriggerAEdgeSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def coupling(self) -> TriggerAEdgeCoupling:
        """Return the ``TRIGger:A:EDGE:COUPling`` command.

        Description:
            - This command sets or queries the type of coupling for the edge trigger. This command
              is equivalent to selecting Edge from the Trigger Type drop-down in the Trigger setup
              context menu, and choosing from the Coupling drop-down list.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:EDGE:COUPling?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE:COUPling?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:EDGE:COUPling value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:EDGE:COUPling {DC|HFRej|LFRej|NOISErej}
            - TRIGger:A:EDGE:COUPling?
            ```

        Info:
            - ``DC`` selects DC trigger coupling, which passes all input signals to the trigger
              circuitry.
            - ``HFRej`` coupling attenuates signals above 50 kHz before passing the signals to the
              trigger circuitry.
            - ``LFRej`` coupling attenuates signals below 80 kHz before passing the signals to the
              trigger circuitry.
            - ``NOISErej`` coupling provides stable triggering by increasing the trigger hysteresis.
              Increased hysteresis reduces the trigger sensitivity to noise but can require greater
              trigger signal amplitude.
        """
        return self._coupling

    @property
    def slope(self) -> TriggerAEdgeSlope:
        """Return the ``TRIGger:A:EDGE:SLOpe`` command.

        Description:
            - Sets or returns the slope for the A edge trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:EDGE:SLOpe?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE:SLOpe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:EDGE:SLOpe value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:EDGE:SLOpe {RISe|FALL}
            - TRIGger:A:EDGE:SLOpe?
            ```

        Info:
            - ``RISe`` specifies to trigger on the rising or positive edge of a signal.
            - ``FALL`` specifies to trigger on the falling or negative edge of a signal.
        """
        return self._slope

    @property
    def source(self) -> TriggerAEdgeSource:
        """Return the ``TRIGger:A:EDGE:SOUrce`` command.

        Description:
            - Sets or returns the source for the A edge trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:EDGE:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:EDGE:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:EDGE:SOUrce {CH<x>|D<x>|EXT|LINE|AUX}
            - TRIGger:A:EDGE:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog input channel as the A edge trigger source. x has a
              minimum of 1 and a maximum of 4.
            - ``D<x>`` specifies a digital input channel as the A edge trigger source. x has a
              minimum of 0 and a maximum of 15.
            - ``EXT`` specifies an external trigger using the Aux In connector located on the front
              panel of the oscilloscope.
            - ``LINE`` specifies the AC line as the trigger source.
            - ``AUX`` specifies the Auxiliary Input as the trigger source (if available on your
              oscilloscope).
        """
        return self._source


class TriggerABusSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:SOUrce`` command.

    Description:
        - This command specifies the source for a serial or parallel bus trigger, with the
          appropriate application module installed.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:BUS:SOUrce value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:SOUrce {B<x>}
        - TRIGger:A:BUS:SOUrce?
        ```

    Info:
        - ``B1`` specifies the Bus 1 source.
        - ``B2`` specifies the Bus 2 source.
        - ``B3`` specifies the Bus 3 source.
        - ``B4`` specifies the Bus 4 source.
    """


class TriggerABusBItemSpiDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SPI:DATa:SIZe`` command.

    Description:
        - This command specifies the length of the data string to be used for a SPI trigger if the
          trigger condition is DATa. B<x> is the specified bus number.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:SIZe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SPI:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SPI:DATa:SIZe <NR1>
        - TRIGger:A:BUS:B<x>:SPI:DATa:SIZe?
        ```

    Info:
        - ``<NR1>`` is the length of the data string in bytes.
    """


class TriggerABusBItemSpiDataOutValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue`` command.

    Description:
        - This command specifies the binary data string to be used for a SPI trigger if the trigger
          condition is MOSI or MISOMOSI. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue <QString>
        - TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue?
        ```

    Info:
        - ``<QString>`` is the binary data string with the number of bits specified by the
          ``TRIGGER:A:BUS:BX:SPI:DATA:SIZE`` command. The only allowed characters in the QString are
          0, 1, and X.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemSpiDataOut(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SPI:DATa:OUT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:OUT?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:OUT?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemSpiDataOutValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> TriggerABusBItemSpiDataOutValue:
        """Return the ``TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue`` command.

        Description:
            - This command specifies the binary data string to be used for a SPI trigger if the
              trigger condition is MOSI or MISOMOSI. B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue <QString>
            - TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue?
            ```

        Info:
            - ``<QString>`` is the binary data string with the number of bits specified by the
              ``TRIGGER:A:BUS:BX:SPI:DATA:SIZE`` command. The only allowed characters in the QString
              are 0, 1, and X.
        """
        return self._value


class TriggerABusBItemSpiDataMosiValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue`` command.

    Description:
        - This command specifies the binary data string to be used for a SPI trigger if the trigger
          condition is MOSI or MISOMOSI. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue <QString>
        - TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue?
        ```

    Info:
        - ``<QString>`` is the binary data string with the number of bits specified by the
          ``TRIGGER:A:BUS:BX:SPI:DATA:SIZE`` command. The only allowed characters in the QString are
          0, 1, and X.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemSpiDataMosi(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SPI:DATa:MOSI`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:MOSI?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:MOSI?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemSpiDataMosiValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> TriggerABusBItemSpiDataMosiValue:
        """Return the ``TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue`` command.

        Description:
            - This command specifies the binary data string to be used for a SPI trigger if the
              trigger condition is MOSI or MISOMOSI. B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue <QString>
            - TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue?
            ```

        Info:
            - ``<QString>`` is the binary data string with the number of bits specified by the
              ``TRIGGER:A:BUS:BX:SPI:DATA:SIZE`` command. The only allowed characters in the QString
              are 0, 1, and X.
        """
        return self._value


class TriggerABusBItemSpiDataMisoValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue`` command.

    Description:
        - This command specifies the binary data string to be used for a SPI trigger if the trigger
          condition is MISO or MISOMOSI. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue <QString>
        - TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue?
        ```

    Info:
        - ``<QString>`` is the binary data string, where the number of bits is 8 times the number of
          bytes specified. The only allowed characters in the string are 0, 1, and X.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemSpiDataMiso(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SPI:DATa:MISO`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:MISO?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:MISO?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemSpiDataMisoValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> TriggerABusBItemSpiDataMisoValue:
        """Return the ``TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue`` command.

        Description:
            - This command specifies the binary data string to be used for a SPI trigger if the
              trigger condition is MISO or MISOMOSI. B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue <QString>
            - TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue?
            ```

        Info:
            - ``<QString>`` is the binary data string, where the number of bits is 8 times the
              number of bytes specified. The only allowed characters in the string are 0, 1, and X.
        """
        return self._value


class TriggerABusBItemSpiDataInValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue`` command.

    Description:
        - This command specifies the binary data string to be used for a SPI trigger if the trigger
          condition is MISO or MISOMOSI. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue <QString>
        - TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue?
        ```

    Info:
        - ``<QString>`` is the binary data string, where the number of bits is 8 times the number of
          bytes specified. The only allowed characters in the string are 0, 1, and X.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemSpiDataIn(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SPI:DATa:IN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:IN?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:IN?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemSpiDataInValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> TriggerABusBItemSpiDataInValue:
        """Return the ``TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue`` command.

        Description:
            - This command specifies the binary data string to be used for a SPI trigger if the
              trigger condition is MISO or MISOMOSI. B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue <QString>
            - TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue?
            ```

        Info:
            - ``<QString>`` is the binary data string, where the number of bits is 8 times the
              number of bytes specified. The only allowed characters in the string are 0, 1, and X.
        """
        return self._value


class TriggerABusBItemSpiData(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SPI:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.size``: The ``TRIGger:A:BUS:B<x>:SPI:DATa:SIZe`` command.
        - ``.in``: The ``TRIGger:A:BUS:B<x>:SPI:DATa:IN`` command tree.
        - ``.miso``: The ``TRIGger:A:BUS:B<x>:SPI:DATa:MISO`` command tree.
        - ``.out``: The ``TRIGger:A:BUS:B<x>:SPI:DATa:OUT`` command tree.
        - ``.mosi``: The ``TRIGger:A:BUS:B<x>:SPI:DATa:MOSI`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._size = TriggerABusBItemSpiDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._in = TriggerABusBItemSpiDataIn(device, f"{self._cmd_syntax}:IN")
        self._miso = TriggerABusBItemSpiDataMiso(device, f"{self._cmd_syntax}:MISO")
        self._out = TriggerABusBItemSpiDataOut(device, f"{self._cmd_syntax}:OUT")
        self._mosi = TriggerABusBItemSpiDataMosi(device, f"{self._cmd_syntax}:MOSI")

    @property
    def size(self) -> TriggerABusBItemSpiDataSize:
        """Return the ``TRIGger:A:BUS:B<x>:SPI:DATa:SIZe`` command.

        Description:
            - This command specifies the length of the data string to be used for a SPI trigger if
              the trigger condition is DATa. B<x> is the specified bus number.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:SIZe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SPI:DATa:SIZe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SPI:DATa:SIZe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SPI:DATa:SIZe <NR1>
            - TRIGger:A:BUS:B<x>:SPI:DATa:SIZe?
            ```

        Info:
            - ``<NR1>`` is the length of the data string in bytes.
        """
        return self._size

    @property
    def in_(self) -> TriggerABusBItemSpiDataIn:
        """Return the ``TRIGger:A:BUS:B<x>:SPI:DATa:IN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:IN?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:IN?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:SPI:DATa:IN:VALue`` command.
        """
        return self._in

    @property
    def miso(self) -> TriggerABusBItemSpiDataMiso:
        """Return the ``TRIGger:A:BUS:B<x>:SPI:DATa:MISO`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:MISO?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SPI:DATa:MISO?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:SPI:DATa:MISO:VALue`` command.
        """
        return self._miso

    @property
    def out(self) -> TriggerABusBItemSpiDataOut:
        """Return the ``TRIGger:A:BUS:B<x>:SPI:DATa:OUT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:OUT?``
              query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:OUT?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:SPI:DATa:OUT:VALue`` command.
        """
        return self._out

    @property
    def mosi(self) -> TriggerABusBItemSpiDataMosi:
        """Return the ``TRIGger:A:BUS:B<x>:SPI:DATa:MOSI`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:MOSI?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SPI:DATa:MOSI?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:SPI:DATa:MOSI:VALue`` command.
        """
        return self._mosi


class TriggerABusBItemSpiCondition(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SPI:CONDition`` command.

    Description:
        - This command specifies the trigger condition for a SPI trigger. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SPI:CONDition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SPI:CONDition value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SPI:CONDition {SS|STARTofframe|MISO|MOSI|MISOMOSI}
        - TRIGger:A:BUS:B<x>:SPI:CONDition?
        ```

    Info:
        - ``SS`` specifies the Slave Selection condition.
        - ``STARTofframe`` is applicable when ``BUS:B<x>:SPI:FRAMING`` is set to IDLEtime. When the
          trigger condition is set to STARTofframe, the instrument triggers on the first SPI clock
          after an idle time when there are no clocks.
        - ``MISO`` specifies the Master-In Slave-Out condition.
        - ``MOSI`` specifies the Master-Out Slave-In condition.
        - ``MISOMOSI`` specifies the Master-In Slave-Out and Master-Out Slave-In conditions.
    """


class TriggerABusBItemSpi(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SPI`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SPI?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``TRIGger:A:BUS:B<x>:SPI:CONDition`` command.
        - ``.data``: The ``TRIGger:A:BUS:B<x>:SPI:DATa`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = TriggerABusBItemSpiCondition(device, f"{self._cmd_syntax}:CONDition")
        self._data = TriggerABusBItemSpiData(device, f"{self._cmd_syntax}:DATa")

    @property
    def condition(self) -> TriggerABusBItemSpiCondition:
        """Return the ``TRIGger:A:BUS:B<x>:SPI:CONDition`` command.

        Description:
            - This command specifies the trigger condition for a SPI trigger. B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:CONDition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SPI:CONDition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SPI:CONDition value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SPI:CONDition {SS|STARTofframe|MISO|MOSI|MISOMOSI}
            - TRIGger:A:BUS:B<x>:SPI:CONDition?
            ```

        Info:
            - ``SS`` specifies the Slave Selection condition.
            - ``STARTofframe`` is applicable when ``BUS:B<x>:SPI:FRAMING`` is set to IDLEtime. When
              the trigger condition is set to STARTofframe, the instrument triggers on the first SPI
              clock after an idle time when there are no clocks.
            - ``MISO`` specifies the Master-In Slave-Out condition.
            - ``MOSI`` specifies the Master-Out Slave-In condition.
            - ``MISOMOSI`` specifies the Master-In Slave-Out and Master-Out Slave-In conditions.
        """
        return self._condition

    @property
    def data(self) -> TriggerABusBItemSpiData:
        """Return the ``TRIGger:A:BUS:B<x>:SPI:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.size``: The ``TRIGger:A:BUS:B<x>:SPI:DATa:SIZe`` command.
            - ``.in``: The ``TRIGger:A:BUS:B<x>:SPI:DATa:IN`` command tree.
            - ``.miso``: The ``TRIGger:A:BUS:B<x>:SPI:DATa:MISO`` command tree.
            - ``.out``: The ``TRIGger:A:BUS:B<x>:SPI:DATa:OUT`` command tree.
            - ``.mosi``: The ``TRIGger:A:BUS:B<x>:SPI:DATa:MOSI`` command tree.
        """
        return self._data


class TriggerABusBItemRs232cTxDataValue(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue`` command.

    Description:
        - This command specifies the binary data string for an RS-232 trigger if the condition
          involves TX. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue
        - TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue?
        ```

    Info:
        - ``<Qstring>`` is the binary data string to be used for the trigger.
    """


class TriggerABusBItemRs232cTxDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe`` command.

    Description:
        - This command specifies the length of the data string for an RS-232 trigger if the trigger
          condition is TXDATA. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe <NR1>
        - TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe?
        ```

    Info:
        - ``<NR1>`` is the length of the data string in Bytes.
    """


class TriggerABusBItemRs232cTxData(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.size``: The ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._size = TriggerABusBItemRs232cTxDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._value = TriggerABusBItemRs232cTxDataValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def size(self) -> TriggerABusBItemRs232cTxDataSize:
        """Return the ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe`` command.

        Description:
            - This command specifies the length of the data string for an RS-232 trigger if the
              trigger condition is TXDATA. B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe <NR1>
            - TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe?
            ```

        Info:
            - ``<NR1>`` is the length of the data string in Bytes.
        """
        return self._size

    @property
    def value(self) -> TriggerABusBItemRs232cTxDataValue:
        """Return the ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue`` command.

        Description:
            - This command specifies the binary data string for an RS-232 trigger if the condition
              involves TX. B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write()`` method will send the
              ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue
            - TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue?
            ```

        Info:
            - ``<Qstring>`` is the binary data string to be used for the trigger.
        """
        return self._value


class TriggerABusBItemRs232cTx(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:RS232C:TX`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:TX?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:TX?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.data``: The ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._data = TriggerABusBItemRs232cTxData(device, f"{self._cmd_syntax}:DATa")

    @property
    def data(self) -> TriggerABusBItemRs232cTxData:
        """Return the ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.size``: The ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue`` command.
        """
        return self._data


class TriggerABusBItemRs232cRxDataValue(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue`` command.

    Description:
        - This command specifies the binary data string for an RS-232 trigger if the trigger
          condition involves RX. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue
        - TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue?
        ```

    Info:
        - ``<Qstring>`` is the binary data string to be used for the trigger.
    """


class TriggerABusBItemRs232cRxDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe`` command.

    Description:
        - This command specifies the length of the data string in Bytes for an RS-232 Trigger if the
          trigger condition is RXDATA. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe <NR1>
        - TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe?
        ```

    Info:
        - ``<NR1>`` is the length of the data string in bytes.
    """


class TriggerABusBItemRs232cRxData(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.size``: The ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._size = TriggerABusBItemRs232cRxDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._value = TriggerABusBItemRs232cRxDataValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def size(self) -> TriggerABusBItemRs232cRxDataSize:
        """Return the ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe`` command.

        Description:
            - This command specifies the length of the data string in Bytes for an RS-232 Trigger if
              the trigger condition is RXDATA. B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe <NR1>
            - TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe?
            ```

        Info:
            - ``<NR1>`` is the length of the data string in bytes.
        """
        return self._size

    @property
    def value(self) -> TriggerABusBItemRs232cRxDataValue:
        """Return the ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue`` command.

        Description:
            - This command specifies the binary data string for an RS-232 trigger if the trigger
              condition involves RX. B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write()`` method will send the
              ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue
            - TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue?
            ```

        Info:
            - ``<Qstring>`` is the binary data string to be used for the trigger.
        """
        return self._value


class TriggerABusBItemRs232cRx(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:RS232C:RX`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:RX?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:RX?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.data``: The ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._data = TriggerABusBItemRs232cRxData(device, f"{self._cmd_syntax}:DATa")

    @property
    def data(self) -> TriggerABusBItemRs232cRxData:
        """Return the ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.size``: The ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue`` command.
        """
        return self._data


class TriggerABusBItemRs232cCondition(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:RS232C:CONDition`` command.

    Description:
        - Sets or returns the condition for a RS232C trigger, where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:CONDition?``
          query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:CONDition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:RS232C:CONDition value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:RS232C:CONDition {RXSTArt|RXDATA|RXENDPacket|RXPARity|TXSTArt|TXDATA|TXENDPacket|TXPARity|}
        - TRIGger:A:BUS:B<x>:RS232C:CONDition?
        ```

    Info:
        - ``RXSTArt`` specifies a search based on the RX Start Bit.
        - ``RXDATA`` specifies a search based on RX Data.
        - ``RXENDPacket`` specifies a search based on the RX End of Packet condition.
        - ``RXPARity`` specifies a search based on the RX parity.
        - ``TXSTArt`` specifies a search base on the TX Start Bit.
        - ``TXDATA`` specifies a search based on TX Data.
        - ``TXENDPacket`` specifies a search based on the TX End of Packet condition.
        - ``TXPARity`` specifies a search based on the TX parity.
    """  # noqa: E501


class TriggerABusBItemRs232c(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:RS232C`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:RS232C?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``TRIGger:A:BUS:B<x>:RS232C:CONDition`` command.
        - ``.rx``: The ``TRIGger:A:BUS:B<x>:RS232C:RX`` command tree.
        - ``.tx``: The ``TRIGger:A:BUS:B<x>:RS232C:TX`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = TriggerABusBItemRs232cCondition(device, f"{self._cmd_syntax}:CONDition")
        self._rx = TriggerABusBItemRs232cRx(device, f"{self._cmd_syntax}:RX")
        self._tx = TriggerABusBItemRs232cTx(device, f"{self._cmd_syntax}:TX")

    @property
    def condition(self) -> TriggerABusBItemRs232cCondition:
        """Return the ``TRIGger:A:BUS:B<x>:RS232C:CONDition`` command.

        Description:
            - Sets or returns the condition for a RS232C trigger, where x is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:CONDition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:RS232C:CONDition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:RS232C:CONDition value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:RS232C:CONDition {RXSTArt|RXDATA|RXENDPacket|RXPARity|TXSTArt|TXDATA|TXENDPacket|TXPARity|}
            - TRIGger:A:BUS:B<x>:RS232C:CONDition?
            ```

        Info:
            - ``RXSTArt`` specifies a search based on the RX Start Bit.
            - ``RXDATA`` specifies a search based on RX Data.
            - ``RXENDPacket`` specifies a search based on the RX End of Packet condition.
            - ``RXPARity`` specifies a search based on the RX parity.
            - ``TXSTArt`` specifies a search base on the TX Start Bit.
            - ``TXDATA`` specifies a search based on TX Data.
            - ``TXENDPacket`` specifies a search based on the TX End of Packet condition.
            - ``TXPARity`` specifies a search based on the TX parity.
        """  # noqa: E501
        return self._condition

    @property
    def rx(self) -> TriggerABusBItemRs232cRx:
        """Return the ``TRIGger:A:BUS:B<x>:RS232C:RX`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:RX?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:RX?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.data``: The ``TRIGger:A:BUS:B<x>:RS232C:RX:DATa`` command tree.
        """
        return self._rx

    @property
    def tx(self) -> TriggerABusBItemRs232cTx:
        """Return the ``TRIGger:A:BUS:B<x>:RS232C:TX`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:TX?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:TX?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.data``: The ``TRIGger:A:BUS:B<x>:RS232C:TX:DATa`` command tree.
        """
        return self._tx


class TriggerABusBItemParallelValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:PARallel:VALue`` command.

    Description:
        - This command specifies the binary data string to be used for a Parallel trigger. Applies
          to bus <x>, where x

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:PARallel:VALue?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:PARallel:VALue?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:PARallel:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:PARallel:VALue <QString>
        - TRIGger:A:BUS:B<x>:PARallel:VALue?
        ```

    Info:
        - ``<QString>`` is the binary data string.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemParallel(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:PARallel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:PARallel?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:PARallel?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:PARallel:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemParallelValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> TriggerABusBItemParallelValue:
        """Return the ``TRIGger:A:BUS:B<x>:PARallel:VALue`` command.

        Description:
            - This command specifies the binary data string to be used for a Parallel trigger.
              Applies to bus <x>, where x

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:PARallel:VALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:PARallel:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:PARallel:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:PARallel:VALue <QString>
            - TRIGger:A:BUS:B<x>:PARallel:VALue?
            ```

        Info:
            - ``<QString>`` is the binary data string.
        """
        return self._value


class TriggerABusBItemLinIdentifierValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue`` command.

    Description:
        - This command specifies the binary address string used for LIN bus trigger if the trigger
          condition is ID or IDANDDATA. The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue <QString>
        - TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue?
        ```

    Info:
        - ``<QString>`` is the binary address string used for LIN trigger if the trigger condition
          is ID or IDANDDATA.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemLinIdentifier(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:LIN:IDentifier`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:IDentifier?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN:IDentifier?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemLinIdentifierValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> TriggerABusBItemLinIdentifierValue:
        """Return the ``TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue`` command.

        Description:
            - This command specifies the binary address string used for LIN bus trigger if the
              trigger condition is ID or IDANDDATA. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue <QString>
            - TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue?
            ```

        Info:
            - ``<QString>`` is the binary address string used for LIN trigger if the trigger
              condition is ID or IDANDDATA.
        """
        return self._value


class TriggerABusBItemLinErrtype(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:LIN:ERRTYPE`` command.

    Description:
        - This command specifies the error type be used for LIN trigger. The bus number is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:ERRTYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN:ERRTYPE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN:ERRTYPE value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:LIN:ERRTYPE {SYNC|PARity|CHecksum}
        - TRIGger:A:BUS:B<x>:LIN:ERRTYPE?
        ```

    Info:
        - ``SYNC`` sets the LIN error type to SYNC.
        - ``PARity`` sets the LIN error type to parity.
        - ``CHecksum`` sets the LIN error type to checksum.
    """


class TriggerABusBItemLinDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:LIN:DATa:VALue`` command.

    Description:
        - This command specifies the binary data string to be used for LIN trigger condition if
          trigger condition is ID or IDANDDATA. The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa:VALue?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa:VALue?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:LIN:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:LIN:DATa:VALue <QString>
        - TRIGger:A:BUS:B<x>:LIN:DATa:VALue?
        ```

    Info:
        - ``<QString>`` is a quoted string that is the LIN trigger data value.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemLinDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:LIN:DATa:SIZe`` command.

    Description:
        - This command specifies the length of the data string in bytes to be used for LIN trigger.
          The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa:SIZe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:LIN:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:LIN:DATa:SIZe <NR1>
        - TRIGger:A:BUS:B<x>:LIN:DATa:SIZe?
        ```

    Info:
        - ``<NR1>`` is the size of the data string in bytes.
    """


class TriggerABusBItemLinDataQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier`` command.

    Description:
        - Sets or returns the LIN data qualifier. This only applies if the trigger condition is
          IDANDDATA or DATA.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?
        ```

    Info:
        - ``LESSThan`` sets the LIN data qualifier to less than.
        - ``MOREThan`` sets the LIN data qualifier to greater than.
        - ``EQUal`` sets the LIN data qualifier to equal.
        - ``UNEQual`` sets the LIN data qualifier to not equal.
        - ``LESSEQual`` sets the LIN data qualifier to less than or equal.
        - ``MOREEQual`` sets the LIN data qualifier to greater than or equal.
        - ``INrange`` sets the LIN data qualifier to in range.
        - ``OUTrange`` sets the LIN data qualifier to out of range.
    """  # noqa: E501


class TriggerABusBItemLinDataHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue`` command.

    Description:
        - This command specifies the high data value string used for a LIN bus trigger when the
          trigger condition is DATA or IDANDDATA and the data qualifier is INRANGE or OUTRANGE. The
          bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue?``
          query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue <QString>
        - TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue?
        ```

    Info:
        - ``<QString>`` is a quoted string that is the binary data string used for LIN trigger if
          the trigger condition is ID or IDANDDATA.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemLinData(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:LIN:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue`` command.
        - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier`` command.
        - ``.size``: The ``TRIGger:A:BUS:B<x>:LIN:DATa:SIZe`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:LIN:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = TriggerABusBItemLinDataHivalue(device, f"{self._cmd_syntax}:HIVALue")
        self._qualifier = TriggerABusBItemLinDataQualifier(device, f"{self._cmd_syntax}:QUALifier")
        self._size = TriggerABusBItemLinDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._value = TriggerABusBItemLinDataValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def hivalue(self) -> TriggerABusBItemLinDataHivalue:
        """Return the ``TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue`` command.

        Description:
            - This command specifies the high data value string used for a LIN bus trigger when the
              trigger condition is DATA or IDANDDATA and the data qualifier is INRANGE or OUTRANGE.
              The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue <QString>
            - TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue?
            ```

        Info:
            - ``<QString>`` is a quoted string that is the binary data string used for LIN trigger
              if the trigger condition is ID or IDANDDATA.
        """
        return self._hivalue

    @property
    def qualifier(self) -> TriggerABusBItemLinDataQualifier:
        """Return the ``TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier`` command.

        Description:
            - Sets or returns the LIN data qualifier. This only applies if the trigger condition is
              IDANDDATA or DATA.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?
            ```

        Info:
            - ``LESSThan`` sets the LIN data qualifier to less than.
            - ``MOREThan`` sets the LIN data qualifier to greater than.
            - ``EQUal`` sets the LIN data qualifier to equal.
            - ``UNEQual`` sets the LIN data qualifier to not equal.
            - ``LESSEQual`` sets the LIN data qualifier to less than or equal.
            - ``MOREEQual`` sets the LIN data qualifier to greater than or equal.
            - ``INrange`` sets the LIN data qualifier to in range.
            - ``OUTrange`` sets the LIN data qualifier to out of range.
        """  # noqa: E501
        return self._qualifier

    @property
    def size(self) -> TriggerABusBItemLinDataSize:
        """Return the ``TRIGger:A:BUS:B<x>:LIN:DATa:SIZe`` command.

        Description:
            - This command specifies the length of the data string in bytes to be used for LIN
              trigger. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa:SIZe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:DATa:SIZe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:DATa:SIZe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:LIN:DATa:SIZe <NR1>
            - TRIGger:A:BUS:B<x>:LIN:DATa:SIZe?
            ```

        Info:
            - ``<NR1>`` is the size of the data string in bytes.
        """
        return self._size

    @property
    def value(self) -> TriggerABusBItemLinDataValue:
        """Return the ``TRIGger:A:BUS:B<x>:LIN:DATa:VALue`` command.

        Description:
            - This command specifies the binary data string to be used for LIN trigger condition if
              trigger condition is ID or IDANDDATA. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa:VALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:DATa:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:LIN:DATa:VALue <QString>
            - TRIGger:A:BUS:B<x>:LIN:DATa:VALue?
            ```

        Info:
            - ``<QString>`` is a quoted string that is the LIN trigger data value.
        """
        return self._value


class TriggerABusBItemLinCondition(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:LIN:CONDition`` command.

    Description:
        - This command specifies the trigger condition for LIN. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN:CONDition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:LIN:CONDition value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:LIN:CONDition {SYNCField|IDentifier|DATA|IDANDDATA|WAKEup|SLEEP|ERROR}
        - TRIGger:A:BUS:B<x>:LIN:CONDition?
        ```

    Info:
        - ``SYNCField`` sets the LIN trigger condition to sync field.
        - ``IDentifier`` sets the LIN trigger condition to identifier.
        - ``DATA`` sets the LIN trigger condition to data.
        - ``IDANDDATA`` sets the LIN trigger condition to id and data.
        - ``WAKEup`` sets the LIN trigger condition to wake up.
        - ``SLEEP`` sets the LIN trigger condition to sleep.
        - ``ERROR`` sets the LIN trigger condition to error.
    """


class TriggerABusBItemLin(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:LIN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``TRIGger:A:BUS:B<x>:LIN:CONDition`` command.
        - ``.data``: The ``TRIGger:A:BUS:B<x>:LIN:DATa`` command tree.
        - ``.errtype``: The ``TRIGger:A:BUS:B<x>:LIN:ERRTYPE`` command.
        - ``.identifier``: The ``TRIGger:A:BUS:B<x>:LIN:IDentifier`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = TriggerABusBItemLinCondition(device, f"{self._cmd_syntax}:CONDition")
        self._data = TriggerABusBItemLinData(device, f"{self._cmd_syntax}:DATa")
        self._errtype = TriggerABusBItemLinErrtype(device, f"{self._cmd_syntax}:ERRTYPE")
        self._identifier = TriggerABusBItemLinIdentifier(device, f"{self._cmd_syntax}:IDentifier")

    @property
    def condition(self) -> TriggerABusBItemLinCondition:
        """Return the ``TRIGger:A:BUS:B<x>:LIN:CONDition`` command.

        Description:
            - This command specifies the trigger condition for LIN. B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:CONDition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:CONDition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:CONDition value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:LIN:CONDition {SYNCField|IDentifier|DATA|IDANDDATA|WAKEup|SLEEP|ERROR}
            - TRIGger:A:BUS:B<x>:LIN:CONDition?
            ```

        Info:
            - ``SYNCField`` sets the LIN trigger condition to sync field.
            - ``IDentifier`` sets the LIN trigger condition to identifier.
            - ``DATA`` sets the LIN trigger condition to data.
            - ``IDANDDATA`` sets the LIN trigger condition to id and data.
            - ``WAKEup`` sets the LIN trigger condition to wake up.
            - ``SLEEP`` sets the LIN trigger condition to sleep.
            - ``ERROR`` sets the LIN trigger condition to error.
        """  # noqa: E501
        return self._condition

    @property
    def data(self) -> TriggerABusBItemLinData:
        """Return the ``TRIGger:A:BUS:B<x>:LIN:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue`` command.
            - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier`` command.
            - ``.size``: The ``TRIGger:A:BUS:B<x>:LIN:DATa:SIZe`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:LIN:DATa:VALue`` command.
        """
        return self._data

    @property
    def errtype(self) -> TriggerABusBItemLinErrtype:
        """Return the ``TRIGger:A:BUS:B<x>:LIN:ERRTYPE`` command.

        Description:
            - This command specifies the error type be used for LIN trigger. The bus number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:ERRTYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN:ERRTYPE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:ERRTYPE value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:LIN:ERRTYPE {SYNC|PARity|CHecksum}
            - TRIGger:A:BUS:B<x>:LIN:ERRTYPE?
            ```

        Info:
            - ``SYNC`` sets the LIN error type to SYNC.
            - ``PARity`` sets the LIN error type to parity.
            - ``CHecksum`` sets the LIN error type to checksum.
        """
        return self._errtype

    @property
    def identifier(self) -> TriggerABusBItemLinIdentifier:
        """Return the ``TRIGger:A:BUS:B<x>:LIN:IDentifier`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:IDentifier?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:IDentifier?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue`` command.
        """
        return self._identifier


class TriggerABusBItemI2cDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:I2C:DATa:VALue`` command.

    Description:
        - This command specifies the binary data string used for I2C triggering if the trigger
          condition is DATA or ADDRANDDATA. The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:DATa:VALue?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:I2C:DATa:VALue?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:I2C:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:I2C:DATa:VALue <QString>
        - TRIGger:A:BUS:B<x>:I2C:DATa:VALue?
        ```

    Info:
        - ``<QString>`` is the binary data string, where the number of bits is 8 times the number of
          bytes specified. The only allowed characters in the string are 0, 1, and X.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemI2cDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:I2C:DATa:SIZe`` command.

    Description:
        - This command specifies the length of the data string in bytes to be used for an I2C
          trigger if the trigger condition is DATA or ADDRANDDATA. Applies to bus <x>, where the bus
          number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:DATa:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:I2C:DATa:SIZe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:I2C:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:I2C:DATa:SIZe <NR1>
        - TRIGger:A:BUS:B<x>:I2C:DATa:SIZe?
        ```

    Info:
        - ``<NR1>`` is the length of the data string in bytes.
    """


class TriggerABusBItemI2cDataDirection(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:I2C:DATa:DIRection`` command.

    Description:
        - This command specifies the I 2 C trigger type to be valid on a Read, Write, or Either
          condition. Read or write is indicated by the R/W bit in the I 2 C protocol. The bus number
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:DATa:DIRection?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:I2C:DATa:DIRection?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:I2C:DATa:DIRection value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:I2C:DATa:DIRection {READ|WRITE|NOCARE}
        - TRIGger:A:BUS:B<x>:I2C:DATa:DIRection?
        ```

    Info:
        - ``READ`` specifies read as the data direction.
        - ``WRITE`` specifies write as the data direction.
        - ``NOCARE`` specifies either as the data direction.
    """


class TriggerABusBItemI2cData(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:I2C:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:I2C:DATa?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.direction``: The ``TRIGger:A:BUS:B<x>:I2C:DATa:DIRection`` command.
        - ``.size``: The ``TRIGger:A:BUS:B<x>:I2C:DATa:SIZe`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:I2C:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._direction = TriggerABusBItemI2cDataDirection(device, f"{self._cmd_syntax}:DIRection")
        self._size = TriggerABusBItemI2cDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._value = TriggerABusBItemI2cDataValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def direction(self) -> TriggerABusBItemI2cDataDirection:
        """Return the ``TRIGger:A:BUS:B<x>:I2C:DATa:DIRection`` command.

        Description:
            - This command specifies the I 2 C trigger type to be valid on a Read, Write, or Either
              condition. Read or write is indicated by the R/W bit in the I 2 C protocol. The bus
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:DATa:DIRection?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:I2C:DATa:DIRection?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:I2C:DATa:DIRection value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:I2C:DATa:DIRection {READ|WRITE|NOCARE}
            - TRIGger:A:BUS:B<x>:I2C:DATa:DIRection?
            ```

        Info:
            - ``READ`` specifies read as the data direction.
            - ``WRITE`` specifies write as the data direction.
            - ``NOCARE`` specifies either as the data direction.
        """
        return self._direction

    @property
    def size(self) -> TriggerABusBItemI2cDataSize:
        """Return the ``TRIGger:A:BUS:B<x>:I2C:DATa:SIZe`` command.

        Description:
            - This command specifies the length of the data string in bytes to be used for an I2C
              trigger if the trigger condition is DATA or ADDRANDDATA. Applies to bus <x>, where the
              bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:DATa:SIZe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:I2C:DATa:SIZe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:I2C:DATa:SIZe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:I2C:DATa:SIZe <NR1>
            - TRIGger:A:BUS:B<x>:I2C:DATa:SIZe?
            ```

        Info:
            - ``<NR1>`` is the length of the data string in bytes.
        """
        return self._size

    @property
    def value(self) -> TriggerABusBItemI2cDataValue:
        """Return the ``TRIGger:A:BUS:B<x>:I2C:DATa:VALue`` command.

        Description:
            - This command specifies the binary data string used for I2C triggering if the trigger
              condition is DATA or ADDRANDDATA. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:DATa:VALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:I2C:DATa:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:I2C:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:I2C:DATa:VALue <QString>
            - TRIGger:A:BUS:B<x>:I2C:DATa:VALue?
            ```

        Info:
            - ``<QString>`` is the binary data string, where the number of bits is 8 times the
              number of bytes specified. The only allowed characters in the string are 0, 1, and X.
        """
        return self._value


class TriggerABusBItemI2cCondition(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:I2C:CONDition`` command.

    Description:
        - This command specifies the trigger condition for an I 2 C trigger. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:I2C:CONDition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:I2C:CONDition value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:I2C:CONDition {STARt|STOP|REPEATstart|ACKMISS|ADDRess|DATA|ADDRANDDATA}
        - TRIGger:A:BUS:B<x>:I2C:CONDition?
        ```

    Info:
        - ``STARt`` specifies a search based on start condition.
        - ``STOP`` specifies a search based on stop condition.
        - ``REPEATstart`` specifies a search based on repeat of start condition.
        - ``ACKMISS`` specifies a search based on missing acknowledgement condition.
        - ``ADDRess`` specifies a search based on address.
        - ``DATA`` specifies a search based on data.
        - ``ADDRANDDATA`` specifies a search based on address and data.
    """


class TriggerABusBItemI2cAddressValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue`` command.

    Description:
        - This command specifies the binary address string used for the I 2 C trigger if the trigger
          condition is ADDRESS or ADDRANDDATA. The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue <QString>
        - TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue?
        ```

    Info:
        - ``<QString>`` is up to 7 or 10-bits depending on the address mode that specifies the
          address. The only allowed characters in the QString are 0, 1, and X.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemI2cAddressType(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe`` command.

    Description:
        - This command specifies the I 2 C address type. The only supported address type is USER.
          Applies to bus <x>, where x

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe?``
          query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe {GENeralcall|STARtbyte|HSmode|EEPROM|USER}
        - TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe?
        ```

    Info:
        - ``GENeralcall`` specifies a general call address.
        - ``STARtbyte`` specifies a start byte address.
        - ``HSmode`` specifies a high-speed mode address.
        - ``EEPROM`` specifies an EEPROM address.
        - ``USER`` specifies a user address.
    """


class TriggerABusBItemI2cAddressMode(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe`` command.

    Description:
        - This command specifies the I 2 C address mode to 7 or 10-bit. The bus number is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe?``
          query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe {ADDR7|ADDR10}
        - TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe?
        ```

    Info:
        - ``ADDR7`` specifies the 7-bit I2C address mode.
        - ``ADDR10`` specifies the 10-bit I2C address mode.
    """


class TriggerABusBItemI2cAddress(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:I2C:ADDRess`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:ADDRess?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:I2C:ADDRess?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.mode``: The ``TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe`` command.
        - ``.type``: The ``TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = TriggerABusBItemI2cAddressMode(device, f"{self._cmd_syntax}:MODe")
        self._type = TriggerABusBItemI2cAddressType(device, f"{self._cmd_syntax}:TYPe")
        self._value = TriggerABusBItemI2cAddressValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def mode(self) -> TriggerABusBItemI2cAddressMode:
        """Return the ``TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe`` command.

        Description:
            - This command specifies the I 2 C address mode to 7 or 10-bit. The bus number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe {ADDR7|ADDR10}
            - TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe?
            ```

        Info:
            - ``ADDR7`` specifies the 7-bit I2C address mode.
            - ``ADDR10`` specifies the 10-bit I2C address mode.
        """
        return self._mode

    @property
    def type(self) -> TriggerABusBItemI2cAddressType:
        """Return the ``TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe`` command.

        Description:
            - This command specifies the I 2 C address type. The only supported address type is
              USER. Applies to bus <x>, where x

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe {GENeralcall|STARtbyte|HSmode|EEPROM|USER}
            - TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe?
            ```

        Info:
            - ``GENeralcall`` specifies a general call address.
            - ``STARtbyte`` specifies a start byte address.
            - ``HSmode`` specifies a high-speed mode address.
            - ``EEPROM`` specifies an EEPROM address.
            - ``USER`` specifies a user address.
        """
        return self._type

    @property
    def value(self) -> TriggerABusBItemI2cAddressValue:
        """Return the ``TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue`` command.

        Description:
            - This command specifies the binary address string used for the I 2 C trigger if the
              trigger condition is ADDRESS or ADDRANDDATA. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue <QString>
            - TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue?
            ```

        Info:
            - ``<QString>`` is up to 7 or 10-bits depending on the address mode that specifies the
              address. The only allowed characters in the QString are 0, 1, and X.
        """
        return self._value


class TriggerABusBItemI2c(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:I2C`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:I2C?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.address``: The ``TRIGger:A:BUS:B<x>:I2C:ADDRess`` command tree.
        - ``.condition``: The ``TRIGger:A:BUS:B<x>:I2C:CONDition`` command.
        - ``.data``: The ``TRIGger:A:BUS:B<x>:I2C:DATa`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._address = TriggerABusBItemI2cAddress(device, f"{self._cmd_syntax}:ADDRess")
        self._condition = TriggerABusBItemI2cCondition(device, f"{self._cmd_syntax}:CONDition")
        self._data = TriggerABusBItemI2cData(device, f"{self._cmd_syntax}:DATa")

    @property
    def address(self) -> TriggerABusBItemI2cAddress:
        """Return the ``TRIGger:A:BUS:B<x>:I2C:ADDRess`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:ADDRess?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:I2C:ADDRess?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.mode``: The ``TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe`` command.
            - ``.type``: The ``TRIGger:A:BUS:B<x>:I2C:ADDRess:TYPe`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue`` command.
        """
        return self._address

    @property
    def condition(self) -> TriggerABusBItemI2cCondition:
        """Return the ``TRIGger:A:BUS:B<x>:I2C:CONDition`` command.

        Description:
            - This command specifies the trigger condition for an I 2 C trigger. B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:CONDition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:I2C:CONDition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:I2C:CONDition value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:I2C:CONDition {STARt|STOP|REPEATstart|ACKMISS|ADDRess|DATA|ADDRANDDATA}
            - TRIGger:A:BUS:B<x>:I2C:CONDition?
            ```

        Info:
            - ``STARt`` specifies a search based on start condition.
            - ``STOP`` specifies a search based on stop condition.
            - ``REPEATstart`` specifies a search based on repeat of start condition.
            - ``ACKMISS`` specifies a search based on missing acknowledgement condition.
            - ``ADDRess`` specifies a search based on address.
            - ``DATA`` specifies a search based on data.
            - ``ADDRANDDATA`` specifies a search based on address and data.
        """  # noqa: E501
        return self._condition

    @property
    def data(self) -> TriggerABusBItemI2cData:
        """Return the ``TRIGger:A:BUS:B<x>:I2C:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:I2C:DATa?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.direction``: The ``TRIGger:A:BUS:B<x>:I2C:DATa:DIRection`` command.
            - ``.size``: The ``TRIGger:A:BUS:B<x>:I2C:DATa:SIZe`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:I2C:DATa:VALue`` command.
        """
        return self._data


class TriggerABusBItemFlexrayHeaderPaylength(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength`` command.

    Description:
        - This command specifies the payload length portion of the binary header string when
          triggering on the FlexRay bus header. The trigger condition needs to be set to HEADer
          (using ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength <QString>
        - TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength?
        ```

    Info:
        - ``<QString>`` is the length of the payload portion of the Binary header string.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemFlexrayHeaderIndbits(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits`` command.

    Description:
        - This command specifies the indicator bits portion of the binary header string when
          triggering on the FlexRay bus header. The trigger condition needs to be set to HEADer
          (using ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits <QString>
        - TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits?
        ```

    Info:
        - ``<QString>`` is a quoted string that is the indicator bits portion of the binary header
          string.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemFlexrayHeaderFrameid(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID`` command.

    Description:
        - This command specifies the frame ID portion of the binary header string when triggering on
          the FlexRay bus header. The trigger condition needs to be set to HEADer (using
          ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID <QString>
        - TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID?
        ```

    Info:
        - ``<QString>`` is a quoted string that represents the frame ID portion of the binary header
          string.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemFlexrayHeaderCyclecount(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount`` command.

    Description:
        - This command specifies the cycle count portion of the binary header string when triggering
          on the FlexRay bus header. The trigger condition needs to be set to HEADer (using
          ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount <QString>
        - TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount?
        ```

    Info:
        - ``<QString>`` is a quoted string that is the cycle count portion of the binary header
          string.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemFlexrayHeaderCrc(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC`` command.

    Description:
        - This command specifies the CRC portion of the binary header string when triggering on the
          FlexRay bus signal. The trigger condition needs to be set to HEADer (using
          ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC <QString>
        - TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC?
        ```

    Info:
        - ``<QString>`` is a quoted string that is the CRC portion of the binary header string.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemFlexrayHeader(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:FLEXray:HEADER`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:HEADER?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:HEADER?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.crc``: The ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC`` command.
        - ``.cyclecount``: The ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount`` command.
        - ``.frameid``: The ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID`` command.
        - ``.indbits``: The ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits`` command.
        - ``.paylength``: The ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._crc = TriggerABusBItemFlexrayHeaderCrc(device, f"{self._cmd_syntax}:CRC")
        self._cyclecount = TriggerABusBItemFlexrayHeaderCyclecount(
            device, f"{self._cmd_syntax}:CYCLEcount"
        )
        self._frameid = TriggerABusBItemFlexrayHeaderFrameid(device, f"{self._cmd_syntax}:FRAMEID")
        self._indbits = TriggerABusBItemFlexrayHeaderIndbits(device, f"{self._cmd_syntax}:INDBits")
        self._paylength = TriggerABusBItemFlexrayHeaderPaylength(
            device, f"{self._cmd_syntax}:PAYLength"
        )

    @property
    def crc(self) -> TriggerABusBItemFlexrayHeaderCrc:
        """Return the ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC`` command.

        Description:
            - This command specifies the CRC portion of the binary header string when triggering on
              the FlexRay bus signal. The trigger condition needs to be set to HEADer (using
              ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC <QString>
            - TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC?
            ```

        Info:
            - ``<QString>`` is a quoted string that is the CRC portion of the binary header string.
        """
        return self._crc

    @property
    def cyclecount(self) -> TriggerABusBItemFlexrayHeaderCyclecount:
        """Return the ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount`` command.

        Description:
            - This command specifies the cycle count portion of the binary header string when
              triggering on the FlexRay bus header. The trigger condition needs to be set to HEADer
              (using ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount <QString>
            - TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount?
            ```

        Info:
            - ``<QString>`` is a quoted string that is the cycle count portion of the binary header
              string.
        """
        return self._cyclecount

    @property
    def frameid(self) -> TriggerABusBItemFlexrayHeaderFrameid:
        """Return the ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID`` command.

        Description:
            - This command specifies the frame ID portion of the binary header string when
              triggering on the FlexRay bus header. The trigger condition needs to be set to HEADer
              (using ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID <QString>
            - TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID?
            ```

        Info:
            - ``<QString>`` is a quoted string that represents the frame ID portion of the binary
              header string.
        """
        return self._frameid

    @property
    def indbits(self) -> TriggerABusBItemFlexrayHeaderIndbits:
        """Return the ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits`` command.

        Description:
            - This command specifies the indicator bits portion of the binary header string when
              triggering on the FlexRay bus header. The trigger condition needs to be set to HEADer
              (using ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits <QString>
            - TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits?
            ```

        Info:
            - ``<QString>`` is a quoted string that is the indicator bits portion of the binary
              header string.
        """
        return self._indbits

    @property
    def paylength(self) -> TriggerABusBItemFlexrayHeaderPaylength:
        """Return the ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength`` command.

        Description:
            - This command specifies the payload length portion of the binary header string when
              triggering on the FlexRay bus header. The trigger condition needs to be set to HEADer
              (using ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength <QString>
            - TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength?
            ```

        Info:
            - ``<QString>`` is the length of the payload portion of the Binary header string.
        """
        return self._paylength


class TriggerABusBItemFlexrayFrametype(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEType`` command.

    Description:
        - This command specifies the frame type (normal, payload, null, sync or startup) when
          triggering on the FlexRay bus signal. The trigger condition needs to be set to FRAMEType
          (using ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEType?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEType?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEType value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:FLEXray:FRAMEType {NORMal|PAYLoad|NULL|SYNC|STARTup}
        - TRIGger:A:BUS:B<x>:FLEXray:FRAMEType?
        ```

    Info:
        - ``NORMal`` specifies the normal frame type.
        - ``PAYLoad`` specifies the payload frame type.
        - ``NULL`` specifies the null frame type.
        - ``SYNC`` specifies the sync frame type.
        - ``STARTup`` specifies the startup frame type.
    """


class TriggerABusBItemFlexrayFrameidValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue`` command.

    Description:
        - This command specifies the low value when triggering on the FlexRay bus frame ID field.
          (Use ``TRIGGER:A:BUS:BX:FLEXRAY:FRAMEID:HIVALUE`` to set the high value.) The trigger
          condition needs to be set to IDentifier (using ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``).
          B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue <QString>
        - TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue?
        ```

    Info:
        - ``<QString>`` is a quoted string that is the FlexRay frame ID low value.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemFlexrayFrameidQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier`` command.

    Description:
        - Sets or returns the FLEXRAY frame ID qualifier.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier?
        ```

    Info:
        - ``LESSThan`` sets the frame id qualifier to less than.
        - ``MOREThan`` sets the frame id qualifier to greater than.
        - ``EQUal`` sets the frame id qualifier to equal.
        - ``UNEQual`` sets the frame id qualifier to not equal.
        - ``LESSEQual`` sets the frame id qualifier to less than or equal.
        - ``MOREEQual`` sets the frame id qualifier to greater than or equal.
        - ``INrange`` sets the frame id qualifier to in range.
        - ``OUTrange`` sets the frame id qualifier to out of range.
    """  # noqa: E501


class TriggerABusBItemFlexrayFrameidHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue`` command.

    Description:
        - This command specifies the high value when triggering on the FlexRay bus frame ID field.
          (Use ``TRIGGER:A:BUS:BX:FLEXRAY:FRAMEID:VALUE`` to set the low value.) The trigger
          condition needs to be set to IDentifier (using ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``).
          B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue <QString>
        - TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue?
        ```

    Info:
        - ``<QString>`` is a quoted string that is the binary frame ID high value.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemFlexrayFrameid(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue`` command.
        - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = TriggerABusBItemFlexrayFrameidHivalue(device, f"{self._cmd_syntax}:HIVALue")
        self._qualifier = TriggerABusBItemFlexrayFrameidQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._value = TriggerABusBItemFlexrayFrameidValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def hivalue(self) -> TriggerABusBItemFlexrayFrameidHivalue:
        """Return the ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue`` command.

        Description:
            - This command specifies the high value when triggering on the FlexRay bus frame ID
              field. (Use ``TRIGGER:A:BUS:BX:FLEXRAY:FRAMEID:VALUE`` to set the low value.) The
              trigger condition needs to be set to IDentifier (using
              ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue <QString>
            - TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue?
            ```

        Info:
            - ``<QString>`` is a quoted string that is the binary frame ID high value.
        """
        return self._hivalue

    @property
    def qualifier(self) -> TriggerABusBItemFlexrayFrameidQualifier:
        """Return the ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier`` command.

        Description:
            - Sets or returns the FLEXRAY frame ID qualifier.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier?
            ```

        Info:
            - ``LESSThan`` sets the frame id qualifier to less than.
            - ``MOREThan`` sets the frame id qualifier to greater than.
            - ``EQUal`` sets the frame id qualifier to equal.
            - ``UNEQual`` sets the frame id qualifier to not equal.
            - ``LESSEQual`` sets the frame id qualifier to less than or equal.
            - ``MOREEQual`` sets the frame id qualifier to greater than or equal.
            - ``INrange`` sets the frame id qualifier to in range.
            - ``OUTrange`` sets the frame id qualifier to out of range.
        """  # noqa: E501
        return self._qualifier

    @property
    def value(self) -> TriggerABusBItemFlexrayFrameidValue:
        """Return the ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue`` command.

        Description:
            - This command specifies the low value when triggering on the FlexRay bus frame ID
              field. (Use ``TRIGGER:A:BUS:BX:FLEXRAY:FRAMEID:HIVALUE`` to set the high value.) The
              trigger condition needs to be set to IDentifier (using
              ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue <QString>
            - TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue?
            ```

        Info:
            - ``<QString>`` is a quoted string that is the FlexRay frame ID low value.
        """
        return self._value


class TriggerABusBItemFlexrayErrtype(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE`` command.

    Description:
        - This command specifies the error type when triggering on the FlexRay bus signal. The
          trigger condition needs to be set to ERROR (using ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``).
          B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE {CRCHeader|CRCTrailer|SYNCFrame|STARTupnosync|NULLFRStatic|NULLFRDynamic}
        - TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE?
        ```

    Info:
        - ``CRCHeader`` sets the error type to CRCHeader.
        - ``CRCTrailer`` sets the error type to CRCTrailer.
        - ``SYNCFrame`` sets the error type to SYNCFrame.
        - ``STARTupnosync`` sets the error type to STARTupnosync.
        - ``NULLFRStatic`` sets the error type to NULLFRStatic.
        - ``NULLFRDynamic`` sets the error type to NULLFRDynamic.
    """  # noqa: E501


class TriggerABusBItemFlexrayEoftype(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE`` command.

    Description:
        - This command specifies the end of file type (static, dynamic or any) when triggering on
          the FlexRay bus EOF field. The trigger condition needs to be set to EOF (using
          ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE {STATic|DYNAMic|ANY}
        - TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE?
        ```

    Info:
        - ``STATic`` specifies triggering on the STATIC end of file type.
        - ``DYNAMic`` specifies triggering on the DYNAMIC end of file type.
        - ``ANY`` specifies triggering on a STATIC or DYNAMIC end of file type.
    """


class TriggerABusBItemFlexrayDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue`` command.

    Description:
        - This command specifies the low value when triggering on the FlexRay bus data field. (Use
          ``TRIGGER:A:BUS:BX:FLEXRAY:DATA:HIVALUE`` to set the upper value.) The trigger condition
          needs to be set to ID or IDANDDATA (using ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue <QString>
        - TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue?
        ```

    Info:
        - ``<QString>`` is a quoted string.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemFlexrayDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe`` command.

    Description:
        - This command specifies the length of the data string, in bytes, when triggering on the
          FlexRay bus data field. The trigger condition needs to be set to ID or IDANDDATA (using
          ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe <NR1>
        - TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe?
        ```

    Info:
        - ``<NR1>`` is the FlexRay data string length, in bytes.
    """


class TriggerABusBItemFlexrayDataQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier`` command.

    Description:
        - Sets or returns the FLEXRAY data qualifier.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier?
        ```

    Info:
        - ``LESSThan`` sets the FLEXRAY data qualifier to less than.
        - ``MOREThan`` sets the FLEXRAY data qualifier to greater than.
        - ``EQUal`` sets the FLEXRAY data qualifier to eqaual.
        - ``UNEQual`` sets the FLEXRAY data qualifier to not equal.
        - ``LESSEQual`` sets the FLEXRAY data qualifier to less than or equal.
        - ``MOREEQual`` sets the FLEXRAY data qualifier to greater than or equal.
        - ``INrange`` sets the FLEXRAY data qualifier to in range.
        - ``OUTrange`` sets the FLEXRAY data qualifier to out of range.
    """  # noqa: E501


class TriggerABusBItemFlexrayDataOffset(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet`` command.

    Description:
        - This command specifies the offset of the data string, in bytes, when triggering on the
          FlexRay bus data field. The trigger condition needs to be set to ID or IDANDDATA (using
          ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet <NR1>
        - TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet?
        ```

    Info:
        - ``<NR1>`` is the offset of the data string in bytes. A byte offset of -1 signifies 'don't
          care', and no byte offset is used. The instrument will trigger on or match any byte value
          that fits.
    """


class TriggerABusBItemFlexrayDataHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue`` command.

    Description:
        - This command specifies the high value when triggering on the FlexRay bus data field. (Use
          ``TRIGGER:A:BUS:BX:FLEXRAY:DATA:VALUE`` to set the lower value.) The trigger condition
          needs to be set to ID or IDANDDATA (using ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue <QString>
        - TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue?
        ```

    Info:
        - ``<QString>`` is a quoted string that is the binary data high value.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemFlexrayData(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:FLEXray:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:DATa?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue`` command.
        - ``.offset``: The ``TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet`` command.
        - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier`` command.
        - ``.size``: The ``TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = TriggerABusBItemFlexrayDataHivalue(device, f"{self._cmd_syntax}:HIVALue")
        self._offset = TriggerABusBItemFlexrayDataOffset(device, f"{self._cmd_syntax}:OFFSet")
        self._qualifier = TriggerABusBItemFlexrayDataQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._size = TriggerABusBItemFlexrayDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._value = TriggerABusBItemFlexrayDataValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def hivalue(self) -> TriggerABusBItemFlexrayDataHivalue:
        """Return the ``TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue`` command.

        Description:
            - This command specifies the high value when triggering on the FlexRay bus data field.
              (Use ``TRIGGER:A:BUS:BX:FLEXRAY:DATA:VALUE`` to set the lower value.) The trigger
              condition needs to be set to ID or IDANDDATA (using
              ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue <QString>
            - TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue?
            ```

        Info:
            - ``<QString>`` is a quoted string that is the binary data high value.
        """
        return self._hivalue

    @property
    def offset(self) -> TriggerABusBItemFlexrayDataOffset:
        """Return the ``TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet`` command.

        Description:
            - This command specifies the offset of the data string, in bytes, when triggering on the
              FlexRay bus data field. The trigger condition needs to be set to ID or IDANDDATA
              (using ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet <NR1>
            - TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet?
            ```

        Info:
            - ``<NR1>`` is the offset of the data string in bytes. A byte offset of -1 signifies
              'don't care', and no byte offset is used. The instrument will trigger on or match any
              byte value that fits.
        """
        return self._offset

    @property
    def qualifier(self) -> TriggerABusBItemFlexrayDataQualifier:
        """Return the ``TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier`` command.

        Description:
            - Sets or returns the FLEXRAY data qualifier.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier?
            ```

        Info:
            - ``LESSThan`` sets the FLEXRAY data qualifier to less than.
            - ``MOREThan`` sets the FLEXRAY data qualifier to greater than.
            - ``EQUal`` sets the FLEXRAY data qualifier to eqaual.
            - ``UNEQual`` sets the FLEXRAY data qualifier to not equal.
            - ``LESSEQual`` sets the FLEXRAY data qualifier to less than or equal.
            - ``MOREEQual`` sets the FLEXRAY data qualifier to greater than or equal.
            - ``INrange`` sets the FLEXRAY data qualifier to in range.
            - ``OUTrange`` sets the FLEXRAY data qualifier to out of range.
        """  # noqa: E501
        return self._qualifier

    @property
    def size(self) -> TriggerABusBItemFlexrayDataSize:
        """Return the ``TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe`` command.

        Description:
            - This command specifies the length of the data string, in bytes, when triggering on the
              FlexRay bus data field. The trigger condition needs to be set to ID or IDANDDATA
              (using ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe <NR1>
            - TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe?
            ```

        Info:
            - ``<NR1>`` is the FlexRay data string length, in bytes.
        """
        return self._size

    @property
    def value(self) -> TriggerABusBItemFlexrayDataValue:
        """Return the ``TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue`` command.

        Description:
            - This command specifies the low value when triggering on the FlexRay bus data field.
              (Use ``TRIGGER:A:BUS:BX:FLEXRAY:DATA:HIVALUE`` to set the upper value.) The trigger
              condition needs to be set to ID or IDANDDATA (using
              ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue <QString>
            - TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue?
            ```

        Info:
            - ``<QString>`` is a quoted string.
        """
        return self._value


class TriggerABusBItemFlexrayCyclecountValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue`` command.

    Description:
        - This command specifies the low value when triggering on the FlexRay bus cycle count field.
          (Use ``TRIGGER:A:BUS:BX:FLEXRAY:CYCLECOUNT:HIVALUE`` to set the upper value.) The trigger
          condition must be set to CYCLEcount (using ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue <QString>
        - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue?
        ```

    Info:
        - ``<QString>`` is a quoted binary data string that represents the cycle count low value.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemFlexrayCyclecountQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier`` command.

    Description:
        - Sets or returns the FLEXRAY cycle count qualifier.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier?
        ```

    Info:
        - ``LESSThan`` sets the FLEXRAY cycle count qualifier to less than.
        - ``MOREThan`` sets the FLEXRAY cycle count qualifier to more than.
        - ``EQUal`` sets the FLEXRAY cycle count qualifier to equal.
        - ``UNEQual`` sets the FLEXRAY cycle count qualifier to not equal.
        - ``LESSEQual`` sets the FLEXRAY cycle count qualifier to less than or equal.
        - ``MOREEQual`` sets the FLEXRAY cycle count qualifier to greater than or equal.
        - ``INrange`` sets the FLEXRAY cycle count qualifier to in range.
        - ``OUTrange`` sets the FLEXRAY cycle count qualifier to out of range.
    """  # noqa: E501


class TriggerABusBItemFlexrayCyclecountHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue`` command.

    Description:
        - This command specifies the high value when triggering on a FlexRay bus cycle count field.
          (Use ``TRIGGER:A:BUS:BX:FLEXRAY:CYCLECOUNT:VALUE`` to set the low value.) The trigger
          condition must be set to CYCLEcount (using ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue <QString>
        - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue?
        ```

    Info:
        - ``<QString>`` is a quoted string that is the cycle count high value.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemFlexrayCyclecount(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue`` command.
        - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = TriggerABusBItemFlexrayCyclecountHivalue(
            device, f"{self._cmd_syntax}:HIVALue"
        )
        self._qualifier = TriggerABusBItemFlexrayCyclecountQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._value = TriggerABusBItemFlexrayCyclecountValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def hivalue(self) -> TriggerABusBItemFlexrayCyclecountHivalue:
        """Return the ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue`` command.

        Description:
            - This command specifies the high value when triggering on a FlexRay bus cycle count
              field. (Use ``TRIGGER:A:BUS:BX:FLEXRAY:CYCLECOUNT:VALUE`` to set the low value.) The
              trigger condition must be set to CYCLEcount (using
              ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue <QString>
            - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue?
            ```

        Info:
            - ``<QString>`` is a quoted string that is the cycle count high value.
        """
        return self._hivalue

    @property
    def qualifier(self) -> TriggerABusBItemFlexrayCyclecountQualifier:
        """Return the ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier`` command.

        Description:
            - Sets or returns the FLEXRAY cycle count qualifier.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier?
            ```

        Info:
            - ``LESSThan`` sets the FLEXRAY cycle count qualifier to less than.
            - ``MOREThan`` sets the FLEXRAY cycle count qualifier to more than.
            - ``EQUal`` sets the FLEXRAY cycle count qualifier to equal.
            - ``UNEQual`` sets the FLEXRAY cycle count qualifier to not equal.
            - ``LESSEQual`` sets the FLEXRAY cycle count qualifier to less than or equal.
            - ``MOREEQual`` sets the FLEXRAY cycle count qualifier to greater than or equal.
            - ``INrange`` sets the FLEXRAY cycle count qualifier to in range.
            - ``OUTrange`` sets the FLEXRAY cycle count qualifier to out of range.
        """  # noqa: E501
        return self._qualifier

    @property
    def value(self) -> TriggerABusBItemFlexrayCyclecountValue:
        """Return the ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue`` command.

        Description:
            - This command specifies the low value when triggering on the FlexRay bus cycle count
              field. (Use ``TRIGGER:A:BUS:BX:FLEXRAY:CYCLECOUNT:HIVALUE`` to set the upper value.)
              The trigger condition must be set to CYCLEcount (using
              ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue <QString>
            - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue?
            ```

        Info:
            - ``<QString>`` is a quoted binary data string that represents the cycle count low
              value.
        """
        return self._value


class TriggerABusBItemFlexrayCondition(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:FLEXray:CONDition`` command.

    Description:
        - This command specifies the condition to use when triggering on a FlexRay bus signal (start
          of frame, frame type, ID, cycle count, header, data, ID and data, EOF, error). B<x> is the
          bus number B1-B2.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:CONDition?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:CONDition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:FLEXray:CONDition value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:FLEXray:CONDition {SOF|FRAMEType|IDentifier|CYCLEcount|HEADer|DATA|IDANDDATA|EOF|ERROR}
        - TRIGger:A:BUS:B<x>:FLEXray:CONDition?
        ```

    Info:
        - ``SOF`` sets the trigger condition to start of frame.
        - ``FRAMEType`` sets the trigger condition to frame type.
        - ``IDentifier`` sets the trigger condition to identifier.
        - ``CYCLEcount`` sets the trigger condition to cycle count.
        - ``HEADer`` sets the trigger condition to header.
        - ``DATA`` sets the trigger condition to data.
        - ``IDANDDATA`` sets the trigger condition to id and data.
        - ``EOF`` sets the trigger condition to end of frame.
        - ``ERROR`` sets the trigger condition to error.
    """  # noqa: E501


#  pylint: disable=too-many-instance-attributes
class TriggerABusBItemFlexray(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:FLEXray`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``TRIGger:A:BUS:B<x>:FLEXray:CONDition`` command.
        - ``.cyclecount``: The ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount`` command tree.
        - ``.data``: The ``TRIGger:A:BUS:B<x>:FLEXray:DATa`` command tree.
        - ``.eoftype``: The ``TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE`` command.
        - ``.errtype``: The ``TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE`` command.
        - ``.frameid``: The ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID`` command tree.
        - ``.frametype``: The ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEType`` command.
        - ``.header``: The ``TRIGger:A:BUS:B<x>:FLEXray:HEADER`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = TriggerABusBItemFlexrayCondition(device, f"{self._cmd_syntax}:CONDition")
        self._cyclecount = TriggerABusBItemFlexrayCyclecount(
            device, f"{self._cmd_syntax}:CYCLEcount"
        )
        self._data = TriggerABusBItemFlexrayData(device, f"{self._cmd_syntax}:DATa")
        self._eoftype = TriggerABusBItemFlexrayEoftype(device, f"{self._cmd_syntax}:EOFTYPE")
        self._errtype = TriggerABusBItemFlexrayErrtype(device, f"{self._cmd_syntax}:ERRTYPE")
        self._frameid = TriggerABusBItemFlexrayFrameid(device, f"{self._cmd_syntax}:FRAMEID")
        self._frametype = TriggerABusBItemFlexrayFrametype(device, f"{self._cmd_syntax}:FRAMEType")
        self._header = TriggerABusBItemFlexrayHeader(device, f"{self._cmd_syntax}:HEADER")

    @property
    def condition(self) -> TriggerABusBItemFlexrayCondition:
        """Return the ``TRIGger:A:BUS:B<x>:FLEXray:CONDition`` command.

        Description:
            - This command specifies the condition to use when triggering on a FlexRay bus signal
              (start of frame, frame type, ID, cycle count, header, data, ID and data, EOF, error).
              B<x> is the bus number B1-B2.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:CONDition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:CONDition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:CONDition value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:FLEXray:CONDition {SOF|FRAMEType|IDentifier|CYCLEcount|HEADer|DATA|IDANDDATA|EOF|ERROR}
            - TRIGger:A:BUS:B<x>:FLEXray:CONDition?
            ```

        Info:
            - ``SOF`` sets the trigger condition to start of frame.
            - ``FRAMEType`` sets the trigger condition to frame type.
            - ``IDentifier`` sets the trigger condition to identifier.
            - ``CYCLEcount`` sets the trigger condition to cycle count.
            - ``HEADer`` sets the trigger condition to header.
            - ``DATA`` sets the trigger condition to data.
            - ``IDANDDATA`` sets the trigger condition to id and data.
            - ``EOF`` sets the trigger condition to end of frame.
            - ``ERROR`` sets the trigger condition to error.
        """  # noqa: E501
        return self._condition

    @property
    def cyclecount(self) -> TriggerABusBItemFlexrayCyclecount:
        """Return the ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue`` command.
            - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue`` command.
        """
        return self._cyclecount

    @property
    def data(self) -> TriggerABusBItemFlexrayData:
        """Return the ``TRIGger:A:BUS:B<x>:FLEXray:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:DATa?``
              query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:DATa?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue`` command.
            - ``.offset``: The ``TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet`` command.
            - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier`` command.
            - ``.size``: The ``TRIGger:A:BUS:B<x>:FLEXray:DATa:SIZe`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:FLEXray:DATa:VALue`` command.
        """
        return self._data

    @property
    def eoftype(self) -> TriggerABusBItemFlexrayEoftype:
        """Return the ``TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE`` command.

        Description:
            - This command specifies the end of file type (static, dynamic or any) when triggering
              on the FlexRay bus EOF field. The trigger condition needs to be set to EOF (using
              ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE {STATic|DYNAMic|ANY}
            - TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE?
            ```

        Info:
            - ``STATic`` specifies triggering on the STATIC end of file type.
            - ``DYNAMic`` specifies triggering on the DYNAMIC end of file type.
            - ``ANY`` specifies triggering on a STATIC or DYNAMIC end of file type.
        """
        return self._eoftype

    @property
    def errtype(self) -> TriggerABusBItemFlexrayErrtype:
        """Return the ``TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE`` command.

        Description:
            - This command specifies the error type when triggering on the FlexRay bus signal. The
              trigger condition needs to be set to ERROR (using
              ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE {CRCHeader|CRCTrailer|SYNCFrame|STARTupnosync|NULLFRStatic|NULLFRDynamic}
            - TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE?
            ```

        Info:
            - ``CRCHeader`` sets the error type to CRCHeader.
            - ``CRCTrailer`` sets the error type to CRCTrailer.
            - ``SYNCFrame`` sets the error type to SYNCFrame.
            - ``STARTupnosync`` sets the error type to STARTupnosync.
            - ``NULLFRStatic`` sets the error type to NULLFRStatic.
            - ``NULLFRDynamic`` sets the error type to NULLFRDynamic.
        """  # noqa: E501
        return self._errtype

    @property
    def frameid(self) -> TriggerABusBItemFlexrayFrameid:
        """Return the ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:HIVALue`` command.
            - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:VALue`` command.
        """
        return self._frameid

    @property
    def frametype(self) -> TriggerABusBItemFlexrayFrametype:
        """Return the ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEType`` command.

        Description:
            - This command specifies the frame type (normal, payload, null, sync or startup) when
              triggering on the FlexRay bus signal. The trigger condition needs to be set to
              FRAMEType (using ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEType?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEType?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEType value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:FLEXray:FRAMEType {NORMal|PAYLoad|NULL|SYNC|STARTup}
            - TRIGger:A:BUS:B<x>:FLEXray:FRAMEType?
            ```

        Info:
            - ``NORMal`` specifies the normal frame type.
            - ``PAYLoad`` specifies the payload frame type.
            - ``NULL`` specifies the null frame type.
            - ``SYNC`` specifies the sync frame type.
            - ``STARTup`` specifies the startup frame type.
        """
        return self._frametype

    @property
    def header(self) -> TriggerABusBItemFlexrayHeader:
        """Return the ``TRIGger:A:BUS:B<x>:FLEXray:HEADER`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray:HEADER?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:FLEXray:HEADER?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.crc``: The ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:CRC`` command.
            - ``.cyclecount``: The ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:CYCLEcount`` command.
            - ``.frameid``: The ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:FRAMEID`` command.
            - ``.indbits``: The ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:INDBits`` command.
            - ``.paylength``: The ``TRIGger:A:BUS:B<x>:FLEXray:HEADER:PAYLength`` command.
        """
        return self._header


class TriggerABusBItemCanIdentifierValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue`` command.

    Description:
        - This command sets the binary address value to be used when triggering on a CAN bus signal.
          The trigger condition must be set to IDANDDATA OR DATA (using
          ``TRIGGER:A:BUS:BX:CAN:CONDITION``). B<x> is the bus number (1-2).

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue <QString>
        - TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue?
        ```

    Info:
        - ``<QString>`` is up to 29 bits specifying the binary identifier value. The only allowed
          characters in the QString are 0, 1, and X.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemCanIdentifierMode(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe`` command.

    Description:
        - Sets or returns the CAN addressing mode for bus <x>, where x is the bus number.Use this
          command to do the following: Trigger on ID Trigger in IDANDDATA

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe {STandard|EXTended}
        - TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?
        ```

    Info:
        - ``STandard`` specifies the standard addressing mode.
        - ``EXTended`` specifies the extended addressing mode.
    """


class TriggerABusBItemCanIdentifier(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:IDentifier`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:IDentifier?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:IDentifier?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.mode``: The ``TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = TriggerABusBItemCanIdentifierMode(device, f"{self._cmd_syntax}:MODe")
        self._value = TriggerABusBItemCanIdentifierValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def mode(self) -> TriggerABusBItemCanIdentifierMode:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe`` command.

        Description:
            - Sets or returns the CAN addressing mode for bus <x>, where x is the bus number.Use
              this command to do the following: Trigger on ID Trigger in IDANDDATA

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe {STandard|EXTended}
            - TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?
            ```

        Info:
            - ``STandard`` specifies the standard addressing mode.
            - ``EXTended`` specifies the extended addressing mode.
        """
        return self._mode

    @property
    def value(self) -> TriggerABusBItemCanIdentifierValue:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue`` command.

        Description:
            - This command sets the binary address value to be used when triggering on a CAN bus
              signal. The trigger condition must be set to IDANDDATA OR DATA (using
              ``TRIGGER:A:BUS:BX:CAN:CONDITION``). B<x> is the bus number (1-2).

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue <QString>
            - TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue?
            ```

        Info:
            - ``<QString>`` is up to 29 bits specifying the binary identifier value. The only
              allowed characters in the QString are 0, 1, and X.
        """
        return self._value


class TriggerABusBItemCanFrametype(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:FRAMEtype`` command.

    Description:
        - This command sets the frame type (data, remote, error or overload) to be used when
          triggering on a CAN bus signal. The trigger condition must be set to FRAMEtype (using
          ``TRIGGER:A:BUS:BX:CAN:CONDITION``). B<x> is the bus number (1-2).

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:FRAMEtype?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:FRAMEtype?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:FRAMEtype value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:FRAMEtype {DATA|REMote|ERRor|OVERLoad}
        - TRIGger:A:BUS:B<x>:CAN:FRAMEtype?
        ```

    Info:
        - ``DATA`` specifies a data frame type.
        - ``REMote`` specifies a remote frame type.
        - ``ERRor`` specifies an error frame type.
        - ``OVERLold`` specifies an overload frame type.
    """


class TriggerABusBItemCanDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:DATa:VALue`` command.

    Description:
        - This command sets the binary data value to be used when triggering on a CAN bus signal.
          The trigger condition must be set to IDANDDATA or DATa (using
          ``TRIGGER:A:BUS:BX:CAN:CONDITION``). The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa:VALue?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa:VALue?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:DATa:VALue <QString>
        - TRIGger:A:BUS:B<x>:CAN:DATa:VALue?
        ```

    Info:
        - ``<QString>`` is the data value in binary format. The only allowed characters in the
          QString are 0, 1, and X.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemCanDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:DATa:SIZe`` command.

    Description:
        - This command sets the length of the data string, in bytes, to be used when triggering on a
          CAN bus signal. The trigger condition must be set to IDANDDATA or DATa (using
          ``TRIGGER:A:BUS:BX:CAN:CONDITION``). The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa:SIZe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:DATa:SIZe <NR1>
        - TRIGger:A:BUS:B<x>:CAN:DATa:SIZe?
        ```

    Info:
        - ``<NR1>`` is the length of the data string in bytes.
    """


class TriggerABusBItemCanDataQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier`` command.

    Description:
        - Sets or returns the CAN data qualifier for bus <x>, where x is the bus number. This
          applies only, if the trigger condition is IDANDDATA or DATA.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual}
        - TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?
        ```

    Info:
        - ``LESSThan`` sets the oscilloscope to trigger when the data is less than the qualifier
          value.
        - ``MOREThan`` sets the oscilloscope to trigger when the data is more than the qualifier
          value.
        - ``EQUal`` sets the oscilloscope to trigger when the data is equal to the qualifier value.
        - ``UNEQual`` sets the oscilloscope to trigger when the data is not equal to the qualifier
          value.
        - ``LESSEQual`` sets the oscilloscope to trigger when the data is less than or equal to the
          qualifier value.
        - ``MOREEQual`` sets the oscilloscope to trigger when the data is more than or equal to the
          qualifier value.
    """  # noqa: E501


class TriggerABusBItemCanDataDirection(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:DATa:DIRection`` command.

    Description:
        - This command sets the data direction (read, write or 'nocare') to be used to search on a
          CAN bus signal. The trigger condition must be set to IDentifier (using
          ``TRIGGER:A:BUS:BX:CAN:CONDITION``). The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa:DIRection?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:DATa:DIRection?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:DATa:DIRection value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:DATa:DIRection {READ|WRITE|NOCARE}
        - TRIGger:A:BUS:B<x>:CAN:DATa:DIRection?
        ```

    Info:
        - ``READ`` sets the CAN data direction to READ.
        - ``WRITE`` sets the CAN data direction to WRITE.
        - ``NOCARE`` sets the CAN data direction to either.
    """


class TriggerABusBItemCanData(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.direction``: The ``TRIGger:A:BUS:B<x>:CAN:DATa:DIRection`` command.
        - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier`` command.
        - ``.size``: The ``TRIGger:A:BUS:B<x>:CAN:DATa:SIZe`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:CAN:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._direction = TriggerABusBItemCanDataDirection(device, f"{self._cmd_syntax}:DIRection")
        self._qualifier = TriggerABusBItemCanDataQualifier(device, f"{self._cmd_syntax}:QUALifier")
        self._size = TriggerABusBItemCanDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._value = TriggerABusBItemCanDataValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def direction(self) -> TriggerABusBItemCanDataDirection:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:DATa:DIRection`` command.

        Description:
            - This command sets the data direction (read, write or 'nocare') to be used to search on
              a CAN bus signal. The trigger condition must be set to IDentifier (using
              ``TRIGGER:A:BUS:BX:CAN:CONDITION``). The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa:DIRection?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:DATa:DIRection?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:DATa:DIRection value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:CAN:DATa:DIRection {READ|WRITE|NOCARE}
            - TRIGger:A:BUS:B<x>:CAN:DATa:DIRection?
            ```

        Info:
            - ``READ`` sets the CAN data direction to READ.
            - ``WRITE`` sets the CAN data direction to WRITE.
            - ``NOCARE`` sets the CAN data direction to either.
        """
        return self._direction

    @property
    def qualifier(self) -> TriggerABusBItemCanDataQualifier:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier`` command.

        Description:
            - Sets or returns the CAN data qualifier for bus <x>, where x is the bus number. This
              applies only, if the trigger condition is IDANDDATA or DATA.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier {LESSThan|MOREThan|EQUal|UNEQual|LESSEQual|MOREEQual}
            - TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?
            ```

        Info:
            - ``LESSThan`` sets the oscilloscope to trigger when the data is less than the qualifier
              value.
            - ``MOREThan`` sets the oscilloscope to trigger when the data is more than the qualifier
              value.
            - ``EQUal`` sets the oscilloscope to trigger when the data is equal to the qualifier
              value.
            - ``UNEQual`` sets the oscilloscope to trigger when the data is not equal to the
              qualifier value.
            - ``LESSEQual`` sets the oscilloscope to trigger when the data is less than or equal to
              the qualifier value.
            - ``MOREEQual`` sets the oscilloscope to trigger when the data is more than or equal to
              the qualifier value.
        """  # noqa: E501
        return self._qualifier

    @property
    def size(self) -> TriggerABusBItemCanDataSize:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:DATa:SIZe`` command.

        Description:
            - This command sets the length of the data string, in bytes, to be used when triggering
              on a CAN bus signal. The trigger condition must be set to IDANDDATA or DATa (using
              ``TRIGGER:A:BUS:BX:CAN:CONDITION``). The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa:SIZe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:DATa:SIZe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:DATa:SIZe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:CAN:DATa:SIZe <NR1>
            - TRIGger:A:BUS:B<x>:CAN:DATa:SIZe?
            ```

        Info:
            - ``<NR1>`` is the length of the data string in bytes.
        """
        return self._size

    @property
    def value(self) -> TriggerABusBItemCanDataValue:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:DATa:VALue`` command.

        Description:
            - This command sets the binary data value to be used when triggering on a CAN bus
              signal. The trigger condition must be set to IDANDDATA or DATa (using
              ``TRIGGER:A:BUS:BX:CAN:CONDITION``). The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa:VALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:DATa:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:CAN:DATa:VALue <QString>
            - TRIGger:A:BUS:B<x>:CAN:DATa:VALue?
            ```

        Info:
            - ``<QString>`` is the data value in binary format. The only allowed characters in the
              QString are 0, 1, and X.
        """
        return self._value


class TriggerABusBItemCanCondition(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:CONDition`` command.

    Description:
        - Sets or returns the CAN trigger condition for bus <x>, where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:CONDition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:CONDition value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:CONDition {SOF|FRAMEtype|IDentifier|DATA|IDANDDATA|EOF|ACKMISS}
        - TRIGger:A:BUS:B<x>:CAN:CONDition?
        ```

    Info:
        - ``SOF`` enables triggering on the start of frame.
        - ``FRAMEtype`` enables triggering on the type of frame.
        - ``IDentifier`` enables triggering on a matching identifier.
        - ``DATA`` enables triggering on matching data.
        - ``IDANDDATA`` enables triggering on a matching identifier and matching data.
        - ``EOF`` enables triggering on the end of frame.
        - ``ACKMISS`` enables triggering on a missing acknowledge.
    """


class TriggerABusBItemCanAddressValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue`` command.

    Description:
        - This command sets the binary address value to be used when triggering on a CAN bus signal.
          The trigger condition must be set to IDANDDATA OR DATA (using
          ``TRIGGER:A:BUS:BX:CAN:CONDITION``). B<x> is the bus number (1-2).

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue <QString>
        - TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue?
        ```

    Info:
        - ``<QString>`` is up to 29 bits specifying the binary identifier value. The only allowed
          characters in the QString are 0, 1, and X.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemCanAddressMode(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe`` command.

    Description:
        - Sets or returns the CAN addressing mode for bus <x>, where x is the bus number.Use this
          command to do the following: Trigger on ID Trigger in IDANDDATA

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe?``
          query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe {STandard|EXTended}
        - TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe?
        ```

    Info:
        - ``STandard`` specifies the standard addressing mode.
        - ``EXTended`` specifies the extended addressing mode.
    """


class TriggerABusBItemCanAddress(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:ADDRess`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:ADDRess?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:ADDRess?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.mode``: The ``TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = TriggerABusBItemCanAddressMode(device, f"{self._cmd_syntax}:MODe")
        self._value = TriggerABusBItemCanAddressValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def mode(self) -> TriggerABusBItemCanAddressMode:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe`` command.

        Description:
            - Sets or returns the CAN addressing mode for bus <x>, where x is the bus number.Use
              this command to do the following: Trigger on ID Trigger in IDANDDATA

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe {STandard|EXTended}
            - TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe?
            ```

        Info:
            - ``STandard`` specifies the standard addressing mode.
            - ``EXTended`` specifies the extended addressing mode.
        """
        return self._mode

    @property
    def value(self) -> TriggerABusBItemCanAddressValue:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue`` command.

        Description:
            - This command sets the binary address value to be used when triggering on a CAN bus
              signal. The trigger condition must be set to IDANDDATA OR DATA (using
              ``TRIGGER:A:BUS:BX:CAN:CONDITION``). B<x> is the bus number (1-2).

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue <QString>
            - TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue?
            ```

        Info:
            - ``<QString>`` is up to 29 bits specifying the binary identifier value. The only
              allowed characters in the QString are 0, 1, and X.
        """
        return self._value


class TriggerABusBItemCan(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``TRIGger:A:BUS:B<x>:CAN:CONDition`` command.
        - ``.data``: The ``TRIGger:A:BUS:B<x>:CAN:DATa`` command tree.
        - ``.frametype``: The ``TRIGger:A:BUS:B<x>:CAN:FRAMEtype`` command.
        - ``.identifier``: The ``TRIGger:A:BUS:B<x>:CAN:IDentifier`` command tree.
        - ``.address``: The ``TRIGger:A:BUS:B<x>:CAN:ADDRess`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = TriggerABusBItemCanCondition(device, f"{self._cmd_syntax}:CONDition")
        self._data = TriggerABusBItemCanData(device, f"{self._cmd_syntax}:DATa")
        self._frametype = TriggerABusBItemCanFrametype(device, f"{self._cmd_syntax}:FRAMEtype")
        self._identifier = TriggerABusBItemCanIdentifier(device, f"{self._cmd_syntax}:IDentifier")
        self._address = TriggerABusBItemCanAddress(device, f"{self._cmd_syntax}:ADDRess")

    @property
    def condition(self) -> TriggerABusBItemCanCondition:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:CONDition`` command.

        Description:
            - Sets or returns the CAN trigger condition for bus <x>, where x is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:CONDition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:CONDition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:CONDition value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:CAN:CONDition {SOF|FRAMEtype|IDentifier|DATA|IDANDDATA|EOF|ACKMISS}
            - TRIGger:A:BUS:B<x>:CAN:CONDition?
            ```

        Info:
            - ``SOF`` enables triggering on the start of frame.
            - ``FRAMEtype`` enables triggering on the type of frame.
            - ``IDentifier`` enables triggering on a matching identifier.
            - ``DATA`` enables triggering on matching data.
            - ``IDANDDATA`` enables triggering on a matching identifier and matching data.
            - ``EOF`` enables triggering on the end of frame.
            - ``ACKMISS`` enables triggering on a missing acknowledge.
        """
        return self._condition

    @property
    def data(self) -> TriggerABusBItemCanData:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.direction``: The ``TRIGger:A:BUS:B<x>:CAN:DATa:DIRection`` command.
            - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier`` command.
            - ``.size``: The ``TRIGger:A:BUS:B<x>:CAN:DATa:SIZe`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:CAN:DATa:VALue`` command.
        """
        return self._data

    @property
    def frametype(self) -> TriggerABusBItemCanFrametype:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:FRAMEtype`` command.

        Description:
            - This command sets the frame type (data, remote, error or overload) to be used when
              triggering on a CAN bus signal. The trigger condition must be set to FRAMEtype (using
              ``TRIGGER:A:BUS:BX:CAN:CONDITION``). B<x> is the bus number (1-2).

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:FRAMEtype?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:FRAMEtype?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:FRAMEtype value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:CAN:FRAMEtype {DATA|REMote|ERRor|OVERLoad}
            - TRIGger:A:BUS:B<x>:CAN:FRAMEtype?
            ```

        Info:
            - ``DATA`` specifies a data frame type.
            - ``REMote`` specifies a remote frame type.
            - ``ERRor`` specifies an error frame type.
            - ``OVERLold`` specifies an overload frame type.
        """
        return self._frametype

    @property
    def identifier(self) -> TriggerABusBItemCanIdentifier:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:IDentifier`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:IDentifier?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:IDentifier?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.mode``: The ``TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue`` command.
        """
        return self._identifier

    @property
    def address(self) -> TriggerABusBItemCanAddress:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:ADDRess`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:ADDRess?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:ADDRess?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.mode``: The ``TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue`` command.
        """
        return self._address


class TriggerABusBItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.can``: The ``TRIGger:A:BUS:B<x>:CAN`` command tree.
        - ``.flexray``: The ``TRIGger:A:BUS:B<x>:FLEXray`` command tree.
        - ``.i2c``: The ``TRIGger:A:BUS:B<x>:I2C`` command tree.
        - ``.lin``: The ``TRIGger:A:BUS:B<x>:LIN`` command tree.
        - ``.parallel``: The ``TRIGger:A:BUS:B<x>:PARallel`` command tree.
        - ``.rs232c``: The ``TRIGger:A:BUS:B<x>:RS232C`` command tree.
        - ``.spi``: The ``TRIGger:A:BUS:B<x>:SPI`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._can = TriggerABusBItemCan(device, f"{self._cmd_syntax}:CAN")
        self._flexray = TriggerABusBItemFlexray(device, f"{self._cmd_syntax}:FLEXray")
        self._i2c = TriggerABusBItemI2c(device, f"{self._cmd_syntax}:I2C")
        self._lin = TriggerABusBItemLin(device, f"{self._cmd_syntax}:LIN")
        self._parallel = TriggerABusBItemParallel(device, f"{self._cmd_syntax}:PARallel")
        self._rs232c = TriggerABusBItemRs232c(device, f"{self._cmd_syntax}:RS232C")
        self._spi = TriggerABusBItemSpi(device, f"{self._cmd_syntax}:SPI")

    @property
    def can(self) -> TriggerABusBItemCan:
        """Return the ``TRIGger:A:BUS:B<x>:CAN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``TRIGger:A:BUS:B<x>:CAN:CONDition`` command.
            - ``.data``: The ``TRIGger:A:BUS:B<x>:CAN:DATa`` command tree.
            - ``.frametype``: The ``TRIGger:A:BUS:B<x>:CAN:FRAMEtype`` command.
            - ``.identifier``: The ``TRIGger:A:BUS:B<x>:CAN:IDentifier`` command tree.
            - ``.address``: The ``TRIGger:A:BUS:B<x>:CAN:ADDRess`` command tree.
        """
        return self._can

    @property
    def flexray(self) -> TriggerABusBItemFlexray:
        """Return the ``TRIGger:A:BUS:B<x>:FLEXray`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:FLEXray?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``TRIGger:A:BUS:B<x>:FLEXray:CONDition`` command.
            - ``.cyclecount``: The ``TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount`` command tree.
            - ``.data``: The ``TRIGger:A:BUS:B<x>:FLEXray:DATa`` command tree.
            - ``.eoftype``: The ``TRIGger:A:BUS:B<x>:FLEXray:EOFTYPE`` command.
            - ``.errtype``: The ``TRIGger:A:BUS:B<x>:FLEXray:ERRTYPE`` command.
            - ``.frameid``: The ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEID`` command tree.
            - ``.frametype``: The ``TRIGger:A:BUS:B<x>:FLEXray:FRAMEType`` command.
            - ``.header``: The ``TRIGger:A:BUS:B<x>:FLEXray:HEADER`` command tree.
        """
        return self._flexray

    @property
    def i2c(self) -> TriggerABusBItemI2c:
        """Return the ``TRIGger:A:BUS:B<x>:I2C`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:I2C?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.address``: The ``TRIGger:A:BUS:B<x>:I2C:ADDRess`` command tree.
            - ``.condition``: The ``TRIGger:A:BUS:B<x>:I2C:CONDition`` command.
            - ``.data``: The ``TRIGger:A:BUS:B<x>:I2C:DATa`` command tree.
        """
        return self._i2c

    @property
    def lin(self) -> TriggerABusBItemLin:
        """Return the ``TRIGger:A:BUS:B<x>:LIN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``TRIGger:A:BUS:B<x>:LIN:CONDition`` command.
            - ``.data``: The ``TRIGger:A:BUS:B<x>:LIN:DATa`` command tree.
            - ``.errtype``: The ``TRIGger:A:BUS:B<x>:LIN:ERRTYPE`` command.
            - ``.identifier``: The ``TRIGger:A:BUS:B<x>:LIN:IDentifier`` command tree.
        """
        return self._lin

    @property
    def parallel(self) -> TriggerABusBItemParallel:
        """Return the ``TRIGger:A:BUS:B<x>:PARallel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:PARallel?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:PARallel?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:PARallel:VALue`` command.
        """
        return self._parallel

    @property
    def rs232c(self) -> TriggerABusBItemRs232c:
        """Return the ``TRIGger:A:BUS:B<x>:RS232C`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:RS232C?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``TRIGger:A:BUS:B<x>:RS232C:CONDition`` command.
            - ``.rx``: The ``TRIGger:A:BUS:B<x>:RS232C:RX`` command tree.
            - ``.tx``: The ``TRIGger:A:BUS:B<x>:RS232C:TX`` command tree.
        """
        return self._rs232c

    @property
    def spi(self) -> TriggerABusBItemSpi:
        """Return the ``TRIGger:A:BUS:B<x>:SPI`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SPI?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``TRIGger:A:BUS:B<x>:SPI:CONDition`` command.
            - ``.data``: The ``TRIGger:A:BUS:B<x>:SPI:DATa`` command tree.
        """
        return self._spi


class TriggerABus(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS`` command.

    Description:
        - Sets or returns the trigger type: I2C, CAN, SPI, and RS232. There are up to two serial
          buses, B1, B2, depending on your instrument model. Each can be independently set to one of
          the serial trigger types. The serial parameters related to the trigger are broken into two
          sections: ``Trigger:A:SERIAL`` xxx, consisting of parameters the user will change
          frequently, and ``BUS:B1:xxx``, consisting of parameters the user will specify once (bus
          definition).

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:BUS value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS {I2C|SPI|CAN|RS232}
        - TRIGger:A:BUS?
        ```

    Info:
        - ``I2C`` specifies the Inter-IC bus.
        - ``SPI`` specifies the Serial Peripheral Interface bus.
        - ``CAN`` specifies the Controller Area Network bus.

    Properties:
        - ``.b``: The ``TRIGger:A:BUS:B<x>`` command tree.
        - ``.source``: The ``TRIGger:A:BUS:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._b: Dict[int, TriggerABusBItem] = DefaultDictPassKeyToFactory(
            lambda x: TriggerABusBItem(device, f"{self._cmd_syntax}:B{x}")
        )
        self._source = TriggerABusSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def b(self) -> Dict[int, TriggerABusBItem]:
        """Return the ``TRIGger:A:BUS:B<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.can``: The ``TRIGger:A:BUS:B<x>:CAN`` command tree.
            - ``.flexray``: The ``TRIGger:A:BUS:B<x>:FLEXray`` command tree.
            - ``.i2c``: The ``TRIGger:A:BUS:B<x>:I2C`` command tree.
            - ``.lin``: The ``TRIGger:A:BUS:B<x>:LIN`` command tree.
            - ``.parallel``: The ``TRIGger:A:BUS:B<x>:PARallel`` command tree.
            - ``.rs232c``: The ``TRIGger:A:BUS:B<x>:RS232C`` command tree.
            - ``.spi``: The ``TRIGger:A:BUS:B<x>:SPI`` command tree.
        """
        return self._b

    @property
    def source(self) -> TriggerABusSource:
        """Return the ``TRIGger:A:BUS:SOUrce`` command.

        Description:
            - This command specifies the source for a serial or parallel bus trigger, with the
              appropriate application module installed.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:BUS:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:SOUrce {B<x>}
            - TRIGger:A:BUS:SOUrce?
            ```

        Info:
            - ``B1`` specifies the Bus 1 source.
            - ``B2`` specifies the Bus 2 source.
            - ``B3`` specifies the Bus 3 source.
            - ``B4`` specifies the Bus 4 source.
        """
        return self._source


#  pylint: disable=too-many-instance-attributes
class TriggerA(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A`` command.

    Description:
        - This command sets the A trigger level automatically to 50% of the range of the minimum and
          maximum values of the trigger input signal. The query returns current trigger parameters.
          The trigger level is the voltage threshold through which the trigger source signal must
          pass to generate a trigger event. This command is equivalent to pushing the LEVEL knob on
          the front panel.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A SETLevel
        - TRIGger:A?
        ```

    Info:
        - ``SETLevel`` sets the trigger level to 50% of the range of the minimum and maximum values
          of the trigger input signal.

    Properties:
        - ``.bus``: The ``TRIGger:A:BUS`` command.
        - ``.edge``: The ``TRIGger:A:EDGE`` command.
        - ``.holdoff``: The ``TRIGger:A:HOLDoff`` command.
        - ``.level``: The ``TRIGger:A:LEVel`` command.
        - ``.logic``: The ``TRIGger:A:LOGIc`` command.
        - ``.lowerthreshold``: The ``TRIGger:A:LOWerthreshold`` command tree.
        - ``.mode``: The ``TRIGger:A:MODe`` command.
        - ``.pulsewidth``: The ``TRIGger:A:PULSEWidth`` command.
        - ``.pulse``: The ``TRIGger:A:PULse`` command.
        - ``.runt``: The ``TRIGger:A:RUNT`` command.
        - ``.sethold``: The ``TRIGger:A:SETHold`` command.
        - ``.type``: The ``TRIGger:A:TYPe`` command.
        - ``.upperthreshold``: The ``TRIGger:A:UPPerthreshold`` command tree.
        - ``.video``: The ``TRIGger:A:VIDeo`` command.
        - ``.transition``: The ``TRIGger:A:TRANsition`` command.
        - ``.risefall``: The ``TRIGger:A:RISEFall`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bus = TriggerABus(device, f"{self._cmd_syntax}:BUS")
        self._edge = TriggerAEdge(device, f"{self._cmd_syntax}:EDGE")
        self._holdoff = TriggerAHoldoff(device, f"{self._cmd_syntax}:HOLDoff")
        self._level = TriggerALevel(device, f"{self._cmd_syntax}:LEVel")
        self._logic = TriggerALogic(device, f"{self._cmd_syntax}:LOGIc")
        self._lowerthreshold = TriggerALowerthreshold(device, f"{self._cmd_syntax}:LOWerthreshold")
        self._mode = TriggerAMode(device, f"{self._cmd_syntax}:MODe")
        self._pulsewidth = TriggerAPulsewidth(device, f"{self._cmd_syntax}:PULSEWidth")
        self._pulse = TriggerAPulse(device, f"{self._cmd_syntax}:PULse")
        self._runt = TriggerARunt(device, f"{self._cmd_syntax}:RUNT")
        self._sethold = TriggerASethold(device, f"{self._cmd_syntax}:SETHold")
        self._type = TriggerAType(device, f"{self._cmd_syntax}:TYPe")
        self._upperthreshold = TriggerAUpperthreshold(device, f"{self._cmd_syntax}:UPPerthreshold")
        self._video = TriggerAVideo(device, f"{self._cmd_syntax}:VIDeo")
        self._transition = TriggerATransition(device, f"{self._cmd_syntax}:TRANsition")
        self._risefall = TriggerARisefall(device, f"{self._cmd_syntax}:RISEFall")

    @property
    def bus(self) -> TriggerABus:
        """Return the ``TRIGger:A:BUS`` command.

        Description:
            - Sets or returns the trigger type: I2C, CAN, SPI, and RS232. There are up to two serial
              buses, B1, B2, depending on your instrument model. Each can be independently set to
              one of the serial trigger types. The serial parameters related to the trigger are
              broken into two sections: ``Trigger:A:SERIAL`` xxx, consisting of parameters the user
              will change frequently, and ``BUS:B1:xxx``, consisting of parameters the user will
              specify once (bus definition).

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:BUS value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS {I2C|SPI|CAN|RS232}
            - TRIGger:A:BUS?
            ```

        Info:
            - ``I2C`` specifies the Inter-IC bus.
            - ``SPI`` specifies the Serial Peripheral Interface bus.
            - ``CAN`` specifies the Controller Area Network bus.

        Sub-properties:
            - ``.b``: The ``TRIGger:A:BUS:B<x>`` command tree.
            - ``.source``: The ``TRIGger:A:BUS:SOUrce`` command.
        """
        return self._bus

    @property
    def edge(self) -> TriggerAEdge:
        """Return the ``TRIGger:A:EDGE`` command.

        Description:
            - Returns the trigger source, coupling, and slope for the A edge trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:EDGE?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TRIGger:A:EDGE?
            ```

        Sub-properties:
            - ``.coupling``: The ``TRIGger:A:EDGE:COUPling`` command.
            - ``.slope``: The ``TRIGger:A:EDGE:SLOpe`` command.
            - ``.source``: The ``TRIGger:A:EDGE:SOUrce`` command.
        """
        return self._edge

    @property
    def holdoff(self) -> TriggerAHoldoff:
        """Return the ``TRIGger:A:HOLDoff`` command.

        Description:
            - Returns the A trigger holdoff parameters. These parameters specify the time period
              during which the trigger circuitry is not looking to generate a trigger event.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:HOLDoff?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:HOLDoff?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TRIGger:A:HOLDoff?
            ```

        Sub-properties:
            - ``.time``: The ``TRIGger:A:HOLDoff:TIMe`` command.
        """
        return self._holdoff

    @property
    def level(self) -> TriggerALevel:
        """Return the ``TRIGger:A:LEVel`` command.

        Description:
            - Sets or returns the trigger level for the A trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LEVel?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LEVel?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:LEVel value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:LEVel {ECL|TTL|<NR3>}
            - TRIGger:A:LEVel?
            ```

        Info:
            - ``ECL`` specifies a preset ECL high level of -1.3V.
            - ``TTL`` specifies a preset TTL high level of 1.4V.
            - ``<NR3>`` specifies the trigger level in user units (usually volts).

        Sub-properties:
            - ``.auxin``: The ``TRIGger:A:LEVel:AUXin`` command.
            - ``.ch``: The ``TRIGger:A:LEVel:CH<x>`` command.
            - ``.d``: The ``TRIGger:A:LEVel:D<x>`` command.
        """
        return self._level

    @property
    def logic(self) -> TriggerALogic:
        """Return the ``TRIGger:A:LOGIc`` command.

        Description:
            - Returns all of the A logic trigger parameters.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGIc?
            ```

        Sub-properties:
            - ``.class``: The ``TRIGger:A:LOGIc:CLAss`` command.
            - ``.function``: The ``TRIGger:A:LOGIc:FUNCtion`` command.
            - ``.input``: The ``TRIGger:A:LOGIc:INPut`` command.
            - ``.pattern``: The ``TRIGger:A:LOGIc:PATtern`` command.
            - ``.threshold``: The ``TRIGger:A:LOGIc:THReshold`` command tree.
        """
        return self._logic

    @property
    def lowerthreshold(self) -> TriggerALowerthreshold:
        """Return the ``TRIGger:A:LOWerthreshold`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOWerthreshold?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOWerthreshold?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``TRIGger:A:LOWerthreshold:CH<x>`` command.
            - ``.ext``: The ``TRIGger:A:LOWerthreshold:EXT`` command.
            - ``.aux``: The ``TRIGger:A:LOWerthreshold:AUX`` command.
        """
        return self._lowerthreshold

    @property
    def mode(self) -> TriggerAMode:
        """Return the ``TRIGger:A:MODe`` command.

        Description:
            - This command sets or queries the A trigger mode. This command is equivalent to pushing
              the Mode button on the front panel.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:MODe?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:MODe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:MODe {AUTO|NORMal}
            - TRIGger:A:MODe?
            ```

        Info:
            - ``AUTO`` generates a trigger if one is not detected within a specified time period.
            - ``NORMal`` waits for a valid trigger event.
        """
        return self._mode

    @property
    def pulsewidth(self) -> TriggerAPulsewidth:
        """Return the ``TRIGger:A:PULSEWidth`` command.

        Description:
            - Returns the width parameters for the pulse width trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TRIGger:A:PULSEWidth?
            ```

        Sub-properties:
            - ``.polarity``: The ``TRIGger:A:PULSEWidth:POLarity`` command.
            - ``.source``: The ``TRIGger:A:PULSEWidth:SOUrce`` command.
            - ``.when``: The ``TRIGger:A:PULSEWidth:WHEn`` command.
            - ``.width``: The ``TRIGger:A:PULSEWidth:Width`` command.
        """
        return self._pulsewidth

    @property
    def pulse(self) -> TriggerAPulse:
        """Return the ``TRIGger:A:PULse`` command.

        Description:
            - Returns the A pulse trigger parameters.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:PULse?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULse?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TRIGger:A:PULse?
            ```

        Sub-properties:
            - ``.class``: The ``TRIGger:A:PULse:CLAss`` command.
        """
        return self._pulse

    @property
    def runt(self) -> TriggerARunt:
        """Return the ``TRIGger:A:RUNT`` command.

        Description:
            - Returns the current A runt trigger parameters.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:RUNT?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:RUNT?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TRIGger:A:RUNT?
            ```

        Sub-properties:
            - ``.polarity``: The ``TRIGger:A:RUNT:POLarity`` command.
            - ``.source``: The ``TRIGger:A:RUNT:SOUrce`` command.
            - ``.when``: The ``TRIGger:A:RUNT:WHEn`` command.
            - ``.width``: The ``TRIGger:A:RUNT:WIDth`` command.
        """
        return self._runt

    @property
    def sethold(self) -> TriggerASethold:
        """Return the ``TRIGger:A:SETHold`` command.

        Description:
            - Returns the clock edge polarity, voltage threshold and source input; data voltage
              threshold and source; and both setup and hold times for setup and hold violation
              triggering.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:SETHold?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TRIGger:A:SETHold?
            ```

        Sub-properties:
            - ``.clock``: The ``TRIGger:A:SETHold:CLOCk`` command.
            - ``.data``: The ``TRIGger:A:SETHold:DATa`` command.
            - ``.holdtime``: The ``TRIGger:A:SETHold:HOLDTime`` command.
            - ``.settime``: The ``TRIGger:A:SETHold:SETTime`` command.
            - ``.threshold``: The ``TRIGger:A:SETHold:THReshold`` command tree.
        """
        return self._sethold

    @property
    def type(self) -> TriggerAType:
        """Return the ``TRIGger:A:TYPe`` command.

        Description:
            - Sets or returns the type of A trigger. The five types of triggers are of Edge, Logic,
              Pulse, Serial, and Video. Logic and Pulse triggers contain classes. Logic triggers
              consist of State, Pattern, and SetHold classes; Pulse triggers consist of Runt, Width,
              and Transition logic classes. Once you have set the trigger type, you may also need to
              identify the associated trigger class. For details on selecting Logic and Pulse
              trigger classes, see ``TRIGGER:A:LOGIC:CLASS`` and ``TRIGGER:A:PULSE:CLASS``
              respectively.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:TYPe?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:TYPe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:TYPe {EDGe|LOGic|PULSe|BUS|VIDeo}
            - TRIGger:A:TYPe?
            ```

        Info:
            - ``EDGe`` is a normal trigger. A trigger event occurs when a signal passes through a
              specified voltage level in a specified direction and is controlled by the
              ``TRIGGER:A:EDGE`` commands.
            - ``LOGic`` specifies that a trigger occurs when specified conditions are met and is
              controlled by the ``TRIGGER:A:LOGIC`` commands.
            - ``PULSe`` specifies that a trigger occurs when a specified pulse is found and is
              controlled by the ``TRIGGER:A:PULSE`` commands.
            - ``BUS`` specifies that a trigger occurs when a communications signal is found.
              Supports CAN, I2C, SPI, and RS232 communications signals.
            - ``VIDeo`` specifies that the trigger occurs when a video signal is found.
        """
        return self._type

    @property
    def upperthreshold(self) -> TriggerAUpperthreshold:
        """Return the ``TRIGger:A:UPPerthreshold`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:UPPerthreshold?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:UPPerthreshold?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``TRIGger:A:UPPerthreshold:CH<x>`` command.
        """
        return self._upperthreshold

    @property
    def video(self) -> TriggerAVideo:
        """Return the ``TRIGger:A:VIDeo`` command.

        Description:
            - Returns the A trigger video parameters.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TRIGger:A:VIDeo?
            ```

        Sub-properties:
            - ``.custom``: The ``TRIGger:A:VIDeo:CUSTom`` command.
            - ``.hdtv``: The ``TRIGger:A:VIDeo:HDtv`` command tree.
            - ``.holdoff``: The ``TRIGger:A:VIDeo:HOLDoff`` command tree.
            - ``.line``: The ``TRIGger:A:VIDeo:LINE`` command.
            - ``.polarity``: The ``TRIGger:A:VIDeo:POLarity`` command.
            - ``.source``: The ``TRIGger:A:VIDeo:SOUrce`` command.
            - ``.standard``: The ``TRIGger:A:VIDeo:STANdard`` command.
            - ``.sync``: The ``TRIGger:A:VIDeo:SYNC`` command.
            - ``.field``: The ``TRIGger:A:VIDeo:FIELD`` command.
        """
        return self._video

    @property
    def transition(self) -> TriggerATransition:
        """Return the ``TRIGger:A:TRANsition`` command.

        Description:
            - Returns transition time trigger parameters.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:TRANsition?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:TRANsition?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TRIGger:A:TRANsition?
            ```

        Sub-properties:
            - ``.deltatime``: The ``TRIGger:A:TRANsition:DELTatime`` command.
            - ``.polarity``: The ``TRIGger:A:TRANsition:POLarity`` command.
            - ``.source``: The ``TRIGger:A:TRANsition:SOUrce`` command.
            - ``.when``: The ``TRIGger:A:TRANsition:WHEn`` command.
        """
        return self._transition

    @property
    def risefall(self) -> TriggerARisefall:
        """Return the ``TRIGger:A:RISEFall`` command.

        Description:
            - Returns transition time trigger parameters.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:RISEFall?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:RISEFall?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TRIGger:A:RISEFall?
            ```

        Sub-properties:
            - ``.deltatime``: The ``TRIGger:A:RISEFall:DELTatime`` command.
            - ``.polarity``: The ``TRIGger:A:RISEFall:POLarity`` command.
            - ``.source``: The ``TRIGger:A:RISEFall:SOUrce`` command.
            - ``.when``: The ``TRIGger:A:RISEFall:WHEn`` command.
        """
        return self._risefall


class Trigger(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger`` command.

    Description:
        - This command forces a trigger event to occur. The query returns the current trigger
          parameters for the instrument.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger value`` command.

    SCPI Syntax:
        ```
        - TRIGger FORCe
        - TRIGger?
        ```

    Info:
        - ``FORCe`` creates a trigger event. If ``TRIGger:STATE`` is set to READy, the acquisition
          will complete. Otherwise, this command will be ignored. This is equivalent to pressing the
          Force button on the front panel.

    Properties:
        - ``.a``: The ``TRIGger:A`` command.
        - ``.b``: The ``TRIGger:B`` command tree.
        - ``.external``: The ``TRIGger:EXTernal`` command.
        - ``.frequency``: The ``TRIGger:FREQuency`` command.
        - ``.state``: The ``TRIGger:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "TRIGger") -> None:
        super().__init__(device, cmd_syntax)
        self._a = TriggerA(device, f"{self._cmd_syntax}:A")
        self._b = TriggerB(device, f"{self._cmd_syntax}:B")
        self._external = TriggerExternal(device, f"{self._cmd_syntax}:EXTernal")
        self._frequency = TriggerFrequency(device, f"{self._cmd_syntax}:FREQuency")
        self._state = TriggerState(device, f"{self._cmd_syntax}:STATE")

    @property
    def a(self) -> TriggerA:
        """Return the ``TRIGger:A`` command.

        Description:
            - This command sets the A trigger level automatically to 50% of the range of the minimum
              and maximum values of the trigger input signal. The query returns current trigger
              parameters. The trigger level is the voltage threshold through which the trigger
              source signal must pass to generate a trigger event. This command is equivalent to
              pushing the LEVEL knob on the front panel.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A SETLevel
            - TRIGger:A?
            ```

        Info:
            - ``SETLevel`` sets the trigger level to 50% of the range of the minimum and maximum
              values of the trigger input signal.

        Sub-properties:
            - ``.bus``: The ``TRIGger:A:BUS`` command.
            - ``.edge``: The ``TRIGger:A:EDGE`` command.
            - ``.holdoff``: The ``TRIGger:A:HOLDoff`` command.
            - ``.level``: The ``TRIGger:A:LEVel`` command.
            - ``.logic``: The ``TRIGger:A:LOGIc`` command.
            - ``.lowerthreshold``: The ``TRIGger:A:LOWerthreshold`` command tree.
            - ``.mode``: The ``TRIGger:A:MODe`` command.
            - ``.pulsewidth``: The ``TRIGger:A:PULSEWidth`` command.
            - ``.pulse``: The ``TRIGger:A:PULse`` command.
            - ``.runt``: The ``TRIGger:A:RUNT`` command.
            - ``.sethold``: The ``TRIGger:A:SETHold`` command.
            - ``.type``: The ``TRIGger:A:TYPe`` command.
            - ``.upperthreshold``: The ``TRIGger:A:UPPerthreshold`` command tree.
            - ``.video``: The ``TRIGger:A:VIDeo`` command.
            - ``.transition``: The ``TRIGger:A:TRANsition`` command.
            - ``.risefall``: The ``TRIGger:A:RISEFall`` command.
        """
        return self._a

    @property
    def b(self) -> TriggerB:
        """Return the ``TRIGger:B`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.level``: The ``TRIGger:B:LEVel`` command tree.
            - ``.lowerthreshold``: The ``TRIGger:B:LOWerthreshold`` command tree.
        """
        return self._b

    @property
    def external(self) -> TriggerExternal:
        """Return the ``TRIGger:EXTernal`` command.

        Description:
            - Returns all external trigger-related parameters for the probe attached to the Aux
              Input connector.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:EXTernal?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:EXTernal?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TRIGger:EXTernal?
            ```

        Sub-properties:
            - ``.probe``: The ``TRIGger:EXTernal:PRObe`` command.
            - ``.yunits``: The ``TRIGger:EXTernal:YUNIts`` command.
        """
        return self._external

    @property
    def frequency(self) -> TriggerFrequency:
        """Return the ``TRIGger:FREQuency`` command.

        Description:
            - Returns the trigger frequency in hertz if available. If the trigger frequency is not
              currently available, the IEEE Not A Number (NaN = 99.10E+36) value is returned. The
              maximum precision of the returned frequency is 12 digits. Use the
              ``DISPLAY:TRIGFREQUENCY`` command to enable/disable the calculation of the trigger
              frequency.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:FREQuency?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TRIGger:FREQuency?
            ```
        """
        return self._frequency

    @property
    def state(self) -> TriggerState:
        """Return the ``TRIGger:STATE`` command.

        Description:
            - This query-only command returns the current state of the triggering system.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:STATE?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TRIGger:STATE?
            ```
        """
        return self._state
