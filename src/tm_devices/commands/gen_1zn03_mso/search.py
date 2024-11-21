# pylint: disable=line-too-long
"""The search commands module.

These commands are used in the following models:
MSO2

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SEARCH:ADDNew <QString>
    - SEARCH:DELETEALL
    - SEARCH:DELete <QString>
    - SEARCH:LIST?
    - SEARCH:SEARCH<x>:COPy {SEARCHtotrigger|TRIGgertosearch}
    - SEARCH:SEARCH<x>:NAVigate {NEXT|PREVious|MIN|NONE|MAX}
    - SEARCH:SEARCH<x>:TOTAL?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:CONDition {SOF|FRAMEtype|IDentifier|DATa|IDANDDATA|EOF|ERRor|FDBITS}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:CONDition?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:DIRection {READ|WRITE|NOCARE}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:DIRection?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:OFFSet <NR1>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:OFFSet?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:QUALifier {EQUal|LESSEQual|MOREEQua|UNEQual|LESSthan|MOREthan}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:QUALifier?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:SIZe <NR1>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:SIZe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:ERRType {ACKMISS|BITSTUFFing|FORMERRor|ANYERRor}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:ERRType?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:BRSBit {ONE|ZERo|NOCARE}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:BRSBit?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:ESIBit {ONE|ZERo|NOCARE}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:ESIBit?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FRAMEtype {DATa|ERRor|OVERLoad|REMote}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FRAMEtype?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:MODe {EXTENDed|STandard}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:MODe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:MODe {ADDR10|ADDR7}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:MODe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:CONDition {ADDRess|ADDRANDDATA|DATa|ACKMISS|REPEATstart|STARt|STOP}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:CONDition?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:DIRection {NOCARE|READ|WRITE}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:DIRection?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:SIZe <NR1>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:SIZe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:CONDition {DATA|IDANDDATA|ERRor|IDentifier|SLEEP|SYNCfield|WAKEup}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:CONDition?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:HIVALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:HIVALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:QUALifier {EQual|LESSEQual|MOREEQual|UNEQual|LESSthan|MOREthan|INrange|OUTrange}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:QUALifier?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:SIZe <NR1>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:SIZe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:ERRTYPE {CHecksum|PARity|SYNC}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:ERRTYPE?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:IDentifier:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:IDentifier:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel:DATa:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel:DATa:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:CONDition {DATa|EOp|PARItyerror|STARt}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:CONDition?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:SIZe <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:SIZe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:CONDition {START|FAST|SLOW|PAUSE|ERRor}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:CONDition?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType {FRAMELENgth|CRC}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType:CRC {FAST|SLOW}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType:CRC?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:HIVALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:HIVALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|INrange|OUTrange}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:QUALifier?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:VALue <Qstring>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:HIVALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:HIVALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|INrange|OUTrange}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:QUALifier?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:VALue <Qstring>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:HIVALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:HIVALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|INrange|OUTrange}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:QUALifier?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:VALue <Qstring>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:INVERTNIBble:VALue <Qstring>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:INVERTNIBble:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:STATus:VALue <Qstring>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:STATus:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|INrange|OUTrange}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:QUALifier?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:HIVALue <NR1>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:HIVALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:VALue <NR1>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:HIVALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:HIVALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQualINrange|OUTrange}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:QUALifier?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:VALue <Qstring>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:IDentifier:VALue <Qstring>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:IDentifier:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce {B0|B1|B2|B3|B4|B5|B6|B7|B8|B9|B10|B11|B12|B13|B14|B15|B16}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:CONDition {DATA|SS|STARTofframe}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:CONDition?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:SIZe <NR1>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:SIZe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:SOURCETYpe {MISo|MOSi}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:SOURCETYpe?
    - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe {RISe|FALL|EITher}
    - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe?
    - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
    - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce?
    - SEARCH:SEARCH<x>:TRIGger:A:EDGE:THReshold <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:EDGE:THReshold?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:CLOCk:THReshold <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:CLOCk:THReshold?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:DELTatime <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:DELTatime?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion {AND|NANd|NOR|OR}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT:CLOCK:SOUrce {CH<x>|DCH<x>_D<x>|REF<x>_D<x>}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT:CLOCK:SOUrce?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:CH<x> <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:CH<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:MATH<x> <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:MATH<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:REF<x> <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:REF<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:CH<x> {H|L|X}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:CH<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:DCH<x>_D<x> {H|L|X}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:DCH<x>_D<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:MATH<x> {H|L|X}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:MATH<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:REF<x> {H|L|X}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:REF<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:POLarity {POSitive|NEGative|EITher}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:POLarity?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:USEClockedge {OFF|ON|0|1}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:USEClockedge?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:WHEn {TRUe|FALSe|MOREThan|LESSThan|EQual|UNEQual}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:WHEn?
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:HIGHLimit <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:HIGHLimit?
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOGICQUALification {ON|OFF}
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOGICQUALification?
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOWLimit <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOWLimit?
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity {POSitive|NEGative}
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity?
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce?
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:THReshold <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:THReshold?
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn {LESSthan|MOREthan|EQual|UNEQual|WIThin|OUTside}
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn?
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:LOGICQUALification {ON|OFF}
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:LOGICQUALification?
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity {POSitive|NEGative|EITher}
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity?
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce {CH<x>|REF<x>}
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:HIGH <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:HIGH?
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:LOW <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:LOW?
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn {OCCURS|LESSthan|MOREthan|EQual}NOTEQual}
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn?
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:EDGE {FALL|RISe}
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:EDGE?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:THReshold <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:THReshold?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:HOLDTime <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:HOLDTime?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:CH<x> <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:CH<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:MATH<x> <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:MATH<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:REF<x> <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:REF<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:CH<x> {INCLude|DONTInclude}
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:CH<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:DCH<x>_D<x> {INCLude|DONTInclude}
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:DCH<x>_D<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:MATH<x> {INCLude|DONTInclude}
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:MATH<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:REF<x> {INCLude|DONTInclude}
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:REF<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:SETTime <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:SETTime?
    - SEARCH:SEARCH<x>:TRIGger:A:STATE {ON|OFF|<NR1>}
    - SEARCH:SEARCH<x>:TRIGger:A:STATE?
    - SEARCH:SEARCH<x>:TRIGger:A:STOPAcq {ON|OFF|<NR1>}
    - SEARCH:SEARCH<x>:TRIGger:A:STOPAcq?
    - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:LOGICQUALification {ON|OFF}
    - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:LOGICQUALification?
    - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:POLarity {STAYSHigh|STAYSLow|EITher}
    - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:POLarity?
    - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
    - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:SOUrce?
    - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:THReshold <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:THReshold?
    - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:TIMe <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:TIMe?
    - SEARCH:SEARCH<x>:TRIGger:A:TYPe {EDGE|RUNT|TRANsition|PULSEWidth|TIMEOut|LOGIc|SETHold|Bus}
    - SEARCH:SEARCH<x>:TRIGger:A:TYPe?
    - SEARCH:SELected SEARCH1
    - SEARCH:SELected?
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


class SearchSelected(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SELected`` command.

    Description:
        - This command sets or queries the selected search, for example SEARCH1. The search number
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SELected?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SELected?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SEARCH:SELected value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SELected SEARCH1
        - SEARCH:SELected?
        ```

    Info:
        - ``SEARCH1`` is the specified search.
    """


class SearchSearchItemTriggerAType(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:TYPe`` command.

    Description:
        - This command sets or queries the trigger type setting for a search to determine where to
          place a mark. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:TYPe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:TYPe value``
          command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:TYPe {EDGE|RUNT|TRANsition|PULSEWidth|TIMEOut|LOGIc|SETHold|Bus}
        - SEARCH:SEARCH<x>:TRIGger:A:TYPe?
        ```

    Info:
        - ``EDGE`` triggers when the source input signal amplitude crosses the specified level in
          the direction given by the slope.
        - ``RUNT`` triggers when a pulse crosses the first preset voltage threshold but does not
          cross the second preset threshold before recrossing the first. The thresholds are set with
          the ``SEARCH:SEARCH<x>:TRIGger:A:RUNt:HIGH`` and
          ``SEARCH:SEARCH<x>:TRIGger:A:RUNt:LOW THRESHOLD`` commands.
        - ``TRANsition`` triggers when a pulse crosses both thresholds in the same direction as the
          specified polarity and the transition time between the two threshold crossings is greater
          or less than the specified time delta.
        - ``PULSEWidth`` triggers on input signal source pulses that are inside or outside of the
          given time range specified by ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit``
          and ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:MORELimit``. The polarity is selected
          using the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT``: POLarity command.
        - ``TIMEOut`` triggers on an input signal source that stays above, stays below, or stays
          either above or beow the trigger level for a given time.
        - ``LOGIc`` specifies that a search occurs when specified conditions are met, and is
          controlled by the ``SEARCH:A:LOGIc`` commands.
        - ``SETHold`` triggers on a functional pattern combination of one to three data sources at
          the time of the clock transition.
        - ``Bus`` specifies that a search occurs when a communications signal is found.
    """  # noqa: E501


class SearchSearchItemTriggerATimeoutTime(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:TIMe`` command.

    Description:
        - This command sets or queries the time setting for a timeout trigger search to determine
          where to place a mark. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:TIMe?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:TIMe?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:TIMe value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:TIMe <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:TIMe?
        ```

    Info:
        - ``<NR3>`` is the time in seconds.
    """


class SearchSearchItemTriggerATimeoutThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:THReshold`` command.

    Description:
        - Sets or queries the source threshold level for a timeout trigger search to determine where
          to place a mark. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:THReshold?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:THReshold value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:THReshold <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:THReshold?
        ```

    Info:
        - ``<NR3>`` is the source threshold level for a timeout trigger search.
    """


class SearchSearchItemTriggerATimeoutSource(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:SOUrce`` command.

    Description:
        - This command sets and queries the source for timeout search input. The search number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:SOUrce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:SOUrce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:SOUrce value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
        - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an input channel as the edge source, where <x> = 1, 2, 3, 4, 5, 6, 7,
          or 8, depending on the number of channels in your instrument.
        - ``DCH<x>_D<x>`` specifies a digital channel for the search source. The supported digital
          channel value is 1. The supported digital bit values are 0 to 15.
        - ``MATH<x>`` specifies the math waveform as the search source, where <x> = ≥1.
        - ``REF<x>`` specifies the reference waveform as the search source, where <x> = ≥1.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the source waveform the
          specified search.
    """


class SearchSearchItemTriggerATimeoutPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:POLarity`` command.

    Description:
        - The polarity to be used for a Timeout search. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:POLarity?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:POLarity value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:POLarity {STAYSHigh|STAYSLow|EITher}
        - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:POLarity?
        ```

    Info:
        - ``STAYSHigh`` specifies the polarity stays HIGH.
        - ``STAYSLow`` specifies the polarity stays LOW.
        - ``EITher`` specifies the polarity stays HIGH or stays LOW.
    """


class SearchSearchItemTriggerATimeoutLogicqualification(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:LOGICQUALification`` command.

    Description:
        - This command specifies whether or not to use logic qualification for a timeout search. The
          search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:LOGICQUALification?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:LOGICQUALification?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:LOGICQUALification value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:LOGICQUALification {ON|OFF}
        - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:LOGICQUALification?
        ```

    Info:
        - ``ON`` specifies to use logic qualification.
        - ``OFF`` specifies not to use logic qualification.
    """


class SearchSearchItemTriggerATimeout(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.logicqualification``: The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:LOGICQUALification``
          command.
        - ``.polarity``: The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:POLarity`` command.
        - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:SOUrce`` command.
        - ``.threshold``: The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:THReshold`` command.
        - ``.time``: The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:TIMe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._logicqualification = SearchSearchItemTriggerATimeoutLogicqualification(
            device, f"{self._cmd_syntax}:LOGICQUALification"
        )
        self._polarity = SearchSearchItemTriggerATimeoutPolarity(
            device, f"{self._cmd_syntax}:POLarity"
        )
        self._source = SearchSearchItemTriggerATimeoutSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = SearchSearchItemTriggerATimeoutThreshold(
            device, f"{self._cmd_syntax}:THReshold"
        )
        self._time = SearchSearchItemTriggerATimeoutTime(device, f"{self._cmd_syntax}:TIMe")

    @property
    def logicqualification(self) -> SearchSearchItemTriggerATimeoutLogicqualification:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:LOGICQUALification`` command.

        Description:
            - This command specifies whether or not to use logic qualification for a timeout search.
              The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:LOGICQUALification?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:LOGICQUALification?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:LOGICQUALification value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:LOGICQUALification {ON|OFF}
            - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:LOGICQUALification?
            ```

        Info:
            - ``ON`` specifies to use logic qualification.
            - ``OFF`` specifies not to use logic qualification.
        """
        return self._logicqualification

    @property
    def polarity(self) -> SearchSearchItemTriggerATimeoutPolarity:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:POLarity`` command.

        Description:
            - The polarity to be used for a Timeout search. The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:POLarity?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:POLarity value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:POLarity {STAYSHigh|STAYSLow|EITher}
            - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:POLarity?
            ```

        Info:
            - ``STAYSHigh`` specifies the polarity stays HIGH.
            - ``STAYSLow`` specifies the polarity stays LOW.
            - ``EITher`` specifies the polarity stays HIGH or stays LOW.
        """
        return self._polarity

    @property
    def source(self) -> SearchSearchItemTriggerATimeoutSource:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:SOUrce`` command.

        Description:
            - This command sets and queries the source for timeout search input. The search number
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:SOUrce?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:SOUrce value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
            - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an input channel as the edge source, where <x> = 1, 2, 3, 4, 5, 6,
              7, or 8, depending on the number of channels in your instrument.
            - ``DCH<x>_D<x>`` specifies a digital channel for the search source. The supported
              digital channel value is 1. The supported digital bit values are 0 to 15.
            - ``MATH<x>`` specifies the math waveform as the search source, where <x> = ≥1.
            - ``REF<x>`` specifies the reference waveform as the search source, where <x> = ≥1.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the source waveform the
              specified search.
        """  # noqa: E501
        return self._source

    @property
    def threshold(self) -> SearchSearchItemTriggerATimeoutThreshold:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:THReshold`` command.

        Description:
            - Sets or queries the source threshold level for a timeout trigger search to determine
              where to place a mark. The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:THReshold?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:THReshold value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:THReshold <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:THReshold?
            ```

        Info:
            - ``<NR3>`` is the source threshold level for a timeout trigger search.
        """
        return self._threshold

    @property
    def time(self) -> SearchSearchItemTriggerATimeoutTime:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:TIMe`` command.

        Description:
            - This command sets or queries the time setting for a timeout trigger search to
              determine where to place a mark. The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:TIMe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:TIMe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:TIMe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:TIMe <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:TIMe?
            ```

        Info:
            - ``<NR3>`` is the time in seconds.
        """
        return self._time


class SearchSearchItemTriggerAStopacq(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:STOPAcq`` command.

    Description:
        - This command sets or queries whether acquisitions are stopped when a search hit is found.
          The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:STOPAcq?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:STOPAcq?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:STOPAcq value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:STOPAcq {ON|OFF|<NR1>}
        - SEARCH:SEARCH<x>:TRIGger:A:STOPAcq?
        ```

    Info:
        - ``<x>`` is the number of the search on which to enable or disable the stop acquisition
          function.
        - ``<NR1>`` = 1 enables stopping when a search hit is found. Any other character disables
          the feature.
        - ``ON`` enables stopping when a search hit is found.
        - ``OFF`` disables stopping on a search hit.
    """


class SearchSearchItemTriggerAState(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:STATE`` command.

    Description:
        - This command sets or queries the enabled state of the search. The search number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:STATE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:STATE value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:STATE {ON|OFF|<NR1>}
        - SEARCH:SEARCH<x>:TRIGger:A:STATE?
        ```

    Info:
        - ``<NR1>`` = 1 enables the search. Any other character disables the search.
        - ``ON`` enables the search.
        - ``OFF`` disables the search.
    """


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


class SearchSearchItemTriggerASetholdLogicpatternRefItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead
):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:REF<x>`` command.

    Description:
        - This command sets and returns the conditions used for generating an A logic pattern, with
          respect to the defined input pattern, and identifies the time that the selected pattern
          may be true and still generate the trigger. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:REF<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:REF<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:REF<x> {INCLude|DONTInclude}
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:REF<x>?
        ```

    Info:
        - ``INCLude`` specifies including the specified reference SETHOLD inputs in the specified
          search.
        - ``DONTInclude`` specifies not including the specified reference SETHOLD inputs in the
          specified search.
    """


class SearchSearchItemTriggerASetholdLogicpatternMathItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead
):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:MATH<x>`` command.

    Description:
        - This command sets or queries the conditions used for generating an A logic pattern, with
          respect to the defined input pattern, and identifies the time that the selected pattern
          may be true and still generate the trigger. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:MATH<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:MATH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:MATH<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:MATH<x> {INCLude|DONTInclude}
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:MATH<x>?
        ```

    Info:
        - ``INCLude`` specifies including the specified math SETHOLD inputs in the specified search.
        - ``DONTInclude`` specifies not including the specified math SETHOLD inputs in the specified
          search.
    """


class SearchSearchItemTriggerASetholdLogicpatternDchItemDigitalBit(
    ValidatedDigitalBit, SCPICmdWrite, SCPICmdRead
):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:DCH<x>_D<x>`` command.

    Description:
        - This command sets or queries the conditions used for generating an A logic pattern, with
          respect to the defined input pattern, and identifies the time that the selected pattern
          may be true and still generate the trigger. The search number is specified by x. The
          supported digital channel value is 1. The supported digital bit values are 0 to 15.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:DCH<x>_D<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:DCH<x>_D<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:DCH<x>_D<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:DCH<x>_D<x> {INCLude|DONTInclude}
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:DCH<x>_D<x>?
        ```

    Info:
        - ``INCLude`` specifies including the specified channel SETHOLD inputs in the specified
          search.
        - ``DONTInclude`` specifies not including the specified channel SETHOLD inputs in the
          specified search.
    """


class SearchSearchItemTriggerASetholdLogicpatternDchItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:DCH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:DCH<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:DCH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.d``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:DCH<x>_D<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._d: Dict[int, SearchSearchItemTriggerASetholdLogicpatternDchItemDigitalBit] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerASetholdLogicpatternDchItemDigitalBit(
                    device, f"{self._cmd_syntax}_D{x}"
                )
            )
        )

    @property
    def d(self) -> Dict[int, SearchSearchItemTriggerASetholdLogicpatternDchItemDigitalBit]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:DCH<x>_D<x>`` command.

        Description:
            - This command sets or queries the conditions used for generating an A logic pattern,
              with respect to the defined input pattern, and identifies the time that the selected
              pattern may be true and still generate the trigger. The search number is specified by
              x. The supported digital channel value is 1. The supported digital bit values are 0 to
              15.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:DCH<x>_D<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:DCH<x>_D<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:DCH<x>_D<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:DCH<x>_D<x> {INCLude|DONTInclude}
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:DCH<x>_D<x>?
            ```

        Info:
            - ``INCLude`` specifies including the specified channel SETHOLD inputs in the specified
              search.
            - ``DONTInclude`` specifies not including the specified channel SETHOLD inputs in the
              specified search.
        """
        return self._d


class SearchSearchItemTriggerASetholdLogicpatternChannel(
    ValidatedChannel, SCPICmdWrite, SCPICmdRead
):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:CH<x>`` command.

    Description:
        - This command sets or queries the conditions used for generating an A logic pattern, with
          respect to the defined input pattern, and identifies the time that the selected pattern
          may be true and still generate the trigger. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:CH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:CH<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:CH<x> {INCLude|DONTInclude}
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:CH<x>?
        ```

    Info:
        - ``INCLude`` specifies including the specified channel SETHOLD inputs in the specified
          search.
        - ``DONTInclude`` specifies not including the specified channel SETHOLD inputs in the
          specified search.
    """


class SearchSearchItemTriggerASetholdLogicpattern(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:CH<x>`` command.
        - ``.dch``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:DCH<x>`` command tree.
        - ``.math``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:MATH<x>`` command.
        - ``.ref``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:REF<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, SearchSearchItemTriggerASetholdLogicpatternChannel] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerASetholdLogicpatternChannel(
                    device, f"{self._cmd_syntax}:CH{x}"
                )
            )
        )
        self._dch: Dict[int, SearchSearchItemTriggerASetholdLogicpatternDchItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerASetholdLogicpatternDchItem(
                    device, f"{self._cmd_syntax}:DCH{x}"
                )
            )
        )
        self._math: Dict[int, SearchSearchItemTriggerASetholdLogicpatternMathItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerASetholdLogicpatternMathItem(
                    device, f"{self._cmd_syntax}:MATH{x}"
                )
            )
        )
        self._ref: Dict[int, SearchSearchItemTriggerASetholdLogicpatternRefItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerASetholdLogicpatternRefItem(
                    device, f"{self._cmd_syntax}:REF{x}"
                )
            )
        )

    @property
    def ch(self) -> Dict[int, SearchSearchItemTriggerASetholdLogicpatternChannel]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:CH<x>`` command.

        Description:
            - This command sets or queries the conditions used for generating an A logic pattern,
              with respect to the defined input pattern, and identifies the time that the selected
              pattern may be true and still generate the trigger. The search number is specified by
              x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:CH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:CH<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:CH<x> {INCLude|DONTInclude}
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:CH<x>?
            ```

        Info:
            - ``INCLude`` specifies including the specified channel SETHOLD inputs in the specified
              search.
            - ``DONTInclude`` specifies not including the specified channel SETHOLD inputs in the
              specified search.
        """
        return self._ch

    @property
    def dch(self) -> Dict[int, SearchSearchItemTriggerASetholdLogicpatternDchItem]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:DCH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:DCH<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:DCH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.d``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:DCH<x>_D<x>`` command.
        """
        return self._dch

    @property
    def math(self) -> Dict[int, SearchSearchItemTriggerASetholdLogicpatternMathItem]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:MATH<x>`` command.

        Description:
            - This command sets or queries the conditions used for generating an A logic pattern,
              with respect to the defined input pattern, and identifies the time that the selected
              pattern may be true and still generate the trigger. The search number is specified by
              x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:MATH<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:MATH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:MATH<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:MATH<x> {INCLude|DONTInclude}
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:MATH<x>?
            ```

        Info:
            - ``INCLude`` specifies including the specified math SETHOLD inputs in the specified
              search.
            - ``DONTInclude`` specifies not including the specified math SETHOLD inputs in the
              specified search.
        """
        return self._math

    @property
    def ref(self) -> Dict[int, SearchSearchItemTriggerASetholdLogicpatternRefItem]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:REF<x>`` command.

        Description:
            - This command sets and returns the conditions used for generating an A logic pattern,
              with respect to the defined input pattern, and identifies the time that the selected
              pattern may be true and still generate the trigger. The search number is specified by
              x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:REF<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:REF<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:REF<x> {INCLude|DONTInclude}
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:REF<x>?
            ```

        Info:
            - ``INCLude`` specifies including the specified reference SETHOLD inputs in the
              specified search.
            - ``DONTInclude`` specifies not including the specified reference SETHOLD inputs in the
              specified search.
        """
        return self._ref


class SearchSearchItemTriggerASetholdLevelRefItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead
):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:REF<x>`` command.

    Description:
        - This command sets or queries the voltage level to use for setup & hold trigger search. The
          search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:REF<x>?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:REF<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:REF<x> <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:REF<x>?
        ```

    Info:
        - ``<NR3>`` is the voltage level to use for setup & hold trigger search.
    """


class SearchSearchItemTriggerASetholdLevelMathItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead
):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:MATH<x>`` command.

    Description:
        - This command sets or queries the voltage level to use for setup & hold trigger search. The
          search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:MATH<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:MATH<x>?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:MATH<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:MATH<x> <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:MATH<x>?
        ```

    Info:
        - ``<NR3>`` isi the voltage level to use for setup & hold trigger search.
    """


class SearchSearchItemTriggerASetholdLevelChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:CH<x>`` command.

    Description:
        - This command sets or queries the voltage level to use for setup & hold trigger search. The
          search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:CH<x>?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:CH<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:CH<x> <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:CH<x>?
        ```

    Info:
        - ``<NR3>`` the voltage level to use for setup & hold trigger search.
    """


class SearchSearchItemTriggerASetholdLevel(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:CH<x>`` command.
        - ``.math``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:MATH<x>`` command.
        - ``.ref``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:REF<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, SearchSearchItemTriggerASetholdLevelChannel] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerASetholdLevelChannel(
                    device, f"{self._cmd_syntax}:CH{x}"
                )
            )
        )
        self._math: Dict[int, SearchSearchItemTriggerASetholdLevelMathItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerASetholdLevelMathItem(
                    device, f"{self._cmd_syntax}:MATH{x}"
                )
            )
        )
        self._ref: Dict[int, SearchSearchItemTriggerASetholdLevelRefItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerASetholdLevelRefItem(
                    device, f"{self._cmd_syntax}:REF{x}"
                )
            )
        )

    @property
    def ch(self) -> Dict[int, SearchSearchItemTriggerASetholdLevelChannel]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:CH<x>`` command.

        Description:
            - This command sets or queries the voltage level to use for setup & hold trigger search.
              The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:CH<x>?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:CH<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:CH<x> <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:CH<x>?
            ```

        Info:
            - ``<NR3>`` the voltage level to use for setup & hold trigger search.
        """
        return self._ch

    @property
    def math(self) -> Dict[int, SearchSearchItemTriggerASetholdLevelMathItem]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:MATH<x>`` command.

        Description:
            - This command sets or queries the voltage level to use for setup & hold trigger search.
              The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:MATH<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:MATH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:MATH<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:MATH<x> <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:MATH<x>?
            ```

        Info:
            - ``<NR3>`` isi the voltage level to use for setup & hold trigger search.
        """
        return self._math

    @property
    def ref(self) -> Dict[int, SearchSearchItemTriggerASetholdLevelRefItem]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:REF<x>`` command.

        Description:
            - This command sets or queries the voltage level to use for setup & hold trigger search.
              The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:REF<x>?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:REF<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:REF<x> <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:REF<x>?
            ```

        Info:
            - ``<NR3>`` is the voltage level to use for setup & hold trigger search.
        """
        return self._ref


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


class SearchSearchItemTriggerASetholdClockThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:THReshold`` command.

    Description:
        - This command sets or queries the clock threshold setting for a setup/hold trigger search
          to determine where to place a mark. The search number is specified by x.

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
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:THReshold <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:THReshold?
        ```

    Info:
        - ``<NR3>`` the clock threshold setting for a setup/hold trigger search.
    """


class SearchSearchItemTriggerASetholdClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce`` command.

    Description:
        - This command sets or queries the clock source setting for a setup/hold trigger search to
          determine where to place a mark. The search number is specified by x.

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
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an input channel as the edge source, where <x> = 1, 2, 3, 4, 5, 6, 7,
          or 8, depending on the number of channels in your instrument.
        - ``DCH<x>_D<x>`` specifies a digital waveform as the setup and hold clock source waveform
          for the specified search. The supported digital channel value is 1. The supported digital
          bit values are 0 to 15.
        - ``MATH<x>`` specifies the math waveform as the search source, where <x> = ≥1.
        - ``REF<x>`` specifies the reference waveform as the search source, where <x> = ≥1.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the setup and hold clock source
          waveform for the specified search.
    """  # noqa: E501


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
            - This command sets or queries the clock source setting for a setup/hold trigger search
              to determine where to place a mark. The search number is specified by x.

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
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an input channel as the edge source, where <x> = 1, 2, 3, 4, 5, 6,
              7, or 8, depending on the number of channels in your instrument.
            - ``DCH<x>_D<x>`` specifies a digital waveform as the setup and hold clock source
              waveform for the specified search. The supported digital channel value is 1. The
              supported digital bit values are 0 to 15.
            - ``MATH<x>`` specifies the math waveform as the search source, where <x> = ≥1.
            - ``REF<x>`` specifies the reference waveform as the search source, where <x> = ≥1.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the setup and hold clock
              source waveform for the specified search.
        """  # noqa: E501
        return self._source

    @property
    def threshold(self) -> SearchSearchItemTriggerASetholdClockThreshold:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:THReshold`` command.

        Description:
            - This command sets or queries the clock threshold setting for a setup/hold trigger
              search to determine where to place a mark. The search number is specified by x.

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
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:THReshold <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:THReshold?
            ```

        Info:
            - ``<NR3>`` the clock threshold setting for a setup/hold trigger search.
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
        - ``.holdtime``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:HOLDTime`` command.
        - ``.level``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel`` command tree.
        - ``.logicpattern``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern`` command tree.
        - ``.settime``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:SETTime`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._clock = SearchSearchItemTriggerASetholdClock(device, f"{self._cmd_syntax}:CLOCk")
        self._holdtime = SearchSearchItemTriggerASetholdHoldtime(
            device, f"{self._cmd_syntax}:HOLDTime"
        )
        self._level = SearchSearchItemTriggerASetholdLevel(device, f"{self._cmd_syntax}:LEVel")
        self._logicpattern = SearchSearchItemTriggerASetholdLogicpattern(
            device, f"{self._cmd_syntax}:LOGICPattern"
        )
        self._settime = SearchSearchItemTriggerASetholdSettime(
            device, f"{self._cmd_syntax}:SETTime"
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
    def level(self) -> SearchSearchItemTriggerASetholdLevel:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:CH<x>`` command.
            - ``.math``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:MATH<x>`` command.
            - ``.ref``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel:REF<x>`` command.
        """
        return self._level

    @property
    def logicpattern(self) -> SearchSearchItemTriggerASetholdLogicpattern:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:CH<x>`` command.
            - ``.dch``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:DCH<x>`` command tree.
            - ``.math``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:MATH<x>`` command.
            - ``.ref``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern:REF<x>`` command.
        """
        return self._logicpattern

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
        - This command sets or queries the condition setting for a runt trigger search to determine
          where to place a mark. The search number is specified by x.

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
        - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn {OCCURS|LESSthan|MOREthan|EQual}NOTEQual}
        - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn?
        ```

    Info:
        - ``LESSthan`` argument sets the instrument to search if the a runt pulse is detected with
          width less than the time set by the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth`` command.
        - ``MOREthan`` argument sets the instrument to search if the a runt pulse is detected with
          width more than the time set by the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth`` command.
        - ``EQual`` argument sets the instrument to search when the pattern is true for a time
          period equal to the time period specified in ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth``
          within a ±5% tolerance.
        - ``NOTEQual`` argument sets the instrument to search when the pattern is true for atime
          period greater than or less than (but not equal) the time period specified in
          ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth`` within a ±5% tolerance.
        - ``OCCURS`` argument specifies a search event if a runt of any detectable width occurs.
    """


class SearchSearchItemTriggerARuntThresholdLow(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:LOW`` command.

    Description:
        - Sets or queries the source threshold LOW level for a runt trigger search to determine
          where to place a mark. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:LOW?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:LOW?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:LOW value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:LOW <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:LOW?
        ```

    Info:
        - ``<NR3>`` is the source threshold LOW level for a runt trigger search.
    """


class SearchSearchItemTriggerARuntThresholdHigh(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:HIGH`` command.

    Description:
        - This command sets or queries the source threshold HIGH level for a runt trigger search to
          determine where to place a mark.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:HIGH?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:HIGH?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:HIGH value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:HIGH <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:HIGH?
        ```

    Info:
        - ``<NR3>`` is the source threshold HIGH level for a runt trigger search.
    """


class SearchSearchItemTriggerARuntThreshold(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.high``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:HIGH`` command.
        - ``.low``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:LOW`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._high = SearchSearchItemTriggerARuntThresholdHigh(device, f"{self._cmd_syntax}:HIGH")
        self._low = SearchSearchItemTriggerARuntThresholdLow(device, f"{self._cmd_syntax}:LOW")

    @property
    def high(self) -> SearchSearchItemTriggerARuntThresholdHigh:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:HIGH`` command.

        Description:
            - This command sets or queries the source threshold HIGH level for a runt trigger search
              to determine where to place a mark.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:HIGH?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:HIGH?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:HIGH value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:HIGH <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:HIGH?
            ```

        Info:
            - ``<NR3>`` is the source threshold HIGH level for a runt trigger search.
        """
        return self._high

    @property
    def low(self) -> SearchSearchItemTriggerARuntThresholdLow:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:LOW`` command.

        Description:
            - Sets or queries the source threshold LOW level for a runt trigger search to determine
              where to place a mark. The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:LOW?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:LOW?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:LOW value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:LOW <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:LOW?
            ```

        Info:
            - ``<NR3>`` is the source threshold LOW level for a runt trigger search.
        """
        return self._low


class SearchSearchItemTriggerARuntSource(SCPICmdWrite):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce`` command.

    Description:
        - This command sets and queries the source for the Runt search input. The search number is
          specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce {CH<x>|REF<x>}
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the search source, where the channel number is
          specified by x.
        - ``REF<x>`` specifies the reference waveform as the search source, where the reference
          number is specified by x.
    """


class SearchSearchItemTriggerARuntPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity`` command.

    Description:
        - This command specifies the polarity for the runt search. The search number is specified by
          x.

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
        - SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity {POSitive|NEGative|EITher}
        - SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity?
        ```

    Info:
        - ``POSitive`` specifies using positive polarity for the runt search.
        - ``NEGative`` specifies using negative polarity for the runt search.
        - ``EITher`` specifies using either positive or negative polarity for the runt search.
    """


class SearchSearchItemTriggerARuntLogicqualification(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:LOGICQUALification`` command.

    Description:
        - This command specifies whether or not to use logic qualification for a runt search. The
          search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:LOGICQUALification?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:LOGICQUALification?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:LOGICQUALification value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:RUNT:LOGICQUALification {ON|OFF}
        - SEARCH:SEARCH<x>:TRIGger:A:RUNT:LOGICQUALification?
        ```

    Info:
        - ``ON`` specifies to use logic qualification for a runt search.
        - ``OFF`` specifies not to use logic qualification for a runt search.
    """


class SearchSearchItemTriggerARunt(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.logicqualification``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:LOGICQUALification``
          command.
        - ``.polarity``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity`` command.
        - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce`` command.
        - ``.threshold``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold`` command tree.
        - ``.when``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn`` command.
        - ``.width``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._logicqualification = SearchSearchItemTriggerARuntLogicqualification(
            device, f"{self._cmd_syntax}:LOGICQUALification"
        )
        self._polarity = SearchSearchItemTriggerARuntPolarity(
            device, f"{self._cmd_syntax}:POLarity"
        )
        self._source = SearchSearchItemTriggerARuntSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = SearchSearchItemTriggerARuntThreshold(
            device, f"{self._cmd_syntax}:THReshold"
        )
        self._when = SearchSearchItemTriggerARuntWhen(device, f"{self._cmd_syntax}:WHEn")
        self._width = SearchSearchItemTriggerARuntWidth(device, f"{self._cmd_syntax}:WIDth")

    @property
    def logicqualification(self) -> SearchSearchItemTriggerARuntLogicqualification:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:LOGICQUALification`` command.

        Description:
            - This command specifies whether or not to use logic qualification for a runt search.
              The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:LOGICQUALification?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:LOGICQUALification?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:LOGICQUALification value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:RUNT:LOGICQUALification {ON|OFF}
            - SEARCH:SEARCH<x>:TRIGger:A:RUNT:LOGICQUALification?
            ```

        Info:
            - ``ON`` specifies to use logic qualification for a runt search.
            - ``OFF`` specifies not to use logic qualification for a runt search.
        """
        return self._logicqualification

    @property
    def polarity(self) -> SearchSearchItemTriggerARuntPolarity:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity`` command.

        Description:
            - This command specifies the polarity for the runt search. The search number is
              specified by x.

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
            - SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity {POSitive|NEGative|EITher}
            - SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity?
            ```

        Info:
            - ``POSitive`` specifies using positive polarity for the runt search.
            - ``NEGative`` specifies using negative polarity for the runt search.
            - ``EITher`` specifies using either positive or negative polarity for the runt search.
        """
        return self._polarity

    @property
    def source(self) -> SearchSearchItemTriggerARuntSource:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce`` command.

        Description:
            - This command sets and queries the source for the Runt search input. The search number
              is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce {CH<x>|REF<x>}
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the search source, where the channel number
              is specified by x.
            - ``REF<x>`` specifies the reference waveform as the search source, where the reference
              number is specified by x.
        """
        return self._source

    @property
    def threshold(self) -> SearchSearchItemTriggerARuntThreshold:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.high``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:HIGH`` command.
            - ``.low``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold:LOW`` command.
        """
        return self._threshold

    @property
    def when(self) -> SearchSearchItemTriggerARuntWhen:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn`` command.

        Description:
            - This command sets or queries the condition setting for a runt trigger search to
              determine where to place a mark. The search number is specified by x.

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
            - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn {OCCURS|LESSthan|MOREthan|EQual}NOTEQual}
            - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn?
            ```

        Info:
            - ``LESSthan`` argument sets the instrument to search if the a runt pulse is detected
              with width less than the time set by the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth``
              command.
            - ``MOREthan`` argument sets the instrument to search if the a runt pulse is detected
              with width more than the time set by the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth``
              command.
            - ``EQual`` argument sets the instrument to search when the pattern is true for a time
              period equal to the time period specified in ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth``
              within a ±5% tolerance.
            - ``NOTEQual`` argument sets the instrument to search when the pattern is true for atime
              period greater than or less than (but not equal) the time period specified in
              ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth`` within a ±5% tolerance.
            - ``OCCURS`` argument specifies a search event if a runt of any detectable width occurs.
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


class SearchSearchItemTriggerAPulsewidthWhen(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn`` command.

    Description:
        - This command specifies to search for a pulse with a width (duration) that is less than,
          greater than, equal to, or unequal to a specified value (set using
          ``SEARch:A:PULSEWidth:WIDth`` ), OR whose ``SEARch:A:PULSEWidth:LOWLimit`` and
          ``SEARch:A:PULSEWidth:HIGHLimit`` ). The search number is specified by x.

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
        - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn {LESSthan|MOREthan|EQual|UNEQual|WIThin|OUTside}
        - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn?
        ```

    Info:
        - ``LESSthan`` causes a search when a pulse is detected with a width less than the time set
          by the ``SEARch:A:PULSEWidth:WIDth`` command.
        - ``MOREthan`` causes a search when a pulse is detected with a width greater than the time
          set by the ``SEARch:A:PULSEWidth:WIDth`` command.
        - ``EQual`` causes a search when a pulse is detected with a width equal to the time period
          specified in ``SEARch:A:PULSEWidth:WIDth`` within a ±5% tolerance.
        - ``UNEQual`` causes a search when a pulse is detected with a width greater than or less
          than (but not equal) the time period specified in ``SEARch:A:PULSEWidth:WIDth`` within a
          ±5% tolerance.
        - ``WIThin`` causes a search when a pulse is detected that is within a range set by two
          values.
        - ``OUTside`` causes a search when a pulse is detected that is outside of a range set by two
          values.
    """  # noqa: E501


class SearchSearchItemTriggerAPulsewidthThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:THReshold`` command.

    Description:
        - Sets or queries the source threshold level for a pulse width trigger search to determine
          where to place a mark. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:THReshold?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:THReshold value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:THReshold <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:THReshold?
        ```

    Info:
        - ``<NR3>`` is the source threshold level for a pulse width trigger search.
    """


class SearchSearchItemTriggerAPulsewidthSource(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce`` command.

    Description:
        - This command sets and queries the source for the pulse width search input. The search
          number is specified by x.

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
        - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
        - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel to use as the source.
        - ``DCH<x>_D<x>`` specifies a digital channel to use as the source. The supported digital
          channel value is 1. The supported digital bit values are 0 to 15.
        - ``MATH<x>`` specifies a math waveform to use as the source.
        - ``REF<x>`` specifies a reference waveform to use as the source.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the source.
    """  # noqa: E501


class SearchSearchItemTriggerAPulsewidthPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity`` command.

    Description:
        - This command specifies the polarity for a pulse width search. The search number is
          specified by x.

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
        - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity {POSitive|NEGative}
        - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity?
        ```

    Info:
        - ``POSitive`` specifies positive polarity for a pulse width search.
        - ``NEGative`` specifies negative polarity for a pulse width search.
    """


class SearchSearchItemTriggerAPulsewidthLowlimit(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOWLimit`` command.

    Description:
        - This command specifies the lower limit to use, in seconds, when searching for a pulse
          whose duration is inside or outside a range of two values. The search number is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOWLimit?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOWLimit?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOWLimit value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOWLimit <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOWLimit?
        ```

    Info:
        - ``<NR3>`` is the lower limit to use, in seconds, when searching for a pulse.
    """


class SearchSearchItemTriggerAPulsewidthLogicqualification(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOGICQUALification`` command.

    Description:
        - This command specifies whether or not to use logic qualification for a pulse width search.
          The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOGICQUALification?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOGICQUALification?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOGICQUALification value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOGICQUALification {ON|OFF}
        - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOGICQUALification?
        ```

    Info:
        - ``ON`` specifies to use logic qualification.
        - ``OFF`` specifies not to use logic qualification.
    """


class SearchSearchItemTriggerAPulsewidthHighlimit(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:HIGHLimit`` command.

    Description:
        - This command specifies the upper limit to use, in seconds, when searching for a pulse
          whose duration is inside or outside a range of two values. The search number is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:HIGHLimit?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:HIGHLimit?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:HIGHLimit value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:HIGHLimit <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:HIGHLimit?
        ```

    Info:
        - ``<NR3>`` is the upper limit to use, in seconds, when searching for a pulse.
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
        - ``.highlimit``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:HIGHLimit`` command.
        - ``.logicqualification``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOGICQUALification``
          command.
        - ``.lowlimit``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOWLimit`` command.
        - ``.polarity``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity`` command.
        - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce`` command.
        - ``.threshold``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:THReshold`` command.
        - ``.when``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._highlimit = SearchSearchItemTriggerAPulsewidthHighlimit(
            device, f"{self._cmd_syntax}:HIGHLimit"
        )
        self._logicqualification = SearchSearchItemTriggerAPulsewidthLogicqualification(
            device, f"{self._cmd_syntax}:LOGICQUALification"
        )
        self._lowlimit = SearchSearchItemTriggerAPulsewidthLowlimit(
            device, f"{self._cmd_syntax}:LOWLimit"
        )
        self._polarity = SearchSearchItemTriggerAPulsewidthPolarity(
            device, f"{self._cmd_syntax}:POLarity"
        )
        self._source = SearchSearchItemTriggerAPulsewidthSource(
            device, f"{self._cmd_syntax}:SOUrce"
        )
        self._threshold = SearchSearchItemTriggerAPulsewidthThreshold(
            device, f"{self._cmd_syntax}:THReshold"
        )
        self._when = SearchSearchItemTriggerAPulsewidthWhen(device, f"{self._cmd_syntax}:WHEn")

    @property
    def highlimit(self) -> SearchSearchItemTriggerAPulsewidthHighlimit:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:HIGHLimit`` command.

        Description:
            - This command specifies the upper limit to use, in seconds, when searching for a pulse
              whose duration is inside or outside a range of two values. The search number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:HIGHLimit?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:HIGHLimit?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:HIGHLimit value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:HIGHLimit <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:HIGHLimit?
            ```

        Info:
            - ``<NR3>`` is the upper limit to use, in seconds, when searching for a pulse.
        """
        return self._highlimit

    @property
    def logicqualification(self) -> SearchSearchItemTriggerAPulsewidthLogicqualification:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOGICQUALification`` command.

        Description:
            - This command specifies whether or not to use logic qualification for a pulse width
              search. The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOGICQUALification?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOGICQUALification?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOGICQUALification value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOGICQUALification {ON|OFF}
            - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOGICQUALification?
            ```

        Info:
            - ``ON`` specifies to use logic qualification.
            - ``OFF`` specifies not to use logic qualification.
        """
        return self._logicqualification

    @property
    def lowlimit(self) -> SearchSearchItemTriggerAPulsewidthLowlimit:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOWLimit`` command.

        Description:
            - This command specifies the lower limit to use, in seconds, when searching for a pulse
              whose duration is inside or outside a range of two values. The search number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOWLimit?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOWLimit?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOWLimit value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOWLimit <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOWLimit?
            ```

        Info:
            - ``<NR3>`` is the lower limit to use, in seconds, when searching for a pulse.
        """
        return self._lowlimit

    @property
    def polarity(self) -> SearchSearchItemTriggerAPulsewidthPolarity:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity`` command.

        Description:
            - This command specifies the polarity for a pulse width search. The search number is
              specified by x.

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
            - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity {POSitive|NEGative}
            - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity?
            ```

        Info:
            - ``POSitive`` specifies positive polarity for a pulse width search.
            - ``NEGative`` specifies negative polarity for a pulse width search.
        """
        return self._polarity

    @property
    def source(self) -> SearchSearchItemTriggerAPulsewidthSource:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce`` command.

        Description:
            - This command sets and queries the source for the pulse width search input. The search
              number is specified by x.

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
            - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
            - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel to use as the source.
            - ``DCH<x>_D<x>`` specifies a digital channel to use as the source. The supported
              digital channel value is 1. The supported digital bit values are 0 to 15.
            - ``MATH<x>`` specifies a math waveform to use as the source.
            - ``REF<x>`` specifies a reference waveform to use as the source.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the source.
        """  # noqa: E501
        return self._source

    @property
    def threshold(self) -> SearchSearchItemTriggerAPulsewidthThreshold:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:THReshold`` command.

        Description:
            - Sets or queries the source threshold level for a pulse width trigger search to
              determine where to place a mark. The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:THReshold?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:THReshold value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:THReshold <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:THReshold?
            ```

        Info:
            - ``<NR3>`` is the source threshold level for a pulse width trigger search.
        """
        return self._threshold

    @property
    def when(self) -> SearchSearchItemTriggerAPulsewidthWhen:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn`` command.

        Description:
            - This command specifies to search for a pulse with a width (duration) that is less
              than, greater than, equal to, or unequal to a specified value (set using
              ``SEARch:A:PULSEWidth:WIDth`` ), OR whose ``SEARch:A:PULSEWidth:LOWLimit`` and
              ``SEARch:A:PULSEWidth:HIGHLimit`` ). The search number is specified by x.

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
            - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn {LESSthan|MOREthan|EQual|UNEQual|WIThin|OUTside}
            - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn?
            ```

        Info:
            - ``LESSthan`` causes a search when a pulse is detected with a width less than the time
              set by the ``SEARch:A:PULSEWidth:WIDth`` command.
            - ``MOREthan`` causes a search when a pulse is detected with a width greater than the
              time set by the ``SEARch:A:PULSEWidth:WIDth`` command.
            - ``EQual`` causes a search when a pulse is detected with a width equal to the time
              period specified in ``SEARch:A:PULSEWidth:WIDth`` within a ±5% tolerance.
            - ``UNEQual`` causes a search when a pulse is detected with a width greater than or less
              than (but not equal) the time period specified in ``SEARch:A:PULSEWidth:WIDth`` within
              a ±5% tolerance.
            - ``WIThin`` causes a search when a pulse is detected that is within a range set by two
              values.
            - ``OUTside`` causes a search when a pulse is detected that is outside of a range set by
              two values.
        """  # noqa: E501
        return self._when


class SearchSearchItemTriggerALogicWhen(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:WHEn`` command.

    Description:
        - This command sets or queries the condition for generating an A or B logic search with
          respect to the defined input pattern.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:WHEn?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:WHEn?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:WHEn value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:WHEn {TRUe|FALSe|MOREThan|LESSThan|EQual|UNEQual}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:WHEn?
        ```

    Info:
        - ``TRUe`` searches on an input value that is true.
        - ``FALSe`` searches on an input value that is false.
        - ``MOREthan`` searches on an input value that is greater than a set value.
        - ``LESSthan`` searches on an input value that is less than a set value.
        - ``EQual`` searches on an input value that is equal to a set value.
        - ``UNEQual`` searches on an input value that is not equal to a set value.
    """


class SearchSearchItemTriggerALogicUseclockedge(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:USEClockedge`` command.

    Description:
        - This command specifies whether or not Logic search uses a clock source. The search number
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:USEClockedge?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:USEClockedge?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:USEClockedge value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:USEClockedge {OFF|ON|0|1}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:USEClockedge?
        ```

    Info:
        - ``OFF`` specifies not to use the clock source.
        - ``ON`` specifies to use the clock source.
        - ``0`` specifies not to use the clock source.
        - ``1`` specifies to use the clock source.
    """


class SearchSearchItemTriggerALogicPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:POLarity`` command.

    Description:
        - This command sets or queries the polarity for the clock channel when Use Clock Edge is set
          to Yes for Logic search type. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:POLarity?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:POLarity?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:POLarity value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:POLarity {POSitive|NEGative|EITher}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:POLarity?
        ```

    Info:
        - ``POSitive`` specifies using the positive clock edge.
        - ``NEGative`` specifies using negative clock edge.
        - ``EITher`` specifies using either the positive or negative clock edge.
    """


class SearchSearchItemTriggerALogicLogicpatternRefItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead
):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:REF<x>`` command.

    Description:
        - This command sets or queries the conditions used for generating an A logic pattern, with
          respect to the defined input pattern, and identifies the time that the selected pattern
          may be true and still generate the trigger. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:REF<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:REF<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:REF<x> {H|L|X}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:REF<x>?
        ```

    Info:
        - ``H`` specifies triggering when the pattern is high.
        - ``L`` specifies triggering when the pattern is low.
        - ``X`` specifies triggering when the pattern is high or low.
    """


class SearchSearchItemTriggerALogicLogicpatternMathItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead
):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:MATH<x>`` command.

    Description:
        - This command sets or queries the conditions used for generating an A logic pattern, with
          respect to the defined input pattern, and identifies the time that the selected pattern
          may be true and still generate the trigger. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:MATH<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:MATH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:MATH<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:MATH<x> {H|L|X}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:MATH<x>?
        ```

    Info:
        - ``H`` specifies triggering when the pattern is high.
        - ``L`` specifies triggering when the pattern is low.
        - ``X`` specifies triggering when the pattern is high or low.
    """


class SearchSearchItemTriggerALogicLogicpatternDchItemDigitalBit(
    ValidatedDigitalBit, SCPICmdWrite, SCPICmdRead
):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:DCH<x>_D<x>`` command.

    Description:
        - This command sets or queries the conditions used for generating an A logic pattern, with
          respect to the defined input pattern, and identifies the time that the selected pattern
          may be true and still generate the trigger. The search number is specified by x. The
          supported digital channel value is 1. The supported digital bit values are 0 to 15.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:DCH<x>_D<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:DCH<x>_D<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:DCH<x>_D<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:DCH<x>_D<x> {H|L|X}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:DCH<x>_D<x>?
        ```

    Info:
        - ``H`` specifies triggering when the pattern is high.
        - ``L`` specifies triggering when the pattern is low.
        - ``X`` specifies triggering when the pattern is high or low.
    """


class SearchSearchItemTriggerALogicLogicpatternDchItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:DCH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:DCH<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:DCH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.d``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:DCH<x>_D<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._d: Dict[int, SearchSearchItemTriggerALogicLogicpatternDchItemDigitalBit] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerALogicLogicpatternDchItemDigitalBit(
                    device, f"{self._cmd_syntax}_D{x}"
                )
            )
        )

    @property
    def d(self) -> Dict[int, SearchSearchItemTriggerALogicLogicpatternDchItemDigitalBit]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:DCH<x>_D<x>`` command.

        Description:
            - This command sets or queries the conditions used for generating an A logic pattern,
              with respect to the defined input pattern, and identifies the time that the selected
              pattern may be true and still generate the trigger. The search number is specified by
              x. The supported digital channel value is 1. The supported digital bit values are 0 to
              15.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:DCH<x>_D<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:DCH<x>_D<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:DCH<x>_D<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:DCH<x>_D<x> {H|L|X}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:DCH<x>_D<x>?
            ```

        Info:
            - ``H`` specifies triggering when the pattern is high.
            - ``L`` specifies triggering when the pattern is low.
            - ``X`` specifies triggering when the pattern is high or low.
        """
        return self._d


class SearchSearchItemTriggerALogicLogicpatternChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:CH<x>`` command.

    Description:
        - This command sets or queries the conditions used for generating an A logic pattern, with
          respect to the defined input pattern, and identifies the time that the selected pattern
          may be true and still generate the trigger. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:CH<x>?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:CH<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:CH<x> {H|L|X}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:CH<x>?
        ```

    Info:
        - ``H`` specifies triggering when the pattern is high.
        - ``L`` specifies triggering when the pattern is low.
        - ``X`` specifies triggering when the pattern is high or low.
    """


class SearchSearchItemTriggerALogicLogicpattern(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:CH<x>`` command.
        - ``.dch``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:DCH<x>`` command tree.
        - ``.math``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:MATH<x>`` command.
        - ``.ref``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:REF<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, SearchSearchItemTriggerALogicLogicpatternChannel] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerALogicLogicpatternChannel(
                    device, f"{self._cmd_syntax}:CH{x}"
                )
            )
        )
        self._dch: Dict[int, SearchSearchItemTriggerALogicLogicpatternDchItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerALogicLogicpatternDchItem(
                    device, f"{self._cmd_syntax}:DCH{x}"
                )
            )
        )
        self._math: Dict[int, SearchSearchItemTriggerALogicLogicpatternMathItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerALogicLogicpatternMathItem(
                    device, f"{self._cmd_syntax}:MATH{x}"
                )
            )
        )
        self._ref: Dict[int, SearchSearchItemTriggerALogicLogicpatternRefItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerALogicLogicpatternRefItem(
                    device, f"{self._cmd_syntax}:REF{x}"
                )
            )
        )

    @property
    def ch(self) -> Dict[int, SearchSearchItemTriggerALogicLogicpatternChannel]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:CH<x>`` command.

        Description:
            - This command sets or queries the conditions used for generating an A logic pattern,
              with respect to the defined input pattern, and identifies the time that the selected
              pattern may be true and still generate the trigger. The search number is specified by
              x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:CH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:CH<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:CH<x> {H|L|X}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:CH<x>?
            ```

        Info:
            - ``H`` specifies triggering when the pattern is high.
            - ``L`` specifies triggering when the pattern is low.
            - ``X`` specifies triggering when the pattern is high or low.
        """
        return self._ch

    @property
    def dch(self) -> Dict[int, SearchSearchItemTriggerALogicLogicpatternDchItem]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:DCH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:DCH<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:DCH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.d``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:DCH<x>_D<x>`` command.
        """
        return self._dch

    @property
    def math(self) -> Dict[int, SearchSearchItemTriggerALogicLogicpatternMathItem]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:MATH<x>`` command.

        Description:
            - This command sets or queries the conditions used for generating an A logic pattern,
              with respect to the defined input pattern, and identifies the time that the selected
              pattern may be true and still generate the trigger. The search number is specified by
              x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:MATH<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:MATH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:MATH<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:MATH<x> {H|L|X}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:MATH<x>?
            ```

        Info:
            - ``H`` specifies triggering when the pattern is high.
            - ``L`` specifies triggering when the pattern is low.
            - ``X`` specifies triggering when the pattern is high or low.
        """
        return self._math

    @property
    def ref(self) -> Dict[int, SearchSearchItemTriggerALogicLogicpatternRefItem]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:REF<x>`` command.

        Description:
            - This command sets or queries the conditions used for generating an A logic pattern,
              with respect to the defined input pattern, and identifies the time that the selected
              pattern may be true and still generate the trigger. The search number is specified by
              x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:REF<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:REF<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:REF<x> {H|L|X}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:REF<x>?
            ```

        Info:
            - ``H`` specifies triggering when the pattern is high.
            - ``L`` specifies triggering when the pattern is low.
            - ``X`` specifies triggering when the pattern is high or low.
        """
        return self._ref


class SearchSearchItemTriggerALogicLevelRefItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead
):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:REF<x>`` command.

    Description:
        - This command sets the voltage level to use for logic trigger search. The search number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:REF<x>?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:REF<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:REF<x> <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:REF<x>?
        ```

    Info:
        - ``<NR3>`` is the voltage level to use for logic trigger search.
    """


class SearchSearchItemTriggerALogicLevelMathItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead
):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:MATH<x>`` command.

    Description:
        - This command sets the voltage level to use for logic trigger search. The search number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:MATH<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:MATH<x>?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:MATH<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:MATH<x> <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:MATH<x>?
        ```

    Info:
        - ``<NR3>`` is the voltage level to use for logic trigger search.
    """


class SearchSearchItemTriggerALogicLevelChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:CH<x>`` command.

    Description:
        - This command sets or queries the voltage level to use for logic trigger search. The search
          number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:CH<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:CH<x> value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:CH<x> <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:CH<x>?
        ```

    Info:
        - ``<NR3>`` is the voltage level to use for logic trigger search.
    """


class SearchSearchItemTriggerALogicLevel(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:CH<x>`` command.
        - ``.math``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:MATH<x>`` command.
        - ``.ref``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:REF<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, SearchSearchItemTriggerALogicLevelChannel] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerALogicLevelChannel(
                    device, f"{self._cmd_syntax}:CH{x}"
                )
            )
        )
        self._math: Dict[int, SearchSearchItemTriggerALogicLevelMathItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerALogicLevelMathItem(
                    device, f"{self._cmd_syntax}:MATH{x}"
                )
            )
        )
        self._ref: Dict[int, SearchSearchItemTriggerALogicLevelRefItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: SearchSearchItemTriggerALogicLevelRefItem(
                    device, f"{self._cmd_syntax}:REF{x}"
                )
            )
        )

    @property
    def ch(self) -> Dict[int, SearchSearchItemTriggerALogicLevelChannel]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:CH<x>`` command.

        Description:
            - This command sets or queries the voltage level to use for logic trigger search. The
              search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:CH<x>?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:CH<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:CH<x> <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:CH<x>?
            ```

        Info:
            - ``<NR3>`` is the voltage level to use for logic trigger search.
        """
        return self._ch

    @property
    def math(self) -> Dict[int, SearchSearchItemTriggerALogicLevelMathItem]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:MATH<x>`` command.

        Description:
            - This command sets the voltage level to use for logic trigger search. The search number
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:MATH<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:MATH<x>?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:MATH<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:MATH<x> <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:MATH<x>?
            ```

        Info:
            - ``<NR3>`` is the voltage level to use for logic trigger search.
        """
        return self._math

    @property
    def ref(self) -> Dict[int, SearchSearchItemTriggerALogicLevelRefItem]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:REF<x>`` command.

        Description:
            - This command sets the voltage level to use for logic trigger search. The search number
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:REF<x>?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:REF<x> value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:REF<x> <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:REF<x>?
            ```

        Info:
            - ``<NR3>`` is the voltage level to use for logic trigger search.
        """
        return self._ref


class SearchSearchItemTriggerALogicInputClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT:CLOCK:SOUrce`` command.

    Description:
        - This command specifies or queries the channel to use as the clock source for logic
          trigger. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT:CLOCK:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT:CLOCK:SOUrce?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT:CLOCK:SOUrce value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT:CLOCK:SOUrce {CH<x>|DCH<x>_D<x>|REF<x>_D<x>}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT:CLOCK:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies one input channel as the edge source, where the channel number is
          specified by x.
        - ``DCH<x>_D<x>`` specifies a digital waveform as the source waveform for the specified
          search. The supported digital channel value is 1. The supported digital bit values are 0
          to 15.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the source waveform for the
          specified search.
    """


class SearchSearchItemTriggerALogicInputClock(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT:CLOCK`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT:CLOCK?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT:CLOCK?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Info:
        - ``CH<x>`` specifies one input channel as the edge source, where the channel number is
          specified by x.

    Properties:
        - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT:CLOCK:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = SearchSearchItemTriggerALogicInputClockSource(
            device, f"{self._cmd_syntax}:SOUrce"
        )

    @property
    def source(self) -> SearchSearchItemTriggerALogicInputClockSource:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT:CLOCK:SOUrce`` command.

        Description:
            - This command specifies or queries the channel to use as the clock source for logic
              trigger. The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT:CLOCK:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT:CLOCK:SOUrce?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT:CLOCK:SOUrce value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT:CLOCK:SOUrce {CH<x>|DCH<x>_D<x>|REF<x>_D<x>}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT:CLOCK:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies one input channel as the edge source, where the channel number is
              specified by x.
            - ``DCH<x>_D<x>`` specifies a digital waveform as the source waveform for the specified
              search. The supported digital channel value is 1. The supported digital bit values are
              0 to 15.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the source waveform for the
              specified search.
        """
        return self._source


class SearchSearchItemTriggerALogicInput(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Info:
        - ``CH<x>`` specifies one input channel as the edge source, where the channel number is
          specified by x.

    Properties:
        - ``.clock``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT:CLOCK`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._clock = SearchSearchItemTriggerALogicInputClock(device, f"{self._cmd_syntax}:CLOCK")

    @property
    def clock(self) -> SearchSearchItemTriggerALogicInputClock:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT:CLOCK`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT:CLOCK?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT:CLOCK?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Info:
            - ``CH<x>`` specifies one input channel as the edge source, where the channel number is
              specified by x.

        Sub-properties:
            - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT:CLOCK:SOUrce`` command.
        """
        return self._clock


class SearchSearchItemTriggerALogicFunction(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion`` command.

    Description:
        - This command sets or queries the logic operator for a pattern or state trigger search to
          determine where to place a mark. The search number is specified by x.

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
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion {AND|NANd|NOR|OR}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion?
        ```

    Info:
        - ``AND`` places a mark if all conditions are true.
        - ``NANd`` places a mark if any of the conditions are false.
        - ``NOR`` places a mark if all conditions are false.
        - ``OR`` places a mark if any of the conditions are true.
    """


class SearchSearchItemTriggerALogicDeltatime(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:DELTatime`` command.

    Description:
        - This command specifies the Logic search delta time value. The time value is used as part
          of the Logic search condition to determine if the duration of a logic pattern meets the
          specified time constraints. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:DELTatime?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:DELTatime?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:DELTatime value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:DELTatime <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:DELTatime?
        ```

    Info:
        - ``<NR3>`` is delta time value.
    """


class SearchSearchItemTriggerALogicClockThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:CLOCk:THReshold`` command.

    Description:
        - This command sets or queries the logic clock threshold for a logic trigger search to
          determine where to place a mark. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:CLOCk:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:CLOCk:THReshold?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:CLOCk:THReshold value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:CLOCk:THReshold <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:CLOCk:THReshold?
        ```

    Info:
        - ``<NR3>`` is the logic clock threshold.
    """


class SearchSearchItemTriggerALogicClock(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:CLOCk?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:CLOCk?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.threshold``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:CLOCk:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._threshold = SearchSearchItemTriggerALogicClockThreshold(
            device, f"{self._cmd_syntax}:THReshold"
        )

    @property
    def threshold(self) -> SearchSearchItemTriggerALogicClockThreshold:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:CLOCk:THReshold`` command.

        Description:
            - This command sets or queries the logic clock threshold for a logic trigger search to
              determine where to place a mark. The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:CLOCk:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:CLOCk:THReshold?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:CLOCk:THReshold value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:CLOCk:THReshold <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:CLOCk:THReshold?
            ```

        Info:
            - ``<NR3>`` is the logic clock threshold.
        """
        return self._threshold


#  pylint: disable=too-many-instance-attributes
class SearchSearchItemTriggerALogic(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.clock``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:CLOCk`` command tree.
        - ``.deltatime``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:DELTatime`` command.
        - ``.function``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion`` command.
        - ``.input``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT`` command tree.
        - ``.level``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel`` command tree.
        - ``.logicpattern``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern`` command tree.
        - ``.polarity``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:POLarity`` command.
        - ``.useclockedge``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:USEClockedge`` command.
        - ``.when``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:WHEn`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._clock = SearchSearchItemTriggerALogicClock(device, f"{self._cmd_syntax}:CLOCk")
        self._deltatime = SearchSearchItemTriggerALogicDeltatime(
            device, f"{self._cmd_syntax}:DELTatime"
        )
        self._function = SearchSearchItemTriggerALogicFunction(
            device, f"{self._cmd_syntax}:FUNCtion"
        )
        self._input = SearchSearchItemTriggerALogicInput(device, f"{self._cmd_syntax}:INPUT")
        self._level = SearchSearchItemTriggerALogicLevel(device, f"{self._cmd_syntax}:LEVel")
        self._logicpattern = SearchSearchItemTriggerALogicLogicpattern(
            device, f"{self._cmd_syntax}:LOGICPattern"
        )
        self._polarity = SearchSearchItemTriggerALogicPolarity(
            device, f"{self._cmd_syntax}:POLarity"
        )
        self._useclockedge = SearchSearchItemTriggerALogicUseclockedge(
            device, f"{self._cmd_syntax}:USEClockedge"
        )
        self._when = SearchSearchItemTriggerALogicWhen(device, f"{self._cmd_syntax}:WHEn")

    @property
    def clock(self) -> SearchSearchItemTriggerALogicClock:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:CLOCk?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.threshold``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:CLOCk:THReshold`` command.
        """
        return self._clock

    @property
    def deltatime(self) -> SearchSearchItemTriggerALogicDeltatime:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:DELTatime`` command.

        Description:
            - This command specifies the Logic search delta time value. The time value is used as
              part of the Logic search condition to determine if the duration of a logic pattern
              meets the specified time constraints. The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:DELTatime?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:DELTatime?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:DELTatime value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:DELTatime <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:DELTatime?
            ```

        Info:
            - ``<NR3>`` is delta time value.
        """
        return self._deltatime

    @property
    def function(self) -> SearchSearchItemTriggerALogicFunction:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion`` command.

        Description:
            - This command sets or queries the logic operator for a pattern or state trigger search
              to determine where to place a mark. The search number is specified by x.

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
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion {AND|NANd|NOR|OR}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion?
            ```

        Info:
            - ``AND`` places a mark if all conditions are true.
            - ``NANd`` places a mark if any of the conditions are false.
            - ``NOR`` places a mark if all conditions are false.
            - ``OR`` places a mark if any of the conditions are true.
        """
        return self._function

    @property
    def input(self) -> SearchSearchItemTriggerALogicInput:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Info:
            - ``CH<x>`` specifies one input channel as the edge source, where the channel number is
              specified by x.

        Sub-properties:
            - ``.clock``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT:CLOCK`` command tree.
        """
        return self._input

    @property
    def level(self) -> SearchSearchItemTriggerALogicLevel:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:CH<x>`` command.
            - ``.math``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:MATH<x>`` command.
            - ``.ref``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel:REF<x>`` command.
        """
        return self._level

    @property
    def logicpattern(self) -> SearchSearchItemTriggerALogicLogicpattern:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:CH<x>`` command.
            - ``.dch``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:DCH<x>`` command tree.
            - ``.math``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:MATH<x>`` command.
            - ``.ref``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern:REF<x>`` command.
        """
        return self._logicpattern

    @property
    def polarity(self) -> SearchSearchItemTriggerALogicPolarity:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:POLarity`` command.

        Description:
            - This command sets or queries the polarity for the clock channel when Use Clock Edge is
              set to Yes for Logic search type. The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:POLarity?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:POLarity value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:POLarity {POSitive|NEGative|EITher}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:POLarity?
            ```

        Info:
            - ``POSitive`` specifies using the positive clock edge.
            - ``NEGative`` specifies using negative clock edge.
            - ``EITher`` specifies using either the positive or negative clock edge.
        """
        return self._polarity

    @property
    def useclockedge(self) -> SearchSearchItemTriggerALogicUseclockedge:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:USEClockedge`` command.

        Description:
            - This command specifies whether or not Logic search uses a clock source. The search
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:USEClockedge?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:USEClockedge?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:USEClockedge value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:USEClockedge {OFF|ON|0|1}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:USEClockedge?
            ```

        Info:
            - ``OFF`` specifies not to use the clock source.
            - ``ON`` specifies to use the clock source.
            - ``0`` specifies not to use the clock source.
            - ``1`` specifies to use the clock source.
        """
        return self._useclockedge

    @property
    def when(self) -> SearchSearchItemTriggerALogicWhen:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:WHEn`` command.

        Description:
            - This command sets or queries the condition for generating an A or B logic search with
              respect to the defined input pattern.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:WHEn?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:WHEn?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:WHEn value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:WHEn {TRUe|FALSe|MOREThan|LESSThan|EQual|UNEQual}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:WHEn?
            ```

        Info:
            - ``TRUe`` searches on an input value that is true.
            - ``FALSe`` searches on an input value that is false.
            - ``MOREthan`` searches on an input value that is greater than a set value.
            - ``LESSthan`` searches on an input value that is less than a set value.
            - ``EQual`` searches on an input value that is equal to a set value.
            - ``UNEQual`` searches on an input value that is not equal to a set value.
        """
        return self._when


class SearchSearchItemTriggerAEdgeThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:THReshold`` command.

    Description:
        - This command sets or queries the source threshold level for an edge trigger search to
          determine where to place a mark. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:THReshold?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:THReshold?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:THReshold value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:EDGE:THReshold <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:EDGE:THReshold?
        ```

    Info:
        - ``<NR3>`` is the source threshold level for an edge trigger search.
    """


class SearchSearchItemTriggerAEdgeSource(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce`` command.

    Description:
        - This command sets or queries the source waveform for an edge trigger search to determine
          where to place a mark. The search number is specified by x.

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
        - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
        - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies one input channel as the edge source, where the channel number is
          specified by x.
        - ``DCH<x>_D<x>`` specifies a digital waveform as the source waveform for the specified
          search. The supported digital channel value is 1. The supported digital bit values are 0
          to 15.
        - ``MATH<x>`` specifies the math waveform as the search source, where the math number is
          specified by x.
        - ``REF<x>`` specifies the reference waveform as the search source, where the reference
          number is specified by x.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the source waveform for the
          specified search.
    """


class SearchSearchItemTriggerAEdgeSlope(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe`` command.

    Description:
        - This command sets or queries the slope for an edge trigger search to determine where to
          place a mark. The search number is specified by x.

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
        - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe {RISe|FALL|EITher}
        - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe?
        ```

    Info:
        - ``RISe`` specifies a rising edge.
        - ``FALL`` specifies a falling edge.
        - ``EITher`` specifies either rising or falling edge.
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
        - ``.threshold``: The ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._slope = SearchSearchItemTriggerAEdgeSlope(device, f"{self._cmd_syntax}:SLOpe")
        self._source = SearchSearchItemTriggerAEdgeSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = SearchSearchItemTriggerAEdgeThreshold(
            device, f"{self._cmd_syntax}:THReshold"
        )

    @property
    def slope(self) -> SearchSearchItemTriggerAEdgeSlope:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe`` command.

        Description:
            - This command sets or queries the slope for an edge trigger search to determine where
              to place a mark. The search number is specified by x.

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
            - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe {RISe|FALL|EITher}
            - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe?
            ```

        Info:
            - ``RISe`` specifies a rising edge.
            - ``FALL`` specifies a falling edge.
            - ``EITher`` specifies either rising or falling edge.
        """
        return self._slope

    @property
    def source(self) -> SearchSearchItemTriggerAEdgeSource:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce`` command.

        Description:
            - This command sets or queries the source waveform for an edge trigger search to
              determine where to place a mark. The search number is specified by x.

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
            - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
            - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies one input channel as the edge source, where the channel number is
              specified by x.
            - ``DCH<x>_D<x>`` specifies a digital waveform as the source waveform for the specified
              search. The supported digital channel value is 1. The supported digital bit values are
              0 to 15.
            - ``MATH<x>`` specifies the math waveform as the search source, where the math number is
              specified by x.
            - ``REF<x>`` specifies the reference waveform as the search source, where the reference
              number is specified by x.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the source waveform for the
              specified search.
        """
        return self._source

    @property
    def threshold(self) -> SearchSearchItemTriggerAEdgeThreshold:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:THReshold`` command.

        Description:
            - This command sets or queries the source threshold level for an edge trigger search to
              determine where to place a mark. The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:THReshold?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:THReshold value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:EDGE:THReshold <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:EDGE:THReshold?
            ```

        Info:
            - ``<NR3>`` is the source threshold level for an edge trigger search.
        """
        return self._threshold


class SearchSearchItemTriggerABusSpiSourcetype(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:SOURCETYpe`` command.

    Description:
        - This command sets or queries trigger Source for SPI bus. The search number is specified by
          x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:SOURCETYpe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:SOURCETYpe?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:SOURCETYpe value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:SOURCETYpe {MISo|MOSi}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:SOURCETYpe?
        ```

    Info:
        - ``MISo`` specifies the trigger source as MISo. The default search source type is MISo.
        - ``MOSi`` specifies the trigger source as MOSi.
    """


class SearchSearchItemTriggerABusSpiDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:VALue`` command.

    Description:
        - The command sets or queries the binary data string used for an SPI bus search to determine
          where to place a mark. The search number is specified by x. The search condition must be
          DATA.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:VALue?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:VALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:VALue?
        ```

    Info:
        - ``<QString>`` specifies the data value in the specified valid format. The valid characters
          are 0, 1, and X for binary format; and A-F, 0-9, and X for hexadecimal format.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusSpiDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:SIZe`` command.

    Description:
        - This command sets or queries the length of the data string in bytes used for the specified
          SPI bus trigger search to determine where to place a mark. The search condition must be
          DATA. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:SIZe?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:SIZe <NR1>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:SIZe?
        ```

    Info:
        - ``<NR1>`` specifies the number of contiguous data bytes.
    """


class SearchSearchItemTriggerABusSpiData(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:SIZe`` command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._size = SearchSearchItemTriggerABusSpiDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._value = SearchSearchItemTriggerABusSpiDataValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def size(self) -> SearchSearchItemTriggerABusSpiDataSize:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:SIZe`` command.

        Description:
            - This command sets or queries the length of the data string in bytes used for the
              specified SPI bus trigger search to determine where to place a mark. The search
              condition must be DATA. The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:SIZe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:SIZe?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:SIZe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:SIZe <NR1>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:SIZe?
            ```

        Info:
            - ``<NR1>`` specifies the number of contiguous data bytes.
        """
        return self._size

    @property
    def value(self) -> SearchSearchItemTriggerABusSpiDataValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:VALue`` command.

        Description:
            - The command sets or queries the binary data string used for an SPI bus search to
              determine where to place a mark. The search number is specified by x. The search
              condition must be DATA.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:VALue?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:VALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:VALue?
            ```

        Info:
            - ``<QString>`` specifies the data value in the specified valid format. The valid
              characters are 0, 1, and X for binary format; and A-F, 0-9, and X for hexadecimal
              format.
        """
        return self._value


class SearchSearchItemTriggerABusSpiCondition(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:CONDition`` command.

    Description:
        - This command sets or queries the search condition for an SPI bus search to determine where
          to place a mark. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:CONDition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:CONDition value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:CONDition {DATA|SS|STARTofframe}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:CONDition?
        ```

    Info:
        - ``DATA`` specifies the trigger condition as Data.
        - ``SS`` specifies the trigger condition as Slave Selection.
        - ``STARTofframe`` specifies the trigger condition as start of frame.
    """


class SearchSearchItemTriggerABusSpi(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:CONDition`` command.
        - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa`` command tree.
        - ``.sourcetype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:SOURCETYpe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = SearchSearchItemTriggerABusSpiCondition(
            device, f"{self._cmd_syntax}:CONDition"
        )
        self._data = SearchSearchItemTriggerABusSpiData(device, f"{self._cmd_syntax}:DATa")
        self._sourcetype = SearchSearchItemTriggerABusSpiSourcetype(
            device, f"{self._cmd_syntax}:SOURCETYpe"
        )

    @property
    def condition(self) -> SearchSearchItemTriggerABusSpiCondition:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:CONDition`` command.

        Description:
            - This command sets or queries the search condition for an SPI bus search to determine
              where to place a mark. The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:CONDition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:CONDition?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:CONDition value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:CONDition {DATA|SS|STARTofframe}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:CONDition?
            ```

        Info:
            - ``DATA`` specifies the trigger condition as Data.
            - ``SS`` specifies the trigger condition as Slave Selection.
            - ``STARTofframe`` specifies the trigger condition as start of frame.
        """
        return self._condition

    @property
    def data(self) -> SearchSearchItemTriggerABusSpiData:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:SIZe`` command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa:VALue`` command.
        """
        return self._data

    @property
    def sourcetype(self) -> SearchSearchItemTriggerABusSpiSourcetype:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:SOURCETYpe`` command.

        Description:
            - This command sets or queries trigger Source for SPI bus. The search number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:SOURCETYpe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:SOURCETYpe?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:SOURCETYpe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:SOURCETYpe {MISo|MOSi}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:SOURCETYpe?
            ```

        Info:
            - ``MISo`` specifies the trigger source as MISo. The default search source type is MISo.
            - ``MOSi`` specifies the trigger source as MOSi.
        """
        return self._sourcetype


class SearchSearchItemTriggerABusSource(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce`` command.

    Description:
        - This command sets or queries the bus source for the bus search to determine where to place
          a mark. The search number is specified by x.

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
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce {B0|B1|B2|B3|B4|B5|B6|B7|B8|B9|B10|B11|B12|B13|B14|B15|B16}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce?
        ```

    Info:
        - ``B<x>`` specifies the bus source as a bus number from B01 to B16. x has a minimum of 0
          and a maximum of 16.
    """  # noqa: E501


class SearchSearchItemTriggerABusSentSlowIdentifierValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:IDentifier:VALue`` command.

    Description:
        - This command sets or queries the binary slow identifier value to be used when searching on
          a SENT bus signal.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:IDentifier:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:IDentifier:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:IDentifier:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:IDentifier:VALue <Qstring>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:IDentifier:VALue?
        ```

    Info:
        - ``Search<x>`` is the number of the search.
        - ``<Qstring>`` is the slow channel identifier binary value.
    """


class SearchSearchItemTriggerABusSentSlowIdentifier(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:IDentifier`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:IDentifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:IDentifier?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:IDentifier:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = SearchSearchItemTriggerABusSentSlowIdentifierValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> SearchSearchItemTriggerABusSentSlowIdentifierValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:IDentifier:VALue`` command.

        Description:
            - This command sets or queries the binary slow identifier value to be used when
              searching on a SENT bus signal.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:IDentifier:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:IDentifier:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:IDentifier:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:IDentifier:VALue <Qstring>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:IDentifier:VALue?
            ```

        Info:
            - ``Search<x>`` is the number of the search.
            - ``<Qstring>`` is the slow channel identifier binary value.
        """
        return self._value


class SearchSearchItemTriggerABusSentSlowDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:VALue`` command.

    Description:
        - This command sets or queries the binary slow channel data value to be used when searching
          on a SENT bus signal.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:VALue?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:VALue <Qstring>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:VALue?
        ```

    Info:
        - ``Search<x>`` is the number of the search.
        - ``<Qstring>`` is the slow channel data binary value.
    """


class SearchSearchItemTriggerABusSentSlowDataQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:QUALifier`` command.

    Description:
        - This command sets or queries the qualifier to be used when searching on SENT slow packet
          bus data.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:QUALifier?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:QUALifier value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQualINrange|OUTrange}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:QUALifier?
        ```

    Info:
        - ``Search<x>`` is the number of the search.
        - ``EQUal`` specifies the qualifier as Equal.
        - ``LESSEQual`` sets the qualifier as Less Than or Equal to.
        - ``LESSThan`` sets the qualifier as Less Than.
        - ``MOREEQual`` sets the qualifier as More Than or Equal to.
        - ``MOREThan`` sets the qualifier as More Than.
        - ``UNEQual`` specifies the qualifier as Unequal.
        - ``INrange`` sets the search qualifier to inside a range.
        - ``OUTrange`` sets the search qualifier to outside a range.
    """  # noqa: E501


class SearchSearchItemTriggerABusSentSlowDataHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:HIVALue`` command.

    Description:
        - This command sets or queries the high binary Slow channel data value to use when searching
          on a SENT bus signal.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:HIVALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:HIVALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:HIVALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:HIVALue?
        ```

    Info:
        - ``Search<x>`` is the Search identifier number.
        - ``<Qstring>`` sets the binary Slow channel data value.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusSentSlowData(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:HIVALue`` command.
        - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:QUALifier`` command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = SearchSearchItemTriggerABusSentSlowDataHivalue(
            device, f"{self._cmd_syntax}:HIVALue"
        )
        self._qualifier = SearchSearchItemTriggerABusSentSlowDataQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._value = SearchSearchItemTriggerABusSentSlowDataValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def hivalue(self) -> SearchSearchItemTriggerABusSentSlowDataHivalue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:HIVALue`` command.

        Description:
            - This command sets or queries the high binary Slow channel data value to use when
              searching on a SENT bus signal.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:HIVALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:HIVALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:HIVALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:HIVALue?
            ```

        Info:
            - ``Search<x>`` is the Search identifier number.
            - ``<Qstring>`` sets the binary Slow channel data value.
        """
        return self._hivalue

    @property
    def qualifier(self) -> SearchSearchItemTriggerABusSentSlowDataQualifier:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:QUALifier`` command.

        Description:
            - This command sets or queries the qualifier to be used when searching on SENT slow
              packet bus data.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:QUALifier?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:QUALifier value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQualINrange|OUTrange}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:QUALifier?
            ```

        Info:
            - ``Search<x>`` is the number of the search.
            - ``EQUal`` specifies the qualifier as Equal.
            - ``LESSEQual`` sets the qualifier as Less Than or Equal to.
            - ``LESSThan`` sets the qualifier as Less Than.
            - ``MOREEQual`` sets the qualifier as More Than or Equal to.
            - ``MOREThan`` sets the qualifier as More Than.
            - ``UNEQual`` specifies the qualifier as Unequal.
            - ``INrange`` sets the search qualifier to inside a range.
            - ``OUTrange`` sets the search qualifier to outside a range.
        """  # noqa: E501
        return self._qualifier

    @property
    def value(self) -> SearchSearchItemTriggerABusSentSlowDataValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:VALue`` command.

        Description:
            - This command sets or queries the binary slow channel data value to be used when
              searching on a SENT bus signal.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:VALue <Qstring>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:VALue?
            ```

        Info:
            - ``Search<x>`` is the number of the search.
            - ``<Qstring>`` is the slow channel data binary value.
        """
        return self._value


class SearchSearchItemTriggerABusSentSlow(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA`` command tree.
        - ``.identifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:IDentifier`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._data = SearchSearchItemTriggerABusSentSlowData(device, f"{self._cmd_syntax}:DATA")
        self._identifier = SearchSearchItemTriggerABusSentSlowIdentifier(
            device, f"{self._cmd_syntax}:IDentifier"
        )

    @property
    def data(self) -> SearchSearchItemTriggerABusSentSlowData:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:HIVALue`` command.
            - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:QUALifier``
              command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA:VALue`` command.
        """
        return self._data

    @property
    def identifier(self) -> SearchSearchItemTriggerABusSentSlowIdentifier:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:IDentifier`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:IDentifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:IDentifier?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:IDentifier:VALue`` command.
        """
        return self._identifier


class SearchSearchItemTriggerABusSentPauseTicksValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:VALue`` command.

    Description:
        - This command sets or queries the minimum number of pause clock ticks to be used when
          searching on a SENT bus signal.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:VALue <NR1>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:VALue?
        ```

    Info:
        - ``Search<x>`` is the number of the search.
        - ``<NR1>`` is the minimum number of pause clock ticks to be used when searching.
    """


class SearchSearchItemTriggerABusSentPauseTicksHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:HIVALue`` command.

    Description:
        - This command sets or queries the maximum number of pause clock ticks to be used when
          searching on a SENT bus signal.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:HIVALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:HIVALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:HIVALue <NR1>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:HIVALue?
        ```

    Info:
        - ``Search<x>`` is the number of the search.
        - ``<NR1>`` is the maximum number of pause clock ticks to be used when searching.
    """


class SearchSearchItemTriggerABusSentPauseTicks(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:HIVALue`` command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = SearchSearchItemTriggerABusSentPauseTicksHivalue(
            device, f"{self._cmd_syntax}:HIVALue"
        )
        self._value = SearchSearchItemTriggerABusSentPauseTicksValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def hivalue(self) -> SearchSearchItemTriggerABusSentPauseTicksHivalue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:HIVALue`` command.

        Description:
            - This command sets or queries the maximum number of pause clock ticks to be used when
              searching on a SENT bus signal.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:HIVALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:HIVALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:HIVALue <NR1>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:HIVALue?
            ```

        Info:
            - ``Search<x>`` is the number of the search.
            - ``<NR1>`` is the maximum number of pause clock ticks to be used when searching.
        """
        return self._hivalue

    @property
    def value(self) -> SearchSearchItemTriggerABusSentPauseTicksValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:VALue`` command.

        Description:
            - This command sets or queries the minimum number of pause clock ticks to be used when
              searching on a SENT bus signal.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:VALue <NR1>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:VALue?
            ```

        Info:
            - ``Search<x>`` is the number of the search.
            - ``<NR1>`` is the minimum number of pause clock ticks to be used when searching.
        """
        return self._value


class SearchSearchItemTriggerABusSentPauseQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:QUALifier`` command.

    Description:
        - This command sets or queries the qualifier to be used when searching on SENT pause pulses.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:QUALifier?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:QUALifier value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|INrange|OUTrange}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:QUALifier?
        ```

    Info:
        - ``Search<x>`` is the number of the search.
        - ``EQUal`` specifies the qualifier as Equal.
        - ``INrange`` sets the qualifier to be within a range.
        - ``LESSEQual`` sets the qualifier as Less Than or Equal to.
        - ``LESSThan`` sets the qualifier as Less Than.
        - ``MOREEQual`` sets the qualifier as More Than or Equal to.
        - ``MOREThan`` sets the qualifier as More Than.
        - ``OUTrange`` sets the qualifier to be outside a range.
        - ``UNEQual`` specifies the qualifier as Unequal.
    """  # noqa: E501


class SearchSearchItemTriggerABusSentPause(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:QUALifier`` command.
        - ``.ticks``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._qualifier = SearchSearchItemTriggerABusSentPauseQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._ticks = SearchSearchItemTriggerABusSentPauseTicks(device, f"{self._cmd_syntax}:TICKs")

    @property
    def qualifier(self) -> SearchSearchItemTriggerABusSentPauseQualifier:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:QUALifier`` command.

        Description:
            - This command sets or queries the qualifier to be used when searching on SENT pause
              pulses.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:QUALifier?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:QUALifier value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|INrange|OUTrange}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:QUALifier?
            ```

        Info:
            - ``Search<x>`` is the number of the search.
            - ``EQUal`` specifies the qualifier as Equal.
            - ``INrange`` sets the qualifier to be within a range.
            - ``LESSEQual`` sets the qualifier as Less Than or Equal to.
            - ``LESSThan`` sets the qualifier as Less Than.
            - ``MOREEQual`` sets the qualifier as More Than or Equal to.
            - ``MOREThan`` sets the qualifier as More Than.
            - ``OUTrange`` sets the qualifier to be outside a range.
            - ``UNEQual`` specifies the qualifier as Unequal.
        """  # noqa: E501
        return self._qualifier

    @property
    def ticks(self) -> SearchSearchItemTriggerABusSentPauseTicks:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:HIVALue`` command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs:VALue`` command.
        """
        return self._ticks


class SearchSearchItemTriggerABusSentFastStatusValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:STATus:VALue`` command.

    Description:
        - This command sets or queries the binary status value to be used when searching on a SENT
          bus signal.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:STATus:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:STATus:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:STATus:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:STATus:VALue <Qstring>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:STATus:VALue?
        ```

    Info:
        - ``Search<x>`` is the number of the search.
        - ``<Qstring>`` is the binary status binary value.
    """


class SearchSearchItemTriggerABusSentFastStatus(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:STATus`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:STATus?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:STATus?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:STATus:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = SearchSearchItemTriggerABusSentFastStatusValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> SearchSearchItemTriggerABusSentFastStatusValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:STATus:VALue`` command.

        Description:
            - This command sets or queries the binary status value to be used when searching on a
              SENT bus signal.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:STATus:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:STATus:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:STATus:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:STATus:VALue <Qstring>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:STATus:VALue?
            ```

        Info:
            - ``Search<x>`` is the number of the search.
            - ``<Qstring>`` is the binary status binary value.
        """
        return self._value


class SearchSearchItemTriggerABusSentFastInvertnibbleValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:INVERTNIBble:VALue`` command.

    Description:
        - This command sets or queries the binary fast message inverted nibble value to be used when
          searching on a SENT bus signal.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:INVERTNIBble:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:INVERTNIBble:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:INVERTNIBble:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:INVERTNIBble:VALue <Qstring>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:INVERTNIBble:VALue?
        ```

    Info:
        - ``Search<x>`` is the number of the search.
        - ``<Qstring>`` is the fast message inverted nibble binary value.
    """


class SearchSearchItemTriggerABusSentFastInvertnibble(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:INVERTNIBble`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:INVERTNIBble?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:INVERTNIBble?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:INVERTNIBble:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = SearchSearchItemTriggerABusSentFastInvertnibbleValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> SearchSearchItemTriggerABusSentFastInvertnibbleValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:INVERTNIBble:VALue`` command.

        Description:
            - This command sets or queries the binary fast message inverted nibble value to be used
              when searching on a SENT bus signal.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:INVERTNIBble:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:INVERTNIBble:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:INVERTNIBble:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:INVERTNIBble:VALue <Qstring>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:INVERTNIBble:VALue?
            ```

        Info:
            - ``Search<x>`` is the number of the search.
            - ``<Qstring>`` is the fast message inverted nibble binary value.
        """
        return self._value


class SearchSearchItemTriggerABusSentFastCounterValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:VALue`` command.

    Description:
        - This command sets or queries the binary fast message counter value to be used when
          searching on a SENT bus signal.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:VALue <Qstring>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:VALue?
        ```

    Info:
        - ``Search<x>`` is the number of the search.
        - ``<Qstring>`` is the Fast Channel 1 counter value.
    """


class SearchSearchItemTriggerABusSentFastCounterQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:QUALifier`` command.

    Description:
        - This command sets or queries the qualifier to be used when searching on SENT fast packet
          bus data for the secure format counter.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:QUALifier?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:QUALifier value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|INrange|OUTrange}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:QUALifier?
        ```

    Info:
        - ``Search<x>`` is the number of the search.
        - ``EQUal`` specifies the qualifier as Equal.
        - ``LESSEQual`` specifies the qualifier as Less Than or Equal to.
        - ``LESSThan`` specifies the qualifier as Less Than.
        - ``MOREEQual`` specifies the qualifier as More Than or Equal to.
        - ``MOREThan`` specifies the qualifier as More Than.
        - ``UNEQual`` specifies the qualifier as Unequal.
        - ``INrange`` sets the qualifier to inside a range.
        - ``OUTrange`` sets the qualifier to outside a range.
    """  # noqa: E501


class SearchSearchItemTriggerABusSentFastCounterHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:HIVALue`` command.

    Description:
        - This command sets or queries the high binary fast message counter value to use when
          searching on a SENT bus signal.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:HIVALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:HIVALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:HIVALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:HIVALue?
        ```

    Info:
        - ``Search<x>`` is the Search identifier number.
        - ``<Qstring>`` sets the Fast Channel 1 counter binary value.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusSentFastCounter(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:HIVALue`` command.
        - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:QUALifier``
          command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = SearchSearchItemTriggerABusSentFastCounterHivalue(
            device, f"{self._cmd_syntax}:HIVALue"
        )
        self._qualifier = SearchSearchItemTriggerABusSentFastCounterQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._value = SearchSearchItemTriggerABusSentFastCounterValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def hivalue(self) -> SearchSearchItemTriggerABusSentFastCounterHivalue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:HIVALue`` command.

        Description:
            - This command sets or queries the high binary fast message counter value to use when
              searching on a SENT bus signal.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:HIVALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:HIVALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:HIVALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:HIVALue?
            ```

        Info:
            - ``Search<x>`` is the Search identifier number.
            - ``<Qstring>`` sets the Fast Channel 1 counter binary value.
        """
        return self._hivalue

    @property
    def qualifier(self) -> SearchSearchItemTriggerABusSentFastCounterQualifier:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:QUALifier`` command.

        Description:
            - This command sets or queries the qualifier to be used when searching on SENT fast
              packet bus data for the secure format counter.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:QUALifier?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:QUALifier value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|INrange|OUTrange}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:QUALifier?
            ```

        Info:
            - ``Search<x>`` is the number of the search.
            - ``EQUal`` specifies the qualifier as Equal.
            - ``LESSEQual`` specifies the qualifier as Less Than or Equal to.
            - ``LESSThan`` specifies the qualifier as Less Than.
            - ``MOREEQual`` specifies the qualifier as More Than or Equal to.
            - ``MOREThan`` specifies the qualifier as More Than.
            - ``UNEQual`` specifies the qualifier as Unequal.
            - ``INrange`` sets the qualifier to inside a range.
            - ``OUTrange`` sets the qualifier to outside a range.
        """  # noqa: E501
        return self._qualifier

    @property
    def value(self) -> SearchSearchItemTriggerABusSentFastCounterValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:VALue`` command.

        Description:
            - This command sets or queries the binary fast message counter value to be used when
              searching on a SENT bus signal.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:VALue <Qstring>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:VALue?
            ```

        Info:
            - ``Search<x>`` is the number of the search.
            - ``<Qstring>`` is the Fast Channel 1 counter value.
        """
        return self._value


class SearchSearchItemTriggerABusSentFastChan2bValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:VALue`` command.

    Description:
        - This command sets or queries the binary fast channel 2 value to be used when searching on
          a SENT bus signal.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:VALue <Qstring>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:VALue?
        ```

    Info:
        - ``Search<x>`` is the number of the search.
        - ``<Qstring>`` is the Fast Channel 2 binary value.
    """


class SearchSearchItemTriggerABusSentFastChan2bQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:QUALifier`` command.

    Description:
        - This command sets or queries the qualifier to be used when searching on SENT fast packet
          bus data for device channel 2.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:QUALifier?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:QUALifier value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|INrange|OUTrange}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:QUALifier?
        ```

    Info:
        - ``Search<x>`` is the number of the search.
        - ``EQUal`` specifies the qualifier as Equal.
        - ``LESSEQual`` specifies the qualifier as Less Than or Equal to.
        - ``LESSThan`` specifies the qualifier as Less Than.
        - ``MOREEQual`` specifies the qualifier as More Than or Equal to.
        - ``MOREThan`` specifies the qualifier as More Than.
        - ``UNEQual`` specifies the qualifier as Unequal.
        - ``INrange`` sets the qualifier to inside a range.
        - ``OUTrange`` sets the qualifier to outside a range.
    """  # noqa: E501


class SearchSearchItemTriggerABusSentFastChan2bHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:HIVALue`` command.

    Description:
        - This command sets or queries the high binary fast channel 2 value to use when searching on
          a SENT bus signal.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:HIVALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:HIVALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:HIVALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:HIVALue?
        ```

    Info:
        - ``Search<x>`` is the Search identifier number.
        - ``<Qstring>`` sets the Fast Channel 2 high binary data value.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusSentFastChan2b(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:HIVALue`` command.
        - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:QUALifier`` command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = SearchSearchItemTriggerABusSentFastChan2bHivalue(
            device, f"{self._cmd_syntax}:HIVALue"
        )
        self._qualifier = SearchSearchItemTriggerABusSentFastChan2bQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._value = SearchSearchItemTriggerABusSentFastChan2bValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def hivalue(self) -> SearchSearchItemTriggerABusSentFastChan2bHivalue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:HIVALue`` command.

        Description:
            - This command sets or queries the high binary fast channel 2 value to use when
              searching on a SENT bus signal.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:HIVALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:HIVALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:HIVALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:HIVALue?
            ```

        Info:
            - ``Search<x>`` is the Search identifier number.
            - ``<Qstring>`` sets the Fast Channel 2 high binary data value.
        """
        return self._hivalue

    @property
    def qualifier(self) -> SearchSearchItemTriggerABusSentFastChan2bQualifier:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:QUALifier`` command.

        Description:
            - This command sets or queries the qualifier to be used when searching on SENT fast
              packet bus data for device channel 2.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:QUALifier?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:QUALifier value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|INrange|OUTrange}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:QUALifier?
            ```

        Info:
            - ``Search<x>`` is the number of the search.
            - ``EQUal`` specifies the qualifier as Equal.
            - ``LESSEQual`` specifies the qualifier as Less Than or Equal to.
            - ``LESSThan`` specifies the qualifier as Less Than.
            - ``MOREEQual`` specifies the qualifier as More Than or Equal to.
            - ``MOREThan`` specifies the qualifier as More Than.
            - ``UNEQual`` specifies the qualifier as Unequal.
            - ``INrange`` sets the qualifier to inside a range.
            - ``OUTrange`` sets the qualifier to outside a range.
        """  # noqa: E501
        return self._qualifier

    @property
    def value(self) -> SearchSearchItemTriggerABusSentFastChan2bValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:VALue`` command.

        Description:
            - This command sets or queries the binary fast channel 2 value to be used when searching
              on a SENT bus signal.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:VALue <Qstring>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:VALue?
            ```

        Info:
            - ``Search<x>`` is the number of the search.
            - ``<Qstring>`` is the Fast Channel 2 binary value.
        """
        return self._value


class SearchSearchItemTriggerABusSentFastChan1aValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:VALue`` command.

    Description:
        - This command sets or queries the binary fast channel 1 value to be used when searching on
          a SENT bus signal.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:VALue <Qstring>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:VALue?
        ```

    Info:
        - ``Search<x>`` is the number of the search.
        - ``<Qstring>`` is the Fast Channel 1 binary value.
    """


class SearchSearchItemTriggerABusSentFastChan1aQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:QUALifier`` command.

    Description:
        - This command sets or queries the qualifier to be used when searching on SENT fast packet
          bus data for device channel 1.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:QUALifier?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:QUALifier value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|INrange|OUTrange}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:QUALifier?
        ```

    Info:
        - ``Search<x>`` is the number of the search.
        - ``EQUal`` specifies the qualifier as Equal.
        - ``LESSEQual`` specifies the qualifier as Less Than or Equal to.
        - ``LESSThan`` specifies the qualifier as Less Than.
        - ``MOREEQual`` specifies the qualifier as More Than or Equal to.
        - ``MOREThan`` specifies the qualifier as More Than.
        - ``UNEQual`` specifies the qualifier as Unequal.
        - ``INrange`` sets the qualifier to inside a range.
        - ``OUTrange`` sets the qualifier to outside a range.
    """  # noqa: E501


class SearchSearchItemTriggerABusSentFastChan1aHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:HIVALue`` command.

    Description:
        - This command sets or queries the high binary fast channel 1 value to use when searching on
          a SENT bus signal.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:HIVALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:HIVALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:HIVALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:HIVALue?
        ```

    Info:
        - ``Search<x>`` is the Search identifier number.
        - ``<Qstring>`` sets the Fast Channel 1 binary data high value.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusSentFastChan1a(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:HIVALue`` command.
        - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:QUALifier`` command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = SearchSearchItemTriggerABusSentFastChan1aHivalue(
            device, f"{self._cmd_syntax}:HIVALue"
        )
        self._qualifier = SearchSearchItemTriggerABusSentFastChan1aQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._value = SearchSearchItemTriggerABusSentFastChan1aValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def hivalue(self) -> SearchSearchItemTriggerABusSentFastChan1aHivalue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:HIVALue`` command.

        Description:
            - This command sets or queries the high binary fast channel 1 value to use when
              searching on a SENT bus signal.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:HIVALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:HIVALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:HIVALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:HIVALue?
            ```

        Info:
            - ``Search<x>`` is the Search identifier number.
            - ``<Qstring>`` sets the Fast Channel 1 binary data high value.
        """
        return self._hivalue

    @property
    def qualifier(self) -> SearchSearchItemTriggerABusSentFastChan1aQualifier:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:QUALifier`` command.

        Description:
            - This command sets or queries the qualifier to be used when searching on SENT fast
              packet bus data for device channel 1.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:QUALifier?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:QUALifier value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|INrange|OUTrange}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:QUALifier?
            ```

        Info:
            - ``Search<x>`` is the number of the search.
            - ``EQUal`` specifies the qualifier as Equal.
            - ``LESSEQual`` specifies the qualifier as Less Than or Equal to.
            - ``LESSThan`` specifies the qualifier as Less Than.
            - ``MOREEQual`` specifies the qualifier as More Than or Equal to.
            - ``MOREThan`` specifies the qualifier as More Than.
            - ``UNEQual`` specifies the qualifier as Unequal.
            - ``INrange`` sets the qualifier to inside a range.
            - ``OUTrange`` sets the qualifier to outside a range.
        """  # noqa: E501
        return self._qualifier

    @property
    def value(self) -> SearchSearchItemTriggerABusSentFastChan1aValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:VALue`` command.

        Description:
            - This command sets or queries the binary fast channel 1 value to be used when searching
              on a SENT bus signal.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:VALue <Qstring>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:VALue?
            ```

        Info:
            - ``Search<x>`` is the number of the search.
            - ``<Qstring>`` is the Fast Channel 1 binary value.
        """
        return self._value


class SearchSearchItemTriggerABusSentFast(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.chan1a``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A`` command tree.
        - ``.chan2b``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B`` command tree.
        - ``.counter``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer`` command tree.
        - ``.invertnibble``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:INVERTNIBble`` command
          tree.
        - ``.status``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:STATus`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._chan1a = SearchSearchItemTriggerABusSentFastChan1a(
            device, f"{self._cmd_syntax}:CHAN1A"
        )
        self._chan2b = SearchSearchItemTriggerABusSentFastChan2b(
            device, f"{self._cmd_syntax}:CHAN2B"
        )
        self._counter = SearchSearchItemTriggerABusSentFastCounter(
            device, f"{self._cmd_syntax}:COUNTer"
        )
        self._invertnibble = SearchSearchItemTriggerABusSentFastInvertnibble(
            device, f"{self._cmd_syntax}:INVERTNIBble"
        )
        self._status = SearchSearchItemTriggerABusSentFastStatus(
            device, f"{self._cmd_syntax}:STATus"
        )

    @property
    def chan1a(self) -> SearchSearchItemTriggerABusSentFastChan1a:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:HIVALue`` command.
            - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:QUALifier``
              command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A:VALue`` command.
        """
        return self._chan1a

    @property
    def chan2b(self) -> SearchSearchItemTriggerABusSentFastChan2b:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:HIVALue`` command.
            - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:QUALifier``
              command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B:VALue`` command.
        """
        return self._chan2b

    @property
    def counter(self) -> SearchSearchItemTriggerABusSentFastCounter:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:HIVALue``
              command.
            - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:QUALifier``
              command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer:VALue`` command.
        """
        return self._counter

    @property
    def invertnibble(self) -> SearchSearchItemTriggerABusSentFastInvertnibble:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:INVERTNIBble`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:INVERTNIBble?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:INVERTNIBble?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:INVERTNIBble:VALue``
              command.
        """
        return self._invertnibble

    @property
    def status(self) -> SearchSearchItemTriggerABusSentFastStatus:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:STATus`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:STATus?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:STATus?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:STATus:VALue`` command.
        """
        return self._status


class SearchSearchItemTriggerABusSentErrtypeCrc(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType:CRC`` command.

    Description:
        - This command sets or queries the CRC error type to be used when searching on SENT data.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType:CRC?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType:CRC?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType:CRC value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType:CRC {FAST|SLOW}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType:CRC?
        ```

    Info:
        - ``Search<x>`` is the number of the search.
        - ``FAST`` specifies searching for CRC errors only in the fast channel.
        - ``SLOW`` specifies searching for CRC errors only in the slow channel.
    """


class SearchSearchItemTriggerABusSentErrtype(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType`` command.

    Description:
        - This command sets or queries the error type to be used when searching on SENT data.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType {FRAMELENgth|CRC}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType?
        ```

    Info:
        - ``Search<x>`` is the number of the search.
        - ``FRAMELENgth`` specifies searching for SENT frame length errors.
        - ``CRC`` specifies searching for CRC errors.

    Properties:
        - ``.crc``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType:CRC`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._crc = SearchSearchItemTriggerABusSentErrtypeCrc(device, f"{self._cmd_syntax}:CRC")

    @property
    def crc(self) -> SearchSearchItemTriggerABusSentErrtypeCrc:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType:CRC`` command.

        Description:
            - This command sets or queries the CRC error type to be used when searching on SENT
              data.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType:CRC?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType:CRC?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType:CRC value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType:CRC {FAST|SLOW}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType:CRC?
            ```

        Info:
            - ``Search<x>`` is the number of the search.
            - ``FAST`` specifies searching for CRC errors only in the fast channel.
            - ``SLOW`` specifies searching for CRC errors only in the slow channel.
        """
        return self._crc


class SearchSearchItemTriggerABusSentCondition(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:CONDition`` command.

    Description:
        - This command sets or queries the search condition for a SENT bus.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:CONDition?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:CONDition value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:CONDition {START|FAST|SLOW|PAUSE|ERRor}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:CONDition?
        ```

    Info:
        - ``Search<x>`` is the number of the search.
        - ``START`` specifies searching for start of packet.
        - ``FAST`` specifies searching for fast channel data.
        - ``SLOW`` specifies searching for slow channel data.
        - ``PAUSE`` specifies searching for pause pulses.
        - ``ERRor`` specifies searching on errors.
    """


class SearchSearchItemTriggerABusSent(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT?``
          query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:CONDition`` command.
        - ``.errtype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType`` command.
        - ``.fast``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST`` command tree.
        - ``.pause``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE`` command tree.
        - ``.slow``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = SearchSearchItemTriggerABusSentCondition(
            device, f"{self._cmd_syntax}:CONDition"
        )
        self._errtype = SearchSearchItemTriggerABusSentErrtype(
            device, f"{self._cmd_syntax}:ERRType"
        )
        self._fast = SearchSearchItemTriggerABusSentFast(device, f"{self._cmd_syntax}:FAST")
        self._pause = SearchSearchItemTriggerABusSentPause(device, f"{self._cmd_syntax}:PAUSE")
        self._slow = SearchSearchItemTriggerABusSentSlow(device, f"{self._cmd_syntax}:SLOW")

    @property
    def condition(self) -> SearchSearchItemTriggerABusSentCondition:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:CONDition`` command.

        Description:
            - This command sets or queries the search condition for a SENT bus.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:CONDition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:CONDition?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:CONDition value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:CONDition {START|FAST|SLOW|PAUSE|ERRor}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:CONDition?
            ```

        Info:
            - ``Search<x>`` is the number of the search.
            - ``START`` specifies searching for start of packet.
            - ``FAST`` specifies searching for fast channel data.
            - ``SLOW`` specifies searching for slow channel data.
            - ``PAUSE`` specifies searching for pause pulses.
            - ``ERRor`` specifies searching on errors.
        """
        return self._condition

    @property
    def errtype(self) -> SearchSearchItemTriggerABusSentErrtype:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType`` command.

        Description:
            - This command sets or queries the error type to be used when searching on SENT data.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType {FRAMELENgth|CRC}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType?
            ```

        Info:
            - ``Search<x>`` is the number of the search.
            - ``FRAMELENgth`` specifies searching for SENT frame length errors.
            - ``CRC`` specifies searching for CRC errors.

        Sub-properties:
            - ``.crc``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType:CRC`` command.
        """
        return self._errtype

    @property
    def fast(self) -> SearchSearchItemTriggerABusSentFast:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.chan1a``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN1A`` command tree.
            - ``.chan2b``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:CHAN2B`` command tree.
            - ``.counter``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:COUNTer`` command tree.
            - ``.invertnibble``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:INVERTNIBble``
              command tree.
            - ``.status``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST:STATus`` command tree.
        """
        return self._fast

    @property
    def pause(self) -> SearchSearchItemTriggerABusSentPause:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:QUALifier`` command.
            - ``.ticks``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE:TICKs`` command tree.
        """
        return self._pause

    @property
    def slow(self) -> SearchSearchItemTriggerABusSentSlow:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:DATA`` command tree.
            - ``.identifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW:IDentifier`` command
              tree.
        """
        return self._slow


class SearchSearchItemTriggerABusRs232cDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:VALue`` command.

    Description:
        - This command sets or queries the data string used for the specified RS232C bus trigger
          search to determine where to place a mark. The search condition must be Data. The search
          number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:VALue?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:VALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:VALue?
        ```

    Info:
        - ``<QString>`` specifies the value of the data string. The valid characters are 0, 1, and X
          for values in binary format; and A-F, 0-9, and X for values in hexadecimal format.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusRs232cDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:SIZe`` command.

    Description:
        - This command sets or queries the length of the data string in bytes to be used for an
          RS232 bus search to determine where to place a mark when the search condition is Data. The
          search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:SIZe?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:SIZe <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:SIZe?
        ```

    Info:
        - ``<NR3>`` is the number of bits per word in the data string, from 1 to 8.
    """


class SearchSearchItemTriggerABusRs232cData(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:SIZe`` command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._size = SearchSearchItemTriggerABusRs232cDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._value = SearchSearchItemTriggerABusRs232cDataValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def size(self) -> SearchSearchItemTriggerABusRs232cDataSize:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:SIZe`` command.

        Description:
            - This command sets or queries the length of the data string in bytes to be used for an
              RS232 bus search to determine where to place a mark when the search condition is Data.
              The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:SIZe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:SIZe?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:SIZe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:SIZe <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:SIZe?
            ```

        Info:
            - ``<NR3>`` is the number of bits per word in the data string, from 1 to 8.
        """
        return self._size

    @property
    def value(self) -> SearchSearchItemTriggerABusRs232cDataValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:VALue`` command.

        Description:
            - This command sets or queries the data string used for the specified RS232C bus trigger
              search to determine where to place a mark. The search condition must be Data. The
              search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:VALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:VALue?
            ```

        Info:
            - ``<QString>`` specifies the value of the data string. The valid characters are 0, 1,
              and X for values in binary format; and A-F, 0-9, and X for values in hexadecimal
              format.
        """
        return self._value


class SearchSearchItemTriggerABusRs232cCondition(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:CONDition`` command.

    Description:
        - This command sets or queries the condition for an RS232C bus search to determine where to
          place a mark. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:CONDition?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:CONDition value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:CONDition {DATa|EOp|PARItyerror|STARt}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:CONDition?
        ```

    Info:
        - ``DATa`` specifies the search condition as Data.
        - ``EOp`` specifies the search condition as End of Packet.
        - ``PARItyerror`` specifies the search condition as Parity Error.
        - ``STARt`` specifies the search condition as Start.
    """


class SearchSearchItemTriggerABusRs232c(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:CONDition`` command.
        - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = SearchSearchItemTriggerABusRs232cCondition(
            device, f"{self._cmd_syntax}:CONDition"
        )
        self._data = SearchSearchItemTriggerABusRs232cData(device, f"{self._cmd_syntax}:DATa")

    @property
    def condition(self) -> SearchSearchItemTriggerABusRs232cCondition:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:CONDition`` command.

        Description:
            - This command sets or queries the condition for an RS232C bus search to determine where
              to place a mark. The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:CONDition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:CONDition?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:CONDition value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:CONDition {DATa|EOp|PARItyerror|STARt}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:CONDition?
            ```

        Info:
            - ``DATa`` specifies the search condition as Data.
            - ``EOp`` specifies the search condition as End of Packet.
            - ``PARItyerror`` specifies the search condition as Parity Error.
            - ``STARt`` specifies the search condition as Start.
        """
        return self._condition

    @property
    def data(self) -> SearchSearchItemTriggerABusRs232cData:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:SIZe`` command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa:VALue`` command.
        """
        return self._data


class SearchSearchItemTriggerABusParallelDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel:DATa:VALue`` command.

    Description:
        - This command sets or queries the binary data string used for a parallel bus search to
          determine where to place a mark. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel:DATa:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel:DATa:VALue?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel:DATa:VALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel:DATa:VALue?
        ```

    Info:
        - ``<QString>`` specifies the data value in a valid format. Valid characters are 0-9.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusParallelData(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel:DATa?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel:DATa?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = SearchSearchItemTriggerABusParallelDataValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> SearchSearchItemTriggerABusParallelDataValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel:DATa:VALue`` command.

        Description:
            - This command sets or queries the binary data string used for a parallel bus search to
              determine where to place a mark. The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel:DATa:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel:DATa:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel:DATa:VALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel:DATa:VALue?
            ```

        Info:
            - ``<QString>`` specifies the data value in a valid format. Valid characters are 0-9.
        """
        return self._value


class SearchSearchItemTriggerABusParallel(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel:DATa`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._data = SearchSearchItemTriggerABusParallelData(device, f"{self._cmd_syntax}:DATa")

    @property
    def data(self) -> SearchSearchItemTriggerABusParallelData:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel:DATa?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel:DATa?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel:DATa:VALue`` command.
        """
        return self._data


class SearchSearchItemTriggerABusLinIdentifierValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:IDentifier:VALue`` command.

    Description:
        - This command sets or queries the string used for a LIN bus identifier value. The search
          number is specified by x. The search condition must be IDENTIFIER or IDANDDATA.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:IDentifier:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:IDentifier:VALue?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:IDentifier:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:IDentifier:VALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:IDentifier:VALue?
        ```

    Info:
        - ``<QString>`` specifies the identifier value.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusLinIdentifier(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:IDentifier`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:IDentifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:IDentifier?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:IDentifier:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = SearchSearchItemTriggerABusLinIdentifierValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> SearchSearchItemTriggerABusLinIdentifierValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:IDentifier:VALue`` command.

        Description:
            - This command sets or queries the string used for a LIN bus identifier value. The
              search number is specified by x. The search condition must be IDENTIFIER or IDANDDATA.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:IDentifier:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:IDentifier:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:IDentifier:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:IDentifier:VALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:IDentifier:VALue?
            ```

        Info:
            - ``<QString>`` specifies the identifier value.
        """
        return self._value


class SearchSearchItemTriggerABusLinErrtype(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:ERRTYPE`` command.

    Description:
        - This command sets or queries the error type for a LIN bus search. The search number is
          specified by x. The search condition must be set to ERROR.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:ERRTYPE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:ERRTYPE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:ERRTYPE value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:ERRTYPE {CHecksum|PARity|SYNC}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:ERRTYPE?
        ```

    Info:
        - ``CHecksum`` specifies the error type is checksum.
        - ``PARity`` specifies the error type is parity.
        - ``SYNC`` specifies the error type is sync.
    """


class SearchSearchItemTriggerABusLinDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:VALue`` command.

    Description:
        - This command sets or queries the data string used for a LIN bus search. The search number
          is specified by x. The search condition must be DATA or IDANDDATA.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:VALue?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:VALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:VALue?
        ```

    Info:
        - ``<QString>`` specifies the data value.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusLinDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:SIZe`` command.

    Description:
        - This command sets or queries the length of the stat string in bytes used for a LIN bus
          search. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:SIZe?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:SIZe <NR1>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:SIZe?
        ```

    Info:
        - ``<NR1>`` specifies the data size.
    """


class SearchSearchItemTriggerABusLinDataQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:QUALifier`` command.

    Description:
        - This command sets or queries the data qualifier used in a LIN bus search. The search
          number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:QUALifier?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:QUALifier value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:QUALifier {EQual|LESSEQual|MOREEQual|UNEQual|LESSthan|MOREthan|INrange|OUTrange}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:QUALifier?
        ```

    Info:
        - ``EQual`` sets the data qualifier to equal.
        - ``LESSEQual`` sets the data qualifier to less equal.
        - ``MOREEQual`` sets the data qualifier to more equal.
        - ``UNEQual`` sets the data qualifier to unequal.
        - ``LESSthan`` sets the data qualifier to less than.
        - ``MOREthan`` sets the data qualifier to more than.
        - ``INrange`` sets the data qualifier to in range.
        - ``OUTrange`` sets the data qualifier out of range.
    """  # noqa: E501


class SearchSearchItemTriggerABusLinDataHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:HIVALue`` command.

    Description:
        - This command sets or queries the high data value string used in a LIN bus search. The
          search number is specified by x. The search condition must be DATA or IDANDDATA and the
          data qualifier must be INRANGE or OUTRANGE.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:HIVALue?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:HIVALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:HIVALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:HIVALue?
        ```

    Info:
        - ``<QString>`` is a quoted string of 1s, 0s, or Xs representing the binary data string to
          be used in a LIN search if the search condition is IDentifier or IDANDDATA (identifier and
          data).
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusLinData(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:HIVALue`` command.
        - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:QUALifier`` command.
        - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:SIZe`` command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = SearchSearchItemTriggerABusLinDataHivalue(
            device, f"{self._cmd_syntax}:HIVALue"
        )
        self._qualifier = SearchSearchItemTriggerABusLinDataQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._size = SearchSearchItemTriggerABusLinDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._value = SearchSearchItemTriggerABusLinDataValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def hivalue(self) -> SearchSearchItemTriggerABusLinDataHivalue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:HIVALue`` command.

        Description:
            - This command sets or queries the high data value string used in a LIN bus search. The
              search number is specified by x. The search condition must be DATA or IDANDDATA and
              the data qualifier must be INRANGE or OUTRANGE.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:HIVALue?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:HIVALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:HIVALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:HIVALue?
            ```

        Info:
            - ``<QString>`` is a quoted string of 1s, 0s, or Xs representing the binary data string
              to be used in a LIN search if the search condition is IDentifier or IDANDDATA
              (identifier and data).
        """
        return self._hivalue

    @property
    def qualifier(self) -> SearchSearchItemTriggerABusLinDataQualifier:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:QUALifier`` command.

        Description:
            - This command sets or queries the data qualifier used in a LIN bus search. The search
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:QUALifier?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:QUALifier value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:QUALifier {EQual|LESSEQual|MOREEQual|UNEQual|LESSthan|MOREthan|INrange|OUTrange}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:QUALifier?
            ```

        Info:
            - ``EQual`` sets the data qualifier to equal.
            - ``LESSEQual`` sets the data qualifier to less equal.
            - ``MOREEQual`` sets the data qualifier to more equal.
            - ``UNEQual`` sets the data qualifier to unequal.
            - ``LESSthan`` sets the data qualifier to less than.
            - ``MOREthan`` sets the data qualifier to more than.
            - ``INrange`` sets the data qualifier to in range.
            - ``OUTrange`` sets the data qualifier out of range.
        """  # noqa: E501
        return self._qualifier

    @property
    def size(self) -> SearchSearchItemTriggerABusLinDataSize:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:SIZe`` command.

        Description:
            - This command sets or queries the length of the stat string in bytes used for a LIN bus
              search. The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:SIZe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:SIZe?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:SIZe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:SIZe <NR1>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:SIZe?
            ```

        Info:
            - ``<NR1>`` specifies the data size.
        """
        return self._size

    @property
    def value(self) -> SearchSearchItemTriggerABusLinDataValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:VALue`` command.

        Description:
            - This command sets or queries the data string used for a LIN bus search. The search
              number is specified by x. The search condition must be DATA or IDANDDATA.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:VALue?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:VALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:VALue?
            ```

        Info:
            - ``<QString>`` specifies the data value.
        """
        return self._value


class SearchSearchItemTriggerABusLinCondition(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:CONDition`` command.

    Description:
        - This command sets or queries the condition for a LIN bus search. The search number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:CONDition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:CONDition value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:CONDition {DATA|IDANDDATA|ERRor|IDentifier|SLEEP|SYNCfield|WAKEup}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:CONDition?
        ```

    Info:
        - ``DATA`` sets the trigger condition to data.
        - ``IDANDDATA`` sets the trigger condition to ID and data.
        - ``ERRor`` sets the trigger condition to error.
        - ``IDentifier`` sets the trigger condition to identifier.
        - ``SLEEP`` sets the trigger condition to sleep.
        - ``SYNCfield`` sets the trigger condition to sync field.
        - ``WAKEup`` sets the trigger condition to wakeup.
    """  # noqa: E501


class SearchSearchItemTriggerABusLin(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:CONDition`` command.
        - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa`` command tree.
        - ``.errtype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:ERRTYPE`` command.
        - ``.identifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:IDentifier`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = SearchSearchItemTriggerABusLinCondition(
            device, f"{self._cmd_syntax}:CONDition"
        )
        self._data = SearchSearchItemTriggerABusLinData(device, f"{self._cmd_syntax}:DATa")
        self._errtype = SearchSearchItemTriggerABusLinErrtype(device, f"{self._cmd_syntax}:ERRTYPE")
        self._identifier = SearchSearchItemTriggerABusLinIdentifier(
            device, f"{self._cmd_syntax}:IDentifier"
        )

    @property
    def condition(self) -> SearchSearchItemTriggerABusLinCondition:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:CONDition`` command.

        Description:
            - This command sets or queries the condition for a LIN bus search. The search number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:CONDition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:CONDition?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:CONDition value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:CONDition {DATA|IDANDDATA|ERRor|IDentifier|SLEEP|SYNCfield|WAKEup}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:CONDition?
            ```

        Info:
            - ``DATA`` sets the trigger condition to data.
            - ``IDANDDATA`` sets the trigger condition to ID and data.
            - ``ERRor`` sets the trigger condition to error.
            - ``IDentifier`` sets the trigger condition to identifier.
            - ``SLEEP`` sets the trigger condition to sleep.
            - ``SYNCfield`` sets the trigger condition to sync field.
            - ``WAKEup`` sets the trigger condition to wakeup.
        """  # noqa: E501
        return self._condition

    @property
    def data(self) -> SearchSearchItemTriggerABusLinData:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:HIVALue`` command.
            - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:QUALifier`` command.
            - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:SIZe`` command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa:VALue`` command.
        """
        return self._data

    @property
    def errtype(self) -> SearchSearchItemTriggerABusLinErrtype:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:ERRTYPE`` command.

        Description:
            - This command sets or queries the error type for a LIN bus search. The search number is
              specified by x. The search condition must be set to ERROR.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:ERRTYPE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:ERRTYPE?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:ERRTYPE value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:ERRTYPE {CHecksum|PARity|SYNC}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:ERRTYPE?
            ```

        Info:
            - ``CHecksum`` specifies the error type is checksum.
            - ``PARity`` specifies the error type is parity.
            - ``SYNC`` specifies the error type is sync.
        """
        return self._errtype

    @property
    def identifier(self) -> SearchSearchItemTriggerABusLinIdentifier:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:IDentifier`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:IDentifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:IDentifier?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:IDentifier:VALue`` command.
        """
        return self._identifier


class SearchSearchItemTriggerABusI2cDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:VALue`` command.

    Description:
        - This command sets or queries the binary data string used for I2C bus search to determine
          where to place a mark. The search number is specified by x. The search condition must be
          DATA or ADDRANDDATA.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:VALue?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:VALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:VALue?
        ```

    Info:
        - ``<QString>`` specifies the data value. The valid characters are 0, 1, or X for binary
          format; and A-F, 0-9, and X for hexadecimal format.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusI2cDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:SIZe`` command.

    Description:
        - This command sets or queries the length of the data string in bytes used for an I2C bus
          search to determine where to place a mark. The search number is specified by x. The search
          condition must be DATA or ADDRANDDATA.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:SIZe?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:SIZe <NR1>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:SIZe?
        ```

    Info:
        - ``<NR1>`` specifies the data size in bytes.
    """


class SearchSearchItemTriggerABusI2cDataDirection(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:DIRection`` command.

    Description:
        - This command sets or queries the direction of the data for the I2C bus search to determine
          where to place a mark. The search number is specified by x. Read or write is indicated by
          the R/W bit in the I2C protocol.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:DIRection?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:DIRection?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:DIRection value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:DIRection {NOCARE|READ|WRITE}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:DIRection?
        ```

    Info:
        - ``NOCARE`` specifies the direction of data as Don't Care.
        - ``READ`` specifies the direction of data as Read.
        - ``WRITE`` specifies the direction of data as Write.
    """


class SearchSearchItemTriggerABusI2cData(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.direction``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:DIRection`` command.
        - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:SIZe`` command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._direction = SearchSearchItemTriggerABusI2cDataDirection(
            device, f"{self._cmd_syntax}:DIRection"
        )
        self._size = SearchSearchItemTriggerABusI2cDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._value = SearchSearchItemTriggerABusI2cDataValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def direction(self) -> SearchSearchItemTriggerABusI2cDataDirection:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:DIRection`` command.

        Description:
            - This command sets or queries the direction of the data for the I2C bus search to
              determine where to place a mark. The search number is specified by x. Read or write is
              indicated by the R/W bit in the I2C protocol.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:DIRection?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:DIRection?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:DIRection value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:DIRection {NOCARE|READ|WRITE}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:DIRection?
            ```

        Info:
            - ``NOCARE`` specifies the direction of data as Don't Care.
            - ``READ`` specifies the direction of data as Read.
            - ``WRITE`` specifies the direction of data as Write.
        """
        return self._direction

    @property
    def size(self) -> SearchSearchItemTriggerABusI2cDataSize:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:SIZe`` command.

        Description:
            - This command sets or queries the length of the data string in bytes used for an I2C
              bus search to determine where to place a mark. The search number is specified by x.
              The search condition must be DATA or ADDRANDDATA.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:SIZe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:SIZe?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:SIZe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:SIZe <NR1>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:SIZe?
            ```

        Info:
            - ``<NR1>`` specifies the data size in bytes.
        """
        return self._size

    @property
    def value(self) -> SearchSearchItemTriggerABusI2cDataValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:VALue`` command.

        Description:
            - This command sets or queries the binary data string used for I2C bus search to
              determine where to place a mark. The search number is specified by x. The search
              condition must be DATA or ADDRANDDATA.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:VALue?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:VALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:VALue?
            ```

        Info:
            - ``<QString>`` specifies the data value. The valid characters are 0, 1, or X for binary
              format; and A-F, 0-9, and X for hexadecimal format.
        """
        return self._value


class SearchSearchItemTriggerABusI2cCondition(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:CONDition`` command.

    Description:
        - This command sets or queries the search condition for an I2C bus. The search number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:CONDition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:CONDition value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:CONDition {ADDRess|ADDRANDDATA|DATa|ACKMISS|REPEATstart|STARt|STOP}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:CONDition?
        ```

    Info:
        - ``ADDress`` specifies the trigger condition as Address.
        - ``ADDRANDDATA`` specifies the trigger condition as Address and Data.
        - ``DATa`` specifies the trigger condition as Data.
        - ``ACKMISS`` specifies the trigger condition as Missing of Acknowledgement.
        - ``REPEATstart`` specifies the trigger condition as Repeat of Start.
        - ``STARt`` specifies the trigger condition as Start.
        - ``STOP`` specifies the trigger condition as Stop.
    """  # noqa: E501


class SearchSearchItemTriggerABusI2cAddressValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:VALue`` command.

    Description:
        - This command sets or queries the binary address string used for the I2C search the
          specified search condition is Address or AddressData. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:VALue?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:VALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:VALue?
        ```

    Info:
        - ``<QString>`` specifies the address value. This is either a 7-bit or 10-bit value
          depending on the address mode. The valid characters are 0-9, A-F, and X for addresses in
          hexadecimal format; and 0, 1, and X otherwise.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusI2cAddressMode(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:MODe`` command.

    Description:
        - This command sets or queries the I2C address mode for the specified bus search to
          determine where to place a mark. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:MODe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:MODe?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:MODe value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:MODe {ADDR10|ADDR7}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:MODe?
        ```

    Info:
        - ``ADDR10`` specifies the address mode as ADDR10.
        - ``ADDR7`` specifies the address mode as ADDR7.
    """


class SearchSearchItemTriggerABusI2cAddress(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.mode``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:MODe`` command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = SearchSearchItemTriggerABusI2cAddressMode(device, f"{self._cmd_syntax}:MODe")
        self._value = SearchSearchItemTriggerABusI2cAddressValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def mode(self) -> SearchSearchItemTriggerABusI2cAddressMode:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:MODe`` command.

        Description:
            - This command sets or queries the I2C address mode for the specified bus search to
              determine where to place a mark. The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:MODe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:MODe?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:MODe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:MODe {ADDR10|ADDR7}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:MODe?
            ```

        Info:
            - ``ADDR10`` specifies the address mode as ADDR10.
            - ``ADDR7`` specifies the address mode as ADDR7.
        """
        return self._mode

    @property
    def value(self) -> SearchSearchItemTriggerABusI2cAddressValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:VALue`` command.

        Description:
            - This command sets or queries the binary address string used for the I2C search the
              specified search condition is Address or AddressData. The search number is specified
              by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:VALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:VALue?
            ```

        Info:
            - ``<QString>`` specifies the address value. This is either a 7-bit or 10-bit value
              depending on the address mode. The valid characters are 0-9, A-F, and X for addresses
              in hexadecimal format; and 0, 1, and X otherwise.
        """
        return self._value


class SearchSearchItemTriggerABusI2c(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.address``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess`` command tree.
        - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:CONDition`` command.
        - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._address = SearchSearchItemTriggerABusI2cAddress(device, f"{self._cmd_syntax}:ADDRess")
        self._condition = SearchSearchItemTriggerABusI2cCondition(
            device, f"{self._cmd_syntax}:CONDition"
        )
        self._data = SearchSearchItemTriggerABusI2cData(device, f"{self._cmd_syntax}:DATa")

    @property
    def address(self) -> SearchSearchItemTriggerABusI2cAddress:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.mode``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:MODe`` command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess:VALue`` command.
        """
        return self._address

    @property
    def condition(self) -> SearchSearchItemTriggerABusI2cCondition:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:CONDition`` command.

        Description:
            - This command sets or queries the search condition for an I2C bus. The search number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:CONDition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:CONDition?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:CONDition value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:CONDition {ADDRess|ADDRANDDATA|DATa|ACKMISS|REPEATstart|STARt|STOP}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:CONDition?
            ```

        Info:
            - ``ADDress`` specifies the trigger condition as Address.
            - ``ADDRANDDATA`` specifies the trigger condition as Address and Data.
            - ``DATa`` specifies the trigger condition as Data.
            - ``ACKMISS`` specifies the trigger condition as Missing of Acknowledgement.
            - ``REPEATstart`` specifies the trigger condition as Repeat of Start.
            - ``STARt`` specifies the trigger condition as Start.
            - ``STOP`` specifies the trigger condition as Stop.
        """  # noqa: E501
        return self._condition

    @property
    def data(self) -> SearchSearchItemTriggerABusI2cData:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.direction``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:DIRection`` command.
            - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:SIZe`` command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa:VALue`` command.
        """
        return self._data


class SearchSearchItemTriggerABusCanIdentifierValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:VALue`` command.

    Description:
        - This command sets or queries CAN bus trigger identifier (address) value to be used when
          searching on a CAN bus signal. The search number is specified by x. The search condition
          must be set to IDANDDATA or DATA.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:VALue?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:VALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:VALue?
        ```

    Info:
        - ``<QString>`` is the identifier value.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusCanIdentifierMode(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:MODe`` command.

    Description:
        - This command sets or queries the CAN bus trigger identifier (address) mode to be used when
          searching on a CAN bus signal. The search number is specified by x. The search condition
          must be set to IDANDDATA or DATA.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:MODe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:MODe?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:MODe value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:MODe {EXTENDed|STandard}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:MODe?
        ```

    Info:
        - ``EXTENDed`` specifies the extended identifier mode.
        - ``STandard`` specifies the standard identifier mode.
    """


class SearchSearchItemTriggerABusCanIdentifier(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.mode``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:MODe`` command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = SearchSearchItemTriggerABusCanIdentifierMode(
            device, f"{self._cmd_syntax}:MODe"
        )
        self._value = SearchSearchItemTriggerABusCanIdentifierValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def mode(self) -> SearchSearchItemTriggerABusCanIdentifierMode:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:MODe`` command.

        Description:
            - This command sets or queries the CAN bus trigger identifier (address) mode to be used
              when searching on a CAN bus signal. The search number is specified by x. The search
              condition must be set to IDANDDATA or DATA.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:MODe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:MODe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:MODe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:MODe {EXTENDed|STandard}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:MODe?
            ```

        Info:
            - ``EXTENDed`` specifies the extended identifier mode.
            - ``STandard`` specifies the standard identifier mode.
        """
        return self._mode

    @property
    def value(self) -> SearchSearchItemTriggerABusCanIdentifierValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:VALue`` command.

        Description:
            - This command sets or queries CAN bus trigger identifier (address) value to be used
              when searching on a CAN bus signal. The search number is specified by x. The search
              condition must be set to IDANDDATA or DATA.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:VALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:VALue?
            ```

        Info:
            - ``<QString>`` is the identifier value.
        """
        return self._value


class SearchSearchItemTriggerABusCanFrametype(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FRAMEtype`` command.

    Description:
        - This command sets or queries CAN bus trigger frame type to be used when searching on a CAN
          bus signal. The search condition must be set to FRAMEtype. The search number is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FRAMEtype?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FRAMEtype?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FRAMEtype value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FRAMEtype {DATa|ERRor|OVERLoad|REMote}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FRAMEtype?
        ```

    Info:
        - ``DATa`` sets the frame type to data.
        - ``ERRor`` sets the frame type to error.
        - ``OVERLoad`` sets the frame type to overload.
        - ``REMote`` sets the frame type to remote.
    """


class SearchSearchItemTriggerABusCanFdEsibit(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:ESIBit`` command.

    Description:
        - This command sets or queries the value of the error state indicator bit (ESI bit) for a
          CAN bus to search on. The search number is specified by x. The search condition must be
          set to FDBITS, and the CAN standard must be FDISO or FDNONISO.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:ESIBit?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:ESIBit?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:ESIBit value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:ESIBit {ONE|ZERo|NOCARE}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:ESIBit?
        ```

    Info:
        - ``ONE`` filters CAN FD packets to only match those where the ESI bit has a value of 1
          (recessive).
        - ``ZERo`` filters CAN FD packets to only match those where the ESI bit has a value of 0
          (dominant).
        - ``NOCARE`` disables filtering of CAN FD packets on the ESI bit.
    """


class SearchSearchItemTriggerABusCanFdBrsbit(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:BRSBit`` command.

    Description:
        - This command sets or queries the value of the bit rate switch bit (BRS bit) for a CAN bus
          to search on. The search number is specified by x. The search condition must be set to
          FDBITS, and the CAN standard must be FDISO or FDNONISO.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:BRSBit?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:BRSBit?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:BRSBit value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:BRSBit {ONE|ZERo|NOCARE}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:BRSBit?
        ```

    Info:
        - ``ONE`` filters CAN FD packets to only match those where the BRS bit has a value of 1
          (fast data enabled).
        - ``ZERo`` filters CAN FD packets to only match those where the BRS bit has a value of 0
          (fast data disabled).
        - ``NOCARE`` disables filtering of CAN FD packets on the BRS bit.
    """


class SearchSearchItemTriggerABusCanFd(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.brsbit``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:BRSBit`` command.
        - ``.esibit``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:ESIBit`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._brsbit = SearchSearchItemTriggerABusCanFdBrsbit(device, f"{self._cmd_syntax}:BRSBit")
        self._esibit = SearchSearchItemTriggerABusCanFdEsibit(device, f"{self._cmd_syntax}:ESIBit")

    @property
    def brsbit(self) -> SearchSearchItemTriggerABusCanFdBrsbit:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:BRSBit`` command.

        Description:
            - This command sets or queries the value of the bit rate switch bit (BRS bit) for a CAN
              bus to search on. The search number is specified by x. The search condition must be
              set to FDBITS, and the CAN standard must be FDISO or FDNONISO.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:BRSBit?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:BRSBit?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:BRSBit value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:BRSBit {ONE|ZERo|NOCARE}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:BRSBit?
            ```

        Info:
            - ``ONE`` filters CAN FD packets to only match those where the BRS bit has a value of 1
              (fast data enabled).
            - ``ZERo`` filters CAN FD packets to only match those where the BRS bit has a value of 0
              (fast data disabled).
            - ``NOCARE`` disables filtering of CAN FD packets on the BRS bit.
        """
        return self._brsbit

    @property
    def esibit(self) -> SearchSearchItemTriggerABusCanFdEsibit:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:ESIBit`` command.

        Description:
            - This command sets or queries the value of the error state indicator bit (ESI bit) for
              a CAN bus to search on. The search number is specified by x. The search condition must
              be set to FDBITS, and the CAN standard must be FDISO or FDNONISO.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:ESIBit?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:ESIBit?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:ESIBit value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:ESIBit {ONE|ZERo|NOCARE}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:ESIBit?
            ```

        Info:
            - ``ONE`` filters CAN FD packets to only match those where the ESI bit has a value of 1
              (recessive).
            - ``ZERo`` filters CAN FD packets to only match those where the ESI bit has a value of 0
              (dominant).
            - ``NOCARE`` disables filtering of CAN FD packets on the ESI bit.
        """
        return self._esibit


class SearchSearchItemTriggerABusCanErrtype(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:ERRType`` command.

    Description:
        - This command sets or queries the type of error condition for a CAN bus to search on. The
          search number is specified by x. The search condition must be set to ERRor.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:ERRType?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:ERRType?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:ERRType value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:ERRType {ACKMISS|BITSTUFFing|FORMERRor|ANYERRor}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:ERRType?
        ```

    Info:
        - ``ACKMISS`` specifies a search based on a missing ACK field.
        - ``BITSTUFFing`` specifies a search based on a bit stuffing error.
        - ``FORMERRor`` specifies a search based on a CAN FD form error. To use this option, the CAN
          standard must be set to FDISO or FDNONISO.
        - ``ANYERRor`` specifies a search based on any error type.
    """


class SearchSearchItemTriggerABusCanDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:VALue`` command.

    Description:
        - This command sets or queries the binary data value to be used when searching on a CAN bus
          signal. The search condition must be set to IDANDDATA OR DATA.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:VALue?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:VALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:VALue?
        ```

    Info:
        - ``<QString>``
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusCanDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:SIZe`` command.

    Description:
        - This command sets or queries the length of the data string, in bytes, to be used when
          searching on a CAN bus signal. The search condition must be set to IDANDDATA or DATA. The
          search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:SIZe?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:SIZe <NR1>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:SIZe?
        ```

    Info:
        - ``<NR1>`` specifies the data size.
    """


class SearchSearchItemTriggerABusCanDataQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:QUALifier`` command.

    Description:
        - This command sets or queries the CAN bus trigger data qualifier to be used when searching
          on a CAN bus signal. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:QUALifier?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:QUALifier value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:QUALifier {EQUal|LESSEQual|MOREEQua|UNEQual|LESSthan|MOREthan}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:QUALifier?
        ```

    Info:
        - ``EQUal`` sets the data qualifier to equal.
        - ``LESSEQual`` sets the data qualifier to less equal.
        - ``MOREEQua`` sets the data qualifier to more equal.
        - ``UNEQual`` sets the data qualifier to unequal.
        - ``LESSthan`` sets the data qualifier to less than.
        - ``MOREthan`` sets the data qualifier to more than.
    """  # noqa: E501


class SearchSearchItemTriggerABusCanDataOffset(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:OFFSet`` command.

    Description:
        - This command sets or queries the data offset value, in bytes, to use when searching on the
          CAN data field. The search number is specified by x. The search condition must be set to
          DATA or IDANDDATA.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:OFFSet?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:OFFSet?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:OFFSet value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:OFFSet <NR1>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:OFFSet?
        ```

    Info:
        - ``<NR1>`` is an integer whose minimum and default values are -1 (don't care) and maximum
          is up to 7 (for CAN 2.0) or up to 63 (for ISO CAN FD and Non-ISO CAN FD). The maximum is
          dependent on the number of bytes being matched and the CAN standard selected. Its value is
          calculated as [Absolute Maximum] - [Data Match Size]. For CAN 2.0, the absolute maximum is
          8 bytes. For ISO CAN FD and Non-ISO CAN FD, the absolute maximum is 64 bytes. The minimum
          data match size is 1 byte, which produces the ranges listed above. Increasing the data
          match size above 1 byte will adjust the range of valid data offset values accordingly.
    """


class SearchSearchItemTriggerABusCanDataDirection(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:DIRection`` command.

    Description:
        - This command specifies the CAN search type to be valid on a Read, Write, or Either
          condition. The search number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:DIRection?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:DIRection?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:DIRection value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:DIRection {READ|WRITE|NOCARE}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:DIRection?
        ```

    Info:
        - ``READ`` specifies the read direction.
        - ``WRITE`` specifies the write direction.
        - ``NOCARE`` specifies either data direction.
    """


class SearchSearchItemTriggerABusCanData(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.direction``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:DIRection`` command.
        - ``.offset``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:OFFSet`` command.
        - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:QUALifier`` command.
        - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:SIZe`` command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._direction = SearchSearchItemTriggerABusCanDataDirection(
            device, f"{self._cmd_syntax}:DIRection"
        )
        self._offset = SearchSearchItemTriggerABusCanDataOffset(
            device, f"{self._cmd_syntax}:OFFSet"
        )
        self._qualifier = SearchSearchItemTriggerABusCanDataQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._size = SearchSearchItemTriggerABusCanDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._value = SearchSearchItemTriggerABusCanDataValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def direction(self) -> SearchSearchItemTriggerABusCanDataDirection:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:DIRection`` command.

        Description:
            - This command specifies the CAN search type to be valid on a Read, Write, or Either
              condition. The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:DIRection?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:DIRection?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:DIRection value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:DIRection {READ|WRITE|NOCARE}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:DIRection?
            ```

        Info:
            - ``READ`` specifies the read direction.
            - ``WRITE`` specifies the write direction.
            - ``NOCARE`` specifies either data direction.
        """
        return self._direction

    @property
    def offset(self) -> SearchSearchItemTriggerABusCanDataOffset:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:OFFSet`` command.

        Description:
            - This command sets or queries the data offset value, in bytes, to use when searching on
              the CAN data field. The search number is specified by x. The search condition must be
              set to DATA or IDANDDATA.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:OFFSet?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:OFFSet?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:OFFSet value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:OFFSet <NR1>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:OFFSet?
            ```

        Info:
            - ``<NR1>`` is an integer whose minimum and default values are -1 (don't care) and
              maximum is up to 7 (for CAN 2.0) or up to 63 (for ISO CAN FD and Non-ISO CAN FD). The
              maximum is dependent on the number of bytes being matched and the CAN standard
              selected. Its value is calculated as [Absolute Maximum] - [Data Match Size]. For CAN
              2.0, the absolute maximum is 8 bytes. For ISO CAN FD and Non-ISO CAN FD, the absolute
              maximum is 64 bytes. The minimum data match size is 1 byte, which produces the ranges
              listed above. Increasing the data match size above 1 byte will adjust the range of
              valid data offset values accordingly.
        """
        return self._offset

    @property
    def qualifier(self) -> SearchSearchItemTriggerABusCanDataQualifier:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:QUALifier`` command.

        Description:
            - This command sets or queries the CAN bus trigger data qualifier to be used when
              searching on a CAN bus signal. The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:QUALifier?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:QUALifier value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:QUALifier {EQUal|LESSEQual|MOREEQua|UNEQual|LESSthan|MOREthan}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:QUALifier?
            ```

        Info:
            - ``EQUal`` sets the data qualifier to equal.
            - ``LESSEQual`` sets the data qualifier to less equal.
            - ``MOREEQua`` sets the data qualifier to more equal.
            - ``UNEQual`` sets the data qualifier to unequal.
            - ``LESSthan`` sets the data qualifier to less than.
            - ``MOREthan`` sets the data qualifier to more than.
        """  # noqa: E501
        return self._qualifier

    @property
    def size(self) -> SearchSearchItemTriggerABusCanDataSize:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:SIZe`` command.

        Description:
            - This command sets or queries the length of the data string, in bytes, to be used when
              searching on a CAN bus signal. The search condition must be set to IDANDDATA or DATA.
              The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:SIZe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:SIZe?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:SIZe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:SIZe <NR1>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:SIZe?
            ```

        Info:
            - ``<NR1>`` specifies the data size.
        """
        return self._size

    @property
    def value(self) -> SearchSearchItemTriggerABusCanDataValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:VALue`` command.

        Description:
            - This command sets or queries the binary data value to be used when searching on a CAN
              bus signal. The search condition must be set to IDANDDATA OR DATA.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:VALue?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:VALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:VALue?
            ```

        Info:
            - ``<QString>``
        """
        return self._value


class SearchSearchItemTriggerABusCanCondition(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:CONDition`` command.

    Description:
        - This command sets or queries the search condition for a CAN bus. The search number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:CONDition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:CONDition value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:CONDition {SOF|FRAMEtype|IDentifier|DATa|IDANDDATA|EOF|ERRor|FDBITS}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:CONDition?
        ```

    Info:
        - ``SOF`` specifies the search condition for a CAN bus as start of frame.
        - ``FRAMEtype`` specifies the search condition for a CAN bus as frame type.
        - ``IDentifier`` specifies the search condition for a CAN bus as identifier.
        - ``IDANDDATA`` specifies the search condition for a CAN bus as ID and data.
        - ``EOF`` specifies the search condition for a CAN bus as end of frame.
        - ``ERRor`` specifies the search condition for a CAN bus as error.
        - ``FDBITS`` specifies the search condition for a CAN bus as FD bits.
    """  # noqa: E501


class SearchSearchItemTriggerABusCan(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:CONDition`` command.
        - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa`` command tree.
        - ``.errtype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:ERRType`` command.
        - ``.fd``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD`` command tree.
        - ``.frametype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FRAMEtype`` command.
        - ``.identifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = SearchSearchItemTriggerABusCanCondition(
            device, f"{self._cmd_syntax}:CONDition"
        )
        self._data = SearchSearchItemTriggerABusCanData(device, f"{self._cmd_syntax}:DATa")
        self._errtype = SearchSearchItemTriggerABusCanErrtype(device, f"{self._cmd_syntax}:ERRType")
        self._fd = SearchSearchItemTriggerABusCanFd(device, f"{self._cmd_syntax}:FD")
        self._frametype = SearchSearchItemTriggerABusCanFrametype(
            device, f"{self._cmd_syntax}:FRAMEtype"
        )
        self._identifier = SearchSearchItemTriggerABusCanIdentifier(
            device, f"{self._cmd_syntax}:IDentifier"
        )

    @property
    def condition(self) -> SearchSearchItemTriggerABusCanCondition:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:CONDition`` command.

        Description:
            - This command sets or queries the search condition for a CAN bus. The search number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:CONDition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:CONDition?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:CONDition value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:CONDition {SOF|FRAMEtype|IDentifier|DATa|IDANDDATA|EOF|ERRor|FDBITS}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:CONDition?
            ```

        Info:
            - ``SOF`` specifies the search condition for a CAN bus as start of frame.
            - ``FRAMEtype`` specifies the search condition for a CAN bus as frame type.
            - ``IDentifier`` specifies the search condition for a CAN bus as identifier.
            - ``IDANDDATA`` specifies the search condition for a CAN bus as ID and data.
            - ``EOF`` specifies the search condition for a CAN bus as end of frame.
            - ``ERRor`` specifies the search condition for a CAN bus as error.
            - ``FDBITS`` specifies the search condition for a CAN bus as FD bits.
        """  # noqa: E501
        return self._condition

    @property
    def data(self) -> SearchSearchItemTriggerABusCanData:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.direction``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:DIRection`` command.
            - ``.offset``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:OFFSet`` command.
            - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:QUALifier`` command.
            - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:SIZe`` command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa:VALue`` command.
        """
        return self._data

    @property
    def errtype(self) -> SearchSearchItemTriggerABusCanErrtype:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:ERRType`` command.

        Description:
            - This command sets or queries the type of error condition for a CAN bus to search on.
              The search number is specified by x. The search condition must be set to ERRor.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:ERRType?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:ERRType?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:ERRType value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:ERRType {ACKMISS|BITSTUFFing|FORMERRor|ANYERRor}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:ERRType?
            ```

        Info:
            - ``ACKMISS`` specifies a search based on a missing ACK field.
            - ``BITSTUFFing`` specifies a search based on a bit stuffing error.
            - ``FORMERRor`` specifies a search based on a CAN FD form error. To use this option, the
              CAN standard must be set to FDISO or FDNONISO.
            - ``ANYERRor`` specifies a search based on any error type.
        """
        return self._errtype

    @property
    def fd(self) -> SearchSearchItemTriggerABusCanFd:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.brsbit``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:BRSBit`` command.
            - ``.esibit``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD:ESIBit`` command.
        """
        return self._fd

    @property
    def frametype(self) -> SearchSearchItemTriggerABusCanFrametype:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FRAMEtype`` command.

        Description:
            - This command sets or queries CAN bus trigger frame type to be used when searching on a
              CAN bus signal. The search condition must be set to FRAMEtype. The search number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FRAMEtype?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FRAMEtype?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FRAMEtype value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FRAMEtype {DATa|ERRor|OVERLoad|REMote}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FRAMEtype?
            ```

        Info:
            - ``DATa`` sets the frame type to data.
            - ``ERRor`` sets the frame type to error.
            - ``OVERLoad`` sets the frame type to overload.
            - ``REMote`` sets the frame type to remote.
        """
        return self._frametype

    @property
    def identifier(self) -> SearchSearchItemTriggerABusCanIdentifier:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        Sub-properties:
            - ``.mode``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:MODe`` command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier:VALue`` command.
        """
        return self._identifier


#  pylint: disable=too-many-instance-attributes
class SearchSearchItemTriggerABus(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.can``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN`` command tree.
        - ``.i2c``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C`` command tree.
        - ``.lin``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN`` command tree.
        - ``.parallel``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel`` command tree.
        - ``.rs232c``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C`` command tree.
        - ``.sent``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT`` command tree.
        - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce`` command.
        - ``.spi``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._can = SearchSearchItemTriggerABusCan(device, f"{self._cmd_syntax}:CAN")
        self._i2c = SearchSearchItemTriggerABusI2c(device, f"{self._cmd_syntax}:I2C")
        self._lin = SearchSearchItemTriggerABusLin(device, f"{self._cmd_syntax}:LIN")
        self._parallel = SearchSearchItemTriggerABusParallel(device, f"{self._cmd_syntax}:PARallel")
        self._rs232c = SearchSearchItemTriggerABusRs232c(device, f"{self._cmd_syntax}:RS232C")
        self._sent = SearchSearchItemTriggerABusSent(device, f"{self._cmd_syntax}:SENT")
        self._source = SearchSearchItemTriggerABusSource(device, f"{self._cmd_syntax}:SOUrce")
        self._spi = SearchSearchItemTriggerABusSpi(device, f"{self._cmd_syntax}:SPI")

    @property
    def can(self) -> SearchSearchItemTriggerABusCan:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:CONDition`` command.
            - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:DATa`` command tree.
            - ``.errtype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:ERRType`` command.
            - ``.fd``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FD`` command tree.
            - ``.frametype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:FRAMEtype`` command.
            - ``.identifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN:IDentifier`` command tree.
        """
        return self._can

    @property
    def i2c(self) -> SearchSearchItemTriggerABusI2c:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.address``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:ADDRess`` command tree.
            - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:CONDition`` command.
            - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C:DATa`` command tree.
        """
        return self._i2c

    @property
    def lin(self) -> SearchSearchItemTriggerABusLin:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:CONDition`` command.
            - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:DATa`` command tree.
            - ``.errtype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:ERRTYPE`` command.
            - ``.identifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN:IDentifier`` command tree.
        """
        return self._lin

    @property
    def parallel(self) -> SearchSearchItemTriggerABusParallel:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel:DATa`` command tree.
        """
        return self._parallel

    @property
    def rs232c(self) -> SearchSearchItemTriggerABusRs232c:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:CONDition`` command.
            - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C:DATa`` command tree.
        """
        return self._rs232c

    @property
    def sent(self) -> SearchSearchItemTriggerABusSent:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:CONDition`` command.
            - ``.errtype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:ERRType`` command.
            - ``.fast``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:FAST`` command tree.
            - ``.pause``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:PAUSE`` command tree.
            - ``.slow``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT:SLOW`` command tree.
        """
        return self._sent

    @property
    def source(self) -> SearchSearchItemTriggerABusSource:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce`` command.

        Description:
            - This command sets or queries the bus source for the bus search to determine where to
              place a mark. The search number is specified by x.

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
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce {B0|B1|B2|B3|B4|B5|B6|B7|B8|B9|B10|B11|B12|B13|B14|B15|B16}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce?
            ```

        Info:
            - ``B<x>`` specifies the bus source as a bus number from B01 to B16. x has a minimum of
              0 and a maximum of 16.
        """  # noqa: E501
        return self._source

    @property
    def spi(self) -> SearchSearchItemTriggerABusSpi:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:CONDition`` command.
            - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:DATa`` command tree.
            - ``.sourcetype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI:SOURCETYpe`` command.
        """
        return self._spi


#  pylint: disable=too-many-instance-attributes
class SearchSearchItemTriggerA(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bus``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS`` command tree.
        - ``.edge``: The ``SEARCH:SEARCH<x>:TRIGger:A:EDGE`` command tree.
        - ``.logic``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc`` command tree.
        - ``.pulsewidth``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth`` command tree.
        - ``.runt``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT`` command tree.
        - ``.sethold``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold`` command tree.
        - ``.state``: The ``SEARCH:SEARCH<x>:TRIGger:A:STATE`` command.
        - ``.stopacq``: The ``SEARCH:SEARCH<x>:TRIGger:A:STOPAcq`` command.
        - ``.timeout``: The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut`` command tree.
        - ``.type``: The ``SEARCH:SEARCH<x>:TRIGger:A:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bus = SearchSearchItemTriggerABus(device, f"{self._cmd_syntax}:BUS")
        self._edge = SearchSearchItemTriggerAEdge(device, f"{self._cmd_syntax}:EDGE")
        self._logic = SearchSearchItemTriggerALogic(device, f"{self._cmd_syntax}:LOGIc")
        self._pulsewidth = SearchSearchItemTriggerAPulsewidth(
            device, f"{self._cmd_syntax}:PULSEWidth"
        )
        self._runt = SearchSearchItemTriggerARunt(device, f"{self._cmd_syntax}:RUNT")
        self._sethold = SearchSearchItemTriggerASethold(device, f"{self._cmd_syntax}:SETHold")
        self._state = SearchSearchItemTriggerAState(device, f"{self._cmd_syntax}:STATE")
        self._stopacq = SearchSearchItemTriggerAStopacq(device, f"{self._cmd_syntax}:STOPAcq")
        self._timeout = SearchSearchItemTriggerATimeout(device, f"{self._cmd_syntax}:TIMEOut")
        self._type = SearchSearchItemTriggerAType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def bus(self) -> SearchSearchItemTriggerABus:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS?`` query.
            - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.can``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:CAN`` command tree.
            - ``.i2c``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:I2C`` command tree.
            - ``.lin``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:LIN`` command tree.
            - ``.parallel``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:PARallel`` command tree.
            - ``.rs232c``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:RS232C`` command tree.
            - ``.sent``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SENT`` command tree.
            - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce`` command.
            - ``.spi``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:SPI`` command tree.
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
            - ``.threshold``: The ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:THReshold`` command.
        """
        return self._edge

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
            - ``.clock``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:CLOCk`` command tree.
            - ``.deltatime``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:DELTatime`` command.
            - ``.function``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion`` command.
            - ``.input``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPUT`` command tree.
            - ``.level``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LEVel`` command tree.
            - ``.logicpattern``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:LOGICPattern`` command tree.
            - ``.polarity``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:POLarity`` command.
            - ``.useclockedge``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:USEClockedge`` command.
            - ``.when``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:WHEn`` command.
        """
        return self._logic

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
            - ``.highlimit``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:HIGHLimit`` command.
            - ``.logicqualification``: The
              ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOGICQUALification`` command.
            - ``.lowlimit``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOWLimit`` command.
            - ``.polarity``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity`` command.
            - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce`` command.
            - ``.threshold``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:THReshold`` command.
            - ``.when``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn`` command.
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
            - ``.logicqualification``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:LOGICQUALification``
              command.
            - ``.polarity``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity`` command.
            - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce`` command.
            - ``.threshold``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:THReshold`` command tree.
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
            - ``.holdtime``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:HOLDTime`` command.
            - ``.level``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LEVel`` command tree.
            - ``.logicpattern``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:LOGICPattern`` command
              tree.
            - ``.settime``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:SETTime`` command.
        """
        return self._sethold

    @property
    def state(self) -> SearchSearchItemTriggerAState:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:STATE`` command.

        Description:
            - This command sets or queries the enabled state of the search. The search number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:STATE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:STATE value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:STATE {ON|OFF|<NR1>}
            - SEARCH:SEARCH<x>:TRIGger:A:STATE?
            ```

        Info:
            - ``<NR1>`` = 1 enables the search. Any other character disables the search.
            - ``ON`` enables the search.
            - ``OFF`` disables the search.
        """
        return self._state

    @property
    def stopacq(self) -> SearchSearchItemTriggerAStopacq:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:STOPAcq`` command.

        Description:
            - This command sets or queries whether acquisitions are stopped when a search hit is
              found. The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:STOPAcq?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:STOPAcq?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:STOPAcq value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:STOPAcq {ON|OFF|<NR1>}
            - SEARCH:SEARCH<x>:TRIGger:A:STOPAcq?
            ```

        Info:
            - ``<x>`` is the number of the search on which to enable or disable the stop acquisition
              function.
            - ``<NR1>`` = 1 enables stopping when a search hit is found. Any other character
              disables the feature.
            - ``ON`` enables stopping when a search hit is found.
            - ``OFF`` disables stopping on a search hit.
        """
        return self._stopacq

    @property
    def timeout(self) -> SearchSearchItemTriggerATimeout:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.logicqualification``: The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:LOGICQUALification``
              command.
            - ``.polarity``: The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:POLarity`` command.
            - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:SOUrce`` command.
            - ``.threshold``: The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:THReshold`` command.
            - ``.time``: The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:TIMe`` command.
        """
        return self._timeout

    @property
    def type(self) -> SearchSearchItemTriggerAType:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:TYPe`` command.

        Description:
            - This command sets or queries the trigger type setting for a search to determine where
              to place a mark. The search number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:TYPe?``
              query.
            - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:TYPe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TYPe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:TYPe {EDGE|RUNT|TRANsition|PULSEWidth|TIMEOut|LOGIc|SETHold|Bus}
            - SEARCH:SEARCH<x>:TRIGger:A:TYPe?
            ```

        Info:
            - ``EDGE`` triggers when the source input signal amplitude crosses the specified level
              in the direction given by the slope.
            - ``RUNT`` triggers when a pulse crosses the first preset voltage threshold but does not
              cross the second preset threshold before recrossing the first. The thresholds are set
              with the ``SEARCH:SEARCH<x>:TRIGger:A:RUNt:HIGH`` and
              ``SEARCH:SEARCH<x>:TRIGger:A:RUNt:LOW THRESHOLD`` commands.
            - ``TRANsition`` triggers when a pulse crosses both thresholds in the same direction as
              the specified polarity and the transition time between the two threshold crossings is
              greater or less than the specified time delta.
            - ``PULSEWidth`` triggers on input signal source pulses that are inside or outside of
              the given time range specified by
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit`` and
              ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:MORELimit``. The polarity is selected
              using the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT``: POLarity command.
            - ``TIMEOut`` triggers on an input signal source that stays above, stays below, or stays
              either above or beow the trigger level for a given time.
            - ``LOGIc`` specifies that a search occurs when specified conditions are met, and is
              controlled by the ``SEARCH:A:LOGIc`` commands.
            - ``SETHold`` triggers on a functional pattern combination of one to three data sources
              at the time of the clock transition.
            - ``Bus`` specifies that a search occurs when a communications signal is found.
        """  # noqa: E501
        return self._type


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
            - ``.bus``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS`` command tree.
            - ``.edge``: The ``SEARCH:SEARCH<x>:TRIGger:A:EDGE`` command tree.
            - ``.logic``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc`` command tree.
            - ``.pulsewidth``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth`` command tree.
            - ``.runt``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT`` command tree.
            - ``.sethold``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold`` command tree.
            - ``.state``: The ``SEARCH:SEARCH<x>:TRIGger:A:STATE`` command.
            - ``.stopacq``: The ``SEARCH:SEARCH<x>:TRIGger:A:STOPAcq`` command.
            - ``.timeout``: The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut`` command tree.
            - ``.type``: The ``SEARCH:SEARCH<x>:TRIGger:A:TYPe`` command.
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


class SearchSearchItemNavigate(SCPICmdWrite):
    """The ``SEARCH:SEARCH<x>:NAVigate`` command.

    Description:
        - This command sets the navigation action for search marks. The NONE action is the default
          setting when no action is being taken. The search number is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``SEARCH:SEARCH<x>:NAVigate value``
          command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:NAVigate {NEXT|PREVious|MIN|NONE|MAX}
        ```

    Info:
        - ``NEXT`` goes to the next search mark.
        - ``PREVious`` goes to the previous search mark.
        - ``MIN`` goes to the search result with the smallest value. Only supported by search
          results which have quantitative values (example: pulse width is supported, but not edge).
        - ``NONE`` is the default setting when no action is being taken.
        - ``MAX`` goes to the search result with the largest value. Only supported by search results
          which have quantitative values (example: pulse width is supported, but not edge).
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
        - ``.navigate``: The ``SEARCH:SEARCH<x>:NAVigate`` command.
        - ``.total``: The ``SEARCH:SEARCH<x>:TOTAL`` command.
        - ``.trigger``: The ``SEARCH:SEARCH<x>:TRIGger`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._copy = SearchSearchItemCopy(device, f"{self._cmd_syntax}:COPy")
        self._navigate = SearchSearchItemNavigate(device, f"{self._cmd_syntax}:NAVigate")
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
    def navigate(self) -> SearchSearchItemNavigate:
        """Return the ``SEARCH:SEARCH<x>:NAVigate`` command.

        Description:
            - This command sets the navigation action for search marks. The NONE action is the
              default setting when no action is being taken. The search number is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``SEARCH:SEARCH<x>:NAVigate value``
              command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:NAVigate {NEXT|PREVious|MIN|NONE|MAX}
            ```

        Info:
            - ``NEXT`` goes to the next search mark.
            - ``PREVious`` goes to the previous search mark.
            - ``MIN`` goes to the search result with the smallest value. Only supported by search
              results which have quantitative values (example: pulse width is supported, but not
              edge).
            - ``NONE`` is the default setting when no action is being taken.
            - ``MAX`` goes to the search result with the largest value. Only supported by search
              results which have quantitative values (example: pulse width is supported, but not
              edge).
        """
        return self._navigate

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


class SearchList(SCPICmdRead):
    """The ``SEARCH:LIST`` command.

    Description:
        - This command returns a comma separated list of all currently defined searches.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:LIST?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:LIST?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SEARCH:LIST?
        ```
    """


class SearchDelete(SCPICmdWrite):
    """The ``SEARCH:DELete`` command.

    Description:
        - This command deletes the specified search.

    Usage:
        - Using the ``.write(value)`` method will send the ``SEARCH:DELete value`` command.

    SCPI Syntax:
        ```
        - SEARCH:DELete <QString>
        ```

    Info:
        - ``<QString>`` is the specified search. The argument is of the form 'SEARCH<NR1>', where
          <NR1> is ≥ 1).
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchDeleteall(SCPICmdWriteNoArguments):
    """The ``SEARCH:DELETEALL`` command.

    Description:
        - This command deletes all the active instances of search definitions defined in the scope
          application.

    Usage:
        - Using the ``.write()`` method will send the ``SEARCH:DELETEALL`` command.

    SCPI Syntax:
        ```
        - SEARCH:DELETEALL
        ```
    """


class SearchAddnew(SCPICmdWrite):
    """The ``SEARCH:ADDNew`` command.

    Description:
        - This command adds the specified search.

    Usage:
        - Using the ``.write(value)`` method will send the ``SEARCH:ADDNew value`` command.

    SCPI Syntax:
        ```
        - SEARCH:ADDNew <QString>
        ```

    Info:
        - ``<QString>`` is the specified search. The argument is of the form 'SEARCH<NR1>', where
          <NR1> is ≥ 1.
    """

    _WRAP_ARG_WITH_QUOTES = True


class Search(SCPICmdRead):
    """The ``SEARCH`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.addnew``: The ``SEARCH:ADDNew`` command.
        - ``.deleteall``: The ``SEARCH:DELETEALL`` command.
        - ``.delete``: The ``SEARCH:DELete`` command.
        - ``.list``: The ``SEARCH:LIST`` command.
        - ``.search``: The ``SEARCH:SEARCH<x>`` command tree.
        - ``.selected``: The ``SEARCH:SELected`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SEARCH") -> None:
        super().__init__(device, cmd_syntax)
        self._addnew = SearchAddnew(device, f"{self._cmd_syntax}:ADDNew")
        self._deleteall = SearchDeleteall(device, f"{self._cmd_syntax}:DELETEALL")
        self._delete = SearchDelete(device, f"{self._cmd_syntax}:DELete")
        self._list = SearchList(device, f"{self._cmd_syntax}:LIST")
        self._search: Dict[int, SearchSearchItem] = DefaultDictPassKeyToFactory(
            lambda x: SearchSearchItem(device, f"{self._cmd_syntax}:SEARCH{x}")
        )
        self._selected = SearchSelected(device, f"{self._cmd_syntax}:SELected")

    @property
    def addnew(self) -> SearchAddnew:
        """Return the ``SEARCH:ADDNew`` command.

        Description:
            - This command adds the specified search.

        Usage:
            - Using the ``.write(value)`` method will send the ``SEARCH:ADDNew value`` command.

        SCPI Syntax:
            ```
            - SEARCH:ADDNew <QString>
            ```

        Info:
            - ``<QString>`` is the specified search. The argument is of the form 'SEARCH<NR1>',
              where <NR1> is ≥ 1.
        """
        return self._addnew

    @property
    def deleteall(self) -> SearchDeleteall:
        """Return the ``SEARCH:DELETEALL`` command.

        Description:
            - This command deletes all the active instances of search definitions defined in the
              scope application.

        Usage:
            - Using the ``.write()`` method will send the ``SEARCH:DELETEALL`` command.

        SCPI Syntax:
            ```
            - SEARCH:DELETEALL
            ```
        """
        return self._deleteall

    @property
    def delete(self) -> SearchDelete:
        """Return the ``SEARCH:DELete`` command.

        Description:
            - This command deletes the specified search.

        Usage:
            - Using the ``.write(value)`` method will send the ``SEARCH:DELete value`` command.

        SCPI Syntax:
            ```
            - SEARCH:DELete <QString>
            ```

        Info:
            - ``<QString>`` is the specified search. The argument is of the form 'SEARCH<NR1>',
              where <NR1> is ≥ 1).
        """
        return self._delete

    @property
    def list(self) -> SearchList:
        """Return the ``SEARCH:LIST`` command.

        Description:
            - This command returns a comma separated list of all currently defined searches.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:LIST?`` query.
            - Using the ``.verify(value)`` method will send the ``SEARCH:LIST?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SEARCH:LIST?
            ```
        """
        return self._list

    @property
    def search(self) -> Dict[int, SearchSearchItem]:
        """Return the ``SEARCH:SEARCH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.copy``: The ``SEARCH:SEARCH<x>:COPy`` command.
            - ``.navigate``: The ``SEARCH:SEARCH<x>:NAVigate`` command.
            - ``.total``: The ``SEARCH:SEARCH<x>:TOTAL`` command.
            - ``.trigger``: The ``SEARCH:SEARCH<x>:TRIGger`` command tree.
        """
        return self._search

    @property
    def selected(self) -> SearchSelected:
        """Return the ``SEARCH:SELected`` command.

        Description:
            - This command sets or queries the selected search, for example SEARCH1. The search
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SELected?`` query.
            - Using the ``.verify(value)`` method will send the ``SEARCH:SELected?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SEARCH:SELected value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SELected SEARCH1
            - SEARCH:SELected?
            ```

        Info:
            - ``SEARCH1`` is the specified search.
        """
        return self._selected
