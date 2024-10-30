# pylint: disable=line-too-long
"""The measurement commands module.

These commands are used in the following models:
MSO2

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - MEASUrement:ADDMEAS {ACRMS|AMPlITUDE|AREA|BASE|BURSTWIDTH|DATARATE|DELAY|FALLSLEWRATE|FALLTIME|FREQUENCY|HIGHTIME|HOLD|LOWTIME|MAXIMUM|MEAN|MINIMUM|NDUty|NOVERSHOOT|NPERIOD|NWIDTTH|PDUTY|PERIOD|PHASE|PK2Pk|POVERSHOOT|PWIDTH|RISESLEWRATE|RISETIME|RMS|SETUP|SKEW|TIMEOUTSIDELEVEL|TIMETOMAX|TIMETOMIN|TOP}
    - MEASUrement:ADDNew 'QString'
    - MEASUrement:ANNOTate {OFF|AUTO}
    - MEASUrement:ANNOTate?
    - MEASUrement:CH<x>:REFLevels:ABSolute:FALLHigh <NR3>
    - MEASUrement:CH<x>:REFLevels:ABSolute:FALLHigh?
    - MEASUrement:CH<x>:REFLevels:ABSolute:FALLLow <NR3>
    - MEASUrement:CH<x>:REFLevels:ABSolute:FALLLow?
    - MEASUrement:CH<x>:REFLevels:ABSolute:FALLMid <NR3>
    - MEASUrement:CH<x>:REFLevels:ABSolute:FALLMid?
    - MEASUrement:CH<x>:REFLevels:ABSolute:HYSTeresis <NR3>
    - MEASUrement:CH<x>:REFLevels:ABSolute:HYSTeresis?
    - MEASUrement:CH<x>:REFLevels:ABSolute:RISEHigh <NR3>
    - MEASUrement:CH<x>:REFLevels:ABSolute:RISEHigh?
    - MEASUrement:CH<x>:REFLevels:ABSolute:RISELow <NR3>
    - MEASUrement:CH<x>:REFLevels:ABSolute:RISELow?
    - MEASUrement:CH<x>:REFLevels:ABSolute:RISEMid <NR3>
    - MEASUrement:CH<x>:REFLevels:ABSolute:RISEMid?
    - MEASUrement:CH<x>:REFLevels:ABSolute:TYPE {SAME|UNIQue}
    - MEASUrement:CH<x>:REFLevels:ABSolute:TYPE?
    - MEASUrement:CH<x>:REFLevels:BASETop {AUTO|MINMax|MEANhistogram|MODEhistogram}
    - MEASUrement:CH<x>:REFLevels:BASETop?
    - MEASUrement:CH<x>:REFLevels:METHod {PERCent|ABSolute}
    - MEASUrement:CH<x>:REFLevels:METHod?
    - MEASUrement:CH<x>:REFLevels:PERCent:FALLHigh <NR3>
    - MEASUrement:CH<x>:REFLevels:PERCent:FALLHigh?
    - MEASUrement:CH<x>:REFLevels:PERCent:FALLLow <NR3>
    - MEASUrement:CH<x>:REFLevels:PERCent:FALLLow?
    - MEASUrement:CH<x>:REFLevels:PERCent:FALLMid <NR3>
    - MEASUrement:CH<x>:REFLevels:PERCent:FALLMid?
    - MEASUrement:CH<x>:REFLevels:PERCent:HYSTeresis <NR3>
    - MEASUrement:CH<x>:REFLevels:PERCent:HYSTeresis?
    - MEASUrement:CH<x>:REFLevels:PERCent:RISEHigh <NR3>
    - MEASUrement:CH<x>:REFLevels:PERCent:RISEHigh?
    - MEASUrement:CH<x>:REFLevels:PERCent:RISELow <NR3>
    - MEASUrement:CH<x>:REFLevels:PERCent:RISELow?
    - MEASUrement:CH<x>:REFLevels:PERCent:RISEMid <NR3>
    - MEASUrement:CH<x>:REFLevels:PERCent:RISEMid?
    - MEASUrement:CH<x>:REFLevels:PERCent:TYPE {TENNinety|TWENtyeighty|CUSTom}
    - MEASUrement:CH<x>:REFLevels:PERCent:TYPE?
    - MEASUrement:DELETEALL
    - MEASUrement:DELete <QString>
    - MEASUrement:EDGE<x> {RISE|FALL|BOTH}
    - MEASUrement:EDGE<x>?
    - MEASUrement:GATing {NONE|SCREEN|CURSor|LOGic|SEARch|TIMe}
    - MEASUrement:GATing:ACTive {HIGH|LOW}
    - MEASUrement:GATing:ACTive?
    - MEASUrement:GATing:ENDtime <NR3>
    - MEASUrement:GATing:ENDtime?
    - MEASUrement:GATing:HYSTeresis <NR3>
    - MEASUrement:GATing:HYSTeresis?
    - MEASUrement:GATing:LOGICSource {CH<x>|MATH<x>|REF<x>}
    - MEASUrement:GATing:LOGICSource?
    - MEASUrement:GATing:MIDRef <NR3>
    - MEASUrement:GATing:MIDRef?
    - MEASUrement:GATing:SEARCHSource SEARCH<x>
    - MEASUrement:GATing:SEARCHSource?
    - MEASUrement:GATing:STARTtime <NR3>
    - MEASUrement:GATing:STARTtime?
    - MEASUrement:GATing?
    - MEASUrement:INTERp {AUTO|SINX|LINear}
    - MEASUrement:INTERp?
    - MEASUrement:LIST?
    - MEASUrement:MATH<x>:REFLevels:ABSolute:FALLHigh <NR3>
    - MEASUrement:MATH<x>:REFLevels:ABSolute:FALLHigh?
    - MEASUrement:MATH<x>:REFLevels:ABSolute:FALLLow <NR3>
    - MEASUrement:MATH<x>:REFLevels:ABSolute:FALLLow?
    - MEASUrement:MATH<x>:REFLevels:ABSolute:FALLMid <NR3>
    - MEASUrement:MATH<x>:REFLevels:ABSolute:FALLMid?
    - MEASUrement:MATH<x>:REFLevels:ABSolute:HYSTeresis <NR3>
    - MEASUrement:MATH<x>:REFLevels:ABSolute:HYSTeresis?
    - MEASUrement:MATH<x>:REFLevels:ABSolute:RISEHigh <NR3>
    - MEASUrement:MATH<x>:REFLevels:ABSolute:RISEHigh?
    - MEASUrement:MATH<x>:REFLevels:ABSolute:RISELow <NR3>
    - MEASUrement:MATH<x>:REFLevels:ABSolute:RISELow?
    - MEASUrement:MATH<x>:REFLevels:ABSolute:RISEMid <NR3>
    - MEASUrement:MATH<x>:REFLevels:ABSolute:RISEMid?
    - MEASUrement:MATH<x>:REFLevels:ABSolute:TYPE {SAME|UNIQue}
    - MEASUrement:MATH<x>:REFLevels:ABSolute:TYPE?
    - MEASUrement:MATH<x>:REFLevels:BASETop {AUTO|MINMax|MEANhistogram|MODEhistogram|EYEhistogram}
    - MEASUrement:MATH<x>:REFLevels:BASETop?
    - MEASUrement:MATH<x>:REFLevels:METHod {PERCent|ABSolute}
    - MEASUrement:MATH<x>:REFLevels:METHod?
    - MEASUrement:MATH<x>:REFLevels:PERCent:FALLHigh <NR3>
    - MEASUrement:MATH<x>:REFLevels:PERCent:FALLHigh?
    - MEASUrement:MATH<x>:REFLevels:PERCent:FALLLow <NR3>
    - MEASUrement:MATH<x>:REFLevels:PERCent:FALLLow?
    - MEASUrement:MATH<x>:REFLevels:PERCent:FALLMid <NR3>
    - MEASUrement:MATH<x>:REFLevels:PERCent:FALLMid?
    - MEASUrement:MATH<x>:REFLevels:PERCent:HYSTeresis <NR3>
    - MEASUrement:MATH<x>:REFLevels:PERCent:HYSTeresis?
    - MEASUrement:MATH<x>:REFLevels:PERCent:RISEHigh <NR3>
    - MEASUrement:MATH<x>:REFLevels:PERCent:RISEHigh?
    - MEASUrement:MATH<x>:REFLevels:PERCent:RISELow <NR3>
    - MEASUrement:MATH<x>:REFLevels:PERCent:RISELow?
    - MEASUrement:MATH<x>:REFLevels:PERCent:RISEMid <NR3>
    - MEASUrement:MATH<x>:REFLevels:PERCent:RISEMid?
    - MEASUrement:MATH<x>:REFLevels:PERCent:TYPE {TENNinety|TWENtyeighty|CUSTom}
    - MEASUrement:MATH<x>:REFLevels:PERCent:TYPE?
    - MEASUrement:MEAS<x>:BURSTEDGTYPe {RISE|FALL}
    - MEASUrement:MEAS<x>:BURSTEDGTYPe?
    - MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MAXimum?
    - MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MEAN?
    - MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MINimum?
    - MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:PK2PK?
    - MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:POPUlation?
    - MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:STDDev?
    - MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MAXimum?
    - MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MEAN?
    - MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MINimum?
    - MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:PK2PK?
    - MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:POPUlation?
    - MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:STDDev?
    - MEASUrement:MEAS<x>:DELay:EDGE<x> {FALL|RISe|BOTH|SAMEas|OPPositeas}
    - MEASUrement:MEAS<x>:DELay:EDGE<x>?
    - MEASUrement:MEAS<x>:DISPlaystat:ENABle {ON|OFF|<NR1>}
    - MEASUrement:MEAS<x>:DISPlaystat:ENABle?
    - MEASUrement:MEAS<x>:EDGE<x> {RISE|FALL|BOTH}
    - MEASUrement:MEAS<x>:EDGE<x>?
    - MEASUrement:MEAS<x>:EDGEIncre <NR3>
    - MEASUrement:MEAS<x>:EDGEIncre?
    - MEASUrement:MEAS<x>:EDGES:FROMLevel {MID|LOW|HIGH}
    - MEASUrement:MEAS<x>:EDGES:FROMLevel?
    - MEASUrement:MEAS<x>:EDGES:LEVel {HIGH|LOW|BOTH}
    - MEASUrement:MEAS<x>:EDGES:LEVel?
    - MEASUrement:MEAS<x>:EDGES:N <NR3>
    - MEASUrement:MEAS<x>:EDGES:N?
    - MEASUrement:MEAS<x>:EDGES:SLEWRATEMethod {NOMinal|DDR}
    - MEASUrement:MEAS<x>:EDGES:SLEWRATEMethod?
    - MEASUrement:MEAS<x>:EDGES:TOLevel {HIGH|MID|LOW}
    - MEASUrement:MEAS<x>:EDGES:TOLevel?
    - MEASUrement:MEAS<x>:FAILCount?
    - MEASUrement:MEAS<x>:FROMEDGESEARCHDIRect {FORWard|BACKWard}
    - MEASUrement:MEAS<x>:FROMEDGESEARCHDIRect?
    - MEASUrement:MEAS<x>:FROMedge {RISe|FALL|BOTH}
    - MEASUrement:MEAS<x>:FROMedge?
    - MEASUrement:MEAS<x>:GATing {NONE|SCREEN|CURSor|LOGic|SEARch|TIMe}
    - MEASUrement:MEAS<x>:GATing:ACTive {HIGH|LOW}
    - MEASUrement:MEAS<x>:GATing:ACTive?
    - MEASUrement:MEAS<x>:GATing:ENDtime <NR3>
    - MEASUrement:MEAS<x>:GATing:ENDtime?
    - MEASUrement:MEAS<x>:GATing:GLOBal {OFF|ON|0|1}
    - MEASUrement:MEAS<x>:GATing:GLOBal?
    - MEASUrement:MEAS<x>:GATing:HYSTeresis <NR3>
    - MEASUrement:MEAS<x>:GATing:HYSTeresis?
    - MEASUrement:MEAS<x>:GATing:LOGICSource {CH<x>|MATH<x>|REF<x>}
    - MEASUrement:MEAS<x>:GATing:LOGICSource?
    - MEASUrement:MEAS<x>:GATing:MIDRef <NR3>
    - MEASUrement:MEAS<x>:GATing:MIDRef?
    - MEASUrement:MEAS<x>:GATing:SEARCHSource SEARCH1
    - MEASUrement:MEAS<x>:GATing:SEARCHSource?
    - MEASUrement:MEAS<x>:GATing:STARTtime <NR3>
    - MEASUrement:MEAS<x>:GATing:STARTtime?
    - MEASUrement:MEAS<x>:GATing?
    - MEASUrement:MEAS<x>:GLOBalref {OFF|ON|0|1}
    - MEASUrement:MEAS<x>:GLOBalref?
    - MEASUrement:MEAS<x>:HIGHREFVoltage <NR3>
    - MEASUrement:MEAS<x>:HIGHREFVoltage?
    - MEASUrement:MEAS<x>:IDLETime <NR3>
    - MEASUrement:MEAS<x>:IDLETime?
    - MEASUrement:MEAS<x>:LABel <QString>
    - MEASUrement:MEAS<x>:LABel?
    - MEASUrement:MEAS<x>:LOWREFVoltage <NR3>
    - MEASUrement:MEAS<x>:LOWREFVoltage?
    - MEASUrement:MEAS<x>:PASSFAILENabled <NR1>
    - MEASUrement:MEAS<x>:PASSFAILENabled?
    - MEASUrement:MEAS<x>:PASSFAILHIGHlimit <NR2>
    - MEASUrement:MEAS<x>:PASSFAILHIGHlimit?
    - MEASUrement:MEAS<x>:PASSFAILLIMit <NR2>
    - MEASUrement:MEAS<x>:PASSFAILLIMit?
    - MEASUrement:MEAS<x>:PASSFAILLOWlimit <NR2>
    - MEASUrement:MEAS<x>:PASSFAILLOWlimit?
    - MEASUrement:MEAS<x>:PASSFAILMARgin <NR2>
    - MEASUrement:MEAS<x>:PASSFAILMARgin?
    - MEASUrement:MEAS<x>:PASSFAILWHEN {LESSthan|GREATERthan|Equals|NOTEQuals|INSIDErange|OUTSIDErange}
    - MEASUrement:MEAS<x>:PASSFAILWHEN?
    - MEASUrement:MEAS<x>:PERFREQ:EDGE {FIRST|RISE|FALL}
    - MEASUrement:MEAS<x>:PERFREQ:EDGE?
    - MEASUrement:MEAS<x>:POLarity {NORMal|INVerted}
    - MEASUrement:MEAS<x>:POLarity?
    - MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLLow <NR3>
    - MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLLow?
    - MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLMid <NR3>
    - MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLMid?
    - MEASUrement:MEAS<x>:REFLevels1:ABSolute:HYSTeresis <NR3>
    - MEASUrement:MEAS<x>:REFLevels1:ABSolute:HYSTeresis?
    - MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEHigh <NR3>
    - MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEHigh?
    - MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISELow <NR3>
    - MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISELow?
    - MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEMid <NR3>
    - MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEMid?
    - MEASUrement:MEAS<x>:REFLevels1:ABSolute:TYPE {SAME|UNIQue}
    - MEASUrement:MEAS<x>:REFLevels1:ABSolute:TYPE?
    - MEASUrement:MEAS<x>:REFLevels1:BASETop {AUTO|MINMax|MEANhistogram|MODEhistogram|EYEhistogram}
    - MEASUrement:MEAS<x>:REFLevels1:BASETop?
    - MEASUrement:MEAS<x>:REFLevels1:METHod {PERCent|ABSolute}
    - MEASUrement:MEAS<x>:REFLevels1:METHod?
    - MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLHigh <NR3>
    - MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLHigh?
    - MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLLow <NR3>
    - MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLLow?
    - MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLMid <NR3>
    - MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLMid?
    - MEASUrement:MEAS<x>:REFLevels1:PERCent:HYSTeresis <NR3>
    - MEASUrement:MEAS<x>:REFLevels1:PERCent:HYSTeresis?
    - MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEHigh <NR3>
    - MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEHigh?
    - MEASUrement:MEAS<x>:REFLevels1:PERCent:RISELow <NR3>
    - MEASUrement:MEAS<x>:REFLevels1:PERCent:RISELow?
    - MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEMid <NR3>
    - MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEMid?
    - MEASUrement:MEAS<x>:REFLevels1:PERCent:TYPE {TENNinety|TWENtyeighty|CUSTom}
    - MEASUrement:MEAS<x>:REFLevels1:PERCent:TYPE?
    - MEASUrement:MEAS<x>:REFLevels:ABSolute:FALLHigh <NR3>
    - MEASUrement:MEAS<x>:REFLevels:ABSolute:FALLHigh?
    - MEASUrement:MEAS<x>:REFMode {AUTO|MANual}
    - MEASUrement:MEAS<x>:REFMode?
    - MEASUrement:MEAS<x>:REFVoltage <NR3>
    - MEASUrement:MEAS<x>:REFVoltage?
    - MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MAXimum?
    - MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MEAN?
    - MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MINimum?
    - MEASUrement:MEAS<x>:RESUlts:ALLAcqs:PK2PK?
    - MEASUrement:MEAS<x>:RESUlts:ALLAcqs:POPUlation?
    - MEASUrement:MEAS<x>:RESUlts:ALLAcqs:STDDev?
    - MEASUrement:MEAS<x>:RESUlts:CURRentacq:MAXimum?
    - MEASUrement:MEAS<x>:RESUlts:CURRentacq:MEAN?
    - MEASUrement:MEAS<x>:RESUlts:CURRentacq:MINimum?
    - MEASUrement:MEAS<x>:RESUlts:CURRentacq:PK2PK?
    - MEASUrement:MEAS<x>:RESUlts:CURRentacq:POPUlation?
    - MEASUrement:MEAS<x>:RESUlts:CURRentacq:STDDev?
    - MEASUrement:MEAS<x>:SIGNALType {CLOCK|DATA|AUTO}
    - MEASUrement:MEAS<x>:SIGNALType?
    - MEASUrement:MEAS<x>:SOUrce1 {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>}
    - MEASUrement:MEAS<x>:SOUrce1?
    - MEASUrement:MEAS<x>:STATUS?
    - MEASUrement:MEAS<x>:TOEDGESEARCHDIRect {FORWard|BACKWard}
    - MEASUrement:MEAS<x>:TOEDGESEARCHDIRect?
    - MEASUrement:MEAS<x>:TOEdge {SAMEas|OPPositeas|RISe|FALL|BOTH}
    - MEASUrement:MEAS<x>:TOEdge?
    - MEASUrement:MEAS<x>:TRANSition {ON|OFF|<NR1>}
    - MEASUrement:MEAS<x>:TRANSition?
    - MEASUrement:MEAS<x>:TYPe {ACRMS|AMPlITUDE|AREA|BASE|BURSTWIDTH|DATARATE|DELAY|FALLSLEWRATE|FALLTIME|FREQUENCY|HIGHTIME|HOLD|LOWTIME|MAXIMUM|MEAN|MINIMUM|NDUtY|NPERIOD|NOVERSHOOT|NWIDTH|PDUTY|PERIOD|PHASE|PK2Pk|POVERSHOOT|PWIDTH|RISESLEWRATE|RISETIME|RMS|SETUP|SKEW|TIMEOUTSIDELEVEL|TOP}
    - MEASUrement:MEAS<x>:TYPe?
    - MEASUrement:MEAS<x>:XUNIT?
    - MEASUrement:MEAS<x>:YUNIT?
    - MEASUrement:REF<x>:REFLevels:ABSolute:FALLHigh <NR3>
    - MEASUrement:REF<x>:REFLevels:ABSolute:FALLHigh?
    - MEASUrement:REF<x>:REFLevels:ABSolute:FALLLow <NR3>
    - MEASUrement:REF<x>:REFLevels:ABSolute:FALLLow?
    - MEASUrement:REF<x>:REFLevels:ABSolute:FALLMid <NR3>
    - MEASUrement:REF<x>:REFLevels:ABSolute:FALLMid?
    - MEASUrement:REF<x>:REFLevels:ABSolute:HYSTeresis <NR3>
    - MEASUrement:REF<x>:REFLevels:ABSolute:HYSTeresis?
    - MEASUrement:REF<x>:REFLevels:ABSolute:RISEHigh <NR3>
    - MEASUrement:REF<x>:REFLevels:ABSolute:RISEHigh?
    - MEASUrement:REF<x>:REFLevels:ABSolute:RISELow <NR3>
    - MEASUrement:REF<x>:REFLevels:ABSolute:RISELow?
    - MEASUrement:REF<x>:REFLevels:ABSolute:RISEMid <NR3>
    - MEASUrement:REF<x>:REFLevels:ABSolute:RISEMid?
    - MEASUrement:REF<x>:REFLevels:ABSolute:TYPE {SAME|UNIQue}
    - MEASUrement:REF<x>:REFLevels:ABSolute:TYPE?
    - MEASUrement:REF<x>:REFLevels:BASETop {AUTO|MINMax|MEANhistogram|MODEhistogram|EYEhistogram}
    - MEASUrement:REF<x>:REFLevels:BASETop?
    - MEASUrement:REF<x>:REFLevels:METHod {PERCent|ABSolute}
    - MEASUrement:REF<x>:REFLevels:METHod?
    - MEASUrement:REF<x>:REFLevels:PERCent:FALLHigh <NR3>
    - MEASUrement:REF<x>:REFLevels:PERCent:FALLHigh?
    - MEASUrement:REF<x>:REFLevels:PERCent:FALLLow <NR3>
    - MEASUrement:REF<x>:REFLevels:PERCent:FALLLow?
    - MEASUrement:REF<x>:REFLevels:PERCent:FALLMid <NR3>
    - MEASUrement:REF<x>:REFLevels:PERCent:FALLMid?
    - MEASUrement:REF<x>:REFLevels:PERCent:HYSTeresis <NR3>
    - MEASUrement:REF<x>:REFLevels:PERCent:HYSTeresis?
    - MEASUrement:REF<x>:REFLevels:PERCent:RISEHigh <NR3>
    - MEASUrement:REF<x>:REFLevels:PERCent:RISEHigh?
    - MEASUrement:REF<x>:REFLevels:PERCent:RISELow <NR3>
    - MEASUrement:REF<x>:REFLevels:PERCent:RISELow?
    - MEASUrement:REF<x>:REFLevels:PERCent:RISEMid <NR3>
    - MEASUrement:REF<x>:REFLevels:PERCent:RISEMid?
    - MEASUrement:REF<x>:REFLevels:PERCent:TYPE {TENNinety|TWENtyeighty|CUSTom}
    - MEASUrement:REF<x>:REFLevels:PERCent:TYPE?
    - MEASUrement:REFLevels:ABSolute:FALLHigh <NR3>
    - MEASUrement:REFLevels:ABSolute:FALLHigh?
    - MEASUrement:REFLevels:ABSolute:FALLLow <NR3>
    - MEASUrement:REFLevels:ABSolute:FALLLow?
    - MEASUrement:REFLevels:ABSolute:FALLMid <NR3>
    - MEASUrement:REFLevels:ABSolute:FALLMid?
    - MEASUrement:REFLevels:ABSolute:HYSTeresis <NR3>
    - MEASUrement:REFLevels:ABSolute:HYSTeresis?
    - MEASUrement:REFLevels:ABSolute:RISEHigh <NR3>
    - MEASUrement:REFLevels:ABSolute:RISEHigh?
    - MEASUrement:REFLevels:ABSolute:RISELow <NR3>
    - MEASUrement:REFLevels:ABSolute:RISELow?
    - MEASUrement:REFLevels:ABSolute:RISEMid <NR3>
    - MEASUrement:REFLevels:ABSolute:RISEMid?
    - MEASUrement:REFLevels:ABSolute:TYPE {SAME|UNIQue}
    - MEASUrement:REFLevels:ABSolute:TYPE?
    - MEASUrement:REFLevels:BASETop {AUTO|MINMax|MEANhistogram|MODEhistogram|EYEhistogram}
    - MEASUrement:REFLevels:BASETop?
    - MEASUrement:REFLevels:METHod {PERCent|ABSolute}
    - MEASUrement:REFLevels:METHod?
    - MEASUrement:REFLevels:MODE {LATCh|CONTinuous}
    - MEASUrement:REFLevels:MODE?
    - MEASUrement:REFLevels:PERCent:FALLHigh <NR3>
    - MEASUrement:REFLevels:PERCent:FALLHigh?
    - MEASUrement:REFLevels:PERCent:FALLLow <NR3>
    - MEASUrement:REFLevels:PERCent:FALLLow?
    - MEASUrement:REFLevels:PERCent:FALLMid <NR3>
    - MEASUrement:REFLevels:PERCent:FALLMid?
    - MEASUrement:REFLevels:PERCent:HYSTeresis <NR3>
    - MEASUrement:REFLevels:PERCent:HYSTeresis?
    - MEASUrement:REFLevels:PERCent:RISEHigh <NR3>
    - MEASUrement:REFLevels:PERCent:RISEHigh?
    - MEASUrement:REFLevels:PERCent:RISELow <NR3>
    - MEASUrement:REFLevels:PERCent:RISELow?
    - MEASUrement:REFLevels:PERCent:RISEMid <NR3>
    - MEASUrement:REFLevels:PERCent:RISEMid?
    - MEASUrement:REFLevels:PERCent:TYPE {TENNinety|TWENtyeighty|CUSTom}
    - MEASUrement:REFLevels:PERCent:TYPE?
    - MEASUrement:REFLevels:TYPE {GLOBal|PERSource}
    - MEASUrement:REFLevels:TYPE?
    - MEASUrement:STATIstics:CYCLEMode {OFF|ON|0|1}
    - MEASUrement:STATIstics:CYCLEMode?
    - MEASUrement?
    ```
"""  # noqa: E501

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    SCPICmdWriteNoArguments,
    ValidatedChannel,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class MeasurementStatisticsCyclemode(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:STATIstics:CYCLEMode`` command.

    Description:
        - This command turns on and off cycle to cycle measurement statistics tracking and affects
          computation and display of cycle-cycle statistics in the Measurement Result table. It
          affects measurement statistics after being enabled and after new data is acquired and
          measured.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:STATIstics:CYCLEMode?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:STATIstics:CYCLEMode?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:STATIstics:CYCLEMode value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:STATIstics:CYCLEMode {OFF|ON|0|1}
        - MEASUrement:STATIstics:CYCLEMode?
        ```

    Info:
        - ``OFF`` turns off statistics for all measurements. This is the default value.
        - ``ON`` turns on statistics and displays all statistics for each measurement.
        - ``0`` turns off statistics for all measurements.
        - ``1`` turns on statistics and displays all statistics for each measurement.
    """


class MeasurementStatistics(SCPICmdRead):
    """The ``MEASUrement:STATIstics`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:STATIstics?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:STATIstics?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.cyclemode``: The ``MEASUrement:STATIstics:CYCLEMode`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._cyclemode = MeasurementStatisticsCyclemode(device, f"{self._cmd_syntax}:CYCLEMode")

    @property
    def cyclemode(self) -> MeasurementStatisticsCyclemode:
        """Return the ``MEASUrement:STATIstics:CYCLEMode`` command.

        Description:
            - This command turns on and off cycle to cycle measurement statistics tracking and
              affects computation and display of cycle-cycle statistics in the Measurement Result
              table. It affects measurement statistics after being enabled and after new data is
              acquired and measured.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:STATIstics:CYCLEMode?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:STATIstics:CYCLEMode?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:STATIstics:CYCLEMode value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:STATIstics:CYCLEMode {OFF|ON|0|1}
            - MEASUrement:STATIstics:CYCLEMode?
            ```

        Info:
            - ``OFF`` turns off statistics for all measurements. This is the default value.
            - ``ON`` turns on statistics and displays all statistics for each measurement.
            - ``0`` turns off statistics for all measurements.
            - ``1`` turns on statistics and displays all statistics for each measurement.
        """
        return self._cyclemode


class MeasurementReflevelsType(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevels:TYPE`` command.

    Description:
        - This command sets or queries the shared reference level method used for sources of
          measurement calculations.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevels:TYPE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:REFLevels:TYPE value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevels:TYPE {GLOBal|PERSource}
        - MEASUrement:REFLevels:TYPE?
        ```

    Info:
        - ``GLOBal`` shares reference levels across measurements.
        - ``PERSource`` causes reference levels to be used on individual measurements.
    """


class MeasurementReflevelsPercentType(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevels:PERCent:TYPE`` command.

    Description:
        - This command sets or queries the reference level percent type for the measurement.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:PERCent:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevels:PERCent:TYPE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REFLevels:PERCent:TYPE value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevels:PERCent:TYPE {TENNinety|TWENtyeighty|CUSTom}
        - MEASUrement:REFLevels:PERCent:TYPE?
        ```

    Info:
        - ``TENNinety`` sets the values for Low, Mid and High Ref to 10%, 50% and 90% respectively.
        - ``TWENtyeighty`` sets the values for Low, Mid and High Ref are set to 20%, 50% and 80%
          respectively.
        - ``CUSTom`` allows setting other reference level percents.
    """


class MeasurementReflevelsPercentRisemid(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevels:PERCent:RISEMid`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the mid reference level of the rising edge when the measurement's
          ref level method is set to percent.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:PERCent:RISEMid?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REFLevels:PERCent:RISEMid?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REFLevels:PERCent:RISEMid value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevels:PERCent:RISEMid <NR3>
        - MEASUrement:REFLevels:PERCent:RISEMid?
        ```

    Info:
        - ``<NR3>`` is the percentage used to calculate the mid reference level of the rising edge.
    """


class MeasurementReflevelsPercentRiselow(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevels:PERCent:RISELow`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the low reference level of the rising edge when the measurement's
          ref level method is set to percent.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:PERCent:RISELow?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REFLevels:PERCent:RISELow?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REFLevels:PERCent:RISELow value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevels:PERCent:RISELow <NR3>
        - MEASUrement:REFLevels:PERCent:RISELow?
        ```

    Info:
        - ``<NR3>`` is the percentage used to calculate the low reference level of the rising edge.
    """


class MeasurementReflevelsPercentRisehigh(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevels:PERCent:RISEHigh`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the high reference level of the rising edge when the measurement's
          ref level method is set to percent.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:PERCent:RISEHigh?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REFLevels:PERCent:RISEHigh?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REFLevels:PERCent:RISEHigh value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevels:PERCent:RISEHigh <NR3>
        - MEASUrement:REFLevels:PERCent:RISEHigh?
        ```

    Info:
        - ``<NR3>`` is the percentage used to calculate the high reference level of the rising edge.
    """


class MeasurementReflevelsPercentHysteresis(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevels:PERCent:HYSTeresis`` command.

    Description:
        - This command sets or queries the percentage (where 100% is equal to MAX and 1% is equal to
          MIN) used to calculate the hysteresis of the reference level when the measurement's ref
          level method is set to percent.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:PERCent:HYSTeresis?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REFLevels:PERCent:HYSTeresis?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REFLevels:PERCent:HYSTeresis value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevels:PERCent:HYSTeresis <NR3>
        - MEASUrement:REFLevels:PERCent:HYSTeresis?
        ```

    Info:
        - ``<NR3>`` is the percentage used to calculate the hysteresis of the reference level.
    """


class MeasurementReflevelsPercentFallmid(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevels:PERCent:FALLMid`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the mid reference level of the falling edge when the measurement's
          ref level method is set to percent.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:PERCent:FALLMid?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REFLevels:PERCent:FALLMid?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REFLevels:PERCent:FALLMid value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevels:PERCent:FALLMid <NR3>
        - MEASUrement:REFLevels:PERCent:FALLMid?
        ```

    Info:
        - ``<NR3>`` is the percentage used to calculate the mid reference level of the falling edge.
    """


class MeasurementReflevelsPercentFalllow(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevels:PERCent:FALLLow`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the mid reference level of the falling edge when the measurement's
          ref level method is set to percent.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:PERCent:FALLLow?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REFLevels:PERCent:FALLLow?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REFLevels:PERCent:FALLLow value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevels:PERCent:FALLLow <NR3>
        - MEASUrement:REFLevels:PERCent:FALLLow?
        ```

    Info:
        - ``<NR3>`` is the percentage used to calculate the mid reference level of the falling edge.
    """


class MeasurementReflevelsPercentFallhigh(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevels:PERCent:FALLHigh`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the high reference level of the falling edge when the
          measurement's ref level method is set to percent.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:PERCent:FALLHigh?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REFLevels:PERCent:FALLHigh?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REFLevels:PERCent:FALLHigh value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevels:PERCent:FALLHigh <NR3>
        - MEASUrement:REFLevels:PERCent:FALLHigh?
        ```

    Info:
        - ``<NR3>`` is the percentage used to calculate the high reference level of the falling
          edge.
    """


#  pylint: disable=too-many-instance-attributes
class MeasurementReflevelsPercent(SCPICmdRead):
    """The ``MEASUrement:REFLevels:PERCent`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:PERCent?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevels:PERCent?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.fallhigh``: The ``MEASUrement:REFLevels:PERCent:FALLHigh`` command.
        - ``.falllow``: The ``MEASUrement:REFLevels:PERCent:FALLLow`` command.
        - ``.fallmid``: The ``MEASUrement:REFLevels:PERCent:FALLMid`` command.
        - ``.hysteresis``: The ``MEASUrement:REFLevels:PERCent:HYSTeresis`` command.
        - ``.risehigh``: The ``MEASUrement:REFLevels:PERCent:RISEHigh`` command.
        - ``.riselow``: The ``MEASUrement:REFLevels:PERCent:RISELow`` command.
        - ``.risemid``: The ``MEASUrement:REFLevels:PERCent:RISEMid`` command.
        - ``.type``: The ``MEASUrement:REFLevels:PERCent:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fallhigh = MeasurementReflevelsPercentFallhigh(device, f"{self._cmd_syntax}:FALLHigh")
        self._falllow = MeasurementReflevelsPercentFalllow(device, f"{self._cmd_syntax}:FALLLow")
        self._fallmid = MeasurementReflevelsPercentFallmid(device, f"{self._cmd_syntax}:FALLMid")
        self._hysteresis = MeasurementReflevelsPercentHysteresis(
            device, f"{self._cmd_syntax}:HYSTeresis"
        )
        self._risehigh = MeasurementReflevelsPercentRisehigh(device, f"{self._cmd_syntax}:RISEHigh")
        self._riselow = MeasurementReflevelsPercentRiselow(device, f"{self._cmd_syntax}:RISELow")
        self._risemid = MeasurementReflevelsPercentRisemid(device, f"{self._cmd_syntax}:RISEMid")
        self._type = MeasurementReflevelsPercentType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def fallhigh(self) -> MeasurementReflevelsPercentFallhigh:
        """Return the ``MEASUrement:REFLevels:PERCent:FALLHigh`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the high reference level of the falling edge when the
              measurement's ref level method is set to percent.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:REFLevels:PERCent:FALLHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REFLevels:PERCent:FALLHigh?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevels:PERCent:FALLHigh value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevels:PERCent:FALLHigh <NR3>
            - MEASUrement:REFLevels:PERCent:FALLHigh?
            ```

        Info:
            - ``<NR3>`` is the percentage used to calculate the high reference level of the falling
              edge.
        """
        return self._fallhigh

    @property
    def falllow(self) -> MeasurementReflevelsPercentFalllow:
        """Return the ``MEASUrement:REFLevels:PERCent:FALLLow`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the mid reference level of the falling edge when the
              measurement's ref level method is set to percent.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:PERCent:FALLLow?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REFLevels:PERCent:FALLLow?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevels:PERCent:FALLLow value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevels:PERCent:FALLLow <NR3>
            - MEASUrement:REFLevels:PERCent:FALLLow?
            ```

        Info:
            - ``<NR3>`` is the percentage used to calculate the mid reference level of the falling
              edge.
        """
        return self._falllow

    @property
    def fallmid(self) -> MeasurementReflevelsPercentFallmid:
        """Return the ``MEASUrement:REFLevels:PERCent:FALLMid`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the mid reference level of the falling edge when the
              measurement's ref level method is set to percent.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:PERCent:FALLMid?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REFLevels:PERCent:FALLMid?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevels:PERCent:FALLMid value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevels:PERCent:FALLMid <NR3>
            - MEASUrement:REFLevels:PERCent:FALLMid?
            ```

        Info:
            - ``<NR3>`` is the percentage used to calculate the mid reference level of the falling
              edge.
        """
        return self._fallmid

    @property
    def hysteresis(self) -> MeasurementReflevelsPercentHysteresis:
        """Return the ``MEASUrement:REFLevels:PERCent:HYSTeresis`` command.

        Description:
            - This command sets or queries the percentage (where 100% is equal to MAX and 1% is
              equal to MIN) used to calculate the hysteresis of the reference level when the
              measurement's ref level method is set to percent.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:REFLevels:PERCent:HYSTeresis?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REFLevels:PERCent:HYSTeresis?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevels:PERCent:HYSTeresis value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevels:PERCent:HYSTeresis <NR3>
            - MEASUrement:REFLevels:PERCent:HYSTeresis?
            ```

        Info:
            - ``<NR3>`` is the percentage used to calculate the hysteresis of the reference level.
        """
        return self._hysteresis

    @property
    def risehigh(self) -> MeasurementReflevelsPercentRisehigh:
        """Return the ``MEASUrement:REFLevels:PERCent:RISEHigh`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the high reference level of the rising edge when the
              measurement's ref level method is set to percent.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:REFLevels:PERCent:RISEHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REFLevels:PERCent:RISEHigh?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevels:PERCent:RISEHigh value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevels:PERCent:RISEHigh <NR3>
            - MEASUrement:REFLevels:PERCent:RISEHigh?
            ```

        Info:
            - ``<NR3>`` is the percentage used to calculate the high reference level of the rising
              edge.
        """
        return self._risehigh

    @property
    def riselow(self) -> MeasurementReflevelsPercentRiselow:
        """Return the ``MEASUrement:REFLevels:PERCent:RISELow`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the low reference level of the rising edge when the
              measurement's ref level method is set to percent.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:PERCent:RISELow?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REFLevels:PERCent:RISELow?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevels:PERCent:RISELow value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevels:PERCent:RISELow <NR3>
            - MEASUrement:REFLevels:PERCent:RISELow?
            ```

        Info:
            - ``<NR3>`` is the percentage used to calculate the low reference level of the rising
              edge.
        """
        return self._riselow

    @property
    def risemid(self) -> MeasurementReflevelsPercentRisemid:
        """Return the ``MEASUrement:REFLevels:PERCent:RISEMid`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the mid reference level of the rising edge when the
              measurement's ref level method is set to percent.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:PERCent:RISEMid?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REFLevels:PERCent:RISEMid?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevels:PERCent:RISEMid value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevels:PERCent:RISEMid <NR3>
            - MEASUrement:REFLevels:PERCent:RISEMid?
            ```

        Info:
            - ``<NR3>`` is the percentage used to calculate the mid reference level of the rising
              edge.
        """
        return self._risemid

    @property
    def type(self) -> MeasurementReflevelsPercentType:
        """Return the ``MEASUrement:REFLevels:PERCent:TYPE`` command.

        Description:
            - This command sets or queries the reference level percent type for the measurement.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:PERCent:TYPE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REFLevels:PERCent:TYPE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevels:PERCent:TYPE value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevels:PERCent:TYPE {TENNinety|TWENtyeighty|CUSTom}
            - MEASUrement:REFLevels:PERCent:TYPE?
            ```

        Info:
            - ``TENNinety`` sets the values for Low, Mid and High Ref to 10%, 50% and 90%
              respectively.
            - ``TWENtyeighty`` sets the values for Low, Mid and High Ref are set to 20%, 50% and 80%
              respectively.
            - ``CUSTom`` allows setting other reference level percents.
        """
        return self._type


class MeasurementReflevelsMode(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevels:MODE`` command.

    Description:
        - This command sets or queries how often reference levels are calculated.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:MODE?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevels:MODE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:REFLevels:MODE value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevels:MODE {LATCh|CONTinuous}
        - MEASUrement:REFLevels:MODE?
        ```

    Info:
        - ``LATCh`` calculates reference levels only on the first acquisition after a statistics
          reset.
        - ``CONTinuous`` calculates reference levels on every acquisition.
    """


class MeasurementReflevelsMethod(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevels:METHod`` command.

    Description:
        - This command sets or queries the method used to calculate reference levels for the
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:METHod?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevels:METHod?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:REFLevels:METHod value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevels:METHod {PERCent|ABSolute}
        - MEASUrement:REFLevels:METHod?
        ```

    Info:
        - ``PERCent`` specifies that the reference levels are calculated as a percent relative to
          HIGH and LOW. The percentages are defined using the
          ``MEASUrement:REFLevels:REFLevel:PERCent`` commands.
        - ``ABSolute`` specifies that the reference levels are set explicitly using the
          ``MEASUrement:REFLevels:REFLevel:ABSolute`` commands. This method is useful when precise
          values are required.
    """


class MeasurementReflevelsBasetop(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevels:BASETop`` command.

    Description:
        - This command sets or queries the method used to calculate the TOP and BASE, used to
          calculate reference levels for the measurement.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:BASETop?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevels:BASETop?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:REFLevels:BASETop value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevels:BASETop {AUTO|MINMax|MEANhistogram|MODEhistogram|EYEhistogram}
        - MEASUrement:REFLevels:BASETop?
        ```

    Info:
        - ``AUTO`` sets the base top method to AUTO.
        - ``MINMax`` sets the base top method to MINMax.
        - ``MEANhistogram`` sets the base top method to MEANhistogram.
        - ``MODEhistogram`` sets the base top method to MODEhistogram.
        - ``EYEhistogram`` sets the base top method to EYEhistogram.
    """


class MeasurementReflevelsAbsoluteType(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevels:ABSolute:TYPE`` command.

    Description:
        - This command sets or queries the reference level type for the measurement.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:ABSolute:TYPE?``
          query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevels:ABSolute:TYPE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REFLevels:ABSolute:TYPE value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevels:ABSolute:TYPE {SAME|UNIQue}
        - MEASUrement:REFLevels:ABSolute:TYPE?
        ```

    Info:
        - ``SAME`` specifies that the absolute levels are set the same.
        - ``UNIQue`` specifies that the absolute levels can be set independently.
    """


class MeasurementReflevelsAbsoluteRisemid(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevels:ABSolute:RISEMid`` command.

    Description:
        - This command sets or queries the value used as the mid reference level of the rising edge
          when the measurement's ref level method is set to absolute.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:ABSolute:RISEMid?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REFLevels:ABSolute:RISEMid?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REFLevels:ABSolute:RISEMid value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevels:ABSolute:RISEMid <NR3>
        - MEASUrement:REFLevels:ABSolute:RISEMid?
        ```

    Info:
        - ``<NR3>`` is the mid reference level of the rising edge.
    """


class MeasurementReflevelsAbsoluteRiselow(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevels:ABSolute:RISELow`` command.

    Description:
        - This command sets or queries the value used as the low reference level of the rising edge
          when the measurement's ref level method is set to absolute.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:ABSolute:RISELow?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REFLevels:ABSolute:RISELow?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REFLevels:ABSolute:RISELow value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevels:ABSolute:RISELow <NR3>
        - MEASUrement:REFLevels:ABSolute:RISELow?
        ```

    Info:
        - ``<NR3>`` is the value used as the the low reference level of the rising edge.
    """


class MeasurementReflevelsAbsoluteRisehigh(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevels:ABSolute:RISEHigh`` command.

    Description:
        - This command sets or queries the value used as the high reference level of the rising edge
          when the measurement's ref level method is set to absolute.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:ABSolute:RISEHigh?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REFLevels:ABSolute:RISEHigh?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REFLevels:ABSolute:RISEHigh value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevels:ABSolute:RISEHigh <NR3>
        - MEASUrement:REFLevels:ABSolute:RISEHigh?
        ```

    Info:
        - ``<NR3>`` is the value used as the high reference level of the rising edge.
    """


class MeasurementReflevelsAbsoluteHysteresis(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevels:ABSolute:HYSTeresis`` command.

    Description:
        - This command sets or queries the value of the hysteresis of the reference level when the
          measurement's ref level method is set to absolute.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:ABSolute:HYSTeresis?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REFLevels:ABSolute:HYSTeresis?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REFLevels:ABSolute:HYSTeresis value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevels:ABSolute:HYSTeresis <NR3>
        - MEASUrement:REFLevels:ABSolute:HYSTeresis?
        ```

    Info:
        - ``<NR3>`` is the value of the hysteresis of the reference level.
    """


class MeasurementReflevelsAbsoluteFallmid(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevels:ABSolute:FALLMid`` command.

    Description:
        - This command sets or queries the value used as the mid reference level of the falling edge
          when the measurement's ref level method is set to absolute.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:ABSolute:FALLMid?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REFLevels:ABSolute:FALLMid?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REFLevels:ABSolute:FALLMid value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevels:ABSolute:FALLMid <NR3>
        - MEASUrement:REFLevels:ABSolute:FALLMid?
        ```

    Info:
        - ``<NR3>`` is the value used as the mid reference level of the falling edge.
    """


class MeasurementReflevelsAbsoluteFalllow(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevels:ABSolute:FALLLow`` command.

    Description:
        - This command sets or queries the value used as the low reference level of the falling edge
          when the measurement's ref level method is set to absolute.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:ABSolute:FALLLow?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REFLevels:ABSolute:FALLLow?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REFLevels:ABSolute:FALLLow value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevels:ABSolute:FALLLow <NR3>
        - MEASUrement:REFLevels:ABSolute:FALLLow?
        ```

    Info:
        - ``<NR3>`` is the value used as the low reference level of the falling edge.
    """


class MeasurementReflevelsAbsoluteFallhigh(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevels:ABSolute:FALLHigh`` command.

    Description:
        - This command sets or queries the value used as the high reference level of the falling
          edge when the measurement's ref level method is set to absolute.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:ABSolute:FALLHigh?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REFLevels:ABSolute:FALLHigh?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REFLevels:ABSolute:FALLHigh value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevels:ABSolute:FALLHigh <NR3>
        - MEASUrement:REFLevels:ABSolute:FALLHigh?
        ```

    Info:
        - ``<NR3>`` is the value used as the high reference level of the falling edge when the
          measurement's ref level method is set to absolute.
    """


#  pylint: disable=too-many-instance-attributes
class MeasurementReflevelsAbsolute(SCPICmdRead):
    """The ``MEASUrement:REFLevels:ABSolute`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:ABSolute?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevels:ABSolute?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.fallhigh``: The ``MEASUrement:REFLevels:ABSolute:FALLHigh`` command.
        - ``.falllow``: The ``MEASUrement:REFLevels:ABSolute:FALLLow`` command.
        - ``.fallmid``: The ``MEASUrement:REFLevels:ABSolute:FALLMid`` command.
        - ``.hysteresis``: The ``MEASUrement:REFLevels:ABSolute:HYSTeresis`` command.
        - ``.risehigh``: The ``MEASUrement:REFLevels:ABSolute:RISEHigh`` command.
        - ``.riselow``: The ``MEASUrement:REFLevels:ABSolute:RISELow`` command.
        - ``.risemid``: The ``MEASUrement:REFLevels:ABSolute:RISEMid`` command.
        - ``.type``: The ``MEASUrement:REFLevels:ABSolute:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fallhigh = MeasurementReflevelsAbsoluteFallhigh(
            device, f"{self._cmd_syntax}:FALLHigh"
        )
        self._falllow = MeasurementReflevelsAbsoluteFalllow(device, f"{self._cmd_syntax}:FALLLow")
        self._fallmid = MeasurementReflevelsAbsoluteFallmid(device, f"{self._cmd_syntax}:FALLMid")
        self._hysteresis = MeasurementReflevelsAbsoluteHysteresis(
            device, f"{self._cmd_syntax}:HYSTeresis"
        )
        self._risehigh = MeasurementReflevelsAbsoluteRisehigh(
            device, f"{self._cmd_syntax}:RISEHigh"
        )
        self._riselow = MeasurementReflevelsAbsoluteRiselow(device, f"{self._cmd_syntax}:RISELow")
        self._risemid = MeasurementReflevelsAbsoluteRisemid(device, f"{self._cmd_syntax}:RISEMid")
        self._type = MeasurementReflevelsAbsoluteType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def fallhigh(self) -> MeasurementReflevelsAbsoluteFallhigh:
        """Return the ``MEASUrement:REFLevels:ABSolute:FALLHigh`` command.

        Description:
            - This command sets or queries the value used as the high reference level of the falling
              edge when the measurement's ref level method is set to absolute.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:REFLevels:ABSolute:FALLHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REFLevels:ABSolute:FALLHigh?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevels:ABSolute:FALLHigh value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevels:ABSolute:FALLHigh <NR3>
            - MEASUrement:REFLevels:ABSolute:FALLHigh?
            ```

        Info:
            - ``<NR3>`` is the value used as the high reference level of the falling edge when the
              measurement's ref level method is set to absolute.
        """
        return self._fallhigh

    @property
    def falllow(self) -> MeasurementReflevelsAbsoluteFalllow:
        """Return the ``MEASUrement:REFLevels:ABSolute:FALLLow`` command.

        Description:
            - This command sets or queries the value used as the low reference level of the falling
              edge when the measurement's ref level method is set to absolute.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:REFLevels:ABSolute:FALLLow?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REFLevels:ABSolute:FALLLow?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevels:ABSolute:FALLLow value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevels:ABSolute:FALLLow <NR3>
            - MEASUrement:REFLevels:ABSolute:FALLLow?
            ```

        Info:
            - ``<NR3>`` is the value used as the low reference level of the falling edge.
        """
        return self._falllow

    @property
    def fallmid(self) -> MeasurementReflevelsAbsoluteFallmid:
        """Return the ``MEASUrement:REFLevels:ABSolute:FALLMid`` command.

        Description:
            - This command sets or queries the value used as the mid reference level of the falling
              edge when the measurement's ref level method is set to absolute.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:REFLevels:ABSolute:FALLMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REFLevels:ABSolute:FALLMid?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevels:ABSolute:FALLMid value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevels:ABSolute:FALLMid <NR3>
            - MEASUrement:REFLevels:ABSolute:FALLMid?
            ```

        Info:
            - ``<NR3>`` is the value used as the mid reference level of the falling edge.
        """
        return self._fallmid

    @property
    def hysteresis(self) -> MeasurementReflevelsAbsoluteHysteresis:
        """Return the ``MEASUrement:REFLevels:ABSolute:HYSTeresis`` command.

        Description:
            - This command sets or queries the value of the hysteresis of the reference level when
              the measurement's ref level method is set to absolute.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:REFLevels:ABSolute:HYSTeresis?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REFLevels:ABSolute:HYSTeresis?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevels:ABSolute:HYSTeresis value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevels:ABSolute:HYSTeresis <NR3>
            - MEASUrement:REFLevels:ABSolute:HYSTeresis?
            ```

        Info:
            - ``<NR3>`` is the value of the hysteresis of the reference level.
        """
        return self._hysteresis

    @property
    def risehigh(self) -> MeasurementReflevelsAbsoluteRisehigh:
        """Return the ``MEASUrement:REFLevels:ABSolute:RISEHigh`` command.

        Description:
            - This command sets or queries the value used as the high reference level of the rising
              edge when the measurement's ref level method is set to absolute.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:REFLevels:ABSolute:RISEHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REFLevels:ABSolute:RISEHigh?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevels:ABSolute:RISEHigh value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevels:ABSolute:RISEHigh <NR3>
            - MEASUrement:REFLevels:ABSolute:RISEHigh?
            ```

        Info:
            - ``<NR3>`` is the value used as the high reference level of the rising edge.
        """
        return self._risehigh

    @property
    def riselow(self) -> MeasurementReflevelsAbsoluteRiselow:
        """Return the ``MEASUrement:REFLevels:ABSolute:RISELow`` command.

        Description:
            - This command sets or queries the value used as the low reference level of the rising
              edge when the measurement's ref level method is set to absolute.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:REFLevels:ABSolute:RISELow?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REFLevels:ABSolute:RISELow?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevels:ABSolute:RISELow value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevels:ABSolute:RISELow <NR3>
            - MEASUrement:REFLevels:ABSolute:RISELow?
            ```

        Info:
            - ``<NR3>`` is the value used as the the low reference level of the rising edge.
        """
        return self._riselow

    @property
    def risemid(self) -> MeasurementReflevelsAbsoluteRisemid:
        """Return the ``MEASUrement:REFLevels:ABSolute:RISEMid`` command.

        Description:
            - This command sets or queries the value used as the mid reference level of the rising
              edge when the measurement's ref level method is set to absolute.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:REFLevels:ABSolute:RISEMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REFLevels:ABSolute:RISEMid?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevels:ABSolute:RISEMid value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevels:ABSolute:RISEMid <NR3>
            - MEASUrement:REFLevels:ABSolute:RISEMid?
            ```

        Info:
            - ``<NR3>`` is the mid reference level of the rising edge.
        """
        return self._risemid

    @property
    def type(self) -> MeasurementReflevelsAbsoluteType:
        """Return the ``MEASUrement:REFLevels:ABSolute:TYPE`` command.

        Description:
            - This command sets or queries the reference level type for the measurement.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:ABSolute:TYPE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REFLevels:ABSolute:TYPE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevels:ABSolute:TYPE value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevels:ABSolute:TYPE {SAME|UNIQue}
            - MEASUrement:REFLevels:ABSolute:TYPE?
            ```

        Info:
            - ``SAME`` specifies that the absolute levels are set the same.
            - ``UNIQue`` specifies that the absolute levels can be set independently.
        """
        return self._type


class MeasurementReflevels(SCPICmdRead):
    """The ``MEASUrement:REFLevels`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevels?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevels?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.absolute``: The ``MEASUrement:REFLevels:ABSolute`` command tree.
        - ``.basetop``: The ``MEASUrement:REFLevels:BASETop`` command.
        - ``.method``: The ``MEASUrement:REFLevels:METHod`` command.
        - ``.mode``: The ``MEASUrement:REFLevels:MODE`` command.
        - ``.percent``: The ``MEASUrement:REFLevels:PERCent`` command tree.
        - ``.type``: The ``MEASUrement:REFLevels:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._absolute = MeasurementReflevelsAbsolute(device, f"{self._cmd_syntax}:ABSolute")
        self._basetop = MeasurementReflevelsBasetop(device, f"{self._cmd_syntax}:BASETop")
        self._method = MeasurementReflevelsMethod(device, f"{self._cmd_syntax}:METHod")
        self._mode = MeasurementReflevelsMode(device, f"{self._cmd_syntax}:MODE")
        self._percent = MeasurementReflevelsPercent(device, f"{self._cmd_syntax}:PERCent")
        self._type = MeasurementReflevelsType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def absolute(self) -> MeasurementReflevelsAbsolute:
        """Return the ``MEASUrement:REFLevels:ABSolute`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:ABSolute?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevels:ABSolute?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.fallhigh``: The ``MEASUrement:REFLevels:ABSolute:FALLHigh`` command.
            - ``.falllow``: The ``MEASUrement:REFLevels:ABSolute:FALLLow`` command.
            - ``.fallmid``: The ``MEASUrement:REFLevels:ABSolute:FALLMid`` command.
            - ``.hysteresis``: The ``MEASUrement:REFLevels:ABSolute:HYSTeresis`` command.
            - ``.risehigh``: The ``MEASUrement:REFLevels:ABSolute:RISEHigh`` command.
            - ``.riselow``: The ``MEASUrement:REFLevels:ABSolute:RISELow`` command.
            - ``.risemid``: The ``MEASUrement:REFLevels:ABSolute:RISEMid`` command.
            - ``.type``: The ``MEASUrement:REFLevels:ABSolute:TYPE`` command.
        """
        return self._absolute

    @property
    def basetop(self) -> MeasurementReflevelsBasetop:
        """Return the ``MEASUrement:REFLevels:BASETop`` command.

        Description:
            - This command sets or queries the method used to calculate the TOP and BASE, used to
              calculate reference levels for the measurement.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:BASETop?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevels:BASETop?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevels:BASETop value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevels:BASETop {AUTO|MINMax|MEANhistogram|MODEhistogram|EYEhistogram}
            - MEASUrement:REFLevels:BASETop?
            ```

        Info:
            - ``AUTO`` sets the base top method to AUTO.
            - ``MINMax`` sets the base top method to MINMax.
            - ``MEANhistogram`` sets the base top method to MEANhistogram.
            - ``MODEhistogram`` sets the base top method to MODEhistogram.
            - ``EYEhistogram`` sets the base top method to EYEhistogram.
        """
        return self._basetop

    @property
    def method(self) -> MeasurementReflevelsMethod:
        """Return the ``MEASUrement:REFLevels:METHod`` command.

        Description:
            - This command sets or queries the method used to calculate reference levels for the
              measurement.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:METHod?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevels:METHod?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevels:METHod value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevels:METHod {PERCent|ABSolute}
            - MEASUrement:REFLevels:METHod?
            ```

        Info:
            - ``PERCent`` specifies that the reference levels are calculated as a percent relative
              to HIGH and LOW. The percentages are defined using the
              ``MEASUrement:REFLevels:REFLevel:PERCent`` commands.
            - ``ABSolute`` specifies that the reference levels are set explicitly using the
              ``MEASUrement:REFLevels:REFLevel:ABSolute`` commands. This method is useful when
              precise values are required.
        """
        return self._method

    @property
    def mode(self) -> MeasurementReflevelsMode:
        """Return the ``MEASUrement:REFLevels:MODE`` command.

        Description:
            - This command sets or queries how often reference levels are calculated.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:MODE?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevels:MODE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:REFLevels:MODE value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevels:MODE {LATCh|CONTinuous}
            - MEASUrement:REFLevels:MODE?
            ```

        Info:
            - ``LATCh`` calculates reference levels only on the first acquisition after a statistics
              reset.
            - ``CONTinuous`` calculates reference levels on every acquisition.
        """
        return self._mode

    @property
    def percent(self) -> MeasurementReflevelsPercent:
        """Return the ``MEASUrement:REFLevels:PERCent`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:PERCent?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevels:PERCent?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.fallhigh``: The ``MEASUrement:REFLevels:PERCent:FALLHigh`` command.
            - ``.falllow``: The ``MEASUrement:REFLevels:PERCent:FALLLow`` command.
            - ``.fallmid``: The ``MEASUrement:REFLevels:PERCent:FALLMid`` command.
            - ``.hysteresis``: The ``MEASUrement:REFLevels:PERCent:HYSTeresis`` command.
            - ``.risehigh``: The ``MEASUrement:REFLevels:PERCent:RISEHigh`` command.
            - ``.riselow``: The ``MEASUrement:REFLevels:PERCent:RISELow`` command.
            - ``.risemid``: The ``MEASUrement:REFLevels:PERCent:RISEMid`` command.
            - ``.type``: The ``MEASUrement:REFLevels:PERCent:TYPE`` command.
        """
        return self._percent

    @property
    def type(self) -> MeasurementReflevelsType:
        """Return the ``MEASUrement:REFLevels:TYPE`` command.

        Description:
            - This command sets or queries the shared reference level method used for sources of
              measurement calculations.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevels:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevels:TYPE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:REFLevels:TYPE value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevels:TYPE {GLOBal|PERSource}
            - MEASUrement:REFLevels:TYPE?
            ```

        Info:
            - ``GLOBal`` shares reference levels across measurements.
            - ``PERSource`` causes reference levels to be used on individual measurements.
        """
        return self._type


class MeasurementRefItemReflevelsPercentType(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REF<x>:REFLevels:PERCent:TYPE`` command.

    Description:
        - This command sets or queries the reference level percent type for the measurement.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REF<x>:REFLevels:PERCent:TYPE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:PERCent:TYPE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:PERCent:TYPE value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REF<x>:REFLevels:PERCent:TYPE {TENNinety|TWENtyeighty|CUSTom}
        - MEASUrement:REF<x>:REFLevels:PERCent:TYPE?
        ```

    Info:
        - ``TENNinety`` sets the values for Low, Mid and High Ref to 10%, 50% and 90% respectively.
        - ``TWENtyeighty`` sets the values for Low, Mid and High Ref are set to 20%, 50% and 80%
          respectively.
        - ``CUSTom`` allows setting other reference level percents.
    """


class MeasurementRefItemReflevelsPercentRisemid(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REF<x>:REFLevels:PERCent:RISEMid`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the mid reference level of the rising edge when the measurement's
          ref level method is set to percent.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:REF<x>:REFLevels:PERCent:RISEMid?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:PERCent:RISEMid?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:PERCent:RISEMid value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REF<x>:REFLevels:PERCent:RISEMid <NR3>
        - MEASUrement:REF<x>:REFLevels:PERCent:RISEMid?
        ```

    Info:
        - ``<NR3>`` is the percentage used to calculate the mid reference level of the rising edge.
    """


class MeasurementRefItemReflevelsPercentRiselow(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REF<x>:REFLevels:PERCent:RISELow`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the low reference level of the rising edge when the measurement's
          ref level method is set to percent.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:REF<x>:REFLevels:PERCent:RISELow?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:PERCent:RISELow?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:PERCent:RISELow value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REF<x>:REFLevels:PERCent:RISELow <NR3>
        - MEASUrement:REF<x>:REFLevels:PERCent:RISELow?
        ```

    Info:
        - ``<NR3>`` is the percentage used to calculate the low reference level of the rising edge.
    """


class MeasurementRefItemReflevelsPercentRisehigh(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REF<x>:REFLevels:PERCent:RISEHigh`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the high reference level of the rising edge when the measurement's
          ref level method is set to percent.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:REF<x>:REFLevels:PERCent:RISEHigh?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:PERCent:RISEHigh?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:PERCent:RISEHigh value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REF<x>:REFLevels:PERCent:RISEHigh <NR3>
        - MEASUrement:REF<x>:REFLevels:PERCent:RISEHigh?
        ```

    Info:
        - ``<NR3>`` is the percentage used to calculate the high reference level of the rising edge.
    """


class MeasurementRefItemReflevelsPercentHysteresis(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REF<x>:REFLevels:PERCent:HYSTeresis`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to MAX and 1% is equal to
          MIN) used to calculate the hysteresis of the reference level when the measurement's ref
          level method is set to percent.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:REF<x>:REFLevels:PERCent:HYSTeresis?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:PERCent:HYSTeresis?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:PERCent:HYSTeresis value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REF<x>:REFLevels:PERCent:HYSTeresis <NR3>
        - MEASUrement:REF<x>:REFLevels:PERCent:HYSTeresis?
        ```

    Info:
        - ``<NR3>`` is the percentage used to calculate the hysteresis of the reference level.
    """


class MeasurementRefItemReflevelsPercentFallmid(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REF<x>:REFLevels:PERCent:FALLMid`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the mid reference level of the falling edge when the measurement's
          ref level method is set to percent.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:REF<x>:REFLevels:PERCent:FALLMid?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:PERCent:FALLMid?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:PERCent:FALLMid value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REF<x>:REFLevels:PERCent:FALLMid <NR3>
        - MEASUrement:REF<x>:REFLevels:PERCent:FALLMid?
        ```

    Info:
        - ``<NR3>`` is the percentage used to calculate the mid reference level of the falling edge.
    """


class MeasurementRefItemReflevelsPercentFalllow(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REF<x>:REFLevels:PERCent:FALLLow`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the low reference level of the falling edge when the measurement's
          ref level method is set to percent.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:REF<x>:REFLevels:PERCent:FALLLow?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:PERCent:FALLLow?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:PERCent:FALLLow value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REF<x>:REFLevels:PERCent:FALLLow <NR3>
        - MEASUrement:REF<x>:REFLevels:PERCent:FALLLow?
        ```

    Info:
        - ``<NR3>`` is the percentage used to calculate the low reference level.
    """


class MeasurementRefItemReflevelsPercentFallhigh(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REF<x>:REFLevels:PERCent:FALLHigh`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the high reference level of the falling edge when the
          measurement's ref level method is set to percent.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:REF<x>:REFLevels:PERCent:FALLHigh?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:PERCent:FALLHigh?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:PERCent:FALLHigh value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REF<x>:REFLevels:PERCent:FALLHigh <NR3>
        - MEASUrement:REF<x>:REFLevels:PERCent:FALLHigh?
        ```

    Info:
        - ``<NR3>`` is the percentage used to calculate the high reference level of the falling
          edge.
    """


#  pylint: disable=too-many-instance-attributes
class MeasurementRefItemReflevelsPercent(SCPICmdRead):
    """The ``MEASUrement:REF<x>:REFLevels:PERCent`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REF<x>:REFLevels:PERCent?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:PERCent?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.fallhigh``: The ``MEASUrement:REF<x>:REFLevels:PERCent:FALLHigh`` command.
        - ``.falllow``: The ``MEASUrement:REF<x>:REFLevels:PERCent:FALLLow`` command.
        - ``.fallmid``: The ``MEASUrement:REF<x>:REFLevels:PERCent:FALLMid`` command.
        - ``.hysteresis``: The ``MEASUrement:REF<x>:REFLevels:PERCent:HYSTeresis`` command.
        - ``.risehigh``: The ``MEASUrement:REF<x>:REFLevels:PERCent:RISEHigh`` command.
        - ``.riselow``: The ``MEASUrement:REF<x>:REFLevels:PERCent:RISELow`` command.
        - ``.risemid``: The ``MEASUrement:REF<x>:REFLevels:PERCent:RISEMid`` command.
        - ``.type``: The ``MEASUrement:REF<x>:REFLevels:PERCent:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fallhigh = MeasurementRefItemReflevelsPercentFallhigh(
            device, f"{self._cmd_syntax}:FALLHigh"
        )
        self._falllow = MeasurementRefItemReflevelsPercentFalllow(
            device, f"{self._cmd_syntax}:FALLLow"
        )
        self._fallmid = MeasurementRefItemReflevelsPercentFallmid(
            device, f"{self._cmd_syntax}:FALLMid"
        )
        self._hysteresis = MeasurementRefItemReflevelsPercentHysteresis(
            device, f"{self._cmd_syntax}:HYSTeresis"
        )
        self._risehigh = MeasurementRefItemReflevelsPercentRisehigh(
            device, f"{self._cmd_syntax}:RISEHigh"
        )
        self._riselow = MeasurementRefItemReflevelsPercentRiselow(
            device, f"{self._cmd_syntax}:RISELow"
        )
        self._risemid = MeasurementRefItemReflevelsPercentRisemid(
            device, f"{self._cmd_syntax}:RISEMid"
        )
        self._type = MeasurementRefItemReflevelsPercentType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def fallhigh(self) -> MeasurementRefItemReflevelsPercentFallhigh:
        """Return the ``MEASUrement:REF<x>:REFLevels:PERCent:FALLHigh`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the high reference level of the falling edge when the
              measurement's ref level method is set to percent.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:REF<x>:REFLevels:PERCent:FALLHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:PERCent:FALLHigh?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:PERCent:FALLHigh value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REF<x>:REFLevels:PERCent:FALLHigh <NR3>
            - MEASUrement:REF<x>:REFLevels:PERCent:FALLHigh?
            ```

        Info:
            - ``<NR3>`` is the percentage used to calculate the high reference level of the falling
              edge.
        """
        return self._fallhigh

    @property
    def falllow(self) -> MeasurementRefItemReflevelsPercentFalllow:
        """Return the ``MEASUrement:REF<x>:REFLevels:PERCent:FALLLow`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the low reference level of the falling edge when the
              measurement's ref level method is set to percent.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:REF<x>:REFLevels:PERCent:FALLLow?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:PERCent:FALLLow?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:PERCent:FALLLow value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REF<x>:REFLevels:PERCent:FALLLow <NR3>
            - MEASUrement:REF<x>:REFLevels:PERCent:FALLLow?
            ```

        Info:
            - ``<NR3>`` is the percentage used to calculate the low reference level.
        """
        return self._falllow

    @property
    def fallmid(self) -> MeasurementRefItemReflevelsPercentFallmid:
        """Return the ``MEASUrement:REF<x>:REFLevels:PERCent:FALLMid`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the mid reference level of the falling edge when the
              measurement's ref level method is set to percent.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:REF<x>:REFLevels:PERCent:FALLMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:PERCent:FALLMid?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:PERCent:FALLMid value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REF<x>:REFLevels:PERCent:FALLMid <NR3>
            - MEASUrement:REF<x>:REFLevels:PERCent:FALLMid?
            ```

        Info:
            - ``<NR3>`` is the percentage used to calculate the mid reference level of the falling
              edge.
        """
        return self._fallmid

    @property
    def hysteresis(self) -> MeasurementRefItemReflevelsPercentHysteresis:
        """Return the ``MEASUrement:REF<x>:REFLevels:PERCent:HYSTeresis`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to MAX and 1% is equal
              to MIN) used to calculate the hysteresis of the reference level when the measurement's
              ref level method is set to percent.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:REF<x>:REFLevels:PERCent:HYSTeresis?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:PERCent:HYSTeresis?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:PERCent:HYSTeresis value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REF<x>:REFLevels:PERCent:HYSTeresis <NR3>
            - MEASUrement:REF<x>:REFLevels:PERCent:HYSTeresis?
            ```

        Info:
            - ``<NR3>`` is the percentage used to calculate the hysteresis of the reference level.
        """
        return self._hysteresis

    @property
    def risehigh(self) -> MeasurementRefItemReflevelsPercentRisehigh:
        """Return the ``MEASUrement:REF<x>:REFLevels:PERCent:RISEHigh`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the high reference level of the rising edge when the
              measurement's ref level method is set to percent.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:REF<x>:REFLevels:PERCent:RISEHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:PERCent:RISEHigh?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:PERCent:RISEHigh value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REF<x>:REFLevels:PERCent:RISEHigh <NR3>
            - MEASUrement:REF<x>:REFLevels:PERCent:RISEHigh?
            ```

        Info:
            - ``<NR3>`` is the percentage used to calculate the high reference level of the rising
              edge.
        """
        return self._risehigh

    @property
    def riselow(self) -> MeasurementRefItemReflevelsPercentRiselow:
        """Return the ``MEASUrement:REF<x>:REFLevels:PERCent:RISELow`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the low reference level of the rising edge when the
              measurement's ref level method is set to percent.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:REF<x>:REFLevels:PERCent:RISELow?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:PERCent:RISELow?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:PERCent:RISELow value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REF<x>:REFLevels:PERCent:RISELow <NR3>
            - MEASUrement:REF<x>:REFLevels:PERCent:RISELow?
            ```

        Info:
            - ``<NR3>`` is the percentage used to calculate the low reference level of the rising
              edge.
        """
        return self._riselow

    @property
    def risemid(self) -> MeasurementRefItemReflevelsPercentRisemid:
        """Return the ``MEASUrement:REF<x>:REFLevels:PERCent:RISEMid`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the mid reference level of the rising edge when the
              measurement's ref level method is set to percent.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:REF<x>:REFLevels:PERCent:RISEMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:PERCent:RISEMid?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:PERCent:RISEMid value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REF<x>:REFLevels:PERCent:RISEMid <NR3>
            - MEASUrement:REF<x>:REFLevels:PERCent:RISEMid?
            ```

        Info:
            - ``<NR3>`` is the percentage used to calculate the mid reference level of the rising
              edge.
        """
        return self._risemid

    @property
    def type(self) -> MeasurementRefItemReflevelsPercentType:
        """Return the ``MEASUrement:REF<x>:REFLevels:PERCent:TYPE`` command.

        Description:
            - This command sets or queries the reference level percent type for the measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:REF<x>:REFLevels:PERCent:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:PERCent:TYPE?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:PERCent:TYPE value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REF<x>:REFLevels:PERCent:TYPE {TENNinety|TWENtyeighty|CUSTom}
            - MEASUrement:REF<x>:REFLevels:PERCent:TYPE?
            ```

        Info:
            - ``TENNinety`` sets the values for Low, Mid and High Ref to 10%, 50% and 90%
              respectively.
            - ``TWENtyeighty`` sets the values for Low, Mid and High Ref are set to 20%, 50% and 80%
              respectively.
            - ``CUSTom`` allows setting other reference level percents.
        """
        return self._type


class MeasurementRefItemReflevelsMethod(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REF<x>:REFLevels:METHod`` command.

    Description:
        - This command sets or queries the method used to calculate reference levels for the
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REF<x>:REFLevels:METHod?``
          query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:REF<x>:REFLevels:METHod?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:METHod value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REF<x>:REFLevels:METHod {PERCent|ABSolute}
        - MEASUrement:REF<x>:REFLevels:METHod?
        ```

    Info:
        - ``PERCent`` specifies that the reference levels are calculated as a percent relative to
          HIGH and LOW. The percentages are defined using the
          ``MEASUrement:REF<x>:REFLevel:PERCent`` commands.
        - ``ABSolute`` specifies that the reference levels are set explicitly using the
          ``MEASUrement:REF<x>:REFLevel:ABSolute`` commands. This method is useful when precise
          values are required.
    """


class MeasurementRefItemReflevelsBasetop(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REF<x>:REFLevels:BASETop`` command.

    Description:
        - This command sets or queries the method used to calculate the TOP and BASE, used to
          calculate reference levels for the measurement.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REF<x>:REFLevels:BASETop?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:BASETop?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:BASETop value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REF<x>:REFLevels:BASETop {AUTO|MINMax|MEANhistogram|MODEhistogram|EYEhistogram}
        - MEASUrement:REF<x>:REFLevels:BASETop?
        ```

    Info:
        - ``AUTO`` automatically chooses a reference level method.
        - ``MINMax`` specifies that reference levels are relative to the measurement MIN and MAX.
        - ``MEANhistogram`` specifies that reference levels are relative to the histogram mean BASE
          and TOP.
        - ``MODEhistogram`` specifies that reference levels are relative to the histogram mode BASE
          and TOP.
        - ``EYEhistogram`` specifies that reverence levels are relative to the eye histogram BASE
          and TOP.
    """  # noqa: E501


class MeasurementRefItemReflevelsAbsoluteType(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REF<x>:REFLevels:ABSolute:TYPE`` command.

    Description:
        - This command sets or queries the reference level type for the measurement.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:REF<x>:REFLevels:ABSolute:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:ABSolute:TYPE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:ABSolute:TYPE value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REF<x>:REFLevels:ABSolute:TYPE {SAME|UNIQue}
        - MEASUrement:REF<x>:REFLevels:ABSolute:TYPE?
        ```

    Info:
        - ``SAME`` specifies that the absolute levels are set the same.
        - ``UNIQue`` specifies that the absolute levels can be set independently.
    """


class MeasurementRefItemReflevelsAbsoluteRisemid(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REF<x>:REFLevels:ABSolute:RISEMid`` command.

    Description:
        - This command sets or queries the value used as the mid reference level of the rising edge
          when the measurement's ref level method is set to absolute.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:REF<x>:REFLevels:ABSolute:RISEMid?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:ABSolute:RISEMid?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:ABSolute:RISEMid value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REF<x>:REFLevels:ABSolute:RISEMid <NR3>
        - MEASUrement:REF<x>:REFLevels:ABSolute:RISEMid?
        ```

    Info:
        - ``<NR3>`` is the value used as the mid reference level of the rising edge when the
          measurement's ref level method is set to absolute.
    """


class MeasurementRefItemReflevelsAbsoluteRiselow(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REF<x>:REFLevels:ABSolute:RISELow`` command.

    Description:
        - This command sets or queries the value used as the low reference level of the rising edge
          when the measurement's ref level method is set to absolute.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:REF<x>:REFLevels:ABSolute:RISELow?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:ABSolute:RISELow?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:ABSolute:RISELow value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REF<x>:REFLevels:ABSolute:RISELow <NR3>
        - MEASUrement:REF<x>:REFLevels:ABSolute:RISELow?
        ```

    Info:
        - ``<NR3>`` is the value used as the low reference level of the rising edge when the
          measurement's ref level method is set to absolute.
    """


class MeasurementRefItemReflevelsAbsoluteRisehigh(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REF<x>:REFLevels:ABSolute:RISEHigh`` command.

    Description:
        - This command sets or queries the value used as the high reference level of the rising edge
          when the measurement's ref level method is set to absolute.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:REF<x>:REFLevels:ABSolute:RISEHigh?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:ABSolute:RISEHigh?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:ABSolute:RISEHigh value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REF<x>:REFLevels:ABSolute:RISEHigh <NR3>
        - MEASUrement:REF<x>:REFLevels:ABSolute:RISEHigh?
        ```

    Info:
        - ``<NR3>`` is the value used as the high reference level of the rising edge when the
          measurement's ref level method is set to absolute.
    """


class MeasurementRefItemReflevelsAbsoluteHysteresis(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REF<x>:REFLevels:ABSolute:HYSTeresis`` command.

    Description:
        - This command sets or queries the value of the hysteresis of the reference level when the
          measurement's ref level method is set to absolute.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:REF<x>:REFLevels:ABSolute:HYSTeresis?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:ABSolute:HYSTeresis?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:ABSolute:HYSTeresis value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REF<x>:REFLevels:ABSolute:HYSTeresis <NR3>
        - MEASUrement:REF<x>:REFLevels:ABSolute:HYSTeresis?
        ```

    Info:
        - ``<NR3>`` is the value of the hysteresis of the reference level when the measurement's ref
          level method is set to absolute.
    """


class MeasurementRefItemReflevelsAbsoluteFallmid(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLMid`` command.

    Description:
        - This command sets or queries the value used as the mid reference level of the falling edge
          when the measurement's ref level method is set to absolute.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLMid?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLMid?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLMid value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REF<x>:REFLevels:ABSolute:FALLMid <NR3>
        - MEASUrement:REF<x>:REFLevels:ABSolute:FALLMid?
        ```

    Info:
        - ``<NR3>`` is the value used as the mid reference level of the falling edge when the
          measurement's ref level method is set to absolute.
    """


class MeasurementRefItemReflevelsAbsoluteFalllow(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLLow`` command.

    Description:
        - This command sets or queries the value used as the low reference level of the falling edge
          when the measurement's ref level method is set to absolute.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLLow?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLLow?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLLow value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REF<x>:REFLevels:ABSolute:FALLLow <NR3>
        - MEASUrement:REF<x>:REFLevels:ABSolute:FALLLow?
        ```

    Info:
        - ``<NR3>`` is the value used as the low reference level of the falling edge when the
          measurement's ref level method is set to absolute.
    """


class MeasurementRefItemReflevelsAbsoluteFallhigh(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLHigh`` command.

    Description:
        - This command sets or queries the value used as the high reference level of the falling
          edge when the measurement's ref level method is set to absolute.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLHigh?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLHigh?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLHigh value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REF<x>:REFLevels:ABSolute:FALLHigh <NR3>
        - MEASUrement:REF<x>:REFLevels:ABSolute:FALLHigh?
        ```

    Info:
        - ``<NR3>`` is the value used as the high reference level of the falling edge when the
          measurement's ref level method is set to absolute.
    """


#  pylint: disable=too-many-instance-attributes
class MeasurementRefItemReflevelsAbsolute(SCPICmdRead):
    """The ``MEASUrement:REF<x>:REFLevels:ABSolute`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REF<x>:REFLevels:ABSolute?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REF<x>:REFLevels:ABSolute?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.fallhigh``: The ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLHigh`` command.
        - ``.falllow``: The ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLLow`` command.
        - ``.fallmid``: The ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLMid`` command.
        - ``.hysteresis``: The ``MEASUrement:REF<x>:REFLevels:ABSolute:HYSTeresis`` command.
        - ``.risehigh``: The ``MEASUrement:REF<x>:REFLevels:ABSolute:RISEHigh`` command.
        - ``.riselow``: The ``MEASUrement:REF<x>:REFLevels:ABSolute:RISELow`` command.
        - ``.risemid``: The ``MEASUrement:REF<x>:REFLevels:ABSolute:RISEMid`` command.
        - ``.type``: The ``MEASUrement:REF<x>:REFLevels:ABSolute:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fallhigh = MeasurementRefItemReflevelsAbsoluteFallhigh(
            device, f"{self._cmd_syntax}:FALLHigh"
        )
        self._falllow = MeasurementRefItemReflevelsAbsoluteFalllow(
            device, f"{self._cmd_syntax}:FALLLow"
        )
        self._fallmid = MeasurementRefItemReflevelsAbsoluteFallmid(
            device, f"{self._cmd_syntax}:FALLMid"
        )
        self._hysteresis = MeasurementRefItemReflevelsAbsoluteHysteresis(
            device, f"{self._cmd_syntax}:HYSTeresis"
        )
        self._risehigh = MeasurementRefItemReflevelsAbsoluteRisehigh(
            device, f"{self._cmd_syntax}:RISEHigh"
        )
        self._riselow = MeasurementRefItemReflevelsAbsoluteRiselow(
            device, f"{self._cmd_syntax}:RISELow"
        )
        self._risemid = MeasurementRefItemReflevelsAbsoluteRisemid(
            device, f"{self._cmd_syntax}:RISEMid"
        )
        self._type = MeasurementRefItemReflevelsAbsoluteType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def fallhigh(self) -> MeasurementRefItemReflevelsAbsoluteFallhigh:
        """Return the ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLHigh`` command.

        Description:
            - This command sets or queries the value used as the high reference level of the falling
              edge when the measurement's ref level method is set to absolute.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLHigh?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLHigh value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REF<x>:REFLevels:ABSolute:FALLHigh <NR3>
            - MEASUrement:REF<x>:REFLevels:ABSolute:FALLHigh?
            ```

        Info:
            - ``<NR3>`` is the value used as the high reference level of the falling edge when the
              measurement's ref level method is set to absolute.
        """
        return self._fallhigh

    @property
    def falllow(self) -> MeasurementRefItemReflevelsAbsoluteFalllow:
        """Return the ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLLow`` command.

        Description:
            - This command sets or queries the value used as the low reference level of the falling
              edge when the measurement's ref level method is set to absolute.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLLow?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLLow?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLLow value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REF<x>:REFLevels:ABSolute:FALLLow <NR3>
            - MEASUrement:REF<x>:REFLevels:ABSolute:FALLLow?
            ```

        Info:
            - ``<NR3>`` is the value used as the low reference level of the falling edge when the
              measurement's ref level method is set to absolute.
        """
        return self._falllow

    @property
    def fallmid(self) -> MeasurementRefItemReflevelsAbsoluteFallmid:
        """Return the ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLMid`` command.

        Description:
            - This command sets or queries the value used as the mid reference level of the falling
              edge when the measurement's ref level method is set to absolute.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLMid?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLMid value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REF<x>:REFLevels:ABSolute:FALLMid <NR3>
            - MEASUrement:REF<x>:REFLevels:ABSolute:FALLMid?
            ```

        Info:
            - ``<NR3>`` is the value used as the mid reference level of the falling edge when the
              measurement's ref level method is set to absolute.
        """
        return self._fallmid

    @property
    def hysteresis(self) -> MeasurementRefItemReflevelsAbsoluteHysteresis:
        """Return the ``MEASUrement:REF<x>:REFLevels:ABSolute:HYSTeresis`` command.

        Description:
            - This command sets or queries the value of the hysteresis of the reference level when
              the measurement's ref level method is set to absolute.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:REF<x>:REFLevels:ABSolute:HYSTeresis?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:ABSolute:HYSTeresis?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:ABSolute:HYSTeresis value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REF<x>:REFLevels:ABSolute:HYSTeresis <NR3>
            - MEASUrement:REF<x>:REFLevels:ABSolute:HYSTeresis?
            ```

        Info:
            - ``<NR3>`` is the value of the hysteresis of the reference level when the measurement's
              ref level method is set to absolute.
        """
        return self._hysteresis

    @property
    def risehigh(self) -> MeasurementRefItemReflevelsAbsoluteRisehigh:
        """Return the ``MEASUrement:REF<x>:REFLevels:ABSolute:RISEHigh`` command.

        Description:
            - This command sets or queries the value used as the high reference level of the rising
              edge when the measurement's ref level method is set to absolute.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:REF<x>:REFLevels:ABSolute:RISEHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:ABSolute:RISEHigh?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:ABSolute:RISEHigh value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REF<x>:REFLevels:ABSolute:RISEHigh <NR3>
            - MEASUrement:REF<x>:REFLevels:ABSolute:RISEHigh?
            ```

        Info:
            - ``<NR3>`` is the value used as the high reference level of the rising edge when the
              measurement's ref level method is set to absolute.
        """
        return self._risehigh

    @property
    def riselow(self) -> MeasurementRefItemReflevelsAbsoluteRiselow:
        """Return the ``MEASUrement:REF<x>:REFLevels:ABSolute:RISELow`` command.

        Description:
            - This command sets or queries the value used as the low reference level of the rising
              edge when the measurement's ref level method is set to absolute.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:REF<x>:REFLevels:ABSolute:RISELow?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:ABSolute:RISELow?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:ABSolute:RISELow value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REF<x>:REFLevels:ABSolute:RISELow <NR3>
            - MEASUrement:REF<x>:REFLevels:ABSolute:RISELow?
            ```

        Info:
            - ``<NR3>`` is the value used as the low reference level of the rising edge when the
              measurement's ref level method is set to absolute.
        """
        return self._riselow

    @property
    def risemid(self) -> MeasurementRefItemReflevelsAbsoluteRisemid:
        """Return the ``MEASUrement:REF<x>:REFLevels:ABSolute:RISEMid`` command.

        Description:
            - This command sets or queries the value used as the mid reference level of the rising
              edge when the measurement's ref level method is set to absolute.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:REF<x>:REFLevels:ABSolute:RISEMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:ABSolute:RISEMid?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:ABSolute:RISEMid value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REF<x>:REFLevels:ABSolute:RISEMid <NR3>
            - MEASUrement:REF<x>:REFLevels:ABSolute:RISEMid?
            ```

        Info:
            - ``<NR3>`` is the value used as the mid reference level of the rising edge when the
              measurement's ref level method is set to absolute.
        """
        return self._risemid

    @property
    def type(self) -> MeasurementRefItemReflevelsAbsoluteType:
        """Return the ``MEASUrement:REF<x>:REFLevels:ABSolute:TYPE`` command.

        Description:
            - This command sets or queries the reference level type for the measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:REF<x>:REFLevels:ABSolute:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:ABSolute:TYPE?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:ABSolute:TYPE value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REF<x>:REFLevels:ABSolute:TYPE {SAME|UNIQue}
            - MEASUrement:REF<x>:REFLevels:ABSolute:TYPE?
            ```

        Info:
            - ``SAME`` specifies that the absolute levels are set the same.
            - ``UNIQue`` specifies that the absolute levels can be set independently.
        """
        return self._type


class MeasurementRefItemReflevels(SCPICmdRead):
    """The ``MEASUrement:REF<x>:REFLevels`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REF<x>:REFLevels?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:REF<x>:REFLevels?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.absolute``: The ``MEASUrement:REF<x>:REFLevels:ABSolute`` command tree.
        - ``.basetop``: The ``MEASUrement:REF<x>:REFLevels:BASETop`` command.
        - ``.method``: The ``MEASUrement:REF<x>:REFLevels:METHod`` command.
        - ``.percent``: The ``MEASUrement:REF<x>:REFLevels:PERCent`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._absolute = MeasurementRefItemReflevelsAbsolute(device, f"{self._cmd_syntax}:ABSolute")
        self._basetop = MeasurementRefItemReflevelsBasetop(device, f"{self._cmd_syntax}:BASETop")
        self._method = MeasurementRefItemReflevelsMethod(device, f"{self._cmd_syntax}:METHod")
        self._percent = MeasurementRefItemReflevelsPercent(device, f"{self._cmd_syntax}:PERCent")

    @property
    def absolute(self) -> MeasurementRefItemReflevelsAbsolute:
        """Return the ``MEASUrement:REF<x>:REFLevels:ABSolute`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REF<x>:REFLevels:ABSolute?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:ABSolute?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.fallhigh``: The ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLHigh`` command.
            - ``.falllow``: The ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLLow`` command.
            - ``.fallmid``: The ``MEASUrement:REF<x>:REFLevels:ABSolute:FALLMid`` command.
            - ``.hysteresis``: The ``MEASUrement:REF<x>:REFLevels:ABSolute:HYSTeresis`` command.
            - ``.risehigh``: The ``MEASUrement:REF<x>:REFLevels:ABSolute:RISEHigh`` command.
            - ``.riselow``: The ``MEASUrement:REF<x>:REFLevels:ABSolute:RISELow`` command.
            - ``.risemid``: The ``MEASUrement:REF<x>:REFLevels:ABSolute:RISEMid`` command.
            - ``.type``: The ``MEASUrement:REF<x>:REFLevels:ABSolute:TYPE`` command.
        """
        return self._absolute

    @property
    def basetop(self) -> MeasurementRefItemReflevelsBasetop:
        """Return the ``MEASUrement:REF<x>:REFLevels:BASETop`` command.

        Description:
            - This command sets or queries the method used to calculate the TOP and BASE, used to
              calculate reference levels for the measurement.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REF<x>:REFLevels:BASETop?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:BASETop?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:BASETop value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REF<x>:REFLevels:BASETop {AUTO|MINMax|MEANhistogram|MODEhistogram|EYEhistogram}
            - MEASUrement:REF<x>:REFLevels:BASETop?
            ```

        Info:
            - ``AUTO`` automatically chooses a reference level method.
            - ``MINMax`` specifies that reference levels are relative to the measurement MIN and
              MAX.
            - ``MEANhistogram`` specifies that reference levels are relative to the histogram mean
              BASE and TOP.
            - ``MODEhistogram`` specifies that reference levels are relative to the histogram mode
              BASE and TOP.
            - ``EYEhistogram`` specifies that reverence levels are relative to the eye histogram
              BASE and TOP.
        """  # noqa: E501
        return self._basetop

    @property
    def method(self) -> MeasurementRefItemReflevelsMethod:
        """Return the ``MEASUrement:REF<x>:REFLevels:METHod`` command.

        Description:
            - This command sets or queries the method used to calculate reference levels for the
              measurement.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REF<x>:REFLevels:METHod?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:METHod?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:METHod value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REF<x>:REFLevels:METHod {PERCent|ABSolute}
            - MEASUrement:REF<x>:REFLevels:METHod?
            ```

        Info:
            - ``PERCent`` specifies that the reference levels are calculated as a percent relative
              to HIGH and LOW. The percentages are defined using the
              ``MEASUrement:REF<x>:REFLevel:PERCent`` commands.
            - ``ABSolute`` specifies that the reference levels are set explicitly using the
              ``MEASUrement:REF<x>:REFLevel:ABSolute`` commands. This method is useful when precise
              values are required.
        """
        return self._method

    @property
    def percent(self) -> MeasurementRefItemReflevelsPercent:
        """Return the ``MEASUrement:REF<x>:REFLevels:PERCent`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REF<x>:REFLevels:PERCent?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REF<x>:REFLevels:PERCent?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.fallhigh``: The ``MEASUrement:REF<x>:REFLevels:PERCent:FALLHigh`` command.
            - ``.falllow``: The ``MEASUrement:REF<x>:REFLevels:PERCent:FALLLow`` command.
            - ``.fallmid``: The ``MEASUrement:REF<x>:REFLevels:PERCent:FALLMid`` command.
            - ``.hysteresis``: The ``MEASUrement:REF<x>:REFLevels:PERCent:HYSTeresis`` command.
            - ``.risehigh``: The ``MEASUrement:REF<x>:REFLevels:PERCent:RISEHigh`` command.
            - ``.riselow``: The ``MEASUrement:REF<x>:REFLevels:PERCent:RISELow`` command.
            - ``.risemid``: The ``MEASUrement:REF<x>:REFLevels:PERCent:RISEMid`` command.
            - ``.type``: The ``MEASUrement:REF<x>:REFLevels:PERCent:TYPE`` command.
        """
        return self._percent


class MeasurementRefItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``MEASUrement:REF<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:REF<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.reflevels``: The ``MEASUrement:REF<x>:REFLevels`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._reflevels = MeasurementRefItemReflevels(device, f"{self._cmd_syntax}:REFLevels")

    @property
    def reflevels(self) -> MeasurementRefItemReflevels:
        """Return the ``MEASUrement:REF<x>:REFLevels`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REF<x>:REFLevels?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:REF<x>:REFLevels?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.absolute``: The ``MEASUrement:REF<x>:REFLevels:ABSolute`` command tree.
            - ``.basetop``: The ``MEASUrement:REF<x>:REFLevels:BASETop`` command.
            - ``.method``: The ``MEASUrement:REF<x>:REFLevels:METHod`` command.
            - ``.percent``: The ``MEASUrement:REF<x>:REFLevels:PERCent`` command tree.
        """
        return self._reflevels


class MeasurementMeasItemYunit(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:YUNIT`` command.

    Description:
        - Returns the vertical scale units of the specified measurement.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:YUNIT?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:YUNIT?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:YUNIT?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
    """


class MeasurementMeasItemXunit(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:XUNIT`` command.

    Description:
        - Returns the horizontal scale units of the specified measurement.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:XUNIT?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:XUNIT?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:XUNIT?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
    """


class MeasurementMeasItemType(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:TYPe`` command.

    Description:
        - This command sets or queries the measurement type for the measurement specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:TYPe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:TYPe value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:TYPe {ACRMS|AMPlITUDE|AREA|BASE|BURSTWIDTH|DATARATE|DELAY|FALLSLEWRATE|FALLTIME|FREQUENCY|HIGHTIME|HOLD|LOWTIME|MAXIMUM|MEAN|MINIMUM|NDUtY|NPERIOD|NOVERSHOOT|NWIDTH|PDUTY|PERIOD|PHASE|PK2Pk|POVERSHOOT|PWIDTH|RISESLEWRATE|RISETIME|RMS|SETUP|SKEW|TIMEOUTSIDELEVEL|TOP}
        - MEASUrement:MEAS<x>:TYPe?
        ```

    Info:
        - ``ACRMS`` (AC RMS) is the true Root Mean Square of the data points, about the Mean. This
          measurement can be made across the entire record, or on each cycle in the record.
        - ``AMPLITUDE`` is the difference between the Top value and the Base value. This measurement
          can be made across the entire record, or on each cycle in the record.
        - ``AREA`` is the area under the curve, calculated by integrating the data points. The area
          measured above ground is positive. The area measured below ground is negative. This
          measurement can be made across the entire record, or on each cycle in the record.
        - ``BASE`` is the most common data value below the midpoint of the waveform. This
          measurement can be made across the entire record, or on each cycle in the record.
        - ``BURSTWIDTH`` (Burst Width) is the duration of a series of adjacent crossings of the Mid
          reference level (RM). Bursts are separated by a user-defined idle time (tI). This
          measurement is made on each burst in the record.
        - ``DATARATE`` (Data Rate) is the reciprocal of Unit Interval. This measurement is made on
          each bit in the record.
        - ``DELay`` is the time between the specified Mid reference level (RM) crossing on one
          source to a specified Mid reference level (RM) crossing on a second source. This
          measurement is made on the first occurrence in the record.
        - ``FALLSLEWRATE`` (Falling Slew Rate) is the rate of change in voltage as an edge
          transitions from the Top reference level (RT) to the Bottom reference level (RB). This
          measurement is made on each cycle in the record.
        - ``FALLTIME`` (Fall Time) is the time required for an edge to fall from the Top reference
          level (RT) to the Base reference level (RB). This measurement is made on each cycle in the
          record.
        - ``FREQuency`` is the reciprocal of Period. This measurement is made on each cycle in the
          record.
        - ``HIGHTIME`` (High Time) is the time the signal remains above the Top reference level
          (RT). This measurement is made on each cycle in the record.
        - ``HOLD`` (Hold Time) is the time between the specified Mid reference level crossing (RM)
          on the Clock source to the closest specified Mid reference level (RM) crossing on the Data
          source. This measurement is made on each specified Clock edge in the record.
        - ``LOWTIME`` (Low Time) is the time the signal remains below the Base reference level (RB).
          This measurement is made on each cycle in the record.
        - ``MAXimum`` is the maximum data point. This measurement can be made across the entire
          record, or on each cycle in the record.
        - ``MEAN`` is the arithmetic mean of the data points. This measurement can be made across
          the entire record, or on each cycle in the record.
        - ``MINImum`` is the minimum data point. This measurement can be made across the entire
          record, or on each cycle in the record.
        - ``NDUty`` (Negative Duty Cycle) is the ratio of the Negative Pulse Width to the Period.
          This measurement is made on each cycle in the record.
        - ``NPERIOD`` (Duration N-Periods) is the time required to complete N cycles. A cycle is the
          time between two adjacent (same direction) crossings of the Mid reference level (RM). This
          measurement is made on each cycle in the record.
        - ``NOVershoot`` (Negative Overshoot) is the difference between Minimum and Base, divided by
          the Amplitude. This measurement can be made across the entire record, or on each cycle in
          the record.
        - ``NWIdth`` (Negative Pulse Width) is the time the signal remains below the Mid reference
          level (RM). This measurement is made on each cycle in the record.
        - ``PDUTY`` (Positive Duty Cycle) is the ratio of the Positive Pulse Width to the Period.
          This measurement is made on each cycle in the record.
        - ``PERIOD`` is the time required to complete a cycle. A cycle is the time between two
          adjacent (same direction) crossings of the Mid reference level (RM). This measurement is
          made on each cycle in the record.
        - ``PHASE`` is the ratio of the Skew between two sources to the Period of the first source.
          This measurement is made on each cycle in the record.
        - ``PK2Pk`` (Peak-to-peak) is the difference between Maximum and Minimum. This measurement
          can be made across the entire record, or on each cycle in the record.
        - ``POVERSHOOT`` (Positive Overshoot) is the difference between Maximum and Top, divided by
          the Amplitude. This measurement can be made across the entire record, or on each cycle in
          the record.
        - ``PWIDTH`` (Positive Pulse Width) is the time the signal remains above the Mid reference
          level (RM). This measurement is made on each cycle in the record.
        - ``RISESLEWRATE`` (Rising Slew Rate) is the rate of change in voltage as an edge
          transitions from the Base reference level (RB) to the Top reference level (RT). This
          measurement is made on each cycle in the record.
        - ``RISETIME`` Rise Time is the time required for an edge to rise from the Base reference
          level (RB) to the Top reference level (RT). This measurement is made on each cycle in the
          record.
        - ``RMS`` is the true Root Mean Square of the data points. This measurement can be made
          across the entire record, or on each cycle in the record.
        - ``SETUP`` (Setup Time) is the time between the specified Mid reference level (RM) crossing
          on the Data source to the closest specified Mid reference level (RM) crossing on the Clock
          source. This measurement is made on each specified Clock edge in the record.
        - ``SKEW`` Skew is the time between the specified Mid reference level (RM) crossing on one
          source to the following specified Mid reference level (RM) crossing on a second source.
          This measurement is made on each cycle in the record.
        - ``TIMEOUTSIDELEVEL`` Time Outside Level is the time the signal remains above the Top
          reference level (RT) and/or below the Base reference level (RB). This measurement is made
          on each occurrence in the record.
        - ``TOP`` is the most common data value above the midpoint of the waveform. This measurement
          can be made across the entire record, or on each cycle in the record.
    """  # noqa: E501


class MeasurementMeasItemTransition(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:TRANSition`` command.

    Description:
        - This command sets or queries the transition edges flag for the measurement. The
          measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:TRANSition?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:TRANSition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:TRANSition value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:TRANSition {ON|OFF|<NR1>}
        - MEASUrement:MEAS<x>:TRANSition?
        ```

    Info:
        - ``<NR1>`` = 1, the measurement is computed on rising (if measurement type is rise time) or
          falling edges (if measurement type is fall time) following a double transition only. If it
          is set to 0, the measurement is computed on all rising (if measurement type is rise time)
          or falling (if measurement type is fall time) edges.
        - ``OFF`` computes the measurement on all rising (if measurement type is rise time) or
          falling (if measurement type is fall time) edges.
        - ``ON`` computes the measurement on rising (if measurement type is rise time) or falling
          edges (if measurement type is fall time) following a double transition only.
    """


class MeasurementMeasItemToedge(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:TOEdge`` command.

    Description:
        - This command sets or queries the 'to edge' type for the measurement. The measurement
          number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:TOEdge?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:TOEdge?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:TOEdge value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:TOEdge {SAMEas|OPPositeas|RISe|FALL|BOTH}
        - MEASUrement:MEAS<x>:TOEdge?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``FALL`` specifies the falling edge of the waveform.
        - ``RISE`` specifies the rising edge of the waveform.
        - ``BOTH`` specifies both a rising and falling edge of the waveform.
        - ``SAMEas`` specifies that both edges of the waveform are the same.
        - ``OPPositeas`` specifies that the edges of the waveform are not the same.
    """


class MeasurementMeasItemToedgesearchdirect(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:TOEDGESEARCHDIRect`` command.

    Description:
        - This command sets or queries the to edge search direction for the measurement. The
          measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:TOEDGESEARCHDIRect?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:TOEDGESEARCHDIRect?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:TOEDGESEARCHDIRect value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:TOEDGESEARCHDIRect {FORWard|BACKWard}
        - MEASUrement:MEAS<x>:TOEDGESEARCHDIRect?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``FORWard`` specifies a forward search to the edge.
        - ``BACKWard`` specifies a backward search to the edge.
    """


class MeasurementMeasItemStatus(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:STATUS`` command.

    Description:
        - This command returns the pass fail status, if applicable, for the selected measurement.
          Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:STATUS?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:STATUS?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:STATUS?
        ```

    Info:
        - ``PASS`` specifies that the user specified measurement limit has not been violated.
        - ``FAIL`` specifies that the user specified measurement limit has been violated.
    """


class MeasurementMeasItemSource1(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:SOUrce1`` command.

    Description:
        - This command sets or queries the measurement source. The measurement number and source are
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:SOUrce1?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:SOUrce1?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:SOUrce1 value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:SOUrce1 {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>}
        - MEASUrement:MEAS<x>:SOUrce1?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``1`` specifies the source number.
        - ``CH<x>`` specifies an analog channel to use as the source.
        - ``DCH<x>_D<x>`` specifies a digital channel to use as the source. The supported digital
          channel value is 1. The supported digital bit values are 0 to 15.
        - ``MATH<x>`` specifies a math waveform to use as the source.
        - ``REF<x>`` specifies a reference waveform to use as the source.
    """


class MeasurementMeasItemSignaltype(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:SIGNALType`` command.

    Description:
        - This command sets or queries the signal type of source 1 for the measurement. The
          measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:SIGNALType?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:SIGNALType?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:SIGNALType value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:SIGNALType {CLOCK|DATA|AUTO}
        - MEASUrement:MEAS<x>:SIGNALType?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``CLOCK`` specifies a clock signal type.
        - ``DATA`` specifies a data signal type.
        - ``AUTO`` automatically selects the signal type.
    """


class MeasurementMeasItemResultsCurrentacqStddev(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:STDDev`` command.

    Description:
        - This query-only command returns the standard deviation for the specified measurement for
          all acquisitions accumulated since statistics were last reset. The measurement number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:STDDev?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:STDDev?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:RESUlts:CURRentacq:STDDev?
        ```
    """


class MeasurementMeasItemResultsCurrentacqPopulation(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:POPUlation`` command.

    Description:
        - This query-only command returns the population for the specified measurement for the
          current acquisition. The measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:POPUlation?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:POPUlation?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:RESUlts:CURRentacq:POPUlation?
        ```
    """


class MeasurementMeasItemResultsCurrentacqPk2pk(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:PK2PK`` command.

    Description:
        - This query-only command returns the peak-to-peak value for the specified measurement for
          the current acquisition. The measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:PK2PK?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:PK2PK?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:RESUlts:CURRentacq:PK2PK?
        ```
    """


class MeasurementMeasItemResultsCurrentacqMinimum(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:MINimum`` command.

    Description:
        - This query-only command returns the minimum value found for the specified measurement
          since the last statistical reset. The measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:MINimum?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:MINimum?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:RESUlts:CURRentacq:MINimum?
        ```
    """


class MeasurementMeasItemResultsCurrentacqMean(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:MEAN`` command.

    Description:
        - This query-only command returns the mean value for the measurement for the current
          acquisition.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:MEAN?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:MEAN?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:RESUlts:CURRentacq:MEAN?
        ```
    """


class MeasurementMeasItemResultsCurrentacqMaximum(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:MAXimum`` command.

    Description:
        - This query-only command returns the maximum value found for the specified measurement
          since the last statistical reset. The measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:MAXimum?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:MAXimum?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:RESUlts:CURRentacq:MAXimum?
        ```
    """


class MeasurementMeasItemResultsCurrentacq(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:RESUlts:CURRentacq`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:RESUlts:CURRentacq?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:RESUlts:CURRentacq?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.maximum``: The ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:MAXimum`` command.
        - ``.mean``: The ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:MEAN`` command.
        - ``.minimum``: The ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:MINimum`` command.
        - ``.pk2pk``: The ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:PK2PK`` command.
        - ``.population``: The ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:POPUlation`` command.
        - ``.stddev``: The ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:STDDev`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._maximum = MeasurementMeasItemResultsCurrentacqMaximum(
            device, f"{self._cmd_syntax}:MAXimum"
        )
        self._mean = MeasurementMeasItemResultsCurrentacqMean(device, f"{self._cmd_syntax}:MEAN")
        self._minimum = MeasurementMeasItemResultsCurrentacqMinimum(
            device, f"{self._cmd_syntax}:MINimum"
        )
        self._pk2pk = MeasurementMeasItemResultsCurrentacqPk2pk(device, f"{self._cmd_syntax}:PK2PK")
        self._population = MeasurementMeasItemResultsCurrentacqPopulation(
            device, f"{self._cmd_syntax}:POPUlation"
        )
        self._stddev = MeasurementMeasItemResultsCurrentacqStddev(
            device, f"{self._cmd_syntax}:STDDev"
        )

    @property
    def maximum(self) -> MeasurementMeasItemResultsCurrentacqMaximum:
        """Return the ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:MAXimum`` command.

        Description:
            - This query-only command returns the maximum value found for the specified measurement
              since the last statistical reset. The measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:MAXimum?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:MAXimum?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:RESUlts:CURRentacq:MAXimum?
            ```
        """
        return self._maximum

    @property
    def mean(self) -> MeasurementMeasItemResultsCurrentacqMean:
        """Return the ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:MEAN`` command.

        Description:
            - This query-only command returns the mean value for the measurement for the current
              acquisition.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:MEAN?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:MEAN?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:RESUlts:CURRentacq:MEAN?
            ```
        """
        return self._mean

    @property
    def minimum(self) -> MeasurementMeasItemResultsCurrentacqMinimum:
        """Return the ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:MINimum`` command.

        Description:
            - This query-only command returns the minimum value found for the specified measurement
              since the last statistical reset. The measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:MINimum?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:MINimum?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:RESUlts:CURRentacq:MINimum?
            ```
        """
        return self._minimum

    @property
    def pk2pk(self) -> MeasurementMeasItemResultsCurrentacqPk2pk:
        """Return the ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:PK2PK`` command.

        Description:
            - This query-only command returns the peak-to-peak value for the specified measurement
              for the current acquisition. The measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:PK2PK?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:PK2PK?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:RESUlts:CURRentacq:PK2PK?
            ```
        """
        return self._pk2pk

    @property
    def population(self) -> MeasurementMeasItemResultsCurrentacqPopulation:
        """Return the ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:POPUlation`` command.

        Description:
            - This query-only command returns the population for the specified measurement for the
              current acquisition. The measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:POPUlation?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:POPUlation?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:RESUlts:CURRentacq:POPUlation?
            ```
        """
        return self._population

    @property
    def stddev(self) -> MeasurementMeasItemResultsCurrentacqStddev:
        """Return the ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:STDDev`` command.

        Description:
            - This query-only command returns the standard deviation for the specified measurement
              for all acquisitions accumulated since statistics were last reset. The measurement
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:STDDev?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:STDDev?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:RESUlts:CURRentacq:STDDev?
            ```
        """
        return self._stddev


class MeasurementMeasItemResultsAllacqsStddev(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:STDDev`` command.

    Description:
        - This query-only command returns the standard deviation for all accumulated measurement
          acquisitions for measurement <x>.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:STDDev?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:STDDev?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:RESUlts:ALLAcqs:STDDev?
        ```
    """


class MeasurementMeasItemResultsAllacqsPopulation(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:POPUlation`` command.

    Description:
        - This query-only command returns the population measurement value for measurement <x>.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:POPUlation?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:POPUlation?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:RESUlts:ALLAcqs:POPUlation?
        ```
    """


class MeasurementMeasItemResultsAllacqsPk2pk(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:PK2PK`` command.

    Description:
        - This query-only command returns the peak-to-peak value for all accumulated measurement
          acquisitions for measurement <x>.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:PK2PK?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:PK2PK?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:RESUlts:ALLAcqs:PK2PK?
        ```
    """


class MeasurementMeasItemResultsAllacqsMinimum(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MINimum`` command.

    Description:
        - This query-only command returns the minimum value for all accumulated measurement
          acquisitions for measurement <x>.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MINimum?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MINimum?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MINimum?
        ```
    """


class MeasurementMeasItemResultsAllacqsMean(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MEAN`` command.

    Description:
        - This query-only command returns the mean value for all accumulated measurement
          acquisitions for measurement <x>.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MEAN?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MEAN?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MEAN?
        ```
    """


class MeasurementMeasItemResultsAllacqsMaximum(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MAXimum`` command.

    Description:
        - This query-only command returns the maximum value for all accumulated measurement
          acquisitions of the specified measurement. The measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MAXimum?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MAXimum?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MAXimum?
        ```
    """


class MeasurementMeasItemResultsAllacqs(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs?``
          query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.maximum``: The ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MAXimum`` command.
        - ``.mean``: The ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MEAN`` command.
        - ``.minimum``: The ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MINimum`` command.
        - ``.pk2pk``: The ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:PK2PK`` command.
        - ``.population``: The ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:POPUlation`` command.
        - ``.stddev``: The ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:STDDev`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._maximum = MeasurementMeasItemResultsAllacqsMaximum(
            device, f"{self._cmd_syntax}:MAXimum"
        )
        self._mean = MeasurementMeasItemResultsAllacqsMean(device, f"{self._cmd_syntax}:MEAN")
        self._minimum = MeasurementMeasItemResultsAllacqsMinimum(
            device, f"{self._cmd_syntax}:MINimum"
        )
        self._pk2pk = MeasurementMeasItemResultsAllacqsPk2pk(device, f"{self._cmd_syntax}:PK2PK")
        self._population = MeasurementMeasItemResultsAllacqsPopulation(
            device, f"{self._cmd_syntax}:POPUlation"
        )
        self._stddev = MeasurementMeasItemResultsAllacqsStddev(device, f"{self._cmd_syntax}:STDDev")

    @property
    def maximum(self) -> MeasurementMeasItemResultsAllacqsMaximum:
        """Return the ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MAXimum`` command.

        Description:
            - This query-only command returns the maximum value for all accumulated measurement
              acquisitions of the specified measurement. The measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MAXimum?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MAXimum?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MAXimum?
            ```
        """
        return self._maximum

    @property
    def mean(self) -> MeasurementMeasItemResultsAllacqsMean:
        """Return the ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MEAN`` command.

        Description:
            - This query-only command returns the mean value for all accumulated measurement
              acquisitions for measurement <x>.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MEAN?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MEAN?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MEAN?
            ```
        """
        return self._mean

    @property
    def minimum(self) -> MeasurementMeasItemResultsAllacqsMinimum:
        """Return the ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MINimum`` command.

        Description:
            - This query-only command returns the minimum value for all accumulated measurement
              acquisitions for measurement <x>.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MINimum?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MINimum?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MINimum?
            ```
        """
        return self._minimum

    @property
    def pk2pk(self) -> MeasurementMeasItemResultsAllacqsPk2pk:
        """Return the ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:PK2PK`` command.

        Description:
            - This query-only command returns the peak-to-peak value for all accumulated measurement
              acquisitions for measurement <x>.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:PK2PK?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:PK2PK?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:RESUlts:ALLAcqs:PK2PK?
            ```
        """
        return self._pk2pk

    @property
    def population(self) -> MeasurementMeasItemResultsAllacqsPopulation:
        """Return the ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:POPUlation`` command.

        Description:
            - This query-only command returns the population measurement value for measurement <x>.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:POPUlation?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:POPUlation?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:RESUlts:ALLAcqs:POPUlation?
            ```
        """
        return self._population

    @property
    def stddev(self) -> MeasurementMeasItemResultsAllacqsStddev:
        """Return the ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:STDDev`` command.

        Description:
            - This query-only command returns the standard deviation for all accumulated measurement
              acquisitions for measurement <x>.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:STDDev?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:STDDev?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:RESUlts:ALLAcqs:STDDev?
            ```
        """
        return self._stddev


class MeasurementMeasItemResults(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:RESUlts`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:RESUlts?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:RESUlts?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.allacqs``: The ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs`` command tree.
        - ``.currentacq``: The ``MEASUrement:MEAS<x>:RESUlts:CURRentacq`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._allacqs = MeasurementMeasItemResultsAllacqs(device, f"{self._cmd_syntax}:ALLAcqs")
        self._currentacq = MeasurementMeasItemResultsCurrentacq(
            device, f"{self._cmd_syntax}:CURRentacq"
        )

    @property
    def allacqs(self) -> MeasurementMeasItemResultsAllacqs:
        """Return the ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.maximum``: The ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MAXimum`` command.
            - ``.mean``: The ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MEAN`` command.
            - ``.minimum``: The ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:MINimum`` command.
            - ``.pk2pk``: The ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:PK2PK`` command.
            - ``.population``: The ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:POPUlation`` command.
            - ``.stddev``: The ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs:STDDev`` command.
        """
        return self._allacqs

    @property
    def currentacq(self) -> MeasurementMeasItemResultsCurrentacq:
        """Return the ``MEASUrement:MEAS<x>:RESUlts:CURRentacq`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:CURRentacq?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:RESUlts:CURRentacq?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.maximum``: The ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:MAXimum`` command.
            - ``.mean``: The ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:MEAN`` command.
            - ``.minimum``: The ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:MINimum`` command.
            - ``.pk2pk``: The ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:PK2PK`` command.
            - ``.population``: The ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:POPUlation`` command.
            - ``.stddev``: The ``MEASUrement:MEAS<x>:RESUlts:CURRentacq:STDDev`` command.
        """
        return self._currentacq


class MeasurementMeasItemRefvoltage(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFVoltage`` command.

    Description:
        - This command sets or queries the reference voltage value for the measurement. The
          measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:REFVoltage?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:REFVoltage?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:REFVoltage value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFVoltage <NR3>
        - MEASUrement:MEAS<x>:REFVoltage?
        ```

    Info:
        - ``MEAS<x>`` is the measurement number.
        - ``<NR3>`` is the reference voltage value for the selected configuration.
    """


class MeasurementMeasItemRefmode(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFMode`` command.

    Description:
        - This command sets or queries the reference level mode for the measurement. The measurement
          number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:REFMode?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:REFMode?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:REFMode value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFMode {AUTO|MANual}
        - MEASUrement:MEAS<x>:REFMode?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``AUTO`` sets the reference level for the measurement automatically.
        - ``MANual`` allows the user to set the reference level for the measurement.
    """


class MeasurementMeasItemReflevelsAbsoluteFallhigh(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevels:ABSolute:FALLHigh`` command.

    Description:
        - This command sets or queries the value used as the high reference level of the falling
          edge when the measurement's ref level method is set to absolute. Measurements are
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels:ABSolute:FALLHigh?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels:ABSolute:FALLHigh?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels:ABSolute:FALLHigh value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFLevels:ABSolute:FALLHigh <NR3>
        - MEASUrement:MEAS<x>:REFLevels:ABSolute:FALLHigh?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``<NR3>`` is the high reference level in volts. The default is 0.0 V.
    """


class MeasurementMeasItemReflevelsAbsolute(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevels:ABSolute`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:REFLevels:ABSolute?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels:ABSolute?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Info:
        - ``MEAS<x>`` specifies the measurement number.

    Properties:
        - ``.fallhigh``: The ``MEASUrement:MEAS<x>:REFLevels:ABSolute:FALLHigh`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fallhigh = MeasurementMeasItemReflevelsAbsoluteFallhigh(
            device, f"{self._cmd_syntax}:FALLHigh"
        )

    @property
    def fallhigh(self) -> MeasurementMeasItemReflevelsAbsoluteFallhigh:
        """Return the ``MEASUrement:MEAS<x>:REFLevels:ABSolute:FALLHigh`` command.

        Description:
            - This command sets or queries the value used as the high reference level of the falling
              edge when the measurement's ref level method is set to absolute. Measurements are
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels:ABSolute:FALLHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels:ABSolute:FALLHigh?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels:ABSolute:FALLHigh value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFLevels:ABSolute:FALLHigh <NR3>
            - MEASUrement:MEAS<x>:REFLevels:ABSolute:FALLHigh?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``<NR3>`` is the high reference level in volts. The default is 0.0 V.
        """
        return self._fallhigh


class MeasurementMeasItemReflevels1PercentType(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevels1:PERCent:TYPE`` command.

    Description:
        - This command specifies or queries the reference level percent type for the measurement.
          The measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:PERCent:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:PERCent:TYPE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:PERCent:TYPE value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFLevels1:PERCent:TYPE {TENNinety|TWENtyeighty|CUSTom}
        - MEASUrement:MEAS<x>:REFLevels1:PERCent:TYPE?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``TENNinety`` sets the values for Low, Mid and High Ref to 10%, 50% and 90% respectively.
        - ``TWENtyeighty`` sets the values for Low, Mid and High Ref are set to 20%, 50% and 80%
          respectively.
        - ``CUSTom`` allows setting other reference level percents.
    """


class MeasurementMeasItemReflevels1PercentRisemid(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEMid`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the mid reference level of the rising edge when the measurement's
          ref level method is set to percent. The measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEMid?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEMid?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEMid value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEMid <NR3>
        - MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEMid?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``<NR3>`` the percentage (where 50% is equal to MID) used to calculate the mid reference
          level when the measurement Ref level method is set to Percent.
    """


class MeasurementMeasItemReflevels1PercentRiselow(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISELow`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the low reference level of the rising edge when the measurement's
          ref level method is set to percent. The measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISELow?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISELow?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISELow value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFLevels1:PERCent:RISELow <NR3>
        - MEASUrement:MEAS<x>:REFLevels1:PERCent:RISELow?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``<NR3>`` is the percentage (where 99% is equal to TOP) used to calculate the mid
          reference level when the measurement's Ref level method is set to Percent.
    """


class MeasurementMeasItemReflevels1PercentRisehigh(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEHigh`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the high reference level of the rising edge when the measurement's
          ref level method is set to percent. The measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEHigh?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEHigh?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEHigh value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEHigh <NR3>
        - MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEHigh?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``<NR3>`` is the percentage (where 99% is equal to TOP) used to calculate the high
          reference level when the measurement's Ref level method is set to Percent.
    """


class MeasurementMeasItemReflevels1PercentHysteresis(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevels1:PERCent:HYSTeresis`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to MAX and 1% is equal to
          MIN) used to calculate the hysteresis of the reference level when the measurement's ref
          level method is set to percent. The measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:PERCent:HYSTeresis?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:PERCent:HYSTeresis?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:PERCent:HYSTeresis value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFLevels1:PERCent:HYSTeresis <NR3>
        - MEASUrement:MEAS<x>:REFLevels1:PERCent:HYSTeresis?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``<NR3>`` is the hysteresis value used for the autoset.
    """


class MeasurementMeasItemReflevels1PercentFallmid(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLMid`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the mid reference level of the falling edge when the measurement's
          ref level method is set to percent. The measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLMid?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLMid?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLMid value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLMid <NR3>
        - MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLMid?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``<NR3>`` is the percentage (where 50% is equal to MID) used to calculate the mid
          reference level.
    """


class MeasurementMeasItemReflevels1PercentFalllow(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLLow`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the low reference level of the falling edge when the measurement's
          ref level method is set to percent. The measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLLow?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLLow?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLLow value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLLow <NR3>
        - MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLLow?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``<NR3>`` is the percentage (where 100% is equal to HIGH) used to calculate the mid
          reference level.
    """


class MeasurementMeasItemReflevels1PercentFallhigh(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLHigh`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the high reference level of the falling edge when the
          measurement's ref level method is set to percent. The measurement number is specified by
          x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLHigh?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLHigh?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLHigh value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLHigh <NR3>
        - MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLHigh?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``<NR3>`` is the percentage (where 100% is equal to HIGH) used to calculate the high
          reference level.
    """


#  pylint: disable=too-many-instance-attributes
class MeasurementMeasItemReflevels1Percent(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevels1:PERCent`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:REFLevels1:PERCent?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:PERCent?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Info:
        - ``MEAS<x>`` specifies the measurement number.

    Properties:
        - ``.fallhigh``: The ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLHigh`` command.
        - ``.falllow``: The ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLLow`` command.
        - ``.fallmid``: The ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLMid`` command.
        - ``.hysteresis``: The ``MEASUrement:MEAS<x>:REFLevels1:PERCent:HYSTeresis`` command.
        - ``.risehigh``: The ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEHigh`` command.
        - ``.riselow``: The ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISELow`` command.
        - ``.risemid``: The ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEMid`` command.
        - ``.type``: The ``MEASUrement:MEAS<x>:REFLevels1:PERCent:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fallhigh = MeasurementMeasItemReflevels1PercentFallhigh(
            device, f"{self._cmd_syntax}:FALLHigh"
        )
        self._falllow = MeasurementMeasItemReflevels1PercentFalllow(
            device, f"{self._cmd_syntax}:FALLLow"
        )
        self._fallmid = MeasurementMeasItemReflevels1PercentFallmid(
            device, f"{self._cmd_syntax}:FALLMid"
        )
        self._hysteresis = MeasurementMeasItemReflevels1PercentHysteresis(
            device, f"{self._cmd_syntax}:HYSTeresis"
        )
        self._risehigh = MeasurementMeasItemReflevels1PercentRisehigh(
            device, f"{self._cmd_syntax}:RISEHigh"
        )
        self._riselow = MeasurementMeasItemReflevels1PercentRiselow(
            device, f"{self._cmd_syntax}:RISELow"
        )
        self._risemid = MeasurementMeasItemReflevels1PercentRisemid(
            device, f"{self._cmd_syntax}:RISEMid"
        )
        self._type = MeasurementMeasItemReflevels1PercentType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def fallhigh(self) -> MeasurementMeasItemReflevels1PercentFallhigh:
        """Return the ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLHigh`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the high reference level of the falling edge when the
              measurement's ref level method is set to percent. The measurement number is specified
              by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLHigh?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLHigh value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLHigh <NR3>
            - MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLHigh?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``<NR3>`` is the percentage (where 100% is equal to HIGH) used to calculate the high
              reference level.
        """
        return self._fallhigh

    @property
    def falllow(self) -> MeasurementMeasItemReflevels1PercentFalllow:
        """Return the ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLLow`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the low reference level of the falling edge when the
              measurement's ref level method is set to percent. The measurement number is specified
              by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLLow?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLLow?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLLow value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLLow <NR3>
            - MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLLow?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``<NR3>`` is the percentage (where 100% is equal to HIGH) used to calculate the mid
              reference level.
        """
        return self._falllow

    @property
    def fallmid(self) -> MeasurementMeasItemReflevels1PercentFallmid:
        """Return the ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLMid`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the mid reference level of the falling edge when the
              measurement's ref level method is set to percent. The measurement number is specified
              by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLMid?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLMid value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLMid <NR3>
            - MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLMid?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``<NR3>`` is the percentage (where 50% is equal to MID) used to calculate the mid
              reference level.
        """
        return self._fallmid

    @property
    def hysteresis(self) -> MeasurementMeasItemReflevels1PercentHysteresis:
        """Return the ``MEASUrement:MEAS<x>:REFLevels1:PERCent:HYSTeresis`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to MAX and 1% is equal
              to MIN) used to calculate the hysteresis of the reference level when the measurement's
              ref level method is set to percent. The measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:PERCent:HYSTeresis?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:PERCent:HYSTeresis?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:PERCent:HYSTeresis value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFLevels1:PERCent:HYSTeresis <NR3>
            - MEASUrement:MEAS<x>:REFLevels1:PERCent:HYSTeresis?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``<NR3>`` is the hysteresis value used for the autoset.
        """
        return self._hysteresis

    @property
    def risehigh(self) -> MeasurementMeasItemReflevels1PercentRisehigh:
        """Return the ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEHigh`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the high reference level of the rising edge when the
              measurement's ref level method is set to percent. The measurement number is specified
              by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEHigh?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEHigh value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEHigh <NR3>
            - MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEHigh?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``<NR3>`` is the percentage (where 99% is equal to TOP) used to calculate the high
              reference level when the measurement's Ref level method is set to Percent.
        """
        return self._risehigh

    @property
    def riselow(self) -> MeasurementMeasItemReflevels1PercentRiselow:
        """Return the ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISELow`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the low reference level of the rising edge when the
              measurement's ref level method is set to percent. The measurement number is specified
              by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISELow?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISELow?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISELow value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFLevels1:PERCent:RISELow <NR3>
            - MEASUrement:MEAS<x>:REFLevels1:PERCent:RISELow?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``<NR3>`` is the percentage (where 99% is equal to TOP) used to calculate the mid
              reference level when the measurement's Ref level method is set to Percent.
        """
        return self._riselow

    @property
    def risemid(self) -> MeasurementMeasItemReflevels1PercentRisemid:
        """Return the ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEMid`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the mid reference level of the rising edge when the
              measurement's ref level method is set to percent. The measurement number is specified
              by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEMid?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEMid value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEMid <NR3>
            - MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEMid?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``<NR3>`` the percentage (where 50% is equal to MID) used to calculate the mid
              reference level when the measurement Ref level method is set to Percent.
        """
        return self._risemid

    @property
    def type(self) -> MeasurementMeasItemReflevels1PercentType:
        """Return the ``MEASUrement:MEAS<x>:REFLevels1:PERCent:TYPE`` command.

        Description:
            - This command specifies or queries the reference level percent type for the
              measurement. The measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:PERCent:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:PERCent:TYPE?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:PERCent:TYPE value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFLevels1:PERCent:TYPE {TENNinety|TWENtyeighty|CUSTom}
            - MEASUrement:MEAS<x>:REFLevels1:PERCent:TYPE?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``TENNinety`` sets the values for Low, Mid and High Ref to 10%, 50% and 90%
              respectively.
            - ``TWENtyeighty`` sets the values for Low, Mid and High Ref are set to 20%, 50% and 80%
              respectively.
            - ``CUSTom`` allows setting other reference level percents.
        """
        return self._type


class MeasurementMeasItemReflevels1Method(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevels1:METHod`` command.

    Description:
        - This command sets or queries the method used to calculate reference levels for the
          measurement. The measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:REFLevels1:METHod?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:METHod?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:METHod value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFLevels1:METHod {PERCent|ABSolute}
        - MEASUrement:MEAS<x>:REFLevels1:METHod?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``PERCent`` specifies that the reference levels are calculated as a percent relative to
          HIGH and LOW. The percentages are defined using the
          ``MEASUrement:MEAS<x>:REFLevel:PERCent`` commands.
        - ``ABSolute`` specifies that the reference levels are set explicitly using the
          ``MEASUrement:MEAS<x>:REFLevel:ABSolute`` commands. This method is useful when precise
          values are required.
    """


class MeasurementMeasItemReflevels1Basetop(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevels1:BASETop`` command.

    Description:
        - This command sets or queries the method used to calculate the TOP and BASE used to
          calculate reference levels for the measurement. The measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:REFLevels1:BASETop?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:BASETop?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:BASETop value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFLevels1:BASETop {AUTO|MINMax|MEANhistogram|MODEhistogram|EYEhistogram}
        - MEASUrement:MEAS<x>:REFLevels1:BASETop?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``AUTO`` automatically chooses a reference level method.
        - ``MINMax`` specifies that reference levels are relative to the measurement MIN and MAX.
        - ``MEANhistogram`` specifies that reference levels are relative to the histogram mean BASE
          and TOP.
        - ``MODEhistogram`` specifies that reference levels are relative to the histogram mode BASE
          and TOP.
        - ``EYEhistogram`` specifies that reverence levels are relative to the eye histogram BASE
          and TOP.
    """  # noqa: E501


class MeasurementMeasItemReflevels1AbsoluteType(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:TYPE`` command.

    Description:
        - This command sets or queries the reference level type for the measurement. The measurement
          number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:TYPE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:TYPE value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFLevels1:ABSolute:TYPE {SAME|UNIQue}
        - MEASUrement:MEAS<x>:REFLevels1:ABSolute:TYPE?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``SAME`` specifies that the absolute levels are set the same.
        - ``UNIQue`` specifies that the absolute levels can be set independently.
    """


class MeasurementMeasItemReflevels1AbsoluteRisemid(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEMid`` command.

    Description:
        - This command sets or queries the value used as the mid reference level of the rising edge
          when the measurement's ref level method is set to absolute. The measurement number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEMid?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEMid?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEMid value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEMid <NR3>
        - MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEMid?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``<NR3>`` is the mid reference level (where 50% is equal to MID) used to calculate the mid
          reference level when the measurement's Ref level method is set to Absolute.
    """


class MeasurementMeasItemReflevels1AbsoluteRiselow(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISELow`` command.

    Description:
        - This command sets or queries the value used as the low reference level of the rising edge
          when the measurement's ref level method is set to absolute. The measurement number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISELow?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISELow?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISELow value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISELow <NR3>
        - MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISELow?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``<NR3>`` is the low reference level, and is the zero percent level when the measurement's
          Ref level method is set to Absolute.
    """


class MeasurementMeasItemReflevels1AbsoluteRisehigh(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEHigh`` command.

    Description:
        - This command sets or queries the value used as the high reference level of the rising edge
          when the measurement's ref level method is set to absolute. The measurement number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEHigh?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEHigh?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEHigh value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEHigh <NR3>
        - MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEHigh?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``<NR3>`` is the high reference level, and is the zero percent level when the
          measurement's Ref level method is set to Absolute.
    """


class MeasurementMeasItemReflevels1AbsoluteHysteresis(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:HYSTeresis`` command.

    Description:
        - This command sets or queries the value of the hysteresis of the reference level when the
          measurement's ref level method is set to absolute. The measurement number is specified by
          x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:HYSTeresis?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:HYSTeresis?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:HYSTeresis value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFLevels1:ABSolute:HYSTeresis <NR3>
        - MEASUrement:MEAS<x>:REFLevels1:ABSolute:HYSTeresis?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``<NR3>`` is the hysteresis value used for autoset.
    """


class MeasurementMeasItemReflevels1AbsoluteFallmid(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLMid`` command.

    Description:
        - This command sets or queries the value used as the mid reference level of the falling edge
          when the measurement's ref level method is set to absolute. Measurements are specified by
          x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLMid?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLMid?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLMid value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLMid <NR3>
        - MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLMid?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``<NR3>`` is the mid reference level in volts. The default is 0.0 V.
    """


class MeasurementMeasItemReflevels1AbsoluteFalllow(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLLow`` command.

    Description:
        - This command sets or queries the value used as the low reference level of the falling edge
          when the measurement's ref level method is set to absolute. Measurements are specified by
          x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLLow?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLLow?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLLow value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLLow <NR3>
        - MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLLow?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``<NR3>`` is the low reference level in volts. The default is 0.0 V.
    """


class MeasurementMeasItemReflevels1Absolute(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevels1:ABSolute`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:REFLevels1:ABSolute?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevels1:ABSolute?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Info:
        - ``MEAS<x>`` specifies the measurement number.

    Properties:
        - ``.falllow``: The ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLLow`` command.
        - ``.fallmid``: The ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLMid`` command.
        - ``.hysteresis``: The ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:HYSTeresis`` command.
        - ``.risehigh``: The ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEHigh`` command.
        - ``.riselow``: The ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISELow`` command.
        - ``.risemid``: The ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEMid`` command.
        - ``.type``: The ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._falllow = MeasurementMeasItemReflevels1AbsoluteFalllow(
            device, f"{self._cmd_syntax}:FALLLow"
        )
        self._fallmid = MeasurementMeasItemReflevels1AbsoluteFallmid(
            device, f"{self._cmd_syntax}:FALLMid"
        )
        self._hysteresis = MeasurementMeasItemReflevels1AbsoluteHysteresis(
            device, f"{self._cmd_syntax}:HYSTeresis"
        )
        self._risehigh = MeasurementMeasItemReflevels1AbsoluteRisehigh(
            device, f"{self._cmd_syntax}:RISEHigh"
        )
        self._riselow = MeasurementMeasItemReflevels1AbsoluteRiselow(
            device, f"{self._cmd_syntax}:RISELow"
        )
        self._risemid = MeasurementMeasItemReflevels1AbsoluteRisemid(
            device, f"{self._cmd_syntax}:RISEMid"
        )
        self._type = MeasurementMeasItemReflevels1AbsoluteType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def falllow(self) -> MeasurementMeasItemReflevels1AbsoluteFalllow:
        """Return the ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLLow`` command.

        Description:
            - This command sets or queries the value used as the low reference level of the falling
              edge when the measurement's ref level method is set to absolute. Measurements are
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLLow?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLLow?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLLow value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLLow <NR3>
            - MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLLow?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``<NR3>`` is the low reference level in volts. The default is 0.0 V.
        """
        return self._falllow

    @property
    def fallmid(self) -> MeasurementMeasItemReflevels1AbsoluteFallmid:
        """Return the ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLMid`` command.

        Description:
            - This command sets or queries the value used as the mid reference level of the falling
              edge when the measurement's ref level method is set to absolute. Measurements are
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLMid?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLMid value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLMid <NR3>
            - MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLMid?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``<NR3>`` is the mid reference level in volts. The default is 0.0 V.
        """
        return self._fallmid

    @property
    def hysteresis(self) -> MeasurementMeasItemReflevels1AbsoluteHysteresis:
        """Return the ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:HYSTeresis`` command.

        Description:
            - This command sets or queries the value of the hysteresis of the reference level when
              the measurement's ref level method is set to absolute. The measurement number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:HYSTeresis?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:HYSTeresis?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:HYSTeresis value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFLevels1:ABSolute:HYSTeresis <NR3>
            - MEASUrement:MEAS<x>:REFLevels1:ABSolute:HYSTeresis?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``<NR3>`` is the hysteresis value used for autoset.
        """
        return self._hysteresis

    @property
    def risehigh(self) -> MeasurementMeasItemReflevels1AbsoluteRisehigh:
        """Return the ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEHigh`` command.

        Description:
            - This command sets or queries the value used as the high reference level of the rising
              edge when the measurement's ref level method is set to absolute. The measurement
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEHigh?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEHigh value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEHigh <NR3>
            - MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEHigh?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``<NR3>`` is the high reference level, and is the zero percent level when the
              measurement's Ref level method is set to Absolute.
        """
        return self._risehigh

    @property
    def riselow(self) -> MeasurementMeasItemReflevels1AbsoluteRiselow:
        """Return the ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISELow`` command.

        Description:
            - This command sets or queries the value used as the low reference level of the rising
              edge when the measurement's ref level method is set to absolute. The measurement
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISELow?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISELow?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISELow value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISELow <NR3>
            - MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISELow?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``<NR3>`` is the low reference level, and is the zero percent level when the
              measurement's Ref level method is set to Absolute.
        """
        return self._riselow

    @property
    def risemid(self) -> MeasurementMeasItemReflevels1AbsoluteRisemid:
        """Return the ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEMid`` command.

        Description:
            - This command sets or queries the value used as the mid reference level of the rising
              edge when the measurement's ref level method is set to absolute. The measurement
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEMid?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEMid value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEMid <NR3>
            - MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEMid?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``<NR3>`` is the mid reference level (where 50% is equal to MID) used to calculate the
              mid reference level when the measurement's Ref level method is set to Absolute.
        """
        return self._risemid

    @property
    def type(self) -> MeasurementMeasItemReflevels1AbsoluteType:
        """Return the ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:TYPE`` command.

        Description:
            - This command sets or queries the reference level type for the measurement. The
              measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:TYPE?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:TYPE value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFLevels1:ABSolute:TYPE {SAME|UNIQue}
            - MEASUrement:MEAS<x>:REFLevels1:ABSolute:TYPE?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``SAME`` specifies that the absolute levels are set the same.
            - ``UNIQue`` specifies that the absolute levels can be set independently.
        """
        return self._type


class MeasurementMeasItemReflevels1(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevels1`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:REFLevels1?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:REFLevels1?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``MEAS<x>`` specifies the measurement number.

    Properties:
        - ``.absolute``: The ``MEASUrement:MEAS<x>:REFLevels1:ABSolute`` command tree.
        - ``.basetop``: The ``MEASUrement:MEAS<x>:REFLevels1:BASETop`` command.
        - ``.method``: The ``MEASUrement:MEAS<x>:REFLevels1:METHod`` command.
        - ``.percent``: The ``MEASUrement:MEAS<x>:REFLevels1:PERCent`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._absolute = MeasurementMeasItemReflevels1Absolute(
            device, f"{self._cmd_syntax}:ABSolute"
        )
        self._basetop = MeasurementMeasItemReflevels1Basetop(device, f"{self._cmd_syntax}:BASETop")
        self._method = MeasurementMeasItemReflevels1Method(device, f"{self._cmd_syntax}:METHod")
        self._percent = MeasurementMeasItemReflevels1Percent(device, f"{self._cmd_syntax}:PERCent")

    @property
    def absolute(self) -> MeasurementMeasItemReflevels1Absolute:
        """Return the ``MEASUrement:MEAS<x>:REFLevels1:ABSolute`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:ABSolute?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:ABSolute?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Info:
            - ``MEAS<x>`` specifies the measurement number.

        Sub-properties:
            - ``.falllow``: The ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLLow`` command.
            - ``.fallmid``: The ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:FALLMid`` command.
            - ``.hysteresis``: The ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:HYSTeresis`` command.
            - ``.risehigh``: The ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEHigh`` command.
            - ``.riselow``: The ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISELow`` command.
            - ``.risemid``: The ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:RISEMid`` command.
            - ``.type``: The ``MEASUrement:MEAS<x>:REFLevels1:ABSolute:TYPE`` command.
        """
        return self._absolute

    @property
    def basetop(self) -> MeasurementMeasItemReflevels1Basetop:
        """Return the ``MEASUrement:MEAS<x>:REFLevels1:BASETop`` command.

        Description:
            - This command sets or queries the method used to calculate the TOP and BASE used to
              calculate reference levels for the measurement. The measurement number is specified by
              x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:BASETop?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:BASETop?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:BASETop value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFLevels1:BASETop {AUTO|MINMax|MEANhistogram|MODEhistogram|EYEhistogram}
            - MEASUrement:MEAS<x>:REFLevels1:BASETop?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``AUTO`` automatically chooses a reference level method.
            - ``MINMax`` specifies that reference levels are relative to the measurement MIN and
              MAX.
            - ``MEANhistogram`` specifies that reference levels are relative to the histogram mean
              BASE and TOP.
            - ``MODEhistogram`` specifies that reference levels are relative to the histogram mode
              BASE and TOP.
            - ``EYEhistogram`` specifies that reverence levels are relative to the eye histogram
              BASE and TOP.
        """  # noqa: E501
        return self._basetop

    @property
    def method(self) -> MeasurementMeasItemReflevels1Method:
        """Return the ``MEASUrement:MEAS<x>:REFLevels1:METHod`` command.

        Description:
            - This command sets or queries the method used to calculate reference levels for the
              measurement. The measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:REFLevels1:METHod?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:METHod?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:METHod value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFLevels1:METHod {PERCent|ABSolute}
            - MEASUrement:MEAS<x>:REFLevels1:METHod?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``PERCent`` specifies that the reference levels are calculated as a percent relative
              to HIGH and LOW. The percentages are defined using the
              ``MEASUrement:MEAS<x>:REFLevel:PERCent`` commands.
            - ``ABSolute`` specifies that the reference levels are set explicitly using the
              ``MEASUrement:MEAS<x>:REFLevel:ABSolute`` commands. This method is useful when precise
              values are required.
        """
        return self._method

    @property
    def percent(self) -> MeasurementMeasItemReflevels1Percent:
        """Return the ``MEASUrement:MEAS<x>:REFLevels1:PERCent`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:PERCent?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels1:PERCent?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Info:
            - ``MEAS<x>`` specifies the measurement number.

        Sub-properties:
            - ``.fallhigh``: The ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLHigh`` command.
            - ``.falllow``: The ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLLow`` command.
            - ``.fallmid``: The ``MEASUrement:MEAS<x>:REFLevels1:PERCent:FALLMid`` command.
            - ``.hysteresis``: The ``MEASUrement:MEAS<x>:REFLevels1:PERCent:HYSTeresis`` command.
            - ``.risehigh``: The ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEHigh`` command.
            - ``.riselow``: The ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISELow`` command.
            - ``.risemid``: The ``MEASUrement:MEAS<x>:REFLevels1:PERCent:RISEMid`` command.
            - ``.type``: The ``MEASUrement:MEAS<x>:REFLevels1:PERCent:TYPE`` command.
        """
        return self._percent


class MeasurementMeasItemReflevels(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevels`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:REFLevels?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:REFLevels?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``MEAS<x>`` specifies the measurement number.

    Properties:
        - ``.absolute``: The ``MEASUrement:MEAS<x>:REFLevels:ABSolute`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._absolute = MeasurementMeasItemReflevelsAbsolute(
            device, f"{self._cmd_syntax}:ABSolute"
        )

    @property
    def absolute(self) -> MeasurementMeasItemReflevelsAbsolute:
        """Return the ``MEASUrement:MEAS<x>:REFLevels:ABSolute`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels:ABSolute?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevels:ABSolute?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Info:
            - ``MEAS<x>`` specifies the measurement number.

        Sub-properties:
            - ``.fallhigh``: The ``MEASUrement:MEAS<x>:REFLevels:ABSolute:FALLHigh`` command.
        """
        return self._absolute


class MeasurementMeasItemPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:POLarity`` command.

    Description:
        - This command sets or queries the polarity for the measurement when the measurement type is
          burst width. Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:POLarity value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:POLarity {NORMal|INVerted}
        - MEASUrement:MEAS<x>:POLarity?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``NORMal`` specifies normal polarity.
        - ``INVerted`` specifies inverted polarity.
    """


class MeasurementMeasItemPerfreqEdge(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:PERFREQ:EDGE`` command.

    Description:
        - This command sets or queries the edge type of a Period/Frequency measurement. The
          measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:PERFREQ:EDGE?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:PERFREQ:EDGE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:PERFREQ:EDGE value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:PERFREQ:EDGE {FIRST|RISE|FALL}
        - MEASUrement:MEAS<x>:PERFREQ:EDGE?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``FIRST`` computes the measurement between Rising edges if the first edge is Rising.
          Computes the measurement between Falling edges if the first edge is Falling.
        - ``RISE`` computes the measurement between Rising edges.
        - ``FALL`` computes the measurement between Falling edges.
    """


class MeasurementMeasItemPerfreq(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:PERFREQ`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:PERFREQ?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:PERFREQ?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``MEAS<x>`` specifies the measurement number.

    Properties:
        - ``.edge``: The ``MEASUrement:MEAS<x>:PERFREQ:EDGE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._edge = MeasurementMeasItemPerfreqEdge(device, f"{self._cmd_syntax}:EDGE")

    @property
    def edge(self) -> MeasurementMeasItemPerfreqEdge:
        """Return the ``MEASUrement:MEAS<x>:PERFREQ:EDGE`` command.

        Description:
            - This command sets or queries the edge type of a Period/Frequency measurement. The
              measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:PERFREQ:EDGE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:PERFREQ:EDGE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:PERFREQ:EDGE value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:PERFREQ:EDGE {FIRST|RISE|FALL}
            - MEASUrement:MEAS<x>:PERFREQ:EDGE?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``FIRST`` computes the measurement between Rising edges if the first edge is Rising.
              Computes the measurement between Falling edges if the first edge is Falling.
            - ``RISE`` computes the measurement between Rising edges.
            - ``FALL`` computes the measurement between Falling edges.
        """
        return self._edge


class MeasurementMeasItemPassfailwhen(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:PASSFAILWHEN`` command.

    Description:
        - This command sets or returns the condition on which a measurement test fails. Measurements
          are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:PASSFAILWHEN?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:PASSFAILWHEN?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:PASSFAILWHEN value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:PASSFAILWHEN {LESSthan|GREATERthan|Equals|NOTEQuals|INSIDErange|OUTSIDErange}
        - MEASUrement:MEAS<x>:PASSFAILWHEN?
        ```

    Info:
        - ``LESSthan`` sets the condition for measurement test failure as less than the given limit.
          This is the default value.
        - ``GREATERthan`` sets the condition for measurement test failure as greater than the given
          limit.
        - ``Equals`` sets the condition for measurement test failure as equals the given limit.
        - ``NOTEQuals`` sets the condition for measurement test failure as not equal to the given
          limit.
        - ``INSIDErange`` sets the condition for measurement test failure as inside the limit range.
        - ``OUTSIDErange`` sets the condition for measurement test failure as outside the limit
          range.
    """  # noqa: E501


class MeasurementMeasItemPassfailmargin(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:PASSFAILMARgin`` command.

    Description:
        - This command returns or sets the allowed margin for limit comparisons for all pass/fail
          checks. This is given as a percentage with a default value of 0.05 representing 5%.
          Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:PASSFAILMARgin?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:PASSFAILMARgin?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:PASSFAILMARgin value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:PASSFAILMARgin <NR2>
        - MEASUrement:MEAS<x>:PASSFAILMARgin?
        ```

    Info:
        - ``<NR2>`` sets the allowed margin for limit comparisons for all pass/fail checks. The
          margin as a percentage of the limit.
    """


class MeasurementMeasItemPassfaillowlimit(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:PASSFAILLOWlimit`` command.

    Description:
        - This command returns or sets the low limit for a measurement test. Used as the test value
          when the 'fail when' criteria is set to 'less than' or 'greater than'. Measurements are
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:PASSFAILLOWlimit?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:PASSFAILLOWlimit?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:PASSFAILLOWlimit value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:PASSFAILLOWlimit <NR2>
        - MEASUrement:MEAS<x>:PASSFAILLOWlimit?
        ```

    Info:
        - ``<NR2>`` sets the low limit for a measurement test. The limit is a number which a
          measurement result will be tested against.
    """


class MeasurementMeasItemPassfaillimit(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:PASSFAILLIMit`` command.

    Description:
        - This command returns or sets the limit for a measurement test. Used as the test value when
          the 'fail when' criteria is set to 'less than' or 'greater than'. Measurements are
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:PASSFAILLIMit?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:PASSFAILLIMit?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:PASSFAILLIMit value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:PASSFAILLIMit <NR2>
        - MEASUrement:MEAS<x>:PASSFAILLIMit?
        ```

    Info:
        - ``<NR2>`` sets the limit for a measurement test. The limit is a number which a measurement
          result will be tested against.
    """


class MeasurementMeasItemPassfailhighlimit(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:PASSFAILHIGHlimit`` command.

    Description:
        - This command returns or sets the high limit for a measurement test. Used as the test value
          when the 'fail when' criteria is set to 'less than' or 'greater than'. Measurements are
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:PASSFAILHIGHlimit?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:PASSFAILHIGHlimit?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:PASSFAILHIGHlimit value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:PASSFAILHIGHlimit <NR2>
        - MEASUrement:MEAS<x>:PASSFAILHIGHlimit?
        ```

    Info:
        - ``<NR2>`` sets the high limit for a measurement test. The high limit is a number which a
          measurement result will be tested against.
    """


class MeasurementMeasItemPassfailenabled(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:PASSFAILENabled`` command.

    Description:
        - This command returns or sets the pass/fail test enable status. If enabled, this will turn
          on pass fail testing for the specified measurement. Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:PASSFAILENabled?``
          query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:PASSFAILENabled?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:PASSFAILENabled value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:PASSFAILENabled <NR1>
        - MEASUrement:MEAS<x>:PASSFAILENabled?
        ```

    Info:
        - ``<NR1>`` enables or disables pass fail testing for the specified measurement. A value of
          1 enables and a value of 0 disables.
    """


class MeasurementMeasItemLowrefvoltage(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:LOWREFVoltage`` command.

    Description:
        - This command sets or queries the low reference voltage value for the 'time outside level'
          measurement. Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:LOWREFVoltage?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:LOWREFVoltage?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:LOWREFVoltage value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:LOWREFVoltage <NR3>
        - MEASUrement:MEAS<x>:LOWREFVoltage?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``<NR3>`` is the low reference voltage value for the selected configuration.
    """


class MeasurementMeasItemLabel(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:LABel`` command.

    Description:
        - This command sets or queries the label for the measurement. As the label can contain non
          7-bit ASCII text, it is stored in Percent Encoding format. The measurement number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:LABel?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:LABel value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:LABel <QString>
        - MEASUrement:MEAS<x>:LABel?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``<QString>`` is the measurement label.
    """

    _WRAP_ARG_WITH_QUOTES = True


class MeasurementMeasItemIdletime(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:IDLETime`` command.

    Description:
        - This command sets or queries the idle time for the measurement when the measurement type
          is burst width. Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:IDLETime?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:IDLETime?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:IDLETime value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:IDLETime <NR3>
        - MEASUrement:MEAS<x>:IDLETime?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``<NR3>`` is the idle time.
    """


class MeasurementMeasItemHighrefvoltage(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:HIGHREFVoltage`` command.

    Description:
        - This command sets or queries the high reference voltage value for the 'time outside level'
          measurement. Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:HIGHREFVoltage?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:HIGHREFVoltage?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:HIGHREFVoltage value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:HIGHREFVoltage <NR3>
        - MEASUrement:MEAS<x>:HIGHREFVoltage?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``<NR3>`` is the high reference voltage value for the selected configuration.
    """


class MeasurementMeasItemGlobalref(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:GLOBalref`` command.

    Description:
        - This command sets or queries the reference levels global flag for the measurement.
          Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:GLOBalref?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:GLOBalref?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:GLOBalref value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:GLOBalref {OFF|ON|0|1}
        - MEASUrement:MEAS<x>:GLOBalref?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``OFF`` allows ref levels to be set separately for each measurement.
        - ``ON`` applies the same ref levels to all measurements.
        - ``0`` allows ref levels to be set separately for each measurement.
        - ``1`` applies the same ref levels to all measurements.
    """


class MeasurementMeasItemGatingStarttime(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:GATing:STARTtime`` command.

    Description:
        - Sets or queries the start gate time for the measurement when using Local gating.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:GATing:STARTtime?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:GATing:STARTtime?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:GATing:STARTtime value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:GATing:STARTtime <NR3>
        - MEASUrement:MEAS<x>:GATing:STARTtime?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``<NR3>`` is the time gating start gate time in seconds. The valid range is -10000 s to
          10000 s.
    """


class MeasurementMeasItemGatingSearchsource(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:GATing:SEARCHSource`` command.

    Description:
        - This command sets or queries the gating search source when the gating type is search. The
          measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:GATing:SEARCHSource?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:GATing:SEARCHSource?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:GATing:SEARCHSource value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:GATing:SEARCHSource SEARCH1
        - MEASUrement:MEAS<x>:GATing:SEARCHSource?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``SEARCH1`` is the gating source for search gating.
    """


class MeasurementMeasItemGatingMidref(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:GATing:MIDRef`` command.

    Description:
        - This command sets or queries the gating mid ref value when the gating type is logic.
          Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:GATing:MIDRef?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:GATing:MIDRef?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:GATing:MIDRef value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:GATing:MIDRef <NR3>
        - MEASUrement:MEAS<x>:GATing:MIDRef?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``<NR3>`` is the mid ref value for gating.
    """


class MeasurementMeasItemGatingLogicsource(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:GATing:LOGICSource`` command.

    Description:
        - This command sets or queries the gating data source when the gating type is logic. The
          measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:GATing:LOGICSource?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:GATing:LOGICSource?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:GATing:LOGICSource value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:GATing:LOGICSource {CH<x>|MATH<x>|REF<x>}
        - MEASUrement:MEAS<x>:GATing:LOGICSource?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
    """


class MeasurementMeasItemGatingHysteresis(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:GATing:HYSTeresis`` command.

    Description:
        - This command sets or queries the gating hysteresis value when the gating type is logic.
          Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:GATing:HYSTeresis?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:GATing:HYSTeresis?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:GATing:HYSTeresis value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:GATing:HYSTeresis <NR3>
        - MEASUrement:MEAS<x>:GATing:HYSTeresis?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``<NR3>`` is the gating hysteresis.
    """


class MeasurementMeasItemGatingGlobal(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:GATing:GLOBal`` command.

    Description:
        - This command sets or queries the gating settings global flag. Measurements are specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:GATing:GLOBal?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:GATing:GLOBal?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:GATing:GLOBal value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:GATing:GLOBal {OFF|ON|0|1}
        - MEASUrement:MEAS<x>:GATing:GLOBal?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``OFF`` specifies gate settings can be changed independently for each individual
          measurement.
        - ``ON`` applies global gate settings to all the measurements' gate settings.
        - ``0`` specifies gate settings can be changed independently for each individual
          measurement.
        - ``1`` applies global gate settings to all the measurements' gate settings.
    """


class MeasurementMeasItemGatingEndtime(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:GATing:ENDtime`` command.

    Description:
        - Sets or queries the end gate time for the measurement when using Local gating.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:GATing:ENDtime?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:GATing:ENDtime?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:GATing:ENDtime value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:GATing:ENDtime <NR3>
        - MEASUrement:MEAS<x>:GATing:ENDtime?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``<NR3>`` is the time gating end gate time in seconds. The valid range is -10000 s to
          10000 s.
    """


class MeasurementMeasItemGatingActive(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:GATing:ACTive`` command.

    Description:
        - This command sets or queries the gating active level when the gating type is logic.
          Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:GATing:ACTive?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:GATing:ACTive?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:GATing:ACTive value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:GATing:ACTive {HIGH|LOW}
        - MEASUrement:MEAS<x>:GATing:ACTive?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``HIGH`` takes a measurement when logic gating is High.
        - ``LOW`` takes a measurement when logic gating Low.
    """


#  pylint: disable=too-many-instance-attributes
class MeasurementMeasItemGating(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:GATing`` command.

    Description:
        - This command sets or queries the gating type for the measurement. Measurements are
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:GATing?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:GATing?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:GATing value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:GATing {NONE|SCREEN|CURSor|LOGic|SEARch|TIMe}
        - MEASUrement:MEAS<x>:GATing?
        ```

    Info:
        - ``MEAS<x>`` is the measurement number for which to return a value.
        - ``NONE`` specifies measurements are taken across the entire record.
        - ``SCREEN`` turns on gating, using the left and right edges of the screen.
        - ``CURSor`` limits measurements to the portion of the waveform between the vertical bar
          cursors, even if they are off screen.
        - ``LOGic`` specifies that measurements are taken only when the logical state of other
          waveforms is true.
        - ``SEARch`` specifies that measurements are taken only where the results of a user
          specified search are found.
        - ``TIMe`` limits measurements to the portion of the waveform between the Start and End gate
          times.

    Properties:
        - ``.active``: The ``MEASUrement:MEAS<x>:GATing:ACTive`` command.
        - ``.endtime``: The ``MEASUrement:MEAS<x>:GATing:ENDtime`` command.
        - ``.global``: The ``MEASUrement:MEAS<x>:GATing:GLOBal`` command.
        - ``.hysteresis``: The ``MEASUrement:MEAS<x>:GATing:HYSTeresis`` command.
        - ``.logicsource``: The ``MEASUrement:MEAS<x>:GATing:LOGICSource`` command.
        - ``.midref``: The ``MEASUrement:MEAS<x>:GATing:MIDRef`` command.
        - ``.searchsource``: The ``MEASUrement:MEAS<x>:GATing:SEARCHSource`` command.
        - ``.starttime``: The ``MEASUrement:MEAS<x>:GATing:STARTtime`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._active = MeasurementMeasItemGatingActive(device, f"{self._cmd_syntax}:ACTive")
        self._endtime = MeasurementMeasItemGatingEndtime(device, f"{self._cmd_syntax}:ENDtime")
        self._global = MeasurementMeasItemGatingGlobal(device, f"{self._cmd_syntax}:GLOBal")
        self._hysteresis = MeasurementMeasItemGatingHysteresis(
            device, f"{self._cmd_syntax}:HYSTeresis"
        )
        self._logicsource = MeasurementMeasItemGatingLogicsource(
            device, f"{self._cmd_syntax}:LOGICSource"
        )
        self._midref = MeasurementMeasItemGatingMidref(device, f"{self._cmd_syntax}:MIDRef")
        self._searchsource = MeasurementMeasItemGatingSearchsource(
            device, f"{self._cmd_syntax}:SEARCHSource"
        )
        self._starttime = MeasurementMeasItemGatingStarttime(
            device, f"{self._cmd_syntax}:STARTtime"
        )

    @property
    def active(self) -> MeasurementMeasItemGatingActive:
        """Return the ``MEASUrement:MEAS<x>:GATing:ACTive`` command.

        Description:
            - This command sets or queries the gating active level when the gating type is logic.
              Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:GATing:ACTive?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:GATing:ACTive?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:GATing:ACTive value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:GATing:ACTive {HIGH|LOW}
            - MEASUrement:MEAS<x>:GATing:ACTive?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``HIGH`` takes a measurement when logic gating is High.
            - ``LOW`` takes a measurement when logic gating Low.
        """
        return self._active

    @property
    def endtime(self) -> MeasurementMeasItemGatingEndtime:
        """Return the ``MEASUrement:MEAS<x>:GATing:ENDtime`` command.

        Description:
            - Sets or queries the end gate time for the measurement when using Local gating.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:GATing:ENDtime?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:GATing:ENDtime?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:GATing:ENDtime value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:GATing:ENDtime <NR3>
            - MEASUrement:MEAS<x>:GATing:ENDtime?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``<NR3>`` is the time gating end gate time in seconds. The valid range is -10000 s to
              10000 s.
        """
        return self._endtime

    @property
    def global_(self) -> MeasurementMeasItemGatingGlobal:
        """Return the ``MEASUrement:MEAS<x>:GATing:GLOBal`` command.

        Description:
            - This command sets or queries the gating settings global flag. Measurements are
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:GATing:GLOBal?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:GATing:GLOBal?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:GATing:GLOBal value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:GATing:GLOBal {OFF|ON|0|1}
            - MEASUrement:MEAS<x>:GATing:GLOBal?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``OFF`` specifies gate settings can be changed independently for each individual
              measurement.
            - ``ON`` applies global gate settings to all the measurements' gate settings.
            - ``0`` specifies gate settings can be changed independently for each individual
              measurement.
            - ``1`` applies global gate settings to all the measurements' gate settings.
        """
        return self._global

    @property
    def hysteresis(self) -> MeasurementMeasItemGatingHysteresis:
        """Return the ``MEASUrement:MEAS<x>:GATing:HYSTeresis`` command.

        Description:
            - This command sets or queries the gating hysteresis value when the gating type is
              logic. Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:GATing:HYSTeresis?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:GATing:HYSTeresis?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:GATing:HYSTeresis value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:GATing:HYSTeresis <NR3>
            - MEASUrement:MEAS<x>:GATing:HYSTeresis?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``<NR3>`` is the gating hysteresis.
        """
        return self._hysteresis

    @property
    def logicsource(self) -> MeasurementMeasItemGatingLogicsource:
        """Return the ``MEASUrement:MEAS<x>:GATing:LOGICSource`` command.

        Description:
            - This command sets or queries the gating data source when the gating type is logic. The
              measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:GATing:LOGICSource?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:GATing:LOGICSource?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:GATing:LOGICSource value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:GATing:LOGICSource {CH<x>|MATH<x>|REF<x>}
            - MEASUrement:MEAS<x>:GATing:LOGICSource?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
        """
        return self._logicsource

    @property
    def midref(self) -> MeasurementMeasItemGatingMidref:
        """Return the ``MEASUrement:MEAS<x>:GATing:MIDRef`` command.

        Description:
            - This command sets or queries the gating mid ref value when the gating type is logic.
              Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:GATing:MIDRef?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:GATing:MIDRef?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:GATing:MIDRef value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:GATing:MIDRef <NR3>
            - MEASUrement:MEAS<x>:GATing:MIDRef?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``<NR3>`` is the mid ref value for gating.
        """
        return self._midref

    @property
    def searchsource(self) -> MeasurementMeasItemGatingSearchsource:
        """Return the ``MEASUrement:MEAS<x>:GATing:SEARCHSource`` command.

        Description:
            - This command sets or queries the gating search source when the gating type is search.
              The measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:GATing:SEARCHSource?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:GATing:SEARCHSource?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:GATing:SEARCHSource value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:GATing:SEARCHSource SEARCH1
            - MEASUrement:MEAS<x>:GATing:SEARCHSource?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``SEARCH1`` is the gating source for search gating.
        """
        return self._searchsource

    @property
    def starttime(self) -> MeasurementMeasItemGatingStarttime:
        """Return the ``MEASUrement:MEAS<x>:GATing:STARTtime`` command.

        Description:
            - Sets or queries the start gate time for the measurement when using Local gating.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:GATing:STARTtime?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:GATing:STARTtime?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:GATing:STARTtime value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:GATing:STARTtime <NR3>
            - MEASUrement:MEAS<x>:GATing:STARTtime?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``<NR3>`` is the time gating start gate time in seconds. The valid range is -10000 s
              to 10000 s.
        """
        return self._starttime


class MeasurementMeasItemFromedge(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:FROMedge`` command.

    Description:
        - This command sets or queries the from edge type for the measurement. Measurements are
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:FROMedge?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:FROMedge?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:FROMedge value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:FROMedge {RISe|FALL|BOTH}
        - MEASUrement:MEAS<x>:FROMedge?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``FALL`` specifies the falling edge of the waveform.
        - ``RISE`` specifies the rising edge of the waveform.
        - ``BOTH`` specifies both the rising and falling edges of the waveform.
    """


class MeasurementMeasItemFromedgesearchdirect(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:FROMEDGESEARCHDIRect`` command.

    Description:
        - This command sets or queries the from edge search direction for the measurement.
          Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:FROMEDGESEARCHDIRect?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:FROMEDGESEARCHDIRect?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:FROMEDGESEARCHDIRect value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:FROMEDGESEARCHDIRect {FORWard|BACKWard}
        - MEASUrement:MEAS<x>:FROMEDGESEARCHDIRect?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``FORWard`` specifies a forward search from the edge.
        - ``BACKWard`` specifies a backward search from the edge.
    """


class MeasurementMeasItemFailcount(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:FAILCount`` command.

    Description:
        - This command returns the number of measurement failures, if applicable, for the selected
          measurement. The measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:FAILCount?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:FAILCount?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:FAILCount?
        ```
    """


class MeasurementMeasItemEdgesTolevel(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:EDGES:TOLevel`` command.

    Description:
        - This command sets or queries the 'to level' edge for the measurement. Measurements are
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:EDGES:TOLevel?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:EDGES:TOLevel?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:EDGES:TOLevel value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:EDGES:TOLevel {HIGH|MID|LOW}
        - MEASUrement:MEAS<x>:EDGES:TOLevel?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``HIGH`` specifies the HIGH level.
        - ``MID`` specifies the MID level.
        - ``LOW`` specifies the LOW level.
    """


class MeasurementMeasItemEdgesSlewratemethod(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:EDGES:SLEWRATEMethod`` command.

    Description:
        - This command sets or queries the slew rate method for the measurement. Measurements are
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:EDGES:SLEWRATEMethod?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:EDGES:SLEWRATEMethod?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:EDGES:SLEWRATEMethod value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:EDGES:SLEWRATEMethod {NOMinal|DDR}
        - MEASUrement:MEAS<x>:EDGES:SLEWRATEMethod?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``NOMinal`` specifies the nominal slew rate method.
        - ``DDR`` specifies the DDR slew rate method.
    """


class MeasurementMeasItemEdgesN(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:EDGES:N`` command.

    Description:
        - The command sets or queries the number of accumulation cycles for the measurement when the
          measurement type is nperiod. Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:EDGES:N?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:EDGES:N?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:EDGES:N value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:EDGES:N <NR3>
        - MEASUrement:MEAS<x>:EDGES:N?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``<NR3>`` is the maximum number of edges used by the measurement.
    """


class MeasurementMeasItemEdgesLevel(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:EDGES:LEVel`` command.

    Description:
        - This sets or queries the level type for the 'time outside level' measurement. Measurements
          are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:EDGES:LEVel?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:EDGES:LEVel?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:EDGES:LEVel value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:EDGES:LEVel {HIGH|LOW|BOTH}
        - MEASUrement:MEAS<x>:EDGES:LEVel?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``HIGH`` specifies the HIGH level.
        - ``LOW`` specifies the LOW level.
        - ``BOTH`` specifies both the HIGH and LOW level.
    """


class MeasurementMeasItemEdgesFromlevel(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:EDGES:FROMLevel`` command.

    Description:
        - This command sets or queries the 'from level' edge for the measurement. Measurements are
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:EDGES:FROMLevel?``
          query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:EDGES:FROMLevel?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:EDGES:FROMLevel value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:EDGES:FROMLevel {MID|LOW|HIGH}
        - MEASUrement:MEAS<x>:EDGES:FROMLevel?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``MID`` specifies the MID level.
        - ``HIGH`` specifies the HIGH level.
        - ``LOW`` specifies the LOW level.
    """


class MeasurementMeasItemEdges(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:EDGES`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:EDGES?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:EDGES?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``MEAS<x>`` specifies the measurement number.

    Properties:
        - ``.fromlevel``: The ``MEASUrement:MEAS<x>:EDGES:FROMLevel`` command.
        - ``.level``: The ``MEASUrement:MEAS<x>:EDGES:LEVel`` command.
        - ``.n``: The ``MEASUrement:MEAS<x>:EDGES:N`` command.
        - ``.slewratemethod``: The ``MEASUrement:MEAS<x>:EDGES:SLEWRATEMethod`` command.
        - ``.tolevel``: The ``MEASUrement:MEAS<x>:EDGES:TOLevel`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fromlevel = MeasurementMeasItemEdgesFromlevel(device, f"{self._cmd_syntax}:FROMLevel")
        self._level = MeasurementMeasItemEdgesLevel(device, f"{self._cmd_syntax}:LEVel")
        self._n = MeasurementMeasItemEdgesN(device, f"{self._cmd_syntax}:N")
        self._slewratemethod = MeasurementMeasItemEdgesSlewratemethod(
            device, f"{self._cmd_syntax}:SLEWRATEMethod"
        )
        self._tolevel = MeasurementMeasItemEdgesTolevel(device, f"{self._cmd_syntax}:TOLevel")

    @property
    def fromlevel(self) -> MeasurementMeasItemEdgesFromlevel:
        """Return the ``MEASUrement:MEAS<x>:EDGES:FROMLevel`` command.

        Description:
            - This command sets or queries the 'from level' edge for the measurement. Measurements
              are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:EDGES:FROMLevel?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:EDGES:FROMLevel?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:EDGES:FROMLevel value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:EDGES:FROMLevel {MID|LOW|HIGH}
            - MEASUrement:MEAS<x>:EDGES:FROMLevel?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``MID`` specifies the MID level.
            - ``HIGH`` specifies the HIGH level.
            - ``LOW`` specifies the LOW level.
        """
        return self._fromlevel

    @property
    def level(self) -> MeasurementMeasItemEdgesLevel:
        """Return the ``MEASUrement:MEAS<x>:EDGES:LEVel`` command.

        Description:
            - This sets or queries the level type for the 'time outside level' measurement.
              Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:EDGES:LEVel?``
              query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:EDGES:LEVel?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:EDGES:LEVel value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:EDGES:LEVel {HIGH|LOW|BOTH}
            - MEASUrement:MEAS<x>:EDGES:LEVel?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``HIGH`` specifies the HIGH level.
            - ``LOW`` specifies the LOW level.
            - ``BOTH`` specifies both the HIGH and LOW level.
        """
        return self._level

    @property
    def n(self) -> MeasurementMeasItemEdgesN:
        """Return the ``MEASUrement:MEAS<x>:EDGES:N`` command.

        Description:
            - The command sets or queries the number of accumulation cycles for the measurement when
              the measurement type is nperiod. Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:EDGES:N?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:EDGES:N?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:EDGES:N value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:EDGES:N <NR3>
            - MEASUrement:MEAS<x>:EDGES:N?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``<NR3>`` is the maximum number of edges used by the measurement.
        """
        return self._n

    @property
    def slewratemethod(self) -> MeasurementMeasItemEdgesSlewratemethod:
        """Return the ``MEASUrement:MEAS<x>:EDGES:SLEWRATEMethod`` command.

        Description:
            - This command sets or queries the slew rate method for the measurement. Measurements
              are specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:EDGES:SLEWRATEMethod?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:EDGES:SLEWRATEMethod?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:EDGES:SLEWRATEMethod value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:EDGES:SLEWRATEMethod {NOMinal|DDR}
            - MEASUrement:MEAS<x>:EDGES:SLEWRATEMethod?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``NOMinal`` specifies the nominal slew rate method.
            - ``DDR`` specifies the DDR slew rate method.
        """
        return self._slewratemethod

    @property
    def tolevel(self) -> MeasurementMeasItemEdgesTolevel:
        """Return the ``MEASUrement:MEAS<x>:EDGES:TOLevel`` command.

        Description:
            - This command sets or queries the 'to level' edge for the measurement. Measurements are
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:EDGES:TOLevel?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:EDGES:TOLevel?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:EDGES:TOLevel value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:EDGES:TOLevel {HIGH|MID|LOW}
            - MEASUrement:MEAS<x>:EDGES:TOLevel?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``HIGH`` specifies the HIGH level.
            - ``MID`` specifies the MID level.
            - ``LOW`` specifies the LOW level.
        """
        return self._tolevel


class MeasurementMeasItemEdgeincre(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:EDGEIncre`` command.

    Description:
        - This command sets or queries the edge increment value for the measurement. Measurements
          are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:EDGEIncre?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:EDGEIncre?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:EDGEIncre value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:EDGEIncre <NR3>
        - MEASUrement:MEAS<x>:EDGEIncre?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``<NR3>`` is the measurements edge increment value.
    """


class MeasurementMeasItemEdgeItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:EDGE<x>`` command.

    Description:
        - This command sets or queries the type of the specified edge, rise or fall, for the
          measurement. The measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:EDGE<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:EDGE<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:EDGE<x> value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:EDGE<x> {RISE|FALL|BOTH}
        - MEASUrement:MEAS<x>:EDGE<x>?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``EDGE<x>`` specifies the edge number.
        - ``RISE`` specifies the rising edge.
        - ``FALL`` specifies the falling edge.
        - ``BOTH`` specifies either the rising or falling edge.
    """


class MeasurementMeasItemDisplaystatEnable(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:DISPlaystat:ENABle`` command.

    Description:
        - This command turns on and off display of statistics in measurement badges in the user
          interface. This command affects only the display of statistics, basic-statistics are
          computed regardless of the state of this command. Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:DISPlaystat:ENABle?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:DISPlaystat:ENABle?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:DISPlaystat:ENABle value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:DISPlaystat:ENABle {ON|OFF|<NR1>}
        - MEASUrement:MEAS<x>:DISPlaystat:ENABle?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``OFF`` turns off the display of statistics in measurement badges.
        - ``ON`` turns on the display of statistics in measurement badges.
        - ``<NR1>`` = 0 turns off the display of statistics in the measurement badge, any other
          value turns on the display of statistics.
    """


class MeasurementMeasItemDisplaystat(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:DISPlaystat`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:DISPlaystat?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:DISPlaystat?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``MEAS<x>`` specifies the measurement number.

    Properties:
        - ``.enable``: The ``MEASUrement:MEAS<x>:DISPlaystat:ENABle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._enable = MeasurementMeasItemDisplaystatEnable(device, f"{self._cmd_syntax}:ENABle")

    @property
    def enable(self) -> MeasurementMeasItemDisplaystatEnable:
        """Return the ``MEASUrement:MEAS<x>:DISPlaystat:ENABle`` command.

        Description:
            - This command turns on and off display of statistics in measurement badges in the user
              interface. This command affects only the display of statistics, basic-statistics are
              computed regardless of the state of this command. Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:DISPlaystat:ENABle?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:DISPlaystat:ENABle?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:DISPlaystat:ENABle value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:DISPlaystat:ENABle {ON|OFF|<NR1>}
            - MEASUrement:MEAS<x>:DISPlaystat:ENABle?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``OFF`` turns off the display of statistics in measurement badges.
            - ``ON`` turns on the display of statistics in measurement badges.
            - ``<NR1>`` = 0 turns off the display of statistics in the measurement badge, any other
              value turns on the display of statistics.
        """
        return self._enable


class MeasurementMeasItemDelayEdgeItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:DELay:EDGE<x>`` command.

    Description:
        - This command sets or queries the 'to edge' type when EDGE<x> is EDGE1 and the 'from edge'
          type when EDGE<x> is EDG2, for the measurement when the measurement type is DELAY.
          Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:DELay:EDGE<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:DELay:EDGE<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:DELay:EDGE<x> value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:DELay:EDGE<x> {FALL|RISe|BOTH|SAMEas|OPPositeas}
        - MEASUrement:MEAS<x>:DELay:EDGE<x>?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``FALL`` specifies the falling edge of the waveform.
        - ``RISE`` specifies the rising edge of the waveform.
        - ``BOTH`` specifies both a rising and falling edge of the waveform.
        - ``SAMEas`` specifies that both edges of the waveform are the same.
        - ``OPPositeas`` specifies that the edges of the waveform are not the same.
    """


class MeasurementMeasItemDelay(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:DELay`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:DELay?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:DELay?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``MEAS<x>`` specifies the measurement number.

    Properties:
        - ``.edge``: The ``MEASUrement:MEAS<x>:DELay:EDGE<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._edge: Dict[int, MeasurementMeasItemDelayEdgeItem] = DefaultDictPassKeyToFactory(
            lambda x: MeasurementMeasItemDelayEdgeItem(device, f"{self._cmd_syntax}:EDGE{x}")
        )

    @property
    def edge(self) -> Dict[int, MeasurementMeasItemDelayEdgeItem]:
        """Return the ``MEASUrement:MEAS<x>:DELay:EDGE<x>`` command.

        Description:
            - This command sets or queries the 'to edge' type when EDGE<x> is EDGE1 and the 'from
              edge' type when EDGE<x> is EDG2, for the measurement when the measurement type is
              DELAY. Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:DELay:EDGE<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:DELay:EDGE<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:DELay:EDGE<x> value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:DELay:EDGE<x> {FALL|RISe|BOTH|SAMEas|OPPositeas}
            - MEASUrement:MEAS<x>:DELay:EDGE<x>?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``FALL`` specifies the falling edge of the waveform.
            - ``RISE`` specifies the rising edge of the waveform.
            - ``BOTH`` specifies both a rising and falling edge of the waveform.
            - ``SAMEas`` specifies that both edges of the waveform are the same.
            - ``OPPositeas`` specifies that the edges of the waveform are not the same.
        """
        return self._edge


class MeasurementMeasItemCcresultsCurrentacqStddev(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:STDDev`` command.

    Description:
        - This query-only command returns the standard deviation cycle-cycle for the specified
          measurement for the current acquisition. Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:STDDev?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:STDDev?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:STDDev?
        ```
    """


class MeasurementMeasItemCcresultsCurrentacqPopulation(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:POPUlation`` command.

    Description:
        - This query-only command returns the population of the cycle-cycle statistics for the
          specified measurement for the current acquisition. Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:POPUlation?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:POPUlation?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:POPUlation?
        ```
    """


class MeasurementMeasItemCcresultsCurrentacqPk2pk(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:PK2PK`` command.

    Description:
        - This query-only command returns the peak to peak cycle-cycle statistic for the specified
          measurement for the current acquisition. Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:PK2PK?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:PK2PK?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:PK2PK?
        ```
    """


class MeasurementMeasItemCcresultsCurrentacqMinimum(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MINimum`` command.

    Description:
        - This query-only command returns the minimum cycle-cycle value for the specified
          measurement for the current acquisition. Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MINimum?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MINimum?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MINimum?
        ```
    """


class MeasurementMeasItemCcresultsCurrentacqMean(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MEAN`` command.

    Description:
        - This query-only command returns the mean cycle-cycle value for the specified measurement
          for the current acquisition. Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MEAN?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MEAN?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MEAN?
        ```
    """


class MeasurementMeasItemCcresultsCurrentacqMaximum(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MAXimum`` command.

    Description:
        - This query-only command returns the maximum cycle-cycle value for the specified
          measurement for the current acquisition. Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MAXimum?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MAXimum?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MAXimum?
        ```
    """


class MeasurementMeasItemCcresultsCurrentacq(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.maximum``: The ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MAXimum`` command.
        - ``.mean``: The ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MEAN`` command.
        - ``.minimum``: The ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MINimum`` command.
        - ``.pk2pk``: The ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:PK2PK`` command.
        - ``.population``: The ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:POPUlation`` command.
        - ``.stddev``: The ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:STDDev`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._maximum = MeasurementMeasItemCcresultsCurrentacqMaximum(
            device, f"{self._cmd_syntax}:MAXimum"
        )
        self._mean = MeasurementMeasItemCcresultsCurrentacqMean(device, f"{self._cmd_syntax}:MEAN")
        self._minimum = MeasurementMeasItemCcresultsCurrentacqMinimum(
            device, f"{self._cmd_syntax}:MINimum"
        )
        self._pk2pk = MeasurementMeasItemCcresultsCurrentacqPk2pk(
            device, f"{self._cmd_syntax}:PK2PK"
        )
        self._population = MeasurementMeasItemCcresultsCurrentacqPopulation(
            device, f"{self._cmd_syntax}:POPUlation"
        )
        self._stddev = MeasurementMeasItemCcresultsCurrentacqStddev(
            device, f"{self._cmd_syntax}:STDDev"
        )

    @property
    def maximum(self) -> MeasurementMeasItemCcresultsCurrentacqMaximum:
        """Return the ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MAXimum`` command.

        Description:
            - This query-only command returns the maximum cycle-cycle value for the specified
              measurement for the current acquisition. Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MAXimum?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MAXimum?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MAXimum?
            ```
        """
        return self._maximum

    @property
    def mean(self) -> MeasurementMeasItemCcresultsCurrentacqMean:
        """Return the ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MEAN`` command.

        Description:
            - This query-only command returns the mean cycle-cycle value for the specified
              measurement for the current acquisition. Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MEAN?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MEAN?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MEAN?
            ```
        """
        return self._mean

    @property
    def minimum(self) -> MeasurementMeasItemCcresultsCurrentacqMinimum:
        """Return the ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MINimum`` command.

        Description:
            - This query-only command returns the minimum cycle-cycle value for the specified
              measurement for the current acquisition. Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MINimum?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MINimum?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MINimum?
            ```
        """
        return self._minimum

    @property
    def pk2pk(self) -> MeasurementMeasItemCcresultsCurrentacqPk2pk:
        """Return the ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:PK2PK`` command.

        Description:
            - This query-only command returns the peak to peak cycle-cycle statistic for the
              specified measurement for the current acquisition. Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:PK2PK?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:PK2PK?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:PK2PK?
            ```
        """
        return self._pk2pk

    @property
    def population(self) -> MeasurementMeasItemCcresultsCurrentacqPopulation:
        """Return the ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:POPUlation`` command.

        Description:
            - This query-only command returns the population of the cycle-cycle statistics for the
              specified measurement for the current acquisition. Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:POPUlation?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:POPUlation?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:POPUlation?
            ```
        """
        return self._population

    @property
    def stddev(self) -> MeasurementMeasItemCcresultsCurrentacqStddev:
        """Return the ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:STDDev`` command.

        Description:
            - This query-only command returns the standard deviation cycle-cycle for the specified
              measurement for the current acquisition. Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:STDDev?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:STDDev?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:STDDev?
            ```
        """
        return self._stddev


class MeasurementMeasItemCcresultsAllacqsStddev(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:STDDev`` command.

    Description:
        - This query-only command returns the standard deviation cycle-cycle for the specified
          measurement for all acquisitions. Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:STDDev?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:STDDev?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:STDDev?
        ```
    """


class MeasurementMeasItemCcresultsAllacqsPopulation(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:POPUlation`` command.

    Description:
        - This query-only command returns the population of all cycle-cycle statistics for the
          specified measurement for all acquisitions accumulated since statistics were last reset.
          Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:POPUlation?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:POPUlation?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:POPUlation?
        ```
    """


class MeasurementMeasItemCcresultsAllacqsPk2pk(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:PK2PK`` command.

    Description:
        - This query-only command returns the peak to peak cycle-cycle statistic for the specified
          measurement for all acquisitions. Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:PK2PK?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:PK2PK?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:PK2PK?
        ```
    """


class MeasurementMeasItemCcresultsAllacqsMinimum(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MINimum`` command.

    Description:
        - This query-only command returns the minimum cycle-cycle value for the specified
          measurement for all acquisitions. Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MINimum?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MINimum?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MINimum?
        ```
    """


class MeasurementMeasItemCcresultsAllacqsMean(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MEAN`` command.

    Description:
        - This query-only command returns the mean cycle-cycle value for the specified measurement
          for all acquisitions. Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MEAN?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MEAN?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MEAN?
        ```
    """


class MeasurementMeasItemCcresultsAllacqsMaximum(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MAXimum`` command.

    Description:
        - This query-only command returns the maximum cycle-cycle value for the specified
          measurement for all acquisitions. Measurements are specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MAXimum?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MAXimum?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MAXimum?
        ```
    """


class MeasurementMeasItemCcresultsAllacqs(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.maximum``: The ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MAXimum`` command.
        - ``.mean``: The ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MEAN`` command.
        - ``.minimum``: The ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MINimum`` command.
        - ``.pk2pk``: The ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:PK2PK`` command.
        - ``.population``: The ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:POPUlation`` command.
        - ``.stddev``: The ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:STDDev`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._maximum = MeasurementMeasItemCcresultsAllacqsMaximum(
            device, f"{self._cmd_syntax}:MAXimum"
        )
        self._mean = MeasurementMeasItemCcresultsAllacqsMean(device, f"{self._cmd_syntax}:MEAN")
        self._minimum = MeasurementMeasItemCcresultsAllacqsMinimum(
            device, f"{self._cmd_syntax}:MINimum"
        )
        self._pk2pk = MeasurementMeasItemCcresultsAllacqsPk2pk(device, f"{self._cmd_syntax}:PK2PK")
        self._population = MeasurementMeasItemCcresultsAllacqsPopulation(
            device, f"{self._cmd_syntax}:POPUlation"
        )
        self._stddev = MeasurementMeasItemCcresultsAllacqsStddev(
            device, f"{self._cmd_syntax}:STDDev"
        )

    @property
    def maximum(self) -> MeasurementMeasItemCcresultsAllacqsMaximum:
        """Return the ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MAXimum`` command.

        Description:
            - This query-only command returns the maximum cycle-cycle value for the specified
              measurement for all acquisitions. Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MAXimum?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MAXimum?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MAXimum?
            ```
        """
        return self._maximum

    @property
    def mean(self) -> MeasurementMeasItemCcresultsAllacqsMean:
        """Return the ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MEAN`` command.

        Description:
            - This query-only command returns the mean cycle-cycle value for the specified
              measurement for all acquisitions. Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MEAN?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MEAN?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MEAN?
            ```
        """
        return self._mean

    @property
    def minimum(self) -> MeasurementMeasItemCcresultsAllacqsMinimum:
        """Return the ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MINimum`` command.

        Description:
            - This query-only command returns the minimum cycle-cycle value for the specified
              measurement for all acquisitions. Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MINimum?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MINimum?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MINimum?
            ```
        """
        return self._minimum

    @property
    def pk2pk(self) -> MeasurementMeasItemCcresultsAllacqsPk2pk:
        """Return the ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:PK2PK`` command.

        Description:
            - This query-only command returns the peak to peak cycle-cycle statistic for the
              specified measurement for all acquisitions. Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:PK2PK?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:PK2PK?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:PK2PK?
            ```
        """
        return self._pk2pk

    @property
    def population(self) -> MeasurementMeasItemCcresultsAllacqsPopulation:
        """Return the ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:POPUlation`` command.

        Description:
            - This query-only command returns the population of all cycle-cycle statistics for the
              specified measurement for all acquisitions accumulated since statistics were last
              reset. Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:POPUlation?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:POPUlation?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:POPUlation?
            ```
        """
        return self._population

    @property
    def stddev(self) -> MeasurementMeasItemCcresultsAllacqsStddev:
        """Return the ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:STDDev`` command.

        Description:
            - This query-only command returns the standard deviation cycle-cycle for the specified
              measurement for all acquisitions. Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:STDDev?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:STDDev?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:STDDev?
            ```
        """
        return self._stddev


class MeasurementMeasItemCcresults(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:CCRESUlts`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:CCRESUlts?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:CCRESUlts?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.allacqs``: The ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs`` command tree.
        - ``.currentacq``: The ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._allacqs = MeasurementMeasItemCcresultsAllacqs(device, f"{self._cmd_syntax}:ALLAcqs")
        self._currentacq = MeasurementMeasItemCcresultsCurrentacq(
            device, f"{self._cmd_syntax}:CURRentacq"
        )

    @property
    def allacqs(self) -> MeasurementMeasItemCcresultsAllacqs:
        """Return the ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.maximum``: The ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MAXimum`` command.
            - ``.mean``: The ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MEAN`` command.
            - ``.minimum``: The ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:MINimum`` command.
            - ``.pk2pk``: The ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:PK2PK`` command.
            - ``.population``: The ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:POPUlation`` command.
            - ``.stddev``: The ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs:STDDev`` command.
        """
        return self._allacqs

    @property
    def currentacq(self) -> MeasurementMeasItemCcresultsCurrentacq:
        """Return the ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.maximum``: The ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MAXimum`` command.
            - ``.mean``: The ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MEAN`` command.
            - ``.minimum``: The ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:MINimum`` command.
            - ``.pk2pk``: The ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:PK2PK`` command.
            - ``.population``: The ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:POPUlation`` command.
            - ``.stddev``: The ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq:STDDev`` command.
        """
        return self._currentacq


class MeasurementMeasItemBurstedgtype(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:BURSTEDGTYPe`` command.

    Description:
        - This command sets or queries the burst edge type for the measurement. Measurements are
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:BURSTEDGTYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:BURSTEDGTYPe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:BURSTEDGTYPe value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:BURSTEDGTYPe {RISE|FALL}
        - MEASUrement:MEAS<x>:BURSTEDGTYPe?
        ```

    Info:
        - ``MEAS<x>`` specifies the measurement number.
        - ``RISE`` specifies a burst with a rising edge.
        - ``FALL`` specifies a burst with a falling edge.
    """


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class MeasurementMeasItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``MEAS<x>`` specifies the measurement number.

    Properties:
        - ``.burstedgtype``: The ``MEASUrement:MEAS<x>:BURSTEDGTYPe`` command.
        - ``.ccresults``: The ``MEASUrement:MEAS<x>:CCRESUlts`` command tree.
        - ``.delay``: The ``MEASUrement:MEAS<x>:DELay`` command tree.
        - ``.displaystat``: The ``MEASUrement:MEAS<x>:DISPlaystat`` command tree.
        - ``.edge``: The ``MEASUrement:MEAS<x>:EDGE<x>`` command.
        - ``.edgeincre``: The ``MEASUrement:MEAS<x>:EDGEIncre`` command.
        - ``.edges``: The ``MEASUrement:MEAS<x>:EDGES`` command tree.
        - ``.failcount``: The ``MEASUrement:MEAS<x>:FAILCount`` command.
        - ``.fromedgesearchdirect``: The ``MEASUrement:MEAS<x>:FROMEDGESEARCHDIRect`` command.
        - ``.fromedge``: The ``MEASUrement:MEAS<x>:FROMedge`` command.
        - ``.gating``: The ``MEASUrement:MEAS<x>:GATing`` command.
        - ``.globalref``: The ``MEASUrement:MEAS<x>:GLOBalref`` command.
        - ``.highrefvoltage``: The ``MEASUrement:MEAS<x>:HIGHREFVoltage`` command.
        - ``.idletime``: The ``MEASUrement:MEAS<x>:IDLETime`` command.
        - ``.label``: The ``MEASUrement:MEAS<x>:LABel`` command.
        - ``.lowrefvoltage``: The ``MEASUrement:MEAS<x>:LOWREFVoltage`` command.
        - ``.passfailenabled``: The ``MEASUrement:MEAS<x>:PASSFAILENabled`` command.
        - ``.passfailhighlimit``: The ``MEASUrement:MEAS<x>:PASSFAILHIGHlimit`` command.
        - ``.passfaillimit``: The ``MEASUrement:MEAS<x>:PASSFAILLIMit`` command.
        - ``.passfaillowlimit``: The ``MEASUrement:MEAS<x>:PASSFAILLOWlimit`` command.
        - ``.passfailmargin``: The ``MEASUrement:MEAS<x>:PASSFAILMARgin`` command.
        - ``.passfailwhen``: The ``MEASUrement:MEAS<x>:PASSFAILWHEN`` command.
        - ``.perfreq``: The ``MEASUrement:MEAS<x>:PERFREQ`` command tree.
        - ``.polarity``: The ``MEASUrement:MEAS<x>:POLarity`` command.
        - ``.reflevels``: The ``MEASUrement:MEAS<x>:REFLevels`` command tree.
        - ``.reflevels1``: The ``MEASUrement:MEAS<x>:REFLevels1`` command tree.
        - ``.refmode``: The ``MEASUrement:MEAS<x>:REFMode`` command.
        - ``.refvoltage``: The ``MEASUrement:MEAS<x>:REFVoltage`` command.
        - ``.results``: The ``MEASUrement:MEAS<x>:RESUlts`` command tree.
        - ``.signaltype``: The ``MEASUrement:MEAS<x>:SIGNALType`` command.
        - ``.source1``: The ``MEASUrement:MEAS<x>:SOUrce1`` command.
        - ``.status``: The ``MEASUrement:MEAS<x>:STATUS`` command.
        - ``.toedgesearchdirect``: The ``MEASUrement:MEAS<x>:TOEDGESEARCHDIRect`` command.
        - ``.toedge``: The ``MEASUrement:MEAS<x>:TOEdge`` command.
        - ``.transition``: The ``MEASUrement:MEAS<x>:TRANSition`` command.
        - ``.type``: The ``MEASUrement:MEAS<x>:TYPe`` command.
        - ``.xunit``: The ``MEASUrement:MEAS<x>:XUNIT`` command.
        - ``.yunit``: The ``MEASUrement:MEAS<x>:YUNIT`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._burstedgtype = MeasurementMeasItemBurstedgtype(
            device, f"{self._cmd_syntax}:BURSTEDGTYPe"
        )
        self._ccresults = MeasurementMeasItemCcresults(device, f"{self._cmd_syntax}:CCRESUlts")
        self._delay = MeasurementMeasItemDelay(device, f"{self._cmd_syntax}:DELay")
        self._displaystat = MeasurementMeasItemDisplaystat(
            device, f"{self._cmd_syntax}:DISPlaystat"
        )
        self._edge: Dict[int, MeasurementMeasItemEdgeItem] = DefaultDictPassKeyToFactory(
            lambda x: MeasurementMeasItemEdgeItem(device, f"{self._cmd_syntax}:EDGE{x}")
        )
        self._edgeincre = MeasurementMeasItemEdgeincre(device, f"{self._cmd_syntax}:EDGEIncre")
        self._edges = MeasurementMeasItemEdges(device, f"{self._cmd_syntax}:EDGES")
        self._failcount = MeasurementMeasItemFailcount(device, f"{self._cmd_syntax}:FAILCount")
        self._fromedgesearchdirect = MeasurementMeasItemFromedgesearchdirect(
            device, f"{self._cmd_syntax}:FROMEDGESEARCHDIRect"
        )
        self._fromedge = MeasurementMeasItemFromedge(device, f"{self._cmd_syntax}:FROMedge")
        self._gating = MeasurementMeasItemGating(device, f"{self._cmd_syntax}:GATing")
        self._globalref = MeasurementMeasItemGlobalref(device, f"{self._cmd_syntax}:GLOBalref")
        self._highrefvoltage = MeasurementMeasItemHighrefvoltage(
            device, f"{self._cmd_syntax}:HIGHREFVoltage"
        )
        self._idletime = MeasurementMeasItemIdletime(device, f"{self._cmd_syntax}:IDLETime")
        self._label = MeasurementMeasItemLabel(device, f"{self._cmd_syntax}:LABel")
        self._lowrefvoltage = MeasurementMeasItemLowrefvoltage(
            device, f"{self._cmd_syntax}:LOWREFVoltage"
        )
        self._passfailenabled = MeasurementMeasItemPassfailenabled(
            device, f"{self._cmd_syntax}:PASSFAILENabled"
        )
        self._passfailhighlimit = MeasurementMeasItemPassfailhighlimit(
            device, f"{self._cmd_syntax}:PASSFAILHIGHlimit"
        )
        self._passfaillimit = MeasurementMeasItemPassfaillimit(
            device, f"{self._cmd_syntax}:PASSFAILLIMit"
        )
        self._passfaillowlimit = MeasurementMeasItemPassfaillowlimit(
            device, f"{self._cmd_syntax}:PASSFAILLOWlimit"
        )
        self._passfailmargin = MeasurementMeasItemPassfailmargin(
            device, f"{self._cmd_syntax}:PASSFAILMARgin"
        )
        self._passfailwhen = MeasurementMeasItemPassfailwhen(
            device, f"{self._cmd_syntax}:PASSFAILWHEN"
        )
        self._perfreq = MeasurementMeasItemPerfreq(device, f"{self._cmd_syntax}:PERFREQ")
        self._polarity = MeasurementMeasItemPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._reflevels = MeasurementMeasItemReflevels(device, f"{self._cmd_syntax}:REFLevels")
        self._reflevels1 = MeasurementMeasItemReflevels1(device, f"{self._cmd_syntax}:REFLevels1")
        self._refmode = MeasurementMeasItemRefmode(device, f"{self._cmd_syntax}:REFMode")
        self._refvoltage = MeasurementMeasItemRefvoltage(device, f"{self._cmd_syntax}:REFVoltage")
        self._results = MeasurementMeasItemResults(device, f"{self._cmd_syntax}:RESUlts")
        self._signaltype = MeasurementMeasItemSignaltype(device, f"{self._cmd_syntax}:SIGNALType")
        self._source1 = MeasurementMeasItemSource1(device, f"{self._cmd_syntax}:SOUrce1")
        self._status = MeasurementMeasItemStatus(device, f"{self._cmd_syntax}:STATUS")
        self._toedgesearchdirect = MeasurementMeasItemToedgesearchdirect(
            device, f"{self._cmd_syntax}:TOEDGESEARCHDIRect"
        )
        self._toedge = MeasurementMeasItemToedge(device, f"{self._cmd_syntax}:TOEdge")
        self._transition = MeasurementMeasItemTransition(device, f"{self._cmd_syntax}:TRANSition")
        self._type = MeasurementMeasItemType(device, f"{self._cmd_syntax}:TYPe")
        self._xunit = MeasurementMeasItemXunit(device, f"{self._cmd_syntax}:XUNIT")
        self._yunit = MeasurementMeasItemYunit(device, f"{self._cmd_syntax}:YUNIT")

    @property
    def burstedgtype(self) -> MeasurementMeasItemBurstedgtype:
        """Return the ``MEASUrement:MEAS<x>:BURSTEDGTYPe`` command.

        Description:
            - This command sets or queries the burst edge type for the measurement. Measurements are
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:BURSTEDGTYPe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:BURSTEDGTYPe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:BURSTEDGTYPe value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:BURSTEDGTYPe {RISE|FALL}
            - MEASUrement:MEAS<x>:BURSTEDGTYPe?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``RISE`` specifies a burst with a rising edge.
            - ``FALL`` specifies a burst with a falling edge.
        """
        return self._burstedgtype

    @property
    def ccresults(self) -> MeasurementMeasItemCcresults:
        """Return the ``MEASUrement:MEAS<x>:CCRESUlts`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:CCRESUlts?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:CCRESUlts?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.allacqs``: The ``MEASUrement:MEAS<x>:CCRESUlts:ALLAcqs`` command tree.
            - ``.currentacq``: The ``MEASUrement:MEAS<x>:CCRESUlts:CURRentacq`` command tree.
        """
        return self._ccresults

    @property
    def delay(self) -> MeasurementMeasItemDelay:
        """Return the ``MEASUrement:MEAS<x>:DELay`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:DELay?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:DELay?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``MEAS<x>`` specifies the measurement number.

        Sub-properties:
            - ``.edge``: The ``MEASUrement:MEAS<x>:DELay:EDGE<x>`` command.
        """
        return self._delay

    @property
    def displaystat(self) -> MeasurementMeasItemDisplaystat:
        """Return the ``MEASUrement:MEAS<x>:DISPlaystat`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:DISPlaystat?``
              query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:DISPlaystat?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``MEAS<x>`` specifies the measurement number.

        Sub-properties:
            - ``.enable``: The ``MEASUrement:MEAS<x>:DISPlaystat:ENABle`` command.
        """
        return self._displaystat

    @property
    def edge(self) -> Dict[int, MeasurementMeasItemEdgeItem]:
        """Return the ``MEASUrement:MEAS<x>:EDGE<x>`` command.

        Description:
            - This command sets or queries the type of the specified edge, rise or fall, for the
              measurement. The measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:EDGE<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:EDGE<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:EDGE<x> value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:EDGE<x> {RISE|FALL|BOTH}
            - MEASUrement:MEAS<x>:EDGE<x>?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``EDGE<x>`` specifies the edge number.
            - ``RISE`` specifies the rising edge.
            - ``FALL`` specifies the falling edge.
            - ``BOTH`` specifies either the rising or falling edge.
        """
        return self._edge

    @property
    def edgeincre(self) -> MeasurementMeasItemEdgeincre:
        """Return the ``MEASUrement:MEAS<x>:EDGEIncre`` command.

        Description:
            - This command sets or queries the edge increment value for the measurement.
              Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:EDGEIncre?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:EDGEIncre?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:EDGEIncre value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:EDGEIncre <NR3>
            - MEASUrement:MEAS<x>:EDGEIncre?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``<NR3>`` is the measurements edge increment value.
        """
        return self._edgeincre

    @property
    def edges(self) -> MeasurementMeasItemEdges:
        """Return the ``MEASUrement:MEAS<x>:EDGES`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:EDGES?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:EDGES?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``MEAS<x>`` specifies the measurement number.

        Sub-properties:
            - ``.fromlevel``: The ``MEASUrement:MEAS<x>:EDGES:FROMLevel`` command.
            - ``.level``: The ``MEASUrement:MEAS<x>:EDGES:LEVel`` command.
            - ``.n``: The ``MEASUrement:MEAS<x>:EDGES:N`` command.
            - ``.slewratemethod``: The ``MEASUrement:MEAS<x>:EDGES:SLEWRATEMethod`` command.
            - ``.tolevel``: The ``MEASUrement:MEAS<x>:EDGES:TOLevel`` command.
        """
        return self._edges

    @property
    def failcount(self) -> MeasurementMeasItemFailcount:
        """Return the ``MEASUrement:MEAS<x>:FAILCount`` command.

        Description:
            - This command returns the number of measurement failures, if applicable, for the
              selected measurement. The measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:FAILCount?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:FAILCount?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:FAILCount?
            ```
        """
        return self._failcount

    @property
    def fromedgesearchdirect(self) -> MeasurementMeasItemFromedgesearchdirect:
        """Return the ``MEASUrement:MEAS<x>:FROMEDGESEARCHDIRect`` command.

        Description:
            - This command sets or queries the from edge search direction for the measurement.
              Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:FROMEDGESEARCHDIRect?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:FROMEDGESEARCHDIRect?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:FROMEDGESEARCHDIRect value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:FROMEDGESEARCHDIRect {FORWard|BACKWard}
            - MEASUrement:MEAS<x>:FROMEDGESEARCHDIRect?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``FORWard`` specifies a forward search from the edge.
            - ``BACKWard`` specifies a backward search from the edge.
        """
        return self._fromedgesearchdirect

    @property
    def fromedge(self) -> MeasurementMeasItemFromedge:
        """Return the ``MEASUrement:MEAS<x>:FROMedge`` command.

        Description:
            - This command sets or queries the from edge type for the measurement. Measurements are
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:FROMedge?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:FROMedge?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:FROMedge value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:FROMedge {RISe|FALL|BOTH}
            - MEASUrement:MEAS<x>:FROMedge?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``FALL`` specifies the falling edge of the waveform.
            - ``RISE`` specifies the rising edge of the waveform.
            - ``BOTH`` specifies both the rising and falling edges of the waveform.
        """
        return self._fromedge

    @property
    def gating(self) -> MeasurementMeasItemGating:
        """Return the ``MEASUrement:MEAS<x>:GATing`` command.

        Description:
            - This command sets or queries the gating type for the measurement. Measurements are
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:GATing?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:GATing?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:GATing value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:GATing {NONE|SCREEN|CURSor|LOGic|SEARch|TIMe}
            - MEASUrement:MEAS<x>:GATing?
            ```

        Info:
            - ``MEAS<x>`` is the measurement number for which to return a value.
            - ``NONE`` specifies measurements are taken across the entire record.
            - ``SCREEN`` turns on gating, using the left and right edges of the screen.
            - ``CURSor`` limits measurements to the portion of the waveform between the vertical bar
              cursors, even if they are off screen.
            - ``LOGic`` specifies that measurements are taken only when the logical state of other
              waveforms is true.
            - ``SEARch`` specifies that measurements are taken only where the results of a user
              specified search are found.
            - ``TIMe`` limits measurements to the portion of the waveform between the Start and End
              gate times.

        Sub-properties:
            - ``.active``: The ``MEASUrement:MEAS<x>:GATing:ACTive`` command.
            - ``.endtime``: The ``MEASUrement:MEAS<x>:GATing:ENDtime`` command.
            - ``.global``: The ``MEASUrement:MEAS<x>:GATing:GLOBal`` command.
            - ``.hysteresis``: The ``MEASUrement:MEAS<x>:GATing:HYSTeresis`` command.
            - ``.logicsource``: The ``MEASUrement:MEAS<x>:GATing:LOGICSource`` command.
            - ``.midref``: The ``MEASUrement:MEAS<x>:GATing:MIDRef`` command.
            - ``.searchsource``: The ``MEASUrement:MEAS<x>:GATing:SEARCHSource`` command.
            - ``.starttime``: The ``MEASUrement:MEAS<x>:GATing:STARTtime`` command.
        """
        return self._gating

    @property
    def globalref(self) -> MeasurementMeasItemGlobalref:
        """Return the ``MEASUrement:MEAS<x>:GLOBalref`` command.

        Description:
            - This command sets or queries the reference levels global flag for the measurement.
              Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:GLOBalref?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:GLOBalref?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:GLOBalref value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:GLOBalref {OFF|ON|0|1}
            - MEASUrement:MEAS<x>:GLOBalref?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``OFF`` allows ref levels to be set separately for each measurement.
            - ``ON`` applies the same ref levels to all measurements.
            - ``0`` allows ref levels to be set separately for each measurement.
            - ``1`` applies the same ref levels to all measurements.
        """
        return self._globalref

    @property
    def highrefvoltage(self) -> MeasurementMeasItemHighrefvoltage:
        """Return the ``MEASUrement:MEAS<x>:HIGHREFVoltage`` command.

        Description:
            - This command sets or queries the high reference voltage value for the 'time outside
              level' measurement. Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:HIGHREFVoltage?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:HIGHREFVoltage?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:HIGHREFVoltage value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:HIGHREFVoltage <NR3>
            - MEASUrement:MEAS<x>:HIGHREFVoltage?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``<NR3>`` is the high reference voltage value for the selected configuration.
        """
        return self._highrefvoltage

    @property
    def idletime(self) -> MeasurementMeasItemIdletime:
        """Return the ``MEASUrement:MEAS<x>:IDLETime`` command.

        Description:
            - This command sets or queries the idle time for the measurement when the measurement
              type is burst width. Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:IDLETime?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:IDLETime?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:IDLETime value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:IDLETime <NR3>
            - MEASUrement:MEAS<x>:IDLETime?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``<NR3>`` is the idle time.
        """
        return self._idletime

    @property
    def label(self) -> MeasurementMeasItemLabel:
        """Return the ``MEASUrement:MEAS<x>:LABel`` command.

        Description:
            - This command sets or queries the label for the measurement. As the label can contain
              non 7-bit ASCII text, it is stored in Percent Encoding format. The measurement number
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:LABel?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:LABel value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:LABel <QString>
            - MEASUrement:MEAS<x>:LABel?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``<QString>`` is the measurement label.
        """
        return self._label

    @property
    def lowrefvoltage(self) -> MeasurementMeasItemLowrefvoltage:
        """Return the ``MEASUrement:MEAS<x>:LOWREFVoltage`` command.

        Description:
            - This command sets or queries the low reference voltage value for the 'time outside
              level' measurement. Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:LOWREFVoltage?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:LOWREFVoltage?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:LOWREFVoltage value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:LOWREFVoltage <NR3>
            - MEASUrement:MEAS<x>:LOWREFVoltage?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``<NR3>`` is the low reference voltage value for the selected configuration.
        """
        return self._lowrefvoltage

    @property
    def passfailenabled(self) -> MeasurementMeasItemPassfailenabled:
        """Return the ``MEASUrement:MEAS<x>:PASSFAILENabled`` command.

        Description:
            - This command returns or sets the pass/fail test enable status. If enabled, this will
              turn on pass fail testing for the specified measurement. Measurements are specified by
              x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:PASSFAILENabled?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:PASSFAILENabled?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:PASSFAILENabled value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:PASSFAILENabled <NR1>
            - MEASUrement:MEAS<x>:PASSFAILENabled?
            ```

        Info:
            - ``<NR1>`` enables or disables pass fail testing for the specified measurement. A value
              of 1 enables and a value of 0 disables.
        """
        return self._passfailenabled

    @property
    def passfailhighlimit(self) -> MeasurementMeasItemPassfailhighlimit:
        """Return the ``MEASUrement:MEAS<x>:PASSFAILHIGHlimit`` command.

        Description:
            - This command returns or sets the high limit for a measurement test. Used as the test
              value when the 'fail when' criteria is set to 'less than' or 'greater than'.
              Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:PASSFAILHIGHlimit?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:PASSFAILHIGHlimit?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:PASSFAILHIGHlimit value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:PASSFAILHIGHlimit <NR2>
            - MEASUrement:MEAS<x>:PASSFAILHIGHlimit?
            ```

        Info:
            - ``<NR2>`` sets the high limit for a measurement test. The high limit is a number which
              a measurement result will be tested against.
        """
        return self._passfailhighlimit

    @property
    def passfaillimit(self) -> MeasurementMeasItemPassfaillimit:
        """Return the ``MEASUrement:MEAS<x>:PASSFAILLIMit`` command.

        Description:
            - This command returns or sets the limit for a measurement test. Used as the test value
              when the 'fail when' criteria is set to 'less than' or 'greater than'. Measurements
              are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:PASSFAILLIMit?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:PASSFAILLIMit?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:PASSFAILLIMit value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:PASSFAILLIMit <NR2>
            - MEASUrement:MEAS<x>:PASSFAILLIMit?
            ```

        Info:
            - ``<NR2>`` sets the limit for a measurement test. The limit is a number which a
              measurement result will be tested against.
        """
        return self._passfaillimit

    @property
    def passfaillowlimit(self) -> MeasurementMeasItemPassfaillowlimit:
        """Return the ``MEASUrement:MEAS<x>:PASSFAILLOWlimit`` command.

        Description:
            - This command returns or sets the low limit for a measurement test. Used as the test
              value when the 'fail when' criteria is set to 'less than' or 'greater than'.
              Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:PASSFAILLOWlimit?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:PASSFAILLOWlimit?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:PASSFAILLOWlimit value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:PASSFAILLOWlimit <NR2>
            - MEASUrement:MEAS<x>:PASSFAILLOWlimit?
            ```

        Info:
            - ``<NR2>`` sets the low limit for a measurement test. The limit is a number which a
              measurement result will be tested against.
        """
        return self._passfaillowlimit

    @property
    def passfailmargin(self) -> MeasurementMeasItemPassfailmargin:
        """Return the ``MEASUrement:MEAS<x>:PASSFAILMARgin`` command.

        Description:
            - This command returns or sets the allowed margin for limit comparisons for all
              pass/fail checks. This is given as a percentage with a default value of 0.05
              representing 5%. Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:PASSFAILMARgin?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:PASSFAILMARgin?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:PASSFAILMARgin value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:PASSFAILMARgin <NR2>
            - MEASUrement:MEAS<x>:PASSFAILMARgin?
            ```

        Info:
            - ``<NR2>`` sets the allowed margin for limit comparisons for all pass/fail checks. The
              margin as a percentage of the limit.
        """
        return self._passfailmargin

    @property
    def passfailwhen(self) -> MeasurementMeasItemPassfailwhen:
        """Return the ``MEASUrement:MEAS<x>:PASSFAILWHEN`` command.

        Description:
            - This command sets or returns the condition on which a measurement test fails.
              Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:PASSFAILWHEN?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:PASSFAILWHEN?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:PASSFAILWHEN value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:PASSFAILWHEN {LESSthan|GREATERthan|Equals|NOTEQuals|INSIDErange|OUTSIDErange}
            - MEASUrement:MEAS<x>:PASSFAILWHEN?
            ```

        Info:
            - ``LESSthan`` sets the condition for measurement test failure as less than the given
              limit. This is the default value.
            - ``GREATERthan`` sets the condition for measurement test failure as greater than the
              given limit.
            - ``Equals`` sets the condition for measurement test failure as equals the given limit.
            - ``NOTEQuals`` sets the condition for measurement test failure as not equal to the
              given limit.
            - ``INSIDErange`` sets the condition for measurement test failure as inside the limit
              range.
            - ``OUTSIDErange`` sets the condition for measurement test failure as outside the limit
              range.
        """  # noqa: E501
        return self._passfailwhen

    @property
    def perfreq(self) -> MeasurementMeasItemPerfreq:
        """Return the ``MEASUrement:MEAS<x>:PERFREQ`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:PERFREQ?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:PERFREQ?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``MEAS<x>`` specifies the measurement number.

        Sub-properties:
            - ``.edge``: The ``MEASUrement:MEAS<x>:PERFREQ:EDGE`` command.
        """
        return self._perfreq

    @property
    def polarity(self) -> MeasurementMeasItemPolarity:
        """Return the ``MEASUrement:MEAS<x>:POLarity`` command.

        Description:
            - This command sets or queries the polarity for the measurement when the measurement
              type is burst width. Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:POLarity value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:POLarity {NORMal|INVerted}
            - MEASUrement:MEAS<x>:POLarity?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``NORMal`` specifies normal polarity.
            - ``INVerted`` specifies inverted polarity.
        """
        return self._polarity

    @property
    def reflevels(self) -> MeasurementMeasItemReflevels:
        """Return the ``MEASUrement:MEAS<x>:REFLevels`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:REFLevels?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:REFLevels?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``MEAS<x>`` specifies the measurement number.

        Sub-properties:
            - ``.absolute``: The ``MEASUrement:MEAS<x>:REFLevels:ABSolute`` command tree.
        """
        return self._reflevels

    @property
    def reflevels1(self) -> MeasurementMeasItemReflevels1:
        """Return the ``MEASUrement:MEAS<x>:REFLevels1`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:REFLevels1?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:REFLevels1?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``MEAS<x>`` specifies the measurement number.

        Sub-properties:
            - ``.absolute``: The ``MEASUrement:MEAS<x>:REFLevels1:ABSolute`` command tree.
            - ``.basetop``: The ``MEASUrement:MEAS<x>:REFLevels1:BASETop`` command.
            - ``.method``: The ``MEASUrement:MEAS<x>:REFLevels1:METHod`` command.
            - ``.percent``: The ``MEASUrement:MEAS<x>:REFLevels1:PERCent`` command tree.
        """
        return self._reflevels1

    @property
    def refmode(self) -> MeasurementMeasItemRefmode:
        """Return the ``MEASUrement:MEAS<x>:REFMode`` command.

        Description:
            - This command sets or queries the reference level mode for the measurement. The
              measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:REFMode?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:REFMode?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:REFMode value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFMode {AUTO|MANual}
            - MEASUrement:MEAS<x>:REFMode?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``AUTO`` sets the reference level for the measurement automatically.
            - ``MANual`` allows the user to set the reference level for the measurement.
        """
        return self._refmode

    @property
    def refvoltage(self) -> MeasurementMeasItemRefvoltage:
        """Return the ``MEASUrement:MEAS<x>:REFVoltage`` command.

        Description:
            - This command sets or queries the reference voltage value for the measurement. The
              measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:REFVoltage?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:REFVoltage?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFVoltage value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFVoltage <NR3>
            - MEASUrement:MEAS<x>:REFVoltage?
            ```

        Info:
            - ``MEAS<x>`` is the measurement number.
            - ``<NR3>`` is the reference voltage value for the selected configuration.
        """
        return self._refvoltage

    @property
    def results(self) -> MeasurementMeasItemResults:
        """Return the ``MEASUrement:MEAS<x>:RESUlts`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:RESUlts?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:RESUlts?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.allacqs``: The ``MEASUrement:MEAS<x>:RESUlts:ALLAcqs`` command tree.
            - ``.currentacq``: The ``MEASUrement:MEAS<x>:RESUlts:CURRentacq`` command tree.
        """
        return self._results

    @property
    def signaltype(self) -> MeasurementMeasItemSignaltype:
        """Return the ``MEASUrement:MEAS<x>:SIGNALType`` command.

        Description:
            - This command sets or queries the signal type of source 1 for the measurement. The
              measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:SIGNALType?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:SIGNALType?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:SIGNALType value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:SIGNALType {CLOCK|DATA|AUTO}
            - MEASUrement:MEAS<x>:SIGNALType?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``CLOCK`` specifies a clock signal type.
            - ``DATA`` specifies a data signal type.
            - ``AUTO`` automatically selects the signal type.
        """
        return self._signaltype

    @property
    def source1(self) -> MeasurementMeasItemSource1:
        """Return the ``MEASUrement:MEAS<x>:SOUrce1`` command.

        Description:
            - This command sets or queries the measurement source. The measurement number and source
              are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:SOUrce1?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:SOUrce1?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:SOUrce1 value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:SOUrce1 {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>}
            - MEASUrement:MEAS<x>:SOUrce1?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``1`` specifies the source number.
            - ``CH<x>`` specifies an analog channel to use as the source.
            - ``DCH<x>_D<x>`` specifies a digital channel to use as the source. The supported
              digital channel value is 1. The supported digital bit values are 0 to 15.
            - ``MATH<x>`` specifies a math waveform to use as the source.
            - ``REF<x>`` specifies a reference waveform to use as the source.
        """
        return self._source1

    @property
    def status(self) -> MeasurementMeasItemStatus:
        """Return the ``MEASUrement:MEAS<x>:STATUS`` command.

        Description:
            - This command returns the pass fail status, if applicable, for the selected
              measurement. Measurements are specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:STATUS?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:STATUS?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:STATUS?
            ```

        Info:
            - ``PASS`` specifies that the user specified measurement limit has not been violated.
            - ``FAIL`` specifies that the user specified measurement limit has been violated.
        """
        return self._status

    @property
    def toedgesearchdirect(self) -> MeasurementMeasItemToedgesearchdirect:
        """Return the ``MEASUrement:MEAS<x>:TOEDGESEARCHDIRect`` command.

        Description:
            - This command sets or queries the to edge search direction for the measurement. The
              measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:TOEDGESEARCHDIRect?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:TOEDGESEARCHDIRect?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:TOEDGESEARCHDIRect value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:TOEDGESEARCHDIRect {FORWard|BACKWard}
            - MEASUrement:MEAS<x>:TOEDGESEARCHDIRect?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``FORWard`` specifies a forward search to the edge.
            - ``BACKWard`` specifies a backward search to the edge.
        """
        return self._toedgesearchdirect

    @property
    def toedge(self) -> MeasurementMeasItemToedge:
        """Return the ``MEASUrement:MEAS<x>:TOEdge`` command.

        Description:
            - This command sets or queries the 'to edge' type for the measurement. The measurement
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:TOEdge?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:TOEdge?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:TOEdge value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:TOEdge {SAMEas|OPPositeas|RISe|FALL|BOTH}
            - MEASUrement:MEAS<x>:TOEdge?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
            - ``FALL`` specifies the falling edge of the waveform.
            - ``RISE`` specifies the rising edge of the waveform.
            - ``BOTH`` specifies both a rising and falling edge of the waveform.
            - ``SAMEas`` specifies that both edges of the waveform are the same.
            - ``OPPositeas`` specifies that the edges of the waveform are not the same.
        """
        return self._toedge

    @property
    def transition(self) -> MeasurementMeasItemTransition:
        """Return the ``MEASUrement:MEAS<x>:TRANSition`` command.

        Description:
            - This command sets or queries the transition edges flag for the measurement. The
              measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:TRANSition?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:TRANSition?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:TRANSition value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:TRANSition {ON|OFF|<NR1>}
            - MEASUrement:MEAS<x>:TRANSition?
            ```

        Info:
            - ``<NR1>`` = 1, the measurement is computed on rising (if measurement type is rise
              time) or falling edges (if measurement type is fall time) following a double
              transition only. If it is set to 0, the measurement is computed on all rising (if
              measurement type is rise time) or falling (if measurement type is fall time) edges.
            - ``OFF`` computes the measurement on all rising (if measurement type is rise time) or
              falling (if measurement type is fall time) edges.
            - ``ON`` computes the measurement on rising (if measurement type is rise time) or
              falling edges (if measurement type is fall time) following a double transition only.
        """
        return self._transition

    @property
    def type(self) -> MeasurementMeasItemType:
        """Return the ``MEASUrement:MEAS<x>:TYPe`` command.

        Description:
            - This command sets or queries the measurement type for the measurement specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:TYPe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:TYPe value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:TYPe {ACRMS|AMPlITUDE|AREA|BASE|BURSTWIDTH|DATARATE|DELAY|FALLSLEWRATE|FALLTIME|FREQUENCY|HIGHTIME|HOLD|LOWTIME|MAXIMUM|MEAN|MINIMUM|NDUtY|NPERIOD|NOVERSHOOT|NWIDTH|PDUTY|PERIOD|PHASE|PK2Pk|POVERSHOOT|PWIDTH|RISESLEWRATE|RISETIME|RMS|SETUP|SKEW|TIMEOUTSIDELEVEL|TOP}
            - MEASUrement:MEAS<x>:TYPe?
            ```

        Info:
            - ``ACRMS`` (AC RMS) is the true Root Mean Square of the data points, about the Mean.
              This measurement can be made across the entire record, or on each cycle in the record.
            - ``AMPLITUDE`` is the difference between the Top value and the Base value. This
              measurement can be made across the entire record, or on each cycle in the record.
            - ``AREA`` is the area under the curve, calculated by integrating the data points. The
              area measured above ground is positive. The area measured below ground is negative.
              This measurement can be made across the entire record, or on each cycle in the record.
            - ``BASE`` is the most common data value below the midpoint of the waveform. This
              measurement can be made across the entire record, or on each cycle in the record.
            - ``BURSTWIDTH`` (Burst Width) is the duration of a series of adjacent crossings of the
              Mid reference level (RM). Bursts are separated by a user-defined idle time (tI). This
              measurement is made on each burst in the record.
            - ``DATARATE`` (Data Rate) is the reciprocal of Unit Interval. This measurement is made
              on each bit in the record.
            - ``DELay`` is the time between the specified Mid reference level (RM) crossing on one
              source to a specified Mid reference level (RM) crossing on a second source. This
              measurement is made on the first occurrence in the record.
            - ``FALLSLEWRATE`` (Falling Slew Rate) is the rate of change in voltage as an edge
              transitions from the Top reference level (RT) to the Bottom reference level (RB). This
              measurement is made on each cycle in the record.
            - ``FALLTIME`` (Fall Time) is the time required for an edge to fall from the Top
              reference level (RT) to the Base reference level (RB). This measurement is made on
              each cycle in the record.
            - ``FREQuency`` is the reciprocal of Period. This measurement is made on each cycle in
              the record.
            - ``HIGHTIME`` (High Time) is the time the signal remains above the Top reference level
              (RT). This measurement is made on each cycle in the record.
            - ``HOLD`` (Hold Time) is the time between the specified Mid reference level crossing
              (RM) on the Clock source to the closest specified Mid reference level (RM) crossing on
              the Data source. This measurement is made on each specified Clock edge in the record.
            - ``LOWTIME`` (Low Time) is the time the signal remains below the Base reference level
              (RB). This measurement is made on each cycle in the record.
            - ``MAXimum`` is the maximum data point. This measurement can be made across the entire
              record, or on each cycle in the record.
            - ``MEAN`` is the arithmetic mean of the data points. This measurement can be made
              across the entire record, or on each cycle in the record.
            - ``MINImum`` is the minimum data point. This measurement can be made across the entire
              record, or on each cycle in the record.
            - ``NDUty`` (Negative Duty Cycle) is the ratio of the Negative Pulse Width to the
              Period. This measurement is made on each cycle in the record.
            - ``NPERIOD`` (Duration N-Periods) is the time required to complete N cycles. A cycle is
              the time between two adjacent (same direction) crossings of the Mid reference level
              (RM). This measurement is made on each cycle in the record.
            - ``NOVershoot`` (Negative Overshoot) is the difference between Minimum and Base,
              divided by the Amplitude. This measurement can be made across the entire record, or on
              each cycle in the record.
            - ``NWIdth`` (Negative Pulse Width) is the time the signal remains below the Mid
              reference level (RM). This measurement is made on each cycle in the record.
            - ``PDUTY`` (Positive Duty Cycle) is the ratio of the Positive Pulse Width to the
              Period. This measurement is made on each cycle in the record.
            - ``PERIOD`` is the time required to complete a cycle. A cycle is the time between two
              adjacent (same direction) crossings of the Mid reference level (RM). This measurement
              is made on each cycle in the record.
            - ``PHASE`` is the ratio of the Skew between two sources to the Period of the first
              source. This measurement is made on each cycle in the record.
            - ``PK2Pk`` (Peak-to-peak) is the difference between Maximum and Minimum. This
              measurement can be made across the entire record, or on each cycle in the record.
            - ``POVERSHOOT`` (Positive Overshoot) is the difference between Maximum and Top, divided
              by the Amplitude. This measurement can be made across the entire record, or on each
              cycle in the record.
            - ``PWIDTH`` (Positive Pulse Width) is the time the signal remains above the Mid
              reference level (RM). This measurement is made on each cycle in the record.
            - ``RISESLEWRATE`` (Rising Slew Rate) is the rate of change in voltage as an edge
              transitions from the Base reference level (RB) to the Top reference level (RT). This
              measurement is made on each cycle in the record.
            - ``RISETIME`` Rise Time is the time required for an edge to rise from the Base
              reference level (RB) to the Top reference level (RT). This measurement is made on each
              cycle in the record.
            - ``RMS`` is the true Root Mean Square of the data points. This measurement can be made
              across the entire record, or on each cycle in the record.
            - ``SETUP`` (Setup Time) is the time between the specified Mid reference level (RM)
              crossing on the Data source to the closest specified Mid reference level (RM) crossing
              on the Clock source. This measurement is made on each specified Clock edge in the
              record.
            - ``SKEW`` Skew is the time between the specified Mid reference level (RM) crossing on
              one source to the following specified Mid reference level (RM) crossing on a second
              source. This measurement is made on each cycle in the record.
            - ``TIMEOUTSIDELEVEL`` Time Outside Level is the time the signal remains above the Top
              reference level (RT) and/or below the Base reference level (RB). This measurement is
              made on each occurrence in the record.
            - ``TOP`` is the most common data value above the midpoint of the waveform. This
              measurement can be made across the entire record, or on each cycle in the record.
        """  # noqa: E501
        return self._type

    @property
    def xunit(self) -> MeasurementMeasItemXunit:
        """Return the ``MEASUrement:MEAS<x>:XUNIT`` command.

        Description:
            - Returns the horizontal scale units of the specified measurement.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:XUNIT?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:XUNIT?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:XUNIT?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
        """
        return self._xunit

    @property
    def yunit(self) -> MeasurementMeasItemYunit:
        """Return the ``MEASUrement:MEAS<x>:YUNIT`` command.

        Description:
            - Returns the vertical scale units of the specified measurement.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:YUNIT?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:YUNIT?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:YUNIT?
            ```

        Info:
            - ``MEAS<x>`` specifies the measurement number.
        """
        return self._yunit


class MeasurementMathItemReflevelsPercentType(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MATH<x>:REFLevels:PERCent:TYPE`` command.

    Description:
        - This command specifies or queries the reference level percent type for the measurement.
          The math number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:PERCent:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:PERCent:TYPE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:PERCent:TYPE value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MATH<x>:REFLevels:PERCent:TYPE {TENNinety|TWENtyeighty|CUSTom}
        - MEASUrement:MATH<x>:REFLevels:PERCent:TYPE?
        ```

    Info:
        - ``MATH<x>`` specifies the math number.
        - ``TENNinety`` sets the values for Low, Mid and High Ref to 10%, 50% and 90% respectively.
        - ``TWENtyeighty`` sets the values for Low, Mid and High Ref are set to 20%, 50% and 80%
          respectively.
        - ``CUSTom`` allows setting other reference level percents.
    """


class MeasurementMathItemReflevelsPercentRisemid(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MATH<x>:REFLevels:PERCent:RISEMid`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the mid reference level of the rising edge when the measurement
          ref level method is set to percent. The math number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:PERCent:RISEMid?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:PERCent:RISEMid?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:PERCent:RISEMid value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MATH<x>:REFLevels:PERCent:RISEMid <NR3>
        - MEASUrement:MATH<x>:REFLevels:PERCent:RISEMid?
        ```

    Info:
        - ``MATH<x>`` specifies the math number.
        - ``<NR3>`` is the percentage (where 50% is equal to MID) used to calculate the mid
          reference level when the measurement Ref level method is set to Percent.
    """


class MeasurementMathItemReflevelsPercentRiselow(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MATH<x>:REFLevels:PERCent:RISELow`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the low reference level of the rising edge when the measurement
          ref level method is set to percent. The math number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:PERCent:RISELow?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:PERCent:RISELow?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:PERCent:RISELow value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MATH<x>:REFLevels:PERCent:RISELow <NR3>
        - MEASUrement:MATH<x>:REFLevels:PERCent:RISELow?
        ```

    Info:
        - ``MATH<x>`` specifies the math number.
        - ``<NR3>`` is the percentage (where 100% is equal to TOP) used to calculate the mid
          reference level when the measurement Ref level method is set to Percent.
    """


class MeasurementMathItemReflevelsPercentRisehigh(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MATH<x>:REFLevels:PERCent:RISEHigh`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the high reference level of the rising edge when the measurement
          ref level method is set to percent. The math number is specified by x. The measurement
          number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:PERCent:RISEHigh?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:PERCent:RISEHigh?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:PERCent:RISEHigh value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MATH<x>:REFLevels:PERCent:RISEHigh <NR3>
        - MEASUrement:MATH<x>:REFLevels:PERCent:RISEHigh?
        ```

    Info:
        - ``MATH<x>`` specifies the math number.
        - ``<NR3>`` is the percentage (where 100% is equal to TOP) used to calculate the high
          reference level when the measurement's Ref level method is set to Percent.
    """


class MeasurementMathItemReflevelsPercentHysteresis(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MATH<x>:REFLevels:PERCent:HYSTeresis`` command.

    Description:
        - This command sets or queries the percentage (where 100% is equal to MAX and 0% is equal to
          MIN) used to calculate the hysteresis of the reference level when the measurement ref
          level method is set to percent. The math number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:PERCent:HYSTeresis?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:PERCent:HYSTeresis?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:PERCent:HYSTeresis value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MATH<x>:REFLevels:PERCent:HYSTeresis <NR3>
        - MEASUrement:MATH<x>:REFLevels:PERCent:HYSTeresis?
        ```

    Info:
        - ``MATH<x>`` specifies the math number.
        - ``<NR3>`` is the hysteresis value used for the autoset.
    """


class MeasurementMathItemReflevelsPercentFallmid(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLMid`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the mid reference level of the falling edge when the measurement
          ref level method is set to percent. The math number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLMid?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLMid?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLMid value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MATH<x>:REFLevels:PERCent:FALLMid <NR3>
        - MEASUrement:MATH<x>:REFLevels:PERCent:FALLMid?
        ```

    Info:
        - ``MATH<x>`` specifies the math number.
        - ``<NR3>`` is the percentage (where 50% is equal to MID) used to calculate the mid
          reference level when the measurement Ref level method is set to Percent.
    """


class MeasurementMathItemReflevelsPercentFalllow(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLLow`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the low reference level of the falling edge when the measurement
          ref level method is set to percent. The math number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLLow?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLLow?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLLow value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MATH<x>:REFLevels:PERCent:FALLLow <NR3>
        - MEASUrement:MATH<x>:REFLevels:PERCent:FALLLow?
        ```

    Info:
        - ``MATH<x>`` specifies the math number.
        - ``<NR3>`` is the percentage (where 100% is equal to HIGH) used to calculate the mid
          reference level when the measurement's Ref level method is set to Percent.
    """


class MeasurementMathItemReflevelsPercentFallhigh(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLHigh`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the high reference level of the falling edge when the measurement
          ref level method is set to percent. The math number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLHigh?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLHigh?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLHigh value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MATH<x>:REFLevels:PERCent:FALLHigh <NR3>
        - MEASUrement:MATH<x>:REFLevels:PERCent:FALLHigh?
        ```

    Info:
        - ``MATH<x>`` specifies the math number.
        - ``<NR3>`` is the percentage (where 100% is equal to HIGH) used to calculate the high
          reference level when the measurement Ref level method is set to Percent.
    """


#  pylint: disable=too-many-instance-attributes
class MeasurementMathItemReflevelsPercent(SCPICmdRead):
    """The ``MEASUrement:MATH<x>:REFLevels:PERCent`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MATH<x>:REFLevels:PERCent?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:PERCent?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Info:
        - ``MATH<x>`` specifies the math number.

    Properties:
        - ``.fallhigh``: The ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLHigh`` command.
        - ``.falllow``: The ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLLow`` command.
        - ``.fallmid``: The ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLMid`` command.
        - ``.hysteresis``: The ``MEASUrement:MATH<x>:REFLevels:PERCent:HYSTeresis`` command.
        - ``.risehigh``: The ``MEASUrement:MATH<x>:REFLevels:PERCent:RISEHigh`` command.
        - ``.riselow``: The ``MEASUrement:MATH<x>:REFLevels:PERCent:RISELow`` command.
        - ``.risemid``: The ``MEASUrement:MATH<x>:REFLevels:PERCent:RISEMid`` command.
        - ``.type``: The ``MEASUrement:MATH<x>:REFLevels:PERCent:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fallhigh = MeasurementMathItemReflevelsPercentFallhigh(
            device, f"{self._cmd_syntax}:FALLHigh"
        )
        self._falllow = MeasurementMathItemReflevelsPercentFalllow(
            device, f"{self._cmd_syntax}:FALLLow"
        )
        self._fallmid = MeasurementMathItemReflevelsPercentFallmid(
            device, f"{self._cmd_syntax}:FALLMid"
        )
        self._hysteresis = MeasurementMathItemReflevelsPercentHysteresis(
            device, f"{self._cmd_syntax}:HYSTeresis"
        )
        self._risehigh = MeasurementMathItemReflevelsPercentRisehigh(
            device, f"{self._cmd_syntax}:RISEHigh"
        )
        self._riselow = MeasurementMathItemReflevelsPercentRiselow(
            device, f"{self._cmd_syntax}:RISELow"
        )
        self._risemid = MeasurementMathItemReflevelsPercentRisemid(
            device, f"{self._cmd_syntax}:RISEMid"
        )
        self._type = MeasurementMathItemReflevelsPercentType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def fallhigh(self) -> MeasurementMathItemReflevelsPercentFallhigh:
        """Return the ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLHigh`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the high reference level of the falling edge when the
              measurement ref level method is set to percent. The math number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLHigh?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLHigh value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MATH<x>:REFLevels:PERCent:FALLHigh <NR3>
            - MEASUrement:MATH<x>:REFLevels:PERCent:FALLHigh?
            ```

        Info:
            - ``MATH<x>`` specifies the math number.
            - ``<NR3>`` is the percentage (where 100% is equal to HIGH) used to calculate the high
              reference level when the measurement Ref level method is set to Percent.
        """
        return self._fallhigh

    @property
    def falllow(self) -> MeasurementMathItemReflevelsPercentFalllow:
        """Return the ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLLow`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the low reference level of the falling edge when the
              measurement ref level method is set to percent. The math number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLLow?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLLow?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLLow value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MATH<x>:REFLevels:PERCent:FALLLow <NR3>
            - MEASUrement:MATH<x>:REFLevels:PERCent:FALLLow?
            ```

        Info:
            - ``MATH<x>`` specifies the math number.
            - ``<NR3>`` is the percentage (where 100% is equal to HIGH) used to calculate the mid
              reference level when the measurement's Ref level method is set to Percent.
        """
        return self._falllow

    @property
    def fallmid(self) -> MeasurementMathItemReflevelsPercentFallmid:
        """Return the ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLMid`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the mid reference level of the falling edge when the
              measurement ref level method is set to percent. The math number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLMid?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLMid value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MATH<x>:REFLevels:PERCent:FALLMid <NR3>
            - MEASUrement:MATH<x>:REFLevels:PERCent:FALLMid?
            ```

        Info:
            - ``MATH<x>`` specifies the math number.
            - ``<NR3>`` is the percentage (where 50% is equal to MID) used to calculate the mid
              reference level when the measurement Ref level method is set to Percent.
        """
        return self._fallmid

    @property
    def hysteresis(self) -> MeasurementMathItemReflevelsPercentHysteresis:
        """Return the ``MEASUrement:MATH<x>:REFLevels:PERCent:HYSTeresis`` command.

        Description:
            - This command sets or queries the percentage (where 100% is equal to MAX and 0% is
              equal to MIN) used to calculate the hysteresis of the reference level when the
              measurement ref level method is set to percent. The math number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:PERCent:HYSTeresis?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:PERCent:HYSTeresis?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:PERCent:HYSTeresis value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MATH<x>:REFLevels:PERCent:HYSTeresis <NR3>
            - MEASUrement:MATH<x>:REFLevels:PERCent:HYSTeresis?
            ```

        Info:
            - ``MATH<x>`` specifies the math number.
            - ``<NR3>`` is the hysteresis value used for the autoset.
        """
        return self._hysteresis

    @property
    def risehigh(self) -> MeasurementMathItemReflevelsPercentRisehigh:
        """Return the ``MEASUrement:MATH<x>:REFLevels:PERCent:RISEHigh`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the high reference level of the rising edge when the
              measurement ref level method is set to percent. The math number is specified by x. The
              measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:PERCent:RISEHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:PERCent:RISEHigh?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:PERCent:RISEHigh value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MATH<x>:REFLevels:PERCent:RISEHigh <NR3>
            - MEASUrement:MATH<x>:REFLevels:PERCent:RISEHigh?
            ```

        Info:
            - ``MATH<x>`` specifies the math number.
            - ``<NR3>`` is the percentage (where 100% is equal to TOP) used to calculate the high
              reference level when the measurement's Ref level method is set to Percent.
        """
        return self._risehigh

    @property
    def riselow(self) -> MeasurementMathItemReflevelsPercentRiselow:
        """Return the ``MEASUrement:MATH<x>:REFLevels:PERCent:RISELow`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the low reference level of the rising edge when the
              measurement ref level method is set to percent. The math number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:PERCent:RISELow?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:PERCent:RISELow?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:PERCent:RISELow value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MATH<x>:REFLevels:PERCent:RISELow <NR3>
            - MEASUrement:MATH<x>:REFLevels:PERCent:RISELow?
            ```

        Info:
            - ``MATH<x>`` specifies the math number.
            - ``<NR3>`` is the percentage (where 100% is equal to TOP) used to calculate the mid
              reference level when the measurement Ref level method is set to Percent.
        """
        return self._riselow

    @property
    def risemid(self) -> MeasurementMathItemReflevelsPercentRisemid:
        """Return the ``MEASUrement:MATH<x>:REFLevels:PERCent:RISEMid`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the mid reference level of the rising edge when the
              measurement ref level method is set to percent. The math number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:PERCent:RISEMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:PERCent:RISEMid?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:PERCent:RISEMid value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MATH<x>:REFLevels:PERCent:RISEMid <NR3>
            - MEASUrement:MATH<x>:REFLevels:PERCent:RISEMid?
            ```

        Info:
            - ``MATH<x>`` specifies the math number.
            - ``<NR3>`` is the percentage (where 50% is equal to MID) used to calculate the mid
              reference level when the measurement Ref level method is set to Percent.
        """
        return self._risemid

    @property
    def type(self) -> MeasurementMathItemReflevelsPercentType:
        """Return the ``MEASUrement:MATH<x>:REFLevels:PERCent:TYPE`` command.

        Description:
            - This command specifies or queries the reference level percent type for the
              measurement. The math number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:PERCent:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:PERCent:TYPE?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:PERCent:TYPE value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MATH<x>:REFLevels:PERCent:TYPE {TENNinety|TWENtyeighty|CUSTom}
            - MEASUrement:MATH<x>:REFLevels:PERCent:TYPE?
            ```

        Info:
            - ``MATH<x>`` specifies the math number.
            - ``TENNinety`` sets the values for Low, Mid and High Ref to 10%, 50% and 90%
              respectively.
            - ``TWENtyeighty`` sets the values for Low, Mid and High Ref are set to 20%, 50% and 80%
              respectively.
            - ``CUSTom`` allows setting other reference level percents.
        """
        return self._type


class MeasurementMathItemReflevelsMethod(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MATH<x>:REFLevels:METHod`` command.

    Description:
        - This command sets or queries the method used to calculate reference levels for the
          measurement. The math number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MATH<x>:REFLevels:METHod?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:METHod?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:METHod value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MATH<x>:REFLevels:METHod {PERCent|ABSolute}
        - MEASUrement:MATH<x>:REFLevels:METHod?
        ```

    Info:
        - ``MATH<x>`` specifies the math number.
        - ``PERCent`` specifies that the reference levels are calculated as a percent relative to
          HIGH and LOW. The percentages are defined using the
          ``MEASUrement:MATH<x>:REFLevel:PERCent`` commands.
        - ``ABSolute`` specifies that the reference levels are set explicitly using the
          ``MEASUrement:MATH<x>:REFLevel:ABSolute`` commands. This method is useful when precise
          values are required.
    """


class MeasurementMathItemReflevelsBasetop(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MATH<x>:REFLevels:BASETop`` command.

    Description:
        - This command sets or queries the method used to calculate the TOP and BASE used to
          calculate reference levels for the measurement. The math number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MATH<x>:REFLevels:BASETop?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:BASETop?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:BASETop value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MATH<x>:REFLevels:BASETop {AUTO|MINMax|MEANhistogram|MODEhistogram|EYEhistogram}
        - MEASUrement:MATH<x>:REFLevels:BASETop?
        ```

    Info:
        - ``MATH<x>`` specifies the math number.
        - ``AUTO`` automatically chooses a reference level method.
        - ``MINMax`` specifies that reference levels are relative to the measurement MIN and MAX.
        - ``MEANhistogram`` specifies that reference levels are relative to the histogram mean BASE
          and TOP.
        - ``MODEhistogram`` specifies that reference levels are relative to the histogram mode BASE
          and TOP.
        - ``EYEhistogram`` specifies that reverence levels are relative to the eye histogram BASE
          and TOP.
    """  # noqa: E501


class MeasurementMathItemReflevelsAbsoluteType(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MATH<x>:REFLevels:ABSolute:TYPE`` command.

    Description:
        - This command sets or queries the reference level type for the measurement. The math number
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:ABSolute:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:ABSolute:TYPE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:ABSolute:TYPE value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MATH<x>:REFLevels:ABSolute:TYPE {SAME|UNIQue}
        - MEASUrement:MATH<x>:REFLevels:ABSolute:TYPE?
        ```

    Info:
        - ``MATH<x>`` specifies the math number.
        - ``SAME`` specifies that the absolute levels are set the same.
        - ``UNIQue`` specifies that the absolute levels can be set independently.
    """


class MeasurementMathItemReflevelsAbsoluteRisemid(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISEMid`` command.

    Description:
        - This command sets or queries the value used as the mid reference level of the rising edge
          when the measurement ref level method is set to absolute. The math number is specified by
          x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISEMid?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISEMid?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISEMid value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MATH<x>:REFLevels:ABSolute:RISEMid <NR3>
        - MEASUrement:MATH<x>:REFLevels:ABSolute:RISEMid?
        ```

    Info:
        - ``MATH<x>`` specifies the math number.
        - ``<NR3>`` is the mid reference level (where 50% is equal to MID) used to calculate the mid
          reference level when the measurement Ref level method is set to Absolute.
    """


class MeasurementMathItemReflevelsAbsoluteRiselow(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISELow`` command.

    Description:
        - This command sets or queries the value used as the low reference level of the rising edge
          when the measurement ref level method is set to absolute. The math number is specified by
          x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISELow?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISELow?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISELow value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MATH<x>:REFLevels:ABSolute:RISELow <NR3>
        - MEASUrement:MATH<x>:REFLevels:ABSolute:RISELow?
        ```

    Info:
        - ``MATH<x>`` specifies the math number.
        - ``<NR3>`` is the high reference level, and is the zero percent level when
          ``MEASUrement:IMMed:REFLevel:METHod`` is set to Absolute.
    """


class MeasurementMathItemReflevelsAbsoluteRisehigh(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISEHigh`` command.

    Description:
        - This command sets or queries the value used as the high reference level of the rising edge
          when the measurement ref level method is set to absolute. The math number is specified by
          x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISEHigh?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISEHigh?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISEHigh value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MATH<x>:REFLevels:ABSolute:RISEHigh <NR3>
        - MEASUrement:MATH<x>:REFLevels:ABSolute:RISEHigh?
        ```

    Info:
        - ``MATH<x>`` specifies the math number.
        - ``<NR3>`` is the high reference level, and is the zero percent level when
          ``MEASUrement:IMMed:REFLevel:METHod`` is set to Absolute.
    """


class MeasurementMathItemReflevelsAbsoluteHysteresis(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MATH<x>:REFLevels:ABSolute:HYSTeresis`` command.

    Description:
        - This command sets or queries the value of the hysteresis of the reference level when the
          measurement ref level method is set to absolute. The math number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:ABSolute:HYSTeresis?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:ABSolute:HYSTeresis?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:ABSolute:HYSTeresis value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MATH<x>:REFLevels:ABSolute:HYSTeresis <NR3>
        - MEASUrement:MATH<x>:REFLevels:ABSolute:HYSTeresis?
        ```

    Info:
        - ``MATH<x>`` specifies the math number.
        - ``<NR3>`` is the hysteresis value used for the autoset.
    """


class MeasurementMathItemReflevelsAbsoluteFallmid(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLMid`` command.

    Description:
        - This command sets or queries the value used as the mid reference level of the falling edge
          when the measurement ref level method is set to absolute. The math number is specified by
          x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLMid?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLMid?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLMid value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MATH<x>:REFLevels:ABSolute:FALLMid <NR3>
        - MEASUrement:MATH<x>:REFLevels:ABSolute:FALLMid?
        ```

    Info:
        - ``MATH<x>`` specifies the math number.
        - ``<NR3>`` is the mid reference level (where 50% is equal to MID) used to calculate the mid
          reference level when the measurement's Ref level method is set to Absolute.
    """


class MeasurementMathItemReflevelsAbsoluteFalllow(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLLow`` command.

    Description:
        - This command sets or queries the value used as the low reference level of the falling edge
          when the measuement ref level method is set to absolute. The math number is specified by
          x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLLow?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLLow?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLLow value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MATH<x>:REFLevels:ABSolute:FALLLow <NR3>
        - MEASUrement:MATH<x>:REFLevels:ABSolute:FALLLow?
        ```

    Info:
        - ``MATH<x>`` specifies the math number.
        - ``<NR3>`` is the high reference level, and is the zero percent level when
          ``MEASUrement:IMMed:REFLevel:METHod`` is set to Absolute.
    """


class MeasurementMathItemReflevelsAbsoluteFallhigh(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLHigh`` command.

    Description:
        - This command sets or queries the value used as the high reference level of the falling
          edge when the measurement ref level method is set to absolute. The math number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLHigh?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLHigh?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLHigh value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MATH<x>:REFLevels:ABSolute:FALLHigh <NR3>
        - MEASUrement:MATH<x>:REFLevels:ABSolute:FALLHigh?
        ```

    Info:
        - ``MATH<x>`` specifies the math number.
        - ``<NR3>`` is the high reference level, and is the zero percent level when
          ``MEASUrement:IMMed:REFLevel:METHod`` is set to Absolute.
    """


#  pylint: disable=too-many-instance-attributes
class MeasurementMathItemReflevelsAbsolute(SCPICmdRead):
    """The ``MEASUrement:MATH<x>:REFLevels:ABSolute`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MATH<x>:REFLevels:ABSolute?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MATH<x>:REFLevels:ABSolute?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Info:
        - ``MATH<x>`` specifies the math number.

    Properties:
        - ``.fallhigh``: The ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLHigh`` command.
        - ``.falllow``: The ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLLow`` command.
        - ``.fallmid``: The ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLMid`` command.
        - ``.hysteresis``: The ``MEASUrement:MATH<x>:REFLevels:ABSolute:HYSTeresis`` command.
        - ``.risehigh``: The ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISEHigh`` command.
        - ``.riselow``: The ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISELow`` command.
        - ``.risemid``: The ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISEMid`` command.
        - ``.type``: The ``MEASUrement:MATH<x>:REFLevels:ABSolute:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fallhigh = MeasurementMathItemReflevelsAbsoluteFallhigh(
            device, f"{self._cmd_syntax}:FALLHigh"
        )
        self._falllow = MeasurementMathItemReflevelsAbsoluteFalllow(
            device, f"{self._cmd_syntax}:FALLLow"
        )
        self._fallmid = MeasurementMathItemReflevelsAbsoluteFallmid(
            device, f"{self._cmd_syntax}:FALLMid"
        )
        self._hysteresis = MeasurementMathItemReflevelsAbsoluteHysteresis(
            device, f"{self._cmd_syntax}:HYSTeresis"
        )
        self._risehigh = MeasurementMathItemReflevelsAbsoluteRisehigh(
            device, f"{self._cmd_syntax}:RISEHigh"
        )
        self._riselow = MeasurementMathItemReflevelsAbsoluteRiselow(
            device, f"{self._cmd_syntax}:RISELow"
        )
        self._risemid = MeasurementMathItemReflevelsAbsoluteRisemid(
            device, f"{self._cmd_syntax}:RISEMid"
        )
        self._type = MeasurementMathItemReflevelsAbsoluteType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def fallhigh(self) -> MeasurementMathItemReflevelsAbsoluteFallhigh:
        """Return the ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLHigh`` command.

        Description:
            - This command sets or queries the value used as the high reference level of the falling
              edge when the measurement ref level method is set to absolute. The math number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLHigh?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLHigh value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MATH<x>:REFLevels:ABSolute:FALLHigh <NR3>
            - MEASUrement:MATH<x>:REFLevels:ABSolute:FALLHigh?
            ```

        Info:
            - ``MATH<x>`` specifies the math number.
            - ``<NR3>`` is the high reference level, and is the zero percent level when
              ``MEASUrement:IMMed:REFLevel:METHod`` is set to Absolute.
        """
        return self._fallhigh

    @property
    def falllow(self) -> MeasurementMathItemReflevelsAbsoluteFalllow:
        """Return the ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLLow`` command.

        Description:
            - This command sets or queries the value used as the low reference level of the falling
              edge when the measuement ref level method is set to absolute. The math number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLLow?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLLow?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLLow value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MATH<x>:REFLevels:ABSolute:FALLLow <NR3>
            - MEASUrement:MATH<x>:REFLevels:ABSolute:FALLLow?
            ```

        Info:
            - ``MATH<x>`` specifies the math number.
            - ``<NR3>`` is the high reference level, and is the zero percent level when
              ``MEASUrement:IMMed:REFLevel:METHod`` is set to Absolute.
        """
        return self._falllow

    @property
    def fallmid(self) -> MeasurementMathItemReflevelsAbsoluteFallmid:
        """Return the ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLMid`` command.

        Description:
            - This command sets or queries the value used as the mid reference level of the falling
              edge when the measurement ref level method is set to absolute. The math number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLMid?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLMid value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MATH<x>:REFLevels:ABSolute:FALLMid <NR3>
            - MEASUrement:MATH<x>:REFLevels:ABSolute:FALLMid?
            ```

        Info:
            - ``MATH<x>`` specifies the math number.
            - ``<NR3>`` is the mid reference level (where 50% is equal to MID) used to calculate the
              mid reference level when the measurement's Ref level method is set to Absolute.
        """
        return self._fallmid

    @property
    def hysteresis(self) -> MeasurementMathItemReflevelsAbsoluteHysteresis:
        """Return the ``MEASUrement:MATH<x>:REFLevels:ABSolute:HYSTeresis`` command.

        Description:
            - This command sets or queries the value of the hysteresis of the reference level when
              the measurement ref level method is set to absolute. The math number is specified by
              x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:ABSolute:HYSTeresis?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:ABSolute:HYSTeresis?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:ABSolute:HYSTeresis value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MATH<x>:REFLevels:ABSolute:HYSTeresis <NR3>
            - MEASUrement:MATH<x>:REFLevels:ABSolute:HYSTeresis?
            ```

        Info:
            - ``MATH<x>`` specifies the math number.
            - ``<NR3>`` is the hysteresis value used for the autoset.
        """
        return self._hysteresis

    @property
    def risehigh(self) -> MeasurementMathItemReflevelsAbsoluteRisehigh:
        """Return the ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISEHigh`` command.

        Description:
            - This command sets or queries the value used as the high reference level of the rising
              edge when the measurement ref level method is set to absolute. The math number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISEHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISEHigh?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISEHigh value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MATH<x>:REFLevels:ABSolute:RISEHigh <NR3>
            - MEASUrement:MATH<x>:REFLevels:ABSolute:RISEHigh?
            ```

        Info:
            - ``MATH<x>`` specifies the math number.
            - ``<NR3>`` is the high reference level, and is the zero percent level when
              ``MEASUrement:IMMed:REFLevel:METHod`` is set to Absolute.
        """
        return self._risehigh

    @property
    def riselow(self) -> MeasurementMathItemReflevelsAbsoluteRiselow:
        """Return the ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISELow`` command.

        Description:
            - This command sets or queries the value used as the low reference level of the rising
              edge when the measurement ref level method is set to absolute. The math number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISELow?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISELow?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISELow value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MATH<x>:REFLevels:ABSolute:RISELow <NR3>
            - MEASUrement:MATH<x>:REFLevels:ABSolute:RISELow?
            ```

        Info:
            - ``MATH<x>`` specifies the math number.
            - ``<NR3>`` is the high reference level, and is the zero percent level when
              ``MEASUrement:IMMed:REFLevel:METHod`` is set to Absolute.
        """
        return self._riselow

    @property
    def risemid(self) -> MeasurementMathItemReflevelsAbsoluteRisemid:
        """Return the ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISEMid`` command.

        Description:
            - This command sets or queries the value used as the mid reference level of the rising
              edge when the measurement ref level method is set to absolute. The math number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISEMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISEMid?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISEMid value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MATH<x>:REFLevels:ABSolute:RISEMid <NR3>
            - MEASUrement:MATH<x>:REFLevels:ABSolute:RISEMid?
            ```

        Info:
            - ``MATH<x>`` specifies the math number.
            - ``<NR3>`` is the mid reference level (where 50% is equal to MID) used to calculate the
              mid reference level when the measurement Ref level method is set to Absolute.
        """
        return self._risemid

    @property
    def type(self) -> MeasurementMathItemReflevelsAbsoluteType:
        """Return the ``MEASUrement:MATH<x>:REFLevels:ABSolute:TYPE`` command.

        Description:
            - This command sets or queries the reference level type for the measurement. The math
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:ABSolute:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:ABSolute:TYPE?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:ABSolute:TYPE value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MATH<x>:REFLevels:ABSolute:TYPE {SAME|UNIQue}
            - MEASUrement:MATH<x>:REFLevels:ABSolute:TYPE?
            ```

        Info:
            - ``MATH<x>`` specifies the math number.
            - ``SAME`` specifies that the absolute levels are set the same.
            - ``UNIQue`` specifies that the absolute levels can be set independently.
        """
        return self._type


class MeasurementMathItemReflevels(SCPICmdRead):
    """The ``MEASUrement:MATH<x>:REFLevels`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MATH<x>:REFLevels?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MATH<x>:REFLevels?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``MATH<x>`` specifies the math number.

    Properties:
        - ``.absolute``: The ``MEASUrement:MATH<x>:REFLevels:ABSolute`` command tree.
        - ``.basetop``: The ``MEASUrement:MATH<x>:REFLevels:BASETop`` command.
        - ``.method``: The ``MEASUrement:MATH<x>:REFLevels:METHod`` command.
        - ``.percent``: The ``MEASUrement:MATH<x>:REFLevels:PERCent`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._absolute = MeasurementMathItemReflevelsAbsolute(
            device, f"{self._cmd_syntax}:ABSolute"
        )
        self._basetop = MeasurementMathItemReflevelsBasetop(device, f"{self._cmd_syntax}:BASETop")
        self._method = MeasurementMathItemReflevelsMethod(device, f"{self._cmd_syntax}:METHod")
        self._percent = MeasurementMathItemReflevelsPercent(device, f"{self._cmd_syntax}:PERCent")

    @property
    def absolute(self) -> MeasurementMathItemReflevelsAbsolute:
        """Return the ``MEASUrement:MATH<x>:REFLevels:ABSolute`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:ABSolute?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:ABSolute?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Info:
            - ``MATH<x>`` specifies the math number.

        Sub-properties:
            - ``.fallhigh``: The ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLHigh`` command.
            - ``.falllow``: The ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLLow`` command.
            - ``.fallmid``: The ``MEASUrement:MATH<x>:REFLevels:ABSolute:FALLMid`` command.
            - ``.hysteresis``: The ``MEASUrement:MATH<x>:REFLevels:ABSolute:HYSTeresis`` command.
            - ``.risehigh``: The ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISEHigh`` command.
            - ``.riselow``: The ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISELow`` command.
            - ``.risemid``: The ``MEASUrement:MATH<x>:REFLevels:ABSolute:RISEMid`` command.
            - ``.type``: The ``MEASUrement:MATH<x>:REFLevels:ABSolute:TYPE`` command.
        """
        return self._absolute

    @property
    def basetop(self) -> MeasurementMathItemReflevelsBasetop:
        """Return the ``MEASUrement:MATH<x>:REFLevels:BASETop`` command.

        Description:
            - This command sets or queries the method used to calculate the TOP and BASE used to
              calculate reference levels for the measurement. The math number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MATH<x>:REFLevels:BASETop?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:BASETop?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:BASETop value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MATH<x>:REFLevels:BASETop {AUTO|MINMax|MEANhistogram|MODEhistogram|EYEhistogram}
            - MEASUrement:MATH<x>:REFLevels:BASETop?
            ```

        Info:
            - ``MATH<x>`` specifies the math number.
            - ``AUTO`` automatically chooses a reference level method.
            - ``MINMax`` specifies that reference levels are relative to the measurement MIN and
              MAX.
            - ``MEANhistogram`` specifies that reference levels are relative to the histogram mean
              BASE and TOP.
            - ``MODEhistogram`` specifies that reference levels are relative to the histogram mode
              BASE and TOP.
            - ``EYEhistogram`` specifies that reverence levels are relative to the eye histogram
              BASE and TOP.
        """  # noqa: E501
        return self._basetop

    @property
    def method(self) -> MeasurementMathItemReflevelsMethod:
        """Return the ``MEASUrement:MATH<x>:REFLevels:METHod`` command.

        Description:
            - This command sets or queries the method used to calculate reference levels for the
              measurement. The math number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MATH<x>:REFLevels:METHod?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:METHod?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:METHod value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MATH<x>:REFLevels:METHod {PERCent|ABSolute}
            - MEASUrement:MATH<x>:REFLevels:METHod?
            ```

        Info:
            - ``MATH<x>`` specifies the math number.
            - ``PERCent`` specifies that the reference levels are calculated as a percent relative
              to HIGH and LOW. The percentages are defined using the
              ``MEASUrement:MATH<x>:REFLevel:PERCent`` commands.
            - ``ABSolute`` specifies that the reference levels are set explicitly using the
              ``MEASUrement:MATH<x>:REFLevel:ABSolute`` commands. This method is useful when precise
              values are required.
        """
        return self._method

    @property
    def percent(self) -> MeasurementMathItemReflevelsPercent:
        """Return the ``MEASUrement:MATH<x>:REFLevels:PERCent`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MATH<x>:REFLevels:PERCent?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MATH<x>:REFLevels:PERCent?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Info:
            - ``MATH<x>`` specifies the math number.

        Sub-properties:
            - ``.fallhigh``: The ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLHigh`` command.
            - ``.falllow``: The ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLLow`` command.
            - ``.fallmid``: The ``MEASUrement:MATH<x>:REFLevels:PERCent:FALLMid`` command.
            - ``.hysteresis``: The ``MEASUrement:MATH<x>:REFLevels:PERCent:HYSTeresis`` command.
            - ``.risehigh``: The ``MEASUrement:MATH<x>:REFLevels:PERCent:RISEHigh`` command.
            - ``.riselow``: The ``MEASUrement:MATH<x>:REFLevels:PERCent:RISELow`` command.
            - ``.risemid``: The ``MEASUrement:MATH<x>:REFLevels:PERCent:RISEMid`` command.
            - ``.type``: The ``MEASUrement:MATH<x>:REFLevels:PERCent:TYPE`` command.
        """
        return self._percent


class MeasurementMathItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``MEASUrement:MATH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MATH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MATH<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``MATH<x>`` specifies the math number.

    Properties:
        - ``.reflevels``: The ``MEASUrement:MATH<x>:REFLevels`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._reflevels = MeasurementMathItemReflevels(device, f"{self._cmd_syntax}:REFLevels")

    @property
    def reflevels(self) -> MeasurementMathItemReflevels:
        """Return the ``MEASUrement:MATH<x>:REFLevels`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MATH<x>:REFLevels?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MATH<x>:REFLevels?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``MATH<x>`` specifies the math number.

        Sub-properties:
            - ``.absolute``: The ``MEASUrement:MATH<x>:REFLevels:ABSolute`` command tree.
            - ``.basetop``: The ``MEASUrement:MATH<x>:REFLevels:BASETop`` command.
            - ``.method``: The ``MEASUrement:MATH<x>:REFLevels:METHod`` command.
            - ``.percent``: The ``MEASUrement:MATH<x>:REFLevels:PERCent`` command tree.
        """
        return self._reflevels


class MeasurementList(SCPICmdRead):
    """The ``MEASUrement:LIST`` command.

    Description:
        - This query returns a comma separated list of all currently defined measurements.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:LIST?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:LIST?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:LIST?
        ```
    """


class MeasurementInterp(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:INTERp`` command.

    Description:
        - This command sets or queries the interpolation mode used to locate edge crossings.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:INTERp?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:INTERp?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:INTERp value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:INTERp {AUTO|SINX|LINear}
        - MEASUrement:INTERp?
        ```

    Info:
        - ``AUTO`` automatically selects the interpolation mode.
        - ``SINX`` specifies sin(x)/x interpolation, where acquired points are fit to a curve.
        - ``LINear`` specifies linear interpolation, where acquired points are connected with
          straight lines.
    """


class MeasurementGatingStarttime(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:GATing:STARTtime`` command.

    Description:
        - Sets or queries the start gate time for all measurements that use Global gating.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:GATing:STARTtime?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:GATing:STARTtime?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:GATing:STARTtime value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:GATing:STARTtime <NR3>
        - MEASUrement:GATing:STARTtime?
        ```

    Info:
        - ``<NR3>`` is the time gating start gate time in seconds. The valid range is -10000 s to
          10000 s.
    """


class MeasurementGatingSearchsource(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:GATing:SEARCHSource`` command.

    Description:
        - This command sets or queries the global gating search source when the gating type is
          search.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:GATing:SEARCHSource?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:GATing:SEARCHSource?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:GATing:SEARCHSource value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:GATing:SEARCHSource SEARCH<x>
        - MEASUrement:GATing:SEARCHSource?
        ```

    Info:
        - ``SEARCH<x>`` specifies the search source.
    """


class MeasurementGatingMidref(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:GATing:MIDRef`` command.

    Description:
        - This command sets or queries the global gating mid ref value used for logic gating.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:GATing:MIDRef?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:GATing:MIDRef?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:GATing:MIDRef value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:GATing:MIDRef <NR3>
        - MEASUrement:GATing:MIDRef?
        ```

    Info:
        - ``<NR3>`` is the mid ref value for gating.
    """


class MeasurementGatingLogicsource(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:GATing:LOGICSource`` command.

    Description:
        - This command sets or queries the gating data source used for logic gating.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:GATing:LOGICSource?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:GATing:LOGICSource?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:GATing:LOGICSource value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:GATing:LOGICSource {CH<x>|MATH<x>|REF<x>}
        - MEASUrement:GATing:LOGICSource?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as source.
        - ``MATH<x>`` specifies a math channel as source.
        - ``REF<x>`` specifies a reference waveform as the source.
    """


class MeasurementGatingHysteresis(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:GATing:HYSTeresis`` command.

    Description:
        - This command sets or queries the global gating hysteresis value used for logic gating.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:GATing:HYSTeresis?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:GATing:HYSTeresis?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:GATing:HYSTeresis value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:GATing:HYSTeresis <NR3>
        - MEASUrement:GATing:HYSTeresis?
        ```

    Info:
        - ``<NR3>`` is the gating hysteresis.
    """


class MeasurementGatingEndtime(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:GATing:ENDtime`` command.

    Description:
        - Sets or queries the end gate time for all measurements that use Global gating.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:GATing:ENDtime?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:GATing:ENDtime?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:GATing:ENDtime value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:GATing:ENDtime <NR3>
        - MEASUrement:GATing:ENDtime?
        ```

    Info:
        - ``<NR3>`` is the time gating end gate time in seconds. The valid range is -10000 s to
          10000 s.
    """


class MeasurementGatingActive(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:GATing:ACTive`` command.

    Description:
        - This command sets or queries the global gating active level used for logic gating.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:GATing:ACTive?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:GATing:ACTive?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:GATing:ACTive value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:GATing:ACTive {HIGH|LOW}
        - MEASUrement:GATing:ACTive?
        ```

    Info:
        - ``HIGH`` specifies the gate is HIGH.
        - ``LOW`` specifies the gate is LOW.
    """


class MeasurementGating(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:GATing`` command.

    Description:
        - This command sets or queries the global gating type for the measurement.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:GATing?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:GATing?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:GATing value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:GATing {NONE|SCREEN|CURSor|LOGic|SEARch|TIMe}
        - MEASUrement:GATing?
        ```

    Info:
        - ``NONE`` turns off measurement gating.
        - ``SCREen`` turns on gating, using the left and right edges of the screen.
        - ``CURSor`` limits measurements to the portion of the waveform between the vertical bar
          cursors, even if they are off screen.
        - ``LOGic`` specifies that measurements are taken only on the portion of the waveform where
          the logic source is in the active state.
        - ``SEARCH`` specifies that measurements are taken based on search criteria.
        - ``TIMe`` limits measurements to the portion of the waveform between the Start and End gate
          times.

    Properties:
        - ``.active``: The ``MEASUrement:GATing:ACTive`` command.
        - ``.endtime``: The ``MEASUrement:GATing:ENDtime`` command.
        - ``.hysteresis``: The ``MEASUrement:GATing:HYSTeresis`` command.
        - ``.logicsource``: The ``MEASUrement:GATing:LOGICSource`` command.
        - ``.midref``: The ``MEASUrement:GATing:MIDRef`` command.
        - ``.searchsource``: The ``MEASUrement:GATing:SEARCHSource`` command.
        - ``.starttime``: The ``MEASUrement:GATing:STARTtime`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._active = MeasurementGatingActive(device, f"{self._cmd_syntax}:ACTive")
        self._endtime = MeasurementGatingEndtime(device, f"{self._cmd_syntax}:ENDtime")
        self._hysteresis = MeasurementGatingHysteresis(device, f"{self._cmd_syntax}:HYSTeresis")
        self._logicsource = MeasurementGatingLogicsource(device, f"{self._cmd_syntax}:LOGICSource")
        self._midref = MeasurementGatingMidref(device, f"{self._cmd_syntax}:MIDRef")
        self._searchsource = MeasurementGatingSearchsource(
            device, f"{self._cmd_syntax}:SEARCHSource"
        )
        self._starttime = MeasurementGatingStarttime(device, f"{self._cmd_syntax}:STARTtime")

    @property
    def active(self) -> MeasurementGatingActive:
        """Return the ``MEASUrement:GATing:ACTive`` command.

        Description:
            - This command sets or queries the global gating active level used for logic gating.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:GATing:ACTive?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:GATing:ACTive?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:GATing:ACTive value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:GATing:ACTive {HIGH|LOW}
            - MEASUrement:GATing:ACTive?
            ```

        Info:
            - ``HIGH`` specifies the gate is HIGH.
            - ``LOW`` specifies the gate is LOW.
        """
        return self._active

    @property
    def endtime(self) -> MeasurementGatingEndtime:
        """Return the ``MEASUrement:GATing:ENDtime`` command.

        Description:
            - Sets or queries the end gate time for all measurements that use Global gating.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:GATing:ENDtime?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:GATing:ENDtime?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:GATing:ENDtime value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:GATing:ENDtime <NR3>
            - MEASUrement:GATing:ENDtime?
            ```

        Info:
            - ``<NR3>`` is the time gating end gate time in seconds. The valid range is -10000 s to
              10000 s.
        """
        return self._endtime

    @property
    def hysteresis(self) -> MeasurementGatingHysteresis:
        """Return the ``MEASUrement:GATing:HYSTeresis`` command.

        Description:
            - This command sets or queries the global gating hysteresis value used for logic gating.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:GATing:HYSTeresis?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:GATing:HYSTeresis?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:GATing:HYSTeresis value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:GATing:HYSTeresis <NR3>
            - MEASUrement:GATing:HYSTeresis?
            ```

        Info:
            - ``<NR3>`` is the gating hysteresis.
        """
        return self._hysteresis

    @property
    def logicsource(self) -> MeasurementGatingLogicsource:
        """Return the ``MEASUrement:GATing:LOGICSource`` command.

        Description:
            - This command sets or queries the gating data source used for logic gating.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:GATing:LOGICSource?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:GATing:LOGICSource?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:GATing:LOGICSource value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:GATing:LOGICSource {CH<x>|MATH<x>|REF<x>}
            - MEASUrement:GATing:LOGICSource?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as source.
            - ``MATH<x>`` specifies a math channel as source.
            - ``REF<x>`` specifies a reference waveform as the source.
        """
        return self._logicsource

    @property
    def midref(self) -> MeasurementGatingMidref:
        """Return the ``MEASUrement:GATing:MIDRef`` command.

        Description:
            - This command sets or queries the global gating mid ref value used for logic gating.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:GATing:MIDRef?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:GATing:MIDRef?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:GATing:MIDRef value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:GATing:MIDRef <NR3>
            - MEASUrement:GATing:MIDRef?
            ```

        Info:
            - ``<NR3>`` is the mid ref value for gating.
        """
        return self._midref

    @property
    def searchsource(self) -> MeasurementGatingSearchsource:
        """Return the ``MEASUrement:GATing:SEARCHSource`` command.

        Description:
            - This command sets or queries the global gating search source when the gating type is
              search.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:GATing:SEARCHSource?``
              query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:GATing:SEARCHSource?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:GATing:SEARCHSource value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:GATing:SEARCHSource SEARCH<x>
            - MEASUrement:GATing:SEARCHSource?
            ```

        Info:
            - ``SEARCH<x>`` specifies the search source.
        """
        return self._searchsource

    @property
    def starttime(self) -> MeasurementGatingStarttime:
        """Return the ``MEASUrement:GATing:STARTtime`` command.

        Description:
            - Sets or queries the start gate time for all measurements that use Global gating.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:GATing:STARTtime?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:GATing:STARTtime?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:GATing:STARTtime value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:GATing:STARTtime <NR3>
            - MEASUrement:GATing:STARTtime?
            ```

        Info:
            - ``<NR3>`` is the time gating start gate time in seconds. The valid range is -10000 s
              to 10000 s.
        """
        return self._starttime


class MeasurementEdgeItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:EDGE<x>`` command.

    Description:
        - This command sets or queries the type of the edge for the measurement.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:EDGE<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:EDGE<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:EDGE<x> value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:EDGE<x> {RISE|FALL|BOTH}
        - MEASUrement:EDGE<x>?
        ```

    Info:
        - ``FALL`` specifies the falling edge of the waveform.
        - ``RISE`` specifies the rising edge of the waveform.
        - ``BOTH`` specifies both a rising and falling edge of the waveform.
    """


class MeasurementDelete(SCPICmdWrite):
    """The ``MEASUrement:DELete`` command.

    Description:
        - The command deletes the specified measurement.

    Usage:
        - Using the ``.write(value)`` method will send the ``MEASUrement:DELete value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:DELete <QString>
        ```

    Info:
        - ``<QString>`` is the measurement to delete. Argument is of the form 'MEAS<NR1>' where
          <NR1> is ≥1.
    """

    _WRAP_ARG_WITH_QUOTES = True


class MeasurementDeleteall(SCPICmdWriteNoArguments):
    """The ``MEASUrement:DELETEALL`` command.

    Description:
        - This command deletes all the active instances of measurements defined in the scope
          application.

    Usage:
        - Using the ``.write()`` method will send the ``MEASUrement:DELETEALL`` command.

    SCPI Syntax:
        ```
        - MEASUrement:DELETEALL
        ```
    """


class MeasurementChannelReflevelsPercentType(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:CH<x>:REFLevels:PERCent:TYPE`` command.

    Description:
        - This command specifies or queries the reference level percent type for the measurement.
          The channel number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:CH<x>:REFLevels:PERCent:TYPE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:PERCent:TYPE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:PERCent:TYPE value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:CH<x>:REFLevels:PERCent:TYPE {TENNinety|TWENtyeighty|CUSTom}
        - MEASUrement:CH<x>:REFLevels:PERCent:TYPE?
        ```

    Info:
        - ``TENNinety`` specifies reference levels at the 10 and 90% levels.
        - ``TWENtyeighty`` specifies reference levels at the 20 and 80% levels.
        - ``CUSTom`` specifies custom reference levels.
    """


class MeasurementChannelReflevelsPercentRisemid(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:CH<x>:REFLevels:PERCent:RISEMid`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the mid reference level of the rising edge when the measurement
          ref level method is set to percent. The channel number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:CH<x>:REFLevels:PERCent:RISEMid?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:PERCent:RISEMid?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:PERCent:RISEMid value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:CH<x>:REFLevels:PERCent:RISEMid <NR3>
        - MEASUrement:CH<x>:REFLevels:PERCent:RISEMid?
        ```

    Info:
        - ``<NR3>`` is the percentage (where 50% is equal to MID) used to calculate the mid
          reference level when the measurement's Ref level method is set to Percent.
    """


class MeasurementChannelReflevelsPercentRiselow(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:CH<x>:REFLevels:PERCent:RISELow`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the low reference level of the rising edge when the measurement
          ref level method is set to percent. The channel number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:CH<x>:REFLevels:PERCent:RISELow?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:PERCent:RISELow?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:PERCent:RISELow value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:CH<x>:REFLevels:PERCent:RISELow <NR3>
        - MEASUrement:CH<x>:REFLevels:PERCent:RISELow?
        ```

    Info:
        - ``<NR3>`` is the percentage (where 100% is equal to TOP) used to calculate the mid
          reference level when the measurement's Ref level method is set to Percent.
    """


class MeasurementChannelReflevelsPercentRisehigh(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:CH<x>:REFLevels:PERCent:RISEHigh`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the high reference level of the rising edge when the measurement
          ref level method is set to percent. The channel number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:CH<x>:REFLevels:PERCent:RISEHigh?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:PERCent:RISEHigh?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:PERCent:RISEHigh value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:CH<x>:REFLevels:PERCent:RISEHigh <NR3>
        - MEASUrement:CH<x>:REFLevels:PERCent:RISEHigh?
        ```

    Info:
        - ``<NR3>`` is the percentage (where 100% is equal to TOP) used to calculate the high
          reference level when the measurement's Ref level method is set to Percent.
    """


class MeasurementChannelReflevelsPercentHysteresis(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:CH<x>:REFLevels:PERCent:HYSTeresis`` command.

    Description:
        - This command sets or queries the percentage (where 100% is equal to MAX and 0% is equal to
          MIN) used to calculate the hysteresis of the reference level when the measurement ref
          level method is set to percent. The channel number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:CH<x>:REFLevels:PERCent:HYSTeresis?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:PERCent:HYSTeresis?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:PERCent:HYSTeresis value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:CH<x>:REFLevels:PERCent:HYSTeresis <NR3>
        - MEASUrement:CH<x>:REFLevels:PERCent:HYSTeresis?
        ```

    Info:
        - ``<NR3>`` is the hysteresis value used for the autoset.
    """


class MeasurementChannelReflevelsPercentFallmid(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:CH<x>:REFLevels:PERCent:FALLMid`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the mid reference level of the falling edge when the source ref
          level method is set to percent. The channel number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:CH<x>:REFLevels:PERCent:FALLMid?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:PERCent:FALLMid?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:PERCent:FALLMid value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:CH<x>:REFLevels:PERCent:FALLMid <NR3>
        - MEASUrement:CH<x>:REFLevels:PERCent:FALLMid?
        ```

    Info:
        - ``<NR3>`` is the percentage (where 50% is equal to MID) used to calculate the mid
          reference level when the measurement's Ref level method is set to Percent.
    """


class MeasurementChannelReflevelsPercentFalllow(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:CH<x>:REFLevels:PERCent:FALLLow`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the low reference level of the falling edge when the source ref
          level method is set to percent. The channel number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:CH<x>:REFLevels:PERCent:FALLLow?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:PERCent:FALLLow?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:PERCent:FALLLow value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:CH<x>:REFLevels:PERCent:FALLLow <NR3>
        - MEASUrement:CH<x>:REFLevels:PERCent:FALLLow?
        ```

    Info:
        - ``<NR3>`` is the percentage (where 100% is equal to TOP) used to calculate the low
          reference level when the measurement Ref level method is set to Percent.
    """


class MeasurementChannelReflevelsPercentFallhigh(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:CH<x>:REFLevels:PERCent:FALLHigh`` command.

    Description:
        - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal to
          BASE) used to calculate the high reference level of the falling edge when the source ref
          level method is set to percent. The channel number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:CH<x>:REFLevels:PERCent:FALLHigh?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:PERCent:FALLHigh?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:PERCent:FALLHigh value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:CH<x>:REFLevels:PERCent:FALLHigh <NR3>
        - MEASUrement:CH<x>:REFLevels:PERCent:FALLHigh?
        ```

    Info:
        - ``<NR3>`` is the percentage (where 100% is equal to TOP) used to calculate the high
          reference level when the measurement's Ref level method is set to Percent.
    """


#  pylint: disable=too-many-instance-attributes
class MeasurementChannelReflevelsPercent(SCPICmdRead):
    """The ``MEASUrement:CH<x>:REFLevels:PERCent`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:CH<x>:REFLevels:PERCent?``
          query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:CH<x>:REFLevels:PERCent?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.fallhigh``: The ``MEASUrement:CH<x>:REFLevels:PERCent:FALLHigh`` command.
        - ``.falllow``: The ``MEASUrement:CH<x>:REFLevels:PERCent:FALLLow`` command.
        - ``.fallmid``: The ``MEASUrement:CH<x>:REFLevels:PERCent:FALLMid`` command.
        - ``.hysteresis``: The ``MEASUrement:CH<x>:REFLevels:PERCent:HYSTeresis`` command.
        - ``.risehigh``: The ``MEASUrement:CH<x>:REFLevels:PERCent:RISEHigh`` command.
        - ``.riselow``: The ``MEASUrement:CH<x>:REFLevels:PERCent:RISELow`` command.
        - ``.risemid``: The ``MEASUrement:CH<x>:REFLevels:PERCent:RISEMid`` command.
        - ``.type``: The ``MEASUrement:CH<x>:REFLevels:PERCent:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fallhigh = MeasurementChannelReflevelsPercentFallhigh(
            device, f"{self._cmd_syntax}:FALLHigh"
        )
        self._falllow = MeasurementChannelReflevelsPercentFalllow(
            device, f"{self._cmd_syntax}:FALLLow"
        )
        self._fallmid = MeasurementChannelReflevelsPercentFallmid(
            device, f"{self._cmd_syntax}:FALLMid"
        )
        self._hysteresis = MeasurementChannelReflevelsPercentHysteresis(
            device, f"{self._cmd_syntax}:HYSTeresis"
        )
        self._risehigh = MeasurementChannelReflevelsPercentRisehigh(
            device, f"{self._cmd_syntax}:RISEHigh"
        )
        self._riselow = MeasurementChannelReflevelsPercentRiselow(
            device, f"{self._cmd_syntax}:RISELow"
        )
        self._risemid = MeasurementChannelReflevelsPercentRisemid(
            device, f"{self._cmd_syntax}:RISEMid"
        )
        self._type = MeasurementChannelReflevelsPercentType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def fallhigh(self) -> MeasurementChannelReflevelsPercentFallhigh:
        """Return the ``MEASUrement:CH<x>:REFLevels:PERCent:FALLHigh`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the high reference level of the falling edge when the
              source ref level method is set to percent. The channel number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:CH<x>:REFLevels:PERCent:FALLHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:PERCent:FALLHigh?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:PERCent:FALLHigh value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:CH<x>:REFLevels:PERCent:FALLHigh <NR3>
            - MEASUrement:CH<x>:REFLevels:PERCent:FALLHigh?
            ```

        Info:
            - ``<NR3>`` is the percentage (where 100% is equal to TOP) used to calculate the high
              reference level when the measurement's Ref level method is set to Percent.
        """
        return self._fallhigh

    @property
    def falllow(self) -> MeasurementChannelReflevelsPercentFalllow:
        """Return the ``MEASUrement:CH<x>:REFLevels:PERCent:FALLLow`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the low reference level of the falling edge when the source
              ref level method is set to percent. The channel number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:CH<x>:REFLevels:PERCent:FALLLow?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:PERCent:FALLLow?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:PERCent:FALLLow value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:CH<x>:REFLevels:PERCent:FALLLow <NR3>
            - MEASUrement:CH<x>:REFLevels:PERCent:FALLLow?
            ```

        Info:
            - ``<NR3>`` is the percentage (where 100% is equal to TOP) used to calculate the low
              reference level when the measurement Ref level method is set to Percent.
        """
        return self._falllow

    @property
    def fallmid(self) -> MeasurementChannelReflevelsPercentFallmid:
        """Return the ``MEASUrement:CH<x>:REFLevels:PERCent:FALLMid`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the mid reference level of the falling edge when the source
              ref level method is set to percent. The channel number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:CH<x>:REFLevels:PERCent:FALLMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:PERCent:FALLMid?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:PERCent:FALLMid value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:CH<x>:REFLevels:PERCent:FALLMid <NR3>
            - MEASUrement:CH<x>:REFLevels:PERCent:FALLMid?
            ```

        Info:
            - ``<NR3>`` is the percentage (where 50% is equal to MID) used to calculate the mid
              reference level when the measurement's Ref level method is set to Percent.
        """
        return self._fallmid

    @property
    def hysteresis(self) -> MeasurementChannelReflevelsPercentHysteresis:
        """Return the ``MEASUrement:CH<x>:REFLevels:PERCent:HYSTeresis`` command.

        Description:
            - This command sets or queries the percentage (where 100% is equal to MAX and 0% is
              equal to MIN) used to calculate the hysteresis of the reference level when the
              measurement ref level method is set to percent. The channel number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:CH<x>:REFLevels:PERCent:HYSTeresis?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:PERCent:HYSTeresis?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:PERCent:HYSTeresis value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:CH<x>:REFLevels:PERCent:HYSTeresis <NR3>
            - MEASUrement:CH<x>:REFLevels:PERCent:HYSTeresis?
            ```

        Info:
            - ``<NR3>`` is the hysteresis value used for the autoset.
        """
        return self._hysteresis

    @property
    def risehigh(self) -> MeasurementChannelReflevelsPercentRisehigh:
        """Return the ``MEASUrement:CH<x>:REFLevels:PERCent:RISEHigh`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the high reference level of the rising edge when the
              measurement ref level method is set to percent. The channel number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:CH<x>:REFLevels:PERCent:RISEHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:PERCent:RISEHigh?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:PERCent:RISEHigh value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:CH<x>:REFLevels:PERCent:RISEHigh <NR3>
            - MEASUrement:CH<x>:REFLevels:PERCent:RISEHigh?
            ```

        Info:
            - ``<NR3>`` is the percentage (where 100% is equal to TOP) used to calculate the high
              reference level when the measurement's Ref level method is set to Percent.
        """
        return self._risehigh

    @property
    def riselow(self) -> MeasurementChannelReflevelsPercentRiselow:
        """Return the ``MEASUrement:CH<x>:REFLevels:PERCent:RISELow`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the low reference level of the rising edge when the
              measurement ref level method is set to percent. The channel number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:CH<x>:REFLevels:PERCent:RISELow?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:PERCent:RISELow?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:PERCent:RISELow value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:CH<x>:REFLevels:PERCent:RISELow <NR3>
            - MEASUrement:CH<x>:REFLevels:PERCent:RISELow?
            ```

        Info:
            - ``<NR3>`` is the percentage (where 100% is equal to TOP) used to calculate the mid
              reference level when the measurement's Ref level method is set to Percent.
        """
        return self._riselow

    @property
    def risemid(self) -> MeasurementChannelReflevelsPercentRisemid:
        """Return the ``MEASUrement:CH<x>:REFLevels:PERCent:RISEMid`` command.

        Description:
            - This command sets or queries the percentage (where 99% is equal to TOP and 1% is equal
              to BASE) used to calculate the mid reference level of the rising edge when the
              measurement ref level method is set to percent. The channel number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:CH<x>:REFLevels:PERCent:RISEMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:PERCent:RISEMid?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:PERCent:RISEMid value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:CH<x>:REFLevels:PERCent:RISEMid <NR3>
            - MEASUrement:CH<x>:REFLevels:PERCent:RISEMid?
            ```

        Info:
            - ``<NR3>`` is the percentage (where 50% is equal to MID) used to calculate the mid
              reference level when the measurement's Ref level method is set to Percent.
        """
        return self._risemid

    @property
    def type(self) -> MeasurementChannelReflevelsPercentType:
        """Return the ``MEASUrement:CH<x>:REFLevels:PERCent:TYPE`` command.

        Description:
            - This command specifies or queries the reference level percent type for the
              measurement. The channel number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:CH<x>:REFLevels:PERCent:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:PERCent:TYPE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:PERCent:TYPE value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:CH<x>:REFLevels:PERCent:TYPE {TENNinety|TWENtyeighty|CUSTom}
            - MEASUrement:CH<x>:REFLevels:PERCent:TYPE?
            ```

        Info:
            - ``TENNinety`` specifies reference levels at the 10 and 90% levels.
            - ``TWENtyeighty`` specifies reference levels at the 20 and 80% levels.
            - ``CUSTom`` specifies custom reference levels.
        """
        return self._type


class MeasurementChannelReflevelsMethod(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:CH<x>:REFLevels:METHod`` command.

    Description:
        - This command sets or queries the method used to calculate reference levels for the
          measurement. The channel number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:CH<x>:REFLevels:METHod?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:CH<x>:REFLevels:METHod?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:METHod value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:CH<x>:REFLevels:METHod {PERCent|ABSolute}
        - MEASUrement:CH<x>:REFLevels:METHod?
        ```

    Info:
        - ``PERCent`` specifies percent reference level units.
        - ``ABSolute`` specifies absolute reference level units.
    """


class MeasurementChannelReflevelsBasetop(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:CH<x>:REFLevels:BASETop`` command.

    Description:
        - This command sets or queries the method used to calculate the TOP and BASE, used to
          calculate reference levels for the measurement. The channel number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:CH<x>:REFLevels:BASETop?``
          query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:CH<x>:REFLevels:BASETop?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:BASETop value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:CH<x>:REFLevels:BASETop {AUTO|MINMax|MEANhistogram|MODEhistogram}
        - MEASUrement:CH<x>:REFLevels:BASETop?
        ```

    Info:
        - ``AUTO`` automatically chooses a reference level method.
        - ``MINMax`` specifies that reference levels are relative to the measurement MIN and MAX.
        - ``MEANhistogram`` specifies that reference levels are relative to the histogram mean BASE
          and TOP.
        - ``MODEhistogram`` specifies that reference levels are relative to the histogram mode BASE
          and TOP.
    """


class MeasurementChannelReflevelsAbsoluteType(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:CH<x>:REFLevels:ABSolute:TYPE`` command.

    Description:
        - This command sets or queries the reference level type for the source. The channel number
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:CH<x>:REFLevels:ABSolute:TYPE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:ABSolute:TYPE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:ABSolute:TYPE value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:CH<x>:REFLevels:ABSolute:TYPE {SAME|UNIQue}
        - MEASUrement:CH<x>:REFLevels:ABSolute:TYPE?
        ```

    Info:
        - ``SAME`` specifies that the absolute reference levels for the specified measurement
          channel are the same.
        - ``UNIQue`` specifies that the absolute reference levels for the specified measurement
          channel are not the same.
    """


class MeasurementChannelReflevelsAbsoluteRisemid(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:CH<x>:REFLevels:ABSolute:RISEMid`` command.

    Description:
        - This command sets or queries the value used as the mid reference level of the rising edge
          when the source ref level method is set to absolute. The channel number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:CH<x>:REFLevels:ABSolute:RISEMid?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:ABSolute:RISEMid?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:ABSolute:RISEMid value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:CH<x>:REFLevels:ABSolute:RISEMid <NR3>
        - MEASUrement:CH<x>:REFLevels:ABSolute:RISEMid?
        ```

    Info:
        - ``<NR3>`` is the mid reference level of the rising edge when the source ref level method
          is set to absolute.
    """


class MeasurementChannelReflevelsAbsoluteRiselow(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:CH<x>:REFLevels:ABSolute:RISELow`` command.

    Description:
        - This command sets or queries the value used as the low reference level of the rising edge
          when the source ref level method is set to absolute. The channel number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:CH<x>:REFLevels:ABSolute:RISELow?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:ABSolute:RISELow?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:ABSolute:RISELow value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:CH<x>:REFLevels:ABSolute:RISELow <NR3>
        - MEASUrement:CH<x>:REFLevels:ABSolute:RISELow?
        ```

    Info:
        - ``<NR3>`` is the low reference level of the rising edge when the source ref level method
          is set to absolute.
    """


class MeasurementChannelReflevelsAbsoluteRisehigh(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:CH<x>:REFLevels:ABSolute:RISEHigh`` command.

    Description:
        - This command sets or queries the value used as the high reference level of the rising edge
          when the source ref level method is set to absolute. The channel number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:CH<x>:REFLevels:ABSolute:RISEHigh?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:ABSolute:RISEHigh?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:ABSolute:RISEHigh value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:CH<x>:REFLevels:ABSolute:RISEHigh <NR3>
        - MEASUrement:CH<x>:REFLevels:ABSolute:RISEHigh?
        ```

    Info:
        - ``<NR3>`` is the high reference level of the rising edge when the source ref level method
          is set to absolute.
    """


class MeasurementChannelReflevelsAbsoluteHysteresis(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:CH<x>:REFLevels:ABSolute:HYSTeresis`` command.

    Description:
        - This command sets or queries the value of the hysteresis of the reference level when the
          source ref level method is set to absolute. The channel number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:CH<x>:REFLevels:ABSolute:HYSTeresis?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:ABSolute:HYSTeresis?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:ABSolute:HYSTeresis value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:CH<x>:REFLevels:ABSolute:HYSTeresis <NR3>
        - MEASUrement:CH<x>:REFLevels:ABSolute:HYSTeresis?
        ```

    Info:
        - ``<NR3>`` is the hysteresis value used for autoset.
    """


class MeasurementChannelReflevelsAbsoluteFallmid(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLMid`` command.

    Description:
        - This command sets or queries the value used as the mid reference level of the falling edge
          when the source ref level method is set to absolute. The channel number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLMid?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLMid?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLMid value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:CH<x>:REFLevels:ABSolute:FALLMid <NR3>
        - MEASUrement:CH<x>:REFLevels:ABSolute:FALLMid?
        ```

    Info:
        - ``<NR3>`` is the mid reference level used to calculate the mid reference level when the
          measurement's Ref level method is set to Absolute.
    """


class MeasurementChannelReflevelsAbsoluteFalllow(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLLow`` command.

    Description:
        - This command sets or queries the value used as the low reference level of the falling edge
          when the source ref level method is set to absolute. The channel number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLLow?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLLow?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLLow value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:CH<x>:REFLevels:ABSolute:FALLLow <NR3>
        - MEASUrement:CH<x>:REFLevels:ABSolute:FALLLow?
        ```

    Info:
        - ``<NR3>`` is the high reference level, and is the zero percent level when
          ``MEASUrement:IMMed:REFLevel:METHod`` is set to Absolute.
    """


class MeasurementChannelReflevelsAbsoluteFallhigh(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLHigh`` command.

    Description:
        - This command sets or queries the value used as the high reference level of the falling
          edge when the source ref level method is set to absolute. The channel number is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLHigh?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLHigh?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLHigh value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:CH<x>:REFLevels:ABSolute:FALLHigh <NR3>
        - MEASUrement:CH<x>:REFLevels:ABSolute:FALLHigh?
        ```

    Info:
        - ``<NR3>`` is the high reference level, and is the zero percent level when
          ``MEASUrement:IMMed:REFLevel:METHod`` is set to Absolute.
    """


#  pylint: disable=too-many-instance-attributes
class MeasurementChannelReflevelsAbsolute(SCPICmdRead):
    """The ``MEASUrement:CH<x>:REFLevels:ABSolute`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:CH<x>:REFLevels:ABSolute?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:CH<x>:REFLevels:ABSolute?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.fallhigh``: The ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLHigh`` command.
        - ``.falllow``: The ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLLow`` command.
        - ``.fallmid``: The ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLMid`` command.
        - ``.hysteresis``: The ``MEASUrement:CH<x>:REFLevels:ABSolute:HYSTeresis`` command.
        - ``.risehigh``: The ``MEASUrement:CH<x>:REFLevels:ABSolute:RISEHigh`` command.
        - ``.riselow``: The ``MEASUrement:CH<x>:REFLevels:ABSolute:RISELow`` command.
        - ``.risemid``: The ``MEASUrement:CH<x>:REFLevels:ABSolute:RISEMid`` command.
        - ``.type``: The ``MEASUrement:CH<x>:REFLevels:ABSolute:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fallhigh = MeasurementChannelReflevelsAbsoluteFallhigh(
            device, f"{self._cmd_syntax}:FALLHigh"
        )
        self._falllow = MeasurementChannelReflevelsAbsoluteFalllow(
            device, f"{self._cmd_syntax}:FALLLow"
        )
        self._fallmid = MeasurementChannelReflevelsAbsoluteFallmid(
            device, f"{self._cmd_syntax}:FALLMid"
        )
        self._hysteresis = MeasurementChannelReflevelsAbsoluteHysteresis(
            device, f"{self._cmd_syntax}:HYSTeresis"
        )
        self._risehigh = MeasurementChannelReflevelsAbsoluteRisehigh(
            device, f"{self._cmd_syntax}:RISEHigh"
        )
        self._riselow = MeasurementChannelReflevelsAbsoluteRiselow(
            device, f"{self._cmd_syntax}:RISELow"
        )
        self._risemid = MeasurementChannelReflevelsAbsoluteRisemid(
            device, f"{self._cmd_syntax}:RISEMid"
        )
        self._type = MeasurementChannelReflevelsAbsoluteType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def fallhigh(self) -> MeasurementChannelReflevelsAbsoluteFallhigh:
        """Return the ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLHigh`` command.

        Description:
            - This command sets or queries the value used as the high reference level of the falling
              edge when the source ref level method is set to absolute. The channel number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLHigh?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLHigh value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:CH<x>:REFLevels:ABSolute:FALLHigh <NR3>
            - MEASUrement:CH<x>:REFLevels:ABSolute:FALLHigh?
            ```

        Info:
            - ``<NR3>`` is the high reference level, and is the zero percent level when
              ``MEASUrement:IMMed:REFLevel:METHod`` is set to Absolute.
        """
        return self._fallhigh

    @property
    def falllow(self) -> MeasurementChannelReflevelsAbsoluteFalllow:
        """Return the ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLLow`` command.

        Description:
            - This command sets or queries the value used as the low reference level of the falling
              edge when the source ref level method is set to absolute. The channel number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLLow?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLLow?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLLow value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:CH<x>:REFLevels:ABSolute:FALLLow <NR3>
            - MEASUrement:CH<x>:REFLevels:ABSolute:FALLLow?
            ```

        Info:
            - ``<NR3>`` is the high reference level, and is the zero percent level when
              ``MEASUrement:IMMed:REFLevel:METHod`` is set to Absolute.
        """
        return self._falllow

    @property
    def fallmid(self) -> MeasurementChannelReflevelsAbsoluteFallmid:
        """Return the ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLMid`` command.

        Description:
            - This command sets or queries the value used as the mid reference level of the falling
              edge when the source ref level method is set to absolute. The channel number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLMid?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLMid value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:CH<x>:REFLevels:ABSolute:FALLMid <NR3>
            - MEASUrement:CH<x>:REFLevels:ABSolute:FALLMid?
            ```

        Info:
            - ``<NR3>`` is the mid reference level used to calculate the mid reference level when
              the measurement's Ref level method is set to Absolute.
        """
        return self._fallmid

    @property
    def hysteresis(self) -> MeasurementChannelReflevelsAbsoluteHysteresis:
        """Return the ``MEASUrement:CH<x>:REFLevels:ABSolute:HYSTeresis`` command.

        Description:
            - This command sets or queries the value of the hysteresis of the reference level when
              the source ref level method is set to absolute. The channel number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:CH<x>:REFLevels:ABSolute:HYSTeresis?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:ABSolute:HYSTeresis?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:ABSolute:HYSTeresis value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:CH<x>:REFLevels:ABSolute:HYSTeresis <NR3>
            - MEASUrement:CH<x>:REFLevels:ABSolute:HYSTeresis?
            ```

        Info:
            - ``<NR3>`` is the hysteresis value used for autoset.
        """
        return self._hysteresis

    @property
    def risehigh(self) -> MeasurementChannelReflevelsAbsoluteRisehigh:
        """Return the ``MEASUrement:CH<x>:REFLevels:ABSolute:RISEHigh`` command.

        Description:
            - This command sets or queries the value used as the high reference level of the rising
              edge when the source ref level method is set to absolute. The channel number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:CH<x>:REFLevels:ABSolute:RISEHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:ABSolute:RISEHigh?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:ABSolute:RISEHigh value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:CH<x>:REFLevels:ABSolute:RISEHigh <NR3>
            - MEASUrement:CH<x>:REFLevels:ABSolute:RISEHigh?
            ```

        Info:
            - ``<NR3>`` is the high reference level of the rising edge when the source ref level
              method is set to absolute.
        """
        return self._risehigh

    @property
    def riselow(self) -> MeasurementChannelReflevelsAbsoluteRiselow:
        """Return the ``MEASUrement:CH<x>:REFLevels:ABSolute:RISELow`` command.

        Description:
            - This command sets or queries the value used as the low reference level of the rising
              edge when the source ref level method is set to absolute. The channel number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:CH<x>:REFLevels:ABSolute:RISELow?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:ABSolute:RISELow?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:ABSolute:RISELow value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:CH<x>:REFLevels:ABSolute:RISELow <NR3>
            - MEASUrement:CH<x>:REFLevels:ABSolute:RISELow?
            ```

        Info:
            - ``<NR3>`` is the low reference level of the rising edge when the source ref level
              method is set to absolute.
        """
        return self._riselow

    @property
    def risemid(self) -> MeasurementChannelReflevelsAbsoluteRisemid:
        """Return the ``MEASUrement:CH<x>:REFLevels:ABSolute:RISEMid`` command.

        Description:
            - This command sets or queries the value used as the mid reference level of the rising
              edge when the source ref level method is set to absolute. The channel number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:CH<x>:REFLevels:ABSolute:RISEMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:ABSolute:RISEMid?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:ABSolute:RISEMid value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:CH<x>:REFLevels:ABSolute:RISEMid <NR3>
            - MEASUrement:CH<x>:REFLevels:ABSolute:RISEMid?
            ```

        Info:
            - ``<NR3>`` is the mid reference level of the rising edge when the source ref level
              method is set to absolute.
        """
        return self._risemid

    @property
    def type(self) -> MeasurementChannelReflevelsAbsoluteType:
        """Return the ``MEASUrement:CH<x>:REFLevels:ABSolute:TYPE`` command.

        Description:
            - This command sets or queries the reference level type for the source. The channel
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:CH<x>:REFLevels:ABSolute:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:ABSolute:TYPE?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:ABSolute:TYPE value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:CH<x>:REFLevels:ABSolute:TYPE {SAME|UNIQue}
            - MEASUrement:CH<x>:REFLevels:ABSolute:TYPE?
            ```

        Info:
            - ``SAME`` specifies that the absolute reference levels for the specified measurement
              channel are the same.
            - ``UNIQue`` specifies that the absolute reference levels for the specified measurement
              channel are not the same.
        """
        return self._type


class MeasurementChannelReflevels(SCPICmdRead):
    """The ``MEASUrement:CH<x>:REFLevels`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:CH<x>:REFLevels?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:CH<x>:REFLevels?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.absolute``: The ``MEASUrement:CH<x>:REFLevels:ABSolute`` command tree.
        - ``.basetop``: The ``MEASUrement:CH<x>:REFLevels:BASETop`` command.
        - ``.method``: The ``MEASUrement:CH<x>:REFLevels:METHod`` command.
        - ``.percent``: The ``MEASUrement:CH<x>:REFLevels:PERCent`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._absolute = MeasurementChannelReflevelsAbsolute(device, f"{self._cmd_syntax}:ABSolute")
        self._basetop = MeasurementChannelReflevelsBasetop(device, f"{self._cmd_syntax}:BASETop")
        self._method = MeasurementChannelReflevelsMethod(device, f"{self._cmd_syntax}:METHod")
        self._percent = MeasurementChannelReflevelsPercent(device, f"{self._cmd_syntax}:PERCent")

    @property
    def absolute(self) -> MeasurementChannelReflevelsAbsolute:
        """Return the ``MEASUrement:CH<x>:REFLevels:ABSolute`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:CH<x>:REFLevels:ABSolute?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:ABSolute?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.fallhigh``: The ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLHigh`` command.
            - ``.falllow``: The ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLLow`` command.
            - ``.fallmid``: The ``MEASUrement:CH<x>:REFLevels:ABSolute:FALLMid`` command.
            - ``.hysteresis``: The ``MEASUrement:CH<x>:REFLevels:ABSolute:HYSTeresis`` command.
            - ``.risehigh``: The ``MEASUrement:CH<x>:REFLevels:ABSolute:RISEHigh`` command.
            - ``.riselow``: The ``MEASUrement:CH<x>:REFLevels:ABSolute:RISELow`` command.
            - ``.risemid``: The ``MEASUrement:CH<x>:REFLevels:ABSolute:RISEMid`` command.
            - ``.type``: The ``MEASUrement:CH<x>:REFLevels:ABSolute:TYPE`` command.
        """
        return self._absolute

    @property
    def basetop(self) -> MeasurementChannelReflevelsBasetop:
        """Return the ``MEASUrement:CH<x>:REFLevels:BASETop`` command.

        Description:
            - This command sets or queries the method used to calculate the TOP and BASE, used to
              calculate reference levels for the measurement. The channel number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:CH<x>:REFLevels:BASETop?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:BASETop?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:BASETop value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:CH<x>:REFLevels:BASETop {AUTO|MINMax|MEANhistogram|MODEhistogram}
            - MEASUrement:CH<x>:REFLevels:BASETop?
            ```

        Info:
            - ``AUTO`` automatically chooses a reference level method.
            - ``MINMax`` specifies that reference levels are relative to the measurement MIN and
              MAX.
            - ``MEANhistogram`` specifies that reference levels are relative to the histogram mean
              BASE and TOP.
            - ``MODEhistogram`` specifies that reference levels are relative to the histogram mode
              BASE and TOP.
        """
        return self._basetop

    @property
    def method(self) -> MeasurementChannelReflevelsMethod:
        """Return the ``MEASUrement:CH<x>:REFLevels:METHod`` command.

        Description:
            - This command sets or queries the method used to calculate reference levels for the
              measurement. The channel number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:CH<x>:REFLevels:METHod?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:METHod?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:METHod value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:CH<x>:REFLevels:METHod {PERCent|ABSolute}
            - MEASUrement:CH<x>:REFLevels:METHod?
            ```

        Info:
            - ``PERCent`` specifies percent reference level units.
            - ``ABSolute`` specifies absolute reference level units.
        """
        return self._method

    @property
    def percent(self) -> MeasurementChannelReflevelsPercent:
        """Return the ``MEASUrement:CH<x>:REFLevels:PERCent`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:CH<x>:REFLevels:PERCent?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:CH<x>:REFLevels:PERCent?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.fallhigh``: The ``MEASUrement:CH<x>:REFLevels:PERCent:FALLHigh`` command.
            - ``.falllow``: The ``MEASUrement:CH<x>:REFLevels:PERCent:FALLLow`` command.
            - ``.fallmid``: The ``MEASUrement:CH<x>:REFLevels:PERCent:FALLMid`` command.
            - ``.hysteresis``: The ``MEASUrement:CH<x>:REFLevels:PERCent:HYSTeresis`` command.
            - ``.risehigh``: The ``MEASUrement:CH<x>:REFLevels:PERCent:RISEHigh`` command.
            - ``.riselow``: The ``MEASUrement:CH<x>:REFLevels:PERCent:RISELow`` command.
            - ``.risemid``: The ``MEASUrement:CH<x>:REFLevels:PERCent:RISEMid`` command.
            - ``.type``: The ``MEASUrement:CH<x>:REFLevels:PERCent:TYPE`` command.
        """
        return self._percent


class MeasurementChannel(ValidatedChannel, SCPICmdRead):
    """The ``MEASUrement:CH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:CH<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.reflevels``: The ``MEASUrement:CH<x>:REFLevels`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._reflevels = MeasurementChannelReflevels(device, f"{self._cmd_syntax}:REFLevels")

    @property
    def reflevels(self) -> MeasurementChannelReflevels:
        """Return the ``MEASUrement:CH<x>:REFLevels`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:CH<x>:REFLevels?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:CH<x>:REFLevels?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.absolute``: The ``MEASUrement:CH<x>:REFLevels:ABSolute`` command tree.
            - ``.basetop``: The ``MEASUrement:CH<x>:REFLevels:BASETop`` command.
            - ``.method``: The ``MEASUrement:CH<x>:REFLevels:METHod`` command.
            - ``.percent``: The ``MEASUrement:CH<x>:REFLevels:PERCent`` command tree.
        """
        return self._reflevels


class MeasurementAnnotate(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:ANNOTate`` command.

    Description:
        - This command sets or queries the annotation state for measurements.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:ANNOTate?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:ANNOTate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:ANNOTate value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:ANNOTate {OFF|AUTO}
        - MEASUrement:ANNOTate?
        ```

    Info:
        - ``OFF`` turns off measurement annotations.
        - ``AUTO`` turns on visible measurement annotations.
    """


class MeasurementAddnew(SCPICmdWrite):
    """The ``MEASUrement:ADDNew`` command.

    Description:
        - This command adds the specified measurement.

    Usage:
        - Using the ``.write(value)`` method will send the ``MEASUrement:ADDNew value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:ADDNew 'QString'
        ```

    Info:
        - ``'QString'`` is the measurement to add. The argument is of the form 'MEAS<NR1>' where NR1
          ≥ 1.
    """


class MeasurementAddmeas(SCPICmdWrite):
    """The ``MEASUrement:ADDMEAS`` command.

    Description:
        - This command adds a measurement.

    Usage:
        - Using the ``.write(value)`` method will send the ``MEASUrement:ADDMEAS value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:ADDMEAS {ACRMS|AMPlITUDE|AREA|BASE|BURSTWIDTH|DATARATE|DELAY|FALLSLEWRATE|FALLTIME|FREQUENCY|HIGHTIME|HOLD|LOWTIME|MAXIMUM|MEAN|MINIMUM|NDUty|NOVERSHOOT|NPERIOD|NWIDTTH|PDUTY|PERIOD|PHASE|PK2Pk|POVERSHOOT|PWIDTH|RISESLEWRATE|RISETIME|RMS|SETUP|SKEW|TIMEOUTSIDELEVEL|TIMETOMAX|TIMETOMIN|TOP}
        ```

    Info:
        - ``ACRMS`` (AC RMS) is the true Root Mean Square of the data points, about the Mean. This
          measurement can be made across the entire record, or on each cycle in the record.
        - ``AMPLITUDE`` is the difference between the Top value and the Base value. This measurement
          can be made across the entire record, or on each cycle in the record.
        - ``AREA`` is the area under the curve, calculated by integrating the data points. The area
          measured above ground is positive. The area measured below ground is negative. This
          measurement can be made across the entire record, or on each cycle in the record.
        - ``BASE`` is the most common data value below the midpoint of the waveform. This
          measurement can be made across the entire record, or on each cycle in the record.
        - ``BURSTWIDTH`` (Burst Width) is the duration of a series of adjacent crossings of the Mid
          reference level (RM). Bursts are separated by a user-defined idle time (tI). This
          measurement is made on each burst in the record.
        - ``DATARATE`` (Data Rate) is the reciprocal of Unit Interval. This measurement is made on
          each bit in the record.
        - ``DELay`` is the time between the specified Mid reference level (RM) crossing on one
          source to a specified Mid reference level (RM) crossing on a second source. This
          measurement is made on the first occurrence in the record.
        - ``FALLSLEWRATE`` (Falling Slew Rate) is the rate of change in voltage as an edge
          transitions from the Top reference level (RT) to the Bottom reference level (RB). This
          measurement is made on each cycle in the record.
        - ``FALLTIME`` (Fall Time) is the time required for an edge to fall from the Top reference
          level (RT) to the Base reference level (RB). This measurement is made on each cycle in the
          record.
        - ``FREQuency`` is the reciprocal of Period. This measurement is made on each cycle in the
          record.
        - ``HIGHTIME`` (High Time) is the time the signal remains above the Top reference level
          (RT). This measurement is made on each cycle in the record.
        - ``HOLD`` (Hold Time) is the time between the specified Mid reference level crossing (RM)
          on the Clock source to the closest specified Mid reference level (RM) crossing on the Data
          source. This measurement is made on each specified Clock edge in the record.
        - ``LOWTIME`` (Low Time) is the time the signal remains below the Base reference level (RB).
          This measurement is made on each cycle in the record.
        - ``MAXimum`` is the maximum data point. This measurement can be made across the entire
          record, or on each cycle in the record.
        - ``MEAN`` is the arithmetic mean of the data points. This measurement can be made across
          the entire record, or on each cycle in the record.
        - ``MINImum`` is the minimum data point. This measurement can be made across the entire
          record, or on each cycle in the record.
        - ``NDUty`` (Negative Duty Cycle) is the ratio of the Negative Pulse Width to the Period.
          This measurement is made on each cycle in the record.
        - ``NPERIOD`` (Duration N-Periods) is the time required to complete N cycles. A cycle is the
          time between two adjacent (same direction) crossings of the Mid reference level (RM). This
          measurement is made on each cycle in the record.
        - ``NOVershoot`` (Negative Overshoot) is the difference between Minimum and Base, divided by
          the Amplitude. This measurement can be made across the entire record, or on each cycle in
          the record.
        - ``NWIdth`` (Negative Pulse Width) is the time the signal remains below the Mid reference
          level (RM). This measurement is made on each cycle in the record.
        - ``PDUTY`` (Positive Duty Cycle) is the ratio of the Positive Pulse Width to the Period.
          This measurement is made on each cycle in the record.
        - ``PERIOD`` is the time required to complete a cycle. A cycle is the time between two
          adjacent (same direction) crossings of the Mid reference level (RM). This measurement is
          made on each cycle in the record.
        - ``PHASE`` is the ratio of the Skew between two sources to the Period of the first source.
          This measurement is made on each cycle in the record.
        - ``PK2Pk`` (Peak-to-peak) is the difference between Maximum and Minimum. This measurement
          can be made across the entire record, or on each cycle in the record.
        - ``POVERSHOOT`` (Positive Overshoot) is the difference between Maximum and Top, divided by
          the Amplitude. This measurement can be made across the entire record, or on each cycle in
          the record.
        - ``PWIDTH`` (Positive Pulse Width) is the time the signal remains above the Mid reference
          level (RM). This measurement is made on each cycle in the record.
        - ``RISESLEWRATE`` (Rising Slew Rate) is the rate of change in voltage as an edge
          transitions from the Base reference level (RB) to the Top reference level (RT). This
          measurement is made on each cycle in the record.
        - ``RISETIME`` Rise Time is the time required for an edge to rise from the Base reference
          level (RB) to the Top reference level (RT). This measurement is made on each cycle in the
          record.
        - ``RMS`` is the true Root Mean Square of the data points. This measurement can be made
          across the entire record, or on each cycle in the record.
        - ``SETUP`` (Setup Time) is the time between the specified Mid reference level (RM) crossing
          on the Data source to the closest specified Mid reference level (RM) crossing on the Clock
          source. This measurement is made on each specified Clock edge in the record.
        - ``SKEW`` Skew is the time between the specified Mid reference level (RM) crossing on one
          source to the following specified Mid reference level (RM) crossing on a second source.
          This measurement is made on each cycle in the record.
        - ``TIMEOUTSIDELEVEL`` Time Outside Level is the time the signal remains above the Top
          reference level (RT) and/or below the Base reference level (RB). This measurement is made
          on each occurrence in the record.
        - ``TIMETOMAX`` Time to Max is the amount of time from the trigger point to the maximum data
          point. This measurement can be made across the entire record or on each cycle in the
          record.
        - ``TIMETOMIN`` Time to Min is the amount of time from the trigger point to the minimum data
          point. This measurement can be made across the entire record or on each cycle in the
          record.
        - ``TOP`` is the most common data value above the midpoint of the waveform. This measurement
          can be made across the entire record, or on each cycle in the record.
    """  # noqa: E501


#  pylint: disable=too-many-instance-attributes
class Measurement(SCPICmdRead):
    """The ``MEASUrement`` command.

    Description:
        - This query-only command returns all measurement parameters.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement?
        ```

    Properties:
        - ``.addmeas``: The ``MEASUrement:ADDMEAS`` command.
        - ``.addnew``: The ``MEASUrement:ADDNew`` command.
        - ``.annotate``: The ``MEASUrement:ANNOTate`` command.
        - ``.ch``: The ``MEASUrement:CH<x>`` command tree.
        - ``.deleteall``: The ``MEASUrement:DELETEALL`` command.
        - ``.delete``: The ``MEASUrement:DELete`` command.
        - ``.edge``: The ``MEASUrement:EDGE<x>`` command.
        - ``.gating``: The ``MEASUrement:GATing`` command.
        - ``.interp``: The ``MEASUrement:INTERp`` command.
        - ``.list``: The ``MEASUrement:LIST`` command.
        - ``.math``: The ``MEASUrement:MATH<x>`` command tree.
        - ``.meas``: The ``MEASUrement:MEAS<x>`` command tree.
        - ``.ref``: The ``MEASUrement:REF<x>`` command tree.
        - ``.reflevels``: The ``MEASUrement:REFLevels`` command tree.
        - ``.statistics``: The ``MEASUrement:STATIstics`` command tree.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "MEASUrement"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._addmeas = MeasurementAddmeas(device, f"{self._cmd_syntax}:ADDMEAS")
        self._addnew = MeasurementAddnew(device, f"{self._cmd_syntax}:ADDNew")
        self._annotate = MeasurementAnnotate(device, f"{self._cmd_syntax}:ANNOTate")
        self._ch: Dict[int, MeasurementChannel] = DefaultDictPassKeyToFactory(
            lambda x: MeasurementChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._deleteall = MeasurementDeleteall(device, f"{self._cmd_syntax}:DELETEALL")
        self._delete = MeasurementDelete(device, f"{self._cmd_syntax}:DELete")
        self._edge: Dict[int, MeasurementEdgeItem] = DefaultDictPassKeyToFactory(
            lambda x: MeasurementEdgeItem(device, f"{self._cmd_syntax}:EDGE{x}")
        )
        self._gating = MeasurementGating(device, f"{self._cmd_syntax}:GATing")
        self._interp = MeasurementInterp(device, f"{self._cmd_syntax}:INTERp")
        self._list = MeasurementList(device, f"{self._cmd_syntax}:LIST")
        self._math: Dict[int, MeasurementMathItem] = DefaultDictPassKeyToFactory(
            lambda x: MeasurementMathItem(device, f"{self._cmd_syntax}:MATH{x}")
        )
        self._meas: Dict[int, MeasurementMeasItem] = DefaultDictPassKeyToFactory(
            lambda x: MeasurementMeasItem(device, f"{self._cmd_syntax}:MEAS{x}")
        )
        self._ref: Dict[int, MeasurementRefItem] = DefaultDictPassKeyToFactory(
            lambda x: MeasurementRefItem(device, f"{self._cmd_syntax}:REF{x}")
        )
        self._reflevels = MeasurementReflevels(device, f"{self._cmd_syntax}:REFLevels")
        self._statistics = MeasurementStatistics(device, f"{self._cmd_syntax}:STATIstics")

    @property
    def addmeas(self) -> MeasurementAddmeas:
        """Return the ``MEASUrement:ADDMEAS`` command.

        Description:
            - This command adds a measurement.

        Usage:
            - Using the ``.write(value)`` method will send the ``MEASUrement:ADDMEAS value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:ADDMEAS {ACRMS|AMPlITUDE|AREA|BASE|BURSTWIDTH|DATARATE|DELAY|FALLSLEWRATE|FALLTIME|FREQUENCY|HIGHTIME|HOLD|LOWTIME|MAXIMUM|MEAN|MINIMUM|NDUty|NOVERSHOOT|NPERIOD|NWIDTTH|PDUTY|PERIOD|PHASE|PK2Pk|POVERSHOOT|PWIDTH|RISESLEWRATE|RISETIME|RMS|SETUP|SKEW|TIMEOUTSIDELEVEL|TIMETOMAX|TIMETOMIN|TOP}
            ```

        Info:
            - ``ACRMS`` (AC RMS) is the true Root Mean Square of the data points, about the Mean.
              This measurement can be made across the entire record, or on each cycle in the record.
            - ``AMPLITUDE`` is the difference between the Top value and the Base value. This
              measurement can be made across the entire record, or on each cycle in the record.
            - ``AREA`` is the area under the curve, calculated by integrating the data points. The
              area measured above ground is positive. The area measured below ground is negative.
              This measurement can be made across the entire record, or on each cycle in the record.
            - ``BASE`` is the most common data value below the midpoint of the waveform. This
              measurement can be made across the entire record, or on each cycle in the record.
            - ``BURSTWIDTH`` (Burst Width) is the duration of a series of adjacent crossings of the
              Mid reference level (RM). Bursts are separated by a user-defined idle time (tI). This
              measurement is made on each burst in the record.
            - ``DATARATE`` (Data Rate) is the reciprocal of Unit Interval. This measurement is made
              on each bit in the record.
            - ``DELay`` is the time between the specified Mid reference level (RM) crossing on one
              source to a specified Mid reference level (RM) crossing on a second source. This
              measurement is made on the first occurrence in the record.
            - ``FALLSLEWRATE`` (Falling Slew Rate) is the rate of change in voltage as an edge
              transitions from the Top reference level (RT) to the Bottom reference level (RB). This
              measurement is made on each cycle in the record.
            - ``FALLTIME`` (Fall Time) is the time required for an edge to fall from the Top
              reference level (RT) to the Base reference level (RB). This measurement is made on
              each cycle in the record.
            - ``FREQuency`` is the reciprocal of Period. This measurement is made on each cycle in
              the record.
            - ``HIGHTIME`` (High Time) is the time the signal remains above the Top reference level
              (RT). This measurement is made on each cycle in the record.
            - ``HOLD`` (Hold Time) is the time between the specified Mid reference level crossing
              (RM) on the Clock source to the closest specified Mid reference level (RM) crossing on
              the Data source. This measurement is made on each specified Clock edge in the record.
            - ``LOWTIME`` (Low Time) is the time the signal remains below the Base reference level
              (RB). This measurement is made on each cycle in the record.
            - ``MAXimum`` is the maximum data point. This measurement can be made across the entire
              record, or on each cycle in the record.
            - ``MEAN`` is the arithmetic mean of the data points. This measurement can be made
              across the entire record, or on each cycle in the record.
            - ``MINImum`` is the minimum data point. This measurement can be made across the entire
              record, or on each cycle in the record.
            - ``NDUty`` (Negative Duty Cycle) is the ratio of the Negative Pulse Width to the
              Period. This measurement is made on each cycle in the record.
            - ``NPERIOD`` (Duration N-Periods) is the time required to complete N cycles. A cycle is
              the time between two adjacent (same direction) crossings of the Mid reference level
              (RM). This measurement is made on each cycle in the record.
            - ``NOVershoot`` (Negative Overshoot) is the difference between Minimum and Base,
              divided by the Amplitude. This measurement can be made across the entire record, or on
              each cycle in the record.
            - ``NWIdth`` (Negative Pulse Width) is the time the signal remains below the Mid
              reference level (RM). This measurement is made on each cycle in the record.
            - ``PDUTY`` (Positive Duty Cycle) is the ratio of the Positive Pulse Width to the
              Period. This measurement is made on each cycle in the record.
            - ``PERIOD`` is the time required to complete a cycle. A cycle is the time between two
              adjacent (same direction) crossings of the Mid reference level (RM). This measurement
              is made on each cycle in the record.
            - ``PHASE`` is the ratio of the Skew between two sources to the Period of the first
              source. This measurement is made on each cycle in the record.
            - ``PK2Pk`` (Peak-to-peak) is the difference between Maximum and Minimum. This
              measurement can be made across the entire record, or on each cycle in the record.
            - ``POVERSHOOT`` (Positive Overshoot) is the difference between Maximum and Top, divided
              by the Amplitude. This measurement can be made across the entire record, or on each
              cycle in the record.
            - ``PWIDTH`` (Positive Pulse Width) is the time the signal remains above the Mid
              reference level (RM). This measurement is made on each cycle in the record.
            - ``RISESLEWRATE`` (Rising Slew Rate) is the rate of change in voltage as an edge
              transitions from the Base reference level (RB) to the Top reference level (RT). This
              measurement is made on each cycle in the record.
            - ``RISETIME`` Rise Time is the time required for an edge to rise from the Base
              reference level (RB) to the Top reference level (RT). This measurement is made on each
              cycle in the record.
            - ``RMS`` is the true Root Mean Square of the data points. This measurement can be made
              across the entire record, or on each cycle in the record.
            - ``SETUP`` (Setup Time) is the time between the specified Mid reference level (RM)
              crossing on the Data source to the closest specified Mid reference level (RM) crossing
              on the Clock source. This measurement is made on each specified Clock edge in the
              record.
            - ``SKEW`` Skew is the time between the specified Mid reference level (RM) crossing on
              one source to the following specified Mid reference level (RM) crossing on a second
              source. This measurement is made on each cycle in the record.
            - ``TIMEOUTSIDELEVEL`` Time Outside Level is the time the signal remains above the Top
              reference level (RT) and/or below the Base reference level (RB). This measurement is
              made on each occurrence in the record.
            - ``TIMETOMAX`` Time to Max is the amount of time from the trigger point to the maximum
              data point. This measurement can be made across the entire record or on each cycle in
              the record.
            - ``TIMETOMIN`` Time to Min is the amount of time from the trigger point to the minimum
              data point. This measurement can be made across the entire record or on each cycle in
              the record.
            - ``TOP`` is the most common data value above the midpoint of the waveform. This
              measurement can be made across the entire record, or on each cycle in the record.
        """  # noqa: E501
        return self._addmeas

    @property
    def addnew(self) -> MeasurementAddnew:
        """Return the ``MEASUrement:ADDNew`` command.

        Description:
            - This command adds the specified measurement.

        Usage:
            - Using the ``.write(value)`` method will send the ``MEASUrement:ADDNew value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:ADDNew 'QString'
            ```

        Info:
            - ``'QString'`` is the measurement to add. The argument is of the form 'MEAS<NR1>' where
              NR1 ≥ 1.
        """
        return self._addnew

    @property
    def annotate(self) -> MeasurementAnnotate:
        """Return the ``MEASUrement:ANNOTate`` command.

        Description:
            - This command sets or queries the annotation state for measurements.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:ANNOTate?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:ANNOTate?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:ANNOTate value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:ANNOTate {OFF|AUTO}
            - MEASUrement:ANNOTate?
            ```

        Info:
            - ``OFF`` turns off measurement annotations.
            - ``AUTO`` turns on visible measurement annotations.
        """
        return self._annotate

    @property
    def ch(self) -> Dict[int, MeasurementChannel]:
        """Return the ``MEASUrement:CH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:CH<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.reflevels``: The ``MEASUrement:CH<x>:REFLevels`` command tree.
        """
        return self._ch

    @property
    def deleteall(self) -> MeasurementDeleteall:
        """Return the ``MEASUrement:DELETEALL`` command.

        Description:
            - This command deletes all the active instances of measurements defined in the scope
              application.

        Usage:
            - Using the ``.write()`` method will send the ``MEASUrement:DELETEALL`` command.

        SCPI Syntax:
            ```
            - MEASUrement:DELETEALL
            ```
        """
        return self._deleteall

    @property
    def delete(self) -> MeasurementDelete:
        """Return the ``MEASUrement:DELete`` command.

        Description:
            - The command deletes the specified measurement.

        Usage:
            - Using the ``.write(value)`` method will send the ``MEASUrement:DELete value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:DELete <QString>
            ```

        Info:
            - ``<QString>`` is the measurement to delete. Argument is of the form 'MEAS<NR1>' where
              <NR1> is ≥1.
        """
        return self._delete

    @property
    def edge(self) -> Dict[int, MeasurementEdgeItem]:
        """Return the ``MEASUrement:EDGE<x>`` command.

        Description:
            - This command sets or queries the type of the edge for the measurement.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:EDGE<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:EDGE<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:EDGE<x> value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:EDGE<x> {RISE|FALL|BOTH}
            - MEASUrement:EDGE<x>?
            ```

        Info:
            - ``FALL`` specifies the falling edge of the waveform.
            - ``RISE`` specifies the rising edge of the waveform.
            - ``BOTH`` specifies both a rising and falling edge of the waveform.
        """
        return self._edge

    @property
    def gating(self) -> MeasurementGating:
        """Return the ``MEASUrement:GATing`` command.

        Description:
            - This command sets or queries the global gating type for the measurement.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:GATing?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:GATing?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:GATing value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:GATing {NONE|SCREEN|CURSor|LOGic|SEARch|TIMe}
            - MEASUrement:GATing?
            ```

        Info:
            - ``NONE`` turns off measurement gating.
            - ``SCREen`` turns on gating, using the left and right edges of the screen.
            - ``CURSor`` limits measurements to the portion of the waveform between the vertical bar
              cursors, even if they are off screen.
            - ``LOGic`` specifies that measurements are taken only on the portion of the waveform
              where the logic source is in the active state.
            - ``SEARCH`` specifies that measurements are taken based on search criteria.
            - ``TIMe`` limits measurements to the portion of the waveform between the Start and End
              gate times.

        Sub-properties:
            - ``.active``: The ``MEASUrement:GATing:ACTive`` command.
            - ``.endtime``: The ``MEASUrement:GATing:ENDtime`` command.
            - ``.hysteresis``: The ``MEASUrement:GATing:HYSTeresis`` command.
            - ``.logicsource``: The ``MEASUrement:GATing:LOGICSource`` command.
            - ``.midref``: The ``MEASUrement:GATing:MIDRef`` command.
            - ``.searchsource``: The ``MEASUrement:GATing:SEARCHSource`` command.
            - ``.starttime``: The ``MEASUrement:GATing:STARTtime`` command.
        """
        return self._gating

    @property
    def interp(self) -> MeasurementInterp:
        """Return the ``MEASUrement:INTERp`` command.

        Description:
            - This command sets or queries the interpolation mode used to locate edge crossings.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:INTERp?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:INTERp?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:INTERp value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:INTERp {AUTO|SINX|LINear}
            - MEASUrement:INTERp?
            ```

        Info:
            - ``AUTO`` automatically selects the interpolation mode.
            - ``SINX`` specifies sin(x)/x interpolation, where acquired points are fit to a curve.
            - ``LINear`` specifies linear interpolation, where acquired points are connected with
              straight lines.
        """
        return self._interp

    @property
    def list(self) -> MeasurementList:
        """Return the ``MEASUrement:LIST`` command.

        Description:
            - This query returns a comma separated list of all currently defined measurements.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:LIST?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:LIST?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:LIST?
            ```
        """
        return self._list

    @property
    def math(self) -> Dict[int, MeasurementMathItem]:
        """Return the ``MEASUrement:MATH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MATH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MATH<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``MATH<x>`` specifies the math number.

        Sub-properties:
            - ``.reflevels``: The ``MEASUrement:MATH<x>:REFLevels`` command tree.
        """
        return self._math

    @property
    def meas(self) -> Dict[int, MeasurementMeasItem]:
        """Return the ``MEASUrement:MEAS<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``MEAS<x>`` specifies the measurement number.

        Sub-properties:
            - ``.burstedgtype``: The ``MEASUrement:MEAS<x>:BURSTEDGTYPe`` command.
            - ``.ccresults``: The ``MEASUrement:MEAS<x>:CCRESUlts`` command tree.
            - ``.delay``: The ``MEASUrement:MEAS<x>:DELay`` command tree.
            - ``.displaystat``: The ``MEASUrement:MEAS<x>:DISPlaystat`` command tree.
            - ``.edge``: The ``MEASUrement:MEAS<x>:EDGE<x>`` command.
            - ``.edgeincre``: The ``MEASUrement:MEAS<x>:EDGEIncre`` command.
            - ``.edges``: The ``MEASUrement:MEAS<x>:EDGES`` command tree.
            - ``.failcount``: The ``MEASUrement:MEAS<x>:FAILCount`` command.
            - ``.fromedgesearchdirect``: The ``MEASUrement:MEAS<x>:FROMEDGESEARCHDIRect`` command.
            - ``.fromedge``: The ``MEASUrement:MEAS<x>:FROMedge`` command.
            - ``.gating``: The ``MEASUrement:MEAS<x>:GATing`` command.
            - ``.globalref``: The ``MEASUrement:MEAS<x>:GLOBalref`` command.
            - ``.highrefvoltage``: The ``MEASUrement:MEAS<x>:HIGHREFVoltage`` command.
            - ``.idletime``: The ``MEASUrement:MEAS<x>:IDLETime`` command.
            - ``.label``: The ``MEASUrement:MEAS<x>:LABel`` command.
            - ``.lowrefvoltage``: The ``MEASUrement:MEAS<x>:LOWREFVoltage`` command.
            - ``.passfailenabled``: The ``MEASUrement:MEAS<x>:PASSFAILENabled`` command.
            - ``.passfailhighlimit``: The ``MEASUrement:MEAS<x>:PASSFAILHIGHlimit`` command.
            - ``.passfaillimit``: The ``MEASUrement:MEAS<x>:PASSFAILLIMit`` command.
            - ``.passfaillowlimit``: The ``MEASUrement:MEAS<x>:PASSFAILLOWlimit`` command.
            - ``.passfailmargin``: The ``MEASUrement:MEAS<x>:PASSFAILMARgin`` command.
            - ``.passfailwhen``: The ``MEASUrement:MEAS<x>:PASSFAILWHEN`` command.
            - ``.perfreq``: The ``MEASUrement:MEAS<x>:PERFREQ`` command tree.
            - ``.polarity``: The ``MEASUrement:MEAS<x>:POLarity`` command.
            - ``.reflevels``: The ``MEASUrement:MEAS<x>:REFLevels`` command tree.
            - ``.reflevels1``: The ``MEASUrement:MEAS<x>:REFLevels1`` command tree.
            - ``.refmode``: The ``MEASUrement:MEAS<x>:REFMode`` command.
            - ``.refvoltage``: The ``MEASUrement:MEAS<x>:REFVoltage`` command.
            - ``.results``: The ``MEASUrement:MEAS<x>:RESUlts`` command tree.
            - ``.signaltype``: The ``MEASUrement:MEAS<x>:SIGNALType`` command.
            - ``.source1``: The ``MEASUrement:MEAS<x>:SOUrce1`` command.
            - ``.status``: The ``MEASUrement:MEAS<x>:STATUS`` command.
            - ``.toedgesearchdirect``: The ``MEASUrement:MEAS<x>:TOEDGESEARCHDIRect`` command.
            - ``.toedge``: The ``MEASUrement:MEAS<x>:TOEdge`` command.
            - ``.transition``: The ``MEASUrement:MEAS<x>:TRANSition`` command.
            - ``.type``: The ``MEASUrement:MEAS<x>:TYPe`` command.
            - ``.xunit``: The ``MEASUrement:MEAS<x>:XUNIT`` command.
            - ``.yunit``: The ``MEASUrement:MEAS<x>:YUNIT`` command.
        """
        return self._meas

    @property
    def ref(self) -> Dict[int, MeasurementRefItem]:
        """Return the ``MEASUrement:REF<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:REF<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.reflevels``: The ``MEASUrement:REF<x>:REFLevels`` command tree.
        """
        return self._ref

    @property
    def reflevels(self) -> MeasurementReflevels:
        """Return the ``MEASUrement:REFLevels`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevels?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevels?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.absolute``: The ``MEASUrement:REFLevels:ABSolute`` command tree.
            - ``.basetop``: The ``MEASUrement:REFLevels:BASETop`` command.
            - ``.method``: The ``MEASUrement:REFLevels:METHod`` command.
            - ``.mode``: The ``MEASUrement:REFLevels:MODE`` command.
            - ``.percent``: The ``MEASUrement:REFLevels:PERCent`` command tree.
            - ``.type``: The ``MEASUrement:REFLevels:TYPE`` command.
        """
        return self._reflevels

    @property
    def statistics(self) -> MeasurementStatistics:
        """Return the ``MEASUrement:STATIstics`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:STATIstics?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:STATIstics?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.cyclemode``: The ``MEASUrement:STATIstics:CYCLEMode`` command.
        """
        return self._statistics
