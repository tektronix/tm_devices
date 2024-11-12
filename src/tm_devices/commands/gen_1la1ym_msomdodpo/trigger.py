# pylint: disable=line-too-long
"""The trigger commands module.

These commands are used in the following models:
DPO4KB, MDO4K, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - TRIGger FORCe
    - TRIGger:A SETLevel
    - TRIGger:A:BANDWidth:RF:HIGH?
    - TRIGger:A:BANDWidth:RF:LOW?
    - TRIGger:A:BUS {I2C|SPI|CAN|RS232C|PARallel|USB|LIN|FLEXRay|AUDio|ETHERnet|MIL1553B}
    - TRIGger:A:BUS:B<x>:ARINC429A:CONDition {STARt|END|LABel|DATA|LABELANDDATA|ERRor}
    - TRIGger:A:BUS:B<x>:ARINC429A:CONDition?
    - TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE {ANY|GAP|WORD|PARity}
    - TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE?
    - TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue <QString>
    - TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue?
    - TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier {LESSthan|MOREthan|Equal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
    - TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier?
    - TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue <QString>
    - TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue?
    - TRIGger:A:BUS:B<x>:ARINC429A:SDI <QString>
    - TRIGger:A:BUS:B<x>:ARINC429A:SDI?
    - TRIGger:A:BUS:B<x>:ARINC429A:SSM <QString>
    - TRIGger:A:BUS:B<x>:ARINC429A:SSM?
    - TRIGger:A:BUS:B<x>:AUDio:CONDition {SOF|DATA}
    - TRIGger:A:BUS:B<x>:AUDio:CONDition?
    - TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue <String>
    - TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue?
    - TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet <NR1>
    - TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet?
    - TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
    - TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier?
    - TRIGger:A:BUS:B<x>:AUDio:DATa:VALue <String>
    - TRIGger:A:BUS:B<x>:AUDio:DATa:VALue?
    - TRIGger:A:BUS:B<x>:AUDio:DATa:WORD {EITher|LEFt|RIGht}
    - TRIGger:A:BUS:B<x>:AUDio:DATa:WORD?
    - TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe {STandard|EXTENDed}
    - TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe?
    - TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue <QString>
    - TRIGger:A:BUS:B<x>:CAN:ADDRess:VALue?
    - TRIGger:A:BUS:B<x>:CAN:CONDition {SOF|FRAMEtype|IDentifier|DATA|IDANDDATA|EOF|ACKMISS|ERROR|FORMERRor|ANYERRor|FDBRS|FDESI}
    - TRIGger:A:BUS:B<x>:CAN:CONDition?
    - TRIGger:A:BUS:B<x>:CAN:DATa:DIRection {READ|WRITE|NOCARE}
    - TRIGger:A:BUS:B<x>:CAN:DATa:DIRection?
    - TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet <NR1>
    - TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet?
    - TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier {LESSthan|Than|EQual|UNEQual|LESSEQual|EQual}
    - TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?
    - TRIGger:A:BUS:B<x>:CAN:DATa:SIZe <NR1>
    - TRIGger:A:BUS:B<x>:CAN:DATa:SIZe?
    - TRIGger:A:BUS:B<x>:CAN:DATa:VALue <QString>
    - TRIGger:A:BUS:B<x>:CAN:DATa:VALue?
    - TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT {ZERo|OFF|0|ONE|ON|1|NOCARE|X|x}
    - TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT?
    - TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT {ZERo|OFF|0|ONE|ON|1|NOCARE|X|x}
    - TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT?
    - TRIGger:A:BUS:B<x>:CAN:FRAMEtype {DATA|REMote|ERRor|OVERLoad}
    - TRIGger:A:BUS:B<x>:CAN:FRAMEtype?
    - TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe {STandard|EXTENDed}
    - TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?
    - TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue <QString>
    - TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue?
    - TRIGger:A:BUS:B<x>:ETHERnet:CONDition {SFD|MACADDRess|MACLENgth|IPHeader|TCPHeader|DATa|EOP|IDLe|FCSError|QTAG}
    - TRIGger:A:BUS:B<x>:ETHERnet:CONDition?
    - TRIGger:A:BUS:B<x>:ETHERnet:DATa:HIVALue <QString>
    - TRIGger:A:BUS:B<x>:ETHERnet:DATa:HIVALue?
    - TRIGger:A:BUS:B<x>:ETHERnet:DATa:OFFSet <NR1>
    - TRIGger:A:BUS:B<x>:ETHERnet:DATa:OFFSet?
    - TRIGger:A:BUS:B<x>:ETHERnet:DATa:SIZe <NR1>
    - TRIGger:A:BUS:B<x>:ETHERnet:DATa:SIZe?
    - TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue <QString>
    - TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue?
    - TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe {BASic|QTAG}
    - TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe?
    - TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:DESTinationaddr:VALue <QString>
    - TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:DESTinationaddr:VALue?
    - TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:PROTOcol:VALue <QString>
    - TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:PROTOcol:VALue?
    - TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:SOUrceaddr:VALue <QString>
    - TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:SOUrceaddr:VALue?
    - TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:DESTination:VALue <QString>
    - TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:DESTination:VALue?
    - TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:SOUrce:VALue <QString>
    - TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:SOUrce:VALue?
    - TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:HIVALue <QString>
    - TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:HIVALue?
    - TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:VALue <QString>
    - TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:VALue?
    - TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:HIVALue <QString>
    - TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:HIVALue?
    - TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:VALue <QString>
    - TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:VALue?
    - TRIGger:A:BUS:B<x>:ETHERnet:QTAG:VALue <QString>
    - TRIGger:A:BUS:B<x>:ETHERnet:QTAG:VALue?
    - TRIGger:A:BUS:B<x>:ETHERnet:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
    - TRIGger:A:BUS:B<x>:ETHERnet:QUALifier?
    - TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:ACKnum:VALue <QString>
    - TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:ACKnum:VALue?
    - TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:DESTinationport:VALue <QString>
    - TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:DESTinationport:VALue?
    - TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SEQnum:VALue <QString>
    - TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SEQnum:VALue?
    - TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SOUrceport:VALue <QString>
    - TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SOUrceport:VALue?
    - TRIGger:A:BUS:B<x>:FLEXray:CONDition {SOF|FRAMEType|IDentifier|CYCLEcount|HEADer|DATA|IDANDDATA|EOF|ERROR}
    - TRIGger:A:BUS:B<x>:FLEXray:CONDition?
    - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue <QString>
    - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:HIVALue?
    - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
    - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier?
    - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue <QString>
    - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:VALue?
    - TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue <QString>
    - TRIGger:A:BUS:B<x>:FLEXray:DATa:HIVALue?
    - TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet <NR1>
    - TRIGger:A:BUS:B<x>:FLEXray:DATa:OFFSet?
    - TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
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
    - TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
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
    - TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
    - TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?
    - TRIGger:A:BUS:B<x>:LIN:DATa:SIZe <NR1>
    - TRIGger:A:BUS:B<x>:LIN:DATa:SIZe?
    - TRIGger:A:BUS:B<x>:LIN:DATa:VALue <QString>
    - TRIGger:A:BUS:B<x>:LIN:DATa:VALue?
    - TRIGger:A:BUS:B<x>:LIN:ERRTYPE {SYNC|PARity|CHecksum|HEADertime|RESPtime|FRAMetime}
    - TRIGger:A:BUS:B<x>:LIN:ERRTYPE?
    - TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue <QString>
    - TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue?
    - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue <QString>
    - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue?
    - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
    - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:QUALifier?
    - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue <QString>
    - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue?
    - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt <QString>
    - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt?
    - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
    - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity?
    - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress <QString>
    - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress?
    - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit {RX|TX|X}
    - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit?
    - TRIGger:A:BUS:B<x>:MIL1553B:CONDition {SYNC|COMMAND|STATus|DATA|TIMe|ERRor}
    - TRIGger:A:BUS:B<x>:MIL1553B:CONDition?
    - TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
    - TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity?
    - TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue <QString>
    - TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue?
    - TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE {PARity|SYNC|MANCHester|DATA}
    - TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE?
    - TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue <QString>
    - TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue?
    - TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
    - TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier?
    - TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue <QString>
    - TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue?
    - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
    - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR?
    - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
    - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY?
    - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
    - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA?
    - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
    - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR?
    - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
    - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME?
    - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
    - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ?
    - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
    - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF?
    - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
    - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF?
    - TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
    - TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity?
    - TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit <NR3>
    - TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit?
    - TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit <NR3>
    - TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit?
    - TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier {LESSthan|MOREthan|INrange|OUTrange}
    - TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier?
    - TRIGger:A:BUS:B<x>:PARallel:VALue <QString>
    - TRIGger:A:BUS:B<x>:PARallel:VALue?
    - TRIGger:A:BUS:B<x>:RS232C:CONDition {RXSTArt|RXDATA|RXENDPacket|TXSTArt|TXDATA|TXENDPacket}
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
    - TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue <QString>
    - TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue?
    - TRIGger:A:BUS:B<x>:USB:ADDRess:VALue <Qstring>
    - TRIGger:A:BUS:B<x>:USB:ADDRess:VALue?
    - TRIGger:A:BUS:B<x>:USB:CONDition {SYNC|RESET|SUSPEND|RESUME|EOP|TOKENPacket|DATAPacket|HANDSHAKEPacket|SPECIALPacket|ERRor}
    - TRIGger:A:BUS:B<x>:USB:CONDition?
    - TRIGger:A:BUS:B<x>:USB:DATa:HIVALue <QString>
    - TRIGger:A:BUS:B<x>:USB:DATa:HIVALue?
    - TRIGger:A:BUS:B<x>:USB:DATa:OFFSet <NR1>
    - TRIGger:A:BUS:B<x>:USB:DATa:OFFSet?
    - TRIGger:A:BUS:B<x>:USB:DATa:SIZe <NR1>
    - TRIGger:A:BUS:B<x>:USB:DATa:SIZe?
    - TRIGger:A:BUS:B<x>:USB:DATa:TYPe {ANY|DATA<x>}
    - TRIGger:A:BUS:B<x>:USB:DATa:TYPe?
    - TRIGger:A:BUS:B<x>:USB:DATa:VALue <QString>
    - TRIGger:A:BUS:B<x>:USB:DATa:VALue?
    - TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue <QString>
    - TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue?
    - TRIGger:A:BUS:B<x>:USB:ERRTYPE {PID|CRC5|CRC16|BITSTUFFing}
    - TRIGger:A:BUS:B<x>:USB:ERRTYPE?
    - TRIGger:A:BUS:B<x>:USB:HANDSHAKEType {ANY|NAK|ACK|STALL}
    - TRIGger:A:BUS:B<x>:USB:HANDSHAKEType?
    - TRIGger:A:BUS:B<x>:USB:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
    - TRIGger:A:BUS:B<x>:USB:QUALifier?
    - TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber <QString>
    - TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber?
    - TRIGger:A:BUS:B<x>:USB:SPECIALType {ANY|PREamble|RESERVed}
    - TRIGger:A:BUS:B<x>:USB:SPECIALType?
    - TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue {NOCARE|CONTRol|ISOchronous|BULK|INTERRUPT}
    - TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue?
    - TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue <QString>
    - TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue?
    - TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue <QString>
    - TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue?
    - TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue {NOCARE|SSPLIT|CSPLIT}
    - TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue?
    - TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue {NOCARE|FULLSPeed|LOWSPeed|ISOSTART|ISOMID|ISOEND|ISOALL}
    - TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue?
    - TRIGger:A:BUS:B<x>:USB:TOKENType {ANY|SOF|OUT|IN|SETUP}
    - TRIGger:A:BUS:B<x>:USB:TOKENType?
    - TRIGger:A:BUS:SOUrce {B<x>}
    - TRIGger:A:BUS:SOUrce?
    - TRIGger:A:BUS?
    - TRIGger:A:EDGE:COUPling {AC|DC|HFRej|LFRej|NOISErej}
    - TRIGger:A:EDGE:COUPling?
    - TRIGger:A:EDGE:SLOpe {RISe|FALL|EITHer}
    - TRIGger:A:EDGE:SLOpe?
    - TRIGger:A:EDGE:SOUrce {AUX|CH<x>|D<x>|LINE|RF}
    - TRIGger:A:EDGE:SOUrce?
    - TRIGger:A:EDGE?
    - TRIGger:A:HOLDoff:TIMe <NR3>
    - TRIGger:A:HOLDoff:TIMe?
    - TRIGger:A:HOLDoff?
    - TRIGger:A:LEVel:AUXin {<NR3>|ECL|TTL}
    - TRIGger:A:LEVel:AUXin?
    - TRIGger:A:LEVel:CH<x> {<NR3>|ECL|TTL}
    - TRIGger:A:LEVel:CH<x>?
    - TRIGger:A:LEVel:D<x> {<NR3>|ECL|TTL}
    - TRIGger:A:LEVel:D<x>?
    - TRIGger:A:LOGIc:CLAss {LOGIC|SETHold}
    - TRIGger:A:LOGIc:CLAss?
    - TRIGger:A:LOGIc:FUNCtion {AND|NANd|NOR|OR}
    - TRIGger:A:LOGIc:FUNCtion?
    - TRIGger:A:LOGIc:INPut:CH<x> {HIGH|LOW|X}
    - TRIGger:A:LOGIc:INPut:CH<x>?
    - TRIGger:A:LOGIc:INPut:CLOCk:EDGE {FALL|RISe}
    - TRIGger:A:LOGIc:INPut:CLOCk:EDGE?
    - TRIGger:A:LOGIc:INPut:CLOCk:SOUrce {CH<x>|D<x>|RF|NONE}
    - TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?
    - TRIGger:A:LOGIc:INPut:D<x> {HIGH|LOW|X}
    - TRIGger:A:LOGIc:INPut:D<x>?
    - TRIGger:A:LOGIc:INPut:RF {HIGH|LOW|X}
    - TRIGger:A:LOGIc:INPut:RF?
    - TRIGger:A:LOGIc:INPut?
    - TRIGger:A:LOGIc:PATtern:DELTatime <NR3>
    - TRIGger:A:LOGIc:PATtern:DELTatime?
    - TRIGger:A:LOGIc:PATtern:WHEn {TRUe|FALSe|LESSthan|MOREthan|EQual|UNEQual}
    - TRIGger:A:LOGIc:PATtern:WHEn?
    - TRIGger:A:LOGIc:PATtern?
    - TRIGger:A:LOGIc:THReshold:CH<x> {<NR3>|ECL|TTL}
    - TRIGger:A:LOGIc:THReshold:CH<x>?
    - TRIGger:A:LOGIc:THReshold:D<x> {<NR3>|ECL|TTL}
    - TRIGger:A:LOGIc:THReshold:D<x>?
    - TRIGger:A:LOGIc:THReshold:RF {<NR3>}
    - TRIGger:A:LOGIc:THReshold:RF?
    - TRIGger:A:LOGIc?
    - TRIGger:A:LOWerthreshold:AUX {<NR3>|ECL|TTL}
    - TRIGger:A:LOWerthreshold:AUX?
    - TRIGger:A:LOWerthreshold:CH<x> {ECL|TTL|<NR3>}
    - TRIGger:A:LOWerthreshold:CH<x>?
    - TRIGger:A:LOWerthreshold:D<x> {<NR3>|ECL|TTL}
    - TRIGger:A:LOWerthreshold:D<x>?
    - TRIGger:A:LOWerthreshold:EXT {<NR3>|ECL|TTL}
    - TRIGger:A:LOWerthreshold:EXT?
    - TRIGger:A:LOWerthreshold:RF {<NR3>}
    - TRIGger:A:LOWerthreshold:RF?
    - TRIGger:A:MODe {AUTO|NORMal}
    - TRIGger:A:MODe?
    - TRIGger:A:PULSEWidth:HIGHLimit <NR3>
    - TRIGger:A:PULSEWidth:HIGHLimit?
    - TRIGger:A:PULSEWidth:LOWLimit <NR3>
    - TRIGger:A:PULSEWidth:LOWLimit?
    - TRIGger:A:PULSEWidth:POLarity {NEGative|POSitive}
    - TRIGger:A:PULSEWidth:POLarity?
    - TRIGger:A:PULSEWidth:SOUrce {CH<x>|LINE|AUX|D<x>|RF}
    - TRIGger:A:PULSEWidth:SOUrce?
    - TRIGger:A:PULSEWidth:WHEn {LESSthan|MOREthan|EQual|UNEQual|WIThin|OUTside}
    - TRIGger:A:PULSEWidth:WHEn?
    - TRIGger:A:PULSEWidth:WIDth <NR3>
    - TRIGger:A:PULSEWidth:WIDth?
    - TRIGger:A:PULse:CLAss {RUNt|WIDth|TRANsition|TIMEOut}
    - TRIGger:A:PULse:CLAss?
    - TRIGger:A:RISEFall:DELTatime <NR3>
    - TRIGger:A:RISEFall:DELTatime?
    - TRIGger:A:RISEFall:POLarity {EITher|NEGative|POSitive}
    - TRIGger:A:RISEFall:POLarity?
    - TRIGger:A:RISEFall:SOUrce {CH<x>}
    - TRIGger:A:RISEFall:SOUrce?
    - TRIGger:A:RISEFall:WHEn {SLOWer|FASTer|EQual|UNEQual}
    - TRIGger:A:RISEFall:WHEn?
    - TRIGger:A:RISEFall?
    - TRIGger:A:RUNT:POLarity {EITher|NEGative|POSitive}
    - TRIGger:A:RUNT:POLarity?
    - TRIGger:A:RUNT:SOUrce {CH<x>|RF}
    - TRIGger:A:RUNT:SOUrce?
    - TRIGger:A:RUNT:WHEn {LESSthan|MOREthan|EQual|UNEQual|OCCURS}
    - TRIGger:A:RUNT:WHEn?
    - TRIGger:A:RUNT:WIDth <NR3>
    - TRIGger:A:RUNT:WIDth?
    - TRIGger:A:RUNT?
    - TRIGger:A:SETHold:CLOCk:EDGE {FALL|RISe}
    - TRIGger:A:SETHold:CLOCk:EDGE?
    - TRIGger:A:SETHold:CLOCk:SOUrce {CH<x>|D<x>|AUX}
    - TRIGger:A:SETHold:CLOCk:SOUrce?
    - TRIGger:A:SETHold:CLOCk:THReshold {<NR3>|TTL}
    - TRIGger:A:SETHold:CLOCk:THReshold?
    - TRIGger:A:SETHold:CLOCk?
    - TRIGger:A:SETHold:DATa:SOUrce {CH<x>|D<x>|AUX}
    - TRIGger:A:SETHold:DATa:SOUrce?
    - TRIGger:A:SETHold:DATa:THReshold {<NR3>|TTL}
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
    - TRIGger:A:TIMEOut:POLarity {STAYSHigh|STAYSLow|EITher}
    - TRIGger:A:TIMEOut:POLarity?
    - TRIGger:A:TIMEOut:SOUrce {CH<x>|LINE|AUX|D<x>|RF}
    - TRIGger:A:TIMEOut:SOUrce?
    - TRIGger:A:TIMEOut:TIMe <NR3>
    - TRIGger:A:TIMEOut:TIMe?
    - TRIGger:A:TRANsition:DELTatime <NR3>
    - TRIGger:A:TRANsition:DELTatime?
    - TRIGger:A:TRANsition:POLarity {EITher|NEGative|POSitive}
    - TRIGger:A:TRANsition:POLarity?
    - TRIGger:A:TRANsition:SOUrce {CH<x>}
    - TRIGger:A:TRANsition:SOUrce?
    - TRIGger:A:TRANsition:WHEn {SLOWer|FASTer|EQual|UNEQual}
    - TRIGger:A:TRANsition:WHEn?
    - TRIGger:A:TRANsition?
    - TRIGger:A:TYPe {EDGe|LOGIc|PULSe|BUS|VIDeo}
    - TRIGger:A:TYPe?
    - TRIGger:A:UPPerthreshold:CH<x> {<NR3>|ECL|TTL}
    - TRIGger:A:UPPerthreshold:CH<x>?
    - TRIGger:A:UPPerthreshold:RF {<NR3>}
    - TRIGger:A:UPPerthreshold:RF?
    - TRIGger:A:VIDeo:CUSTom:FORMat {INTERLAced|PROGressive}
    - TRIGger:A:VIDeo:CUSTom:FORMat?
    - TRIGger:A:VIDeo:CUSTom:LINEPeriod <NR3>
    - TRIGger:A:VIDeo:CUSTom:LINEPeriod?
    - TRIGger:A:VIDeo:CUSTom:SYNCInterval <NR3>
    - TRIGger:A:VIDeo:CUSTom:SYNCInterval?
    - TRIGger:A:VIDeo:CUSTom:TYPe {INTERLAced|PROGressive}
    - TRIGger:A:VIDeo:CUSTom:TYPe?
    - TRIGger:A:VIDeo:FIELD {ODD|EVEN|ALLFields|ALLLines|NUMERic}
    - TRIGger:A:VIDeo:FIELD?
    - TRIGger:A:VIDeo:HOLDoff:FIELD <NR3>
    - TRIGger:A:VIDeo:HOLDoff:FIELD?
    - TRIGger:A:VIDeo:LINE <NR1>
    - TRIGger:A:VIDeo:LINE?
    - TRIGger:A:VIDeo:POLarity {NEGative|POSitive}
    - TRIGger:A:VIDeo:POLarity?
    - TRIGger:A:VIDeo:SOUrce {CH<x>}
    - TRIGger:A:VIDeo:SOUrce?
    - TRIGger:A:VIDeo:STANdard {NTSc|PAL|SECAM|BILevelcustom|TRILevelcustom|HD480P60|HD576P50|HD720P30|HD720P50|HD720P60|HD875I60|HD1080P24|HD1080SF24|HD1080I50|HD1080I60|HD1080P25|HD1080P30|HD1080P50|HD1080P60}
    - TRIGger:A:VIDeo:STANdard?
    - TRIGger:A:VIDeo:SYNC {ODD|EVEN|ALLFields|ALLLines|NUMERic}
    - TRIGger:A:VIDeo:SYNC?
    - TRIGger:A:VIDeo?
    - TRIGger:A?
    - TRIGger:B SETLevel
    - TRIGger:B:BY {EVENTS|TIMe}
    - TRIGger:B:BY?
    - TRIGger:B:EDGE:COUPling {DC|HFRej|LFRej|NOISErej}
    - TRIGger:B:EDGE:COUPling?
    - TRIGger:B:EDGE:SLOpe {RISe|FALL}
    - TRIGger:B:EDGE:SLOpe?
    - TRIGger:B:EDGE:SOUrce {CH<x>|AUX|LINE|RF}
    - TRIGger:B:EDGE:SOUrce?
    - TRIGger:B:EDGE?
    - TRIGger:B:EVENTS:COUNt <NR1>
    - TRIGger:B:EVENTS:COUNt?
    - TRIGger:B:EVENTS?
    - TRIGger:B:LEVel {TTL|<NR3>}
    - TRIGger:B:LEVel:CH<x> {ECL|TTL|<NR3>}
    - TRIGger:B:LEVel:CH<x>?
    - TRIGger:B:LEVel:D<x> {ECL|TTL|<NR3>}
    - TRIGger:B:LEVel:D<x>?
    - TRIGger:B:LEVel?
    - TRIGger:B:LOWerthreshold:CH<x> {ECL|TTL|<NR3>}
    - TRIGger:B:LOWerthreshold:CH<x>?
    - TRIGger:B:LOWerthreshold:D<x> {<NR3>|ECL|TTL}
    - TRIGger:B:LOWerthreshold:D<x>?
    - TRIGger:B:STATE {ON|OFF|<NR1>}
    - TRIGger:B:STATE?
    - TRIGger:B:TIMe <NR3>
    - TRIGger:B:TIMe?
    - TRIGger:B:TYPe EDGE
    - TRIGger:B:TYPe?
    - TRIGger:B?
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


class TriggerBType(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:B:TYPe`` command.

    Description:
        - This command specifies the type of B trigger. The only supported B trigger type is EDGE.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B:TYPe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:B:TYPe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:B:TYPe EDGE
        - TRIGger:B:TYPe?
        ```

    Info:
        - ``EDGE`` sets the B trigger type to edge.
    """


class TriggerBTime(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:B:TIMe`` command.

    Description:
        - This command sets or queries B trigger delay time, in seconds. The B Trigger time applies
          only if ``TRIGger:B:BY`` is set to TIMe.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B:TIMe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B:TIMe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:B:TIMe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:B:TIMe <NR3>
        - TRIGger:B:TIMe?
        ```

    Info:
        - ``<NR3>`` is the B trigger delay time in seconds.
    """


class TriggerBState(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:B:STATE`` command.

    Description:
        - This command sets or queries the state of B trigger activity. If the B trigger state is
          on, the B trigger is part of the triggering sequence. If the B trigger state is off, then
          only the A trigger causes the trigger event.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:B:STATE value`` command.

    SCPI Syntax:
        ```
        - TRIGger:B:STATE {ON|OFF|<NR1>}
        - TRIGger:B:STATE?
        ```

    Info:
        - ``ON`` indicates that the B trigger is active and causes trigger events with the A
          trigger.
        - ``OFF`` indicates that only the A trigger causes trigger events.
        - ``<NR1>`` is an integer number. 0 turns off the B trigger; any other value activates the B
          trigger.
    """


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


class TriggerBLowerthresholdChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:B:LOWerthreshold:CH<x>`` command.

    Description:
        - This command specifies the B trigger lower threshold for the channel <x>, where x is the
          channel number. Each channel can have an independent level. Used in runt and transition
          triggers as the lower threshold. Used for all other trigger types as the single
          level/threshold.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B:LOWerthreshold:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B:LOWerthreshold:CH<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:B:LOWerthreshold:CH<x> value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:B:LOWerthreshold:CH<x> {ECL|TTL|<NR3>}
        - TRIGger:B:LOWerthreshold:CH<x>?
        ```

    Info:
        - ``ECL`` specifies a preset ECL high level of -1.3V.
        - ``TTL`` specifies a preset TTL high level of 1.4V.
        - ``<NR3>`` is a floating point number that specifies the threshold level, in volts.
    """


class TriggerBLowerthreshold(SCPICmdRead):
    """The ``TRIGger:B:LOWerthreshold`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B:LOWerthreshold?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B:LOWerthreshold?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``TRIGger:B:LOWerthreshold:CH<x>`` command.
        - ``.d``: The ``TRIGger:B:LOWerthreshold:D<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, TriggerBLowerthresholdChannel] = DefaultDictPassKeyToFactory(
            lambda x: TriggerBLowerthresholdChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._d: Dict[int, TriggerBLowerthresholdDigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: TriggerBLowerthresholdDigitalBit(device, f"{self._cmd_syntax}:D{x}")
        )

    @property
    def ch(self) -> Dict[int, TriggerBLowerthresholdChannel]:
        """Return the ``TRIGger:B:LOWerthreshold:CH<x>`` command.

        Description:
            - This command specifies the B trigger lower threshold for the channel <x>, where x is
              the channel number. Each channel can have an independent level. Used in runt and
              transition triggers as the lower threshold. Used for all other trigger types as the
              single level/threshold.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B:LOWerthreshold:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B:LOWerthreshold:CH<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:B:LOWerthreshold:CH<x> value`` command.

        SCPI Syntax:
            ```
            - TRIGger:B:LOWerthreshold:CH<x> {ECL|TTL|<NR3>}
            - TRIGger:B:LOWerthreshold:CH<x>?
            ```

        Info:
            - ``ECL`` specifies a preset ECL high level of -1.3V.
            - ``TTL`` specifies a preset TTL high level of 1.4V.
            - ``<NR3>`` is a floating point number that specifies the threshold level, in volts.
        """
        return self._ch

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


class TriggerBLevelChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:B:LEVel:CH<x>`` command.

    Description:
        - This command specifies the B trigger level for channel <x>, where x is the channel number.
          Each Channel can have an independent Level.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B:LEVel:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B:LEVel:CH<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:B:LEVel:CH<x> value`` command.

    SCPI Syntax:
        ```
        - TRIGger:B:LEVel:CH<x> {ECL|TTL|<NR3>}
        - TRIGger:B:LEVel:CH<x>?
        ```

    Info:
        - ``ECL`` specifies a preset ECL high level of -1.3V.
        - ``TTL`` specifies a preset TTL high level of 1.4V.
        - ``<NR3>`` is a floating point number that specifies the trigger level in user units
          (usually volts).
    """


class TriggerBLevel(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:B:LEVel`` command.

    Description:
        - This command specifies the level for the B trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B:LEVel?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B:LEVel?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:B:LEVel value`` command.

    SCPI Syntax:
        ```
        - TRIGger:B:LEVel {TTL|<NR3>}
        - TRIGger:B:LEVel?
        ```

    Info:
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
        - ``<NR3>`` is a floating point number that specifies the B trigger level, in volts.

    Properties:
        - ``.ch``: The ``TRIGger:B:LEVel:CH<x>`` command.
        - ``.d``: The ``TRIGger:B:LEVel:D<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, TriggerBLevelChannel] = DefaultDictPassKeyToFactory(
            lambda x: TriggerBLevelChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._d: Dict[int, TriggerBLevelDigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: TriggerBLevelDigitalBit(device, f"{self._cmd_syntax}:D{x}")
        )

    @property
    def ch(self) -> Dict[int, TriggerBLevelChannel]:
        """Return the ``TRIGger:B:LEVel:CH<x>`` command.

        Description:
            - This command specifies the B trigger level for channel <x>, where x is the channel
              number. Each Channel can have an independent Level.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B:LEVel:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B:LEVel:CH<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:B:LEVel:CH<x> value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:B:LEVel:CH<x> {ECL|TTL|<NR3>}
            - TRIGger:B:LEVel:CH<x>?
            ```

        Info:
            - ``ECL`` specifies a preset ECL high level of -1.3V.
            - ``TTL`` specifies a preset TTL high level of 1.4V.
            - ``<NR3>`` is a floating point number that specifies the trigger level in user units
              (usually volts).
        """
        return self._ch

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


class TriggerBEventsCount(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:B:EVENTS:COUNt`` command.

    Description:
        - This command sets or queries the number of events that must occur before the B trigger.
          The B trigger event count applies only if ``TRIGger:B:BY`` is set to EVENTS.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B:EVENTS:COUNt?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B:EVENTS:COUNt?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:B:EVENTS:COUNt value`` command.

    SCPI Syntax:
        ```
        - TRIGger:B:EVENTS:COUNt <NR1>
        - TRIGger:B:EVENTS:COUNt?
        ```

    Info:
        - ``<NR1>`` is the number of B trigger events, which can range from 1 to 65,471.
    """


class TriggerBEvents(SCPICmdRead):
    """The ``TRIGger:B:EVENTS`` command.

    Description:
        - Returns the current B trigger events parameter.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B:EVENTS?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B:EVENTS?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TRIGger:B:EVENTS?
        ```

    Properties:
        - ``.count``: The ``TRIGger:B:EVENTS:COUNt`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._count = TriggerBEventsCount(device, f"{self._cmd_syntax}:COUNt")

    @property
    def count(self) -> TriggerBEventsCount:
        """Return the ``TRIGger:B:EVENTS:COUNt`` command.

        Description:
            - This command sets or queries the number of events that must occur before the B
              trigger. The B trigger event count applies only if ``TRIGger:B:BY`` is set to EVENTS.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B:EVENTS:COUNt?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B:EVENTS:COUNt?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:B:EVENTS:COUNt value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:B:EVENTS:COUNt <NR1>
            - TRIGger:B:EVENTS:COUNt?
            ```

        Info:
            - ``<NR1>`` is the number of B trigger events, which can range from 1 to 65,471.
        """
        return self._count


class TriggerBEdgeSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:B:EDGE:SOUrce`` command.

    Description:
        - This command specifies the source for the B trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B:EDGE:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B:EDGE:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:B:EDGE:SOUrce value`` command.

    SCPI Syntax:
        ```
        - TRIGger:B:EDGE:SOUrce {CH<x>|AUX|LINE|RF}
        - TRIGger:B:EDGE:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the B trigger source.
        - ``AUX`` specifies an external trigger using the Aux In connector located on the front
          panel of the oscilloscope as the B trigger source. (For 2-channel MDO32 model only.).
        - ``LINE`` specifies the AC power line as the B trigger source.
    """


class TriggerBEdgeSlope(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:B:EDGE:SLOpe`` command.

    Description:
        - This command specifies the slope for the B trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B:EDGE:SLOpe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B:EDGE:SLOpe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:B:EDGE:SLOpe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:B:EDGE:SLOpe {RISe|FALL}
        - TRIGger:B:EDGE:SLOpe?
        ```

    Info:
        - ``RISe`` triggers on the rising or positive edge of a signal.
        - ``FALL`` triggers on the falling or negative edge of a signal.
    """


class TriggerBEdgeCoupling(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:B:EDGE:COUPling`` command.

    Description:
        - This command specifies the type of coupling for the B edge trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B:EDGE:COUPling?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B:EDGE:COUPling?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:B:EDGE:COUPling value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:B:EDGE:COUPling {DC|HFRej|LFRej|NOISErej}
        - TRIGger:B:EDGE:COUPling?
        ```

    Info:
        - ``DC`` selects DC trigger coupling.
        - ``HFRej`` selects high-frequency reject coupling.
        - ``LFRej`` selects low-frequency reject coupling.
        - ``NOISErej`` selects DC low sensitivity.
    """


class TriggerBEdge(SCPICmdRead):
    """The ``TRIGger:B:EDGE`` command.

    Description:
        - Returns the source, slope, and coupling for B trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B:EDGE?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B:EDGE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TRIGger:B:EDGE?
        ```

    Properties:
        - ``.coupling``: The ``TRIGger:B:EDGE:COUPling`` command.
        - ``.slope``: The ``TRIGger:B:EDGE:SLOpe`` command.
        - ``.source``: The ``TRIGger:B:EDGE:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._coupling = TriggerBEdgeCoupling(device, f"{self._cmd_syntax}:COUPling")
        self._slope = TriggerBEdgeSlope(device, f"{self._cmd_syntax}:SLOpe")
        self._source = TriggerBEdgeSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def coupling(self) -> TriggerBEdgeCoupling:
        """Return the ``TRIGger:B:EDGE:COUPling`` command.

        Description:
            - This command specifies the type of coupling for the B edge trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B:EDGE:COUPling?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B:EDGE:COUPling?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:B:EDGE:COUPling value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:B:EDGE:COUPling {DC|HFRej|LFRej|NOISErej}
            - TRIGger:B:EDGE:COUPling?
            ```

        Info:
            - ``DC`` selects DC trigger coupling.
            - ``HFRej`` selects high-frequency reject coupling.
            - ``LFRej`` selects low-frequency reject coupling.
            - ``NOISErej`` selects DC low sensitivity.
        """
        return self._coupling

    @property
    def slope(self) -> TriggerBEdgeSlope:
        """Return the ``TRIGger:B:EDGE:SLOpe`` command.

        Description:
            - This command specifies the slope for the B trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B:EDGE:SLOpe?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B:EDGE:SLOpe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:B:EDGE:SLOpe value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:B:EDGE:SLOpe {RISe|FALL}
            - TRIGger:B:EDGE:SLOpe?
            ```

        Info:
            - ``RISe`` triggers on the rising or positive edge of a signal.
            - ``FALL`` triggers on the falling or negative edge of a signal.
        """
        return self._slope

    @property
    def source(self) -> TriggerBEdgeSource:
        """Return the ``TRIGger:B:EDGE:SOUrce`` command.

        Description:
            - This command specifies the source for the B trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B:EDGE:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B:EDGE:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:B:EDGE:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:B:EDGE:SOUrce {CH<x>|AUX|LINE|RF}
            - TRIGger:B:EDGE:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the B trigger source.
            - ``AUX`` specifies an external trigger using the Aux In connector located on the front
              panel of the oscilloscope as the B trigger source. (For 2-channel MDO32 model only.).
            - ``LINE`` specifies the AC power line as the B trigger source.
        """
        return self._source


class TriggerBBy(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:B:BY`` command.

    Description:
        - This command selects or returns whether the B trigger occurs after a specified number of
          events or a specified period of time after the A trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B:BY?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B:BY?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:B:BY value`` command.

    SCPI Syntax:
        ```
        - TRIGger:B:BY {EVENTS|TIMe}
        - TRIGger:B:BY?
        ```

    Info:
        - ``EVENTS`` sets the B trigger to take place following a set number of trigger events after
          the A trigger occurs. The number of events is specified by ``TRIGger:B:EVENTS:COUNt``.
        - ``TIMe`` sets the B trigger to occur a set time after the A trigger event. The time period
          is specified by ``TRIGger:B:TIMe``.
    """


#  pylint: disable=too-many-instance-attributes
class TriggerB(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:B`` command.

    Description:
        - Sets the B trigger level to 50% of minimum and maximum. The query form of this command
          returns the B trigger parameters. This command is similar to selecting B Event (Delayed)
          Trigger Setup from the Trigger menu and then viewing the current setups.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:B?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:B?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:B value`` command.

    SCPI Syntax:
        ```
        - TRIGger:B SETLevel
        - TRIGger:B?
        ```

    Info:
        - ``SETLevel`` sets the B trigger level to 50% of MIN and MAX.

    Properties:
        - ``.by``: The ``TRIGger:B:BY`` command.
        - ``.edge``: The ``TRIGger:B:EDGE`` command.
        - ``.events``: The ``TRIGger:B:EVENTS`` command.
        - ``.level``: The ``TRIGger:B:LEVel`` command.
        - ``.lowerthreshold``: The ``TRIGger:B:LOWerthreshold`` command tree.
        - ``.state``: The ``TRIGger:B:STATE`` command.
        - ``.time``: The ``TRIGger:B:TIMe`` command.
        - ``.type``: The ``TRIGger:B:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._by = TriggerBBy(device, f"{self._cmd_syntax}:BY")
        self._edge = TriggerBEdge(device, f"{self._cmd_syntax}:EDGE")
        self._events = TriggerBEvents(device, f"{self._cmd_syntax}:EVENTS")
        self._level = TriggerBLevel(device, f"{self._cmd_syntax}:LEVel")
        self._lowerthreshold = TriggerBLowerthreshold(device, f"{self._cmd_syntax}:LOWerthreshold")
        self._state = TriggerBState(device, f"{self._cmd_syntax}:STATE")
        self._time = TriggerBTime(device, f"{self._cmd_syntax}:TIMe")
        self._type = TriggerBType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def by(self) -> TriggerBBy:
        """Return the ``TRIGger:B:BY`` command.

        Description:
            - This command selects or returns whether the B trigger occurs after a specified number
              of events or a specified period of time after the A trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B:BY?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B:BY?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:B:BY value`` command.

        SCPI Syntax:
            ```
            - TRIGger:B:BY {EVENTS|TIMe}
            - TRIGger:B:BY?
            ```

        Info:
            - ``EVENTS`` sets the B trigger to take place following a set number of trigger events
              after the A trigger occurs. The number of events is specified by
              ``TRIGger:B:EVENTS:COUNt``.
            - ``TIMe`` sets the B trigger to occur a set time after the A trigger event. The time
              period is specified by ``TRIGger:B:TIMe``.
        """
        return self._by

    @property
    def edge(self) -> TriggerBEdge:
        """Return the ``TRIGger:B:EDGE`` command.

        Description:
            - Returns the source, slope, and coupling for B trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B:EDGE?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B:EDGE?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TRIGger:B:EDGE?
            ```

        Sub-properties:
            - ``.coupling``: The ``TRIGger:B:EDGE:COUPling`` command.
            - ``.slope``: The ``TRIGger:B:EDGE:SLOpe`` command.
            - ``.source``: The ``TRIGger:B:EDGE:SOUrce`` command.
        """
        return self._edge

    @property
    def events(self) -> TriggerBEvents:
        """Return the ``TRIGger:B:EVENTS`` command.

        Description:
            - Returns the current B trigger events parameter.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B:EVENTS?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B:EVENTS?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TRIGger:B:EVENTS?
            ```

        Sub-properties:
            - ``.count``: The ``TRIGger:B:EVENTS:COUNt`` command.
        """
        return self._events

    @property
    def level(self) -> TriggerBLevel:
        """Return the ``TRIGger:B:LEVel`` command.

        Description:
            - This command specifies the level for the B trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B:LEVel?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B:LEVel?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:B:LEVel value`` command.

        SCPI Syntax:
            ```
            - TRIGger:B:LEVel {TTL|<NR3>}
            - TRIGger:B:LEVel?
            ```

        Info:
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
            - ``<NR3>`` is a floating point number that specifies the B trigger level, in volts.

        Sub-properties:
            - ``.ch``: The ``TRIGger:B:LEVel:CH<x>`` command.
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
            - ``.ch``: The ``TRIGger:B:LOWerthreshold:CH<x>`` command.
            - ``.d``: The ``TRIGger:B:LOWerthreshold:D<x>`` command.
        """
        return self._lowerthreshold

    @property
    def state(self) -> TriggerBState:
        """Return the ``TRIGger:B:STATE`` command.

        Description:
            - This command sets or queries the state of B trigger activity. If the B trigger state
              is on, the B trigger is part of the triggering sequence. If the B trigger state is
              off, then only the A trigger causes the trigger event.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B:STATE?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:B:STATE value`` command.

        SCPI Syntax:
            ```
            - TRIGger:B:STATE {ON|OFF|<NR1>}
            - TRIGger:B:STATE?
            ```

        Info:
            - ``ON`` indicates that the B trigger is active and causes trigger events with the A
              trigger.
            - ``OFF`` indicates that only the A trigger causes trigger events.
            - ``<NR1>`` is an integer number. 0 turns off the B trigger; any other value activates
              the B trigger.
        """
        return self._state

    @property
    def time(self) -> TriggerBTime:
        """Return the ``TRIGger:B:TIMe`` command.

        Description:
            - This command sets or queries B trigger delay time, in seconds. The B Trigger time
              applies only if ``TRIGger:B:BY`` is set to TIMe.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B:TIMe?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B:TIMe?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:B:TIMe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:B:TIMe <NR3>
            - TRIGger:B:TIMe?
            ```

        Info:
            - ``<NR3>`` is the B trigger delay time in seconds.
        """
        return self._time

    @property
    def type(self) -> TriggerBType:
        """Return the ``TRIGger:B:TYPe`` command.

        Description:
            - This command specifies the type of B trigger. The only supported B trigger type is
              EDGE.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B:TYPe?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:B:TYPe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:B:TYPe EDGE
            - TRIGger:B:TYPe?
            ```

        Info:
            - ``EDGE`` sets the B trigger type to edge.
        """
        return self._type


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
        - This command sets the standard to use for triggering on video signals.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:STANdard?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:STANdard?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:VIDeo:STANdard value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:VIDeo:STANdard {NTSc|PAL|SECAM|BILevelcustom|TRILevelcustom|HD480P60|HD576P50|HD720P30|HD720P50|HD720P60|HD875I60|HD1080P24|HD1080SF24|HD1080I50|HD1080I60|HD1080P25|HD1080P30|HD1080P50|HD1080P60}
        - TRIGger:A:VIDeo:STANdard?
        ```

    Info:
        - ``NTSc`` sets the oscilloscope to trigger on video signals that meet the NTSC
          525/60/``2:1`` standard (a line rate of 525 lines per frame and a field rate of 60 Hz).
        - ``PAL`` sets the oscilloscope to trigger on video signals that meet the NTSC
          625/50/``2:1`` standard (a line rate of 625 lines per frame and a field rate of 50 Hz).
        - ``SECAM`` sets the oscilloscope to trigger on video signals that meet the SECAM standard.
        - ``BILevelcustom`` sets the oscilloscope to trigger on video horizontal scan rate
          parameters defined by the.
        - ``TRILevelcustom`` sets the oscilloscope to trigger on video horizontal scan rate
          parameters defined by the.
        - ``HD480P60`` set the oscilloscope to trigger on an HDTV video signal that meets standards
          defined in the following table.
        - ``HD576P50`` set the oscilloscope to trigger on an HDTV video signal that meets standards
          defined in the following table.
        - ``HD720P30`` set the oscilloscope to trigger on an HDTV video signal that meets standards
          defined in the following table.
        - ``HD720P50`` set the oscilloscope to trigger on an HDTV video signal that meets standards
          defined in the following table.
        - ``HD720P60`` set the oscilloscope to trigger on an HDTV video signal that meets standards
          defined in the following table.
        - ``HD875I60`` set the oscilloscope to trigger on an HDTV video signal that meets standards
          defined in the following table.
        - ``HD1080P24`` set the oscilloscope to trigger on an HDTV video signal that meets standards
          defined in the following table.
        - ``HD1080SF24`` set the oscilloscope to trigger on an HDTV video signal that meets
          standards defined in the following table.
        - ``HD1080I50`` set the oscilloscope to trigger on an HDTV video signal that meets standards
          defined in the following table.
        - ``HD1080I60`` set the oscilloscope to trigger on an HDTV video signal that meets standards
          defined in the following table.
        - ``HD1080P25`` set the oscilloscope to trigger on an HDTV video signal that meets standards
          defined in the following table.
        - ``HD1080P30`` set the oscilloscope to trigger on an HDTV video signal that meets standards
          defined in the following table.
        - ``HD1080P50`` set the oscilloscope to trigger on an HDTV video signal that meets standards
          defined in the following table.
        - ``HD1080P60`` set the oscilloscope to trigger on an HDTV video signal that meets standards
          defined in the following table.
    """  # noqa: E501


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
        - This command sets the polarity to use for triggering on video signals.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:POLarity?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:VIDeo:POLarity value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:VIDeo:POLarity {NEGative|POSitive}
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
    """The ``TRIGger:A:VIDeo:CUSTom:TYPe`` command.

    Description:
        - This command sets the video trigger format (either interlaced or progressive) to use for
          triggering on video signals. To use this command, you must also set the video standard to
          BILevelcustom or TRILevelcustom (using ``TRIGGER:A:VIDEO:STANDARD``).

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:CUSTom:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:CUSTom:TYPe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:VIDeo:CUSTom:TYPe value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:VIDeo:CUSTom:TYPe {INTERLAced|PROGressive}
        - TRIGger:A:VIDeo:CUSTom:TYPe?
        ```

    Info:
        - ``INTERLAced`` argument sets the format to interlaced video lines.
        - ``PROGressive`` argument sets the format to progressive video lines.
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
        - This command sets the video trigger format (either interlaced or progressive) to use for
          triggering on video signals. To use this command, you must also set the video standard to
          BILevelcustom or TRILevelcustom (using ``TRIGGER:A:VIDEO:STANDARD``).

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
        - ``INTERLAced`` argument sets the format to interlaced video lines.
        - ``PROGressive`` argument sets the format to progressive video lines.
    """


class TriggerAVideoCustom(SCPICmdRead):
    """The ``TRIGger:A:VIDeo:CUSTom`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:CUSTom?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:CUSTom?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.lineperiod``: The ``TRIGger:A:VIDeo:CUSTom:LINEPeriod`` command.
        - ``.syncinterval``: The ``TRIGger:A:VIDeo:CUSTom:SYNCInterval`` command.
        - ``.format``: The ``TRIGger:A:VIDeo:CUSTom:FORMat`` command.
        - ``.type``: The ``TRIGger:A:VIDeo:CUSTom:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._lineperiod = TriggerAVideoCustomLineperiod(device, f"{self._cmd_syntax}:LINEPeriod")
        self._syncinterval = TriggerAVideoCustomSyncinterval(
            device, f"{self._cmd_syntax}:SYNCInterval"
        )
        self._format = TriggerAVideoCustomFormat(device, f"{self._cmd_syntax}:FORMat")
        self._type = TriggerAVideoCustomType(device, f"{self._cmd_syntax}:TYPe")

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
            - This command sets the video trigger format (either interlaced or progressive) to use
              for triggering on video signals. To use this command, you must also set the video
              standard to BILevelcustom or TRILevelcustom (using ``TRIGGER:A:VIDEO:STANDARD``).

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
            - ``INTERLAced`` argument sets the format to interlaced video lines.
            - ``PROGressive`` argument sets the format to progressive video lines.
        """
        return self._format

    @property
    def type(self) -> TriggerAVideoCustomType:
        """Return the ``TRIGger:A:VIDeo:CUSTom:TYPe`` command.

        Description:
            - This command sets the video trigger format (either interlaced or progressive) to use
              for triggering on video signals. To use this command, you must also set the video
              standard to BILevelcustom or TRILevelcustom (using ``TRIGGER:A:VIDEO:STANDARD``).

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:CUSTom:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:CUSTom:TYPe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:VIDeo:CUSTom:TYPe value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:VIDeo:CUSTom:TYPe {INTERLAced|PROGressive}
            - TRIGger:A:VIDeo:CUSTom:TYPe?
            ```

        Info:
            - ``INTERLAced`` argument sets the format to interlaced video lines.
            - ``PROGressive`` argument sets the format to progressive video lines.
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
        - ``.custom``: The ``TRIGger:A:VIDeo:CUSTom`` command tree.
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
        self._holdoff = TriggerAVideoHoldoff(device, f"{self._cmd_syntax}:HOLDoff")
        self._line = TriggerAVideoLine(device, f"{self._cmd_syntax}:LINE")
        self._polarity = TriggerAVideoPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = TriggerAVideoSource(device, f"{self._cmd_syntax}:SOUrce")
        self._standard = TriggerAVideoStandard(device, f"{self._cmd_syntax}:STANdard")
        self._sync = TriggerAVideoSync(device, f"{self._cmd_syntax}:SYNC")
        self._field = TriggerAVideoField(device, f"{self._cmd_syntax}:FIELD")

    @property
    def custom(self) -> TriggerAVideoCustom:
        """Return the ``TRIGger:A:VIDeo:CUSTom`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:CUSTom?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:CUSTom?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.lineperiod``: The ``TRIGger:A:VIDeo:CUSTom:LINEPeriod`` command.
            - ``.syncinterval``: The ``TRIGger:A:VIDeo:CUSTom:SYNCInterval`` command.
            - ``.format``: The ``TRIGger:A:VIDeo:CUSTom:FORMat`` command.
            - ``.type``: The ``TRIGger:A:VIDeo:CUSTom:TYPe`` command.
        """
        return self._custom

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
            - This command sets the polarity to use for triggering on video signals.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:POLarity?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:VIDeo:POLarity value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:VIDeo:POLarity {NEGative|POSitive}
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
            - This command sets the standard to use for triggering on video signals.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:VIDeo:STANdard?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:VIDeo:STANdard?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:VIDeo:STANdard value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:VIDeo:STANdard {NTSc|PAL|SECAM|BILevelcustom|TRILevelcustom|HD480P60|HD576P50|HD720P30|HD720P50|HD720P60|HD875I60|HD1080P24|HD1080SF24|HD1080I50|HD1080I60|HD1080P25|HD1080P30|HD1080P50|HD1080P60}
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
            - ``BILevelcustom`` sets the oscilloscope to trigger on video horizontal scan rate
              parameters defined by the.
            - ``TRILevelcustom`` sets the oscilloscope to trigger on video horizontal scan rate
              parameters defined by the.
            - ``HD480P60`` set the oscilloscope to trigger on an HDTV video signal that meets
              standards defined in the following table.
            - ``HD576P50`` set the oscilloscope to trigger on an HDTV video signal that meets
              standards defined in the following table.
            - ``HD720P30`` set the oscilloscope to trigger on an HDTV video signal that meets
              standards defined in the following table.
            - ``HD720P50`` set the oscilloscope to trigger on an HDTV video signal that meets
              standards defined in the following table.
            - ``HD720P60`` set the oscilloscope to trigger on an HDTV video signal that meets
              standards defined in the following table.
            - ``HD875I60`` set the oscilloscope to trigger on an HDTV video signal that meets
              standards defined in the following table.
            - ``HD1080P24`` set the oscilloscope to trigger on an HDTV video signal that meets
              standards defined in the following table.
            - ``HD1080SF24`` set the oscilloscope to trigger on an HDTV video signal that meets
              standards defined in the following table.
            - ``HD1080I50`` set the oscilloscope to trigger on an HDTV video signal that meets
              standards defined in the following table.
            - ``HD1080I60`` set the oscilloscope to trigger on an HDTV video signal that meets
              standards defined in the following table.
            - ``HD1080P25`` set the oscilloscope to trigger on an HDTV video signal that meets
              standards defined in the following table.
            - ``HD1080P30`` set the oscilloscope to trigger on an HDTV video signal that meets
              standards defined in the following table.
            - ``HD1080P50`` set the oscilloscope to trigger on an HDTV video signal that meets
              standards defined in the following table.
            - ``HD1080P60`` set the oscilloscope to trigger on an HDTV video signal that meets
              standards defined in the following table.
        """  # noqa: E501
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


class TriggerAUpperthresholdRf(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:UPPerthreshold:RF`` command.

    Description:
        - This command specifies the upper threshold when the internal RF power level is used during
          runt triggering. To specify the lower threshold for the RUNT trigger type as well as the
          single threshold for the Pulse and Timeout trigger types, use the command
          ``TRIGGER:A:LOWERTHRESHOLD:RF``. To choose the RUNT trigger type, use the command
          ``TRIGGER:A:PULSE:CLASS``. To specify RF power as a source during runt triggering, use
          ``TRIGGER:A:RUNT:SOURCE``.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:UPPerthreshold:RF?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:UPPerthreshold:RF?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:UPPerthreshold:RF value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:UPPerthreshold:RF {<NR3>}
        - TRIGger:A:UPPerthreshold:RF?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the threshold to use, in the currently
          selected RF units (using ``RF:UNITS``). The range is (ref level - 40 dBm) to (ref level +
          10 dBm), but never less than -65 dBm or more than +30 dBm.
    """


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
        - ``.rf``: The ``TRIGger:A:UPPerthreshold:RF`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, TriggerAUpperthresholdChannel] = DefaultDictPassKeyToFactory(
            lambda x: TriggerAUpperthresholdChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._rf = TriggerAUpperthresholdRf(device, f"{self._cmd_syntax}:RF")

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

    @property
    def rf(self) -> TriggerAUpperthresholdRf:
        """Return the ``TRIGger:A:UPPerthreshold:RF`` command.

        Description:
            - This command specifies the upper threshold when the internal RF power level is used
              during runt triggering. To specify the lower threshold for the RUNT trigger type as
              well as the single threshold for the Pulse and Timeout trigger types, use the command
              ``TRIGGER:A:LOWERTHRESHOLD:RF``. To choose the RUNT trigger type, use the command
              ``TRIGGER:A:PULSE:CLASS``. To specify RF power as a source during runt triggering, use
              ``TRIGGER:A:RUNT:SOURCE``.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:UPPerthreshold:RF?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:UPPerthreshold:RF?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:UPPerthreshold:RF value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:UPPerthreshold:RF {<NR3>}
            - TRIGger:A:UPPerthreshold:RF?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the threshold to use, in the
              currently selected RF units (using ``RF:UNITS``). The range is (ref level - 40 dBm) to
              (ref level + 10 dBm), but never less than -65 dBm or more than +30 dBm.
        """
        return self._rf


class TriggerAType(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:TYPe`` command.

    Description:
        - This command sets the type of A trigger (either edge, logic, pulse, bus or video). If you
          set the trigger type to LOGIc, you also need to set the logic trigger class (logic or
          setup/hold) using the command ``TRIGGER:A:LOGIC:CLASS``. If you set the trigger type to
          PULSe, you also need to set the pulse trigger class (either runt, width, transition or
          timeout), using the command ``TRIGGER:A:PULSE:CLASS``. If you set the trigger type to BUS,
          you also need to set the bus type (CAN, I 2 C, SPI, RS-232, Ethernet, MIL-STD-1553, LIN,
          USB, audio, FlexRay, or parallel) using the command ``TRIGGER:A:BUS``.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:TYPe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:TYPe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:TYPe {EDGe|LOGIc|PULSe|BUS|VIDeo}
        - TRIGger:A:TYPe?
        ```

    Info:
        - ``EDGe`` is the default trigger. A trigger event occurs when a signal passes through a
          specified voltage level in a specified direction and is controlled by the
          ``TRIGGER:A:EDGE`` commands.
        - ``LOGIc`` specifies that a trigger occurs when specified conditions are met and is
          controlled by the ``TRIGGER:A:LOGIC`` commands. This trigger type is equivalent to the
          logic and setup/hold triggers found in the user interface. Use ``TRIGGER:A:LOGIC:CLASS``
          to further select the logic trigger class (either LOGIC or SETHOLD).
        - ``PULSe`` specifies that a trigger occurs when a specified pulse is found. Use
          ``TRIGGER:A:PULSE:CLASS`` to further select the pulse trigger class (either runt, width,
          transition or timeout).
        - ``BUS`` specifies that a trigger occurs when a bus signal is found. Supports CAN, I2C,
          SPI, RS-232, Ethernet, MIL-STD-1553, LIN, USB, audio, FlexRay buses (with the appropriate
          application module installed) as well as parallel buses. Requires the installation of
          option 3-MSO. Use ``TRIGGER:A:BUS`` to set the bus type.
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
        - This command specifies the source for a transition trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:TRANsition:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:TRANsition:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:TRANsition:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:TRANsition:SOUrce {CH<x>}
        - TRIGger:A:TRANsition:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies one of the analog channels to be used as the source for a transition
          trigger.
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
            - This command specifies the source for a transition trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:TRANsition:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:TRANsition:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:TRANsition:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:TRANsition:SOUrce {CH<x>}
            - TRIGger:A:TRANsition:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies one of the analog channels to be used as the source for a
              transition trigger.
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


class TriggerATimeoutTime(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:TIMEOut:TIMe`` command.

    Description:
        - When triggering using the TIMEOut trigger type, this command specifies the timeout time,
          in seconds. This command is equivalent to selecting Timeout from the Trig menu and setting
          a value for Time Limit. The timeout trigger type is selected using
          ``TRIGGER:A:TYPE TIMEOut``

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:TIMEOut:TIMe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:TIMEOut:TIMe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:TIMEOut:TIMe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:TIMEOut:TIMe <NR3>
        - TRIGger:A:TIMEOut:TIMe?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the timeout time, in seconds.
    """


class TriggerATimeoutSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:TIMEOut:SOUrce`` command.

    Description:
        - When triggering using the TIMEOut trigger type, this command specifies the source. The
          available sources are live channels, the digital channels, the Aux Input connector (for
          2-channel MDO32 model only). The default is channel 1. The timeout trigger type is
          selected using ``TRIGGER:A:PULSE:CLASS TIMEOut``.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:TIMEOut:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:TIMEOut:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:TIMEOut:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:TIMEOut:SOUrce {CH<x>|LINE|AUX|D<x>|RF}
        - TRIGger:A:TIMEOut:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the timeout trigger source.
        - ``AUX`` specifies an external trigger using the Aux In connector located on the front
          panel of the oscilloscope. (For 2-channel MDO32 model only.).
        - ``LINE`` specifies the AC line as the timeout trigger source.
        - ``D<x>`` specifies a digital channel as the timeout trigger source. (Requires option
          3-MSO.).
    """


class TriggerATimeoutPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:TIMEOut:POLarity`` command.

    Description:
        - When triggering using the TIMEOut trigger type, this commands specifies the polarity to be
          used.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:TIMEOut:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:TIMEOut:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:TIMEOut:POLarity value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:TIMEOut:POLarity {STAYSHigh|STAYSLow|EITher}
        - TRIGger:A:TIMEOut:POLarity?
        ```

    Info:
        - ``STAYSHigh`` . Trigger when the signal stays high during the timeout time specified by
          the command ``TRIGGER:A:TIMEOUT:TIME``.
        - ``STAYSLow`` . Trigger when the signal stays low during the timeout time specified by the
          command ``TRIGGER:A:TIMEOUT:TIME``.
        - ``EITher`` . Trigger when the signal is either high or low during the timeout time
          specified by the command ``TRIGGER:A:TIMEOUT:TIME``.
    """


class TriggerATimeout(SCPICmdRead):
    """The ``TRIGger:A:TIMEOut`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:TIMEOut?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:TIMEOut?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.polarity``: The ``TRIGger:A:TIMEOut:POLarity`` command.
        - ``.source``: The ``TRIGger:A:TIMEOut:SOUrce`` command.
        - ``.time``: The ``TRIGger:A:TIMEOut:TIMe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = TriggerATimeoutPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = TriggerATimeoutSource(device, f"{self._cmd_syntax}:SOUrce")
        self._time = TriggerATimeoutTime(device, f"{self._cmd_syntax}:TIMe")

    @property
    def polarity(self) -> TriggerATimeoutPolarity:
        """Return the ``TRIGger:A:TIMEOut:POLarity`` command.

        Description:
            - When triggering using the TIMEOut trigger type, this commands specifies the polarity
              to be used.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:TIMEOut:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:TIMEOut:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:TIMEOut:POLarity value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:TIMEOut:POLarity {STAYSHigh|STAYSLow|EITher}
            - TRIGger:A:TIMEOut:POLarity?
            ```

        Info:
            - ``STAYSHigh`` . Trigger when the signal stays high during the timeout time specified
              by the command ``TRIGGER:A:TIMEOUT:TIME``.
            - ``STAYSLow`` . Trigger when the signal stays low during the timeout time specified by
              the command ``TRIGGER:A:TIMEOUT:TIME``.
            - ``EITher`` . Trigger when the signal is either high or low during the timeout time
              specified by the command ``TRIGGER:A:TIMEOUT:TIME``.
        """
        return self._polarity

    @property
    def source(self) -> TriggerATimeoutSource:
        """Return the ``TRIGger:A:TIMEOut:SOUrce`` command.

        Description:
            - When triggering using the TIMEOut trigger type, this command specifies the source. The
              available sources are live channels, the digital channels, the Aux Input connector
              (for 2-channel MDO32 model only). The default is channel 1. The timeout trigger type
              is selected using ``TRIGGER:A:PULSE:CLASS TIMEOut``.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:TIMEOut:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:TIMEOut:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:TIMEOut:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:TIMEOut:SOUrce {CH<x>|LINE|AUX|D<x>|RF}
            - TRIGger:A:TIMEOut:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the timeout trigger source.
            - ``AUX`` specifies an external trigger using the Aux In connector located on the front
              panel of the oscilloscope. (For 2-channel MDO32 model only.).
            - ``LINE`` specifies the AC line as the timeout trigger source.
            - ``D<x>`` specifies a digital channel as the timeout trigger source. (Requires option
              3-MSO.).
        """
        return self._source

    @property
    def time(self) -> TriggerATimeoutTime:
        """Return the ``TRIGger:A:TIMEOut:TIMe`` command.

        Description:
            - When triggering using the TIMEOut trigger type, this command specifies the timeout
              time, in seconds. This command is equivalent to selecting Timeout from the Trig menu
              and setting a value for Time Limit. The timeout trigger type is selected using
              ``TRIGGER:A:TYPE TIMEOut``

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:TIMEOut:TIMe?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:TIMEOut:TIMe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:TIMEOut:TIMe value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:TIMEOut:TIMe <NR3>
            - TRIGger:A:TIMEOut:TIMe?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the timeout time, in seconds.
        """
        return self._time


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
        - This command specifies the data voltage threshold for setup and hold trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:DATa:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:DATa:THReshold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:SETHold:DATa:THReshold value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:SETHold:DATa:THReshold {<NR3>|TTL}
        - TRIGger:A:SETHold:DATa:THReshold?
        ```

    Info:
        - ``TTL`` specifies the preset TTL high level of 1.4 V.
        - ``<NR3>`` is a floating point number that specifies the setup and hold data level, in
          volts.
    """


class TriggerASetholdDataSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:SETHold:DATa:SOUrce`` command.

    Description:
        - This command specifies the data source or sources for setup and hold triggering. You can
          specify any combination of sources as long as none of them are also the clock source.
          Requires installation of option 3-MSO, which enables you to specify any combination of
          CH1-CH4 and D0-D15 as the data sources. For 2-channel MDO32, you can also use Aux Input.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:DATa:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:DATa:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:SETHold:DATa:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:SETHold:DATa:SOUrce {CH<x>|D<x>|AUX}
        - TRIGger:A:SETHold:DATa:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog input channel as the data source for the setup and hold
          trigger.
        - ``D<x>`` specifies a digital channel as the source. Requires option 3-MSO.
        - ``AUX`` specifies an external trigger using the Aux In connector located on the front
          panel of the oscilloscope. (For 2-channel MDO32 only.).
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
            - This command specifies the data source or sources for setup and hold triggering. You
              can specify any combination of sources as long as none of them are also the clock
              source. Requires installation of option 3-MSO, which enables you to specify any
              combination of CH1-CH4 and D0-D15 as the data sources. For 2-channel MDO32, you can
              also use Aux Input.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:DATa:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:DATa:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:SETHold:DATa:SOUrce value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:SETHold:DATa:SOUrce {CH<x>|D<x>|AUX}
            - TRIGger:A:SETHold:DATa:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog input channel as the data source for the setup and hold
              trigger.
            - ``D<x>`` specifies a digital channel as the source. Requires option 3-MSO.
            - ``AUX`` specifies an external trigger using the Aux In connector located on the front
              panel of the oscilloscope. (For 2-channel MDO32 only.).
        """
        return self._source

    @property
    def threshold(self) -> TriggerASetholdDataThreshold:
        """Return the ``TRIGger:A:SETHold:DATa:THReshold`` command.

        Description:
            - This command specifies the data voltage threshold for setup and hold trigger.

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
            - TRIGger:A:SETHold:DATa:THReshold {<NR3>|TTL}
            - TRIGger:A:SETHold:DATa:THReshold?
            ```

        Info:
            - ``TTL`` specifies the preset TTL high level of 1.4 V.
            - ``<NR3>`` is a floating point number that specifies the setup and hold data level, in
              volts.
        """
        return self._threshold


class TriggerASetholdClockThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:SETHold:CLOCk:THReshold`` command.

    Description:
        - This command specifies the clock voltage threshold for the setup and hold trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:CLOCk:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:CLOCk:THReshold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:SETHold:CLOCk:THReshold value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:SETHold:CLOCk:THReshold {<NR3>|TTL}
        - TRIGger:A:SETHold:CLOCk:THReshold?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the clock level, in volts.
        - ``TTL`` specifies a preset TTL high level of 1.4 V.
    """


class TriggerASetholdClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:SETHold:CLOCk:SOUrce`` command.

    Description:
        - This command specifies the clock source for the setup and hold triggering. You cannot
          specify the same source for both clock and data.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:CLOCk:SOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:SETHold:CLOCk:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:SETHold:CLOCk:SOUrce {CH<x>|D<x>|AUX}
        - TRIGger:A:SETHold:CLOCk:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies the analog channel to use as the clock source waveform.
        - ``D<x>`` specifies the digital channel to use as the clock source waveform. (Requires
          option 3-MSO.).
        - ``AUX`` specifies an external trigger using the Aux In connector located on the front
          panel of the oscilloscope. (Available for 2-channel MDO32, as it has an Aux Input
          connector.).
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
            - This command specifies the clock source for the setup and hold triggering. You cannot
              specify the same source for both clock and data.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:CLOCk:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:CLOCk:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:SETHold:CLOCk:SOUrce value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:SETHold:CLOCk:SOUrce {CH<x>|D<x>|AUX}
            - TRIGger:A:SETHold:CLOCk:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies the analog channel to use as the clock source waveform.
            - ``D<x>`` specifies the digital channel to use as the clock source waveform. (Requires
              option 3-MSO.).
            - ``AUX`` specifies an external trigger using the Aux In connector located on the front
              panel of the oscilloscope. (Available for 2-channel MDO32, as it has an Aux Input
              connector.).
        """
        return self._source

    @property
    def threshold(self) -> TriggerASetholdClockThreshold:
        """Return the ``TRIGger:A:SETHold:CLOCk:THReshold`` command.

        Description:
            - This command specifies the clock voltage threshold for the setup and hold trigger.

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
            - TRIGger:A:SETHold:CLOCk:THReshold {<NR3>|TTL}
            - TRIGger:A:SETHold:CLOCk:THReshold?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the clock level, in volts.
            - ``TTL`` specifies a preset TTL high level of 1.4 V.
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
        - This command specifies the source waveform for the A runt trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:RUNT:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:RUNT:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:RUNT:SOUrce value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:RUNT:SOUrce {CH<x>|RF}
        - TRIGger:A:RUNT:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies the analog channel number to use as the source waveform for the runt
          trigger. To specify the threshold levels when using CH1-CH4 as the source, use
          ``TRIGGER:A:LOWERTHRESHOLD:CHX`` and ``TRIGGER:A:UPPERTHRESHOLD:CHX``. x has a minimum of
          1 and a maximum of 4.
        - ``RF`` specifies the internal RF power level as the source (MDO4000/B/C models only, and
          requires installation of an MDO4TRIG application module.) To specify the threshold levels
          when using RF power level as the source, use ``TRIGGER:A:LOWERTHRESHOLD:RF`` and
          ``TRIGGER:A:UPPERTHRESHOLD:RF``.
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
            - This command specifies the source waveform for the A runt trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:RUNT:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:RUNT:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:RUNT:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:RUNT:SOUrce {CH<x>|RF}
            - TRIGger:A:RUNT:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies the analog channel number to use as the source waveform for the
              runt trigger. To specify the threshold levels when using CH1-CH4 as the source, use
              ``TRIGGER:A:LOWERTHRESHOLD:CHX`` and ``TRIGGER:A:UPPERTHRESHOLD:CHX``. x has a minimum
              of 1 and a maximum of 4.
            - ``RF`` specifies the internal RF power level as the source (MDO4000/B/C models only,
              and requires installation of an MDO4TRIG application module.) To specify the threshold
              levels when using RF power level as the source, use ``TRIGGER:A:LOWERTHRESHOLD:RF``
              and ``TRIGGER:A:UPPERTHRESHOLD:RF``.
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
        - This command specifies the source for a transition trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:RISEFall:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:RISEFall:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:RISEFall:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:RISEFall:SOUrce {CH<x>}
        - TRIGger:A:RISEFall:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies one of the analog channels to be used as the source for a transition
          trigger.
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
            - This command specifies the source for a transition trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:RISEFall:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:RISEFall:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:RISEFall:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:RISEFall:SOUrce {CH<x>}
            - TRIGger:A:RISEFall:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies one of the analog channels to be used as the source for a
              transition trigger.
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
        - This command specifies which kind of pulse to trigger on (either runt, width, transition
          (rise/fall or slew rate) or timeout). You also need to set the trigger type to PULSe using
          the command ``TRIGGER:A:TYPE``. To set the trigger source for a pulse trigger, use
          ``TRIGGER:A:RUNT:SOURCE``, ``TRIGGER:A:PULSEWIDTH:SOURCE``, , or
          ``TRIGGER:A:TIMEOUT:SOURCE``. To set the trigger voltage threshold level for a pulse
          trigger, use ``TRIGGER:A:LEVEL:AUXIN``, ``TRIGGER:A:LEVEL:CHX``, or
          ``TRIGGER:A:LEVEL:DX``.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:PULse:CLAss?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULse:CLAss?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:PULse:CLAss value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:PULse:CLAss {RUNt|WIDth|TRANsition|TIMEOut}
        - TRIGger:A:PULse:CLAss?
        ```

    Info:
        - ``RUNt`` triggers when a pulse crosses the first preset voltage threshold but does not
          cross the second preset threshold before recrossing the first. Use with the command
          ``TRIGGER:A:RUNT:SOURCE``, ``TRIGGER:A:RUNT:POLARITY``, ``TRIGGER:A:RUNT:WHEN``, and
          ``TRIGGER:A:RUNT:WIDTH``.
        - ``WIDth`` triggers when a pulse is found that has the specified width or duration and is
          either inside or outside the specified time limits. Use with the commands
          ``TRIGGER:A:PULSEWIDTH:HIGHLIMIT``, ``TRIGGER:A:PULSEWIDTH:LOWLIMIT``,
          ``TRIGGER:A:PULSEWIDTH:POLARITY``, ``TRIGGER:A:PULSEWIDTH:SOURCE``,
          ``TRIGGER:A:PULSEWIDTH:WHEN``, and ``TRIGGER:A:PULSEWIDTH:WIDTH``.
        - ``TRANsition`` (AKA rise/fall or slew rate) triggers when a pulse crosses both thresholds
          in the same direction as the specified polarity and the transition time between the two
          threshold crossings is greater or less than the specified time delta. Use with the
          commands.
        - ``TIMEout`` triggers when no pulse is detected within a specified time. The signal stays
          above, below, or either above or below, a set value for a set amount of time. Use with the
          commands ``TRIGGER:A:TIMEOUT:TIME``, ``TRIGGER:A:TIMEOUT:POLARITY``,
          ``TRIGGER:A:TIMEOUT:SOURCE``.
    """


class TriggerAPulse(SCPICmdRead):
    """The ``TRIGger:A:PULse`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:PULse?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULse?`` query and raise an
          AssertionError if the returned value does not match ``value``.

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
            - This command specifies which kind of pulse to trigger on (either runt, width,
              transition (rise/fall or slew rate) or timeout). You also need to set the trigger type
              to PULSe using the command ``TRIGGER:A:TYPE``. To set the trigger source for a pulse
              trigger, use ``TRIGGER:A:RUNT:SOURCE``, ``TRIGGER:A:PULSEWIDTH:SOURCE``, , or
              ``TRIGGER:A:TIMEOUT:SOURCE``. To set the trigger voltage threshold level for a pulse
              trigger, use ``TRIGGER:A:LEVEL:AUXIN``, ``TRIGGER:A:LEVEL:CHX``, or
              ``TRIGGER:A:LEVEL:DX``.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:PULse:CLAss?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULse:CLAss?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:PULse:CLAss value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:PULse:CLAss {RUNt|WIDth|TRANsition|TIMEOut}
            - TRIGger:A:PULse:CLAss?
            ```

        Info:
            - ``RUNt`` triggers when a pulse crosses the first preset voltage threshold but does not
              cross the second preset threshold before recrossing the first. Use with the command
              ``TRIGGER:A:RUNT:SOURCE``, ``TRIGGER:A:RUNT:POLARITY``, ``TRIGGER:A:RUNT:WHEN``, and
              ``TRIGGER:A:RUNT:WIDTH``.
            - ``WIDth`` triggers when a pulse is found that has the specified width or duration and
              is either inside or outside the specified time limits. Use with the commands
              ``TRIGGER:A:PULSEWIDTH:HIGHLIMIT``, ``TRIGGER:A:PULSEWIDTH:LOWLIMIT``,
              ``TRIGGER:A:PULSEWIDTH:POLARITY``, ``TRIGGER:A:PULSEWIDTH:SOURCE``,
              ``TRIGGER:A:PULSEWIDTH:WHEN``, and ``TRIGGER:A:PULSEWIDTH:WIDTH``.
            - ``TRANsition`` (AKA rise/fall or slew rate) triggers when a pulse crosses both
              thresholds in the same direction as the specified polarity and the transition time
              between the two threshold crossings is greater or less than the specified time delta.
              Use with the commands.
            - ``TIMEout`` triggers when no pulse is detected within a specified time. The signal
              stays above, below, or either above or below, a set value for a set amount of time.
              Use with the commands ``TRIGGER:A:TIMEOUT:TIME``, ``TRIGGER:A:TIMEOUT:POLARITY``,
              ``TRIGGER:A:TIMEOUT:SOURCE``.
        """
        return self._class


class TriggerAPulsewidthWidth(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:PULSEWidth:WIDth`` command.

    Description:
        - This command specifies the pulse width (duration), in seconds, for triggering on pulses
          whose widths are greater than, less than, equal to, or not equal to the specified value.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:WIDth?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:WIDth?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:PULSEWidth:WIDth value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:PULSEWidth:WIDth <NR3>
        - TRIGger:A:PULSEWidth:WIDth?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the pulse width in seconds.
    """


class TriggerAPulsewidthWhen(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:PULSEWidth:WHEn`` command.

    Description:
        - This command specifies to trigger when a pulse is detected with a width (duration) that is
          less than, greater than, equal to, or unequal to a specified value (set using
          ``TRIGGER:A:PULSEWIDTH:LOWLIMIT``), OR whose width falls outside of or within a specified
          range of two values (set using ``TRIGGER:A:PULSEWIDTH:LOWLIMIT`` and
          ``TRIGGER:A:PULSEWIDTH:HIGHLIMIT``).

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:WHEn?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:WHEn?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:PULSEWidth:WHEn value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:PULSEWidth:WHEn {LESSthan|MOREthan|EQual|UNEQual|WIThin|OUTside}
        - TRIGger:A:PULSEWidth:WHEn?
        ```

    Info:
        - ``LESSthan`` causes a trigger when a pulse is detected with a width less than the time set
          by the ``TRIGGER:A:PULSEWIDTH:LOWLIMIT`` command.
        - ``MOREthan`` causes a trigger when a pulse is detected with a width greater than the time
          set by the ``TRIGGER:A:PULSEWIDTH:LOWLIMIT`` command.
        - ``EQual`` causes a trigger when a pulse is detected with a width equal to the time period
          specified in ``TRIGGER:A:PULSEWIDTH:LOWLIMIT`` within a ±5% tolerance.
        - ``UNEQual`` causes a trigger when a pulse is detected with a width greater than or less
          than (but not equal) the time period specified in ``TRIGGER:A:PULSEWIDTH:LOWLIMIT`` within
          a ±5% tolerance.
        - ``WIThin`` causes a trigger when a pulse is detected that is within a range set by two
          values.
        - ``OUTside`` causes a trigger when a pulse is detected that is outside of a range set by
          two values.
    """


class TriggerAPulsewidthSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:PULSEWidth:SOUrce`` command.

    Description:
        - This command specifies the source waveform for a pulse width trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:PULSEWidth:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:PULSEWidth:SOUrce {CH<x>|LINE|AUX|D<x>|RF}
        - TRIGger:A:PULSEWidth:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog input channel as the pulse-width trigger source.
        - ``AUX`` specifies an external trigger using the Aux In connector located on the front
          panel of the oscilloscope. (Only for 2-channel model MDO32.).
        - ``LINE`` specifies AC line voltage as the trigger source.
        - ``D<x>`` specifies a digital channel as the trigger source.
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


class TriggerAPulsewidthLowlimit(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:PULSEWidth:LOWLimit`` command.

    Description:
        - This command specifies the lower limit to use, in seconds, when triggering on detection of
          a pulse whose duration is inside or outside a range of two values. (Use
          ``TRIGGER:A:PULSEWIDTH:HIGHLIMIT`` to specify the upper limit of the range.) This command
          also specifies the single limit to use, in seconds, when triggering on detection of a
          pulse whose duration is less than, greater than, equal to, or not equal to this time
          limit.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:LOWLimit?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:LOWLimit?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:PULSEWidth:LOWLimit value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:PULSEWidth:LOWLimit <NR3>
        - TRIGger:A:PULSEWidth:LOWLimit?
        ```

    Info:
        - ``<NR3>`` is a floating point number that represents the lower value of the range.
    """


class TriggerAPulsewidthHighlimit(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:PULSEWidth:HIGHLimit`` command.

    Description:
        - This command specifies the upper limit to use, in seconds, when triggering on detection of
          a pulse whose duration is inside or outside a range of two values. (Use
          ``TRIGGER:A:PULSEWIDTH:LOWLIMIT`` to specify the lower value of the range.)

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:HIGHLimit?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:HIGHLimit?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:PULSEWidth:HIGHLimit value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:PULSEWidth:HIGHLimit <NR3>
        - TRIGger:A:PULSEWidth:HIGHLimit?
        ```

    Info:
        - ``<NR3>`` is a floating point number that represents the higher value of the range.
    """


class TriggerAPulsewidth(SCPICmdRead):
    """The ``TRIGger:A:PULSEWidth`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.highlimit``: The ``TRIGger:A:PULSEWidth:HIGHLimit`` command.
        - ``.lowlimit``: The ``TRIGger:A:PULSEWidth:LOWLimit`` command.
        - ``.polarity``: The ``TRIGger:A:PULSEWidth:POLarity`` command.
        - ``.source``: The ``TRIGger:A:PULSEWidth:SOUrce`` command.
        - ``.when``: The ``TRIGger:A:PULSEWidth:WHEn`` command.
        - ``.width``: The ``TRIGger:A:PULSEWidth:WIDth`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._highlimit = TriggerAPulsewidthHighlimit(device, f"{self._cmd_syntax}:HIGHLimit")
        self._lowlimit = TriggerAPulsewidthLowlimit(device, f"{self._cmd_syntax}:LOWLimit")
        self._polarity = TriggerAPulsewidthPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = TriggerAPulsewidthSource(device, f"{self._cmd_syntax}:SOUrce")
        self._when = TriggerAPulsewidthWhen(device, f"{self._cmd_syntax}:WHEn")
        self._width = TriggerAPulsewidthWidth(device, f"{self._cmd_syntax}:WIDth")

    @property
    def highlimit(self) -> TriggerAPulsewidthHighlimit:
        """Return the ``TRIGger:A:PULSEWidth:HIGHLimit`` command.

        Description:
            - This command specifies the upper limit to use, in seconds, when triggering on
              detection of a pulse whose duration is inside or outside a range of two values. (Use
              ``TRIGGER:A:PULSEWIDTH:LOWLIMIT`` to specify the lower value of the range.)

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:HIGHLimit?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:HIGHLimit?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:PULSEWidth:HIGHLimit value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:PULSEWidth:HIGHLimit <NR3>
            - TRIGger:A:PULSEWidth:HIGHLimit?
            ```

        Info:
            - ``<NR3>`` is a floating point number that represents the higher value of the range.
        """
        return self._highlimit

    @property
    def lowlimit(self) -> TriggerAPulsewidthLowlimit:
        """Return the ``TRIGger:A:PULSEWidth:LOWLimit`` command.

        Description:
            - This command specifies the lower limit to use, in seconds, when triggering on
              detection of a pulse whose duration is inside or outside a range of two values. (Use
              ``TRIGGER:A:PULSEWIDTH:HIGHLIMIT`` to specify the upper limit of the range.) This
              command also specifies the single limit to use, in seconds, when triggering on
              detection of a pulse whose duration is less than, greater than, equal to, or not equal
              to this time limit.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:LOWLimit?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:LOWLimit?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:PULSEWidth:LOWLimit value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:PULSEWidth:LOWLimit <NR3>
            - TRIGger:A:PULSEWidth:LOWLimit?
            ```

        Info:
            - ``<NR3>`` is a floating point number that represents the lower value of the range.
        """
        return self._lowlimit

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
            - This command specifies the source waveform for a pulse width trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:PULSEWidth:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:PULSEWidth:SOUrce {CH<x>|LINE|AUX|D<x>|RF}
            - TRIGger:A:PULSEWidth:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog input channel as the pulse-width trigger source.
            - ``AUX`` specifies an external trigger using the Aux In connector located on the front
              panel of the oscilloscope. (Only for 2-channel model MDO32.).
            - ``LINE`` specifies AC line voltage as the trigger source.
            - ``D<x>`` specifies a digital channel as the trigger source.
        """
        return self._source

    @property
    def when(self) -> TriggerAPulsewidthWhen:
        """Return the ``TRIGger:A:PULSEWidth:WHEn`` command.

        Description:
            - This command specifies to trigger when a pulse is detected with a width (duration)
              that is less than, greater than, equal to, or unequal to a specified value (set using
              ``TRIGGER:A:PULSEWIDTH:LOWLIMIT``), OR whose width falls outside of or within a
              specified range of two values (set using ``TRIGGER:A:PULSEWIDTH:LOWLIMIT`` and
              ``TRIGGER:A:PULSEWIDTH:HIGHLIMIT``).

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:WHEn?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:WHEn?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:PULSEWidth:WHEn value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:PULSEWidth:WHEn {LESSthan|MOREthan|EQual|UNEQual|WIThin|OUTside}
            - TRIGger:A:PULSEWidth:WHEn?
            ```

        Info:
            - ``LESSthan`` causes a trigger when a pulse is detected with a width less than the time
              set by the ``TRIGGER:A:PULSEWIDTH:LOWLIMIT`` command.
            - ``MOREthan`` causes a trigger when a pulse is detected with a width greater than the
              time set by the ``TRIGGER:A:PULSEWIDTH:LOWLIMIT`` command.
            - ``EQual`` causes a trigger when a pulse is detected with a width equal to the time
              period specified in ``TRIGGER:A:PULSEWIDTH:LOWLIMIT`` within a ±5% tolerance.
            - ``UNEQual`` causes a trigger when a pulse is detected with a width greater than or
              less than (but not equal) the time period specified in
              ``TRIGGER:A:PULSEWIDTH:LOWLIMIT`` within a ±5% tolerance.
            - ``WIThin`` causes a trigger when a pulse is detected that is within a range set by two
              values.
            - ``OUTside`` causes a trigger when a pulse is detected that is outside of a range set
              by two values.
        """
        return self._when

    @property
    def width(self) -> TriggerAPulsewidthWidth:
        """Return the ``TRIGger:A:PULSEWidth:WIDth`` command.

        Description:
            - This command specifies the pulse width (duration), in seconds, for triggering on
              pulses whose widths are greater than, less than, equal to, or not equal to the
              specified value.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:WIDth?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:WIDth?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:PULSEWidth:WIDth value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:PULSEWidth:WIDth <NR3>
            - TRIGger:A:PULSEWidth:WIDth?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the pulse width in seconds.
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


class TriggerALowerthresholdRf(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOWerthreshold:RF`` command.

    Description:
        - This command specifies the lower threshold when using the internal RF power level for a
          RUNT trigger, or the single threshold in the cases of the PULSE and TIMEOUT triggers. To
          specify the upper threshold for the internal RF power level for the RUNT trigger type, use
          the command ``TRIGGER:A:UPPERTHRESHOLD:RF``. To choose the RUNT trigger type, use the
          command ``TRIGGER:A:PULSE:CLASS``.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOWerthreshold:RF?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOWerthreshold:RF?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LOWerthreshold:RF value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOWerthreshold:RF {<NR3>}
        - TRIGger:A:LOWerthreshold:RF?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the threshold to use, in the currently
          selected RF units (using ``RF:UNITS``). The range is (ref level - 40 dBm) to (ref level +
          10 dBm), but never less than -65 dBm or more than +30 dBm.
    """


class TriggerALowerthresholdExt(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOWerthreshold:EXT`` command.

    Description:
        - This command specifies the lower threshold for the Aux Input connector. Used for the
          following trigger types: runt, transition.

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
        - ``<NR3>`` is a floating point number that specifies the threshold level in volts.
        - ``ECL`` specifies a preset ECL high level of -1.3V.
        - ``TTL`` specifies a preset TTL high level of 1.4V.
    """


class TriggerALowerthresholdDigitalBit(ValidatedDigitalBit, SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOWerthreshold:D<x>`` command.

    Description:
        - Sets the lower threshold for the digital channel selected. Each channel can have an
          independent level. Used in runt and transition as the lower threshold. Used for all other
          trigger types as the single level/threshold.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOWerthreshold:D<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOWerthreshold:D<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LOWerthreshold:D<x> value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOWerthreshold:D<x> {<NR3>|ECL|TTL}
        - TRIGger:A:LOWerthreshold:D<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the threshold voltage, in volts.
        - ``ECL`` specifies a preset ECL high level of -1.3V.
        - ``TTL`` specifies a preset TTL high level of 1.4V.
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
        - This command specifies the lower threshold for the Aux Input connector. Used for the
          following trigger types: runt, transition.

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
        - ``<NR3>`` is a floating point number that specifies the threshold level in volts.
        - ``ECL`` specifies a preset ECL high level of -1.3V.
        - ``TTL`` specifies a preset TTL high level of 1.4V.
    """


class TriggerALowerthreshold(SCPICmdRead):
    """The ``TRIGger:A:LOWerthreshold`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOWerthreshold?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOWerthreshold?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``TRIGger:A:LOWerthreshold:CH<x>`` command.
        - ``.d``: The ``TRIGger:A:LOWerthreshold:D<x>`` command.
        - ``.rf``: The ``TRIGger:A:LOWerthreshold:RF`` command.
        - ``.aux``: The ``TRIGger:A:LOWerthreshold:AUX`` command.
        - ``.ext``: The ``TRIGger:A:LOWerthreshold:EXT`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, TriggerALowerthresholdChannel] = DefaultDictPassKeyToFactory(
            lambda x: TriggerALowerthresholdChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._d: Dict[int, TriggerALowerthresholdDigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: TriggerALowerthresholdDigitalBit(device, f"{self._cmd_syntax}:D{x}")
        )
        self._rf = TriggerALowerthresholdRf(device, f"{self._cmd_syntax}:RF")
        self._aux = TriggerALowerthresholdAux(device, f"{self._cmd_syntax}:AUX")
        self._ext = TriggerALowerthresholdExt(device, f"{self._cmd_syntax}:EXT")

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
    def d(self) -> Dict[int, TriggerALowerthresholdDigitalBit]:
        """Return the ``TRIGger:A:LOWerthreshold:D<x>`` command.

        Description:
            - Sets the lower threshold for the digital channel selected. Each channel can have an
              independent level. Used in runt and transition as the lower threshold. Used for all
              other trigger types as the single level/threshold.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOWerthreshold:D<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOWerthreshold:D<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:LOWerthreshold:D<x> value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOWerthreshold:D<x> {<NR3>|ECL|TTL}
            - TRIGger:A:LOWerthreshold:D<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the threshold voltage, in volts.
            - ``ECL`` specifies a preset ECL high level of -1.3V.
            - ``TTL`` specifies a preset TTL high level of 1.4V.
        """
        return self._d

    @property
    def rf(self) -> TriggerALowerthresholdRf:
        """Return the ``TRIGger:A:LOWerthreshold:RF`` command.

        Description:
            - This command specifies the lower threshold when using the internal RF power level for
              a RUNT trigger, or the single threshold in the cases of the PULSE and TIMEOUT
              triggers. To specify the upper threshold for the internal RF power level for the RUNT
              trigger type, use the command ``TRIGGER:A:UPPERTHRESHOLD:RF``. To choose the RUNT
              trigger type, use the command ``TRIGGER:A:PULSE:CLASS``.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOWerthreshold:RF?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOWerthreshold:RF?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:LOWerthreshold:RF value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOWerthreshold:RF {<NR3>}
            - TRIGger:A:LOWerthreshold:RF?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the threshold to use, in the
              currently selected RF units (using ``RF:UNITS``). The range is (ref level - 40 dBm) to
              (ref level + 10 dBm), but never less than -65 dBm or more than +30 dBm.
        """
        return self._rf

    @property
    def aux(self) -> TriggerALowerthresholdAux:
        """Return the ``TRIGger:A:LOWerthreshold:AUX`` command.

        Description:
            - This command specifies the lower threshold for the Aux Input connector. Used for the
              following trigger types: runt, transition.

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
            - ``<NR3>`` is a floating point number that specifies the threshold level in volts.
            - ``ECL`` specifies a preset ECL high level of -1.3V.
            - ``TTL`` specifies a preset TTL high level of 1.4V.
        """
        return self._aux

    @property
    def ext(self) -> TriggerALowerthresholdExt:
        """Return the ``TRIGger:A:LOWerthreshold:EXT`` command.

        Description:
            - This command specifies the lower threshold for the Aux Input connector. Used for the
              following trigger types: runt, transition.

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
            - ``<NR3>`` is a floating point number that specifies the threshold level in volts.
            - ``ECL`` specifies a preset ECL high level of -1.3V.
            - ``TTL`` specifies a preset TTL high level of 1.4V.
        """
        return self._ext


class TriggerALogicThresholdRf(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOGIc:THReshold:RF`` command.

    Description:
        - This command specifies the threshold to use when the internal RF power level is the source
          for a logic trigger. It will affect all trigger types using the channel.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:THReshold:RF?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:THReshold:RF?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGIc:THReshold:RF value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc:THReshold:RF {<NR3>}
        - TRIGger:A:LOGIc:THReshold:RF?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the threshold to use, in the currently
          selected RF units (using ``RF:UNITS``). The range is (ref level - 40 dBm) to (ref level +
          10 dBm), but never less than -65 dBm or more than +30 dBm.
    """


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
        - This command sets or queries the trigger A logic threshold voltage for the specified
          channel x.

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
        - ``<NR3>`` is a floating point number that specifies the threshold voltage, in volts.
        - ``ECL`` specifies a preset ECL high level of -1.3V.
        - ``TTL`` specifies a preset TTL high level of 1.4V.
    """


class TriggerALogicThreshold(SCPICmdRead):
    """The ``TRIGger:A:LOGIc:THReshold`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:THReshold?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``TRIGger:A:LOGIc:THReshold:CH<x>`` command.
        - ``.d``: The ``TRIGger:A:LOGIc:THReshold:D<x>`` command.
        - ``.rf``: The ``TRIGger:A:LOGIc:THReshold:RF`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, TriggerALogicThresholdChannel] = DefaultDictPassKeyToFactory(
            lambda x: TriggerALogicThresholdChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._d: Dict[int, TriggerALogicThresholdDigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: TriggerALogicThresholdDigitalBit(device, f"{self._cmd_syntax}:D{x}")
        )
        self._rf = TriggerALogicThresholdRf(device, f"{self._cmd_syntax}:RF")

    @property
    def ch(self) -> Dict[int, TriggerALogicThresholdChannel]:
        """Return the ``TRIGger:A:LOGIc:THReshold:CH<x>`` command.

        Description:
            - This command sets or queries the trigger A logic threshold voltage for the specified
              channel x.

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
            - ``<NR3>`` is a floating point number that specifies the threshold voltage, in volts.
            - ``ECL`` specifies a preset ECL high level of -1.3V.
            - ``TTL`` specifies a preset TTL high level of 1.4V.
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

    @property
    def rf(self) -> TriggerALogicThresholdRf:
        """Return the ``TRIGger:A:LOGIc:THReshold:RF`` command.

        Description:
            - This command specifies the threshold to use when the internal RF power level is the
              source for a logic trigger. It will affect all trigger types using the channel.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:THReshold:RF?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:THReshold:RF?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:LOGIc:THReshold:RF value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGIc:THReshold:RF {<NR3>}
            - TRIGger:A:LOGIc:THReshold:RF?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the threshold to use, in the
              currently selected RF units (using ``RF:UNITS``). The range is (ref level - 40 dBm) to
              (ref level + 10 dBm), but never less than -65 dBm or more than +30 dBm.
        """
        return self._rf


class TriggerALogicPatternWhen(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOGIc:PATtern:WHEn`` command.

    Description:
        - This command specifies the pattern logic condition on which to trigger the oscilloscope.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:PATtern:WHEn?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:PATtern:WHEn?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGIc:PATtern:WHEn value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc:PATtern:WHEn {TRUe|FALSe|LESSthan|MOREthan|EQual|UNEQual}
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
    """


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
        - ``.when``: The ``TRIGger:A:LOGIc:PATtern:WHEn`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._deltatime = TriggerALogicPatternDeltatime(device, f"{self._cmd_syntax}:DELTatime")
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
    def when(self) -> TriggerALogicPatternWhen:
        """Return the ``TRIGger:A:LOGIc:PATtern:WHEn`` command.

        Description:
            - This command specifies the pattern logic condition on which to trigger the
              oscilloscope.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:PATtern:WHEn?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:PATtern:WHEn?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:LOGIc:PATtern:WHEn value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGIc:PATtern:WHEn {TRUe|FALSe|LESSthan|MOREthan|EQual|UNEQual}
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
        """
        return self._when


class TriggerALogicInputRf(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOGIc:INPut:RF`` command.

    Description:
        - This command specifies the logic level to use when the internal RF power level is the
          source for a logic pattern trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:INPut:RF?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:INPut:RF?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGIc:INPut:RF value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc:INPut:RF {HIGH|LOW|X}
        - TRIGger:A:LOGIc:INPut:RF?
        ```

    Info:
        - ``HIGH`` specifies to trigger on a high logic level.
        - ``LOW`` specifies to trigger on a low logic level.
        - ``X`` specifies a 'don't care' condition.
    """


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
        - This command specifies the channel to use as the clock source. The clock can be selected
          as NONE. A selection of None implies pattern trigger. Any other selection implies state
          trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:LOGIc:INPut:CLOCk:SOUrce value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc:INPut:CLOCk:SOUrce {CH<x>|D<x>|RF|NONE}
        - TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the clock source.
        - ``D<x>`` specifies a digital channel as the clock source. (Requires option 3-MSO.).
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
        - TRIGger:A:LOGIc:INPut:CLOCk:EDGE {FALL|RISe}
        - TRIGger:A:LOGIc:INPut:CLOCk:EDGE?
        ```

    Info:
        - ``RISe`` specifies to trigger on the rising or positive edge of a signal.
        - ``FALL`` specifies to trigger on the falling or negative edge of a signal.
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
            - TRIGger:A:LOGIc:INPut:CLOCk:EDGE {FALL|RISe}
            - TRIGger:A:LOGIc:INPut:CLOCk:EDGE?
            ```

        Info:
            - ``RISe`` specifies to trigger on the rising or positive edge of a signal.
            - ``FALL`` specifies to trigger on the falling or negative edge of a signal.
        """
        return self._edge

    @property
    def source(self) -> TriggerALogicInputClockSource:
        """Return the ``TRIGger:A:LOGIc:INPut:CLOCk:SOUrce`` command.

        Description:
            - This command specifies the channel to use as the clock source. The clock can be
              selected as NONE. A selection of None implies pattern trigger. Any other selection
              implies state trigger.

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
            - TRIGger:A:LOGIc:INPut:CLOCk:SOUrce {CH<x>|D<x>|RF|NONE}
            - TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the clock source.
            - ``D<x>`` specifies a digital channel as the clock source. (Requires option 3-MSO.).
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
        - ``.rf``: The ``TRIGger:A:LOGIc:INPut:RF`` command.
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
        self._rf = TriggerALogicInputRf(device, f"{self._cmd_syntax}:RF")

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

    @property
    def rf(self) -> TriggerALogicInputRf:
        """Return the ``TRIGger:A:LOGIc:INPut:RF`` command.

        Description:
            - This command specifies the logic level to use when the internal RF power level is the
              source for a logic pattern trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:INPut:RF?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:INPut:RF?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGIc:INPut:RF value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGIc:INPut:RF {HIGH|LOW|X}
            - TRIGger:A:LOGIc:INPut:RF?
            ```

        Info:
            - ``HIGH`` specifies to trigger on a high logic level.
            - ``LOW`` specifies to trigger on a low logic level.
            - ``X`` specifies a 'don't care' condition.
        """
        return self._rf


class TriggerALogicFunction(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOGIc:FUNCtion`` command.

    Description:
        - This command sets or queries the logical combination of the input channels for logic
          triggers. This command is equivalent to selecting Logic for the Trigger Type, and setting
          or viewing the Define Logic.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:FUNCtion?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:FUNCtion?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGIc:FUNCtion value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc:FUNCtion {AND|NANd|NOR|OR}
        - TRIGger:A:LOGIc:FUNCtion?
        ```

    Info:
        - ``AND`` specifies to trigger if all conditions are true.
        - ``NANd`` specifies to trigger if any of the conditions are false.
        - ``NOR`` specifies to trigger if all conditions are false.
        - ``OR`` specifies to trigger if any of the conditions are true.
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
            - This command sets or queries the logical combination of the input channels for logic
              triggers. This command is equivalent to selecting Logic for the Trigger Type, and
              setting or viewing the Define Logic.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:FUNCtion?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:FUNCtion?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGIc:FUNCtion value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGIc:FUNCtion {AND|NANd|NOR|OR}
            - TRIGger:A:LOGIc:FUNCtion?
            ```

        Info:
            - ``AND`` specifies to trigger if all conditions are true.
            - ``NANd`` specifies to trigger if any of the conditions are false.
            - ``NOR`` specifies to trigger if all conditions are false.
            - ``OR`` specifies to trigger if any of the conditions are true.
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
            - ``.rf``: The ``TRIGger:A:LOGIc:INPut:RF`` command.
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
            - ``.ch``: The ``TRIGger:A:LOGIc:THReshold:CH<x>`` command.
            - ``.d``: The ``TRIGger:A:LOGIc:THReshold:D<x>`` command.
            - ``.rf``: The ``TRIGger:A:LOGIc:THReshold:RF`` command.
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
        - This command sets the threshold voltage level to use for an Edge, Pulse Width, Runt or
          Rise/Fall (aka Transition, aka Slew Rate) trigger when triggering on an analog channel
          waveform. x can be 1 - 4. Each channel can have an independent trigger level.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LEVel:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LEVel:CH<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LEVel:CH<x> value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:LEVel:CH<x> {<NR3>|ECL|TTL}
        - TRIGger:A:LEVel:CH<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that sets the trigger threshold level, in Volts, for
          the specified analog channel.
        - ``ECL`` sets the threshold level to a preset ECL high level of -1.3V.
        - ``TTL`` sets the threshold level to a preset TTL high level of 1.4V.
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


class TriggerALevel(SCPICmdRead):
    """The ``TRIGger:A:LEVel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LEVel?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LEVel?`` query and raise an
          AssertionError if the returned value does not match ``value``.

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
            - This command sets the threshold voltage level to use for an Edge, Pulse Width, Runt or
              Rise/Fall (aka Transition, aka Slew Rate) trigger when triggering on an analog channel
              waveform. x can be 1 - 4. Each channel can have an independent trigger level.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LEVel:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LEVel:CH<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:LEVel:CH<x> value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:LEVel:CH<x> {<NR3>|ECL|TTL}
            - TRIGger:A:LEVel:CH<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that sets the trigger threshold level, in Volts,
              for the specified analog channel.
            - ``ECL`` sets the threshold level to a preset ECL high level of -1.3V.
            - ``TTL`` sets the threshold level to a preset TTL high level of 1.4V.
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
        - This command specifies the source for the A edge trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:EDGE:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:EDGE:SOUrce value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:EDGE:SOUrce {AUX|CH<x>|D<x>|LINE|RF}
        - TRIGger:A:EDGE:SOUrce?
        ```

    Info:
        - ``AUX`` specifies an external trigger using the auxiliary input connector located on the
          front panel of the oscilloscope. (For 2-channel MDO32 model only.).
        - ``CH<x>`` specifies an analog input channel as the A edge trigger source.
        - ``D<x>`` specifies a digital channel as the source (only with option 3-MSO installed).
        - ``LINE`` specifies the AC power line as the trigger source.
    """


class TriggerAEdgeSlope(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:EDGE:SLOpe`` command.

    Description:
        - This command specifies the slope for the A edge trigger: rising, falling or either.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:EDGE:SLOpe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE:SLOpe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:EDGE:SLOpe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:EDGE:SLOpe {RISe|FALL|EITHer}
        - TRIGger:A:EDGE:SLOpe?
        ```

    Info:
        - ``RISe`` specifies to trigger on the rising or positive edge of a signal.
        - ``FALL`` specifies to trigger on the falling or negative edge of a signal.
        - ``EITHer`` specifies to trigger on either the rising or falling edge of a signal.
    """


class TriggerAEdgeCoupling(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:EDGE:COUPling`` command.

    Description:
        - This command specifies the type of coupling for the A edge trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:EDGE:COUPling?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE:COUPling?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:EDGE:COUPling value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:EDGE:COUPling {AC|DC|HFRej|LFRej|NOISErej}
        - TRIGger:A:EDGE:COUPling?
        ```

    Info:
        - ``AC`` specifies AC trigger coupling.
        - ``DC`` specifies DC trigger coupling, which passes all input signals to the trigger
          circuitry.
        - ``HFRej`` specifies high-frequency rejection coupling, which attenuates signals above 50
          kHz before passing the signals to the trigger circuitry.
        - ``LFRej`` specifies low-frequency rejection coupling, which attenuates signals below 50
          kHz before passing the signals to the trigger circuitry.
        - ``NOISErej`` specifies noise-rejection coupling, which provides stable triggering by
          increasing the trigger hysteresis. Increased hysteresis reduces the trigger sensitivity to
          noise but may require greater trigger signal amplitude.
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
            - This command specifies the type of coupling for the A edge trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:EDGE:COUPling?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE:COUPling?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:EDGE:COUPling value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:EDGE:COUPling {AC|DC|HFRej|LFRej|NOISErej}
            - TRIGger:A:EDGE:COUPling?
            ```

        Info:
            - ``AC`` specifies AC trigger coupling.
            - ``DC`` specifies DC trigger coupling, which passes all input signals to the trigger
              circuitry.
            - ``HFRej`` specifies high-frequency rejection coupling, which attenuates signals above
              50 kHz before passing the signals to the trigger circuitry.
            - ``LFRej`` specifies low-frequency rejection coupling, which attenuates signals below
              50 kHz before passing the signals to the trigger circuitry.
            - ``NOISErej`` specifies noise-rejection coupling, which provides stable triggering by
              increasing the trigger hysteresis. Increased hysteresis reduces the trigger
              sensitivity to noise but may require greater trigger signal amplitude.
        """
        return self._coupling

    @property
    def slope(self) -> TriggerAEdgeSlope:
        """Return the ``TRIGger:A:EDGE:SLOpe`` command.

        Description:
            - This command specifies the slope for the A edge trigger: rising, falling or either.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:EDGE:SLOpe?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE:SLOpe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:EDGE:SLOpe value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:EDGE:SLOpe {RISe|FALL|EITHer}
            - TRIGger:A:EDGE:SLOpe?
            ```

        Info:
            - ``RISe`` specifies to trigger on the rising or positive edge of a signal.
            - ``FALL`` specifies to trigger on the falling or negative edge of a signal.
            - ``EITHer`` specifies to trigger on either the rising or falling edge of a signal.
        """
        return self._slope

    @property
    def source(self) -> TriggerAEdgeSource:
        """Return the ``TRIGger:A:EDGE:SOUrce`` command.

        Description:
            - This command specifies the source for the A edge trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:EDGE:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:EDGE:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:EDGE:SOUrce {AUX|CH<x>|D<x>|LINE|RF}
            - TRIGger:A:EDGE:SOUrce?
            ```

        Info:
            - ``AUX`` specifies an external trigger using the auxiliary input connector located on
              the front panel of the oscilloscope. (For 2-channel MDO32 model only.).
            - ``CH<x>`` specifies an analog input channel as the A edge trigger source.
            - ``D<x>`` specifies a digital channel as the source (only with option 3-MSO installed).
            - ``LINE`` specifies the AC power line as the trigger source.
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


class TriggerABusBItemUsbTokentype(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:TOKENType`` command.

    Description:
        - This command specifies the token type for the USB trigger. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:TOKENType?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:TOKENType?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:TOKENType value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:USB:TOKENType {ANY|SOF|OUT|IN|SETUP}
        - TRIGger:A:BUS:B<x>:USB:TOKENType?
        ```

    Info:
        - ``ANY``
        - ``SOF`` indicates a SOF (start-of-frame) token type.
        - ``OUT`` indicates an OUT token type.
        - ``IN`` indicates an IN token type.
        - ``SETUP`` indicates a SETUP token type.
    """


class TriggerABusBItemUsbSplitSeValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue`` command.

    Description:
        - When triggering on a high-speed USB split transaction, this command specifies the split
          transaction start/end bit value to trigger on. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue {NOCARE|FULLSPeed|LOWSPeed|ISOSTART|ISOMID|ISOEND|ISOALL}
        - TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue?
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


class TriggerABusBItemUsbSplitSe(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:SPLit:SE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit:SE?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit:SE?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemUsbSplitSeValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> TriggerABusBItemUsbSplitSeValue:
        """Return the ``TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue`` command.

        Description:
            - When triggering on a high-speed USB split transaction, this command specifies the
              split transaction start/end bit value to trigger on. B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue {NOCARE|FULLSPeed|LOWSPeed|ISOSTART|ISOMID|ISOEND|ISOALL}
            - TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue?
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


class TriggerABusBItemUsbSplitScValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue`` command.

    Description:
        - When triggering on a high-speed USB split transaction, this command specifies whether to
          trigger on the start or complete phase of the split transaction, based on the
          Start/Complete bit field value. (0 = Start, 1 = Complete). The default is NOCARE. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue {NOCARE|SSPLIT|CSPLIT}
        - TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue?
        ```

    Info:
        - ``NOCARE`` - trigger on either the start or complete phase of the split transaction.
        - ``SSPLIT`` - trigger on the start phase of the split transaction.
        - ``CSPLIT`` - trigger on the complete phase of the split transaction.
    """


class TriggerABusBItemUsbSplitSc(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:SPLit:SC`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit:SC?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit:SC?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemUsbSplitScValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> TriggerABusBItemUsbSplitScValue:
        """Return the ``TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue`` command.

        Description:
            - When triggering on a high-speed USB split transaction, this command specifies whether
              to trigger on the start or complete phase of the split transaction, based on the
              Start/Complete bit field value. (0 = Start, 1 = Complete). The default is NOCARE. B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue {NOCARE|SSPLIT|CSPLIT}
            - TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue?
            ```

        Info:
            - ``NOCARE`` - trigger on either the start or complete phase of the split transaction.
            - ``SSPLIT`` - trigger on the start phase of the split transaction.
            - ``CSPLIT`` - trigger on the complete phase of the split transaction.
        """
        return self._value


class TriggerABusBItemUsbSplitPortValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue`` command.

    Description:
        - When triggering on a high-speed USB split transaction, this command specifies the split
          transaction port address value to trigger on. The value can be up to 7 characters long.
          The default is all X's (don't care). B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue <QString>
        - TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue?
        ```

    Info:
        - ``QString`` is a quoted string of up to 7 characters. The valid characters are 0 and 1.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemUsbSplitPort(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:SPLit:PORT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit:PORT?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit:PORT?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemUsbSplitPortValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> TriggerABusBItemUsbSplitPortValue:
        """Return the ``TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue`` command.

        Description:
            - When triggering on a high-speed USB split transaction, this command specifies the
              split transaction port address value to trigger on. The value can be up to 7
              characters long. The default is all X's (don't care). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue <QString>
            - TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue?
            ```

        Info:
            - ``QString`` is a quoted string of up to 7 characters. The valid characters are 0 and
              1.
        """
        return self._value


class TriggerABusBItemUsbSplitHubValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue`` command.

    Description:
        - When triggering on a high-speed USB split transaction, this command specifies the split
          transaction hub address value to trigger on. The value can be up to 7 characters long. The
          default is all X's (don't care). B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue <QString>
        - TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue?
        ```

    Info:
        - ``QString`` is a quoted string of up to 7 characters. The valid characters are 0 and 1.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemUsbSplitHub(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:SPLit:HUB`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit:HUB?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit:HUB?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemUsbSplitHubValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> TriggerABusBItemUsbSplitHubValue:
        """Return the ``TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue`` command.

        Description:
            - When triggering on a high-speed USB split transaction, this command specifies the
              split transaction hub address value to trigger on. The value can be up to 7 characters
              long. The default is all X's (don't care). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue <QString>
            - TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue?
            ```

        Info:
            - ``QString`` is a quoted string of up to 7 characters. The valid characters are 0 and
              1.
        """
        return self._value


class TriggerABusBItemUsbSplitEtValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue`` command.

    Description:
        - When triggering on a high-speed USB split transaction, this command specifies the split
          transaction endpoint type value to trigger on. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue {NOCARE|CONTRol|ISOchronous|BULK|INTERRUPT}
        - TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue?
        ```

    Info:
        - ``NOCARE`` - any endpoint type.
        - ``CONTRol`` - control endpoint type.
        - ``ISOchronous`` - isochronous endpoint type.
        - ``BULK`` - bulk endpoint type (BULK-IN or BULK-OUT).
        - ``INTERRUPT`` - interrupt endpoint type (Interrupt-IN).
    """


class TriggerABusBItemUsbSplitEt(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:SPLit:ET`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit:ET?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit:ET?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemUsbSplitEtValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> TriggerABusBItemUsbSplitEtValue:
        """Return the ``TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue`` command.

        Description:
            - When triggering on a high-speed USB split transaction, this command specifies the
              split transaction endpoint type value to trigger on. B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue {NOCARE|CONTRol|ISOchronous|BULK|INTERRUPT}
            - TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue?
            ```

        Info:
            - ``NOCARE`` - any endpoint type.
            - ``CONTRol`` - control endpoint type.
            - ``ISOchronous`` - isochronous endpoint type.
            - ``BULK`` - bulk endpoint type (BULK-IN or BULK-OUT).
            - ``INTERRUPT`` - interrupt endpoint type (Interrupt-IN).
        """
        return self._value


class TriggerABusBItemUsbSplit(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:SPLit`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.et``: The ``TRIGger:A:BUS:B<x>:USB:SPLit:ET`` command tree.
        - ``.hub``: The ``TRIGger:A:BUS:B<x>:USB:SPLit:HUB`` command tree.
        - ``.port``: The ``TRIGger:A:BUS:B<x>:USB:SPLit:PORT`` command tree.
        - ``.sc``: The ``TRIGger:A:BUS:B<x>:USB:SPLit:SC`` command tree.
        - ``.se``: The ``TRIGger:A:BUS:B<x>:USB:SPLit:SE`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._et = TriggerABusBItemUsbSplitEt(device, f"{self._cmd_syntax}:ET")
        self._hub = TriggerABusBItemUsbSplitHub(device, f"{self._cmd_syntax}:HUB")
        self._port = TriggerABusBItemUsbSplitPort(device, f"{self._cmd_syntax}:PORT")
        self._sc = TriggerABusBItemUsbSplitSc(device, f"{self._cmd_syntax}:SC")
        self._se = TriggerABusBItemUsbSplitSe(device, f"{self._cmd_syntax}:SE")

    @property
    def et(self) -> TriggerABusBItemUsbSplitEt:
        """Return the ``TRIGger:A:BUS:B<x>:USB:SPLit:ET`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit:ET?``
              query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit:ET?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:USB:SPLit:ET:VALue`` command.
        """
        return self._et

    @property
    def hub(self) -> TriggerABusBItemUsbSplitHub:
        """Return the ``TRIGger:A:BUS:B<x>:USB:SPLit:HUB`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit:HUB?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:SPLit:HUB?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:USB:SPLit:HUB:VALue`` command.
        """
        return self._hub

    @property
    def port(self) -> TriggerABusBItemUsbSplitPort:
        """Return the ``TRIGger:A:BUS:B<x>:USB:SPLit:PORT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit:PORT?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:SPLit:PORT?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:USB:SPLit:PORT:VALue`` command.
        """
        return self._port

    @property
    def sc(self) -> TriggerABusBItemUsbSplitSc:
        """Return the ``TRIGger:A:BUS:B<x>:USB:SPLit:SC`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit:SC?``
              query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit:SC?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:USB:SPLit:SC:VALue`` command.
        """
        return self._sc

    @property
    def se(self) -> TriggerABusBItemUsbSplitSe:
        """Return the ``TRIGger:A:BUS:B<x>:USB:SPLit:SE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit:SE?``
              query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit:SE?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:USB:SPLit:SE:VALue`` command.
        """
        return self._se


class TriggerABusBItemUsbSpecialtype(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:SPECIALType`` command.

    Description:
        - This command specifies the packet ID (PID) for the special packet. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPECIALType?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPECIALType?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:SPECIALType value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:USB:SPECIALType {ANY|PREamble|RESERVed}
        - TRIGger:A:BUS:B<x>:USB:SPECIALType?
        ```

    Info:
        - ``ANY`` indicates any type of special packet.
        - ``PREamble`` indicates a preamble special packet.
        - ``RESERVed`` indicates a reserved special packet.
    """


class TriggerABusBItemUsbSofframenumber(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber`` command.

    Description:
        - This command specifies the binary data string to be used for start of frame number, when
          the trigger condition is Token Packet and the token type is Start of Frame. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber <QString>
        - TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber?
        ```

    Info:
        - ``<QString>`` within the range 000 0000 0000 to 111 1111 1111 (000 hex to 7FF hex).
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemUsbQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:QUALifier`` command.

    Description:
        - This command specifies the USB trigger qualifier for address, endpoint and data. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:QUALifier?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:QUALifier value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:USB:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - TRIGger:A:BUS:B<x>:USB:QUALifier?
        ```

    Info:
        - ``LESSthan`` triggers on an input value that is less than a set value.
        - ``MOREthan`` triggers on an input value that is greater than a set value.
        - ``EQual`` triggers on an input value that is equal to a set value.
        - ``UNEQual`` triggers on an input value that is not equal to a set value.
        - ``LESSEQual`` triggers on an input value that is less than or equal to a set value.
        - ``MOREEQual`` triggers on an input value that is more than or equal to a set value.
        - ``INrange`` triggers on an input value that is within a range set by two values.
        - ``OUTrange`` triggers on an input value that is outside of a range set by two values.
    """  # noqa: E501


class TriggerABusBItemUsbHandshaketype(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:HANDSHAKEType`` command.

    Description:
        - This command specifies the handshake type for the USB trigger. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:HANDSHAKEType?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:HANDSHAKEType?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:HANDSHAKEType value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:USB:HANDSHAKEType {ANY|NAK|ACK|STALL}
        - TRIGger:A:BUS:B<x>:USB:HANDSHAKEType?
        ```

    Info:
        - ``ANY`` indicates the oscilloscope will trigger on any handshake type.
        - ``NAK`` indicates the oscilloscope will trigger when a device cannot send or receive data.
        - ``ACK`` indicates the oscilloscope will trigger when a packet is successfully received.
        - ``STALL`` indicates the oscilloscope will trigger when a device requires intervention from
          the host.
    """


class TriggerABusBItemUsbErrtype(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:ERRTYPE`` command.

    Description:
        - This command specifies the error type to be used when the trigger condition is set to
          ERRor. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:ERRTYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:ERRTYPE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:ERRTYPE value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:USB:ERRTYPE {PID|CRC5|CRC16|BITSTUFFing}
        - TRIGger:A:BUS:B<x>:USB:ERRTYPE?
        ```

    Info:
        - ``PID`` indicates the error type is set to packet ID.
        - ``CRC5`` indicates the error type is set to 5-bit CRC.
        - ``CRC16`` indicates the error type is set to 16-bit CRC.
        - ``BITSTUFFing`` indicates the error type is set to bit stuffing.
    """


class TriggerABusBItemUsbEndpointValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue`` command.

    Description:
        - This command specifies the binary endpoint string to be used for the USB trigger. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue <QString>
        - TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue?
        ```

    Info:
        - ``<QString>`` within the range 0000 to 1111 (00 hex to 0F hex).
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemUsbEndpoint(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:ENDPoint`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:ENDPoint?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:ENDPoint?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemUsbEndpointValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> TriggerABusBItemUsbEndpointValue:
        """Return the ``TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue`` command.

        Description:
            - This command specifies the binary endpoint string to be used for the USB trigger. B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue <QString>
            - TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue?
            ```

        Info:
            - ``<QString>`` within the range 0000 to 1111 (00 hex to 0F hex).
        """
        return self._value


class TriggerABusBItemUsbDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:DATa:VALue`` command.

    Description:
        - This command specifies the binary data string to be used for the USB trigger when the
          trigger condition is DATAPacket. This command also specifies the binary data string for
          the lower limit for inside-of-range and outside-of-range qualifiers for the USB trigger
          when trigger condition is DATAPacket. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:DATa:VALue?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:DATa:VALue?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:USB:DATa:VALue <QString>
        - TRIGger:A:BUS:B<x>:USB:DATa:VALue?
        ```

    Info:
        - ``<QString>`` within the range 00000000 to 11111111 (00 hex to FF hex).
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemUsbDataType(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:DATa:TYPe`` command.

    Description:
        - This command specifies the data type for when the trigger condition is set to DATAPacket.
          B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:DATa:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:DATa:TYPe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:DATa:TYPe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:USB:DATa:TYPe {ANY|DATA<x>}
        - TRIGger:A:BUS:B<x>:USB:DATa:TYPe?
        ```

    Info:
        - ``ANY`` indicates either a DATA0 or DATA1 data packet type.
        - ``DATA0`` indicates a DATA0 data packet type.
        - ``DATA1`` indicates a DATA1 data packet type.
    """


class TriggerABusBItemUsbDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:DATa:SIZe`` command.

    Description:
        - This command specifies the number of contiguous data bytes to trigger on. The minimum and
          default values are 1 and maximum is 16. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:DATa:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:DATa:SIZe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:USB:DATa:SIZe <NR1>
        - TRIGger:A:BUS:B<x>:USB:DATa:SIZe?
        ```
    """


class TriggerABusBItemUsbDataOffset(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:DATa:OFFSet`` command.

    Description:
        - This command specifies the data offset in bytes to trigger on. The minimum and default
          values are 0 and the maximum is 1024. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:DATa:OFFSet?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:DATa:OFFSet?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:DATa:OFFSet value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:USB:DATa:OFFSet <NR1>
        - TRIGger:A:BUS:B<x>:USB:DATa:OFFSet?
        ```
    """


class TriggerABusBItemUsbDataHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:DATa:HIVALue`` command.

    Description:
        - This command specifies the binary data string for the upper limit for inside-of-range and
          outside-of-range qualifiers for the USB trigger when the trigger condition is DATAPacket.
          Use the command ``TRIGGER:A:BUS:BX:USB:DATA:VALUE`` to set the lower limit. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:DATa:HIVALue?``
          query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:DATa:HIVALue?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:DATa:HIVALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:USB:DATa:HIVALue <QString>
        - TRIGger:A:BUS:B<x>:USB:DATa:HIVALue?
        ```

    Info:
        - ``<QString>`` within the range 00000000 to 11111111 (00 hex to FF hex).
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemUsbData(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:DATa?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:USB:DATa:HIVALue`` command.
        - ``.offset``: The ``TRIGger:A:BUS:B<x>:USB:DATa:OFFSet`` command.
        - ``.size``: The ``TRIGger:A:BUS:B<x>:USB:DATa:SIZe`` command.
        - ``.type``: The ``TRIGger:A:BUS:B<x>:USB:DATa:TYPe`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:USB:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = TriggerABusBItemUsbDataHivalue(device, f"{self._cmd_syntax}:HIVALue")
        self._offset = TriggerABusBItemUsbDataOffset(device, f"{self._cmd_syntax}:OFFSet")
        self._size = TriggerABusBItemUsbDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._type = TriggerABusBItemUsbDataType(device, f"{self._cmd_syntax}:TYPe")
        self._value = TriggerABusBItemUsbDataValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def hivalue(self) -> TriggerABusBItemUsbDataHivalue:
        """Return the ``TRIGger:A:BUS:B<x>:USB:DATa:HIVALue`` command.

        Description:
            - This command specifies the binary data string for the upper limit for inside-of-range
              and outside-of-range qualifiers for the USB trigger when the trigger condition is
              DATAPacket. Use the command ``TRIGGER:A:BUS:BX:USB:DATA:VALUE`` to set the lower
              limit. B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:DATa:HIVALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:DATa:HIVALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:DATa:HIVALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:USB:DATa:HIVALue <QString>
            - TRIGger:A:BUS:B<x>:USB:DATa:HIVALue?
            ```

        Info:
            - ``<QString>`` within the range 00000000 to 11111111 (00 hex to FF hex).
        """
        return self._hivalue

    @property
    def offset(self) -> TriggerABusBItemUsbDataOffset:
        """Return the ``TRIGger:A:BUS:B<x>:USB:DATa:OFFSet`` command.

        Description:
            - This command specifies the data offset in bytes to trigger on. The minimum and default
              values are 0 and the maximum is 1024. B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:DATa:OFFSet?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:DATa:OFFSet?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:DATa:OFFSet value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:USB:DATa:OFFSet <NR1>
            - TRIGger:A:BUS:B<x>:USB:DATa:OFFSet?
            ```
        """
        return self._offset

    @property
    def size(self) -> TriggerABusBItemUsbDataSize:
        """Return the ``TRIGger:A:BUS:B<x>:USB:DATa:SIZe`` command.

        Description:
            - This command specifies the number of contiguous data bytes to trigger on. The minimum
              and default values are 1 and maximum is 16. B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:DATa:SIZe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:DATa:SIZe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:DATa:SIZe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:USB:DATa:SIZe <NR1>
            - TRIGger:A:BUS:B<x>:USB:DATa:SIZe?
            ```
        """
        return self._size

    @property
    def type(self) -> TriggerABusBItemUsbDataType:
        """Return the ``TRIGger:A:BUS:B<x>:USB:DATa:TYPe`` command.

        Description:
            - This command specifies the data type for when the trigger condition is set to
              DATAPacket. B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:DATa:TYPe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:DATa:TYPe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:DATa:TYPe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:USB:DATa:TYPe {ANY|DATA<x>}
            - TRIGger:A:BUS:B<x>:USB:DATa:TYPe?
            ```

        Info:
            - ``ANY`` indicates either a DATA0 or DATA1 data packet type.
            - ``DATA0`` indicates a DATA0 data packet type.
            - ``DATA1`` indicates a DATA1 data packet type.
        """
        return self._type

    @property
    def value(self) -> TriggerABusBItemUsbDataValue:
        """Return the ``TRIGger:A:BUS:B<x>:USB:DATa:VALue`` command.

        Description:
            - This command specifies the binary data string to be used for the USB trigger when the
              trigger condition is DATAPacket. This command also specifies the binary data string
              for the lower limit for inside-of-range and outside-of-range qualifiers for the USB
              trigger when trigger condition is DATAPacket. B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:DATa:VALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:DATa:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:USB:DATa:VALue <QString>
            - TRIGger:A:BUS:B<x>:USB:DATa:VALue?
            ```

        Info:
            - ``<QString>`` within the range 00000000 to 11111111 (00 hex to FF hex).
        """
        return self._value


class TriggerABusBItemUsbCondition(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:CONDition`` command.

    Description:
        - This command specifies the trigger condition for the USB trigger. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:CONDition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:CONDition value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:USB:CONDition {SYNC|RESET|SUSPEND|RESUME|EOP|TOKENPacket|DATAPacket|HANDSHAKEPacket|SPECIALPacket|ERRor}
        - TRIGger:A:BUS:B<x>:USB:CONDition?
        ```

    Info:
        - ``SYNC`` indicates triggering on a Sync field of a packet.
        - ``RESET`` sets triggering on a reset condition.
        - ``SUSPEND`` sets triggering on a suspend condition.
        - ``RESUME`` sets triggering on a resume condition.
        - ``EOP`` indicates triggering on an end-of-packet signal.
        - ``TOKENPacket`` indicates triggering on a token packet.
        - ``DATAPacket`` indicates triggering on a data packet.
        - ``HANDSHAKEPacket`` indicates triggering on a handshake packet.
        - ``SPECIALPacket`` indicates triggering on a special status packet.
        - ``ERRor`` indicates triggering on an error condition.
    """  # noqa: E501


class TriggerABusBItemUsbAddressValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:ADDRess:VALue`` command.

    Description:
        - This command specifies the binary address string to be used for USB trigger. This command
          also specifies the binary address string for the lower limit for inside-of-range and
          outside-of-range qualifiers for the USB trigger. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:ADDRess:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:ADDRess:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:ADDRess:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:USB:ADDRess:VALue <Qstring>
        - TRIGger:A:BUS:B<x>:USB:ADDRess:VALue?
        ```

    Info:
        - ``<QString>`` within the range 0000000 to 1111111 (00 hex to 7F hex).
    """


class TriggerABusBItemUsbAddressHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue`` command.

    Description:
        - This command specifies the binary address string for the upper limit for inside-of-range
          and outside-of-range qualifiers for the USB trigger. Use the command
          ``TRIGGER:A:BUS:BX:USB:ADDRESS:VALUE`` to set the lower limit. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue <QString>
        - TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue?
        ```

    Info:
        - ``<QString>`` within the range 0000000 to 1111111 (00 hex to 7F hex).
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemUsbAddress(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB:ADDRess`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:ADDRess?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:ADDRess?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:USB:ADDRess:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = TriggerABusBItemUsbAddressHivalue(device, f"{self._cmd_syntax}:HIVALue")
        self._value = TriggerABusBItemUsbAddressValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def hivalue(self) -> TriggerABusBItemUsbAddressHivalue:
        """Return the ``TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue`` command.

        Description:
            - This command specifies the binary address string for the upper limit for
              inside-of-range and outside-of-range qualifiers for the USB trigger. Use the command
              ``TRIGGER:A:BUS:BX:USB:ADDRESS:VALUE`` to set the lower limit. B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue <QString>
            - TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue?
            ```

        Info:
            - ``<QString>`` within the range 0000000 to 1111111 (00 hex to 7F hex).
        """
        return self._hivalue

    @property
    def value(self) -> TriggerABusBItemUsbAddressValue:
        """Return the ``TRIGger:A:BUS:B<x>:USB:ADDRess:VALue`` command.

        Description:
            - This command specifies the binary address string to be used for USB trigger. This
              command also specifies the binary address string for the lower limit for
              inside-of-range and outside-of-range qualifiers for the USB trigger. B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:ADDRess:VALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:ADDRess:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:ADDRess:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:USB:ADDRess:VALue <Qstring>
            - TRIGger:A:BUS:B<x>:USB:ADDRess:VALue?
            ```

        Info:
            - ``<QString>`` within the range 0000000 to 1111111 (00 hex to 7F hex).
        """
        return self._value


#  pylint: disable=too-many-instance-attributes
class TriggerABusBItemUsb(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:USB`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.address``: The ``TRIGger:A:BUS:B<x>:USB:ADDRess`` command tree.
        - ``.condition``: The ``TRIGger:A:BUS:B<x>:USB:CONDition`` command.
        - ``.data``: The ``TRIGger:A:BUS:B<x>:USB:DATa`` command tree.
        - ``.endpoint``: The ``TRIGger:A:BUS:B<x>:USB:ENDPoint`` command tree.
        - ``.errtype``: The ``TRIGger:A:BUS:B<x>:USB:ERRTYPE`` command.
        - ``.handshaketype``: The ``TRIGger:A:BUS:B<x>:USB:HANDSHAKEType`` command.
        - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:USB:QUALifier`` command.
        - ``.sofframenumber``: The ``TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber`` command.
        - ``.specialtype``: The ``TRIGger:A:BUS:B<x>:USB:SPECIALType`` command.
        - ``.split``: The ``TRIGger:A:BUS:B<x>:USB:SPLit`` command tree.
        - ``.tokentype``: The ``TRIGger:A:BUS:B<x>:USB:TOKENType`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._address = TriggerABusBItemUsbAddress(device, f"{self._cmd_syntax}:ADDRess")
        self._condition = TriggerABusBItemUsbCondition(device, f"{self._cmd_syntax}:CONDition")
        self._data = TriggerABusBItemUsbData(device, f"{self._cmd_syntax}:DATa")
        self._endpoint = TriggerABusBItemUsbEndpoint(device, f"{self._cmd_syntax}:ENDPoint")
        self._errtype = TriggerABusBItemUsbErrtype(device, f"{self._cmd_syntax}:ERRTYPE")
        self._handshaketype = TriggerABusBItemUsbHandshaketype(
            device, f"{self._cmd_syntax}:HANDSHAKEType"
        )
        self._qualifier = TriggerABusBItemUsbQualifier(device, f"{self._cmd_syntax}:QUALifier")
        self._sofframenumber = TriggerABusBItemUsbSofframenumber(
            device, f"{self._cmd_syntax}:SOFFRAMENUMber"
        )
        self._specialtype = TriggerABusBItemUsbSpecialtype(
            device, f"{self._cmd_syntax}:SPECIALType"
        )
        self._split = TriggerABusBItemUsbSplit(device, f"{self._cmd_syntax}:SPLit")
        self._tokentype = TriggerABusBItemUsbTokentype(device, f"{self._cmd_syntax}:TOKENType")

    @property
    def address(self) -> TriggerABusBItemUsbAddress:
        """Return the ``TRIGger:A:BUS:B<x>:USB:ADDRess`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:ADDRess?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:ADDRess?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:USB:ADDRess:HIVALue`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:USB:ADDRess:VALue`` command.
        """
        return self._address

    @property
    def condition(self) -> TriggerABusBItemUsbCondition:
        """Return the ``TRIGger:A:BUS:B<x>:USB:CONDition`` command.

        Description:
            - This command specifies the trigger condition for the USB trigger. B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:CONDition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:CONDition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:CONDition value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:USB:CONDition {SYNC|RESET|SUSPEND|RESUME|EOP|TOKENPacket|DATAPacket|HANDSHAKEPacket|SPECIALPacket|ERRor}
            - TRIGger:A:BUS:B<x>:USB:CONDition?
            ```

        Info:
            - ``SYNC`` indicates triggering on a Sync field of a packet.
            - ``RESET`` sets triggering on a reset condition.
            - ``SUSPEND`` sets triggering on a suspend condition.
            - ``RESUME`` sets triggering on a resume condition.
            - ``EOP`` indicates triggering on an end-of-packet signal.
            - ``TOKENPacket`` indicates triggering on a token packet.
            - ``DATAPacket`` indicates triggering on a data packet.
            - ``HANDSHAKEPacket`` indicates triggering on a handshake packet.
            - ``SPECIALPacket`` indicates triggering on a special status packet.
            - ``ERRor`` indicates triggering on an error condition.
        """  # noqa: E501
        return self._condition

    @property
    def data(self) -> TriggerABusBItemUsbData:
        """Return the ``TRIGger:A:BUS:B<x>:USB:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:DATa?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:USB:DATa:HIVALue`` command.
            - ``.offset``: The ``TRIGger:A:BUS:B<x>:USB:DATa:OFFSet`` command.
            - ``.size``: The ``TRIGger:A:BUS:B<x>:USB:DATa:SIZe`` command.
            - ``.type``: The ``TRIGger:A:BUS:B<x>:USB:DATa:TYPe`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:USB:DATa:VALue`` command.
        """
        return self._data

    @property
    def endpoint(self) -> TriggerABusBItemUsbEndpoint:
        """Return the ``TRIGger:A:BUS:B<x>:USB:ENDPoint`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:ENDPoint?``
              query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:ENDPoint?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:USB:ENDPoint:VALue`` command.
        """
        return self._endpoint

    @property
    def errtype(self) -> TriggerABusBItemUsbErrtype:
        """Return the ``TRIGger:A:BUS:B<x>:USB:ERRTYPE`` command.

        Description:
            - This command specifies the error type to be used when the trigger condition is set to
              ERRor. B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:ERRTYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:ERRTYPE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:ERRTYPE value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:USB:ERRTYPE {PID|CRC5|CRC16|BITSTUFFing}
            - TRIGger:A:BUS:B<x>:USB:ERRTYPE?
            ```

        Info:
            - ``PID`` indicates the error type is set to packet ID.
            - ``CRC5`` indicates the error type is set to 5-bit CRC.
            - ``CRC16`` indicates the error type is set to 16-bit CRC.
            - ``BITSTUFFing`` indicates the error type is set to bit stuffing.
        """
        return self._errtype

    @property
    def handshaketype(self) -> TriggerABusBItemUsbHandshaketype:
        """Return the ``TRIGger:A:BUS:B<x>:USB:HANDSHAKEType`` command.

        Description:
            - This command specifies the handshake type for the USB trigger. B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:HANDSHAKEType?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:HANDSHAKEType?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:HANDSHAKEType value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:USB:HANDSHAKEType {ANY|NAK|ACK|STALL}
            - TRIGger:A:BUS:B<x>:USB:HANDSHAKEType?
            ```

        Info:
            - ``ANY`` indicates the oscilloscope will trigger on any handshake type.
            - ``NAK`` indicates the oscilloscope will trigger when a device cannot send or receive
              data.
            - ``ACK`` indicates the oscilloscope will trigger when a packet is successfully
              received.
            - ``STALL`` indicates the oscilloscope will trigger when a device requires intervention
              from the host.
        """
        return self._handshaketype

    @property
    def qualifier(self) -> TriggerABusBItemUsbQualifier:
        """Return the ``TRIGger:A:BUS:B<x>:USB:QUALifier`` command.

        Description:
            - This command specifies the USB trigger qualifier for address, endpoint and data. B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:QUALifier?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:QUALifier?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:QUALifier value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:USB:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - TRIGger:A:BUS:B<x>:USB:QUALifier?
            ```

        Info:
            - ``LESSthan`` triggers on an input value that is less than a set value.
            - ``MOREthan`` triggers on an input value that is greater than a set value.
            - ``EQual`` triggers on an input value that is equal to a set value.
            - ``UNEQual`` triggers on an input value that is not equal to a set value.
            - ``LESSEQual`` triggers on an input value that is less than or equal to a set value.
            - ``MOREEQual`` triggers on an input value that is more than or equal to a set value.
            - ``INrange`` triggers on an input value that is within a range set by two values.
            - ``OUTrange`` triggers on an input value that is outside of a range set by two values.
        """  # noqa: E501
        return self._qualifier

    @property
    def sofframenumber(self) -> TriggerABusBItemUsbSofframenumber:
        """Return the ``TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber`` command.

        Description:
            - This command specifies the binary data string to be used for start of frame number,
              when the trigger condition is Token Packet and the token type is Start of Frame. B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber <QString>
            - TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber?
            ```

        Info:
            - ``<QString>`` within the range 000 0000 0000 to 111 1111 1111 (000 hex to 7FF hex).
        """
        return self._sofframenumber

    @property
    def specialtype(self) -> TriggerABusBItemUsbSpecialtype:
        """Return the ``TRIGger:A:BUS:B<x>:USB:SPECIALType`` command.

        Description:
            - This command specifies the packet ID (PID) for the special packet. B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPECIALType?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:SPECIALType?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:SPECIALType value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:USB:SPECIALType {ANY|PREamble|RESERVed}
            - TRIGger:A:BUS:B<x>:USB:SPECIALType?
            ```

        Info:
            - ``ANY`` indicates any type of special packet.
            - ``PREamble`` indicates a preamble special packet.
            - ``RESERVed`` indicates a reserved special packet.
        """
        return self._specialtype

    @property
    def split(self) -> TriggerABusBItemUsbSplit:
        """Return the ``TRIGger:A:BUS:B<x>:USB:SPLit`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB:SPLit?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.et``: The ``TRIGger:A:BUS:B<x>:USB:SPLit:ET`` command tree.
            - ``.hub``: The ``TRIGger:A:BUS:B<x>:USB:SPLit:HUB`` command tree.
            - ``.port``: The ``TRIGger:A:BUS:B<x>:USB:SPLit:PORT`` command tree.
            - ``.sc``: The ``TRIGger:A:BUS:B<x>:USB:SPLit:SC`` command tree.
            - ``.se``: The ``TRIGger:A:BUS:B<x>:USB:SPLit:SE`` command tree.
        """
        return self._split

    @property
    def tokentype(self) -> TriggerABusBItemUsbTokentype:
        """Return the ``TRIGger:A:BUS:B<x>:USB:TOKENType`` command.

        Description:
            - This command specifies the token type for the USB trigger. B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB:TOKENType?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:TOKENType?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:USB:TOKENType value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:USB:TOKENType {ANY|SOF|OUT|IN|SETUP}
            - TRIGger:A:BUS:B<x>:USB:TOKENType?
            ```

        Info:
            - ``ANY``
            - ``SOF`` indicates a SOF (start-of-frame) token type.
            - ``OUT`` indicates an OUT token type.
            - ``IN`` indicates an IN token type.
            - ``SETUP`` indicates a SETUP token type.
        """
        return self._tokentype


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
        - This command specifies the condition for an RS-232C trigger, where x B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:CONDition?``
          query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:CONDition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:RS232C:CONDition value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:RS232C:CONDition {RXSTArt|RXDATA|RXENDPacket|TXSTArt|TXDATA|TXENDPacket}
        - TRIGger:A:BUS:B<x>:RS232C:CONDition?
        ```

    Info:
        - ``RXSTArt`` specifies a search based on the RX Start Bit.
        - ``RXDATA`` specifies a search based on RX Data.
        - ``RXENDPacket`` specifies a search based on the RX End of Packet condition.
        - ``TXSTArt`` specifies a search base on the TX Start Bit.
        - ``TXDATA`` specifies a search based on TX Data.
        - ``TXENDPacket`` specifies a search based on the TX End of Packet condition.
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
            - This command specifies the condition for an RS-232C trigger, where x B<x>

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
            - TRIGger:A:BUS:B<x>:RS232C:CONDition {RXSTArt|RXDATA|RXENDPacket|TXSTArt|TXDATA|TXENDPacket}
            - TRIGger:A:BUS:B<x>:RS232C:CONDition?
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


class TriggerABusBItemMil1553bTimeQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier`` command.

    Description:
        - When the MIL-STD-1553 bus trigger condition is set to TIMe, this command specifies the
          trigger data time qualifier. (This includes a smaller set of arguments than other
          qualifier commands.) B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier {LESSthan|MOREthan|INrange|OUTrange}
        - TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier?
        ```

    Info:
        - ``LESSthan`` sets the Time qualifier to less than minimum.
        - ``MOREthan`` sets the Time qualifier to greater than maximum.
        - ``INrange`` sets the Time qualifier to inside range.
        - ``OUTrange`` sets the Time qualifier to out of range.
    """


class TriggerABusBItemMil1553bTimeMorelimit(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit`` command.

    Description:
        - When the MIL-STD-1553 bus trigger condition is set to TIMe, this command specifies either
          the maximum remote terminal response time (RT) limit for the amount of time the terminal
          has to transmit, or it specifies the maximum inter-message gap (IMG). (You can specify the
          RT and IMG using the ``TRIGGER:A:BUS:BX:MIL1553B:CONDITION TIMe`` command.)

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit <NR3>
        - TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies either the maximum remote terminal
          response time (RT) or the inter-message gap (IMG) in seconds.
    """


class TriggerABusBItemMil1553bTimeLesslimit(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit`` command.

    Description:
        - When the MIL-STD-1553 bus trigger condition is set to TIMe, this command specifies either
          the minimum remote terminal response time (RT) limit for the amount of time the terminal
          has to transmit, or it specifies the minimum inter-message gap (IMG). (You can specify RT
          or IMG using the ``TRIGGER:A:BUS:BX:MIL1553B:CONDITION TIMe`` command.) B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit <NR3>
        - TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies either the minimum remote terminal
          response time (RT) or the inter-message gap (IMG) in seconds.
    """


class TriggerABusBItemMil1553bTime(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.lesslimit``: The ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit`` command.
        - ``.morelimit``: The ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit`` command.
        - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._lesslimit = TriggerABusBItemMil1553bTimeLesslimit(
            device, f"{self._cmd_syntax}:LESSLimit"
        )
        self._morelimit = TriggerABusBItemMil1553bTimeMorelimit(
            device, f"{self._cmd_syntax}:MORELimit"
        )
        self._qualifier = TriggerABusBItemMil1553bTimeQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )

    @property
    def lesslimit(self) -> TriggerABusBItemMil1553bTimeLesslimit:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit`` command.

        Description:
            - When the MIL-STD-1553 bus trigger condition is set to TIMe, this command specifies
              either the minimum remote terminal response time (RT) limit for the amount of time the
              terminal has to transmit, or it specifies the minimum inter-message gap (IMG). (You
              can specify RT or IMG using the ``TRIGGER:A:BUS:BX:MIL1553B:CONDITION TIMe`` command.)
              B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit <NR3>
            - TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies either the minimum remote terminal
              response time (RT) or the inter-message gap (IMG) in seconds.
        """
        return self._lesslimit

    @property
    def morelimit(self) -> TriggerABusBItemMil1553bTimeMorelimit:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit`` command.

        Description:
            - When the MIL-STD-1553 bus trigger condition is set to TIMe, this command specifies
              either the maximum remote terminal response time (RT) limit for the amount of time the
              terminal has to transmit, or it specifies the maximum inter-message gap (IMG). (You
              can specify the RT and IMG using the ``TRIGGER:A:BUS:BX:MIL1553B:CONDITION TIMe``
              command.)

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit <NR3>
            - TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies either the maximum remote terminal
              response time (RT) or the inter-message gap (IMG) in seconds.
        """
        return self._morelimit

    @property
    def qualifier(self) -> TriggerABusBItemMil1553bTimeQualifier:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier`` command.

        Description:
            - When the MIL-STD-1553 bus trigger condition is set to TIMe, this command specifies the
              trigger data time qualifier. (This includes a smaller set of arguments than other
              qualifier commands.) B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier {LESSthan|MOREthan|INrange|OUTrange}
            - TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier?
            ```

        Info:
            - ``LESSthan`` sets the Time qualifier to less than minimum.
            - ``MOREthan`` sets the Time qualifier to greater than maximum.
            - ``INrange`` sets the Time qualifier to inside range.
            - ``OUTrange`` sets the Time qualifier to out of range.
        """
        return self._qualifier


class TriggerABusBItemMil1553bStatusParity(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity`` command.

    Description:
        - When the MIL-STD-1553 bus trigger condition is set to STATus, this command specifies the
          status parity bit value to be used in the trigger. Returned values are 0, 1, or X (don't
          care, which is the default). B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
        - TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity?
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


class TriggerABusBItemMil1553bStatusBitTf(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF`` command.

    Description:
        - When the MIL-STD-1553 bus trigger condition is set to STATus, this command specifies the
          status word terminal flag bit value (bit 19) to be used in the trigger. Returned values
          are 0, 1, or X (don't care, which is the default). B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
        - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF?
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


class TriggerABusBItemMil1553bStatusBitSubsf(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF`` command.

    Description:
        - When the MIL-STD-1553 bus trigger condition is set to STATus, this command specifies the
          status word subsystem flag bit value (bit 17) to be used in the trigger. Returned values
          are 0, 1, or X (don't care, which is the default). B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
        - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF?
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


class TriggerABusBItemMil1553bStatusBitSrq(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ`` command.

    Description:
        - When the MIL-STD-1553 bus trigger condition is set to STATus, this command specifies the
          status word service request (SRQ) bit value (bit 11) to be used in the trigger. Returned
          values are 0, 1, or X (don't care, which is the default). B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
        - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ?
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


class TriggerABusBItemMil1553bStatusBitMe(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME`` command.

    Description:
        - When the MIL-STD-1553 bus trigger condition is set to STATus, this command specifies the
          status word message error bit value (bit 9) to be used in the trigger. Returned values are
          0, 1, or X (don't care, which is the default). B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
        - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME?
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


class TriggerABusBItemMil1553bStatusBitInstr(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR`` command.

    Description:
        - When the MIL-STD-1553 bus trigger condition is set to STATus, this command specifies the
          status word instrumentation bit value (bit 10) to be used in the trigger. Returned values
          are 0, 1, or X (don't care, which is the default). B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
        - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR?
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


class TriggerABusBItemMil1553bStatusBitDbca(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA`` command.

    Description:
        - When the MIL-STD-1553 bus trigger condition is set to STATus, this command specifies the
          status word dynamic bus control acceptance (DBCA) bit value (bit 18) to be used in the
          trigger. Returned values are 0, 1, or X (don't care, which is the default). B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
        - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA?
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


class TriggerABusBItemMil1553bStatusBitBusy(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY`` command.

    Description:
        - When the MIL-STD-1553 bus trigger condition is set to STATus, this command specifies the
          status word busy bit value (bit 16) to be used in the trigger. Returned values are 0, 1,
          or X (don't care, which is the default). B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
        - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY?
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


class TriggerABusBItemMil1553bStatusBitBcr(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR`` command.

    Description:
        - When the MIL-STD-1553 bus trigger condition is set to STATus, this command specifies the
          status word broadcast command received (BCR) bit value (bit 15) to be used in the trigger.
          Returned values are 0, 1, or X (don't care, which is the default). B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
        - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR?
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
class TriggerABusBItemMil1553bStatusBit(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.bcr``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR`` command.
        - ``.busy``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY`` command.
        - ``.dbca``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA`` command.
        - ``.instr``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR`` command.
        - ``.me``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME`` command.
        - ``.srq``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ`` command.
        - ``.subsf``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF`` command.
        - ``.tf``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bcr = TriggerABusBItemMil1553bStatusBitBcr(device, f"{self._cmd_syntax}:BCR")
        self._busy = TriggerABusBItemMil1553bStatusBitBusy(device, f"{self._cmd_syntax}:BUSY")
        self._dbca = TriggerABusBItemMil1553bStatusBitDbca(device, f"{self._cmd_syntax}:DBCA")
        self._instr = TriggerABusBItemMil1553bStatusBitInstr(device, f"{self._cmd_syntax}:INSTR")
        self._me = TriggerABusBItemMil1553bStatusBitMe(device, f"{self._cmd_syntax}:ME")
        self._srq = TriggerABusBItemMil1553bStatusBitSrq(device, f"{self._cmd_syntax}:SRQ")
        self._subsf = TriggerABusBItemMil1553bStatusBitSubsf(device, f"{self._cmd_syntax}:SUBSF")
        self._tf = TriggerABusBItemMil1553bStatusBitTf(device, f"{self._cmd_syntax}:TF")

    @property
    def bcr(self) -> TriggerABusBItemMil1553bStatusBitBcr:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR`` command.

        Description:
            - When the MIL-STD-1553 bus trigger condition is set to STATus, this command specifies
              the status word broadcast command received (BCR) bit value (bit 15) to be used in the
              trigger. Returned values are 0, 1, or X (don't care, which is the default). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
            - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR?
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
        return self._bcr

    @property
    def busy(self) -> TriggerABusBItemMil1553bStatusBitBusy:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY`` command.

        Description:
            - When the MIL-STD-1553 bus trigger condition is set to STATus, this command specifies
              the status word busy bit value (bit 16) to be used in the trigger. Returned values are
              0, 1, or X (don't care, which is the default). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
            - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY?
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
        return self._busy

    @property
    def dbca(self) -> TriggerABusBItemMil1553bStatusBitDbca:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA`` command.

        Description:
            - When the MIL-STD-1553 bus trigger condition is set to STATus, this command specifies
              the status word dynamic bus control acceptance (DBCA) bit value (bit 18) to be used in
              the trigger. Returned values are 0, 1, or X (don't care, which is the default). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
            - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA?
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
        return self._dbca

    @property
    def instr(self) -> TriggerABusBItemMil1553bStatusBitInstr:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR`` command.

        Description:
            - When the MIL-STD-1553 bus trigger condition is set to STATus, this command specifies
              the status word instrumentation bit value (bit 10) to be used in the trigger. Returned
              values are 0, 1, or X (don't care, which is the default). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
            - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR?
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
        return self._instr

    @property
    def me(self) -> TriggerABusBItemMil1553bStatusBitMe:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME`` command.

        Description:
            - When the MIL-STD-1553 bus trigger condition is set to STATus, this command specifies
              the status word message error bit value (bit 9) to be used in the trigger. Returned
              values are 0, 1, or X (don't care, which is the default). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
            - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME?
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
        return self._me

    @property
    def srq(self) -> TriggerABusBItemMil1553bStatusBitSrq:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ`` command.

        Description:
            - When the MIL-STD-1553 bus trigger condition is set to STATus, this command specifies
              the status word service request (SRQ) bit value (bit 11) to be used in the trigger.
              Returned values are 0, 1, or X (don't care, which is the default). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
            - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ?
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
        return self._srq

    @property
    def subsf(self) -> TriggerABusBItemMil1553bStatusBitSubsf:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF`` command.

        Description:
            - When the MIL-STD-1553 bus trigger condition is set to STATus, this command specifies
              the status word subsystem flag bit value (bit 17) to be used in the trigger. Returned
              values are 0, 1, or X (don't care, which is the default). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
            - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF?
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
        return self._subsf

    @property
    def tf(self) -> TriggerABusBItemMil1553bStatusBitTf:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF`` command.

        Description:
            - When the MIL-STD-1553 bus trigger condition is set to STATus, this command specifies
              the status word terminal flag bit value (bit 19) to be used in the trigger. Returned
              values are 0, 1, or X (don't care, which is the default). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
            - TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF?
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
        return self._tf


class TriggerABusBItemMil1553bStatusAddressValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue`` command.

    Description:
        - When the MIL-STD-1553 bus trigger condition is set to STATus, and the qualifier is set to
          LESSthan, MOREthan, EQual, UNEQual, LESSEQual or MOREEQual, this command specifies the
          value of the 5-bit remote terminal address to be used in the trigger. When the
          MIL-STD-1553 bus trigger condition is set to STATus, and the qualifier is set to INrange
          or OUTrange, this command specifies the lower limit of the range. (Use the command
          ``TRIGGER:A:BUS:BX:MIL1553B:STATUS:ADDRESS:HIVALUE`` to specify the upper limit of the
          range.) The default is all X's (don't care). B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue <QString>
        - TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemMil1553bStatusAddressQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier`` command.

    Description:
        - When the MIL-STD-1553 bus trigger condition is set to STATus, this command specifies the
          qualifier to be used with the address field. The default is EQUAL. B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier?
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


class TriggerABusBItemMil1553bStatusAddressHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue`` command.

    Description:
        - When the MIL-STD-1553 bus trigger condition is set to STATus, and the qualifier is set to
          INrange or OUTrange, this command specifies the upper limit for the 5 bit remote terminal
          address field of the Status word. (Use the command
          ``TRIGGER:A:BUS:BX:MIL1553B:STATUS:ADDRESS:VALUE`` to specify the lower limit.) The
          default is all X's (don't care). B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue <QString>
        - TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemMil1553bStatusAddress(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue`` command.
        - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = TriggerABusBItemMil1553bStatusAddressHivalue(
            device, f"{self._cmd_syntax}:HIVALue"
        )
        self._qualifier = TriggerABusBItemMil1553bStatusAddressQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._value = TriggerABusBItemMil1553bStatusAddressValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def hivalue(self) -> TriggerABusBItemMil1553bStatusAddressHivalue:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue`` command.

        Description:
            - When the MIL-STD-1553 bus trigger condition is set to STATus, and the qualifier is set
              to INrange or OUTrange, this command specifies the upper limit for the 5 bit remote
              terminal address field of the Status word. (Use the command
              ``TRIGGER:A:BUS:BX:MIL1553B:STATUS:ADDRESS:VALUE`` to specify the lower limit.) The
              default is all X's (don't care). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue <QString>
            - TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue?
            ```
        """
        return self._hivalue

    @property
    def qualifier(self) -> TriggerABusBItemMil1553bStatusAddressQualifier:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier`` command.

        Description:
            - When the MIL-STD-1553 bus trigger condition is set to STATus, this command specifies
              the qualifier to be used with the address field. The default is EQUAL. B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier?
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
    def value(self) -> TriggerABusBItemMil1553bStatusAddressValue:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue`` command.

        Description:
            - When the MIL-STD-1553 bus trigger condition is set to STATus, and the qualifier is set
              to LESSthan, MOREthan, EQual, UNEQual, LESSEQual or MOREEQual, this command specifies
              the value of the 5-bit remote terminal address to be used in the trigger. When the
              MIL-STD-1553 bus trigger condition is set to STATus, and the qualifier is set to
              INrange or OUTrange, this command specifies the lower limit of the range. (Use the
              command ``TRIGGER:A:BUS:BX:MIL1553B:STATUS:ADDRESS:HIVALUE`` to specify the upper
              limit of the range.) The default is all X's (don't care). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue <QString>
            - TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue?
            ```
        """
        return self._value


class TriggerABusBItemMil1553bStatus(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B:STATus?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B:STATus?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.address``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess`` command tree.
        - ``.bit``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT`` command tree.
        - ``.parity``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._address = TriggerABusBItemMil1553bStatusAddress(device, f"{self._cmd_syntax}:ADDRess")
        self._bit = TriggerABusBItemMil1553bStatusBit(device, f"{self._cmd_syntax}:BIT")
        self._parity = TriggerABusBItemMil1553bStatusParity(device, f"{self._cmd_syntax}:PARity")

    @property
    def address(self) -> TriggerABusBItemMil1553bStatusAddress:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:HIVALue`` command.
            - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:QUALifier`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess:VALue`` command.
        """
        return self._address

    @property
    def bit(self) -> TriggerABusBItemMil1553bStatusBit:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.bcr``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BCR`` command.
            - ``.busy``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:BUSY`` command.
            - ``.dbca``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:DBCA`` command.
            - ``.instr``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:INSTR`` command.
            - ``.me``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:ME`` command.
            - ``.srq``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SRQ`` command.
            - ``.subsf``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:SUBSF`` command.
            - ``.tf``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT:TF`` command.
        """
        return self._bit

    @property
    def parity(self) -> TriggerABusBItemMil1553bStatusParity:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity`` command.

        Description:
            - When the MIL-STD-1553 bus trigger condition is set to STATus, this command specifies
              the status parity bit value to be used in the trigger. Returned values are 0, 1, or X
              (don't care, which is the default). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
            - TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity?
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
        return self._parity


class TriggerABusBItemMil1553bErrtype(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE`` command.

    Description:
        - When the MIL-STD-1553 bus trigger condition is set to ERRor, this command specifies the
          signaling error type to be used in the trigger: Parity, Sync, Manchester or Data. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE?``
          query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE {PARity|SYNC|MANCHester|DATA}
        - TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE?
        ```
    """


class TriggerABusBItemMil1553bDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue`` command.

    Description:
        - When the MIL-STD-1553 bus trigger condition is set to DATa, this command specifies the
          data binary pattern to be used in the trigger. This is a 16-bit field. The default is all
          X's (don't care). B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue <QString>
        - TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemMil1553bDataParity(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity`` command.

    Description:
        - When the MIL-STD-1553 bus trigger condition is set to DATa, this command specifies the
          data parity bit to be used in the trigger. Returned values are 0, 1, or X (don't care).
          B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
        - TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity?
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


class TriggerABusBItemMil1553bData(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B:DATa?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.parity``: The ``TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._parity = TriggerABusBItemMil1553bDataParity(device, f"{self._cmd_syntax}:PARity")
        self._value = TriggerABusBItemMil1553bDataValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def parity(self) -> TriggerABusBItemMil1553bDataParity:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity`` command.

        Description:
            - When the MIL-STD-1553 bus trigger condition is set to DATa, this command specifies the
              data parity bit to be used in the trigger. Returned values are 0, 1, or X (don't
              care). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
            - TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity?
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
        return self._parity

    @property
    def value(self) -> TriggerABusBItemMil1553bDataValue:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue`` command.

        Description:
            - When the MIL-STD-1553 bus trigger condition is set to DATa, this command specifies the
              data binary pattern to be used in the trigger. This is a 16-bit field. The default is
              all X's (don't care). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue <QString>
            - TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue?
            ```
        """
        return self._value


class TriggerABusBItemMil1553bCondition(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:CONDition`` command.

    Description:
        - This command specifies a word type or condition within a MIL-STD-1553 bus word to trigger
          on. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B:CONDition?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:CONDition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:CONDition value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:MIL1553B:CONDition {SYNC|COMMAND|STATus|DATA|TIMe|ERRor}
        - TRIGger:A:BUS:B<x>:MIL1553B:CONDition?
        ```

    Info:
        - ``SYNC`` refers to the 3-bit sync pulse that precedes each word.
        - ``COMMAND`` is one of 3 16-bit word types. It specifies the function that a remote
          terminal is to perform.
        - ``STATus`` is one of 3 16-bit word types. Remote terminals respond to valid message
          transmissions via status words.
        - ``DATA`` is one of 3 16-bit word types.
        - ``TIMe`` specifies to trigger on either the RT (remote terminal response time), or the IMG
          (Inter-message Gap). Use the commands ``TRIGGER:A:BUS:BX:MIL1553B:TIME:QUALIFIER``,
          ``TRIGGER:A:BUS:BX:MIL1553B:TIME:LESSLIMIT``, and
          ``TRIGGER:A:BUS:BX:MIL1553B:TIME:MORELIMIT`` to specify the time parameters.
        - ``ERRor`` specifies to trigger upon a signaling error. (You can specify which type of
          error - Parity, Sync, Manchester or Non-contiguous Data - by using the
          ``TRIGGER:A:BUS:BX:MIL1553B:ERRTYPE`` command.).
    """


class TriggerABusBItemMil1553bCommandTrbit(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit`` command.

    Description:
        - When the MIL-STD-1553 bus trigger condition is set to COMMAND, this command specifies that
          the transmit/receive bit (bit 9) is to be used in the trigger. The transmit/receive bit
          defines the direction of information flow, and is always from the point of view of the
          remote terminal. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit {RX|TX|X}
        - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit?
        ```

    Info:
        - ``RX`` (logic 0) directs the instrument to trigger on a TX or 'transmit' from a remote
          terminal .
        - ``TX`` (logic 1) directs the instrument to trigger on an RX or 'receive' from a remote
          terminal.
        - ``X`` indicates 'don't care'.
    """


class TriggerABusBItemMil1553bCommandSubaddress(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress`` command.

    Description:
        - When the MIL-STD-1553 bus trigger condition is set to COMMAND, this command specifies the
          5 bit sub-address that is to be used in the trigger. When the sub-address value is set to
          00000 or 11111 binary, it specifies that the command is a 'Mode Code' command. Any other
          value specifies that it is a 'Word Count' command. The default is all X's (don't care).
          B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress <QString>
        - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemMil1553bCommandParity(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity`` command.

    Description:
        - When the MIL-STD-1553 bus trigger condition is set to COMMAND, this command specifies the
          Command word parity that is to be used in the trigger. B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
        - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity?
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


class TriggerABusBItemMil1553bCommandCount(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt`` command.

    Description:
        - When the MIL-STD-1553 bus trigger condition is set to COMMAND, this command specifies the
          bit pattern for the 5-bit Word Count/Mode Code sub-address field that is to be used in the
          trigger. (Use the command ``TRIGGER:A:BUS:BX:MIL1553B:COMMAND:SUBADDRESS`` to specify Word
          Count or Mode Code.) In Word Count mode, this field defines the number of data words that
          is to be transmitted, or received, depending on the T/R bit setting. (Use the command
          ``TRIGGER:A:BUS:BX:MIL1553B:COMMAND:TRBIT`` to set the T/R bit.) A word count value of 0
          actually indicates a transfer of 32 data words. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt <QString>
        - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt?
        ```

    Info:
        - ``QString`` is a quoted string of up to 5 characters, where the allowable characters are
          0, 1 and X. The bits specified in the quoted string replace the least significant bits,
          leaving any unspecified upper bits unchanged.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemMil1553bCommandAddressValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue`` command.

    Description:
        - When the MIL-STD-1553 bus trigger condition is set to COMMAND, and the qualifier is set to
          LESSthan, MOREthan, EQual, UNEQual, LESSEQual or MOREEQual, this command specifies the
          value of the 5-bit remote terminal address to be used in the trigger. When the
          MIL-STD-1553 bus trigger condition is set to COMMAND, and the qualifier is set to INrange
          or OUTrange, this command specifies the lower limit of the remote terminal address range.
          The default is all X's (don't care). B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue <QString>
        - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemMil1553bCommandAddressQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:QUALifier`` command.

    Description:
        - When the MIL-STD-1553 bus trigger condition is set to COMMAND, this command specifies the
          qualifier to be used with the remote terminal address field. B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:QUALifier?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:QUALifier value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:QUALifier?
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


class TriggerABusBItemMil1553bCommandAddressHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue`` command.

    Description:
        - When the MIL-STD-1553 bus trigger condition is set to COMMAND, and the qualifier is set to
          INrange or OUTrange, this command specifies the upper limit of the range for the remote
          terminal address field. (Use the command
          ``TRIGGER:A:BUS:BX:MIL1553B:COMMAND:ADDRESS:VALUE`` to specify the lower limit of the
          range.) The default is all X's (don't care). B<x>

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue <QString>
        - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemMil1553bCommandAddress(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue`` command.
        - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:QUALifier`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = TriggerABusBItemMil1553bCommandAddressHivalue(
            device, f"{self._cmd_syntax}:HIVALue"
        )
        self._qualifier = TriggerABusBItemMil1553bCommandAddressQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._value = TriggerABusBItemMil1553bCommandAddressValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def hivalue(self) -> TriggerABusBItemMil1553bCommandAddressHivalue:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue`` command.

        Description:
            - When the MIL-STD-1553 bus trigger condition is set to COMMAND, and the qualifier is
              set to INrange or OUTrange, this command specifies the upper limit of the range for
              the remote terminal address field. (Use the command
              ``TRIGGER:A:BUS:BX:MIL1553B:COMMAND:ADDRESS:VALUE`` to specify the lower limit of the
              range.) The default is all X's (don't care). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue <QString>
            - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue?
            ```
        """
        return self._hivalue

    @property
    def qualifier(self) -> TriggerABusBItemMil1553bCommandAddressQualifier:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:QUALifier`` command.

        Description:
            - When the MIL-STD-1553 bus trigger condition is set to COMMAND, this command specifies
              the qualifier to be used with the remote terminal address field. B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:QUALifier?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:QUALifier value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:QUALifier?
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
        return self._qualifier

    @property
    def value(self) -> TriggerABusBItemMil1553bCommandAddressValue:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue`` command.

        Description:
            - When the MIL-STD-1553 bus trigger condition is set to COMMAND, and the qualifier is
              set to LESSthan, MOREthan, EQual, UNEQual, LESSEQual or MOREEQual, this command
              specifies the value of the 5-bit remote terminal address to be used in the trigger.
              When the MIL-STD-1553 bus trigger condition is set to COMMAND, and the qualifier is
              set to INrange or OUTrange, this command specifies the lower limit of the remote
              terminal address range. The default is all X's (don't care). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue <QString>
            - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue?
            ```
        """
        return self._value


class TriggerABusBItemMil1553bCommand(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND?``
          query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.address``: The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess`` command tree.
        - ``.count``: The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt`` command.
        - ``.parity``: The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity`` command.
        - ``.subaddress``: The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress`` command.
        - ``.trbit``: The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._address = TriggerABusBItemMil1553bCommandAddress(
            device, f"{self._cmd_syntax}:ADDRess"
        )
        self._count = TriggerABusBItemMil1553bCommandCount(device, f"{self._cmd_syntax}:COUNt")
        self._parity = TriggerABusBItemMil1553bCommandParity(device, f"{self._cmd_syntax}:PARity")
        self._subaddress = TriggerABusBItemMil1553bCommandSubaddress(
            device, f"{self._cmd_syntax}:SUBADdress"
        )
        self._trbit = TriggerABusBItemMil1553bCommandTrbit(device, f"{self._cmd_syntax}:TRBit")

    @property
    def address(self) -> TriggerABusBItemMil1553bCommandAddress:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:HIVALue`` command.
            - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:QUALifier`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess:VALue`` command.
        """
        return self._address

    @property
    def count(self) -> TriggerABusBItemMil1553bCommandCount:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt`` command.

        Description:
            - When the MIL-STD-1553 bus trigger condition is set to COMMAND, this command specifies
              the bit pattern for the 5-bit Word Count/Mode Code sub-address field that is to be
              used in the trigger. (Use the command ``TRIGGER:A:BUS:BX:MIL1553B:COMMAND:SUBADDRESS``
              to specify Word Count or Mode Code.) In Word Count mode, this field defines the number
              of data words that is to be transmitted, or received, depending on the T/R bit
              setting. (Use the command ``TRIGGER:A:BUS:BX:MIL1553B:COMMAND:TRBIT`` to set the T/R
              bit.) A word count value of 0 actually indicates a transfer of 32 data words. B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt <QString>
            - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt?
            ```

        Info:
            - ``QString`` is a quoted string of up to 5 characters, where the allowable characters
              are 0, 1 and X. The bits specified in the quoted string replace the least significant
              bits, leaving any unspecified upper bits unchanged.
        """
        return self._count

    @property
    def parity(self) -> TriggerABusBItemMil1553bCommandParity:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity`` command.

        Description:
            - When the MIL-STD-1553 bus trigger condition is set to COMMAND, this command specifies
              the Command word parity that is to be used in the trigger. B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity {0|1|X|ZERo|ONE|NOCARE|OFF|ON}
            - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity?
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
        return self._parity

    @property
    def subaddress(self) -> TriggerABusBItemMil1553bCommandSubaddress:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress`` command.

        Description:
            - When the MIL-STD-1553 bus trigger condition is set to COMMAND, this command specifies
              the 5 bit sub-address that is to be used in the trigger. When the sub-address value is
              set to 00000 or 11111 binary, it specifies that the command is a 'Mode Code' command.
              Any other value specifies that it is a 'Word Count' command. The default is all X's
              (don't care). B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress <QString>
            - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress?
            ```
        """
        return self._subaddress

    @property
    def trbit(self) -> TriggerABusBItemMil1553bCommandTrbit:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit`` command.

        Description:
            - When the MIL-STD-1553 bus trigger condition is set to COMMAND, this command specifies
              that the transmit/receive bit (bit 9) is to be used in the trigger. The
              transmit/receive bit defines the direction of information flow, and is always from the
              point of view of the remote terminal. B<x>

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit {RX|TX|X}
            - TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit?
            ```

        Info:
            - ``RX`` (logic 0) directs the instrument to trigger on a TX or 'transmit' from a remote
              terminal .
            - ``TX`` (logic 1) directs the instrument to trigger on an RX or 'receive' from a remote
              terminal.
            - ``X`` indicates 'don't care'.
        """
        return self._trbit


class TriggerABusBItemMil1553b(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:MIL1553B`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.command``: The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND`` command tree.
        - ``.condition``: The ``TRIGger:A:BUS:B<x>:MIL1553B:CONDition`` command.
        - ``.data``: The ``TRIGger:A:BUS:B<x>:MIL1553B:DATa`` command tree.
        - ``.errtype``: The ``TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE`` command.
        - ``.status``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus`` command tree.
        - ``.time``: The ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._command = TriggerABusBItemMil1553bCommand(device, f"{self._cmd_syntax}:COMMAND")
        self._condition = TriggerABusBItemMil1553bCondition(device, f"{self._cmd_syntax}:CONDition")
        self._data = TriggerABusBItemMil1553bData(device, f"{self._cmd_syntax}:DATa")
        self._errtype = TriggerABusBItemMil1553bErrtype(device, f"{self._cmd_syntax}:ERRTYPE")
        self._status = TriggerABusBItemMil1553bStatus(device, f"{self._cmd_syntax}:STATus")
        self._time = TriggerABusBItemMil1553bTime(device, f"{self._cmd_syntax}:TIMe")

    @property
    def command(self) -> TriggerABusBItemMil1553bCommand:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.address``: The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:ADDRess`` command tree.
            - ``.count``: The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:COUNt`` command.
            - ``.parity``: The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:PARity`` command.
            - ``.subaddress``: The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:SUBADdress`` command.
            - ``.trbit``: The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND:TRBit`` command.
        """
        return self._command

    @property
    def condition(self) -> TriggerABusBItemMil1553bCondition:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:CONDition`` command.

        Description:
            - This command specifies a word type or condition within a MIL-STD-1553 bus word to
              trigger on. B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B:CONDition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:CONDition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:CONDition value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:MIL1553B:CONDition {SYNC|COMMAND|STATus|DATA|TIMe|ERRor}
            - TRIGger:A:BUS:B<x>:MIL1553B:CONDition?
            ```

        Info:
            - ``SYNC`` refers to the 3-bit sync pulse that precedes each word.
            - ``COMMAND`` is one of 3 16-bit word types. It specifies the function that a remote
              terminal is to perform.
            - ``STATus`` is one of 3 16-bit word types. Remote terminals respond to valid message
              transmissions via status words.
            - ``DATA`` is one of 3 16-bit word types.
            - ``TIMe`` specifies to trigger on either the RT (remote terminal response time), or the
              IMG (Inter-message Gap). Use the commands
              ``TRIGGER:A:BUS:BX:MIL1553B:TIME:QUALIFIER``,
              ``TRIGGER:A:BUS:BX:MIL1553B:TIME:LESSLIMIT``, and
              ``TRIGGER:A:BUS:BX:MIL1553B:TIME:MORELIMIT`` to specify the time parameters.
            - ``ERRor`` specifies to trigger upon a signaling error. (You can specify which type of
              error - Parity, Sync, Manchester or Non-contiguous Data - by using the
              ``TRIGGER:A:BUS:BX:MIL1553B:ERRTYPE`` command.).
        """
        return self._condition

    @property
    def data(self) -> TriggerABusBItemMil1553bData:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B:DATa?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:DATa?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.parity``: The ``TRIGger:A:BUS:B<x>:MIL1553B:DATa:PARity`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:MIL1553B:DATa:VALue`` command.
        """
        return self._data

    @property
    def errtype(self) -> TriggerABusBItemMil1553bErrtype:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE`` command.

        Description:
            - When the MIL-STD-1553 bus trigger condition is set to ERRor, this command specifies
              the signaling error type to be used in the trigger: Parity, Sync, Manchester or Data.
              B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE {PARity|SYNC|MANCHester|DATA}
            - TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE?
            ```
        """
        return self._errtype

    @property
    def status(self) -> TriggerABusBItemMil1553bStatus:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:STATus`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B:STATus?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:STATus?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.address``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:ADDRess`` command tree.
            - ``.bit``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:BIT`` command tree.
            - ``.parity``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus:PARity`` command.
        """
        return self._status

    @property
    def time(self) -> TriggerABusBItemMil1553bTime:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.lesslimit``: The ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:LESSLimit`` command.
            - ``.morelimit``: The ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:MORELimit`` command.
            - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe:QUALifier`` command.
        """
        return self._time


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
        - This command specifies the error type be used for LIN trigger. B<x>

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:ERRTYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN:ERRTYPE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN:ERRTYPE value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:LIN:ERRTYPE {SYNC|PARity|CHecksum|HEADertime|RESPtime|FRAMetime}
        - TRIGger:A:BUS:B<x>:LIN:ERRTYPE?
        ```

    Info:
        - ``SYNC`` sets the LIN error type to SYNC.
        - ``PARity`` sets the LIN error type to parity.
        - ``CHecksum`` sets the LIN error type to checksum.
        - ``HEADertime`` sets the LIN error type to header time.
        - ``RESPtime`` sets the LIN error type to response time.
        - ``FRAMetime`` sets the LIN error type to frame time.
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
        - This command specifies the LIN data qualifier. This only applies if the trigger condition
          is IDANDDATA or DATA. The bus number is specified by x.

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
        - TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?
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
            - This command specifies the LIN data qualifier. This only applies if the trigger
              condition is IDANDDATA or DATA. The bus number is specified by x.

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
            - TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?
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
            - This command specifies the error type be used for LIN trigger. B<x>

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:ERRTYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN:ERRTYPE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:ERRTYPE value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:LIN:ERRTYPE {SYNC|PARity|CHecksum|HEADertime|RESPtime|FRAMetime}
            - TRIGger:A:BUS:B<x>:LIN:ERRTYPE?
            ```

        Info:
            - ``SYNC`` sets the LIN error type to SYNC.
            - ``PARity`` sets the LIN error type to parity.
            - ``CHecksum`` sets the LIN error type to checksum.
            - ``HEADertime`` sets the LIN error type to header time.
            - ``RESPtime`` sets the LIN error type to response time.
            - ``FRAMetime`` sets the LIN error type to frame time.
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
        - This command specifies the qualifier to use when triggering on the FlexRay bus frame ID
          field. The trigger condition needs to be set to IDentifier (using
          ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

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
        - TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier?
        ```

    Info:
        - ``LESSthan`` sets the frame ID qualifier to less than.
        - ``MOREthan`` sets the frame ID qualifier to greater than.
        - ``EQual`` sets the frame ID qualifier to equal.
        - ``UNEQual`` sets the frame ID qualifier to not equal.
        - ``LESSEQual`` sets the frame ID qualifier to less than or equal.
        - ``MOREEQual`` sets the frame ID qualifier to greater than or equal.
        - ``INrange`` sets the frame ID qualifier to in range.
        - ``OUTrange`` sets the frame ID qualifier to out of range.
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
            - This command specifies the qualifier to use when triggering on the FlexRay bus frame
              ID field. The trigger condition needs to be set to IDentifier (using
              ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

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
            - TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - TRIGger:A:BUS:B<x>:FLEXray:FRAMEID:QUALifier?
            ```

        Info:
            - ``LESSthan`` sets the frame ID qualifier to less than.
            - ``MOREthan`` sets the frame ID qualifier to greater than.
            - ``EQual`` sets the frame ID qualifier to equal.
            - ``UNEQual`` sets the frame ID qualifier to not equal.
            - ``LESSEQual`` sets the frame ID qualifier to less than or equal.
            - ``MOREEQual`` sets the frame ID qualifier to greater than or equal.
            - ``INrange`` sets the frame ID qualifier to in range.
            - ``OUTrange`` sets the frame ID qualifier to out of range.
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
        - This command specifies the qualifier (<, >, =, <=, >=, not =, in range, out of range) to
          use when triggering on the FlexRay bus data field. The trigger condition needs to be set
          to ID or IDANDDATA (using ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

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
        - TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier?
        ```

    Info:
        - ``LESSthan`` sets the data qualifier to less than.
        - ``MOREthan`` sets the data qualifier to greater than.
        - ``EQual`` sets the data qualifier to eqaual.
        - ``UNEQual`` sets the data qualifier to not equal.
        - ``LESSEQual`` sets the data qualifier to less than or equal.
        - ``MOREEQual`` sets the data qualifier to greater than or equal.
        - ``INrange`` sets the data qualifier to in range.
        - ``OUTrange`` sets the data qualifier to out of range.
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
            - This command specifies the qualifier (<, >, =, <=, >=, not =, in range, out of range)
              to use when triggering on the FlexRay bus data field. The trigger condition needs to
              be set to ID or IDANDDATA (using ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

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
            - TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - TRIGger:A:BUS:B<x>:FLEXray:DATa:QUALifier?
            ```

        Info:
            - ``LESSthan`` sets the data qualifier to less than.
            - ``MOREthan`` sets the data qualifier to greater than.
            - ``EQual`` sets the data qualifier to eqaual.
            - ``UNEQual`` sets the data qualifier to not equal.
            - ``LESSEQual`` sets the data qualifier to less than or equal.
            - ``MOREEQual`` sets the data qualifier to greater than or equal.
            - ``INrange`` sets the data qualifier to in range.
            - ``OUTrange`` sets the data qualifier to out of range.
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
        - This command specifies the qualifier (<, >, =, <=, >=, not =, in range, out of range) to
          use when triggering on the FlexRay bus cycle count field. The trigger condition must be
          set to CYCLEcount (using ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

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
        - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier?
        ```

    Info:
        - ``LESSthan`` sets the cycle count qualifier to less than.
        - ``MOREthan`` sets the cycle count qualifier to more than.
        - ``EQual`` sets the cycle count qualifier to equal.
        - ``UNEQual`` sets the cycle count qualifier to not equal.
        - ``LESSEQual`` sets the cycle count qualifier to less than or equal.
        - ``MOREEQual`` sets the cycle count qualifier to greater than or equal.
        - ``INrange`` sets the cycle count qualifier to in range.
        - ``OUTrange`` sets the cycle count qualifier to out of range.
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
            - This command specifies the qualifier (<, >, =, <=, >=, not =, in range, out of range)
              to use when triggering on the FlexRay bus cycle count field. The trigger condition
              must be set to CYCLEcount (using ``TRIGGER:A:BUS:BX:FLEXRAY:CONDITION``). B<x>

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
            - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - TRIGger:A:BUS:B<x>:FLEXray:CYCLEcount:QUALifier?
            ```

        Info:
            - ``LESSthan`` sets the cycle count qualifier to less than.
            - ``MOREthan`` sets the cycle count qualifier to more than.
            - ``EQual`` sets the cycle count qualifier to equal.
            - ``UNEQual`` sets the cycle count qualifier to not equal.
            - ``LESSEQual`` sets the cycle count qualifier to less than or equal.
            - ``MOREEQual`` sets the cycle count qualifier to greater than or equal.
            - ``INrange`` sets the cycle count qualifier to in range.
            - ``OUTrange`` sets the cycle count qualifier to out of range.
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


class TriggerABusBItemEthernetTcpheaderSourceportValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SOUrceport:VALue`` command.

    Description:
        - When the Ethernet trigger condition is set to TCPHeader, this command specifies the 16-bit
          source port address that is to be used in the trigger (along with the destination port
          address, the sequence number and the acknowledgement number). The default is all X's
          (don't care). B<x> is the bus number B1-B4.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SOUrceport:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SOUrceport:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SOUrceport:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SOUrceport:VALue <QString>
        - TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SOUrceport:VALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemEthernetTcpheaderSourceport(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SOUrceport`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SOUrceport?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SOUrceport?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SOUrceport:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemEthernetTcpheaderSourceportValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> TriggerABusBItemEthernetTcpheaderSourceportValue:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SOUrceport:VALue`` command.

        Description:
            - When the Ethernet trigger condition is set to TCPHeader, this command specifies the
              16-bit source port address that is to be used in the trigger (along with the
              destination port address, the sequence number and the acknowledgement number). The
              default is all X's (don't care). B<x> is the bus number B1-B4.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SOUrceport:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SOUrceport:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SOUrceport:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SOUrceport:VALue <QString>
            - TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SOUrceport:VALue?
            ```
        """
        return self._value


class TriggerABusBItemEthernetTcpheaderSeqnumValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SEQnum:VALue`` command.

    Description:
        - When the Ethernet trigger condition is set to TCPHeader, this command specifies the 32-bit
          sequence number that is to be used in the trigger (along with the destination and source
          port addresses and the acknowledgement value). The default is all X's (don't care). B<x>
          is the bus number B1-B4.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SEQnum:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SEQnum:VALue?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SEQnum:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SEQnum:VALue <QString>
        - TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SEQnum:VALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemEthernetTcpheaderSeqnum(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SEQnum`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SEQnum?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SEQnum?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SEQnum:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemEthernetTcpheaderSeqnumValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> TriggerABusBItemEthernetTcpheaderSeqnumValue:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SEQnum:VALue`` command.

        Description:
            - When the Ethernet trigger condition is set to TCPHeader, this command specifies the
              32-bit sequence number that is to be used in the trigger (along with the destination
              and source port addresses and the acknowledgement value). The default is all X's
              (don't care). B<x> is the bus number B1-B4.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SEQnum:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SEQnum:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SEQnum:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SEQnum:VALue <QString>
            - TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SEQnum:VALue?
            ```
        """
        return self._value


class TriggerABusBItemEthernetTcpheaderDestinationportValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:DESTinationport:VALue`` command.

    Description:
        - When the Ethernet trigger condition is set TCPHeader, this command specifies the 16-bit
          destination port address value that is to be used in the trigger (along with the
          acknowledgement value, source port address and the sequence number). The default is all
          X's (don't care). B<x> is the bus number B1-B4.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:DESTinationport:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:DESTinationport:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:DESTinationport:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:DESTinationport:VALue <QString>
        - TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:DESTinationport:VALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemEthernetTcpheaderDestinationport(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:DESTinationport`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:DESTinationport?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:DESTinationport?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:DESTinationport:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemEthernetTcpheaderDestinationportValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> TriggerABusBItemEthernetTcpheaderDestinationportValue:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:DESTinationport:VALue`` command.

        Description:
            - When the Ethernet trigger condition is set TCPHeader, this command specifies the
              16-bit destination port address value that is to be used in the trigger (along with
              the acknowledgement value, source port address and the sequence number). The default
              is all X's (don't care). B<x> is the bus number B1-B4.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:DESTinationport:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:DESTinationport:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:DESTinationport:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:DESTinationport:VALue <QString>
            - TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:DESTinationport:VALue?
            ```
        """
        return self._value


class TriggerABusBItemEthernetTcpheaderAcknumValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:ACKnum:VALue`` command.

    Description:
        - When the Ethernet trigger condition is set to TCPHeader, this command specifies the 32-bit
          acknowledgement number that is to be used in the trigger (along with the destination and
          source port addresses and the sequence number). The default is all X's (don't care). B<x>
          is the bus number B1-B4.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:ACKnum:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:ACKnum:VALue?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:ACKnum:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:ACKnum:VALue <QString>
        - TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:ACKnum:VALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemEthernetTcpheaderAcknum(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:ACKnum`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:ACKnum?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:ACKnum?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:ACKnum:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemEthernetTcpheaderAcknumValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> TriggerABusBItemEthernetTcpheaderAcknumValue:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:ACKnum:VALue`` command.

        Description:
            - When the Ethernet trigger condition is set to TCPHeader, this command specifies the
              32-bit acknowledgement number that is to be used in the trigger (along with the
              destination and source port addresses and the sequence number). The default is all X's
              (don't care). B<x> is the bus number B1-B4.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:ACKnum:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:ACKnum:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:ACKnum:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:ACKnum:VALue <QString>
            - TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:ACKnum:VALue?
            ```
        """
        return self._value


class TriggerABusBItemEthernetTcpheader(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.acknum``: The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:ACKnum`` command tree.
        - ``.destinationport``: The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:DESTinationport``
          command tree.
        - ``.seqnum``: The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SEQnum`` command tree.
        - ``.sourceport``: The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SOUrceport`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._acknum = TriggerABusBItemEthernetTcpheaderAcknum(device, f"{self._cmd_syntax}:ACKnum")
        self._destinationport = TriggerABusBItemEthernetTcpheaderDestinationport(
            device, f"{self._cmd_syntax}:DESTinationport"
        )
        self._seqnum = TriggerABusBItemEthernetTcpheaderSeqnum(device, f"{self._cmd_syntax}:SEQnum")
        self._sourceport = TriggerABusBItemEthernetTcpheaderSourceport(
            device, f"{self._cmd_syntax}:SOUrceport"
        )

    @property
    def acknum(self) -> TriggerABusBItemEthernetTcpheaderAcknum:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:ACKnum`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:ACKnum?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:ACKnum?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:ACKnum:VALue`` command.
        """
        return self._acknum

    @property
    def destinationport(self) -> TriggerABusBItemEthernetTcpheaderDestinationport:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:DESTinationport`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:DESTinationport?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:DESTinationport?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:DESTinationport:VALue``
              command.
        """
        return self._destinationport

    @property
    def seqnum(self) -> TriggerABusBItemEthernetTcpheaderSeqnum:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SEQnum`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SEQnum?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SEQnum?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SEQnum:VALue`` command.
        """
        return self._seqnum

    @property
    def sourceport(self) -> TriggerABusBItemEthernetTcpheaderSourceport:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SOUrceport`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SOUrceport?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SOUrceport?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SOUrceport:VALue`` command.
        """
        return self._sourceport


class TriggerABusBItemEthernetQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:QUALifier`` command.

    Description:
        - This command specifies the qualifier to be used when the Ethernet trigger condition is set
          to MACLENgth or DATa. Normally, the Ethernet qualifier is set to 'Equal to'. B<x> is the
          bus number B1-B4.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:QUALifier?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:QUALifier?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:QUALifier value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ETHERnet:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - TRIGger:A:BUS:B<x>:ETHERnet:QUALifier?
        ```
    """  # noqa: E501


class TriggerABusBItemEthernetQtagValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:QTAG:VALue`` command.

    Description:
        - When the Ethernet trigger condition is set to QTAG, this command specifies the 32-bit
          Q-Tag value to trigger on. The default is all X's (don't care). B<x> is the bus number
          B1-B4.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:QTAG:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:QTAG:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:QTAG:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ETHERnet:QTAG:VALue <QString>
        - TRIGger:A:BUS:B<x>:ETHERnet:QTAG:VALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemEthernetQtag(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:QTAG`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:QTAG?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:QTAG?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:ETHERnet:QTAG:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemEthernetQtagValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> TriggerABusBItemEthernetQtagValue:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:QTAG:VALue`` command.

        Description:
            - When the Ethernet trigger condition is set to QTAG, this command specifies the 32-bit
              Q-Tag value to trigger on. The default is all X's (don't care). B<x> is the bus number
              B1-B4.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:QTAG:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:QTAG:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:QTAG:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ETHERnet:QTAG:VALue <QString>
            - TRIGger:A:BUS:B<x>:ETHERnet:QTAG:VALue?
            ```
        """
        return self._value


class TriggerABusBItemEthernetMacTypeValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:VALue`` command.

    Description:
        - When the Ethernet trigger condition is set to MACLENgth, and the qualifier is set to
          LESSthan, MOREthan, EQual, UNEQual, LESSEQual or MOREEQual, this command specifies the
          16-bit value to trigger on. When the qualifier is set to INrange or OUTrange, this command
          specifies the lower limit of the range. (Use the command to set the upper limit of the
          range.) The default is all X's (don't care). B<x> is the bus number B1-B4.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:VALue <QString>
        - TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:VALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemEthernetMacTypeHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:HIVALue`` command.

    Description:
        - When the Ethernet trigger condition is set to MACLENgth, and the qualifier is set to
          INrange or OUTrange, this command specifies the upper data value of the range. (Use the
          command to specify the lower limit of the range.) The default is all X's (don't care).
          B<x> is the bus number B1-B4.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:HIVALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:HIVALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:HIVALue <QString>
        - TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:HIVALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemEthernetMacType(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:HIVALue`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = TriggerABusBItemEthernetMacTypeHivalue(
            device, f"{self._cmd_syntax}:HIVALue"
        )
        self._value = TriggerABusBItemEthernetMacTypeValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def hivalue(self) -> TriggerABusBItemEthernetMacTypeHivalue:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:HIVALue`` command.

        Description:
            - When the Ethernet trigger condition is set to MACLENgth, and the qualifier is set to
              INrange or OUTrange, this command specifies the upper data value of the range. (Use
              the command to specify the lower limit of the range.) The default is all X's (don't
              care). B<x> is the bus number B1-B4.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:HIVALue?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:HIVALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:HIVALue <QString>
            - TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:HIVALue?
            ```
        """
        return self._hivalue

    @property
    def value(self) -> TriggerABusBItemEthernetMacTypeValue:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:VALue`` command.

        Description:
            - When the Ethernet trigger condition is set to MACLENgth, and the qualifier is set to
              LESSthan, MOREthan, EQual, UNEQual, LESSEQual or MOREEQual, this command specifies the
              16-bit value to trigger on. When the qualifier is set to INrange or OUTrange, this
              command specifies the lower limit of the range. (Use the command to set the upper
              limit of the range.) The default is all X's (don't care). B<x> is the bus number
              B1-B4.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:VALue?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:VALue <QString>
            - TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:VALue?
            ```
        """
        return self._value


class TriggerABusBItemEthernetMacLengthValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:VALue`` command.

    Description:
        - When the Ethernet trigger condition is set to MACLENgth, and the qualifier is set to
          LESSthan, MOREthan, EQual, UNEQual, LESSEQual or MOREEQual, this command specifies the
          16-bit value to trigger on. When the qualifier is set to INrange or OUTrange, this command
          specifies the lower limit of the range. (Use the command to set the upper limit of the
          range.) The default is all X's (don't care). B<x> is the bus number B1-B4.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:VALue <QString>
        - TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:VALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemEthernetMacLengthHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:HIVALue`` command.

    Description:
        - When the Ethernet trigger condition is set to MACLENgth, and the qualifier is set to
          INrange or OUTrange, this command specifies the upper data value of the range. (Use the
          command to specify the lower limit of the range.) The default is all X's (don't care).
          B<x> is the bus number B1-B4.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:HIVALue?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:HIVALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:HIVALue <QString>
        - TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:HIVALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemEthernetMacLength(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:HIVALue`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = TriggerABusBItemEthernetMacLengthHivalue(
            device, f"{self._cmd_syntax}:HIVALue"
        )
        self._value = TriggerABusBItemEthernetMacLengthValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def hivalue(self) -> TriggerABusBItemEthernetMacLengthHivalue:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:HIVALue`` command.

        Description:
            - When the Ethernet trigger condition is set to MACLENgth, and the qualifier is set to
              INrange or OUTrange, this command specifies the upper data value of the range. (Use
              the command to specify the lower limit of the range.) The default is all X's (don't
              care). B<x> is the bus number B1-B4.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:HIVALue?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:HIVALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:HIVALue <QString>
            - TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:HIVALue?
            ```
        """
        return self._hivalue

    @property
    def value(self) -> TriggerABusBItemEthernetMacLengthValue:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:VALue`` command.

        Description:
            - When the Ethernet trigger condition is set to MACLENgth, and the qualifier is set to
              LESSthan, MOREthan, EQual, UNEQual, LESSEQual or MOREEQual, this command specifies the
              16-bit value to trigger on. When the qualifier is set to INrange or OUTrange, this
              command specifies the lower limit of the range. (Use the command to set the upper
              limit of the range.) The default is all X's (don't care). B<x> is the bus number
              B1-B4.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:VALue?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:VALue <QString>
            - TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:VALue?
            ```
        """
        return self._value


class TriggerABusBItemEthernetMacAddressSourceValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:SOUrce:VALue`` command.

    Description:
        - When the Ethernet trigger condition is set to MACADDress, this command specifies the
          48-bit MAC source address value that is to be used in the trigger (along with the
          destination address value). The default is all X's (don't care). B<x> is the bus number
          B1-B4.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:SOUrce:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:SOUrce:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:SOUrce:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:SOUrce:VALue <QString>
        - TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:SOUrce:VALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemEthernetMacAddressSource(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:SOUrce`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:SOUrce?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:SOUrce:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemEthernetMacAddressSourceValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> TriggerABusBItemEthernetMacAddressSourceValue:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:SOUrce:VALue`` command.

        Description:
            - When the Ethernet trigger condition is set to MACADDress, this command specifies the
              48-bit MAC source address value that is to be used in the trigger (along with the
              destination address value). The default is all X's (don't care). B<x> is the bus
              number B1-B4.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:SOUrce:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:SOUrce:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:SOUrce:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:SOUrce:VALue <QString>
            - TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:SOUrce:VALue?
            ```
        """
        return self._value


class TriggerABusBItemEthernetMacAddressDestinationValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:DESTination:VALue`` command.

    Description:
        - When the Ethernet trigger condition is set to MACADDress, this command specifies the
          48-bit MAC destination address that is to be used in the trigger (along with the source
          address value). The default is all X's (don't care). B<x> is the bus number B1-B4.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:DESTination:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:DESTination:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:DESTination:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:DESTination:VALue <QString>
        - TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:DESTination:VALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemEthernetMacAddressDestination(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:DESTination`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:DESTination?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:DESTination?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:DESTination:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemEthernetMacAddressDestinationValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> TriggerABusBItemEthernetMacAddressDestinationValue:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:DESTination:VALue`` command.

        Description:
            - When the Ethernet trigger condition is set to MACADDress, this command specifies the
              48-bit MAC destination address that is to be used in the trigger (along with the
              source address value). The default is all X's (don't care). B<x> is the bus number
              B1-B4.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:DESTination:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:DESTination:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:DESTination:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:DESTination:VALue <QString>
            - TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:DESTination:VALue?
            ```
        """
        return self._value


class TriggerABusBItemEthernetMacAddress(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.destination``: The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:DESTination`` command
          tree.
        - ``.source``: The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:SOUrce`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._destination = TriggerABusBItemEthernetMacAddressDestination(
            device, f"{self._cmd_syntax}:DESTination"
        )
        self._source = TriggerABusBItemEthernetMacAddressSource(
            device, f"{self._cmd_syntax}:SOUrce"
        )

    @property
    def destination(self) -> TriggerABusBItemEthernetMacAddressDestination:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:DESTination`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:DESTination?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:DESTination?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:DESTination:VALue`` command.
        """
        return self._destination

    @property
    def source(self) -> TriggerABusBItemEthernetMacAddressSource:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:SOUrce`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:SOUrce?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:SOUrce:VALue`` command.
        """
        return self._source


class TriggerABusBItemEthernetMac(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:MAC?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:MAC?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.address``: The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess`` command tree.
        - ``.length``: The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth`` command tree.
        - ``.type``: The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._address = TriggerABusBItemEthernetMacAddress(device, f"{self._cmd_syntax}:ADDRess")
        self._length = TriggerABusBItemEthernetMacLength(device, f"{self._cmd_syntax}:LENgth")
        self._type = TriggerABusBItemEthernetMacType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def address(self) -> TriggerABusBItemEthernetMacAddress:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.destination``: The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:DESTination`` command
              tree.
            - ``.source``: The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess:SOUrce`` command tree.
        """
        return self._address

    @property
    def length(self) -> TriggerABusBItemEthernetMacLength:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:HIVALue`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth:VALue`` command.
        """
        return self._length

    @property
    def type(self) -> TriggerABusBItemEthernetMacType:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:HIVALue`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe:VALue`` command.
        """
        return self._type


class TriggerABusBItemEthernetIpheaderSourceaddrValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:SOUrceaddr:VALue`` command.

    Description:
        - When the Ethernet trigger condition is set to IPHeader, this command specifies the value
          of the 32-bit source address that is to be used in the trigger (along with the destination
          address and protocol value). The IP source address is a standard IP address such as
          192.168.0.1. The default is all X's (don't care). B<x> is the bus number B1-B4.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:SOUrceaddr:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:SOUrceaddr:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:SOUrceaddr:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:SOUrceaddr:VALue <QString>
        - TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:SOUrceaddr:VALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemEthernetIpheaderSourceaddr(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:SOUrceaddr`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:SOUrceaddr?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:SOUrceaddr?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:SOUrceaddr:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemEthernetIpheaderSourceaddrValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> TriggerABusBItemEthernetIpheaderSourceaddrValue:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:SOUrceaddr:VALue`` command.

        Description:
            - When the Ethernet trigger condition is set to IPHeader, this command specifies the
              value of the 32-bit source address that is to be used in the trigger (along with the
              destination address and protocol value). The IP source address is a standard IP
              address such as 192.168.0.1. The default is all X's (don't care). B<x> is the bus
              number B1-B4.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:SOUrceaddr:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:SOUrceaddr:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:SOUrceaddr:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:SOUrceaddr:VALue <QString>
            - TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:SOUrceaddr:VALue?
            ```
        """
        return self._value


class TriggerABusBItemEthernetIpheaderProtocolValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:PROTOcol:VALue`` command.

    Description:
        - When the Ethernet trigger condition is set to IPHeader, this command specifies the value
          of the 8-bit protocol field that is to be used in the trigger (along with the source and
          destination addresses). The default is all X's (don't care). B<x> is the bus number B1-B4.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:PROTOcol:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:PROTOcol:VALue?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:PROTOcol:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:PROTOcol:VALue <QString>
        - TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:PROTOcol:VALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemEthernetIpheaderProtocol(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:PROTOcol`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:PROTOcol?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:PROTOcol?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:PROTOcol:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemEthernetIpheaderProtocolValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> TriggerABusBItemEthernetIpheaderProtocolValue:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:PROTOcol:VALue`` command.

        Description:
            - When the Ethernet trigger condition is set to IPHeader, this command specifies the
              value of the 8-bit protocol field that is to be used in the trigger (along with the
              source and destination addresses). The default is all X's (don't care). B<x> is the
              bus number B1-B4.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:PROTOcol:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:PROTOcol:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:PROTOcol:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:PROTOcol:VALue <QString>
            - TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:PROTOcol:VALue?
            ```
        """
        return self._value


class TriggerABusBItemEthernetIpheaderDestinationaddrValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:DESTinationaddr:VALue`` command.

    Description:
        - When the Ethernet trigger condition is set to IPHeader, this command specifies the value
          of the 32-bit destination address that is to be used in the trigger (along with the source
          address and protocol value). The IP destination address is a standard IP address such as
          192.168.0.1. The default is all X's (don't care). B<x> is the bus number B1-B4.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:DESTinationaddr:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:DESTinationaddr:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:DESTinationaddr:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:DESTinationaddr:VALue <QString>
        - TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:DESTinationaddr:VALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemEthernetIpheaderDestinationaddr(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:DESTinationaddr`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:DESTinationaddr?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:DESTinationaddr?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:DESTinationaddr:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemEthernetIpheaderDestinationaddrValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def value(self) -> TriggerABusBItemEthernetIpheaderDestinationaddrValue:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:DESTinationaddr:VALue`` command.

        Description:
            - When the Ethernet trigger condition is set to IPHeader, this command specifies the
              value of the 32-bit destination address that is to be used in the trigger (along with
              the source address and protocol value). The IP destination address is a standard IP
              address such as 192.168.0.1. The default is all X's (don't care). B<x> is the bus
              number B1-B4.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:DESTinationaddr:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:DESTinationaddr:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:DESTinationaddr:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:DESTinationaddr:VALue <QString>
            - TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:DESTinationaddr:VALue?
            ```
        """
        return self._value


class TriggerABusBItemEthernetIpheader(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.destinationaddr``: The ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:DESTinationaddr`` command
          tree.
        - ``.protocol``: The ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:PROTOcol`` command tree.
        - ``.sourceaddr``: The ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:SOUrceaddr`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._destinationaddr = TriggerABusBItemEthernetIpheaderDestinationaddr(
            device, f"{self._cmd_syntax}:DESTinationaddr"
        )
        self._protocol = TriggerABusBItemEthernetIpheaderProtocol(
            device, f"{self._cmd_syntax}:PROTOcol"
        )
        self._sourceaddr = TriggerABusBItemEthernetIpheaderSourceaddr(
            device, f"{self._cmd_syntax}:SOUrceaddr"
        )

    @property
    def destinationaddr(self) -> TriggerABusBItemEthernetIpheaderDestinationaddr:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:DESTinationaddr`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:DESTinationaddr?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:DESTinationaddr?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:DESTinationaddr:VALue``
              command.
        """
        return self._destinationaddr

    @property
    def protocol(self) -> TriggerABusBItemEthernetIpheaderProtocol:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:PROTOcol`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:PROTOcol?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:PROTOcol?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:PROTOcol:VALue`` command.
        """
        return self._protocol

    @property
    def sourceaddr(self) -> TriggerABusBItemEthernetIpheaderSourceaddr:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:SOUrceaddr`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:SOUrceaddr?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:SOUrceaddr?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:SOUrceaddr:VALue`` command.
        """
        return self._sourceaddr


class TriggerABusBItemEthernetFrametype(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe`` command.

    Description:
        - This command specifies the Ethernet frame type: either Basic or QTag (IEEE 802.1Q, or VLAN
          tagging). The default is Basic. B<x> is the bus number B1-B4.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe {BASic|QTAG}
        - TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe?
        ```

    Info:
        - ``BASic`` is the standard Ethernet frame.
        - ``QTAG`` is the Q-Tag Ethernet frame (also called VLAN tagging.).
    """


class TriggerABusBItemEthernetDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue`` command.

    Description:
        - When the Ethernet trigger condition is set to DATa, and the qualifier is set to LESSthan,
          MOREthan, EQual, UNEQual, LESSEQual or MOREEQual, this command specifies the value to
          trigger on. When the Ethernet trigger condition is set to DATa, and the qualifier is set
          to INrange or OUTrange, this command specifies the lower limit of the range. (Use the
          command ``TRIGGER:A:BUS:BX:ETHERNET:DATA:HIVALUE`` to set the upper limit of the range.)
          The default is all X's (don't care). B<x> is the bus number B1-B4.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue <QString>
        - TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemEthernetDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:SIZe`` command.

    Description:
        - When the Ethernet trigger condition is set to DATa, this command specifies the number of
          contiguous TCP/IPv4/MAC client data bytes to trigger on. B<x> is the bus number B1-B4.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:SIZe?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:SIZe?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ETHERnet:DATa:SIZe <NR1>
        - TRIGger:A:BUS:B<x>:ETHERnet:DATa:SIZe?
        ```
    """


class TriggerABusBItemEthernetDataOffset(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:OFFSet`` command.

    Description:
        - When the Ethernet trigger condition is set to DATa, this command specifies where in the
          data field to look for the data trigger value. It specifies the offset into the data
          field, in bytes, where the value will be matched. The default is -1 (don't care). B<x> is
          the bus number B1-B4.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:OFFSet?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:OFFSet?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:OFFSet value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ETHERnet:DATa:OFFSet <NR1>
        - TRIGger:A:BUS:B<x>:ETHERnet:DATa:OFFSet?
        ```

    Info:
        - ``<NR1>`` is an integer whose minimum and default values are -1 (don't care) and maximum
          is 1,499.
    """


class TriggerABusBItemEthernetDataHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:HIVALue`` command.

    Description:
        - When the Ethernet trigger condition is set to DATa, and the qualifier is set to either
          INrange or OUTrange, this command specifies the upper data value of the range. (Use the
          command ``TRIGGER:A:BUS:BX:ETHERNET:DATA:VALUE`` to specify the lower limit of the range.)
          The default is all X's (don't care). B<x> is the bus number B1-B4.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:HIVALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:HIVALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:HIVALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ETHERnet:DATa:HIVALue <QString>
        - TRIGger:A:BUS:B<x>:ETHERnet:DATa:HIVALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemEthernetData(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:DATa?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:HIVALue`` command.
        - ``.offset``: The ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:OFFSet`` command.
        - ``.size``: The ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:SIZe`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = TriggerABusBItemEthernetDataHivalue(device, f"{self._cmd_syntax}:HIVALue")
        self._offset = TriggerABusBItemEthernetDataOffset(device, f"{self._cmd_syntax}:OFFSet")
        self._size = TriggerABusBItemEthernetDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._value = TriggerABusBItemEthernetDataValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def hivalue(self) -> TriggerABusBItemEthernetDataHivalue:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:HIVALue`` command.

        Description:
            - When the Ethernet trigger condition is set to DATa, and the qualifier is set to either
              INrange or OUTrange, this command specifies the upper data value of the range. (Use
              the command ``TRIGGER:A:BUS:BX:ETHERNET:DATA:VALUE`` to specify the lower limit of the
              range.) The default is all X's (don't care). B<x> is the bus number B1-B4.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:HIVALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:HIVALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ETHERnet:DATa:HIVALue <QString>
            - TRIGger:A:BUS:B<x>:ETHERnet:DATa:HIVALue?
            ```
        """
        return self._hivalue

    @property
    def offset(self) -> TriggerABusBItemEthernetDataOffset:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:OFFSet`` command.

        Description:
            - When the Ethernet trigger condition is set to DATa, this command specifies where in
              the data field to look for the data trigger value. It specifies the offset into the
              data field, in bytes, where the value will be matched. The default is -1 (don't care).
              B<x> is the bus number B1-B4.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:OFFSet?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:OFFSet?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:OFFSet value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ETHERnet:DATa:OFFSet <NR1>
            - TRIGger:A:BUS:B<x>:ETHERnet:DATa:OFFSet?
            ```

        Info:
            - ``<NR1>`` is an integer whose minimum and default values are -1 (don't care) and
              maximum is 1,499.
        """
        return self._offset

    @property
    def size(self) -> TriggerABusBItemEthernetDataSize:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:SIZe`` command.

        Description:
            - When the Ethernet trigger condition is set to DATa, this command specifies the number
              of contiguous TCP/IPv4/MAC client data bytes to trigger on. B<x> is the bus number
              B1-B4.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:SIZe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:SIZe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:SIZe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ETHERnet:DATa:SIZe <NR1>
            - TRIGger:A:BUS:B<x>:ETHERnet:DATa:SIZe?
            ```
        """
        return self._size

    @property
    def value(self) -> TriggerABusBItemEthernetDataValue:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue`` command.

        Description:
            - When the Ethernet trigger condition is set to DATa, and the qualifier is set to
              LESSthan, MOREthan, EQual, UNEQual, LESSEQual or MOREEQual, this command specifies the
              value to trigger on. When the Ethernet trigger condition is set to DATa, and the
              qualifier is set to INrange or OUTrange, this command specifies the lower limit of the
              range. (Use the command ``TRIGGER:A:BUS:BX:ETHERNET:DATA:HIVALUE`` to set the upper
              limit of the range.) The default is all X's (don't care). B<x> is the bus number
              B1-B4.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue <QString>
            - TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue?
            ```
        """
        return self._value


class TriggerABusBItemEthernetCondition(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet:CONDition`` command.

    Description:
        - This command specifies a field or condition within an Ethernet frame to trigger on. B<x>
          is the bus number B1-B4.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:CONDition?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:CONDition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ETHERnet:CONDition value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ETHERnet:CONDition {SFD|MACADDRess|MACLENgth|IPHeader|TCPHeader|DATa|EOP|IDLe|FCSError|QTAG}
        - TRIGger:A:BUS:B<x>:ETHERnet:CONDition?
        ```

    Info:
        - ``SFD`` - Start of frame delimiter.
        - ``MACADDRess`` - MAC addresses field.
        - ``MACLENgth`` - MAC length/type field.
        - ``IPHeader`` - IP header field. This argument is only available when PROTOCOL is set to
          IPv4 (using the command ``BUS:BX:ETHERNET:PROTOCOL``).
        - ``TCPHeader`` - TCP header field. This argument is only available when PROTOCOL is set to
          IPv4 (using the command ``BUS:BX:ETHERNET:PROTOCOL``).
        - ``DATa`` - TCP/IPv4 or MAC protocol client data field. Use the command
          ``BUS:BX:ETHERNET:PROTOCOL`` to specify either TCP/IPv4 or OTHER. If the protocol is set
          to OTHER, then DATa refers to the MAC client data.
        - ``EOP`` - End of Packet field.
        - ``IDLe`` - Idle field.
        - ``FCSError`` - Frame Check Sequence Error (CRC) field.
        - ``QTAG`` - IEEE 802.1Q (VLAN) control information field. In order to use QTAG as a trigger
          condition, the frame type must be set to QTAG (using
          ``TRIGGER:A:BUS:BX:ETHERNET:FRAMETYPE`` ).
    """  # noqa: E501


#  pylint: disable=too-many-instance-attributes
class TriggerABusBItemEthernet(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ETHERnet`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``TRIGger:A:BUS:B<x>:ETHERnet:CONDition`` command.
        - ``.data``: The ``TRIGger:A:BUS:B<x>:ETHERnet:DATa`` command tree.
        - ``.frametype``: The ``TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe`` command.
        - ``.ipheader``: The ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader`` command tree.
        - ``.mac``: The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC`` command tree.
        - ``.qtag``: The ``TRIGger:A:BUS:B<x>:ETHERnet:QTAG`` command tree.
        - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:ETHERnet:QUALifier`` command.
        - ``.tcpheader``: The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = TriggerABusBItemEthernetCondition(device, f"{self._cmd_syntax}:CONDition")
        self._data = TriggerABusBItemEthernetData(device, f"{self._cmd_syntax}:DATa")
        self._frametype = TriggerABusBItemEthernetFrametype(device, f"{self._cmd_syntax}:FRAMETYPe")
        self._ipheader = TriggerABusBItemEthernetIpheader(device, f"{self._cmd_syntax}:IPHeader")
        self._mac = TriggerABusBItemEthernetMac(device, f"{self._cmd_syntax}:MAC")
        self._qtag = TriggerABusBItemEthernetQtag(device, f"{self._cmd_syntax}:QTAG")
        self._qualifier = TriggerABusBItemEthernetQualifier(device, f"{self._cmd_syntax}:QUALifier")
        self._tcpheader = TriggerABusBItemEthernetTcpheader(device, f"{self._cmd_syntax}:TCPHeader")

    @property
    def condition(self) -> TriggerABusBItemEthernetCondition:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:CONDition`` command.

        Description:
            - This command specifies a field or condition within an Ethernet frame to trigger on.
              B<x> is the bus number B1-B4.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:CONDition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:CONDition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:CONDition value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ETHERnet:CONDition {SFD|MACADDRess|MACLENgth|IPHeader|TCPHeader|DATa|EOP|IDLe|FCSError|QTAG}
            - TRIGger:A:BUS:B<x>:ETHERnet:CONDition?
            ```

        Info:
            - ``SFD`` - Start of frame delimiter.
            - ``MACADDRess`` - MAC addresses field.
            - ``MACLENgth`` - MAC length/type field.
            - ``IPHeader`` - IP header field. This argument is only available when PROTOCOL is set
              to IPv4 (using the command ``BUS:BX:ETHERNET:PROTOCOL``).
            - ``TCPHeader`` - TCP header field. This argument is only available when PROTOCOL is set
              to IPv4 (using the command ``BUS:BX:ETHERNET:PROTOCOL``).
            - ``DATa`` - TCP/IPv4 or MAC protocol client data field. Use the command
              ``BUS:BX:ETHERNET:PROTOCOL`` to specify either TCP/IPv4 or OTHER. If the protocol is
              set to OTHER, then DATa refers to the MAC client data.
            - ``EOP`` - End of Packet field.
            - ``IDLe`` - Idle field.
            - ``FCSError`` - Frame Check Sequence Error (CRC) field.
            - ``QTAG`` - IEEE 802.1Q (VLAN) control information field. In order to use QTAG as a
              trigger condition, the frame type must be set to QTAG (using
              ``TRIGGER:A:BUS:BX:ETHERNET:FRAMETYPE`` ).
        """  # noqa: E501
        return self._condition

    @property
    def data(self) -> TriggerABusBItemEthernetData:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:DATa?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:DATa?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:HIVALue`` command.
            - ``.offset``: The ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:OFFSet`` command.
            - ``.size``: The ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:SIZe`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:ETHERnet:DATa:VALue`` command.
        """
        return self._data

    @property
    def frametype(self) -> TriggerABusBItemEthernetFrametype:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe`` command.

        Description:
            - This command specifies the Ethernet frame type: either Basic or QTag (IEEE 802.1Q, or
              VLAN tagging). The default is Basic. B<x> is the bus number B1-B4.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe {BASic|QTAG}
            - TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe?
            ```

        Info:
            - ``BASic`` is the standard Ethernet frame.
            - ``QTAG`` is the Q-Tag Ethernet frame (also called VLAN tagging.).
        """
        return self._frametype

    @property
    def ipheader(self) -> TriggerABusBItemEthernetIpheader:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.destinationaddr``: The ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:DESTinationaddr``
              command tree.
            - ``.protocol``: The ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:PROTOcol`` command tree.
            - ``.sourceaddr``: The ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader:SOUrceaddr`` command tree.
        """
        return self._ipheader

    @property
    def mac(self) -> TriggerABusBItemEthernetMac:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:MAC`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:MAC?``
              query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:MAC?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.address``: The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:ADDRess`` command tree.
            - ``.length``: The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:LENgth`` command tree.
            - ``.type``: The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC:TYPe`` command tree.
        """
        return self._mac

    @property
    def qtag(self) -> TriggerABusBItemEthernetQtag:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:QTAG`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:QTAG?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:QTAG?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:ETHERnet:QTAG:VALue`` command.
        """
        return self._qtag

    @property
    def qualifier(self) -> TriggerABusBItemEthernetQualifier:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:QUALifier`` command.

        Description:
            - This command specifies the qualifier to be used when the Ethernet trigger condition is
              set to MACLENgth or DATa. Normally, the Ethernet qualifier is set to 'Equal to'. B<x>
              is the bus number B1-B4.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:QUALifier?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:QUALifier?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:QUALifier value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ETHERnet:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - TRIGger:A:BUS:B<x>:ETHERnet:QUALifier?
            ```
        """  # noqa: E501
        return self._qualifier

    @property
    def tcpheader(self) -> TriggerABusBItemEthernetTcpheader:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.acknum``: The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:ACKnum`` command tree.
            - ``.destinationport``: The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:DESTinationport``
              command tree.
            - ``.seqnum``: The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SEQnum`` command tree.
            - ``.sourceport``: The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader:SOUrceport`` command
              tree.
        """
        return self._tcpheader


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
        - This command sets the addressing mode (standard or extended format) to be used when
          triggering on a CAN bus signal. The trigger condition must be set to IDANDDATA OR DATA
          (using ``TRIGGER:A:BUS:BX:CAN:CONDITION``). B<x> is the bus number (1-2).

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
        - TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe {STandard|EXTENDed}
        - TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?
        ```

    Info:
        - ``STandard`` specifies the standard addressing mode.
        - ``EXTENDed`` specifies the extended addressing mode.
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
            - This command sets the addressing mode (standard or extended format) to be used when
              triggering on a CAN bus signal. The trigger condition must be set to IDANDDATA OR DATA
              (using ``TRIGGER:A:BUS:BX:CAN:CONDITION``). B<x> is the bus number (1-2).

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
            - TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe {STandard|EXTENDed}
            - TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?
            ```

        Info:
            - ``STandard`` specifies the standard addressing mode.
            - ``EXTENDed`` specifies the extended addressing mode.
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


class TriggerABusBItemCanFdEsibit(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT`` command.

    Description:
        - This command specifies the binary data value to be used to search on CAN FD ESI bits. This
          only applies if the search condition has been set to FDESIBIT (using
          ``TRIGger:A:BUS:B<x>:CAN:CONDition`` ). B<x> is the bus number (1-2).

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT {ZERo|OFF|0|ONE|ON|1|NOCARE|X|x}
        - TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT?
        ```

    Info:
        - ``ZERo`` , OFF, and 0 specify that the BRS bit must have value 0. If queried, the command
          will always return 0 if set with these arguments.
        - ``ONE`` , ON, and 1 specify that the BRS bit must have value 1. If queried, the command
          will always return 1 if set with these arguments.
        - ``NOCARE`` , X, and x specify that the BRS bit may be either 1 or 0. If queried, the
          command will always return X if set with these arguments.
    """


class TriggerABusBItemCanFdBrsbit(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT`` command.

    Description:
        - This command specifies the binary data value to be used to search on CAN FD BRS bits. This
          only applies if the search condition has been set to FDBRSBIT (using
          ``TRIGger:A:BUS:B<x>:CAN:CONDition`` ). B<x> is the bus number (1-2).

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT {ZERo|OFF|0|ONE|ON|1|NOCARE|X|x}
        - TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT?
        ```

    Info:
        - ``ZERo`` , OFF, and 0 specify that the BRS bit must have value 0. If queried, the command
          will always return 0 if set with these arguments.
        - ``ONE`` , ON, and 1 specify that the BRS bit must have value 1. If queried, the command
          will always return 1 if set with these arguments.
        - ``NOCARE`` , X, and x specify that the BRS bit may be either 1 or 0. If queried, the
          command will always return X if set with these arguments.
    """


class TriggerABusBItemCanFd(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:FD`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:FD?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:FD?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.brsbit``: The ``TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT`` command.
        - ``.esibit``: The ``TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._brsbit = TriggerABusBItemCanFdBrsbit(device, f"{self._cmd_syntax}:BRSBIT")
        self._esibit = TriggerABusBItemCanFdEsibit(device, f"{self._cmd_syntax}:ESIBIT")

    @property
    def brsbit(self) -> TriggerABusBItemCanFdBrsbit:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT`` command.

        Description:
            - This command specifies the binary data value to be used to search on CAN FD BRS bits.
              This only applies if the search condition has been set to FDBRSBIT (using
              ``TRIGger:A:BUS:B<x>:CAN:CONDition`` ). B<x> is the bus number (1-2).

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT {ZERo|OFF|0|ONE|ON|1|NOCARE|X|x}
            - TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT?
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
    def esibit(self) -> TriggerABusBItemCanFdEsibit:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT`` command.

        Description:
            - This command specifies the binary data value to be used to search on CAN FD ESI bits.
              This only applies if the search condition has been set to FDESIBIT (using
              ``TRIGger:A:BUS:B<x>:CAN:CONDition`` ). B<x> is the bus number (1-2).

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT {ZERo|OFF|0|ONE|ON|1|NOCARE|X|x}
            - TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT?
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
        - This command sets the qualifier (<, >, =, not =, <=) to be used when triggering on a CAN
          bus signal. The trigger condition must be set to IDANDDATA OR DATA (using
          ``TRIGGER:A:BUS:BX:CAN:CONDITION``). B<x> is the bus number (1-2).

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
        - TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier {LESSthan|Than|EQual|UNEQual|LESSEQual|EQual}
        - TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?
        ```

    Info:
        - ``LESSthan`` sets the oscilloscope to trigger when the data is less than the qualifier
          value.
        - ``Than`` sets the oscilloscope to trigger when the data is than the qualifier value.
        - ``EQual`` sets the oscilloscope to trigger when the data is equal to the qualifier value.
        - ``UNEQual`` sets the oscilloscope to trigger when the data is not equal to the qualifier
          value.
        - ``LESSEQual`` sets the oscilloscope to trigger when the data is less than or equal to the
          qualifier value.
        - ``EQual`` sets the oscilloscope to trigger when the data is than or equal to the qualifier
          value.
    """


class TriggerABusBItemCanDataOffset(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet`` command.

    Description:
        - This command sets or queries the data offset value, in bytes, to use when triggering on
          the CAN data field. The bus number is specified by x. The trigger condition must be set to
          DATA or IDANDDATA.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet <NR1>
        - TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet?
        ```

    Info:
        - ``<NR1>`` is an integer whose minimum and default values are -1 (don't care), and the
          maximum is up to 7 (for CAN 2.0) or up to 63 (for ISO CAN FD and Non-ISO CAN FD).
    """


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
        - ``.offset``: The ``TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet`` command.
        - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier`` command.
        - ``.size``: The ``TRIGger:A:BUS:B<x>:CAN:DATa:SIZe`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:CAN:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._direction = TriggerABusBItemCanDataDirection(device, f"{self._cmd_syntax}:DIRection")
        self._offset = TriggerABusBItemCanDataOffset(device, f"{self._cmd_syntax}:OFFSet")
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
    def offset(self) -> TriggerABusBItemCanDataOffset:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet`` command.

        Description:
            - This command sets or queries the data offset value, in bytes, to use when triggering
              on the CAN data field. The bus number is specified by x. The trigger condition must be
              set to DATA or IDANDDATA.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet <NR1>
            - TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet?
            ```

        Info:
            - ``<NR1>`` is an integer whose minimum and default values are -1 (don't care), and the
              maximum is up to 7 (for CAN 2.0) or up to 63 (for ISO CAN FD and Non-ISO CAN FD).
        """
        return self._offset

    @property
    def qualifier(self) -> TriggerABusBItemCanDataQualifier:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier`` command.

        Description:
            - This command sets the qualifier (<, >, =, not =, <=) to be used when triggering on a
              CAN bus signal. The trigger condition must be set to IDANDDATA OR DATA (using
              ``TRIGGER:A:BUS:BX:CAN:CONDITION``). B<x> is the bus number (1-2).

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
            - TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier {LESSthan|Than|EQual|UNEQual|LESSEQual|EQual}
            - TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?
            ```

        Info:
            - ``LESSthan`` sets the oscilloscope to trigger when the data is less than the qualifier
              value.
            - ``Than`` sets the oscilloscope to trigger when the data is than the qualifier value.
            - ``EQual`` sets the oscilloscope to trigger when the data is equal to the qualifier
              value.
            - ``UNEQual`` sets the oscilloscope to trigger when the data is not equal to the
              qualifier value.
            - ``LESSEQual`` sets the oscilloscope to trigger when the data is less than or equal to
              the qualifier value.
            - ``EQual`` sets the oscilloscope to trigger when the data is than or equal to the
              qualifier value.
        """
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
        - This command sets the condition (start of frame, frame type, identifier, matching data,
          end of frame, missing ACK field, bit-stuffing error, form error, any error, CAN FD BRS
          bit, or CAN FD ESI bit) to be used to search on CAN bus data. B<x> is the bus number
          (1-2).

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:CONDition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:CONDition value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:CONDition {SOF|FRAMEtype|IDentifier|DATA|IDANDDATA|EOF|ACKMISS|ERROR|FORMERRor|ANYERRor|FDBRS|FDESI}
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
        - ``ERROR`` enables triggering on bit stuffing errors.
        - ``FORMERRor`` enables triggering on packet form errors.
        - ``ANYERRor`` enables triggering on any packet error (missing ACK, bit stuffing error, or
          form error).
        - ``FDBRS`` enables triggering on a CAN FD frame's BRS bit.
        - ``FDESI`` enables triggering on a CAN FD frame's ESI bit.
    """  # noqa: E501


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
        - This command sets the addressing mode (standard or extended format) to be used when
          triggering on a CAN bus signal. The trigger condition must be set to IDANDDATA OR DATA
          (using ``TRIGGER:A:BUS:BX:CAN:CONDITION``). B<x> is the bus number (1-2).

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe?``
          query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe {STandard|EXTENDed}
        - TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe?
        ```

    Info:
        - ``STandard`` specifies the standard addressing mode.
        - ``EXTENDed`` specifies the extended addressing mode.
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
            - This command sets the addressing mode (standard or extended format) to be used when
              triggering on a CAN bus signal. The trigger condition must be set to IDANDDATA OR DATA
              (using ``TRIGGER:A:BUS:BX:CAN:CONDITION``). B<x> is the bus number (1-2).

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
            - TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe {STandard|EXTENDed}
            - TRIGger:A:BUS:B<x>:CAN:ADDRess:MODe?
            ```

        Info:
            - ``STandard`` specifies the standard addressing mode.
            - ``EXTENDed`` specifies the extended addressing mode.
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
        - ``.fd``: The ``TRIGger:A:BUS:B<x>:CAN:FD`` command tree.
        - ``.frametype``: The ``TRIGger:A:BUS:B<x>:CAN:FRAMEtype`` command.
        - ``.identifier``: The ``TRIGger:A:BUS:B<x>:CAN:IDentifier`` command tree.
        - ``.address``: The ``TRIGger:A:BUS:B<x>:CAN:ADDRess`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = TriggerABusBItemCanCondition(device, f"{self._cmd_syntax}:CONDition")
        self._data = TriggerABusBItemCanData(device, f"{self._cmd_syntax}:DATa")
        self._fd = TriggerABusBItemCanFd(device, f"{self._cmd_syntax}:FD")
        self._frametype = TriggerABusBItemCanFrametype(device, f"{self._cmd_syntax}:FRAMEtype")
        self._identifier = TriggerABusBItemCanIdentifier(device, f"{self._cmd_syntax}:IDentifier")
        self._address = TriggerABusBItemCanAddress(device, f"{self._cmd_syntax}:ADDRess")

    @property
    def condition(self) -> TriggerABusBItemCanCondition:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:CONDition`` command.

        Description:
            - This command sets the condition (start of frame, frame type, identifier, matching
              data, end of frame, missing ACK field, bit-stuffing error, form error, any error, CAN
              FD BRS bit, or CAN FD ESI bit) to be used to search on CAN bus data. B<x> is the bus
              number (1-2).

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
            - TRIGger:A:BUS:B<x>:CAN:CONDition {SOF|FRAMEtype|IDentifier|DATA|IDANDDATA|EOF|ACKMISS|ERROR|FORMERRor|ANYERRor|FDBRS|FDESI}
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
            - ``ERROR`` enables triggering on bit stuffing errors.
            - ``FORMERRor`` enables triggering on packet form errors.
            - ``ANYERRor`` enables triggering on any packet error (missing ACK, bit stuffing error,
              or form error).
            - ``FDBRS`` enables triggering on a CAN FD frame's BRS bit.
            - ``FDESI`` enables triggering on a CAN FD frame's ESI bit.
        """  # noqa: E501
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
            - ``.offset``: The ``TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet`` command.
            - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier`` command.
            - ``.size``: The ``TRIGger:A:BUS:B<x>:CAN:DATa:SIZe`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:CAN:DATa:VALue`` command.
        """
        return self._data

    @property
    def fd(self) -> TriggerABusBItemCanFd:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:FD`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:FD?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:FD?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.brsbit``: The ``TRIGger:A:BUS:B<x>:CAN:FD:BRSBIT`` command.
            - ``.esibit``: The ``TRIGger:A:BUS:B<x>:CAN:FD:ESIBIT`` command.
        """
        return self._fd

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


class TriggerABusBItemAudioDataWord(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:AUDio:DATa:WORD`` command.

    Description:
        - This command sets the alignment of the data (left, right or either) to be used to trigger
          on an audio bus signal. The trigger condition must be set to DATA using
          ``TRIGGER:A:BUS:BX:AUDIO:CONDITION``. B<x> is the bus number (1-2).

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:AUDio:DATa:WORD?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:AUDio:DATa:WORD?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:AUDio:DATa:WORD value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:AUDio:DATa:WORD {EITher|LEFt|RIGht}
        - TRIGger:A:BUS:B<x>:AUDio:DATa:WORD?
        ```

    Info:
        - ``EITher`` aligns the trigger data to either left or right.
        - ``LEFt`` aligns the trigger data to the left.
        - ``RIGht`` aligns the trigger data to the right.
    """


class TriggerABusBItemAudioDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:AUDio:DATa:VALue`` command.

    Description:
        - This command sets the lower word value to be used when triggering on an audio bus signal.
          The trigger condition must be set to DATA using ``TRIGGER:A:BUS:BX:AUDIO:CONDITION``. B<x>
          is the bus number (1-2).

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:AUDio:DATa:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:AUDio:DATa:VALue?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:AUDio:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:AUDio:DATa:VALue <String>
        - TRIGger:A:BUS:B<x>:AUDio:DATa:VALue?
        ```

    Info:
        - ``<String>`` specifies the trigger data lower word.
    """


class TriggerABusBItemAudioDataQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier`` command.

    Description:
        - This command sets the qualifier (<, >, =, <=, >=, not =, in range, out of range) to be
          used when triggering on an audio bus signal. The trigger condition must be set to DATA
          using ``TRIGGER:A:BUS:BX:AUDIO:CONDITION``. B<x> is the bus number (1-2).

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier?
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


class TriggerABusBItemAudioDataOffset(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet`` command.

    Description:
        - This command sets the data offset value to be used when triggering on an audio bus signal.
          The trigger condition must be set to DATA using ``TRIGGER:A:BUS:BX:AUDIO:CONDITION``. B<x>
          is the bus number (1-2).

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet <NR1>
        - TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet?
        ```

    Info:
        - ``<NR1>`` is the data offset value.
    """


class TriggerABusBItemAudioDataHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue`` command.

    Description:
        - This command sets the upper word value to be used when triggering on an audio bus signal.
          The trigger condition must be set to DATA using ``TRIGGER:A:BUS:BX:AUDIO:CONDITION``. B<x>
          is the bus number (1-2).

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue <String>
        - TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue?
        ```
    """


class TriggerABusBItemAudioData(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:AUDio:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:AUDio:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:AUDio:DATa?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue`` command.
        - ``.offset``: The ``TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet`` command.
        - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:AUDio:DATa:VALue`` command.
        - ``.word``: The ``TRIGger:A:BUS:B<x>:AUDio:DATa:WORD`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = TriggerABusBItemAudioDataHivalue(device, f"{self._cmd_syntax}:HIVALue")
        self._offset = TriggerABusBItemAudioDataOffset(device, f"{self._cmd_syntax}:OFFSet")
        self._qualifier = TriggerABusBItemAudioDataQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._value = TriggerABusBItemAudioDataValue(device, f"{self._cmd_syntax}:VALue")
        self._word = TriggerABusBItemAudioDataWord(device, f"{self._cmd_syntax}:WORD")

    @property
    def hivalue(self) -> TriggerABusBItemAudioDataHivalue:
        """Return the ``TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue`` command.

        Description:
            - This command sets the upper word value to be used when triggering on an audio bus
              signal. The trigger condition must be set to DATA using
              ``TRIGGER:A:BUS:BX:AUDIO:CONDITION``. B<x> is the bus number (1-2).

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue <String>
            - TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue?
            ```
        """
        return self._hivalue

    @property
    def offset(self) -> TriggerABusBItemAudioDataOffset:
        """Return the ``TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet`` command.

        Description:
            - This command sets the data offset value to be used when triggering on an audio bus
              signal. The trigger condition must be set to DATA using
              ``TRIGGER:A:BUS:BX:AUDIO:CONDITION``. B<x> is the bus number (1-2).

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet <NR1>
            - TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet?
            ```

        Info:
            - ``<NR1>`` is the data offset value.
        """
        return self._offset

    @property
    def qualifier(self) -> TriggerABusBItemAudioDataQualifier:
        """Return the ``TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier`` command.

        Description:
            - This command sets the qualifier (<, >, =, <=, >=, not =, in range, out of range) to be
              used when triggering on an audio bus signal. The trigger condition must be set to DATA
              using ``TRIGGER:A:BUS:BX:AUDIO:CONDITION``. B<x> is the bus number (1-2).

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier?
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
    def value(self) -> TriggerABusBItemAudioDataValue:
        """Return the ``TRIGger:A:BUS:B<x>:AUDio:DATa:VALue`` command.

        Description:
            - This command sets the lower word value to be used when triggering on an audio bus
              signal. The trigger condition must be set to DATA using
              ``TRIGGER:A:BUS:BX:AUDIO:CONDITION``. B<x> is the bus number (1-2).

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:AUDio:DATa:VALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:AUDio:DATa:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:AUDio:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:AUDio:DATa:VALue <String>
            - TRIGger:A:BUS:B<x>:AUDio:DATa:VALue?
            ```

        Info:
            - ``<String>`` specifies the trigger data lower word.
        """
        return self._value

    @property
    def word(self) -> TriggerABusBItemAudioDataWord:
        """Return the ``TRIGger:A:BUS:B<x>:AUDio:DATa:WORD`` command.

        Description:
            - This command sets the alignment of the data (left, right or either) to be used to
              trigger on an audio bus signal. The trigger condition must be set to DATA using
              ``TRIGGER:A:BUS:BX:AUDIO:CONDITION``. B<x> is the bus number (1-2).

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:AUDio:DATa:WORD?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:AUDio:DATa:WORD?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:AUDio:DATa:WORD value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:AUDio:DATa:WORD {EITher|LEFt|RIGht}
            - TRIGger:A:BUS:B<x>:AUDio:DATa:WORD?
            ```

        Info:
            - ``EITher`` aligns the trigger data to either left or right.
            - ``LEFt`` aligns the trigger data to the left.
            - ``RIGht`` aligns the trigger data to the right.
        """
        return self._word


class TriggerABusBItemAudioCondition(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:AUDio:CONDition`` command.

    Description:
        - This command sets the condition (start of frame or matching data) to be used when
          triggering on an audio bus signal. B<x> is the bus number (1-2).

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:AUDio:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:AUDio:CONDition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:AUDio:CONDition value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:AUDio:CONDition {SOF|DATA}
        - TRIGger:A:BUS:B<x>:AUDio:CONDition?
        ```

    Info:
        - ``SOF`` enables triggering on the start of frame.
        - ``DATA`` enables triggering on matching data.
    """


class TriggerABusBItemAudio(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:AUDio`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:AUDio?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:AUDio?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``TRIGger:A:BUS:B<x>:AUDio:CONDition`` command.
        - ``.data``: The ``TRIGger:A:BUS:B<x>:AUDio:DATa`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = TriggerABusBItemAudioCondition(device, f"{self._cmd_syntax}:CONDition")
        self._data = TriggerABusBItemAudioData(device, f"{self._cmd_syntax}:DATa")

    @property
    def condition(self) -> TriggerABusBItemAudioCondition:
        """Return the ``TRIGger:A:BUS:B<x>:AUDio:CONDition`` command.

        Description:
            - This command sets the condition (start of frame or matching data) to be used when
              triggering on an audio bus signal. B<x> is the bus number (1-2).

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:AUDio:CONDition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:AUDio:CONDition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:AUDio:CONDition value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:AUDio:CONDition {SOF|DATA}
            - TRIGger:A:BUS:B<x>:AUDio:CONDition?
            ```

        Info:
            - ``SOF`` enables triggering on the start of frame.
            - ``DATA`` enables triggering on matching data.
        """
        return self._condition

    @property
    def data(self) -> TriggerABusBItemAudioData:
        """Return the ``TRIGger:A:BUS:B<x>:AUDio:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:AUDio:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:AUDio:DATa?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:AUDio:DATa:HIVALue`` command.
            - ``.offset``: The ``TRIGger:A:BUS:B<x>:AUDio:DATa:OFFSet`` command.
            - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:AUDio:DATa:QUALifier`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:AUDio:DATa:VALue`` command.
            - ``.word``: The ``TRIGger:A:BUS:B<x>:AUDio:DATa:WORD`` command.
        """
        return self._data


class TriggerABusBItemArinc429aSsm(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ARINC429A:SSM`` command.

    Description:
        - This command specifies the value for the SSM field to be used when triggering on the
          ARINC429 bus data field(s). The trigger condition must be set to DATA or LABELANDDATA
          (using ``TRIGGER:A:BUS:BX:ARINC429A:CONDITION``). The default is all X's (don't care).
          B<x> is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ARINC429A:SSM?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:ARINC429A:SSM?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ARINC429A:SSM value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ARINC429A:SSM <QString>
        - TRIGger:A:BUS:B<x>:ARINC429A:SSM?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemArinc429aSdi(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ARINC429A:SDI`` command.

    Description:
        - This command specifies the value for the SDI field to be used when triggering on the
          ARINC429 bus data field(s). The trigger condition must be set to DATA or LABELANDDATA
          (using ``TRIGGER:A:BUS:BX:ARINC429A:CONDITION``). The default is all X's (don't care).
          B<x> is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ARINC429A:SDI?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:ARINC429A:SDI?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ARINC429A:SDI value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ARINC429A:SDI <QString>
        - TRIGger:A:BUS:B<x>:ARINC429A:SDI?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemArinc429aLabelValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue`` command.

    Description:
        - This command specifies the low value to be used when triggering on the ARINC429 bus label
          field. The trigger condition must be set to LABel or LABELANDDATA (using
          ``TRIGGER:A:BUS:BX:ARINC429A:CONDITION``). The default is all X's (don't care). B<x> is
          the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue <QString>
        - TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemArinc429aLabelQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier`` command.

    Description:
        - This command specifies the qualifier to be used when triggering on the ARINC429 label
          field. The trigger condition must be set to LABel or LABELANDDATA. The default qualifier
          is 'Equal to'. B<x> is the bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier {LESSthan|MOREthan|Equal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier?
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


class TriggerABusBItemArinc429aLabelHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue`` command.

    Description:
        - When the trigger condition is set to LABel, and the qualifier is set to either INrange or
          OUTrange, this command specifies the upper value of the range for a trigger on the label
          field. (Use the command ``TRIGGER:A:BUS:BX:ARINC429A:LABEL:VALUE`` to specify the lower
          value of the range). The default is all X's (don't care). B<x> is the bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue <QString>
        - TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemArinc429aLabel(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ARINC429A:LABel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ARINC429A:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:ARINC429A:LABel?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue`` command.
        - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = TriggerABusBItemArinc429aLabelHivalue(device, f"{self._cmd_syntax}:HIVALue")
        self._qualifier = TriggerABusBItemArinc429aLabelQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._value = TriggerABusBItemArinc429aLabelValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def hivalue(self) -> TriggerABusBItemArinc429aLabelHivalue:
        """Return the ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue`` command.

        Description:
            - When the trigger condition is set to LABel, and the qualifier is set to either INrange
              or OUTrange, this command specifies the upper value of the range for a trigger on the
              label field. (Use the command ``TRIGGER:A:BUS:BX:ARINC429A:LABEL:VALUE`` to specify
              the lower value of the range). The default is all X's (don't care). B<x> is the bus
              number.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue <QString>
            - TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue?
            ```
        """
        return self._hivalue

    @property
    def qualifier(self) -> TriggerABusBItemArinc429aLabelQualifier:
        """Return the ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier`` command.

        Description:
            - This command specifies the qualifier to be used when triggering on the ARINC429 label
              field. The trigger condition must be set to LABel or LABELANDDATA. The default
              qualifier is 'Equal to'. B<x> is the bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier {LESSthan|MOREthan|Equal|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier?
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
    def value(self) -> TriggerABusBItemArinc429aLabelValue:
        """Return the ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue`` command.

        Description:
            - This command specifies the low value to be used when triggering on the ARINC429 bus
              label field. The trigger condition must be set to LABel or LABELANDDATA (using
              ``TRIGGER:A:BUS:BX:ARINC429A:CONDITION``). The default is all X's (don't care). B<x>
              is the bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue <QString>
            - TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue?
            ```
        """
        return self._value


class TriggerABusBItemArinc429aErrtype(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE`` command.

    Description:
        - This command specifies the error type when triggering on an ARINC429 bus signal. The
          trigger condition needs to be set to ERROR (using
          ``TRIGGER:A:BUS:BX:ARINC429A:CONDITION``). B<x> is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE {ANY|GAP|WORD|PARity}
        - TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE?
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


class TriggerABusBItemArinc429aCondition(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ARINC429A:CONDition`` command.

    Description:
        - This command sets the condition (word start, label, matching data, word end, or error) to
          be used to trigger on CAN bus data. B<x> is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ARINC429A:CONDition?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ARINC429A:CONDition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:ARINC429A:CONDition value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:ARINC429A:CONDition {STARt|END|LABel|DATA|LABELANDDATA|ERRor}
        - TRIGger:A:BUS:B<x>:ARINC429A:CONDition?
        ```

    Info:
        - ``STARt`` enables triggering on the first bit of a word.
        - ``END`` enables triggering on the 32nd bit of a word.
        - ``LABel`` enables trigger on a matching label.
        - ``DATA`` enables triggering on matching packet data field(s).
        - ``LABELANDDATA`` enables triggering on matching label and matching packet data field(s).
        - ``ERROR`` enables triggering on a specified packet error.
    """


class TriggerABusBItemArinc429a(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:ARINC429A`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ARINC429A?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:ARINC429A?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``TRIGger:A:BUS:B<x>:ARINC429A:CONDition`` command.
        - ``.errtype``: The ``TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE`` command.
        - ``.label``: The ``TRIGger:A:BUS:B<x>:ARINC429A:LABel`` command tree.
        - ``.sdi``: The ``TRIGger:A:BUS:B<x>:ARINC429A:SDI`` command.
        - ``.ssm``: The ``TRIGger:A:BUS:B<x>:ARINC429A:SSM`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = TriggerABusBItemArinc429aCondition(
            device, f"{self._cmd_syntax}:CONDition"
        )
        self._errtype = TriggerABusBItemArinc429aErrtype(device, f"{self._cmd_syntax}:ERRTYPE")
        self._label = TriggerABusBItemArinc429aLabel(device, f"{self._cmd_syntax}:LABel")
        self._sdi = TriggerABusBItemArinc429aSdi(device, f"{self._cmd_syntax}:SDI")
        self._ssm = TriggerABusBItemArinc429aSsm(device, f"{self._cmd_syntax}:SSM")

    @property
    def condition(self) -> TriggerABusBItemArinc429aCondition:
        """Return the ``TRIGger:A:BUS:B<x>:ARINC429A:CONDition`` command.

        Description:
            - This command sets the condition (word start, label, matching data, word end, or error)
              to be used to trigger on CAN bus data. B<x> is the bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:ARINC429A:CONDition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ARINC429A:CONDition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ARINC429A:CONDition value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ARINC429A:CONDition {STARt|END|LABel|DATA|LABELANDDATA|ERRor}
            - TRIGger:A:BUS:B<x>:ARINC429A:CONDition?
            ```

        Info:
            - ``STARt`` enables triggering on the first bit of a word.
            - ``END`` enables triggering on the 32nd bit of a word.
            - ``LABel`` enables trigger on a matching label.
            - ``DATA`` enables triggering on matching packet data field(s).
            - ``LABELANDDATA`` enables triggering on matching label and matching packet data
              field(s).
            - ``ERROR`` enables triggering on a specified packet error.
        """
        return self._condition

    @property
    def errtype(self) -> TriggerABusBItemArinc429aErrtype:
        """Return the ``TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE`` command.

        Description:
            - This command specifies the error type when triggering on an ARINC429 bus signal. The
              trigger condition needs to be set to ERROR (using
              ``TRIGGER:A:BUS:BX:ARINC429A:CONDITION``). B<x> is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE {ANY|GAP|WORD|PARity}
            - TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE?
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
    def label(self) -> TriggerABusBItemArinc429aLabel:
        """Return the ``TRIGger:A:BUS:B<x>:ARINC429A:LABel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ARINC429A:LABel?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ARINC429A:LABel?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:HIVALue`` command.
            - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:QUALifier`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:ARINC429A:LABel:VALue`` command.
        """
        return self._label

    @property
    def sdi(self) -> TriggerABusBItemArinc429aSdi:
        """Return the ``TRIGger:A:BUS:B<x>:ARINC429A:SDI`` command.

        Description:
            - This command specifies the value for the SDI field to be used when triggering on the
              ARINC429 bus data field(s). The trigger condition must be set to DATA or LABELANDDATA
              (using ``TRIGGER:A:BUS:BX:ARINC429A:CONDITION``). The default is all X's (don't care).
              B<x> is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ARINC429A:SDI?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ARINC429A:SDI?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ARINC429A:SDI value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ARINC429A:SDI <QString>
            - TRIGger:A:BUS:B<x>:ARINC429A:SDI?
            ```
        """
        return self._sdi

    @property
    def ssm(self) -> TriggerABusBItemArinc429aSsm:
        """Return the ``TRIGger:A:BUS:B<x>:ARINC429A:SSM`` command.

        Description:
            - This command specifies the value for the SSM field to be used when triggering on the
              ARINC429 bus data field(s). The trigger condition must be set to DATA or LABELANDDATA
              (using ``TRIGGER:A:BUS:BX:ARINC429A:CONDITION``). The default is all X's (don't care).
              B<x> is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ARINC429A:SSM?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ARINC429A:SSM?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:ARINC429A:SSM value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:ARINC429A:SSM <QString>
            - TRIGger:A:BUS:B<x>:ARINC429A:SSM?
            ```
        """
        return self._ssm


#  pylint: disable=too-many-instance-attributes
class TriggerABusBItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.arinc429a``: The ``TRIGger:A:BUS:B<x>:ARINC429A`` command tree.
        - ``.audio``: The ``TRIGger:A:BUS:B<x>:AUDio`` command tree.
        - ``.can``: The ``TRIGger:A:BUS:B<x>:CAN`` command tree.
        - ``.ethernet``: The ``TRIGger:A:BUS:B<x>:ETHERnet`` command tree.
        - ``.flexray``: The ``TRIGger:A:BUS:B<x>:FLEXray`` command tree.
        - ``.i2c``: The ``TRIGger:A:BUS:B<x>:I2C`` command tree.
        - ``.lin``: The ``TRIGger:A:BUS:B<x>:LIN`` command tree.
        - ``.mil1553b``: The ``TRIGger:A:BUS:B<x>:MIL1553B`` command tree.
        - ``.parallel``: The ``TRIGger:A:BUS:B<x>:PARallel`` command tree.
        - ``.rs232c``: The ``TRIGger:A:BUS:B<x>:RS232C`` command tree.
        - ``.spi``: The ``TRIGger:A:BUS:B<x>:SPI`` command tree.
        - ``.usb``: The ``TRIGger:A:BUS:B<x>:USB`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._arinc429a = TriggerABusBItemArinc429a(device, f"{self._cmd_syntax}:ARINC429A")
        self._audio = TriggerABusBItemAudio(device, f"{self._cmd_syntax}:AUDio")
        self._can = TriggerABusBItemCan(device, f"{self._cmd_syntax}:CAN")
        self._ethernet = TriggerABusBItemEthernet(device, f"{self._cmd_syntax}:ETHERnet")
        self._flexray = TriggerABusBItemFlexray(device, f"{self._cmd_syntax}:FLEXray")
        self._i2c = TriggerABusBItemI2c(device, f"{self._cmd_syntax}:I2C")
        self._lin = TriggerABusBItemLin(device, f"{self._cmd_syntax}:LIN")
        self._mil1553b = TriggerABusBItemMil1553b(device, f"{self._cmd_syntax}:MIL1553B")
        self._parallel = TriggerABusBItemParallel(device, f"{self._cmd_syntax}:PARallel")
        self._rs232c = TriggerABusBItemRs232c(device, f"{self._cmd_syntax}:RS232C")
        self._spi = TriggerABusBItemSpi(device, f"{self._cmd_syntax}:SPI")
        self._usb = TriggerABusBItemUsb(device, f"{self._cmd_syntax}:USB")

    @property
    def arinc429a(self) -> TriggerABusBItemArinc429a:
        """Return the ``TRIGger:A:BUS:B<x>:ARINC429A`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ARINC429A?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:ARINC429A?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``TRIGger:A:BUS:B<x>:ARINC429A:CONDition`` command.
            - ``.errtype``: The ``TRIGger:A:BUS:B<x>:ARINC429A:ERRTYPE`` command.
            - ``.label``: The ``TRIGger:A:BUS:B<x>:ARINC429A:LABel`` command tree.
            - ``.sdi``: The ``TRIGger:A:BUS:B<x>:ARINC429A:SDI`` command.
            - ``.ssm``: The ``TRIGger:A:BUS:B<x>:ARINC429A:SSM`` command.
        """
        return self._arinc429a

    @property
    def audio(self) -> TriggerABusBItemAudio:
        """Return the ``TRIGger:A:BUS:B<x>:AUDio`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:AUDio?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:AUDio?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``TRIGger:A:BUS:B<x>:AUDio:CONDition`` command.
            - ``.data``: The ``TRIGger:A:BUS:B<x>:AUDio:DATa`` command tree.
        """
        return self._audio

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
            - ``.fd``: The ``TRIGger:A:BUS:B<x>:CAN:FD`` command tree.
            - ``.frametype``: The ``TRIGger:A:BUS:B<x>:CAN:FRAMEtype`` command.
            - ``.identifier``: The ``TRIGger:A:BUS:B<x>:CAN:IDentifier`` command tree.
            - ``.address``: The ``TRIGger:A:BUS:B<x>:CAN:ADDRess`` command tree.
        """
        return self._can

    @property
    def ethernet(self) -> TriggerABusBItemEthernet:
        """Return the ``TRIGger:A:BUS:B<x>:ETHERnet`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:ETHERnet?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``TRIGger:A:BUS:B<x>:ETHERnet:CONDition`` command.
            - ``.data``: The ``TRIGger:A:BUS:B<x>:ETHERnet:DATa`` command tree.
            - ``.frametype``: The ``TRIGger:A:BUS:B<x>:ETHERnet:FRAMETYPe`` command.
            - ``.ipheader``: The ``TRIGger:A:BUS:B<x>:ETHERnet:IPHeader`` command tree.
            - ``.mac``: The ``TRIGger:A:BUS:B<x>:ETHERnet:MAC`` command tree.
            - ``.qtag``: The ``TRIGger:A:BUS:B<x>:ETHERnet:QTAG`` command tree.
            - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:ETHERnet:QUALifier`` command.
            - ``.tcpheader``: The ``TRIGger:A:BUS:B<x>:ETHERnet:TCPHeader`` command tree.
        """
        return self._ethernet

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
    def mil1553b(self) -> TriggerABusBItemMil1553b:
        """Return the ``TRIGger:A:BUS:B<x>:MIL1553B`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:MIL1553B?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.command``: The ``TRIGger:A:BUS:B<x>:MIL1553B:COMMAND`` command tree.
            - ``.condition``: The ``TRIGger:A:BUS:B<x>:MIL1553B:CONDition`` command.
            - ``.data``: The ``TRIGger:A:BUS:B<x>:MIL1553B:DATa`` command tree.
            - ``.errtype``: The ``TRIGger:A:BUS:B<x>:MIL1553B:ERRTYPE`` command.
            - ``.status``: The ``TRIGger:A:BUS:B<x>:MIL1553B:STATus`` command tree.
            - ``.time``: The ``TRIGger:A:BUS:B<x>:MIL1553B:TIMe`` command tree.
        """
        return self._mil1553b

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

    @property
    def usb(self) -> TriggerABusBItemUsb:
        """Return the ``TRIGger:A:BUS:B<x>:USB`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:USB?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:USB?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.address``: The ``TRIGger:A:BUS:B<x>:USB:ADDRess`` command tree.
            - ``.condition``: The ``TRIGger:A:BUS:B<x>:USB:CONDition`` command.
            - ``.data``: The ``TRIGger:A:BUS:B<x>:USB:DATa`` command tree.
            - ``.endpoint``: The ``TRIGger:A:BUS:B<x>:USB:ENDPoint`` command tree.
            - ``.errtype``: The ``TRIGger:A:BUS:B<x>:USB:ERRTYPE`` command.
            - ``.handshaketype``: The ``TRIGger:A:BUS:B<x>:USB:HANDSHAKEType`` command.
            - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:USB:QUALifier`` command.
            - ``.sofframenumber``: The ``TRIGger:A:BUS:B<x>:USB:SOFFRAMENUMber`` command.
            - ``.specialtype``: The ``TRIGger:A:BUS:B<x>:USB:SPECIALType`` command.
            - ``.split``: The ``TRIGger:A:BUS:B<x>:USB:SPLit`` command tree.
            - ``.tokentype``: The ``TRIGger:A:BUS:B<x>:USB:TOKENType`` command.
        """
        return self._usb


class TriggerABus(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS`` command.

    Description:
        - This command specifies the bus type to trigger on. It supports CAN, I 2 C, SPI, RS-232,
          Ethernet, MIL-STD-1553, LIN, USB, audio, FlexRay buses (with the appropriate application
          module installed) as well as parallel signals (with option 3-MSO only.). There are two
          buses, B1-B2. Each bus can be independently set to one of the serial trigger types.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:BUS value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS {I2C|SPI|CAN|RS232C|PARallel|USB|LIN|FLEXRay|AUDio|ETHERnet|MIL1553B}
        - TRIGger:A:BUS?
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
            - ``.arinc429a``: The ``TRIGger:A:BUS:B<x>:ARINC429A`` command tree.
            - ``.audio``: The ``TRIGger:A:BUS:B<x>:AUDio`` command tree.
            - ``.can``: The ``TRIGger:A:BUS:B<x>:CAN`` command tree.
            - ``.ethernet``: The ``TRIGger:A:BUS:B<x>:ETHERnet`` command tree.
            - ``.flexray``: The ``TRIGger:A:BUS:B<x>:FLEXray`` command tree.
            - ``.i2c``: The ``TRIGger:A:BUS:B<x>:I2C`` command tree.
            - ``.lin``: The ``TRIGger:A:BUS:B<x>:LIN`` command tree.
            - ``.mil1553b``: The ``TRIGger:A:BUS:B<x>:MIL1553B`` command tree.
            - ``.parallel``: The ``TRIGger:A:BUS:B<x>:PARallel`` command tree.
            - ``.rs232c``: The ``TRIGger:A:BUS:B<x>:RS232C`` command tree.
            - ``.spi``: The ``TRIGger:A:BUS:B<x>:SPI`` command tree.
            - ``.usb``: The ``TRIGger:A:BUS:B<x>:USB`` command tree.
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


class TriggerABandwidthRfLow(SCPICmdRead):
    """The ``TRIGger:A:BANDWidth:RF:LOW`` command.

    Description:
        - Returns the low end of the power level trigger bandwidth range as an NR3 value in hertz.
          This is the value that is displayed in the user interface when the trigger source is RF.
          This command requires the MDO4TRIG advanced trigger feature to be enabled.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BANDWidth:RF:LOW?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BANDWidth:RF:LOW?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TRIGger:A:BANDWidth:RF:LOW?
        ```
    """


class TriggerABandwidthRfHigh(SCPICmdRead):
    """The ``TRIGger:A:BANDWidth:RF:HIGH`` command.

    Description:
        - Returns the high end of the power level trigger bandwidth range as an NR3 value in hertz.
          This is the value that is displayed in the user interface when the trigger source is RF.
          This command requires the MDO4TRIG advanced trigger feature to be enabled.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BANDWidth:RF:HIGH?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BANDWidth:RF:HIGH?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TRIGger:A:BANDWidth:RF:HIGH?
        ```
    """


class TriggerABandwidthRf(SCPICmdRead):
    """The ``TRIGger:A:BANDWidth:RF`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BANDWidth:RF?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BANDWidth:RF?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.high``: The ``TRIGger:A:BANDWidth:RF:HIGH`` command.
        - ``.low``: The ``TRIGger:A:BANDWidth:RF:LOW`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._high = TriggerABandwidthRfHigh(device, f"{self._cmd_syntax}:HIGH")
        self._low = TriggerABandwidthRfLow(device, f"{self._cmd_syntax}:LOW")

    @property
    def high(self) -> TriggerABandwidthRfHigh:
        """Return the ``TRIGger:A:BANDWidth:RF:HIGH`` command.

        Description:
            - Returns the high end of the power level trigger bandwidth range as an NR3 value in
              hertz. This is the value that is displayed in the user interface when the trigger
              source is RF. This command requires the MDO4TRIG advanced trigger feature to be
              enabled.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BANDWidth:RF:HIGH?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BANDWidth:RF:HIGH?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TRIGger:A:BANDWidth:RF:HIGH?
            ```
        """
        return self._high

    @property
    def low(self) -> TriggerABandwidthRfLow:
        """Return the ``TRIGger:A:BANDWidth:RF:LOW`` command.

        Description:
            - Returns the low end of the power level trigger bandwidth range as an NR3 value in
              hertz. This is the value that is displayed in the user interface when the trigger
              source is RF. This command requires the MDO4TRIG advanced trigger feature to be
              enabled.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BANDWidth:RF:LOW?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BANDWidth:RF:LOW?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TRIGger:A:BANDWidth:RF:LOW?
            ```
        """
        return self._low


class TriggerABandwidth(SCPICmdRead):
    """The ``TRIGger:A:BANDWidth`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BANDWidth?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BANDWidth?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.rf``: The ``TRIGger:A:BANDWidth:RF`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._rf = TriggerABandwidthRf(device, f"{self._cmd_syntax}:RF")

    @property
    def rf(self) -> TriggerABandwidthRf:
        """Return the ``TRIGger:A:BANDWidth:RF`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BANDWidth:RF?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BANDWidth:RF?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.high``: The ``TRIGger:A:BANDWidth:RF:HIGH`` command.
            - ``.low``: The ``TRIGger:A:BANDWidth:RF:LOW`` command.
        """
        return self._rf


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
        - ``.bandwidth``: The ``TRIGger:A:BANDWidth`` command tree.
        - ``.bus``: The ``TRIGger:A:BUS`` command.
        - ``.edge``: The ``TRIGger:A:EDGE`` command.
        - ``.holdoff``: The ``TRIGger:A:HOLDoff`` command.
        - ``.level``: The ``TRIGger:A:LEVel`` command tree.
        - ``.logic``: The ``TRIGger:A:LOGIc`` command.
        - ``.lowerthreshold``: The ``TRIGger:A:LOWerthreshold`` command tree.
        - ``.mode``: The ``TRIGger:A:MODe`` command.
        - ``.pulsewidth``: The ``TRIGger:A:PULSEWidth`` command tree.
        - ``.pulse``: The ``TRIGger:A:PULse`` command tree.
        - ``.runt``: The ``TRIGger:A:RUNT`` command.
        - ``.sethold``: The ``TRIGger:A:SETHold`` command.
        - ``.timeout``: The ``TRIGger:A:TIMEOut`` command tree.
        - ``.type``: The ``TRIGger:A:TYPe`` command.
        - ``.upperthreshold``: The ``TRIGger:A:UPPerthreshold`` command tree.
        - ``.video``: The ``TRIGger:A:VIDeo`` command.
        - ``.transition``: The ``TRIGger:A:TRANsition`` command.
        - ``.risefall``: The ``TRIGger:A:RISEFall`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bandwidth = TriggerABandwidth(device, f"{self._cmd_syntax}:BANDWidth")
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
        self._timeout = TriggerATimeout(device, f"{self._cmd_syntax}:TIMEOut")
        self._type = TriggerAType(device, f"{self._cmd_syntax}:TYPe")
        self._upperthreshold = TriggerAUpperthreshold(device, f"{self._cmd_syntax}:UPPerthreshold")
        self._video = TriggerAVideo(device, f"{self._cmd_syntax}:VIDeo")
        self._transition = TriggerATransition(device, f"{self._cmd_syntax}:TRANsition")
        self._risefall = TriggerARisefall(device, f"{self._cmd_syntax}:RISEFall")

    @property
    def bandwidth(self) -> TriggerABandwidth:
        """Return the ``TRIGger:A:BANDWidth`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BANDWidth?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BANDWidth?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.rf``: The ``TRIGger:A:BANDWidth:RF`` command tree.
        """
        return self._bandwidth

    @property
    def bus(self) -> TriggerABus:
        """Return the ``TRIGger:A:BUS`` command.

        Description:
            - This command specifies the bus type to trigger on. It supports CAN, I 2 C, SPI,
              RS-232, Ethernet, MIL-STD-1553, LIN, USB, audio, FlexRay buses (with the appropriate
              application module installed) as well as parallel signals (with option 3-MSO only.).
              There are two buses, B1-B2. Each bus can be independently set to one of the serial
              trigger types.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:BUS value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS {I2C|SPI|CAN|RS232C|PARallel|USB|LIN|FLEXRay|AUDio|ETHERnet|MIL1553B}
            - TRIGger:A:BUS?
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
        """Return the ``TRIGger:A:LEVel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LEVel?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LEVel?`` query and raise
              an AssertionError if the returned value does not match ``value``.

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
            - ``.d``: The ``TRIGger:A:LOWerthreshold:D<x>`` command.
            - ``.rf``: The ``TRIGger:A:LOWerthreshold:RF`` command.
            - ``.aux``: The ``TRIGger:A:LOWerthreshold:AUX`` command.
            - ``.ext``: The ``TRIGger:A:LOWerthreshold:EXT`` command.
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
        """Return the ``TRIGger:A:PULSEWidth`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.highlimit``: The ``TRIGger:A:PULSEWidth:HIGHLimit`` command.
            - ``.lowlimit``: The ``TRIGger:A:PULSEWidth:LOWLimit`` command.
            - ``.polarity``: The ``TRIGger:A:PULSEWidth:POLarity`` command.
            - ``.source``: The ``TRIGger:A:PULSEWidth:SOUrce`` command.
            - ``.when``: The ``TRIGger:A:PULSEWidth:WHEn`` command.
            - ``.width``: The ``TRIGger:A:PULSEWidth:WIDth`` command.
        """
        return self._pulsewidth

    @property
    def pulse(self) -> TriggerAPulse:
        """Return the ``TRIGger:A:PULse`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:PULse?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULse?`` query and raise
              an AssertionError if the returned value does not match ``value``.

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
    def timeout(self) -> TriggerATimeout:
        """Return the ``TRIGger:A:TIMEOut`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:TIMEOut?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:TIMEOut?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``TRIGger:A:TIMEOut:POLarity`` command.
            - ``.source``: The ``TRIGger:A:TIMEOut:SOUrce`` command.
            - ``.time``: The ``TRIGger:A:TIMEOut:TIMe`` command.
        """
        return self._timeout

    @property
    def type(self) -> TriggerAType:
        """Return the ``TRIGger:A:TYPe`` command.

        Description:
            - This command sets the type of A trigger (either edge, logic, pulse, bus or video). If
              you set the trigger type to LOGIc, you also need to set the logic trigger class (logic
              or setup/hold) using the command ``TRIGGER:A:LOGIC:CLASS``. If you set the trigger
              type to PULSe, you also need to set the pulse trigger class (either runt, width,
              transition or timeout), using the command ``TRIGGER:A:PULSE:CLASS``. If you set the
              trigger type to BUS, you also need to set the bus type (CAN, I 2 C, SPI, RS-232,
              Ethernet, MIL-STD-1553, LIN, USB, audio, FlexRay, or parallel) using the command
              ``TRIGGER:A:BUS``.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:TYPe?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:TYPe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:TYPe {EDGe|LOGIc|PULSe|BUS|VIDeo}
            - TRIGger:A:TYPe?
            ```

        Info:
            - ``EDGe`` is the default trigger. A trigger event occurs when a signal passes through a
              specified voltage level in a specified direction and is controlled by the
              ``TRIGGER:A:EDGE`` commands.
            - ``LOGIc`` specifies that a trigger occurs when specified conditions are met and is
              controlled by the ``TRIGGER:A:LOGIC`` commands. This trigger type is equivalent to the
              logic and setup/hold triggers found in the user interface. Use
              ``TRIGGER:A:LOGIC:CLASS`` to further select the logic trigger class (either LOGIC or
              SETHOLD).
            - ``PULSe`` specifies that a trigger occurs when a specified pulse is found. Use
              ``TRIGGER:A:PULSE:CLASS`` to further select the pulse trigger class (either runt,
              width, transition or timeout).
            - ``BUS`` specifies that a trigger occurs when a bus signal is found. Supports CAN, I2C,
              SPI, RS-232, Ethernet, MIL-STD-1553, LIN, USB, audio, FlexRay buses (with the
              appropriate application module installed) as well as parallel buses. Requires the
              installation of option 3-MSO. Use ``TRIGGER:A:BUS`` to set the bus type.
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
            - ``.rf``: The ``TRIGger:A:UPPerthreshold:RF`` command.
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
            - ``.custom``: The ``TRIGger:A:VIDeo:CUSTom`` command tree.
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
        - ``.b``: The ``TRIGger:B`` command.
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
            - ``.bandwidth``: The ``TRIGger:A:BANDWidth`` command tree.
            - ``.bus``: The ``TRIGger:A:BUS`` command.
            - ``.edge``: The ``TRIGger:A:EDGE`` command.
            - ``.holdoff``: The ``TRIGger:A:HOLDoff`` command.
            - ``.level``: The ``TRIGger:A:LEVel`` command tree.
            - ``.logic``: The ``TRIGger:A:LOGIc`` command.
            - ``.lowerthreshold``: The ``TRIGger:A:LOWerthreshold`` command tree.
            - ``.mode``: The ``TRIGger:A:MODe`` command.
            - ``.pulsewidth``: The ``TRIGger:A:PULSEWidth`` command tree.
            - ``.pulse``: The ``TRIGger:A:PULse`` command tree.
            - ``.runt``: The ``TRIGger:A:RUNT`` command.
            - ``.sethold``: The ``TRIGger:A:SETHold`` command.
            - ``.timeout``: The ``TRIGger:A:TIMEOut`` command tree.
            - ``.type``: The ``TRIGger:A:TYPe`` command.
            - ``.upperthreshold``: The ``TRIGger:A:UPPerthreshold`` command tree.
            - ``.video``: The ``TRIGger:A:VIDeo`` command.
            - ``.transition``: The ``TRIGger:A:TRANsition`` command.
            - ``.risefall``: The ``TRIGger:A:RISEFall`` command.
        """
        return self._a

    @property
    def b(self) -> TriggerB:
        """Return the ``TRIGger:B`` command.

        Description:
            - Sets the B trigger level to 50% of minimum and maximum. The query form of this command
              returns the B trigger parameters. This command is similar to selecting B Event
              (Delayed) Trigger Setup from the Trigger menu and then viewing the current setups.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:B?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:B?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:B value`` command.

        SCPI Syntax:
            ```
            - TRIGger:B SETLevel
            - TRIGger:B?
            ```

        Info:
            - ``SETLevel`` sets the B trigger level to 50% of MIN and MAX.

        Sub-properties:
            - ``.by``: The ``TRIGger:B:BY`` command.
            - ``.edge``: The ``TRIGger:B:EDGE`` command.
            - ``.events``: The ``TRIGger:B:EVENTS`` command.
            - ``.level``: The ``TRIGger:B:LEVel`` command.
            - ``.lowerthreshold``: The ``TRIGger:B:LOWerthreshold`` command tree.
            - ``.state``: The ``TRIGger:B:STATE`` command.
            - ``.time``: The ``TRIGger:B:TIMe`` command.
            - ``.type``: The ``TRIGger:B:TYPe`` command.
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
