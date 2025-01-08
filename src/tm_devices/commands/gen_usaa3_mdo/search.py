# pylint: disable=line-too-long
"""The search commands module.

These commands are used in the following models:
MDO3K

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SEARCH:SEARCH<x>:COPy {SEARCHtotrigger|TRIGgertosearch}
    - SEARCH:SEARCH<x>:LIST?
    - SEARCH:SEARCH<x>:STATE {ON|OFF|<NR1>}
    - SEARCH:SEARCH<x>:STATE?
    - SEARCH:SEARCH<x>:TOTal?
    - SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND:ADDR:QUAL {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
    - SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND:ADDR:QUAL?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:CONDition {STARt|END|LABel|DATA|LABELANDDATA|ERRor}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:CONDition?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:HIVALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:HIVALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:QUALifier {LESSthan|MOREthan|Equal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:QUALifier?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE {ANY|GAP|WORD|PARity}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier {LESSthan|MOREthan|Equal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SDI <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SDI?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SSM <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SSM?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:CONDition {SOF|DATA}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:CONDition?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue <String>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet <NR1>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:VALue <String>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:WORD {EITher|LEFt|RIGht}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:WORD?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe {STandard|EXTENDed}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue <bin>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:CONDition {SOF|FRAMEtype|IDentifier|DATA|IDANDDATA|EOF|ACKMISS|ERROR|FORMERRor|ANYERRor|FDBRS|FDESI}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:CONDition?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:DIRection {READ|WRITE|NOCARE}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:DIRection?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet <NR1>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:SIZe <NR1>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:SIZe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:VALue <bin>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT {ZERo|OFF|0|ONE|ON|1|NOCARE|X|x}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT {ZERo|OFF|0|ONE|ON|1|NOCARE|X|x}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FRAMEtype {DATA|REMote|ERRor|OVERLoad}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FRAMEtype?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe {STandard|EXTENDed}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue <bin>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe {BASic|QTAG}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CONDition {SOF|FRAMETypeid|CYCLEcount|HEADer|DATA|IDANDDATA|EOF|ERROR}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CONDition?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet <NR1>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
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
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
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
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:SIZe <NR1>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:SIZe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:ERRTYPE {SYNC|PARity|CHecksum|HEADertime|RESPtime|FRAMetime}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:ERRTYPE?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit {RX|TX|X}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:CONDition {SYNC|COMMAND|STATus|DATA|TIMe|ERRor}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:CONDition?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE {PARity|SYNC|MANCHester|DATA}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier {LESSthan|MOREthan|INrange|OUTrange}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:CONDition {RXSTArt|RXDATA|RXENDPacket|TXSTArt|TXDATA|TXENDPacket}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:CONDition?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:SIZe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:RX:DATa:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:SIZe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:TX:DATa:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:CONDition {SS|STARTofframe|MISO|MOSI|MISOMOSI}
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
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:CONDition {SYNC|RESET|SUSPEND|RESUME|EOP|TOKENPacket|DATAPacket|HANDSHAKEPacket|SPECIALPacket|ERRor}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:CONDition?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:HIVALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:HIVALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:OFFSet <NR1>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:OFFSet?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:SIZe <NR1>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:SIZe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:TYPe {ANY|DATA<x>}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:TYPe?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ERRTYPE {PID|CRC5|CRC16|BITSTUFFing}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ERRTYPE?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:HANDSHAKEType {ANY|NAK|ACK|STALL}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:HANDSHAKEType?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:QUALifier?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPECIALType {ANY|PREamble|RESERVed}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPECIALType?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue {NOCARE|CONTRol|ISOchronous|BULK|INTERRUPT}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue <QString>
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue {NOCARE|SSPLIT|CSPLIT}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue {NOCARE|FULLSPeed|LOWSPeed|ISOSTART|ISOMID|ISOEND|ISOALL}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:TOKENType {ANY|SOF|OUT|IN|SETUP}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:TOKENType?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce {B<x>}
    - SEARCH:SEARCH<x>:TRIGger:A:BUS:SOUrce?
    - SEARCH:SEARCH<x>:TRIGger:A:BUS?
    - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe {RISe|FALL|EITHer}
    - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe?
    - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce {CH<x>|MATH|REF<x>|D<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe}
    - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce?
    - SEARCH:SEARCH<x>:TRIGger:A:LEVel:CH<x> {<NR3>|ECL|TTL}
    - SEARCH:SEARCH<x>:TRIGger:A:LEVel:CH<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LEVel:MATH {<NR3>|ECL|TTL}
    - SEARCH:SEARCH<x>:TRIGger:A:LEVel:MATH?
    - SEARCH:SEARCH<x>:TRIGger:A:LEVel:REF<x> {<NR3>|ECL|TTL}
    - SEARCH:SEARCH<x>:TRIGger:A:LEVel:REF<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_AMPlitude {<NR3>|ECL|TTL}
    - SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_AMPlitude?
    - SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_FREQuency {<NR3>|ECL|TTL}
    - SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_FREQuency?
    - SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_PHASe {<NR1>|ECL|TTL}
    - SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_PHASe?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion {AND|NANd|NOR|OR}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:FUNCtion?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CH<x> {HIGH|LOW|X}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CH<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:EDGE {FALL|RISe}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:EDGE?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:SOUrce {CH<x>|MATH|REF|NONe|D<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:D<x> {HIGH|LOW|X}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:D<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:MATH {HIGH|LOW|X}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:MATH?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:REF<x> {HIGH|LOW|X}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:REF<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:CH<x> {HIGH|LOW|X}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:INPut:CH<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn {TRUe|FALSe|LESSthan|Than|EQual|UNEQual}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:MORELimit <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn:MORELimit?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:CH<x> {<NR3>|TTL}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:CH<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:MATH {TTL}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:MATH?
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:REF<x> {TTL}
    - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:REF<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:CH<x> {TTL}
    - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:CH<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:MATH {TTL}
    - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:MATH?
    - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:REF<x> {TTL}
    - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:REF<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_FREQuency {<NR3>}
    - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_FREQuency?
    - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_PHASe {<NR3>}
    - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_PHASe?
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:HIGHLimit <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:HIGHLimit?
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOWLimit <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOWLimit?
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity {NEGative|POSitive}
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity?
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce {CH<x>|MATH|REF<x>|D<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe}
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce?
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn {LESSthan|MOREthan|EQual|UNEQual|WIThin|OUTside}
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn?
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WIDth <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WIDth?
    - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:DELTatime <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:DELTatime?
    - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:POLarity {EITher|NEGative|POSitive}
    - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:POLarity?
    - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:SOUrce {CH<x>|MATH|REF<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe}
    - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:SOUrce?
    - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:WHEn {SLOWer|FASTer|EQual|UNEQual}
    - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:WHEn?
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity {EITher|NEGative|POSitive}
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:POLarity?
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce {CH<x>|MATH|REF<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe}
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce?
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn {LESSthan|than|EQual|UNEQual|OCCURS}
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn?
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WIDth?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:EDGE {FALL|RISe}
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:EDGE?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce {CH<x>|MATH|REF1|REF3|REF3|REF4|D<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe}
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:THReshold {<NR3>|TTL|ECL}
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:THReshold?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:SOUrce {CH<x>|MATH|REF<x>|D<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe}
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:SOUrce?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:THReshold {<NR3>|TTL}
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:THReshold?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:HOLDTime <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:HOLDTime?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:SETTime <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:SETTime?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH1 <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH1?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH?
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:REF<x> <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:REF<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:POLarity {STAYSHigh|STAYSLow|EITher}
    - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:POLarity?
    - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:SOUrce {CH<x>|MATH|REF<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|RF_AMPlitude|RF_FREQuency|RF_PHASe}
    - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:SOUrce?
    - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:TIMe <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:TIMe?
    - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:DELTatime <NR3>
    - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:DELTatime?
    - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:POLarity {EITher|NEGative|POSitive}
    - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:POLarity?
    - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:SOUrce {CH<x>|MATH|REF<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe}
    - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:SOUrce?
    - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:WHEn {SLOWer|FASTer|EQual|UNEQual}
    - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:WHEn?
    - SEARCH:SEARCH<x>:TRIGger:A:TYPe {EDGe|PULSEWidth|SETHold|RUNt|TRANsition|LOGIc|TIMEOut|BUS (with the appropriate application module installed)}
    - SEARCH:SEARCH<x>:TRIGger:A:TYPe?
    - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:CH<x> {TTL}
    - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:CH<x>?
    - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:MATH {TTL}
    - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:MATH?
    - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:REF<x> {TTL}
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
        - This command specifies the reference waveform upper threshold to determine where to place
          a mark. This setting is applied to all reference waveform searches that use an upper
          threshold. SEARCH<x> is the search number, which is always 1, and REF<x> is the reference
          channel number, which can be 1-4.

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
        - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:REF<x> {TTL}
        - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:REF<x>?
        ```

    Info:
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
    """


class SearchSearchItemTriggerAUpperthresholdMath(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:MATH`` command.

    Description:
        - This command specifies the math waveform upper threshold to determine where to place a
          mark. This setting is applied to all math waveform searches that uses an upper threshold.
          <x> is the search number.

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
        - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:MATH {TTL}
        - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:MATH?
        ```

    Info:
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
    """


class SearchSearchItemTriggerAUpperthresholdChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:CH<x>`` command.

    Description:
        - This command specifies the channel waveform upper threshold to determine where to place a
          mark. This setting is applied to all channel searches that uses an upper threshold.
          SEARCH<x> is the search number, which is always 1, and CH<x> is the channel number, which
          is 1-4.

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
        - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:CH<x> {TTL}
        - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:CH<x>?
        ```

    Info:
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
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
            - This command specifies the channel waveform upper threshold to determine where to
              place a mark. This setting is applied to all channel searches that uses an upper
              threshold. SEARCH<x> is the search number, which is always 1, and CH<x> is the channel
              number, which is 1-4.

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
            - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:CH<x> {TTL}
            - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:CH<x>?
            ```

        Info:
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
        """
        return self._ch

    @property
    def math(self) -> SearchSearchItemTriggerAUpperthresholdMath:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:MATH`` command.

        Description:
            - This command specifies the math waveform upper threshold to determine where to place a
              mark. This setting is applied to all math waveform searches that uses an upper
              threshold. <x> is the search number.

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
            - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:MATH {TTL}
            - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:MATH?
            ```

        Info:
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
        """
        return self._math

    @property
    def ref(self) -> Dict[int, SearchSearchItemTriggerAUpperthresholdRefItem]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:REF<x>`` command.

        Description:
            - This command specifies the reference waveform upper threshold to determine where to
              place a mark. This setting is applied to all reference waveform searches that use an
              upper threshold. SEARCH<x> is the search number, which is always 1, and REF<x> is the
              reference channel number, which can be 1-4.

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
            - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:REF<x> {TTL}
            - SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold:REF<x>?
            ```

        Info:
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
        """
        return self._ref


class SearchSearchItemTriggerAType(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:TYPe`` command.

    Description:
        - This command specifies the search type to determine where to place a mark. The default
          search type is EDGe. SEARCH<x> is the search number, which is always 1.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:TYPe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:TYPe value``
          command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:TYPe {EDGe|PULSEWidth|SETHold|RUNt|TRANsition|LOGIc|TIMEOut|BUS (with the appropriate application module installed)}
        - SEARCH:SEARCH<x>:TRIGger:A:TYPe?
        ```

    Info:
        - ``EDGe`` is the default search. An edge search occurs when a signal passes through a
          specified voltage level in a specified direction and is controlled by the
          ``SEARCH:SEARCHX:TRIGGER:A:EDGE:SOURCE`` and ``SEARCH:SEARCHX:TRIGGER:A:EDGE:SLOPE``
          commands.
        - ``PULSEWIdth`` searches when a pulse is found that has the specified polarity, and is
          either inside or outside the limits as specified by
          ``SEARCH:SEARCHX:TRIGGER:A:LOGIC:PATTERN:WHEN:LESSLIMIT`` and
          ``SEARCH:SEARCHX:TRIGGER:A:LOGIC:PATTERN:WHEN:MORELIMIT``. The polarity is selected using
          the ``SEARCH:SEARCHX:TRIGGER:A:RUNT:POLARITY`` command.
        - ``SETHold`` specifies a setup and hold search.
        - ``RUNt`` searches for when a pulse crosses the first preset voltage threshold, but does
          not cross the second preset threshold before recrossing the first. The thresholds are set
          using the ``SEARCH:SEARCHX:TRIGGER:A:LOWERTHRESHOLD:CHX`` and
          ``SEARCH:SEARCHX:TRIGGER:A:UPPERTHRESHOLD:CHX`` commands.
        - ``TRANsition`` searches for when a pulse crosses both thresholds in the same direction as
          the specified polarity and the transition time between the two threshold crossings is
          greater or less than the specified time delta.
        - ``LOGic`` specifies that a search occurs when specified conditions are met, and is
          controlled by the ``SEARCH:A:LOGIc`` commands.
        - ``TIMEout`` specifies that a search occurs when no pulse is detected in a specified time.
        - ``BUS`` specifies that a search occurs when a communications signal is found.
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
        - This command specifies the source for a transition search to determine where to place a
          mark. SEARCH<x> is the search number, which is always 1.

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
        - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:SOUrce {CH<x>|MATH|REF<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe}
        - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies one input channel as the source.
        - ``MATH`` specifies the math waveform as the source.
        - ``REF<x>`` specifies the reference waveform as the source.
    """  # noqa: E501


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
            - This command specifies the source for a transition search to determine where to place
              a mark. SEARCH<x> is the search number, which is always 1.

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
            - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:SOUrce {CH<x>|MATH|REF<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe}
            - SEARCH:SEARCH<x>:TRIGger:A:TRANsition:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies one input channel as the source.
            - ``MATH`` specifies the math waveform as the source.
            - ``REF<x>`` specifies the reference waveform as the source.
        """  # noqa: E501
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


class SearchSearchItemTriggerATimeoutSource(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:SOUrce`` command.

    Description:
        - When searching using the TIMEOut search type, this command specifies the source. The
          available sources are live channels, reference waveforms, the math waveform, or the
          digital channels. The default is channel 1. The timeout search type is selected using
          ``SEARCH:SEARCHX:TRIGGER:A:TYPE``. SEARCH<x> is the search number, which is always 1.

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
        - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:SOUrce {CH<x>|MATH|REF<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|RF_AMPlitude|RF_FREQuency|RF_PHASe}
        - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies to use one of the analog channels as the source waveform.
        - ``MATH`` specifies to use the math waveform as the as the source waveform.
        - ``REF<x>`` specifies to use one of the reference waveforms 1-4 as the as the source
          waveform.
        - ``D<x>`` specifies to use one of the digital channels as the source waveform. (Requires
          option 3-MSO.).
    """  # noqa: E501


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


class SearchSearchItemTriggerATimeout(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.polarity``: The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:POLarity`` command.
        - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:SOUrce`` command.
        - ``.time``: The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:TIMe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = SearchSearchItemTriggerATimeoutPolarity(
            device, f"{self._cmd_syntax}:POLarity"
        )
        self._source = SearchSearchItemTriggerATimeoutSource(device, f"{self._cmd_syntax}:SOUrce")
        self._time = SearchSearchItemTriggerATimeoutTime(device, f"{self._cmd_syntax}:TIMe")

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
            - When searching using the TIMEOut search type, this command specifies the source. The
              available sources are live channels, reference waveforms, the math waveform, or the
              digital channels. The default is channel 1. The timeout search type is selected using
              ``SEARCH:SEARCHX:TRIGGER:A:TYPE``. SEARCH<x> is the search number, which is always 1.

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
            - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:SOUrce {CH<x>|MATH|REF<x>|D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|RF_AMPlitude|RF_FREQuency|RF_PHASe}
            - SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies to use one of the analog channels as the source waveform.
            - ``MATH`` specifies to use the math waveform as the as the source waveform.
            - ``REF<x>`` specifies to use one of the reference waveforms 1-4 as the as the source
              waveform.
            - ``D<x>`` specifies to use one of the digital channels as the source waveform.
              (Requires option 3-MSO.).
        """  # noqa: E501
        return self._source

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


class SearchSearchItemTriggerASetholdThreshold(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.ref``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:REF<x>`` command.
        - ``.math``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH`` command.
        - ``.math1``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:THReshold:MATH1`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
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
        - This command specifies the data threshold setting for an setup/hold search to determine
          where to place a mark. SEARCH<x> is the search number, which is always 1.

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
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:THReshold {<NR3>|TTL}
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:THReshold?
        ```

    Info:
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
        - ``<NR3>`` is a floating point number that specifies the clock level, in volts.
    """


class SearchSearchItemTriggerASetholdDataSource(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:SOUrce`` command.

    Description:
        - This command specifies the data source setting for an setup/hold search to determine where
          to place a mark. <x> is the search number. You cannot specify the same source for both
          clock and data.

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
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:SOUrce {CH<x>|MATH|REF<x>|D<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe}
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the data source.
        - ``MATH`` specifies the math waveform as the data source.
        - ``REF<x>`` specifies a reference waveform as the data source.
        - ``D<x>`` specifies a digital input as the data source (models with option 3-MSO
          installed.).
    """  # noqa: E501


class SearchSearchItemTriggerASetholdData(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Info:
        - ``CH<x>`` specifies an analog channel as the data source.

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
            - This command specifies the data source setting for an setup/hold search to determine
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
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:SOUrce {CH<x>|MATH|REF<x>|D<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe}
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the data source.
            - ``MATH`` specifies the math waveform as the data source.
            - ``REF<x>`` specifies a reference waveform as the data source.
            - ``D<x>`` specifies a digital input as the data source (models with option 3-MSO
              installed.).
        """  # noqa: E501
        return self._source

    @property
    def threshold(self) -> SearchSearchItemTriggerASetholdDataThreshold:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:THReshold`` command.

        Description:
            - This command specifies the data threshold setting for an setup/hold search to
              determine where to place a mark. SEARCH<x> is the search number, which is always 1.

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
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:THReshold {<NR3>|TTL}
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:DATa:THReshold?
            ```

        Info:
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
            - ``<NR3>`` is a floating point number that specifies the clock level, in volts.
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
        - This command specifies the clock source setting for a setup/hold search to determine where
          to place a mark. SEARCH<x> is the search number, which is always 1.

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
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce {CH<x>|MATH|REF1|REF3|REF3|REF4|D<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe}
        - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the clock source waveform. x has a minimum of 1
          and a maximum of 4.
        - ``MATH`` specifies the math waveform as the clock source waveform.
        - ``REF<x>`` specifies a reference waveform as the clock source waveform. x has a minimum of
          1 and a maximum of 4.
        - ``D<x>`` specifies a digital channel as the clock source waveform. x has a minimum of 0
          and a maximum of 15.
        - ``RF_AMPlitude`` specifies an RF time domain trace as the clock source waveform.
          (MDO4000/B/C only.).
        - ``RF_FREQuency`` specifies an RF time domain trace as the clock source waveform.
          (MDO4000/B/C only.).
        - ``RF_PHASe`` specifies an RF time domain trace as the clock source waveform. (MDO4000/B/C
          only.).
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
            - This command specifies the clock source setting for a setup/hold search to determine
              where to place a mark. SEARCH<x> is the search number, which is always 1.

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
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce {CH<x>|MATH|REF1|REF3|REF3|REF4|D<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe}
            - SEARCH:SEARCH<x>:TRIGger:A:SETHold:CLOCk:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the clock source waveform. x has a minimum of
              1 and a maximum of 4.
            - ``MATH`` specifies the math waveform as the clock source waveform.
            - ``REF<x>`` specifies a reference waveform as the clock source waveform. x has a
              minimum of 1 and a maximum of 4.
            - ``D<x>`` specifies a digital channel as the clock source waveform. x has a minimum of
              0 and a maximum of 15.
            - ``RF_AMPlitude`` specifies an RF time domain trace as the clock source waveform.
              (MDO4000/B/C only.).
            - ``RF_FREQuency`` specifies an RF time domain trace as the clock source waveform.
              (MDO4000/B/C only.).
            - ``RF_PHASe`` specifies an RF time domain trace as the clock source waveform.
              (MDO4000/B/C only.).
        """  # noqa: E501
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
            - ``CH<x>`` specifies an analog channel as the data source.

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
        - This command specifies the condition setting for a runt search to determine where to place
          a mark. SEARCH<x> is the search number, which is always 1.

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
        - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn {LESSthan|than|EQual|UNEQual|OCCURS}
        - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn?
        ```

    Info:
        - ``LESSthan`` argument sets the oscilloscope to search if the a runt pulse is detected with
          width less than the time set by the ``SEARCH:SEARCHX:TRIGGER:A:RUNT:WIDTH`` command.
        - ``than`` argument sets the oscilloscope to search if the a runt pulse is detected with
          width than the time set by the ``SEARCH:SEARCHX:TRIGGER:A:RUNT:WIDTH`` command.
        - ``EQual`` argument sets the oscilloscope to search when the pattern is true for a time
          period equal to the time period specified in ``SEARCH:SEARCHX:TRIGGER:A:RUNT:WIDTH``
          within a ±5% tolerance.
        - ``UNEQual`` argument sets the oscilloscope to search when the pattern is true for a time
          period greater than or less than (but not equal) the time period specified in
          ``SEARCH:SEARCHX:TRIGGER:A:RUNT:WIDTH`` within a ±5% tolerance.
        - ``OCCURS`` argument specifies a search event if a runt of any detectable width occurs.
    """


class SearchSearchItemTriggerARuntSource(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce`` command.

    Description:
        - This command specifies the source setting for a runt search to determine where to place a
          mark. SEARCH<x> is the search number, which is always 1.

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
        - SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce {CH<x>|MATH|REF<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe}
        - SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the runt search source.
        - ``MATH`` specifies the math waveform as the runt search source.
        - ``REF<x>`` specifies a reference waveform as the runt search source.
    """  # noqa: E501


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
            - This command specifies the source setting for a runt search to determine where to
              place a mark. SEARCH<x> is the search number, which is always 1.

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
            - SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce {CH<x>|MATH|REF<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe}
            - SEARCH:SEARCH<x>:TRIGger:A:RUNT:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the runt search source.
            - ``MATH`` specifies the math waveform as the runt search source.
            - ``REF<x>`` specifies a reference waveform as the runt search source.
        """  # noqa: E501
        return self._source

    @property
    def when(self) -> SearchSearchItemTriggerARuntWhen:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn`` command.

        Description:
            - This command specifies the condition setting for a runt search to determine where to
              place a mark. SEARCH<x> is the search number, which is always 1.

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
            - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn {LESSthan|than|EQual|UNEQual|OCCURS}
            - SEARCH:SEARCH<x>:TRIGger:A:RUNT:WHEn?
            ```

        Info:
            - ``LESSthan`` argument sets the oscilloscope to search if the a runt pulse is detected
              with width less than the time set by the ``SEARCH:SEARCHX:TRIGGER:A:RUNT:WIDTH``
              command.
            - ``than`` argument sets the oscilloscope to search if the a runt pulse is detected with
              width than the time set by the ``SEARCH:SEARCHX:TRIGGER:A:RUNT:WIDTH`` command.
            - ``EQual`` argument sets the oscilloscope to search when the pattern is true for a time
              period equal to the time period specified in ``SEARCH:SEARCHX:TRIGGER:A:RUNT:WIDTH``
              within a ±5% tolerance.
            - ``UNEQual`` argument sets the oscilloscope to search when the pattern is true for a
              time period greater than or less than (but not equal) the time period specified in
              ``SEARCH:SEARCHX:TRIGGER:A:RUNT:WIDTH`` within a ±5% tolerance.
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
        - This command specifies the source for a transition search to determine where to place a
          mark. SEARCH<x> is the search number, which is always 1.

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
        - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:SOUrce {CH<x>|MATH|REF<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe}
        - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies one input channel as the source.
        - ``MATH`` specifies the math waveform as the source.
        - ``REF<x>`` specifies the reference waveform as the source.
    """  # noqa: E501


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
            - This command specifies the source for a transition search to determine where to place
              a mark. SEARCH<x> is the search number, which is always 1.

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
            - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:SOUrce {CH<x>|MATH|REF<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe}
            - SEARCH:SEARCH<x>:TRIGger:A:RISEFall:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies one input channel as the source.
            - ``MATH`` specifies the math waveform as the source.
            - ``REF<x>`` specifies the reference waveform as the source.
        """  # noqa: E501
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


class SearchSearchItemTriggerAPulsewidthSource(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce`` command.

    Description:
        - This command specifies the source waveform for a pulse search to determine where to place
          a mark. SEARCH<x> is the search number, which is always 1.

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
        - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce {CH<x>|MATH|REF<x>|D<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe}
        - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the source waveform. x has a minimum of 1 and a
          maximum of 4.
        - ``MATH`` specifies the math waveform as the source waveform.
        - ``REF<x>`` specifies a reference waveform as the source waveform. x has a minimum of 1 and
          a maximum of 4.
        - ``D<x>`` specifies a digital channel as the source waveform. x has a minimum of 0 and a
          maximum of 15.
        - ``RF_AMPlitude`` specify an RF vs. time trace as the source. (MDO4000/B/C models only.).
        - ``RF_FREQuency`` specify an RF vs. time trace as the source. (MDO4000/B/C models only.).
        - ``RF_PHASe`` specify an RF vs. time trace as the source. (MDO4000/B/C models only.).
    """  # noqa: E501


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
        - ``.lowlimit``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOWLimit`` command.
        - ``.polarity``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:POLarity`` command.
        - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce`` command.
        - ``.when``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WHEn`` command.
        - ``.width``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:WIDth`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._highlimit = SearchSearchItemTriggerAPulsewidthHighlimit(
            device, f"{self._cmd_syntax}:HIGHLimit"
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
        self._when = SearchSearchItemTriggerAPulsewidthWhen(device, f"{self._cmd_syntax}:WHEn")
        self._width = SearchSearchItemTriggerAPulsewidthWidth(device, f"{self._cmd_syntax}:WIDth")

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
            - This command specifies the source waveform for a pulse search to determine where to
              place a mark. SEARCH<x> is the search number, which is always 1.

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
            - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce {CH<x>|MATH|REF<x>|D<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe}
            - SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the source waveform. x has a minimum of 1 and
              a maximum of 4.
            - ``MATH`` specifies the math waveform as the source waveform.
            - ``REF<x>`` specifies a reference waveform as the source waveform. x has a minimum of 1
              and a maximum of 4.
            - ``D<x>`` specifies a digital channel as the source waveform. x has a minimum of 0 and
              a maximum of 15.
            - ``RF_AMPlitude`` specify an RF vs. time trace as the source. (MDO4000/B/C models
              only.).
            - ``RF_FREQuency`` specify an RF vs. time trace as the source. (MDO4000/B/C models
              only.).
            - ``RF_PHASe`` specify an RF vs. time trace as the source. (MDO4000/B/C models only.).
        """  # noqa: E501
        return self._source

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


class SearchSearchItemTriggerALowerthresholdRfPhase(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_PHASe`` command.

    Description:
        - This command specifies the lower threshold, in degrees, for searching the RF Phase vs.
          Time waveform. For runt and transition searches, this level is the lower threshold. For
          other search types, this is the single threshold. (To specify the upper threshold for runt
          and transition searches, use the command
          ``SEARCH:SEARCHX:TRIGGER:A:UPPERTHRESHOLD:RF_PHASE``.)

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_PHASe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_PHASe?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_PHASe value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_PHASe {<NR3>}
        - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_PHASe?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the threshold for the time domain
          trace, in degrees.
    """


class SearchSearchItemTriggerALowerthresholdRfFrequency(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_FREQuency`` command.

    Description:
        - This command specifies the threshold for RF Frequency vs. Time trace searches. For runt
          and transition searches, this level is the lower threshold. For other search types, this
          is the single threshold. (To specify the upper threshold for runt and transition searches,
          use the command ``SEARCH:SEARCHX:TRIGGER:A:UPPERTHRESHOLD:RF_FREQUENCY``.)

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_FREQuency?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_FREQuency value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_FREQuency {<NR3>}
        - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_FREQuency?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the threshold for the time domain
          trace, in Hz.
    """


class SearchSearchItemTriggerALowerthresholdRefItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead
):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:REF<x>`` command.

    Description:
        - This command specifies the reference waveform lower threshold to determine where to place
          a mark. This setting is applied to all reference searches that use a lower threshold.
          SEARCH<x> is the search number, which is always 1, and REF<x> is the reference channel
          number, which is 1-4.

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
        - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:REF<x> {TTL}
        - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:REF<x>?
        ```

    Info:
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
    """


class SearchSearchItemTriggerALowerthresholdMath(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:MATH`` command.

    Description:
        - This command specifies the math waveform lower threshold to determine where to place a
          mark. This setting is applied to all math searches that use a lower threshold. SEARCH<x>
          is the search number, which is always 1.

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
        - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:MATH {TTL}
        - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:MATH?
        ```

    Info:
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
    """


class SearchSearchItemTriggerALowerthresholdChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:CH<x>`` command.

    Description:
        - This command specifies the lower threshold of the channel waveform to be used in a search.
          This setting is applied to all channel searches that use a lower threshold. SEARCH<x> is
          the search number, which is always 1, and CH<x> is the channel number, which can be 1-4.

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
        - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:CH<x> {TTL}
        - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:CH<x>?
        ```

    Info:
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
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
        - ``.rf_frequency``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_FREQuency`` command.
        - ``.rf_phase``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_PHASe`` command.
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
        self._rf_frequency = SearchSearchItemTriggerALowerthresholdRfFrequency(
            device, f"{self._cmd_syntax}:RF_FREQuency"
        )
        self._rf_phase = SearchSearchItemTriggerALowerthresholdRfPhase(
            device, f"{self._cmd_syntax}:RF_PHASe"
        )

    @property
    def ch(self) -> Dict[int, SearchSearchItemTriggerALowerthresholdChannel]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:CH<x>`` command.

        Description:
            - This command specifies the lower threshold of the channel waveform to be used in a
              search. This setting is applied to all channel searches that use a lower threshold.
              SEARCH<x> is the search number, which is always 1, and CH<x> is the channel number,
              which can be 1-4.

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
            - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:CH<x> {TTL}
            - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:CH<x>?
            ```

        Info:
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
        """
        return self._ch

    @property
    def math(self) -> SearchSearchItemTriggerALowerthresholdMath:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:MATH`` command.

        Description:
            - This command specifies the math waveform lower threshold to determine where to place a
              mark. This setting is applied to all math searches that use a lower threshold.
              SEARCH<x> is the search number, which is always 1.

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
            - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:MATH {TTL}
            - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:MATH?
            ```

        Info:
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
        """
        return self._math

    @property
    def ref(self) -> Dict[int, SearchSearchItemTriggerALowerthresholdRefItem]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:REF<x>`` command.

        Description:
            - This command specifies the reference waveform lower threshold to determine where to
              place a mark. This setting is applied to all reference searches that use a lower
              threshold. SEARCH<x> is the search number, which is always 1, and REF<x> is the
              reference channel number, which is 1-4.

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
            - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:REF<x> {TTL}
            - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:REF<x>?
            ```

        Info:
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
        """
        return self._ref

    @property
    def rf_frequency(self) -> SearchSearchItemTriggerALowerthresholdRfFrequency:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_FREQuency`` command.

        Description:
            - This command specifies the threshold for RF Frequency vs. Time trace searches. For
              runt and transition searches, this level is the lower threshold. For other search
              types, this is the single threshold. (To specify the upper threshold for runt and
              transition searches, use the command
              ``SEARCH:SEARCHX:TRIGGER:A:UPPERTHRESHOLD:RF_FREQUENCY``.)

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_FREQuency?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_FREQuency value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_FREQuency {<NR3>}
            - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_FREQuency?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the threshold for the time domain
              trace, in Hz.
        """
        return self._rf_frequency

    @property
    def rf_phase(self) -> SearchSearchItemTriggerALowerthresholdRfPhase:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_PHASe`` command.

        Description:
            - This command specifies the lower threshold, in degrees, for searching the RF Phase vs.
              Time waveform. For runt and transition searches, this level is the lower threshold.
              For other search types, this is the single threshold. (To specify the upper threshold
              for runt and transition searches, use the command
              ``SEARCH:SEARCHX:TRIGGER:A:UPPERTHRESHOLD:RF_PHASE``.)

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_PHASe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_PHASe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_PHASe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_PHASe {<NR3>}
            - SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_PHASe?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the threshold for the time domain
              trace, in degrees.
        """
        return self._rf_phase


class SearchSearchItemTriggerALogicThresholdRefItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead
):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:REF<x>`` command.

    Description:
        - This command specifies the reference waveform threshold level for a logic search to
          determine where to place a mark. SEARCH<x> is the search number, which is always 1, and
          REF<x> is the reference channel number, which can be 1-4.

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
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:REF<x> {TTL}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:REF<x>?
        ```

    Info:
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
    """


class SearchSearchItemTriggerALogicThresholdMath(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:MATH`` command.

    Description:
        - This command specifies the math waveform threshold level for a logic search to determine
          where to place a mark. SEARCH<x> is the search number, which is always 1.

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
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:MATH {TTL}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:MATH?
        ```

    Info:
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
    """


class SearchSearchItemTriggerALogicThresholdChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:CH<x>`` command.

    Description:
        - This command specifies the channel threshold level for a logic search to determine where
          to place a mark. SEARCH<x> is the search number, which is always 1, and CH<x> is the
          channel number, which can be 1-4.

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
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:CH<x> {<NR3>|TTL}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:CH<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the search level, in volts.
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
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
            - This command specifies the channel threshold level for a logic search to determine
              where to place a mark. SEARCH<x> is the search number, which is always 1, and CH<x> is
              the channel number, which can be 1-4.

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
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:CH<x> {<NR3>|TTL}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:CH<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the search level, in volts.
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
        """
        return self._ch

    @property
    def math(self) -> SearchSearchItemTriggerALogicThresholdMath:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:MATH`` command.

        Description:
            - This command specifies the math waveform threshold level for a logic search to
              determine where to place a mark. SEARCH<x> is the search number, which is always 1.

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
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:MATH {TTL}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:MATH?
            ```

        Info:
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
        """
        return self._math

    @property
    def ref(self) -> Dict[int, SearchSearchItemTriggerALogicThresholdRefItem]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:REF<x>`` command.

        Description:
            - This command specifies the reference waveform threshold level for a logic search to
              determine where to place a mark. SEARCH<x> is the search number, which is always 1,
              and REF<x> is the reference channel number, which can be 1-4.

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
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:REF<x> {TTL}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:THReshold:REF<x>?
            ```

        Info:
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
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
        - This command specifies the qualifier to be used in a logic pattern search. <x> is the
          search number, which is always 1.

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
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn {TRUe|FALSe|LESSthan|Than|EQual|UNEQual}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn?
        ```

    Info:
        - ``TRUe`` places a mark when the pattern becomes true.
        - ``FALSe`` places a mark when the pattern becomes false.
        - ``LESSthan`` places a mark if the specific pattern is true less than the time set by the
          ``SEARCH:SEARCHX:TRIGGER:A:LOGIC:PATTERN:WHEN:LESSLIMIT`` command.
        - ``Than`` places a mark if the specific pattern is true longer than the specified time set
          by the ``SEARCH:SEARCHX:TRIGGER:A:LOGIC:PATTERN:WHEN:MORELIMIT`` command.
        - ``EQual`` places a mark if the specific pattern is true longer than the time set by the
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
    """

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
        """
        return self._input

    @property
    def when(self) -> SearchSearchItemTriggerALogicPatternWhen:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn`` command.

        Description:
            - This command specifies the qualifier to be used in a logic pattern search. <x> is the
              search number, which is always 1.

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
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn {TRUe|FALSe|LESSthan|Than|EQual|UNEQual}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:PATtern:WHEn?
            ```

        Info:
            - ``TRUe`` places a mark when the pattern becomes true.
            - ``FALSe`` places a mark when the pattern becomes false.
            - ``LESSthan`` places a mark if the specific pattern is true less than the time set by
              the ``SEARCH:SEARCHX:TRIGGER:A:LOGIC:PATTERN:WHEN:LESSLIMIT`` command.
            - ``Than`` places a mark if the specific pattern is true longer than the specified time
              set by the ``SEARCH:SEARCHX:TRIGGER:A:LOGIC:PATTERN:WHEN:MORELIMIT`` command.
            - ``EQual`` places a mark if the specific pattern is true longer than the time set by
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
        """
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
        - This command specifies the clock source to be used in a logic search. <x> is the search
          number, which is always 1. If a clock source is defined, then the logic search is
          determined by the state of the other inputs at the clock transition. If no clock source is
          defined, then the logic search is determined only by the state of the inputs.

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
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:SOUrce {CH<x>|MATH|REF|NONe|D<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the clock source. x has a minimum of 1 and a
          maximum of 4.
        - ``MATH`` specifies the math waveform as the clock source.
        - ``REF`` specifies the reference waveform as the clock source.
        - ``NONe`` specifies no clock source.
        - ``D<x>`` specifies a digital channel as the clock source. x has a minimum of 0 and a
          maximum of 15.
        - ``RF_AMPlitude`` specify an RF time domain trace as the clock source. (MDO4000/B/C only.).
        - ``RF_FREQuency`` specify an RF time domain trace as the clock source. (MDO4000/B/C only.).
        - ``RF_PHASe`` specify an RF time domain trace as the clock source. (MDO4000/B/C only.).
    """  # noqa: E501


class SearchSearchItemTriggerALogicInputClockEdge(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:EDGE`` command.

    Description:
        - This command specifies the clock edge condition (rising or falling) to be used in a logic
          search. <x> is the search number, which is always 1.

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
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:EDGE {FALL|RISe}
        - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:EDGE?
        ```

    Info:
        - ``RISe`` specifies a rising edge.
        - ``FALL`` specifies a falling edge.
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
            - This command specifies the clock edge condition (rising or falling) to be used in a
              logic search. <x> is the search number, which is always 1.

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
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:EDGE {FALL|RISe}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:EDGE?
            ```

        Info:
            - ``RISe`` specifies a rising edge.
            - ``FALL`` specifies a falling edge.
        """
        return self._edge

    @property
    def source(self) -> SearchSearchItemTriggerALogicInputClockSource:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:SOUrce`` command.

        Description:
            - This command specifies the clock source to be used in a logic search. <x> is the
              search number, which is always 1. If a clock source is defined, then the logic search
              is determined by the state of the other inputs at the clock transition. If no clock
              source is defined, then the logic search is determined only by the state of the
              inputs.

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
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:SOUrce {CH<x>|MATH|REF|NONe|D<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe}
            - SEARCH:SEARCH<x>:TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the clock source. x has a minimum of 1 and a
              maximum of 4.
            - ``MATH`` specifies the math waveform as the clock source.
            - ``REF`` specifies the reference waveform as the clock source.
            - ``NONe`` specifies no clock source.
            - ``D<x>`` specifies a digital channel as the clock source. x has a minimum of 0 and a
              maximum of 15.
            - ``RF_AMPlitude`` specify an RF time domain trace as the clock source. (MDO4000/B/C
              only.).
            - ``RF_FREQuency`` specify an RF time domain trace as the clock source. (MDO4000/B/C
              only.).
            - ``RF_PHASe`` specify an RF time domain trace as the clock source. (MDO4000/B/C only.).
        """  # noqa: E501
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


class SearchSearchItemTriggerALevelRfPhase(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_PHASe`` command.

    Description:
        - This command sets the threshold level to use when searching on the RF Phase vs. Time
          trace.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_PHASe?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_PHASe?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_PHASe value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_PHASe {<NR1>|ECL|TTL}
        - SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_PHASe?
        ```

    Info:
        - ``<NR3>`` is a floating point number that sets the threshold level, in Volts, to use when
          searching on the RF Phase vs. Time trace.
        - ``ECL`` sets the threshold level to a preset ECL high level of -1.3V.
        - ``TTL`` sets the threshold level to a preset TTL high level of 1.4V.
    """


class SearchSearchItemTriggerALevelRfFrequency(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_FREQuency`` command.

    Description:
        - This command sets the threshold level to use when searching on the RF Frequency vs. Time
          trace.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_FREQuency?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_FREQuency value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_FREQuency {<NR3>|ECL|TTL}
        - SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_FREQuency?
        ```

    Info:
        - ``<NR3>`` is a floating point number that sets the threshold level, in Volts, to use when
          searching on the RF Frequency vs. Time trace.
        - ``ECL`` sets the threshold level to a preset ECL high level of -1.3V.
        - ``TTL`` sets the threshold level to a preset TTL high level of 1.4V.
    """


class SearchSearchItemTriggerALevelRfAmplitude(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_AMPlitude`` command.

    Description:
        - This command sets the threshold level to use when searching on the RF Amplitude vs. Time
          trace.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_AMPlitude?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_AMPlitude?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_AMPlitude value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_AMPlitude {<NR3>|ECL|TTL}
        - SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_AMPlitude?
        ```

    Info:
        - ``<NR3>`` is a floating point number that sets the threshold level, in Volts, to use when
          searching on the RF Amplitude vs. Time trace.
        - ``ECL`` sets the threshold level to a preset ECL high level of -1.3V.
        - ``TTL`` sets the threshold level to a preset TTL high level of 1.4V.
    """


class SearchSearchItemTriggerALevelRefItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:REF<x>`` command.

    Description:
        - This command sets the threshold level to use when searching on a reference waveform.

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
        - SEARCH:SEARCH<x>:TRIGger:A:LEVel:REF<x> {<NR3>|ECL|TTL}
        - SEARCH:SEARCH<x>:TRIGger:A:LEVel:REF<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that sets the threshold level to search for, in
          Volts, when searching on a reference waveform.
        - ``ECL`` sets the threshold level to a preset ECL high level of -1.3V.
        - ``TTL`` sets the threshold level to a preset TTL high level of 1.4V.
    """


class SearchSearchItemTriggerALevelMath(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:MATH`` command.

    Description:
        - This command sets the threshold level to use when searching on the math waveform.

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
        - SEARCH:SEARCH<x>:TRIGger:A:LEVel:MATH {<NR3>|ECL|TTL}
        - SEARCH:SEARCH<x>:TRIGger:A:LEVel:MATH?
        ```

    Info:
        - ``<NR3>`` is a floating point number that sets the threshold level to search for, in
          Volts, when searching on a math waveform.
        - ``ECL`` sets the threshold level to a preset ECL high level of -1.3V.
        - ``TTL`` sets the threshold level to a preset TTL high level of 1.4V.
    """


class SearchSearchItemTriggerALevelChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:CH<x>`` command.

    Description:
        - This command sets the threshold level to use when searching on an analog waveform. x can
          be 1 - 4.

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
        - SEARCH:SEARCH<x>:TRIGger:A:LEVel:CH<x> {<NR3>|ECL|TTL}
        - SEARCH:SEARCH<x>:TRIGger:A:LEVel:CH<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that sets the threshold level to search for, in
          Volts, when searching on channel <x>.
        - ``ECL`` sets the threshold level to a preset ECL high level of -1.3V.
        - ``TTL`` sets the threshold level to a preset TTL high level of 1.4V.
    """


class SearchSearchItemTriggerALevel(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:LEVel?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:LEVel?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:CH<x>`` command.
        - ``.math``: The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:MATH`` command.
        - ``.ref``: The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:REF<x>`` command.
        - ``.rf_amplitude``: The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_AMPlitude`` command.
        - ``.rf_frequency``: The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_FREQuency`` command.
        - ``.rf_phase``: The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_PHASe`` command.
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
        self._rf_amplitude = SearchSearchItemTriggerALevelRfAmplitude(
            device, f"{self._cmd_syntax}:RF_AMPlitude"
        )
        self._rf_frequency = SearchSearchItemTriggerALevelRfFrequency(
            device, f"{self._cmd_syntax}:RF_FREQuency"
        )
        self._rf_phase = SearchSearchItemTriggerALevelRfPhase(
            device, f"{self._cmd_syntax}:RF_PHASe"
        )

    @property
    def ch(self) -> Dict[int, SearchSearchItemTriggerALevelChannel]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:CH<x>`` command.

        Description:
            - This command sets the threshold level to use when searching on an analog waveform. x
              can be 1 - 4.

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
            - SEARCH:SEARCH<x>:TRIGger:A:LEVel:CH<x> {<NR3>|ECL|TTL}
            - SEARCH:SEARCH<x>:TRIGger:A:LEVel:CH<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that sets the threshold level to search for, in
              Volts, when searching on channel <x>.
            - ``ECL`` sets the threshold level to a preset ECL high level of -1.3V.
            - ``TTL`` sets the threshold level to a preset TTL high level of 1.4V.
        """
        return self._ch

    @property
    def math(self) -> SearchSearchItemTriggerALevelMath:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:MATH`` command.

        Description:
            - This command sets the threshold level to use when searching on the math waveform.

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
            - SEARCH:SEARCH<x>:TRIGger:A:LEVel:MATH {<NR3>|ECL|TTL}
            - SEARCH:SEARCH<x>:TRIGger:A:LEVel:MATH?
            ```

        Info:
            - ``<NR3>`` is a floating point number that sets the threshold level to search for, in
              Volts, when searching on a math waveform.
            - ``ECL`` sets the threshold level to a preset ECL high level of -1.3V.
            - ``TTL`` sets the threshold level to a preset TTL high level of 1.4V.
        """
        return self._math

    @property
    def ref(self) -> Dict[int, SearchSearchItemTriggerALevelRefItem]:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:REF<x>`` command.

        Description:
            - This command sets the threshold level to use when searching on a reference waveform.

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
            - SEARCH:SEARCH<x>:TRIGger:A:LEVel:REF<x> {<NR3>|ECL|TTL}
            - SEARCH:SEARCH<x>:TRIGger:A:LEVel:REF<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that sets the threshold level to search for, in
              Volts, when searching on a reference waveform.
            - ``ECL`` sets the threshold level to a preset ECL high level of -1.3V.
            - ``TTL`` sets the threshold level to a preset TTL high level of 1.4V.
        """
        return self._ref

    @property
    def rf_amplitude(self) -> SearchSearchItemTriggerALevelRfAmplitude:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_AMPlitude`` command.

        Description:
            - This command sets the threshold level to use when searching on the RF Amplitude vs.
              Time trace.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_AMPlitude?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_AMPlitude?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_AMPlitude value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_AMPlitude {<NR3>|ECL|TTL}
            - SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_AMPlitude?
            ```

        Info:
            - ``<NR3>`` is a floating point number that sets the threshold level, in Volts, to use
              when searching on the RF Amplitude vs. Time trace.
            - ``ECL`` sets the threshold level to a preset ECL high level of -1.3V.
            - ``TTL`` sets the threshold level to a preset TTL high level of 1.4V.
        """
        return self._rf_amplitude

    @property
    def rf_frequency(self) -> SearchSearchItemTriggerALevelRfFrequency:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_FREQuency`` command.

        Description:
            - This command sets the threshold level to use when searching on the RF Frequency vs.
              Time trace.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_FREQuency?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_FREQuency value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_FREQuency {<NR3>|ECL|TTL}
            - SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_FREQuency?
            ```

        Info:
            - ``<NR3>`` is a floating point number that sets the threshold level, in Volts, to use
              when searching on the RF Frequency vs. Time trace.
            - ``ECL`` sets the threshold level to a preset ECL high level of -1.3V.
            - ``TTL`` sets the threshold level to a preset TTL high level of 1.4V.
        """
        return self._rf_frequency

    @property
    def rf_phase(self) -> SearchSearchItemTriggerALevelRfPhase:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_PHASe`` command.

        Description:
            - This command sets the threshold level to use when searching on the RF Phase vs. Time
              trace.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_PHASe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_PHASe?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_PHASe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_PHASe {<NR1>|ECL|TTL}
            - SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_PHASe?
            ```

        Info:
            - ``<NR3>`` is a floating point number that sets the threshold level, in Volts, to use
              when searching on the RF Phase vs. Time trace.
            - ``ECL`` sets the threshold level to a preset ECL high level of -1.3V.
            - ``TTL`` sets the threshold level to a preset TTL high level of 1.4V.
        """
        return self._rf_phase


class SearchSearchItemTriggerAEdgeSource(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce`` command.

    Description:
        - This command specifies the source waveform to be used in an edge search . <x> is the
          search number. SEARCH<x> is the search number, which is always 1.

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
        - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce {CH<x>|MATH|REF<x>|D<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe}
        - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the source waveform.
        - ``MATH`` specifies the math waveform as the source waveform.
        - ``REF<x>`` specifies a reference waveform as the source waveform.
        - ``D<x>`` specifies a digital channel as the source waveform.
    """  # noqa: E501


class SearchSearchItemTriggerAEdgeSlope(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe`` command.

    Description:
        - This command specifies the slope to be used in an edge search: rising, falling or either.
          <x> is the search number. SEARCH<x> is the search number, which is always 1.

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
        - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe {RISe|FALL|EITHer}
        - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe?
        ```

    Info:
        - ``RISe`` specifies a rising edge.
        - ``FALL`` specifies a falling edge.
        - ``EITHer`` specifies to trigger on either the rising or falling edge of a signal.
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
            - This command specifies the slope to be used in an edge search: rising, falling or
              either. <x> is the search number. SEARCH<x> is the search number, which is always 1.

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
            - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe {RISe|FALL|EITHer}
            - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SLOpe?
            ```

        Info:
            - ``RISe`` specifies a rising edge.
            - ``FALL`` specifies a falling edge.
            - ``EITHer`` specifies to trigger on either the rising or falling edge of a signal.
        """
        return self._slope

    @property
    def source(self) -> SearchSearchItemTriggerAEdgeSource:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce`` command.

        Description:
            - This command specifies the source waveform to be used in an edge search . <x> is the
              search number. SEARCH<x> is the search number, which is always 1.

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
            - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce {CH<x>|MATH|REF<x>|D<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe}
            - SEARCH:SEARCH<x>:TRIGger:A:EDGE:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the source waveform.
            - ``MATH`` specifies the math waveform as the source waveform.
            - ``REF<x>`` specifies a reference waveform as the source waveform.
            - ``D<x>`` specifies a digital channel as the source waveform.
        """  # noqa: E501
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


class SearchSearchItemTriggerABusBItemUsbTokentype(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:TOKENType`` command.

    Description:
        - This command specifies the token type to be used in a USB search: any, start of frame,
          out, in, or setup. SEARCH<x> is the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:TOKENType?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:TOKENType?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:TOKENType value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:TOKENType {ANY|SOF|OUT|IN|SETUP}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:TOKENType?
        ```

    Info:
        - ``ANY`` indicates any of the token types.
        - ``SOF`` indicates a SOF (start-of-frame) token type.
        - ``OUT`` indicates an OUT token type.
        - ``IN`` indicates an IN token type.
        - ``SETUP`` indicates a SETUP token type.
    """


class SearchSearchItemTriggerABusBItemUsbSplitSeValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue`` command.

    Description:
        - When searching for a high-speed USB split transaction, this command specifies the split
          transaction start/end bit value to search for. SEARCH<x> is the search number, which is
          always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue {NOCARE|FULLSPeed|LOWSPeed|ISOSTART|ISOMID|ISOEND|ISOALL}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue?
        ```

    Info:
        - ``NOCARE`` - any combination of S and E bits.
        - ``FULLSPeed`` - S bit = 0, E bit = 0.
        - ``LOWSPeed`` - S bit = 1, E bit = 0.
        - ``ISOSTART`` - S bit = 1, E bit = 0.
        - ``ISOMID`` - see note above.
        - ``ISOEND`` - see note above.
        - ``ISOALL`` - see note above.
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemUsbSplitSe(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SE?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = SearchSearchItemTriggerABusBItemUsbSplitSeValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemUsbSplitSeValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue`` command.

        Description:
            - When searching for a high-speed USB split transaction, this command specifies the
              split transaction start/end bit value to search for. SEARCH<x> is the search number,
              which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue {NOCARE|FULLSPeed|LOWSPeed|ISOSTART|ISOMID|ISOEND|ISOALL}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue?
            ```

        Info:
            - ``NOCARE`` - any combination of S and E bits.
            - ``FULLSPeed`` - S bit = 0, E bit = 0.
            - ``LOWSPeed`` - S bit = 1, E bit = 0.
            - ``ISOSTART`` - S bit = 1, E bit = 0.
            - ``ISOMID`` - see note above.
            - ``ISOEND`` - see note above.
            - ``ISOALL`` - see note above.
        """  # noqa: E501
        return self._value


class SearchSearchItemTriggerABusBItemUsbSplitScValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue`` command.

    Description:
        - When searching on a high-speed USB split transaction, this command specifies whether to
          search for the start or complete phase of the split transaction, based on the
          Start/Complete bit field value. (0 = Start, 1 = Complete). The default is NOCARE.
          SEARCH<x> is the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue {NOCARE|SSPLIT|CSPLIT}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue?
        ```

    Info:
        - ``NOCARE`` - search for either the start or complete phase of the split transaction.
        - ``SSPLIT`` - search for the start phase of the split transaction.
        - ``CSPLIT`` - search for the complete phase of the split transaction.
    """


class SearchSearchItemTriggerABusBItemUsbSplitSc(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SC`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SC?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SC?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = SearchSearchItemTriggerABusBItemUsbSplitScValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemUsbSplitScValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue`` command.

        Description:
            - When searching on a high-speed USB split transaction, this command specifies whether
              to search for the start or complete phase of the split transaction, based on the
              Start/Complete bit field value. (0 = Start, 1 = Complete). The default is NOCARE.
              SEARCH<x> is the search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue {NOCARE|SSPLIT|CSPLIT}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue?
            ```

        Info:
            - ``NOCARE`` - search for either the start or complete phase of the split transaction.
            - ``SSPLIT`` - search for the start phase of the split transaction.
            - ``CSPLIT`` - search for the complete phase of the split transaction.
        """
        return self._value


class SearchSearchItemTriggerABusBItemUsbSplitPortValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue`` command.

    Description:
        - When searching on a high-speed USB split transaction, this command specifies the split
          transaction port address value to search for. The value can be up to 7 characters long.
          The default is all X's (don't care). SEARCH<x> is the search number, which is always 1,
          and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue?
        ```

    Info:
        - ``QString`` is a quoted string of up to 7 characters. The valid characters are 0 and 1.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemUsbSplitPort(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:PORT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:PORT?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:PORT?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = SearchSearchItemTriggerABusBItemUsbSplitPortValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemUsbSplitPortValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue`` command.

        Description:
            - When searching on a high-speed USB split transaction, this command specifies the split
              transaction port address value to search for. The value can be up to 7 characters
              long. The default is all X's (don't care). SEARCH<x> is the search number, which is
              always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue?
            ```

        Info:
            - ``QString`` is a quoted string of up to 7 characters. The valid characters are 0 and
              1.
        """
        return self._value


class SearchSearchItemTriggerABusBItemUsbSplitHubValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue`` command.

    Description:
        - When searching on a high-speed USB split transaction, this command specifies the split
          transaction hub address value to search for. The value can be up to 7 characters long. The
          default is all X's (don't care). SEARCH<x> is the search number, which is always 1, and
          B<x>.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue?
        ```

    Info:
        - ``QString`` is a quoted string of up to 7 characters. The valid characters are 0 and 1.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemUsbSplitHub(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:HUB`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:HUB?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:HUB?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = SearchSearchItemTriggerABusBItemUsbSplitHubValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemUsbSplitHubValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue`` command.

        Description:
            - When searching on a high-speed USB split transaction, this command specifies the split
              transaction hub address value to search for. The value can be up to 7 characters long.
              The default is all X's (don't care). SEARCH<x> is the search number, which is always
              1, and B<x>.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue?
            ```

        Info:
            - ``QString`` is a quoted string of up to 7 characters. The valid characters are 0 and
              1.
        """
        return self._value


class SearchSearchItemTriggerABusBItemUsbSplitEtValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue`` command.

    Description:
        - When searching on a high-speed USB split transaction, this command specifies the split
          transaction endpoint type value to search for. SEARCH<x> is the search number, which is
          always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue {NOCARE|CONTRol|ISOchronous|BULK|INTERRUPT}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue?
        ```

    Info:
        - ``NOCARE`` - any endpoint type.
        - ``CONTRol`` - control endpoint type.
        - ``ISOchronous`` - isochronous endpoint type.
        - ``BULK`` - bulk endpoint type (BULK-IN or BULK-OUT).
        - ``INTERRUPT`` - interrupt endpoint type (Interrupt-IN).
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemUsbSplitEt(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:ET`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:ET?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:ET?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = SearchSearchItemTriggerABusBItemUsbSplitEtValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemUsbSplitEtValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue`` command.

        Description:
            - When searching on a high-speed USB split transaction, this command specifies the split
              transaction endpoint type value to search for. SEARCH<x> is the search number, which
              is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue {NOCARE|CONTRol|ISOchronous|BULK|INTERRUPT}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue?
            ```

        Info:
            - ``NOCARE`` - any endpoint type.
            - ``CONTRol`` - control endpoint type.
            - ``ISOchronous`` - isochronous endpoint type.
            - ``BULK`` - bulk endpoint type (BULK-IN or BULK-OUT).
            - ``INTERRUPT`` - interrupt endpoint type (Interrupt-IN).
        """  # noqa: E501
        return self._value


class SearchSearchItemTriggerABusBItemUsbSplit(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.et``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:ET`` command tree.
        - ``.hub``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:HUB`` command tree.
        - ``.port``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:PORT`` command tree.
        - ``.sc``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SC`` command tree.
        - ``.se``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SE`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._et = SearchSearchItemTriggerABusBItemUsbSplitEt(device, f"{self._cmd_syntax}:ET")
        self._hub = SearchSearchItemTriggerABusBItemUsbSplitHub(device, f"{self._cmd_syntax}:HUB")
        self._port = SearchSearchItemTriggerABusBItemUsbSplitPort(
            device, f"{self._cmd_syntax}:PORT"
        )
        self._sc = SearchSearchItemTriggerABusBItemUsbSplitSc(device, f"{self._cmd_syntax}:SC")
        self._se = SearchSearchItemTriggerABusBItemUsbSplitSe(device, f"{self._cmd_syntax}:SE")

    @property
    def et(self) -> SearchSearchItemTriggerABusBItemUsbSplitEt:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:ET`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:ET?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:ET?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue`` command.
        """
        return self._et

    @property
    def hub(self) -> SearchSearchItemTriggerABusBItemUsbSplitHub:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:HUB`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:HUB?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:HUB?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue`` command.
        """
        return self._hub

    @property
    def port(self) -> SearchSearchItemTriggerABusBItemUsbSplitPort:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:PORT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:PORT?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:PORT?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue`` command.
        """
        return self._port

    @property
    def sc(self) -> SearchSearchItemTriggerABusBItemUsbSplitSc:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SC`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SC?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SC?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue`` command.
        """
        return self._sc

    @property
    def se(self) -> SearchSearchItemTriggerABusBItemUsbSplitSe:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SE?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue`` command.
        """
        return self._se


class SearchSearchItemTriggerABusBItemUsbSpecialtype(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPECIALType`` command.

    Description:
        - This command specifies the packet ID (PID) for the special packet to be used in a USB
          search: any, preamble or reserved. SEARCH<x> is the search number, which is always 1, and
          B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPECIALType?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPECIALType?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPECIALType value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPECIALType {ANY|PREamble|RESERVed}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPECIALType?
        ```

    Info:
        - ``ANY`` indicates the oscilloscope will search for any type of special packet.
        - ``PREamble`` indicates the oscilloscope will search for a preamble special packet.
        - ``RESERVed`` indicates the oscilloscope will search for a reserved special packet.
    """


class SearchSearchItemTriggerABusBItemUsbSofframenumber(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber`` command.

    Description:
        - This command specifies the value for the start of frame to be used in a USB search, when
          the search condition is set to TOKENPacket, and the token type is set to SOF (Start of
          Frame). SEARCH<x> is the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber?
        ```

    Info:
        - ``<QString>`` within the range 000 0000 0000 to 111 1111 1111 (000 hex to 7FF hex).
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemUsbQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:QUALifier`` command.

    Description:
        - This command specifies the qualifiers for address, endpoint and data to be used in a USB
          search . SEARCH<x> is the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:QUALifier?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:QUALifier value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:QUALifier?
        ```

    Info:
        - ``LESSthan`` indicates the oscilloscope will search for a value that is less than a set
          value.
        - ``MOREthan`` indicates the oscilloscope will search for a value that is greater than a set
          value.
        - ``EQual`` indicates the oscilloscope will search for a value that is equal to a set value.
        - ``UNEQual`` indicates the oscilloscope will search for a value that is not equal to a set
          value.
        - ``LESSEQual`` indicates the oscilloscope will search for a value that is less than or
          equal to a set value.
        - ``MOREEQual`` indicates the oscilloscope will search for a value that is greater than or
          equal to a set value.
        - ``INrange`` indicates the oscilloscope will search for a value that is within a range set
          by two values.
        - ``OUTrange`` indicates the oscilloscope will search for a value that is outside of a range
          set by two values.
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemUsbHandshaketype(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:HANDSHAKEType`` command.

    Description:
        - This command specifies the handshake type to be used in a USB search. SEARCH<x> is the
          search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:HANDSHAKEType?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:HANDSHAKEType?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:HANDSHAKEType value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:HANDSHAKEType {ANY|NAK|ACK|STALL}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:HANDSHAKEType?
        ```

    Info:
        - ``ANY`` indicates the oscilloscope will search for any handshake type.
        - ``NAK`` indicates the oscilloscope will search for when a device cannot send or receive
          data.
        - ``ACK`` indicates the oscilloscope will search for when a packet is successfully received.
        - ``STALL`` indicates the oscilloscope will search for when a device requires intervention
          from the host.
    """


class SearchSearchItemTriggerABusBItemUsbErrtype(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ERRTYPE`` command.

    Description:
        - This command specifies the error type to search for in a USB search, when the search
          condition is set to ERRor. SEARCH<x> is the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ERRTYPE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ERRTYPE?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ERRTYPE value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ERRTYPE {PID|CRC5|CRC16|BITSTUFFing}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ERRTYPE?
        ```

    Info:
        - ``PID`` indicates the error type is set to packet ID.
        - ``CRC5`` indicates the error type is set to 5-bit CRC.
        - ``CRC16`` indicates the error type is set to 16-bit CRC.
        - ``BITSTUFFing`` indicates the error type is set to bit stuffing.
    """


class SearchSearchItemTriggerABusBItemUsbEndpointValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue`` command.

    Description:
        - This command specifies the endpoint value to be used for a USB search. SEARCH<x> is the
          search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue?
        ```

    Info:
        - ``<QString>`` within the range 0000 to 1111 (00 hex to 0F hex).
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemUsbEndpoint(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ENDPoint`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ENDPoint?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ENDPoint?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = SearchSearchItemTriggerABusBItemUsbEndpointValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemUsbEndpointValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue`` command.

        Description:
            - This command specifies the endpoint value to be used for a USB search. SEARCH<x> is
              the search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue?
            ```

        Info:
            - ``<QString>`` within the range 0000 to 1111 (00 hex to 0F hex).
        """
        return self._value


class SearchSearchItemTriggerABusBItemUsbDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:VALue`` command.

    Description:
        - This command specifies the lower limit value for the inside-of-range and outside-of-range
          qualifiers to be used in a USB search, when the search condition is set to DATAPacket.
          SEARCH<x> is the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:VALue?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:VALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:VALue?
        ```

    Info:
        - ``<QString>`` within the range 00000000 to 11111111 (00 hex to FF hex).
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemUsbDataType(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:TYPe`` command.

    Description:
        - This command specifies the data type to be used in a USB search, when the search condition
          is set to DATAPacket. SEARCH<x> is the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:TYPe?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:TYPe value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:TYPe {ANY|DATA<x>}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:TYPe?
        ```

    Info:
        - ``ANY`` indicates either a DATA0 or DATA1 data packet type.
        - ``DATA0`` indicates a DATA0 data packet type.
        - ``DATA1`` indicates a DATA1 data packet type.
    """


class SearchSearchItemTriggerABusBItemUsbDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:SIZe`` command.

    Description:
        - This command specifies the number of contiguous data bytes to search for in a USB search.
          The minimum and default values are 1 and the maximum value is 16. SEARCH<x> is the search
          number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:SIZe?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:SIZe <NR1>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:SIZe?
        ```
    """


class SearchSearchItemTriggerABusBItemUsbDataOffset(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:OFFSet`` command.

    Description:
        - This command specifies the data offset in bytes to search for in a USB search. The minimum
          and default values are 0 and the maximum is 1024. SEARCH<x> is the search number, which is
          always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:OFFSet?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:OFFSet?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:OFFSet value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:OFFSet <NR1>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:OFFSet?
        ```
    """


class SearchSearchItemTriggerABusBItemUsbDataHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:HIVALue`` command.

    Description:
        - This command specifies the upper limit data value for the inside-of-range and
          outside-of-range qualifiers to be used in a USB search, when the search condition is set
          to DATAPacket. Use the command ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:USB:DATA:VALUE`` to set
          the lower limit. SEARCH<x> is the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:HIVALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:HIVALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:HIVALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:HIVALue?
        ```

    Info:
        - ``<QString>`` within the range 00000000 to 11111111 (00 hex to FF hex).
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemUsbData(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:HIVALue`` command.
        - ``.offset``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:OFFSet`` command.
        - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:SIZe`` command.
        - ``.type``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:TYPe`` command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = SearchSearchItemTriggerABusBItemUsbDataHivalue(
            device, f"{self._cmd_syntax}:HIVALue"
        )
        self._offset = SearchSearchItemTriggerABusBItemUsbDataOffset(
            device, f"{self._cmd_syntax}:OFFSet"
        )
        self._size = SearchSearchItemTriggerABusBItemUsbDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._type = SearchSearchItemTriggerABusBItemUsbDataType(device, f"{self._cmd_syntax}:TYPe")
        self._value = SearchSearchItemTriggerABusBItemUsbDataValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def hivalue(self) -> SearchSearchItemTriggerABusBItemUsbDataHivalue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:HIVALue`` command.

        Description:
            - This command specifies the upper limit data value for the inside-of-range and
              outside-of-range qualifiers to be used in a USB search, when the search condition is
              set to DATAPacket. Use the command ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:USB:DATA:VALUE``
              to set the lower limit. SEARCH<x> is the search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:HIVALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:HIVALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:HIVALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:HIVALue?
            ```

        Info:
            - ``<QString>`` within the range 00000000 to 11111111 (00 hex to FF hex).
        """
        return self._hivalue

    @property
    def offset(self) -> SearchSearchItemTriggerABusBItemUsbDataOffset:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:OFFSet`` command.

        Description:
            - This command specifies the data offset in bytes to search for in a USB search. The
              minimum and default values are 0 and the maximum is 1024. SEARCH<x> is the search
              number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:OFFSet?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:OFFSet?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:OFFSet value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:OFFSet <NR1>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:OFFSet?
            ```
        """
        return self._offset

    @property
    def size(self) -> SearchSearchItemTriggerABusBItemUsbDataSize:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:SIZe`` command.

        Description:
            - This command specifies the number of contiguous data bytes to search for in a USB
              search. The minimum and default values are 1 and the maximum value is 16. SEARCH<x> is
              the search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:SIZe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:SIZe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:SIZe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:SIZe <NR1>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:SIZe?
            ```
        """
        return self._size

    @property
    def type(self) -> SearchSearchItemTriggerABusBItemUsbDataType:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:TYPe`` command.

        Description:
            - This command specifies the data type to be used in a USB search, when the search
              condition is set to DATAPacket. SEARCH<x> is the search number, which is always 1, and
              B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:TYPe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:TYPe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:TYPe {ANY|DATA<x>}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:TYPe?
            ```

        Info:
            - ``ANY`` indicates either a DATA0 or DATA1 data packet type.
            - ``DATA0`` indicates a DATA0 data packet type.
            - ``DATA1`` indicates a DATA1 data packet type.
        """
        return self._type

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemUsbDataValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:VALue`` command.

        Description:
            - This command specifies the lower limit value for the inside-of-range and
              outside-of-range qualifiers to be used in a USB search, when the search condition is
              set to DATAPacket. SEARCH<x> is the search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:VALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:VALue?
            ```

        Info:
            - ``<QString>`` within the range 00000000 to 11111111 (00 hex to FF hex).
        """
        return self._value


class SearchSearchItemTriggerABusBItemUsbCondition(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:CONDition`` command.

    Description:
        - This command specifies the search condition for a USB search. SEARCH<x> is the search
          number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:CONDition?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:CONDition value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:CONDition {SYNC|RESET|SUSPEND|RESUME|EOP|TOKENPacket|DATAPacket|HANDSHAKEPacket|SPECIALPacket|ERRor}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:CONDition?
        ```

    Info:
        - ``SYNC`` specifies to search for a Sync field of a packet.
        - ``RESET`` specifies to search for a reset condition.
        - ``SUSPEND`` specifies to search for a suspend condition.
        - ``RESUME`` specifies to search for a resume condition.
        - ``EOP`` specifies to search for an end-of-packet signal.
        - ``TOKENPacket`` specifies to search for a token packet.
        - ``DATAPacket`` specifies to search for a data packet.
        - ``HANDSHAKEPacket`` specifies to search for a handshake packet.
        - ``SPECIALPacket`` specifies to search for a special status packet.
        - ``ERRor`` specifies to search for an error condition.
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemUsbAddressValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:VALue`` command.

    Description:
        - This command specifies the address value for the lower limit for inside-of-range and
          outside-of-range qualifiers to be used in a USB search. SEARCH<x> is the search number,
          which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:VALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:VALue?
        ```

    Info:
        - ``<QString>`` within the range 0000000 to 1111111 (00 hex to 7F hex).
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemUsbAddressHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue`` command.

    Description:
        - This command specifies the upper limit of the address string for the inside-of-range and
          outside-of-range qualifiers to be used in aUSB search. Use the command
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:USB:ADDRESS:VALUE`` to set the lower limit. SEARCH<x> is
          the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue?
        ```

    Info:
        - ``<QString>`` within the range 0000000 to 1111111 (00 hex to 7F hex).
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemUsbAddress(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue`` command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = SearchSearchItemTriggerABusBItemUsbAddressHivalue(
            device, f"{self._cmd_syntax}:HIVALue"
        )
        self._value = SearchSearchItemTriggerABusBItemUsbAddressValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def hivalue(self) -> SearchSearchItemTriggerABusBItemUsbAddressHivalue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue`` command.

        Description:
            - This command specifies the upper limit of the address string for the inside-of-range
              and outside-of-range qualifiers to be used in aUSB search. Use the command
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:USB:ADDRESS:VALUE`` to set the lower limit.
              SEARCH<x> is the search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue?
            ```

        Info:
            - ``<QString>`` within the range 0000000 to 1111111 (00 hex to 7F hex).
        """
        return self._hivalue

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemUsbAddressValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:VALue`` command.

        Description:
            - This command specifies the address value for the lower limit for inside-of-range and
              outside-of-range qualifiers to be used in a USB search. SEARCH<x> is the search
              number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:VALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:VALue?
            ```

        Info:
            - ``<QString>`` within the range 0000000 to 1111111 (00 hex to 7F hex).
        """
        return self._value


#  pylint: disable=too-many-instance-attributes
class SearchSearchItemTriggerABusBItemUsb(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.address``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess`` command tree.
        - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:CONDition`` command.
        - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa`` command tree.
        - ``.endpoint``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ENDPoint`` command tree.
        - ``.errtype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ERRTYPE`` command.
        - ``.handshaketype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:HANDSHAKEType`` command.
        - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:QUALifier`` command.
        - ``.sofframenumber``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber``
          command.
        - ``.specialtype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPECIALType`` command.
        - ``.split``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit`` command tree.
        - ``.tokentype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:TOKENType`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._address = SearchSearchItemTriggerABusBItemUsbAddress(
            device, f"{self._cmd_syntax}:ADDRess"
        )
        self._condition = SearchSearchItemTriggerABusBItemUsbCondition(
            device, f"{self._cmd_syntax}:CONDition"
        )
        self._data = SearchSearchItemTriggerABusBItemUsbData(device, f"{self._cmd_syntax}:DATa")
        self._endpoint = SearchSearchItemTriggerABusBItemUsbEndpoint(
            device, f"{self._cmd_syntax}:ENDPoint"
        )
        self._errtype = SearchSearchItemTriggerABusBItemUsbErrtype(
            device, f"{self._cmd_syntax}:ERRTYPE"
        )
        self._handshaketype = SearchSearchItemTriggerABusBItemUsbHandshaketype(
            device, f"{self._cmd_syntax}:HANDSHAKEType"
        )
        self._qualifier = SearchSearchItemTriggerABusBItemUsbQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._sofframenumber = SearchSearchItemTriggerABusBItemUsbSofframenumber(
            device, f"{self._cmd_syntax}:SOFFRAMENUMber"
        )
        self._specialtype = SearchSearchItemTriggerABusBItemUsbSpecialtype(
            device, f"{self._cmd_syntax}:SPECIALType"
        )
        self._split = SearchSearchItemTriggerABusBItemUsbSplit(device, f"{self._cmd_syntax}:SPLit")
        self._tokentype = SearchSearchItemTriggerABusBItemUsbTokentype(
            device, f"{self._cmd_syntax}:TOKENType"
        )

    @property
    def address(self) -> SearchSearchItemTriggerABusBItemUsbAddress:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue`` command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess:VALue`` command.
        """
        return self._address

    @property
    def condition(self) -> SearchSearchItemTriggerABusBItemUsbCondition:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:CONDition`` command.

        Description:
            - This command specifies the search condition for a USB search. SEARCH<x> is the search
              number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:CONDition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:CONDition?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:CONDition value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:CONDition {SYNC|RESET|SUSPEND|RESUME|EOP|TOKENPacket|DATAPacket|HANDSHAKEPacket|SPECIALPacket|ERRor}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:CONDition?
            ```

        Info:
            - ``SYNC`` specifies to search for a Sync field of a packet.
            - ``RESET`` specifies to search for a reset condition.
            - ``SUSPEND`` specifies to search for a suspend condition.
            - ``RESUME`` specifies to search for a resume condition.
            - ``EOP`` specifies to search for an end-of-packet signal.
            - ``TOKENPacket`` specifies to search for a token packet.
            - ``DATAPacket`` specifies to search for a data packet.
            - ``HANDSHAKEPacket`` specifies to search for a handshake packet.
            - ``SPECIALPacket`` specifies to search for a special status packet.
            - ``ERRor`` specifies to search for an error condition.
        """  # noqa: E501
        return self._condition

    @property
    def data(self) -> SearchSearchItemTriggerABusBItemUsbData:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:HIVALue`` command.
            - ``.offset``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:OFFSet`` command.
            - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:SIZe`` command.
            - ``.type``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:TYPe`` command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa:VALue`` command.
        """
        return self._data

    @property
    def endpoint(self) -> SearchSearchItemTriggerABusBItemUsbEndpoint:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ENDPoint`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ENDPoint?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ENDPoint?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue`` command.
        """
        return self._endpoint

    @property
    def errtype(self) -> SearchSearchItemTriggerABusBItemUsbErrtype:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ERRTYPE`` command.

        Description:
            - This command specifies the error type to search for in a USB search, when the search
              condition is set to ERRor. SEARCH<x> is the search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ERRTYPE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ERRTYPE?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ERRTYPE value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ERRTYPE {PID|CRC5|CRC16|BITSTUFFing}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ERRTYPE?
            ```

        Info:
            - ``PID`` indicates the error type is set to packet ID.
            - ``CRC5`` indicates the error type is set to 5-bit CRC.
            - ``CRC16`` indicates the error type is set to 16-bit CRC.
            - ``BITSTUFFing`` indicates the error type is set to bit stuffing.
        """
        return self._errtype

    @property
    def handshaketype(self) -> SearchSearchItemTriggerABusBItemUsbHandshaketype:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:HANDSHAKEType`` command.

        Description:
            - This command specifies the handshake type to be used in a USB search. SEARCH<x> is the
              search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:HANDSHAKEType?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:HANDSHAKEType?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:HANDSHAKEType value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:HANDSHAKEType {ANY|NAK|ACK|STALL}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:HANDSHAKEType?
            ```

        Info:
            - ``ANY`` indicates the oscilloscope will search for any handshake type.
            - ``NAK`` indicates the oscilloscope will search for when a device cannot send or
              receive data.
            - ``ACK`` indicates the oscilloscope will search for when a packet is successfully
              received.
            - ``STALL`` indicates the oscilloscope will search for when a device requires
              intervention from the host.
        """
        return self._handshaketype

    @property
    def qualifier(self) -> SearchSearchItemTriggerABusBItemUsbQualifier:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:QUALifier`` command.

        Description:
            - This command specifies the qualifiers for address, endpoint and data to be used in a
              USB search . SEARCH<x> is the search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:QUALifier?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:QUALifier value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:QUALifier?
            ```

        Info:
            - ``LESSthan`` indicates the oscilloscope will search for a value that is less than a
              set value.
            - ``MOREthan`` indicates the oscilloscope will search for a value that is greater than a
              set value.
            - ``EQual`` indicates the oscilloscope will search for a value that is equal to a set
              value.
            - ``UNEQual`` indicates the oscilloscope will search for a value that is not equal to a
              set value.
            - ``LESSEQual`` indicates the oscilloscope will search for a value that is less than or
              equal to a set value.
            - ``MOREEQual`` indicates the oscilloscope will search for a value that is greater than
              or equal to a set value.
            - ``INrange`` indicates the oscilloscope will search for a value that is within a range
              set by two values.
            - ``OUTrange`` indicates the oscilloscope will search for a value that is outside of a
              range set by two values.
        """  # noqa: E501
        return self._qualifier

    @property
    def sofframenumber(self) -> SearchSearchItemTriggerABusBItemUsbSofframenumber:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber`` command.

        Description:
            - This command specifies the value for the start of frame to be used in a USB search,
              when the search condition is set to TOKENPacket, and the token type is set to SOF
              (Start of Frame). SEARCH<x> is the search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber?
            ```

        Info:
            - ``<QString>`` within the range 000 0000 0000 to 111 1111 1111 (000 hex to 7FF hex).
        """
        return self._sofframenumber

    @property
    def specialtype(self) -> SearchSearchItemTriggerABusBItemUsbSpecialtype:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPECIALType`` command.

        Description:
            - This command specifies the packet ID (PID) for the special packet to be used in a USB
              search: any, preamble or reserved. SEARCH<x> is the search number, which is always 1,
              and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPECIALType?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPECIALType?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPECIALType value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPECIALType {ANY|PREamble|RESERVed}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPECIALType?
            ```

        Info:
            - ``ANY`` indicates the oscilloscope will search for any type of special packet.
            - ``PREamble`` indicates the oscilloscope will search for a preamble special packet.
            - ``RESERVed`` indicates the oscilloscope will search for a reserved special packet.
        """
        return self._specialtype

    @property
    def split(self) -> SearchSearchItemTriggerABusBItemUsbSplit:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        Sub-properties:
            - ``.et``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:ET`` command tree.
            - ``.hub``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:HUB`` command tree.
            - ``.port``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:PORT`` command tree.
            - ``.sc``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SC`` command tree.
            - ``.se``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit:SE`` command tree.
        """
        return self._split

    @property
    def tokentype(self) -> SearchSearchItemTriggerABusBItemUsbTokentype:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:TOKENType`` command.

        Description:
            - This command specifies the token type to be used in a USB search: any, start of frame,
              out, in, or setup. SEARCH<x> is the search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:TOKENType?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:TOKENType?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:TOKENType value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:TOKENType {ANY|SOF|OUT|IN|SETUP}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:TOKENType?
            ```

        Info:
            - ``ANY`` indicates any of the token types.
            - ``SOF`` indicates a SOF (start-of-frame) token type.
            - ``OUT`` indicates an OUT token type.
            - ``IN`` indicates an IN token type.
            - ``SETUP`` indicates a SETUP token type.
        """
        return self._tokentype


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
        - This command specifies the search condition for a SPI search. SEARCH<x> is the search
          number, which is always 1, and B<x>

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
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:CONDition {SS|STARTofframe|MISO|MOSI|MISOMOSI}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:CONDition?
        ```

    Info:
        - ``SS`` specifies a search based on the Slave Selection condition.
        - ``STARTofframe`` is applicable when ``BUS:B<x>:SPI:FRAMING`` is set to IDLEtime. When the
          search condition is set to STARTofframe, the instrument searches on the first SPI clock
          after an idle time when there are no clocks.
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
            - This command specifies the search condition for a SPI search. SEARCH<x> is the search
              number, which is always 1, and B<x>

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
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:CONDition {SS|STARTofframe|MISO|MOSI|MISOMOSI}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI:CONDition?
            ```

        Info:
            - ``SS`` specifies a search based on the Slave Selection condition.
            - ``STARTofframe`` is applicable when ``BUS:B<x>:SPI:FRAMING`` is set to IDLEtime. When
              the search condition is set to STARTofframe, the instrument searches on the first SPI
              clock after an idle time when there are no clocks.
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
        - This command specifies the condition to be used in an RS-232 search. SEARCH<x> is the
          search number, which is always 1, and B<x>

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
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:CONDition {RXSTArt|RXDATA|RXENDPacket|TXSTArt|TXDATA|TXENDPacket}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:CONDition?
        ```

    Info:
        - ``RXSTArt`` specifies a search based on the RX Start Bit.
        - ``RXDATA`` specifies a search based on RX Data.
        - ``RXENDPacket`` specifies a search based on the RX End of Packet condition.
        - ``TXSTArt`` specifies a search base on the TX Start Bit.
        - ``TXDATA`` specifies a search based on TX Data.
        - ``TXENDPacket`` specifies a search based on the TX End of Packet condition.
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
            - This command specifies the condition to be used in an RS-232 search. SEARCH<x> is the
              search number, which is always 1, and B<x>

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
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:CONDition {RXSTArt|RXDATA|RXENDPacket|TXSTArt|TXDATA|TXENDPacket}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C:CONDition?
            ```

        Info:
            - ``RXSTArt`` specifies a search based on the RX Start Bit.
            - ``RXDATA`` specifies a search based on RX Data.
            - ``RXENDPacket`` specifies a search based on the RX End of Packet condition.
            - ``TXSTArt`` specifies a search base on the TX Start Bit.
            - ``TXDATA`` specifies a search based on TX Data.
            - ``TXENDPacket`` specifies a search based on the TX End of Packet condition.
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


class SearchSearchItemTriggerABusBItemMil1553bTimeQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier`` command.

    Description:
        - When the MIL-STD-1553 bus search condition is set to TIMe, this command specifies the
          search data time qualifier. (This includes a smaller set of arguments than other qualifier
          commands.) B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier {LESSthan|MOREthan|INrange|OUTrange}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier?
        ```

    Info:
        - ``LESSthan`` sets the Time qualifier to less than minimum.
        - ``MOREthan`` sets the Time qualifier to greater than maximum.
        - ``INrange`` sets the Time qualifier to inside range.
        - ``OUTrange`` sets the Time qualifier to out of range.
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemMil1553bTimeMorelimit(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit`` command.

    Description:
        - When the MIL-STD-1553 bus search condition is set to TIMe, this command specifies either
          the maximum remote terminal response time (RT) limit for the amount of time the terminal
          has to transmit, or it specifies the maximum inter-message gap (IMG). (You can specify RT
          or IMG using the ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:MIL1553B:CONDITION TIMe`` command.)
          SEARCH<x> is the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies either the maximum remote terminal
          response time (RT) or the inter-message gap (IMG) in seconds.
    """


class SearchSearchItemTriggerABusBItemMil1553bTimeLesslimit(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit`` command.

    Description:
        - When the MIL-STD-1553 bus search condition is set to TIMe, this command specifies either
          the minimum remote terminal response time (RT) limit for the amount of time the terminal
          has to transmit, or it specifies the minimum inter-message gap (IMG). (You can specify RT
          or IMG using the ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:MIL1553B:CONDITION TIMe`` command.)
          SEARCH<x> is the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit <NR3>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies either the minimum remote terminal
          response time (RT) or the inter-message gap (IMG) in seconds.
    """


class SearchSearchItemTriggerABusBItemMil1553bTime(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    Properties:
        - ``.lesslimit``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit``
          command.
        - ``.morelimit``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit``
          command.
        - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier``
          command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._lesslimit = SearchSearchItemTriggerABusBItemMil1553bTimeLesslimit(
            device, f"{self._cmd_syntax}:LESSLimit"
        )
        self._morelimit = SearchSearchItemTriggerABusBItemMil1553bTimeMorelimit(
            device, f"{self._cmd_syntax}:MORELimit"
        )
        self._qualifier = SearchSearchItemTriggerABusBItemMil1553bTimeQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )

    @property
    def lesslimit(self) -> SearchSearchItemTriggerABusBItemMil1553bTimeLesslimit:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit`` command.

        Description:
            - When the MIL-STD-1553 bus search condition is set to TIMe, this command specifies
              either the minimum remote terminal response time (RT) limit for the amount of time the
              terminal has to transmit, or it specifies the minimum inter-message gap (IMG). (You
              can specify RT or IMG using the
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:MIL1553B:CONDITION TIMe`` command.) SEARCH<x> is the
              search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies either the minimum remote terminal
              response time (RT) or the inter-message gap (IMG) in seconds.
        """
        return self._lesslimit

    @property
    def morelimit(self) -> SearchSearchItemTriggerABusBItemMil1553bTimeMorelimit:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit`` command.

        Description:
            - When the MIL-STD-1553 bus search condition is set to TIMe, this command specifies
              either the maximum remote terminal response time (RT) limit for the amount of time the
              terminal has to transmit, or it specifies the maximum inter-message gap (IMG). (You
              can specify RT or IMG using the
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:MIL1553B:CONDITION TIMe`` command.) SEARCH<x> is the
              search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit <NR3>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies either the maximum remote terminal
              response time (RT) or the inter-message gap (IMG) in seconds.
        """
        return self._morelimit

    @property
    def qualifier(self) -> SearchSearchItemTriggerABusBItemMil1553bTimeQualifier:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier`` command.

        Description:
            - When the MIL-STD-1553 bus search condition is set to TIMe, this command specifies the
              search data time qualifier. (This includes a smaller set of arguments than other
              qualifier commands.) B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier {LESSthan|MOREthan|INrange|OUTrange}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier?
            ```

        Info:
            - ``LESSthan`` sets the Time qualifier to less than minimum.
            - ``MOREthan`` sets the Time qualifier to greater than maximum.
            - ``INrange`` sets the Time qualifier to inside range.
            - ``OUTrange`` sets the Time qualifier to out of range.
        """  # noqa: E501
        return self._qualifier


class SearchSearchItemTriggerABusBItemMil1553bStatusParity(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity`` command.

    Description:
        - When the MIL-STD-1553 bus search condition is set to STATus, this command specifies the
          status parity bit value to be used in the search. Returned values are 0, 1, or X (don't
          care, which is the default). SEARCH<x> is the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity?
        ```

    Info:
        - ``0``
        - ``1``
        - ``X`` sets the value to X ('don't care') which is the default.
        - ``ZERO`` sets the value to 0.
        - ``ONE`` sets the value to 1.
        - ``NOCARE`` sets the value to X ('don't care') which is the default.
        - ``OFF`` sets the value to 0.
        - ``ON`` sets the value to 1.
    """


class SearchSearchItemTriggerABusBItemMil1553bStatusBitTf(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF`` command.

    Description:
        - When the MIL-STD-1553 bus search condition is set to STATus, this command specifies the
          status word terminal flag bit value (bit 19) to be used in the search. Returned values are
          0, 1, or X (don't care, which is the default). SEARCH<x> is the search number, which is
          always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF?
        ```

    Info:
        - ``0``
        - ``1``
        - ``X`` sets the value to X ('don't care') which is the default.
        - ``ZERO`` sets the value to 0.
        - ``ONE`` sets the value to 1.
        - ``NOCARE`` sets the value to X ('don't care') which is the default.
        - ``OFF`` sets the value to 0.
        - ``ON`` sets the value to 1.
    """


class SearchSearchItemTriggerABusBItemMil1553bStatusBitSubsf(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF`` command.

    Description:
        - When the MIL-STD-1553 bus search condition is set to STATus, this command specifies the
          status word subsystem flag bit value (bit 17) to be used in the search. Returned values
          are 0, 1, or X (don't care, which is the default). SEARCH<x> is the search number, which
          is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF?
        ```

    Info:
        - ``0``
        - ``1``
        - ``X`` sets the value to X ('don't care') which is the default.
        - ``ZERO`` sets the value to 0.
        - ``ONE`` sets the value to 1.
        - ``NOCARE`` sets the value to X ('don't care') which is the default.
        - ``OFF`` sets the value to 0.
        - ``ON`` sets the value to 1.
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemMil1553bStatusBitSrq(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ`` command.

    Description:
        - When the MIL-STD-1553 bus search condition is set to STATus, this command specifies the
          status word service request (SRQ) bit value (bit 11) to be used in the search. Returned
          values are 0, 1, or X (don't care, which is the default). SEARCH<x> is the search number,
          which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ?
        ```
    """


class SearchSearchItemTriggerABusBItemMil1553bStatusBitMe(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME`` command.

    Description:
        - When the MIL-STD-1553 bus search condition is set to STATus, this command specifies the
          status word message error bit value (bit 9) to be used in the search. Returned values are
          0, 1, or X (don't care, which is the default). SEARCH<x> is the search number, which is
          always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME?
        ```

    Info:
        - ``0``
        - ``1``
        - ``X`` sets the value to X ('don't care') which is the default.
        - ``ZERO`` sets the value to 0.
        - ``ONE`` sets the value to 1.
        - ``NOCARE`` sets the value to X ('don't care') which is the default.
        - ``OFF`` sets the value to 0.
        - ``ON`` sets the value to 1.
    """


class SearchSearchItemTriggerABusBItemMil1553bStatusBitInstr(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR`` command.

    Description:
        - When the MIL-STD-1553 bus search condition is set to STATus, this command specifies the
          status word instrumentation bit value (bit 10) to be used in the search. Returned values
          are 0, 1, or X (don't care, which is the default). SEARCH<x> is the search number, which
          is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR?
        ```

    Info:
        - ``0``
        - ``1``
        - ``X`` sets the value to X ('don't care') which is the default.
        - ``ZERO`` sets the value to 0.
        - ``ONE`` sets the value to 1.
        - ``NOCARE`` sets the value to X ('don't care') which is the default.
        - ``OFF`` sets the value to 0.
        - ``ON`` sets the value to 1.
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemMil1553bStatusBitDbca(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA`` command.

    Description:
        - When the MIL-STD-1553 bus search condition is set to STATus, this command specifies the
          status word dynamic bus control acceptance (DBCA) bit value (bit 18) to be used in the
          search. Returned values are 0, 1, or X (don't care, which is the default). SEARCH<x> is
          the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA?
        ```

    Info:
        - ``0``
        - ``1``
        - ``X`` sets the value to X ('don't care') which is the default.
        - ``ZERO`` sets the value to 0.
        - ``ONE`` sets the value to 1.
        - ``NOCARE`` sets the value to X ('don't care') which is the default.
        - ``OFF`` sets the value to 0.
        - ``ON`` sets the value to 1.
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemMil1553bStatusBitBusy(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY`` command.

    Description:
        - When the MIL-STD-1553 bus search condition is set to STATus, this command specifies the
          status word busy bit value (bit 16) to be used in the search. Returned values are 0, 1, or
          X (don't care, which is the default). SEARCH<x> is the search number, which is always 1,
          and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY?
        ```

    Info:
        - ``0``
        - ``1``
        - ``X`` sets the value to X ('don't care') which is the default.
        - ``ZERO`` sets the value to 0.
        - ``ONE`` sets the value to 1.
        - ``NOCARE`` sets the value to X ('don't care') which is the default.
        - ``OFF`` sets the value to 0.
        - ``ON`` sets the value to 1.
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemMil1553bStatusBitBcr(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR`` command.

    Description:
        - When the MIL-STD-1553 bus search condition is set to STATus, this command specifies the
          status word broadcast command received (BCR) bit value (bit 15) to be used in the search.
          SEARCH<x> is the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR?
        ```

    Info:
        - ``0``
        - ``1``
        - ``X`` sets the value to X ('don't care') which is the default.
        - ``ZERO`` sets the value to 0.
        - ``ONE`` sets the value to 1.
        - ``NOCARE`` sets the value to X ('don't care') which is the default.
        - ``OFF`` sets the value to 0.
        - ``ON`` sets the value to 1.
    """


#  pylint: disable=too-many-instance-attributes
class SearchSearchItemTriggerABusBItemMil1553bStatusBit(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bcr``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR`` command.
        - ``.busy``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY`` command.
        - ``.dbca``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA`` command.
        - ``.instr``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR`` command.
        - ``.me``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME`` command.
        - ``.srq``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ`` command.
        - ``.subsf``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF`` command.
        - ``.tf``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bcr = SearchSearchItemTriggerABusBItemMil1553bStatusBitBcr(
            device, f"{self._cmd_syntax}:BCR"
        )
        self._busy = SearchSearchItemTriggerABusBItemMil1553bStatusBitBusy(
            device, f"{self._cmd_syntax}:BUSY"
        )
        self._dbca = SearchSearchItemTriggerABusBItemMil1553bStatusBitDbca(
            device, f"{self._cmd_syntax}:DBCA"
        )
        self._instr = SearchSearchItemTriggerABusBItemMil1553bStatusBitInstr(
            device, f"{self._cmd_syntax}:INSTR"
        )
        self._me = SearchSearchItemTriggerABusBItemMil1553bStatusBitMe(
            device, f"{self._cmd_syntax}:ME"
        )
        self._srq = SearchSearchItemTriggerABusBItemMil1553bStatusBitSrq(
            device, f"{self._cmd_syntax}:SRQ"
        )
        self._subsf = SearchSearchItemTriggerABusBItemMil1553bStatusBitSubsf(
            device, f"{self._cmd_syntax}:SUBSF"
        )
        self._tf = SearchSearchItemTriggerABusBItemMil1553bStatusBitTf(
            device, f"{self._cmd_syntax}:TF"
        )

    @property
    def bcr(self) -> SearchSearchItemTriggerABusBItemMil1553bStatusBitBcr:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR`` command.

        Description:
            - When the MIL-STD-1553 bus search condition is set to STATus, this command specifies
              the status word broadcast command received (BCR) bit value (bit 15) to be used in the
              search. SEARCH<x> is the search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR?
            ```

        Info:
            - ``0``
            - ``1``
            - ``X`` sets the value to X ('don't care') which is the default.
            - ``ZERO`` sets the value to 0.
            - ``ONE`` sets the value to 1.
            - ``NOCARE`` sets the value to X ('don't care') which is the default.
            - ``OFF`` sets the value to 0.
            - ``ON`` sets the value to 1.
        """  # noqa: E501
        return self._bcr

    @property
    def busy(self) -> SearchSearchItemTriggerABusBItemMil1553bStatusBitBusy:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY`` command.

        Description:
            - When the MIL-STD-1553 bus search condition is set to STATus, this command specifies
              the status word busy bit value (bit 16) to be used in the search. Returned values are
              0, 1, or X (don't care, which is the default). SEARCH<x> is the search number, which
              is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY?
            ```

        Info:
            - ``0``
            - ``1``
            - ``X`` sets the value to X ('don't care') which is the default.
            - ``ZERO`` sets the value to 0.
            - ``ONE`` sets the value to 1.
            - ``NOCARE`` sets the value to X ('don't care') which is the default.
            - ``OFF`` sets the value to 0.
            - ``ON`` sets the value to 1.
        """  # noqa: E501
        return self._busy

    @property
    def dbca(self) -> SearchSearchItemTriggerABusBItemMil1553bStatusBitDbca:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA`` command.

        Description:
            - When the MIL-STD-1553 bus search condition is set to STATus, this command specifies
              the status word dynamic bus control acceptance (DBCA) bit value (bit 18) to be used in
              the search. Returned values are 0, 1, or X (don't care, which is the default).
              SEARCH<x> is the search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA?
            ```

        Info:
            - ``0``
            - ``1``
            - ``X`` sets the value to X ('don't care') which is the default.
            - ``ZERO`` sets the value to 0.
            - ``ONE`` sets the value to 1.
            - ``NOCARE`` sets the value to X ('don't care') which is the default.
            - ``OFF`` sets the value to 0.
            - ``ON`` sets the value to 1.
        """  # noqa: E501
        return self._dbca

    @property
    def instr(self) -> SearchSearchItemTriggerABusBItemMil1553bStatusBitInstr:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR`` command.

        Description:
            - When the MIL-STD-1553 bus search condition is set to STATus, this command specifies
              the status word instrumentation bit value (bit 10) to be used in the search. Returned
              values are 0, 1, or X (don't care, which is the default). SEARCH<x> is the search
              number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR?
            ```

        Info:
            - ``0``
            - ``1``
            - ``X`` sets the value to X ('don't care') which is the default.
            - ``ZERO`` sets the value to 0.
            - ``ONE`` sets the value to 1.
            - ``NOCARE`` sets the value to X ('don't care') which is the default.
            - ``OFF`` sets the value to 0.
            - ``ON`` sets the value to 1.
        """  # noqa: E501
        return self._instr

    @property
    def me(self) -> SearchSearchItemTriggerABusBItemMil1553bStatusBitMe:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME`` command.

        Description:
            - When the MIL-STD-1553 bus search condition is set to STATus, this command specifies
              the status word message error bit value (bit 9) to be used in the search. Returned
              values are 0, 1, or X (don't care, which is the default). SEARCH<x> is the search
              number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME?
            ```

        Info:
            - ``0``
            - ``1``
            - ``X`` sets the value to X ('don't care') which is the default.
            - ``ZERO`` sets the value to 0.
            - ``ONE`` sets the value to 1.
            - ``NOCARE`` sets the value to X ('don't care') which is the default.
            - ``OFF`` sets the value to 0.
            - ``ON`` sets the value to 1.
        """  # noqa: E501
        return self._me

    @property
    def srq(self) -> SearchSearchItemTriggerABusBItemMil1553bStatusBitSrq:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ`` command.

        Description:
            - When the MIL-STD-1553 bus search condition is set to STATus, this command specifies
              the status word service request (SRQ) bit value (bit 11) to be used in the search.
              Returned values are 0, 1, or X (don't care, which is the default). SEARCH<x> is the
              search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ?
            ```
        """  # noqa: E501
        return self._srq

    @property
    def subsf(self) -> SearchSearchItemTriggerABusBItemMil1553bStatusBitSubsf:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF`` command.

        Description:
            - When the MIL-STD-1553 bus search condition is set to STATus, this command specifies
              the status word subsystem flag bit value (bit 17) to be used in the search. Returned
              values are 0, 1, or X (don't care, which is the default). SEARCH<x> is the search
              number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF?
            ```

        Info:
            - ``0``
            - ``1``
            - ``X`` sets the value to X ('don't care') which is the default.
            - ``ZERO`` sets the value to 0.
            - ``ONE`` sets the value to 1.
            - ``NOCARE`` sets the value to X ('don't care') which is the default.
            - ``OFF`` sets the value to 0.
            - ``ON`` sets the value to 1.
        """  # noqa: E501
        return self._subsf

    @property
    def tf(self) -> SearchSearchItemTriggerABusBItemMil1553bStatusBitTf:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF`` command.

        Description:
            - When the MIL-STD-1553 bus search condition is set to STATus, this command specifies
              the status word terminal flag bit value (bit 19) to be used in the search. Returned
              values are 0, 1, or X (don't care, which is the default). SEARCH<x> is the search
              number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF?
            ```

        Info:
            - ``0``
            - ``1``
            - ``X`` sets the value to X ('don't care') which is the default.
            - ``ZERO`` sets the value to 0.
            - ``ONE`` sets the value to 1.
            - ``NOCARE`` sets the value to X ('don't care') which is the default.
            - ``OFF`` sets the value to 0.
            - ``ON`` sets the value to 1.
        """  # noqa: E501
        return self._tf


class SearchSearchItemTriggerABusBItemMil1553bStatusAddressValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue`` command.

    Description:
        - When the MIL-STD-1553 bus search condition is set to STATus, and the qualifier is set to
          LESSthan, MOREthan, EQual, UNEQual, LESSEQual or MOREEQual, this command specifies the
          value of the 5-bit remote terminal address to be used in the search. When the MIL-STD-1553
          bus search condition is set to STATus, and the qualifier is set to INrange or OUTrange,
          this command specifies the lower limit of the range. (Use the command
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:MIL1553B:STATUS:ADDRESS:HIVALUE`` to specify the upper
          limit of the range.) The default is all X's (don't care). SEARCH<x> is the search number,
          which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemMil1553bStatusAddressQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier`` command.

    Description:
        - When the MIL-STD-1553 bus search condition is set to STATus, this command specifies the
          qualifier to be used with the address field. SEARCH<x> is the search number, which is
          always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier?
        ```

    Info:
        - ``LESSthan`` sets the Status Address qualifier to less than.
        - ``MOREthan`` sets the Status Address qualifier to greater than.
        - ``EQual`` sets the Status Address qualifier to equal.
        - ``UNEQual`` sets the Status Address qualifier to not equal.
        - ``LESSEQual`` sets the Status Address qualifier to less than or equal.
        - ``MOREEQual`` sets the Status Address qualifier to greater than or equal.
        - ``INrange`` sets the Status Address qualifier to in range.
        - ``OUTrange`` sets the Status Address qualifier to out of range.
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemMil1553bStatusAddressHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue`` command.

    Description:
        - When the MIL-STD-1553 bus search condition is set to STATus, and the qualifier is set to
          INrange or OUTrange, this command specifies the upper limit for the 5 bit remote terminal
          address field of the Status word. (Use the command
          ``TRIGGER:A:BUS:BX:MIL1553B:STATUS:ADDRESS:VALUE`` to specify the lower limit.) The
          default is all X's (don't care). SEARCH<x> is the search number, which is always 1, and
          B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemMil1553bStatusAddress(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue``
          command.
        - ``.qualifier``: The
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier`` command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue``
          command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = SearchSearchItemTriggerABusBItemMil1553bStatusAddressHivalue(
            device, f"{self._cmd_syntax}:HIVALue"
        )
        self._qualifier = SearchSearchItemTriggerABusBItemMil1553bStatusAddressQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._value = SearchSearchItemTriggerABusBItemMil1553bStatusAddressValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def hivalue(self) -> SearchSearchItemTriggerABusBItemMil1553bStatusAddressHivalue:
        """``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue`` command.

        Description:
            - When the MIL-STD-1553 bus search condition is set to STATus, and the qualifier is set
              to INrange or OUTrange, this command specifies the upper limit for the 5 bit remote
              terminal address field of the Status word. (Use the command
              ``TRIGGER:A:BUS:BX:MIL1553B:STATUS:ADDRESS:VALUE`` to specify the lower limit.) The
              default is all X's (don't care). SEARCH<x> is the search number, which is always 1,
              and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue?
            ```
        """
        return self._hivalue

    @property
    def qualifier(self) -> SearchSearchItemTriggerABusBItemMil1553bStatusAddressQualifier:
        """``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier`` command.

        Description:
            - When the MIL-STD-1553 bus search condition is set to STATus, this command specifies
              the qualifier to be used with the address field. SEARCH<x> is the search number, which
              is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier value``
              command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier?
            ```

        Info:
            - ``LESSthan`` sets the Status Address qualifier to less than.
            - ``MOREthan`` sets the Status Address qualifier to greater than.
            - ``EQual`` sets the Status Address qualifier to equal.
            - ``UNEQual`` sets the Status Address qualifier to not equal.
            - ``LESSEQual`` sets the Status Address qualifier to less than or equal.
            - ``MOREEQual`` sets the Status Address qualifier to greater than or equal.
            - ``INrange`` sets the Status Address qualifier to in range.
            - ``OUTrange`` sets the Status Address qualifier to out of range.
        """  # noqa: E501
        return self._qualifier

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemMil1553bStatusAddressValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue`` command.

        Description:
            - When the MIL-STD-1553 bus search condition is set to STATus, and the qualifier is set
              to LESSthan, MOREthan, EQual, UNEQual, LESSEQual or MOREEQual, this command specifies
              the value of the 5-bit remote terminal address to be used in the search. When the
              MIL-STD-1553 bus search condition is set to STATus, and the qualifier is set to
              INrange or OUTrange, this command specifies the lower limit of the range. (Use the
              command ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:MIL1553B:STATUS:ADDRESS:HIVALUE`` to specify
              the upper limit of the range.) The default is all X's (don't care). SEARCH<x> is the
              search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue?
            ```
        """
        return self._value


class SearchSearchItemTriggerABusBItemMil1553bStatus(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    Properties:
        - ``.address``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess`` command
          tree.
        - ``.bit``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT`` command tree.
        - ``.parity``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._address = SearchSearchItemTriggerABusBItemMil1553bStatusAddress(
            device, f"{self._cmd_syntax}:ADDRess"
        )
        self._bit = SearchSearchItemTriggerABusBItemMil1553bStatusBit(
            device, f"{self._cmd_syntax}:BIT"
        )
        self._parity = SearchSearchItemTriggerABusBItemMil1553bStatusParity(
            device, f"{self._cmd_syntax}:PARity"
        )

    @property
    def address(self) -> SearchSearchItemTriggerABusBItemMil1553bStatusAddress:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue`` command.
            - ``.qualifier``: The
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier`` command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue``
              command.
        """
        return self._address

    @property
    def bit(self) -> SearchSearchItemTriggerABusBItemMil1553bStatusBit:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bcr``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR`` command.
            - ``.busy``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY``
              command.
            - ``.dbca``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA``
              command.
            - ``.instr``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR``
              command.
            - ``.me``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME`` command.
            - ``.srq``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ`` command.
            - ``.subsf``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF``
              command.
            - ``.tf``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF`` command.
        """
        return self._bit

    @property
    def parity(self) -> SearchSearchItemTriggerABusBItemMil1553bStatusParity:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity`` command.

        Description:
            - When the MIL-STD-1553 bus search condition is set to STATus, this command specifies
              the status parity bit value to be used in the search. Returned values are 0, 1, or X
              (don't care, which is the default). SEARCH<x> is the search number, which is always 1,
              and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity?
            ```

        Info:
            - ``0``
            - ``1``
            - ``X`` sets the value to X ('don't care') which is the default.
            - ``ZERO`` sets the value to 0.
            - ``ONE`` sets the value to 1.
            - ``NOCARE`` sets the value to X ('don't care') which is the default.
            - ``OFF`` sets the value to 0.
            - ``ON`` sets the value to 1.
        """  # noqa: E501
        return self._parity


class SearchSearchItemTriggerABusBItemMil1553bErrtype(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE`` command.

    Description:
        - When the MIL-STD-1553 bus search condition is set to ERRor, this command specifies the
          signaling error type to be used in the search: Parity, Sync, Manchester or Data. SEARCH<x>
          is the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE {PARity|SYNC|MANCHester|DATA}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE?
        ```
    """


class SearchSearchItemTriggerABusBItemMil1553bDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue`` command.

    Description:
        - When the MIL-STD-1553 bus search condition is set to DATa, this command specifies the data
          binary pattern to be used in the search. This is a 16-bit field. SEARCH<x> is the search
          number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemMil1553bDataParity(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity`` command.

    Description:
        - When the MIL-STD-1553 bus search condition is set to DATa, this command specifies the data
          parity bit to be used in the search. Returned values are 0, 1, or X (don't care).
          SEARCH<x> is the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity?
        ```

    Info:
        - ``0``
        - ``1``
        - ``X`` sets the value to X ('don't care') which is the default.
        - ``ZERO`` sets the value to 0.
        - ``ONE`` sets the value to 1.
        - ``NOCARE`` sets the value to X ('don't care') which is the default.
        - ``OFF`` sets the value to 0.
        - ``ON`` sets the value to 1.
    """


class SearchSearchItemTriggerABusBItemMil1553bData(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    Properties:
        - ``.parity``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity`` command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._parity = SearchSearchItemTriggerABusBItemMil1553bDataParity(
            device, f"{self._cmd_syntax}:PARity"
        )
        self._value = SearchSearchItemTriggerABusBItemMil1553bDataValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def parity(self) -> SearchSearchItemTriggerABusBItemMil1553bDataParity:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity`` command.

        Description:
            - When the MIL-STD-1553 bus search condition is set to DATa, this command specifies the
              data parity bit to be used in the search. Returned values are 0, 1, or X (don't care).
              SEARCH<x> is the search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity?
            ```

        Info:
            - ``0``
            - ``1``
            - ``X`` sets the value to X ('don't care') which is the default.
            - ``ZERO`` sets the value to 0.
            - ``ONE`` sets the value to 1.
            - ``NOCARE`` sets the value to X ('don't care') which is the default.
            - ``OFF`` sets the value to 0.
            - ``ON`` sets the value to 1.
        """  # noqa: E501
        return self._parity

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemMil1553bDataValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue`` command.

        Description:
            - When the MIL-STD-1553 bus search condition is set to DATa, this command specifies the
              data binary pattern to be used in the search. This is a 16-bit field. SEARCH<x> is the
              search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue?
            ```
        """
        return self._value


class SearchSearchItemTriggerABusBItemMil1553bCondition(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:CONDition`` command.

    Description:
        - This command specifies a word type or condition within a MIL-STD-1553 bus word to search
          for. SEARCH<x> is the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:CONDition?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:CONDition value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:CONDition {SYNC|COMMAND|STATus|DATA|TIMe|ERRor}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:CONDition?
        ```

    Info:
        - ``SYNC`` refers to the 3-bit sync pulse that precedes each word.
        - ``COMMAND`` is one of 3 16-bit word types. It specifies the function that a remote
          terminal is to perform.
        - ``STATus`` is one of 3 16-bit word types. Remote terminals respond to valid message
          transmissions via status words.
        - ``DATA`` is one of 3 16-bit word types.
        - ``TIMe`` specifies to search for either the RT (remote terminal response time), or the IMG
          (Inter-message Gap). Use the commands
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:MIL1553B:TIME:QUALIFIER``,
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:MIL1553B:TIME:LESSLIMIT``, and
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:MIL1553B:TIME:MORELIMIT`` to specify the time
          parameters.
        - ``ERRor`` specifies to search for a signaling error. (You can specify which type of error
          - Parity, Sync, Manchester or Non-contiguous Data - by using the command
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:MIL1553B:ERRTYPE``.).
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemMil1553bCommandTrbit(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit`` command.

    Description:
        - When the MIL-STD-1553 bus search condition is set to COMMAND, this command specifies that
          the transmit/receive bit (bit 9) is to be used in the search. The transmit/receive bit
          defines the direction of information flow, and is always from the point of view of the
          remote terminal. SEARCH<x> is the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit {RX|TX|X}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit?
        ```

    Info:
        - ``RX`` (logic 0) directs the instrument to search for a TX or 'transmit' from a remote
          terminal .
        - ``TX`` (logic 1) directs the instrument to search for an RX or 'receive' from a remote
          terminal.
        - ``X`` indicates 'don't care'.
    """


class SearchSearchItemTriggerABusBItemMil1553bCommandSubaddress(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress`` command.

    Description:
        - When the MIL-STD-1553 bus search condition is set to COMMAND, this command specifies the 5
          bit sub-address that is to be used in the search. When the sub-address value is set to
          00000 or 11111 binary, it specifies that the command is a 'Mode Code' command. Any other
          value specifies that it is a 'Word Count' command. The default is all X's (don't care).
          SEARCH<x> is the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemMil1553bCommandParity(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity`` command.

    Description:
        - When the MIL-STD-1553 bus search condition is set to COMMAND, this command specifies the
          Command word parity that is to be used in the search. SEARCH<x> is the search number,
          which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity?
        ```

    Info:
        - ``0``
        - ``1``
        - ``X`` sets the value to X ('don't care') which is the default.
        - ``ZERO`` sets the value to 0.
        - ``ONE`` sets the value to 1.
        - ``NOCARE`` sets the value to X ('don't care') which is the default.
        - ``OFF`` sets the value to 0.
        - ``ON`` sets the value to 1.
    """


class SearchSearchItemTriggerABusBItemMil1553bCommandCount(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt`` command.

    Description:
        - When the MIL-STD-1553 bus search condition is set to COMMAND, this command specifies the
          bit pattern for the 5-bit Word Count/Mode Code sub-address field that is to be used in the
          search. (Use the ``commandSEARCH:SEARCHX:TRIGGER:A:BUS:BX:MIL1553B:COMMAND:SUBADDRESS`` to
          specify Word Count or Mode Code.) In Word Count mode, this field defines the number of
          data words that is to be transmitted, or received, depending on the T/R bit setting. (Use
          the ``commandSEARCH:SEARCHX:TRIGGER:A:BUS:BX:MIL1553B:COMMAND:TRBIT`` to set the T/R bit.)
          A word count value of 0 actually indicates a transfer of 32 data words. SEARCH<x> is the
          search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt?
        ```

    Info:
        - ``QString`` is a quoted string of up to 5 characters, where the allowable characters are
          0, 1 and X.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemMil1553bCommandAddressValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue`` command.

    Description:
        - When the MIL-STD-1553 bus search condition is set to COMMAND, and the qualifier is set to
          LESSthan, MOREthan, EQual, UNEQual, LESSEQual or MOREEQual, this command specifies the
          value of the 5-bit remote terminal address to be used in the search. When the MIL-STD-1553
          bus search condition is set to COMMAND, and the qualifier is set to INrange or OUTrange,
          this command specifies the lower limit of the remote terminal address range. The default
          is all X's (don't care). SEARCH<x> is the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemMil1553bCommandAddressHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue`` command.

    Description:
        - When the MIL-STD-1553 bus search condition is set to COMMAND, and the qualifier is set to
          INrange or OUTrange, this command specifies the upper limit of the range for the remote
          terminal address field. (Use the command
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:MIL1553B:COMMAND:ADDRESS:VALUE`` to specify the lower
          limit of the range.) SEARCH<x> is the search number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemMil1553bCommandAddress(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue``
          command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue``
          command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = SearchSearchItemTriggerABusBItemMil1553bCommandAddressHivalue(
            device, f"{self._cmd_syntax}:HIVALue"
        )
        self._value = SearchSearchItemTriggerABusBItemMil1553bCommandAddressValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def hivalue(self) -> SearchSearchItemTriggerABusBItemMil1553bCommandAddressHivalue:
        """``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue`` command.

        Description:
            - When the MIL-STD-1553 bus search condition is set to COMMAND, and the qualifier is set
              to INrange or OUTrange, this command specifies the upper limit of the range for the
              remote terminal address field. (Use the command
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:MIL1553B:COMMAND:ADDRESS:VALUE`` to specify the
              lower limit of the range.) SEARCH<x> is the search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue value``
              command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue?
            ```
        """
        return self._hivalue

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemMil1553bCommandAddressValue:
        """``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue`` command.

        Description:
            - When the MIL-STD-1553 bus search condition is set to COMMAND, and the qualifier is set
              to LESSthan, MOREthan, EQual, UNEQual, LESSEQual or MOREEQual, this command specifies
              the value of the 5-bit remote terminal address to be used in the search. When the
              MIL-STD-1553 bus search condition is set to COMMAND, and the qualifier is set to
              INrange or OUTrange, this command specifies the lower limit of the remote terminal
              address range. The default is all X's (don't care). SEARCH<x> is the search number,
              which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue?
            ```
        """
        return self._value


class SearchSearchItemTriggerABusBItemMil1553bCommand(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.address``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess`` command
          tree.
        - ``.count``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt`` command.
        - ``.parity``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity`` command.
        - ``.subaddress``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress``
          command.
        - ``.trbit``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._address = SearchSearchItemTriggerABusBItemMil1553bCommandAddress(
            device, f"{self._cmd_syntax}:ADDRess"
        )
        self._count = SearchSearchItemTriggerABusBItemMil1553bCommandCount(
            device, f"{self._cmd_syntax}:COUNt"
        )
        self._parity = SearchSearchItemTriggerABusBItemMil1553bCommandParity(
            device, f"{self._cmd_syntax}:PARity"
        )
        self._subaddress = SearchSearchItemTriggerABusBItemMil1553bCommandSubaddress(
            device, f"{self._cmd_syntax}:SUBADdress"
        )
        self._trbit = SearchSearchItemTriggerABusBItemMil1553bCommandTrbit(
            device, f"{self._cmd_syntax}:TRBit"
        )

    @property
    def address(self) -> SearchSearchItemTriggerABusBItemMil1553bCommandAddress:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue`` command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue``
              command.
        """
        return self._address

    @property
    def count(self) -> SearchSearchItemTriggerABusBItemMil1553bCommandCount:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt`` command.

        Description:
            - When the MIL-STD-1553 bus search condition is set to COMMAND, this command specifies
              the bit pattern for the 5-bit Word Count/Mode Code sub-address field that is to be
              used in the search. (Use the
              ``commandSEARCH:SEARCHX:TRIGGER:A:BUS:BX:MIL1553B:COMMAND:SUBADDRESS`` to specify Word
              Count or Mode Code.) In Word Count mode, this field defines the number of data words
              that is to be transmitted, or received, depending on the T/R bit setting. (Use the
              ``commandSEARCH:SEARCHX:TRIGGER:A:BUS:BX:MIL1553B:COMMAND:TRBIT`` to set the T/R bit.)
              A word count value of 0 actually indicates a transfer of 32 data words. SEARCH<x> is
              the search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt?
            ```

        Info:
            - ``QString`` is a quoted string of up to 5 characters, where the allowable characters
              are 0, 1 and X.
        """
        return self._count

    @property
    def parity(self) -> SearchSearchItemTriggerABusBItemMil1553bCommandParity:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity`` command.

        Description:
            - When the MIL-STD-1553 bus search condition is set to COMMAND, this command specifies
              the Command word parity that is to be used in the search. SEARCH<x> is the search
              number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity?
            ```

        Info:
            - ``0``
            - ``1``
            - ``X`` sets the value to X ('don't care') which is the default.
            - ``ZERO`` sets the value to 0.
            - ``ONE`` sets the value to 1.
            - ``NOCARE`` sets the value to X ('don't care') which is the default.
            - ``OFF`` sets the value to 0.
            - ``ON`` sets the value to 1.
        """  # noqa: E501
        return self._parity

    @property
    def subaddress(self) -> SearchSearchItemTriggerABusBItemMil1553bCommandSubaddress:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress`` command.

        Description:
            - When the MIL-STD-1553 bus search condition is set to COMMAND, this command specifies
              the 5 bit sub-address that is to be used in the search. When the sub-address value is
              set to 00000 or 11111 binary, it specifies that the command is a 'Mode Code' command.
              Any other value specifies that it is a 'Word Count' command. The default is all X's
              (don't care). SEARCH<x> is the search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress?
            ```
        """
        return self._subaddress

    @property
    def trbit(self) -> SearchSearchItemTriggerABusBItemMil1553bCommandTrbit:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit`` command.

        Description:
            - When the MIL-STD-1553 bus search condition is set to COMMAND, this command specifies
              that the transmit/receive bit (bit 9) is to be used in the search. The
              transmit/receive bit defines the direction of information flow, and is always from the
              point of view of the remote terminal. SEARCH<x> is the search number, which is always
              1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit {RX|TX|X}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit?
            ```

        Info:
            - ``RX`` (logic 0) directs the instrument to search for a TX or 'transmit' from a remote
              terminal .
            - ``TX`` (logic 1) directs the instrument to search for an RX or 'receive' from a remote
              terminal.
            - ``X`` indicates 'don't care'.
        """
        return self._trbit


class SearchSearchItemTriggerABusBItemMil1553b(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.command``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND`` command tree.
        - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:CONDition`` command.
        - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa`` command tree.
        - ``.errtype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE`` command.
        - ``.status``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus`` command tree.
        - ``.time``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._command = SearchSearchItemTriggerABusBItemMil1553bCommand(
            device, f"{self._cmd_syntax}:COMMAND"
        )
        self._condition = SearchSearchItemTriggerABusBItemMil1553bCondition(
            device, f"{self._cmd_syntax}:CONDition"
        )
        self._data = SearchSearchItemTriggerABusBItemMil1553bData(
            device, f"{self._cmd_syntax}:DATa"
        )
        self._errtype = SearchSearchItemTriggerABusBItemMil1553bErrtype(
            device, f"{self._cmd_syntax}:ERRTYPE"
        )
        self._status = SearchSearchItemTriggerABusBItemMil1553bStatus(
            device, f"{self._cmd_syntax}:STATus"
        )
        self._time = SearchSearchItemTriggerABusBItemMil1553bTime(
            device, f"{self._cmd_syntax}:TIMe"
        )

    @property
    def command(self) -> SearchSearchItemTriggerABusBItemMil1553bCommand:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.address``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess``
              command tree.
            - ``.count``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt``
              command.
            - ``.parity``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity``
              command.
            - ``.subaddress``: The
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress`` command.
            - ``.trbit``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit``
              command.
        """
        return self._command

    @property
    def condition(self) -> SearchSearchItemTriggerABusBItemMil1553bCondition:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:CONDition`` command.

        Description:
            - This command specifies a word type or condition within a MIL-STD-1553 bus word to
              search for. SEARCH<x> is the search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:CONDition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:CONDition?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:CONDition value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:CONDition {SYNC|COMMAND|STATus|DATA|TIMe|ERRor}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:CONDition?
            ```

        Info:
            - ``SYNC`` refers to the 3-bit sync pulse that precedes each word.
            - ``COMMAND`` is one of 3 16-bit word types. It specifies the function that a remote
              terminal is to perform.
            - ``STATus`` is one of 3 16-bit word types. Remote terminals respond to valid message
              transmissions via status words.
            - ``DATA`` is one of 3 16-bit word types.
            - ``TIMe`` specifies to search for either the RT (remote terminal response time), or the
              IMG (Inter-message Gap). Use the commands
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:MIL1553B:TIME:QUALIFIER``,
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:MIL1553B:TIME:LESSLIMIT``, and
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:MIL1553B:TIME:MORELIMIT`` to specify the time
              parameters.
            - ``ERRor`` specifies to search for a signaling error. (You can specify which type of
              error - Parity, Sync, Manchester or Non-contiguous Data - by using the command
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:MIL1553B:ERRTYPE``.).
        """  # noqa: E501
        return self._condition

    @property
    def data(self) -> SearchSearchItemTriggerABusBItemMil1553bData:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.parity``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity`` command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue`` command.
        """
        return self._data

    @property
    def errtype(self) -> SearchSearchItemTriggerABusBItemMil1553bErrtype:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE`` command.

        Description:
            - When the MIL-STD-1553 bus search condition is set to ERRor, this command specifies the
              signaling error type to be used in the search: Parity, Sync, Manchester or Data.
              SEARCH<x> is the search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE {PARity|SYNC|MANCHester|DATA}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE?
            ```
        """
        return self._errtype

    @property
    def status(self) -> SearchSearchItemTriggerABusBItemMil1553bStatus:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.address``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess``
              command tree.
            - ``.bit``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT`` command
              tree.
            - ``.parity``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity``
              command.
        """
        return self._status

    @property
    def time(self) -> SearchSearchItemTriggerABusBItemMil1553bTime:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.lesslimit``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit``
              command.
            - ``.morelimit``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit``
              command.
            - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier``
              command.
        """
        return self._time


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
        - This command specifies the error type used for a LIN search. SEARCH<x> is the search
          number, which is always 1, and B<x>

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
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:ERRTYPE {SYNC|PARity|CHecksum|HEADertime|RESPtime|FRAMetime}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:ERRTYPE?
        ```

    Info:
        - ``SYNC`` specifies a sync error type.
        - ``PARity`` specifies a parity error type.
        - ``CHecksum`` specifies a checksum error type.
        - ``HEADertime`` specifies a header time error type.
        - ``RESPtime`` specifies a response time error type.
        - ``RAMetime`` specifies a frame time error type.
    """  # noqa: E501


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
        - This command specifies the LIN data qualifier. This only applies if the search condition
          is set to IDentifier or IDANDDATA (identifier and data). SEARCH<x> is the search number,
          which is always 1, and B<x>

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
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?
        ```

    Info:
        - ``LESSthan`` sets the LIN data qualifier to less than.
        - ``MOREthan`` sets the LIN data qualifier to greater than.
        - ``EQual`` sets the LIN data qualifier to equal.
        - ``UNEQual`` sets the LIN data qualifier to not equal.
        - ``LESSEQual`` sets the LIN data qualifier to less than or equal.
        - ``MOREEQual`` sets the LIN data qualifier to greater than or equal.
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
            - This command specifies the LIN data qualifier. This only applies if the search
              condition is set to IDentifier or IDANDDATA (identifier and data). SEARCH<x> is the
              search number, which is always 1, and B<x>

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
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?
            ```

        Info:
            - ``LESSthan`` sets the LIN data qualifier to less than.
            - ``MOREthan`` sets the LIN data qualifier to greater than.
            - ``EQual`` sets the LIN data qualifier to equal.
            - ``UNEQual`` sets the LIN data qualifier to not equal.
            - ``LESSEQual`` sets the LIN data qualifier to less than or equal.
            - ``MOREEQual`` sets the LIN data qualifier to greater than or equal.
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
            - This command specifies the error type used for a LIN search. SEARCH<x> is the search
              number, which is always 1, and B<x>

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
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:ERRTYPE {SYNC|PARity|CHecksum|HEADertime|RESPtime|FRAMetime}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN:ERRTYPE?
            ```

        Info:
            - ``SYNC`` specifies a sync error type.
            - ``PARity`` specifies a parity error type.
            - ``CHecksum`` specifies a checksum error type.
            - ``HEADertime`` specifies a header time error type.
            - ``RESPtime`` specifies a response time error type.
            - ``RAMetime`` specifies a frame time error type.
        """  # noqa: E501
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
        - This command specifies the qualifier to use when searching on the FlexRay bus frame ID
          field. The search condition needs to be set to IDentifier (using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search number,
          which is always 1, and B<x>

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
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier?
        ```

    Info:
        - ``LESSthan`` sets the frame ID qualifier to less than.
        - ``MOREthan`` sets the frame ID qualifier to more than.
        - ``EQual`` sets the frame ID qualifier to equal.
        - ``UNEQual`` sets the frame ID qualifier to unequal.
        - ``LESSEQual`` sets the frame ID qualifier to less than or equal.
        - ``MOREEQual`` sets the frame ID qualifier to greater than or equal.
        - ``INrange`` sets the frame ID qualifier to in range.
        - ``OUTrange`` sets the frame ID qualifier to outside of range.
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
            - This command specifies the qualifier to use when searching on the FlexRay bus frame ID
              field. The search condition needs to be set to IDentifier (using
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is the search
              number, which is always 1, and B<x>

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
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier?
            ```

        Info:
            - ``LESSthan`` sets the frame ID qualifier to less than.
            - ``MOREthan`` sets the frame ID qualifier to more than.
            - ``EQual`` sets the frame ID qualifier to equal.
            - ``UNEQual`` sets the frame ID qualifier to unequal.
            - ``LESSEQual`` sets the frame ID qualifier to less than or equal.
            - ``MOREEQual`` sets the frame ID qualifier to greater than or equal.
            - ``INrange`` sets the frame ID qualifier to in range.
            - ``OUTrange`` sets the frame ID qualifier to outside of range.
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
        - This command specifies the qualifier (<, >, =, <=, >=, not =, in range, out of range) to
          use when searching on the FlexRay bus data field. The search condition needs to be set to
          ID or IDANDDATA (using ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x>
          is the search number, which is always 1, and B<x>

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
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier?
        ```

    Info:
        - ``LESSthan`` sets the data qualifier to less than.
        - ``MOREthan`` sets the data qualifier to greater than.
        - ``EQual`` sets the data qualifier to equal.
        - ``UNEQual`` sets the data qualifier to not equal.
        - ``LESSEQual`` sets the data qualifier to less than or equal.
        - ``MOREEQual`` sets the data qualifier to greater than or equal.
        - ``INrange`` sets the data qualifier to in range.
        - ``OUTrange`` sets the data qualifier to out of range.
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
            - This command specifies the qualifier (<, >, =, <=, >=, not =, in range, out of range)
              to use when searching on the FlexRay bus data field. The search condition needs to be
              set to ID or IDANDDATA (using ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``).
              SEARCH<x> is the search number, which is always 1, and B<x>

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
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier?
            ```

        Info:
            - ``LESSthan`` sets the data qualifier to less than.
            - ``MOREthan`` sets the data qualifier to greater than.
            - ``EQual`` sets the data qualifier to equal.
            - ``UNEQual`` sets the data qualifier to not equal.
            - ``LESSEQual`` sets the data qualifier to less than or equal.
            - ``MOREEQual`` sets the data qualifier to greater than or equal.
            - ``INrange`` sets the data qualifier to in range.
            - ``OUTrange`` sets the data qualifier to out of range.
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
        - This command specifies the qualifier (<, >, =, <=, >=, not =, in range, out of range) to
          use when searching on the FlexRay bus cycle count field. The search condition must be set
          to CYCLEcount (using ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). SEARCH<x> is
          the search number, which is always 1, and B<x>

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
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
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
            - This command specifies the qualifier (<, >, =, <=, >=, not =, in range, out of range)
              to use when searching on the FlexRay bus cycle count field. The search condition must
              be set to CYCLEcount (using ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``).
              SEARCH<x> is the search number, which is always 1, and B<x>

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
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
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


class SearchSearchItemTriggerABusBItemEthernetFrametype(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe`` command.

    Description:
        - This command specifies which Ethernet frame type to search for: either Basic or QTAG (IEEE
          802.1Q, or VLAN tagging). The default is Basic. SEARCH<x> is the search number, which is
          always 1, and B<x> is the bus number 1-2.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe {BASic|QTAG}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe?
        ```

    Info:
        - ``BASic`` is the standard Ethernet frame.
        - ``QTAG`` is the Q-Tag Ethernet frame (also called VLAN tagging.).
    """


class SearchSearchItemTriggerABusBItemEthernetDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue`` command.

    Description:
        - When the search condition is set to DATa, and the qualifier is set to LESSthan, MOREthan,
          EQual, UNEQual, LESSEQual or MOREEQual, this command specifies the value to search for.
          When the search condition is set to DATa, and the qualifier is set to INrange or OUTrange,
          this command specifies the lower limit of the range. (Use the command
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:ETHERNET:DATA:HIVALUE`` to specify the upper limit of
          the range.) The default is all X's (don't care). SEARCH<x> is the search number, which is
          always 1, and B<x> is the bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue?
        ```

    Info:
        - ``QString`` is a quoted string where the allowable characters are 0, 1, and X. The
          allowable number of characters depends on the setting for size. (Use the command
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:ETHERNET:DATA:SIZE`` to specify size.) The bits
          specified in the quoted string replace the least significant bits, leaving any unspecified
          upper bits unchanged.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemEthernetData(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:DATa?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:DATa?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = SearchSearchItemTriggerABusBItemEthernetDataValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemEthernetDataValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue`` command.

        Description:
            - When the search condition is set to DATa, and the qualifier is set to LESSthan,
              MOREthan, EQual, UNEQual, LESSEQual or MOREEQual, this command specifies the value to
              search for. When the search condition is set to DATa, and the qualifier is set to
              INrange or OUTrange, this command specifies the lower limit of the range. (Use the
              command ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:ETHERNET:DATA:HIVALUE`` to specify the upper
              limit of the range.) The default is all X's (don't care). SEARCH<x> is the search
              number, which is always 1, and B<x> is the bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue?
            ```

        Info:
            - ``QString`` is a quoted string where the allowable characters are 0, 1, and X. The
              allowable number of characters depends on the setting for size. (Use the command
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:ETHERNET:DATA:SIZE`` to specify size.) The bits
              specified in the quoted string replace the least significant bits, leaving any
              unspecified upper bits unchanged.
        """
        return self._value


class SearchSearchItemTriggerABusBItemEthernet(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:DATa`` command tree.
        - ``.frametype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._data = SearchSearchItemTriggerABusBItemEthernetData(
            device, f"{self._cmd_syntax}:DATa"
        )
        self._frametype = SearchSearchItemTriggerABusBItemEthernetFrametype(
            device, f"{self._cmd_syntax}:FRAMETYPe"
        )

    @property
    def data(self) -> SearchSearchItemTriggerABusBItemEthernetData:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:DATa?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:DATa?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue`` command.
        """
        return self._data

    @property
    def frametype(self) -> SearchSearchItemTriggerABusBItemEthernetFrametype:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe`` command.

        Description:
            - This command specifies which Ethernet frame type to search for: either Basic or QTAG
              (IEEE 802.1Q, or VLAN tagging). The default is Basic. SEARCH<x> is the search number,
              which is always 1, and B<x> is the bus number 1-2.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe {BASic|QTAG}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe?
            ```

        Info:
            - ``BASic`` is the standard Ethernet frame.
            - ``QTAG`` is the Q-Tag Ethernet frame (also called VLAN tagging.).
        """
        return self._frametype


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
        - This command sets the addressing mode (standard or extended format) to be used to search
          on CAN bus data. This only applies if the search condition has been set to IDANDDATA or
          DATA (using ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:CONDITION``). SEARCH<x> is the search
          number, which is always 1, and B<x> is the bus number (1-2).

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
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe {STandard|EXTENDed}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?
        ```

    Info:
        - ``STandard`` specifies an 11-bit identifier field.
        - ``EXTENDed`` specifies a 29-bit identifier field.
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
            - This command sets the addressing mode (standard or extended format) to be used to
              search on CAN bus data. This only applies if the search condition has been set to
              IDANDDATA or DATA (using ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:CONDITION``). SEARCH<x>
              is the search number, which is always 1, and B<x> is the bus number (1-2).

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
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe {STandard|EXTENDed}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?
            ```

        Info:
            - ``STandard`` specifies an 11-bit identifier field.
            - ``EXTENDed`` specifies a 29-bit identifier field.
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


class SearchSearchItemTriggerABusBItemCanFdEsibit(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT`` command.

    Description:
        - This command specifies the binary data value to be used to search on CAN FD ESI bits. This
          only applies if the search condition has been set to FDESIBIT (using
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:CONDition`` ). ``SEARCH:<x>`` is the search
          number, which is always 1, and B<x> is the bus number (1-2).

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT {ZERo|OFF|0|ONE|ON|1|NOCARE|X|x}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT?
        ```

    Info:
        - ``ZERo`` , OFF, and 0 specify that the BRS bit must have value 0. If queried, the command
          will always return 0 if set with these arguments.
        - ``ONE`` , ON, and 1 specify that the BRS bit must have value 1. If queried, the command
          will always return 1 if set with these arguments.
        - ``NOCARE`` , X, and x specify that the BRS bit may be either 1 or 0. If queried, the
          command will always return X if set with these arguments.
    """


class SearchSearchItemTriggerABusBItemCanFdBrsbit(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT`` command.

    Description:
        - This command specifies the binary data value to be used to search on CAN FD BRS bits. This
          only applies if the search condition has been set to FDBRSBIT (using
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:CONDition`` ). ``SEARCH:<x>`` is the search
          number, which is always 1, and B<x> is the bus number (1-2).

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT {ZERo|OFF|0|ONE|ON|1|NOCARE|X|x}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT?
        ```

    Info:
        - ``ZERo`` , OFF, and 0 specify that the BRS bit must have value 0. If queried, the command
          will always return 0 if set with these arguments.
        - ``ONE`` , ON, and 1 specify that the BRS bit must have value 1. If queried, the command
          will always return 1 if set with these arguments.
        - ``NOCARE`` , X, and x specify that the BRS bit may be either 1 or 0. If queried, the
          command will always return X if set with these arguments.
    """


class SearchSearchItemTriggerABusBItemCanFd(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.brsbit``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT`` command.
        - ``.esibit``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._brsbit = SearchSearchItemTriggerABusBItemCanFdBrsbit(
            device, f"{self._cmd_syntax}:BRSBIT"
        )
        self._esibit = SearchSearchItemTriggerABusBItemCanFdEsibit(
            device, f"{self._cmd_syntax}:ESIBIT"
        )

    @property
    def brsbit(self) -> SearchSearchItemTriggerABusBItemCanFdBrsbit:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT`` command.

        Description:
            - This command specifies the binary data value to be used to search on CAN FD BRS bits.
              This only applies if the search condition has been set to FDBRSBIT (using
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:CONDition`` ). ``SEARCH:<x>`` is the search
              number, which is always 1, and B<x> is the bus number (1-2).

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT {ZERo|OFF|0|ONE|ON|1|NOCARE|X|x}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT?
            ```

        Info:
            - ``ZERo`` , OFF, and 0 specify that the BRS bit must have value 0. If queried, the
              command will always return 0 if set with these arguments.
            - ``ONE`` , ON, and 1 specify that the BRS bit must have value 1. If queried, the
              command will always return 1 if set with these arguments.
            - ``NOCARE`` , X, and x specify that the BRS bit may be either 1 or 0. If queried, the
              command will always return X if set with these arguments.
        """
        return self._brsbit

    @property
    def esibit(self) -> SearchSearchItemTriggerABusBItemCanFdEsibit:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT`` command.

        Description:
            - This command specifies the binary data value to be used to search on CAN FD ESI bits.
              This only applies if the search condition has been set to FDESIBIT (using
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:CONDition`` ). ``SEARCH:<x>`` is the search
              number, which is always 1, and B<x> is the bus number (1-2).

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT {ZERo|OFF|0|ONE|ON|1|NOCARE|X|x}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT?
            ```

        Info:
            - ``ZERo`` , OFF, and 0 specify that the BRS bit must have value 0. If queried, the
              command will always return 0 if set with these arguments.
            - ``ONE`` , ON, and 1 specify that the BRS bit must have value 1. If queried, the
              command will always return 1 if set with these arguments.
            - ``NOCARE`` , X, and x specify that the BRS bit may be either 1 or 0. If queried, the
              command will always return X if set with these arguments.
        """
        return self._esibit


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
        - This command sets the qualifier (<, >, =, not =, <=) to be used to search on CAN bus data.
          This only applies if the search condition has been set to IDANDDATA or DATA (using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:CONDITION``). SEARCH<x> is the search number, which
          is always 1, and B<x> is the bus number (1-2).

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
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?
        ```

    Info:
        - ``LESSthan`` searches for bus data less than the value specified by
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:DATA:VALUE``.
        - ``MOREthan`` searches for bus data greater than the value specified by
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:DATA:VALUE``.
        - ``EQual`` searches for bus data equal to the value specified by
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:DATA:VALUE``.
        - ``UNEQual`` searches for bus data not equal to the value specified by
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:DATA:VALUE``.
        - ``LESSEQual`` searches for bus data less equal to the value specified by
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:DATA:VALUE``.
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemCanDataOffset(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet`` command.

    Description:
        - This command specifies the data offset in bytes to search for in a CAN search. The default
          value is 0. SEARCH<x> is the search number, which is always 1, and B<x> is the bus number
          (1-2).

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet <NR1>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet?
        ```

    Info:
        - ``<NR1>`` is a number specifying the data offset. It can be set to -1 to 7 for CAN 2.0 and
          -1 to 63 for CAN FD. These ranges are modified by the following.
    """


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
        - ``.offset``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet`` command.
        - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier`` command.
        - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:SIZe`` command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._direction = SearchSearchItemTriggerABusBItemCanDataDirection(
            device, f"{self._cmd_syntax}:DIRection"
        )
        self._offset = SearchSearchItemTriggerABusBItemCanDataOffset(
            device, f"{self._cmd_syntax}:OFFSet"
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
    def offset(self) -> SearchSearchItemTriggerABusBItemCanDataOffset:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet`` command.

        Description:
            - This command specifies the data offset in bytes to search for in a CAN search. The
              default value is 0. SEARCH<x> is the search number, which is always 1, and B<x> is the
              bus number (1-2).

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet <NR1>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet?
            ```

        Info:
            - ``<NR1>`` is a number specifying the data offset. It can be set to -1 to 7 for CAN 2.0
              and -1 to 63 for CAN FD. These ranges are modified by the following.
        """
        return self._offset

    @property
    def qualifier(self) -> SearchSearchItemTriggerABusBItemCanDataQualifier:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier`` command.

        Description:
            - This command sets the qualifier (<, >, =, not =, <=) to be used to search on CAN bus
              data. This only applies if the search condition has been set to IDANDDATA or DATA
              (using ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:CONDITION``). SEARCH<x> is the search
              number, which is always 1, and B<x> is the bus number (1-2).

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
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?
            ```

        Info:
            - ``LESSthan`` searches for bus data less than the value specified by
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:DATA:VALUE``.
            - ``MOREthan`` searches for bus data greater than the value specified by
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:DATA:VALUE``.
            - ``EQual`` searches for bus data equal to the value specified by
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:DATA:VALUE``.
            - ``UNEQual`` searches for bus data not equal to the value specified by
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:DATA:VALUE``.
            - ``LESSEQual`` searches for bus data less equal to the value specified by
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
        - This command sets the condition (start of frame, frame type, identifier, matching data,
          end of frame, missing ACK field, bit-stuffing error, form error, any error, CAN FD BRS
          bit, or CAN FD ESI bit) to be used to search on CAN bus data. SEARCH<x> is the search
          number, which is always 1, and B<x> is the bus number (1-2).

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
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:CONDition {SOF|FRAMEtype|IDentifier|DATA|IDANDDATA|EOF|ACKMISS|ERROR|FORMERRor|ANYERRor|FDBRS|FDESI}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:CONDition?
        ```

    Info:
        - ``SOF`` specifies a search based on the start of frame.
        - ``FRAMEtype`` specifies a search based on the frame type.
        - ``IDentifier`` specifies a search based on the frame identifier.
        - ``DATA`` specifies a search based on the frame data.
        - ``IDANDDATA`` specifies a search based on the frame identifier and data.
        - ``EOF`` specifies a search based on the end of frame.
        - ``ACKMISS`` specifies a search based on the missing ACK field.
        - ``ERROR`` specifies a search based on bit stuffing errors.
        - ``FORMERRor`` specifies a search based on packet form errors.
        - ``ANYERRor`` specifies a search based on matching any packet error (missing ACK, or form
          error).
        - ``FDBRS`` specifies a search based on a CAN FD frame's BRS bit.
        - ``FDESI`` specifies a search based on a CAN FD frame's ESI bit.
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
        - This command sets the addressing mode (standard or extended format) to be used to search
          on CAN bus data. This only applies if the search condition has been set to IDANDDATA or
          DATA (using ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:CONDITION``). SEARCH<x> is the search
          number, which is always 1, and B<x> is the bus number (1-2).

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
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe {STandard|EXTENDed}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe?
        ```

    Info:
        - ``STandard`` specifies an 11-bit identifier field.
        - ``EXTENDed`` specifies a 29-bit identifier field.
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
            - This command sets the addressing mode (standard or extended format) to be used to
              search on CAN bus data. This only applies if the search condition has been set to
              IDANDDATA or DATA (using ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:CAN:CONDITION``). SEARCH<x>
              is the search number, which is always 1, and B<x> is the bus number (1-2).

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
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe {STandard|EXTENDed}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe?
            ```

        Info:
            - ``STandard`` specifies an 11-bit identifier field.
            - ``EXTENDed`` specifies a 29-bit identifier field.
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
        - ``.fd``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD`` command tree.
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
        self._fd = SearchSearchItemTriggerABusBItemCanFd(device, f"{self._cmd_syntax}:FD")
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
            - This command sets the condition (start of frame, frame type, identifier, matching
              data, end of frame, missing ACK field, bit-stuffing error, form error, any error, CAN
              FD BRS bit, or CAN FD ESI bit) to be used to search on CAN bus data. SEARCH<x> is the
              search number, which is always 1, and B<x> is the bus number (1-2).

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
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:CONDition {SOF|FRAMEtype|IDentifier|DATA|IDANDDATA|EOF|ACKMISS|ERROR|FORMERRor|ANYERRor|FDBRS|FDESI}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:CONDition?
            ```

        Info:
            - ``SOF`` specifies a search based on the start of frame.
            - ``FRAMEtype`` specifies a search based on the frame type.
            - ``IDentifier`` specifies a search based on the frame identifier.
            - ``DATA`` specifies a search based on the frame data.
            - ``IDANDDATA`` specifies a search based on the frame identifier and data.
            - ``EOF`` specifies a search based on the end of frame.
            - ``ACKMISS`` specifies a search based on the missing ACK field.
            - ``ERROR`` specifies a search based on bit stuffing errors.
            - ``FORMERRor`` specifies a search based on packet form errors.
            - ``ANYERRor`` specifies a search based on matching any packet error (missing ACK, or
              form error).
            - ``FDBRS`` specifies a search based on a CAN FD frame's BRS bit.
            - ``FDESI`` specifies a search based on a CAN FD frame's ESI bit.
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
            - ``.offset``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet`` command.
            - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier``
              command.
            - ``.size``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:SIZe`` command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:DATa:VALue`` command.
        """
        return self._data

    @property
    def fd(self) -> SearchSearchItemTriggerABusBItemCanFd:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.brsbit``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT`` command.
            - ``.esibit``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT`` command.
        """
        return self._fd

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


class SearchSearchItemTriggerABusBItemAudioDataWord(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:WORD`` command.

    Description:
        - This command sets the alignment of the data (left, right or either) to be used to search
          on audio bus data. The search condition must be set to DATA using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:AUDIO:CONDITION``. SEARCH<x> is the search number, which
          is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:WORD?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:WORD?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:WORD value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:WORD {EITher|LEFt|RIGht}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:WORD?
        ```

    Info:
        - ``EITher`` aligns the data to either left or right.
        - ``LEFt`` aligns the data to the left.
        - ``RIGht`` aligns the data to the right.
    """


class SearchSearchItemTriggerABusBItemAudioDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:VALue`` command.

    Description:
        - This command sets the lower word value to be used to search on audio bus data. (Use
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:AUDIO:DATA:HIVALUE`` to set the upper word value.) The
          search condition must be set to DATA using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:AUDIO:CONDITION``. SEARCH<x> is the search number, which
          is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:VALue <String>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:VALue?
        ```
    """


class SearchSearchItemTriggerABusBItemAudioDataQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier`` command.

    Description:
        - This command sets the qualifier (<, >, =, <=, >=, not =, in range, out of range) to be
          used to search on audio bus data. The search condition must be set to DATA using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:AUDIO:CONDITION``. SEARCH<x> is the search number, which
          is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier?
        ```

    Info:
        - ``LESSthan`` sets the qualifier to less than.
        - ``MOREthan`` sets the qualifier to greater than.
        - ``EQual`` sets the qualifier to equal.
        - ``UNEQual`` sets the qualifier to not equal.
        - ``LESSEQual`` sets the qualifier to less than or equal.
        - ``MOREEQual`` sets the qualifier to greater than or equal.
        - ``INrange`` sets the qualifier to in range.
        - ``OUTrange`` sets the qualifier to out of range.
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemAudioDataOffset(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet`` command.

    Description:
        - This commands sets the data offset value to be used to search on audio bus data. The
          search condition must be set to DATA using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:AUDIO:CONDITION``. SEARCH<x> is the search number, which
          is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet <NR1>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet?
        ```

    Info:
        - ``<NR1>`` is the data offset value.
    """


class SearchSearchItemTriggerABusBItemAudioDataHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue`` command.

    Description:
        - This command sets the upper word value to be used to search on audio bus data. (Use
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:AUDIO:DATA:VALUE`` to search on the lower word value.)
          The search condition must be set to DATA using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:AUDIO:CONDITION``. SEARCH<x> is the search number, which
          is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue <String>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue?
        ```

    Info:
        - ``<String>`` specifies the upper word value.
    """


class SearchSearchItemTriggerABusBItemAudioData(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue`` command.
        - ``.offset``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet`` command.
        - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier`` command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:VALue`` command.
        - ``.word``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:WORD`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = SearchSearchItemTriggerABusBItemAudioDataHivalue(
            device, f"{self._cmd_syntax}:HIVALue"
        )
        self._offset = SearchSearchItemTriggerABusBItemAudioDataOffset(
            device, f"{self._cmd_syntax}:OFFSet"
        )
        self._qualifier = SearchSearchItemTriggerABusBItemAudioDataQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._value = SearchSearchItemTriggerABusBItemAudioDataValue(
            device, f"{self._cmd_syntax}:VALue"
        )
        self._word = SearchSearchItemTriggerABusBItemAudioDataWord(
            device, f"{self._cmd_syntax}:WORD"
        )

    @property
    def hivalue(self) -> SearchSearchItemTriggerABusBItemAudioDataHivalue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue`` command.

        Description:
            - This command sets the upper word value to be used to search on audio bus data. (Use
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:AUDIO:DATA:VALUE`` to search on the lower word
              value.) The search condition must be set to DATA using
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:AUDIO:CONDITION``. SEARCH<x> is the search number,
              which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue <String>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue?
            ```

        Info:
            - ``<String>`` specifies the upper word value.
        """
        return self._hivalue

    @property
    def offset(self) -> SearchSearchItemTriggerABusBItemAudioDataOffset:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet`` command.

        Description:
            - This commands sets the data offset value to be used to search on audio bus data. The
              search condition must be set to DATA using
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:AUDIO:CONDITION``. SEARCH<x> is the search number,
              which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet <NR1>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet?
            ```

        Info:
            - ``<NR1>`` is the data offset value.
        """
        return self._offset

    @property
    def qualifier(self) -> SearchSearchItemTriggerABusBItemAudioDataQualifier:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier`` command.

        Description:
            - This command sets the qualifier (<, >, =, <=, >=, not =, in range, out of range) to be
              used to search on audio bus data. The search condition must be set to DATA using
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:AUDIO:CONDITION``. SEARCH<x> is the search number,
              which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier?
            ```

        Info:
            - ``LESSthan`` sets the qualifier to less than.
            - ``MOREthan`` sets the qualifier to greater than.
            - ``EQual`` sets the qualifier to equal.
            - ``UNEQual`` sets the qualifier to not equal.
            - ``LESSEQual`` sets the qualifier to less than or equal.
            - ``MOREEQual`` sets the qualifier to greater than or equal.
            - ``INrange`` sets the qualifier to in range.
            - ``OUTrange`` sets the qualifier to out of range.
        """  # noqa: E501
        return self._qualifier

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemAudioDataValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:VALue`` command.

        Description:
            - This command sets the lower word value to be used to search on audio bus data. (Use
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:AUDIO:DATA:HIVALUE`` to set the upper word value.)
              The search condition must be set to DATA using
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:AUDIO:CONDITION``. SEARCH<x> is the search number,
              which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:VALue <String>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:VALue?
            ```
        """
        return self._value

    @property
    def word(self) -> SearchSearchItemTriggerABusBItemAudioDataWord:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:WORD`` command.

        Description:
            - This command sets the alignment of the data (left, right or either) to be used to
              search on audio bus data. The search condition must be set to DATA using
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:AUDIO:CONDITION``. SEARCH<x> is the search number,
              which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:WORD?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:WORD?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:WORD value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:WORD {EITher|LEFt|RIGht}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:WORD?
            ```

        Info:
            - ``EITher`` aligns the data to either left or right.
            - ``LEFt`` aligns the data to the left.
            - ``RIGht`` aligns the data to the right.
        """
        return self._word


class SearchSearchItemTriggerABusBItemAudioCondition(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:CONDition`` command.

    Description:
        - This command sets the condition (start of frame or matching data) to be used to search on
          audio bus data. SEARCH<x> is the search number, which is always 1, and B<x> is the bus
          number (1-2).

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:CONDition?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:CONDition value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:CONDition {SOF|DATA}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:CONDition?
        ```

    Info:
        - ``SOF`` specifies to search on the start of frame.
        - ``DATA`` specifies to search on matching data.
    """


class SearchSearchItemTriggerABusBItemAudio(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:CONDition`` command.
        - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = SearchSearchItemTriggerABusBItemAudioCondition(
            device, f"{self._cmd_syntax}:CONDition"
        )
        self._data = SearchSearchItemTriggerABusBItemAudioData(device, f"{self._cmd_syntax}:DATa")

    @property
    def condition(self) -> SearchSearchItemTriggerABusBItemAudioCondition:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:CONDition`` command.

        Description:
            - This command sets the condition (start of frame or matching data) to be used to search
              on audio bus data. SEARCH<x> is the search number, which is always 1, and B<x> is the
              bus number (1-2).

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:CONDition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:CONDition?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:CONDition value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:CONDition {SOF|DATA}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:CONDition?
            ```

        Info:
            - ``SOF`` specifies to search on the start of frame.
            - ``DATA`` specifies to search on matching data.
        """
        return self._condition

    @property
    def data(self) -> SearchSearchItemTriggerABusBItemAudioData:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue`` command.
            - ``.offset``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet`` command.
            - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier``
              command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:VALue`` command.
            - ``.word``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa:WORD`` command.
        """
        return self._data


class SearchSearchItemTriggerABusBItemArinc429aSsm(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SSM`` command.

    Description:
        - This command specifies the value for the SSM field to be used when searching on the
          ARINC429 bus data field(s). The search condition must be set to DATA or LABELANDDATA
          (using ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:ARINC429A:CONDITION``). The default is all X's
          (don't care). SEARCH<x> is the search number, which is always 1. B<x> is the bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SSM?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SSM?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SSM value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SSM <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SSM?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemArinc429aSdi(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SDI`` command.

    Description:
        - This command specifies the value for the SDI field to be used when searching on the
          ARINC429 bus data field(s). The search condition must be set to DATA or LABELANDDATA
          (using ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:ARINC429A:CONDITION``). The default is all X's
          (don't care). SEARCH<x> is the search number, which is always 1. B<x> is the bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SDI?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SDI?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SDI value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SDI <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SDI?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemArinc429aLabelValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue`` command.

    Description:
        - This command specifies the low value to be used when searching on the ARINC429 bus label
          field. The search condition must be set to LABel or LABELANDDATA (using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:ARINC429A:CONDITION``). The default is all X's (don't
          care). SEARCH<x> is the search number, which is always 1. B<x> is the bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemArinc429aLabelQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier`` command.

    Description:
        - This command specifies the qualifier to be used when searching on the ARINC429 label
          field. The search condition must be set to LABel or LABELANDDATA. The default qualifier is
          'Equal to'. SEARCH<x> is the search number, which is always 1. B<x> is the bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier {LESSthan|MOREthan|Equal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier?
        ```

    Info:
        - ``LESSthan`` sets label qualifier to less than.
        - ``MOREthan`` sets the label qualifier to greater than.
        - ``EQual`` sets the label qualifier to equal.
        - ``UNEQual`` sets the label qualifier to not equal.
        - ``LESSEQual`` sets the label qualifier to less than or equal.
        - ``MOREEQual`` sets the label qualifier to greater than or equal.
        - ``INrange`` sets the label qualifier to in range.
        - ``OUTrange`` sets the label qualifier to out of range.
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemArinc429aLabelHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue`` command.

    Description:
        - When the search condition is set to LABel, and the qualifier is set to either INrange or
          OUTrange, this command specifies the upper value of the range for a match on the label
          field. (Use the command ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:ARINC429A:LABEL:VALUE`` to
          specify the lower value of the range). The default is all X's (don't care). SEARCH<x> is
          the search number, which is always 1. B<x> is the bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemArinc429aLabel(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue`` command.
        - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier``
          command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = SearchSearchItemTriggerABusBItemArinc429aLabelHivalue(
            device, f"{self._cmd_syntax}:HIVALue"
        )
        self._qualifier = SearchSearchItemTriggerABusBItemArinc429aLabelQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._value = SearchSearchItemTriggerABusBItemArinc429aLabelValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def hivalue(self) -> SearchSearchItemTriggerABusBItemArinc429aLabelHivalue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue`` command.

        Description:
            - When the search condition is set to LABel, and the qualifier is set to either INrange
              or OUTrange, this command specifies the upper value of the range for a match on the
              label field. (Use the command
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:ARINC429A:LABEL:VALUE`` to specify the lower value
              of the range). The default is all X's (don't care). SEARCH<x> is the search number,
              which is always 1. B<x> is the bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue?
            ```
        """
        return self._hivalue

    @property
    def qualifier(self) -> SearchSearchItemTriggerABusBItemArinc429aLabelQualifier:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier`` command.

        Description:
            - This command specifies the qualifier to be used when searching on the ARINC429 label
              field. The search condition must be set to LABel or LABELANDDATA. The default
              qualifier is 'Equal to'. SEARCH<x> is the search number, which is always 1. B<x> is
              the bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier {LESSthan|MOREthan|Equal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier?
            ```

        Info:
            - ``LESSthan`` sets label qualifier to less than.
            - ``MOREthan`` sets the label qualifier to greater than.
            - ``EQual`` sets the label qualifier to equal.
            - ``UNEQual`` sets the label qualifier to not equal.
            - ``LESSEQual`` sets the label qualifier to less than or equal.
            - ``MOREEQual`` sets the label qualifier to greater than or equal.
            - ``INrange`` sets the label qualifier to in range.
            - ``OUTrange`` sets the label qualifier to out of range.
        """  # noqa: E501
        return self._qualifier

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemArinc429aLabelValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue`` command.

        Description:
            - This command specifies the low value to be used when searching on the ARINC429 bus
              label field. The search condition must be set to LABel or LABELANDDATA (using
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:ARINC429A:CONDITION``). The default is all X's
              (don't care). SEARCH<x> is the search number, which is always 1. B<x> is the bus
              number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue?
            ```
        """
        return self._value


class SearchSearchItemTriggerABusBItemArinc429aErrtype(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE`` command.

    Description:
        - This command specifies the error type when searching on an ARINC429 bus signal. The search
          condition needs to be set to ERROR (using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:ARINC429A:CONDITION``). SEARCH<x> is the search number,
          which is always 1. B<x> is the bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE {ANY|GAP|WORD|PARity}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE?
        ```

    Info:
        - ``ANY`` sets the error type to match any of the other available error types.
        - ``GAP`` sets the error type to match on gap violations (less than 4 bits idle time between
          two packets on the bus).
        - ``WORD`` sets the error type to match on word errors (incorrect number of bits in a word
          or bits that violate return to zero transmission).
        - ``PARity`` sets the error type to match on parity errors (parity value results in even
          parity count for a word).
    """


class SearchSearchItemTriggerABusBItemArinc429aDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:VALue`` command.

    Description:
        - This command specifies the low value to be used when searching on the ARINC429 bus data
          field(s). The search condition must be set to DATA or LABELANDDATA (using
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:ARINC429A:CONDITION``). The default is all X's (don't
          care). SEARCH<x> is the search number, which is always 1. B<x> is the bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:VALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:VALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:VALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemArinc429aDataQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:QUALifier`` command.

    Description:
        - This command specifies the qualifier to be used when searching on the ARINC429 data
          field(s). The search condition must be set to DATA or LABELANDDATA. The default qualifier
          is 'Equal to'. SEARCH<x> is the search number, which is always 1. B<x> is the bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:QUALifier?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:QUALifier value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:QUALifier {LESSthan|MOREthan|Equal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:QUALifier?
        ```

    Info:
        - ``LESSthan`` sets data qualifier to less than.
        - ``MOREthan`` sets the data qualifier to greater than.
        - ``EQual`` sets the data qualifier to equal.
        - ``UNEQual`` sets the data qualifier to not equal.
        - ``LESSEQual`` sets the data qualifier to less than or equal.
        - ``MOREEQual`` sets the data qualifier to greater than or equal.
        - ``INrange`` sets the data qualifier to in range.
        - ``OUTrange`` sets the data qualifier to out of range.
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemArinc429aDataHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:HIVALue`` command.

    Description:
        - When the search condition is set to DATA or LABELANDDATA, and the qualifier is set to
          either INrange or OUTrange, this command specifies the upper value of the range for a
          match on the data field. (Use the command
          ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:ARINC429A:DATA:VALUE`` to specify the lower value of the
          range). The default is all X's (don't care). SEARCH<x> is the search number, which is
          always 1. B<x> is the bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:HIVALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:HIVALue value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:HIVALue <QString>
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:HIVALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class SearchSearchItemTriggerABusBItemArinc429aData(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:HIVALue`` command.
        - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:QUALifier``
          command.
        - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = SearchSearchItemTriggerABusBItemArinc429aDataHivalue(
            device, f"{self._cmd_syntax}:HIVALue"
        )
        self._qualifier = SearchSearchItemTriggerABusBItemArinc429aDataQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._value = SearchSearchItemTriggerABusBItemArinc429aDataValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def hivalue(self) -> SearchSearchItemTriggerABusBItemArinc429aDataHivalue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:HIVALue`` command.

        Description:
            - When the search condition is set to DATA or LABELANDDATA, and the qualifier is set to
              either INrange or OUTrange, this command specifies the upper value of the range for a
              match on the data field. (Use the command
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:ARINC429A:DATA:VALUE`` to specify the lower value of
              the range). The default is all X's (don't care). SEARCH<x> is the search number, which
              is always 1. B<x> is the bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:HIVALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:HIVALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:HIVALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:HIVALue?
            ```
        """
        return self._hivalue

    @property
    def qualifier(self) -> SearchSearchItemTriggerABusBItemArinc429aDataQualifier:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:QUALifier`` command.

        Description:
            - This command specifies the qualifier to be used when searching on the ARINC429 data
              field(s). The search condition must be set to DATA or LABELANDDATA. The default
              qualifier is 'Equal to'. SEARCH<x> is the search number, which is always 1. B<x> is
              the bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:QUALifier?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:QUALifier value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:QUALifier {LESSthan|MOREthan|Equal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:QUALifier?
            ```

        Info:
            - ``LESSthan`` sets data qualifier to less than.
            - ``MOREthan`` sets the data qualifier to greater than.
            - ``EQual`` sets the data qualifier to equal.
            - ``UNEQual`` sets the data qualifier to not equal.
            - ``LESSEQual`` sets the data qualifier to less than or equal.
            - ``MOREEQual`` sets the data qualifier to greater than or equal.
            - ``INrange`` sets the data qualifier to in range.
            - ``OUTrange`` sets the data qualifier to out of range.
        """  # noqa: E501
        return self._qualifier

    @property
    def value(self) -> SearchSearchItemTriggerABusBItemArinc429aDataValue:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:VALue`` command.

        Description:
            - This command specifies the low value to be used when searching on the ARINC429 bus
              data field(s). The search condition must be set to DATA or LABELANDDATA (using
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:ARINC429A:CONDITION``). The default is all X's
              (don't care). SEARCH<x> is the search number, which is always 1. B<x> is the bus
              number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:VALue value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:VALue <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:VALue?
            ```
        """
        return self._value


class SearchSearchItemTriggerABusBItemArinc429aCondition(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:CONDition`` command.

    Description:
        - This command sets the condition (word start, label, matching data, word end, or error) to
          be used to search on ARINC429 bus data. SEARCH<x> is the search number, which is always 1.
          B<x> is the bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:CONDition?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:CONDition value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:CONDition {STARt|END|LABel|DATA|LABELANDDATA|ERRor}
        - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:CONDition?
        ```

    Info:
        - ``STARt`` specifies a search based on the first bit of a word.
        - ``END`` specifies a search based on the 32nd bit of a word.
        - ``LABel`` specifies a search for a matching label.
        - ``DATA`` specifies a search for matching packet data field(s).
        - ``LABELANDDATA`` specifies a search for matching label and matching packet data field(s).
        - ``ERROR`` specifies a search for specified packet error.
    """  # noqa: E501


class SearchSearchItemTriggerABusBItemArinc429a(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:CONDition`` command.
        - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA`` command tree.
        - ``.errtype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE`` command.
        - ``.label``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel`` command tree.
        - ``.sdi``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SDI`` command.
        - ``.ssm``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SSM`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = SearchSearchItemTriggerABusBItemArinc429aCondition(
            device, f"{self._cmd_syntax}:CONDition"
        )
        self._data = SearchSearchItemTriggerABusBItemArinc429aData(
            device, f"{self._cmd_syntax}:DATA"
        )
        self._errtype = SearchSearchItemTriggerABusBItemArinc429aErrtype(
            device, f"{self._cmd_syntax}:ERRTYPE"
        )
        self._label = SearchSearchItemTriggerABusBItemArinc429aLabel(
            device, f"{self._cmd_syntax}:LABel"
        )
        self._sdi = SearchSearchItemTriggerABusBItemArinc429aSdi(device, f"{self._cmd_syntax}:SDI")
        self._ssm = SearchSearchItemTriggerABusBItemArinc429aSsm(device, f"{self._cmd_syntax}:SSM")

    @property
    def condition(self) -> SearchSearchItemTriggerABusBItemArinc429aCondition:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:CONDition`` command.

        Description:
            - This command sets the condition (word start, label, matching data, word end, or error)
              to be used to search on ARINC429 bus data. SEARCH<x> is the search number, which is
              always 1. B<x> is the bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:CONDition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:CONDition?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:CONDition value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:CONDition {STARt|END|LABel|DATA|LABELANDDATA|ERRor}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:CONDition?
            ```

        Info:
            - ``STARt`` specifies a search based on the first bit of a word.
            - ``END`` specifies a search based on the 32nd bit of a word.
            - ``LABel`` specifies a search for a matching label.
            - ``DATA`` specifies a search for matching packet data field(s).
            - ``LABELANDDATA`` specifies a search for matching label and matching packet data
              field(s).
            - ``ERROR`` specifies a search for specified packet error.
        """  # noqa: E501
        return self._condition

    @property
    def data(self) -> SearchSearchItemTriggerABusBItemArinc429aData:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:HIVALue``
              command.
            - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:QUALifier``
              command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA:VALue`` command.
        """
        return self._data

    @property
    def errtype(self) -> SearchSearchItemTriggerABusBItemArinc429aErrtype:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE`` command.

        Description:
            - This command specifies the error type when searching on an ARINC429 bus signal. The
              search condition needs to be set to ERROR (using
              ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:ARINC429A:CONDITION``). SEARCH<x> is the search
              number, which is always 1. B<x> is the bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE {ANY|GAP|WORD|PARity}
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE?
            ```

        Info:
            - ``ANY`` sets the error type to match any of the other available error types.
            - ``GAP`` sets the error type to match on gap violations (less than 4 bits idle time
              between two packets on the bus).
            - ``WORD`` sets the error type to match on word errors (incorrect number of bits in a
              word or bits that violate return to zero transmission).
            - ``PARity`` sets the error type to match on parity errors (parity value results in even
              parity count for a word).
        """
        return self._errtype

    @property
    def label(self) -> SearchSearchItemTriggerABusBItemArinc429aLabel:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue``
              command.
            - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier``
              command.
            - ``.value``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue`` command.
        """
        return self._label

    @property
    def sdi(self) -> SearchSearchItemTriggerABusBItemArinc429aSdi:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SDI`` command.

        Description:
            - This command specifies the value for the SDI field to be used when searching on the
              ARINC429 bus data field(s). The search condition must be set to DATA or LABELANDDATA
              (using ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:ARINC429A:CONDITION``). The default is all
              X's (don't care). SEARCH<x> is the search number, which is always 1. B<x> is the bus
              number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SDI?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SDI?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SDI value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SDI <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SDI?
            ```
        """
        return self._sdi

    @property
    def ssm(self) -> SearchSearchItemTriggerABusBItemArinc429aSsm:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SSM`` command.

        Description:
            - This command specifies the value for the SSM field to be used when searching on the
              ARINC429 bus data field(s). The search condition must be set to DATA or LABELANDDATA
              (using ``SEARCH:SEARCHX:TRIGGER:A:BUS:BX:ARINC429A:CONDITION``). The default is all
              X's (don't care). SEARCH<x> is the search number, which is always 1. B<x> is the bus
              number.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SSM?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SSM?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SSM value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SSM <QString>
            - SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SSM?
            ```
        """
        return self._ssm


#  pylint: disable=too-many-instance-attributes
class SearchSearchItemTriggerABusBItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>?``
          query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.arinc429a``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A`` command tree.
        - ``.audio``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio`` command tree.
        - ``.can``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN`` command tree.
        - ``.ethernet``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet`` command tree.
        - ``.flexray``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray`` command tree.
        - ``.i2c``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C`` command tree.
        - ``.lin``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN`` command tree.
        - ``.mil1553b``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B`` command tree.
        - ``.parallel``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel`` command tree.
        - ``.rs232c``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C`` command tree.
        - ``.spi``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI`` command tree.
        - ``.usb``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._arinc429a = SearchSearchItemTriggerABusBItemArinc429a(
            device, f"{self._cmd_syntax}:ARINC429A"
        )
        self._audio = SearchSearchItemTriggerABusBItemAudio(device, f"{self._cmd_syntax}:AUDio")
        self._can = SearchSearchItemTriggerABusBItemCan(device, f"{self._cmd_syntax}:CAN")
        self._ethernet = SearchSearchItemTriggerABusBItemEthernet(
            device, f"{self._cmd_syntax}:ETHERnet"
        )
        self._flexray = SearchSearchItemTriggerABusBItemFlexray(
            device, f"{self._cmd_syntax}:FLEXray"
        )
        self._i2c = SearchSearchItemTriggerABusBItemI2c(device, f"{self._cmd_syntax}:I2C")
        self._lin = SearchSearchItemTriggerABusBItemLin(device, f"{self._cmd_syntax}:LIN")
        self._mil1553b = SearchSearchItemTriggerABusBItemMil1553b(
            device, f"{self._cmd_syntax}:MIL1553B"
        )
        self._parallel = SearchSearchItemTriggerABusBItemParallel(
            device, f"{self._cmd_syntax}:PARallel"
        )
        self._rs232c = SearchSearchItemTriggerABusBItemRs232c(device, f"{self._cmd_syntax}:RS232C")
        self._spi = SearchSearchItemTriggerABusBItemSpi(device, f"{self._cmd_syntax}:SPI")
        self._usb = SearchSearchItemTriggerABusBItemUsb(device, f"{self._cmd_syntax}:USB")

    @property
    def arinc429a(self) -> SearchSearchItemTriggerABusBItemArinc429a:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:CONDition``
              command.
            - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:DATA`` command tree.
            - ``.errtype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE`` command.
            - ``.label``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:LABel`` command tree.
            - ``.sdi``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SDI`` command.
            - ``.ssm``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A:SSM`` command.
        """
        return self._arinc429a

    @property
    def audio(self) -> SearchSearchItemTriggerABusBItemAudio:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:CONDition`` command.
            - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio:DATa`` command tree.
        """
        return self._audio

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
            - ``.fd``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FD`` command tree.
            - ``.frametype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:FRAMEtype`` command.
            - ``.identifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:IDentifier`` command
              tree.
            - ``.address``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN:ADDRess`` command tree.
        """
        return self._can

    @property
    def ethernet(self) -> SearchSearchItemTriggerABusBItemEthernet:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:DATa`` command tree.
            - ``.frametype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe``
              command.
        """
        return self._ethernet

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
    def mil1553b(self) -> SearchSearchItemTriggerABusBItemMil1553b:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.command``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:COMMAND`` command
              tree.
            - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:CONDition``
              command.
            - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:DATa`` command tree.
            - ``.errtype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE`` command.
            - ``.status``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:STATus`` command tree.
            - ``.time``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B:TIMe`` command tree.
        """
        return self._mil1553b

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

    @property
    def usb(self) -> SearchSearchItemTriggerABusBItemUsb:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.address``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ADDRess`` command tree.
            - ``.condition``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:CONDition`` command.
            - ``.data``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:DATa`` command tree.
            - ``.endpoint``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ENDPoint`` command tree.
            - ``.errtype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:ERRTYPE`` command.
            - ``.handshaketype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:HANDSHAKEType``
              command.
            - ``.qualifier``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:QUALifier`` command.
            - ``.sofframenumber``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber``
              command.
            - ``.specialtype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPECIALType`` command.
            - ``.split``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:SPLit`` command tree.
            - ``.tokentype``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB:TOKENType`` command.
        """
        return self._usb


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
            - ``.arinc429a``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ARINC429A`` command tree.
            - ``.audio``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:AUDio`` command tree.
            - ``.can``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:CAN`` command tree.
            - ``.ethernet``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:ETHERnet`` command tree.
            - ``.flexray``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:FLEXray`` command tree.
            - ``.i2c``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:I2C`` command tree.
            - ``.lin``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:LIN`` command tree.
            - ``.mil1553b``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:MIL1553B`` command tree.
            - ``.parallel``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:PARallel`` command tree.
            - ``.rs232c``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:RS232C`` command tree.
            - ``.spi``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:SPI`` command tree.
            - ``.usb``: The ``SEARCH:SEARCH<x>:TRIGger:A:BUS:B<x>:USB`` command tree.
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
        - ``.level``: The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel`` command tree.
        - ``.logic``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc`` command tree.
        - ``.lowerthreshold``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold`` command tree.
        - ``.pulsewidth``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth`` command tree.
        - ``.runt``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT`` command tree.
        - ``.sethold``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold`` command tree.
        - ``.timeout``: The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut`` command tree.
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
        self._timeout = SearchSearchItemTriggerATimeout(device, f"{self._cmd_syntax}:TIMEOut")
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
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:LEVel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:LEVel?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:LEVel?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:CH<x>`` command.
            - ``.math``: The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:MATH`` command.
            - ``.ref``: The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:REF<x>`` command.
            - ``.rf_amplitude``: The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_AMPlitude`` command.
            - ``.rf_frequency``: The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_FREQuency`` command.
            - ``.rf_phase``: The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel:RF_PHASe`` command.
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
            - ``.rf_frequency``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_FREQuency``
              command.
            - ``.rf_phase``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold:RF_PHASe`` command.
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
            - ``.highlimit``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:HIGHLimit`` command.
            - ``.lowlimit``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth:LOWLimit`` command.
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
    def timeout(self) -> SearchSearchItemTriggerATimeout:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:POLarity`` command.
            - ``.source``: The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:SOUrce`` command.
            - ``.time``: The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut:TIMe`` command.
        """
        return self._timeout

    @property
    def type(self) -> SearchSearchItemTriggerAType:
        """Return the ``SEARCH:SEARCH<x>:TRIGger:A:TYPe`` command.

        Description:
            - This command specifies the search type to determine where to place a mark. The default
              search type is EDGe. SEARCH<x> is the search number, which is always 1.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:TYPe?``
              query.
            - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIGger:A:TYPe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIGger:A:TYPe value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIGger:A:TYPe {EDGe|PULSEWidth|SETHold|RUNt|TRANsition|LOGIc|TIMEOut|BUS (with the appropriate application module installed)}
            - SEARCH:SEARCH<x>:TRIGger:A:TYPe?
            ```

        Info:
            - ``EDGe`` is the default search. An edge search occurs when a signal passes through a
              specified voltage level in a specified direction and is controlled by the
              ``SEARCH:SEARCHX:TRIGGER:A:EDGE:SOURCE`` and ``SEARCH:SEARCHX:TRIGGER:A:EDGE:SLOPE``
              commands.
            - ``PULSEWIdth`` searches when a pulse is found that has the specified polarity, and is
              either inside or outside the limits as specified by
              ``SEARCH:SEARCHX:TRIGGER:A:LOGIC:PATTERN:WHEN:LESSLIMIT`` and
              ``SEARCH:SEARCHX:TRIGGER:A:LOGIC:PATTERN:WHEN:MORELIMIT``. The polarity is selected
              using the ``SEARCH:SEARCHX:TRIGGER:A:RUNT:POLARITY`` command.
            - ``SETHold`` specifies a setup and hold search.
            - ``RUNt`` searches for when a pulse crosses the first preset voltage threshold, but
              does not cross the second preset threshold before recrossing the first. The thresholds
              are set using the ``SEARCH:SEARCHX:TRIGGER:A:LOWERTHRESHOLD:CHX`` and
              ``SEARCH:SEARCHX:TRIGGER:A:UPPERTHRESHOLD:CHX`` commands.
            - ``TRANsition`` searches for when a pulse crosses both thresholds in the same direction
              as the specified polarity and the transition time between the two threshold crossings
              is greater or less than the specified time delta.
            - ``LOGic`` specifies that a search occurs when specified conditions are met, and is
              controlled by the ``SEARCH:A:LOGIc`` commands.
            - ``TIMEout`` specifies that a search occurs when no pulse is detected in a specified
              time.
            - ``BUS`` specifies that a search occurs when a communications signal is found.
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
            - ``.level``: The ``SEARCH:SEARCH<x>:TRIGger:A:LEVel`` command tree.
            - ``.logic``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOGIc`` command tree.
            - ``.lowerthreshold``: The ``SEARCH:SEARCH<x>:TRIGger:A:LOWerthreshold`` command tree.
            - ``.pulsewidth``: The ``SEARCH:SEARCH<x>:TRIGger:A:PULSEWidth`` command tree.
            - ``.runt``: The ``SEARCH:SEARCH<x>:TRIGger:A:RUNT`` command tree.
            - ``.sethold``: The ``SEARCH:SEARCH<x>:TRIGger:A:SETHold`` command tree.
            - ``.timeout``: The ``SEARCH:SEARCH<x>:TRIGger:A:TIMEOut`` command tree.
            - ``.type``: The ``SEARCH:SEARCH<x>:TRIGger:A:TYPe`` command.
            - ``.upperthreshold``: The ``SEARCH:SEARCH<x>:TRIGger:A:UPPerthreshold`` command tree.
            - ``.transition``: The ``SEARCH:SEARCH<x>:TRIGger:A:TRANsition`` command tree.
            - ``.risefall``: The ``SEARCH:SEARCH<x>:TRIGger:A:RISEFall`` command tree.
        """
        return self._a


class SearchSearchItemTrigABusBItemMil1553bCommandAddrQual(SCPICmdWrite, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND:ADDR:QUAL`` command.

    Description:
        - When the MIL-STD-1553 bus search condition is set to COMMAND, this command specifies the
          qualifier to be used with the remote terminal address field. SEARCH<x> is the search
          number, which is always 1, and B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND:ADDR:QUAL?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND:ADDR:QUAL?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND:ADDR:QUAL value`` command.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND:ADDR:QUAL {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND:ADDR:QUAL?
        ```

    Info:
        - ``LESSthan`` sets the Command Address qualifier to less than.
        - ``MOREthan`` sets the Command Address qualifier to greater than.
        - ``EQual`` sets the Command Address qualifier to equal.
        - ``UNEQual`` sets the Command Address qualifier to not equal.
        - ``LESSEQual`` sets the Command Address qualifier to less than or equal.
        - ``MOREEQual`` sets the Command Address qualifier to greater than or equal.
        - ``INrange`` sets the Command Address qualifier to in range.
        - ``OUTrange`` sets the Command Address qualifier to out of range.
    """  # noqa: E501


class SearchSearchItemTrigABusBItemMil1553bCommandAddr(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND:ADDR`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND:ADDR?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND:ADDR?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.qual``: The ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND:ADDR:QUAL`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._qual = SearchSearchItemTrigABusBItemMil1553bCommandAddrQual(
            device, f"{self._cmd_syntax}:QUAL"
        )

    @property
    def qual(self) -> SearchSearchItemTrigABusBItemMil1553bCommandAddrQual:
        """Return the ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND:ADDR:QUAL`` command.

        Description:
            - When the MIL-STD-1553 bus search condition is set to COMMAND, this command specifies
              the qualifier to be used with the remote terminal address field. SEARCH<x> is the
              search number, which is always 1, and B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND:ADDR:QUAL?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND:ADDR:QUAL?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND:ADDR:QUAL value`` command.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND:ADDR:QUAL {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND:ADDR:QUAL?
            ```

        Info:
            - ``LESSthan`` sets the Command Address qualifier to less than.
            - ``MOREthan`` sets the Command Address qualifier to greater than.
            - ``EQual`` sets the Command Address qualifier to equal.
            - ``UNEQual`` sets the Command Address qualifier to not equal.
            - ``LESSEQual`` sets the Command Address qualifier to less than or equal.
            - ``MOREEQual`` sets the Command Address qualifier to greater than or equal.
            - ``INrange`` sets the Command Address qualifier to in range.
            - ``OUTrange`` sets the Command Address qualifier to out of range.
        """  # noqa: E501
        return self._qual


class SearchSearchItemTrigABusBItemMil1553bCommand(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND?`` query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    Properties:
        - ``.addr``: The ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND:ADDR`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._addr = SearchSearchItemTrigABusBItemMil1553bCommandAddr(
            device, f"{self._cmd_syntax}:ADDR"
        )

    @property
    def addr(self) -> SearchSearchItemTrigABusBItemMil1553bCommandAddr:
        """Return the ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND:ADDR`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND:ADDR?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND:ADDR?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.qual``: The ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND:ADDR:QUAL``
              command.
        """
        return self._addr


class SearchSearchItemTrigABusBItemMil1553b(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.command``: The ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._command = SearchSearchItemTrigABusBItemMil1553bCommand(
            device, f"{self._cmd_syntax}:COMMAND"
        )

    @property
    def command(self) -> SearchSearchItemTrigABusBItemMil1553bCommand:
        """Return the ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.addr``: The ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND:ADDR`` command
              tree.
        """
        return self._command


class SearchSearchItemTrigABusBItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.mil1553b``: The ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mil1553b = SearchSearchItemTrigABusBItemMil1553b(
            device, f"{self._cmd_syntax}:MIL1553B"
        )

    @property
    def mil1553b(self) -> SearchSearchItemTrigABusBItemMil1553b:
        """Return the ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.command``: The ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B:COMMAND`` command tree.
        """
        return self._mil1553b


class SearchSearchItemTrigABus(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIG:A:BUS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIG:A:BUS?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIG:A:BUS?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.b``: The ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._b: Dict[int, SearchSearchItemTrigABusBItem] = DefaultDictPassKeyToFactory(
            lambda x: SearchSearchItemTrigABusBItem(device, f"{self._cmd_syntax}:B{x}")
        )

    @property
    def b(self) -> Dict[int, SearchSearchItemTrigABusBItem]:
        """Return the ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.mil1553b``: The ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>:MIL1553B`` command tree.
        """
        return self._b


class SearchSearchItemTrigA(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIG:A`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIG:A?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIG:A?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bus``: The ``SEARCH:SEARCH<x>:TRIG:A:BUS`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bus = SearchSearchItemTrigABus(device, f"{self._cmd_syntax}:BUS")

    @property
    def bus(self) -> SearchSearchItemTrigABus:
        """Return the ``SEARCH:SEARCH<x>:TRIG:A:BUS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIG:A:BUS?`` query.
            - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIG:A:BUS?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.b``: The ``SEARCH:SEARCH<x>:TRIG:A:BUS:B<x>`` command tree.
        """
        return self._bus


class SearchSearchItemTrig(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TRIG`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIG?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIG?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.a``: The ``SEARCH:SEARCH<x>:TRIG:A`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._a = SearchSearchItemTrigA(device, f"{self._cmd_syntax}:A")

    @property
    def a(self) -> SearchSearchItemTrigA:
        """Return the ``SEARCH:SEARCH<x>:TRIG:A`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIG:A?`` query.
            - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIG:A?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bus``: The ``SEARCH:SEARCH<x>:TRIG:A:BUS`` command tree.
        """
        return self._a


class SearchSearchItemTotal(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:TOTal`` command.

    Description:
        - Returns the total number of matches for the search. The total number of matches may be
          than the number of marks placed. <x> is the search number, which is always 1.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TOTal?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TOTal?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:TOTal?
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


class SearchSearchItemList(SCPICmdRead):
    """The ``SEARCH:SEARCH<x>:LIST`` command.

    Description:
        - This query returns a list of all automatically created search marks on waveforms in the
          time domain (leaving out any manually created marks). These automatic marks are created
          using a search command. The entries returned are in the form of an enumeration
          representing the source waveform, followed by 7 time mark parameters. SEARCH<x> is the
          search number, which is always 1. To return a list of manual marks, use the query form of
          ``MARK:USERLIST``.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:LIST?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:LIST?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SEARCH:SEARCH<x>:LIST?
        ```
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
        - ``.list``: The ``SEARCH:SEARCH<x>:LIST`` command.
        - ``.state``: The ``SEARCH:SEARCH<x>:STATE`` command.
        - ``.total``: The ``SEARCH:SEARCH<x>:TOTal`` command.
        - ``.trig``: The ``SEARCH:SEARCH<x>:TRIG`` command tree.
        - ``.trigger``: The ``SEARCH:SEARCH<x>:TRIGger`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._copy = SearchSearchItemCopy(device, f"{self._cmd_syntax}:COPy")
        self._list = SearchSearchItemList(device, f"{self._cmd_syntax}:LIST")
        self._state = SearchSearchItemState(device, f"{self._cmd_syntax}:STATE")
        self._total = SearchSearchItemTotal(device, f"{self._cmd_syntax}:TOTal")
        self._trig = SearchSearchItemTrig(device, f"{self._cmd_syntax}:TRIG")
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
    def list(self) -> SearchSearchItemList:
        """Return the ``SEARCH:SEARCH<x>:LIST`` command.

        Description:
            - This query returns a list of all automatically created search marks on waveforms in
              the time domain (leaving out any manually created marks). These automatic marks are
              created using a search command. The entries returned are in the form of an enumeration
              representing the source waveform, followed by 7 time mark parameters. SEARCH<x> is the
              search number, which is always 1. To return a list of manual marks, use the query form
              of ``MARK:USERLIST``.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:LIST?`` query.
            - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:LIST?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:LIST?
            ```
        """
        return self._list

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
        """Return the ``SEARCH:SEARCH<x>:TOTal`` command.

        Description:
            - Returns the total number of matches for the search. The total number of matches may be
              than the number of marks placed. <x> is the search number, which is always 1.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TOTal?`` query.
            - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TOTal?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SEARCH:SEARCH<x>:TOTal?
            ```
        """
        return self._total

    @property
    def trig(self) -> SearchSearchItemTrig:
        """Return the ``SEARCH:SEARCH<x>:TRIG`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH:SEARCH<x>:TRIG?`` query.
            - Using the ``.verify(value)`` method will send the ``SEARCH:SEARCH<x>:TRIG?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.a``: The ``SEARCH:SEARCH<x>:TRIG:A`` command tree.
        """
        return self._trig

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
            - ``.list``: The ``SEARCH:SEARCH<x>:LIST`` command.
            - ``.state``: The ``SEARCH:SEARCH<x>:STATE`` command.
            - ``.total``: The ``SEARCH:SEARCH<x>:TOTal`` command.
            - ``.trig``: The ``SEARCH:SEARCH<x>:TRIG`` command tree.
            - ``.trigger``: The ``SEARCH:SEARCH<x>:TRIGger`` command tree.
        """
        return self._search
