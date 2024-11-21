# pylint: disable=line-too-long
"""The bus commands module.

These commands are used in the following models:
TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - BUS:ADDNew <QString>
    - BUS:B<x>:ARINC429A:BITRate {LOW|HI|CUSTom}
    - BUS:B<x>:ARINC429A:BITRate:CUSTom <NR1>
    - BUS:B<x>:ARINC429A:BITRate:CUSTom?
    - BUS:B<x>:ARINC429A:BITRate?
    - BUS:B<x>:ARINC429A:DATAFORmat {DATA|SDIDATA|SDIDATASSM}
    - BUS:B<x>:ARINC429A:DATAFORmat?
    - BUS:B<x>:ARINC429A:POLARITY {NORMal|INVERTed}
    - BUS:B<x>:ARINC429A:POLARITY?
    - BUS:B<x>:ARINC429A:SOUrce {S<x>_Ch<x>|CH<x>|Math<x>|REF<x>}
    - BUS:B<x>:ARINC429A:SOUrce?
    - BUS:B<x>:ARINC429A:THRESHold <NR3>
    - BUS:B<x>:ARINC429A:THRESHold?
    - BUS:B<x>:AUDio:BITDelay <NR1>
    - BUS:B<x>:AUDio:BITDelay?
    - BUS:B<x>:AUDio:BITOrder {MSB|LSB}
    - BUS:B<x>:AUDio:BITOrder?
    - BUS:B<x>:AUDio:CLOCk:POLarity {FALL|RISE}
    - BUS:B<x>:AUDio:CLOCk:POLarity?
    - BUS:B<x>:AUDio:CLOCk:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|Math<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:AUDio:CLOCk:SOUrce?
    - BUS:B<x>:AUDio:CLOCk:THReshold <NR3>
    - BUS:B<x>:AUDio:CLOCk:THReshold?
    - BUS:B<x>:AUDio:DATa:POLarity {HIGH|LOW}
    - BUS:B<x>:AUDio:DATa:POLarity?
    - BUS:B<x>:AUDio:DATa:SIZe <NR1>
    - BUS:B<x>:AUDio:DATa:SIZe?
    - BUS:B<x>:AUDio:DATa:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:AUDio:DATa:SOUrce?
    - BUS:B<x>:AUDio:DATa:THReshold <NR3>
    - BUS:B<x>:AUDio:DATa:THReshold?
    - BUS:B<x>:AUDio:DATa:WORDSize <NR1>
    - BUS:B<x>:AUDio:DATa:WORDSize?
    - BUS:B<x>:AUDio:FRAME:CLOCKBITSPERCHANNEL <NR1>
    - BUS:B<x>:AUDio:FRAME:CLOCKBITSPERCHANNEL?
    - BUS:B<x>:AUDio:FRAME:SIZe <NR1>
    - BUS:B<x>:AUDio:FRAME:SIZe?
    - BUS:B<x>:AUDio:TYPe {I2S|LJ|RJ|TDM}
    - BUS:B<x>:AUDio:TYPe?
    - BUS:B<x>:AUDio:WORDSel:POLarity {NORMal|INVERTed}
    - BUS:B<x>:AUDio:WORDSel:POLarity?
    - BUS:B<x>:AUDio:WORDSel:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:AUDio:WORDSel:SOUrce?
    - BUS:B<x>:AUDio:WORDSel:THReshold <NR3>
    - BUS:B<x>:AUDio:WORDSel:THReshold?
    - BUS:B<x>:AUTOETHERnet:DATAMINUSTHRESHOLD <NR3>
    - BUS:B<x>:AUTOETHERnet:DATAMINUSTHRESHOLD?
    - BUS:B<x>:AUTOETHERnet:DATAPLUSTHRESHold <NR3>
    - BUS:B<x>:AUTOETHERnet:DATAPLUSTHRESHold?
    - BUS:B<x>:AUTOETHERnet:LOWDATAMINus <NR3>
    - BUS:B<x>:AUTOETHERnet:LOWDATAMINus?
    - BUS:B<x>:AUTOETHERnet:LOWDATAPLUS <NR3>
    - BUS:B<x>:AUTOETHERnet:LOWDATAPLUS?
    - BUS:B<x>:AUTOETHERnet:LOWTHRESHold <NR3>
    - BUS:B<x>:AUTOETHERnet:LOWTHRESHold?
    - BUS:B<x>:AUTOETHERnet:SIGNALTYpe {SINGLE|DIFF}
    - BUS:B<x>:AUTOETHERnet:SIGNALTYpe?
    - BUS:B<x>:AUTOETHERnet:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
    - BUS:B<x>:AUTOETHERnet:SOUrce:DMINus {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
    - BUS:B<x>:AUTOETHERnet:SOUrce:DMINus?
    - BUS:B<x>:AUTOETHERnet:SOUrce:DPLUs {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
    - BUS:B<x>:AUTOETHERnet:SOUrce:DPLUs?
    - BUS:B<x>:AUTOETHERnet:SOUrce?
    - BUS:B<x>:AUTOETHERnet:THRESHold <NR3>
    - BUS:B<x>:AUTOETHERnet:THRESHold?
    - BUS:B<x>:AUTOETHERnet:TYPe {HUNDREDBASET1}
    - BUS:B<x>:AUTOETHERnet:TYPe?
    - BUS:B<x>:CAN:BITRate {RATE10K|RATE100K|RATE1M|RATE125K|RATE153K|RATE20K|RATE25K|RATE250K|RATE31K|RATE33K|RATE400K|RATE50K|RATE500K|RATE62K|RATE68K|RATE800K|RATE83K|RATE92K|CUSTom}
    - BUS:B<x>:CAN:BITRate:VALue <NR3>
    - BUS:B<x>:CAN:BITRate:VALue?
    - BUS:B<x>:CAN:BITRate?
    - BUS:B<x>:CAN:FD:BITRate {RATE1M|RATE2M|RATE3M|RATE4M|RATE5M|RATE6M|RATE7M|RATE8M|RATE9M|RATE10M|RATE11M|RATE12M|RATE13M|RATE14M|RATE15M|RATE16M|CUSTom}
    - BUS:B<x>:CAN:FD:BITRate:CUSTom <NR1>
    - BUS:B<x>:CAN:FD:BITRate:CUSTom?
    - BUS:B<x>:CAN:FD:BITRate?
    - BUS:B<x>:CAN:SAMPLEpoint <NR1>
    - BUS:B<x>:CAN:SAMPLEpoint?
    - BUS:B<x>:CAN:SIGNal {DIFFerential|CANH|CANL|RX|TX}
    - BUS:B<x>:CAN:SIGNal?
    - BUS:B<x>:CAN:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:CAN:SOUrce?
    - BUS:B<x>:CAN:STANDard {CAN2X|FDISO|FDNONISO}
    - BUS:B<x>:CAN:STANDard?
    - BUS:B<x>:CAN:THReshold <NR3>
    - BUS:B<x>:CAN:THReshold?
    - BUS:B<x>:CPHY:A:DATA:THRESHold <NR3>
    - BUS:B<x>:CPHY:A:DATA:THRESHold?
    - BUS:B<x>:CPHY:A:LP:THRESHold <NR3>
    - BUS:B<x>:CPHY:A:LP:THRESHold?
    - BUS:B<x>:CPHY:A:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:CPHY:A:SOUrce?
    - BUS:B<x>:CPHY:AB:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:CPHY:AB:SOUrce?
    - BUS:B<x>:CPHY:AB:THReshold <NR3>
    - BUS:B<x>:CPHY:AB:THReshold?
    - BUS:B<x>:CPHY:AGND:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:CPHY:AGND:SOUrce?
    - BUS:B<x>:CPHY:AGND:THReshold <NR3>
    - BUS:B<x>:CPHY:AGND:THReshold?
    - BUS:B<x>:CPHY:B:DATA:THRESHold <NR3>
    - BUS:B<x>:CPHY:B:DATA:THRESHold?
    - BUS:B<x>:CPHY:B:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:CPHY:B:SOUrce?
    - BUS:B<x>:CPHY:BC:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:CPHY:BC:SOUrce?
    - BUS:B<x>:CPHY:BC:THReshold <NR3>
    - BUS:B<x>:CPHY:BC:THReshold?
    - BUS:B<x>:CPHY:BITRate <NR1>
    - BUS:B<x>:CPHY:BITRate?
    - BUS:B<x>:CPHY:C:DATA:THRESHold <NR3>
    - BUS:B<x>:CPHY:C:DATA:THRESHold?
    - BUS:B<x>:CPHY:C:LP:THRESHold <NR3>
    - BUS:B<x>:CPHY:C:LP:THRESHold?
    - BUS:B<x>:CPHY:C:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:CPHY:C:SOUrce?
    - BUS:B<x>:CPHY:CA:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:CPHY:CA:SOUrce?
    - BUS:B<x>:CPHY:CA:THReshold <NR3>
    - BUS:B<x>:CPHY:CA:THReshold?
    - BUS:B<x>:CPHY:CGND:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:CPHY:CGND:SOUrce?
    - BUS:B<x>:CPHY:CGND:THReshold <NR3>
    - BUS:B<x>:CPHY:CGND:THReshold?
    - BUS:B<x>:CPHY:LP:DIRection {forward|reverse}
    - BUS:B<x>:CPHY:LP:DIRection?
    - BUS:B<x>:CPHY:SIGNALTYpe {SINGLE|DIFF}
    - BUS:B<x>:CPHY:SIGNALTYpe?
    - BUS:B<x>:CPHY:SUBTYPe {CSI|DSI|Word|Symbol}
    - BUS:B<x>:CPHY:SUBTYPe?
    - BUS:B<x>:CXPI:BITRate <NR1>
    - BUS:B<x>:CXPI:BITRate?
    - BUS:B<x>:CXPI:REC:THReshold <NR3>
    - BUS:B<x>:CXPI:REC:THReshold?
    - BUS:B<x>:CXPI:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:CXPI:SOUrce?
    - BUS:B<x>:DISplay:FORMat {HEX|BINARY|MIXEDASCII|MIXEDHEX|ASCII|DECIMAL|MIXED}
    - BUS:B<x>:DISplay:FORMat?
    - BUS:B<x>:DISplay:LAYout {BUS|BUSANDWAVEFORM}
    - BUS:B<x>:DISplay:LAYout?
    - BUS:B<x>:DPHY:CLOCk:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
    - BUS:B<x>:DPHY:CLOCk:SOUrce?
    - BUS:B<x>:DPHY:CLOCk:THRESHold <NR3>
    - BUS:B<x>:DPHY:CLOCk:THRESHold?
    - BUS:B<x>:DPHY:DMINus:DATATHRESHold <NR3>
    - BUS:B<x>:DPHY:DMINus:DATATHRESHold?
    - BUS:B<x>:DPHY:DMINus:LPTHRESHold <NR3>
    - BUS:B<x>:DPHY:DMINus:LPTHRESHold?
    - BUS:B<x>:DPHY:DMINus:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
    - BUS:B<x>:DPHY:DMINus:SOUrce?
    - BUS:B<x>:DPHY:DPlus:DATATHRESHold <NR3>
    - BUS:B<x>:DPHY:DPlus:DATATHRESHold?
    - BUS:B<x>:DPHY:DPlus:LPTHRESHold <NR3>
    - BUS:B<x>:DPHY:DPlus:LPTHRESHold?
    - BUS:B<x>:DPHY:DPlus:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
    - BUS:B<x>:DPHY:DPlus:SOUrce?
    - BUS:B<x>:DPHY:LP:DIRection {forward|reverse}
    - BUS:B<x>:DPHY:LP:DIRection?
    - BUS:B<x>:DPHY:PROTocol:TYPe {CSI|DSI}
    - BUS:B<x>:DPHY:PROTocol:TYPe?
    - BUS:B<x>:DPHY:SIGNal:ENCoding {false|true}
    - BUS:B<x>:DPHY:SIGNal:ENCoding?
    - BUS:B<x>:ESPI:ALERTVIEW {ON|OFF}
    - BUS:B<x>:ESPI:ALERTVIEW?
    - BUS:B<x>:ESPI:ALERt:POLarity {HIGH|LOW}
    - BUS:B<x>:ESPI:ALERt:POLarity?
    - BUS:B<x>:ESPI:ALERt:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
    - BUS:B<x>:ESPI:ALERt:SOUrce?
    - BUS:B<x>:ESPI:ALERt:THReshold <NR3>
    - BUS:B<x>:ESPI:ALERt:THReshold?
    - BUS:B<x>:ESPI:CHIPSELect:POLarity {HIGH|LOW}
    - BUS:B<x>:ESPI:CHIPSELect:POLarity?
    - BUS:B<x>:ESPI:CHIPSELect:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
    - BUS:B<x>:ESPI:CHIPSELect:SOUrce?
    - BUS:B<x>:ESPI:CHIPSELect:THReshold <NR3>
    - BUS:B<x>:ESPI:CHIPSELect:THReshold?
    - BUS:B<x>:ESPI:CLOCk:POLarity {FALL|RISE}
    - BUS:B<x>:ESPI:CLOCk:POLarity?
    - BUS:B<x>:ESPI:CLOCk:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
    - BUS:B<x>:ESPI:CLOCk:SOUrce?
    - BUS:B<x>:ESPI:CLOCk:THReshold <NR3>
    - BUS:B<x>:ESPI:CLOCk:THReshold?
    - BUS:B<x>:ESPI:DATAONE:POLarity {HIGH|LOW}
    - BUS:B<x>:ESPI:DATAONE:POLarity?
    - BUS:B<x>:ESPI:DATAONE:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
    - BUS:B<x>:ESPI:DATAONE:SOUrce?
    - BUS:B<x>:ESPI:DATAONE:THReshold <NR3>
    - BUS:B<x>:ESPI:DATAONE:THReshold?
    - BUS:B<x>:ESPI:DATATWO:POLarity {HIGH|LOW}
    - BUS:B<x>:ESPI:DATATWO:POLarity?
    - BUS:B<x>:ESPI:DATATWO:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
    - BUS:B<x>:ESPI:DATATWO:SOUrce?
    - BUS:B<x>:ESPI:DATATWO:THReshold <NR3>
    - BUS:B<x>:ESPI:DATATWO:THReshold?
    - BUS:B<x>:ESPI:IOMODe {SINGle|DUAL}
    - BUS:B<x>:ESPI:IOMODe?
    - BUS:B<x>:ETHERCAT:DATAMINUSTHRESHold <NR3>
    - BUS:B<x>:ETHERCAT:DATAMINUSTHRESHold?
    - BUS:B<x>:ETHERCAT:DATAPLUSTHRESHold <NR3>
    - BUS:B<x>:ETHERCAT:DATAPLUSTHRESHold?
    - BUS:B<x>:ETHERCAT:SIGNALTYpe {SINGLE|DIFF}
    - BUS:B<x>:ETHERCAT:SIGNALTYpe?
    - BUS:B<x>:ETHERCAT:SOUrce:DIFF {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:ETHERCAT:SOUrce:DIFF?
    - BUS:B<x>:ETHERCAT:SOUrce:DMINus {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:ETHERCAT:SOUrce:DMINus?
    - BUS:B<x>:ETHERCAT:SOUrce:DPLUs {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:ETHERCAT:SOUrce:DPLUs?
    - BUS:B<x>:ETHERCAT:THRESHold <NR3>
    - BUS:B<x>:ETHERCAT:THRESHold?
    - BUS:B<x>:ETHERnet:DATAMINUSTHRESHold <NR3>
    - BUS:B<x>:ETHERnet:DATAMINUSTHRESHold?
    - BUS:B<x>:ETHERnet:DATAPLUSTHRESHold <NR3>
    - BUS:B<x>:ETHERnet:DATAPLUSTHRESHold?
    - BUS:B<x>:ETHERnet:IPVFOUR {YES|NO}
    - BUS:B<x>:ETHERnet:IPVFOUR?
    - BUS:B<x>:ETHERnet:LOWTHRESHold <NR3>
    - BUS:B<x>:ETHERnet:LOWTHRESHold?
    - BUS:B<x>:ETHERnet:QTAGGING {YES|NO}
    - BUS:B<x>:ETHERnet:QTAGGING?
    - BUS:B<x>:ETHERnet:SIGNALTYpe {SINGLE|DIFF}
    - BUS:B<x>:ETHERnet:SIGNALTYpe?
    - BUS:B<x>:ETHERnet:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:ETHERnet:SOUrce:DMINus {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:ETHERnet:SOUrce:DMINus?
    - BUS:B<x>:ETHERnet:SOUrce:DPLUs {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:ETHERnet:SOUrce:DPLUs?
    - BUS:B<x>:ETHERnet:SOUrce?
    - BUS:B<x>:ETHERnet:THRESHold <NR3>
    - BUS:B<x>:ETHERnet:THRESHold?
    - BUS:B<x>:ETHERnet:TYPe {TENBASET|HUNDREDBASETX}
    - BUS:B<x>:ETHERnet:TYPe?
    - BUS:B<x>:EUSB:BITRate {HIGH|FULL|LOW}
    - BUS:B<x>:EUSB:BITRate?
    - BUS:B<x>:EUSB:DATAMINUS:DATA:THRESHold <NR3>
    - BUS:B<x>:EUSB:DATAMINUS:DATA:THRESHold?
    - BUS:B<x>:EUSB:DATAMINUSTHRESHold <NR3>
    - BUS:B<x>:EUSB:DATAMINUSTHRESHold?
    - BUS:B<x>:EUSB:DATAPLUS:DATA:THRESHold <NR3>
    - BUS:B<x>:EUSB:DATAPLUS:DATA:THRESHold?
    - BUS:B<x>:EUSB:DATAPLUSTHRESHold <NR3>
    - BUS:B<x>:EUSB:DATAPLUSTHRESHold?
    - BUS:B<x>:EUSB:LOWTHRESHold <NR3>
    - BUS:B<x>:EUSB:LOWTHRESHold?
    - BUS:B<x>:EUSB:OPERating:MODe {NATive|REPEATERHOSt|REPEATERPERIPHERAL}
    - BUS:B<x>:EUSB:OPERating:MODe?
    - BUS:B<x>:EUSB:SIGNALTYpe {SINGLE|DIFF}
    - BUS:B<x>:EUSB:SIGNALTYpe?
    - BUS:B<x>:EUSB:SOUrce:DIFF {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:EUSB:SOUrce:DIFF?
    - BUS:B<x>:EUSB:SOUrce:DMINus {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:EUSB:SOUrce:DMINus?
    - BUS:B<x>:EUSB:SOUrce:DPLUs {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:EUSB:SOUrce:DPLUs?
    - BUS:B<x>:EUSB:THRESHold <NR3>
    - BUS:B<x>:EUSB:THRESHold?
    - BUS:B<x>:FLEXray:BITRate {CUSTOM|RATE2M|RATE5M|RATE10M}
    - BUS:B<x>:FLEXray:BITRate:CUSTom <NR1>
    - BUS:B<x>:FLEXray:BITRate:CUSTom?
    - BUS:B<x>:FLEXray:BITRate?
    - BUS:B<x>:FLEXray:CHannel {A|B}
    - BUS:B<x>:FLEXray:CHannel?
    - BUS:B<x>:FLEXray:LOWTHRESHold <NR3>
    - BUS:B<x>:FLEXray:LOWTHRESHold?
    - BUS:B<x>:FLEXray:SIGnal {BDIFFBP|BM|TXRX}
    - BUS:B<x>:FLEXray:SIGnal?
    - BUS:B<x>:FLEXray:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:FLEXray:SOUrce:TXRX {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:FLEXray:SOUrce:TXRX?
    - BUS:B<x>:FLEXray:SOUrce?
    - BUS:B<x>:FLEXray:THRESHold <NR3>
    - BUS:B<x>:FLEXray:THRESHold?
    - BUS:B<x>:FLEXray:TXRXTHRESHold <NR3>
    - BUS:B<x>:FLEXray:TXRXTHRESHold?
    - BUS:B<x>:I2C:CLOCk:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:I2C:CLOCk:SOUrce?
    - BUS:B<x>:I2C:CLOCk:THReshold <NR3>
    - BUS:B<x>:I2C:CLOCk:THReshold?
    - BUS:B<x>:I2C:DATa:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:I2C:DATa:SOUrce?
    - BUS:B<x>:I2C:DATa:THReshold <NR3>
    - BUS:B<x>:I2C:DATa:THReshold?
    - BUS:B<x>:I2C:RWINADDR {0|1}
    - BUS:B<x>:I2C:RWINADDR?
    - BUS:B<x>:I3C:CLOCk:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:I3C:CLOCk:SOUrce?
    - BUS:B<x>:I3C:CLOCk:THReshold <NR3>
    - BUS:B<x>:I3C:CLOCk:THReshold?
    - BUS:B<x>:I3C:DATa:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:I3C:DATa:SOUrce?
    - BUS:B<x>:I3C:DATa:THReshold {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:I3C:DATa:THReshold?
    - BUS:B<x>:LABel:COLor <QString>
    - BUS:B<x>:LABel:COLor?
    - BUS:B<x>:LABel:FONT:BOLD {ON|OFF|1|0}
    - BUS:B<x>:LABel:FONT:BOLD?
    - BUS:B<x>:LABel:FONT:ITALic {ON|OFF|1|0}
    - BUS:B<x>:LABel:FONT:ITALic?
    - BUS:B<x>:LABel:FONT:SIZE <NR1>
    - BUS:B<x>:LABel:FONT:SIZE?
    - BUS:B<x>:LABel:FONT:TYPE <QString>
    - BUS:B<x>:LABel:FONT:TYPE?
    - BUS:B<x>:LABel:FONT:UNDERline {ON|OFF|1|0}
    - BUS:B<x>:LABel:FONT:UNDERline?
    - BUS:B<x>:LABel:XPOS <NR3>
    - BUS:B<x>:LABel:XPOS?
    - BUS:B<x>:LABel:YPOS <NR3>
    - BUS:B<x>:LABel:YPOS?
    - BUS:B<x>:LABel:name <QString>
    - BUS:B<x>:LABel:name?
    - BUS:B<x>:LIN:BITRate {RATE10K|RATE1K|RATE19K|RATE2K|RATE4K|RATE9K|CUSTom}
    - BUS:B<x>:LIN:BITRate:CUSTom <NR1>
    - BUS:B<x>:LIN:BITRate:CUSTom?
    - BUS:B<x>:LIN:BITRate?
    - BUS:B<x>:LIN:IDFORmat {NOPARity|PARity}
    - BUS:B<x>:LIN:IDFORmat?
    - BUS:B<x>:LIN:POLarity {INVerted|NORmal}
    - BUS:B<x>:LIN:POLarity?
    - BUS:B<x>:LIN:SAMPLEpoint <NR1>
    - BUS:B<x>:LIN:SAMPLEpoint?
    - BUS:B<x>:LIN:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:LIN:SOUrce:THReshold <NR3>
    - BUS:B<x>:LIN:SOUrce:THReshold?
    - BUS:B<x>:LIN:SOUrce?
    - BUS:B<x>:LIN:STANDard {MIXed|V1X|V2X}
    - BUS:B<x>:LIN:STANDard?
    - BUS:B<x>:MANChester:BITORDer {LSB|MSB}
    - BUS:B<x>:MANChester:BITORDer?
    - BUS:B<x>:MANChester:BITRate <NR1>
    - BUS:B<x>:MANChester:BITRate?
    - BUS:B<x>:MANChester:DISplaymode {BITS|PACKET}
    - BUS:B<x>:MANChester:DISplaymode?
    - BUS:B<x>:MANChester:HEADer:LENGth <NR1>
    - BUS:B<x>:MANChester:HEADer:LENGth?
    - BUS:B<x>:MANChester:IDLE:BITS <NR1>
    - BUS:B<x>:MANChester:IDLE:BITS?
    - BUS:B<x>:MANChester:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:MANChester:SOUrce?
    - BUS:B<x>:MANChester:START:INDex <NR1>
    - BUS:B<x>:MANChester:START:INDex?
    - BUS:B<x>:MANChester:SYNC:SIZe <NR1>
    - BUS:B<x>:MANChester:SYNC:SIZe?
    - BUS:B<x>:MANChester:THReshold <NR3>
    - BUS:B<x>:MANChester:THReshold?
    - BUS:B<x>:MANChester:TOLerance <NR3>
    - BUS:B<x>:MANChester:TOLerance?
    - BUS:B<x>:MANChester:TRANstion:ZERo {FALLing|RISing}
    - BUS:B<x>:MANChester:TRANstion:ZERo?
    - BUS:B<x>:MANChester:TRAiler:LENGth <NR1>
    - BUS:B<x>:MANChester:TRAiler:LENGth?
    - BUS:B<x>:MANChester:WORD:COUNt <NR1>
    - BUS:B<x>:MANChester:WORD:COUNt?
    - BUS:B<x>:MANChester:WORDSIZe <NR1>
    - BUS:B<x>:MANChester:WORDSIZe?
    - BUS:B<x>:MANChester:parity {ODD|EVEN|NONE}
    - BUS:B<x>:MANChester:parity?
    - BUS:B<x>:MDIO:CLOCk:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:MDIO:CLOCk:SOUrce?
    - BUS:B<x>:MDIO:CLOCk:THReshold <NR3>
    - BUS:B<x>:MDIO:CLOCk:THReshold?
    - BUS:B<x>:MDIO:DATA:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:MDIO:DATA:SOUrce?
    - BUS:B<x>:MDIO:DATA:THReshold <NR3>
    - BUS:B<x>:MDIO:DATA:THReshold?
    - BUS:B<x>:MIL1553B:LOWTHRESHold <NR3>
    - BUS:B<x>:MIL1553B:LOWTHRESHold?
    - BUS:B<x>:MIL1553B:POLarity {NORMal|INVERTed}
    - BUS:B<x>:MIL1553B:POLarity?
    - BUS:B<x>:MIL1553B:RESPonsetime:MAXimum <NR3>
    - BUS:B<x>:MIL1553B:RESPonsetime:MAXimum?
    - BUS:B<x>:MIL1553B:RESPonsetime:MINimum <NR3>
    - BUS:B<x>:MIL1553B:RESPonsetime:MINimum?
    - BUS:B<x>:MIL1553B:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:MIL1553B:SOUrce?
    - BUS:B<x>:MIL1553B:THRESHold <NR3>
    - BUS:B<x>:MIL1553B:THRESHold?
    - BUS:B<x>:NRZ:BITOrder {LSB|MSB}
    - BUS:B<x>:NRZ:BITOrder?
    - BUS:B<x>:NRZ:BITRate <NR1>
    - BUS:B<x>:NRZ:BITRate?
    - BUS:B<x>:NRZ:POLarity {INVerted|NORmal}
    - BUS:B<x>:NRZ:POLarity?
    - BUS:B<x>:NRZ:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>]
    - BUS:B<x>:NRZ:SOUrce?
    - BUS:B<x>:NRZ:SPMI:VERsion {v<x>}
    - BUS:B<x>:NRZ:SPMI:VERsion?
    - BUS:B<x>:NRZ:THReshold <NR3>
    - BUS:B<x>:NRZ:THReshold?
    - BUS:B<x>:ONEWIRe:DATA:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>]
    - BUS:B<x>:ONEWIRe:DATA:SOUrce?
    - BUS:B<x>:ONEWIRe:DATA:THReshold <NR3>
    - BUS:B<x>:ONEWIRe:DATA:THReshold?
    - BUS:B<x>:ONEWIRe:MODe {STAndard|OVErdrive}
    - BUS:B<x>:ONEWIRe:MODe?
    - BUS:B<x>:PARallel:ALLTHResholds <NR3>
    - BUS:B<x>:PARallel:ALLTHResholds:APPly
    - BUS:B<x>:PARallel:BIT<n>SOUrce {S<x>_Ch<x>_D|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>|NONE}
    - BUS:B<x>:PARallel:BIT<n>SOUrce:THReshold <NR3>
    - BUS:B<x>:PARallel:CLOCk:EDGE {FALLING|RISING|EITHER}
    - BUS:B<x>:PARallel:CLOCk:EDGE?
    - BUS:B<x>:PARallel:CLOCk:ISCLOCKED {OFF|ON|NR1>
    - BUS:B<x>:PARallel:CLOCk:ISCLOCKED?
    - BUS:B<x>:PARallel:CLOCkSOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>|NONE}
    - BUS:B<x>:PARallel:CLOCkSOUrce:THReshold <NR3>
    - BUS:B<x>:PARallel:CLOCkSOUrce:THReshold?
    - BUS:B<x>:PARallel:CLOCkSOUrce?
    - BUS:B<x>:PSIFIVe:BITPERiod <NR1>
    - BUS:B<x>:PSIFIVe:BITPERiod?
    - BUS:B<x>:PSIFIVe:BITRate {RATE125K|RATE189K|RATE83K}
    - BUS:B<x>:PSIFIVe:BITRate?
    - BUS:B<x>:PSIFIVe:COMM:DIRection {SENSORECU|ECUSENSor}
    - BUS:B<x>:PSIFIVe:COMM:DIRection?
    - BUS:B<x>:PSIFIVe:DATAA <NR1>
    - BUS:B<x>:PSIFIVe:DATAA?
    - BUS:B<x>:PSIFIVe:DATAB <NR1>
    - BUS:B<x>:PSIFIVe:DATAB?
    - BUS:B<x>:PSIFIVe:DATAFORMat {NIBBLe|BYTe}
    - BUS:B<x>:PSIFIVe:DATAFORMat?
    - BUS:B<x>:PSIFIVe:ECUSOURce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:PSIFIVe:ECUSOURce?
    - BUS:B<x>:PSIFIVe:FRAMECONTrol <NR1>
    - BUS:B<x>:PSIFIVe:FRAMECONTrol?
    - BUS:B<x>:PSIFIVe:MESSaging {OFF|ON}
    - BUS:B<x>:PSIFIVe:MESSaging?
    - BUS:B<x>:PSIFIVe:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:PSIFIVe:SOUrce?
    - BUS:B<x>:PSIFIVe:STATus <NR1>
    - BUS:B<x>:PSIFIVe:STATus?
    - BUS:B<x>:PSIFIVe:SYNCMODe {PULSEWIDTh|TOOTHGAP}
    - BUS:B<x>:PSIFIVe:SYNCMODe?
    - BUS:B<x>:PSIFIVe:SYNCTHRESHold <NR3>
    - BUS:B<x>:PSIFIVe:SYNCTHRESHold?
    - BUS:B<x>:PSIFIVe:THRESHold <NR3>
    - BUS:B<x>:PSIFIVe:THRESHold?
    - BUS:B<x>:RS232C:BITRate {CUSTOM|RATE300|RATE1K|RATE2K|RATE9K|RATE19K|RATE38K|RATE115K|RATE921K}
    - BUS:B<x>:RS232C:BITRate:CUSTom <NR1>
    - BUS:B<x>:RS232C:BITRate:CUSTom?
    - BUS:B<x>:RS232C:BITRate?
    - BUS:B<x>:RS232C:DATABits {7|8|9}
    - BUS:B<x>:RS232C:DATABits?
    - BUS:B<x>:RS232C:DELIMiter {NULl|CR|LF|SPace|XFF}
    - BUS:B<x>:RS232C:DELIMiter?
    - BUS:B<x>:RS232C:DISplaymode {FRame|PACKET}
    - BUS:B<x>:RS232C:DISplaymode?
    - BUS:B<x>:RS232C:PARity {NONe|EVEN|ODD}
    - BUS:B<x>:RS232C:PARity?
    - BUS:B<x>:RS232C:POLarity {NORmal|INVERTed}
    - BUS:B<x>:RS232C:POLarity?
    - BUS:B<x>:RS232C:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|REF<x>|MATH<x>|REF<x>_D<x>}
    - BUS:B<x>:RS232C:SOUrce:THReshold <NR3>
    - BUS:B<x>:RS232C:SOUrce:THReshold?
    - BUS:B<x>:RS232C:SOUrce?
    - BUS:B<x>:S8B10B:BITRate <NR1>
    - BUS:B<x>:S8B10B:BITRate?
    - BUS:B<x>:S8B10B:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:S8B10B:SOUrce?
    - BUS:B<x>:S8B10B:THReshold <NR3>
    - BUS:B<x>:S8B10B:THReshold?
    - BUS:B<x>:SDLC:BITRate <NR1>
    - BUS:B<x>:SDLC:BITRate?
    - BUS:B<x>:SDLC:DATA:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:SDLC:DATA:SOUrce?
    - BUS:B<x>:SDLC:DATA:THReshold <NR3>
    - BUS:B<x>:SDLC:DATA:THReshold?
    - BUS:B<x>:SDLC:ENCoding {DISCrete|INVert}
    - BUS:B<x>:SDLC:ENCoding?
    - BUS:B<x>:SDLC:MODulo {8|128}
    - BUS:B<x>:SDLC:MODulo?
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
    - BUS:B<x>:SENT:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|Math<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:SENT:SOUrce?
    - BUS:B<x>:SENT:THRESHold <NR3>
    - BUS:B<x>:SENT:THRESHold?
    - BUS:B<x>:SENT:TICKTIME <NR3>
    - BUS:B<x>:SENT:TICKTIME?
    - BUS:B<x>:SENT:TICKTOLerance <NR3>
    - BUS:B<x>:SENT:TICKTOLerance?
    - BUS:B<x>:SMBUS:CLOCk:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:SMBUS:CLOCk:SOUrce?
    - BUS:B<x>:SMBUS:CLOCk:THReshold <NR3>
    - BUS:B<x>:SMBUS:CLOCk:THReshold?
    - BUS:B<x>:SMBUS:DATA:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:SMBUS:DATA:SOUrce?
    - BUS:B<x>:SMBUS:DATA:THReshold <NR3>
    - BUS:B<x>:SMBUS:DATA:THReshold?
    - BUS:B<x>:SMBUS:PEC:VALUe {TRUe|FALSe}
    - BUS:B<x>:SMBUS:PEC:VALUe?
    - BUS:B<x>:SPACEWIRe:BITRate <NR3>
    - BUS:B<x>:SPACEWIRe:BITRate?
    - BUS:B<x>:SPACEWIRe:DATa:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:SPACEWIRe:DATa:SOUrce?
    - BUS:B<x>:SPACEWIRe:DATa:THReshold <NR3>
    - BUS:B<x>:SPACEWIRe:DATa:THReshold?
    - BUS:B<x>:SPACEWIRe:DECode:TYPe {STRObe|DATARate}
    - BUS:B<x>:SPACEWIRe:DECode:TYPe?
    - BUS:B<x>:SPACEWIRe:STRobe:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:SPACEWIRe:STRobe:SOUrce?
    - BUS:B<x>:SPACEWIRe:STRobe:THReshold <NR3>
    - BUS:B<x>:SPACEWIRe:STRobe:THReshold?
    - BUS:B<x>:SPACEWIRe:SYNC {DATA|NULL|AUTO|CUSTom}
    - BUS:B<x>:SPACEWIRe:SYNC:COUnt <NR1>
    - BUS:B<x>:SPACEWIRe:SYNC:COUnt?
    - BUS:B<x>:SPACEWIRe:SYNC:PATTern <NR3>
    - BUS:B<x>:SPACEWIRe:SYNC:PATTern?
    - BUS:B<x>:SPACEWIRe:SYNC:VALUe <NR3>
    - BUS:B<x>:SPACEWIRe:SYNC:VALUe?
    - BUS:B<x>:SPACEWIRe:SYNC?
    - BUS:B<x>:SPI:BITOrder {LSB|MSB}
    - BUS:B<x>:SPI:BITOrder?
    - BUS:B<x>:SPI:CLOCk:POLarity {FALL|RISE}
    - BUS:B<x>:SPI:CLOCk:POLarity?
    - BUS:B<x>:SPI:CLOCk:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:SPI:CLOCk:SOUrce?
    - BUS:B<x>:SPI:CLOCk:THReshold <NR3>
    - BUS:B<x>:SPI:CLOCk:THReshold?
    - BUS:B<x>:SPI:DATa:POLarity {HIGH|LOW}
    - BUS:B<x>:SPI:DATa:POLarity?
    - BUS:B<x>:SPI:DATa:SIZe <NR1>
    - BUS:B<x>:SPI:DATa:SIZe?
    - BUS:B<x>:SPI:DATa:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:SPI:DATa:SOUrce?
    - BUS:B<x>:SPI:DATa:THReshold <NR3>
    - BUS:B<x>:SPI:DATa:THReshold?
    - BUS:B<x>:SPI:FRAMING {IDLE|SS}
    - BUS:B<x>:SPI:FRAMING?
    - BUS:B<x>:SPI:IDLETime <NR3>
    - BUS:B<x>:SPI:IDLETime?
    - BUS:B<x>:SPI:MISo:DATa:POLarity {HIGH|LOW}
    - BUS:B<x>:SPI:MISo:DATa:POLarity?
    - BUS:B<x>:SPI:MISo:INPut {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:SPI:MISo:INPut?
    - BUS:B<x>:SPI:MISo:THReshold <NR3>
    - BUS:B<x>:SPI:MISo:THReshold?
    - BUS:B<x>:SPI:MOSi:DATa:POLarity {HIGH|LOW}
    - BUS:B<x>:SPI:MOSi:DATa:POLarity?
    - BUS:B<x>:SPI:MOSi:INPut {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:SPI:MOSi:INPut?
    - BUS:B<x>:SPI:MOSi:THReshold <NR3>
    - BUS:B<x>:SPI:MOSi:THReshold?
    - BUS:B<x>:SPI:NUMBer:INputs {ONE|TWO}
    - BUS:B<x>:SPI:NUMBer:INputs?
    - BUS:B<x>:SPI:SELect:POLarity {LOW|HIGH}
    - BUS:B<x>:SPI:SELect:POLarity?
    - BUS:B<x>:SPI:SELect:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:SPI:SELect:SOUrce?
    - BUS:B<x>:SPI:SELect:THReshold <NR3>
    - BUS:B<x>:SPI:SELect:THReshold?
    - BUS:B<x>:SPMI:SCLk:SOUrce {CH<x>|CH<x>_Dx>|Math<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:SPMI:SCLk:SOUrce?
    - BUS:B<x>:SPMI:SCLk:THReshold <NR3>
    - BUS:B<x>:SPMI:SCLk:THReshold?
    - BUS:B<x>:SPMI:SDATa:SOUrce {CH<x>|CH<x>_Dx>|Math<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:SPMI:SDATa:SOUrce?
    - BUS:B<x>:SPMI:SDATa:THReshold <NR3>
    - BUS:B<x>:SPMI:SDATa:THReshold?
    - BUS:B<x>:SVID:ALERT:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:SVID:ALERT:SOUrce?
    - BUS:B<x>:SVID:ALERT:THReshold <NR3>
    - BUS:B<x>:SVID:ALERT:THReshold?
    - BUS:B<x>:SVID:CLOCk:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:SVID:CLOCk:SOUrce?
    - BUS:B<x>:SVID:CLOCk:THReshold <NR3>
    - BUS:B<x>:SVID:CLOCk:THReshold?
    - BUS:B<x>:SVID:DATA:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:SVID:DATA:SOUrce?
    - BUS:B<x>:SVID:DATA:THReshold <NR3>
    - BUS:B<x>:SVID:DATA:THReshold?
    - BUS:B<x>:TYPe {ARINC429|AUDio|CAN|ETHernet|EUSB|FLEXRAY|I2C|I3C|LIN|MDIO|MIL1553B|PARallel|RS232C|SENT|SPI|SPMI|SVID|USB}
    - BUS:B<x>:TYPe?
    - BUS:B<x>:USB:BITRate {FULL|HIGH|LOW}
    - BUS:B<x>:USB:BITRate?
    - BUS:B<x>:USB:DATAMINUSTHRESHold <NR3>
    - BUS:B<x>:USB:DATAMINUSTHRESHold?
    - BUS:B<x>:USB:DATAPLUSTHRESHold <NR3>
    - BUS:B<x>:USB:DATAPLUSTHRESHold?
    - BUS:B<x>:USB:LOWTHRESHold <NR3>
    - BUS:B<x>:USB:LOWTHRESHold?
    - BUS:B<x>:USB:SIGNALTYpe {SINGLE|DIFF}
    - BUS:B<x>:USB:SIGNALTYpe?
    - BUS:B<x>:USB:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
    - BUS:B<x>:USB:SOUrce:DMINus {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:USB:SOUrce:DMINus?
    - BUS:B<x>:USB:SOUrce:DPLUs {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:USB:SOUrce:DPLUs?
    - BUS:B<x>:USB:SOUrce?
    - BUS:B<x>:USB:THRESHold <NR3>
    - BUS:B<x>:USB:THRESHold?
    - BUS:DELete <QString>
    - BUS:LIST?
    ```
"""  # noqa: E501

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    SCPICmdWriteNoArguments,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class BusList(SCPICmdRead):
    """The ``BUS:LIST`` command.

    Description:
        - This query returns a comma separated list of all currently defined buses.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:LIST?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:LIST?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - BUS:LIST?
        ```
    """


class BusDelete(SCPICmdWrite):
    """The ``BUS:DELete`` command.

    Description:
        - This command deletes the specified bus.

    Usage:
        - Using the ``.write(value)`` method will send the ``BUS:DELete value`` command.

    SCPI Syntax:
        ```
        - BUS:DELete <QString>
        ```

    Info:
        - ``<QString>`` specifies the bus to delete and is of the form 'B<NR1>', where <NR1> is ≥1.
    """

    _WRAP_ARG_WITH_QUOTES = True


class BusBItemUsbThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:USB:THRESHold`` command.

    Description:
        - This command sets or queries the USB DATA source High threshold for the specified bus when
          the signal source is differential. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:USB:THRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:THRESHold?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:THRESHold value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:USB:THRESHold <NR3>
        - BUS:B<x>:USB:THRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` is the USB DATA source High threshold for the specified bus.
    """


class BusBItemUsbSourceDplus(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:USB:SOUrce:DPLUs`` command.

    Description:
        - This command sets or queries the USB dataPlus (SDATAPLUS) source for the specified bus
          when the signal type is single ended. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:USB:SOUrce:DPLUs?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:SOUrce:DPLUs?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:SOUrce:DPLUs value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:USB:SOUrce:DPLUs {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:USB:SOUrce:DPLUs?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``S<x>_Ch<x>_D<x>`` specifies is the remote scope number, the analog channel and the
          digital channel.
        - ``CH<x>`` specifies an analog channel as the D+ source for the specified USB bus.
        - ``CH<x>_D<x>`` specifies a digital channel as the D+ source for the specified USB bus.
        - ``MATH<x>`` specifies a math channel as the D+ source for the specified USB bus.
        - ``REF<x>`` specifies a reference waveform as the source.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the clock source waveform for
          the specified USB bus.
    """


class BusBItemUsbSourceDminus(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:USB:SOUrce:DMINus`` command.

    Description:
        - This command sets or queries the USB D- (SDATAMINUS) source for bus <x> when the signal
          type is single ended. The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:USB:SOUrce:DMINus?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:SOUrce:DMINus?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:SOUrce:DMINus value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:USB:SOUrce:DMINus {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:USB:SOUrce:DMINus?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``S<x>_Ch<x>_D<x>`` specifies is the remote scope number, the analog channel and the
          digital channel.
        - ``CH<x>`` specifies an analog channel as the D- source for the specified USB bus.
        - ``CH<x>_D<x>`` specifies a digital channel as the D- source for the specified USB bus.
        - ``MATH<x>`` specifies a math channel as the D- source for the specified USB bus.
        - ``REF<x>`` specifies a reference waveform as the source.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the clock source waveform for
          the specified USB bus.
    """


class BusBItemUsbSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:USB:SOUrce`` command.

    Description:
        - This command sets or queries the USB data source when the signal type is differential for
          bus <x>. The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:USB:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:SOUrce?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:USB:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:USB:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog channel as the data source for the specified USB bus.
        - ``MATH<x>`` specifies a math channel as the data source for the specified USB bus.
        - ``REF<x>`` specifies a reference waveform as the data source.

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
            - This command sets or queries the USB D- (SDATAMINUS) source for bus <x> when the
              signal type is single ended. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:USB:SOUrce:DMINus?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:SOUrce:DMINus?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:SOUrce:DMINus value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:USB:SOUrce:DMINus {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:USB:SOUrce:DMINus?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``S<x>_Ch<x>_D<x>`` specifies is the remote scope number, the analog channel and the
              digital channel.
            - ``CH<x>`` specifies an analog channel as the D- source for the specified USB bus.
            - ``CH<x>_D<x>`` specifies a digital channel as the D- source for the specified USB bus.
            - ``MATH<x>`` specifies a math channel as the D- source for the specified USB bus.
            - ``REF<x>`` specifies a reference waveform as the source.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the clock source waveform
              for the specified USB bus.
        """  # noqa: E501
        return self._dminus

    @property
    def dplus(self) -> BusBItemUsbSourceDplus:
        """Return the ``BUS:B<x>:USB:SOUrce:DPLUs`` command.

        Description:
            - This command sets or queries the USB dataPlus (SDATAPLUS) source for the specified bus
              when the signal type is single ended. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:USB:SOUrce:DPLUs?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:SOUrce:DPLUs?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:SOUrce:DPLUs value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:USB:SOUrce:DPLUs {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:USB:SOUrce:DPLUs?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``S<x>_Ch<x>_D<x>`` specifies is the remote scope number, the analog channel and the
              digital channel.
            - ``CH<x>`` specifies an analog channel as the D+ source for the specified USB bus.
            - ``CH<x>_D<x>`` specifies a digital channel as the D+ source for the specified USB bus.
            - ``MATH<x>`` specifies a math channel as the D+ source for the specified USB bus.
            - ``REF<x>`` specifies a reference waveform as the source.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the clock source waveform
              for the specified USB bus.
        """  # noqa: E501
        return self._dplus


class BusBItemUsbSignaltype(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:USB:SIGNALTYpe`` command.

    Description:
        - This command sets or queries the USB signal type for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:USB:SIGNALTYpe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:SIGNALTYpe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:SIGNALTYpe value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:USB:SIGNALTYpe {SINGLE|DIFF}
        - BUS:B<x>:USB:SIGNALTYpe?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``SINGLE`` specifies single-ended signals.
        - ``DIFF`` specifies differential signals.
    """


class BusBItemUsbLowthreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:USB:LOWTHRESHold`` command.

    Description:
        - This command sets or queries the USB data source threshold for the specified bus when the
          signal type is differential. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:USB:LOWTHRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:LOWTHRESHold?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:LOWTHRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:USB:LOWTHRESHold <NR3>
        - BUS:B<x>:USB:LOWTHRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` is the Low threshold.
    """


class BusBItemUsbDataplusthreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:USB:DATAPLUSTHRESHold`` command.

    Description:
        - This command sets or queries the USB D+ source threshold for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:USB:DATAPLUSTHRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:DATAPLUSTHRESHold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:DATAPLUSTHRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:USB:DATAPLUSTHRESHold <NR3>
        - BUS:B<x>:USB:DATAPLUSTHRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` is the Plus threshold.
    """


class BusBItemUsbDataminusthreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:USB:DATAMINUSTHRESHold`` command.

    Description:
        - This command sets or queries the USB D- source threshold for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:USB:DATAMINUSTHRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:DATAMINUSTHRESHold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:DATAMINUSTHRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:USB:DATAMINUSTHRESHold <NR3>
        - BUS:B<x>:USB:DATAMINUSTHRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` is the Minus threshold.
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
        - ``.dataminusthreshold``: The ``BUS:B<x>:USB:DATAMINUSTHRESHold`` command.
        - ``.dataplusthreshold``: The ``BUS:B<x>:USB:DATAPLUSTHRESHold`` command.
        - ``.lowthreshold``: The ``BUS:B<x>:USB:LOWTHRESHold`` command.
        - ``.signaltype``: The ``BUS:B<x>:USB:SIGNALTYpe`` command.
        - ``.source``: The ``BUS:B<x>:USB:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:USB:THRESHold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemUsbBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._dataminusthreshold = BusBItemUsbDataminusthreshold(
            device, f"{self._cmd_syntax}:DATAMINUSTHRESHold"
        )
        self._dataplusthreshold = BusBItemUsbDataplusthreshold(
            device, f"{self._cmd_syntax}:DATAPLUSTHRESHold"
        )
        self._lowthreshold = BusBItemUsbLowthreshold(device, f"{self._cmd_syntax}:LOWTHRESHold")
        self._signaltype = BusBItemUsbSignaltype(device, f"{self._cmd_syntax}:SIGNALTYpe")
        self._source = BusBItemUsbSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemUsbThreshold(device, f"{self._cmd_syntax}:THRESHold")

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
    def dataminusthreshold(self) -> BusBItemUsbDataminusthreshold:
        """Return the ``BUS:B<x>:USB:DATAMINUSTHRESHold`` command.

        Description:
            - This command sets or queries the USB D- source threshold for the specified bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:USB:DATAMINUSTHRESHold?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:DATAMINUSTHRESHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:USB:DATAMINUSTHRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:USB:DATAMINUSTHRESHold <NR3>
            - BUS:B<x>:USB:DATAMINUSTHRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` is the Minus threshold.
        """
        return self._dataminusthreshold

    @property
    def dataplusthreshold(self) -> BusBItemUsbDataplusthreshold:
        """Return the ``BUS:B<x>:USB:DATAPLUSTHRESHold`` command.

        Description:
            - This command sets or queries the USB D+ source threshold for the specified bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:USB:DATAPLUSTHRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:DATAPLUSTHRESHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:USB:DATAPLUSTHRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:USB:DATAPLUSTHRESHold <NR3>
            - BUS:B<x>:USB:DATAPLUSTHRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` is the Plus threshold.
        """
        return self._dataplusthreshold

    @property
    def lowthreshold(self) -> BusBItemUsbLowthreshold:
        """Return the ``BUS:B<x>:USB:LOWTHRESHold`` command.

        Description:
            - This command sets or queries the USB data source threshold for the specified bus when
              the signal type is differential. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:USB:LOWTHRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:LOWTHRESHold?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:LOWTHRESHold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:USB:LOWTHRESHold <NR3>
            - BUS:B<x>:USB:LOWTHRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` is the Low threshold.
        """
        return self._lowthreshold

    @property
    def signaltype(self) -> BusBItemUsbSignaltype:
        """Return the ``BUS:B<x>:USB:SIGNALTYpe`` command.

        Description:
            - This command sets or queries the USB signal type for the specified bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:USB:SIGNALTYpe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:SIGNALTYpe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:SIGNALTYpe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:USB:SIGNALTYpe {SINGLE|DIFF}
            - BUS:B<x>:USB:SIGNALTYpe?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``SINGLE`` specifies single-ended signals.
            - ``DIFF`` specifies differential signals.
        """
        return self._signaltype

    @property
    def source(self) -> BusBItemUsbSource:
        """Return the ``BUS:B<x>:USB:SOUrce`` command.

        Description:
            - This command sets or queries the USB data source when the signal type is differential
              for bus <x>. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:USB:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:USB:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:USB:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog channel as the data source for the specified USB bus.
            - ``MATH<x>`` specifies a math channel as the data source for the specified USB bus.
            - ``REF<x>`` specifies a reference waveform as the data source.

        Sub-properties:
            - ``.dminus``: The ``BUS:B<x>:USB:SOUrce:DMINus`` command.
            - ``.dplus``: The ``BUS:B<x>:USB:SOUrce:DPLUs`` command.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemUsbThreshold:
        """Return the ``BUS:B<x>:USB:THRESHold`` command.

        Description:
            - This command sets or queries the USB DATA source High threshold for the specified bus
              when the signal source is differential. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:USB:THRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:USB:THRESHold?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:USB:THRESHold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:USB:THRESHold <NR3>
            - BUS:B<x>:USB:THRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` is the USB DATA source High threshold for the specified bus.
        """
        return self._threshold


class BusBItemType(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:TYPe`` command.

    Description:
        - This command sets or queries the bus type or standard for the specified bus. The bus is
          specified by x. Arguments for a bus type are only available then the required serial bus
          option is installed.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:TYPe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:TYPe value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:TYPe {ARINC429|AUDio|CAN|ETHernet|EUSB|FLEXRAY|I2C|I3C|LIN|MDIO|MIL1553B|PARallel|RS232C|SENT|SPI|SPMI|SVID|USB}
        - BUS:B<x>:TYPe?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``ARINC429`` specifies the ARINC 429 avionics serial bus.
        - ``AUDio`` specifies an audio bus.
        - ``CAN`` specifies a Controller Area Network bus.
        - ``ETHernet`` specifies the Ethernet bus.
        - ``EUSB`` specifies a eUSB bus. Requires option SR-EUSB2.
        - ``FLEXRAY`` specifies a FlexRay bus.
        - ``I2C`` specifies the Inter-IC bus.
        - ``I3C`` specifies the MIPI Improved Inter Integrated Circuit (I3C) bus.
        - ``LIN`` specifies a Local Interconnect Network bus.
        - ``MDIO`` specifies a MDIO bus.
        - ``MIL1553B`` specifies the MIL-STD-1553 avionics serial bus.
        - ``PARallel`` specifies a parallel bus.
        - ``RS232C`` specifies the RS-232 Serial bus.
        - ``SENT`` specifies the Single Edge Nibble Transmission (SENT) automotive serial bus.
        - ``SPI`` specifies the Serial Peripheral Interface bus.
        - ``SPMI`` Specifies a System Power Management Interface bus.
        - ``SVID`` Specifies a Serial VID bus.
        - ``USB`` specifies the Universal Serial bus.
    """  # noqa: E501


class BusBItemSvidDataThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SVID:DATA:THReshold`` command.

    Description:
        - This command sets or queries the data threshold for the specified SVID bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SVID:DATA:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SVID:DATA:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SVID:DATA:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SVID:DATA:THReshold <NR3>
        - BUS:B<x>:SVID:DATA:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` is the SVID Strobe threshold for the specified bus. The argument range is -8V to
          +8V.
    """


class BusBItemSvidDataSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SVID:DATA:SOUrce`` command.

    Description:
        - This command sets or queries data source channel for the specified SVID bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SVID:DATA:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SVID:DATA:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SVID:DATA:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SVID:DATA:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:SVID:DATA:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``MATH<x>`` specifies a math channel as the source.
        - ``REF<x>`` specifies a digital reference waveform as the source.
    """


class BusBItemSvidData(SCPICmdRead):
    """The ``BUS:B<x>:SVID:DATA`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SVID:DATA?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SVID:DATA?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.source``: The ``BUS:B<x>:SVID:DATA:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:SVID:DATA:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemSvidDataSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemSvidDataThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def source(self) -> BusBItemSvidDataSource:
        """Return the ``BUS:B<x>:SVID:DATA:SOUrce`` command.

        Description:
            - This command sets or queries data source channel for the specified SVID bus. The bus
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SVID:DATA:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SVID:DATA:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SVID:DATA:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SVID:DATA:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:SVID:DATA:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``MATH<x>`` specifies a math channel as the source.
            - ``REF<x>`` specifies a digital reference waveform as the source.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemSvidDataThreshold:
        """Return the ``BUS:B<x>:SVID:DATA:THReshold`` command.

        Description:
            - This command sets or queries the data threshold for the specified SVID bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SVID:DATA:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SVID:DATA:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SVID:DATA:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SVID:DATA:THReshold <NR3>
            - BUS:B<x>:SVID:DATA:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` is the SVID Strobe threshold for the specified bus. The argument range is
              -8V to +8V.
        """
        return self._threshold


class BusBItemSvidClockThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SVID:CLOCk:THReshold`` command.

    Description:
        - This command sets or queries the clock threshold for the specified SVID bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SVID:CLOCk:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SVID:CLOCk:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SVID:CLOCk:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SVID:CLOCk:THReshold <NR3>
        - BUS:B<x>:SVID:CLOCk:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` is the SVID Strobe threshold for the specified bus. The argument range is -8V to
          +8V.
    """


class BusBItemSvidClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SVID:CLOCk:SOUrce`` command.

    Description:
        - This command sets or queries clock source channel for the specified SVID bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SVID:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SVID:CLOCk:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SVID:CLOCk:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SVID:CLOCk:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:SVID:CLOCk:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``MATH<x>`` specifies a math channel as the source.
        - ``REF<x>`` specifies a digital reference waveform as the source.
    """


class BusBItemSvidClock(SCPICmdRead):
    """The ``BUS:B<x>:SVID:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SVID:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SVID:CLOCk?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.source``: The ``BUS:B<x>:SVID:CLOCk:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:SVID:CLOCk:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemSvidClockSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemSvidClockThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def source(self) -> BusBItemSvidClockSource:
        """Return the ``BUS:B<x>:SVID:CLOCk:SOUrce`` command.

        Description:
            - This command sets or queries clock source channel for the specified SVID bus. The bus
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SVID:CLOCk:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SVID:CLOCk:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SVID:CLOCk:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SVID:CLOCk:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:SVID:CLOCk:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``MATH<x>`` specifies a math channel as the source.
            - ``REF<x>`` specifies a digital reference waveform as the source.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemSvidClockThreshold:
        """Return the ``BUS:B<x>:SVID:CLOCk:THReshold`` command.

        Description:
            - This command sets or queries the clock threshold for the specified SVID bus. The bus
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SVID:CLOCk:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SVID:CLOCk:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SVID:CLOCk:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SVID:CLOCk:THReshold <NR3>
            - BUS:B<x>:SVID:CLOCk:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` is the SVID Strobe threshold for the specified bus. The argument range is
              -8V to +8V.
        """
        return self._threshold


class BusBItemSvidAlertThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SVID:ALERT:THReshold`` command.

    Description:
        - This command sets or queries the alert threshold for the specified SVID bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SVID:ALERT:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SVID:ALERT:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SVID:ALERT:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SVID:ALERT:THReshold <NR3>
        - BUS:B<x>:SVID:ALERT:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` is the SVID Strobe threshold for the specified bus. The argument range is -8V to
          +8V.
    """


class BusBItemSvidAlertSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SVID:ALERT:SOUrce`` command.

    Description:
        - This command sets or queries alert source channel for the specified SVID bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SVID:ALERT:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SVID:ALERT:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SVID:ALERT:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SVID:ALERT:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:SVID:ALERT:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog channel as the data source.
        - ``MATH<x>`` specifies a math channel as the data source.
        - ``REF<x>`` specifies a digital reference waveform as the data source.
    """


class BusBItemSvidAlert(SCPICmdRead):
    """The ``BUS:B<x>:SVID:ALERT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SVID:ALERT?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SVID:ALERT?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.source``: The ``BUS:B<x>:SVID:ALERT:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:SVID:ALERT:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemSvidAlertSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemSvidAlertThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def source(self) -> BusBItemSvidAlertSource:
        """Return the ``BUS:B<x>:SVID:ALERT:SOUrce`` command.

        Description:
            - This command sets or queries alert source channel for the specified SVID bus. The bus
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SVID:ALERT:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SVID:ALERT:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SVID:ALERT:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SVID:ALERT:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:SVID:ALERT:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog channel as the data source.
            - ``MATH<x>`` specifies a math channel as the data source.
            - ``REF<x>`` specifies a digital reference waveform as the data source.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemSvidAlertThreshold:
        """Return the ``BUS:B<x>:SVID:ALERT:THReshold`` command.

        Description:
            - This command sets or queries the alert threshold for the specified SVID bus. The bus
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SVID:ALERT:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SVID:ALERT:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SVID:ALERT:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SVID:ALERT:THReshold <NR3>
            - BUS:B<x>:SVID:ALERT:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` is the SVID Strobe threshold for the specified bus. The argument range is
              -8V to +8V.
        """
        return self._threshold


class BusBItemSvid(SCPICmdRead):
    """The ``BUS:B<x>:SVID`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SVID?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SVID?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.alert``: The ``BUS:B<x>:SVID:ALERT`` command tree.
        - ``.clock``: The ``BUS:B<x>:SVID:CLOCk`` command tree.
        - ``.data``: The ``BUS:B<x>:SVID:DATA`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._alert = BusBItemSvidAlert(device, f"{self._cmd_syntax}:ALERT")
        self._clock = BusBItemSvidClock(device, f"{self._cmd_syntax}:CLOCk")
        self._data = BusBItemSvidData(device, f"{self._cmd_syntax}:DATA")

    @property
    def alert(self) -> BusBItemSvidAlert:
        """Return the ``BUS:B<x>:SVID:ALERT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SVID:ALERT?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SVID:ALERT?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:SVID:ALERT:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:SVID:ALERT:THReshold`` command.
        """
        return self._alert

    @property
    def clock(self) -> BusBItemSvidClock:
        """Return the ``BUS:B<x>:SVID:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SVID:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SVID:CLOCk?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:SVID:CLOCk:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:SVID:CLOCk:THReshold`` command.
        """
        return self._clock

    @property
    def data(self) -> BusBItemSvidData:
        """Return the ``BUS:B<x>:SVID:DATA`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SVID:DATA?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SVID:DATA?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:SVID:DATA:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:SVID:DATA:THReshold`` command.
        """
        return self._data


class BusBItemSpmiSdataThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPMI:SDATa:THReshold`` command.

    Description:
        - This command sets or queries the SPMI Data (SDATA) source threshold for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPMI:SDATa:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPMI:SDATa:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPMI:SDATa:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPMI:SDATa:THReshold <NR3>
        - BUS:B<x>:SPMI:SDATa:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` is the data (SDATA) source threshold value for the specified SPMI bus.
    """


class BusBItemSpmiSdataSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPMI:SDATa:SOUrce`` command.

    Description:
        - This command sets or queries the SPMI Data (SDATA) source for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPMI:SDATa:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPMI:SDATa:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPMI:SDATa:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPMI:SDATa:SOUrce {CH<x>|CH<x>_Dx>|Math<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:SPMI:SDATa:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``CH<x>`` specifies an analog channel as the data source waveform for the SPMI bus.
        - ``CH<x>_Dx>`` specifies a digital channel and bit as the data source waveform for the
          specified SPMI bus.
        - ``Math<x>`` specifies a math waveform as the data source waveform for the specified SPMI
          bus.
        - ``REF<x>`` specifies a reference waveform as the data source waveform for the specified
          SPMI bus.
        - ``REF<x>_D<x>`` specifies a digital reference waveform and bit as the data source waveform
          for the specified SPMI bus.
    """


class BusBItemSpmiSdata(SCPICmdRead):
    """The ``BUS:B<x>:SPMI:SDATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPMI:SDATa?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPMI:SDATa?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.source``: The ``BUS:B<x>:SPMI:SDATa:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:SPMI:SDATa:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemSpmiSdataSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemSpmiSdataThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def source(self) -> BusBItemSpmiSdataSource:
        """Return the ``BUS:B<x>:SPMI:SDATa:SOUrce`` command.

        Description:
            - This command sets or queries the SPMI Data (SDATA) source for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPMI:SDATa:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPMI:SDATa:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPMI:SDATa:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPMI:SDATa:SOUrce {CH<x>|CH<x>_Dx>|Math<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:SPMI:SDATa:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``CH<x>`` specifies an analog channel as the data source waveform for the SPMI bus.
            - ``CH<x>_Dx>`` specifies a digital channel and bit as the data source waveform for the
              specified SPMI bus.
            - ``Math<x>`` specifies a math waveform as the data source waveform for the specified
              SPMI bus.
            - ``REF<x>`` specifies a reference waveform as the data source waveform for the
              specified SPMI bus.
            - ``REF<x>_D<x>`` specifies a digital reference waveform and bit as the data source
              waveform for the specified SPMI bus.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemSpmiSdataThreshold:
        """Return the ``BUS:B<x>:SPMI:SDATa:THReshold`` command.

        Description:
            - This command sets or queries the SPMI Data (SDATA) source threshold for the specified
              bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPMI:SDATa:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPMI:SDATa:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPMI:SDATa:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPMI:SDATa:THReshold <NR3>
            - BUS:B<x>:SPMI:SDATa:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` is the data (SDATA) source threshold value for the specified SPMI bus.
        """
        return self._threshold


class BusBItemSpmiSclkThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPMI:SCLk:THReshold`` command.

    Description:
        - This command sets or queries the SPMI Clock (SCLK) source threshold for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPMI:SCLk:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPMI:SCLk:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPMI:SCLk:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPMI:SCLk:THReshold <NR3>
        - BUS:B<x>:SPMI:SCLk:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` is the clock (SCLK) source threshold value for the specified SPMI bus.
    """


class BusBItemSpmiSclkSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPMI:SCLk:SOUrce`` command.

    Description:
        - This command sets or queries the SPMI Clock (SCLK) source for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPMI:SCLk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPMI:SCLk:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPMI:SCLk:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPMI:SCLk:SOUrce {CH<x>|CH<x>_Dx>|Math<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:SPMI:SCLk:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``CH<x>`` specifies an analog channel as the clock source waveform for the SPMI bus.
        - ``CH<x>_Dx>`` specifies a digital channel and bit as the clock source waveform for the
          specified SPMI bus.
        - ``Math<x>`` specifies a math waveform as the clock source waveform for the specified SPMI
          bus.
        - ``REF<x>`` specifies a reference waveform as the clock source waveform for the specified
          SPMI bus.
        - ``REF<x>_D<x>`` specifies a digital reference waveform and bit as the clock source
          waveform for the specified SPMI bus.
    """


class BusBItemSpmiSclk(SCPICmdRead):
    """The ``BUS:B<x>:SPMI:SCLk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPMI:SCLk?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPMI:SCLk?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.source``: The ``BUS:B<x>:SPMI:SCLk:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:SPMI:SCLk:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemSpmiSclkSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemSpmiSclkThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def source(self) -> BusBItemSpmiSclkSource:
        """Return the ``BUS:B<x>:SPMI:SCLk:SOUrce`` command.

        Description:
            - This command sets or queries the SPMI Clock (SCLK) source for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPMI:SCLk:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPMI:SCLk:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPMI:SCLk:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPMI:SCLk:SOUrce {CH<x>|CH<x>_Dx>|Math<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:SPMI:SCLk:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``CH<x>`` specifies an analog channel as the clock source waveform for the SPMI bus.
            - ``CH<x>_Dx>`` specifies a digital channel and bit as the clock source waveform for the
              specified SPMI bus.
            - ``Math<x>`` specifies a math waveform as the clock source waveform for the specified
              SPMI bus.
            - ``REF<x>`` specifies a reference waveform as the clock source waveform for the
              specified SPMI bus.
            - ``REF<x>_D<x>`` specifies a digital reference waveform and bit as the clock source
              waveform for the specified SPMI bus.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemSpmiSclkThreshold:
        """Return the ``BUS:B<x>:SPMI:SCLk:THReshold`` command.

        Description:
            - This command sets or queries the SPMI Clock (SCLK) source threshold for the specified
              bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPMI:SCLk:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPMI:SCLk:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPMI:SCLk:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPMI:SCLk:THReshold <NR3>
            - BUS:B<x>:SPMI:SCLk:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` is the clock (SCLK) source threshold value for the specified SPMI bus.
        """
        return self._threshold


class BusBItemSpmi(SCPICmdRead):
    """The ``BUS:B<x>:SPMI`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPMI?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPMI?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.sclk``: The ``BUS:B<x>:SPMI:SCLk`` command tree.
        - ``.sdata``: The ``BUS:B<x>:SPMI:SDATa`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._sclk = BusBItemSpmiSclk(device, f"{self._cmd_syntax}:SCLk")
        self._sdata = BusBItemSpmiSdata(device, f"{self._cmd_syntax}:SDATa")

    @property
    def sclk(self) -> BusBItemSpmiSclk:
        """Return the ``BUS:B<x>:SPMI:SCLk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPMI:SCLk?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPMI:SCLk?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:SPMI:SCLk:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:SPMI:SCLk:THReshold`` command.
        """
        return self._sclk

    @property
    def sdata(self) -> BusBItemSpmiSdata:
        """Return the ``BUS:B<x>:SPMI:SDATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPMI:SDATa?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPMI:SDATa?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:SPMI:SDATa:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:SPMI:SDATa:THReshold`` command.
        """
        return self._sdata


class BusBItemSpiSelectThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:SELect:THReshold`` command.

    Description:
        - This command sets or queries the SPI Select (SS) source threshold for the specified bus.
          The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SELect:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:SELect:THReshold <NR3>
        - BUS:B<x>:SPI:SELect:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` is the SPI Select (SS) source threshold for the specified bus.
    """


class BusBItemSpiSelectSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:SELect:SOUrce`` command.

    Description:
        - This command sets or queries the SPI Slave Select (SS) source for the specified bus. The
          bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:SELect:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:SPI:SELect:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``S<x>_Ch<x>_D<x>`` specifies is the remote scope number, the analog channel and the
          digital channel.
        - ``CH<x>`` designates an analog channel as the buses' SPI Slave Select source.
        - ``CH<x>_D<x>`` designates a digital channel as the buses' SPI Slave Select source.
        - ``MATH<x>`` designates a math waveform as the Slave Select source.
        - ``REF<x>`` designates a reference waveform as the Slave Select source.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the clock source waveform for
          the specified SPI bus.
    """


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
        - ``.threshold``: The ``BUS:B<x>:SPI:SELect:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemSpiSelectPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemSpiSelectSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemSpiSelectThreshold(device, f"{self._cmd_syntax}:THReshold")

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
              The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:SELect:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:SPI:SELect:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``S<x>_Ch<x>_D<x>`` specifies is the remote scope number, the analog channel and the
              digital channel.
            - ``CH<x>`` designates an analog channel as the buses' SPI Slave Select source.
            - ``CH<x>_D<x>`` designates a digital channel as the buses' SPI Slave Select source.
            - ``MATH<x>`` designates a math waveform as the Slave Select source.
            - ``REF<x>`` designates a reference waveform as the Slave Select source.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the clock source waveform
              for the specified SPI bus.
        """  # noqa: E501
        return self._source

    @property
    def threshold(self) -> BusBItemSpiSelectThreshold:
        """Return the ``BUS:B<x>:SPI:SELect:THReshold`` command.

        Description:
            - This command sets or queries the SPI Select (SS) source threshold for the specified
              bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPI:SELect:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:SELect:THReshold <NR3>
            - BUS:B<x>:SPI:SELect:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` is the SPI Select (SS) source threshold for the specified bus.
        """
        return self._threshold


class BusBItemSpiNumberInputs(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:NUMBer:INputs`` command.

    Description:
        - This command sets or queries the number of inputs for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:NUMBer:INputs?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:NUMBer:INputs?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:NUMBer:INputs value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:NUMBer:INputs {ONE|TWO}
        - BUS:B<x>:SPI:NUMBer:INputs?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``ONE`` sets the Data Inputs as one.
        - ``TWO`` sets the Data Inputs as two.
    """


class BusBItemSpiNumber(SCPICmdRead):
    """The ``BUS:B<x>:SPI:NUMBer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:NUMBer?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:NUMBer?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.inputs``: The ``BUS:B<x>:SPI:NUMBer:INputs`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._inputs = BusBItemSpiNumberInputs(device, f"{self._cmd_syntax}:INputs")

    @property
    def inputs(self) -> BusBItemSpiNumberInputs:
        """Return the ``BUS:B<x>:SPI:NUMBer:INputs`` command.

        Description:
            - This command sets or queries the number of inputs for the specified bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:NUMBer:INputs?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:NUMBer:INputs?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:NUMBer:INputs value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:NUMBer:INputs {ONE|TWO}
            - BUS:B<x>:SPI:NUMBer:INputs?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``ONE`` sets the Data Inputs as one.
            - ``TWO`` sets the Data Inputs as two.
        """
        return self._inputs


class BusBItemSpiMosiThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:MOSi:THReshold`` command.

    Description:
        - This command sets or queries the SPI MOSI source thresold for the specified bus. The bus
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MOSi:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MOSi:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:MOSi:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:MOSi:THReshold <NR3>
        - BUS:B<x>:SPI:MOSi:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` is the SPI MOSI Data source threshold for the specified bus.
    """


class BusBItemSpiMosiInput(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:MOSi:INPut`` command.

    Description:
        - This command sets or queries the SPI MOSI source for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MOSi:INPut?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MOSi:INPut?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:MOSi:INPut value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:MOSi:INPut {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:SPI:MOSi:INPut?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` designates an analog channel as the source.
        - ``MATH<x>`` designates a math waveform as the source.
        - ``REF<x>`` designates a reference waveform as the source.
    """


class BusBItemSpiMosiDataPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:MOSi:DATa:POLarity`` command.

    Description:
        - This command sets or queries the SPI MOSI source polarity for the specified bus. The bus
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MOSi:DATa:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MOSi:DATa:POLarity?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:MOSi:DATa:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:MOSi:DATa:POLarity {HIGH|LOW}
        - BUS:B<x>:SPI:MOSi:DATa:POLarity?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``HIGH`` sets the polarity to high.
        - ``LOW`` sets the polarity to low.
    """


class BusBItemSpiMosiData(SCPICmdRead):
    """The ``BUS:B<x>:SPI:MOSi:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MOSi:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MOSi:DATa?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:SPI:MOSi:DATa:POLarity`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemSpiMosiDataPolarity(device, f"{self._cmd_syntax}:POLarity")

    @property
    def polarity(self) -> BusBItemSpiMosiDataPolarity:
        """Return the ``BUS:B<x>:SPI:MOSi:DATa:POLarity`` command.

        Description:
            - This command sets or queries the SPI MOSI source polarity for the specified bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MOSi:DATa:POLarity?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MOSi:DATa:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPI:MOSi:DATa:POLarity value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:MOSi:DATa:POLarity {HIGH|LOW}
            - BUS:B<x>:SPI:MOSi:DATa:POLarity?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``HIGH`` sets the polarity to high.
            - ``LOW`` sets the polarity to low.
        """
        return self._polarity


class BusBItemSpiMosi(SCPICmdRead):
    """The ``BUS:B<x>:SPI:MOSi`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MOSi?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MOSi?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.data``: The ``BUS:B<x>:SPI:MOSi:DATa`` command tree.
        - ``.input``: The ``BUS:B<x>:SPI:MOSi:INPut`` command.
        - ``.threshold``: The ``BUS:B<x>:SPI:MOSi:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._data = BusBItemSpiMosiData(device, f"{self._cmd_syntax}:DATa")
        self._input = BusBItemSpiMosiInput(device, f"{self._cmd_syntax}:INPut")
        self._threshold = BusBItemSpiMosiThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def data(self) -> BusBItemSpiMosiData:
        """Return the ``BUS:B<x>:SPI:MOSi:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MOSi:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MOSi:DATa?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:SPI:MOSi:DATa:POLarity`` command.
        """
        return self._data

    @property
    def input(self) -> BusBItemSpiMosiInput:
        """Return the ``BUS:B<x>:SPI:MOSi:INPut`` command.

        Description:
            - This command sets or queries the SPI MOSI source for the specified bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MOSi:INPut?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MOSi:INPut?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:MOSi:INPut value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:MOSi:INPut {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:SPI:MOSi:INPut?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` designates an analog channel as the source.
            - ``MATH<x>`` designates a math waveform as the source.
            - ``REF<x>`` designates a reference waveform as the source.
        """
        return self._input

    @property
    def threshold(self) -> BusBItemSpiMosiThreshold:
        """Return the ``BUS:B<x>:SPI:MOSi:THReshold`` command.

        Description:
            - This command sets or queries the SPI MOSI source thresold for the specified bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MOSi:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MOSi:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:MOSi:THReshold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:MOSi:THReshold <NR3>
            - BUS:B<x>:SPI:MOSi:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` is the SPI MOSI Data source threshold for the specified bus.
        """
        return self._threshold


class BusBItemSpiMisoThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:MISo:THReshold`` command.

    Description:
        - This command sets or queries the SPI MISo Data source threshold for the specified bus. The
          bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MISo:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MISo:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:MISo:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:MISo:THReshold <NR3>
        - BUS:B<x>:SPI:MISo:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` is the SPI MISo Data source threshold for the specified bus.
    """


class BusBItemSpiMisoInput(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:MISo:INPut`` command.

    Description:
        - This command sets or queries the SPI MISo source for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MISo:INPut?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MISo:INPut?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:MISo:INPut value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:MISo:INPut {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:SPI:MISo:INPut?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` designates an analog channel as the source.
        - ``MATH<x>`` designates a math waveform as the source.
        - ``REF<x>`` designates a reference waveform as the source.
    """


class BusBItemSpiMisoDataPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:MISo:DATa:POLarity`` command.

    Description:
        - This command sets or queries the SPI MISo Data source polarity for the specified bus. The
          bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MISo:DATa:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MISo:DATa:POLarity?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:MISo:DATa:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:MISo:DATa:POLarity {HIGH|LOW}
        - BUS:B<x>:SPI:MISo:DATa:POLarity?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``HIGH`` sets the polarity to high.
        - ``LOW`` sets the polarity to low.
    """


class BusBItemSpiMisoData(SCPICmdRead):
    """The ``BUS:B<x>:SPI:MISo:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MISo:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MISo:DATa?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:SPI:MISo:DATa:POLarity`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemSpiMisoDataPolarity(device, f"{self._cmd_syntax}:POLarity")

    @property
    def polarity(self) -> BusBItemSpiMisoDataPolarity:
        """Return the ``BUS:B<x>:SPI:MISo:DATa:POLarity`` command.

        Description:
            - This command sets or queries the SPI MISo Data source polarity for the specified bus.
              The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MISo:DATa:POLarity?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MISo:DATa:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPI:MISo:DATa:POLarity value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:MISo:DATa:POLarity {HIGH|LOW}
            - BUS:B<x>:SPI:MISo:DATa:POLarity?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``HIGH`` sets the polarity to high.
            - ``LOW`` sets the polarity to low.
        """
        return self._polarity


class BusBItemSpiMiso(SCPICmdRead):
    """The ``BUS:B<x>:SPI:MISo`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MISo?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MISo?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.data``: The ``BUS:B<x>:SPI:MISo:DATa`` command tree.
        - ``.input``: The ``BUS:B<x>:SPI:MISo:INPut`` command.
        - ``.threshold``: The ``BUS:B<x>:SPI:MISo:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._data = BusBItemSpiMisoData(device, f"{self._cmd_syntax}:DATa")
        self._input = BusBItemSpiMisoInput(device, f"{self._cmd_syntax}:INPut")
        self._threshold = BusBItemSpiMisoThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def data(self) -> BusBItemSpiMisoData:
        """Return the ``BUS:B<x>:SPI:MISo:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MISo:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MISo:DATa?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:SPI:MISo:DATa:POLarity`` command.
        """
        return self._data

    @property
    def input(self) -> BusBItemSpiMisoInput:
        """Return the ``BUS:B<x>:SPI:MISo:INPut`` command.

        Description:
            - This command sets or queries the SPI MISo source for the specified bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MISo:INPut?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MISo:INPut?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:MISo:INPut value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:MISo:INPut {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:SPI:MISo:INPut?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` designates an analog channel as the source.
            - ``MATH<x>`` designates a math waveform as the source.
            - ``REF<x>`` designates a reference waveform as the source.
        """
        return self._input

    @property
    def threshold(self) -> BusBItemSpiMisoThreshold:
        """Return the ``BUS:B<x>:SPI:MISo:THReshold`` command.

        Description:
            - This command sets or queries the SPI MISo Data source threshold for the specified bus.
              The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MISo:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MISo:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:MISo:THReshold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:MISo:THReshold <NR3>
            - BUS:B<x>:SPI:MISo:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` is the SPI MISo Data source threshold for the specified bus.
        """
        return self._threshold


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


class BusBItemSpiDataThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa:THReshold`` command.

    Description:
        - This command sets or queries the SPI Data (Data) source threshold for the specified bus.
          The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATa:THReshold <NR3>
        - BUS:B<x>:SPI:DATa:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` is the SPI Data (SDA) source threshold for the specified bus.
    """


class BusBItemSpiDataSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa:SOUrce`` command.

    Description:
        - This command sets or queries the SPI Data (Data) source for the bus number specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATa:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:SPI:DATa:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``S<x>_Ch<x>_D<x>`` specifies is the remote scope number, the analog channel and the
          digital channel.
        - ``CH<x>`` designates an analog channel as the data source for the specified SPI bus.
        - ``CH<x>_D<x>`` designates an digital channel as the bus SPI clock source.
        - ``MATH<x>`` designates a math waveform as the data source.
        - ``REF<x>`` designates a reference waveform as the data source.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the data source waveform for the
          specified SPI bus.
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


class BusBItemSpiDataPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa:POLarity`` command.

    Description:
        - This command sets or queries the SPI Data (Data) source polarity for the bus number
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATa:POLarity {HIGH|LOW}
        - BUS:B<x>:SPI:DATa:POLarity?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``HIGH`` sets the SPI data polarity to active high.
        - ``LOW`` sets the SPI data polarity to active low.
    """


class BusBItemSpiData(SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:SPI:DATa:POLarity`` command.
        - ``.size``: The ``BUS:B<x>:SPI:DATa:SIZe`` command.
        - ``.source``: The ``BUS:B<x>:SPI:DATa:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:SPI:DATa:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemSpiDataPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._size = BusBItemSpiDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._source = BusBItemSpiDataSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemSpiDataThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def polarity(self) -> BusBItemSpiDataPolarity:
        """Return the ``BUS:B<x>:SPI:DATa:POLarity`` command.

        Description:
            - This command sets or queries the SPI Data (Data) source polarity for the bus number
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:POLarity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATa:POLarity {HIGH|LOW}
            - BUS:B<x>:SPI:DATa:POLarity?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``HIGH`` sets the SPI data polarity to active high.
            - ``LOW`` sets the SPI data polarity to active low.
        """
        return self._polarity

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
    def source(self) -> BusBItemSpiDataSource:
        """Return the ``BUS:B<x>:SPI:DATa:SOUrce`` command.

        Description:
            - This command sets or queries the SPI Data (Data) source for the bus number specified
              by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATa:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:SPI:DATa:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``S<x>_Ch<x>_D<x>`` specifies is the remote scope number, the analog channel and the
              digital channel.
            - ``CH<x>`` designates an analog channel as the data source for the specified SPI bus.
            - ``CH<x>_D<x>`` designates an digital channel as the bus SPI clock source.
            - ``MATH<x>`` designates a math waveform as the data source.
            - ``REF<x>`` designates a reference waveform as the data source.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the data source waveform for
              the specified SPI bus.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemSpiDataThreshold:
        """Return the ``BUS:B<x>:SPI:DATa:THReshold`` command.

        Description:
            - This command sets or queries the SPI Data (Data) source threshold for the specified
              bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:THReshold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATa:THReshold <NR3>
            - BUS:B<x>:SPI:DATa:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` is the SPI Data (SDA) source threshold for the specified bus.
        """
        return self._threshold


class BusBItemSpiClockThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:CLOCk:THReshold`` command.

    Description:
        - This command sets or queries the SPI Clock (SCLK) source threshold for the specified bus.
          The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCk:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:CLOCk:THReshold <NR3>
        - BUS:B<x>:SPI:CLOCk:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` is the SPI Clock (SCLK) source threshold for the specified bus.
    """


class BusBItemSpiClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:CLOCk:SOUrce`` command.

    Description:
        - This command sets or queries the SPI clock (SCLK) source for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:CLOCk:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:SPI:CLOCk:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``S<x>_Ch<x>_D<x>`` specifies is the remote scope number, the analog channel and the
          digital channel.
        - ``CH<x>`` designates an analog channel as the bus SPI clock source.
        - ``CH<x>_D<x>`` designates an digital channel as the bus SPI clock source.
        - ``MATH<x>`` designates a math waveform as the clock source.
        - ``REF<x>`` designates a reference waveform as the clock source.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the clock source waveform for
          the specified SPI bus.
    """


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
        - ``.threshold``: The ``BUS:B<x>:SPI:CLOCk:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemSpiClockPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemSpiClockSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemSpiClockThreshold(device, f"{self._cmd_syntax}:THReshold")

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
            - This command sets or queries the SPI clock (SCLK) source for the specified bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCk:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:CLOCk:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:SPI:CLOCk:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``S<x>_Ch<x>_D<x>`` specifies is the remote scope number, the analog channel and the
              digital channel.
            - ``CH<x>`` designates an analog channel as the bus SPI clock source.
            - ``CH<x>_D<x>`` designates an digital channel as the bus SPI clock source.
            - ``MATH<x>`` designates a math waveform as the clock source.
            - ``REF<x>`` designates a reference waveform as the clock source.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the clock source waveform
              for the specified SPI bus.
        """  # noqa: E501
        return self._source

    @property
    def threshold(self) -> BusBItemSpiClockThreshold:
        """Return the ``BUS:B<x>:SPI:CLOCk:THReshold`` command.

        Description:
            - This command sets or queries the SPI Clock (SCLK) source threshold for the specified
              bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCk:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPI:CLOCk:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:CLOCk:THReshold <NR3>
            - BUS:B<x>:SPI:CLOCk:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` is the SPI Clock (SCLK) source threshold for the specified bus.
        """
        return self._threshold


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
        - ``.clock``: The ``BUS:B<x>:SPI:CLOCk`` command tree.
        - ``.data``: The ``BUS:B<x>:SPI:DATa`` command tree.
        - ``.framing``: The ``BUS:B<x>:SPI:FRAMING`` command.
        - ``.idletime``: The ``BUS:B<x>:SPI:IDLETime`` command.
        - ``.miso``: The ``BUS:B<x>:SPI:MISo`` command tree.
        - ``.mosi``: The ``BUS:B<x>:SPI:MOSi`` command tree.
        - ``.number``: The ``BUS:B<x>:SPI:NUMBer`` command tree.
        - ``.select``: The ``BUS:B<x>:SPI:SELect`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitorder = BusBItemSpiBitorder(device, f"{self._cmd_syntax}:BITOrder")
        self._clock = BusBItemSpiClock(device, f"{self._cmd_syntax}:CLOCk")
        self._data = BusBItemSpiData(device, f"{self._cmd_syntax}:DATa")
        self._framing = BusBItemSpiFraming(device, f"{self._cmd_syntax}:FRAMING")
        self._idletime = BusBItemSpiIdletime(device, f"{self._cmd_syntax}:IDLETime")
        self._miso = BusBItemSpiMiso(device, f"{self._cmd_syntax}:MISo")
        self._mosi = BusBItemSpiMosi(device, f"{self._cmd_syntax}:MOSi")
        self._number = BusBItemSpiNumber(device, f"{self._cmd_syntax}:NUMBer")
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
            - ``.threshold``: The ``BUS:B<x>:SPI:CLOCk:THReshold`` command.
        """
        return self._clock

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
            - ``.polarity``: The ``BUS:B<x>:SPI:DATa:POLarity`` command.
            - ``.size``: The ``BUS:B<x>:SPI:DATa:SIZe`` command.
            - ``.source``: The ``BUS:B<x>:SPI:DATa:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:SPI:DATa:THReshold`` command.
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
    def miso(self) -> BusBItemSpiMiso:
        """Return the ``BUS:B<x>:SPI:MISo`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MISo?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MISo?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.data``: The ``BUS:B<x>:SPI:MISo:DATa`` command tree.
            - ``.input``: The ``BUS:B<x>:SPI:MISo:INPut`` command.
            - ``.threshold``: The ``BUS:B<x>:SPI:MISo:THReshold`` command.
        """
        return self._miso

    @property
    def mosi(self) -> BusBItemSpiMosi:
        """Return the ``BUS:B<x>:SPI:MOSi`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MOSi?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MOSi?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.data``: The ``BUS:B<x>:SPI:MOSi:DATa`` command tree.
            - ``.input``: The ``BUS:B<x>:SPI:MOSi:INPut`` command.
            - ``.threshold``: The ``BUS:B<x>:SPI:MOSi:THReshold`` command.
        """
        return self._mosi

    @property
    def number(self) -> BusBItemSpiNumber:
        """Return the ``BUS:B<x>:SPI:NUMBer`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:NUMBer?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:NUMBer?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.inputs``: The ``BUS:B<x>:SPI:NUMBer:INputs`` command.
        """
        return self._number

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
            - ``.threshold``: The ``BUS:B<x>:SPI:SELect:THReshold`` command.
        """
        return self._select


class BusBItemSpacewireSyncValue(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPACEWIRe:SYNC:VALUe`` command.

    Description:
        - This command sets or queries sync value for sync option data.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe:SYNC:VALUe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPACEWIRe:SYNC:VALUe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPACEWIRe:SYNC:VALUe value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPACEWIRe:SYNC:VALUe <NR3>
        - BUS:B<x>:SPACEWIRe:SYNC:VALUe?
        ```

    Info:
        - ``B<x>`` is the bus number.
        - ``NR3`` specifies the sync value for sync option data.
    """


class BusBItemSpacewireSyncPattern(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPACEWIRe:SYNC:PATTern`` command.

    Description:
        - This command sets or queries sync pattern for SpaceWire decoding.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe:SYNC:PATTern?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPACEWIRe:SYNC:PATTern?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPACEWIRe:SYNC:PATTern value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPACEWIRe:SYNC:PATTern <NR3>
        - BUS:B<x>:SPACEWIRe:SYNC:PATTern?
        ```

    Info:
        - ``B<x>`` is the bus number.
        - ``NR3`` specifies the sync pattern.
    """


class BusBItemSpacewireSyncCount(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPACEWIRe:SYNC:COUnt`` command.

    Description:
        - This command sets or queries the length of the data string in bytes to be used for a
          SpaceWire sync bytes.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe:SYNC:COUnt?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPACEWIRe:SYNC:COUnt?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPACEWIRe:SYNC:COUnt value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPACEWIRe:SYNC:COUnt <NR1>
        - BUS:B<x>:SPACEWIRe:SYNC:COUnt?
        ```

    Info:
        - ``B<x>`` is the bus number.
        - ``NR1`` specifies the length of the data string in bytes. The mininum is 2 and the maximum
          is 10. The default is 2 bytes.
    """


class BusBItemSpacewireSync(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPACEWIRe:SYNC`` command.

    Description:
        - This command sets or queries sync for SpaceWire decoding.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe:SYNC?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPACEWIRe:SYNC?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPACEWIRe:SYNC value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPACEWIRe:SYNC {DATA|NULL|AUTO|CUSTom}
        - BUS:B<x>:SPACEWIRe:SYNC?
        ```

    Info:
        - ``B<x>`` is the bus number.
        - ``DATA`` specifies sync as data.
        - ``NULL`` specifies sync as null.
        - ``AUTO`` specifies sync as auto.
        - ``CUSTom`` specifies sync as custom.

    Properties:
        - ``.count``: The ``BUS:B<x>:SPACEWIRe:SYNC:COUnt`` command.
        - ``.pattern``: The ``BUS:B<x>:SPACEWIRe:SYNC:PATTern`` command.
        - ``.value``: The ``BUS:B<x>:SPACEWIRe:SYNC:VALUe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._count = BusBItemSpacewireSyncCount(device, f"{self._cmd_syntax}:COUnt")
        self._pattern = BusBItemSpacewireSyncPattern(device, f"{self._cmd_syntax}:PATTern")
        self._value = BusBItemSpacewireSyncValue(device, f"{self._cmd_syntax}:VALUe")

    @property
    def count(self) -> BusBItemSpacewireSyncCount:
        """Return the ``BUS:B<x>:SPACEWIRe:SYNC:COUnt`` command.

        Description:
            - This command sets or queries the length of the data string in bytes to be used for a
              SpaceWire sync bytes.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe:SYNC:COUnt?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPACEWIRe:SYNC:COUnt?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPACEWIRe:SYNC:COUnt value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPACEWIRe:SYNC:COUnt <NR1>
            - BUS:B<x>:SPACEWIRe:SYNC:COUnt?
            ```

        Info:
            - ``B<x>`` is the bus number.
            - ``NR1`` specifies the length of the data string in bytes. The mininum is 2 and the
              maximum is 10. The default is 2 bytes.
        """
        return self._count

    @property
    def pattern(self) -> BusBItemSpacewireSyncPattern:
        """Return the ``BUS:B<x>:SPACEWIRe:SYNC:PATTern`` command.

        Description:
            - This command sets or queries sync pattern for SpaceWire decoding.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe:SYNC:PATTern?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPACEWIRe:SYNC:PATTern?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPACEWIRe:SYNC:PATTern value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPACEWIRe:SYNC:PATTern <NR3>
            - BUS:B<x>:SPACEWIRe:SYNC:PATTern?
            ```

        Info:
            - ``B<x>`` is the bus number.
            - ``NR3`` specifies the sync pattern.
        """
        return self._pattern

    @property
    def value(self) -> BusBItemSpacewireSyncValue:
        """Return the ``BUS:B<x>:SPACEWIRe:SYNC:VALUe`` command.

        Description:
            - This command sets or queries sync value for sync option data.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe:SYNC:VALUe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPACEWIRe:SYNC:VALUe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPACEWIRe:SYNC:VALUe value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPACEWIRe:SYNC:VALUe <NR3>
            - BUS:B<x>:SPACEWIRe:SYNC:VALUe?
            ```

        Info:
            - ``B<x>`` is the bus number.
            - ``NR3`` specifies the sync value for sync option data.
        """
        return self._value


class BusBItemSpacewireStrobeThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPACEWIRe:STRobe:THReshold`` command.

    Description:
        - This command sets or queries the threshold level of the SpaceWire Strobe signal for the
          specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe:STRobe:THReshold?``
          query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPACEWIRe:STRobe:THReshold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:SPACEWIRe:STRobe:THReshold value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPACEWIRe:STRobe:THReshold <NR3>
        - BUS:B<x>:SPACEWIRe:STRobe:THReshold?
        ```

    Info:
        - ``B<x>`` is the bus number.
        - ``NR3`` specifies the SpaceWire Strobe signal threshold level for the specified bus, in
          volts.
    """


class BusBItemSpacewireStrobeSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPACEWIRe:STRobe:SOUrce`` command.

    Description:
        - This command sets or queries the source of the SpaceWire Strobe signal for the specified
          bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe:STRobe:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPACEWIRe:STRobe:SOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:SPACEWIRe:STRobe:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPACEWIRe:STRobe:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:SPACEWIRe:STRobe:SOUrce?
        ```

    Info:
        - ``B<x>`` is the bus number.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog channel as the source for the strobe signal, where <x> is
          the channel number.
        - ``MATH<x>`` specifies a math channel as the source for the strobe signal, where <x> is the
          math waveform number.
        - ``REF<x>`` specifies a reference waveform as the source for the strobe signal, where <x>
          is the reference waveform number.
    """


class BusBItemSpacewireStrobe(SCPICmdRead):
    """The ``BUS:B<x>:SPACEWIRe:STRobe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe:STRobe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPACEWIRe:STRobe?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the bus number.

    Properties:
        - ``.source``: The ``BUS:B<x>:SPACEWIRe:STRobe:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:SPACEWIRe:STRobe:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemSpacewireStrobeSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemSpacewireStrobeThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def source(self) -> BusBItemSpacewireStrobeSource:
        """Return the ``BUS:B<x>:SPACEWIRe:STRobe:SOUrce`` command.

        Description:
            - This command sets or queries the source of the SpaceWire Strobe signal for the
              specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe:STRobe:SOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:SPACEWIRe:STRobe:SOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPACEWIRe:STRobe:SOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPACEWIRe:STRobe:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:SPACEWIRe:STRobe:SOUrce?
            ```

        Info:
            - ``B<x>`` is the bus number.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog channel as the source for the strobe signal, where <x>
              is the channel number.
            - ``MATH<x>`` specifies a math channel as the source for the strobe signal, where <x> is
              the math waveform number.
            - ``REF<x>`` specifies a reference waveform as the source for the strobe signal, where
              <x> is the reference waveform number.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemSpacewireStrobeThreshold:
        """Return the ``BUS:B<x>:SPACEWIRe:STRobe:THReshold`` command.

        Description:
            - This command sets or queries the threshold level of the SpaceWire Strobe signal for
              the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe:STRobe:THReshold?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:SPACEWIRe:STRobe:THReshold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPACEWIRe:STRobe:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPACEWIRe:STRobe:THReshold <NR3>
            - BUS:B<x>:SPACEWIRe:STRobe:THReshold?
            ```

        Info:
            - ``B<x>`` is the bus number.
            - ``NR3`` specifies the SpaceWire Strobe signal threshold level for the specified bus,
              in volts.
        """
        return self._threshold


class BusBItemSpacewireDecodeType(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPACEWIRe:DECode:TYPe`` command.

    Description:
        - This command sets or queries the decode type for SpaceWire bus decode.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe:DECode:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPACEWIRe:DECode:TYPe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPACEWIRe:DECode:TYPe value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPACEWIRe:DECode:TYPe {STRObe|DATARate}
        - BUS:B<x>:SPACEWIRe:DECode:TYPe?
        ```

    Info:
        - ``B<x>`` is the bus number.
        - ``STRObe`` specifies the decode type as strobe.
        - ``DATARate`` specifies the decode type as data rate.
    """


class BusBItemSpacewireDecode(SCPICmdRead):
    """The ``BUS:B<x>:SPACEWIRe:DECode`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe:DECode?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPACEWIRe:DECode?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the bus number.

    Properties:
        - ``.type``: The ``BUS:B<x>:SPACEWIRe:DECode:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._type = BusBItemSpacewireDecodeType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def type(self) -> BusBItemSpacewireDecodeType:
        """Return the ``BUS:B<x>:SPACEWIRe:DECode:TYPe`` command.

        Description:
            - This command sets or queries the decode type for SpaceWire bus decode.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe:DECode:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPACEWIRe:DECode:TYPe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPACEWIRe:DECode:TYPe value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPACEWIRe:DECode:TYPe {STRObe|DATARate}
            - BUS:B<x>:SPACEWIRe:DECode:TYPe?
            ```

        Info:
            - ``B<x>`` is the bus number.
            - ``STRObe`` specifies the decode type as strobe.
            - ``DATARate`` specifies the decode type as data rate.
        """
        return self._type


class BusBItemSpacewireDataThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPACEWIRe:DATa:THReshold`` command.

    Description:
        - This command sets or queries the threshold of the SpaceWire Data signal for the specified
          bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe:DATa:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPACEWIRe:DATa:THReshold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:SPACEWIRe:DATa:THReshold value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPACEWIRe:DATa:THReshold <NR3>
        - BUS:B<x>:SPACEWIRe:DATa:THReshold?
        ```

    Info:
        - ``B<x>`` is the bus number.
        - ``NR3`` specifies the SpaceWire Data threshold level for the specified bus, in volts.
    """


class BusBItemSpacewireDataSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPACEWIRe:DATa:SOUrce`` command.

    Description:
        - This command sets or queries the source of the SpaceWire Data signal for the specified
          bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe:DATa:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPACEWIRe:DATa:SOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPACEWIRe:DATa:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPACEWIRe:DATa:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:SPACEWIRe:DATa:SOUrce?
        ```

    Info:
        - ``B<x>`` is the bus number.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog channel as the source for the data signal, where <x> is the
          channel number.
        - ``MATH<x>`` specifies a math channel as the source for the data signal, where <x> is the
          math waveform number.
        - ``REF<x>`` specifies a reference waveform as the source for the data signal, where <x> is
          the reference waveform number.
    """


class BusBItemSpacewireData(SCPICmdRead):
    """The ``BUS:B<x>:SPACEWIRe:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPACEWIRe:DATa?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the bus number.

    Properties:
        - ``.source``: The ``BUS:B<x>:SPACEWIRe:DATa:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:SPACEWIRe:DATa:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemSpacewireDataSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemSpacewireDataThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def source(self) -> BusBItemSpacewireDataSource:
        """Return the ``BUS:B<x>:SPACEWIRe:DATa:SOUrce`` command.

        Description:
            - This command sets or queries the source of the SpaceWire Data signal for the specified
              bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe:DATa:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPACEWIRe:DATa:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPACEWIRe:DATa:SOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPACEWIRe:DATa:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:SPACEWIRe:DATa:SOUrce?
            ```

        Info:
            - ``B<x>`` is the bus number.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog channel as the source for the data signal, where <x> is
              the channel number.
            - ``MATH<x>`` specifies a math channel as the source for the data signal, where <x> is
              the math waveform number.
            - ``REF<x>`` specifies a reference waveform as the source for the data signal, where <x>
              is the reference waveform number.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemSpacewireDataThreshold:
        """Return the ``BUS:B<x>:SPACEWIRe:DATa:THReshold`` command.

        Description:
            - This command sets or queries the threshold of the SpaceWire Data signal for the
              specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe:DATa:THReshold?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:SPACEWIRe:DATa:THReshold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPACEWIRe:DATa:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPACEWIRe:DATa:THReshold <NR3>
            - BUS:B<x>:SPACEWIRe:DATa:THReshold?
            ```

        Info:
            - ``B<x>`` is the bus number.
            - ``NR3`` specifies the SpaceWire Data threshold level for the specified bus, in volts.
        """
        return self._threshold


class BusBItemSpacewireBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPACEWIRe:BITRate`` command.

    Description:
        - This command sets or queries the SpaceWire bit rate.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPACEWIRe:BITRate?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPACEWIRe:BITRate value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPACEWIRe:BITRate <NR3>
        - BUS:B<x>:SPACEWIRe:BITRate?
        ```

    Info:
        - ``B<x>`` is the bus number.
        - ``NR3`` specifies the SpaceWire bit rate for the specified bus. The valid bit rate range
          is 2 Mbps to 200 Mbps. The default value is 10 Mbps.
    """


class BusBItemSpacewire(SCPICmdRead):
    """The ``BUS:B<x>:SPACEWIRe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPACEWIRe?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the bus number.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:SPACEWIRe:BITRate`` command.
        - ``.data``: The ``BUS:B<x>:SPACEWIRe:DATa`` command tree.
        - ``.decode``: The ``BUS:B<x>:SPACEWIRe:DECode`` command tree.
        - ``.strobe``: The ``BUS:B<x>:SPACEWIRe:STRobe`` command tree.
        - ``.sync``: The ``BUS:B<x>:SPACEWIRe:SYNC`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemSpacewireBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._data = BusBItemSpacewireData(device, f"{self._cmd_syntax}:DATa")
        self._decode = BusBItemSpacewireDecode(device, f"{self._cmd_syntax}:DECode")
        self._strobe = BusBItemSpacewireStrobe(device, f"{self._cmd_syntax}:STRobe")
        self._sync = BusBItemSpacewireSync(device, f"{self._cmd_syntax}:SYNC")

    @property
    def bitrate(self) -> BusBItemSpacewireBitrate:
        """Return the ``BUS:B<x>:SPACEWIRe:BITRate`` command.

        Description:
            - This command sets or queries the SpaceWire bit rate.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPACEWIRe:BITRate?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPACEWIRe:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPACEWIRe:BITRate <NR3>
            - BUS:B<x>:SPACEWIRe:BITRate?
            ```

        Info:
            - ``B<x>`` is the bus number.
            - ``NR3`` specifies the SpaceWire bit rate for the specified bus. The valid bit rate
              range is 2 Mbps to 200 Mbps. The default value is 10 Mbps.
        """
        return self._bitrate

    @property
    def data(self) -> BusBItemSpacewireData:
        """Return the ``BUS:B<x>:SPACEWIRe:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPACEWIRe:DATa?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the bus number.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:SPACEWIRe:DATa:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:SPACEWIRe:DATa:THReshold`` command.
        """
        return self._data

    @property
    def decode(self) -> BusBItemSpacewireDecode:
        """Return the ``BUS:B<x>:SPACEWIRe:DECode`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe:DECode?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPACEWIRe:DECode?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the bus number.

        Sub-properties:
            - ``.type``: The ``BUS:B<x>:SPACEWIRe:DECode:TYPe`` command.
        """
        return self._decode

    @property
    def strobe(self) -> BusBItemSpacewireStrobe:
        """Return the ``BUS:B<x>:SPACEWIRe:STRobe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe:STRobe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPACEWIRe:STRobe?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the bus number.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:SPACEWIRe:STRobe:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:SPACEWIRe:STRobe:THReshold`` command.
        """
        return self._strobe

    @property
    def sync(self) -> BusBItemSpacewireSync:
        """Return the ``BUS:B<x>:SPACEWIRe:SYNC`` command.

        Description:
            - This command sets or queries sync for SpaceWire decoding.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe:SYNC?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPACEWIRe:SYNC?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPACEWIRe:SYNC value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPACEWIRe:SYNC {DATA|NULL|AUTO|CUSTom}
            - BUS:B<x>:SPACEWIRe:SYNC?
            ```

        Info:
            - ``B<x>`` is the bus number.
            - ``DATA`` specifies sync as data.
            - ``NULL`` specifies sync as null.
            - ``AUTO`` specifies sync as auto.
            - ``CUSTom`` specifies sync as custom.

        Sub-properties:
            - ``.count``: The ``BUS:B<x>:SPACEWIRe:SYNC:COUnt`` command.
            - ``.pattern``: The ``BUS:B<x>:SPACEWIRe:SYNC:PATTern`` command.
            - ``.value``: The ``BUS:B<x>:SPACEWIRe:SYNC:VALUe`` command.
        """
        return self._sync


class BusBItemSmbusPecValue(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SMBUS:PEC:VALUe`` command.

    Description:
        - This command sets or queries the SMBus PEC selection for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SMBUS:PEC:VALUe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SMBUS:PEC:VALUe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SMBUS:PEC:VALUe value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SMBUS:PEC:VALUe {TRUe|FALSe}
        - BUS:B<x>:SMBUS:PEC:VALUe?
        ```

    Info:
        - ``B<x>`` is the bus number.
        - ``TRUe`` specifies the SMBus PEC selection as true.
        - ``FALSe`` specifies the SMBus PEC selection as false.
    """


class BusBItemSmbusPec(SCPICmdRead):
    """The ``BUS:B<x>:SMBUS:PEC`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SMBUS:PEC?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SMBUS:PEC?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the bus number.

    Properties:
        - ``.value``: The ``BUS:B<x>:SMBUS:PEC:VALUe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = BusBItemSmbusPecValue(device, f"{self._cmd_syntax}:VALUe")

    @property
    def value(self) -> BusBItemSmbusPecValue:
        """Return the ``BUS:B<x>:SMBUS:PEC:VALUe`` command.

        Description:
            - This command sets or queries the SMBus PEC selection for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SMBUS:PEC:VALUe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SMBUS:PEC:VALUe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SMBUS:PEC:VALUe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SMBUS:PEC:VALUe {TRUe|FALSe}
            - BUS:B<x>:SMBUS:PEC:VALUe?
            ```

        Info:
            - ``B<x>`` is the bus number.
            - ``TRUe`` specifies the SMBus PEC selection as true.
            - ``FALSe`` specifies the SMBus PEC selection as false.
        """
        return self._value


class BusBItemSmbusDataThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SMBUS:DATA:THReshold`` command.

    Description:
        - This command sets or queries the SMBUS data source threshold for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SMBUS:DATA:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SMBUS:DATA:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SMBUS:DATA:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SMBUS:DATA:THReshold <NR3>
        - BUS:B<x>:SMBUS:DATA:THReshold?
        ```

    Info:
        - ``B<x>`` is the bus number.
        - ``<NR3>`` specifies the SMBUS data threshold for the specified bus. The valid range is -8V
          to +8V.
    """


class BusBItemSmbusDataSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SMBUS:DATA:SOUrce`` command.

    Description:
        - This command sets or queries the data source for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SMBUS:DATA:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SMBUS:DATA:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SMBUS:DATA:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SMBUS:DATA:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:SMBUS:DATA:SOUrce?
        ```

    Info:
        - ``B<x>`` is the bus number.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog channel as the source for the data signal, where <x> is the
          channel number.
        - ``MATH<x>`` specifies a math channel as the source for the data signal, where <x> is the
          math waveform number.
        - ``REF<x>`` specifies a reference waveform as the source for the data signal, where <x> is
          the reference waveform number.
    """


class BusBItemSmbusData(SCPICmdRead):
    """The ``BUS:B<x>:SMBUS:DATA`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SMBUS:DATA?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SMBUS:DATA?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the bus number.

    Properties:
        - ``.source``: The ``BUS:B<x>:SMBUS:DATA:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:SMBUS:DATA:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemSmbusDataSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemSmbusDataThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def source(self) -> BusBItemSmbusDataSource:
        """Return the ``BUS:B<x>:SMBUS:DATA:SOUrce`` command.

        Description:
            - This command sets or queries the data source for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SMBUS:DATA:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SMBUS:DATA:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SMBUS:DATA:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SMBUS:DATA:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:SMBUS:DATA:SOUrce?
            ```

        Info:
            - ``B<x>`` is the bus number.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog channel as the source for the data signal, where <x> is
              the channel number.
            - ``MATH<x>`` specifies a math channel as the source for the data signal, where <x> is
              the math waveform number.
            - ``REF<x>`` specifies a reference waveform as the source for the data signal, where <x>
              is the reference waveform number.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemSmbusDataThreshold:
        """Return the ``BUS:B<x>:SMBUS:DATA:THReshold`` command.

        Description:
            - This command sets or queries the SMBUS data source threshold for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SMBUS:DATA:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SMBUS:DATA:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SMBUS:DATA:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SMBUS:DATA:THReshold <NR3>
            - BUS:B<x>:SMBUS:DATA:THReshold?
            ```

        Info:
            - ``B<x>`` is the bus number.
            - ``<NR3>`` specifies the SMBUS data threshold for the specified bus. The valid range is
              -8V to +8V.
        """
        return self._threshold


class BusBItemSmbusClockThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SMBUS:CLOCk:THReshold`` command.

    Description:
        - This command sets or queries the SMBUS clock source threshold for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SMBUS:CLOCk:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SMBUS:CLOCk:THReshold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SMBUS:CLOCk:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SMBUS:CLOCk:THReshold <NR3>
        - BUS:B<x>:SMBUS:CLOCk:THReshold?
        ```

    Info:
        - ``B<x>`` is the bus number.
        - ``<NR3>`` specifies the SMBUS clock threshold for the specified bus. The valid range is
          -8V to +8V.
    """


class BusBItemSmbusClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SMBUS:CLOCk:SOUrce`` command.

    Description:
        - This command sets or queries the clock source for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SMBUS:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SMBUS:CLOCk:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SMBUS:CLOCk:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SMBUS:CLOCk:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:SMBUS:CLOCk:SOUrce?
        ```

    Info:
        - ``B<x>`` is the bus number.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog channel as the source for the data signal, where <x> is the
          channel number.
        - ``MATH<x>`` specifies a math channel as the source for the data signal, where <x> is the
          math waveform number.
        - ``REF<x>`` specifies a reference waveform as the source for the data signal, where <x> is
          the reference waveform number.
    """


class BusBItemSmbusClock(SCPICmdRead):
    """The ``BUS:B<x>:SMBUS:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SMBUS:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SMBUS:CLOCk?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the bus number.

    Properties:
        - ``.source``: The ``BUS:B<x>:SMBUS:CLOCk:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:SMBUS:CLOCk:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemSmbusClockSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemSmbusClockThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def source(self) -> BusBItemSmbusClockSource:
        """Return the ``BUS:B<x>:SMBUS:CLOCk:SOUrce`` command.

        Description:
            - This command sets or queries the clock source for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SMBUS:CLOCk:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SMBUS:CLOCk:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SMBUS:CLOCk:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SMBUS:CLOCk:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:SMBUS:CLOCk:SOUrce?
            ```

        Info:
            - ``B<x>`` is the bus number.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog channel as the source for the data signal, where <x> is
              the channel number.
            - ``MATH<x>`` specifies a math channel as the source for the data signal, where <x> is
              the math waveform number.
            - ``REF<x>`` specifies a reference waveform as the source for the data signal, where <x>
              is the reference waveform number.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemSmbusClockThreshold:
        """Return the ``BUS:B<x>:SMBUS:CLOCk:THReshold`` command.

        Description:
            - This command sets or queries the SMBUS clock source threshold for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SMBUS:CLOCk:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SMBUS:CLOCk:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SMBUS:CLOCk:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SMBUS:CLOCk:THReshold <NR3>
            - BUS:B<x>:SMBUS:CLOCk:THReshold?
            ```

        Info:
            - ``B<x>`` is the bus number.
            - ``<NR3>`` specifies the SMBUS clock threshold for the specified bus. The valid range
              is -8V to +8V.
        """
        return self._threshold


class BusBItemSmbus(SCPICmdRead):
    """The ``BUS:B<x>:SMBUS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SMBUS?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SMBUS?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the bus number.

    Properties:
        - ``.clock``: The ``BUS:B<x>:SMBUS:CLOCk`` command tree.
        - ``.data``: The ``BUS:B<x>:SMBUS:DATA`` command tree.
        - ``.pec``: The ``BUS:B<x>:SMBUS:PEC`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._clock = BusBItemSmbusClock(device, f"{self._cmd_syntax}:CLOCk")
        self._data = BusBItemSmbusData(device, f"{self._cmd_syntax}:DATA")
        self._pec = BusBItemSmbusPec(device, f"{self._cmd_syntax}:PEC")

    @property
    def clock(self) -> BusBItemSmbusClock:
        """Return the ``BUS:B<x>:SMBUS:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SMBUS:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SMBUS:CLOCk?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the bus number.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:SMBUS:CLOCk:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:SMBUS:CLOCk:THReshold`` command.
        """
        return self._clock

    @property
    def data(self) -> BusBItemSmbusData:
        """Return the ``BUS:B<x>:SMBUS:DATA`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SMBUS:DATA?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SMBUS:DATA?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the bus number.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:SMBUS:DATA:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:SMBUS:DATA:THReshold`` command.
        """
        return self._data

    @property
    def pec(self) -> BusBItemSmbusPec:
        """Return the ``BUS:B<x>:SMBUS:PEC`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SMBUS:PEC?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SMBUS:PEC?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the bus number.

        Sub-properties:
            - ``.value``: The ``BUS:B<x>:SMBUS:PEC:VALUe`` command.
        """
        return self._pec


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


class BusBItemSentThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SENT:THRESHold`` command.

    Description:
        - This command sets or queries the SENT DATA source threshold for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:THRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:THRESHold?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:THRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SENT:THRESHold <NR3>
        - BUS:B<x>:SENT:THRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` sets the data source threshold value in volts.
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
        - BUS:B<x>:SENT:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|Math<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:SENT:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``S<x>_Ch<x>_D<x>`` specifies is the remote scope number, the analog channel and the
          digital channel.
        - ``CH<x>`` specifies an analog channel as the clock source waveform for the audio bus.
        - ``CH<x>_D<x>`` specifies a digital channel as the clock source waveform for the specified
          audio bus.
        - ``Math<x>`` specifies a math waveform as the clock source waveform for the audio bus.
        - ``REF<x>`` specifies a reference waveform as the clock source waveform for the audio bus.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the clock source waveform for
          the specified audio bus.
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
        - ``.threshold``: The ``BUS:B<x>:SENT:THRESHold`` command.
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
        self._threshold = BusBItemSentThreshold(device, f"{self._cmd_syntax}:THRESHold")
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
            - BUS:B<x>:SENT:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|Math<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:SENT:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``S<x>_Ch<x>_D<x>`` specifies is the remote scope number, the analog channel and the
              digital channel.
            - ``CH<x>`` specifies an analog channel as the clock source waveform for the audio bus.
            - ``CH<x>_D<x>`` specifies a digital channel as the clock source waveform for the
              specified audio bus.
            - ``Math<x>`` specifies a math waveform as the clock source waveform for the audio bus.
            - ``REF<x>`` specifies a reference waveform as the clock source waveform for the audio
              bus.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the clock source waveform
              for the specified audio bus.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemSentThreshold:
        """Return the ``BUS:B<x>:SENT:THRESHold`` command.

        Description:
            - This command sets or queries the SENT DATA source threshold for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:THRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:THRESHold?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:THRESHold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SENT:THRESHold <NR3>
            - BUS:B<x>:SENT:THRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` sets the data source threshold value in volts.
        """
        return self._threshold

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


class BusBItemSdlcModulo(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SDLC:MODulo`` command.

    Description:
        - This command sets or queries the SDLC Bus Modulo. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SDLC:MODulo?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SDLC:MODulo?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SDLC:MODulo value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SDLC:MODulo {8|128}
        - BUS:B<x>:SDLC:MODulo?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``8`` specifies the C-Field size is 8 bit in SDLC frame.
        - ``128`` specifies the C-Field size is 16 bit in SDLC frame.
    """


class BusBItemSdlcEncoding(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SDLC:ENCoding`` command.

    Description:
        - This command sets or queries the SDLC Bus Encoding. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SDLC:ENCoding?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SDLC:ENCoding?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SDLC:ENCoding value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SDLC:ENCoding {DISCrete|INVert}
        - BUS:B<x>:SDLC:ENCoding?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``DISCrete`` specifies the encoding mechanism is Discrete Transmission (NRZ).
        - ``INVert`` specifies that encoding mechanism is Invert On Zero i.e. NRZI.
    """


class BusBItemSdlcDataThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SDLC:DATA:THReshold`` command.

    Description:
        - This command sets or queries the SDLC data source threshold for the specified bus. The bus
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SDLC:DATA:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SDLC:DATA:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SDLC:DATA:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SDLC:DATA:THReshold <NR3>
        - BUS:B<x>:SDLC:DATA:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the SDLC Strobe threshold for the specified bus. The valid range is -8V to
          +8V.
    """


class BusBItemSdlcDataSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SDLC:DATA:SOUrce`` command.

    Description:
        - This command sets or queries the source for the specified bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SDLC:DATA:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SDLC:DATA:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SDLC:DATA:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SDLC:DATA:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:SDLC:DATA:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``MATH<x>`` specifies a math waveform as the source.
        - ``REF<x>`` specifies a digital reference waveform as the source.
    """


class BusBItemSdlcData(SCPICmdRead):
    """The ``BUS:B<x>:SDLC:DATA`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SDLC:DATA?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SDLC:DATA?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.source``: The ``BUS:B<x>:SDLC:DATA:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:SDLC:DATA:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemSdlcDataSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemSdlcDataThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def source(self) -> BusBItemSdlcDataSource:
        """Return the ``BUS:B<x>:SDLC:DATA:SOUrce`` command.

        Description:
            - This command sets or queries the source for the specified bus. The bus is specified by
              x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SDLC:DATA:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SDLC:DATA:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SDLC:DATA:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SDLC:DATA:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:SDLC:DATA:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``MATH<x>`` specifies a math waveform as the source.
            - ``REF<x>`` specifies a digital reference waveform as the source.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemSdlcDataThreshold:
        """Return the ``BUS:B<x>:SDLC:DATA:THReshold`` command.

        Description:
            - This command sets or queries the SDLC data source threshold for the specified bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SDLC:DATA:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SDLC:DATA:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SDLC:DATA:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SDLC:DATA:THReshold <NR3>
            - BUS:B<x>:SDLC:DATA:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the SDLC Strobe threshold for the specified bus. The valid range is -8V
              to +8V.
        """
        return self._threshold


class BusBItemSdlcBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SDLC:BITRate`` command.

    Description:
        - This command sets or queries the bit rate for the specified SDLC bus. The bus is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SDLC:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SDLC:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SDLC:BITRate value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SDLC:BITRate <NR1>
        - BUS:B<x>:SDLC:BITRate?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` specifies the bit rate. The default bit rate is 10 kbs and varies 300 ~
          1000000000.
    """


class BusBItemSdlc(SCPICmdRead):
    """The ``BUS:B<x>:SDLC`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SDLC?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SDLC?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:SDLC:BITRate`` command.
        - ``.data``: The ``BUS:B<x>:SDLC:DATA`` command tree.
        - ``.encoding``: The ``BUS:B<x>:SDLC:ENCoding`` command.
        - ``.modulo``: The ``BUS:B<x>:SDLC:MODulo`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemSdlcBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._data = BusBItemSdlcData(device, f"{self._cmd_syntax}:DATA")
        self._encoding = BusBItemSdlcEncoding(device, f"{self._cmd_syntax}:ENCoding")
        self._modulo = BusBItemSdlcModulo(device, f"{self._cmd_syntax}:MODulo")

    @property
    def bitrate(self) -> BusBItemSdlcBitrate:
        """Return the ``BUS:B<x>:SDLC:BITRate`` command.

        Description:
            - This command sets or queries the bit rate for the specified SDLC bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SDLC:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SDLC:BITRate?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SDLC:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SDLC:BITRate <NR1>
            - BUS:B<x>:SDLC:BITRate?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` specifies the bit rate. The default bit rate is 10 kbs and varies 300 ~
              1000000000.
        """
        return self._bitrate

    @property
    def data(self) -> BusBItemSdlcData:
        """Return the ``BUS:B<x>:SDLC:DATA`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SDLC:DATA?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SDLC:DATA?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:SDLC:DATA:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:SDLC:DATA:THReshold`` command.
        """
        return self._data

    @property
    def encoding(self) -> BusBItemSdlcEncoding:
        """Return the ``BUS:B<x>:SDLC:ENCoding`` command.

        Description:
            - This command sets or queries the SDLC Bus Encoding. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SDLC:ENCoding?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SDLC:ENCoding?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SDLC:ENCoding value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SDLC:ENCoding {DISCrete|INVert}
            - BUS:B<x>:SDLC:ENCoding?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``DISCrete`` specifies the encoding mechanism is Discrete Transmission (NRZ).
            - ``INVert`` specifies that encoding mechanism is Invert On Zero i.e. NRZI.
        """
        return self._encoding

    @property
    def modulo(self) -> BusBItemSdlcModulo:
        """Return the ``BUS:B<x>:SDLC:MODulo`` command.

        Description:
            - This command sets or queries the SDLC Bus Modulo. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SDLC:MODulo?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SDLC:MODulo?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SDLC:MODulo value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SDLC:MODulo {8|128}
            - BUS:B<x>:SDLC:MODulo?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``8`` specifies the C-Field size is 8 bit in SDLC frame.
            - ``128`` specifies the C-Field size is 16 bit in SDLC frame.
        """
        return self._modulo


class BusBItemS8b10bThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:S8B10B:THReshold`` command.

    Description:
        - This command sets or queries the 8B10b threshold for the specified bus, where the bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:S8B10B:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S8B10B:THReshold?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:S8B10B:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:S8B10B:THReshold <NR3>
        - BUS:B<x>:S8B10B:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the 8B10b Strobe threshold for the specified bus in volts. The valid range is
          -8V to +8V.
    """


class BusBItemS8b10bSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:S8B10B:SOUrce`` command.

    Description:
        - This command sets or queries the 8B10b source for the specified bus, where the bus is
          specified by x. This command specifies the source channel.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:S8B10B:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S8B10B:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:S8B10B:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:S8B10B:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:S8B10B:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``MATH<x>`` specifies a math waveform as the source.
        - ``REF<x>`` specifies a digital reference waveform as the source.
    """


class BusBItemS8b10bBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:S8B10B:BITRate`` command.

    Description:
        - This command sets or queries the 8B10b bit rate for the specified bus, where the bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:S8B10B:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S8B10B:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:S8B10B:BITRate value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:S8B10B:BITRate <NR1>
        - BUS:B<x>:S8B10B:BITRate?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` sets the bit rate for the specified bus. Arguments are the available bit rates
          up to 1 Tbps.
    """


class BusBItemS8b10b(SCPICmdRead):
    """The ``BUS:B<x>:S8B10B`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:S8B10B?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S8B10B?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:S8B10B:BITRate`` command.
        - ``.source``: The ``BUS:B<x>:S8B10B:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:S8B10B:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemS8b10bBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._source = BusBItemS8b10bSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemS8b10bThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def bitrate(self) -> BusBItemS8b10bBitrate:
        """Return the ``BUS:B<x>:S8B10B:BITRate`` command.

        Description:
            - This command sets or queries the 8B10b bit rate for the specified bus, where the bus
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:S8B10B:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S8B10B:BITRate?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:S8B10B:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:S8B10B:BITRate <NR1>
            - BUS:B<x>:S8B10B:BITRate?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` sets the bit rate for the specified bus. Arguments are the available bit
              rates up to 1 Tbps.
        """
        return self._bitrate

    @property
    def source(self) -> BusBItemS8b10bSource:
        """Return the ``BUS:B<x>:S8B10B:SOUrce`` command.

        Description:
            - This command sets or queries the 8B10b source for the specified bus, where the bus is
              specified by x. This command specifies the source channel.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:S8B10B:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S8B10B:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:S8B10B:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:S8B10B:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:S8B10B:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``MATH<x>`` specifies a math waveform as the source.
            - ``REF<x>`` specifies a digital reference waveform as the source.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemS8b10bThreshold:
        """Return the ``BUS:B<x>:S8B10B:THReshold`` command.

        Description:
            - This command sets or queries the 8B10b threshold for the specified bus, where the bus
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:S8B10B:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S8B10B:THReshold?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:S8B10B:THReshold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:S8B10B:THReshold <NR3>
            - BUS:B<x>:S8B10B:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the 8B10b Strobe threshold for the specified bus in volts. The valid
              range is -8V to +8V.
        """
        return self._threshold


class BusBItemRs232cSourceThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:SOUrce:THReshold`` command.

    Description:
        - This command sets or queries the RS-232C source threshold for the specified bus. The bus
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:SOUrce:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:SOUrce:THReshold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:RS232C:SOUrce:THReshold value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:SOUrce:THReshold <NR3>
        - BUS:B<x>:RS232C:SOUrce:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the RS-232C source threshold for the specified bus.
    """


class BusBItemRs232cSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:SOUrce`` command.

    Description:
        - This command sets or queries the RS-232C source for bus <x>, where the bus number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|REF<x>|MATH<x>|REF<x>_D<x>}
        - BUS:B<x>:RS232C:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>_D<x>`` specifies the remote scope number, the analog channel and the digital
          channel as the source.
        - ``CH<x>`` specifies an analog channel to use as the RS-232C source.
        - ``CH<x>_D<x>`` specifies a digital channel of a specified FlexChannel to use for the
          RS-232C source.
        - ``MATH<x>`` specifies a math channel to use for the RS-232C source.
        - ``REF<x>`` specifies a reference channel to use for the RS-232C source.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the source waveform for the
          specified RS-232C bus.

    Properties:
        - ``.threshold``: The ``BUS:B<x>:RS232C:SOUrce:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._threshold = BusBItemRs232cSourceThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def threshold(self) -> BusBItemRs232cSourceThreshold:
        """Return the ``BUS:B<x>:RS232C:SOUrce:THReshold`` command.

        Description:
            - This command sets or queries the RS-232C source threshold for the specified bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:SOUrce:THReshold?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:RS232C:SOUrce:THReshold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:RS232C:SOUrce:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:SOUrce:THReshold <NR3>
            - BUS:B<x>:RS232C:SOUrce:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the RS-232C source threshold for the specified bus.
        """
        return self._threshold


class BusBItemRs232cPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:POLarity`` command.

    Description:
        - This command sets or queries the RS-232C source polarity for bus <x>, where the bus number
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:POLarity?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:POLarity {NORmal|INVERTed}
        - BUS:B<x>:RS232C:POLarity?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``NORmal`` sets the RS-232C bus polarity to positive.
        - ``INVERTed`` sets the RS-232C bus polarity to negative.
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
        - This command sets or queries the RS-232C display mode for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:DISplaymode?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:DISplaymode?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:DISplaymode value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:DISplaymode {FRame|PACKET}
        - BUS:B<x>:RS232C:DISplaymode?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``FRame`` displays each frame as a single entity.
        - ``PACKET`` displays a group of frames terminated with a single frame defined by the
          ``BUS:B<x>:RS232C:DELImiter`` command.
    """


class BusBItemRs232cDelimiter(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:DELIMiter`` command.

    Description:
        - This command sets or queries the RS-232C string delimiter on bus <x>, where the bus number
          is specified by x. This command only applies when Packet view is turned On.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:DELIMiter?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:DELIMiter?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:DELIMiter value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:DELIMiter {NULl|CR|LF|SPace|XFF}
        - BUS:B<x>:RS232C:DELIMiter?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``NULl`` specifies NULL (0x00 ) delimiting value for a packet.
        - ``CR`` specifies CR (0x0D) delimiting value for a packet.
        - ``LF`` specifies LF (0x0A) delimiting value for a packet.
        - ``XFF`` specifies XFF (0xFF) delimiting value for a packet.
        - ``SPace`` specifies SPace delimiting value for a packet.
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


class BusBItemRs232cBitrateCustom(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:BITRate:CUSTom`` command.

    Description:
        - This command sets or queries the RS-232C custom bit rate for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:BITRate:CUSTom?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:BITRate:CUSTom?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:BITRate:CUSTom value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:BITRate:CUSTom <NR1>
        - BUS:B<x>:RS232C:BITRate:CUSTom?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` is the custom bit rate.
    """


class BusBItemRs232cBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:BITRate`` command.

    Description:
        - This command sets or queries the RS-232C bit rate for bus<x>, where the bus number is
          specified by x. If you select Custom, use ``BUS:BX:RS232C:BITRATE:CUSTOM`` to set the bit
          rate.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:BITRate value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:BITRate {CUSTOM|RATE300|RATE1K|RATE2K|RATE9K|RATE19K|RATE38K|RATE115K|RATE921K}
        - BUS:B<x>:RS232C:BITRate?
        ```

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.custom``: The ``BUS:B<x>:RS232C:BITRate:CUSTom`` command.
    """  # noqa: E501

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._custom = BusBItemRs232cBitrateCustom(device, f"{self._cmd_syntax}:CUSTom")

    @property
    def custom(self) -> BusBItemRs232cBitrateCustom:
        """Return the ``BUS:B<x>:RS232C:BITRate:CUSTom`` command.

        Description:
            - This command sets or queries the RS-232C custom bit rate for the specified bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:BITRate:CUSTom?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:BITRate:CUSTom?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:RS232C:BITRate:CUSTom value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:BITRate:CUSTom <NR1>
            - BUS:B<x>:RS232C:BITRate:CUSTom?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` is the custom bit rate.
        """
        return self._custom


class BusBItemRs232c(SCPICmdRead):
    """The ``BUS:B<x>:RS232C`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

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
            - This command sets or queries the RS-232C bit rate for bus<x>, where the bus number is
              specified by x. If you select Custom, use ``BUS:BX:RS232C:BITRATE:CUSTOM`` to set the
              bit rate.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:BITRate?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:BITRate {CUSTOM|RATE300|RATE1K|RATE2K|RATE9K|RATE19K|RATE38K|RATE115K|RATE921K}
            - BUS:B<x>:RS232C:BITRate?
            ```

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.custom``: The ``BUS:B<x>:RS232C:BITRate:CUSTom`` command.
        """  # noqa: E501
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
            - This command sets or queries the RS-232C string delimiter on bus <x>, where the bus
              number is specified by x. This command only applies when Packet view is turned On.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:DELIMiter?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:DELIMiter?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:DELIMiter value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:DELIMiter {NULl|CR|LF|SPace|XFF}
            - BUS:B<x>:RS232C:DELIMiter?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``NULl`` specifies NULL (0x00 ) delimiting value for a packet.
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
            - This command sets or queries the RS-232C display mode for the specified bus. The bus
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:DISplaymode?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:DISplaymode?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:DISplaymode value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:DISplaymode {FRame|PACKET}
            - BUS:B<x>:RS232C:DISplaymode?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``FRame`` displays each frame as a single entity.
            - ``PACKET`` displays a group of frames terminated with a single frame defined by the
              ``BUS:B<x>:RS232C:DELImiter`` command.
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
            - This command sets or queries the RS-232C source polarity for bus <x>, where the bus
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:POLarity?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:POLarity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:POLarity {NORmal|INVERTed}
            - BUS:B<x>:RS232C:POLarity?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``NORmal`` sets the RS-232C bus polarity to positive.
            - ``INVERTed`` sets the RS-232C bus polarity to negative.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemRs232cSource:
        """Return the ``BUS:B<x>:RS232C:SOUrce`` command.

        Description:
            - This command sets or queries the RS-232C source for bus <x>, where the bus number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|REF<x>|MATH<x>|REF<x>_D<x>}
            - BUS:B<x>:RS232C:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>_D<x>`` specifies the remote scope number, the analog channel and the
              digital channel as the source.
            - ``CH<x>`` specifies an analog channel to use as the RS-232C source.
            - ``CH<x>_D<x>`` specifies a digital channel of a specified FlexChannel to use for the
              RS-232C source.
            - ``MATH<x>`` specifies a math channel to use for the RS-232C source.
            - ``REF<x>`` specifies a reference channel to use for the RS-232C source.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the source waveform for the
              specified RS-232C bus.

        Sub-properties:
            - ``.threshold``: The ``BUS:B<x>:RS232C:SOUrce:THReshold`` command.
        """
        return self._source


class BusBItemPsifiveThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PSIFIVe:THRESHold`` command.

    Description:
        - This command sets or queries the PSI5 threshold for the Sensor To ECU specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:THRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:THRESHold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PSIFIVe:THRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PSIFIVe:THRESHold <NR3>
        - BUS:B<x>:PSIFIVe:THRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` specifies the PSI5 Strobe threshold for the specified bus. The threshold range
          is -8 V to +8 V.
    """


class BusBItemPsifiveSyncthreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PSIFIVe:SYNCTHRESHold`` command.

    Description:
        - This command sets or queries the PSI5 threshold for the ECU To Sensor specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:SYNCTHRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:SYNCTHRESHold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PSIFIVe:SYNCTHRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PSIFIVe:SYNCTHRESHold <NR3>
        - BUS:B<x>:PSIFIVe:SYNCTHRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` specifies the PSI5 Strobe threshold for the specified bus. The threshold range
          is -8 V to +8 V.
    """


class BusBItemPsifiveSyncmode(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PSIFIVe:SYNCMODe`` command.

    Description:
        - This command sets or queries the PSI5 Sync Mode.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:SYNCMODe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:SYNCMODe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PSIFIVe:SYNCMODe value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PSIFIVe:SYNCMODe {PULSEWIDTh|TOOTHGAP}
        - BUS:B<x>:PSIFIVe:SYNCMODe?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``PULSEWIDTh`` specifies the Sync Mode as Pulse Width.
        - ``TOOTHGAP`` specifies the Sync Mode as Tooth Gap.
    """


class BusBItemPsifiveStatus(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PSIFIVe:STATus`` command.

    Description:
        - This command sets or queries the optional status bits of PSI5.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:STATus?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:STATus?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PSIFIVe:STATus value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PSIFIVe:STATus <NR1>
        - BUS:B<x>:PSIFIVe:STATus?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` specifies the status value in bits. The default status value is 0 bits,
          otherwise it ranges between 0 to 2 bits.
    """


class BusBItemPsifiveSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PSIFIVe:SOUrce`` command.

    Description:
        - This command sets or queries serial channel on or off.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PSIFIVe:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PSIFIVe:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:PSIFIVe:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``MATH<x>`` specifies a math waveform as the source.
        - ``REF<x>`` specifies a digital reference waveform as the source.
    """


class BusBItemPsifiveMessaging(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PSIFIVe:MESSaging`` command.

    Description:
        - This command sets or queries the PSI5 optional messaging bits.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:MESSaging?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:MESSaging?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PSIFIVe:MESSaging value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PSIFIVe:MESSaging {OFF|ON}
        - BUS:B<x>:PSIFIVe:MESSaging?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``OFF`` specifies the messaging bits as the default value of 0.
        - ``ON`` specifies the messaging bits as 2.
    """


class BusBItemPsifiveFramecontrol(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PSIFIVe:FRAMECONTrol`` command.

    Description:
        - This command sets or queries the PSI5 frame optional control bits.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:FRAMECONTrol?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:FRAMECONTrol?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PSIFIVe:FRAMECONTrol value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PSIFIVe:FRAMECONTrol <NR1>
        - BUS:B<x>:PSIFIVe:FRAMECONTrol?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` specifies the frame control value in bits. The default frame control value is 0
          bits, otherwise it ranges between 0 to 4 bits.
    """


class BusBItemPsifiveEcusource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PSIFIVe:ECUSOURce`` command.

    Description:
        - This command sets or queries the ECU to sensor source channel for the specified Bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:ECUSOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:ECUSOURce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PSIFIVe:ECUSOURce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PSIFIVe:ECUSOURce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:PSIFIVe:ECUSOURce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``MATH<x>`` specifies a math waveform as the source.
        - ``REF<x>`` specifies a digital reference waveform as the source.
    """


class BusBItemPsifiveDataformat(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PSIFIVe:DATAFORMat`` command.

    Description:
        - This command sets or queries the data format in PSI5 Frame2 packet.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:DATAFORMat?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:DATAFORMat?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PSIFIVe:DATAFORMat value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PSIFIVe:DATAFORMat {NIBBLe|BYTe}
        - BUS:B<x>:PSIFIVe:DATAFORMat?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``NIBBLe`` specifies the data format as Nibble.
        - ``BYTe`` specifies the data format as Byte.
    """


class BusBItemPsifiveDatab(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PSIFIVe:DATAB`` command.

    Description:
        - This command sets or queries the PSI5 frame optional bits of data region B.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:DATAB?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:DATAB?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PSIFIVe:DATAB value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PSIFIVe:DATAB <NR1>
        - BUS:B<x>:PSIFIVe:DATAB?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` specifies the dataA value in bits. The default dataB value is 0 bits, otherwise
          it ranges between 0 to 12 bits.
    """


class BusBItemPsifiveDataa(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PSIFIVe:DATAA`` command.

    Description:
        - This command sets or queries the PSI5 frame mandatory data region A.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:DATAA?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:DATAA?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PSIFIVe:DATAA value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PSIFIVe:DATAA <NR1>
        - BUS:B<x>:PSIFIVe:DATAA?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` specifies the dataA value in bits. The default dataA value is 10 bits, otherwise
          it ranges between 10 to 24 bits.
    """


class BusBItemPsifiveCommDirection(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PSIFIVe:COMM:DIRection`` command.

    Description:
        - This command sets or queries the PSI5 bus communication direction. Communication direction
          by default is set to Sensor to ECU.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:COMM:DIRection?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:COMM:DIRection?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PSIFIVe:COMM:DIRection value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PSIFIVe:COMM:DIRection {SENSORECU|ECUSENSor}
        - BUS:B<x>:PSIFIVe:COMM:DIRection?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``SENSORECU`` specifies the communication direction to Sensor to ECU. This is the default
          value.
        - ``ECUSENSor`` specifies the communication direction to ECU to Sensor.
    """


class BusBItemPsifiveComm(SCPICmdRead):
    """The ``BUS:B<x>:PSIFIVe:COMM`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:COMM?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:COMM?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.direction``: The ``BUS:B<x>:PSIFIVe:COMM:DIRection`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._direction = BusBItemPsifiveCommDirection(device, f"{self._cmd_syntax}:DIRection")

    @property
    def direction(self) -> BusBItemPsifiveCommDirection:
        """Return the ``BUS:B<x>:PSIFIVe:COMM:DIRection`` command.

        Description:
            - This command sets or queries the PSI5 bus communication direction. Communication
              direction by default is set to Sensor to ECU.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:COMM:DIRection?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:COMM:DIRection?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PSIFIVe:COMM:DIRection value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PSIFIVe:COMM:DIRection {SENSORECU|ECUSENSor}
            - BUS:B<x>:PSIFIVe:COMM:DIRection?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``SENSORECU`` specifies the communication direction to Sensor to ECU. This is the
              default value.
            - ``ECUSENSor`` specifies the communication direction to ECU to Sensor.
        """
        return self._direction


class BusBItemPsifiveBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PSIFIVe:BITRate`` command.

    Description:
        - This command sets or queries the PSI5 bitrate.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PSIFIVe:BITRate value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PSIFIVe:BITRate {RATE125K|RATE189K|RATE83K}
        - BUS:B<x>:PSIFIVe:BITRate?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
    """


class BusBItemPsifiveBitperiod(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PSIFIVe:BITPERiod`` command.

    Description:
        - This command sets or queries the PSI5 Bit period bus parameter.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:BITPERiod?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:BITPERiod?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PSIFIVe:BITPERiod value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PSIFIVe:BITPERiod <NR1>
        - BUS:B<x>:PSIFIVe:BITPERiod?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` specifies the bit period. The default bit period is 60 Micro seconds.
    """


#  pylint: disable=too-many-instance-attributes
class BusBItemPsifive(SCPICmdRead):
    """The ``BUS:B<x>:PSIFIVe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.bitperiod``: The ``BUS:B<x>:PSIFIVe:BITPERiod`` command.
        - ``.bitrate``: The ``BUS:B<x>:PSIFIVe:BITRate`` command.
        - ``.comm``: The ``BUS:B<x>:PSIFIVe:COMM`` command tree.
        - ``.dataa``: The ``BUS:B<x>:PSIFIVe:DATAA`` command.
        - ``.datab``: The ``BUS:B<x>:PSIFIVe:DATAB`` command.
        - ``.dataformat``: The ``BUS:B<x>:PSIFIVe:DATAFORMat`` command.
        - ``.ecusource``: The ``BUS:B<x>:PSIFIVe:ECUSOURce`` command.
        - ``.framecontrol``: The ``BUS:B<x>:PSIFIVe:FRAMECONTrol`` command.
        - ``.messaging``: The ``BUS:B<x>:PSIFIVe:MESSaging`` command.
        - ``.source``: The ``BUS:B<x>:PSIFIVe:SOUrce`` command.
        - ``.status``: The ``BUS:B<x>:PSIFIVe:STATus`` command.
        - ``.syncmode``: The ``BUS:B<x>:PSIFIVe:SYNCMODe`` command.
        - ``.syncthreshold``: The ``BUS:B<x>:PSIFIVe:SYNCTHRESHold`` command.
        - ``.threshold``: The ``BUS:B<x>:PSIFIVe:THRESHold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitperiod = BusBItemPsifiveBitperiod(device, f"{self._cmd_syntax}:BITPERiod")
        self._bitrate = BusBItemPsifiveBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._comm = BusBItemPsifiveComm(device, f"{self._cmd_syntax}:COMM")
        self._dataa = BusBItemPsifiveDataa(device, f"{self._cmd_syntax}:DATAA")
        self._datab = BusBItemPsifiveDatab(device, f"{self._cmd_syntax}:DATAB")
        self._dataformat = BusBItemPsifiveDataformat(device, f"{self._cmd_syntax}:DATAFORMat")
        self._ecusource = BusBItemPsifiveEcusource(device, f"{self._cmd_syntax}:ECUSOURce")
        self._framecontrol = BusBItemPsifiveFramecontrol(device, f"{self._cmd_syntax}:FRAMECONTrol")
        self._messaging = BusBItemPsifiveMessaging(device, f"{self._cmd_syntax}:MESSaging")
        self._source = BusBItemPsifiveSource(device, f"{self._cmd_syntax}:SOUrce")
        self._status = BusBItemPsifiveStatus(device, f"{self._cmd_syntax}:STATus")
        self._syncmode = BusBItemPsifiveSyncmode(device, f"{self._cmd_syntax}:SYNCMODe")
        self._syncthreshold = BusBItemPsifiveSyncthreshold(
            device, f"{self._cmd_syntax}:SYNCTHRESHold"
        )
        self._threshold = BusBItemPsifiveThreshold(device, f"{self._cmd_syntax}:THRESHold")

    @property
    def bitperiod(self) -> BusBItemPsifiveBitperiod:
        """Return the ``BUS:B<x>:PSIFIVe:BITPERiod`` command.

        Description:
            - This command sets or queries the PSI5 Bit period bus parameter.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:BITPERiod?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:BITPERiod?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:PSIFIVe:BITPERiod value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PSIFIVe:BITPERiod <NR1>
            - BUS:B<x>:PSIFIVe:BITPERiod?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` specifies the bit period. The default bit period is 60 Micro seconds.
        """
        return self._bitperiod

    @property
    def bitrate(self) -> BusBItemPsifiveBitrate:
        """Return the ``BUS:B<x>:PSIFIVe:BITRate`` command.

        Description:
            - This command sets or queries the PSI5 bitrate.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:BITRate?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:PSIFIVe:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PSIFIVe:BITRate {RATE125K|RATE189K|RATE83K}
            - BUS:B<x>:PSIFIVe:BITRate?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
        """
        return self._bitrate

    @property
    def comm(self) -> BusBItemPsifiveComm:
        """Return the ``BUS:B<x>:PSIFIVe:COMM`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:COMM?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:COMM?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.direction``: The ``BUS:B<x>:PSIFIVe:COMM:DIRection`` command.
        """
        return self._comm

    @property
    def dataa(self) -> BusBItemPsifiveDataa:
        """Return the ``BUS:B<x>:PSIFIVe:DATAA`` command.

        Description:
            - This command sets or queries the PSI5 frame mandatory data region A.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:DATAA?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:DATAA?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:PSIFIVe:DATAA value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PSIFIVe:DATAA <NR1>
            - BUS:B<x>:PSIFIVe:DATAA?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` specifies the dataA value in bits. The default dataA value is 10 bits,
              otherwise it ranges between 10 to 24 bits.
        """
        return self._dataa

    @property
    def datab(self) -> BusBItemPsifiveDatab:
        """Return the ``BUS:B<x>:PSIFIVe:DATAB`` command.

        Description:
            - This command sets or queries the PSI5 frame optional bits of data region B.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:DATAB?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:DATAB?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:PSIFIVe:DATAB value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PSIFIVe:DATAB <NR1>
            - BUS:B<x>:PSIFIVe:DATAB?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` specifies the dataA value in bits. The default dataB value is 0 bits,
              otherwise it ranges between 0 to 12 bits.
        """
        return self._datab

    @property
    def dataformat(self) -> BusBItemPsifiveDataformat:
        """Return the ``BUS:B<x>:PSIFIVe:DATAFORMat`` command.

        Description:
            - This command sets or queries the data format in PSI5 Frame2 packet.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:DATAFORMat?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:DATAFORMat?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:PSIFIVe:DATAFORMat value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PSIFIVe:DATAFORMat {NIBBLe|BYTe}
            - BUS:B<x>:PSIFIVe:DATAFORMat?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``NIBBLe`` specifies the data format as Nibble.
            - ``BYTe`` specifies the data format as Byte.
        """
        return self._dataformat

    @property
    def ecusource(self) -> BusBItemPsifiveEcusource:
        """Return the ``BUS:B<x>:PSIFIVe:ECUSOURce`` command.

        Description:
            - This command sets or queries the ECU to sensor source channel for the specified Bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:ECUSOURce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:ECUSOURce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:PSIFIVe:ECUSOURce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PSIFIVe:ECUSOURce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:PSIFIVe:ECUSOURce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``MATH<x>`` specifies a math waveform as the source.
            - ``REF<x>`` specifies a digital reference waveform as the source.
        """
        return self._ecusource

    @property
    def framecontrol(self) -> BusBItemPsifiveFramecontrol:
        """Return the ``BUS:B<x>:PSIFIVe:FRAMECONTrol`` command.

        Description:
            - This command sets or queries the PSI5 frame optional control bits.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:FRAMECONTrol?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:FRAMECONTrol?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PSIFIVe:FRAMECONTrol value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PSIFIVe:FRAMECONTrol <NR1>
            - BUS:B<x>:PSIFIVe:FRAMECONTrol?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` specifies the frame control value in bits. The default frame control value
              is 0 bits, otherwise it ranges between 0 to 4 bits.
        """
        return self._framecontrol

    @property
    def messaging(self) -> BusBItemPsifiveMessaging:
        """Return the ``BUS:B<x>:PSIFIVe:MESSaging`` command.

        Description:
            - This command sets or queries the PSI5 optional messaging bits.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:MESSaging?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:MESSaging?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:PSIFIVe:MESSaging value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PSIFIVe:MESSaging {OFF|ON}
            - BUS:B<x>:PSIFIVe:MESSaging?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``OFF`` specifies the messaging bits as the default value of 0.
            - ``ON`` specifies the messaging bits as 2.
        """
        return self._messaging

    @property
    def source(self) -> BusBItemPsifiveSource:
        """Return the ``BUS:B<x>:PSIFIVe:SOUrce`` command.

        Description:
            - This command sets or queries serial channel on or off.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:PSIFIVe:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PSIFIVe:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:PSIFIVe:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``MATH<x>`` specifies a math waveform as the source.
            - ``REF<x>`` specifies a digital reference waveform as the source.
        """
        return self._source

    @property
    def status(self) -> BusBItemPsifiveStatus:
        """Return the ``BUS:B<x>:PSIFIVe:STATus`` command.

        Description:
            - This command sets or queries the optional status bits of PSI5.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:STATus?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:STATus?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:PSIFIVe:STATus value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PSIFIVe:STATus <NR1>
            - BUS:B<x>:PSIFIVe:STATus?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` specifies the status value in bits. The default status value is 0 bits,
              otherwise it ranges between 0 to 2 bits.
        """
        return self._status

    @property
    def syncmode(self) -> BusBItemPsifiveSyncmode:
        """Return the ``BUS:B<x>:PSIFIVe:SYNCMODe`` command.

        Description:
            - This command sets or queries the PSI5 Sync Mode.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:SYNCMODe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:SYNCMODe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:PSIFIVe:SYNCMODe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PSIFIVe:SYNCMODe {PULSEWIDTh|TOOTHGAP}
            - BUS:B<x>:PSIFIVe:SYNCMODe?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``PULSEWIDTh`` specifies the Sync Mode as Pulse Width.
            - ``TOOTHGAP`` specifies the Sync Mode as Tooth Gap.
        """
        return self._syncmode

    @property
    def syncthreshold(self) -> BusBItemPsifiveSyncthreshold:
        """Return the ``BUS:B<x>:PSIFIVe:SYNCTHRESHold`` command.

        Description:
            - This command sets or queries the PSI5 threshold for the ECU To Sensor specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:SYNCTHRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:SYNCTHRESHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PSIFIVe:SYNCTHRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PSIFIVe:SYNCTHRESHold <NR3>
            - BUS:B<x>:PSIFIVe:SYNCTHRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` specifies the PSI5 Strobe threshold for the specified bus. The threshold
              range is -8 V to +8 V.
        """
        return self._syncthreshold

    @property
    def threshold(self) -> BusBItemPsifiveThreshold:
        """Return the ``BUS:B<x>:PSIFIVe:THRESHold`` command.

        Description:
            - This command sets or queries the PSI5 threshold for the Sensor To ECU specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe:THRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe:THRESHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:PSIFIVe:THRESHold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PSIFIVe:THRESHold <NR3>
            - BUS:B<x>:PSIFIVe:THRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` specifies the PSI5 Strobe threshold for the specified bus. The threshold
              range is -8 V to +8 V.
        """
        return self._threshold


class BusBItemParallelClocksourceThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:CLOCkSOUrce:THReshold`` command.

    Description:
        - This command sets or queries the clock source threshold for the parallel bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCkSOUrce:THReshold?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``BUS:B<x>:PARallel:CLOCkSOUrce:THReshold?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:PARallel:CLOCkSOUrce:THReshold value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:CLOCkSOUrce:THReshold <NR3>
        - BUS:B<x>:PARallel:CLOCkSOUrce:THReshold?
        ```

    Info:
        - ``<NR3>`` is the clock bit source threshold for the parallel bus.
    """


class BusBItemParallelClocksource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:CLOCkSOUrce`` command.

    Description:
        - This command sets or queries the Parallel clock bit source for the specified bus. The bus
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCkSOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCkSOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PARallel:CLOCkSOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:CLOCkSOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>|NONE}
        - BUS:B<x>:PARallel:CLOCkSOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>_D<x>`` specifies the remote scope number, the analog channel and the digital
          channel as the source.
        - ``CH<x>`` specifies an analog FlexChannel to use as the bus clock source.
        - ``CH<x>_D<x>`` specifies a digital channel on a specified FlexChannel to use as the bus
          clock source.
        - ``MATH<x>`` specifies the math channel to use as the bus clock source.
        - ``REF<x>`` specifies the reference channel to use as the bus clock source.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the clock source waveform for
          the specified parallel bus.
        - ``NONE`` specifies the reference channel to use as the bus clock source.

    Properties:
        - ``.threshold``: The ``BUS:B<x>:PARallel:CLOCkSOUrce:THReshold`` command.
    """  # noqa: E501

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._threshold = BusBItemParallelClocksourceThreshold(
            device, f"{self._cmd_syntax}:THReshold"
        )

    @property
    def threshold(self) -> BusBItemParallelClocksourceThreshold:
        """Return the ``BUS:B<x>:PARallel:CLOCkSOUrce:THReshold`` command.

        Description:
            - This command sets or queries the clock source threshold for the parallel bus. The bus
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``BUS:B<x>:PARallel:CLOCkSOUrce:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:PARallel:CLOCkSOUrce:THReshold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PARallel:CLOCkSOUrce:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:CLOCkSOUrce:THReshold <NR3>
            - BUS:B<x>:PARallel:CLOCkSOUrce:THReshold?
            ```

        Info:
            - ``<NR3>`` is the clock bit source threshold for the parallel bus.
        """
        return self._threshold


class BusBItemParallelClockIsclocked(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:CLOCk:ISCLOCKED`` command.

    Description:
        - This command determines whether the bus operates in a clocked or asynchronous fashion. The
          bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCk:ISCLOCKED?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk:ISCLOCKED?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:PARallel:CLOCk:ISCLOCKED value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:CLOCk:ISCLOCKED {OFF|ON|NR1>
        - BUS:B<x>:PARallel:CLOCk:ISCLOCKED?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``OFF`` argument specifies an asynchronous bus.
        - ``ON`` argument specifies a clocked bus.
        - ``<NR1>`` = 0 specifies an asynchronous bus; any other value specifies a clocked bus.
    """


class BusBItemParallelClockEdge(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:CLOCk:EDGE`` command.

    Description:
        - This command sets or queries the clock edge for the parallel bus. The bus is specified by
          x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCk:EDGE?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk:EDGE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk:EDGE value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:CLOCk:EDGE {FALLING|RISING|EITHER}
        - BUS:B<x>:PARallel:CLOCk:EDGE?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``FALLING`` decodes on the falling edge of the clocked parallel bus signal.
        - ``RISING`` decodes on the rising edge of the clocked parallel bus signal.
        - ``EITHER`` decodes on the rising or falling edge of the clocked parallel bus signal.
    """


class BusBItemParallelClock(SCPICmdRead):
    """The ``BUS:B<x>:PARallel:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.edge``: The ``BUS:B<x>:PARallel:CLOCk:EDGE`` command.
        - ``.isclocked``: The ``BUS:B<x>:PARallel:CLOCk:ISCLOCKED`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._edge = BusBItemParallelClockEdge(device, f"{self._cmd_syntax}:EDGE")
        self._isclocked = BusBItemParallelClockIsclocked(device, f"{self._cmd_syntax}:ISCLOCKED")

    @property
    def edge(self) -> BusBItemParallelClockEdge:
        """Return the ``BUS:B<x>:PARallel:CLOCk:EDGE`` command.

        Description:
            - This command sets or queries the clock edge for the parallel bus. The bus is specified
              by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCk:EDGE?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk:EDGE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PARallel:CLOCk:EDGE value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:CLOCk:EDGE {FALLING|RISING|EITHER}
            - BUS:B<x>:PARallel:CLOCk:EDGE?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``FALLING`` decodes on the falling edge of the clocked parallel bus signal.
            - ``RISING`` decodes on the rising edge of the clocked parallel bus signal.
            - ``EITHER`` decodes on the rising or falling edge of the clocked parallel bus signal.
        """
        return self._edge

    @property
    def isclocked(self) -> BusBItemParallelClockIsclocked:
        """Return the ``BUS:B<x>:PARallel:CLOCk:ISCLOCKED`` command.

        Description:
            - This command determines whether the bus operates in a clocked or asynchronous fashion.
              The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCk:ISCLOCKED?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:PARallel:CLOCk:ISCLOCKED?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PARallel:CLOCk:ISCLOCKED value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:CLOCk:ISCLOCKED {OFF|ON|NR1>
            - BUS:B<x>:PARallel:CLOCk:ISCLOCKED?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``OFF`` argument specifies an asynchronous bus.
            - ``ON`` argument specifies a clocked bus.
            - ``<NR1>`` = 0 specifies an asynchronous bus; any other value specifies a clocked bus.
        """
        return self._isclocked


class BusBItemParallelBitsourceItemThreshold(SCPICmdWrite):
    """The ``BUS:B<x>:PARallel:BIT<n>SOUrce:THReshold`` command.

    Description:
        - This command sets or queries the specified bit source threshold for the specified parallel
          bus. The bus is specified by x. The bit is specified by n and is an integer in the range
          of 1 to 64.

    Usage:
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:PARallel:BIT<n>SOUrce:THReshold value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:BIT<n>SOUrce:THReshold <NR3>
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the specified bit source threshold for the specified parallel bus.
    """


class BusBItemParallelBitsourceItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:BIT<n>SOUrce`` command.

    Description:
        - This command sets or queries the specified bit source for specified parallel bus. The bus
          is specified by x. The bit is specified by n and is an integer in the range of 1 to 64.

    Usage:
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PARallel:BIT<n>SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:BIT<n>SOUrce {S<x>_Ch<x>_D|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>|NONE}
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>_D<x>`` specifies the remote scope number, the analog channel and the digital
          channel as the source.
        - ``CH<x>`` is the specified bit source.
        - ``CH<x>_D<x>`` is the specified bit source.
        - ``MATH<x>`` is the specified bit source.
        - ``REF<x>`` is the specified bit source.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the bit<x> source waveform for
          the specified parallel bus.
        - ``NONE`` disables the bit source.

    Properties:
        - ``.threshold``: The ``BUS:B<x>:PARallel:BIT<n>SOUrce:THReshold`` command.
    """  # noqa: E501

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._threshold = BusBItemParallelBitsourceItemThreshold(
            device, f"{self._cmd_syntax}:THReshold"
        )

    @property
    def threshold(self) -> BusBItemParallelBitsourceItemThreshold:
        """Return the ``BUS:B<x>:PARallel:BIT<n>SOUrce:THReshold`` command.

        Description:
            - This command sets or queries the specified bit source threshold for the specified
              parallel bus. The bus is specified by x. The bit is specified by n and is an integer
              in the range of 1 to 64.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PARallel:BIT<n>SOUrce:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:BIT<n>SOUrce:THReshold <NR3>
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the specified bit source threshold for the specified parallel bus.
        """
        return self._threshold


class BusBItemParallelAllthresholdsApply(SCPICmdWriteNoArguments):
    """The ``BUS:B<x>:PARallel:ALLTHResholds:APPly`` command.

    Description:
        - This command sets all of the data source thresholds to the value set by
          ``BUS:BX:PARALLEL:ALLTHRESHOLDS`` for the parallel bus. The bus is specified by x.

    Usage:
        - Using the ``.write()`` method will send the ``BUS:B<x>:PARallel:ALLTHResholds:APPly``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:ALLTHResholds:APPly
        ```

    Info:
        - ``B<x>`` is the Bus number.
    """


class BusBItemParallelAllthresholds(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:ALLTHResholds`` command.

    Description:
        - This command sets or queries a threshold value for sources for the parallel bus. Use the
          ``BUS:BX:PARALLEL:ALLTHRESHOLDS:APPLY`` command to set the thresholds to this value. The
          bus is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PARallel:ALLTHResholds value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:ALLTHResholds <NR3>
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the source threshold.

    Properties:
        - ``.apply``: The ``BUS:B<x>:PARallel:ALLTHResholds:APPly`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._apply = BusBItemParallelAllthresholdsApply(device, f"{self._cmd_syntax}:APPly")

    @property
    def apply(self) -> BusBItemParallelAllthresholdsApply:
        """Return the ``BUS:B<x>:PARallel:ALLTHResholds:APPly`` command.

        Description:
            - This command sets all of the data source thresholds to the value set by
              ``BUS:BX:PARALLEL:ALLTHRESHOLDS`` for the parallel bus. The bus is specified by x.

        Usage:
            - Using the ``.write()`` method will send the ``BUS:B<x>:PARallel:ALLTHResholds:APPly``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:ALLTHResholds:APPly
            ```

        Info:
            - ``B<x>`` is the Bus number.
        """
        return self._apply


class BusBItemParallel(SCPICmdRead):
    """The ``BUS:B<x>:PARallel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.allthresholds``: The ``BUS:B<x>:PARallel:ALLTHResholds`` command.
        - ``.bitsource``: The ``BUS:B<x>:PARallel:BIT<n>SOUrce`` command.
        - ``.clock``: The ``BUS:B<x>:PARallel:CLOCk`` command tree.
        - ``.clocksource``: The ``BUS:B<x>:PARallel:CLOCkSOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._allthresholds = BusBItemParallelAllthresholds(
            device, f"{self._cmd_syntax}:ALLTHResholds"
        )
        self._bitsource: Dict[int, BusBItemParallelBitsourceItem] = DefaultDictPassKeyToFactory(
            lambda x: BusBItemParallelBitsourceItem(device, f"{self._cmd_syntax}:BIT{x}SOUrce")
        )
        self._clock = BusBItemParallelClock(device, f"{self._cmd_syntax}:CLOCk")
        self._clocksource = BusBItemParallelClocksource(device, f"{self._cmd_syntax}:CLOCkSOUrce")

    @property
    def allthresholds(self) -> BusBItemParallelAllthresholds:
        """Return the ``BUS:B<x>:PARallel:ALLTHResholds`` command.

        Description:
            - This command sets or queries a threshold value for sources for the parallel bus. Use
              the ``BUS:BX:PARALLEL:ALLTHRESHOLDS:APPLY`` command to set the thresholds to this
              value. The bus is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PARallel:ALLTHResholds value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:ALLTHResholds <NR3>
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the source threshold.

        Sub-properties:
            - ``.apply``: The ``BUS:B<x>:PARallel:ALLTHResholds:APPly`` command.
        """
        return self._allthresholds

    @property
    def bitsource(self) -> Dict[int, BusBItemParallelBitsourceItem]:
        """Return the ``BUS:B<x>:PARallel:BIT<n>SOUrce`` command.

        Description:
            - This command sets or queries the specified bit source for specified parallel bus. The
              bus is specified by x. The bit is specified by n and is an integer in the range of 1
              to 64.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PARallel:BIT<n>SOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:BIT<n>SOUrce {S<x>_Ch<x>_D|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>|NONE}
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>_D<x>`` specifies the remote scope number, the analog channel and the
              digital channel as the source.
            - ``CH<x>`` is the specified bit source.
            - ``CH<x>_D<x>`` is the specified bit source.
            - ``MATH<x>`` is the specified bit source.
            - ``REF<x>`` is the specified bit source.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the bit<x> source waveform
              for the specified parallel bus.
            - ``NONE`` disables the bit source.

        Sub-properties:
            - ``.threshold``: The ``BUS:B<x>:PARallel:BIT<n>SOUrce:THReshold`` command.
        """  # noqa: E501
        return self._bitsource

    @property
    def clock(self) -> BusBItemParallelClock:
        """Return the ``BUS:B<x>:PARallel:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.edge``: The ``BUS:B<x>:PARallel:CLOCk:EDGE`` command.
            - ``.isclocked``: The ``BUS:B<x>:PARallel:CLOCk:ISCLOCKED`` command.
        """
        return self._clock

    @property
    def clocksource(self) -> BusBItemParallelClocksource:
        """Return the ``BUS:B<x>:PARallel:CLOCkSOUrce`` command.

        Description:
            - This command sets or queries the Parallel clock bit source for the specified bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCkSOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCkSOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PARallel:CLOCkSOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:CLOCkSOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>|NONE}
            - BUS:B<x>:PARallel:CLOCkSOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>_D<x>`` specifies the remote scope number, the analog channel and the
              digital channel as the source.
            - ``CH<x>`` specifies an analog FlexChannel to use as the bus clock source.
            - ``CH<x>_D<x>`` specifies a digital channel on a specified FlexChannel to use as the
              bus clock source.
            - ``MATH<x>`` specifies the math channel to use as the bus clock source.
            - ``REF<x>`` specifies the reference channel to use as the bus clock source.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the clock source waveform
              for the specified parallel bus.
            - ``NONE`` specifies the reference channel to use as the bus clock source.

        Sub-properties:
            - ``.threshold``: The ``BUS:B<x>:PARallel:CLOCkSOUrce:THReshold`` command.
        """  # noqa: E501
        return self._clocksource


class BusBItemOnewireMode(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ONEWIRe:MODe`` command.

    Description:
        - This command sets or queries the mode for the specified ONEWIRe bus. The bus number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ONEWIRe:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ONEWIRe:MODe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ONEWIRe:MODe value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ONEWIRe:MODe {STAndard|OVErdrive}
        - BUS:B<x>:ONEWIRe:MODe?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``STAndard`` specifies the mode as standard. Standard is the default mode whose value is
          15.4 kbs.
        - ``OVErdrive`` specifies the mode as overdrive.
    """


class BusBItemOnewireDataThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ONEWIRe:DATA:THReshold`` command.

    Description:
        - This command sets or queries the ONEWIRe data source threshold for the specified bus. The
          bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ONEWIRe:DATA:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ONEWIRe:DATA:THReshold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ONEWIRe:DATA:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ONEWIRe:DATA:THReshold <NR3>
        - BUS:B<x>:ONEWIRe:DATA:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the ONEWIRe Strobe threshold for the specified bus in volts. The valid range
          is -8 V to +8 V. The default value is 1.25 V.
    """


class BusBItemOnewireDataSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ONEWIRe:DATA:SOUrce`` command.

    Description:
        - This command sets or queries the ONEWIRe source for the specified bus. This command
          specifies the source channel. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ONEWIRe:DATA:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ONEWIRe:DATA:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ONEWIRe:DATA:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ONEWIRe:DATA:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>]
        - BUS:B<x>:ONEWIRe:DATA:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``MATH<x>`` specifies a math waveform as the source.
        - ``REF<x>`` specifies a digital reference waveform as the source.
    """


class BusBItemOnewireData(SCPICmdRead):
    """The ``BUS:B<x>:ONEWIRe:DATA`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ONEWIRe:DATA?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ONEWIRe:DATA?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.source``: The ``BUS:B<x>:ONEWIRe:DATA:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:ONEWIRe:DATA:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemOnewireDataSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemOnewireDataThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def source(self) -> BusBItemOnewireDataSource:
        """Return the ``BUS:B<x>:ONEWIRe:DATA:SOUrce`` command.

        Description:
            - This command sets or queries the ONEWIRe source for the specified bus. This command
              specifies the source channel. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ONEWIRe:DATA:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ONEWIRe:DATA:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ONEWIRe:DATA:SOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ONEWIRe:DATA:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>]
            - BUS:B<x>:ONEWIRe:DATA:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``MATH<x>`` specifies a math waveform as the source.
            - ``REF<x>`` specifies a digital reference waveform as the source.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemOnewireDataThreshold:
        """Return the ``BUS:B<x>:ONEWIRe:DATA:THReshold`` command.

        Description:
            - This command sets or queries the ONEWIRe data source threshold for the specified bus.
              The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ONEWIRe:DATA:THReshold?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ONEWIRe:DATA:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ONEWIRe:DATA:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ONEWIRe:DATA:THReshold <NR3>
            - BUS:B<x>:ONEWIRe:DATA:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the ONEWIRe Strobe threshold for the specified bus in volts. The valid
              range is -8 V to +8 V. The default value is 1.25 V.
        """
        return self._threshold


class BusBItemOnewire(SCPICmdRead):
    """The ``BUS:B<x>:ONEWIRe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ONEWIRe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ONEWIRe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.data``: The ``BUS:B<x>:ONEWIRe:DATA`` command tree.
        - ``.mode``: The ``BUS:B<x>:ONEWIRe:MODe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._data = BusBItemOnewireData(device, f"{self._cmd_syntax}:DATA")
        self._mode = BusBItemOnewireMode(device, f"{self._cmd_syntax}:MODe")

    @property
    def data(self) -> BusBItemOnewireData:
        """Return the ``BUS:B<x>:ONEWIRe:DATA`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ONEWIRe:DATA?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ONEWIRe:DATA?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:ONEWIRe:DATA:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:ONEWIRe:DATA:THReshold`` command.
        """
        return self._data

    @property
    def mode(self) -> BusBItemOnewireMode:
        """Return the ``BUS:B<x>:ONEWIRe:MODe`` command.

        Description:
            - This command sets or queries the mode for the specified ONEWIRe bus. The bus number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ONEWIRe:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ONEWIRe:MODe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:ONEWIRe:MODe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ONEWIRe:MODe {STAndard|OVErdrive}
            - BUS:B<x>:ONEWIRe:MODe?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``STAndard`` specifies the mode as standard. Standard is the default mode whose value
              is 15.4 kbs.
            - ``OVErdrive`` specifies the mode as overdrive.
        """
        return self._mode


class BusBItemNrzThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:NRZ:THReshold`` command.

    Description:
        - This command sets or queries the NRZ threshold for the specified bus. The bus number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:NRZ:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:NRZ:THReshold?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:NRZ:THReshold value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:NRZ:THReshold <NR3>
        - BUS:B<x>:NRZ:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the NRZ Strobe threshold for the specified bus in volts. The valid range is
          -8 V to +8 V.
    """


class BusBItemNrzSpmiVersion(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:NRZ:SPMI:VERsion`` command.

    Description:
        - This command sets or queries the Version for the specified bus. The bus number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:NRZ:SPMI:VERsion?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:NRZ:SPMI:VERsion?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:NRZ:SPMI:VERsion value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:NRZ:SPMI:VERsion {v<x>}
        - BUS:B<x>:NRZ:SPMI:VERsion?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``v1`` specifies version 1.
        - ``v2`` specifies version 2.
    """


class BusBItemNrzSpmi(SCPICmdRead):
    """The ``BUS:B<x>:NRZ:SPMI`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:NRZ:SPMI?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:NRZ:SPMI?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.version``: The ``BUS:B<x>:NRZ:SPMI:VERsion`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._version = BusBItemNrzSpmiVersion(device, f"{self._cmd_syntax}:VERsion")

    @property
    def version(self) -> BusBItemNrzSpmiVersion:
        """Return the ``BUS:B<x>:NRZ:SPMI:VERsion`` command.

        Description:
            - This command sets or queries the Version for the specified bus. The bus number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:NRZ:SPMI:VERsion?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:NRZ:SPMI:VERsion?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:NRZ:SPMI:VERsion value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:NRZ:SPMI:VERsion {v<x>}
            - BUS:B<x>:NRZ:SPMI:VERsion?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``v1`` specifies version 1.
            - ``v2`` specifies version 2.
        """
        return self._version


class BusBItemNrzSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:NRZ:SOUrce`` command.

    Description:
        - This command sets or queries the NRZ source for the specified bus. This command specifies
          the source channel. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:NRZ:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:NRZ:SOUrce?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:NRZ:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:NRZ:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>]
        - BUS:B<x>:NRZ:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``MATH<x>`` specifies a math waveform as the source.
        - ``REF<x>`` specifies a digital reference waveform as the source.
    """


class BusBItemNrzPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:NRZ:POLarity`` command.

    Description:
        - This command sets or queries the NRZ source polarity for the specified bus. The bus number
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:NRZ:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:NRZ:POLarity?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:NRZ:POLarity value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:NRZ:POLarity {INVerted|NORmal}
        - BUS:B<x>:NRZ:POLarity?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``INVerted`` specifies inverted polarity.
        - ``NORmal`` specifies normal polarity.
    """


class BusBItemNrzBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:NRZ:BITRate`` command.

    Description:
        - This command sets or queries the NRZ bus bit rate. The bus number is specified by <x>.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:NRZ:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:NRZ:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:NRZ:BITRate value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:NRZ:BITRate <NR1>
        - BUS:B<x>:NRZ:BITRate?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` sets the bit rate up to 1 G.
    """


class BusBItemNrzBitorder(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:NRZ:BITOrder`` command.

    Description:
        - This command sets or queries the NRZ bit order for the specified bus. The bus is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:NRZ:BITOrder?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:NRZ:BITOrder?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:NRZ:BITOrder value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:NRZ:BITOrder {LSB|MSB}
        - BUS:B<x>:NRZ:BITOrder?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``LSB`` specifies that each bit becomes the recovered value's new LSB, after shifting
          previously recovered bits one place to the left. The decoding happens right to left.
        - ``MSB`` specifies that each successive bit from the bus's data line becomes the new MSB of
          the recovered value, shifting any previously recovered bits one place to the right. The
          decoding happens left to right.
    """


class BusBItemNrz(SCPICmdRead):
    """The ``BUS:B<x>:NRZ`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:NRZ?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:NRZ?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.bitorder``: The ``BUS:B<x>:NRZ:BITOrder`` command.
        - ``.bitrate``: The ``BUS:B<x>:NRZ:BITRate`` command.
        - ``.polarity``: The ``BUS:B<x>:NRZ:POLarity`` command.
        - ``.source``: The ``BUS:B<x>:NRZ:SOUrce`` command.
        - ``.spmi``: The ``BUS:B<x>:NRZ:SPMI`` command tree.
        - ``.threshold``: The ``BUS:B<x>:NRZ:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitorder = BusBItemNrzBitorder(device, f"{self._cmd_syntax}:BITOrder")
        self._bitrate = BusBItemNrzBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._polarity = BusBItemNrzPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemNrzSource(device, f"{self._cmd_syntax}:SOUrce")
        self._spmi = BusBItemNrzSpmi(device, f"{self._cmd_syntax}:SPMI")
        self._threshold = BusBItemNrzThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def bitorder(self) -> BusBItemNrzBitorder:
        """Return the ``BUS:B<x>:NRZ:BITOrder`` command.

        Description:
            - This command sets or queries the NRZ bit order for the specified bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:NRZ:BITOrder?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:NRZ:BITOrder?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:NRZ:BITOrder value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:NRZ:BITOrder {LSB|MSB}
            - BUS:B<x>:NRZ:BITOrder?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``LSB`` specifies that each bit becomes the recovered value's new LSB, after shifting
              previously recovered bits one place to the left. The decoding happens right to left.
            - ``MSB`` specifies that each successive bit from the bus's data line becomes the new
              MSB of the recovered value, shifting any previously recovered bits one place to the
              right. The decoding happens left to right.
        """
        return self._bitorder

    @property
    def bitrate(self) -> BusBItemNrzBitrate:
        """Return the ``BUS:B<x>:NRZ:BITRate`` command.

        Description:
            - This command sets or queries the NRZ bus bit rate. The bus number is specified by <x>.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:NRZ:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:NRZ:BITRate?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:NRZ:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:NRZ:BITRate <NR1>
            - BUS:B<x>:NRZ:BITRate?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` sets the bit rate up to 1 G.
        """
        return self._bitrate

    @property
    def polarity(self) -> BusBItemNrzPolarity:
        """Return the ``BUS:B<x>:NRZ:POLarity`` command.

        Description:
            - This command sets or queries the NRZ source polarity for the specified bus. The bus
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:NRZ:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:NRZ:POLarity?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:NRZ:POLarity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:NRZ:POLarity {INVerted|NORmal}
            - BUS:B<x>:NRZ:POLarity?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``INVerted`` specifies inverted polarity.
            - ``NORmal`` specifies normal polarity.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemNrzSource:
        """Return the ``BUS:B<x>:NRZ:SOUrce`` command.

        Description:
            - This command sets or queries the NRZ source for the specified bus. This command
              specifies the source channel. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:NRZ:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:NRZ:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:NRZ:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:NRZ:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>]
            - BUS:B<x>:NRZ:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``MATH<x>`` specifies a math waveform as the source.
            - ``REF<x>`` specifies a digital reference waveform as the source.
        """
        return self._source

    @property
    def spmi(self) -> BusBItemNrzSpmi:
        """Return the ``BUS:B<x>:NRZ:SPMI`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:NRZ:SPMI?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:NRZ:SPMI?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.version``: The ``BUS:B<x>:NRZ:SPMI:VERsion`` command.
        """
        return self._spmi

    @property
    def threshold(self) -> BusBItemNrzThreshold:
        """Return the ``BUS:B<x>:NRZ:THReshold`` command.

        Description:
            - This command sets or queries the NRZ threshold for the specified bus. The bus number
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:NRZ:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:NRZ:THReshold?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:NRZ:THReshold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:NRZ:THReshold <NR3>
            - BUS:B<x>:NRZ:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the NRZ Strobe threshold for the specified bus in volts. The valid range
              is -8 V to +8 V.
        """
        return self._threshold


class BusBItemMil1553bThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MIL1553B:THRESHold`` command.

    Description:
        - This command sets or queries the MIL-STD-1553 upper threshold for the specified bus. The
          bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIL1553B:THRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIL1553B:THRESHold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:MIL1553B:THRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MIL1553B:THRESHold <NR3>
        - BUS:B<x>:MIL1553B:THRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the MIL-STD-1553 upper threshold for the specified bus.
    """


class BusBItemMil1553bSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MIL1553B:SOUrce`` command.

    Description:
        - This command sets or queries the source for the specified MIL-STD-1553 bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIL1553B:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIL1553B:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:MIL1553B:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MIL1553B:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:MIL1553B:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog channel as the source waveform for the MIL-STD-1553 bus.
        - ``Math<x>`` specifies a math waveform as the source waveform for the MIL-STD-1553 bus.
        - ``REF<x>`` specifies a reference waveform as the source waveform for the MIL-STD-1553 bus.
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


class BusBItemMil1553bLowthreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MIL1553B:LOWTHRESHold`` command.

    Description:
        - This command sets or queries the MIL-STD-1553 lower threshold for the specified bus. The
          bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MIL1553B:LOWTHRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIL1553B:LOWTHRESHold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:MIL1553B:LOWTHRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MIL1553B:LOWTHRESHold <NR3>
        - BUS:B<x>:MIL1553B:LOWTHRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the MIL-STD-1553 lower threshold for the specified bus.
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
        - ``.lowthreshold``: The ``BUS:B<x>:MIL1553B:LOWTHRESHold`` command.
        - ``.polarity``: The ``BUS:B<x>:MIL1553B:POLarity`` command.
        - ``.responsetime``: The ``BUS:B<x>:MIL1553B:RESPonsetime`` command tree.
        - ``.source``: The ``BUS:B<x>:MIL1553B:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:MIL1553B:THRESHold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._lowthreshold = BusBItemMil1553bLowthreshold(
            device, f"{self._cmd_syntax}:LOWTHRESHold"
        )
        self._polarity = BusBItemMil1553bPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._responsetime = BusBItemMil1553bResponsetime(
            device, f"{self._cmd_syntax}:RESPonsetime"
        )
        self._source = BusBItemMil1553bSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemMil1553bThreshold(device, f"{self._cmd_syntax}:THRESHold")

    @property
    def lowthreshold(self) -> BusBItemMil1553bLowthreshold:
        """Return the ``BUS:B<x>:MIL1553B:LOWTHRESHold`` command.

        Description:
            - This command sets or queries the MIL-STD-1553 lower threshold for the specified bus.
              The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MIL1553B:LOWTHRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIL1553B:LOWTHRESHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MIL1553B:LOWTHRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MIL1553B:LOWTHRESHold <NR3>
            - BUS:B<x>:MIL1553B:LOWTHRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the MIL-STD-1553 lower threshold for the specified bus.
        """
        return self._lowthreshold

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
            - This command sets or queries the source for the specified MIL-STD-1553 bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MIL1553B:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIL1553B:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:MIL1553B:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MIL1553B:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:MIL1553B:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog channel as the source waveform for the MIL-STD-1553 bus.
            - ``Math<x>`` specifies a math waveform as the source waveform for the MIL-STD-1553 bus.
            - ``REF<x>`` specifies a reference waveform as the source waveform for the MIL-STD-1553
              bus.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemMil1553bThreshold:
        """Return the ``BUS:B<x>:MIL1553B:THRESHold`` command.

        Description:
            - This command sets or queries the MIL-STD-1553 upper threshold for the specified bus.
              The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MIL1553B:THRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MIL1553B:THRESHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:MIL1553B:THRESHold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MIL1553B:THRESHold <NR3>
            - BUS:B<x>:MIL1553B:THRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the MIL-STD-1553 upper threshold for the specified bus.
        """
        return self._threshold


class BusBItemMdioDataThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MDIO:DATA:THReshold`` command.

    Description:
        - This command sets or queries the MDIO Data source threshold for the specified bus. The bus
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MDIO:DATA:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MDIO:DATA:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:MDIO:DATA:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MDIO:DATA:THReshold <NR3>
        - BUS:B<x>:MDIO:DATA:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the data source threshold for the specified bus. The argument range is -8V to
          +8V.
    """


class BusBItemMdioDataSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MDIO:DATA:SOUrce`` command.

    Description:
        - This command sets or queries the data for the specified bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MDIO:DATA:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MDIO:DATA:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:MDIO:DATA:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MDIO:DATA:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:MDIO:DATA:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog channel as the data source.
        - ``Math<x>`` specifies a math waveform as the data source.
        - ``REF<x>`` specifies a reference waveform as the data source.
    """


class BusBItemMdioData(SCPICmdRead):
    """The ``BUS:B<x>:MDIO:DATA`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MDIO:DATA?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MDIO:DATA?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.source``: The ``BUS:B<x>:MDIO:DATA:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:MDIO:DATA:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemMdioDataSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemMdioDataThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def source(self) -> BusBItemMdioDataSource:
        """Return the ``BUS:B<x>:MDIO:DATA:SOUrce`` command.

        Description:
            - This command sets or queries the data for the specified bus. The bus is specified by
              x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MDIO:DATA:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MDIO:DATA:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:MDIO:DATA:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MDIO:DATA:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:MDIO:DATA:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog channel as the data source.
            - ``Math<x>`` specifies a math waveform as the data source.
            - ``REF<x>`` specifies a reference waveform as the data source.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemMdioDataThreshold:
        """Return the ``BUS:B<x>:MDIO:DATA:THReshold`` command.

        Description:
            - This command sets or queries the MDIO Data source threshold for the specified bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MDIO:DATA:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MDIO:DATA:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MDIO:DATA:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MDIO:DATA:THReshold <NR3>
            - BUS:B<x>:MDIO:DATA:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the data source threshold for the specified bus. The argument range is
              -8V to +8V.
        """
        return self._threshold


class BusBItemMdioClockThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MDIO:CLOCk:THReshold`` command.

    Description:
        - This command sets or queries the MDIO clock source threshold for the specified bus. The
          bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MDIO:CLOCk:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MDIO:CLOCk:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:MDIO:CLOCk:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MDIO:CLOCk:THReshold <NR3>
        - BUS:B<x>:MDIO:CLOCk:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the clock source threshold for the specified bus. The argument range is -8V
          to +8V.
    """


class BusBItemMdioClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MDIO:CLOCk:SOUrce`` command.

    Description:
        - This command sets or queries the MDIO Clock source for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MDIO:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MDIO:CLOCk:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:MDIO:CLOCk:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MDIO:CLOCk:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:MDIO:CLOCk:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog channel as the Clock source.
        - ``Math<x>`` specifies a math waveform as the Clock source.
        - ``REF<x>`` specifies a reference waveform as the Clock source.
    """


class BusBItemMdioClock(SCPICmdRead):
    """The ``BUS:B<x>:MDIO:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MDIO:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MDIO:CLOCk?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.source``: The ``BUS:B<x>:MDIO:CLOCk:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:MDIO:CLOCk:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemMdioClockSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemMdioClockThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def source(self) -> BusBItemMdioClockSource:
        """Return the ``BUS:B<x>:MDIO:CLOCk:SOUrce`` command.

        Description:
            - This command sets or queries the MDIO Clock source for the specified bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MDIO:CLOCk:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MDIO:CLOCk:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:MDIO:CLOCk:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MDIO:CLOCk:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:MDIO:CLOCk:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog channel as the Clock source.
            - ``Math<x>`` specifies a math waveform as the Clock source.
            - ``REF<x>`` specifies a reference waveform as the Clock source.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemMdioClockThreshold:
        """Return the ``BUS:B<x>:MDIO:CLOCk:THReshold`` command.

        Description:
            - This command sets or queries the MDIO clock source threshold for the specified bus.
              The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MDIO:CLOCk:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MDIO:CLOCk:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MDIO:CLOCk:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MDIO:CLOCk:THReshold <NR3>
            - BUS:B<x>:MDIO:CLOCk:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the clock source threshold for the specified bus. The argument range is
              -8V to +8V.
        """
        return self._threshold


class BusBItemMdio(SCPICmdRead):
    """The ``BUS:B<x>:MDIO`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MDIO?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MDIO?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.clock``: The ``BUS:B<x>:MDIO:CLOCk`` command tree.
        - ``.data``: The ``BUS:B<x>:MDIO:DATA`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._clock = BusBItemMdioClock(device, f"{self._cmd_syntax}:CLOCk")
        self._data = BusBItemMdioData(device, f"{self._cmd_syntax}:DATA")

    @property
    def clock(self) -> BusBItemMdioClock:
        """Return the ``BUS:B<x>:MDIO:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MDIO:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MDIO:CLOCk?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:MDIO:CLOCk:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:MDIO:CLOCk:THReshold`` command.
        """
        return self._clock

    @property
    def data(self) -> BusBItemMdioData:
        """Return the ``BUS:B<x>:MDIO:DATA`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MDIO:DATA?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MDIO:DATA?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:MDIO:DATA:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:MDIO:DATA:THReshold`` command.
        """
        return self._data


class BusBItemManchesterParity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MANChester:parity`` command.

    Description:
        - This command sets or queries the Manchester bus Parity. The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:parity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:parity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:MANChester:parity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MANChester:parity {ODD|EVEN|NONE}
        - BUS:B<x>:MANChester:parity?
        ```

    Info:
        - ``ODD`` sets the number of 1's to odd.
        - ``EVEN`` sets the number of 1's to even.
        - ``NONE`` specifies that Parity is not considered.
    """


class BusBItemManchesterWordsize(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MANChester:WORDSIZe`` command.

    Description:
        - This command sets or queries the Manchester word size in bits. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:WORDSIZe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:WORDSIZe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:MANChester:WORDSIZe value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MANChester:WORDSIZe <NR1>
        - BUS:B<x>:MANChester:WORDSIZe?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` sets the word size in bits.
    """


class BusBItemManchesterWordCount(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MANChester:WORD:COUNt`` command.

    Description:
        - This command sets or queries the Manchester word count in bits. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:WORD:COUNt?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:WORD:COUNt?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:MANChester:WORD:COUNt value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MANChester:WORD:COUNt <NR1>
        - BUS:B<x>:MANChester:WORD:COUNt?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` sets the word count in bits.
    """


class BusBItemManchesterWord(SCPICmdRead):
    """The ``BUS:B<x>:MANChester:WORD`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:WORD?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:WORD?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.count``: The ``BUS:B<x>:MANChester:WORD:COUNt`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._count = BusBItemManchesterWordCount(device, f"{self._cmd_syntax}:COUNt")

    @property
    def count(self) -> BusBItemManchesterWordCount:
        """Return the ``BUS:B<x>:MANChester:WORD:COUNt`` command.

        Description:
            - This command sets or queries the Manchester word count in bits. The bus is specified
              by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:WORD:COUNt?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:WORD:COUNt?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MANChester:WORD:COUNt value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MANChester:WORD:COUNt <NR1>
            - BUS:B<x>:MANChester:WORD:COUNt?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` sets the word count in bits.
        """
        return self._count


class BusBItemManchesterTrailerLength(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MANChester:TRAiler:LENGth`` command.

    Description:
        - This command sets or queries the Manchester trailer length in bits. The bus is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:TRAiler:LENGth?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:TRAiler:LENGth?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:MANChester:TRAiler:LENGth value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MANChester:TRAiler:LENGth <NR1>
        - BUS:B<x>:MANChester:TRAiler:LENGth?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` sets the trailer length in bits.
    """


class BusBItemManchesterTrailer(SCPICmdRead):
    """The ``BUS:B<x>:MANChester:TRAiler`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:TRAiler?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:TRAiler?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.length``: The ``BUS:B<x>:MANChester:TRAiler:LENGth`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._length = BusBItemManchesterTrailerLength(device, f"{self._cmd_syntax}:LENGth")

    @property
    def length(self) -> BusBItemManchesterTrailerLength:
        """Return the ``BUS:B<x>:MANChester:TRAiler:LENGth`` command.

        Description:
            - This command sets or queries the Manchester trailer length in bits. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:TRAiler:LENGth?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:MANChester:TRAiler:LENGth?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MANChester:TRAiler:LENGth value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MANChester:TRAiler:LENGth <NR1>
            - BUS:B<x>:MANChester:TRAiler:LENGth?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` sets the trailer length in bits.
        """
        return self._length


class BusBItemManchesterTranstionZero(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MANChester:TRANstion:ZERo`` command.

    Description:
        - This command sets or queries the Manchester bus for zero falling or rising. Manchester bit
          are defined by transition in the middle of the bit. Depending on the transition,
          conventions are defined. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:TRANstion:ZERo?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:TRANstion:ZERo?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:MANChester:TRANstion:ZERo value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MANChester:TRANstion:ZERo {FALLing|RISing}
        - BUS:B<x>:MANChester:TRANstion:ZERo?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``FALLing`` sets Falling as 0.
        - ``RISing`` sets Rising as 0.
    """


class BusBItemManchesterTranstion(SCPICmdRead):
    """The ``BUS:B<x>:MANChester:TRANstion`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:TRANstion?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:TRANstion?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.zero``: The ``BUS:B<x>:MANChester:TRANstion:ZERo`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._zero = BusBItemManchesterTranstionZero(device, f"{self._cmd_syntax}:ZERo")

    @property
    def zero(self) -> BusBItemManchesterTranstionZero:
        """Return the ``BUS:B<x>:MANChester:TRANstion:ZERo`` command.

        Description:
            - This command sets or queries the Manchester bus for zero falling or rising. Manchester
              bit are defined by transition in the middle of the bit. Depending on the transition,
              conventions are defined. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:TRANstion:ZERo?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:MANChester:TRANstion:ZERo?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MANChester:TRANstion:ZERo value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MANChester:TRANstion:ZERo {FALLing|RISing}
            - BUS:B<x>:MANChester:TRANstion:ZERo?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``FALLing`` sets Falling as 0.
            - ``RISing`` sets Rising as 0.
        """
        return self._zero


class BusBItemManchesterTolerance(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MANChester:TOLerance`` command.

    Description:
        - This command sets or queries the Tolerance bus parameter. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:TOLerance?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:TOLerance?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:MANChester:TOLerance value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MANChester:TOLerance <NR3>
        - BUS:B<x>:MANChester:TOLerance?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` sets the Tolerance bus parameter.
    """


class BusBItemManchesterThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MANChester:THReshold`` command.

    Description:
        - This command sets or queries the Manchester threshold for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:MANChester:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MANChester:THReshold <NR3>
        - BUS:B<x>:MANChester:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` sets the Manchester Strobe threshold for the specified bus in Volts. The
          argument range is -8V to +8V.
    """


class BusBItemManchesterSyncSize(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MANChester:SYNC:SIZe`` command.

    Description:
        - This command sets or queries the Manchester sync Bit Size in bits. The bus is specified by
          x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:SYNC:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:SYNC:SIZe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:MANChester:SYNC:SIZe value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MANChester:SYNC:SIZe <NR1>
        - BUS:B<x>:MANChester:SYNC:SIZe?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` sets the Bit Size in bits.
    """


class BusBItemManchesterSync(SCPICmdRead):
    """The ``BUS:B<x>:MANChester:SYNC`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:SYNC?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:SYNC?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.size``: The ``BUS:B<x>:MANChester:SYNC:SIZe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._size = BusBItemManchesterSyncSize(device, f"{self._cmd_syntax}:SIZe")

    @property
    def size(self) -> BusBItemManchesterSyncSize:
        """Return the ``BUS:B<x>:MANChester:SYNC:SIZe`` command.

        Description:
            - This command sets or queries the Manchester sync Bit Size in bits. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:SYNC:SIZe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:SYNC:SIZe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MANChester:SYNC:SIZe value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MANChester:SYNC:SIZe <NR1>
            - BUS:B<x>:MANChester:SYNC:SIZe?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` sets the Bit Size in bits.
        """
        return self._size


class BusBItemManchesterStartIndex(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MANChester:START:INDex`` command.

    Description:
        - This command sets or queries the Manchester start Index in bits. The bus is specified by
          x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:START:INDex?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:START:INDex?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:MANChester:START:INDex value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MANChester:START:INDex <NR1>
        - BUS:B<x>:MANChester:START:INDex?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` sets the start Index in bits.
    """


class BusBItemManchesterStart(SCPICmdRead):
    """The ``BUS:B<x>:MANChester:START`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:START?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:START?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.index``: The ``BUS:B<x>:MANChester:START:INDex`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._index = BusBItemManchesterStartIndex(device, f"{self._cmd_syntax}:INDex")

    @property
    def index(self) -> BusBItemManchesterStartIndex:
        """Return the ``BUS:B<x>:MANChester:START:INDex`` command.

        Description:
            - This command sets or queries the Manchester start Index in bits. The bus is specified
              by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:START:INDex?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:START:INDex?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MANChester:START:INDex value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MANChester:START:INDex <NR1>
            - BUS:B<x>:MANChester:START:INDex?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` sets the start Index in bits.
        """
        return self._index


class BusBItemManchesterSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MANChester:SOUrce`` command.

    Description:
        - This command sets or queries the Manchester source for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:MANChester:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MANChester:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:MANChester:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``Math<x>`` specifies a math waveform as the source.
        - ``REF<x>`` specifies a reference waveform as the source.
    """


class BusBItemManchesterIdleBits(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MANChester:IDLE:BITS`` command.

    Description:
        - This command sets or queries the Manchester idle bit size in bits. The bus number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:IDLE:BITS?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:IDLE:BITS?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:MANChester:IDLE:BITS value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MANChester:IDLE:BITS <NR1>
        - BUS:B<x>:MANChester:IDLE:BITS?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` sets the idle bit size.
    """


class BusBItemManchesterIdle(SCPICmdRead):
    """The ``BUS:B<x>:MANChester:IDLE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:IDLE?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:IDLE?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.bits``: The ``BUS:B<x>:MANChester:IDLE:BITS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bits = BusBItemManchesterIdleBits(device, f"{self._cmd_syntax}:BITS")

    @property
    def bits(self) -> BusBItemManchesterIdleBits:
        """Return the ``BUS:B<x>:MANChester:IDLE:BITS`` command.

        Description:
            - This command sets or queries the Manchester idle bit size in bits. The bus number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:IDLE:BITS?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:IDLE:BITS?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MANChester:IDLE:BITS value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MANChester:IDLE:BITS <NR1>
            - BUS:B<x>:MANChester:IDLE:BITS?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` sets the idle bit size.
        """
        return self._bits


class BusBItemManchesterHeaderLength(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MANChester:HEADer:LENGth`` command.

    Description:
        - This command sets or queries the Manchester header length in bits. The bus number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:HEADer:LENGth?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:HEADer:LENGth?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:MANChester:HEADer:LENGth value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MANChester:HEADer:LENGth <NR1>
        - BUS:B<x>:MANChester:HEADer:LENGth?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` sets the header length in bits.
    """


class BusBItemManchesterHeader(SCPICmdRead):
    """The ``BUS:B<x>:MANChester:HEADer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:HEADer?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:HEADer?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.length``: The ``BUS:B<x>:MANChester:HEADer:LENGth`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._length = BusBItemManchesterHeaderLength(device, f"{self._cmd_syntax}:LENGth")

    @property
    def length(self) -> BusBItemManchesterHeaderLength:
        """Return the ``BUS:B<x>:MANChester:HEADer:LENGth`` command.

        Description:
            - This command sets or queries the Manchester header length in bits. The bus number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:HEADer:LENGth?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:MANChester:HEADer:LENGth?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MANChester:HEADer:LENGth value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MANChester:HEADer:LENGth <NR1>
            - BUS:B<x>:MANChester:HEADer:LENGth?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` sets the header length in bits.
        """
        return self._length


class BusBItemManchesterDisplaymode(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MANChester:DISplaymode`` command.

    Description:
        - This command sets or queries the Manchester bus Packet View. The bus number is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:DISplaymode?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:DISplaymode?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:MANChester:DISplaymode value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MANChester:DISplaymode {BITS|PACKET}
        - BUS:B<x>:MANChester:DISplaymode?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``BITS`` sets the PacketView to off and the data to be seen as single bits formats.
        - ``PACKET`` sets the PacketView to on and the data to be seen in the form of fields.
    """


class BusBItemManchesterBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MANChester:BITRate`` command.

    Description:
        - This command sets or queries the Manchester bus bit rate. The bus number is specified by
          x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:BITRate?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:MANChester:BITRate value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MANChester:BITRate <NR1>
        - BUS:B<x>:MANChester:BITRate?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` sets the bit rate up to 1 Gbps.
    """


class BusBItemManchesterBitorder(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:MANChester:BITORDer`` command.

    Description:
        - This command sets or queries the Manchester bus Bit Order. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:BITORDer?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:BITORDer?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:MANChester:BITORDer value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:MANChester:BITORDer {LSB|MSB}
        - BUS:B<x>:MANChester:BITORDer?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``LSB`` arranges the bits in LSB format, least significant bits first.
        - ``MSB`` arranges the bits in MSB format, most significant bits first.
    """


#  pylint: disable=too-many-instance-attributes
class BusBItemManchester(SCPICmdRead):
    """The ``BUS:B<x>:MANChester`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.bitorder``: The ``BUS:B<x>:MANChester:BITORDer`` command.
        - ``.bitrate``: The ``BUS:B<x>:MANChester:BITRate`` command.
        - ``.displaymode``: The ``BUS:B<x>:MANChester:DISplaymode`` command.
        - ``.header``: The ``BUS:B<x>:MANChester:HEADer`` command tree.
        - ``.idle``: The ``BUS:B<x>:MANChester:IDLE`` command tree.
        - ``.source``: The ``BUS:B<x>:MANChester:SOUrce`` command.
        - ``.start``: The ``BUS:B<x>:MANChester:START`` command tree.
        - ``.sync``: The ``BUS:B<x>:MANChester:SYNC`` command tree.
        - ``.threshold``: The ``BUS:B<x>:MANChester:THReshold`` command.
        - ``.tolerance``: The ``BUS:B<x>:MANChester:TOLerance`` command.
        - ``.transtion``: The ``BUS:B<x>:MANChester:TRANstion`` command tree.
        - ``.trailer``: The ``BUS:B<x>:MANChester:TRAiler`` command tree.
        - ``.word``: The ``BUS:B<x>:MANChester:WORD`` command tree.
        - ``.wordsize``: The ``BUS:B<x>:MANChester:WORDSIZe`` command.
        - ``.parity``: The ``BUS:B<x>:MANChester:parity`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitorder = BusBItemManchesterBitorder(device, f"{self._cmd_syntax}:BITORDer")
        self._bitrate = BusBItemManchesterBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._displaymode = BusBItemManchesterDisplaymode(device, f"{self._cmd_syntax}:DISplaymode")
        self._header = BusBItemManchesterHeader(device, f"{self._cmd_syntax}:HEADer")
        self._idle = BusBItemManchesterIdle(device, f"{self._cmd_syntax}:IDLE")
        self._source = BusBItemManchesterSource(device, f"{self._cmd_syntax}:SOUrce")
        self._start = BusBItemManchesterStart(device, f"{self._cmd_syntax}:START")
        self._sync = BusBItemManchesterSync(device, f"{self._cmd_syntax}:SYNC")
        self._threshold = BusBItemManchesterThreshold(device, f"{self._cmd_syntax}:THReshold")
        self._tolerance = BusBItemManchesterTolerance(device, f"{self._cmd_syntax}:TOLerance")
        self._transtion = BusBItemManchesterTranstion(device, f"{self._cmd_syntax}:TRANstion")
        self._trailer = BusBItemManchesterTrailer(device, f"{self._cmd_syntax}:TRAiler")
        self._word = BusBItemManchesterWord(device, f"{self._cmd_syntax}:WORD")
        self._wordsize = BusBItemManchesterWordsize(device, f"{self._cmd_syntax}:WORDSIZe")
        self._parity = BusBItemManchesterParity(device, f"{self._cmd_syntax}:parity")

    @property
    def bitorder(self) -> BusBItemManchesterBitorder:
        """Return the ``BUS:B<x>:MANChester:BITORDer`` command.

        Description:
            - This command sets or queries the Manchester bus Bit Order. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:BITORDer?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:BITORDer?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MANChester:BITORDer value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MANChester:BITORDer {LSB|MSB}
            - BUS:B<x>:MANChester:BITORDer?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``LSB`` arranges the bits in LSB format, least significant bits first.
            - ``MSB`` arranges the bits in MSB format, most significant bits first.
        """
        return self._bitorder

    @property
    def bitrate(self) -> BusBItemManchesterBitrate:
        """Return the ``BUS:B<x>:MANChester:BITRate`` command.

        Description:
            - This command sets or queries the Manchester bus bit rate. The bus number is specified
              by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:BITRate?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:MANChester:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MANChester:BITRate <NR1>
            - BUS:B<x>:MANChester:BITRate?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` sets the bit rate up to 1 Gbps.
        """
        return self._bitrate

    @property
    def displaymode(self) -> BusBItemManchesterDisplaymode:
        """Return the ``BUS:B<x>:MANChester:DISplaymode`` command.

        Description:
            - This command sets or queries the Manchester bus Packet View. The bus number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:DISplaymode?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:DISplaymode?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MANChester:DISplaymode value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MANChester:DISplaymode {BITS|PACKET}
            - BUS:B<x>:MANChester:DISplaymode?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``BITS`` sets the PacketView to off and the data to be seen as single bits formats.
            - ``PACKET`` sets the PacketView to on and the data to be seen in the form of fields.
        """
        return self._displaymode

    @property
    def header(self) -> BusBItemManchesterHeader:
        """Return the ``BUS:B<x>:MANChester:HEADer`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:HEADer?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:HEADer?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.length``: The ``BUS:B<x>:MANChester:HEADer:LENGth`` command.
        """
        return self._header

    @property
    def idle(self) -> BusBItemManchesterIdle:
        """Return the ``BUS:B<x>:MANChester:IDLE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:IDLE?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:IDLE?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.bits``: The ``BUS:B<x>:MANChester:IDLE:BITS`` command.
        """
        return self._idle

    @property
    def source(self) -> BusBItemManchesterSource:
        """Return the ``BUS:B<x>:MANChester:SOUrce`` command.

        Description:
            - This command sets or queries the Manchester source for the specified bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:MANChester:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MANChester:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:MANChester:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``Math<x>`` specifies a math waveform as the source.
            - ``REF<x>`` specifies a reference waveform as the source.
        """
        return self._source

    @property
    def start(self) -> BusBItemManchesterStart:
        """Return the ``BUS:B<x>:MANChester:START`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:START?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:START?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.index``: The ``BUS:B<x>:MANChester:START:INDex`` command.
        """
        return self._start

    @property
    def sync(self) -> BusBItemManchesterSync:
        """Return the ``BUS:B<x>:MANChester:SYNC`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:SYNC?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:SYNC?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.size``: The ``BUS:B<x>:MANChester:SYNC:SIZe`` command.
        """
        return self._sync

    @property
    def threshold(self) -> BusBItemManchesterThreshold:
        """Return the ``BUS:B<x>:MANChester:THReshold`` command.

        Description:
            - This command sets or queries the Manchester threshold for the specified bus. The bus
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MANChester:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MANChester:THReshold <NR3>
            - BUS:B<x>:MANChester:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` sets the Manchester Strobe threshold for the specified bus in Volts. The
              argument range is -8V to +8V.
        """
        return self._threshold

    @property
    def tolerance(self) -> BusBItemManchesterTolerance:
        """Return the ``BUS:B<x>:MANChester:TOLerance`` command.

        Description:
            - This command sets or queries the Tolerance bus parameter. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:TOLerance?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:TOLerance?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MANChester:TOLerance value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MANChester:TOLerance <NR3>
            - BUS:B<x>:MANChester:TOLerance?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` sets the Tolerance bus parameter.
        """
        return self._tolerance

    @property
    def transtion(self) -> BusBItemManchesterTranstion:
        """Return the ``BUS:B<x>:MANChester:TRANstion`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:TRANstion?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:TRANstion?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.zero``: The ``BUS:B<x>:MANChester:TRANstion:ZERo`` command.
        """
        return self._transtion

    @property
    def trailer(self) -> BusBItemManchesterTrailer:
        """Return the ``BUS:B<x>:MANChester:TRAiler`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:TRAiler?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:TRAiler?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.length``: The ``BUS:B<x>:MANChester:TRAiler:LENGth`` command.
        """
        return self._trailer

    @property
    def word(self) -> BusBItemManchesterWord:
        """Return the ``BUS:B<x>:MANChester:WORD`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:WORD?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:WORD?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.count``: The ``BUS:B<x>:MANChester:WORD:COUNt`` command.
        """
        return self._word

    @property
    def wordsize(self) -> BusBItemManchesterWordsize:
        """Return the ``BUS:B<x>:MANChester:WORDSIZe`` command.

        Description:
            - This command sets or queries the Manchester word size in bits. The bus is specified by
              x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:WORDSIZe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:WORDSIZe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:MANChester:WORDSIZe value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MANChester:WORDSIZe <NR1>
            - BUS:B<x>:MANChester:WORDSIZe?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` sets the word size in bits.
        """
        return self._wordsize

    @property
    def parity(self) -> BusBItemManchesterParity:
        """Return the ``BUS:B<x>:MANChester:parity`` command.

        Description:
            - This command sets or queries the Manchester bus Parity. The bus number is specified by
              x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester:parity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester:parity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:MANChester:parity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:MANChester:parity {ODD|EVEN|NONE}
            - BUS:B<x>:MANChester:parity?
            ```

        Info:
            - ``ODD`` sets the number of 1's to odd.
            - ``EVEN`` sets the number of 1's to even.
            - ``NONE`` specifies that Parity is not considered.
        """
        return self._parity


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


class BusBItemLinSourceThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LIN:SOUrce:THReshold`` command.

    Description:
        - This command sets or queries the LIN source threshold for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:SOUrce:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:SOUrce:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:SOUrce:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:SOUrce:THReshold <NR3>
        - BUS:B<x>:LIN:SOUrce:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` the LIN source threshold for the specified bus.
    """


class BusBItemLinSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LIN:SOUrce`` command.

    Description:
        - This command sets or queries the LIN data source for the specified bus. The bus number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:SOUrce?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:LIN:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.threshold``: The ``BUS:B<x>:LIN:SOUrce:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._threshold = BusBItemLinSourceThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def threshold(self) -> BusBItemLinSourceThreshold:
        """Return the ``BUS:B<x>:LIN:SOUrce:THReshold`` command.

        Description:
            - This command sets or queries the LIN source threshold for the specified bus. The bus
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:SOUrce:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:SOUrce:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:LIN:SOUrce:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:SOUrce:THReshold <NR3>
            - BUS:B<x>:LIN:SOUrce:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` the LIN source threshold for the specified bus.
        """
        return self._threshold


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
        - This command sets or queries the LIN source polarity for the specified bus. The bus number
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:POLarity?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:POLarity value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:POLarity {INVerted|NORmal}
        - BUS:B<x>:LIN:POLarity?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
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


class BusBItemLinBitrateCustom(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LIN:BITRate:CUSTom`` command.

    Description:
        - This command sets or queries LIN custom bit rate for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:BITRate:CUSTom?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:BITRate:CUSTom?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:BITRate:CUSTom value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:BITRate:CUSTom <NR1>
        - BUS:B<x>:LIN:BITRate:CUSTom?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` is the LIN custom bit rate for the specified bus.
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
        - ``.custom``: The ``BUS:B<x>:LIN:BITRate:CUSTom`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._custom = BusBItemLinBitrateCustom(device, f"{self._cmd_syntax}:CUSTom")

    @property
    def custom(self) -> BusBItemLinBitrateCustom:
        """Return the ``BUS:B<x>:LIN:BITRate:CUSTom`` command.

        Description:
            - This command sets or queries LIN custom bit rate for the specified bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:BITRate:CUSTom?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:BITRate:CUSTom?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:BITRate:CUSTom value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:BITRate:CUSTom <NR1>
            - BUS:B<x>:LIN:BITRate:CUSTom?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` is the LIN custom bit rate for the specified bus.
        """
        return self._custom


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
        - ``.samplepoint``: The ``BUS:B<x>:LIN:SAMPLEpoint`` command.
        - ``.source``: The ``BUS:B<x>:LIN:SOUrce`` command.
        - ``.standard``: The ``BUS:B<x>:LIN:STANDard`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemLinBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._idformat = BusBItemLinIdformat(device, f"{self._cmd_syntax}:IDFORmat")
        self._polarity = BusBItemLinPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._samplepoint = BusBItemLinSamplepoint(device, f"{self._cmd_syntax}:SAMPLEpoint")
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
            - ``.custom``: The ``BUS:B<x>:LIN:BITRate:CUSTom`` command.
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
            - This command sets or queries the LIN source polarity for the specified bus. The bus
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:POLarity?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:POLarity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:POLarity {INVerted|NORmal}
            - BUS:B<x>:LIN:POLarity?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
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
            - This command sets or queries the LIN data source for the specified bus. The bus number
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:LIN:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.threshold``: The ``BUS:B<x>:LIN:SOUrce:THReshold`` command.
        """
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


class BusBItemLabelName(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LABel:name`` command.

    Description:
        - This command sets or queries the label for the specified bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:name?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:name?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:name value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LABel:name <QString>
        - BUS:B<x>:LABel:name?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<QString>`` is an alphanumeric string of text enclosed in quotes. The text string is
          limited to 30 characters. It contains the text label information for the bus.
    """

    _WRAP_ARG_WITH_QUOTES = True


class BusBItemLabelYpos(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LABel:YPOS`` command.

    Description:
        - This command sets or queries the y-position of the specified bus label. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:YPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:YPOS?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:YPOS value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LABel:YPOS <NR3>
        - BUS:B<x>:LABel:YPOS?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the y-position, in pixels relative to the baseline of the waveform, of the
          specified bus label.
    """


class BusBItemLabelXpos(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LABel:XPOS`` command.

    Description:
        - This command sets or queries the x-position of the specified bus label. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:XPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:XPOS?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:XPOS value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LABel:XPOS <NR3>
        - BUS:B<x>:LABel:XPOS?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the x-position, in pixels relative to the left edge of the screen of the
          specified bus label.
    """


class BusBItemLabelFontUnderline(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LABel:FONT:UNDERline`` command.

    Description:
        - This command sets or queries the underline state of the specified bus label. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:FONT:UNDERline?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:FONT:UNDERline?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:FONT:UNDERline value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LABel:FONT:UNDERline {ON|OFF|1|0}
        - BUS:B<x>:LABel:FONT:UNDERline?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``ON`` displays the label in underlined font.
        - ``OFF`` does not display the label in underlined font.
        - ``1`` displays the label in underlined font.
        - ``0`` does not display the label in underlined font.
    """


class BusBItemLabelFontType(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LABel:FONT:TYPE`` command.

    Description:
        - This command sets or queries the font type of the specified bus label, such as Arial or
          Times New Roman. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:FONT:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:FONT:TYPE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:FONT:TYPE value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LABel:FONT:TYPE <QString>
        - BUS:B<x>:LABel:FONT:TYPE?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<QString>`` is the specified font type. Available fonts include: DejaVu Sans, DejaVu
          Sans Mono, DejaVu Serif, Frutiger LT Std, Monospace, Sans Serif, Serif, Ubuntu, Ubuntu
          Condensed, and Ubuntu Mono.
    """

    _WRAP_ARG_WITH_QUOTES = True


class BusBItemLabelFontSize(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LABel:FONT:SIZE`` command.

    Description:
        - This command sets or queries the font size of the specified bus label. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:FONT:SIZE?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:FONT:SIZE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:FONT:SIZE value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LABel:FONT:SIZE <NR1>
        - BUS:B<x>:LABel:FONT:SIZE?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` is the font size.
    """


class BusBItemLabelFontItalic(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LABel:FONT:ITALic`` command.

    Description:
        - This command sets or queries the italic state of the specified bus label. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:FONT:ITALic?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:FONT:ITALic?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:FONT:ITALic value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LABel:FONT:ITALic {ON|OFF|1|0}
        - BUS:B<x>:LABel:FONT:ITALic?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``ON`` displays the label in italic font.
        - ``OFF`` does not display the label in italic font.
        - ``1`` displays the label in italic font.
        - ``0`` does not display the label in italic font.
    """


class BusBItemLabelFontBold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LABel:FONT:BOLD`` command.

    Description:
        - This command sets or queries the bold state of the specified bus label. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:FONT:BOLD?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:FONT:BOLD?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:FONT:BOLD value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LABel:FONT:BOLD {ON|OFF|1|0}
        - BUS:B<x>:LABel:FONT:BOLD?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``ON`` displays the label in bold font.
        - ``OFF`` does not display the label in bold font.
        - ``1`` displays the label in bold font.
        - ``0`` does not display the label in bold font.
    """


class BusBItemLabelFont(SCPICmdRead):
    """The ``BUS:B<x>:LABel:FONT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:FONT?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:FONT?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.bold``: The ``BUS:B<x>:LABel:FONT:BOLD`` command.
        - ``.italic``: The ``BUS:B<x>:LABel:FONT:ITALic`` command.
        - ``.size``: The ``BUS:B<x>:LABel:FONT:SIZE`` command.
        - ``.type``: The ``BUS:B<x>:LABel:FONT:TYPE`` command.
        - ``.underline``: The ``BUS:B<x>:LABel:FONT:UNDERline`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bold = BusBItemLabelFontBold(device, f"{self._cmd_syntax}:BOLD")
        self._italic = BusBItemLabelFontItalic(device, f"{self._cmd_syntax}:ITALic")
        self._size = BusBItemLabelFontSize(device, f"{self._cmd_syntax}:SIZE")
        self._type = BusBItemLabelFontType(device, f"{self._cmd_syntax}:TYPE")
        self._underline = BusBItemLabelFontUnderline(device, f"{self._cmd_syntax}:UNDERline")

    @property
    def bold(self) -> BusBItemLabelFontBold:
        """Return the ``BUS:B<x>:LABel:FONT:BOLD`` command.

        Description:
            - This command sets or queries the bold state of the specified bus label. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:FONT:BOLD?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:FONT:BOLD?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:FONT:BOLD value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LABel:FONT:BOLD {ON|OFF|1|0}
            - BUS:B<x>:LABel:FONT:BOLD?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``ON`` displays the label in bold font.
            - ``OFF`` does not display the label in bold font.
            - ``1`` displays the label in bold font.
            - ``0`` does not display the label in bold font.
        """
        return self._bold

    @property
    def italic(self) -> BusBItemLabelFontItalic:
        """Return the ``BUS:B<x>:LABel:FONT:ITALic`` command.

        Description:
            - This command sets or queries the italic state of the specified bus label. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:FONT:ITALic?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:FONT:ITALic?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:FONT:ITALic value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LABel:FONT:ITALic {ON|OFF|1|0}
            - BUS:B<x>:LABel:FONT:ITALic?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``ON`` displays the label in italic font.
            - ``OFF`` does not display the label in italic font.
            - ``1`` displays the label in italic font.
            - ``0`` does not display the label in italic font.
        """
        return self._italic

    @property
    def size(self) -> BusBItemLabelFontSize:
        """Return the ``BUS:B<x>:LABel:FONT:SIZE`` command.

        Description:
            - This command sets or queries the font size of the specified bus label. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:FONT:SIZE?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:FONT:SIZE?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:FONT:SIZE value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LABel:FONT:SIZE <NR1>
            - BUS:B<x>:LABel:FONT:SIZE?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` is the font size.
        """
        return self._size

    @property
    def type(self) -> BusBItemLabelFontType:
        """Return the ``BUS:B<x>:LABel:FONT:TYPE`` command.

        Description:
            - This command sets or queries the font type of the specified bus label, such as Arial
              or Times New Roman. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:FONT:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:FONT:TYPE?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:FONT:TYPE value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LABel:FONT:TYPE <QString>
            - BUS:B<x>:LABel:FONT:TYPE?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<QString>`` is the specified font type. Available fonts include: DejaVu Sans, DejaVu
              Sans Mono, DejaVu Serif, Frutiger LT Std, Monospace, Sans Serif, Serif, Ubuntu, Ubuntu
              Condensed, and Ubuntu Mono.
        """
        return self._type

    @property
    def underline(self) -> BusBItemLabelFontUnderline:
        """Return the ``BUS:B<x>:LABel:FONT:UNDERline`` command.

        Description:
            - This command sets or queries the underline state of the specified bus label. The bus
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:FONT:UNDERline?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:FONT:UNDERline?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:LABel:FONT:UNDERline value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LABel:FONT:UNDERline {ON|OFF|1|0}
            - BUS:B<x>:LABel:FONT:UNDERline?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``ON`` displays the label in underlined font.
            - ``OFF`` does not display the label in underlined font.
            - ``1`` displays the label in underlined font.
            - ``0`` does not display the label in underlined font.
        """
        return self._underline


class BusBItemLabelColor(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LABel:COLor`` command.

    Description:
        - This command sets or queries the color of the specified bus label. The bus is specified by
          x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:COLor?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:COLor?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:COLor value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LABel:COLor <QString>
        - BUS:B<x>:LABel:COLor?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<QString>`` is the bus label color. To return the color to the default color, send an
          empty string as in this example: ``:BUS:B1:LABEL:COLOR`` ''.
    """

    _WRAP_ARG_WITH_QUOTES = True


class BusBItemLabel(SCPICmdRead):
    """The ``BUS:B<x>:LABel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.color``: The ``BUS:B<x>:LABel:COLor`` command.
        - ``.font``: The ``BUS:B<x>:LABel:FONT`` command tree.
        - ``.xpos``: The ``BUS:B<x>:LABel:XPOS`` command.
        - ``.ypos``: The ``BUS:B<x>:LABel:YPOS`` command.
        - ``.name``: The ``BUS:B<x>:LABel:name`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._color = BusBItemLabelColor(device, f"{self._cmd_syntax}:COLor")
        self._font = BusBItemLabelFont(device, f"{self._cmd_syntax}:FONT")
        self._xpos = BusBItemLabelXpos(device, f"{self._cmd_syntax}:XPOS")
        self._ypos = BusBItemLabelYpos(device, f"{self._cmd_syntax}:YPOS")
        self._name = BusBItemLabelName(device, f"{self._cmd_syntax}:name")

    @property
    def color(self) -> BusBItemLabelColor:
        """Return the ``BUS:B<x>:LABel:COLor`` command.

        Description:
            - This command sets or queries the color of the specified bus label. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:COLor?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:COLor?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:COLor value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LABel:COLor <QString>
            - BUS:B<x>:LABel:COLor?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<QString>`` is the bus label color. To return the color to the default color, send
              an empty string as in this example: ``:BUS:B1:LABEL:COLOR`` ''.
        """
        return self._color

    @property
    def font(self) -> BusBItemLabelFont:
        """Return the ``BUS:B<x>:LABel:FONT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:FONT?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:FONT?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.bold``: The ``BUS:B<x>:LABel:FONT:BOLD`` command.
            - ``.italic``: The ``BUS:B<x>:LABel:FONT:ITALic`` command.
            - ``.size``: The ``BUS:B<x>:LABel:FONT:SIZE`` command.
            - ``.type``: The ``BUS:B<x>:LABel:FONT:TYPE`` command.
            - ``.underline``: The ``BUS:B<x>:LABel:FONT:UNDERline`` command.
        """
        return self._font

    @property
    def xpos(self) -> BusBItemLabelXpos:
        """Return the ``BUS:B<x>:LABel:XPOS`` command.

        Description:
            - This command sets or queries the x-position of the specified bus label. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:XPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:XPOS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:XPOS value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LABel:XPOS <NR3>
            - BUS:B<x>:LABel:XPOS?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the x-position, in pixels relative to the left edge of the screen of the
              specified bus label.
        """
        return self._xpos

    @property
    def ypos(self) -> BusBItemLabelYpos:
        """Return the ``BUS:B<x>:LABel:YPOS`` command.

        Description:
            - This command sets or queries the y-position of the specified bus label. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:YPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:YPOS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:YPOS value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LABel:YPOS <NR3>
            - BUS:B<x>:LABel:YPOS?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the y-position, in pixels relative to the baseline of the waveform, of
              the specified bus label.
        """
        return self._ypos

    @property
    def name(self) -> BusBItemLabelName:
        """Return the ``BUS:B<x>:LABel:name`` command.

        Description:
            - This command sets or queries the label for the specified bus. The bus is specified by
              x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:name?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:name?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:name value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LABel:name <QString>
            - BUS:B<x>:LABel:name?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<QString>`` is an alphanumeric string of text enclosed in quotes. The text string is
              limited to 30 characters. It contains the text label information for the bus.
        """
        return self._name


class BusBItemI3cDataThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I3C:DATa:THReshold`` command.

    Description:
        - This command sets or queries the I3C clock (SDA) data threshold level for the specified
          bus. Requires purchase and installation of option SRI3C.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I3C:DATa:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I3C:DATa:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I3C:DATa:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I3C:DATa:THReshold {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:I3C:DATa:THReshold?
        ```

    Info:
        - ``B<x>`` specifies the bus number.
        - ``<NR3>`` is the threshold value for I3C Data Clock (SDA) source of the specified bus.
    """


class BusBItemI3cDataSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I3C:DATa:SOUrce`` command.

    Description:
        - This command sets or queries the I3C data clock (SDA) source for the specified bus.
          Requires purchase and installation of option SRI3C.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I3C:DATa:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I3C:DATa:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I3C:DATa:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I3C:DATa:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:I3C:DATa:SOUrce?
        ```

    Info:
        - ``B<x>`` specifies the bus number.
        - ``S<x>_Ch<x>_D<x>`` specifies is the remote scope number, the analog channel and the
          digital channel.
        - ``CH<x>`` specifies the analog channel to use as the I3C SDA source.
        - ``CH<x>_D<x>`` specifies the digital channel to use as the I3C SDA source.
        - ``Math<x>`` specifies the math waveform to use as the I3C SDA source.
        - ``REF<x>`` specifies the reference waveform to use as the I3C SDA source.
        - ``REF<x>_D<x>`` specifies the digital reference waveform to use as the I3C SDA source.
    """


class BusBItemI3cData(SCPICmdRead):
    """The ``BUS:B<x>:I3C:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I3C:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I3C:DATa?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` specifies the bus number.

    Properties:
        - ``.source``: The ``BUS:B<x>:I3C:DATa:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:I3C:DATa:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemI3cDataSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemI3cDataThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def source(self) -> BusBItemI3cDataSource:
        """Return the ``BUS:B<x>:I3C:DATa:SOUrce`` command.

        Description:
            - This command sets or queries the I3C data clock (SDA) source for the specified bus.
              Requires purchase and installation of option SRI3C.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I3C:DATa:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I3C:DATa:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:I3C:DATa:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I3C:DATa:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:I3C:DATa:SOUrce?
            ```

        Info:
            - ``B<x>`` specifies the bus number.
            - ``S<x>_Ch<x>_D<x>`` specifies is the remote scope number, the analog channel and the
              digital channel.
            - ``CH<x>`` specifies the analog channel to use as the I3C SDA source.
            - ``CH<x>_D<x>`` specifies the digital channel to use as the I3C SDA source.
            - ``Math<x>`` specifies the math waveform to use as the I3C SDA source.
            - ``REF<x>`` specifies the reference waveform to use as the I3C SDA source.
            - ``REF<x>_D<x>`` specifies the digital reference waveform to use as the I3C SDA source.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemI3cDataThreshold:
        """Return the ``BUS:B<x>:I3C:DATa:THReshold`` command.

        Description:
            - This command sets or queries the I3C clock (SDA) data threshold level for the
              specified bus. Requires purchase and installation of option SRI3C.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I3C:DATa:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I3C:DATa:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:I3C:DATa:THReshold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I3C:DATa:THReshold {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:I3C:DATa:THReshold?
            ```

        Info:
            - ``B<x>`` specifies the bus number.
            - ``<NR3>`` is the threshold value for I3C Data Clock (SDA) source of the specified bus.
        """  # noqa: E501
        return self._threshold


class BusBItemI3cClockThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I3C:CLOCk:THReshold`` command.

    Description:
        - This command sets or queries the I3C clock (SCLK) source threshold level for the specified
          bus. Requires purchase and installation of option SRI3C.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I3C:CLOCk:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I3C:CLOCk:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I3C:CLOCk:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I3C:CLOCk:THReshold <NR3>
        - BUS:B<x>:I3C:CLOCk:THReshold?
        ```

    Info:
        - ``B<x>`` specifies the bus number.
        - ``<NR3>`` is the threshold value for I3C Clock (SCLK) source of the specified bus.
    """


class BusBItemI3cClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I3C:CLOCk:SOUrce`` command.

    Description:
        - This command sets or queries the I3C clock (SCLK) source for the specified bus. Requires
          purchase and installation of option SRI3C.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I3C:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I3C:CLOCk:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I3C:CLOCk:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I3C:CLOCk:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:I3C:CLOCk:SOUrce?
        ```

    Info:
        - ``B<x>`` specifies the bus number.
        - ``S<x>_Ch<x>_D<x>`` specifies is the remote scope number, the analog channel and the
          digital channel.
        - ``CH<x>`` specifies the analog channel to use as the I3C SCLK source.
        - ``CH<x>_D<x>`` specifies the digital channel to use as the I3C SCLK source.
        - ``Math<x>`` specifies the math waveform to use as the I3C SCLK source.
        - ``REF<x>`` specifies the reference waveform to use as the I3C SCLK source.
        - ``REF<x>_D<x>`` specifies the digital reference waveform to use as the I3C SCLK source.
    """


class BusBItemI3cClock(SCPICmdRead):
    """The ``BUS:B<x>:I3C:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I3C:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I3C:CLOCk?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` specifies the bus number.

    Properties:
        - ``.source``: The ``BUS:B<x>:I3C:CLOCk:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:I3C:CLOCk:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemI3cClockSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemI3cClockThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def source(self) -> BusBItemI3cClockSource:
        """Return the ``BUS:B<x>:I3C:CLOCk:SOUrce`` command.

        Description:
            - This command sets or queries the I3C clock (SCLK) source for the specified bus.
              Requires purchase and installation of option SRI3C.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I3C:CLOCk:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I3C:CLOCk:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:I3C:CLOCk:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I3C:CLOCk:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:I3C:CLOCk:SOUrce?
            ```

        Info:
            - ``B<x>`` specifies the bus number.
            - ``S<x>_Ch<x>_D<x>`` specifies is the remote scope number, the analog channel and the
              digital channel.
            - ``CH<x>`` specifies the analog channel to use as the I3C SCLK source.
            - ``CH<x>_D<x>`` specifies the digital channel to use as the I3C SCLK source.
            - ``Math<x>`` specifies the math waveform to use as the I3C SCLK source.
            - ``REF<x>`` specifies the reference waveform to use as the I3C SCLK source.
            - ``REF<x>_D<x>`` specifies the digital reference waveform to use as the I3C SCLK
              source.
        """  # noqa: E501
        return self._source

    @property
    def threshold(self) -> BusBItemI3cClockThreshold:
        """Return the ``BUS:B<x>:I3C:CLOCk:THReshold`` command.

        Description:
            - This command sets or queries the I3C clock (SCLK) source threshold level for the
              specified bus. Requires purchase and installation of option SRI3C.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I3C:CLOCk:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I3C:CLOCk:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:I3C:CLOCk:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I3C:CLOCk:THReshold <NR3>
            - BUS:B<x>:I3C:CLOCk:THReshold?
            ```

        Info:
            - ``B<x>`` specifies the bus number.
            - ``<NR3>`` is the threshold value for I3C Clock (SCLK) source of the specified bus.
        """
        return self._threshold


class BusBItemI3c(SCPICmdRead):
    """The ``BUS:B<x>:I3C`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I3C?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I3C?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` specifies the bus number.

    Properties:
        - ``.clock``: The ``BUS:B<x>:I3C:CLOCk`` command tree.
        - ``.data``: The ``BUS:B<x>:I3C:DATa`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._clock = BusBItemI3cClock(device, f"{self._cmd_syntax}:CLOCk")
        self._data = BusBItemI3cData(device, f"{self._cmd_syntax}:DATa")

    @property
    def clock(self) -> BusBItemI3cClock:
        """Return the ``BUS:B<x>:I3C:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I3C:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I3C:CLOCk?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` specifies the bus number.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:I3C:CLOCk:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:I3C:CLOCk:THReshold`` command.
        """
        return self._clock

    @property
    def data(self) -> BusBItemI3cData:
        """Return the ``BUS:B<x>:I3C:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I3C:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I3C:DATa?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` specifies the bus number.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:I3C:DATa:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:I3C:DATa:THReshold`` command.
        """
        return self._data


class BusBItemI2cRwinaddr(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I2C:RWINADDR`` command.

    Description:
        - This command sets or queries the manner in which seven-bit I2C addresses are represented
          in the busform display of the specified bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:RWINADDR?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:RWINADDR?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:RWINADDR value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I2C:RWINADDR {0|1}
        - BUS:B<x>:I2C:RWINADDR?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``0`` displays seven-bit slave addresses as integers in the range of 0 to 127, with the
          state of the R/W* bit from the LSB of the slave address byte. For example, the slave
          address byte of 0b10100101 is displayed as the value 0x52 R.
        - ``1`` displays the entire slave address byte as a number, with the R/W* signal as its LSB
          (bit 0) and the slave address in bits 7..1. For example, the slave address byte of
          0b10100101 is displayed as the value 0xA5 R.
    """


class BusBItemI2cDataThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I2C:DATa:THReshold`` command.

    Description:
        - This command sets or queries the I2C Data (SDA) source threshold for the specified bus.
          The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:DATa:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:DATa:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:DATa:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I2C:DATa:THReshold <NR3>
        - BUS:B<x>:I2C:DATa:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the I2C Data (SDA) source threshold for the specified bus.
    """


class BusBItemI2cDataSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I2C:DATa:SOUrce`` command.

    Description:
        - This command sets or queries the I2C data (SDA) source for the specified I2C bus. The bus
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:DATa:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:DATa:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:DATa:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I2C:DATa:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:I2C:DATa:SOUrce?
        ```

    Info:
        - ``S<x>_Ch<x>_D<x>`` specifies is the remote scope number, the analog channel and the
          digital channel.
        - ``CH<x>`` specifies an analog channel to use as the I2C SDA source.
        - ``CH<x>_D<x>`` specifies a digital channel to use as the I2C SDA source.
        - ``MATH<x>`` specifies a math waveform to use as the I2C SDA source.
        - ``REF<x>`` specifies a reference waveform to use as the I2C SDA source.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the data source waveform for the
          specified I2C bus.
    """


class BusBItemI2cData(SCPICmdRead):
    """The ``BUS:B<x>:I2C:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:DATa?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``BUS:B<x>:I2C:DATa:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:I2C:DATa:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemI2cDataSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemI2cDataThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def source(self) -> BusBItemI2cDataSource:
        """Return the ``BUS:B<x>:I2C:DATa:SOUrce`` command.

        Description:
            - This command sets or queries the I2C data (SDA) source for the specified I2C bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:DATa:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:DATa:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:DATa:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I2C:DATa:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:I2C:DATa:SOUrce?
            ```

        Info:
            - ``S<x>_Ch<x>_D<x>`` specifies is the remote scope number, the analog channel and the
              digital channel.
            - ``CH<x>`` specifies an analog channel to use as the I2C SDA source.
            - ``CH<x>_D<x>`` specifies a digital channel to use as the I2C SDA source.
            - ``MATH<x>`` specifies a math waveform to use as the I2C SDA source.
            - ``REF<x>`` specifies a reference waveform to use as the I2C SDA source.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the data source waveform for
              the specified I2C bus.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemI2cDataThreshold:
        """Return the ``BUS:B<x>:I2C:DATa:THReshold`` command.

        Description:
            - This command sets or queries the I2C Data (SDA) source threshold for the specified
              bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:DATa:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:DATa:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:DATa:THReshold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I2C:DATa:THReshold <NR3>
            - BUS:B<x>:I2C:DATa:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the I2C Data (SDA) source threshold for the specified bus.
        """
        return self._threshold


class BusBItemI2cClockThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I2C:CLOCk:THReshold`` command.

    Description:
        - This command sets or queries the I2C Clock (SCLK) source threshold for the specified bus.
          The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:CLOCk:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:CLOCk:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:CLOCk:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I2C:CLOCk:THReshold <NR3>
        - BUS:B<x>:I2C:CLOCk:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the I2C Clock (SCLK) source threshold for the specified bus.
    """


class BusBItemI2cClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I2C:CLOCk:SOUrce`` command.

    Description:
        - This command sets or queries the I2C clock (SCLK) source for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:CLOCk:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:CLOCk:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I2C:CLOCk:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:I2C:CLOCk:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>_D<x>`` specifies is the remote scope number, the analog channel and the
          digital channel.
        - ``CH<x>`` specifies an analog channel to use as the I2C SCLK source.
        - ``CH<x>_D<x>`` specifies a digital channel to use as the I2C SCLK source.
        - ``MATH<x>`` specifies a math waveform to use as the I2C SCLK source.
        - ``REF<x>`` specifies a reference waveform to use as the I2C SCLK source.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the clock source waveform for
          the specified I2C bus.
    """


class BusBItemI2cClock(SCPICmdRead):
    """The ``BUS:B<x>:I2C:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:CLOCk?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.source``: The ``BUS:B<x>:I2C:CLOCk:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:I2C:CLOCk:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemI2cClockSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemI2cClockThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def source(self) -> BusBItemI2cClockSource:
        """Return the ``BUS:B<x>:I2C:CLOCk:SOUrce`` command.

        Description:
            - This command sets or queries the I2C clock (SCLK) source for the specified bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:CLOCk:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:CLOCk:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:CLOCk:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I2C:CLOCk:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:I2C:CLOCk:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>_D<x>`` specifies is the remote scope number, the analog channel and the
              digital channel.
            - ``CH<x>`` specifies an analog channel to use as the I2C SCLK source.
            - ``CH<x>_D<x>`` specifies a digital channel to use as the I2C SCLK source.
            - ``MATH<x>`` specifies a math waveform to use as the I2C SCLK source.
            - ``REF<x>`` specifies a reference waveform to use as the I2C SCLK source.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the clock source waveform
              for the specified I2C bus.
        """  # noqa: E501
        return self._source

    @property
    def threshold(self) -> BusBItemI2cClockThreshold:
        """Return the ``BUS:B<x>:I2C:CLOCk:THReshold`` command.

        Description:
            - This command sets or queries the I2C Clock (SCLK) source threshold for the specified
              bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:CLOCk:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:CLOCk:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:I2C:CLOCk:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I2C:CLOCk:THReshold <NR3>
            - BUS:B<x>:I2C:CLOCk:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the I2C Clock (SCLK) source threshold for the specified bus.
        """
        return self._threshold


class BusBItemI2c(SCPICmdRead):
    """The ``BUS:B<x>:I2C`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

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

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:I2C:CLOCk:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:I2C:CLOCk:THReshold`` command.
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
            - ``.threshold``: The ``BUS:B<x>:I2C:DATa:THReshold`` command.
        """
        return self._data

    @property
    def rwinaddr(self) -> BusBItemI2cRwinaddr:
        """Return the ``BUS:B<x>:I2C:RWINADDR`` command.

        Description:
            - This command sets or queries the manner in which seven-bit I2C addresses are
              represented in the busform display of the specified bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:RWINADDR?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:RWINADDR?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:RWINADDR value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I2C:RWINADDR {0|1}
            - BUS:B<x>:I2C:RWINADDR?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``0`` displays seven-bit slave addresses as integers in the range of 0 to 127, with
              the state of the R/W* bit from the LSB of the slave address byte. For example, the
              slave address byte of 0b10100101 is displayed as the value 0x52 R.
            - ``1`` displays the entire slave address byte as a number, with the R/W* signal as its
              LSB (bit 0) and the slave address in bits 7..1. For example, the slave address byte of
              0b10100101 is displayed as the value 0xA5 R.
        """
        return self._rwinaddr


class BusBItemFlexrayTxrxthreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:FLEXray:TXRXTHRESHold`` command.

    Description:
        - This command sets or queries the FlexRay data source TxRx threshold for the specified bus.
          The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:TXRXTHRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:TXRXTHRESHold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXray:TXRXTHRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:FLEXray:TXRXTHRESHold <NR3>
        - BUS:B<x>:FLEXray:TXRXTHRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the TxRx threshold.
    """


class BusBItemFlexrayThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:FLEXray:THRESHold`` command.

    Description:
        - This command sets or queries the FlexRay data source high threshold for the specified bus.
          The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:THRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:THRESHold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXray:THRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:FLEXray:THRESHold <NR3>
        - BUS:B<x>:FLEXray:THRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the FlexRay data source high threshold for the specified bus.
    """


class BusBItemFlexraySourceTxrx(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:FLEXray:SOUrce:TXRX`` command.

    Description:
        - This command sets or queries the FlexRay TxRx data source for the specified bus when the
          signal type is TXRX. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:SOUrce:TXRX?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:SOUrce:TXRX?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXray:SOUrce:TXRX value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:FLEXray:SOUrce:TXRX {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:FLEXray:SOUrce:TXRX?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>_D<x>`` specifies the remote scope number, the analog channel and the digital
          channel as the source.
        - ``CH<x>_D<x>`` specifies an analog channel and the digital channel as the source.
        - ``REF<x>_D<x>`` specifies a reference waveform and the digital channel as the source.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``Math<x>`` specifies a math waveform as the source.
        - ``REF<x>`` specifies a reference waveform as the source.
    """


class BusBItemFlexraySource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:FLEXray:SOUrce`` command.

    Description:
        - This command sets or queries the Flexray bus data source for the specified bus when the
          signal type is BDIFFBP or BM. The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXray:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:FLEXray:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:FLEXray:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``Math<x>`` specifies a math waveform as the source.
        - ``REF<x>`` specifies a reference waveform as the source.

    Properties:
        - ``.txrx``: The ``BUS:B<x>:FLEXray:SOUrce:TXRX`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._txrx = BusBItemFlexraySourceTxrx(device, f"{self._cmd_syntax}:TXRX")

    @property
    def txrx(self) -> BusBItemFlexraySourceTxrx:
        """Return the ``BUS:B<x>:FLEXray:SOUrce:TXRX`` command.

        Description:
            - This command sets or queries the FlexRay TxRx data source for the specified bus when
              the signal type is TXRX. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:SOUrce:TXRX?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:SOUrce:TXRX?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:FLEXray:SOUrce:TXRX value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:FLEXray:SOUrce:TXRX {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:FLEXray:SOUrce:TXRX?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>_D<x>`` specifies the remote scope number, the analog channel and the
              digital channel as the source.
            - ``CH<x>_D<x>`` specifies an analog channel and the digital channel as the source.
            - ``REF<x>_D<x>`` specifies a reference waveform and the digital channel as the source.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``Math<x>`` specifies a math waveform as the source.
            - ``REF<x>`` specifies a reference waveform as the source.
        """  # noqa: E501
        return self._txrx


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


class BusBItemFlexrayLowthreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:FLEXray:LOWTHRESHold`` command.

    Description:
        - This command sets or queries the FlexRay data source low threshold for the specified bus.
          The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:LOWTHRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:LOWTHRESHold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXray:LOWTHRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:FLEXray:LOWTHRESHold <NR3>
        - BUS:B<x>:FLEXray:LOWTHRESHold?
        ```

    Info:
        - ``<NR3>`` is the FlexRay data source low threshold for the specified bus.
        - ``B<x>`` is the number of the bus.
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


class BusBItemFlexrayBitrateCustom(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:FLEXray:BITRate:CUSTom`` command.

    Description:
        - This command sets or queries the FlexRay custom bit rate for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:BITRate:CUSTom?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:BITRate:CUSTom?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXray:BITRate:CUSTom value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:FLEXray:BITRate:CUSTom <NR1>
        - BUS:B<x>:FLEXray:BITRate:CUSTom?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` is the FlexRay custom bit rate for the specified bus.
    """


class BusBItemFlexrayBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:FLEXray:BITRate`` command.

    Description:
        - This command sets or queries the FlexRay bus bit rate. The bus is specified by x. If you
          select Custom, use ``BUS:BX:FLEXRAY:BITRATE:CUSTOM`` to set the bit rate.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXray:BITRate value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:FLEXray:BITRate {CUSTOM|RATE2M|RATE5M|RATE10M}
        - BUS:B<x>:FLEXray:BITRate?
        ```

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.custom``: The ``BUS:B<x>:FLEXray:BITRate:CUSTom`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._custom = BusBItemFlexrayBitrateCustom(device, f"{self._cmd_syntax}:CUSTom")

    @property
    def custom(self) -> BusBItemFlexrayBitrateCustom:
        """Return the ``BUS:B<x>:FLEXray:BITRate:CUSTom`` command.

        Description:
            - This command sets or queries the FlexRay custom bit rate for the specified bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:BITRate:CUSTom?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:BITRate:CUSTom?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:FLEXray:BITRate:CUSTom value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:FLEXray:BITRate:CUSTom <NR1>
            - BUS:B<x>:FLEXray:BITRate:CUSTom?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` is the FlexRay custom bit rate for the specified bus.
        """
        return self._custom


class BusBItemFlexray(SCPICmdRead):
    """The ``BUS:B<x>:FLEXray`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:FLEXray:BITRate`` command.
        - ``.channel``: The ``BUS:B<x>:FLEXray:CHannel`` command.
        - ``.lowthreshold``: The ``BUS:B<x>:FLEXray:LOWTHRESHold`` command.
        - ``.signal``: The ``BUS:B<x>:FLEXray:SIGnal`` command.
        - ``.source``: The ``BUS:B<x>:FLEXray:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:FLEXray:THRESHold`` command.
        - ``.txrxthreshold``: The ``BUS:B<x>:FLEXray:TXRXTHRESHold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemFlexrayBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._channel = BusBItemFlexrayChannel(device, f"{self._cmd_syntax}:CHannel")
        self._lowthreshold = BusBItemFlexrayLowthreshold(device, f"{self._cmd_syntax}:LOWTHRESHold")
        self._signal = BusBItemFlexraySignal(device, f"{self._cmd_syntax}:SIGnal")
        self._source = BusBItemFlexraySource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemFlexrayThreshold(device, f"{self._cmd_syntax}:THRESHold")
        self._txrxthreshold = BusBItemFlexrayTxrxthreshold(
            device, f"{self._cmd_syntax}:TXRXTHRESHold"
        )

    @property
    def bitrate(self) -> BusBItemFlexrayBitrate:
        """Return the ``BUS:B<x>:FLEXray:BITRate`` command.

        Description:
            - This command sets or queries the FlexRay bus bit rate. The bus is specified by x. If
              you select Custom, use ``BUS:BX:FLEXRAY:BITRATE:CUSTOM`` to set the bit rate.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:BITRate?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXray:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:FLEXray:BITRate {CUSTOM|RATE2M|RATE5M|RATE10M}
            - BUS:B<x>:FLEXray:BITRate?
            ```

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.custom``: The ``BUS:B<x>:FLEXray:BITRate:CUSTom`` command.
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
    def lowthreshold(self) -> BusBItemFlexrayLowthreshold:
        """Return the ``BUS:B<x>:FLEXray:LOWTHRESHold`` command.

        Description:
            - This command sets or queries the FlexRay data source low threshold for the specified
              bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:LOWTHRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:LOWTHRESHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:FLEXray:LOWTHRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:FLEXray:LOWTHRESHold <NR3>
            - BUS:B<x>:FLEXray:LOWTHRESHold?
            ```

        Info:
            - ``<NR3>`` is the FlexRay data source low threshold for the specified bus.
            - ``B<x>`` is the number of the bus.
        """
        return self._lowthreshold

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
            - This command sets or queries the Flexray bus data source for the specified bus when
              the signal type is BDIFFBP or BM. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXray:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:FLEXray:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:FLEXray:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``Math<x>`` specifies a math waveform as the source.
            - ``REF<x>`` specifies a reference waveform as the source.

        Sub-properties:
            - ``.txrx``: The ``BUS:B<x>:FLEXray:SOUrce:TXRX`` command.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemFlexrayThreshold:
        """Return the ``BUS:B<x>:FLEXray:THRESHold`` command.

        Description:
            - This command sets or queries the FlexRay data source high threshold for the specified
              bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:THRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:THRESHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXray:THRESHold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:FLEXray:THRESHold <NR3>
            - BUS:B<x>:FLEXray:THRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the FlexRay data source high threshold for the specified bus.
        """
        return self._threshold

    @property
    def txrxthreshold(self) -> BusBItemFlexrayTxrxthreshold:
        """Return the ``BUS:B<x>:FLEXray:TXRXTHRESHold`` command.

        Description:
            - This command sets or queries the FlexRay data source TxRx threshold for the specified
              bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:TXRXTHRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:TXRXTHRESHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:FLEXray:TXRXTHRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:FLEXray:TXRXTHRESHold <NR3>
            - BUS:B<x>:FLEXray:TXRXTHRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the TxRx threshold.
        """
        return self._txrxthreshold


class BusBItemEusbThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:EUSB:THRESHold`` command.

    Description:
        - This command sets or queries the eUSB source High threshold for the specified bus when
          signal type is Diff.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:THRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:THRESHold?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:EUSB:THRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:EUSB:THRESHold <NR3>
        - BUS:B<x>:EUSB:THRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the eUSB Strobe threshold for the specified bus. The argument range is -8 V
          to +8 V.
    """


class BusBItemEusbSourceDplus(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:EUSB:SOUrce:DPLUs`` command.

    Description:
        - This command sets or queries the eUSB dataPlus (SDATAPLUS) source for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:SOUrce:DPLUs?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:SOUrce:DPLUs?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:EUSB:SOUrce:DPLUs value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:EUSB:SOUrce:DPLUs {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:EUSB:SOUrce:DPLUs?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``Math<x>`` specifies a math waveform as the source.
        - ``REF<x>`` specifies a reference waveform as the source.
    """


class BusBItemEusbSourceDminus(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:EUSB:SOUrce:DMINus`` command.

    Description:
        - This command sets or queries the eUSB DataMinus (SDATAMINUS) source for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:SOUrce:DMINus?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:SOUrce:DMINus?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:EUSB:SOUrce:DMINus value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:EUSB:SOUrce:DMINus {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:EUSB:SOUrce:DMINus?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``Math<x>`` specifies a math waveform as the source.
        - ``REF<x>`` specifies a reference waveform as the source.
    """


class BusBItemEusbSourceDiff(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:EUSB:SOUrce:DIFF`` command.

    Description:
        - This command sets or queries the eUSB Diff source for the specified bus when signal type
          is Diff.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:SOUrce:DIFF?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:SOUrce:DIFF?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:EUSB:SOUrce:DIFF value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:EUSB:SOUrce:DIFF {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:EUSB:SOUrce:DIFF?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``Math<x>`` specifies a math waveform as the source.
        - ``REF<x>`` specifies a reference waveform as the source.
    """


class BusBItemEusbSource(SCPICmdRead):
    """The ``BUS:B<x>:EUSB:SOUrce`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.diff``: The ``BUS:B<x>:EUSB:SOUrce:DIFF`` command.
        - ``.dminus``: The ``BUS:B<x>:EUSB:SOUrce:DMINus`` command.
        - ``.dplus``: The ``BUS:B<x>:EUSB:SOUrce:DPLUs`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._diff = BusBItemEusbSourceDiff(device, f"{self._cmd_syntax}:DIFF")
        self._dminus = BusBItemEusbSourceDminus(device, f"{self._cmd_syntax}:DMINus")
        self._dplus = BusBItemEusbSourceDplus(device, f"{self._cmd_syntax}:DPLUs")

    @property
    def diff(self) -> BusBItemEusbSourceDiff:
        """Return the ``BUS:B<x>:EUSB:SOUrce:DIFF`` command.

        Description:
            - This command sets or queries the eUSB Diff source for the specified bus when signal
              type is Diff.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:SOUrce:DIFF?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:SOUrce:DIFF?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:EUSB:SOUrce:DIFF value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:EUSB:SOUrce:DIFF {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:EUSB:SOUrce:DIFF?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``Math<x>`` specifies a math waveform as the source.
            - ``REF<x>`` specifies a reference waveform as the source.
        """
        return self._diff

    @property
    def dminus(self) -> BusBItemEusbSourceDminus:
        """Return the ``BUS:B<x>:EUSB:SOUrce:DMINus`` command.

        Description:
            - This command sets or queries the eUSB DataMinus (SDATAMINUS) source for the specified
              bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:SOUrce:DMINus?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:SOUrce:DMINus?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:EUSB:SOUrce:DMINus value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:EUSB:SOUrce:DMINus {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:EUSB:SOUrce:DMINus?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``Math<x>`` specifies a math waveform as the source.
            - ``REF<x>`` specifies a reference waveform as the source.
        """
        return self._dminus

    @property
    def dplus(self) -> BusBItemEusbSourceDplus:
        """Return the ``BUS:B<x>:EUSB:SOUrce:DPLUs`` command.

        Description:
            - This command sets or queries the eUSB dataPlus (SDATAPLUS) source for the specified
              bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:SOUrce:DPLUs?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:SOUrce:DPLUs?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:EUSB:SOUrce:DPLUs value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:EUSB:SOUrce:DPLUs {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:EUSB:SOUrce:DPLUs?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``Math<x>`` specifies a math waveform as the source.
            - ``REF<x>`` specifies a reference waveform as the source.
        """
        return self._dplus


class BusBItemEusbSignaltype(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:EUSB:SIGNALTYpe`` command.

    Description:
        - This command sets or queries the eUSB signal type for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:SIGNALTYpe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:SIGNALTYpe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:EUSB:SIGNALTYpe value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:EUSB:SIGNALTYpe {SINGLE|DIFF}
        - BUS:B<x>:EUSB:SIGNALTYpe?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
    """


class BusBItemEusbOperatingMode(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:EUSB:OPERating:MODe`` command.

    Description:
        - This command sets or queries the eUSB mode for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:OPERating:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:OPERating:MODe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:EUSB:OPERating:MODe value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:EUSB:OPERating:MODe {NATive|REPEATERHOSt|REPEATERPERIPHERAL}
        - BUS:B<x>:EUSB:OPERating:MODe?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``NATive`` sets the operating mode as native.
        - ``REPEATERHOSt`` sets the operating mode as repeater host.
        - ``REPEATERPERIPHERAL`` sets the operating mode as repeater peripheral.
    """


class BusBItemEusbOperating(SCPICmdRead):
    """The ``BUS:B<x>:EUSB:OPERating`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:OPERating?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:OPERating?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.mode``: The ``BUS:B<x>:EUSB:OPERating:MODe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = BusBItemEusbOperatingMode(device, f"{self._cmd_syntax}:MODe")

    @property
    def mode(self) -> BusBItemEusbOperatingMode:
        """Return the ``BUS:B<x>:EUSB:OPERating:MODe`` command.

        Description:
            - This command sets or queries the eUSB mode for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:OPERating:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:OPERating:MODe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:EUSB:OPERating:MODe value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:EUSB:OPERating:MODe {NATive|REPEATERHOSt|REPEATERPERIPHERAL}
            - BUS:B<x>:EUSB:OPERating:MODe?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``NATive`` sets the operating mode as native.
            - ``REPEATERHOSt`` sets the operating mode as repeater host.
            - ``REPEATERPERIPHERAL`` sets the operating mode as repeater peripheral.
        """
        return self._mode


class BusBItemEusbLowthreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:EUSB:LOWTHRESHold`` command.

    Description:
        - This command sets or queries the eUSB source Low threshold for the specified bus when
          signal type is Differential.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:LOWTHRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:LOWTHRESHold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:EUSB:LOWTHRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:EUSB:LOWTHRESHold <NR3>
        - BUS:B<x>:EUSB:LOWTHRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the eUSB Strobe threshold for the specified bus. The argument range is -8 V
          to +8 V.
    """


class BusBItemEusbDataplusthreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:EUSB:DATAPLUSTHRESHold`` command.

    Description:
        - This command sets or queries the eUSB DATA Plus source threshold for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:DATAPLUSTHRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:DATAPLUSTHRESHold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:EUSB:DATAPLUSTHRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:EUSB:DATAPLUSTHRESHold <NR3>
        - BUS:B<x>:EUSB:DATAPLUSTHRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the eUSB DATA Plus source threshold. The argument range is -8 V to +8 V.
    """


class BusBItemEusbDataplusDataThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:EUSB:DATAPLUS:DATA:THRESHold`` command.

    Description:
        - This command sets or queries the eUSB D+ Input Source Data Threshold for Data line decode
          for specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:DATAPLUS:DATA:THRESHold?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``BUS:B<x>:EUSB:DATAPLUS:DATA:THRESHold?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:EUSB:DATAPLUS:DATA:THRESHold value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:EUSB:DATAPLUS:DATA:THRESHold <NR3>
        - BUS:B<x>:EUSB:DATAPLUS:DATA:THRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the eUSB Strobe threshold for the specified bus. The argument range is -8 V
          to +8 V.
    """


class BusBItemEusbDataplusData(SCPICmdRead):
    """The ``BUS:B<x>:EUSB:DATAPLUS:DATA`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:DATAPLUS:DATA?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:DATAPLUS:DATA?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.threshold``: The ``BUS:B<x>:EUSB:DATAPLUS:DATA:THRESHold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._threshold = BusBItemEusbDataplusDataThreshold(device, f"{self._cmd_syntax}:THRESHold")

    @property
    def threshold(self) -> BusBItemEusbDataplusDataThreshold:
        """Return the ``BUS:B<x>:EUSB:DATAPLUS:DATA:THRESHold`` command.

        Description:
            - This command sets or queries the eUSB D+ Input Source Data Threshold for Data line
              decode for specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:DATAPLUS:DATA:THRESHold?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:EUSB:DATAPLUS:DATA:THRESHold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:EUSB:DATAPLUS:DATA:THRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:EUSB:DATAPLUS:DATA:THRESHold <NR3>
            - BUS:B<x>:EUSB:DATAPLUS:DATA:THRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the eUSB Strobe threshold for the specified bus. The argument range is -8
              V to +8 V.
        """
        return self._threshold


class BusBItemEusbDataplus(SCPICmdRead):
    """The ``BUS:B<x>:EUSB:DATAPLUS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:DATAPLUS?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:DATAPLUS?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.data``: The ``BUS:B<x>:EUSB:DATAPLUS:DATA`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._data = BusBItemEusbDataplusData(device, f"{self._cmd_syntax}:DATA")

    @property
    def data(self) -> BusBItemEusbDataplusData:
        """Return the ``BUS:B<x>:EUSB:DATAPLUS:DATA`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:DATAPLUS:DATA?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:DATAPLUS:DATA?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.threshold``: The ``BUS:B<x>:EUSB:DATAPLUS:DATA:THRESHold`` command.
        """
        return self._data


class BusBItemEusbDataminusthreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:EUSB:DATAMINUSTHRESHold`` command.

    Description:
        - This command sets or queries the eUSB D- Input Source Data Threshold for Data line decode
          for specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:DATAMINUSTHRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:DATAMINUSTHRESHold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:EUSB:DATAMINUSTHRESHold value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:EUSB:DATAMINUSTHRESHold <NR3>
        - BUS:B<x>:EUSB:DATAMINUSTHRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the eUSB DATA Minus source threshold. The argument range is -8 V to +8 V.
    """


class BusBItemEusbDataminusDataThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:EUSB:DATAMINUS:DATA:THRESHold`` command.

    Description:
        - This command sets or queries the eUSB D- Input Source Data Threshold for Data line decode
          for specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:DATAMINUS:DATA:THRESHold?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``BUS:B<x>:EUSB:DATAMINUS:DATA:THRESHold?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:EUSB:DATAMINUS:DATA:THRESHold value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:EUSB:DATAMINUS:DATA:THRESHold <NR3>
        - BUS:B<x>:EUSB:DATAMINUS:DATA:THRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the EUSB Strobe threshold for the specified bus. The argument range is -8 V
          to +8 V.
    """


class BusBItemEusbDataminusData(SCPICmdRead):
    """The ``BUS:B<x>:EUSB:DATAMINUS:DATA`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:DATAMINUS:DATA?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:DATAMINUS:DATA?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.threshold``: The ``BUS:B<x>:EUSB:DATAMINUS:DATA:THRESHold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._threshold = BusBItemEusbDataminusDataThreshold(
            device, f"{self._cmd_syntax}:THRESHold"
        )

    @property
    def threshold(self) -> BusBItemEusbDataminusDataThreshold:
        """Return the ``BUS:B<x>:EUSB:DATAMINUS:DATA:THRESHold`` command.

        Description:
            - This command sets or queries the eUSB D- Input Source Data Threshold for Data line
              decode for specified bus.

        Usage:
            - Using the ``.query()`` method will send the
              ``BUS:B<x>:EUSB:DATAMINUS:DATA:THRESHold?`` query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:EUSB:DATAMINUS:DATA:THRESHold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:EUSB:DATAMINUS:DATA:THRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:EUSB:DATAMINUS:DATA:THRESHold <NR3>
            - BUS:B<x>:EUSB:DATAMINUS:DATA:THRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the EUSB Strobe threshold for the specified bus. The argument range is -8
              V to +8 V.
        """
        return self._threshold


class BusBItemEusbDataminus(SCPICmdRead):
    """The ``BUS:B<x>:EUSB:DATAMINUS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:DATAMINUS?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:DATAMINUS?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.data``: The ``BUS:B<x>:EUSB:DATAMINUS:DATA`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._data = BusBItemEusbDataminusData(device, f"{self._cmd_syntax}:DATA")

    @property
    def data(self) -> BusBItemEusbDataminusData:
        """Return the ``BUS:B<x>:EUSB:DATAMINUS:DATA`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:DATAMINUS:DATA?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:DATAMINUS:DATA?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.threshold``: The ``BUS:B<x>:EUSB:DATAMINUS:DATA:THRESHold`` command.
        """
        return self._data


class BusBItemEusbBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:EUSB:BITRate`` command.

    Description:
        - This command sets or queries the eUSB data rate for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:EUSB:BITRate value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:EUSB:BITRate {HIGH|FULL|LOW}
        - BUS:B<x>:EUSB:BITRate?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``HIGH`` sets the bit rate to Bit Rate to 480 Mbps.
        - ``FULL`` sets the bit rate to Bit Rate to 12 Mbps.
        - ``LOW`` sets the bit rate to Bit Rate to 1.5 Mbps.
    """


#  pylint: disable=too-many-instance-attributes
class BusBItemEusb(SCPICmdRead):
    """The ``BUS:B<x>:EUSB`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:EUSB:BITRate`` command.
        - ``.dataminus``: The ``BUS:B<x>:EUSB:DATAMINUS`` command tree.
        - ``.dataminusthreshold``: The ``BUS:B<x>:EUSB:DATAMINUSTHRESHold`` command.
        - ``.dataplus``: The ``BUS:B<x>:EUSB:DATAPLUS`` command tree.
        - ``.dataplusthreshold``: The ``BUS:B<x>:EUSB:DATAPLUSTHRESHold`` command.
        - ``.lowthreshold``: The ``BUS:B<x>:EUSB:LOWTHRESHold`` command.
        - ``.operating``: The ``BUS:B<x>:EUSB:OPERating`` command tree.
        - ``.signaltype``: The ``BUS:B<x>:EUSB:SIGNALTYpe`` command.
        - ``.source``: The ``BUS:B<x>:EUSB:SOUrce`` command tree.
        - ``.threshold``: The ``BUS:B<x>:EUSB:THRESHold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemEusbBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._dataminus = BusBItemEusbDataminus(device, f"{self._cmd_syntax}:DATAMINUS")
        self._dataminusthreshold = BusBItemEusbDataminusthreshold(
            device, f"{self._cmd_syntax}:DATAMINUSTHRESHold"
        )
        self._dataplus = BusBItemEusbDataplus(device, f"{self._cmd_syntax}:DATAPLUS")
        self._dataplusthreshold = BusBItemEusbDataplusthreshold(
            device, f"{self._cmd_syntax}:DATAPLUSTHRESHold"
        )
        self._lowthreshold = BusBItemEusbLowthreshold(device, f"{self._cmd_syntax}:LOWTHRESHold")
        self._operating = BusBItemEusbOperating(device, f"{self._cmd_syntax}:OPERating")
        self._signaltype = BusBItemEusbSignaltype(device, f"{self._cmd_syntax}:SIGNALTYpe")
        self._source = BusBItemEusbSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemEusbThreshold(device, f"{self._cmd_syntax}:THRESHold")

    @property
    def bitrate(self) -> BusBItemEusbBitrate:
        """Return the ``BUS:B<x>:EUSB:BITRate`` command.

        Description:
            - This command sets or queries the eUSB data rate for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:BITRate?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:EUSB:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:EUSB:BITRate {HIGH|FULL|LOW}
            - BUS:B<x>:EUSB:BITRate?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``HIGH`` sets the bit rate to Bit Rate to 480 Mbps.
            - ``FULL`` sets the bit rate to Bit Rate to 12 Mbps.
            - ``LOW`` sets the bit rate to Bit Rate to 1.5 Mbps.
        """
        return self._bitrate

    @property
    def dataminus(self) -> BusBItemEusbDataminus:
        """Return the ``BUS:B<x>:EUSB:DATAMINUS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:DATAMINUS?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:DATAMINUS?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.data``: The ``BUS:B<x>:EUSB:DATAMINUS:DATA`` command tree.
        """
        return self._dataminus

    @property
    def dataminusthreshold(self) -> BusBItemEusbDataminusthreshold:
        """Return the ``BUS:B<x>:EUSB:DATAMINUSTHRESHold`` command.

        Description:
            - This command sets or queries the eUSB D- Input Source Data Threshold for Data line
              decode for specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:DATAMINUSTHRESHold?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:EUSB:DATAMINUSTHRESHold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:EUSB:DATAMINUSTHRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:EUSB:DATAMINUSTHRESHold <NR3>
            - BUS:B<x>:EUSB:DATAMINUSTHRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the eUSB DATA Minus source threshold. The argument range is -8 V to +8 V.
        """
        return self._dataminusthreshold

    @property
    def dataplus(self) -> BusBItemEusbDataplus:
        """Return the ``BUS:B<x>:EUSB:DATAPLUS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:DATAPLUS?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:DATAPLUS?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.data``: The ``BUS:B<x>:EUSB:DATAPLUS:DATA`` command tree.
        """
        return self._dataplus

    @property
    def dataplusthreshold(self) -> BusBItemEusbDataplusthreshold:
        """Return the ``BUS:B<x>:EUSB:DATAPLUSTHRESHold`` command.

        Description:
            - This command sets or queries the eUSB DATA Plus source threshold for the specified
              bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:DATAPLUSTHRESHold?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:DATAPLUSTHRESHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:EUSB:DATAPLUSTHRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:EUSB:DATAPLUSTHRESHold <NR3>
            - BUS:B<x>:EUSB:DATAPLUSTHRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the eUSB DATA Plus source threshold. The argument range is -8 V to +8 V.
        """
        return self._dataplusthreshold

    @property
    def lowthreshold(self) -> BusBItemEusbLowthreshold:
        """Return the ``BUS:B<x>:EUSB:LOWTHRESHold`` command.

        Description:
            - This command sets or queries the eUSB source Low threshold for the specified bus when
              signal type is Differential.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:LOWTHRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:LOWTHRESHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:EUSB:LOWTHRESHold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:EUSB:LOWTHRESHold <NR3>
            - BUS:B<x>:EUSB:LOWTHRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the eUSB Strobe threshold for the specified bus. The argument range is -8
              V to +8 V.
        """
        return self._lowthreshold

    @property
    def operating(self) -> BusBItemEusbOperating:
        """Return the ``BUS:B<x>:EUSB:OPERating`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:OPERating?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:OPERating?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.mode``: The ``BUS:B<x>:EUSB:OPERating:MODe`` command.
        """
        return self._operating

    @property
    def signaltype(self) -> BusBItemEusbSignaltype:
        """Return the ``BUS:B<x>:EUSB:SIGNALTYpe`` command.

        Description:
            - This command sets or queries the eUSB signal type for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:SIGNALTYpe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:SIGNALTYpe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:EUSB:SIGNALTYpe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:EUSB:SIGNALTYpe {SINGLE|DIFF}
            - BUS:B<x>:EUSB:SIGNALTYpe?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
        """
        return self._signaltype

    @property
    def source(self) -> BusBItemEusbSource:
        """Return the ``BUS:B<x>:EUSB:SOUrce`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.diff``: The ``BUS:B<x>:EUSB:SOUrce:DIFF`` command.
            - ``.dminus``: The ``BUS:B<x>:EUSB:SOUrce:DMINus`` command.
            - ``.dplus``: The ``BUS:B<x>:EUSB:SOUrce:DPLUs`` command.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemEusbThreshold:
        """Return the ``BUS:B<x>:EUSB:THRESHold`` command.

        Description:
            - This command sets or queries the eUSB source High threshold for the specified bus when
              signal type is Diff.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB:THRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB:THRESHold?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:EUSB:THRESHold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:EUSB:THRESHold <NR3>
            - BUS:B<x>:EUSB:THRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the eUSB Strobe threshold for the specified bus. The argument range is -8
              V to +8 V.
        """
        return self._threshold


class BusBItemEthernetType(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ETHERnet:TYPe`` command.

    Description:
        - This command specifies the Ethernet standard speed. The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:TYPe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERnet:TYPe value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERnet:TYPe {TENBASET|HUNDREDBASETX}
        - BUS:B<x>:ETHERnet:TYPe?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``TENBASET`` specifies the Ethernet speed as 10Base-T.
        - ``HUNDREDBASETX`` specifies the Ethernet speed as 100Base-T.
    """


class BusBItemEthernetThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ETHERnet:THRESHold`` command.

    Description:
        - This command sets or queries the Ethernet DATA source High threshold for the specified
          bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:THRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:THRESHold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERnet:THRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERnet:THRESHold <NR3>
        - BUS:B<x>:ETHERnet:THRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the Ethernet DATA source High threshold for the specified bus.
    """


class BusBItemEthernetSourceDplus(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ETHERnet:SOUrce:DPLUs`` command.

    Description:
        - This command sets or queries the Ethernet D+ source for the specified bus. this command
          specifies the source channel to use when the signal type is single ended. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DPLUs?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DPLUs?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DPLUs value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERnet:SOUrce:DPLUs {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:ETHERnet:SOUrce:DPLUs?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``Math<x>`` specifies a math waveform as the source.
        - ``REF<x>`` specifies a reference waveform as the source.
    """


class BusBItemEthernetSourceDminus(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ETHERnet:SOUrce:DMINus`` command.

    Description:
        - This command sets or queries the Ethernet D- source for the specified bus. this command
          specifies the source channel to use when the signal type is single ended. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DMINus?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DMINus?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DMINus value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERnet:SOUrce:DMINus {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:ETHERnet:SOUrce:DMINus?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``Math<x>`` specifies a math waveform as the source.
        - ``REF<x>`` specifies a reference waveform as the source.
    """


class BusBItemEthernetSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ETHERnet:SOUrce`` command.

    Description:
        - This command sets or queries the Ethernet data (SDATA) source for the specified bus. This
          command controls the source channel when the signal type is differential. The bus number
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERnet:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:ETHERnet:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies to use one of the analog channels as the Ethernet data source for
          differential input.
        - ``MATH<x>`` specifies to use a math waveform as the source for Ethernet data differential
          input.
        - ``REF<x>`` specifies to use one of the reference waveforms as the Ethernet data source for
          differential input.

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
            - This command sets or queries the Ethernet D- source for the specified bus. this
              command specifies the source channel to use when the signal type is single ended. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DMINus?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DMINus?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ETHERnet:SOUrce:DMINus value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERnet:SOUrce:DMINus {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:ETHERnet:SOUrce:DMINus?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``Math<x>`` specifies a math waveform as the source.
            - ``REF<x>`` specifies a reference waveform as the source.
        """
        return self._dminus

    @property
    def dplus(self) -> BusBItemEthernetSourceDplus:
        """Return the ``BUS:B<x>:ETHERnet:SOUrce:DPLUs`` command.

        Description:
            - This command sets or queries the Ethernet D+ source for the specified bus. this
              command specifies the source channel to use when the signal type is single ended. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DPLUs?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce:DPLUs?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ETHERnet:SOUrce:DPLUs value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERnet:SOUrce:DPLUs {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:ETHERnet:SOUrce:DPLUs?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``Math<x>`` specifies a math waveform as the source.
            - ``REF<x>`` specifies a reference waveform as the source.
        """
        return self._dplus


class BusBItemEthernetSignaltype(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ETHERnet:SIGNALTYpe`` command.

    Description:
        - This command sets or queries the Ethernet signal type for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:SIGNALTYpe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:SIGNALTYpe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERnet:SIGNALTYpe value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERnet:SIGNALTYpe {SINGLE|DIFF}
        - BUS:B<x>:ETHERnet:SIGNALTYpe?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``SINGLE`` specifies single-ended signals.
        - ``DIFF`` specifies differential signals.
    """


class BusBItemEthernetQtagging(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ETHERnet:QTAGGING`` command.

    Description:
        - This command sets or queries whether Q-Tagging packets are available for triggering on
          Ethernet. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:QTAGGING?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:QTAGGING?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERnet:QTAGGING value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERnet:QTAGGING {YES|NO}
        - BUS:B<x>:ETHERnet:QTAGGING?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``YES`` specifies that Q-Tagging packets are available.
        - ``NO`` specifies that Q-Tagging packets are not available.
    """


class BusBItemEthernetLowthreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ETHERnet:LOWTHRESHold`` command.

    Description:
        - This command sets or queries the Ethernet source Low threshold for the specified bus. This
          threshold only applies when the Ethernet signal type is differential. The bus is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:LOWTHRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:LOWTHRESHold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERnet:LOWTHRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERnet:LOWTHRESHold <NR3>
        - BUS:B<x>:ETHERnet:LOWTHRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the Ethernet source Low threshold for the specified bus.
    """


class BusBItemEthernetIpvfour(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ETHERnet:IPVFOUR`` command.

    Description:
        - This command sets or queries whether IPV4 packets are available for triggering on
          Ethernet. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:IPVFOUR?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:IPVFOUR?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERnet:IPVFOUR value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERnet:IPVFOUR {YES|NO}
        - BUS:B<x>:ETHERnet:IPVFOUR?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``YES`` specifies that IPV4 packets are available.
        - ``NO`` specifies that IPV4 packets are not available.
    """


class BusBItemEthernetDataplusthreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ETHERnet:DATAPLUSTHRESHold`` command.

    Description:
        - This command sets or queries the Ethernet D+ source threshold for the specified bus. This
          threshold only applies when the Ethernet signal type is single ended. The bus is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:DATAPLUSTHRESHold?``
          query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:DATAPLUSTHRESHold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:ETHERnet:DATAPLUSTHRESHold value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERnet:DATAPLUSTHRESHold <NR3>
        - BUS:B<x>:ETHERnet:DATAPLUSTHRESHold?
        ```

    Info:
        - ``B<x>`` is the Bus number.
        - ``<NR3>`` is the Ethernet D+ source threshold for the specified bus.
    """


class BusBItemEthernetDataminusthreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ETHERnet:DATAMINUSTHRESHold`` command.

    Description:
        - This command sets or queries the Ethernet D- source threshold for the specified bus. This
          threshold only applies when the Ethernet signal type is single ended. The bus is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:DATAMINUSTHRESHold?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``BUS:B<x>:ETHERnet:DATAMINUSTHRESHold?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:ETHERnet:DATAMINUSTHRESHold value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERnet:DATAMINUSTHRESHold <NR3>
        - BUS:B<x>:ETHERnet:DATAMINUSTHRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the Ethernet D- source threshold for the specified bus.
    """


#  pylint: disable=too-many-instance-attributes
class BusBItemEthernet(SCPICmdRead):
    """The ``BUS:B<x>:ETHERnet`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.dataminusthreshold``: The ``BUS:B<x>:ETHERnet:DATAMINUSTHRESHold`` command.
        - ``.dataplusthreshold``: The ``BUS:B<x>:ETHERnet:DATAPLUSTHRESHold`` command.
        - ``.ipvfour``: The ``BUS:B<x>:ETHERnet:IPVFOUR`` command.
        - ``.lowthreshold``: The ``BUS:B<x>:ETHERnet:LOWTHRESHold`` command.
        - ``.qtagging``: The ``BUS:B<x>:ETHERnet:QTAGGING`` command.
        - ``.signaltype``: The ``BUS:B<x>:ETHERnet:SIGNALTYpe`` command.
        - ``.source``: The ``BUS:B<x>:ETHERnet:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:ETHERnet:THRESHold`` command.
        - ``.type``: The ``BUS:B<x>:ETHERnet:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._dataminusthreshold = BusBItemEthernetDataminusthreshold(
            device, f"{self._cmd_syntax}:DATAMINUSTHRESHold"
        )
        self._dataplusthreshold = BusBItemEthernetDataplusthreshold(
            device, f"{self._cmd_syntax}:DATAPLUSTHRESHold"
        )
        self._ipvfour = BusBItemEthernetIpvfour(device, f"{self._cmd_syntax}:IPVFOUR")
        self._lowthreshold = BusBItemEthernetLowthreshold(
            device, f"{self._cmd_syntax}:LOWTHRESHold"
        )
        self._qtagging = BusBItemEthernetQtagging(device, f"{self._cmd_syntax}:QTAGGING")
        self._signaltype = BusBItemEthernetSignaltype(device, f"{self._cmd_syntax}:SIGNALTYpe")
        self._source = BusBItemEthernetSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemEthernetThreshold(device, f"{self._cmd_syntax}:THRESHold")
        self._type = BusBItemEthernetType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def dataminusthreshold(self) -> BusBItemEthernetDataminusthreshold:
        """Return the ``BUS:B<x>:ETHERnet:DATAMINUSTHRESHold`` command.

        Description:
            - This command sets or queries the Ethernet D- source threshold for the specified bus.
              This threshold only applies when the Ethernet signal type is single ended. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:DATAMINUSTHRESHold?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:ETHERnet:DATAMINUSTHRESHold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ETHERnet:DATAMINUSTHRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERnet:DATAMINUSTHRESHold <NR3>
            - BUS:B<x>:ETHERnet:DATAMINUSTHRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the Ethernet D- source threshold for the specified bus.
        """
        return self._dataminusthreshold

    @property
    def dataplusthreshold(self) -> BusBItemEthernetDataplusthreshold:
        """Return the ``BUS:B<x>:ETHERnet:DATAPLUSTHRESHold`` command.

        Description:
            - This command sets or queries the Ethernet D+ source threshold for the specified bus.
              This threshold only applies when the Ethernet signal type is single ended. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:DATAPLUSTHRESHold?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:ETHERnet:DATAPLUSTHRESHold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ETHERnet:DATAPLUSTHRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERnet:DATAPLUSTHRESHold <NR3>
            - BUS:B<x>:ETHERnet:DATAPLUSTHRESHold?
            ```

        Info:
            - ``B<x>`` is the Bus number.
            - ``<NR3>`` is the Ethernet D+ source threshold for the specified bus.
        """
        return self._dataplusthreshold

    @property
    def ipvfour(self) -> BusBItemEthernetIpvfour:
        """Return the ``BUS:B<x>:ETHERnet:IPVFOUR`` command.

        Description:
            - This command sets or queries whether IPV4 packets are available for triggering on
              Ethernet. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:IPVFOUR?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:IPVFOUR?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERnet:IPVFOUR value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERnet:IPVFOUR {YES|NO}
            - BUS:B<x>:ETHERnet:IPVFOUR?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``YES`` specifies that IPV4 packets are available.
            - ``NO`` specifies that IPV4 packets are not available.
        """
        return self._ipvfour

    @property
    def lowthreshold(self) -> BusBItemEthernetLowthreshold:
        """Return the ``BUS:B<x>:ETHERnet:LOWTHRESHold`` command.

        Description:
            - This command sets or queries the Ethernet source Low threshold for the specified bus.
              This threshold only applies when the Ethernet signal type is differential. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:LOWTHRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:LOWTHRESHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ETHERnet:LOWTHRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERnet:LOWTHRESHold <NR3>
            - BUS:B<x>:ETHERnet:LOWTHRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the Ethernet source Low threshold for the specified bus.
        """
        return self._lowthreshold

    @property
    def qtagging(self) -> BusBItemEthernetQtagging:
        """Return the ``BUS:B<x>:ETHERnet:QTAGGING`` command.

        Description:
            - This command sets or queries whether Q-Tagging packets are available for triggering on
              Ethernet. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:QTAGGING?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:QTAGGING?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERnet:QTAGGING value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERnet:QTAGGING {YES|NO}
            - BUS:B<x>:ETHERnet:QTAGGING?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``YES`` specifies that Q-Tagging packets are available.
            - ``NO`` specifies that Q-Tagging packets are not available.
        """
        return self._qtagging

    @property
    def signaltype(self) -> BusBItemEthernetSignaltype:
        """Return the ``BUS:B<x>:ETHERnet:SIGNALTYpe`` command.

        Description:
            - This command sets or queries the Ethernet signal type for the specified bus. The bus
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:SIGNALTYpe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:SIGNALTYpe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ETHERnet:SIGNALTYpe value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERnet:SIGNALTYpe {SINGLE|DIFF}
            - BUS:B<x>:ETHERnet:SIGNALTYpe?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``SINGLE`` specifies single-ended signals.
            - ``DIFF`` specifies differential signals.
        """
        return self._signaltype

    @property
    def source(self) -> BusBItemEthernetSource:
        """Return the ``BUS:B<x>:ETHERnet:SOUrce`` command.

        Description:
            - This command sets or queries the Ethernet data (SDATA) source for the specified bus.
              This command controls the source channel when the signal type is differential. The bus
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERnet:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERnet:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:ETHERnet:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies to use one of the analog channels as the Ethernet data source for
              differential input.
            - ``MATH<x>`` specifies to use a math waveform as the source for Ethernet data
              differential input.
            - ``REF<x>`` specifies to use one of the reference waveforms as the Ethernet data source
              for differential input.

        Sub-properties:
            - ``.dminus``: The ``BUS:B<x>:ETHERnet:SOUrce:DMINus`` command.
            - ``.dplus``: The ``BUS:B<x>:ETHERnet:SOUrce:DPLUs`` command.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemEthernetThreshold:
        """Return the ``BUS:B<x>:ETHERnet:THRESHold`` command.

        Description:
            - This command sets or queries the Ethernet DATA source High threshold for the specified
              bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:THRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:THRESHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERnet:THRESHold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERnet:THRESHold <NR3>
            - BUS:B<x>:ETHERnet:THRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the Ethernet DATA source High threshold for the specified bus.
        """
        return self._threshold

    @property
    def type(self) -> BusBItemEthernetType:
        """Return the ``BUS:B<x>:ETHERnet:TYPe`` command.

        Description:
            - This command specifies the Ethernet standard speed. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet:TYPe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERnet:TYPe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERnet:TYPe {TENBASET|HUNDREDBASETX}
            - BUS:B<x>:ETHERnet:TYPe?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``TENBASET`` specifies the Ethernet speed as 10Base-T.
            - ``HUNDREDBASETX`` specifies the Ethernet speed as 100Base-T.
        """
        return self._type


class BusBItemEthercatThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ETHERCAT:THRESHold`` command.

    Description:
        - This command sets or queries the differential source threshold for the specified EtherCAT
          bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERCAT:THRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERCAT:THRESHold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERCAT:THRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERCAT:THRESHold <NR3>
        - BUS:B<x>:ETHERCAT:THRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` specifies the EtherCAT differential Source threshold for the specified bus. The
          default value is 0 V. The valid range is -8 V to +8 V.
    """


class BusBItemEthercatSourceDplus(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ETHERCAT:SOUrce:DPLUs`` command.

    Description:
        - This command sets or queries the DataPlus (SDATAPLUS) source for the specified EtherCAT
          bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERCAT:SOUrce:DPLUs?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERCAT:SOUrce:DPLUs?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERCAT:SOUrce:DPLUs value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERCAT:SOUrce:DPLUs {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:ETHERCAT:SOUrce:DPLUs?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies to use one of the analog channels as the DataPlus source.
        - ``MATH<x>`` specifies to use a math waveform as the DataPlus source.
        - ``REF<x>`` specifies to use one of the reference waveforms as the DataPlus source.
    """


class BusBItemEthercatSourceDminus(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ETHERCAT:SOUrce:DMINus`` command.

    Description:
        - This command sets or queries the DataMinus (SDATAMINUS) source for the specified EtherCAT
          bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERCAT:SOUrce:DMINus?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERCAT:SOUrce:DMINus?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERCAT:SOUrce:DMINus value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERCAT:SOUrce:DMINus {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:ETHERCAT:SOUrce:DMINus?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies to use one of the analog channels as the DataMinus source.
        - ``MATH<x>`` specifies to use a math waveform as the DataMinus source.
        - ``REF<x>`` specifies to use one of the reference waveforms as the DataMinus source.
    """


class BusBItemEthercatSourceDiff(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ETHERCAT:SOUrce:DIFF`` command.

    Description:
        - This command sets or queries the differential source for the specified EtherCAT bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERCAT:SOUrce:DIFF?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERCAT:SOUrce:DIFF?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERCAT:SOUrce:DIFF value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERCAT:SOUrce:DIFF {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:ETHERCAT:SOUrce:DIFF?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies to use one of the analog channels as the differential source.
        - ``MATH<x>`` specifies to use a math waveform as the differential source.
        - ``REF<x>`` specifies to use one of the reference waveforms as the differential source.
    """


class BusBItemEthercatSource(SCPICmdRead):
    """The ``BUS:B<x>:ETHERCAT:SOUrce`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERCAT:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERCAT:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.diff``: The ``BUS:B<x>:ETHERCAT:SOUrce:DIFF`` command.
        - ``.dminus``: The ``BUS:B<x>:ETHERCAT:SOUrce:DMINus`` command.
        - ``.dplus``: The ``BUS:B<x>:ETHERCAT:SOUrce:DPLUs`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._diff = BusBItemEthercatSourceDiff(device, f"{self._cmd_syntax}:DIFF")
        self._dminus = BusBItemEthercatSourceDminus(device, f"{self._cmd_syntax}:DMINus")
        self._dplus = BusBItemEthercatSourceDplus(device, f"{self._cmd_syntax}:DPLUs")

    @property
    def diff(self) -> BusBItemEthercatSourceDiff:
        """Return the ``BUS:B<x>:ETHERCAT:SOUrce:DIFF`` command.

        Description:
            - This command sets or queries the differential source for the specified EtherCAT bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERCAT:SOUrce:DIFF?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERCAT:SOUrce:DIFF?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ETHERCAT:SOUrce:DIFF value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERCAT:SOUrce:DIFF {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:ETHERCAT:SOUrce:DIFF?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies to use one of the analog channels as the differential source.
            - ``MATH<x>`` specifies to use a math waveform as the differential source.
            - ``REF<x>`` specifies to use one of the reference waveforms as the differential source.
        """
        return self._diff

    @property
    def dminus(self) -> BusBItemEthercatSourceDminus:
        """Return the ``BUS:B<x>:ETHERCAT:SOUrce:DMINus`` command.

        Description:
            - This command sets or queries the DataMinus (SDATAMINUS) source for the specified
              EtherCAT bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERCAT:SOUrce:DMINus?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERCAT:SOUrce:DMINus?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ETHERCAT:SOUrce:DMINus value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERCAT:SOUrce:DMINus {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:ETHERCAT:SOUrce:DMINus?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies to use one of the analog channels as the DataMinus source.
            - ``MATH<x>`` specifies to use a math waveform as the DataMinus source.
            - ``REF<x>`` specifies to use one of the reference waveforms as the DataMinus source.
        """
        return self._dminus

    @property
    def dplus(self) -> BusBItemEthercatSourceDplus:
        """Return the ``BUS:B<x>:ETHERCAT:SOUrce:DPLUs`` command.

        Description:
            - This command sets or queries the DataPlus (SDATAPLUS) source for the specified
              EtherCAT bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERCAT:SOUrce:DPLUs?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERCAT:SOUrce:DPLUs?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ETHERCAT:SOUrce:DPLUs value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERCAT:SOUrce:DPLUs {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:ETHERCAT:SOUrce:DPLUs?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies to use one of the analog channels as the DataPlus source.
            - ``MATH<x>`` specifies to use a math waveform as the DataPlus source.
            - ``REF<x>`` specifies to use one of the reference waveforms as the DataPlus source.
        """
        return self._dplus


class BusBItemEthercatSignaltype(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ETHERCAT:SIGNALTYpe`` command.

    Description:
        - This command sets or queries the signal type for the specified EtherCAT bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERCAT:SIGNALTYpe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERCAT:SIGNALTYpe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERCAT:SIGNALTYpe value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERCAT:SIGNALTYpe {SINGLE|DIFF}
        - BUS:B<x>:ETHERCAT:SIGNALTYpe?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``SINGLE`` specifies single-ended signals.
        - ``DIFF`` specifies differential signals.
    """


class BusBItemEthercatDataplusthreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ETHERCAT:DATAPLUSTHRESHold`` command.

    Description:
        - This command sets or queries the DATA Plus source threshold for the specified EtherCAT
          bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERCAT:DATAPLUSTHRESHold?``
          query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERCAT:DATAPLUSTHRESHold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:ETHERCAT:DATAPLUSTHRESHold value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERCAT:DATAPLUSTHRESHold <NR3>
        - BUS:B<x>:ETHERCAT:DATAPLUSTHRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the EtherCAT DataPinus source threshold for the specified bus. The valid
          range is -8V to +8V. The default value is 0 V.
    """


class BusBItemEthercatDataminusthreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ETHERCAT:DATAMINUSTHRESHold`` command.

    Description:
        - This command sets or queries the DATA Minus source threshold for the specified EtherCAT
          bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERCAT:DATAMINUSTHRESHold?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``BUS:B<x>:ETHERCAT:DATAMINUSTHRESHold?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:ETHERCAT:DATAMINUSTHRESHold value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ETHERCAT:DATAMINUSTHRESHold <NR3>
        - BUS:B<x>:ETHERCAT:DATAMINUSTHRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the EtherCAT DataMinus source threshold for the specified bus. The valid
          range is -8V to +8V. The default value is 0 V.
    """


class BusBItemEthercat(SCPICmdRead):
    """The ``BUS:B<x>:ETHERCAT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERCAT?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERCAT?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.dataminusthreshold``: The ``BUS:B<x>:ETHERCAT:DATAMINUSTHRESHold`` command.
        - ``.dataplusthreshold``: The ``BUS:B<x>:ETHERCAT:DATAPLUSTHRESHold`` command.
        - ``.signaltype``: The ``BUS:B<x>:ETHERCAT:SIGNALTYpe`` command.
        - ``.source``: The ``BUS:B<x>:ETHERCAT:SOUrce`` command tree.
        - ``.threshold``: The ``BUS:B<x>:ETHERCAT:THRESHold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._dataminusthreshold = BusBItemEthercatDataminusthreshold(
            device, f"{self._cmd_syntax}:DATAMINUSTHRESHold"
        )
        self._dataplusthreshold = BusBItemEthercatDataplusthreshold(
            device, f"{self._cmd_syntax}:DATAPLUSTHRESHold"
        )
        self._signaltype = BusBItemEthercatSignaltype(device, f"{self._cmd_syntax}:SIGNALTYpe")
        self._source = BusBItemEthercatSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemEthercatThreshold(device, f"{self._cmd_syntax}:THRESHold")

    @property
    def dataminusthreshold(self) -> BusBItemEthercatDataminusthreshold:
        """Return the ``BUS:B<x>:ETHERCAT:DATAMINUSTHRESHold`` command.

        Description:
            - This command sets or queries the DATA Minus source threshold for the specified
              EtherCAT bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERCAT:DATAMINUSTHRESHold?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:ETHERCAT:DATAMINUSTHRESHold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ETHERCAT:DATAMINUSTHRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERCAT:DATAMINUSTHRESHold <NR3>
            - BUS:B<x>:ETHERCAT:DATAMINUSTHRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the EtherCAT DataMinus source threshold for the specified bus. The valid
              range is -8V to +8V. The default value is 0 V.
        """
        return self._dataminusthreshold

    @property
    def dataplusthreshold(self) -> BusBItemEthercatDataplusthreshold:
        """Return the ``BUS:B<x>:ETHERCAT:DATAPLUSTHRESHold`` command.

        Description:
            - This command sets or queries the DATA Plus source threshold for the specified EtherCAT
              bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERCAT:DATAPLUSTHRESHold?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:ETHERCAT:DATAPLUSTHRESHold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ETHERCAT:DATAPLUSTHRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERCAT:DATAPLUSTHRESHold <NR3>
            - BUS:B<x>:ETHERCAT:DATAPLUSTHRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the EtherCAT DataPinus source threshold for the specified bus. The valid
              range is -8V to +8V. The default value is 0 V.
        """
        return self._dataplusthreshold

    @property
    def signaltype(self) -> BusBItemEthercatSignaltype:
        """Return the ``BUS:B<x>:ETHERCAT:SIGNALTYpe`` command.

        Description:
            - This command sets or queries the signal type for the specified EtherCAT bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERCAT:SIGNALTYpe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERCAT:SIGNALTYpe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ETHERCAT:SIGNALTYpe value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERCAT:SIGNALTYpe {SINGLE|DIFF}
            - BUS:B<x>:ETHERCAT:SIGNALTYpe?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``SINGLE`` specifies single-ended signals.
            - ``DIFF`` specifies differential signals.
        """
        return self._signaltype

    @property
    def source(self) -> BusBItemEthercatSource:
        """Return the ``BUS:B<x>:ETHERCAT:SOUrce`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERCAT:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERCAT:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.diff``: The ``BUS:B<x>:ETHERCAT:SOUrce:DIFF`` command.
            - ``.dminus``: The ``BUS:B<x>:ETHERCAT:SOUrce:DMINus`` command.
            - ``.dplus``: The ``BUS:B<x>:ETHERCAT:SOUrce:DPLUs`` command.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemEthercatThreshold:
        """Return the ``BUS:B<x>:ETHERCAT:THRESHold`` command.

        Description:
            - This command sets or queries the differential source threshold for the specified
              EtherCAT bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERCAT:THRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERCAT:THRESHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:ETHERCAT:THRESHold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ETHERCAT:THRESHold <NR3>
            - BUS:B<x>:ETHERCAT:THRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` specifies the EtherCAT differential Source threshold for the specified bus.
              The default value is 0 V. The valid range is -8 V to +8 V.
        """
        return self._threshold


class BusBItemEspiIomode(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ESPI:IOMODe`` command.

    Description:
        - This command sets or queries the ESPI Input/Output mode for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:IOMODe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:IOMODe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ESPI:IOMODe value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ESPI:IOMODe {SINGle|DUAL}
        - BUS:B<x>:ESPI:IOMODe?
        ```

    Info:
        - ``B<x>`` is the Bus number.
        - ``SINGle`` displays the command and response decode in two lanes.
        - ``DUAL`` displays the decode in a single data lane.
    """


class BusBItemEspiDatatwoThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ESPI:DATATWO:THReshold`` command.

    Description:
        - This command sets or queries the response (single mode)/ IO[1] (dual mode) Data source
          threshold for the specified bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:DATATWO:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:DATATWO:THReshold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ESPI:DATATWO:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ESPI:DATATWO:THReshold <NR3>
        - BUS:B<x>:ESPI:DATATWO:THReshold?
        ```

    Info:
        - ``B<x>`` is the Bus number.
        - ``<NR3>`` sets the command/data threshold for the specified bus. The valid range is -8V to
          +8V.
    """


class BusBItemEspiDatatwoSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ESPI:DATATWO:SOUrce`` command.

    Description:
        - This command sets or queries the response (single mode)/ IO[1] (dual mode) Data source for
          the specified bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:DATATWO:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:DATATWO:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ESPI:DATATWO:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ESPI:DATATWO:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
        - BUS:B<x>:ESPI:DATATWO:SOUrce?
        ```

    Info:
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``Math<x>`` specifies a math waveform as the source.
        - ``REF<x>`` specifies a reference waveform as the source.
    """


class BusBItemEspiDatatwoPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ESPI:DATATWO:POLarity`` command.

    Description:
        - This command sets or queries the ESPI response (single mode)/ IO[1] (dual mode) polarity
          for the specified bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:DATATWO:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:DATATWO:POLarity?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ESPI:DATATWO:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ESPI:DATATWO:POLarity {HIGH|LOW}
        - BUS:B<x>:ESPI:DATATWO:POLarity?
        ```

    Info:
        - ``B<x>`` is the Bus number.
        - ``HIGH`` sets the ESPI data polarity to active high.
        - ``LOW`` sets the ESPI data polarity to active low.
    """


class BusBItemEspiDatatwo(SCPICmdRead):
    """The ``BUS:B<x>:ESPI:DATATWO`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:DATATWO?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:DATATWO?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the Bus number.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:ESPI:DATATWO:POLarity`` command.
        - ``.source``: The ``BUS:B<x>:ESPI:DATATWO:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:ESPI:DATATWO:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemEspiDatatwoPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemEspiDatatwoSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemEspiDatatwoThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def polarity(self) -> BusBItemEspiDatatwoPolarity:
        """Return the ``BUS:B<x>:ESPI:DATATWO:POLarity`` command.

        Description:
            - This command sets or queries the ESPI response (single mode)/ IO[1] (dual mode)
              polarity for the specified bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:DATATWO:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:DATATWO:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ESPI:DATATWO:POLarity value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ESPI:DATATWO:POLarity {HIGH|LOW}
            - BUS:B<x>:ESPI:DATATWO:POLarity?
            ```

        Info:
            - ``B<x>`` is the Bus number.
            - ``HIGH`` sets the ESPI data polarity to active high.
            - ``LOW`` sets the ESPI data polarity to active low.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemEspiDatatwoSource:
        """Return the ``BUS:B<x>:ESPI:DATATWO:SOUrce`` command.

        Description:
            - This command sets or queries the response (single mode)/ IO[1] (dual mode) Data source
              for the specified bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:DATATWO:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:DATATWO:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ESPI:DATATWO:SOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ESPI:DATATWO:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
            - BUS:B<x>:ESPI:DATATWO:SOUrce?
            ```

        Info:
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``Math<x>`` specifies a math waveform as the source.
            - ``REF<x>`` specifies a reference waveform as the source.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemEspiDatatwoThreshold:
        """Return the ``BUS:B<x>:ESPI:DATATWO:THReshold`` command.

        Description:
            - This command sets or queries the response (single mode)/ IO[1] (dual mode) Data source
              threshold for the specified bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:DATATWO:THReshold?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:DATATWO:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ESPI:DATATWO:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ESPI:DATATWO:THReshold <NR3>
            - BUS:B<x>:ESPI:DATATWO:THReshold?
            ```

        Info:
            - ``B<x>`` is the Bus number.
            - ``<NR3>`` sets the command/data threshold for the specified bus. The valid range is
              -8V to +8V.
        """
        return self._threshold


class BusBItemEspiDataoneThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ESPI:DATAONE:THReshold`` command.

    Description:
        - This command sets or queries the command (single mode)/ IO[0] (dual mode) Data source
          threshold for the specified bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:DATAONE:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:DATAONE:THReshold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ESPI:DATAONE:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ESPI:DATAONE:THReshold <NR3>
        - BUS:B<x>:ESPI:DATAONE:THReshold?
        ```

    Info:
        - ``B<x>`` is the Bus number.
        - ``<NR3>`` sets the command/data threshold for the specified bus. The valid range is -8V to
          +8V.
    """


class BusBItemEspiDataoneSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ESPI:DATAONE:SOUrce`` command.

    Description:
        - This command sets or queries the command (single mode)/ IO[0] (dual mode) Data source for
          the specified bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:DATAONE:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:DATAONE:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ESPI:DATAONE:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ESPI:DATAONE:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
        - BUS:B<x>:ESPI:DATAONE:SOUrce?
        ```

    Info:
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``Math<x>`` specifies a math waveform as the source.
        - ``REF<x>`` specifies a reference waveform as the source.
    """


class BusBItemEspiDataonePolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ESPI:DATAONE:POLarity`` command.

    Description:
        - This command sets or queries the ESPI command (single mode)/ IO[0] (dual mode) polarity
          for the specified bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:DATAONE:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:DATAONE:POLarity?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ESPI:DATAONE:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ESPI:DATAONE:POLarity {HIGH|LOW}
        - BUS:B<x>:ESPI:DATAONE:POLarity?
        ```

    Info:
        - ``B<x>`` is the Bus number.
        - ``HIGH`` sets the ESPI data polarity to active high.
        - ``LOW`` sets the ESPI data polarity to active low.
    """


class BusBItemEspiDataone(SCPICmdRead):
    """The ``BUS:B<x>:ESPI:DATAONE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:DATAONE?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:DATAONE?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the Bus number.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:ESPI:DATAONE:POLarity`` command.
        - ``.source``: The ``BUS:B<x>:ESPI:DATAONE:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:ESPI:DATAONE:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemEspiDataonePolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemEspiDataoneSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemEspiDataoneThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def polarity(self) -> BusBItemEspiDataonePolarity:
        """Return the ``BUS:B<x>:ESPI:DATAONE:POLarity`` command.

        Description:
            - This command sets or queries the ESPI command (single mode)/ IO[0] (dual mode)
              polarity for the specified bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:DATAONE:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:DATAONE:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ESPI:DATAONE:POLarity value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ESPI:DATAONE:POLarity {HIGH|LOW}
            - BUS:B<x>:ESPI:DATAONE:POLarity?
            ```

        Info:
            - ``B<x>`` is the Bus number.
            - ``HIGH`` sets the ESPI data polarity to active high.
            - ``LOW`` sets the ESPI data polarity to active low.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemEspiDataoneSource:
        """Return the ``BUS:B<x>:ESPI:DATAONE:SOUrce`` command.

        Description:
            - This command sets or queries the command (single mode)/ IO[0] (dual mode) Data source
              for the specified bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:DATAONE:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:DATAONE:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ESPI:DATAONE:SOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ESPI:DATAONE:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
            - BUS:B<x>:ESPI:DATAONE:SOUrce?
            ```

        Info:
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``Math<x>`` specifies a math waveform as the source.
            - ``REF<x>`` specifies a reference waveform as the source.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemEspiDataoneThreshold:
        """Return the ``BUS:B<x>:ESPI:DATAONE:THReshold`` command.

        Description:
            - This command sets or queries the command (single mode)/ IO[0] (dual mode) Data source
              threshold for the specified bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:DATAONE:THReshold?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:DATAONE:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ESPI:DATAONE:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ESPI:DATAONE:THReshold <NR3>
            - BUS:B<x>:ESPI:DATAONE:THReshold?
            ```

        Info:
            - ``B<x>`` is the Bus number.
            - ``<NR3>`` sets the command/data threshold for the specified bus. The valid range is
              -8V to +8V.
        """
        return self._threshold


class BusBItemEspiClockThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ESPI:CLOCk:THReshold`` command.

    Description:
        - This command sets or queries the Clock source threshold for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:CLOCk:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:CLOCk:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ESPI:CLOCk:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ESPI:CLOCk:THReshold <NR3>
        - BUS:B<x>:ESPI:CLOCk:THReshold?
        ```

    Info:
        - ``B<x>`` is the Bus number.
        - ``<NR3>`` sets the clock threshold for the specified bus. The valid range is -8V to +8V.
    """


class BusBItemEspiClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ESPI:CLOCk:SOUrce`` command.

    Description:
        - This command sets or queries the Clock source for the specified bus. The bus is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:CLOCk:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ESPI:CLOCk:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ESPI:CLOCk:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
        - BUS:B<x>:ESPI:CLOCk:SOUrce?
        ```

    Info:
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``Math<x>`` specifies a math waveform as the source.
        - ``REF<x>`` specifies a reference waveform as the source.
    """


class BusBItemEspiClockPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ESPI:CLOCk:POLarity`` command.

    Description:
        - This command sets or queries the ESPI Clock (SCLK) source polarity for the specified bus.
          The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:CLOCk:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:CLOCk:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ESPI:CLOCk:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ESPI:CLOCk:POLarity {FALL|RISE}
        - BUS:B<x>:ESPI:CLOCk:POLarity?
        ```

    Info:
        - ``B<x>`` is the Bus number.
        - ``FALL`` sets the ESPI clock polarity to fall.
        - ``RISE`` sets the ESPI clock polarity to rise.
    """


class BusBItemEspiClock(SCPICmdRead):
    """The ``BUS:B<x>:ESPI:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:CLOCk?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the Bus number.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:ESPI:CLOCk:POLarity`` command.
        - ``.source``: The ``BUS:B<x>:ESPI:CLOCk:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:ESPI:CLOCk:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemEspiClockPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemEspiClockSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemEspiClockThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def polarity(self) -> BusBItemEspiClockPolarity:
        """Return the ``BUS:B<x>:ESPI:CLOCk:POLarity`` command.

        Description:
            - This command sets or queries the ESPI Clock (SCLK) source polarity for the specified
              bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:CLOCk:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:CLOCk:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ESPI:CLOCk:POLarity value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ESPI:CLOCk:POLarity {FALL|RISE}
            - BUS:B<x>:ESPI:CLOCk:POLarity?
            ```

        Info:
            - ``B<x>`` is the Bus number.
            - ``FALL`` sets the ESPI clock polarity to fall.
            - ``RISE`` sets the ESPI clock polarity to rise.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemEspiClockSource:
        """Return the ``BUS:B<x>:ESPI:CLOCk:SOUrce`` command.

        Description:
            - This command sets or queries the Clock source for the specified bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:CLOCk:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:CLOCk:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:ESPI:CLOCk:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ESPI:CLOCk:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
            - BUS:B<x>:ESPI:CLOCk:SOUrce?
            ```

        Info:
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``Math<x>`` specifies a math waveform as the source.
            - ``REF<x>`` specifies a reference waveform as the source.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemEspiClockThreshold:
        """Return the ``BUS:B<x>:ESPI:CLOCk:THReshold`` command.

        Description:
            - This command sets or queries the Clock source threshold for the specified bus. The bus
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:CLOCk:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:CLOCk:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ESPI:CLOCk:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ESPI:CLOCk:THReshold <NR3>
            - BUS:B<x>:ESPI:CLOCk:THReshold?
            ```

        Info:
            - ``B<x>`` is the Bus number.
            - ``<NR3>`` sets the clock threshold for the specified bus. The valid range is -8V to
              +8V.
        """
        return self._threshold


class BusBItemEspiChipselectThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ESPI:CHIPSELect:THReshold`` command.

    Description:
        - This command sets or queries the chip select source threshold for the specified bus. The
          bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:CHIPSELect:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:CHIPSELect:THReshold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:ESPI:CHIPSELect:THReshold value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ESPI:CHIPSELect:THReshold <NR3>
        - BUS:B<x>:ESPI:CHIPSELect:THReshold?
        ```

    Info:
        - ``B<x>`` is the Bus number.
        - ``<NR3>`` sets the chip select threshold for the specified bus. The valid range is -8V to
          +8V.
    """


class BusBItemEspiChipselectSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ESPI:CHIPSELect:SOUrce`` command.

    Description:
        - This command sets or queries the chip select source for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:CHIPSELect:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:CHIPSELect:SOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ESPI:CHIPSELect:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ESPI:CHIPSELect:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
        - BUS:B<x>:ESPI:CHIPSELect:SOUrce?
        ```

    Info:
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``Math<x>`` specifies a math waveform as the source.
        - ``REF<x>`` specifies a reference waveform as the source.
    """


class BusBItemEspiChipselectPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ESPI:CHIPSELect:POLarity`` command.

    Description:
        - This command sets or queries the ESPI chip select polarity for the specified bus. The bus
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:CHIPSELect:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:CHIPSELect:POLarity?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:ESPI:CHIPSELect:POLarity value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ESPI:CHIPSELect:POLarity {HIGH|LOW}
        - BUS:B<x>:ESPI:CHIPSELect:POLarity?
        ```

    Info:
        - ``B<x>`` is the Bus number.
        - ``HIGH`` sets the ESPI chip select polarity to active high.
        - ``LOW`` sets the ESPI chip select polarity to active low.
    """


class BusBItemEspiChipselect(SCPICmdRead):
    """The ``BUS:B<x>:ESPI:CHIPSELect`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:CHIPSELect?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:CHIPSELect?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the Bus number.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:ESPI:CHIPSELect:POLarity`` command.
        - ``.source``: The ``BUS:B<x>:ESPI:CHIPSELect:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:ESPI:CHIPSELect:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemEspiChipselectPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemEspiChipselectSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemEspiChipselectThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def polarity(self) -> BusBItemEspiChipselectPolarity:
        """Return the ``BUS:B<x>:ESPI:CHIPSELect:POLarity`` command.

        Description:
            - This command sets or queries the ESPI chip select polarity for the specified bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:CHIPSELect:POLarity?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:ESPI:CHIPSELect:POLarity?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ESPI:CHIPSELect:POLarity value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ESPI:CHIPSELect:POLarity {HIGH|LOW}
            - BUS:B<x>:ESPI:CHIPSELect:POLarity?
            ```

        Info:
            - ``B<x>`` is the Bus number.
            - ``HIGH`` sets the ESPI chip select polarity to active high.
            - ``LOW`` sets the ESPI chip select polarity to active low.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemEspiChipselectSource:
        """Return the ``BUS:B<x>:ESPI:CHIPSELect:SOUrce`` command.

        Description:
            - This command sets or queries the chip select source for the specified bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:CHIPSELect:SOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:CHIPSELect:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ESPI:CHIPSELect:SOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ESPI:CHIPSELect:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
            - BUS:B<x>:ESPI:CHIPSELect:SOUrce?
            ```

        Info:
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``Math<x>`` specifies a math waveform as the source.
            - ``REF<x>`` specifies a reference waveform as the source.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemEspiChipselectThreshold:
        """Return the ``BUS:B<x>:ESPI:CHIPSELect:THReshold`` command.

        Description:
            - This command sets or queries the chip select source threshold for the specified bus.
              The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:CHIPSELect:THReshold?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:ESPI:CHIPSELect:THReshold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ESPI:CHIPSELect:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ESPI:CHIPSELect:THReshold <NR3>
            - BUS:B<x>:ESPI:CHIPSELect:THReshold?
            ```

        Info:
            - ``B<x>`` is the Bus number.
            - ``<NR3>`` sets the chip select threshold for the specified bus. The valid range is -8V
              to +8V.
        """
        return self._threshold


class BusBItemEspiAlertThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ESPI:ALERt:THReshold`` command.

    Description:
        - This command sets or queries the alert source threshold for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:ALERt:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:ALERt:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ESPI:ALERt:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ESPI:ALERt:THReshold <NR3>
        - BUS:B<x>:ESPI:ALERt:THReshold?
        ```

    Info:
        - ``B<x>`` is the Bus number.
        - ``<NR3>`` sets the alert threshold for the specified bus. The valid range is -8V to +8V.
    """


class BusBItemEspiAlertSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ESPI:ALERt:SOUrce`` command.

    Description:
        - This command sets or queries the alert source for the specified bus. The bus is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:ALERt:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:ALERt:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ESPI:ALERt:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ESPI:ALERt:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
        - BUS:B<x>:ESPI:ALERt:SOUrce?
        ```

    Info:
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``Math<x>`` specifies a math waveform as the source.
        - ``REF<x>`` specifies a reference waveform as the source.
    """


class BusBItemEspiAlertPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ESPI:ALERt:POLarity`` command.

    Description:
        - This command sets or queries the ESPI alert polarity for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:ALERt:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:ALERt:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ESPI:ALERt:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ESPI:ALERt:POLarity {HIGH|LOW}
        - BUS:B<x>:ESPI:ALERt:POLarity?
        ```

    Info:
        - ``B<x>`` is the Bus number.
        - ``HIGH`` sets the ESPI alert polarity to active high.
        - ``LOW`` sets the ESPI alert polarity to active low.
    """


class BusBItemEspiAlert(SCPICmdRead):
    """The ``BUS:B<x>:ESPI:ALERt`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:ALERt?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:ALERt?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the Bus number.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:ESPI:ALERt:POLarity`` command.
        - ``.source``: The ``BUS:B<x>:ESPI:ALERt:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:ESPI:ALERt:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemEspiAlertPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemEspiAlertSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemEspiAlertThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def polarity(self) -> BusBItemEspiAlertPolarity:
        """Return the ``BUS:B<x>:ESPI:ALERt:POLarity`` command.

        Description:
            - This command sets or queries the ESPI alert polarity for the specified bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:ALERt:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:ALERt:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ESPI:ALERt:POLarity value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ESPI:ALERt:POLarity {HIGH|LOW}
            - BUS:B<x>:ESPI:ALERt:POLarity?
            ```

        Info:
            - ``B<x>`` is the Bus number.
            - ``HIGH`` sets the ESPI alert polarity to active high.
            - ``LOW`` sets the ESPI alert polarity to active low.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemEspiAlertSource:
        """Return the ``BUS:B<x>:ESPI:ALERt:SOUrce`` command.

        Description:
            - This command sets or queries the alert source for the specified bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:ALERt:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:ALERt:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:ESPI:ALERt:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ESPI:ALERt:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
            - BUS:B<x>:ESPI:ALERt:SOUrce?
            ```

        Info:
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``Math<x>`` specifies a math waveform as the source.
            - ``REF<x>`` specifies a reference waveform as the source.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemEspiAlertThreshold:
        """Return the ``BUS:B<x>:ESPI:ALERt:THReshold`` command.

        Description:
            - This command sets or queries the alert source threshold for the specified bus. The bus
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:ALERt:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:ALERt:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ESPI:ALERt:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ESPI:ALERt:THReshold <NR3>
            - BUS:B<x>:ESPI:ALERt:THReshold?
            ```

        Info:
            - ``B<x>`` is the Bus number.
            - ``<NR3>`` sets the alert threshold for the specified bus. The valid range is -8V to
              +8V.
        """
        return self._threshold


class BusBItemEspiAlertview(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ESPI:ALERTVIEW`` command.

    Description:
        - This command sets or queries the ESPI alert view for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:ALERTVIEW?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:ALERTVIEW?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ESPI:ALERTVIEW value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ESPI:ALERTVIEW {ON|OFF}
        - BUS:B<x>:ESPI:ALERTVIEW?
        ```

    Info:
        - ``B<x>`` is the Bus number.
        - ``ON`` turns the alert source on.
        - ``OFF`` turns the alert source on.
    """


class BusBItemEspi(SCPICmdRead):
    """The ``BUS:B<x>:ESPI`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the Bus number.

    Properties:
        - ``.alertview``: The ``BUS:B<x>:ESPI:ALERTVIEW`` command.
        - ``.alert``: The ``BUS:B<x>:ESPI:ALERt`` command tree.
        - ``.chipselect``: The ``BUS:B<x>:ESPI:CHIPSELect`` command tree.
        - ``.clock``: The ``BUS:B<x>:ESPI:CLOCk`` command tree.
        - ``.dataone``: The ``BUS:B<x>:ESPI:DATAONE`` command tree.
        - ``.datatwo``: The ``BUS:B<x>:ESPI:DATATWO`` command tree.
        - ``.iomode``: The ``BUS:B<x>:ESPI:IOMODe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._alertview = BusBItemEspiAlertview(device, f"{self._cmd_syntax}:ALERTVIEW")
        self._alert = BusBItemEspiAlert(device, f"{self._cmd_syntax}:ALERt")
        self._chipselect = BusBItemEspiChipselect(device, f"{self._cmd_syntax}:CHIPSELect")
        self._clock = BusBItemEspiClock(device, f"{self._cmd_syntax}:CLOCk")
        self._dataone = BusBItemEspiDataone(device, f"{self._cmd_syntax}:DATAONE")
        self._datatwo = BusBItemEspiDatatwo(device, f"{self._cmd_syntax}:DATATWO")
        self._iomode = BusBItemEspiIomode(device, f"{self._cmd_syntax}:IOMODe")

    @property
    def alertview(self) -> BusBItemEspiAlertview:
        """Return the ``BUS:B<x>:ESPI:ALERTVIEW`` command.

        Description:
            - This command sets or queries the ESPI alert view for the specified bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:ALERTVIEW?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:ALERTVIEW?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:ESPI:ALERTVIEW value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ESPI:ALERTVIEW {ON|OFF}
            - BUS:B<x>:ESPI:ALERTVIEW?
            ```

        Info:
            - ``B<x>`` is the Bus number.
            - ``ON`` turns the alert source on.
            - ``OFF`` turns the alert source on.
        """
        return self._alertview

    @property
    def alert(self) -> BusBItemEspiAlert:
        """Return the ``BUS:B<x>:ESPI:ALERt`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:ALERt?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:ALERt?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the Bus number.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:ESPI:ALERt:POLarity`` command.
            - ``.source``: The ``BUS:B<x>:ESPI:ALERt:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:ESPI:ALERt:THReshold`` command.
        """
        return self._alert

    @property
    def chipselect(self) -> BusBItemEspiChipselect:
        """Return the ``BUS:B<x>:ESPI:CHIPSELect`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:CHIPSELect?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:CHIPSELect?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the Bus number.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:ESPI:CHIPSELect:POLarity`` command.
            - ``.source``: The ``BUS:B<x>:ESPI:CHIPSELect:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:ESPI:CHIPSELect:THReshold`` command.
        """
        return self._chipselect

    @property
    def clock(self) -> BusBItemEspiClock:
        """Return the ``BUS:B<x>:ESPI:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:CLOCk?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the Bus number.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:ESPI:CLOCk:POLarity`` command.
            - ``.source``: The ``BUS:B<x>:ESPI:CLOCk:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:ESPI:CLOCk:THReshold`` command.
        """
        return self._clock

    @property
    def dataone(self) -> BusBItemEspiDataone:
        """Return the ``BUS:B<x>:ESPI:DATAONE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:DATAONE?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:DATAONE?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the Bus number.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:ESPI:DATAONE:POLarity`` command.
            - ``.source``: The ``BUS:B<x>:ESPI:DATAONE:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:ESPI:DATAONE:THReshold`` command.
        """
        return self._dataone

    @property
    def datatwo(self) -> BusBItemEspiDatatwo:
        """Return the ``BUS:B<x>:ESPI:DATATWO`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:DATATWO?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:DATATWO?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the Bus number.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:ESPI:DATATWO:POLarity`` command.
            - ``.source``: The ``BUS:B<x>:ESPI:DATATWO:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:ESPI:DATATWO:THReshold`` command.
        """
        return self._datatwo

    @property
    def iomode(self) -> BusBItemEspiIomode:
        """Return the ``BUS:B<x>:ESPI:IOMODe`` command.

        Description:
            - This command sets or queries the ESPI Input/Output mode for the specified bus. The bus
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI:IOMODe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI:IOMODe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:ESPI:IOMODe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ESPI:IOMODe {SINGle|DUAL}
            - BUS:B<x>:ESPI:IOMODe?
            ```

        Info:
            - ``B<x>`` is the Bus number.
            - ``SINGle`` displays the command and response decode in two lanes.
            - ``DUAL`` displays the decode in a single data lane.
        """
        return self._iomode


class BusBItemDphySignalEncoding(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:DPHY:SIGNal:ENCoding`` command.

    Description:
        - This command sets or queries the 8b9b encoding for DPHY bus decode. By default 8b9b
          encoding is set to false. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:SIGNal:ENCoding?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:SIGNal:ENCoding?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:DPHY:SIGNal:ENCoding value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:DPHY:SIGNal:ENCoding {false|true}
        - BUS:B<x>:DPHY:SIGNal:ENCoding?
        ```

    Info:
        - ``B<x>`` is the Bus number.
        - ``false`` specifies the 8b9b encoding disabled.
        - ``true`` specifies 8b9b encoding disabled.
    """


class BusBItemDphySignal(SCPICmdRead):
    """The ``BUS:B<x>:DPHY:SIGNal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:SIGNal?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:SIGNal?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the Bus number.

    Properties:
        - ``.encoding``: The ``BUS:B<x>:DPHY:SIGNal:ENCoding`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._encoding = BusBItemDphySignalEncoding(device, f"{self._cmd_syntax}:ENCoding")

    @property
    def encoding(self) -> BusBItemDphySignalEncoding:
        """Return the ``BUS:B<x>:DPHY:SIGNal:ENCoding`` command.

        Description:
            - This command sets or queries the 8b9b encoding for DPHY bus decode. By default 8b9b
              encoding is set to false. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:SIGNal:ENCoding?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:SIGNal:ENCoding?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:DPHY:SIGNal:ENCoding value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:DPHY:SIGNal:ENCoding {false|true}
            - BUS:B<x>:DPHY:SIGNal:ENCoding?
            ```

        Info:
            - ``B<x>`` is the Bus number.
            - ``false`` specifies the 8b9b encoding disabled.
            - ``true`` specifies 8b9b encoding disabled.
        """
        return self._encoding


class BusBItemDphyProtocolType(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:DPHY:PROTocol:TYPe`` command.

    Description:
        - This command sets or queries the protocol type for DPHY bus decode. The default type is
          CSI. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:PROTocol:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:PROTocol:TYPe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:DPHY:PROTocol:TYPe value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:DPHY:PROTocol:TYPe {CSI|DSI}
        - BUS:B<x>:DPHY:PROTocol:TYPe?
        ```

    Info:
        - ``B<x>`` is the Bus number.
        - ``CSI`` specifies the protocol type as CSI.
        - ``DSI`` specifies the protocol type as DSI.
    """


class BusBItemDphyProtocol(SCPICmdRead):
    """The ``BUS:B<x>:DPHY:PROTocol`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:PROTocol?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:PROTocol?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the Bus number.

    Properties:
        - ``.type``: The ``BUS:B<x>:DPHY:PROTocol:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._type = BusBItemDphyProtocolType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def type(self) -> BusBItemDphyProtocolType:
        """Return the ``BUS:B<x>:DPHY:PROTocol:TYPe`` command.

        Description:
            - This command sets or queries the protocol type for DPHY bus decode. The default type
              is CSI. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:PROTocol:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:PROTocol:TYPe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:DPHY:PROTocol:TYPe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:DPHY:PROTocol:TYPe {CSI|DSI}
            - BUS:B<x>:DPHY:PROTocol:TYPe?
            ```

        Info:
            - ``B<x>`` is the Bus number.
            - ``CSI`` specifies the protocol type as CSI.
            - ``DSI`` specifies the protocol type as DSI.
        """
        return self._type


class BusBItemDphyLpDirection(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:DPHY:LP:DIRection`` command.

    Description:
        - This command sets or queries the DPHY bus direction in low power. By default lp direction
          is set to forward. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:LP:DIRection?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:LP:DIRection?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:DPHY:LP:DIRection value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:DPHY:LP:DIRection {forward|reverse}
        - BUS:B<x>:DPHY:LP:DIRection?
        ```

    Info:
        - ``B<x>`` is the Bus number.
        - ``forward`` specifies the direction as forward.
        - ``reverse`` specifies the direction as reverse.
    """


class BusBItemDphyLp(SCPICmdRead):
    """The ``BUS:B<x>:DPHY:LP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:LP?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:LP?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the Bus number.

    Properties:
        - ``.direction``: The ``BUS:B<x>:DPHY:LP:DIRection`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._direction = BusBItemDphyLpDirection(device, f"{self._cmd_syntax}:DIRection")

    @property
    def direction(self) -> BusBItemDphyLpDirection:
        """Return the ``BUS:B<x>:DPHY:LP:DIRection`` command.

        Description:
            - This command sets or queries the DPHY bus direction in low power. By default lp
              direction is set to forward. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:LP:DIRection?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:LP:DIRection?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:DPHY:LP:DIRection value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:DPHY:LP:DIRection {forward|reverse}
            - BUS:B<x>:DPHY:LP:DIRection?
            ```

        Info:
            - ``B<x>`` is the Bus number.
            - ``forward`` specifies the direction as forward.
            - ``reverse`` specifies the direction as reverse.
        """
        return self._direction


class BusBItemDphyDplusSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:DPHY:DPlus:SOUrce`` command.

    Description:
        - This command sets or queries the DPHY D+ source for the specified bus line. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:DPlus:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:DPlus:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:DPHY:DPlus:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:DPHY:DPlus:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
        - BUS:B<x>:DPHY:DPlus:SOUrce?
        ```

    Info:
        - ``Bus<x>`` is the Bus number.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
        - ``CH<x>`` specifies an analog channel as the source, where <x> is the channel number.
        - ``MATH<x>`` specifies a math channel as the source, where <x> is the math waveform number.
        - ``REF<x>`` specifies a reference waveform as the source, where <x> is the reference
          waveform number.
    """


class BusBItemDphyDplusLpthreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:DPHY:DPlus:LPTHRESHold`` command.

    Description:
        - This command sets or queries the DPHY D+ source low power threshold for the specified bus.
          The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:DPlus:LPTHRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:DPlus:LPTHRESHold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:DPHY:DPlus:LPTHRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:DPHY:DPlus:LPTHRESHold <NR3>
        - BUS:B<x>:DPHY:DPlus:LPTHRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the DPHY D+ source low power threshold for the specified bus. The argument
          range is -8V to +8V.
    """


class BusBItemDphyDplusDatathreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:DPHY:DPlus:DATATHRESHold`` command.

    Description:
        - This command sets or queries the D+ source data threshold for the specified bus. The bus
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:DPlus:DATATHRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:DPlus:DATATHRESHold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:DPHY:DPlus:DATATHRESHold value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:DPHY:DPlus:DATATHRESHold <NR3>
        - BUS:B<x>:DPHY:DPlus:DATATHRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the DPHY D+ source data threshold for the specified bus. The argument range
          is -8V to +8V.
    """


class BusBItemDphyDplus(SCPICmdRead):
    """The ``BUS:B<x>:DPHY:DPlus`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:DPlus?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:DPlus?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.datathreshold``: The ``BUS:B<x>:DPHY:DPlus:DATATHRESHold`` command.
        - ``.lpthreshold``: The ``BUS:B<x>:DPHY:DPlus:LPTHRESHold`` command.
        - ``.source``: The ``BUS:B<x>:DPHY:DPlus:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._datathreshold = BusBItemDphyDplusDatathreshold(
            device, f"{self._cmd_syntax}:DATATHRESHold"
        )
        self._lpthreshold = BusBItemDphyDplusLpthreshold(device, f"{self._cmd_syntax}:LPTHRESHold")
        self._source = BusBItemDphyDplusSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def datathreshold(self) -> BusBItemDphyDplusDatathreshold:
        """Return the ``BUS:B<x>:DPHY:DPlus:DATATHRESHold`` command.

        Description:
            - This command sets or queries the D+ source data threshold for the specified bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:DPlus:DATATHRESHold?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:DPHY:DPlus:DATATHRESHold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:DPHY:DPlus:DATATHRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:DPHY:DPlus:DATATHRESHold <NR3>
            - BUS:B<x>:DPHY:DPlus:DATATHRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the DPHY D+ source data threshold for the specified bus. The argument
              range is -8V to +8V.
        """
        return self._datathreshold

    @property
    def lpthreshold(self) -> BusBItemDphyDplusLpthreshold:
        """Return the ``BUS:B<x>:DPHY:DPlus:LPTHRESHold`` command.

        Description:
            - This command sets or queries the DPHY D+ source low power threshold for the specified
              bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:DPlus:LPTHRESHold?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:DPlus:LPTHRESHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:DPHY:DPlus:LPTHRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:DPHY:DPlus:LPTHRESHold <NR3>
            - BUS:B<x>:DPHY:DPlus:LPTHRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the DPHY D+ source low power threshold for the specified bus. The
              argument range is -8V to +8V.
        """
        return self._lpthreshold

    @property
    def source(self) -> BusBItemDphyDplusSource:
        """Return the ``BUS:B<x>:DPHY:DPlus:SOUrce`` command.

        Description:
            - This command sets or queries the DPHY D+ source for the specified bus line. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:DPlus:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:DPlus:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:DPHY:DPlus:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:DPHY:DPlus:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
            - BUS:B<x>:DPHY:DPlus:SOUrce?
            ```

        Info:
            - ``Bus<x>`` is the Bus number.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
            - ``CH<x>`` specifies an analog channel as the source, where <x> is the channel number.
            - ``MATH<x>`` specifies a math channel as the source, where <x> is the math waveform
              number.
            - ``REF<x>`` specifies a reference waveform as the source, where <x> is the reference
              waveform number.
        """
        return self._source


class BusBItemDphyDminusSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:DPHY:DMINus:SOUrce`` command.

    Description:
        - This command sets or queries the DPHY D- source for the specified bus line. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:DMINus:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:DMINus:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:DPHY:DMINus:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:DPHY:DMINus:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
        - BUS:B<x>:DPHY:DMINus:SOUrce?
        ```

    Info:
        - ``Bus<x>`` is the Bus number.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
        - ``CH<x>`` specifies an analog channel as the source, where <x> is the channel number.
        - ``MATH<x>`` specifies a math channel as the source, where <x> is the math waveform number.
        - ``REF<x>`` specifies a reference waveform as the source, where <x> is the reference
          waveform number.
    """


class BusBItemDphyDminusLpthreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:DPHY:DMINus:LPTHRESHold`` command.

    Description:
        - This command sets or queries the DPHY D- source low power threshold for the specified bus.
          The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:DMINus:LPTHRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:DMINus:LPTHRESHold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:DPHY:DMINus:LPTHRESHold value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:DPHY:DMINus:LPTHRESHold <NR3>
        - BUS:B<x>:DPHY:DMINus:LPTHRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the DPHY D- source low power threshold for the specified bus. The argument
          range is -8V to +8V.
    """


class BusBItemDphyDminusDatathreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:DPHY:DMINus:DATATHRESHold`` command.

    Description:
        - This command sets or queries the DPHY D- source data threshold for the specified bus. The
          bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:DMINus:DATATHRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:DMINus:DATATHRESHold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:DPHY:DMINus:DATATHRESHold value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:DPHY:DMINus:DATATHRESHold <NR3>
        - BUS:B<x>:DPHY:DMINus:DATATHRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the DPHY D- source data threshold for the specified bus. The argument range
          is -8V to +8V.
    """


class BusBItemDphyDminus(SCPICmdRead):
    """The ``BUS:B<x>:DPHY:DMINus`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:DMINus?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:DMINus?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.datathreshold``: The ``BUS:B<x>:DPHY:DMINus:DATATHRESHold`` command.
        - ``.lpthreshold``: The ``BUS:B<x>:DPHY:DMINus:LPTHRESHold`` command.
        - ``.source``: The ``BUS:B<x>:DPHY:DMINus:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._datathreshold = BusBItemDphyDminusDatathreshold(
            device, f"{self._cmd_syntax}:DATATHRESHold"
        )
        self._lpthreshold = BusBItemDphyDminusLpthreshold(device, f"{self._cmd_syntax}:LPTHRESHold")
        self._source = BusBItemDphyDminusSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def datathreshold(self) -> BusBItemDphyDminusDatathreshold:
        """Return the ``BUS:B<x>:DPHY:DMINus:DATATHRESHold`` command.

        Description:
            - This command sets or queries the DPHY D- source data threshold for the specified bus.
              The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:DMINus:DATATHRESHold?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:DPHY:DMINus:DATATHRESHold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:DPHY:DMINus:DATATHRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:DPHY:DMINus:DATATHRESHold <NR3>
            - BUS:B<x>:DPHY:DMINus:DATATHRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the DPHY D- source data threshold for the specified bus. The argument
              range is -8V to +8V.
        """
        return self._datathreshold

    @property
    def lpthreshold(self) -> BusBItemDphyDminusLpthreshold:
        """Return the ``BUS:B<x>:DPHY:DMINus:LPTHRESHold`` command.

        Description:
            - This command sets or queries the DPHY D- source low power threshold for the specified
              bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:DMINus:LPTHRESHold?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:DPHY:DMINus:LPTHRESHold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:DPHY:DMINus:LPTHRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:DPHY:DMINus:LPTHRESHold <NR3>
            - BUS:B<x>:DPHY:DMINus:LPTHRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the DPHY D- source low power threshold for the specified bus. The
              argument range is -8V to +8V.
        """
        return self._lpthreshold

    @property
    def source(self) -> BusBItemDphyDminusSource:
        """Return the ``BUS:B<x>:DPHY:DMINus:SOUrce`` command.

        Description:
            - This command sets or queries the DPHY D- source for the specified bus line. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:DMINus:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:DMINus:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:DPHY:DMINus:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:DPHY:DMINus:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
            - BUS:B<x>:DPHY:DMINus:SOUrce?
            ```

        Info:
            - ``Bus<x>`` is the Bus number.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
            - ``CH<x>`` specifies an analog channel as the source, where <x> is the channel number.
            - ``MATH<x>`` specifies a math channel as the source, where <x> is the math waveform
              number.
            - ``REF<x>`` specifies a reference waveform as the source, where <x> is the reference
              waveform number.
        """
        return self._source


class BusBItemDphyClockThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:DPHY:CLOCk:THRESHold`` command.

    Description:
        - This command sets or queries the DPHY Clock source threshold for the specified bus. The
          bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:CLOCk:THRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:CLOCk:THRESHold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:DPHY:CLOCk:THRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:DPHY:CLOCk:THRESHold <NR3>
        - BUS:B<x>:DPHY:CLOCk:THRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the DPHY clock high threshold for the specified bus. The argument range is
          -8V to +8V.
    """


class BusBItemDphyClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:DPHY:CLOCk:SOUrce`` command.

    Description:
        - This command sets or queries the DPHY Clock source for the specified bus line. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:CLOCk:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:DPHY:CLOCk:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:DPHY:CLOCk:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
        - BUS:B<x>:DPHY:CLOCk:SOUrce?
        ```

    Info:
        - ``Bus<x>`` is the Bus number.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
        - ``CH<x>`` specifies an analog channel as the source, where <x> is the channel number.
        - ``MATH<x>`` specifies a math channel as the source, where <x> is the math waveform number.
        - ``REF<x>`` specifies a reference waveform as the source, where <x> is the reference
          waveform number.
    """


class BusBItemDphyClock(SCPICmdRead):
    """The ``BUS:B<x>:DPHY:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:CLOCk?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``BUS:B<x>:DPHY:CLOCk:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:DPHY:CLOCk:THRESHold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemDphyClockSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemDphyClockThreshold(device, f"{self._cmd_syntax}:THRESHold")

    @property
    def source(self) -> BusBItemDphyClockSource:
        """Return the ``BUS:B<x>:DPHY:CLOCk:SOUrce`` command.

        Description:
            - This command sets or queries the DPHY Clock source for the specified bus line. The bus
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:CLOCk:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:CLOCk:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:DPHY:CLOCk:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:DPHY:CLOCk:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
            - BUS:B<x>:DPHY:CLOCk:SOUrce?
            ```

        Info:
            - ``Bus<x>`` is the Bus number.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
            - ``CH<x>`` specifies an analog channel as the source, where <x> is the channel number.
            - ``MATH<x>`` specifies a math channel as the source, where <x> is the math waveform
              number.
            - ``REF<x>`` specifies a reference waveform as the source, where <x> is the reference
              waveform number.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemDphyClockThreshold:
        """Return the ``BUS:B<x>:DPHY:CLOCk:THRESHold`` command.

        Description:
            - This command sets or queries the DPHY Clock source threshold for the specified bus.
              The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:CLOCk:THRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:CLOCk:THRESHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:DPHY:CLOCk:THRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:DPHY:CLOCk:THRESHold <NR3>
            - BUS:B<x>:DPHY:CLOCk:THRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the DPHY clock high threshold for the specified bus. The argument range
              is -8V to +8V.
        """
        return self._threshold


class BusBItemDphy(SCPICmdRead):
    """The ``BUS:B<x>:DPHY`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.clock``: The ``BUS:B<x>:DPHY:CLOCk`` command tree.
        - ``.dminus``: The ``BUS:B<x>:DPHY:DMINus`` command tree.
        - ``.dplus``: The ``BUS:B<x>:DPHY:DPlus`` command tree.
        - ``.lp``: The ``BUS:B<x>:DPHY:LP`` command tree.
        - ``.protocol``: The ``BUS:B<x>:DPHY:PROTocol`` command tree.
        - ``.signal``: The ``BUS:B<x>:DPHY:SIGNal`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._clock = BusBItemDphyClock(device, f"{self._cmd_syntax}:CLOCk")
        self._dminus = BusBItemDphyDminus(device, f"{self._cmd_syntax}:DMINus")
        self._dplus = BusBItemDphyDplus(device, f"{self._cmd_syntax}:DPlus")
        self._lp = BusBItemDphyLp(device, f"{self._cmd_syntax}:LP")
        self._protocol = BusBItemDphyProtocol(device, f"{self._cmd_syntax}:PROTocol")
        self._signal = BusBItemDphySignal(device, f"{self._cmd_syntax}:SIGNal")

    @property
    def clock(self) -> BusBItemDphyClock:
        """Return the ``BUS:B<x>:DPHY:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:CLOCk?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:DPHY:CLOCk:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:DPHY:CLOCk:THRESHold`` command.
        """
        return self._clock

    @property
    def dminus(self) -> BusBItemDphyDminus:
        """Return the ``BUS:B<x>:DPHY:DMINus`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:DMINus?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:DMINus?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.datathreshold``: The ``BUS:B<x>:DPHY:DMINus:DATATHRESHold`` command.
            - ``.lpthreshold``: The ``BUS:B<x>:DPHY:DMINus:LPTHRESHold`` command.
            - ``.source``: The ``BUS:B<x>:DPHY:DMINus:SOUrce`` command.
        """
        return self._dminus

    @property
    def dplus(self) -> BusBItemDphyDplus:
        """Return the ``BUS:B<x>:DPHY:DPlus`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:DPlus?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:DPlus?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.datathreshold``: The ``BUS:B<x>:DPHY:DPlus:DATATHRESHold`` command.
            - ``.lpthreshold``: The ``BUS:B<x>:DPHY:DPlus:LPTHRESHold`` command.
            - ``.source``: The ``BUS:B<x>:DPHY:DPlus:SOUrce`` command.
        """
        return self._dplus

    @property
    def lp(self) -> BusBItemDphyLp:
        """Return the ``BUS:B<x>:DPHY:LP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:LP?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:LP?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the Bus number.

        Sub-properties:
            - ``.direction``: The ``BUS:B<x>:DPHY:LP:DIRection`` command.
        """
        return self._lp

    @property
    def protocol(self) -> BusBItemDphyProtocol:
        """Return the ``BUS:B<x>:DPHY:PROTocol`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:PROTocol?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:PROTocol?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the Bus number.

        Sub-properties:
            - ``.type``: The ``BUS:B<x>:DPHY:PROTocol:TYPe`` command.
        """
        return self._protocol

    @property
    def signal(self) -> BusBItemDphySignal:
        """Return the ``BUS:B<x>:DPHY:SIGNal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY:SIGNal?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY:SIGNal?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the Bus number.

        Sub-properties:
            - ``.encoding``: The ``BUS:B<x>:DPHY:SIGNal:ENCoding`` command.
        """
        return self._signal


class BusBItemDisplayLayout(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:DISplay:LAYout`` command.

    Description:
        - This command sets or queries what to display for the specified bus. The bus is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay:LAYout?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay:LAYout?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:DISplay:LAYout value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:DISplay:LAYout {BUS|BUSANDWAVEFORM}
        - BUS:B<x>:DISplay:LAYout?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``BUS`` specifies displaying the bus form only.
        - ``BUSANDWAVEFORM`` specifies displaying the bus form and the constituent source
          waveform(s). This argument is not available for some bus types and some bus
          configurations.
    """


class BusBItemDisplayFormat(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:DISplay:FORMat`` command.

    Description:
        - This command sets or queries how the data is represented in the bus form for the specified
          bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay:FORMat?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay:FORMat?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:DISplay:FORMat value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:DISplay:FORMat {HEX|BINARY|MIXEDASCII|MIXEDHEX|ASCII|DECIMAL|MIXED}
        - BUS:B<x>:DISplay:FORMat?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``HEX`` specifies hexadecimal format.
        - ``BINARY`` specifies binary format.
        - ``MIXEDASCII`` specifies mixed ASCII format.
        - ``MIXEDHEX`` specifies mixed hexadecimal format.
        - ``ASCII`` specifies ASCII format.
        - ``DECIMAL`` specifies decimal format.
        - ``MIXED`` specifies mixed format.
    """


class BusBItemDisplay(SCPICmdRead):
    """The ``BUS:B<x>:DISplay`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.format``: The ``BUS:B<x>:DISplay:FORMat`` command.
        - ``.layout``: The ``BUS:B<x>:DISplay:LAYout`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._format = BusBItemDisplayFormat(device, f"{self._cmd_syntax}:FORMat")
        self._layout = BusBItemDisplayLayout(device, f"{self._cmd_syntax}:LAYout")

    @property
    def format(self) -> BusBItemDisplayFormat:
        """Return the ``BUS:B<x>:DISplay:FORMat`` command.

        Description:
            - This command sets or queries how the data is represented in the bus form for the
              specified bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay:FORMat?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay:FORMat?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:DISplay:FORMat value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:DISplay:FORMat {HEX|BINARY|MIXEDASCII|MIXEDHEX|ASCII|DECIMAL|MIXED}
            - BUS:B<x>:DISplay:FORMat?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``HEX`` specifies hexadecimal format.
            - ``BINARY`` specifies binary format.
            - ``MIXEDASCII`` specifies mixed ASCII format.
            - ``MIXEDHEX`` specifies mixed hexadecimal format.
            - ``ASCII`` specifies ASCII format.
            - ``DECIMAL`` specifies decimal format.
            - ``MIXED`` specifies mixed format.
        """
        return self._format

    @property
    def layout(self) -> BusBItemDisplayLayout:
        """Return the ``BUS:B<x>:DISplay:LAYout`` command.

        Description:
            - This command sets or queries what to display for the specified bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay:LAYout?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay:LAYout?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:DISplay:LAYout value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:DISplay:LAYout {BUS|BUSANDWAVEFORM}
            - BUS:B<x>:DISplay:LAYout?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``BUS`` specifies displaying the bus form only.
            - ``BUSANDWAVEFORM`` specifies displaying the bus form and the constituent source
              waveform(s). This argument is not available for some bus types and some bus
              configurations.
        """
        return self._layout


class BusBItemCxpiSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CXPI:SOUrce`` command.

    Description:
        - This command sets or queries the source channel for the specified CXPI bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CXPI:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CXPI:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CXPI:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CXPI:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:CXPI:SOUrce?
        ```

    Info:
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog channel as the source, where <x> is the channel number.
        - ``MATH<x>`` specifies a math channel as the source, where <x> is the math waveform number.
        - ``REF<x>`` specifies a digital reference waveform as the source, where <x> is the
          reference waveform number.
    """


class BusBItemCxpiRecThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CXPI:REC:THReshold`` command.

    Description:
        - This command sets or queries the source channel recessive threshold for the specified CXPI
          bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CXPI:REC:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CXPI:REC:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CXPI:REC:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CXPI:REC:THReshold <NR3>
        - BUS:B<x>:CXPI:REC:THReshold?
        ```

    Info:
        - ``<NR3>`` sets the CXPI Source recessive threshold for the specified bus. The default
          value is 0 V and the valid range is -12 V to +12 V.
    """


class BusBItemCxpiRec(SCPICmdRead):
    """The ``BUS:B<x>:CXPI:REC`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CXPI:REC?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CXPI:REC?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.threshold``: The ``BUS:B<x>:CXPI:REC:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._threshold = BusBItemCxpiRecThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def threshold(self) -> BusBItemCxpiRecThreshold:
        """Return the ``BUS:B<x>:CXPI:REC:THReshold`` command.

        Description:
            - This command sets or queries the source channel recessive threshold for the specified
              CXPI bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CXPI:REC:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CXPI:REC:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CXPI:REC:THReshold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CXPI:REC:THReshold <NR3>
            - BUS:B<x>:CXPI:REC:THReshold?
            ```

        Info:
            - ``<NR3>`` sets the CXPI Source recessive threshold for the specified bus. The default
              value is 0 V and the valid range is -12 V to +12 V.
        """
        return self._threshold


class BusBItemCxpiBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CXPI:BITRate`` command.

    Description:
        - This command sets or queries the bit rate for the specified CXPI bus. The bus is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CXPI:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CXPI:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CXPI:BITRate value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CXPI:BITRate <NR1>
        - BUS:B<x>:CXPI:BITRate?
        ```

    Info:
        - ``<NR1>`` sets the CXPI Source bit rate for the specified bus. The default value is 19.2
          kbps and the valid range is 1 bps to 20 kbps.
    """


class BusBItemCxpi(SCPICmdRead):
    """The ``BUS:B<x>:CXPI`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CXPI?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CXPI?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:CXPI:BITRate`` command.
        - ``.rec``: The ``BUS:B<x>:CXPI:REC`` command tree.
        - ``.source``: The ``BUS:B<x>:CXPI:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemCxpiBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._rec = BusBItemCxpiRec(device, f"{self._cmd_syntax}:REC")
        self._source = BusBItemCxpiSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def bitrate(self) -> BusBItemCxpiBitrate:
        """Return the ``BUS:B<x>:CXPI:BITRate`` command.

        Description:
            - This command sets or queries the bit rate for the specified CXPI bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CXPI:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CXPI:BITRate?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CXPI:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CXPI:BITRate <NR1>
            - BUS:B<x>:CXPI:BITRate?
            ```

        Info:
            - ``<NR1>`` sets the CXPI Source bit rate for the specified bus. The default value is
              19.2 kbps and the valid range is 1 bps to 20 kbps.
        """
        return self._bitrate

    @property
    def rec(self) -> BusBItemCxpiRec:
        """Return the ``BUS:B<x>:CXPI:REC`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CXPI:REC?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CXPI:REC?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.threshold``: The ``BUS:B<x>:CXPI:REC:THReshold`` command.
        """
        return self._rec

    @property
    def source(self) -> BusBItemCxpiSource:
        """Return the ``BUS:B<x>:CXPI:SOUrce`` command.

        Description:
            - This command sets or queries the source channel for the specified CXPI bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CXPI:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CXPI:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CXPI:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CXPI:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:CXPI:SOUrce?
            ```

        Info:
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog channel as the source, where <x> is the channel number.
            - ``MATH<x>`` specifies a math channel as the source, where <x> is the math waveform
              number.
            - ``REF<x>`` specifies a digital reference waveform as the source, where <x> is the
              reference waveform number.
        """
        return self._source


class BusBItemCphySubtype(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CPHY:SUBTYPe`` command.

    Description:
        - This command sets or queries the sub type for CPHY bus decode. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:SUBTYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:SUBTYPe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:SUBTYPe value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CPHY:SUBTYPe {CSI|DSI|Word|Symbol}
        - BUS:B<x>:CPHY:SUBTYPe?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``CSI`` specifies the protocol type to CSI. The default type is CSI.
        - ``DSI`` specifies the protocol type to DSI.
        - ``Word`` specifies the protocol type to word.
        - ``Symbol`` specifies the protocol type to symbol.
    """


class BusBItemCphySignaltype(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CPHY:SIGNALTYpe`` command.

    Description:
        - This command sets or queries the signal type for CPHY bus decode. The bus is specified by
          x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:SIGNALTYpe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:SIGNALTYpe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:SIGNALTYpe value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CPHY:SIGNALTYpe {SINGLE|DIFF}
        - BUS:B<x>:CPHY:SIGNALTYpe?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``SINGLE`` specifies the signal type to single ended.
        - ``DIFF`` specifies the signal type to differential. The default type is differential.
    """


class BusBItemCphyLpDirection(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CPHY:LP:DIRection`` command.

    Description:
        - This command sets or queries the CPHY bus direction in low power. The bus is specified by
          x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:LP:DIRection?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:LP:DIRection?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:LP:DIRection value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CPHY:LP:DIRection {forward|reverse}
        - BUS:B<x>:CPHY:LP:DIRection?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``forward`` specifies the direction in low power to forward. The default direction is
          forward.
        - ``reverse`` specifies the direction in low power to reverse.
    """


class BusBItemCphyLp(SCPICmdRead):
    """The ``BUS:B<x>:CPHY:LP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:LP?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:LP?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.direction``: The ``BUS:B<x>:CPHY:LP:DIRection`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._direction = BusBItemCphyLpDirection(device, f"{self._cmd_syntax}:DIRection")

    @property
    def direction(self) -> BusBItemCphyLpDirection:
        """Return the ``BUS:B<x>:CPHY:LP:DIRection`` command.

        Description:
            - This command sets or queries the CPHY bus direction in low power. The bus is specified
              by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:LP:DIRection?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:LP:DIRection?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:LP:DIRection value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CPHY:LP:DIRection {forward|reverse}
            - BUS:B<x>:CPHY:LP:DIRection?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``forward`` specifies the direction in low power to forward. The default direction is
              forward.
            - ``reverse`` specifies the direction in low power to reverse.
        """
        return self._direction


class BusBItemCphyCgndThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CPHY:CGND:THReshold`` command.

    Description:
        - This command sets or queries the CPHY differential CGND source threshold for the specified
          bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:CGND:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:CGND:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:CGND:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CPHY:CGND:THReshold <NR3>
        - BUS:B<x>:CPHY:CGND:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the CPHY differential C GND threshold for the specified bus. The argument
          range is -8 V to +8 V.
    """


class BusBItemCphyCgndSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CPHY:CGND:SOUrce`` command.

    Description:
        - This command sets or queries the CPHY differential CGND source for the specified bus line.
          The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:CGND:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:CGND:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:CGND:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CPHY:CGND:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:CPHY:CGND:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog/digital channel as the source.
        - ``MATH<x>`` specifies a math channel as the source.
        - ``REF<x>`` specifies an analog/digital reference waveform as the source.
    """


class BusBItemCphyCgnd(SCPICmdRead):
    """The ``BUS:B<x>:CPHY:CGND`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:CGND?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:CGND?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.source``: The ``BUS:B<x>:CPHY:CGND:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:CPHY:CGND:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemCphyCgndSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemCphyCgndThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def source(self) -> BusBItemCphyCgndSource:
        """Return the ``BUS:B<x>:CPHY:CGND:SOUrce`` command.

        Description:
            - This command sets or queries the CPHY differential CGND source for the specified bus
              line. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:CGND:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:CGND:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:CGND:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CPHY:CGND:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:CPHY:CGND:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog/digital channel as the source.
            - ``MATH<x>`` specifies a math channel as the source.
            - ``REF<x>`` specifies an analog/digital reference waveform as the source.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemCphyCgndThreshold:
        """Return the ``BUS:B<x>:CPHY:CGND:THReshold`` command.

        Description:
            - This command sets or queries the CPHY differential CGND source threshold for the
              specified bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:CGND:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:CGND:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:CPHY:CGND:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CPHY:CGND:THReshold <NR3>
            - BUS:B<x>:CPHY:CGND:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the CPHY differential C GND threshold for the specified bus. The argument
              range is -8 V to +8 V.
        """
        return self._threshold


class BusBItemCphyCaThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CPHY:CA:THReshold`` command.

    Description:
        - This command sets or queries the CPHY differential CA source threshold for the specified
          bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:CA:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:CA:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:CA:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CPHY:CA:THReshold <NR3>
        - BUS:B<x>:CPHY:CA:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the CPHY differential CA threshold for the specified bus. The argument range
          is -8 V to +8 V.
    """


class BusBItemCphyCaSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CPHY:CA:SOUrce`` command.

    Description:
        - This command sets or queries the CPHY differential CA source for the specified bus line.
          The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:CA:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:CA:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:CA:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CPHY:CA:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:CPHY:CA:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog/digital channel as the source.
        - ``MATH<x>`` specifies a math channel as the source.
        - ``REF<x>`` specifies an analog/digital reference waveform as the source.
    """


class BusBItemCphyCa(SCPICmdRead):
    """The ``BUS:B<x>:CPHY:CA`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:CA?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:CA?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.source``: The ``BUS:B<x>:CPHY:CA:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:CPHY:CA:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemCphyCaSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemCphyCaThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def source(self) -> BusBItemCphyCaSource:
        """Return the ``BUS:B<x>:CPHY:CA:SOUrce`` command.

        Description:
            - This command sets or queries the CPHY differential CA source for the specified bus
              line. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:CA:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:CA:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:CA:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CPHY:CA:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:CPHY:CA:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog/digital channel as the source.
            - ``MATH<x>`` specifies a math channel as the source.
            - ``REF<x>`` specifies an analog/digital reference waveform as the source.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemCphyCaThreshold:
        """Return the ``BUS:B<x>:CPHY:CA:THReshold`` command.

        Description:
            - This command sets or queries the CPHY differential CA source threshold for the
              specified bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:CA:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:CA:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:CA:THReshold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CPHY:CA:THReshold <NR3>
            - BUS:B<x>:CPHY:CA:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the CPHY differential CA threshold for the specified bus. The argument
              range is -8 V to +8 V.
        """
        return self._threshold


class BusBItemCphyCSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CPHY:C:SOUrce`` command.

    Description:
        - This command sets or queries the CPHY Single Ended C source for the specified bus line.
          The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:C:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:C:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:C:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CPHY:C:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:CPHY:C:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``MATH<x>`` specifies a math channel as the source.
        - ``REF<x>`` specifies an analog reference waveform as the source.
    """


class BusBItemCphyCLpThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CPHY:C:LP:THRESHold`` command.

    Description:
        - This command sets or queries the CPHY Single Ended C LP threshold for the specified bus.
          The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:C:LP:THRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:C:LP:THRESHold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:C:LP:THRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CPHY:C:LP:THRESHold <NR3>
        - BUS:B<x>:CPHY:C:LP:THRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the CPHY Single Ended C LP threshold for the specified bus. The argument
          range is -8 V to +8 V.
    """


class BusBItemCphyCLp(SCPICmdRead):
    """The ``BUS:B<x>:CPHY:C:LP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:C:LP?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:C:LP?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.threshold``: The ``BUS:B<x>:CPHY:C:LP:THRESHold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._threshold = BusBItemCphyCLpThreshold(device, f"{self._cmd_syntax}:THRESHold")

    @property
    def threshold(self) -> BusBItemCphyCLpThreshold:
        """Return the ``BUS:B<x>:CPHY:C:LP:THRESHold`` command.

        Description:
            - This command sets or queries the CPHY Single Ended C LP threshold for the specified
              bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:C:LP:THRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:C:LP:THRESHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:CPHY:C:LP:THRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CPHY:C:LP:THRESHold <NR3>
            - BUS:B<x>:CPHY:C:LP:THRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the CPHY Single Ended C LP threshold for the specified bus. The argument
              range is -8 V to +8 V.
        """
        return self._threshold


class BusBItemCphyCDataThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CPHY:C:DATA:THRESHold`` command.

    Description:
        - This command sets or queries the CPHY Single Ended C source threshold for the specified
          bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:C:DATA:THRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:C:DATA:THRESHold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:C:DATA:THRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CPHY:C:DATA:THRESHold <NR3>
        - BUS:B<x>:CPHY:C:DATA:THRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the CPHY Single Ended C threshold for the specified bus. The argument range
          is -8 V to +8 V.
    """


class BusBItemCphyCData(SCPICmdRead):
    """The ``BUS:B<x>:CPHY:C:DATA`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:C:DATA?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:C:DATA?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.threshold``: The ``BUS:B<x>:CPHY:C:DATA:THRESHold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._threshold = BusBItemCphyCDataThreshold(device, f"{self._cmd_syntax}:THRESHold")

    @property
    def threshold(self) -> BusBItemCphyCDataThreshold:
        """Return the ``BUS:B<x>:CPHY:C:DATA:THRESHold`` command.

        Description:
            - This command sets or queries the CPHY Single Ended C source threshold for the
              specified bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:C:DATA:THRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:C:DATA:THRESHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:CPHY:C:DATA:THRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CPHY:C:DATA:THRESHold <NR3>
            - BUS:B<x>:CPHY:C:DATA:THRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the CPHY Single Ended C threshold for the specified bus. The argument
              range is -8 V to +8 V.
        """
        return self._threshold


class BusBItemCphyC(SCPICmdRead):
    """The ``BUS:B<x>:CPHY:C`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:C?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:C?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.data``: The ``BUS:B<x>:CPHY:C:DATA`` command tree.
        - ``.lp``: The ``BUS:B<x>:CPHY:C:LP`` command tree.
        - ``.source``: The ``BUS:B<x>:CPHY:C:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._data = BusBItemCphyCData(device, f"{self._cmd_syntax}:DATA")
        self._lp = BusBItemCphyCLp(device, f"{self._cmd_syntax}:LP")
        self._source = BusBItemCphyCSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def data(self) -> BusBItemCphyCData:
        """Return the ``BUS:B<x>:CPHY:C:DATA`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:C:DATA?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:C:DATA?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.threshold``: The ``BUS:B<x>:CPHY:C:DATA:THRESHold`` command.
        """
        return self._data

    @property
    def lp(self) -> BusBItemCphyCLp:
        """Return the ``BUS:B<x>:CPHY:C:LP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:C:LP?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:C:LP?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.threshold``: The ``BUS:B<x>:CPHY:C:LP:THRESHold`` command.
        """
        return self._lp

    @property
    def source(self) -> BusBItemCphyCSource:
        """Return the ``BUS:B<x>:CPHY:C:SOUrce`` command.

        Description:
            - This command sets or queries the CPHY Single Ended C source for the specified bus
              line. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:C:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:C:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:C:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CPHY:C:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:CPHY:C:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``MATH<x>`` specifies a math channel as the source.
            - ``REF<x>`` specifies an analog reference waveform as the source.
        """
        return self._source


class BusBItemCphyBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CPHY:BITRate`` command.

    Description:
        - This command sets or queries the bit rate for the specified CPHY bus. The bus is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:BITRate value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CPHY:BITRate <NR1>
        - BUS:B<x>:CPHY:BITRate?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` specifies the bit rate. The default bit rate is 1 Gbps and varies 4 Mbps ~
          10Gps.
    """


class BusBItemCphyBcThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CPHY:BC:THReshold`` command.

    Description:
        - This command sets or queries the CPHY differential BC source threshold for the specified
          bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:BC:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:BC:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:BC:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CPHY:BC:THReshold <NR3>
        - BUS:B<x>:CPHY:BC:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the CPHY differential BC threshold for the specified bus. The argument range
          is -8 V to +8 V.
    """


class BusBItemCphyBcSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CPHY:BC:SOUrce`` command.

    Description:
        - This command sets or queries the CPHY differential BC source for the specified bus line.
          The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:BC:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:BC:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:BC:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CPHY:BC:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:CPHY:BC:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog/digital channel as the source.
        - ``MATH<x>`` specifies a math channel as the source.
        - ``REF<x>`` specifies an analog/digital reference waveform as the source.
    """


class BusBItemCphyBc(SCPICmdRead):
    """The ``BUS:B<x>:CPHY:BC`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:BC?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:BC?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.source``: The ``BUS:B<x>:CPHY:BC:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:CPHY:BC:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemCphyBcSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemCphyBcThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def source(self) -> BusBItemCphyBcSource:
        """Return the ``BUS:B<x>:CPHY:BC:SOUrce`` command.

        Description:
            - This command sets or queries the CPHY differential BC source for the specified bus
              line. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:BC:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:BC:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:BC:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CPHY:BC:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:CPHY:BC:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog/digital channel as the source.
            - ``MATH<x>`` specifies a math channel as the source.
            - ``REF<x>`` specifies an analog/digital reference waveform as the source.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemCphyBcThreshold:
        """Return the ``BUS:B<x>:CPHY:BC:THReshold`` command.

        Description:
            - This command sets or queries the CPHY differential BC source threshold for the
              specified bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:BC:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:BC:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:BC:THReshold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CPHY:BC:THReshold <NR3>
            - BUS:B<x>:CPHY:BC:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the CPHY differential BC threshold for the specified bus. The argument
              range is -8 V to +8 V.
        """
        return self._threshold


class BusBItemCphyBSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CPHY:B:SOUrce`` command.

    Description:
        - This command sets or queries the CPHY Single Ended B source for the specified bus line.
          The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:B:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:B:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:B:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CPHY:B:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:CPHY:B:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``MATH<x>`` specifies a math channel as the source.
        - ``REF<x>`` specifies an analog reference waveform as the source.
    """


class BusBItemCphyBDataThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CPHY:B:DATA:THRESHold`` command.

    Description:
        - This command sets or queries the CPHY Single Ended B source threshold for the specified
          bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:B:DATA:THRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:B:DATA:THRESHold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:B:DATA:THRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CPHY:B:DATA:THRESHold <NR3>
        - BUS:B<x>:CPHY:B:DATA:THRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the CPHY Single Ended B threshold for the specified bus. The argument range
          is -8 V to +8 V.
    """


class BusBItemCphyBData(SCPICmdRead):
    """The ``BUS:B<x>:CPHY:B:DATA`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:B:DATA?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:B:DATA?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.threshold``: The ``BUS:B<x>:CPHY:B:DATA:THRESHold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._threshold = BusBItemCphyBDataThreshold(device, f"{self._cmd_syntax}:THRESHold")

    @property
    def threshold(self) -> BusBItemCphyBDataThreshold:
        """Return the ``BUS:B<x>:CPHY:B:DATA:THRESHold`` command.

        Description:
            - This command sets or queries the CPHY Single Ended B source threshold for the
              specified bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:B:DATA:THRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:B:DATA:THRESHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:CPHY:B:DATA:THRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CPHY:B:DATA:THRESHold <NR3>
            - BUS:B<x>:CPHY:B:DATA:THRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the CPHY Single Ended B threshold for the specified bus. The argument
              range is -8 V to +8 V.
        """
        return self._threshold


class BusBItemCphyB(SCPICmdRead):
    """The ``BUS:B<x>:CPHY:B`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:B?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:B?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.data``: The ``BUS:B<x>:CPHY:B:DATA`` command tree.
        - ``.source``: The ``BUS:B<x>:CPHY:B:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._data = BusBItemCphyBData(device, f"{self._cmd_syntax}:DATA")
        self._source = BusBItemCphyBSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def data(self) -> BusBItemCphyBData:
        """Return the ``BUS:B<x>:CPHY:B:DATA`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:B:DATA?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:B:DATA?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.threshold``: The ``BUS:B<x>:CPHY:B:DATA:THRESHold`` command.
        """
        return self._data

    @property
    def source(self) -> BusBItemCphyBSource:
        """Return the ``BUS:B<x>:CPHY:B:SOUrce`` command.

        Description:
            - This command sets or queries the CPHY Single Ended B source for the specified bus
              line. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:B:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:B:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:B:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CPHY:B:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:CPHY:B:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``MATH<x>`` specifies a math channel as the source.
            - ``REF<x>`` specifies an analog reference waveform as the source.
        """
        return self._source


class BusBItemCphyAgndThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CPHY:AGND:THReshold`` command.

    Description:
        - This command sets or queries the CPHY differential AGND source threshold for the specified
          bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:AGND:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:AGND:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:AGND:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CPHY:AGND:THReshold <NR3>
        - BUS:B<x>:CPHY:AGND:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the CPHY differential A GND threshold for the specified bus. The argument
          range is -8 V to +8 V.
    """


class BusBItemCphyAgndSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CPHY:AGND:SOUrce`` command.

    Description:
        - This command sets or queries the CPHY differential AGND source for the specified bus line.
          The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:AGND:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:AGND:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:AGND:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CPHY:AGND:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:CPHY:AGND:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog/digital channel as the source.
        - ``MATH<x>`` specifies a math channel as the source.
        - ``REF<x>`` specifies an analog/digital reference waveform as the source.
    """


class BusBItemCphyAgnd(SCPICmdRead):
    """The ``BUS:B<x>:CPHY:AGND`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:AGND?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:AGND?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.source``: The ``BUS:B<x>:CPHY:AGND:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:CPHY:AGND:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemCphyAgndSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemCphyAgndThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def source(self) -> BusBItemCphyAgndSource:
        """Return the ``BUS:B<x>:CPHY:AGND:SOUrce`` command.

        Description:
            - This command sets or queries the CPHY differential AGND source for the specified bus
              line. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:AGND:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:AGND:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:AGND:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CPHY:AGND:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:CPHY:AGND:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog/digital channel as the source.
            - ``MATH<x>`` specifies a math channel as the source.
            - ``REF<x>`` specifies an analog/digital reference waveform as the source.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemCphyAgndThreshold:
        """Return the ``BUS:B<x>:CPHY:AGND:THReshold`` command.

        Description:
            - This command sets or queries the CPHY differential AGND source threshold for the
              specified bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:AGND:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:AGND:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:CPHY:AGND:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CPHY:AGND:THReshold <NR3>
            - BUS:B<x>:CPHY:AGND:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the CPHY differential A GND threshold for the specified bus. The argument
              range is -8 V to +8 V.
        """
        return self._threshold


class BusBItemCphyAbThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CPHY:AB:THReshold`` command.

    Description:
        - This command sets or queries the CPHY differential AB source threshold for the specified
          bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:AB:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:AB:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:AB:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CPHY:AB:THReshold <NR3>
        - BUS:B<x>:CPHY:AB:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the CPHY differential AB threshold for the specified bus. The argument range
          is -8 V to +8 V.
    """


class BusBItemCphyAbSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CPHY:AB:SOUrce`` command.

    Description:
        - This command sets or queries the CPHY differential AB source for the specified bus line.
          The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:AB:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:AB:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:AB:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CPHY:AB:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:CPHY:AB:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog/digital channel as the source.
        - ``MATH<x>`` specifies a math channel as the source.
        - ``REF<x>`` specifies an analog/digital reference waveform as the source.
    """


class BusBItemCphyAb(SCPICmdRead):
    """The ``BUS:B<x>:CPHY:AB`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:AB?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:AB?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.source``: The ``BUS:B<x>:CPHY:AB:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:CPHY:AB:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemCphyAbSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemCphyAbThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def source(self) -> BusBItemCphyAbSource:
        """Return the ``BUS:B<x>:CPHY:AB:SOUrce`` command.

        Description:
            - This command sets or queries the CPHY differential AB source for the specified bus
              line. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:AB:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:AB:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:AB:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CPHY:AB:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:CPHY:AB:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog/digital channel as the source.
            - ``MATH<x>`` specifies a math channel as the source.
            - ``REF<x>`` specifies an analog/digital reference waveform as the source.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemCphyAbThreshold:
        """Return the ``BUS:B<x>:CPHY:AB:THReshold`` command.

        Description:
            - This command sets or queries the CPHY differential AB source threshold for the
              specified bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:AB:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:AB:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:AB:THReshold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CPHY:AB:THReshold <NR3>
            - BUS:B<x>:CPHY:AB:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the CPHY differential AB threshold for the specified bus. The argument
              range is -8 V to +8 V.
        """
        return self._threshold


class BusBItemCphyASource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CPHY:A:SOUrce`` command.

    Description:
        - This command sets or queries the CPHY Single Ended A source for the specified bus line.
          The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:A:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:A:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:A:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CPHY:A:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
        - BUS:B<x>:CPHY:A:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``MATH<x>`` specifies a math channel as the source.
        - ``REF<x>`` specifies an analog reference waveform as the source.
    """


class BusBItemCphyALpThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CPHY:A:LP:THRESHold`` command.

    Description:
        - This command sets or queries the CPHY Single Ended A LP threshold for the specified bus.
          The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:A:LP:THRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:A:LP:THRESHold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:A:LP:THRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CPHY:A:LP:THRESHold <NR3>
        - BUS:B<x>:CPHY:A:LP:THRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the CPHY Single Ended A LP threshold in Volts for the specified bus. The
          argument range is -8 V to +8 V.
    """


class BusBItemCphyALp(SCPICmdRead):
    """The ``BUS:B<x>:CPHY:A:LP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:A:LP?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:A:LP?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.threshold``: The ``BUS:B<x>:CPHY:A:LP:THRESHold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._threshold = BusBItemCphyALpThreshold(device, f"{self._cmd_syntax}:THRESHold")

    @property
    def threshold(self) -> BusBItemCphyALpThreshold:
        """Return the ``BUS:B<x>:CPHY:A:LP:THRESHold`` command.

        Description:
            - This command sets or queries the CPHY Single Ended A LP threshold for the specified
              bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:A:LP:THRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:A:LP:THRESHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:CPHY:A:LP:THRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CPHY:A:LP:THRESHold <NR3>
            - BUS:B<x>:CPHY:A:LP:THRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the CPHY Single Ended A LP threshold in Volts for the specified bus. The
              argument range is -8 V to +8 V.
        """
        return self._threshold


class BusBItemCphyADataThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CPHY:A:DATA:THRESHold`` command.

    Description:
        - This command sets or queries the CPHY Single Ended A source threshold for the specified
          bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:A:DATA:THRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:A:DATA:THRESHold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:A:DATA:THRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CPHY:A:DATA:THRESHold <NR3>
        - BUS:B<x>:CPHY:A:DATA:THRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the CPHY Single Ended A threshold in Volts for the specified bus. The
          argument range is -8 V to +8 V.
    """


class BusBItemCphyAData(SCPICmdRead):
    """The ``BUS:B<x>:CPHY:A:DATA`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:A:DATA?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:A:DATA?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.threshold``: The ``BUS:B<x>:CPHY:A:DATA:THRESHold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._threshold = BusBItemCphyADataThreshold(device, f"{self._cmd_syntax}:THRESHold")

    @property
    def threshold(self) -> BusBItemCphyADataThreshold:
        """Return the ``BUS:B<x>:CPHY:A:DATA:THRESHold`` command.

        Description:
            - This command sets or queries the CPHY Single Ended A source threshold for the
              specified bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:A:DATA:THRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:A:DATA:THRESHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:CPHY:A:DATA:THRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CPHY:A:DATA:THRESHold <NR3>
            - BUS:B<x>:CPHY:A:DATA:THRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the CPHY Single Ended A threshold in Volts for the specified bus. The
              argument range is -8 V to +8 V.
        """
        return self._threshold


class BusBItemCphyA(SCPICmdRead):
    """The ``BUS:B<x>:CPHY:A`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:A?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:A?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.data``: The ``BUS:B<x>:CPHY:A:DATA`` command tree.
        - ``.lp``: The ``BUS:B<x>:CPHY:A:LP`` command tree.
        - ``.source``: The ``BUS:B<x>:CPHY:A:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._data = BusBItemCphyAData(device, f"{self._cmd_syntax}:DATA")
        self._lp = BusBItemCphyALp(device, f"{self._cmd_syntax}:LP")
        self._source = BusBItemCphyASource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def data(self) -> BusBItemCphyAData:
        """Return the ``BUS:B<x>:CPHY:A:DATA`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:A:DATA?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:A:DATA?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.threshold``: The ``BUS:B<x>:CPHY:A:DATA:THRESHold`` command.
        """
        return self._data

    @property
    def lp(self) -> BusBItemCphyALp:
        """Return the ``BUS:B<x>:CPHY:A:LP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:A:LP?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:A:LP?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.threshold``: The ``BUS:B<x>:CPHY:A:LP:THRESHold`` command.
        """
        return self._lp

    @property
    def source(self) -> BusBItemCphyASource:
        """Return the ``BUS:B<x>:CPHY:A:SOUrce`` command.

        Description:
            - This command sets or queries the CPHY Single Ended A source for the specified bus
              line. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:A:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:A:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:A:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CPHY:A:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x>}
            - BUS:B<x>:CPHY:A:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``MATH<x>`` specifies a math channel as the source.
            - ``REF<x>`` specifies an analog reference waveform as the source.
        """
        return self._source


#  pylint: disable=too-many-instance-attributes
class BusBItemCphy(SCPICmdRead):
    """The ``BUS:B<x>:CPHY`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.a``: The ``BUS:B<x>:CPHY:A`` command tree.
        - ``.ab``: The ``BUS:B<x>:CPHY:AB`` command tree.
        - ``.agnd``: The ``BUS:B<x>:CPHY:AGND`` command tree.
        - ``.b``: The ``BUS:B<x>:CPHY:B`` command tree.
        - ``.bc``: The ``BUS:B<x>:CPHY:BC`` command tree.
        - ``.bitrate``: The ``BUS:B<x>:CPHY:BITRate`` command.
        - ``.c``: The ``BUS:B<x>:CPHY:C`` command tree.
        - ``.ca``: The ``BUS:B<x>:CPHY:CA`` command tree.
        - ``.cgnd``: The ``BUS:B<x>:CPHY:CGND`` command tree.
        - ``.lp``: The ``BUS:B<x>:CPHY:LP`` command tree.
        - ``.signaltype``: The ``BUS:B<x>:CPHY:SIGNALTYpe`` command.
        - ``.subtype``: The ``BUS:B<x>:CPHY:SUBTYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._a = BusBItemCphyA(device, f"{self._cmd_syntax}:A")
        self._ab = BusBItemCphyAb(device, f"{self._cmd_syntax}:AB")
        self._agnd = BusBItemCphyAgnd(device, f"{self._cmd_syntax}:AGND")
        self._b = BusBItemCphyB(device, f"{self._cmd_syntax}:B")
        self._bc = BusBItemCphyBc(device, f"{self._cmd_syntax}:BC")
        self._bitrate = BusBItemCphyBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._c = BusBItemCphyC(device, f"{self._cmd_syntax}:C")
        self._ca = BusBItemCphyCa(device, f"{self._cmd_syntax}:CA")
        self._cgnd = BusBItemCphyCgnd(device, f"{self._cmd_syntax}:CGND")
        self._lp = BusBItemCphyLp(device, f"{self._cmd_syntax}:LP")
        self._signaltype = BusBItemCphySignaltype(device, f"{self._cmd_syntax}:SIGNALTYpe")
        self._subtype = BusBItemCphySubtype(device, f"{self._cmd_syntax}:SUBTYPe")

    @property
    def a(self) -> BusBItemCphyA:
        """Return the ``BUS:B<x>:CPHY:A`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:A?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:A?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.data``: The ``BUS:B<x>:CPHY:A:DATA`` command tree.
            - ``.lp``: The ``BUS:B<x>:CPHY:A:LP`` command tree.
            - ``.source``: The ``BUS:B<x>:CPHY:A:SOUrce`` command.
        """
        return self._a

    @property
    def ab(self) -> BusBItemCphyAb:
        """Return the ``BUS:B<x>:CPHY:AB`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:AB?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:AB?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:CPHY:AB:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:CPHY:AB:THReshold`` command.
        """
        return self._ab

    @property
    def agnd(self) -> BusBItemCphyAgnd:
        """Return the ``BUS:B<x>:CPHY:AGND`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:AGND?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:AGND?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:CPHY:AGND:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:CPHY:AGND:THReshold`` command.
        """
        return self._agnd

    @property
    def b(self) -> BusBItemCphyB:
        """Return the ``BUS:B<x>:CPHY:B`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:B?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:B?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.data``: The ``BUS:B<x>:CPHY:B:DATA`` command tree.
            - ``.source``: The ``BUS:B<x>:CPHY:B:SOUrce`` command.
        """
        return self._b

    @property
    def bc(self) -> BusBItemCphyBc:
        """Return the ``BUS:B<x>:CPHY:BC`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:BC?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:BC?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:CPHY:BC:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:CPHY:BC:THReshold`` command.
        """
        return self._bc

    @property
    def bitrate(self) -> BusBItemCphyBitrate:
        """Return the ``BUS:B<x>:CPHY:BITRate`` command.

        Description:
            - This command sets or queries the bit rate for the specified CPHY bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:BITRate?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CPHY:BITRate <NR1>
            - BUS:B<x>:CPHY:BITRate?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` specifies the bit rate. The default bit rate is 1 Gbps and varies 4 Mbps ~
              10Gps.
        """
        return self._bitrate

    @property
    def c(self) -> BusBItemCphyC:
        """Return the ``BUS:B<x>:CPHY:C`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:C?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:C?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.data``: The ``BUS:B<x>:CPHY:C:DATA`` command tree.
            - ``.lp``: The ``BUS:B<x>:CPHY:C:LP`` command tree.
            - ``.source``: The ``BUS:B<x>:CPHY:C:SOUrce`` command.
        """
        return self._c

    @property
    def ca(self) -> BusBItemCphyCa:
        """Return the ``BUS:B<x>:CPHY:CA`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:CA?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:CA?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:CPHY:CA:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:CPHY:CA:THReshold`` command.
        """
        return self._ca

    @property
    def cgnd(self) -> BusBItemCphyCgnd:
        """Return the ``BUS:B<x>:CPHY:CGND`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:CGND?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:CGND?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:CPHY:CGND:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:CPHY:CGND:THReshold`` command.
        """
        return self._cgnd

    @property
    def lp(self) -> BusBItemCphyLp:
        """Return the ``BUS:B<x>:CPHY:LP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:LP?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:LP?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.direction``: The ``BUS:B<x>:CPHY:LP:DIRection`` command.
        """
        return self._lp

    @property
    def signaltype(self) -> BusBItemCphySignaltype:
        """Return the ``BUS:B<x>:CPHY:SIGNALTYpe`` command.

        Description:
            - This command sets or queries the signal type for CPHY bus decode. The bus is specified
              by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:SIGNALTYpe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:SIGNALTYpe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:SIGNALTYpe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CPHY:SIGNALTYpe {SINGLE|DIFF}
            - BUS:B<x>:CPHY:SIGNALTYpe?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``SINGLE`` specifies the signal type to single ended.
            - ``DIFF`` specifies the signal type to differential. The default type is differential.
        """
        return self._signaltype

    @property
    def subtype(self) -> BusBItemCphySubtype:
        """Return the ``BUS:B<x>:CPHY:SUBTYPe`` command.

        Description:
            - This command sets or queries the sub type for CPHY bus decode. The bus is specified by
              x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY:SUBTYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY:SUBTYPe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CPHY:SUBTYPe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CPHY:SUBTYPe {CSI|DSI|Word|Symbol}
            - BUS:B<x>:CPHY:SUBTYPe?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``CSI`` specifies the protocol type to CSI. The default type is CSI.
            - ``DSI`` specifies the protocol type to DSI.
            - ``Word`` specifies the protocol type to word.
            - ``Symbol`` specifies the protocol type to symbol.
        """
        return self._subtype


class BusBItemCanThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:THReshold`` command.

    Description:
        - This command sets or queries the source channel threshold for the specified CAN bus. The
          bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:THReshold?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:THReshold value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:THReshold <NR3>
        - BUS:B<x>:CAN:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the source channel threshold for the specified CAN bus.
    """


class BusBItemCanStandard(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:STANDard`` command.

    Description:
        - This command sets or queries which CAN standard specification to analyze the specified CAN
          bus with. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:STANDard?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:STANDard?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:STANDard value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:STANDard {CAN2X|FDISO|FDNONISO}
        - BUS:B<x>:CAN:STANDard?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``CAN2X`` sets the CAN bus standard to CAN 2.0.
        - ``FDISO`` sets the CAN bus standard to ISO CAN FD (11898-``1:2015``).
        - ``FDNONISO`` sets the CAN bus standard to non-ISO CAN FD (``Bosch:2012``).
    """


class BusBItemCanSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:SOUrce`` command.

    Description:
        - This command sets or queries the CAN source channel for the specified CAN bus. The bus
          number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:SOUrce?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:CAN:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>_D<x>`` specifies the remote scope number, the analog channel, and the digital
          channel.
        - ``CH<x>_D<x>`` specifies an analog channel and the digital channel as the source.
        - ``REF<x>_D<x>`` specifies a reference waveform and digital channel as the source.
        - ``CH<x>`` specifies an analog channel as the source.
        - ``Math<x>`` specifies a math waveform as the source.
        - ``REF<x>`` specifies a reference waveform as the source.
    """


class BusBItemCanSignal(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:SIGNal`` command.

    Description:
        - This command sets or queries the signal type for the specified CAN bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:SIGNal?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:SIGNal?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:SIGNal value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:SIGNal {DIFFerential|CANH|CANL|RX|TX}
        - BUS:B<x>:CAN:SIGNal?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
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


class BusBItemCanFdBitrateCustom(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:FD:BITRate:CUSTom`` command.

    Description:
        - This command sets or queries the custom bit rate for the increased data phase of CAN FD
          packets on the specified CAN bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:FD:BITRate:CUSTom?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:FD:BITRate:CUSTom?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:FD:BITRate:CUSTom value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:FD:BITRate:CUSTom <NR1>
        - BUS:B<x>:CAN:FD:BITRate:CUSTom?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` is the custom FD bit rate for the specified bus.
    """


class BusBItemCanFdBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:FD:BITRate`` command.

    Description:
        - This command sets or queries the increased data phase bit rate used by CAN FD packets on
          the specified CAN bus. The bus is specified by x. If you select Custom, use
          ``BUS:B<x>:CAN:FD:BITRate:CUSTom`` to set the bit rate.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:FD:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:FD:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:FD:BITRate value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:FD:BITRate {RATE1M|RATE2M|RATE3M|RATE4M|RATE5M|RATE6M|RATE7M|RATE8M|RATE9M|RATE10M|RATE11M|RATE12M|RATE13M|RATE14M|RATE15M|RATE16M|CUSTom}
        - BUS:B<x>:CAN:FD:BITRate?
        ```

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.custom``: The ``BUS:B<x>:CAN:FD:BITRate:CUSTom`` command.
    """  # noqa: E501

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._custom = BusBItemCanFdBitrateCustom(device, f"{self._cmd_syntax}:CUSTom")

    @property
    def custom(self) -> BusBItemCanFdBitrateCustom:
        """Return the ``BUS:B<x>:CAN:FD:BITRate:CUSTom`` command.

        Description:
            - This command sets or queries the custom bit rate for the increased data phase of CAN
              FD packets on the specified CAN bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:FD:BITRate:CUSTom?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:FD:BITRate:CUSTom?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:CAN:FD:BITRate:CUSTom value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:FD:BITRate:CUSTom <NR1>
            - BUS:B<x>:CAN:FD:BITRate:CUSTom?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` is the custom FD bit rate for the specified bus.
        """
        return self._custom


class BusBItemCanFd(SCPICmdRead):
    """The ``BUS:B<x>:CAN:FD`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:FD?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:FD?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:CAN:FD:BITRate`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemCanFdBitrate(device, f"{self._cmd_syntax}:BITRate")

    @property
    def bitrate(self) -> BusBItemCanFdBitrate:
        """Return the ``BUS:B<x>:CAN:FD:BITRate`` command.

        Description:
            - This command sets or queries the increased data phase bit rate used by CAN FD packets
              on the specified CAN bus. The bus is specified by x. If you select Custom, use
              ``BUS:B<x>:CAN:FD:BITRate:CUSTom`` to set the bit rate.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:FD:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:FD:BITRate?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:FD:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:FD:BITRate {RATE1M|RATE2M|RATE3M|RATE4M|RATE5M|RATE6M|RATE7M|RATE8M|RATE9M|RATE10M|RATE11M|RATE12M|RATE13M|RATE14M|RATE15M|RATE16M|CUSTom}
            - BUS:B<x>:CAN:FD:BITRate?
            ```

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.custom``: The ``BUS:B<x>:CAN:FD:BITRate:CUSTom`` command.
        """  # noqa: E501
        return self._bitrate


class BusBItemCanBitrateValue(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:BITRate:VALue`` command.

    Description:
        - This command sets or queries CAN bit rate when Custom is selected by
          ``BUS:BX:CAN:BITRATE``. The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:BITRate:VALue?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:BITRate:VALue?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:BITRate:VALue value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:BITRate:VALue <NR3>
        - BUS:B<x>:CAN:BITRate:VALue?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` specifies the CAN bit rate.
    """


class BusBItemCanBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:BITRate`` command.

    Description:
        - This command sets or queries the CAN bit rate. The bus number is specified by x. If you
          select Custom, use ``BUS:BX:CAN:BITRATE:VALUE`` to set the bit rate.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:BITRate value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:BITRate {RATE10K|RATE100K|RATE1M|RATE125K|RATE153K|RATE20K|RATE25K|RATE250K|RATE31K|RATE33K|RATE400K|RATE50K|RATE500K|RATE62K|RATE68K|RATE800K|RATE83K|RATE92K|CUSTom}
        - BUS:B<x>:CAN:BITRate?
        ```

    Info:
        - ``B<x>`` is the number of the bus.

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
            - This command sets or queries CAN bit rate when Custom is selected by
              ``BUS:BX:CAN:BITRATE``. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:BITRate:VALue?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:BITRate:VALue?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:BITRate:VALue value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:BITRate:VALue <NR3>
            - BUS:B<x>:CAN:BITRate:VALue?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` specifies the CAN bit rate.
        """
        return self._value


class BusBItemCan(SCPICmdRead):
    """The ``BUS:B<x>:CAN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:CAN:BITRate`` command.
        - ``.fd``: The ``BUS:B<x>:CAN:FD`` command tree.
        - ``.samplepoint``: The ``BUS:B<x>:CAN:SAMPLEpoint`` command.
        - ``.signal``: The ``BUS:B<x>:CAN:SIGNal`` command.
        - ``.source``: The ``BUS:B<x>:CAN:SOUrce`` command.
        - ``.standard``: The ``BUS:B<x>:CAN:STANDard`` command.
        - ``.threshold``: The ``BUS:B<x>:CAN:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemCanBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._fd = BusBItemCanFd(device, f"{self._cmd_syntax}:FD")
        self._samplepoint = BusBItemCanSamplepoint(device, f"{self._cmd_syntax}:SAMPLEpoint")
        self._signal = BusBItemCanSignal(device, f"{self._cmd_syntax}:SIGNal")
        self._source = BusBItemCanSource(device, f"{self._cmd_syntax}:SOUrce")
        self._standard = BusBItemCanStandard(device, f"{self._cmd_syntax}:STANDard")
        self._threshold = BusBItemCanThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def bitrate(self) -> BusBItemCanBitrate:
        """Return the ``BUS:B<x>:CAN:BITRate`` command.

        Description:
            - This command sets or queries the CAN bit rate. The bus number is specified by x. If
              you select Custom, use ``BUS:BX:CAN:BITRATE:VALUE`` to set the bit rate.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:BITRate?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:BITRate {RATE10K|RATE100K|RATE1M|RATE125K|RATE153K|RATE20K|RATE25K|RATE250K|RATE31K|RATE33K|RATE400K|RATE50K|RATE500K|RATE62K|RATE68K|RATE800K|RATE83K|RATE92K|CUSTom}
            - BUS:B<x>:CAN:BITRate?
            ```

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.value``: The ``BUS:B<x>:CAN:BITRate:VALue`` command.
        """  # noqa: E501
        return self._bitrate

    @property
    def fd(self) -> BusBItemCanFd:
        """Return the ``BUS:B<x>:CAN:FD`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:FD?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:FD?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:CAN:FD:BITRate`` command.
        """
        return self._fd

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
    def signal(self) -> BusBItemCanSignal:
        """Return the ``BUS:B<x>:CAN:SIGNal`` command.

        Description:
            - This command sets or queries the signal type for the specified CAN bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:SIGNal?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:SIGNal?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:SIGNal value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:SIGNal {DIFFerential|CANH|CANL|RX|TX}
            - BUS:B<x>:CAN:SIGNal?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
        """
        return self._signal

    @property
    def source(self) -> BusBItemCanSource:
        """Return the ``BUS:B<x>:CAN:SOUrce`` command.

        Description:
            - This command sets or queries the CAN source channel for the specified CAN bus. The bus
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:CAN:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>_D<x>`` specifies the remote scope number, the analog channel, and the
              digital channel.
            - ``CH<x>_D<x>`` specifies an analog channel and the digital channel as the source.
            - ``REF<x>_D<x>`` specifies a reference waveform and digital channel as the source.
            - ``CH<x>`` specifies an analog channel as the source.
            - ``Math<x>`` specifies a math waveform as the source.
            - ``REF<x>`` specifies a reference waveform as the source.
        """
        return self._source

    @property
    def standard(self) -> BusBItemCanStandard:
        """Return the ``BUS:B<x>:CAN:STANDard`` command.

        Description:
            - This command sets or queries which CAN standard specification to analyze the specified
              CAN bus with. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:STANDard?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:STANDard?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:STANDard value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:STANDard {CAN2X|FDISO|FDNONISO}
            - BUS:B<x>:CAN:STANDard?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``CAN2X`` sets the CAN bus standard to CAN 2.0.
            - ``FDISO`` sets the CAN bus standard to ISO CAN FD (11898-``1:2015``).
            - ``FDNONISO`` sets the CAN bus standard to non-ISO CAN FD (``Bosch:2012``).
        """
        return self._standard

    @property
    def threshold(self) -> BusBItemCanThreshold:
        """Return the ``BUS:B<x>:CAN:THReshold`` command.

        Description:
            - This command sets or queries the source channel threshold for the specified CAN bus.
              The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:THReshold?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:THReshold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:THReshold <NR3>
            - BUS:B<x>:CAN:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the source channel threshold for the specified CAN bus.
        """
        return self._threshold


class BusBItemAutoethernetType(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUTOETHERnet:TYPe`` command.

    Description:
        - This command sets or queries the AutoEthernet standard speed.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUTOETHERnet:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUTOETHERnet:TYPe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUTOETHERnet:TYPe value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUTOETHERnet:TYPe {HUNDREDBASET1}
        - BUS:B<x>:AUTOETHERnet:TYPe?
        ```

    Info:
        - ``B<x>`` is the Bus number.
        - ``HUNDREDBASET1`` specifies the AutoEthernet speed as 100Base-T1.
    """


class BusBItemAutoethernetThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUTOETHERnet:THRESHold`` command.

    Description:
        - This command sets or queries the AutoEthernet DATA source High threshold level for the
          specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUTOETHERnet:THRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUTOETHERnet:THRESHold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUTOETHERnet:THRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUTOETHERnet:THRESHold <NR3>
        - BUS:B<x>:AUTOETHERnet:THRESHold?
        ```

    Info:
        - ``B<x>`` is the Bus number.
        - ``NR3`` specifies the AutoEthernet DATA source High threshold level for the specified bus,
          in volts.
    """


class BusBItemAutoethernetSourceDplus(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUTOETHERnet:SOUrce:DPLUs`` command.

    Description:
        - This command sets or queries the AutoEthernet D+ source for the specified bus. This
          command specifies the source channel to use when the signal type is single ended.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUTOETHERnet:SOUrce:DPLUs?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUTOETHERnet:SOUrce:DPLUs?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:AUTOETHERnet:SOUrce:DPLUs value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUTOETHERnet:SOUrce:DPLUs {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
        - BUS:B<x>:AUTOETHERnet:SOUrce:DPLUs?
        ```

    Info:
        - ``Bus<x>`` is the Bus number.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
        - ``CH<x>`` specifies an analog channel as the source for the D+ signal, where <x> is the
          channel number.
        - ``MATH<x>`` specifies a math channel as the source for the D+ signal, where <x> is the
          math waveform number.
        - ``REF<x>`` specifies a reference waveform as the source for the D+ signal, where <x> is
          the reference waveform number.
    """


class BusBItemAutoethernetSourceDminus(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUTOETHERnet:SOUrce:DMINus`` command.

    Description:
        - This command sets or queries the AutoEthernet D- source for the specified bus. This
          command specifies the source channel to use when the signal type is single ended.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUTOETHERnet:SOUrce:DMINus?``
          query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUTOETHERnet:SOUrce:DMINus?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:AUTOETHERnet:SOUrce:DMINus value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUTOETHERnet:SOUrce:DMINus {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
        - BUS:B<x>:AUTOETHERnet:SOUrce:DMINus?
        ```

    Info:
        - ``Bus<x>`` is the Bus number.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog channel as the source for the D- signal, where <x> is the
          channel number.
        - ``MATH<x>`` specifies a math channel as the source for the D- signal, where <x> is the
          math waveform number.
        - ``REF<x>`` specifies a reference waveform as the source for the D- signal, where <x> is
          the reference waveform number.
    """


class BusBItemAutoethernetSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUTOETHERnet:SOUrce`` command.

    Description:
        - This command sets or queries the AutoEthernet data (SDATA) source for the specified bus.
          This command controls the source channel when the signal type is differential.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUTOETHERnet:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUTOETHERnet:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUTOETHERnet:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUTOETHERnet:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
        - BUS:B<x>:AUTOETHERnet:SOUrce?
        ```

    Info:
        - ``Bus<x>`` is the Bus number.
        - ``CH<x>`` specifies an analog channel as the AutoEthernet data source for differential
          input, where <x> is the channel number.
        - ``MATH<x>`` specifies a math channel as the AutoEthernet data source for differential
          input, where <x> is the math waveform number.
        - ``REF<x>`` specifies a reference waveform as the AutoEthernet data source for differential
          input, where <x> is the reference waveform number.
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.

    Properties:
        - ``.dminus``: The ``BUS:B<x>:AUTOETHERnet:SOUrce:DMINus`` command.
        - ``.dplus``: The ``BUS:B<x>:AUTOETHERnet:SOUrce:DPLUs`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._dminus = BusBItemAutoethernetSourceDminus(device, f"{self._cmd_syntax}:DMINus")
        self._dplus = BusBItemAutoethernetSourceDplus(device, f"{self._cmd_syntax}:DPLUs")

    @property
    def dminus(self) -> BusBItemAutoethernetSourceDminus:
        """Return the ``BUS:B<x>:AUTOETHERnet:SOUrce:DMINus`` command.

        Description:
            - This command sets or queries the AutoEthernet D- source for the specified bus. This
              command specifies the source channel to use when the signal type is single ended.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUTOETHERnet:SOUrce:DMINus?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:AUTOETHERnet:SOUrce:DMINus?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:AUTOETHERnet:SOUrce:DMINus value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUTOETHERnet:SOUrce:DMINus {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
            - BUS:B<x>:AUTOETHERnet:SOUrce:DMINus?
            ```

        Info:
            - ``Bus<x>`` is the Bus number.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog channel as the source for the D- signal, where <x> is
              the channel number.
            - ``MATH<x>`` specifies a math channel as the source for the D- signal, where <x> is the
              math waveform number.
            - ``REF<x>`` specifies a reference waveform as the source for the D- signal, where <x>
              is the reference waveform number.
        """
        return self._dminus

    @property
    def dplus(self) -> BusBItemAutoethernetSourceDplus:
        """Return the ``BUS:B<x>:AUTOETHERnet:SOUrce:DPLUs`` command.

        Description:
            - This command sets or queries the AutoEthernet D+ source for the specified bus. This
              command specifies the source channel to use when the signal type is single ended.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUTOETHERnet:SOUrce:DPLUs?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:AUTOETHERnet:SOUrce:DPLUs?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:AUTOETHERnet:SOUrce:DPLUs value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUTOETHERnet:SOUrce:DPLUs {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
            - BUS:B<x>:AUTOETHERnet:SOUrce:DPLUs?
            ```

        Info:
            - ``Bus<x>`` is the Bus number.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.
            - ``CH<x>`` specifies an analog channel as the source for the D+ signal, where <x> is
              the channel number.
            - ``MATH<x>`` specifies a math channel as the source for the D+ signal, where <x> is the
              math waveform number.
            - ``REF<x>`` specifies a reference waveform as the source for the D+ signal, where <x>
              is the reference waveform number.
        """
        return self._dplus


class BusBItemAutoethernetSignaltype(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUTOETHERnet:SIGNALTYpe`` command.

    Description:
        - This command sets or queries the AutoEthernet signal type for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUTOETHERnet:SIGNALTYpe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUTOETHERnet:SIGNALTYpe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:AUTOETHERnet:SIGNALTYpe value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUTOETHERnet:SIGNALTYpe {SINGLE|DIFF}
        - BUS:B<x>:AUTOETHERnet:SIGNALTYpe?
        ```

    Info:
        - ``B<x>`` is the Bus number.
        - ``SINGLE`` specifies single-ended signals.
        - ``DIFF`` specifies differential signals.
    """


class BusBItemAutoethernetLowthreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUTOETHERnet:LOWTHRESHold`` command.

    Description:
        - This command sets or queries the AutoEthernet Data source Low threshold level for the
          specified bus. This threshold only applies when the AutoEthernet signal type is
          differential.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUTOETHERnet:LOWTHRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUTOETHERnet:LOWTHRESHold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:AUTOETHERnet:LOWTHRESHold value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUTOETHERnet:LOWTHRESHold <NR3>
        - BUS:B<x>:AUTOETHERnet:LOWTHRESHold?
        ```

    Info:
        - ``B<x>`` is the Bus number.
        - ``NR3`` specifies the AutoEthernet DATA source Low threshold level for the specified bus,
          in volts. This threshold only applies when the AutoEthernet signal type is differential.
    """


class BusBItemAutoethernetLowdataplus(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUTOETHERnet:LOWDATAPLUS`` command.

    Description:
        - This command sets or queries the AutoEthernet D+ source low threshold level for the
          specified bus. This threshold only applies when the AutoEthernet signal type is single
          ended.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUTOETHERnet:LOWDATAPLUS?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUTOETHERnet:LOWDATAPLUS?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:AUTOETHERnet:LOWDATAPLUS value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUTOETHERnet:LOWDATAPLUS <NR3>
        - BUS:B<x>:AUTOETHERnet:LOWDATAPLUS?
        ```

    Info:
        - ``B<x>`` is the Bus number.
        - ``NR3`` specifies the AutoEthernet D+ source low threshold level for the specified bus, in
          volts. This threshold only applies when the AutoEthernet signal type is single ended.
    """


class BusBItemAutoethernetLowdataminus(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUTOETHERnet:LOWDATAMINus`` command.

    Description:
        - This command sets or queries the AutoEthernet D- source low threshold level for the
          specified bus. This threshold only applies when the AutoEthernet signal type is single
          ended.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUTOETHERnet:LOWDATAMINus?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUTOETHERnet:LOWDATAMINus?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:AUTOETHERnet:LOWDATAMINus value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUTOETHERnet:LOWDATAMINus <NR3>
        - BUS:B<x>:AUTOETHERnet:LOWDATAMINus?
        ```

    Info:
        - ``B<x>`` is the Bus number.
        - ``NR3`` specifies the AutoEthernet D- source low threshold level for the specified bus, in
          volts. This threshold only applies when the AutoEthernet signal type is single ended.
    """


class BusBItemAutoethernetDataplusthreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUTOETHERnet:DATAPLUSTHRESHold`` command.

    Description:
        - This command sets or queries the AutoEthernet D+ source threshold level for the specified
          bus. This threshold only applies when the AutoEthernet signal type is single ended.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUTOETHERnet:DATAPLUSTHRESHold?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``BUS:B<x>:AUTOETHERnet:DATAPLUSTHRESHold?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:AUTOETHERnet:DATAPLUSTHRESHold value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUTOETHERnet:DATAPLUSTHRESHold <NR3>
        - BUS:B<x>:AUTOETHERnet:DATAPLUSTHRESHold?
        ```

    Info:
        - ``B<x>`` is the Bus number.
        - ``NR3`` specifies the AutoEthernet D+ source threshold for the specified bus, in volts.
          This threshold only applies when the AutoEthernet signal type is single ended.
    """


class BusBItemAutoethernetDataminusthreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUTOETHERnet:DATAMINUSTHRESHOLD`` command.

    Description:
        - This command sets or queries the AutoEthernet D- source threshold level for the specified
          bus. This threshold only applies when the AutoEthernet signal type is single ended.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUTOETHERnet:DATAMINUSTHRESHOLD?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``BUS:B<x>:AUTOETHERnet:DATAMINUSTHRESHOLD?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:AUTOETHERnet:DATAMINUSTHRESHOLD value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUTOETHERnet:DATAMINUSTHRESHOLD <NR3>
        - BUS:B<x>:AUTOETHERnet:DATAMINUSTHRESHOLD?
        ```

    Info:
        - ``B<x>`` is the Bus number.
        - ``NR3`` specifies the AutoEthernet D- source threshold level for the specified bus, in
          volts. This threshold only applies when the AutoEthernet signal type is single ended.
    """


#  pylint: disable=too-many-instance-attributes
class BusBItemAutoethernet(SCPICmdRead):
    """The ``BUS:B<x>:AUTOETHERnet`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUTOETHERnet?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUTOETHERnet?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the Bus number.

    Properties:
        - ``.dataminusthreshold``: The ``BUS:B<x>:AUTOETHERnet:DATAMINUSTHRESHOLD`` command.
        - ``.dataplusthreshold``: The ``BUS:B<x>:AUTOETHERnet:DATAPLUSTHRESHold`` command.
        - ``.lowdataminus``: The ``BUS:B<x>:AUTOETHERnet:LOWDATAMINus`` command.
        - ``.lowdataplus``: The ``BUS:B<x>:AUTOETHERnet:LOWDATAPLUS`` command.
        - ``.lowthreshold``: The ``BUS:B<x>:AUTOETHERnet:LOWTHRESHold`` command.
        - ``.signaltype``: The ``BUS:B<x>:AUTOETHERnet:SIGNALTYpe`` command.
        - ``.source``: The ``BUS:B<x>:AUTOETHERnet:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:AUTOETHERnet:THRESHold`` command.
        - ``.type``: The ``BUS:B<x>:AUTOETHERnet:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._dataminusthreshold = BusBItemAutoethernetDataminusthreshold(
            device, f"{self._cmd_syntax}:DATAMINUSTHRESHOLD"
        )
        self._dataplusthreshold = BusBItemAutoethernetDataplusthreshold(
            device, f"{self._cmd_syntax}:DATAPLUSTHRESHold"
        )
        self._lowdataminus = BusBItemAutoethernetLowdataminus(
            device, f"{self._cmd_syntax}:LOWDATAMINus"
        )
        self._lowdataplus = BusBItemAutoethernetLowdataplus(
            device, f"{self._cmd_syntax}:LOWDATAPLUS"
        )
        self._lowthreshold = BusBItemAutoethernetLowthreshold(
            device, f"{self._cmd_syntax}:LOWTHRESHold"
        )
        self._signaltype = BusBItemAutoethernetSignaltype(device, f"{self._cmd_syntax}:SIGNALTYpe")
        self._source = BusBItemAutoethernetSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemAutoethernetThreshold(device, f"{self._cmd_syntax}:THRESHold")
        self._type = BusBItemAutoethernetType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def dataminusthreshold(self) -> BusBItemAutoethernetDataminusthreshold:
        """Return the ``BUS:B<x>:AUTOETHERnet:DATAMINUSTHRESHOLD`` command.

        Description:
            - This command sets or queries the AutoEthernet D- source threshold level for the
              specified bus. This threshold only applies when the AutoEthernet signal type is single
              ended.

        Usage:
            - Using the ``.query()`` method will send the
              ``BUS:B<x>:AUTOETHERnet:DATAMINUSTHRESHOLD?`` query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:AUTOETHERnet:DATAMINUSTHRESHOLD?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:AUTOETHERnet:DATAMINUSTHRESHOLD value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUTOETHERnet:DATAMINUSTHRESHOLD <NR3>
            - BUS:B<x>:AUTOETHERnet:DATAMINUSTHRESHOLD?
            ```

        Info:
            - ``B<x>`` is the Bus number.
            - ``NR3`` specifies the AutoEthernet D- source threshold level for the specified bus, in
              volts. This threshold only applies when the AutoEthernet signal type is single ended.
        """
        return self._dataminusthreshold

    @property
    def dataplusthreshold(self) -> BusBItemAutoethernetDataplusthreshold:
        """Return the ``BUS:B<x>:AUTOETHERnet:DATAPLUSTHRESHold`` command.

        Description:
            - This command sets or queries the AutoEthernet D+ source threshold level for the
              specified bus. This threshold only applies when the AutoEthernet signal type is single
              ended.

        Usage:
            - Using the ``.query()`` method will send the
              ``BUS:B<x>:AUTOETHERnet:DATAPLUSTHRESHold?`` query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:AUTOETHERnet:DATAPLUSTHRESHold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:AUTOETHERnet:DATAPLUSTHRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUTOETHERnet:DATAPLUSTHRESHold <NR3>
            - BUS:B<x>:AUTOETHERnet:DATAPLUSTHRESHold?
            ```

        Info:
            - ``B<x>`` is the Bus number.
            - ``NR3`` specifies the AutoEthernet D+ source threshold for the specified bus, in
              volts. This threshold only applies when the AutoEthernet signal type is single ended.
        """
        return self._dataplusthreshold

    @property
    def lowdataminus(self) -> BusBItemAutoethernetLowdataminus:
        """Return the ``BUS:B<x>:AUTOETHERnet:LOWDATAMINus`` command.

        Description:
            - This command sets or queries the AutoEthernet D- source low threshold level for the
              specified bus. This threshold only applies when the AutoEthernet signal type is single
              ended.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUTOETHERnet:LOWDATAMINus?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:AUTOETHERnet:LOWDATAMINus?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:AUTOETHERnet:LOWDATAMINus value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUTOETHERnet:LOWDATAMINus <NR3>
            - BUS:B<x>:AUTOETHERnet:LOWDATAMINus?
            ```

        Info:
            - ``B<x>`` is the Bus number.
            - ``NR3`` specifies the AutoEthernet D- source low threshold level for the specified
              bus, in volts. This threshold only applies when the AutoEthernet signal type is single
              ended.
        """
        return self._lowdataminus

    @property
    def lowdataplus(self) -> BusBItemAutoethernetLowdataplus:
        """Return the ``BUS:B<x>:AUTOETHERnet:LOWDATAPLUS`` command.

        Description:
            - This command sets or queries the AutoEthernet D+ source low threshold level for the
              specified bus. This threshold only applies when the AutoEthernet signal type is single
              ended.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUTOETHERnet:LOWDATAPLUS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:AUTOETHERnet:LOWDATAPLUS?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:AUTOETHERnet:LOWDATAPLUS value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUTOETHERnet:LOWDATAPLUS <NR3>
            - BUS:B<x>:AUTOETHERnet:LOWDATAPLUS?
            ```

        Info:
            - ``B<x>`` is the Bus number.
            - ``NR3`` specifies the AutoEthernet D+ source low threshold level for the specified
              bus, in volts. This threshold only applies when the AutoEthernet signal type is single
              ended.
        """
        return self._lowdataplus

    @property
    def lowthreshold(self) -> BusBItemAutoethernetLowthreshold:
        """Return the ``BUS:B<x>:AUTOETHERnet:LOWTHRESHold`` command.

        Description:
            - This command sets or queries the AutoEthernet Data source Low threshold level for the
              specified bus. This threshold only applies when the AutoEthernet signal type is
              differential.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUTOETHERnet:LOWTHRESHold?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:AUTOETHERnet:LOWTHRESHold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:AUTOETHERnet:LOWTHRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUTOETHERnet:LOWTHRESHold <NR3>
            - BUS:B<x>:AUTOETHERnet:LOWTHRESHold?
            ```

        Info:
            - ``B<x>`` is the Bus number.
            - ``NR3`` specifies the AutoEthernet DATA source Low threshold level for the specified
              bus, in volts. This threshold only applies when the AutoEthernet signal type is
              differential.
        """
        return self._lowthreshold

    @property
    def signaltype(self) -> BusBItemAutoethernetSignaltype:
        """Return the ``BUS:B<x>:AUTOETHERnet:SIGNALTYpe`` command.

        Description:
            - This command sets or queries the AutoEthernet signal type for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUTOETHERnet:SIGNALTYpe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:AUTOETHERnet:SIGNALTYpe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:AUTOETHERnet:SIGNALTYpe value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUTOETHERnet:SIGNALTYpe {SINGLE|DIFF}
            - BUS:B<x>:AUTOETHERnet:SIGNALTYpe?
            ```

        Info:
            - ``B<x>`` is the Bus number.
            - ``SINGLE`` specifies single-ended signals.
            - ``DIFF`` specifies differential signals.
        """
        return self._signaltype

    @property
    def source(self) -> BusBItemAutoethernetSource:
        """Return the ``BUS:B<x>:AUTOETHERnet:SOUrce`` command.

        Description:
            - This command sets or queries the AutoEthernet data (SDATA) source for the specified
              bus. This command controls the source channel when the signal type is differential.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUTOETHERnet:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUTOETHERnet:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:AUTOETHERnet:SOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUTOETHERnet:SOUrce {S<x>_Ch<x>|CH<x>|MATH<x>|REF<x<>}
            - BUS:B<x>:AUTOETHERnet:SOUrce?
            ```

        Info:
            - ``Bus<x>`` is the Bus number.
            - ``CH<x>`` specifies an analog channel as the AutoEthernet data source for differential
              input, where <x> is the channel number.
            - ``MATH<x>`` specifies a math channel as the AutoEthernet data source for differential
              input, where <x> is the math waveform number.
            - ``REF<x>`` specifies a reference waveform as the AutoEthernet data source for
              differential input, where <x> is the reference waveform number.
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel as the source.

        Sub-properties:
            - ``.dminus``: The ``BUS:B<x>:AUTOETHERnet:SOUrce:DMINus`` command.
            - ``.dplus``: The ``BUS:B<x>:AUTOETHERnet:SOUrce:DPLUs`` command.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemAutoethernetThreshold:
        """Return the ``BUS:B<x>:AUTOETHERnet:THRESHold`` command.

        Description:
            - This command sets or queries the AutoEthernet DATA source High threshold level for the
              specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUTOETHERnet:THRESHold?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUTOETHERnet:THRESHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:AUTOETHERnet:THRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUTOETHERnet:THRESHold <NR3>
            - BUS:B<x>:AUTOETHERnet:THRESHold?
            ```

        Info:
            - ``B<x>`` is the Bus number.
            - ``NR3`` specifies the AutoEthernet DATA source High threshold level for the specified
              bus, in volts.
        """
        return self._threshold

    @property
    def type(self) -> BusBItemAutoethernetType:
        """Return the ``BUS:B<x>:AUTOETHERnet:TYPe`` command.

        Description:
            - This command sets or queries the AutoEthernet standard speed.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUTOETHERnet:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUTOETHERnet:TYPe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUTOETHERnet:TYPe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUTOETHERnet:TYPe {HUNDREDBASET1}
            - BUS:B<x>:AUTOETHERnet:TYPe?
            ```

        Info:
            - ``B<x>`` is the Bus number.
            - ``HUNDREDBASET1`` specifies the AutoEthernet speed as 100Base-T1.
        """
        return self._type


class BusBItemAudioWordselThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUDio:WORDSel:THReshold`` command.

    Description:
        - This command sets or queries the audio word select source threshold for the specified bus.
          The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:WORDSel:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:WORDSel:THReshold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:AUDio:WORDSel:THReshold value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUDio:WORDSel:THReshold <NR3>
        - BUS:B<x>:AUDio:WORDSel:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the audio word select source threshold for the specified bus.
    """


class BusBItemAudioWordselSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUDio:WORDSel:SOUrce`` command.

    Description:
        - This command sets or queries the audio word select source waveform for the specified audio
          bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:WORDSel:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:WORDSel:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:WORDSel:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUDio:WORDSel:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:AUDio:WORDSel:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>_D<x>`` specifies is the remote scope number, the analog channel and the
          digital channel.
        - ``CH<x>`` specifies an analog channel as the word select source waveform.
        - ``CH<x>_D<x>`` specifies a digital channel as the word select source waveform.
        - ``MATH<x>`` specifies an math waveform as the word select source waveform.
        - ``REF<x>`` specifies an reference waveform as the word select source waveform.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the word select source waveform
          for the specified audio bus.
    """  # noqa: E501


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
        - ``.threshold``: The ``BUS:B<x>:AUDio:WORDSel:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemAudioWordselPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemAudioWordselSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemAudioWordselThreshold(device, f"{self._cmd_syntax}:THReshold")

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
            - This command sets or queries the audio word select source waveform for the specified
              audio bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:WORDSel:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:WORDSel:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:AUDio:WORDSel:SOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUDio:WORDSel:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:AUDio:WORDSel:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>_D<x>`` specifies is the remote scope number, the analog channel and the
              digital channel.
            - ``CH<x>`` specifies an analog channel as the word select source waveform.
            - ``CH<x>_D<x>`` specifies a digital channel as the word select source waveform.
            - ``MATH<x>`` specifies an math waveform as the word select source waveform.
            - ``REF<x>`` specifies an reference waveform as the word select source waveform.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the word select source
              waveform for the specified audio bus.
        """  # noqa: E501
        return self._source

    @property
    def threshold(self) -> BusBItemAudioWordselThreshold:
        """Return the ``BUS:B<x>:AUDio:WORDSel:THReshold`` command.

        Description:
            - This command sets or queries the audio word select source threshold for the specified
              bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:WORDSel:THReshold?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:AUDio:WORDSel:THReshold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:AUDio:WORDSel:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUDio:WORDSel:THReshold <NR3>
            - BUS:B<x>:AUDio:WORDSel:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the audio word select source threshold for the specified bus.
        """
        return self._threshold


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


class BusBItemAudioFrameClockbitsperchannel(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUDio:FRAME:CLOCKBITSPERCHANNEL`` command.

    Description:
        - This command sets or queries the audio bits of sync width for the specified bus. The bus
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:FRAME:CLOCKBITSPERCHANNEL?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``BUS:B<x>:AUDio:FRAME:CLOCKBITSPERCHANNEL?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:AUDio:FRAME:CLOCKBITSPERCHANNEL value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUDio:FRAME:CLOCKBITSPERCHANNEL <NR1>
        - BUS:B<x>:AUDio:FRAME:CLOCKBITSPERCHANNEL?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` is the audio bits of sync width for the specified bus.
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
        - ``.clockbitsperchannel``: The ``BUS:B<x>:AUDio:FRAME:CLOCKBITSPERCHANNEL`` command.
        - ``.size``: The ``BUS:B<x>:AUDio:FRAME:SIZe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._clockbitsperchannel = BusBItemAudioFrameClockbitsperchannel(
            device, f"{self._cmd_syntax}:CLOCKBITSPERCHANNEL"
        )
        self._size = BusBItemAudioFrameSize(device, f"{self._cmd_syntax}:SIZe")

    @property
    def clockbitsperchannel(self) -> BusBItemAudioFrameClockbitsperchannel:
        """Return the ``BUS:B<x>:AUDio:FRAME:CLOCKBITSPERCHANNEL`` command.

        Description:
            - This command sets or queries the audio bits of sync width for the specified bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``BUS:B<x>:AUDio:FRAME:CLOCKBITSPERCHANNEL?`` query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:AUDio:FRAME:CLOCKBITSPERCHANNEL?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:AUDio:FRAME:CLOCKBITSPERCHANNEL value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUDio:FRAME:CLOCKBITSPERCHANNEL <NR1>
            - BUS:B<x>:AUDio:FRAME:CLOCKBITSPERCHANNEL?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` is the audio bits of sync width for the specified bus.
        """
        return self._clockbitsperchannel

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


class BusBItemAudioDataWordsize(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUDio:DATa:WORDSize`` command.

    Description:
        - This command sets or queries the audio bits per word for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:DATa:WORDSize?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:DATa:WORDSize?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:DATa:WORDSize value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUDio:DATa:WORDSize <NR1>
        - BUS:B<x>:AUDio:DATa:WORDSize?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` is the audio bits per word for the specified bus.
    """


class BusBItemAudioDataThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUDio:DATa:THReshold`` command.

    Description:
        - This command sets or queries the audio data source threshold for the specified bus. The
          bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:DATa:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:DATa:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:DATa:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUDio:DATa:THReshold <NR3>
        - BUS:B<x>:AUDio:DATa:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the audio data source threshold for the specified bus.
    """


class BusBItemAudioDataSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUDio:DATa:SOUrce`` command.

    Description:
        - This command sets or queries the audio data source for the specified audio bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:DATa:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:DATa:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:DATa:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUDio:DATa:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:AUDio:DATa:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>_D<x>`` specifies is the remote scope number, the analog channel and the
          digital channel.
        - ``CH<x>`` specifies an analog channel as the data source waveform for the audio bus.
        - ``CH<x>_D<x>`` specifies a digital channel as the data source waveform for the audio bus.
        - ``MATH<x>`` specifies an math waveform as the data source waveform for the audio bus.
        - ``REF<x>`` specifies an reference waveform as the data source waveform for the audio bus.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the data source waveform for the
          specified audio bus.
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
        - This command sets or queries the audio data source polarity for the specified audio bus.
          The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:DATa:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:DATa:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:DATa:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUDio:DATa:POLarity {HIGH|LOW}
        - BUS:B<x>:AUDio:DATa:POLarity?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``HIGH`` specifies positive data polarity for the audio bus.
        - ``LOW`` specifies negative data polarity for the audio bus.
    """


class BusBItemAudioData(SCPICmdRead):
    """The ``BUS:B<x>:AUDio:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:DATa?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:AUDio:DATa:POLarity`` command.
        - ``.size``: The ``BUS:B<x>:AUDio:DATa:SIZe`` command.
        - ``.source``: The ``BUS:B<x>:AUDio:DATa:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:AUDio:DATa:THReshold`` command.
        - ``.wordsize``: The ``BUS:B<x>:AUDio:DATa:WORDSize`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemAudioDataPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._size = BusBItemAudioDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._source = BusBItemAudioDataSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemAudioDataThreshold(device, f"{self._cmd_syntax}:THReshold")
        self._wordsize = BusBItemAudioDataWordsize(device, f"{self._cmd_syntax}:WORDSize")

    @property
    def polarity(self) -> BusBItemAudioDataPolarity:
        """Return the ``BUS:B<x>:AUDio:DATa:POLarity`` command.

        Description:
            - This command sets or queries the audio data source polarity for the specified audio
              bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:DATa:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:DATa:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:AUDio:DATa:POLarity value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUDio:DATa:POLarity {HIGH|LOW}
            - BUS:B<x>:AUDio:DATa:POLarity?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``HIGH`` specifies positive data polarity for the audio bus.
            - ``LOW`` specifies negative data polarity for the audio bus.
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
            - This command sets or queries the audio data source for the specified audio bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:DATa:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:DATa:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:DATa:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUDio:DATa:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:AUDio:DATa:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>_D<x>`` specifies is the remote scope number, the analog channel and the
              digital channel.
            - ``CH<x>`` specifies an analog channel as the data source waveform for the audio bus.
            - ``CH<x>_D<x>`` specifies a digital channel as the data source waveform for the audio
              bus.
            - ``MATH<x>`` specifies an math waveform as the data source waveform for the audio bus.
            - ``REF<x>`` specifies an reference waveform as the data source waveform for the audio
              bus.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the data source waveform for
              the specified audio bus.
        """  # noqa: E501
        return self._source

    @property
    def threshold(self) -> BusBItemAudioDataThreshold:
        """Return the ``BUS:B<x>:AUDio:DATa:THReshold`` command.

        Description:
            - This command sets or queries the audio data source threshold for the specified bus.
              The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:DATa:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:DATa:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:AUDio:DATa:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUDio:DATa:THReshold <NR3>
            - BUS:B<x>:AUDio:DATa:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the audio data source threshold for the specified bus.
        """
        return self._threshold

    @property
    def wordsize(self) -> BusBItemAudioDataWordsize:
        """Return the ``BUS:B<x>:AUDio:DATa:WORDSize`` command.

        Description:
            - This command sets or queries the audio bits per word for the specified bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:DATa:WORDSize?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:DATa:WORDSize?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:AUDio:DATa:WORDSize value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUDio:DATa:WORDSize <NR1>
            - BUS:B<x>:AUDio:DATa:WORDSize?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` is the audio bits per word for the specified bus.
        """
        return self._wordsize


class BusBItemAudioClockThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUDio:CLOCk:THReshold`` command.

    Description:
        - This command sets or queries the audio clock source threshold for the specified bus. The
          bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:CLOCk:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:CLOCk:THReshold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:CLOCk:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUDio:CLOCk:THReshold <NR3>
        - BUS:B<x>:AUDio:CLOCk:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the audio clock source threshold for the specified bus.
    """


class BusBItemAudioClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUDio:CLOCk:SOUrce`` command.

    Description:
        - This command sets or queries the clock source waveform for the specified AUDIO bus. The
          bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:CLOCk:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:CLOCk:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUDio:CLOCk:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|Math<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:AUDio:CLOCk:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``S<x>_Ch<x>_D<x>`` specifies is the remote scope number, the analog channel and the
          digital channel.
        - ``CH<x>`` specifies an analog channel as the clock source waveform for the audio bus.
        - ``CH<x>_D<x>`` specifies a digital channel as the clock source waveform for the specified
          audio bus.
        - ``Math<x>`` specifies a math waveform as the clock source waveform for the audio bus.
        - ``REF<x>`` specifies a reference waveform as the clock source waveform for the audio bus.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the clock source waveform for
          the specified audio bus.
    """


class BusBItemAudioClockPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:AUDio:CLOCk:POLarity`` command.

    Description:
        - This command sets or queries the clock source polarity for the specified AUDIO bus. The
          bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:CLOCk:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:CLOCk:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:CLOCk:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:AUDio:CLOCk:POLarity {FALL|RISE}
        - BUS:B<x>:AUDio:CLOCk:POLarity?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``FALL`` sets falling edge as the clock polarity.
        - ``RISE`` sets rising edge as the clock polarity.
    """


class BusBItemAudioClock(SCPICmdRead):
    """The ``BUS:B<x>:AUDio:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:CLOCk?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:AUDio:CLOCk:POLarity`` command.
        - ``.source``: The ``BUS:B<x>:AUDio:CLOCk:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:AUDio:CLOCk:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemAudioClockPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemAudioClockSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemAudioClockThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def polarity(self) -> BusBItemAudioClockPolarity:
        """Return the ``BUS:B<x>:AUDio:CLOCk:POLarity`` command.

        Description:
            - This command sets or queries the clock source polarity for the specified AUDIO bus.
              The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:CLOCk:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:CLOCk:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:AUDio:CLOCk:POLarity value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUDio:CLOCk:POLarity {FALL|RISE}
            - BUS:B<x>:AUDio:CLOCk:POLarity?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``FALL`` sets falling edge as the clock polarity.
            - ``RISE`` sets rising edge as the clock polarity.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemAudioClockSource:
        """Return the ``BUS:B<x>:AUDio:CLOCk:SOUrce`` command.

        Description:
            - This command sets or queries the clock source waveform for the specified AUDIO bus.
              The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:CLOCk:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:CLOCk:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:AUDio:CLOCk:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUDio:CLOCk:SOUrce {S<x>_Ch<x>_D<x>|CH<x>|CH<x>_D<x>|Math<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:AUDio:CLOCk:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``S<x>_Ch<x>_D<x>`` specifies is the remote scope number, the analog channel and the
              digital channel.
            - ``CH<x>`` specifies an analog channel as the clock source waveform for the audio bus.
            - ``CH<x>_D<x>`` specifies a digital channel as the clock source waveform for the
              specified audio bus.
            - ``Math<x>`` specifies a math waveform as the clock source waveform for the audio bus.
            - ``REF<x>`` specifies a reference waveform as the clock source waveform for the audio
              bus.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the clock source waveform
              for the specified audio bus.
        """  # noqa: E501
        return self._source

    @property
    def threshold(self) -> BusBItemAudioClockThreshold:
        """Return the ``BUS:B<x>:AUDio:CLOCk:THReshold`` command.

        Description:
            - This command sets or queries the audio clock source threshold for the specified bus.
              The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:CLOCk:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:CLOCk:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:AUDio:CLOCk:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:AUDio:CLOCk:THReshold <NR3>
            - BUS:B<x>:AUDio:CLOCk:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the audio clock source threshold for the specified bus.
        """
        return self._threshold


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
        - ``.clock``: The ``BUS:B<x>:AUDio:CLOCk`` command tree.
        - ``.data``: The ``BUS:B<x>:AUDio:DATa`` command tree.
        - ``.frame``: The ``BUS:B<x>:AUDio:FRAME`` command tree.
        - ``.type``: The ``BUS:B<x>:AUDio:TYPe`` command.
        - ``.wordsel``: The ``BUS:B<x>:AUDio:WORDSel`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitdelay = BusBItemAudioBitdelay(device, f"{self._cmd_syntax}:BITDelay")
        self._bitorder = BusBItemAudioBitorder(device, f"{self._cmd_syntax}:BITOrder")
        self._clock = BusBItemAudioClock(device, f"{self._cmd_syntax}:CLOCk")
        self._data = BusBItemAudioData(device, f"{self._cmd_syntax}:DATa")
        self._frame = BusBItemAudioFrame(device, f"{self._cmd_syntax}:FRAME")
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
    def clock(self) -> BusBItemAudioClock:
        """Return the ``BUS:B<x>:AUDio:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:CLOCk?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:AUDio:CLOCk:POLarity`` command.
            - ``.source``: The ``BUS:B<x>:AUDio:CLOCk:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:AUDio:CLOCk:THReshold`` command.
        """
        return self._clock

    @property
    def data(self) -> BusBItemAudioData:
        """Return the ``BUS:B<x>:AUDio:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUDio:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUDio:DATa?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:AUDio:DATa:POLarity`` command.
            - ``.size``: The ``BUS:B<x>:AUDio:DATa:SIZe`` command.
            - ``.source``: The ``BUS:B<x>:AUDio:DATa:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:AUDio:DATa:THReshold`` command.
            - ``.wordsize``: The ``BUS:B<x>:AUDio:DATa:WORDSize`` command.
        """
        return self._data

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
            - ``.clockbitsperchannel``: The ``BUS:B<x>:AUDio:FRAME:CLOCKBITSPERCHANNEL`` command.
            - ``.size``: The ``BUS:B<x>:AUDio:FRAME:SIZe`` command.
        """
        return self._frame

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
            - ``.threshold``: The ``BUS:B<x>:AUDio:WORDSel:THReshold`` command.
        """
        return self._wordsel


class BusBItemArinc429aThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ARINC429A:THRESHold`` command.

    Description:
        - This command sets or queries the ARINC429 upper threshold for the specified bus. The bus
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ARINC429A:THRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ARINC429A:THRESHold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ARINC429A:THRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ARINC429A:THRESHold <NR3>
        - BUS:B<x>:ARINC429A:THRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the ARINC429 lower threshold for the specified bus.
    """


class BusBItemArinc429aSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ARINC429A:SOUrce`` command.

    Description:
        - This command sets or queries the source for the specified ARINC429 bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ARINC429A:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ARINC429A:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ARINC429A:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ARINC429A:SOUrce {S<x>_Ch<x>|CH<x>|Math<x>|REF<x>}
        - BUS:B<x>:ARINC429A:SOUrce?
        ```

    Info:
        - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
        - ``CH<x>`` specifies an analog channel as the source waveform for the ARINC429 bus.
        - ``Math<x>`` specifies a math waveform as the source waveform for the ARINC429 bus.
        - ``REF<x>`` specifies a reference waveform as the source waveform for the ARINC429 bus.
    """


class BusBItemArinc429aPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ARINC429A:POLARITY`` command.

    Description:
        - This command sets or queries the source polarity for the specified ARINC429 bus. The bus
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ARINC429A:POLARITY?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ARINC429A:POLARITY?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ARINC429A:POLARITY value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ARINC429A:POLARITY {NORMal|INVERTed}
        - BUS:B<x>:ARINC429A:POLARITY?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``NORMal`` specifies normal polarity.
        - ``INVERTed`` specifies inverted polarity.
    """


class BusBItemArinc429aDataformat(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ARINC429A:DATAFORmat`` command.

    Description:
        - This command sets or queries the format of the DATA field for the specified ARINC429 bus.
          The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ARINC429A:DATAFORmat?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ARINC429A:DATAFORmat?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ARINC429A:DATAFORmat value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ARINC429A:DATAFORmat {DATA|SDIDATA|SDIDATASSM}
        - BUS:B<x>:ARINC429A:DATAFORmat?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``DATA`` specifies a DATA field width of 19 bits (covering bits 11 through 29 of the 32
          bit packet).
        - ``SDIDATA`` specifies a DATA field width of 21 bits (covering bits 9 through 29 of the 32
          bit packet).
        - ``SDIDATASSM`` specifies a DATA field width of 23 bits (covering bits 9 through 31 of the
          32 bit packet).
    """


class BusBItemArinc429aBitrateCustom(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ARINC429A:BITRate:CUSTom`` command.

    Description:
        - This command sets or queries the ARINC429 custom bit rate for the specified bus. The bus
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ARINC429A:BITRate:CUSTom?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ARINC429A:BITRate:CUSTom?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:ARINC429A:BITRate:CUSTom value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ARINC429A:BITRate:CUSTom <NR1>
        - BUS:B<x>:ARINC429A:BITRate:CUSTom?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` is the ARINC429 custom bit rate for the specified bus.
    """


class BusBItemArinc429aBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:ARINC429A:BITRate`` command.

    Description:
        - This command sets or queries the ARINC429 bit rate for the specified bus. The bus number
          is specified by x. If you select Custom, use ``BUS:B<x>:ARINC429A:BITRate:CUSTom`` to set
          the bit rate.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ARINC429A:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ARINC429A:BITRate?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:ARINC429A:BITRate value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:ARINC429A:BITRate {LOW|HI|CUSTom}
        - BUS:B<x>:ARINC429A:BITRate?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``LOW`` sets the bit rate to handle low speed signals.
        - ``HI`` sets the bit rate to handle high speed signals.
        - ``CUSTom`` uses the custom bit rate set by ``BUS:B<x>:ARINC429A:BITRate:CUSTom``.

    Properties:
        - ``.custom``: The ``BUS:B<x>:ARINC429A:BITRate:CUSTom`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._custom = BusBItemArinc429aBitrateCustom(device, f"{self._cmd_syntax}:CUSTom")

    @property
    def custom(self) -> BusBItemArinc429aBitrateCustom:
        """Return the ``BUS:B<x>:ARINC429A:BITRate:CUSTom`` command.

        Description:
            - This command sets or queries the ARINC429 custom bit rate for the specified bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ARINC429A:BITRate:CUSTom?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:ARINC429A:BITRate:CUSTom?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ARINC429A:BITRate:CUSTom value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ARINC429A:BITRate:CUSTom <NR1>
            - BUS:B<x>:ARINC429A:BITRate:CUSTom?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` is the ARINC429 custom bit rate for the specified bus.
        """
        return self._custom


class BusBItemArinc429a(SCPICmdRead):
    """The ``BUS:B<x>:ARINC429A`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:ARINC429A?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ARINC429A?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:ARINC429A:BITRate`` command.
        - ``.dataformat``: The ``BUS:B<x>:ARINC429A:DATAFORmat`` command.
        - ``.polarity``: The ``BUS:B<x>:ARINC429A:POLARITY`` command.
        - ``.source``: The ``BUS:B<x>:ARINC429A:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:ARINC429A:THRESHold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemArinc429aBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._dataformat = BusBItemArinc429aDataformat(device, f"{self._cmd_syntax}:DATAFORmat")
        self._polarity = BusBItemArinc429aPolarity(device, f"{self._cmd_syntax}:POLARITY")
        self._source = BusBItemArinc429aSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemArinc429aThreshold(device, f"{self._cmd_syntax}:THRESHold")

    @property
    def bitrate(self) -> BusBItemArinc429aBitrate:
        """Return the ``BUS:B<x>:ARINC429A:BITRate`` command.

        Description:
            - This command sets or queries the ARINC429 bit rate for the specified bus. The bus
              number is specified by x. If you select Custom, use
              ``BUS:B<x>:ARINC429A:BITRate:CUSTom`` to set the bit rate.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ARINC429A:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ARINC429A:BITRate?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:ARINC429A:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ARINC429A:BITRate {LOW|HI|CUSTom}
            - BUS:B<x>:ARINC429A:BITRate?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``LOW`` sets the bit rate to handle low speed signals.
            - ``HI`` sets the bit rate to handle high speed signals.
            - ``CUSTom`` uses the custom bit rate set by ``BUS:B<x>:ARINC429A:BITRate:CUSTom``.

        Sub-properties:
            - ``.custom``: The ``BUS:B<x>:ARINC429A:BITRate:CUSTom`` command.
        """
        return self._bitrate

    @property
    def dataformat(self) -> BusBItemArinc429aDataformat:
        """Return the ``BUS:B<x>:ARINC429A:DATAFORmat`` command.

        Description:
            - This command sets or queries the format of the DATA field for the specified ARINC429
              bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ARINC429A:DATAFORmat?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ARINC429A:DATAFORmat?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ARINC429A:DATAFORmat value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ARINC429A:DATAFORmat {DATA|SDIDATA|SDIDATASSM}
            - BUS:B<x>:ARINC429A:DATAFORmat?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``DATA`` specifies a DATA field width of 19 bits (covering bits 11 through 29 of the
              32 bit packet).
            - ``SDIDATA`` specifies a DATA field width of 21 bits (covering bits 9 through 29 of the
              32 bit packet).
            - ``SDIDATASSM`` specifies a DATA field width of 23 bits (covering bits 9 through 31 of
              the 32 bit packet).
        """
        return self._dataformat

    @property
    def polarity(self) -> BusBItemArinc429aPolarity:
        """Return the ``BUS:B<x>:ARINC429A:POLARITY`` command.

        Description:
            - This command sets or queries the source polarity for the specified ARINC429 bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ARINC429A:POLARITY?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ARINC429A:POLARITY?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:ARINC429A:POLARITY value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ARINC429A:POLARITY {NORMal|INVERTed}
            - BUS:B<x>:ARINC429A:POLARITY?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``NORMal`` specifies normal polarity.
            - ``INVERTed`` specifies inverted polarity.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemArinc429aSource:
        """Return the ``BUS:B<x>:ARINC429A:SOUrce`` command.

        Description:
            - This command sets or queries the source for the specified ARINC429 bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ARINC429A:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ARINC429A:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:ARINC429A:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ARINC429A:SOUrce {S<x>_Ch<x>|CH<x>|Math<x>|REF<x>}
            - BUS:B<x>:ARINC429A:SOUrce?
            ```

        Info:
            - ``S<x>_Ch<x>`` specifies the remote scope number and the analog channel.
            - ``CH<x>`` specifies an analog channel as the source waveform for the ARINC429 bus.
            - ``Math<x>`` specifies a math waveform as the source waveform for the ARINC429 bus.
            - ``REF<x>`` specifies a reference waveform as the source waveform for the ARINC429 bus.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemArinc429aThreshold:
        """Return the ``BUS:B<x>:ARINC429A:THRESHold`` command.

        Description:
            - This command sets or queries the ARINC429 upper threshold for the specified bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ARINC429A:THRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ARINC429A:THRESHold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:ARINC429A:THRESHold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:ARINC429A:THRESHold <NR3>
            - BUS:B<x>:ARINC429A:THRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the ARINC429 lower threshold for the specified bus.
        """
        return self._threshold


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class BusBItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``BUS:B<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.arinc429a``: The ``BUS:B<x>:ARINC429A`` command tree.
        - ``.audio``: The ``BUS:B<x>:AUDio`` command tree.
        - ``.autoethernet``: The ``BUS:B<x>:AUTOETHERnet`` command tree.
        - ``.can``: The ``BUS:B<x>:CAN`` command tree.
        - ``.cphy``: The ``BUS:B<x>:CPHY`` command tree.
        - ``.cxpi``: The ``BUS:B<x>:CXPI`` command tree.
        - ``.display``: The ``BUS:B<x>:DISplay`` command tree.
        - ``.dphy``: The ``BUS:B<x>:DPHY`` command tree.
        - ``.espi``: The ``BUS:B<x>:ESPI`` command tree.
        - ``.ethercat``: The ``BUS:B<x>:ETHERCAT`` command tree.
        - ``.ethernet``: The ``BUS:B<x>:ETHERnet`` command tree.
        - ``.eusb``: The ``BUS:B<x>:EUSB`` command tree.
        - ``.flexray``: The ``BUS:B<x>:FLEXray`` command tree.
        - ``.i2c``: The ``BUS:B<x>:I2C`` command tree.
        - ``.i3c``: The ``BUS:B<x>:I3C`` command tree.
        - ``.label``: The ``BUS:B<x>:LABel`` command tree.
        - ``.lin``: The ``BUS:B<x>:LIN`` command tree.
        - ``.manchester``: The ``BUS:B<x>:MANChester`` command tree.
        - ``.mdio``: The ``BUS:B<x>:MDIO`` command tree.
        - ``.mil1553b``: The ``BUS:B<x>:MIL1553B`` command tree.
        - ``.nrz``: The ``BUS:B<x>:NRZ`` command tree.
        - ``.onewire``: The ``BUS:B<x>:ONEWIRe`` command tree.
        - ``.parallel``: The ``BUS:B<x>:PARallel`` command tree.
        - ``.psifive``: The ``BUS:B<x>:PSIFIVe`` command tree.
        - ``.rs232c``: The ``BUS:B<x>:RS232C`` command tree.
        - ``.s8b10b``: The ``BUS:B<x>:S8B10B`` command tree.
        - ``.sdlc``: The ``BUS:B<x>:SDLC`` command tree.
        - ``.sent``: The ``BUS:B<x>:SENT`` command tree.
        - ``.smbus``: The ``BUS:B<x>:SMBUS`` command tree.
        - ``.spacewire``: The ``BUS:B<x>:SPACEWIRe`` command tree.
        - ``.spi``: The ``BUS:B<x>:SPI`` command tree.
        - ``.spmi``: The ``BUS:B<x>:SPMI`` command tree.
        - ``.svid``: The ``BUS:B<x>:SVID`` command tree.
        - ``.type``: The ``BUS:B<x>:TYPe`` command.
        - ``.usb``: The ``BUS:B<x>:USB`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._arinc429a = BusBItemArinc429a(device, f"{self._cmd_syntax}:ARINC429A")
        self._audio = BusBItemAudio(device, f"{self._cmd_syntax}:AUDio")
        self._autoethernet = BusBItemAutoethernet(device, f"{self._cmd_syntax}:AUTOETHERnet")
        self._can = BusBItemCan(device, f"{self._cmd_syntax}:CAN")
        self._cphy = BusBItemCphy(device, f"{self._cmd_syntax}:CPHY")
        self._cxpi = BusBItemCxpi(device, f"{self._cmd_syntax}:CXPI")
        self._display = BusBItemDisplay(device, f"{self._cmd_syntax}:DISplay")
        self._dphy = BusBItemDphy(device, f"{self._cmd_syntax}:DPHY")
        self._espi = BusBItemEspi(device, f"{self._cmd_syntax}:ESPI")
        self._ethercat = BusBItemEthercat(device, f"{self._cmd_syntax}:ETHERCAT")
        self._ethernet = BusBItemEthernet(device, f"{self._cmd_syntax}:ETHERnet")
        self._eusb = BusBItemEusb(device, f"{self._cmd_syntax}:EUSB")
        self._flexray = BusBItemFlexray(device, f"{self._cmd_syntax}:FLEXray")
        self._i2c = BusBItemI2c(device, f"{self._cmd_syntax}:I2C")
        self._i3c = BusBItemI3c(device, f"{self._cmd_syntax}:I3C")
        self._label = BusBItemLabel(device, f"{self._cmd_syntax}:LABel")
        self._lin = BusBItemLin(device, f"{self._cmd_syntax}:LIN")
        self._manchester = BusBItemManchester(device, f"{self._cmd_syntax}:MANChester")
        self._mdio = BusBItemMdio(device, f"{self._cmd_syntax}:MDIO")
        self._mil1553b = BusBItemMil1553b(device, f"{self._cmd_syntax}:MIL1553B")
        self._nrz = BusBItemNrz(device, f"{self._cmd_syntax}:NRZ")
        self._onewire = BusBItemOnewire(device, f"{self._cmd_syntax}:ONEWIRe")
        self._parallel = BusBItemParallel(device, f"{self._cmd_syntax}:PARallel")
        self._psifive = BusBItemPsifive(device, f"{self._cmd_syntax}:PSIFIVe")
        self._rs232c = BusBItemRs232c(device, f"{self._cmd_syntax}:RS232C")
        self._s8b10b = BusBItemS8b10b(device, f"{self._cmd_syntax}:S8B10B")
        self._sdlc = BusBItemSdlc(device, f"{self._cmd_syntax}:SDLC")
        self._sent = BusBItemSent(device, f"{self._cmd_syntax}:SENT")
        self._smbus = BusBItemSmbus(device, f"{self._cmd_syntax}:SMBUS")
        self._spacewire = BusBItemSpacewire(device, f"{self._cmd_syntax}:SPACEWIRe")
        self._spi = BusBItemSpi(device, f"{self._cmd_syntax}:SPI")
        self._spmi = BusBItemSpmi(device, f"{self._cmd_syntax}:SPMI")
        self._svid = BusBItemSvid(device, f"{self._cmd_syntax}:SVID")
        self._type = BusBItemType(device, f"{self._cmd_syntax}:TYPe")
        self._usb = BusBItemUsb(device, f"{self._cmd_syntax}:USB")

    @property
    def arinc429a(self) -> BusBItemArinc429a:
        """Return the ``BUS:B<x>:ARINC429A`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ARINC429A?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ARINC429A?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:ARINC429A:BITRate`` command.
            - ``.dataformat``: The ``BUS:B<x>:ARINC429A:DATAFORmat`` command.
            - ``.polarity``: The ``BUS:B<x>:ARINC429A:POLARITY`` command.
            - ``.source``: The ``BUS:B<x>:ARINC429A:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:ARINC429A:THRESHold`` command.
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
            - ``.clock``: The ``BUS:B<x>:AUDio:CLOCk`` command tree.
            - ``.data``: The ``BUS:B<x>:AUDio:DATa`` command tree.
            - ``.frame``: The ``BUS:B<x>:AUDio:FRAME`` command tree.
            - ``.type``: The ``BUS:B<x>:AUDio:TYPe`` command.
            - ``.wordsel``: The ``BUS:B<x>:AUDio:WORDSel`` command tree.
        """
        return self._audio

    @property
    def autoethernet(self) -> BusBItemAutoethernet:
        """Return the ``BUS:B<x>:AUTOETHERnet`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:AUTOETHERnet?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:AUTOETHERnet?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the Bus number.

        Sub-properties:
            - ``.dataminusthreshold``: The ``BUS:B<x>:AUTOETHERnet:DATAMINUSTHRESHOLD`` command.
            - ``.dataplusthreshold``: The ``BUS:B<x>:AUTOETHERnet:DATAPLUSTHRESHold`` command.
            - ``.lowdataminus``: The ``BUS:B<x>:AUTOETHERnet:LOWDATAMINus`` command.
            - ``.lowdataplus``: The ``BUS:B<x>:AUTOETHERnet:LOWDATAPLUS`` command.
            - ``.lowthreshold``: The ``BUS:B<x>:AUTOETHERnet:LOWTHRESHold`` command.
            - ``.signaltype``: The ``BUS:B<x>:AUTOETHERnet:SIGNALTYpe`` command.
            - ``.source``: The ``BUS:B<x>:AUTOETHERnet:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:AUTOETHERnet:THRESHold`` command.
            - ``.type``: The ``BUS:B<x>:AUTOETHERnet:TYPe`` command.
        """
        return self._autoethernet

    @property
    def can(self) -> BusBItemCan:
        """Return the ``BUS:B<x>:CAN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:CAN:BITRate`` command.
            - ``.fd``: The ``BUS:B<x>:CAN:FD`` command tree.
            - ``.samplepoint``: The ``BUS:B<x>:CAN:SAMPLEpoint`` command.
            - ``.signal``: The ``BUS:B<x>:CAN:SIGNal`` command.
            - ``.source``: The ``BUS:B<x>:CAN:SOUrce`` command.
            - ``.standard``: The ``BUS:B<x>:CAN:STANDard`` command.
            - ``.threshold``: The ``BUS:B<x>:CAN:THReshold`` command.
        """
        return self._can

    @property
    def cphy(self) -> BusBItemCphy:
        """Return the ``BUS:B<x>:CPHY`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CPHY?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CPHY?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.a``: The ``BUS:B<x>:CPHY:A`` command tree.
            - ``.ab``: The ``BUS:B<x>:CPHY:AB`` command tree.
            - ``.agnd``: The ``BUS:B<x>:CPHY:AGND`` command tree.
            - ``.b``: The ``BUS:B<x>:CPHY:B`` command tree.
            - ``.bc``: The ``BUS:B<x>:CPHY:BC`` command tree.
            - ``.bitrate``: The ``BUS:B<x>:CPHY:BITRate`` command.
            - ``.c``: The ``BUS:B<x>:CPHY:C`` command tree.
            - ``.ca``: The ``BUS:B<x>:CPHY:CA`` command tree.
            - ``.cgnd``: The ``BUS:B<x>:CPHY:CGND`` command tree.
            - ``.lp``: The ``BUS:B<x>:CPHY:LP`` command tree.
            - ``.signaltype``: The ``BUS:B<x>:CPHY:SIGNALTYpe`` command.
            - ``.subtype``: The ``BUS:B<x>:CPHY:SUBTYPe`` command.
        """
        return self._cphy

    @property
    def cxpi(self) -> BusBItemCxpi:
        """Return the ``BUS:B<x>:CXPI`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CXPI?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CXPI?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:CXPI:BITRate`` command.
            - ``.rec``: The ``BUS:B<x>:CXPI:REC`` command tree.
            - ``.source``: The ``BUS:B<x>:CXPI:SOUrce`` command.
        """
        return self._cxpi

    @property
    def display(self) -> BusBItemDisplay:
        """Return the ``BUS:B<x>:DISplay`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.format``: The ``BUS:B<x>:DISplay:FORMat`` command.
            - ``.layout``: The ``BUS:B<x>:DISplay:LAYout`` command.
        """
        return self._display

    @property
    def dphy(self) -> BusBItemDphy:
        """Return the ``BUS:B<x>:DPHY`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DPHY?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DPHY?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.clock``: The ``BUS:B<x>:DPHY:CLOCk`` command tree.
            - ``.dminus``: The ``BUS:B<x>:DPHY:DMINus`` command tree.
            - ``.dplus``: The ``BUS:B<x>:DPHY:DPlus`` command tree.
            - ``.lp``: The ``BUS:B<x>:DPHY:LP`` command tree.
            - ``.protocol``: The ``BUS:B<x>:DPHY:PROTocol`` command tree.
            - ``.signal``: The ``BUS:B<x>:DPHY:SIGNal`` command tree.
        """
        return self._dphy

    @property
    def espi(self) -> BusBItemEspi:
        """Return the ``BUS:B<x>:ESPI`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ESPI?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ESPI?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the Bus number.

        Sub-properties:
            - ``.alertview``: The ``BUS:B<x>:ESPI:ALERTVIEW`` command.
            - ``.alert``: The ``BUS:B<x>:ESPI:ALERt`` command tree.
            - ``.chipselect``: The ``BUS:B<x>:ESPI:CHIPSELect`` command tree.
            - ``.clock``: The ``BUS:B<x>:ESPI:CLOCk`` command tree.
            - ``.dataone``: The ``BUS:B<x>:ESPI:DATAONE`` command tree.
            - ``.datatwo``: The ``BUS:B<x>:ESPI:DATATWO`` command tree.
            - ``.iomode``: The ``BUS:B<x>:ESPI:IOMODe`` command.
        """
        return self._espi

    @property
    def ethercat(self) -> BusBItemEthercat:
        """Return the ``BUS:B<x>:ETHERCAT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERCAT?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERCAT?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.dataminusthreshold``: The ``BUS:B<x>:ETHERCAT:DATAMINUSTHRESHold`` command.
            - ``.dataplusthreshold``: The ``BUS:B<x>:ETHERCAT:DATAPLUSTHRESHold`` command.
            - ``.signaltype``: The ``BUS:B<x>:ETHERCAT:SIGNALTYpe`` command.
            - ``.source``: The ``BUS:B<x>:ETHERCAT:SOUrce`` command tree.
            - ``.threshold``: The ``BUS:B<x>:ETHERCAT:THRESHold`` command.
        """
        return self._ethercat

    @property
    def ethernet(self) -> BusBItemEthernet:
        """Return the ``BUS:B<x>:ETHERnet`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ETHERnet?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ETHERnet?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.dataminusthreshold``: The ``BUS:B<x>:ETHERnet:DATAMINUSTHRESHold`` command.
            - ``.dataplusthreshold``: The ``BUS:B<x>:ETHERnet:DATAPLUSTHRESHold`` command.
            - ``.ipvfour``: The ``BUS:B<x>:ETHERnet:IPVFOUR`` command.
            - ``.lowthreshold``: The ``BUS:B<x>:ETHERnet:LOWTHRESHold`` command.
            - ``.qtagging``: The ``BUS:B<x>:ETHERnet:QTAGGING`` command.
            - ``.signaltype``: The ``BUS:B<x>:ETHERnet:SIGNALTYpe`` command.
            - ``.source``: The ``BUS:B<x>:ETHERnet:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:ETHERnet:THRESHold`` command.
            - ``.type``: The ``BUS:B<x>:ETHERnet:TYPe`` command.
        """
        return self._ethernet

    @property
    def eusb(self) -> BusBItemEusb:
        """Return the ``BUS:B<x>:EUSB`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:EUSB?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:EUSB?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:EUSB:BITRate`` command.
            - ``.dataminus``: The ``BUS:B<x>:EUSB:DATAMINUS`` command tree.
            - ``.dataminusthreshold``: The ``BUS:B<x>:EUSB:DATAMINUSTHRESHold`` command.
            - ``.dataplus``: The ``BUS:B<x>:EUSB:DATAPLUS`` command tree.
            - ``.dataplusthreshold``: The ``BUS:B<x>:EUSB:DATAPLUSTHRESHold`` command.
            - ``.lowthreshold``: The ``BUS:B<x>:EUSB:LOWTHRESHold`` command.
            - ``.operating``: The ``BUS:B<x>:EUSB:OPERating`` command tree.
            - ``.signaltype``: The ``BUS:B<x>:EUSB:SIGNALTYpe`` command.
            - ``.source``: The ``BUS:B<x>:EUSB:SOUrce`` command tree.
            - ``.threshold``: The ``BUS:B<x>:EUSB:THRESHold`` command.
        """
        return self._eusb

    @property
    def flexray(self) -> BusBItemFlexray:
        """Return the ``BUS:B<x>:FLEXray`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:FLEXray:BITRate`` command.
            - ``.channel``: The ``BUS:B<x>:FLEXray:CHannel`` command.
            - ``.lowthreshold``: The ``BUS:B<x>:FLEXray:LOWTHRESHold`` command.
            - ``.signal``: The ``BUS:B<x>:FLEXray:SIGnal`` command.
            - ``.source``: The ``BUS:B<x>:FLEXray:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:FLEXray:THRESHold`` command.
            - ``.txrxthreshold``: The ``BUS:B<x>:FLEXray:TXRXTHRESHold`` command.
        """
        return self._flexray

    @property
    def i2c(self) -> BusBItemI2c:
        """Return the ``BUS:B<x>:I2C`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.clock``: The ``BUS:B<x>:I2C:CLOCk`` command tree.
            - ``.data``: The ``BUS:B<x>:I2C:DATa`` command tree.
            - ``.rwinaddr``: The ``BUS:B<x>:I2C:RWINADDR`` command.
        """
        return self._i2c

    @property
    def i3c(self) -> BusBItemI3c:
        """Return the ``BUS:B<x>:I3C`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I3C?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I3C?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` specifies the bus number.

        Sub-properties:
            - ``.clock``: The ``BUS:B<x>:I3C:CLOCk`` command tree.
            - ``.data``: The ``BUS:B<x>:I3C:DATa`` command tree.
        """
        return self._i3c

    @property
    def label(self) -> BusBItemLabel:
        """Return the ``BUS:B<x>:LABel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.color``: The ``BUS:B<x>:LABel:COLor`` command.
            - ``.font``: The ``BUS:B<x>:LABel:FONT`` command tree.
            - ``.xpos``: The ``BUS:B<x>:LABel:XPOS`` command.
            - ``.ypos``: The ``BUS:B<x>:LABel:YPOS`` command.
            - ``.name``: The ``BUS:B<x>:LABel:name`` command.
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
            - ``.samplepoint``: The ``BUS:B<x>:LIN:SAMPLEpoint`` command.
            - ``.source``: The ``BUS:B<x>:LIN:SOUrce`` command.
            - ``.standard``: The ``BUS:B<x>:LIN:STANDard`` command.
        """
        return self._lin

    @property
    def manchester(self) -> BusBItemManchester:
        """Return the ``BUS:B<x>:MANChester`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MANChester?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MANChester?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.bitorder``: The ``BUS:B<x>:MANChester:BITORDer`` command.
            - ``.bitrate``: The ``BUS:B<x>:MANChester:BITRate`` command.
            - ``.displaymode``: The ``BUS:B<x>:MANChester:DISplaymode`` command.
            - ``.header``: The ``BUS:B<x>:MANChester:HEADer`` command tree.
            - ``.idle``: The ``BUS:B<x>:MANChester:IDLE`` command tree.
            - ``.source``: The ``BUS:B<x>:MANChester:SOUrce`` command.
            - ``.start``: The ``BUS:B<x>:MANChester:START`` command tree.
            - ``.sync``: The ``BUS:B<x>:MANChester:SYNC`` command tree.
            - ``.threshold``: The ``BUS:B<x>:MANChester:THReshold`` command.
            - ``.tolerance``: The ``BUS:B<x>:MANChester:TOLerance`` command.
            - ``.transtion``: The ``BUS:B<x>:MANChester:TRANstion`` command tree.
            - ``.trailer``: The ``BUS:B<x>:MANChester:TRAiler`` command tree.
            - ``.word``: The ``BUS:B<x>:MANChester:WORD`` command tree.
            - ``.wordsize``: The ``BUS:B<x>:MANChester:WORDSIZe`` command.
            - ``.parity``: The ``BUS:B<x>:MANChester:parity`` command.
        """
        return self._manchester

    @property
    def mdio(self) -> BusBItemMdio:
        """Return the ``BUS:B<x>:MDIO`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:MDIO?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:MDIO?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.clock``: The ``BUS:B<x>:MDIO:CLOCk`` command tree.
            - ``.data``: The ``BUS:B<x>:MDIO:DATA`` command tree.
        """
        return self._mdio

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
            - ``.lowthreshold``: The ``BUS:B<x>:MIL1553B:LOWTHRESHold`` command.
            - ``.polarity``: The ``BUS:B<x>:MIL1553B:POLarity`` command.
            - ``.responsetime``: The ``BUS:B<x>:MIL1553B:RESPonsetime`` command tree.
            - ``.source``: The ``BUS:B<x>:MIL1553B:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:MIL1553B:THRESHold`` command.
        """
        return self._mil1553b

    @property
    def nrz(self) -> BusBItemNrz:
        """Return the ``BUS:B<x>:NRZ`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:NRZ?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:NRZ?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.bitorder``: The ``BUS:B<x>:NRZ:BITOrder`` command.
            - ``.bitrate``: The ``BUS:B<x>:NRZ:BITRate`` command.
            - ``.polarity``: The ``BUS:B<x>:NRZ:POLarity`` command.
            - ``.source``: The ``BUS:B<x>:NRZ:SOUrce`` command.
            - ``.spmi``: The ``BUS:B<x>:NRZ:SPMI`` command tree.
            - ``.threshold``: The ``BUS:B<x>:NRZ:THReshold`` command.
        """
        return self._nrz

    @property
    def onewire(self) -> BusBItemOnewire:
        """Return the ``BUS:B<x>:ONEWIRe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:ONEWIRe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:ONEWIRe?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.data``: The ``BUS:B<x>:ONEWIRe:DATA`` command tree.
            - ``.mode``: The ``BUS:B<x>:ONEWIRe:MODe`` command.
        """
        return self._onewire

    @property
    def parallel(self) -> BusBItemParallel:
        """Return the ``BUS:B<x>:PARallel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.allthresholds``: The ``BUS:B<x>:PARallel:ALLTHResholds`` command.
            - ``.bitsource``: The ``BUS:B<x>:PARallel:BIT<n>SOUrce`` command.
            - ``.clock``: The ``BUS:B<x>:PARallel:CLOCk`` command tree.
            - ``.clocksource``: The ``BUS:B<x>:PARallel:CLOCkSOUrce`` command.
        """
        return self._parallel

    @property
    def psifive(self) -> BusBItemPsifive:
        """Return the ``BUS:B<x>:PSIFIVe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PSIFIVe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PSIFIVe?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.bitperiod``: The ``BUS:B<x>:PSIFIVe:BITPERiod`` command.
            - ``.bitrate``: The ``BUS:B<x>:PSIFIVe:BITRate`` command.
            - ``.comm``: The ``BUS:B<x>:PSIFIVe:COMM`` command tree.
            - ``.dataa``: The ``BUS:B<x>:PSIFIVe:DATAA`` command.
            - ``.datab``: The ``BUS:B<x>:PSIFIVe:DATAB`` command.
            - ``.dataformat``: The ``BUS:B<x>:PSIFIVe:DATAFORMat`` command.
            - ``.ecusource``: The ``BUS:B<x>:PSIFIVe:ECUSOURce`` command.
            - ``.framecontrol``: The ``BUS:B<x>:PSIFIVe:FRAMECONTrol`` command.
            - ``.messaging``: The ``BUS:B<x>:PSIFIVe:MESSaging`` command.
            - ``.source``: The ``BUS:B<x>:PSIFIVe:SOUrce`` command.
            - ``.status``: The ``BUS:B<x>:PSIFIVe:STATus`` command.
            - ``.syncmode``: The ``BUS:B<x>:PSIFIVe:SYNCMODe`` command.
            - ``.syncthreshold``: The ``BUS:B<x>:PSIFIVe:SYNCTHRESHold`` command.
            - ``.threshold``: The ``BUS:B<x>:PSIFIVe:THRESHold`` command.
        """
        return self._psifive

    @property
    def rs232c(self) -> BusBItemRs232c:
        """Return the ``BUS:B<x>:RS232C`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

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
    def s8b10b(self) -> BusBItemS8b10b:
        """Return the ``BUS:B<x>:S8B10B`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:S8B10B?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:S8B10B?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:S8B10B:BITRate`` command.
            - ``.source``: The ``BUS:B<x>:S8B10B:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:S8B10B:THReshold`` command.
        """
        return self._s8b10b

    @property
    def sdlc(self) -> BusBItemSdlc:
        """Return the ``BUS:B<x>:SDLC`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SDLC?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SDLC?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:SDLC:BITRate`` command.
            - ``.data``: The ``BUS:B<x>:SDLC:DATA`` command tree.
            - ``.encoding``: The ``BUS:B<x>:SDLC:ENCoding`` command.
            - ``.modulo``: The ``BUS:B<x>:SDLC:MODulo`` command.
        """
        return self._sdlc

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
            - ``.threshold``: The ``BUS:B<x>:SENT:THRESHold`` command.
            - ``.ticktime``: The ``BUS:B<x>:SENT:TICKTIME`` command.
            - ``.ticktolerance``: The ``BUS:B<x>:SENT:TICKTOLerance`` command.
        """
        return self._sent

    @property
    def smbus(self) -> BusBItemSmbus:
        """Return the ``BUS:B<x>:SMBUS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SMBUS?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SMBUS?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the bus number.

        Sub-properties:
            - ``.clock``: The ``BUS:B<x>:SMBUS:CLOCk`` command tree.
            - ``.data``: The ``BUS:B<x>:SMBUS:DATA`` command tree.
            - ``.pec``: The ``BUS:B<x>:SMBUS:PEC`` command tree.
        """
        return self._smbus

    @property
    def spacewire(self) -> BusBItemSpacewire:
        """Return the ``BUS:B<x>:SPACEWIRe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPACEWIRe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPACEWIRe?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the bus number.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:SPACEWIRe:BITRate`` command.
            - ``.data``: The ``BUS:B<x>:SPACEWIRe:DATa`` command tree.
            - ``.decode``: The ``BUS:B<x>:SPACEWIRe:DECode`` command tree.
            - ``.strobe``: The ``BUS:B<x>:SPACEWIRe:STRobe`` command tree.
            - ``.sync``: The ``BUS:B<x>:SPACEWIRe:SYNC`` command.
        """
        return self._spacewire

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
            - ``.miso``: The ``BUS:B<x>:SPI:MISo`` command tree.
            - ``.mosi``: The ``BUS:B<x>:SPI:MOSi`` command tree.
            - ``.number``: The ``BUS:B<x>:SPI:NUMBer`` command tree.
            - ``.select``: The ``BUS:B<x>:SPI:SELect`` command tree.
        """
        return self._spi

    @property
    def spmi(self) -> BusBItemSpmi:
        """Return the ``BUS:B<x>:SPMI`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPMI?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPMI?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.sclk``: The ``BUS:B<x>:SPMI:SCLk`` command tree.
            - ``.sdata``: The ``BUS:B<x>:SPMI:SDATa`` command tree.
        """
        return self._spmi

    @property
    def svid(self) -> BusBItemSvid:
        """Return the ``BUS:B<x>:SVID`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SVID?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SVID?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.alert``: The ``BUS:B<x>:SVID:ALERT`` command tree.
            - ``.clock``: The ``BUS:B<x>:SVID:CLOCk`` command tree.
            - ``.data``: The ``BUS:B<x>:SVID:DATA`` command tree.
        """
        return self._svid

    @property
    def type(self) -> BusBItemType:
        """Return the ``BUS:B<x>:TYPe`` command.

        Description:
            - This command sets or queries the bus type or standard for the specified bus. The bus
              is specified by x. Arguments for a bus type are only available then the required
              serial bus option is installed.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:TYPe?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:TYPe value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:TYPe {ARINC429|AUDio|CAN|ETHernet|EUSB|FLEXRAY|I2C|I3C|LIN|MDIO|MIL1553B|PARallel|RS232C|SENT|SPI|SPMI|SVID|USB}
            - BUS:B<x>:TYPe?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``ARINC429`` specifies the ARINC 429 avionics serial bus.
            - ``AUDio`` specifies an audio bus.
            - ``CAN`` specifies a Controller Area Network bus.
            - ``ETHernet`` specifies the Ethernet bus.
            - ``EUSB`` specifies a eUSB bus. Requires option SR-EUSB2.
            - ``FLEXRAY`` specifies a FlexRay bus.
            - ``I2C`` specifies the Inter-IC bus.
            - ``I3C`` specifies the MIPI Improved Inter Integrated Circuit (I3C) bus.
            - ``LIN`` specifies a Local Interconnect Network bus.
            - ``MDIO`` specifies a MDIO bus.
            - ``MIL1553B`` specifies the MIL-STD-1553 avionics serial bus.
            - ``PARallel`` specifies a parallel bus.
            - ``RS232C`` specifies the RS-232 Serial bus.
            - ``SENT`` specifies the Single Edge Nibble Transmission (SENT) automotive serial bus.
            - ``SPI`` specifies the Serial Peripheral Interface bus.
            - ``SPMI`` Specifies a System Power Management Interface bus.
            - ``SVID`` Specifies a Serial VID bus.
            - ``USB`` specifies the Universal Serial bus.
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
            - ``.dataminusthreshold``: The ``BUS:B<x>:USB:DATAMINUSTHRESHold`` command.
            - ``.dataplusthreshold``: The ``BUS:B<x>:USB:DATAPLUSTHRESHold`` command.
            - ``.lowthreshold``: The ``BUS:B<x>:USB:LOWTHRESHold`` command.
            - ``.signaltype``: The ``BUS:B<x>:USB:SIGNALTYpe`` command.
            - ``.source``: The ``BUS:B<x>:USB:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:USB:THRESHold`` command.
        """
        return self._usb


class BusAddnew(SCPICmdWrite):
    """The ``BUS:ADDNew`` command.

    Description:
        - This command adds the specified bus. This command creates/adds the bus but does not
          display it (turn it on). In order to enable bus decoding and see the bus display on
          screen, send the ``DISPLAY:WAVEVIEWX:BUS:BX:STATE ON`` command.

    Usage:
        - Using the ``.write(value)`` method will send the ``BUS:ADDNew value`` command.

    SCPI Syntax:
        ```
        - BUS:ADDNew <QString>
        ```

    Info:
        - ``<QString>`` is a quoted string of the form 'B<NR1>' where NR1 is ≥1.
    """

    _WRAP_ARG_WITH_QUOTES = True


class Bus(SCPICmdRead):
    """The ``BUS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.addnew``: The ``BUS:ADDNew`` command.
        - ``.b``: The ``BUS:B<x>`` command tree.
        - ``.delete``: The ``BUS:DELete`` command.
        - ``.list``: The ``BUS:LIST`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "BUS") -> None:
        super().__init__(device, cmd_syntax)
        self._addnew = BusAddnew(device, f"{self._cmd_syntax}:ADDNew")
        self._b: Dict[int, BusBItem] = DefaultDictPassKeyToFactory(
            lambda x: BusBItem(device, f"{self._cmd_syntax}:B{x}")
        )
        self._delete = BusDelete(device, f"{self._cmd_syntax}:DELete")
        self._list = BusList(device, f"{self._cmd_syntax}:LIST")

    @property
    def addnew(self) -> BusAddnew:
        """Return the ``BUS:ADDNew`` command.

        Description:
            - This command adds the specified bus. This command creates/adds the bus but does not
              display it (turn it on). In order to enable bus decoding and see the bus display on
              screen, send the ``DISPLAY:WAVEVIEWX:BUS:BX:STATE ON`` command.

        Usage:
            - Using the ``.write(value)`` method will send the ``BUS:ADDNew value`` command.

        SCPI Syntax:
            ```
            - BUS:ADDNew <QString>
            ```

        Info:
            - ``<QString>`` is a quoted string of the form 'B<NR1>' where NR1 is ≥1.
        """
        return self._addnew

    @property
    def b(self) -> Dict[int, BusBItem]:
        """Return the ``BUS:B<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.arinc429a``: The ``BUS:B<x>:ARINC429A`` command tree.
            - ``.audio``: The ``BUS:B<x>:AUDio`` command tree.
            - ``.autoethernet``: The ``BUS:B<x>:AUTOETHERnet`` command tree.
            - ``.can``: The ``BUS:B<x>:CAN`` command tree.
            - ``.cphy``: The ``BUS:B<x>:CPHY`` command tree.
            - ``.cxpi``: The ``BUS:B<x>:CXPI`` command tree.
            - ``.display``: The ``BUS:B<x>:DISplay`` command tree.
            - ``.dphy``: The ``BUS:B<x>:DPHY`` command tree.
            - ``.espi``: The ``BUS:B<x>:ESPI`` command tree.
            - ``.ethercat``: The ``BUS:B<x>:ETHERCAT`` command tree.
            - ``.ethernet``: The ``BUS:B<x>:ETHERnet`` command tree.
            - ``.eusb``: The ``BUS:B<x>:EUSB`` command tree.
            - ``.flexray``: The ``BUS:B<x>:FLEXray`` command tree.
            - ``.i2c``: The ``BUS:B<x>:I2C`` command tree.
            - ``.i3c``: The ``BUS:B<x>:I3C`` command tree.
            - ``.label``: The ``BUS:B<x>:LABel`` command tree.
            - ``.lin``: The ``BUS:B<x>:LIN`` command tree.
            - ``.manchester``: The ``BUS:B<x>:MANChester`` command tree.
            - ``.mdio``: The ``BUS:B<x>:MDIO`` command tree.
            - ``.mil1553b``: The ``BUS:B<x>:MIL1553B`` command tree.
            - ``.nrz``: The ``BUS:B<x>:NRZ`` command tree.
            - ``.onewire``: The ``BUS:B<x>:ONEWIRe`` command tree.
            - ``.parallel``: The ``BUS:B<x>:PARallel`` command tree.
            - ``.psifive``: The ``BUS:B<x>:PSIFIVe`` command tree.
            - ``.rs232c``: The ``BUS:B<x>:RS232C`` command tree.
            - ``.s8b10b``: The ``BUS:B<x>:S8B10B`` command tree.
            - ``.sdlc``: The ``BUS:B<x>:SDLC`` command tree.
            - ``.sent``: The ``BUS:B<x>:SENT`` command tree.
            - ``.smbus``: The ``BUS:B<x>:SMBUS`` command tree.
            - ``.spacewire``: The ``BUS:B<x>:SPACEWIRe`` command tree.
            - ``.spi``: The ``BUS:B<x>:SPI`` command tree.
            - ``.spmi``: The ``BUS:B<x>:SPMI`` command tree.
            - ``.svid``: The ``BUS:B<x>:SVID`` command tree.
            - ``.type``: The ``BUS:B<x>:TYPe`` command.
            - ``.usb``: The ``BUS:B<x>:USB`` command tree.
        """
        return self._b

    @property
    def delete(self) -> BusDelete:
        """Return the ``BUS:DELete`` command.

        Description:
            - This command deletes the specified bus.

        Usage:
            - Using the ``.write(value)`` method will send the ``BUS:DELete value`` command.

        SCPI Syntax:
            ```
            - BUS:DELete <QString>
            ```

        Info:
            - ``<QString>`` specifies the bus to delete and is of the form 'B<NR1>', where <NR1> is
              ≥1.
        """
        return self._delete

    @property
    def list(self) -> BusList:
        """Return the ``BUS:LIST`` command.

        Description:
            - This query returns a comma separated list of all currently defined buses.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:LIST?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:LIST?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - BUS:LIST?
            ```
        """
        return self._list
